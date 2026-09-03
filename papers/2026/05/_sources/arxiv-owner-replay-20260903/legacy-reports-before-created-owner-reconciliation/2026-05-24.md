# Daily Research — 2026-05-24

**Research Date:** 2026-05-24

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-23 09:00:00 ～ 2026-05-24 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；technical claims bind official arXiv exact-v1 HTML/PDF。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。24/24 项已写入 canonical owner 正文，并通过未参与本日 pre-write 与写作的 reviewer 的 post-write semantic audit。

## Executive Summary

独立重放 289/289 个窗口身份：author denominator 23，经 2 个 false positive 与 19 个 false negative reconciliation 后冻结为 40；pre-denominator closures=249，exact-v1=40/40，blocked=0，ordinary pending=0。current Books owner+adjacent challenge 将 author queue 20 重判为最终 Integrate queue 24，另有 1 个 Structural Candidate；24/24 项已进入 canonical owner 的机制演进正文，并通过独立 post-write semantic audit。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-24 |
| Window End | 2026-05-24 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260524-V2-INDEPENDENT |
| Denominator Frozen At | 2026-09-01T11:30:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-23T09:00:00+08:00 | 2026-05-24T09:00:00+08:00 | 2026-09-01T11:30:00+08:00 | DataCite v2 00..99 + independent 289/289 title+abstract replay + official exact-v1 HTML/PDF | checked | 289 | SF-2026-ARXIV-2606-00089;SF-2026-ARXIV-2606-02606;SF-2026-ARXIV-2605-24326;SF-2026-ARXIV-2605-24391;SF-2026-ARXIV-2605-24420;SF-2026-ARXIV-2605-24421;SF-2026-ARXIV-2605-24425;SF-2026-ARXIV-2605-24426;SF-2026-ARXIV-2605-24461;SF-2026-ARXIV-2605-24468;SF-2026-ARXIV-2605-24517;SF-2026-ARXIV-2605-24547;SF-2026-ARXIV-2605-24558;SF-2026-ARXIV-2605-24579;SF-2026-ARXIV-2605-24583;SF-2026-ARXIV-2605-24598;SF-2026-ARXIV-2605-24614;SF-2026-ARXIV-2605-24619;SF-2026-ARXIV-2605-24657;SF-2026-ARXIV-2605-24659;SF-2026-ARXIV-2605-24660;SF-2026-ARXIV-2605-24661;SF-2026-ARXIV-2605-24662;SF-2026-ARXIV-2605-24667;SF-2026-ARXIV-2605-24683;SF-2026-ARXIV-2605-24697;SF-2026-ARXIV-2605-24709;SF-2026-ARXIV-2605-24727;SF-2026-ARXIV-2605-24728;SF-2026-ARXIV-2605-24733;SF-2026-ARXIV-2605-24737;SF-2026-ARXIV-2605-24743;SF-2026-ARXIV-2605-24749;SF-2026-ARXIV-2605-24756;SF-2026-ARXIV-2605-24770;SF-2026-ARXIV-2605-24775;SF-2026-ARXIV-2605-24785;SF-2026-ARXIV-2605-24786;SF-2026-ARXIV-2605-24793;SF-2026-ARXIV-2605-28872 | pages=300;final_cursor=end;raw=91841;registered=289;screened=289;retained=40;closure=249 | 2026-05-24T00:59:59Z | screening-ledger-final.json#sha256=5b5a6cb4a9aaa8f189e10abe9cfdb5b4d8ff6d8cbe9ba2964b2afff1bf2c3f80 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260524:start -->289/289 identity 已由非作者独立逐项重放；19 个 false negative 恢复，2 个领域/通用 RAG false positive 降回 family-specific closure。first-public、v1、revision、owner day 与重复 family 已对账；无 ordinary pending 或 exact-version blocker。<!-- coverage:SRC-ARXIV:20260524:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-00089 | arXiv:2606.00089v1 | paper-v1:2606.00089 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00089 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-00089 | no |
| SF-2026-ARXIV-2606-02606 | arXiv:2606.02606v1 | paper-v1:2606.02606 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-02606 | self | — | new_in_window | PLATFORM-PRODUCTION | Integrate | books-review:SF-2026-ARXIV-2606-02606 | no |
| SF-2026-ARXIV-2605-24326 | arXiv:2605.24326v1 | paper-v1:2605.24326 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24326 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24326 | no |
| SF-2026-ARXIV-2605-24391 | arXiv:2605.24391v1 | paper-v1:2605.24391 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24391 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-24391 | no |
| SF-2026-ARXIV-2605-24420 | arXiv:2605.24420v1 | paper-v1:2605.24420 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24420 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-24420 | no |
| SF-2026-ARXIV-2605-24421 | arXiv:2605.24421v1 | paper-v1:2605.24421 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24421 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-24421 | no |
| SF-2026-ARXIV-2605-24425 | arXiv:2605.24425v1 | paper-v1:2605.24425 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24425 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Integrate | books-review:SF-2026-ARXIV-2605-24425 | no |
| SF-2026-ARXIV-2605-24426 | arXiv:2605.24426v1 | paper-v1:2605.24426 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24426 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-24426 | no |
| SF-2026-ARXIV-2605-24461 | arXiv:2605.24461v1 | paper-v1:2605.24461 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24461 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Integrate | books-review:SF-2026-ARXIV-2605-24461 | no |
| SF-2026-ARXIV-2605-24468 | arXiv:2605.24468v1 | paper-v1:2605.24468 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24468 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24468 | no |
| SF-2026-ARXIV-2605-24517 | arXiv:2605.24517v1 | paper-v1:2605.24517 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24517 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24517 | no |
| SF-2026-ARXIV-2605-24547 | arXiv:2605.24547v1 | paper-v1:2605.24547 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24547 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-24547 | no |
| SF-2026-ARXIV-2605-24558 | arXiv:2605.24558v1 | paper-v1:2605.24558 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24558 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24558 | no |
| SF-2026-ARXIV-2605-24579 | arXiv:2605.24579v1 | paper-v1:2605.24579 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24579 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-24579 | no |
| SF-2026-ARXIV-2605-24583 | arXiv:2605.24583v1 | paper-v1:2605.24583 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24583 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24583 | no |
| SF-2026-ARXIV-2605-24598 | arXiv:2605.24598v1 | paper-v1:2605.24598 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24598 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-24598 | no |
| SF-2026-ARXIV-2605-24614 | arXiv:2605.24614v1 | paper-v1:2605.24614 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24614 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24614 | no |
| SF-2026-ARXIV-2605-24619 | arXiv:2605.24619v1 | paper-v1:2605.24619 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24619 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24619 | no |
| SF-2026-ARXIV-2605-24657 | arXiv:2605.24657v1 | paper-v1:2605.24657 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24657 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24657 | no |
| SF-2026-ARXIV-2605-24659 | arXiv:2605.24659v1 | paper-v1:2605.24659 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24659 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24659 | no |
| SF-2026-ARXIV-2605-24660 | arXiv:2605.24660v1 | paper-v1:2605.24660 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24660 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-24660 | no |
| SF-2026-ARXIV-2605-24661 | arXiv:2605.24661v1 | paper-v1:2605.24661 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24661 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24661 | no |
| SF-2026-ARXIV-2605-24662 | arXiv:2605.24662v1 | paper-v1:2605.24662 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24662 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24662 | no |
| SF-2026-ARXIV-2605-24667 | arXiv:2605.24667v1 | paper-v1:2605.24667 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24667 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-24667 | no |
| SF-2026-ARXIV-2605-24683 | arXiv:2605.24683v1 | paper-v1:2605.24683 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24683 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-24683 | no |
| SF-2026-ARXIV-2605-24697 | arXiv:2605.24697v1 | paper-v1:2605.24697 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24697 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Integrate | books-review:SF-2026-ARXIV-2605-24697 | no |
| SF-2026-ARXIV-2605-24709 | arXiv:2605.24709v1 | paper-v1:2605.24709 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24709 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-24709 | no |
| SF-2026-ARXIV-2605-24727 | arXiv:2605.24727v1 | paper-v1:2605.24727 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24727 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24727 | no |
| SF-2026-ARXIV-2605-24728 | arXiv:2605.24728v1 | paper-v1:2605.24728 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24728 | self | — | new_in_window | — | Structural Candidate | books-review:SF-2026-ARXIV-2605-24728 | no |
| SF-2026-ARXIV-2605-24733 | arXiv:2605.24733v1 | paper-v1:2605.24733 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24733 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24733 | no |
| SF-2026-ARXIV-2605-24737 | arXiv:2605.24737v1 | paper-v1:2605.24737 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24737 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24737 | no |
| SF-2026-ARXIV-2605-24743 | arXiv:2605.24743v1 | paper-v1:2605.24743 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24743 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-24743 | no |
| SF-2026-ARXIV-2605-24749 | arXiv:2605.24749v1 | paper-v1:2605.24749 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24749 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-24749 | no |
| SF-2026-ARXIV-2605-24756 | arXiv:2605.24756v1 | paper-v1:2605.24756 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24756 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24756 | no |
| SF-2026-ARXIV-2605-24770 | arXiv:2605.24770v1 | paper-v1:2605.24770 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24770 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-24770 | no |
| SF-2026-ARXIV-2605-24775 | arXiv:2605.24775v1 | paper-v1:2605.24775 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24775 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24775 | no |
| SF-2026-ARXIV-2605-24785 | arXiv:2605.24785v1 | paper-v1:2605.24785 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24785 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24785 | no |
| SF-2026-ARXIV-2605-24786 | arXiv:2605.24786v1 | paper-v1:2605.24786 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24786 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24786 | no |
| SF-2026-ARXIV-2605-24793 | arXiv:2605.24793v1 | paper-v1:2605.24793 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24793 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-24793 | no |
| SF-2026-ARXIV-2605-28872 | arXiv:2605.28872v1 | paper-v1:2605.28872 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28872 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Integrate | books-review:SF-2026-ARXIV-2605-28872 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-00089 | RP-89b2bae4c571f9e0 | deep | arXiv:2606.00089v1 | SRC-ARXIV@arXiv:2606.00089v1 | https://arxiv.org/html/2606.00089v1 — §§3–5 prediction-control interface, physical conditions and rejection semantics | https://arxiv.org/html/2606.00089v1 — §6 Experimental Protocol | https://arxiv.org/html/2606.00089v1 — §7.1 Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2606-00089 | complete |
| SF-2026-ARXIV-2606-02606 | RP-81ebb0bb8aaf5481 | deep | arXiv:2606.02606v1 | SRC-ARXIV@arXiv:2606.02606v1 | https://arxiv.org/html/2606.02606v1 — §III Method; III-A–III-C adaptive initialization and scheduled regularization | https://arxiv.org/html/2606.02606v1 — §IV Evaluation; IV-A–IV-E | https://arxiv.org/html/2606.02606v1 — §VI Discussion and Limitation; VI-C–VI-D | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2606-02606 | complete |
| SF-2026-ARXIV-2605-24326 | RP-4f648fc711474d89 | deep | arXiv:2605.24326v1 | SRC-ARXIV@arXiv:2605.24326v1 | https://arxiv.org/html/2605.24326v1 — §3–§6 placement, scheduling, network and ScaleAcross Explorer | https://arxiv.org/html/2605.24326v1 — §6.3 Evaluation Results; Appendix A testbed/simulation settings | https://arxiv.org/html/2605.24326v1 — §7 Lessons Learned; §8 Conclusion; cross-building testbed/simulator scope | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24326 | complete |
| SF-2026-ARXIV-2605-24391 | RP-55e9632e2d963538 | deep | arXiv:2605.24391v1 | SRC-ARXIV@arXiv:2605.24391v1 | https://arxiv.org/html/2605.24391v1 — §IV MX-SAFE format; §V accelerator | https://arxiv.org/html/2605.24391v1 — §VI Experimental Results | https://arxiv.org/html/2605.24391v1 — §VII Conclusion; tested MXSF hardware/model boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24391 | complete |
| SF-2026-ARXIV-2605-24420 | RP-b36175ce3407cad2 | deep | arXiv:2605.24420v1 | SRC-ARXIV@arXiv:2605.24420v1 | https://arxiv.org/html/2605.24420v1 — §3 Methodology; §5 theory; §6 mitigation | https://arxiv.org/html/2605.24420v1 — §4 Experiments; §4.3 membership inference | https://arxiv.org/html/2605.24420v1 — Appendix A.3 theoretical limitations; tested normalization/model/data boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24420 | complete |
| SF-2026-ARXIV-2605-24421 | RP-102e187f2447e1a2 | deep | arXiv:2605.24421v1 | SRC-ARXIV@arXiv:2605.24421v1 | https://arxiv.org/html/2605.24421v1 — §2 Threat Model; §3 taxonomy; §4 pipeline/defenses | https://arxiv.org/html/2605.24421v1 — §5 Experiments | https://arxiv.org/html/2605.24421v1 — §6.4 Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24421 | complete |
| SF-2026-ARXIV-2605-24425 | RP-f3674382966e9490 | deep | arXiv:2605.24425v1 | SRC-ARXIV@arXiv:2605.24425v1 | https://arxiv.org/html/2605.24425v1 — §§3–5 optimizer view, optimizer-inspired block and momentum stream | https://arxiv.org/html/2605.24425v1 — §4.2; §§5–6; Appendix D Experimental Details | https://arxiv.org/html/2605.24425v1 — §7 Conclusion; architecture/scale/recipe boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24425 | complete |
| SF-2026-ARXIV-2605-24426 | RP-98d07cd64cd7d6ad | deep | arXiv:2605.24426v1 | SRC-ARXIV@arXiv:2605.24426v1 | https://arxiv.org/html/2605.24426v1 — §3 verifier-grounded diagnosis, interface evolution and advantage reweighting | https://arxiv.org/html/2605.24426v1 — §4 Experiments; Appendix C controlled protocol | https://arxiv.org/html/2605.24426v1 — §5 Conclusion and Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24426 | complete |
| SF-2026-ARXIV-2605-24461 | RP-972614f3963dd9ae | deep | arXiv:2605.24461v1 | SRC-ARXIV@arXiv:2605.24461v1 | https://arxiv.org/html/2605.24461v1 — §3 power hierarchy; §§4–6 provisioning, validation and active operation | https://arxiv.org/html/2605.24461v1 — §4.2 empirical data; §§5–7 deployment/runtime measurements | https://arxiv.org/html/2605.24461v1 — §8 Research Wishlist; §10 Conclusion; single 150MW/83K-GB200 site boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24461 | complete |
| SF-2026-ARXIV-2605-24468 | RP-9e8b74037551a48d | deep | arXiv:2605.24468v1 | SRC-ARXIV@arXiv:2605.24468v1 | https://arxiv.org/html/2605.24468v1 — §2.2–§2.3 State-Adaptive Memory and optimization | https://arxiv.org/html/2605.24468v1 — §3 Experiments; §4 Discussions | https://arxiv.org/html/2605.24468v1 — Appendix A Limitations and Broader Impact | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24468 | complete |
| SF-2026-ARXIV-2605-24517 | RP-8cf791c6ad1be8e1 | deep | arXiv:2605.24517v1 | SRC-ARXIV@arXiv:2605.24517v1 | https://arxiv.org/pdf/2605.24517v1 — §3 Method; ECHO hybrid policy/observation objective | https://arxiv.org/pdf/2605.24517v1 — §4 Experimental Setup; §5 Results | https://arxiv.org/pdf/2605.24517v1 — §7 Conclusion; terminal-environment and training-only auxiliary-loss boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24517 | complete |
| SF-2026-ARXIV-2605-24547 | RP-e0e458f246e1cf50 | deep | arXiv:2605.24547v1 | SRC-ARXIV@arXiv:2605.24547v1 | https://arxiv.org/html/2605.24547v1 — §2 problem formulation; §3 bilevel natural-language actor-critic | https://arxiv.org/html/2605.24547v1 — §4 Experiments; Appendix A.5 efficiency | https://arxiv.org/html/2605.24547v1 — §5 Conclusion; tested task/model and higher-order-gradient boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24547 | complete |
| SF-2026-ARXIV-2605-24558 | RP-86300338cd43f93c | deep | arXiv:2605.24558v1 | SRC-ARXIV@arXiv:2605.24558v1 | https://arxiv.org/html/2605.24558v1 — §§2–3 measurement pipeline as observation/inference component | https://arxiv.org/html/2605.24558v1 — §4 empirical audit; §5 alternative views | https://arxiv.org/html/2605.24558v1 — §6 Call to Action; position/audit does not prove a universal pipeline | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24558 | complete |
| SF-2026-ARXIV-2605-24579 | RP-03689a15f3910dd8 | deep | arXiv:2605.24579v1 | SRC-ARXIV@arXiv:2605.24579v1 | https://arxiv.org/html/2605.24579v1 — §3 four-condition diagnostic; §4 expected predictive compression | https://arxiv.org/html/2605.24579v1 — §5 Experimental Setup; §6 Results; §7 Analysis | https://arxiv.org/html/2605.24579v1 — §7 Analysis and §8 Conclusion; tested readers, memories and two benchmarks | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24579 | complete |
| SF-2026-ARXIV-2605-24583 | RP-94172e9bb59bd455 | deep | arXiv:2605.24583v1 | SRC-ARXIV@arXiv:2605.24583v1 | https://arxiv.org/html/2605.24583v1 — §§2–4 separability metric and three confound-control tests | https://arxiv.org/html/2605.24583v1 — §§5–6 calibration and current-alignment audit | https://arxiv.org/html/2605.24583v1 — §7 Scope; §8 open problem and failed spectral-gap claim | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24583 | complete |
| SF-2026-ARXIV-2605-24598 | RP-25d0449947a6ad7a | deep | arXiv:2605.24598v1 | SRC-ARXIV@arXiv:2605.24598v1 | https://arxiv.org/html/2605.24598v1 — §5 Hera step-level device-cloud coordinator | https://arxiv.org/html/2605.24598v1 — §6 Experiment; §6.2–§6.4 | https://arxiv.org/html/2605.24598v1 — Appendix E Limitations and Future Work | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24598 | complete |
| SF-2026-ARXIV-2605-24614 | RP-3a00f3e1da3ee4ac | deep | arXiv:2605.24614v1 | SRC-ARXIV@arXiv:2605.24614v1 | https://arxiv.org/html/2605.24614v1 — §3 Unlearning Depth Score and activation patching | https://arxiv.org/html/2605.24614v1 — §4 Meta-Evaluation; §5 case studies | https://arxiv.org/html/2605.24614v1 — Limitations after §7 Conclusion | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24614 | complete |
| SF-2026-ARXIV-2605-24619 | RP-6de6abc06fda9317 | deep | arXiv:2605.24619v1 | SRC-ARXIV@arXiv:2605.24619v1 | https://arxiv.org/html/2605.24619v1 — §4 Design; §5 Implementation | https://arxiv.org/html/2605.24619v1 — §6 Evaluation | https://arxiv.org/html/2605.24619v1 — §7.2 Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24619 | complete |
| SF-2026-ARXIV-2605-24657 | RP-6e4c98528d814c8c | deep | arXiv:2605.24657v1 | SRC-ARXIV@arXiv:2605.24657v1 | https://arxiv.org/html/2605.24657v1 — §2 Method; memory taxonomy and consolidation/compaction pipelines | https://arxiv.org/html/2605.24657v1 — §3 Evaluation | https://arxiv.org/html/2605.24657v1 — §4 Discussion — Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24657 | complete |
| SF-2026-ARXIV-2605-24659 | RP-e1f6275b0ab9bf33 | deep | arXiv:2605.24659v1 | SRC-ARXIV@arXiv:2605.24659v1 | https://arxiv.org/html/2605.24659v1 — §3 Threat Model; §4 feedback-guided payload optimization | https://arxiv.org/html/2605.24659v1 — §5 Experimental Setup; §6 Evaluation | https://arxiv.org/html/2605.24659v1 — Limitations after §7 Conclusion; tested agents/channels only | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24659 | complete |
| SF-2026-ARXIV-2605-24660 | RP-e10fd5ac2e6315c9 | deep | arXiv:2605.24660v1 | SRC-ARXIV@arXiv:2605.24660v1 | https://arxiv.org/html/2605.24660v1 — §3 Bits-over-Random and MDP exposure policy | https://arxiv.org/html/2605.24660v1 — §4 Empirical Evaluation | https://arxiv.org/html/2605.24660v1 — §5.3 Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24660 | complete |
| SF-2026-ARXIV-2605-24661 | RP-39c314eb0adaeffa | deep | arXiv:2605.24661v1 | SRC-ARXIV@arXiv:2605.24661v1 | https://arxiv.org/html/2605.24661v1 — §4 multi-dimensional behavioral framework and aggregation | https://arxiv.org/html/2605.24661v1 — §5 Results | https://arxiv.org/html/2605.24661v1 — §6.2 Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24661 | complete |
| SF-2026-ARXIV-2605-24662 | RP-ae966f511033343f | deep | arXiv:2605.24662v1 | SRC-ARXIV@arXiv:2605.24662v1 | https://arxiv.org/pdf/2605.24662v1 — §II–§IV OpenTwin closed-loop data assimilation, calibration and policy-validation workflow | https://arxiv.org/pdf/2605.24662v1 — §A Experimental Setup; §B Experimental Results | https://arxiv.org/pdf/2605.24662v1 — §V Limitations; real-network drift and Open-RAN testbed boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24662 | complete |
| SF-2026-ARXIV-2605-24667 | RP-581d1df78a56b1a8 | deep | arXiv:2605.24667v1 | SRC-ARXIV@arXiv:2605.24667v1 | https://arxiv.org/html/2605.24667v1 — §§3–4 mean/median CE interventions and top-K self-distillation | https://arxiv.org/html/2605.24667v1 — §3.2; §§4.2–4.4; Appendix C protocol | https://arxiv.org/html/2605.24667v1 — §5 Discussion — Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24667 | complete |
| SF-2026-ARXIV-2605-24683 | RP-59a2b83cfa3da81b | deep | arXiv:2605.24683v1 | SRC-ARXIV@arXiv:2605.24683v1 | https://arxiv.org/html/2605.24683v1 — §III deterministic L2 topology, identity loop and HIL protocol | https://arxiv.org/html/2605.24683v1 — §IV Implementation and Results | https://arxiv.org/html/2605.24683v1 — §V Limitations and Constraints | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24683 | complete |
| SF-2026-ARXIV-2605-24697 | RP-9f4e2f1043856416 | deep | arXiv:2605.24697v1 | SRC-ARXIV@arXiv:2605.24697v1 | https://arxiv.org/html/2605.24697v1 — §3 future-stability labels, learned commitment and TraceLock deployment | https://arxiv.org/html/2605.24697v1 — §4 Experiments; §§4.2–4.4 | https://arxiv.org/html/2605.24697v1 — §5 Conclusion; frozen generator/tested diffusion backbones boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24697 | complete |
| SF-2026-ARXIV-2605-24709 | RP-e754b0014f15c7c7 | deep | arXiv:2605.24709v1 | SRC-ARXIV@arXiv:2605.24709v1 | https://arxiv.org/pdf/2605.24709v1 — §3 Methodology; streaming partially-observed recurrent policy with exact RTRL | https://arxiv.org/pdf/2605.24709v1 — §4 Experiments | https://arxiv.org/pdf/2605.24709v1 — §6 Discussion and Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24709 | complete |
| SF-2026-ARXIV-2605-24727 | RP-9695b6567a93af77 | deep | arXiv:2605.24727v1 | SRC-ARXIV@arXiv:2605.24727v1 | https://arxiv.org/html/2605.24727v1 — §3 four explanation conditions; §4 quadrilemma theorem/implications | https://arxiv.org/html/2605.24727v1 — formal construction and implications in §4 | https://arxiv.org/html/2605.24727v1 — §5 Conclusion, limitations and future work | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24727 | complete |
| SF-2026-ARXIV-2605-24728 | RP-9c320a39b9208093 | deep | arXiv:2605.24728v1 | SRC-ARXIV@arXiv:2605.24728v1 | https://arxiv.org/html/2605.24728v1 — §4 operability state/graph, spatial transactions and effect diffs; §5 agency gates | https://arxiv.org/html/2605.24728v1 — §6 repair stress test; §7 qualitative result | https://arxiv.org/html/2605.24728v1 — §1.2 Scope of Claims; prototype/trajectory does not establish general runtime validity | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24728 | complete |
| SF-2026-ARXIV-2605-24733 | RP-0193a60be397b1bf | deep | arXiv:2605.24733v1 | SRC-ARXIV@arXiv:2605.24733v1 | https://arxiv.org/html/2605.24733v1 — §3 formulation; §4 hybrid checker; §5 typed process reward | https://arxiv.org/html/2605.24733v1 — §6 checker evaluation; §7 GRPO training | https://arxiv.org/html/2605.24733v1 — Limitations after §8 Conclusion | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24733 | complete |
| SF-2026-ARXIV-2605-24737 | RP-f76afdb14139d1ac | deep | arXiv:2605.24737v1 | SRC-ARXIV@arXiv:2605.24737v1 | https://arxiv.org/pdf/2605.24737v1 — §3 governance from metrics; §4 govllm architecture; §5 contributions | https://arxiv.org/pdf/2605.24737v1 — §6 Preliminary experiments | https://arxiv.org/pdf/2605.24737v1 — §6.3 and §7.4 Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24737 | complete |
| SF-2026-ARXIV-2605-24743 | RP-14b1da66185ab9e6 | deep | arXiv:2605.24743v1 | SRC-ARXIV@arXiv:2605.24743v1 | https://arxiv.org/html/2605.24743v1 — §3 bilevel synthetic-trajectory weighting; §4 theory | https://arxiv.org/html/2605.24743v1 — §§5–6 experiments and learned-weight analysis | https://arxiv.org/html/2605.24743v1 — §7 Conclusion; three tasks and synthetic-generator boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24743 | complete |
| SF-2026-ARXIV-2605-24749 | RP-6a6251126779544a | deep | arXiv:2605.24749v1 | SRC-ARXIV@arXiv:2605.24749v1 | https://arxiv.org/html/2605.24749v1 — §§3–5 reward-weighted feature recovery and tilted-policy value gap | https://arxiv.org/html/2605.24749v1 — theory and deployment-temperature analysis in §§4–5 | https://arxiv.org/html/2605.24749v1 — §6 Conclusion and Discussion; single-index/theoretical-assumption boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24749 | complete |
| SF-2026-ARXIV-2605-24756 | RP-4a2017558a4cac29 | deep | arXiv:2605.24756v1 | SRC-ARXIV@arXiv:2605.24756v1 | https://arxiv.org/html/2605.24756v1 — §4 proper trajectory scores under complete and censored observation | https://arxiv.org/html/2605.24756v1 — §5 metrics; §6 Experiments | https://arxiv.org/html/2605.24756v1 — §7 Conclusion and Limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24756 | complete |
| SF-2026-ARXIV-2605-24770 | RP-b893b2cab66aa0ad | deep | arXiv:2605.24770v1 | SRC-ARXIV@arXiv:2605.24770v1 | https://arxiv.org/html/2605.24770v1 — §§2–5 Muon geometry and recipe interaction | https://arxiv.org/html/2605.24770v1 — §§3–6; Appendices C–E | https://arxiv.org/html/2605.24770v1 — §7 Conclusions and limitations | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24770 | complete |
| SF-2026-ARXIV-2605-24775 | RP-3886915343290683 | deep | arXiv:2605.24775v1 | SRC-ARXIV@arXiv:2605.24775v1 | https://arxiv.org/html/2605.24775v1 — §III identity; §§IV–VIII protocol, scoring, orchestration and persistence | https://arxiv.org/html/2605.24775v1 — reported operational examples and convergence traces in §§VI–VIII | https://arxiv.org/html/2605.24775v1 — §I/§II claim scope; pattern/prototype rather than general production proof | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24775 | complete |
| SF-2026-ARXIV-2605-24785 | RP-c03d089563b69109 | deep | arXiv:2605.24785v1 | SRC-ARXIV@arXiv:2605.24785v1 | https://arxiv.org/pdf/2605.24785v1 — §3 cost decomposition and online skill-distillation lifecycle | https://arxiv.org/pdf/2605.24785v1 — §5 Experimental Setup and reported results | https://arxiv.org/pdf/2605.24785v1 — §7 Limitations and Conclusion | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24785 | complete |
| SF-2026-ARXIV-2605-24786 | RP-c5d198be81110b11 | deep | arXiv:2605.24786v1 | SRC-ARXIV@arXiv:2605.24786v1 | https://arxiv.org/html/2605.24786v1 — §3 confidence-aware mixed-precision cache manager | https://arxiv.org/html/2605.24786v1 — §§4–6 setup, results and ablations | https://arxiv.org/html/2605.24786v1 — §7 failure modes; §8 Limitations and conclusion | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24786 | complete |
| SF-2026-ARXIV-2605-24793 | RP-d267c48a39ae48a5 | deep | arXiv:2605.24793v1 | SRC-ARXIV@arXiv:2605.24793v1 | https://arxiv.org/html/2605.24793v1 — §3 utility view, collaborative arbitration and RL training | https://arxiv.org/html/2605.24793v1 — §4 Experiments; §§4.2–4.4 | https://arxiv.org/html/2605.24793v1 — §5 Conclusion and Appendix A tested-model/benchmark boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24793 | complete |
| SF-2026-ARXIV-2605-28872 | RP-0e4d872b0df5dfcd | deep | arXiv:2605.28872v1 | SRC-ARXIV@arXiv:2605.28872v1 | https://arxiv.org/html/2605.28872v1 — §IV measurement; §§V–VI reclaim-aware membership/lease protocol | https://arxiv.org/html/2605.28872v1 — §VII Evaluation and campus deployment measurements | https://arxiv.org/html/2605.28872v1 — §VIII Limitations and Conclusion; voluntary campus-network and failure-domain boundary | Not Disclosed — no separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-28872 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-00089:start -->
#### Can Predicted Dynamics Exist in the Physical World?

**问题与机制。** We formalize this prediction-control interface and prove that the all-pairs displacement term is redundant within a max-aggregated composite. owner=`MULTIMODAL-EMBODIED-VLA`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§3–5 prediction-control interface, physical conditions and rejection semantics`；Evaluation=`§6 Experimental Protocol`；Limitations/Counterevidence=`§7.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2606-00089:start -->Can Predicted Dynamics Exist in the Physical World? only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2606-00089:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2606-00089:end -->

<!-- review:SF-2026-ARXIV-2606-02606:start -->
#### ReLoRA: Knowledge-Reusing Adaptation for Fast Rollout of Evolving LLM Services

**问题与机制。** To address this problem, we propose ReLoRA, a knowledge-reusing re-adaptation framework that efficiently restores service-ready LoRA adapters for evolving LLM services while preserving or improving task performance. owner=`PLATFORM-PRODUCTION`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§III Method; III-A–III-C adaptive initialization and scheduled regularization`；Evaluation=`§IV Evaluation; IV-A–IV-E`；Limitations/Counterevidence=`§VI Discussion and Limitation; VI-C–VI-D`。

<!-- claim:SF-2026-ARXIV-2606-02606:start -->ReLoRA: Knowledge-Reusing Adaptation for Fast Rollout of Evolving LLM Services only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2606-02606:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2606-02606:end -->

<!-- review:SF-2026-ARXIV-2605-24326:start -->
#### ScaleAcross Explorer: Exploring Communication Optimization for Scale-Across AI Model Training

**问题与机制。** As infrastructure expands, the system design space becomes increasingly intricate, encompassing new model architectures, hardware heterogeneity, and evolving communication patterns. owner=`TRAIN-DISTRIBUTED-TRAINING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3–§6 placement, scheduling, network and ScaleAcross Explorer`；Evaluation=`§6.3 Evaluation Results; Appendix A testbed/simulation settings`；Limitations/Counterevidence=`§7 Lessons Learned; §8 Conclusion; cross-building testbed/simulator scope`。

<!-- claim:SF-2026-ARXIV-2605-24326:start -->ScaleAcross Explorer: Exploring Communication Optimization for Scale-Across AI Model Training only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24326:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24326:end -->

<!-- review:SF-2026-ARXIV-2605-24391:start -->
#### MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format with On-the-Fly Exponent and Mantissa Bit Allocation

**问题与机制。** In this work, we present a versatile MXFP format, called MX-SAFE (MXSF in short), that adaptively uses two modes, i.e., a wider mantissa mode (FP8 E2M5) and a subnormal FP mode (FP5 E3M2), to support both training and direct-cast inference. owner=`INFER-TENSORRT-LLM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§IV MX-SAFE format; §V accelerator`；Evaluation=`§VI Experimental Results`；Limitations/Counterevidence=`§VII Conclusion; tested MXSF hardware/model boundary`。

<!-- claim:SF-2026-ARXIV-2605-24391:start -->MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format with On-the-Fly Exponent and Mantissa Bit Allocation only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24391:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24391:end -->

<!-- review:SF-2026-ARXIV-2605-24420:start -->
#### Batch Normalization Amplifies Memorization and Privacy Risks

**问题与机制。** We conduct an extensive empirical study using three complementary approaches: (i) unintended memorization of out-of-distribution training samples, (ii) per-sample influence measured via gradient norms, and (iii) susceptibility to membership inference attacks (MIA). owner=`PLATFORM-SECURITY`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Methodology; §5 theory; §6 mitigation`；Evaluation=`§4 Experiments; §4.3 membership inference`；Limitations/Counterevidence=`Appendix A.3 theoretical limitations; tested normalization/model/data boundary`。

<!-- claim:SF-2026-ARXIV-2605-24420:start -->Batch Normalization Amplifies Memorization and Privacy Risks only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24420:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24420:end -->

<!-- review:SF-2026-ARXIV-2605-24421:start -->
#### Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content

**问题与机制。** We study a structural failure mode of this design: many log fields are attacker controlled. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§2 Threat Model; §3 taxonomy; §4 pipeline/defenses`；Evaluation=`§5 Experiments`；Limitations/Counterevidence=`§6.4 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24421:start -->Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24421:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24421:end -->

<!-- review:SF-2026-ARXIV-2605-24425:start -->
#### Momentum Streams for Optimizer-Inspired Transformers

**问题与机制。** A controlled ablation and supporting theory show that momentum, not preconditioning, is the main source of the gain. owner=`MODEL-TRANSFORMER-LAYER`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§3–5 optimizer view, optimizer-inspired block and momentum stream`；Evaluation=`§4.2; §§5–6; Appendix D Experimental Details`；Limitations/Counterevidence=`§7 Conclusion; architecture/scale/recipe boundary`。

<!-- claim:SF-2026-ARXIV-2605-24425:start -->Momentum Streams for Optimizer-Inspired Transformers only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24425:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24425:end -->

<!-- review:SF-2026-ARXIV-2605-24426:start -->
#### SEAL: Synergistic Co-Evolution of Agents and Learning Environments

**问题与机制。** We identify this structural gap as \emph{Agent-Environment Misalignment}: the agent's capability frontier changes during training, while the environment that provides supervision remains static or only weakly coupled to the agent's revealed failures. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 verifier-grounded diagnosis, interface evolution and advantage reweighting`；Evaluation=`§4 Experiments; Appendix C controlled protocol`；Limitations/Counterevidence=`§5 Conclusion and Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24426:start -->SEAL: Synergistic Co-Evolution of Agents and Learning Environments only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24426:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24426:end -->

<!-- review:SF-2026-ARXIV-2605-24461:start -->
#### Provisioning to Runtime Optimization of a 100 MW-Scale AI Cluster

**问题与机制。** We present detailed power measurements for a 150 MW datacenter hosting a cluster of 83K GB200 GPUs. owner=`PLATFORM-GPU-SCHEDULER`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 power hierarchy; §§4–6 provisioning, validation and active operation`；Evaluation=`§4.2 empirical data; §§5–7 deployment/runtime measurements`；Limitations/Counterevidence=`§8 Research Wishlist; §10 Conclusion; single 150MW/83K-GB200 site boundary`。

<!-- claim:SF-2026-ARXIV-2605-24461:start -->Provisioning to Runtime Optimization of a 100 MW-Scale AI Cluster only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24461:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24461:end -->

<!-- review:SF-2026-ARXIV-2605-24468:start -->
#### SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent

**问题与机制。** To this end, we propose State-Adaptive Memory~(SAM), a standalone framework that consolidates ongoing interaction into compact memory cues while preserving raw trajectory pages for intent-driven recall. owner=`AGENT-MEMORY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§2.2–§2.3 State-Adaptive Memory and optimization`；Evaluation=`§3 Experiments; §4 Discussions`；Limitations/Counterevidence=`Appendix A Limitations and Broader Impact`。

<!-- claim:SF-2026-ARXIV-2605-24468:start -->SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24468:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24468:end -->

<!-- review:SF-2026-ARXIV-2605-24517:start -->
#### ECHO: Terminal Agents Learn World Models for Free

**问题与机制。** We introduce ECHO (Environment Cross-entropy Hybrid Objective), a hybrid objective that combines the standard policy-gradient loss on action tokens with an auxiliary loss that trains the policy to predict environment observation tokens resulting from its own actions. owner=`MULTIMODAL-WORLD-MODELS`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Method; ECHO hybrid policy/observation objective`；Evaluation=`§4 Experimental Setup; §5 Results`；Limitations/Counterevidence=`§7 Conclusion; terminal-environment and training-only auxiliary-loss boundary`。

<!-- claim:SF-2026-ARXIV-2605-24517:start -->ECHO: Terminal Agents Learn World Models for Free only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24517:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24517:end -->

<!-- review:SF-2026-ARXIV-2605-24547:start -->
#### RL with Learnable Textual Feedback: A Bilevel Approach

**问题与机制。** We formalize this coupling as a Stackelberg bilevel program and derive Bilevel Natural Language Actor-Critic (Bi-NAC), which jointly trains a critic to generate reward-improving feedback and an actor to exploit it. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§2 problem formulation; §3 bilevel natural-language actor-critic`；Evaluation=`§4 Experiments; Appendix A.5 efficiency`；Limitations/Counterevidence=`§5 Conclusion; tested task/model and higher-order-gradient boundary`。

<!-- claim:SF-2026-ARXIV-2605-24547:start -->RL with Learnable Textual Feedback: A Bilevel Approach only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24547:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24547:end -->

<!-- review:SF-2026-ARXIV-2605-24558:start -->
#### Position: AI for Science Should Treat Measurement-to-Dataset Pipelines as Inference Components

**问题与机制。** \textbf{We argue that these measurement-to-dataset pipelines are inference components: treating their outputs as ``given data'' freezes an observation model and obscures uncertainty over feasible pipeline choices.} We identify three failure modes arising from this ``frozen lens'': \textbf{(C1) hidden hypothesis space}, where the released dataset does not specify the pipeline configuration or its validity conditions; \textbf{(C2) uncertified transportability}, where a pipeline may be documented but its regime of validity is untested, so failures under distribution shift cannot be adjudicated; \textbf{(C3) ungoverned multiplicity}, where many defensible pipelines exist and dispersion is real but not propagated into uncertainty-aware evidence. owner=`TRAIN-DATA`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§2–3 measurement pipeline as observation/inference component`；Evaluation=`§4 empirical audit; §5 alternative views`；Limitations/Counterevidence=`§6 Call to Action; position/audit does not prove a universal pipeline`。

<!-- claim:SF-2026-ARXIV-2605-24558:start -->Position: AI for Science Should Treat Measurement-to-Dataset Pipelines as Inference Components only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24558:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24558:end -->

<!-- review:SF-2026-ARXIV-2605-24579:start -->
#### WhenLoss: Diagnosing Write and Retrieval Bottlenecks in Long-Context Memory Systems

**问题与机制。** We introduce a four-condition diagnostic protocol that evaluates a fixed reader under truncated full context (TFC), oracle evidence (OE), complete stored memory (CSM), and retrieved memory (RM). owner=`AGENT-MEMORY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 four-condition diagnostic; §4 expected predictive compression`；Evaluation=`§5 Experimental Setup; §6 Results; §7 Analysis`；Limitations/Counterevidence=`§7 Analysis and §8 Conclusion; tested readers, memories and two benchmarks`。

<!-- claim:SF-2026-ARXIV-2605-24579:start -->WhenLoss: Diagnosing Write and Retrieval Bottlenecks in Long-Context Memory Systems only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24579:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24579:end -->

<!-- review:SF-2026-ARXIV-2605-24583:start -->
#### Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol

**问题与机制。** We show the obvious way to form this matrix is confounded. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§2–4 separability metric and three confound-control tests`；Evaluation=`§§5–6 calibration and current-alignment audit`；Limitations/Counterevidence=`§7 Scope; §8 open problem and failed spectral-gap claim`。

<!-- claim:SF-2026-ARXIV-2605-24583:start -->Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24583:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24583:end -->

<!-- review:SF-2026-ARXIV-2605-24598:start -->
#### Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents

**问题与机制。** To address this issue, we present Hera, a step-level device--cloud LLM agent coordinator for long-horizon tasks achieving a strong performance--cost Pareto frontier. owner=`AGENT-MULTI-AGENT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§5 Hera step-level device-cloud coordinator`；Evaluation=`§6 Experiment; §6.2–§6.4`；Limitations/Counterevidence=`Appendix E Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-24598:start -->Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24598:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24598:end -->

<!-- review:SF-2026-ARXIV-2605-24614:start -->
#### Measuring the Depth of LLM Unlearning via Activation Patching

**问题与机制。** To address these limitations, we propose the Unlearning Depth Score (UDS), a metric that quantifies the mechanistic depth of unlearning via activation patching. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Unlearning Depth Score and activation patching`；Evaluation=`§4 Meta-Evaluation; §5 case studies`；Limitations/Counterevidence=`Limitations after §7 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-24614:start -->Measuring the Depth of LLM Unlearning via Activation Patching only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24614:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24614:end -->

<!-- review:SF-2026-ARXIV-2605-24619:start -->
#### Synthesizing Inductive Invariants for Distributed Protocols via IC3 and Large Language Models

**问题与机制。** We present IC3Syn, a neuro-symbolic framework that synthesizes inductive invariants by executing an IC3-style process over TLA+ states with the assistance of Large Language Models (LLMs). owner=`AGENT-PLATFORM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§4 Design; §5 Implementation`；Evaluation=`§6 Evaluation`；Limitations/Counterevidence=`§7.2 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24619:start -->Synthesizing Inductive Invariants for Distributed Protocols via IC3 and Large Language Models only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24619:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24619:end -->

<!-- review:SF-2026-ARXIV-2605-24657:start -->
#### Beyond Inference-Only Deployment: Comparing Weight-Based Consolidation Against Cascading Compaction

**问题与机制。** Major LLM platforms deploy models in an inference-only configuration: the model serves requests but never updates per-user weights. owner=`AGENT-CONTEXT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§2 Method; memory taxonomy and consolidation/compaction pipelines`；Evaluation=`§3 Evaluation`；Limitations/Counterevidence=`§4 Discussion — Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24657:start -->Beyond Inference-Only Deployment: Comparing Weight-Based Consolidation Against Cascading Compaction only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24657:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24657:end -->

<!-- review:SF-2026-ARXIV-2605-24659:start -->
#### IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization

**问题与机制。** We introduce \oursys, a feedback-guided iterative framework that closes the loop between injection, diagnosis, and refinement: a rule-based diagnoser produces structured outcome labels with behavioral descriptions, and an LLM-based optimizer refines payloads conditioned on the full optimization history. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Threat Model; §4 feedback-guided payload optimization`；Evaluation=`§5 Experimental Setup; §6 Evaluation`；Limitations/Counterevidence=`Limitations after §7 Conclusion; tested agents/channels only`。

<!-- claim:SF-2026-ARXIV-2605-24659:start -->IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24659:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24659:end -->

<!-- review:SF-2026-ARXIV-2605-24660:start -->
#### How Many Tools Should an LLM Agent See? A Chance-Corrected Answer

**问题与机制。** Before an LLM agent can use a tool, a retrieval system must decide which candidate tools to show to the agent. owner=`AGENT-TOOL-CALLING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Bits-over-Random and MDP exposure policy`；Evaluation=`§4 Empirical Evaluation`；Limitations/Counterevidence=`§5.3 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24660:start -->How Many Tools Should an LLM Agent See? A Chance-Corrected Answer only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24660:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24660:end -->

<!-- review:SF-2026-ARXIV-2605-24661:start -->
#### Measuring Reasoning Quality in LLMs: A Multi-Dimensional Behavioral Framework

**问题与机制。** Despite remarkable progress on reasoning benchmarks, current LLM evaluation practice remains anchored to final-answer correctness, providing limited insight into how models reason, how reliably they behave under contextual variation, or how efficiently they reach conclusions. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§4 multi-dimensional behavioral framework and aggregation`；Evaluation=`§5 Results`；Limitations/Counterevidence=`§6.2 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24661:start -->Measuring Reasoning Quality in LLMs: A Multi-Dimensional Behavioral Framework only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24661:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24661:end -->

<!-- review:SF-2026-ARXIV-2605-24662:start -->
#### OpenTwin: Closed-Loop Digital Twins for Trustworthy Policy Deployment in Open RAN

**问题与机制。** To fill this gap, we present OpenTwin, a closed-loop framework that learns the simulator configuration reproducing an operating deployment streamed measurements, certifies the resulting DT by re-simulation, calibrates it online, and evaluates each xApp action before it executes on the physical network. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§II–§IV OpenTwin closed-loop data assimilation, calibration and policy-validation workflow`；Evaluation=`§A Experimental Setup; §B Experimental Results`；Limitations/Counterevidence=`§V Limitations; real-network drift and Open-RAN testbed boundary`。

<!-- claim:SF-2026-ARXIV-2605-24662:start -->OpenTwin: Closed-Loop Digital Twins for Trustworthy Policy Deployment in Open RAN only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24662:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24662:end -->

<!-- review:SF-2026-ARXIV-2605-24667:start -->
#### When Mean CE Fails: Median CE Can Better Track Language Model Quality

**问题与机制。** Mean cross-entropy is the standard validation metric for language models, but it can fail to track model quality during training. owner=`TRAIN-PRETRAINING`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§3–4 mean/median CE interventions and top-K self-distillation`；Evaluation=`§3.2; §§4.2–4.4; Appendix C protocol`；Limitations/Counterevidence=`§5 Discussion — Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24667:start -->When Mean CE Fails: Median CE Can Better Track Language Model Quality only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24667:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24667:end -->

<!-- review:SF-2026-ARXIV-2605-24683:start -->
#### B.O.D.Y.: Beyond-Overlay Deterministic topologY -- A Layer-2 Declarative Ground Truth for AIOps Pipelines under Fragmented Administrative Boundaries

**问题与机制。** Modern AIOps environments operating within multi-campus institutional infrastructures suffer acutely from topological drift and black-box unmanaged physical network segments. owner=`PLATFORM-MONITORING`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§III deterministic L2 topology, identity loop and HIL protocol`；Evaluation=`§IV Implementation and Results`；Limitations/Counterevidence=`§V Limitations and Constraints`。

<!-- claim:SF-2026-ARXIV-2605-24683:start -->B.O.D.Y.: Beyond-Overlay Deterministic topologY -- A Layer-2 Declarative Ground Truth for AIOps Pipelines under Fragmented Administrative Boundaries only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24683:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24683:end -->

<!-- review:SF-2026-ARXIV-2605-24697:start -->
#### The Path Matters: Learning a Token-Commitment Policy for Diffusion Language Models

**问题与机制。** We introduce TraceLock, a lightweight plug-in controller that instantiates this policy for a frozen diffusion language model. owner=`MULTIMODAL-GENERATIVE-PARADIGMS`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 future-stability labels, learned commitment and TraceLock deployment`；Evaluation=`§4 Experiments; §§4.2–4.4`；Limitations/Counterevidence=`§5 Conclusion; frozen generator/tested diffusion backbones boundary`。

<!-- claim:SF-2026-ARXIV-2605-24697:start -->The Path Matters: Learning a Token-Commitment Policy for Diffusion Language Models only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24697:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24697:end -->

<!-- review:SF-2026-ARXIV-2605-24709:start -->
#### Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning

**问题与机制。** We close this gap using recurrent trace units, a diagonal recurrent architecture that enables exact RTRL with linear time and memory complexity in the parameter count, and show that they integrate cleanly into existing streaming algorithms across both discrete and continuous control. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Methodology; streaming partially-observed recurrent policy with exact RTRL`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§6 Discussion and Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24709:start -->Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24709:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24709:end -->

<!-- review:SF-2026-ARXIV-2605-24727:start -->
#### Fundamental Limitation in Explaining AI

**问题与机制。** In this paper, we mathematically prove a fundamental quadrilemma in explaining AI, stating that AI and its explanation cannot satisfy the following four conditions simultaneously: 1) the complexity of the operation environment, 2) the goodness of the AI's performance, 3) the interpretability of the AI's explanation, and 4) the complete faithfulness of the AI's explanation. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 four explanation conditions; §4 quadrilemma theorem/implications`；Evaluation=`formal construction and implications in §4`；Limitations/Counterevidence=`§5 Conclusion, limitations and future work`。

<!-- claim:SF-2026-ARXIV-2605-24727:start -->Fundamental Limitation in Explaining AI only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24727:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24727:end -->

<!-- review:SF-2026-ARXIV-2605-24728:start -->
#### Hylos: Operability Contracts for Model-Native Spatial Intelligence

**问题与机制。** A generated object or environment becomes useful to an agent only when the system can identify its entities, frames, surfaces, constraints, provenance, admissible actions, expected effects, and validation failures. owner=`MULTIMODAL-EMBODIED-VLA`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§4 operability state/graph, spatial transactions and effect diffs; §5 agency gates`；Evaluation=`§6 repair stress test; §7 qualitative result`；Limitations/Counterevidence=`§1.2 Scope of Claims; prototype/trajectory does not establish general runtime validity`。

<!-- claim:SF-2026-ARXIV-2605-24728:start -->Hylos: Operability Contracts for Model-Native Spatial Intelligence only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24728:end -->

Books Decision=`Structural Candidate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24728:end -->

<!-- review:SF-2026-ARXIV-2605-24733:start -->
#### StepGap: A Hybrid NLI-LLM Checker for Step-Level Evidence-Gap Detectionin Multi-Hop Question Answering

**问题与机制。** We present \textbf{StepGap}, a hybrid NLI-LLM decision tree that detects step-level evidence gaps in multi-hop QA and emits one of three typed labels: \textsc{Contradicted Claim} (CC), \textsc{Irrelevant Evidence} (IE), or \textsc{Missing Bridge} (MB), each tied to a concrete repair action. owner=`AGENT-REFLECTION`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 formulation; §4 hybrid checker; §5 typed process reward`；Evaluation=`§6 checker evaluation; §7 GRPO training`；Limitations/Counterevidence=`Limitations after §8 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-24733:start -->StepGap: A Hybrid NLI-LLM Checker for Step-Level Evidence-Gap Detectionin Multi-Hop Question Answering only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24733:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24733:end -->

<!-- review:SF-2026-ARXIV-2605-24737:start -->
#### Who judges the judges? Governance from metrics: a runtime framework for continuous LLM compliance monitoring

**问题与机制。** Current approaches to AI compliance treat conformity as a binary, audit-time verdict rather than a continuous, measurable property of production systems. owner=`PLATFORM-MONITORING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 governance from metrics; §4 govllm architecture; §5 contributions`；Evaluation=`§6 Preliminary experiments`；Limitations/Counterevidence=`§6.3 and §7.4 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24737:start -->Who judges the judges? Governance from metrics: a runtime framework for continuous LLM compliance monitoring only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24737:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24737:end -->

<!-- review:SF-2026-ARXIV-2605-24743:start -->
#### Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning

**问题与机制。** We propose BOOST, a bilevel optimization framework where the inner level trains the LLM on reweighted data and the outer level trains a lightweight reweighting head on held-out real validation tasks, assigning continuous trajectory-level weights without requiring an external judge. owner=`TRAIN-DATA`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 bilevel synthetic-trajectory weighting; §4 theory`；Evaluation=`§§5–6 experiments and learned-weight analysis`；Limitations/Counterevidence=`§7 Conclusion; three tasks and synthetic-generator boundary`。

<!-- claim:SF-2026-ARXIV-2605-24743:start -->Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24743:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24743:end -->

<!-- review:SF-2026-ARXIV-2605-24749:start -->
#### How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis

**问题与机制。** We study this feedback in a Gaussian single-index model with $r^*(x) = σ^*(\langle θ^*, x\rangle)$ and $x \sim N(0, I_d)$. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§3–5 reward-weighted feature recovery and tilted-policy value gap`；Evaluation=`theory and deployment-temperature analysis in §§4–5`；Limitations/Counterevidence=`§6 Conclusion and Discussion; single-index/theoretical-assumption boundary`。

<!-- claim:SF-2026-ARXIV-2605-24749:start -->How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24749:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24749:end -->

<!-- review:SF-2026-ARXIV-2605-24756:start -->
#### Proper Scoring Rules for Agentic Uncertainty Quantification

**问题与机制。** Building on prequential proper scoring, we introduce the Trajectory Proper Score (TPS), a predictor-agnostic family of strictly proper trajectory-level scoring rules for any per-step uncertainty signal calibrated into a probability of eventual success. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§4 proper trajectory scores under complete and censored observation`；Evaluation=`§5 metrics; §6 Experiments`；Limitations/Counterevidence=`§7 Conclusion and Limitations`。

<!-- claim:SF-2026-ARXIV-2605-24756:start -->Proper Scoring Rules for Agentic Uncertainty Quantification only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24756:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24756:end -->

<!-- review:SF-2026-ARXIV-2605-24770:start -->
#### Muon in Vision Transformers: Optimizer-Recipe Interactions and Gradient Spectra

**问题与机制。** We study Muon for ViT training, largely on ImageNet-100 and Pl@ntNet-300K, comparing against AdamW under standard vision recipes involving mixup, cutmix, smoothing, and random augmentation and erasing. owner=`TRAIN-PRETRAINING`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§§2–5 Muon geometry and recipe interaction`；Evaluation=`§§3–6; Appendices C–E`；Limitations/Counterevidence=`§7 Conclusions and limitations`。

<!-- claim:SF-2026-ARXIV-2605-24770:start -->Muon in Vision Transformers: Optimizer-Recipe Interactions and Gradient Spectra only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24770:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24770:end -->

<!-- review:SF-2026-ARXIV-2605-24775:start -->
#### PRIMA: Operational Patterns for Resilient Multi-Agent Research with Verifiable Identity and Convergent Feedback

**问题与机制。** We present PRIMA, whose primary contributions are three operational patterns for surviving these failure modes: (1) a resilience-and-recovery layer that detects upstream rate-limit signals, persists a typed pause record to disk, and resumes long-running runs without re-executing converged work even across process restarts; (2) a sub-agent operating discipline encoding task-fidelity, tool-use, revision, and inter-step context-boundary norms as a structural prompt layer; (3) a multi-phase application pattern for structured engineering deliverables pairing orthogonal draft steps with an explicit cross-document harmonization pass before final synthesis. owner=`AGENT-MULTI-AGENT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§III identity; §§IV–VIII protocol, scoring, orchestration and persistence`；Evaluation=`reported operational examples and convergence traces in §§VI–VIII`；Limitations/Counterevidence=`§I/§II claim scope; pattern/prototype rather than general production proof`。

<!-- claim:SF-2026-ARXIV-2605-24775:start -->PRIMA: Operational Patterns for Resilient Multi-Agent Research with Verifiable Identity and Convergent Feedback only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24775:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24775:end -->

<!-- review:SF-2026-ARXIV-2605-24785:start -->
#### PANDO: Efficient Multimodal AI Agents via Online Skill Distillation

**问题与机制。** We first analyze trajectories from VisualWebArena and identify three recurring sources of inefficiency: repeat-action loops, hidden discovery costs, and low prompt-cache reuse. owner=`AGENT-PLATFORM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 cost decomposition and online skill-distillation lifecycle`；Evaluation=`§5 Experimental Setup and reported results`；Limitations/Counterevidence=`§7 Limitations and Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-24785:start -->PANDO: Efficient Multimodal AI Agents via Online Skill Distillation only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24785:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24785:end -->

<!-- review:SF-2026-ARXIV-2605-24786:start -->
#### CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM

**问题与机制。** We introduce CONF-KV, a KV-cache manager that converts the next-token distribution into a scalar confidence score and uses it to choose the per-step cache budget, retaining more context when the model is uncertain and pruning aggressively when it is confident. owner=`INFER-KV-CACHE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 confidence-aware mixed-precision cache manager`；Evaluation=`§§4–6 setup, results and ablations`；Limitations/Counterevidence=`§7 failure modes; §8 Limitations and conclusion`。

<!-- claim:SF-2026-ARXIV-2605-24786:start -->CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24786:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24786:end -->

<!-- review:SF-2026-ARXIV-2605-24793:start -->
#### Beyond the Target: From Imitation to Collaboration in Speculative Decoding

**问题与机制。** Speculative decoding (SPD) accelerates large language model (LLM) inference by letting a smaller draft model propose multiple future tokens that are verified in parallel by a larger target model. owner=`INFER-SPECULATIVE-DECODING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 utility view, collaborative arbitration and RL training`；Evaluation=`§4 Experiments; §§4.2–4.4`；Limitations/Counterevidence=`§5 Conclusion and Appendix A tested-model/benchmark boundary`。

<!-- claim:SF-2026-ARXIV-2605-24793:start -->Beyond the Target: From Imitation to Collaboration in Speculative Decoding only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-24793:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24793:end -->

<!-- review:SF-2026-ARXIV-2605-28872:start -->
#### ReclaimNet: Reclaim-Aware Network Protocols for Voluntary GPU Sharing on Campus

**问题与机制。** We present ReclaimNet, a network-layer migration protocol suite that treats provider reclaim as a first-class contract rather than a failure case, combining three mechanisms: (i) reclaim-aware checkpoint scheduling that jointly adapts to time-varying departure hazards and contended bandwidth across co-resident jobs; (ii) volatility-aware destination selection integrating topology, survival probability, and notice-window feasibility; and (iii) deadline-aware migration traffic control with edge enforcement and a submillisecond TC BPF kill-switch. owner=`PLATFORM-GPU-SCHEDULER`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§IV measurement; §§V–VI reclaim-aware membership/lease protocol`；Evaluation=`§VII Evaluation and campus deployment measurements`；Limitations/Counterevidence=`§VIII Limitations and Conclusion; voluntary campus-network and failure-domain boundary`。

<!-- claim:SF-2026-ARXIV-2605-28872:start -->ReclaimNet: Reclaim-Aware Network Protocols for Voluntary GPU Sharing on Campus only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-28872:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-28872:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-00089 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2606-00089 |
| SF-2026-ARXIV-2606-02606 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2606-02606 |
| SF-2026-ARXIV-2605-24326 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24326 |
| SF-2026-ARXIV-2605-24391 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24391 |
| SF-2026-ARXIV-2605-24420 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24420 |
| SF-2026-ARXIV-2605-24421 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24421 |
| SF-2026-ARXIV-2605-24425 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24425 |
| SF-2026-ARXIV-2605-24426 | score_7_9;forced_review;potential_books_delta | selected | DA-COEVOLUTION-CONTROL | — | 跨层改变 power、training control 或 token commit ownership | analysis:DA-COEVOLUTION-CONTROL |
| SF-2026-ARXIV-2605-24461 | score_7_9;forced_review;potential_books_delta | selected | DA-POWER-LIFECYCLE | — | 跨层改变 power、training control 或 token commit ownership | analysis:DA-POWER-LIFECYCLE |
| SF-2026-ARXIV-2605-24468 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24468 |
| SF-2026-ARXIV-2605-24517 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24517 |
| SF-2026-ARXIV-2605-24547 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24547 |
| SF-2026-ARXIV-2605-24558 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24558 |
| SF-2026-ARXIV-2605-24579 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24579 |
| SF-2026-ARXIV-2605-24583 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24583 |
| SF-2026-ARXIV-2605-24598 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24598 |
| SF-2026-ARXIV-2605-24614 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24614 |
| SF-2026-ARXIV-2605-24619 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24619 |
| SF-2026-ARXIV-2605-24657 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24657 |
| SF-2026-ARXIV-2605-24659 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24659 |
| SF-2026-ARXIV-2605-24660 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24660 |
| SF-2026-ARXIV-2605-24661 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24661 |
| SF-2026-ARXIV-2605-24662 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24662 |
| SF-2026-ARXIV-2605-24667 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24667 |
| SF-2026-ARXIV-2605-24683 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24683 |
| SF-2026-ARXIV-2605-24697 | score_7_9;forced_review;potential_books_delta | selected | DA-TOKEN-COMMIT | — | 跨层改变 power、training control 或 token commit ownership | analysis:DA-TOKEN-COMMIT |
| SF-2026-ARXIV-2605-24709 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24709 |
| SF-2026-ARXIV-2605-24727 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24727 |
| SF-2026-ARXIV-2605-24728 | score_7_9;forced_review;potential_structural_gap | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24728 |
| SF-2026-ARXIV-2605-24733 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24733 |
| SF-2026-ARXIV-2605-24737 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24737 |
| SF-2026-ARXIV-2605-24743 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24743 |
| SF-2026-ARXIV-2605-24749 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24749 |
| SF-2026-ARXIV-2605-24756 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24756 |
| SF-2026-ARXIV-2605-24770 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24770 |
| SF-2026-ARXIV-2605-24775 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24775 |
| SF-2026-ARXIV-2605-24785 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24785 |
| SF-2026-ARXIV-2605-24786 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24786 |
| SF-2026-ARXIV-2605-24793 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24793 |
| SF-2026-ARXIV-2605-28872 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选只受三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-28872 |

<!-- analysis:DA-POWER-LIFECYCLE:start -->
### DA-POWER-LIFECYCLE

旧 scheduler 在 facility power 被视为静态容量时只需排 GPU；100MW 级 cluster 的 rack variance、cooling demand 与 power swing 让 provisioning、validation 和 runtime cap 成为连续状态机。收益是提高可用功率与设备利用率，代价是 telemetry/model drift 和 correlated thermal failure；单站测量不能外推所有 datacenter，失配时回退保守 cap。
<!-- analysis:DA-POWER-LIFECYCLE:end -->

<!-- analysis:DA-COEVOLUTION-CONTROL:start -->
### DA-COEVOLUTION-CONTROL

固定 environment/interface 在任务分布稳定时可简化 RL；当 agent failure 暴露 observation、tool schema 或 feedback interface 的系统缺口，只有改 policy 会反复学习坏接口。SEAL 把 verifier diagnosis 同时路由到 interface evolution 与 advantage reweighting，收益是闭合 agent/environment feedback，代价是双边漂移和 credit ambiguity；验证失败时冻结 interface 并回到固定环境。
<!-- analysis:DA-COEVOLUTION-CONTROL:end -->

<!-- analysis:DA-TOKEN-COMMIT:start -->
### DA-TOKEN-COMMIT

固定 block 或 confidence threshold 在 diffusion trajectory 稳定时可并行 commit；不同 token 的 future stability 不同后，commit controller 必须观察 trace-local evidence。TraceLock 学习 token-local policy，提高并行度但引入 selector drift、错误早提交与回滚成本；只证明所测 frozen generator，置信不足时回退保守 schedule。
<!-- analysis:DA-TOKEN-COMMIT:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-00089:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2606-00089:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-02606:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2606-02606:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24326:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24326:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24391:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24391:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24420:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24420:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24421:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24421:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24425:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24425:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24468:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24468:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24517:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24517:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24547:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24547:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24558:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24558:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24579:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24579:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24583:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24583:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24598:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24598:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24614:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24614:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24619:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24619:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24657:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24657:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24659:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24659:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24660:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24660:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24661:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24661:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24662:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24662:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24667:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24667:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24683:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24683:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24709:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24709:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24727:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24727:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24728:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24728:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24733:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24733:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24737:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24737:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24743:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24743:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24749:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24749:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24756:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24756:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24770:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24770:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24775:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24775:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24785:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24785:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24786:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24786:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24793:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24793:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-28872:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-28872:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-00089 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2606-00089 | delta:SF-2026-ARXIV-2606-00089 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-00089 |
| SF-2026-ARXIV-2606-02606 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | books/part-06-ai-infrastructure/72-security.md#chapter-72 | existing:SF-2026-ARXIV-2606-02606 | delta:SF-2026-ARXIV-2606-02606 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-02606 |
| SF-2026-ARXIV-2605-24326 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-24326 | delta:SF-2026-ARXIV-2605-24326 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24326 |
| SF-2026-ARXIV-2605-24391 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-24391 | delta:SF-2026-ARXIV-2605-24391 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24391 |
| SF-2026-ARXIV-2605-24420 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24420 | delta:SF-2026-ARXIV-2605-24420 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24420 |
| SF-2026-ARXIV-2605-24421 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24421 | delta:SF-2026-ARXIV-2605-24421 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24421 |
| SF-2026-ARXIV-2605-24425 | MODEL-TRANSFORMER-LAYER | books/part-02-model/17-transformer-layer.md#chapter-17 | books/part-02-model/16-feed-forward-mlp.md#chapter-16;books/part-02-model/18-decoder-only.md#chapter-18 | existing:SF-2026-ARXIV-2605-24425 | delta:SF-2026-ARXIV-2605-24425 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24425 |
| SF-2026-ARXIV-2605-24426 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24426 | delta:SF-2026-ARXIV-2605-24426 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24426 |
| SF-2026-ARXIV-2605-24461 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#chapter-63 | books/part-06-ai-infrastructure/62-gateway.md#chapter-62;books/part-06-ai-infrastructure/64-volcano.md#chapter-64 | existing:SF-2026-ARXIV-2605-24461 | delta:SF-2026-ARXIV-2605-24461 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24461 |
| SF-2026-ARXIV-2605-24468 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-24468 | delta:SF-2026-ARXIV-2605-24468 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24468 |
| SF-2026-ARXIV-2605-24517 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-24517 | delta:SF-2026-ARXIV-2605-24517 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24517 |
| SF-2026-ARXIV-2605-24547 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24547 | delta:SF-2026-ARXIV-2605-24547 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24547 |
| SF-2026-ARXIV-2605-24558 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-24558 | delta:SF-2026-ARXIV-2605-24558 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24558 |
| SF-2026-ARXIV-2605-24579 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-24579 | delta:SF-2026-ARXIV-2605-24579 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24579 |
| SF-2026-ARXIV-2605-24583 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24583 | delta:SF-2026-ARXIV-2605-24583 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24583 |
| SF-2026-ARXIV-2605-24598 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24598 | delta:SF-2026-ARXIV-2605-24598 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24598 |
| SF-2026-ARXIV-2605-24614 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24614 | delta:SF-2026-ARXIV-2605-24614 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24614 |
| SF-2026-ARXIV-2605-24619 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24619 | delta:SF-2026-ARXIV-2605-24619 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24619 |
| SF-2026-ARXIV-2605-24657 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-24657 | delta:SF-2026-ARXIV-2605-24657 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24657 |
| SF-2026-ARXIV-2605-24659 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24659 | delta:SF-2026-ARXIV-2605-24659 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24659 |
| SF-2026-ARXIV-2605-24660 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-24660 | delta:SF-2026-ARXIV-2605-24660 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24660 |
| SF-2026-ARXIV-2605-24661 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24661 | delta:SF-2026-ARXIV-2605-24661 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24661 |
| SF-2026-ARXIV-2605-24662 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24662 | delta:SF-2026-ARXIV-2605-24662 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24662 |
| SF-2026-ARXIV-2605-24667 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-24667 | delta:SF-2026-ARXIV-2605-24667 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24667 |
| SF-2026-ARXIV-2605-24683 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-24683 | delta:SF-2026-ARXIV-2605-24683 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24683 |
| SF-2026-ARXIV-2605-24697 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-24697 | delta:SF-2026-ARXIV-2605-24697 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24697 |
| SF-2026-ARXIV-2605-24709 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24709 | delta:SF-2026-ARXIV-2605-24709 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24709 |
| SF-2026-ARXIV-2605-24727 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24727 | delta:SF-2026-ARXIV-2605-24727 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24727 |
| SF-2026-ARXIV-2605-24728 | considered:MULTIMODAL-EMBODIED-VLA,AGENT-WORKFLOW | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-24728 | delta:SF-2026-ARXIV-2605-24728 | Layering / Dependency | Structural Candidate | books-review:SF-2026-ARXIV-2605-24728 |
| SF-2026-ARXIV-2605-24733 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#chapter-80 | books/part-07-agent/79-planning.md#chapter-79;books/part-07-agent/81-workflow.md#chapter-81 | existing:SF-2026-ARXIV-2605-24733 | delta:SF-2026-ARXIV-2605-24733 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24733 |
| SF-2026-ARXIV-2605-24737 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-24737 | delta:SF-2026-ARXIV-2605-24737 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24737 |
| SF-2026-ARXIV-2605-24743 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-24743 | delta:SF-2026-ARXIV-2605-24743 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24743 |
| SF-2026-ARXIV-2605-24749 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24749 | delta:SF-2026-ARXIV-2605-24749 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24749 |
| SF-2026-ARXIV-2605-24756 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24756 | delta:SF-2026-ARXIV-2605-24756 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24756 |
| SF-2026-ARXIV-2605-24770 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-24770 | delta:SF-2026-ARXIV-2605-24770 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24770 |
| SF-2026-ARXIV-2605-24775 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24775 | delta:SF-2026-ARXIV-2605-24775 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24775 |
| SF-2026-ARXIV-2605-24785 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24785 | delta:SF-2026-ARXIV-2605-24785 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24785 |
| SF-2026-ARXIV-2605-24786 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-24786 | delta:SF-2026-ARXIV-2605-24786 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24786 |
| SF-2026-ARXIV-2605-24793 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47;books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-24793 | delta:SF-2026-ARXIV-2605-24793 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24793 |
| SF-2026-ARXIV-2605-28872 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#chapter-63 | books/part-06-ai-infrastructure/62-gateway.md#chapter-62;books/part-06-ai-infrastructure/64-volcano.md#chapter-64 | existing:SF-2026-ARXIV-2605-28872 | delta:SF-2026-ARXIV-2605-28872 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-28872 |
<!-- books-review:SF-2026-ARXIV-2606-00089:start -->
<!-- existing:SF-2026-ARXIV-2606-00089:start -->现有 physical safety gate 尚未明确分离 action-conditioned transition violation 与 merely off-log behavior，混合 max score 会丢失 rejection semantics。<!-- existing:SF-2026-ARXIV-2606-00089:end -->
<!-- delta:SF-2026-ARXIV-2606-00089:start -->We formalize this prediction-control interface and prove that the all-pairs displacement term is redundant within a max-aggregated composite.<!-- delta:SF-2026-ARXIV-2606-00089:end --> Independent decision=`Integrate`；owner_sha256=a78e439d8d301c686575bc38f307852352bf950dc9a3066df7fa01fb6734131b。
<!-- books-review:SF-2026-ARXIV-2606-00089:end -->
<!-- books-review:SF-2026-ARXIV-2606-02606:start -->
<!-- existing:SF-2026-ARXIV-2606-02606:start -->现有 production/registry 已绑定 adapter 与 base revision，但没有定义 base service 演进后 adapter initialization、service-readiness recovery 与 rollout promotion 的同一迁移契约。<!-- existing:SF-2026-ARXIV-2606-02606:end -->
<!-- delta:SF-2026-ARXIV-2606-02606:start -->To address this problem, we propose ReLoRA, a knowledge-reusing re-adaptation framework that efficiently restores service-ready LoRA adapters for evolving LLM services while preserving or improving task performance.<!-- delta:SF-2026-ARXIV-2606-02606:end --> Independent decision=`Integrate`；owner_sha256=8a1230c5475bc0996e1bc446b54154f914d1177178f82eb98e8c9ebe5ad29679。
<!-- books-review:SF-2026-ARXIV-2606-02606:end -->
<!-- books-review:SF-2026-ARXIV-2605-24326:start -->
<!-- existing:SF-2026-ARXIV-2605-24326:start -->现有章节已覆盖 topology-aware placement、collective/parallelism co-design、异构网络 profile、simulation 与 fallback；ScaleAcross 属于同一机制的跨楼宇实例。<!-- existing:SF-2026-ARXIV-2605-24326:end -->
<!-- delta:SF-2026-ARXIV-2605-24326:start -->As infrastructure expands, the system design space becomes increasingly intricate, encompassing new model architectures, hardware heterogeneity, and evolving communication patterns.<!-- delta:SF-2026-ARXIV-2605-24326:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=4f93d876e7023721408d2cb9a84c868ecf7049796c99bb18d430ffb936337560。
<!-- books-review:SF-2026-ARXIV-2605-24326:end -->
<!-- books-review:SF-2026-ARXIV-2605-24391:start -->
<!-- existing:SF-2026-ARXIV-2605-24391:start -->现有执行计划覆盖 bit-exact format，却未表达同一 microscaling block 在 training/direct-cast inference 间按 exponent/mantissa mode 切换的格式与硬件共同身份。<!-- existing:SF-2026-ARXIV-2605-24391:end -->
<!-- delta:SF-2026-ARXIV-2605-24391:start -->In this work, we present a versatile MXFP format, called MX-SAFE (MXSF in short), that adaptively uses two modes, i.e., a wider mantissa mode (FP8 E2M5) and a subnormal FP mode (FP5 E3M2), to support both training and direct-cast inference.<!-- delta:SF-2026-ARXIV-2605-24391:end --> Independent decision=`Integrate`；owner_sha256=86a67912e98da1110924056b16139a49e3854f707c8d56e04448ce75d12c6950。
<!-- books-review:SF-2026-ARXIV-2605-24391:end -->
<!-- books-review:SF-2026-ARXIV-2605-24420:start -->
<!-- existing:SF-2026-ARXIV-2605-24420:start -->现有 privacy 章没有把 BatchNorm cross-sample statistics 作为 memorization 与 membership inference 的训练态共享通道。<!-- existing:SF-2026-ARXIV-2605-24420:end -->
<!-- delta:SF-2026-ARXIV-2605-24420:start -->We conduct an extensive empirical study using three complementary approaches: (i) unintended memorization of out-of-distribution training samples, (ii) per-sample influence measured via gradient norms, and (iii) susceptibility to membership inference attacks (MIA).<!-- delta:SF-2026-ARXIV-2605-24420:end --> Independent decision=`Integrate`；owner_sha256=ef7882199869af53c1d9715b6343b35023fff4e4a578647be098c6dbdd21cf0e。
<!-- books-review:SF-2026-ARXIV-2605-24420:end -->
<!-- books-review:SF-2026-ARXIV-2605-24421:start -->
<!-- existing:SF-2026-ARXIV-2605-24421:start -->现有 prompt-injection 边界没有把 attacker-controlled log field 明确视为安全分析链路的 untrusted instruction substrate。<!-- existing:SF-2026-ARXIV-2605-24421:end -->
<!-- delta:SF-2026-ARXIV-2605-24421:start -->We study a structural failure mode of this design: many log fields are attacker controlled.<!-- delta:SF-2026-ARXIV-2605-24421:end --> Independent decision=`Integrate`；owner_sha256=ef7882199869af53c1d9715b6343b35023fff4e4a578647be098c6dbdd21cf0e。
<!-- books-review:SF-2026-ARXIV-2605-24421:end -->
<!-- books-review:SF-2026-ARXIV-2605-24425:start -->
<!-- existing:SF-2026-ARXIV-2605-24425:start -->现有 Transformer Layer 把 residual stream 当 activation carrier，未表达跨层 momentum state 如何改变深度方向更新以及与 preconditioning 分工。<!-- existing:SF-2026-ARXIV-2605-24425:end -->
<!-- delta:SF-2026-ARXIV-2605-24425:start -->A controlled ablation and supporting theory show that momentum, not preconditioning, is the main source of the gain.<!-- delta:SF-2026-ARXIV-2605-24425:end --> Independent decision=`Integrate`；owner_sha256=c03328e1ab575411f62dbdf61f64d8559082b96df8e231b5b3795adde2a69a15。
<!-- books-review:SF-2026-ARXIV-2605-24425:end -->
<!-- books-review:SF-2026-ARXIV-2605-24426:start -->
<!-- existing:SF-2026-ARXIV-2605-24426:start -->现有 RLHF 将 environment/interface 多视作固定 rollout 条件；缺少 verifier diagnosis 驱动 learning interface 与 policy 同步演进的双 owner 闭环。<!-- existing:SF-2026-ARXIV-2605-24426:end -->
<!-- delta:SF-2026-ARXIV-2605-24426:start -->We identify this structural gap as \emph{Agent-Environment Misalignment}: the agent's capability frontier changes during training, while the environment that provides supervision remains static or only weakly coupled to the agent's revealed failures.<!-- delta:SF-2026-ARXIV-2605-24426:end --> Independent decision=`Integrate`；owner_sha256=df76cc355aa8203c222d08d5ef206aedc1549bbadcbf2b404d0b341eac4694e8。
<!-- books-review:SF-2026-ARXIV-2605-24426:end -->
<!-- books-review:SF-2026-ARXIV-2605-24461:start -->
<!-- existing:SF-2026-ARXIV-2605-24461:start -->现有 scheduler 讨论 power-aware admission，但未贯通 design provisioning、rack validation、operational cap 与 runtime power swing 的责任交接。<!-- existing:SF-2026-ARXIV-2605-24461:end -->
<!-- delta:SF-2026-ARXIV-2605-24461:start -->We present detailed power measurements for a 150 MW datacenter hosting a cluster of 83K GB200 GPUs.<!-- delta:SF-2026-ARXIV-2605-24461:end --> Independent decision=`Integrate`；owner_sha256=f44097493dfbe426ed1dadf2e27d3f87e14068d7f9d96027f8fa7c8a51511b45。
<!-- books-review:SF-2026-ARXIV-2605-24461:end -->
<!-- books-review:SF-2026-ARXIV-2605-24468:start -->
<!-- existing:SF-2026-ARXIV-2605-24468:start -->现有章节已经由 raw immutable trajectory、derived cue、write/read policy、provenance 和 rollback 构成同一 memory lifecycle；SAM 未改变该 owner。<!-- existing:SF-2026-ARXIV-2605-24468:end -->
<!-- delta:SF-2026-ARXIV-2605-24468:start -->To this end, we propose State-Adaptive Memory~(SAM), a standalone framework that consolidates ongoing interaction into compact memory cues while preserving raw trajectory pages for intent-driven recall.<!-- delta:SF-2026-ARXIV-2605-24468:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=859029c176f33208548742c32d8bbd45836601858f6f8205cf7227795a2a6f51。
<!-- books-review:SF-2026-ARXIV-2605-24468:end -->
<!-- books-review:SF-2026-ARXIV-2605-24517:start -->
<!-- existing:SF-2026-ARXIV-2605-24517:start -->现有章节已明确 training-only observation/world-token auxiliary supervision 不等于 runtime world state；ECHO 是该边界内案例。<!-- existing:SF-2026-ARXIV-2605-24517:end -->
<!-- delta:SF-2026-ARXIV-2605-24517:start -->We introduce ECHO (Environment Cross-entropy Hybrid Objective), a hybrid objective that combines the standard policy-gradient loss on action tokens with an auxiliary loss that trains the policy to predict environment observation tokens resulting from its own actions.<!-- delta:SF-2026-ARXIV-2605-24517:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=8eba6188ba7b28ccead4779988e06a1e42eb7c8b638cc8e8319281251ae3446e。
<!-- books-review:SF-2026-ARXIV-2605-24517:end -->
<!-- books-review:SF-2026-ARXIV-2605-24547:start -->
<!-- existing:SF-2026-ARXIV-2605-24547:start -->现有 textual feedback 是静态 rubric/critic artifact；缺少以 policy return 为上层目标反向学习 feedback generator 的 bilevel control loop。<!-- existing:SF-2026-ARXIV-2605-24547:end -->
<!-- delta:SF-2026-ARXIV-2605-24547:start -->We formalize this coupling as a Stackelberg bilevel program and derive Bilevel Natural Language Actor-Critic (Bi-NAC), which jointly trains a critic to generate reward-improving feedback and an actor to exploit it.<!-- delta:SF-2026-ARXIV-2605-24547:end --> Independent decision=`Integrate`；owner_sha256=df76cc355aa8203c222d08d5ef206aedc1549bbadcbf2b404d0b341eac4694e8。
<!-- books-review:SF-2026-ARXIV-2605-24547:end -->
<!-- books-review:SF-2026-ARXIV-2605-24558:start -->
<!-- existing:SF-2026-ARXIV-2605-24558:start -->现有 Data 章已把 observation/measurement pipeline、schema/provenance 与 transformation version 纳入 dataset identity；position paper 未给出新的可验证接口。<!-- existing:SF-2026-ARXIV-2605-24558:end -->
<!-- delta:SF-2026-ARXIV-2605-24558:start -->\textbf{We argue that these measurement-to-dataset pipelines are inference components: treating their outputs as ``given data'' freezes an observation model and obscures uncertainty over feasible pipeline choices.} We identify three failure modes arising from this ``frozen lens'': \textbf{(C1) hidden hypothesis space}, where the released dataset does not specify the pipeline configuration or its validity conditions; \textbf{(C2) uncertified transportability}, where a pipeline may be documented but its regime of validity is untested, so failures under distribution shift cannot be adjudicated; \textbf{(C3) ungoverned multiplicity}, where many defensible pipelines exist and dispersion is real but not propagated into uncertainty-aware evidence.<!-- delta:SF-2026-ARXIV-2605-24558:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=0e382b1714d3c389d41845aaad046f5179c117a50d6c613102efed4b564f3755。
<!-- books-review:SF-2026-ARXIV-2605-24558:end -->
<!-- books-review:SF-2026-ARXIV-2605-24579:start -->
<!-- existing:SF-2026-ARXIV-2605-24579:start -->现有 Memory 章有 write/read 分离，却没有以 TFC/OE/CSM/RM 四个干预条件区分 reader ceiling、write loss 与 retrieval loss。<!-- existing:SF-2026-ARXIV-2605-24579:end -->
<!-- delta:SF-2026-ARXIV-2605-24579:start -->We introduce a four-condition diagnostic protocol that evaluates a fixed reader under truncated full context (TFC), oracle evidence (OE), complete stored memory (CSM), and retrieved memory (RM).<!-- delta:SF-2026-ARXIV-2605-24579:end --> Independent decision=`Integrate`；owner_sha256=859029c176f33208548742c32d8bbd45836601858f6f8205cf7227795a2a6f51。
<!-- books-review:SF-2026-ARXIV-2605-24579:end -->
<!-- books-review:SF-2026-ARXIV-2605-24583:start -->
<!-- existing:SF-2026-ARXIV-2605-24583:start -->现有 alignment evaluation 未把 prompt/template confound、mean-direction shift、effective-rank proxy 与 causal ablation 组织成可反驳的 activation audit。<!-- existing:SF-2026-ARXIV-2605-24583:end -->
<!-- delta:SF-2026-ARXIV-2605-24583:start -->We show the obvious way to form this matrix is confounded.<!-- delta:SF-2026-ARXIV-2605-24583:end --> Independent decision=`Integrate`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24583:end -->
<!-- books-review:SF-2026-ARXIV-2605-24598:start -->
<!-- existing:SF-2026-ARXIV-2605-24598:start -->现有多 Agent 协调未覆盖 device/cloud step-level routing 在任务历史、成功概率、网络开销与 cost budget 下的可学习控制状态。<!-- existing:SF-2026-ARXIV-2605-24598:end -->
<!-- delta:SF-2026-ARXIV-2605-24598:start -->To address this issue, we present Hera, a step-level device--cloud LLM agent coordinator for long-horizon tasks achieving a strong performance--cost Pareto frontier.<!-- delta:SF-2026-ARXIV-2605-24598:end --> Independent decision=`Integrate`；owner_sha256=48b45443639518cec718da5a162973b920b5de48c6fb030e443c51b41e37000a。
<!-- books-review:SF-2026-ARXIV-2605-24598:end -->
<!-- books-review:SF-2026-ARXIV-2605-24614:start -->
<!-- existing:SF-2026-ARXIV-2605-24614:start -->现有 Evaluation 已覆盖 unlearning counterfactual/activation audit、多维 score、simulator feedback loop 与 release gate；对应 family 是已覆盖受限实例。<!-- existing:SF-2026-ARXIV-2605-24614:end -->
<!-- delta:SF-2026-ARXIV-2605-24614:start -->To address these limitations, we propose the Unlearning Depth Score (UDS), a metric that quantifies the mechanistic depth of unlearning via activation patching.<!-- delta:SF-2026-ARXIV-2605-24614:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24614:end -->
<!-- books-review:SF-2026-ARXIV-2605-24619:start -->
<!-- existing:SF-2026-ARXIV-2605-24619:start -->现有章节已把 LLM proposal 与 deterministic/formal verifier 的 authority 分离；IC3Syn 未改变 commit owner。<!-- existing:SF-2026-ARXIV-2605-24619:end -->
<!-- delta:SF-2026-ARXIV-2605-24619:start -->We present IC3Syn, a neuro-symbolic framework that synthesizes inductive invariants by executing an IC3-style process over TLA+ states with the assistance of Large Language Models (LLMs).<!-- delta:SF-2026-ARXIV-2605-24619:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=fb79e1d1dc0522d217986d7a6df65191484bbc5d4ad827f59cbc2fbf9a80ba11。
<!-- books-review:SF-2026-ARXIV-2605-24619:end -->
<!-- books-review:SF-2026-ARXIV-2605-24657:start -->
<!-- existing:SF-2026-ARXIV-2605-24657:start -->现有 Context/Memory 已比较 compaction 与 durable learned state，并绑定 base/model revision；该 consolidation 实验未改变 owner。<!-- existing:SF-2026-ARXIV-2605-24657:end -->
<!-- delta:SF-2026-ARXIV-2605-24657:start -->Major LLM platforms deploy models in an inference-only configuration: the model serves requests but never updates per-user weights.<!-- delta:SF-2026-ARXIV-2605-24657:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=55db3e124881a0bcde65d0587c9c31fa32ada720f92e5a0fc530cbb77952a53d。
<!-- books-review:SF-2026-ARXIV-2605-24657:end -->
<!-- books-review:SF-2026-ARXIV-2605-24659:start -->
<!-- existing:SF-2026-ARXIV-2605-24659:start -->现有章节已覆盖 indirect injection、adaptive adversary、tool/output boundary 与 defense-in-depth；IterInject 是攻击搜索增强，不是新的生产防御契约。<!-- existing:SF-2026-ARXIV-2605-24659:end -->
<!-- delta:SF-2026-ARXIV-2605-24659:start -->We introduce \oursys, a feedback-guided iterative framework that closes the loop between injection, diagnosis, and refinement: a rule-based diagnoser produces structured outcome labels with behavioral descriptions, and an LLM-based optimizer refines payloads conditioned on the full optimization history.<!-- delta:SF-2026-ARXIV-2605-24659:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=ef7882199869af53c1d9715b6343b35023fff4e4a578647be098c6dbdd21cf0e。
<!-- books-review:SF-2026-ARXIV-2605-24659:end -->
<!-- books-review:SF-2026-ARXIV-2605-24660:start -->
<!-- existing:SF-2026-ARXIV-2605-24660:start -->现有 tool shortlist 没有用 chance-corrected information gain 把 candidate-set size 与 random baseline 从 tool exposure reward 中扣除。<!-- existing:SF-2026-ARXIV-2605-24660:end -->
<!-- delta:SF-2026-ARXIV-2605-24660:start -->Before an LLM agent can use a tool, a retrieval system must decide which candidate tools to show to the agent.<!-- delta:SF-2026-ARXIV-2605-24660:end --> Independent decision=`Integrate`；owner_sha256=3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9。
<!-- books-review:SF-2026-ARXIV-2605-24660:end -->
<!-- books-review:SF-2026-ARXIV-2605-24661:start -->
<!-- existing:SF-2026-ARXIV-2605-24661:start -->现有 Evaluation 已覆盖 unlearning counterfactual/activation audit、多维 score、simulator feedback loop 与 release gate；对应 family 是已覆盖受限实例。<!-- existing:SF-2026-ARXIV-2605-24661:end -->
<!-- delta:SF-2026-ARXIV-2605-24661:start -->Despite remarkable progress on reasoning benchmarks, current LLM evaluation practice remains anchored to final-answer correctness, providing limited insight into how models reason, how reliably they behave under contextual variation, or how efficiently they reach conclusions.<!-- delta:SF-2026-ARXIV-2605-24661:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24661:end -->
<!-- books-review:SF-2026-ARXIV-2605-24662:start -->
<!-- existing:SF-2026-ARXIV-2605-24662:start -->现有 Evaluation 已覆盖 unlearning counterfactual/activation audit、多维 score、simulator feedback loop 与 release gate；对应 family 是已覆盖受限实例。<!-- existing:SF-2026-ARXIV-2605-24662:end -->
<!-- delta:SF-2026-ARXIV-2605-24662:start -->To fill this gap, we present OpenTwin, a closed-loop framework that learns the simulator configuration reproducing an operating deployment streamed measurements, certifies the resulting DT by re-simulation, calibrates it online, and evaluates each xApp action before it executes on the physical network.<!-- delta:SF-2026-ARXIV-2605-24662:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24662:end -->
<!-- books-review:SF-2026-ARXIV-2605-24667:start -->
<!-- existing:SF-2026-ARXIV-2605-24667:start -->现有 pretraining 以 mean CE 为主，没有记录 heavy-tail token loss 下 median CE/mean CE 与 downstream quality 的 concordance regime。<!-- existing:SF-2026-ARXIV-2605-24667:end -->
<!-- delta:SF-2026-ARXIV-2605-24667:start -->Mean cross-entropy is the standard validation metric for language models, but it can fail to track model quality during training.<!-- delta:SF-2026-ARXIV-2605-24667:end --> Independent decision=`Integrate`；owner_sha256=7ed3a8bde8bbf14b9d742176e34c931da3630528bbad900256f07bdc2df3e9c7。
<!-- books-review:SF-2026-ARXIV-2605-24667:end -->
<!-- books-review:SF-2026-ARXIV-2605-24683:start -->
<!-- existing:SF-2026-ARXIV-2605-24683:start -->现有 monitoring 假设 topology/asset identity 可得；缺少 fragmented admin domain 下 deterministic L2 ground truth、integrity loop 与 HIL admission。<!-- existing:SF-2026-ARXIV-2605-24683:end -->
<!-- delta:SF-2026-ARXIV-2605-24683:start -->Modern AIOps environments operating within multi-campus institutional infrastructures suffer acutely from topological drift and black-box unmanaged physical network segments.<!-- delta:SF-2026-ARXIV-2605-24683:end --> Independent decision=`Integrate`；owner_sha256=b61889e5ef350937dfc6eaff0029815bd5239105a48de2145e51210c0673919a。
<!-- books-review:SF-2026-ARXIV-2605-24683:end -->
<!-- books-review:SF-2026-ARXIV-2605-24697:start -->
<!-- existing:SF-2026-ARXIV-2605-24697:start -->现有 diffusion commit 比较 confidence/block schedule，未包含从 future stability trace 学习 token-local commitment policy 与动态 threshold 的分支。<!-- existing:SF-2026-ARXIV-2605-24697:end -->
<!-- delta:SF-2026-ARXIV-2605-24697:start -->We introduce TraceLock, a lightweight plug-in controller that instantiates this policy for a frozen diffusion language model.<!-- delta:SF-2026-ARXIV-2605-24697:end --> Independent decision=`Integrate`；owner_sha256=82d67a82821a384369ee36c24794db1b14bdfd6d538877525c38e9420761df30。
<!-- books-review:SF-2026-ARXIV-2605-24697:end -->
<!-- books-review:SF-2026-ARXIV-2605-24709:start -->
<!-- existing:SF-2026-ARXIV-2605-24709:start -->现有 RL loop 多按完整 trajectory 更新；缺少 partial observation 下 recurrent hidden/eligibility state 的 per-step exact online update ownership。<!-- existing:SF-2026-ARXIV-2605-24709:end -->
<!-- delta:SF-2026-ARXIV-2605-24709:start -->We close this gap using recurrent trace units, a diagonal recurrent architecture that enables exact RTRL with linear time and memory complexity in the parameter count, and show that they integrate cleanly into existing streaming algorithms across both discrete and continuous control.<!-- delta:SF-2026-ARXIV-2605-24709:end --> Independent decision=`Integrate`；owner_sha256=df76cc355aa8203c222d08d5ef206aedc1549bbadcbf2b404d0b341eac4694e8。
<!-- books-review:SF-2026-ARXIV-2605-24709:end -->
<!-- books-review:SF-2026-ARXIV-2605-24727:start -->
<!-- existing:SF-2026-ARXIV-2605-24727:start -->现有 explainability/evidence 章节未显式给出 fidelity、completeness、human comprehensibility 与 universal applicability 不可同时保证的 claim boundary。<!-- existing:SF-2026-ARXIV-2605-24727:end -->
<!-- delta:SF-2026-ARXIV-2605-24727:start -->In this paper, we mathematically prove a fundamental quadrilemma in explaining AI, stating that AI and its explanation cannot satisfy the following four conditions simultaneously: 1) the complexity of the operation environment, 2) the goodness of the AI's performance, 3) the interpretability of the AI's explanation, and 4) the complete faithfulness of the AI's explanation.<!-- delta:SF-2026-ARXIV-2605-24727:end --> Independent decision=`Integrate`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24727:end -->
<!-- books-review:SF-2026-ARXIV-2605-24728:start -->
<!-- existing:SF-2026-ARXIV-2605-24728:start -->当前 owner 与相邻章节已覆盖同一长期 mechanism、identity、trade-off 与 fallback；该 exact-v1 仅提供受限实例。<!-- existing:SF-2026-ARXIV-2605-24728:end -->
<!-- delta:SF-2026-ARXIV-2605-24728:start -->A generated object or environment becomes useful to an agent only when the system can identify its entities, frames, surfaces, constraints, provenance, admissible actions, expected effects, and validation failures.<!-- delta:SF-2026-ARXIV-2605-24728:end --> Independent decision=`Structural Candidate`；owner_sha256=a78e439d8d301c686575bc38f307852352bf950dc9a3066df7fa01fb6734131b。
<!-- books-review:SF-2026-ARXIV-2605-24728:end -->
<!-- books-review:SF-2026-ARXIV-2605-24733:start -->
<!-- existing:SF-2026-ARXIV-2605-24733:start -->现有章节已经以 evidence gap、typed verification failure 与 selective rerun 组织 reflection；StepGap 是 NLI/LLM 实现实例。<!-- existing:SF-2026-ARXIV-2605-24733:end -->
<!-- delta:SF-2026-ARXIV-2605-24733:start -->We present \textbf{StepGap}, a hybrid NLI-LLM decision tree that detects step-level evidence gaps in multi-hop QA and emits one of three typed labels: \textsc{Contradicted Claim} (CC), \textsc{Irrelevant Evidence} (IE), or \textsc{Missing Bridge} (MB), each tied to a concrete repair action.<!-- delta:SF-2026-ARXIV-2605-24733:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=c1293a34a41ce0c0ee8d27ebdb10d68cada38430db2d77545ddb7873abd6fe08。
<!-- books-review:SF-2026-ARXIV-2605-24733:end -->
<!-- books-review:SF-2026-ARXIV-2605-24737:start -->
<!-- existing:SF-2026-ARXIV-2605-24737:start -->现有 monitoring 已覆盖 policy-bound sensor、versioned metric、continuous compliance 与 unknown propagation；govllm 未改变 owner。<!-- existing:SF-2026-ARXIV-2605-24737:end -->
<!-- delta:SF-2026-ARXIV-2605-24737:start -->Current approaches to AI compliance treat conformity as a binary, audit-time verdict rather than a continuous, measurable property of production systems.<!-- delta:SF-2026-ARXIV-2605-24737:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=b61889e5ef350937dfc6eaff0029815bd5239105a48de2145e51210c0673919a。
<!-- books-review:SF-2026-ARXIV-2605-24737:end -->
<!-- books-review:SF-2026-ARXIV-2605-24743:start -->
<!-- existing:SF-2026-ARXIV-2605-24743:start -->现有 synthetic-data admission 未表达由 held-out real trajectory loss 反向拥有每条 multi-turn synthetic trajectory weight 的 bilevel选择。<!-- existing:SF-2026-ARXIV-2605-24743:end -->
<!-- delta:SF-2026-ARXIV-2605-24743:start -->We propose BOOST, a bilevel optimization framework where the inner level trains the LLM on reweighted data and the outer level trains a lightweight reweighting head on held-out real validation tasks, assigning continuous trajectory-level weights without requiring an external judge.<!-- delta:SF-2026-ARXIV-2605-24743:end --> Independent decision=`Integrate`；owner_sha256=0e382b1714d3c389d41845aaad046f5179c117a50d6c613102efed4b564f3755。
<!-- books-review:SF-2026-ARXIV-2605-24743:end -->
<!-- books-review:SF-2026-ARXIV-2605-24749:start -->
<!-- existing:SF-2026-ARXIV-2605-24749:start -->现有 reward model 评价未把 training distribution 的 prediction error 与 reward-tilted deployment distribution 的 policy value gap分开。<!-- existing:SF-2026-ARXIV-2605-24749:end -->
<!-- delta:SF-2026-ARXIV-2605-24749:start -->We study this feedback in a Gaussian single-index model with $r^*(x) = σ^*(\langle θ^*, x\rangle)$ and $x \sim N(0, I_d)$.<!-- delta:SF-2026-ARXIV-2605-24749:end --> Independent decision=`Integrate`；owner_sha256=df76cc355aa8203c222d08d5ef206aedc1549bbadcbf2b404d0b341eac4694e8。
<!-- books-review:SF-2026-ARXIV-2605-24749:end -->
<!-- books-review:SF-2026-ARXIV-2605-24756:start -->
<!-- existing:SF-2026-ARXIV-2605-24756:start -->现有 proper scoring 主要针对 outcome/confidence；缺少带 early termination/censoring 的整条 agent trajectory 的严格 proper score。<!-- existing:SF-2026-ARXIV-2605-24756:end -->
<!-- delta:SF-2026-ARXIV-2605-24756:start -->Building on prequential proper scoring, we introduce the Trajectory Proper Score (TPS), a predictor-agnostic family of strictly proper trajectory-level scoring rules for any per-step uncertainty signal calibrated into a probability of eventual success.<!-- delta:SF-2026-ARXIV-2605-24756:end --> Independent decision=`Integrate`；owner_sha256=ec7aa353d8c12a45a4efc02c1ff1a58c3e703f2e4ef5a2f308e43eb9e88be10e。
<!-- books-review:SF-2026-ARXIV-2605-24756:end -->
<!-- books-review:SF-2026-ARXIV-2605-24770:start -->
<!-- existing:SF-2026-ARXIV-2605-24770:start -->现有 Muon 机制讨论 update geometry，但未把 augmentation/mixing/smoothing recipe 与 gradient spectrum 共同纳入 optimizer recipe identity。<!-- existing:SF-2026-ARXIV-2605-24770:end -->
<!-- delta:SF-2026-ARXIV-2605-24770:start -->We study Muon for ViT training, largely on ImageNet-100 and Pl@ntNet-300K, comparing against AdamW under standard vision recipes involving mixup, cutmix, smoothing, and random augmentation and erasing.<!-- delta:SF-2026-ARXIV-2605-24770:end --> Independent decision=`Integrate`；owner_sha256=7ed3a8bde8bbf14b9d742176e34c931da3630528bbad900256f07bdc2df3e9c7。
<!-- books-review:SF-2026-ARXIV-2605-24770:end -->
<!-- books-review:SF-2026-ARXIV-2605-24775:start -->
<!-- existing:SF-2026-ARXIV-2605-24775:start -->现有章节已覆盖 verifiable identity、delegation、convergence feedback、append-only state 与 branch/merge；PRIMA 是同构 pattern bundle。<!-- existing:SF-2026-ARXIV-2605-24775:end -->
<!-- delta:SF-2026-ARXIV-2605-24775:start -->We present PRIMA, whose primary contributions are three operational patterns for surviving these failure modes: (1) a resilience-and-recovery layer that detects upstream rate-limit signals, persists a typed pause record to disk, and resumes long-running runs without re-executing converged work even across process restarts; (2) a sub-agent operating discipline encoding task-fidelity, tool-use, revision, and inter-step context-boundary norms as a structural prompt layer; (3) a multi-phase application pattern for structured engineering deliverables pairing orthogonal draft steps with an explicit cross-document harmonization pass before final synthesis.<!-- delta:SF-2026-ARXIV-2605-24775:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=48b45443639518cec718da5a162973b920b5de48c6fb030e443c51b41e37000a。
<!-- books-review:SF-2026-ARXIV-2605-24775:end -->
<!-- books-review:SF-2026-ARXIV-2605-24785:start -->
<!-- existing:SF-2026-ARXIV-2605-24785:start -->现有 Agent Platform 已拥有 skill distillation、promotion、drift、rollback 与 lifecycle evidence；PANDO 的 web-agent实验不改变该 contract。<!-- existing:SF-2026-ARXIV-2605-24785:end -->
<!-- delta:SF-2026-ARXIV-2605-24785:start -->We first analyze trajectories from VisualWebArena and identify three recurring sources of inefficiency: repeat-action loops, hidden discovery costs, and low prompt-cache reuse.<!-- delta:SF-2026-ARXIV-2605-24785:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=fb79e1d1dc0522d217986d7a6df65191484bbc5d4ad827f59cbc2fbf9a80ba11。
<!-- books-review:SF-2026-ARXIV-2605-24785:end -->
<!-- books-review:SF-2026-ARXIV-2605-24786:start -->
<!-- existing:SF-2026-ARXIV-2605-24786:start -->现有 KV 章已拥有 confidence-aware mixed precision、budget/eviction、estimator drift 和 FullKV fallback；CONF-KV 属已覆盖分支。<!-- existing:SF-2026-ARXIV-2605-24786:end -->
<!-- delta:SF-2026-ARXIV-2605-24786:start -->We introduce CONF-KV, a KV-cache manager that converts the next-token distribution into a scalar confidence score and uses it to choose the per-step cache budget, retaining more context when the model is uncertain and pruning aggressively when it is confident.<!-- delta:SF-2026-ARXIV-2605-24786:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=322a087f0629a6acc48fc085f83172b753f8fa38a54f182e7b9d5f8d36b02348。
<!-- books-review:SF-2026-ARXIV-2605-24786:end -->
<!-- books-review:SF-2026-ARXIV-2605-24793:start -->
<!-- existing:SF-2026-ARXIV-2605-24793:start -->现有 speculation 以 target exactness 为 commit contract；缺少 draft 可能优于 target 时由 utility-aware arbitrator 拥有非 exact commit 的 alternative branch。<!-- existing:SF-2026-ARXIV-2605-24793:end -->
<!-- delta:SF-2026-ARXIV-2605-24793:start -->Speculative decoding (SPD) accelerates large language model (LLM) inference by letting a smaller draft model propose multiple future tokens that are verified in parallel by a larger target model.<!-- delta:SF-2026-ARXIV-2605-24793:end --> Independent decision=`Integrate`；owner_sha256=63abd49ea9f1fc8cb365512ea7b41f59d786879ec3603ab77545700307a29ce8。
<!-- books-review:SF-2026-ARXIV-2605-24793:end -->
<!-- books-review:SF-2026-ARXIV-2605-28872:start -->
<!-- existing:SF-2026-ARXIV-2605-28872:start -->现有 reclaim 以 scheduler-owned GPU 为前提；缺少 voluntary host、membership lease、network reachability 与 reclaim notice 共同决定可用容量的协议。<!-- existing:SF-2026-ARXIV-2605-28872:end -->
<!-- delta:SF-2026-ARXIV-2605-28872:start -->We present ReclaimNet, a network-layer migration protocol suite that treats provider reclaim as a first-class contract rather than a failure case, combining three mechanisms: (i) reclaim-aware checkpoint scheduling that jointly adapts to time-varying departure hazards and contended bandwidth across co-resident jobs; (ii) volatility-aware destination selection integrating topology, survival probability, and notice-window feasibility; and (iii) deadline-aware migration traffic control with edge enforcement and a submillisecond TC BPF kill-switch.<!-- delta:SF-2026-ARXIV-2605-28872:end --> Independent decision=`Integrate`；owner_sha256=f44097493dfbe426ed1dadf2e27d3f87e14068d7f9d96027f8fa7c8a51511b45。
<!-- books-review:SF-2026-ARXIV-2605-28872:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260524-COVERAGE | fresh-context:may2026-day03-non-author | coverage | coverage:SRC-ARXIV:20260524 | none | semantic-independent-audit.json#scope | passed |
| SA-20260524-EVIDENCE | fresh-context:may2026-day03-non-author | evidence | review:SF-2026-ARXIV-2606-00089 | none | semantic-independent-audit.json#scope | passed |
| SA-20260524-SELECTION | fresh-context:may2026-day03-non-author | deep_analysis_selection | analysis:DA-POWER-LIFECYCLE | none | semantic-independent-audit.json#scope | passed |
| SA-20260524-BOOKS | fresh-context:may2026-day03-non-author | books | books-review:SF-2026-ARXIV-2606-00089 | none | semantic-independent-audit.json#scope | passed |

Cross-model skipped: non-interactive delegated context。

## 8. Ignored Noise

249 条 family-specific pre-denominator closure 保存在 `screening-ledger-final.json`；每条保留 title、abstract 机制、排除边界与重开条件。

## 9. Recommended Action

`2605.24728` 保留为 Structural Candidate，进入结构复核而非强塞现有章节。24 项写回已经未参与本日 pre-write 与 root 写作的 reviewer 顺读 owner+adjacent，并通过机制、边界、唯一 owner 与章节流验收。

## 10. Repository Changes

- 重建 05-24 independent ledger、40 项 exact-v1 receipt、current Books comparison、24 项 root writeback queue、semantic audit 与空 Materials Request。
- 24/24 项已写入 16 个 canonical owner 章节；marker、owner 路径、`Review notes` 前 placement 与 scoped `git diff --check` 已通过。
- 新增 `post-write-semantic-audit.json`；首轮发现的 4 组 placement 问题经 root 修复后完成第二轮复验，queue 24/24 标记为 `post_write_semantic_audit_passed`。
- 未 stage、commit 或 push。

## 11. Open Questions

- Hylos 的 operability contract 是否在季度结构审计中需要独立 owner，还是可由 Embodied 与 Agent Workflow 双向 handoff 承载？

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 12. Sources

- [Can Predicted Dynamics Exist in the Physical World?](https://arxiv.org/html/2606.00089v1) — arXiv:2606.00089v1；first-public 2026-05-23；accessed 2026-09-01
- [ReLoRA: Knowledge-Reusing Adaptation for Fast Rollout of Evolving LLM Services](https://arxiv.org/html/2606.02606v1) — arXiv:2606.02606v1；first-public 2026-05-23；accessed 2026-09-01
- [ScaleAcross Explorer: Exploring Communication Optimization for Scale-Across AI Model Training](https://arxiv.org/html/2605.24326v1) — arXiv:2605.24326v1；first-public 2026-05-23；accessed 2026-09-01
- [MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format with On-the-Fly Exponent and Mantissa Bit Allocation](https://arxiv.org/html/2605.24391v1) — arXiv:2605.24391v1；first-public 2026-05-23；accessed 2026-09-01
- [Batch Normalization Amplifies Memorization and Privacy Risks](https://arxiv.org/html/2605.24420v1) — arXiv:2605.24420v1；first-public 2026-05-23；accessed 2026-09-01
- [Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content](https://arxiv.org/html/2605.24421v1) — arXiv:2605.24421v1；first-public 2026-05-23；accessed 2026-09-01
- [Momentum Streams for Optimizer-Inspired Transformers](https://arxiv.org/html/2605.24425v1) — arXiv:2605.24425v1；first-public 2026-05-23；accessed 2026-09-01
- [SEAL: Synergistic Co-Evolution of Agents and Learning Environments](https://arxiv.org/html/2605.24426v1) — arXiv:2605.24426v1；first-public 2026-05-23；accessed 2026-09-01
- [Provisioning to Runtime Optimization of a 100 MW-Scale AI Cluster](https://arxiv.org/html/2605.24461v1) — arXiv:2605.24461v1；first-public 2026-05-23；accessed 2026-09-01
- [SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent](https://arxiv.org/html/2605.24468v1) — arXiv:2605.24468v1；first-public 2026-05-23；accessed 2026-09-01
- [ECHO: Terminal Agents Learn World Models for Free](https://arxiv.org/pdf/2605.24517v1) — arXiv:2605.24517v1；first-public 2026-05-23；accessed 2026-09-01
- [RL with Learnable Textual Feedback: A Bilevel Approach](https://arxiv.org/html/2605.24547v1) — arXiv:2605.24547v1；first-public 2026-05-23；accessed 2026-09-01
- [Position: AI for Science Should Treat Measurement-to-Dataset Pipelines as Inference Components](https://arxiv.org/html/2605.24558v1) — arXiv:2605.24558v1；first-public 2026-05-23；accessed 2026-09-01
- [WhenLoss: Diagnosing Write and Retrieval Bottlenecks in Long-Context Memory Systems](https://arxiv.org/html/2605.24579v1) — arXiv:2605.24579v1；first-public 2026-05-23；accessed 2026-09-01
- [Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol](https://arxiv.org/html/2605.24583v1) — arXiv:2605.24583v1；first-public 2026-05-23；accessed 2026-09-01
- [Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents](https://arxiv.org/html/2605.24598v1) — arXiv:2605.24598v1；first-public 2026-05-23；accessed 2026-09-01
- [Measuring the Depth of LLM Unlearning via Activation Patching](https://arxiv.org/html/2605.24614v1) — arXiv:2605.24614v1；first-public 2026-05-23；accessed 2026-09-01
- [Synthesizing Inductive Invariants for Distributed Protocols via IC3 and Large Language Models](https://arxiv.org/html/2605.24619v1) — arXiv:2605.24619v1；first-public 2026-05-23；accessed 2026-09-01
- [Beyond Inference-Only Deployment: Comparing Weight-Based Consolidation Against Cascading Compaction](https://arxiv.org/html/2605.24657v1) — arXiv:2605.24657v1；first-public 2026-05-23；accessed 2026-09-01
- [IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization](https://arxiv.org/html/2605.24659v1) — arXiv:2605.24659v1；first-public 2026-05-23；accessed 2026-09-01
- [How Many Tools Should an LLM Agent See? A Chance-Corrected Answer](https://arxiv.org/html/2605.24660v1) — arXiv:2605.24660v1；first-public 2026-05-23；accessed 2026-09-01
- [Measuring Reasoning Quality in LLMs: A Multi-Dimensional Behavioral Framework](https://arxiv.org/html/2605.24661v1) — arXiv:2605.24661v1；first-public 2026-05-23；accessed 2026-09-01
- [OpenTwin: Closed-Loop Digital Twins for Trustworthy Policy Deployment in Open RAN](https://arxiv.org/pdf/2605.24662v1) — arXiv:2605.24662v1；first-public 2026-05-23；accessed 2026-09-01
- [When Mean CE Fails: Median CE Can Better Track Language Model Quality](https://arxiv.org/html/2605.24667v1) — arXiv:2605.24667v1；first-public 2026-05-23；accessed 2026-09-01
- [B.O.D.Y.: Beyond-Overlay Deterministic topologY -- A Layer-2 Declarative Ground Truth for AIOps Pipelines under Fragmented Administrative Boundaries](https://arxiv.org/html/2605.24683v1) — arXiv:2605.24683v1；first-public 2026-05-23；accessed 2026-09-01
- [The Path Matters: Learning a Token-Commitment Policy for Diffusion Language Models](https://arxiv.org/html/2605.24697v1) — arXiv:2605.24697v1；first-public 2026-05-23；accessed 2026-09-01
- [Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning](https://arxiv.org/pdf/2605.24709v1) — arXiv:2605.24709v1；first-public 2026-05-23；accessed 2026-09-01
- [Fundamental Limitation in Explaining AI](https://arxiv.org/html/2605.24727v1) — arXiv:2605.24727v1；first-public 2026-05-23；accessed 2026-09-01
- [Hylos: Operability Contracts for Model-Native Spatial Intelligence](https://arxiv.org/html/2605.24728v1) — arXiv:2605.24728v1；first-public 2026-05-23；accessed 2026-09-01
- [StepGap: A Hybrid NLI-LLM Checker for Step-Level Evidence-Gap Detectionin Multi-Hop Question Answering](https://arxiv.org/html/2605.24733v1) — arXiv:2605.24733v1；first-public 2026-05-23；accessed 2026-09-01
- [Who judges the judges? Governance from metrics: a runtime framework for continuous LLM compliance monitoring](https://arxiv.org/pdf/2605.24737v1) — arXiv:2605.24737v1；first-public 2026-05-23；accessed 2026-09-01
- [Bilevel Optimization of Synthetic Trajectories for Multi-Turn LLM Fine-Tuning](https://arxiv.org/html/2605.24743v1) — arXiv:2605.24743v1；first-public 2026-05-23；accessed 2026-09-01
- [How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis](https://arxiv.org/html/2605.24749v1) — arXiv:2605.24749v1；first-public 2026-05-23；accessed 2026-09-01
- [Proper Scoring Rules for Agentic Uncertainty Quantification](https://arxiv.org/html/2605.24756v1) — arXiv:2605.24756v1；first-public 2026-05-23；accessed 2026-09-01
- [Muon in Vision Transformers: Optimizer-Recipe Interactions and Gradient Spectra](https://arxiv.org/html/2605.24770v1) — arXiv:2605.24770v1；first-public 2026-05-23；accessed 2026-09-01
- [PRIMA: Operational Patterns for Resilient Multi-Agent Research with Verifiable Identity and Convergent Feedback](https://arxiv.org/html/2605.24775v1) — arXiv:2605.24775v1；first-public 2026-05-23；accessed 2026-09-01
- [PANDO: Efficient Multimodal AI Agents via Online Skill Distillation](https://arxiv.org/pdf/2605.24785v1) — arXiv:2605.24785v1；first-public 2026-05-23；accessed 2026-09-01
- [CONF-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage for Long-Horizon LLM](https://arxiv.org/html/2605.24786v1) — arXiv:2605.24786v1；first-public 2026-05-23；accessed 2026-09-01
- [Beyond the Target: From Imitation to Collaboration in Speculative Decoding](https://arxiv.org/html/2605.24793v1) — arXiv:2605.24793v1；first-public 2026-05-23；accessed 2026-09-01
- [ReclaimNet: Reclaim-Aware Network Protocols for Voluntary GPU Sharing on Campus](https://arxiv.org/html/2605.28872v1) — arXiv:2605.28872v1；first-public 2026-05-23；accessed 2026-09-01

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

05-24 已完成 289/289、40/40 exact-v1、ordinary pending=0、blocked=0 与 24/24 Books 写回；不同 reviewer 已完成 owner+adjacent post-write semantic audit，首轮 4 组 placement finding 均修复并复验通过，Daily 全链路闭合。
