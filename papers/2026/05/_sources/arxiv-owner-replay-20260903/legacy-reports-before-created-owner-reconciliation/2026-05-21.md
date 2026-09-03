# Daily Research — 2026-05-21

**Research Date:** 2026-05-21

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-20 09:00:00 ～ 2026-05-21 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；技术结论绑定 official arXiv exact-v1。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。15 项 Books 写回均已通过非写作者 fresh-context post-write semantic audit（15/15）。

## Executive Summary

从 91,841 条月度 raw records 中注册并独立重放 629/629 identity。author denominator 36 经审计移除 3 个 false positive、恢复 33 个 false negative，最终 66 项（10.49%），563 项以逐 family 唯一理由在分母前闭合。66/66 exact-v1 完成 source-specific Review，blocked=0。current owner 与相邻章节比较后冻结 15 项 Books queue；本 lane 未修改共享 Books。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-21 |
| Window End | 2026-05-21 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260521-V2-INDEPENDENT |
| Denominator Frozen At | 2026-09-01T02:13:45.998190+00:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-20T09:00:00+08:00 | 2026-05-21T09:00:00+08:00 | 2026-09-01T02:13:45.998190+00:00 | DataCite v2 00..99 + independent 629/629 semantic replay + official exact-v1 | checked | 629 | SF-2026-ARXIV-2605-20616;SF-2026-ARXIV-2605-20630;SF-2026-ARXIV-2605-20641;SF-2026-ARXIV-2605-20696;SF-2026-ARXIV-2605-20704;SF-2026-ARXIV-2605-20706;SF-2026-ARXIV-2605-20734;SF-2026-ARXIV-2605-20744;SF-2026-ARXIV-2605-20749;SF-2026-ARXIV-2605-20752;SF-2026-ARXIV-2605-20756;SF-2026-ARXIV-2605-20767;SF-2026-ARXIV-2605-20774;SF-2026-ARXIV-2605-20798;SF-2026-ARXIV-2605-20799;SF-2026-ARXIV-2605-20833;SF-2026-ARXIV-2605-20834;SF-2026-ARXIV-2605-20863;SF-2026-ARXIV-2605-20866;SF-2026-ARXIV-2605-20868;SF-2026-ARXIV-2605-20874;SF-2026-ARXIV-2605-20876;SF-2026-ARXIV-2605-20923;SF-2026-ARXIV-2605-20926;SF-2026-ARXIV-2605-20948;SF-2026-ARXIV-2605-21061;SF-2026-ARXIV-2605-21100;SF-2026-ARXIV-2605-21103;SF-2026-ARXIV-2605-21125;SF-2026-ARXIV-2605-21127;SF-2026-ARXIV-2605-21177;SF-2026-ARXIV-2605-21187;SF-2026-ARXIV-2605-21266;SF-2026-ARXIV-2605-21273;SF-2026-ARXIV-2605-21312;SF-2026-ARXIV-2605-21347;SF-2026-ARXIV-2605-21384;SF-2026-ARXIV-2605-21392;SF-2026-ARXIV-2605-21427;SF-2026-ARXIV-2605-21434;SF-2026-ARXIV-2605-21446;SF-2026-ARXIV-2605-21467;SF-2026-ARXIV-2605-21468;SF-2026-ARXIV-2605-21470;SF-2026-ARXIV-2605-21482;SF-2026-ARXIV-2605-21486;SF-2026-ARXIV-2605-21543;SF-2026-ARXIV-2605-21602;SF-2026-ARXIV-2605-21603;SF-2026-ARXIV-2605-21606;SF-2026-ARXIV-2605-21642;SF-2026-ARXIV-2605-21648;SF-2026-ARXIV-2605-21649;SF-2026-ARXIV-2605-21768;SF-2026-ARXIV-2605-21779;SF-2026-ARXIV-2605-21800;SF-2026-ARXIV-2605-21801;SF-2026-ARXIV-2605-21803;SF-2026-ARXIV-2605-21847;SF-2026-ARXIV-2605-21850;SF-2026-ARXIV-2605-22882;SF-2026-ARXIV-2605-22883;SF-2026-ARXIV-2605-22884;SF-2026-ARXIV-2605-24022;SF-2026-ARXIV-2605-26128;SF-2026-ARXIV-2605-26132 | pages=300;final_cursor=end;raw=91841;registered=629;screened=629;retained=66;closure=563 | 2026-05-21T00:59:59Z | screening-ledger-independent-final.json#sha256=b0ad8ab2d2b72fedd41fb3a66cb770201c325bdca8a93c4c1df522d58d176993 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260521:start -->629/629 identity 已独立重放；563 个 closure reason 全部唯一。Coverage=Closed。所有 retained family 均完成 exact-v1；没有 access blocker。<!-- coverage:SRC-ARXIV:20260521:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-20616 | arXiv:2605.20616v1 | paper-v1:2605.20616 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20616 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20616 | no |
| SF-2026-ARXIV-2605-20630 | arXiv:2605.20630v1 | paper-v1:2605.20630 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20630 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20630 | no |
| SF-2026-ARXIV-2605-20641 | arXiv:2605.20641v1 | paper-v1:2605.20641 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20641 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-20641 | no |
| SF-2026-ARXIV-2605-20696 | arXiv:2605.20696v1 | paper-v1:2605.20696 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20696 | self | — | new_in_window | TRAIN-DPO | Integrate | books-review:SF-2026-ARXIV-2605-20696 | no |
| SF-2026-ARXIV-2605-20704 | arXiv:2605.20704v1 | paper-v1:2605.20704 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20704 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20704 | no |
| SF-2026-ARXIV-2605-20706 | arXiv:2605.20706v1 | paper-v1:2605.20706 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20706 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20706 | no |
| SF-2026-ARXIV-2605-20734 | arXiv:2605.20734v1 | paper-v1:2605.20734 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20734 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20734 | no |
| SF-2026-ARXIV-2605-20744 | arXiv:2605.20744v1 | paper-v1:2605.20744 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20744 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20744 | no |
| SF-2026-ARXIV-2605-20749 | arXiv:2605.20749v1 | paper-v1:2605.20749 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20749 | self | — | new_in_window | MODEL-FFN | Integrate | books-review:SF-2026-ARXIV-2605-20749 | no |
| SF-2026-ARXIV-2605-20752 | arXiv:2605.20752v1 | paper-v1:2605.20752 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20752 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20752 | no |
| SF-2026-ARXIV-2605-20756 | arXiv:2605.20756v1 | paper-v1:2605.20756 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20756 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-20756 | no |
| SF-2026-ARXIV-2605-20767 | arXiv:2605.20767v1 | paper-v1:2605.20767 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20767 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20767 | no |
| SF-2026-ARXIV-2605-20774 | arXiv:2605.20774v1 | paper-v1:2605.20774 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20774 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20774 | no |
| SF-2026-ARXIV-2605-20798 | arXiv:2605.20798v1 | paper-v1:2605.20798 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20798 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20798 | no |
| SF-2026-ARXIV-2605-20799 | arXiv:2605.20799v1 | paper-v1:2605.20799 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20799 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-20799 | no |
| SF-2026-ARXIV-2605-20833 | arXiv:2605.20833v1 | paper-v1:2605.20833 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20833 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20833 | no |
| SF-2026-ARXIV-2605-20834 | arXiv:2605.20834v1 | paper-v1:2605.20834 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20834 | self | — | new_in_window | TRAIN-DPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20834 | no |
| SF-2026-ARXIV-2605-20863 | arXiv:2605.20863v1 | paper-v1:2605.20863 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20863 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20863 | no |
| SF-2026-ARXIV-2605-20866 | arXiv:2605.20866v1 | paper-v1:2605.20866 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20866 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20866 | no |
| SF-2026-ARXIV-2605-20868 | arXiv:2605.20868v1 | paper-v1:2605.20868 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20868 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20868 | no |
| SF-2026-ARXIV-2605-20874 | arXiv:2605.20874v1 | paper-v1:2605.20874 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20874 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20874 | no |
| SF-2026-ARXIV-2605-20876 | arXiv:2605.20876v1 | paper-v1:2605.20876 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20876 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20876 | no |
| SF-2026-ARXIV-2605-20923 | arXiv:2605.20923v1 | paper-v1:2605.20923 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20923 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-20923 | no |
| SF-2026-ARXIV-2605-20926 | arXiv:2605.20926v1 | paper-v1:2605.20926 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20926 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20926 | no |
| SF-2026-ARXIV-2605-20948 | arXiv:2605.20948v1 | paper-v1:2605.20948 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20948 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20948 | no |
| SF-2026-ARXIV-2605-21061 | arXiv:2605.21061v1 | paper-v1:2605.21061 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21061 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-21061 | no |
| SF-2026-ARXIV-2605-21100 | arXiv:2605.21100v1 | paper-v1:2605.21100 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21100 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-21100 | no |
| SF-2026-ARXIV-2605-21103 | arXiv:2605.21103v1 | paper-v1:2605.21103 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21103 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-21103 | no |
| SF-2026-ARXIV-2605-21125 | arXiv:2605.21125v1 | paper-v1:2605.21125 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21125 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21125 | no |
| SF-2026-ARXIV-2605-21127 | arXiv:2605.21127v1 | paper-v1:2605.21127 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21127 | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-ARXIV-2605-21127 | no |
| SF-2026-ARXIV-2605-21177 | arXiv:2605.21177v1 | paper-v1:2605.21177 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21177 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21177 | no |
| SF-2026-ARXIV-2605-21187 | arXiv:2605.21187v1 | paper-v1:2605.21187 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21187 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21187 | no |
| SF-2026-ARXIV-2605-21266 | arXiv:2605.21266v1 | paper-v1:2605.21266 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21266 | self | — | new_in_window | TRAIN-DPO | Integrate | books-review:SF-2026-ARXIV-2605-21266 | no |
| SF-2026-ARXIV-2605-21273 | arXiv:2605.21273v1 | paper-v1:2605.21273 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21273 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-21273 | no |
| SF-2026-ARXIV-2605-21312 | arXiv:2605.21312v1 | paper-v1:2605.21312 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21312 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21312 | no |
| SF-2026-ARXIV-2605-21347 | arXiv:2605.21347v1 | paper-v1:2605.21347 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21347 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21347 | no |
| SF-2026-ARXIV-2605-21384 | arXiv:2605.21384v1 | paper-v1:2605.21384 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21384 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21384 | no |
| SF-2026-ARXIV-2605-21392 | arXiv:2605.21392v1 | paper-v1:2605.21392 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21392 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21392 | no |
| SF-2026-ARXIV-2605-21427 | arXiv:2605.21427v1 | paper-v1:2605.21427 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21427 | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21427 | no |
| SF-2026-ARXIV-2605-21434 | arXiv:2605.21434v1 | paper-v1:2605.21434 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21434 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21434 | no |
| SF-2026-ARXIV-2605-21446 | arXiv:2605.21446v1 | paper-v1:2605.21446 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21446 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21446 | no |
| SF-2026-ARXIV-2605-21467 | arXiv:2605.21467v1 | paper-v1:2605.21467 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21467 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21467 | no |
| SF-2026-ARXIV-2605-21468 | arXiv:2605.21468v1 | paper-v1:2605.21468 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21468 | self | — | new_in_window | TRAIN-CHECKPOINT | Integrate | books-review:SF-2026-ARXIV-2605-21468 | no |
| SF-2026-ARXIV-2605-21470 | arXiv:2605.21470v1 | paper-v1:2605.21470 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21470 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21470 | no |
| SF-2026-ARXIV-2605-21482 | arXiv:2605.21482v1 | paper-v1:2605.21482 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21482 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21482 | no |
| SF-2026-ARXIV-2605-21486 | arXiv:2605.21486v1 | paper-v1:2605.21486 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21486 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21486 | no |
| SF-2026-ARXIV-2605-21543 | arXiv:2605.21543v1 | paper-v1:2605.21543 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21543 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21543 | no |
| SF-2026-ARXIV-2605-21602 | arXiv:2605.21602v1 | paper-v1:2605.21602 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21602 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21602 | no |
| SF-2026-ARXIV-2605-21603 | arXiv:2605.21603v1 | paper-v1:2605.21603 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21603 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21603 | no |
| SF-2026-ARXIV-2605-21606 | arXiv:2605.21606v1 | paper-v1:2605.21606 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21606 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21606 | no |
| SF-2026-ARXIV-2605-21642 | arXiv:2605.21642v1 | paper-v1:2605.21642 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21642 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21642 | no |
| SF-2026-ARXIV-2605-21648 | arXiv:2605.21648v1 | paper-v1:2605.21648 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21648 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21648 | no |
| SF-2026-ARXIV-2605-21649 | arXiv:2605.21649v1 | paper-v1:2605.21649 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21649 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21649 | no |
| SF-2026-ARXIV-2605-21768 | arXiv:2605.21768v1 | paper-v1:2605.21768 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21768 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21768 | no |
| SF-2026-ARXIV-2605-21779 | arXiv:2605.21779v1 | paper-v1:2605.21779 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21779 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21779 | no |
| SF-2026-ARXIV-2605-21800 | arXiv:2605.21800v1 | paper-v1:2605.21800 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21800 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21800 | no |
| SF-2026-ARXIV-2605-21801 | arXiv:2605.21801v1 | paper-v1:2605.21801 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21801 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21801 | no |
| SF-2026-ARXIV-2605-21803 | arXiv:2605.21803v1 | paper-v1:2605.21803 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21803 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21803 | no |
| SF-2026-ARXIV-2605-21847 | arXiv:2605.21847v1 | paper-v1:2605.21847 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21847 | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21847 | no |
| SF-2026-ARXIV-2605-21850 | arXiv:2605.21850v1 | paper-v1:2605.21850 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21850 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21850 | no |
| SF-2026-ARXIV-2605-22882 | arXiv:2605.22882v1 | paper-v1:2605.22882 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22882 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22882 | no |
| SF-2026-ARXIV-2605-22883 | arXiv:2605.22883v1 | paper-v1:2605.22883 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22883 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2605-22883 | no |
| SF-2026-ARXIV-2605-22884 | arXiv:2605.22884v1 | paper-v1:2605.22884 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22884 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-22884 | no |
| SF-2026-ARXIV-2605-24022 | arXiv:2605.24022v1 | paper-v1:2605.24022 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24022 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24022 | no |
| SF-2026-ARXIV-2605-26128 | arXiv:2605.26128v1 | paper-v1:2605.26128 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26128 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26128 | no |
| SF-2026-ARXIV-2605-26132 | arXiv:2605.26132v1 | paper-v1:2605.26132 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26132 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26132 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-20616 | RP-3c8483398da1e9c8 | deep | arXiv:2605.20616v1 | SRC-ARXIV@arXiv:2605.20616v1 | arXiv:2605.20616v1 HTML — §4 Offline Memory Consolidation | arXiv:2605.20616v1 HTML — §5 Experiments | arXiv:2605.20616v1 HTML — Appendix A Limitations | https://arxiv.org/html/2605.20616v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20616 | complete |
| SF-2026-ARXIV-2605-20630 | RP-b18decace203d62c | deep | arXiv:2605.20630v1 | SRC-ARXIV@arXiv:2605.20630v1 | arXiv:2605.20630v1 HTML — §3 Optimization Framework | arXiv:2605.20630v1 HTML — §4 Results | arXiv:2605.20630v1 HTML — §5 Limitations and Failure Modes | https://arxiv.org/html/2605.20630v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20630 | complete |
| SF-2026-ARXIV-2605-20641 | RP-0af1c36c45e213b8 | deep | arXiv:2605.20641v1 | SRC-ARXIV@arXiv:2605.20641v1 | arXiv:2605.20641v1 HTML — §3 Optimization-Triggered Attack Design | arXiv:2605.20641v1 HTML — §4 Implementation and Evaluation | arXiv:2605.20641v1 HTML — Appendix C Limitations | https://arxiv.org/html/2605.20641v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20641 | complete |
| SF-2026-ARXIV-2605-20696 | RP-bad47fe65a10384f | deep | arXiv:2605.20696v1 | SRC-ARXIV@arXiv:2605.20696v1 | arXiv:2605.20696v1 HTML — §3 Problem Formulation and Preliminaries | arXiv:2605.20696v1 HTML — §7 Numerical Results; §Appendix E Additional Detail for Experimental Setup; §Appendix F Additional Results | arXiv:2605.20696v1 HTML — §8 Conclusion | https://arxiv.org/html/2605.20696v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20696 | complete |
| SF-2026-ARXIV-2605-20704 | RP-4a6655121c220736 | deep | arXiv:2605.20704v1 | SRC-ARXIV@arXiv:2605.20704v1 | arXiv:2605.20704v1 HTML — §4.1–§4.6 Heartbeat-Bound Credential Protocol | arXiv:2605.20704v1 HTML — §6 Evaluation | arXiv:2605.20704v1 HTML — §7 Limitations and Future Work | https://arxiv.org/html/2605.20704v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20704 | complete |
| SF-2026-ARXIV-2605-20706 | RP-bd1d9c0d2aa3ce0c | deep | arXiv:2605.20706v1 | SRC-ARXIV@arXiv:2605.20706v1 | arXiv:2605.20706v1 HTML — §3 LlamaWeb Architecture | arXiv:2605.20706v1 HTML — §5 Evaluation | arXiv:2605.20706v1 HTML — §6 Discussion and WebGPU portability boundary | https://arxiv.org/html/2605.20706v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20706 | complete |
| SF-2026-ARXIV-2605-20734 | RP-885a316010579e11 | deep | arXiv:2605.20734v1 | SRC-ARXIV@arXiv:2605.20734v1 | arXiv:2605.20734v1 HTML — §4 Multi-Modal Reference Monitor | arXiv:2605.20734v1 HTML — §7 Evaluation | arXiv:2605.20734v1 HTML — §8 Limitations and Future Work | https://arxiv.org/html/2605.20734v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20734 | complete |
| SF-2026-ARXIV-2605-20744 | RP-d8091284d933cac8 | deep | arXiv:2605.20744v1 | SRC-ARXIV@arXiv:2605.20744v1 | arXiv:2605.20744v1 HTML — §3 Hack-Verifiable Environment Construction | arXiv:2605.20744v1 HTML — §5 Evaluation | arXiv:2605.20744v1 HTML — §7 Limitations and Future Work | https://arxiv.org/html/2605.20744v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20744 | complete |
| SF-2026-ARXIV-2605-20749 | RP-59f2f20578298545 | deep | arXiv:2605.20749v1 | SRC-ARXIV@arXiv:2605.20749v1 | arXiv:2605.20749v1 HTML — §4 Training Dynamics in the Kernel Regime: From NTK Spectrum to Loss Crossing | arXiv:2605.20749v1 HTML — §3.3 Experimental Verification; §5 Generalization Gap Analysis; §Appendix C Proof of Loss Crossing Results | arXiv:2605.20749v1 HTML — §6 Conclusion | https://arxiv.org/html/2605.20749v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20749 | complete |
| SF-2026-ARXIV-2605-20752 | RP-a801055f54dc9022 | deep | arXiv:2605.20752v1 | SRC-ARXIV@arXiv:2605.20752v1 | arXiv:2605.20752v1 HTML — §3 Method; §3.4 GaussianDream Training and Efficient Inference; §Stage I: GaussianDream pretraining. | arXiv:2605.20752v1 HTML — §4 Experiments; §4.1 Experimental Setup; §Simulation benchmarks. | arXiv:2605.20752v1 HTML — §5 Conclusion | https://arxiv.org/html/2605.20752v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20752 | complete |
| SF-2026-ARXIV-2605-20756 | RP-29baa519fa9f5341 | deep | arXiv:2605.20756v1 | SRC-ARXIV@arXiv:2605.20756v1 | arXiv:2605.20756v1 HTML — §5 Proposed method; §7.1 Main pretraining results; §Appendix A Algorithm and instantiations | arXiv:2605.20756v1 HTML — §6 Convergence analysis; §7 Experiments; §7.1 Main pretraining results | arXiv:2605.20756v1 HTML — §8 Limitations; §9 Conclusion; §Appendix C Discussion | https://arxiv.org/html/2605.20756v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20756 | complete |
| SF-2026-ARXIV-2605-20767 | RP-894e00dbb265731a | deep | arXiv:2605.20767v1 | SRC-ARXIV@arXiv:2605.20767v1 | arXiv:2605.20767v1 HTML — §3 Causal Estimands for LLM-Simulated Interventions | arXiv:2605.20767v1 HTML — §4 Experiments | arXiv:2605.20767v1 HTML — §6 Discussion and observational-study boundary | https://arxiv.org/html/2605.20767v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20767 | complete |
| SF-2026-ARXIV-2605-20774 | RP-0fb828e6d2ddf085 | deep | arXiv:2605.20774v1 | SRC-ARXIV@arXiv:2605.20774v1 | arXiv:2605.20774v1 HTML — §4.1 Algorithms; §Appendix F Training Details | arXiv:2605.20774v1 HTML — §VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models; §3 The VLA-Replica Benchmark; §3.3 Task Suite and Evaluation Protocols | arXiv:2605.20774v1 HTML — §5 Conclusion &amp; Limitation | https://arxiv.org/html/2605.20774v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20774 | complete |
| SF-2026-ARXIV-2605-20798 | RP-9c7d4707084b18af | deep | arXiv:2605.20798v1 | SRC-ARXIV@arXiv:2605.20798v1 | arXiv:2605.20798v1 HTML — §3 Experimental Methodology; §3.1 Methods and taxonomy; §3.2 Training setup | arXiv:2605.20798v1 HTML — §Most Transformer Modifications Still Do Not Transfer at 1–3B: A 2020–2026 Update to Narang et al. (2021) with Downstream Evaluation and a Noise Floor; §3 Experimental Methodology; §3.4 Downstream evaluation suite | arXiv:2605.20798v1 HTML — §6 Discussion; §Limitations | https://arxiv.org/html/2605.20798v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20798 | complete |
| SF-2026-ARXIV-2605-20799 | RP-85d10d3ebe77180b | deep | arXiv:2605.20799v1 | SRC-ARXIV@arXiv:2605.20799v1 | arXiv:2605.20799v1 HTML — §III Overall FLOP Utilization | arXiv:2605.20799v1 HTML — §IV Validation | arXiv:2605.20799v1 HTML — §VI Conclusion and approximation boundary | https://arxiv.org/html/2605.20799v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20799 | complete |
| SF-2026-ARXIV-2605-20833 | RP-142bc0331b3a89e7 | deep | arXiv:2605.20833v1 | SRC-ARXIV@arXiv:2605.20833v1 | arXiv:2605.20833v1 HTML — §3 MemGym : A Memory-Centric Evaluation and Training Framework; §B.1 Agentic Memory Systems (Detailed); §Appendix H MemRM Training Details | arXiv:2605.20833v1 HTML — §3 MemGym : A Memory-Centric Evaluation and Training Framework; §3.3 MemRM as a Lightweight Evaluation Signal; §3.4 Constructed Pipelines for Memory-Grounded Evaluation | arXiv:2605.20833v1 HTML — §5 Conclusion; §Appendix J Discussion, Limitations, and Future Work; §J.1 Discussion | https://arxiv.org/html/2605.20833v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20833 | complete |
| SF-2026-ARXIV-2605-20834 | RP-c390e25cda3f4306 | deep | arXiv:2605.20834v1 | SRC-ARXIV@arXiv:2605.20834v1 | arXiv:2605.20834v1 HTML — §3 Conditional Equivalence and Failure Modes | arXiv:2605.20834v1 HTML — §5 Experiments | arXiv:2605.20834v1 HTML — §6 Conclusion and disclosed assumptions | https://arxiv.org/html/2605.20834v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20834 | complete |
| SF-2026-ARXIV-2605-20863 | RP-8d1b66a79597c3af | deep | arXiv:2605.20863v1 | SRC-ARXIV@arXiv:2605.20863v1 | arXiv:2605.20863v1 HTML — §3 PlexRL Cluster-Level Orchestration | arXiv:2605.20863v1 HTML — §5 Evaluation | arXiv:2605.20863v1 HTML — §6 Conclusion and cluster/workload boundary | https://arxiv.org/html/2605.20863v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20863 | complete |
| SF-2026-ARXIV-2605-20866 | RP-731e444e92f13f54 | deep | arXiv:2605.20866v1 | SRC-ARXIV@arXiv:2605.20866v1 | arXiv:2605.20866v1 HTML — §Local training; §Asynchronous methods | arXiv:2605.20866v1 HTML — §5 Experiments; §Appendix B Additional Experimental Details; §Experimental organization. | arXiv:2605.20866v1 HTML — §6 Conclusion | https://arxiv.org/html/2605.20866v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20866 | complete |
| SF-2026-ARXIV-2605-20868 | RP-e386899285ccd4ec | deep | arXiv:2605.20868v1 | SRC-ARXIV@arXiv:2605.20868v1 | arXiv:2605.20868v1 HTML — §4 Tiered Runtime-Certified Attention | arXiv:2605.20868v1 HTML — §9 Evaluation | arXiv:2605.20868v1 HTML — §11 Limitations | https://arxiv.org/html/2605.20868v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20868 | complete |
| SF-2026-ARXIV-2605-20874 | RP-948a3e279b479e94 | deep | arXiv:2605.20874v1 | SRC-ARXIV@arXiv:2605.20874v1 | arXiv:2605.20874v1 HTML — §3 Policy-as-Code Architecture | arXiv:2605.20874v1 HTML — §4 Demonstration and Evaluation | arXiv:2605.20874v1 HTML — §5 Conclusion and demo-scope boundary | https://arxiv.org/html/2605.20874v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20874 | complete |
| SF-2026-ARXIV-2605-20876 | RP-f12cb7661d1fe76f | deep | arXiv:2605.20876v1 | SRC-ARXIV@arXiv:2605.20876v1 | arXiv:2605.20876v1 HTML — §B.4 Training Compute Details Back to ToC | arXiv:2605.20876v1 HTML — §4 Experiments; §4.1 Experiment Setting; §Benchmarks | arXiv:2605.20876v1 HTML — §6 Conclusion | https://arxiv.org/html/2605.20876v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20876 | complete |
| SF-2026-ARXIV-2605-20923 | RP-588d7d56bc9ab8a8 | deep | arXiv:2605.20923v1 | SRC-ARXIV@arXiv:2605.20923v1 | arXiv:2605.20923v1 HTML — §3 Causal Past Logic | arXiv:2605.20923v1 HTML — §5 Runtime Verification Evaluation | arXiv:2605.20923v1 HTML — §6 Conclusion and workflow-model boundary | https://arxiv.org/html/2605.20923v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20923 | complete |
| SF-2026-ARXIV-2605-20926 | RP-1decbb1055250791 | deep | arXiv:2605.20926v1 | SRC-ARXIV@arXiv:2605.20926v1 | arXiv:2605.20926v1 HTML — §3 MemConflict Framework | arXiv:2605.20926v1 HTML — §4 Experiments | arXiv:2605.20926v1 HTML — §5 Conclusion and benchmark limits | https://arxiv.org/html/2605.20926v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20926 | complete |
| SF-2026-ARXIV-2605-20948 | RP-ee1583478455dd4b | deep | arXiv:2605.20948v1 | SRC-ARXIV@arXiv:2605.20948v1 | arXiv:2605.20948v1 HTML — §Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory; §3 Method; §A.1 Model Architecture and Hyper Parameters | arXiv:2605.20948v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.20948v1 HTML — §5 Conclusion; §Appendix C Limitations & Discussion; §C.1 Limitations | https://arxiv.org/html/2605.20948v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20948 | complete |
| SF-2026-ARXIV-2605-21061 | RP-8ad11b566b9045d4 | deep | arXiv:2605.21061v1 | SRC-ARXIV@arXiv:2605.21061v1 | arXiv:2605.21061v1 HTML — §2.2 Phenomena due to Formulation of Existing VLA; §3 Methods; §Appendix B Architecture Details | arXiv:2605.21061v1 HTML — §4 Experiments; §4.2 Main Experiments; §4.2.1 Experiments on NAVSIM. | arXiv:2605.21061v1 HTML — §5 Conclusion; §Appendix O Limitations and future work. | https://arxiv.org/html/2605.21061v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21061 | complete |
| SF-2026-ARXIV-2605-21100 | RP-7029228c2d8b1821 | deep | arXiv:2605.21100v1 | SRC-ARXIV@arXiv:2605.21100v1 | arXiv:2605.21100v1 HTML — §3 NanoCP Request-Level Context Parallelism | arXiv:2605.21100v1 HTML — §5 Evaluation | arXiv:2605.21100v1 HTML — §6 Conclusion and topology boundary | https://arxiv.org/html/2605.21100v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21100 | complete |
| SF-2026-ARXIV-2605-21103 | RP-005add45222d65d1 | deep | arXiv:2605.21103v1 | SRC-ARXIV@arXiv:2605.21103v1 | arXiv:2605.21103v1 HTML — §2 Typed Tensor Language; §3 Shared-State Factorization | arXiv:2605.21103v1 HTML — §4 Differentiable Programs; §5 Discussion | arXiv:2605.21103v1 HTML — §5 Discussion — formal one-round/shared-state scope | https://arxiv.org/html/2605.21103v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21103 | complete |
| SF-2026-ARXIV-2605-21125 | RP-1567e1e42b8c52ff | deep | arXiv:2605.21125v1 | SRC-ARXIV@arXiv:2605.21125v1 | arXiv:2605.21125v1 HTML — §3 Advantage-Collapse Diagnosis; §4 Mitigation | arXiv:2605.21125v1 HTML — §5 Experiments | arXiv:2605.21125v1 HTML — §6 Conclusion and GRPO-scope boundary | https://arxiv.org/html/2605.21125v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21125 | complete |
| SF-2026-ARXIV-2605-21127 | RP-f87e14d248f9adf4 | deep | arXiv:2605.21127v1 | SRC-ARXIV@arXiv:2605.21127v1 | arXiv:2605.21127v1 HTML — §Tools and frameworks for reasoning models.; §3 Reasoning-Trace Collapse: Definition & Evaluation Framework; §A structural evaluation framework. | arXiv:2605.21127v1 HTML — §3 Reasoning-Trace Collapse: Definition & Evaluation Framework; §A structural evaluation framework.; §4 ThinkPack : Operationalising Structural Reasoning Evaluation | arXiv:2605.21127v1 HTML — §6 Discussion; §7 Limitations; §8 Conclusion | https://arxiv.org/html/2605.21127v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21127 | complete |
| SF-2026-ARXIV-2605-21177 | RP-88ef212b118ef706 | deep | arXiv:2605.21177v1 | SRC-ARXIV@arXiv:2605.21177v1 | arXiv:2605.21177v1 HTML — §3 Method; §3.1 Algorithm Description | arXiv:2605.21177v1 HTML — §Convergence result.; §3.2 BP Time Analysis; §3.3 Memory Consumption Analysis | arXiv:2605.21177v1 HTML — §5 Conclusion; §Appendix H Limitations | https://arxiv.org/html/2605.21177v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21177 | complete |
| SF-2026-ARXIV-2605-21187 | RP-a52f46fbbc594594 | deep | arXiv:2605.21187v1 | SRC-ARXIV@arXiv:2605.21187v1 | arXiv:2605.21187v1 HTML — §III Spectrum-X Multiplane Architecture | arXiv:2605.21187v1 HTML — §IV Evaluation | arXiv:2605.21187v1 HTML — §V Deployment Evidence; §VI Conclusion | https://arxiv.org/html/2605.21187v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21187 | complete |
| SF-2026-ARXIV-2605-21266 | RP-983345b4bc381b18 | deep | arXiv:2605.21266v1 | SRC-ARXIV@arXiv:2605.21266v1 | arXiv:2605.21266v1 HTML — §Iterative and hybrid methods. | arXiv:2605.21266v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.21266v1 HTML — §6 Conclusion; §Appendix B Discussion; §Limitations. | https://arxiv.org/html/2605.21266v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21266 | complete |
| SF-2026-ARXIV-2605-21273 | RP-64ba1d8270158172 | deep | arXiv:2605.21273v1 | SRC-ARXIV@arXiv:2605.21273v1 | arXiv:2605.21273v1 HTML — §3.3 Action-Centric Supervised Training; §Driving Action Alignment Pretraining.; §4.5 Ablation Study of Training Strategy | arXiv:2605.21273v1 HTML — §4 Experiments; §4.1 Experiments Setup; §4.2 Main Results | arXiv:2605.21273v1 HTML — §5 Conclusion | https://arxiv.org/html/2605.21273v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21273 | complete |
| SF-2026-ARXIV-2605-21312 | RP-c21af2f613607f73 | deep | arXiv:2605.21312v1 | SRC-ARXIV@arXiv:2605.21312v1 | arXiv:2605.21312v1 HTML — §3 Frontier Simulator Architecture | arXiv:2605.21312v1 HTML — §5 Fidelity Evaluation | arXiv:2605.21312v1 HTML — §6 Workload Studies; §7 Conclusion | https://arxiv.org/html/2605.21312v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21312 | complete |
| SF-2026-ARXIV-2605-21347 | RP-980999ab4adc0664 | deep | arXiv:2605.21347v1 | SRC-ARXIV@arXiv:2605.21347v1 | arXiv:2605.21347v1 HTML — §Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents; §3.1 System Overview; §A.1 Agent System Prompts | arXiv:2605.21347v1 HTML — §3.6 Iterative Analysis Loop; §4 Evaluation; §A.4 Benchmark and Corpus Statistics | arXiv:2605.21347v1 HTML — §5 Discussion; §5.3 Limitations and Future Work; §6 Conclusion | https://arxiv.org/html/2605.21347v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21347 | complete |
| SF-2026-ARXIV-2605-21384 | RP-bb3f6e4ebda9502c | deep | arXiv:2605.21384v1 | SRC-ARXIV@arXiv:2605.21384v1 | arXiv:2605.21384v1 HTML — §2 Benchmark Design | arXiv:2605.21384v1 HTML — §3 Experiments; §4 Analysis | arXiv:2605.21384v1 HTML — §Appendix A Limitations and Broader Impacts | https://arxiv.org/html/2605.21384v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21384 | complete |
| SF-2026-ARXIV-2605-21392 | RP-3f08b3a9c49df6c5 | deep | arXiv:2605.21392v1 | SRC-ARXIV@arXiv:2605.21392v1 | arXiv:2605.21392v1 HTML — §III VIPER-MCP Taint Analysis | arXiv:2605.21392v1 HTML — §V Evaluation | arXiv:2605.21392v1 HTML — §VII Conclusion; Limitations and Future Work | https://arxiv.org/html/2605.21392v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21392 | complete |
| SF-2026-ARXIV-2605-21427 | RP-ceb8743093ad6661 | deep | arXiv:2605.21427v1 | SRC-ARXIV@arXiv:2605.21427v1 | arXiv:2605.21427v1 HTML — §3 PALS Joint Power/Batch Controller | arXiv:2605.21427v1 HTML — §7 Evaluation | arXiv:2605.21427v1 HTML — §8 Conclusion and GPU/MoE scope | https://arxiv.org/html/2605.21427v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21427 | complete |
| SF-2026-ARXIV-2605-21434 | RP-22dd6d5d62eb118c | deep | arXiv:2605.21434v1 | SRC-ARXIV@arXiv:2605.21434v1 | arXiv:2605.21434v1 HTML — §3 Agent-Propose/Solver-Verify Workflow | arXiv:2605.21434v1 HTML — §5 Evaluation | arXiv:2605.21434v1 HTML — §6 Limitations and bounded-model-checking scope | https://arxiv.org/html/2605.21434v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21434 | complete |
| SF-2026-ARXIV-2605-21446 | RP-d4c180075d355865 | deep | arXiv:2605.21446v1 | SRC-ARXIV@arXiv:2605.21446v1 | arXiv:2605.21446v1 HTML — §3 Controlled Sensor-Perturbation Protocol | arXiv:2605.21446v1 HTML — §4 Experiments | arXiv:2605.21446v1 HTML — §5.1 Limitations | https://arxiv.org/html/2605.21446v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21446 | complete |
| SF-2026-ARXIV-2605-21467 | RP-4c1411d1f5ac5be2 | deep | arXiv:2605.21467v1 | SRC-ARXIV@arXiv:2605.21467v1 | arXiv:2605.21467v1 HTML — §3 Method; §4.3 Training Dynamics; §Use in training. | arXiv:2605.21467v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.21467v1 HTML — §7 Conclusion; §Appendix A Limitations | https://arxiv.org/html/2605.21467v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21467 | complete |
| SF-2026-ARXIV-2605-21468 | RP-d5257297c7654d44 | deep | arXiv:2605.21468v1 | SRC-ARXIV@arXiv:2605.21468v1 | arXiv:2605.21468v1 HTML — §You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories; §3 Method; §Zero training cost. | arXiv:2605.21468v1 HTML — §4 Experiments; §4.1 Experimental Setup; §RLVR training and evaluation. | arXiv:2605.21468v1 HTML — §6 Discussion; §Limitations.; §7 Conclusion | https://arxiv.org/html/2605.21468v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21468 | complete |
| SF-2026-ARXIV-2605-21470 | RP-e8b83a8a4d5c6742 | deep | arXiv:2605.21470v1 | SRC-ARXIV@arXiv:2605.21470v1 | arXiv:2605.21470v1 HTML — §3 Methods | arXiv:2605.21470v1 HTML — §4 Evaluation; §5 Results | arXiv:2605.21470v1 HTML — §6 Limitations | https://arxiv.org/html/2605.21470v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21470 | complete |
| SF-2026-ARXIV-2605-21482 | RP-7c53f8d7522ea5e7 | deep | arXiv:2605.21482v1 | SRC-ARXIV@arXiv:2605.21482v1 | arXiv:2605.21482v1 HTML — §3 DeepWeb-Bench; §3.4 Evaluation Protocol | arXiv:2605.21482v1 HTML — §4 Experiments | arXiv:2605.21482v1 HTML — §Appendix K Limitations | https://arxiv.org/html/2605.21482v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21482 | complete |
| SF-2026-ARXIV-2605-21486 | RP-2f0e0464ce5e4c03 | deep | arXiv:2605.21486v1 | SRC-ARXIV@arXiv:2605.21486v1 | arXiv:2605.21486v1 HTML — §4.1 Methodology; §6 The Effect of Weight Decay and Compute Optimal Training; §H.2 Model Architecture | arXiv:2605.21486v1 HTML — §Appendix A Experimental Details; §H.3 Design Principles for Scaling Analysis | arXiv:2605.21486v1 HTML — §8 Discussion and Conclusion | https://arxiv.org/html/2605.21486v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21486 | complete |
| SF-2026-ARXIV-2605-21543 | RP-240d9ad303a50e90 | deep | arXiv:2605.21543v1 | SRC-ARXIV@arXiv:2605.21543v1 | arXiv:2605.21543v1 HTML — §3 Joint Decontamination Procedure | arXiv:2605.21543v1 HTML — §4 Controlled Experiments | arXiv:2605.21543v1 HTML — §6 Limitations | https://arxiv.org/html/2605.21543v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21543 | complete |
| SF-2026-ARXIV-2605-21602 | RP-5c335c79eba9f41d | deep | arXiv:2605.21602v1 | SRC-ARXIV@arXiv:2605.21602v1 | arXiv:2605.21602v1 HTML — §3 MOOD Benchmark and Monitor Design | arXiv:2605.21602v1 HTML — §5 Experiments | arXiv:2605.21602v1 HTML — §6 Conclusion and stated monitor limitations | https://arxiv.org/html/2605.21602v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21602 | complete |
| SF-2026-ARXIV-2605-21603 | RP-23d10aa259ab99cb | deep | arXiv:2605.21603v1 | SRC-ARXIV@arXiv:2605.21603v1 | arXiv:2605.21603v1 HTML — §3 Programmable Operator Scheduling | arXiv:2605.21603v1 HTML — §5 Evaluation | arXiv:2605.21603v1 HTML — §7 Conclusion and evaluated-hardware boundary | https://arxiv.org/html/2605.21603v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21603 | complete |
| SF-2026-ARXIV-2605-21606 | RP-94d88674b6729336 | deep | arXiv:2605.21606v1 | SRC-ARXIV@arXiv:2605.21606v1 | arXiv:2605.21606v1 HTML — §3 Method; §Appendix F Adaptive-loss template and method comparison; §Appendix G PW-OPSD training pseudocode | arXiv:2605.21606v1 HTML — §4 Experiments; §Evaluation.; §4.2 Main results on Qwen3-4B | arXiv:2605.21606v1 HTML — §5 Conclusion, Limitations, and Future Work | https://arxiv.org/html/2605.21606v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21606 | complete |
| SF-2026-ARXIV-2605-21642 | RP-275b7a7e2d099140 | deep | arXiv:2605.21642v1 | SRC-ARXIV@arXiv:2605.21642v1 | arXiv:2605.21642v1 HTML — §3 Method; §Training objective.; §4.2 Training and implementation details | arXiv:2605.21642v1 HTML — §4 Experiments; §4.1 Task and evaluation protocol; §Depth reasoning benchmark. | arXiv:2605.21642v1 HTML — §5 Discussion | https://arxiv.org/html/2605.21642v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21642 | complete |
| SF-2026-ARXIV-2605-21648 | RP-f266b39ac8de3782 | deep | arXiv:2605.21648v1 | SRC-ARXIV@arXiv:2605.21648v1 | arXiv:2605.21648v1 HTML — §1 Introduction — exact-v1 disclosed mechanism | arXiv:2605.21648v1 HTML — §Appendix D Experimental Details and Additional Figures; §D.2 Dropout Scheduling Experiments | arXiv:2605.21648v1 HTML — §4 Conclusions and further scope for research; §5 Limitations | https://arxiv.org/html/2605.21648v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21648 | complete |
| SF-2026-ARXIV-2605-21649 | RP-b190dea5c29b3ff4 | deep | arXiv:2605.21649v1 | SRC-ARXIV@arXiv:2605.21649v1 | arXiv:2605.21649v1 HTML — §4 EntmaxKV | arXiv:2605.21649v1 HTML — §5 Experiments; §5.1 Approximation Error Analysis | arXiv:2605.21649v1 HTML — §7 Conclusion — exact-v1 workload/model boundary | https://arxiv.org/html/2605.21649v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21649 | complete |
| SF-2026-ARXIV-2605-21768 | RP-54025a8a20fcd5fe | deep | arXiv:2605.21768v1 | SRC-ARXIV@arXiv:2605.21768v1 | arXiv:2605.21768v1 HTML — §2.1 Memory Agent Architectures; §3 Method; §3.1 Problem Formulation: Multi-step Memory Bank Construction | arXiv:2605.21768v1 HTML — §4 Experiments; §4.1 Experiment Setup; §Datasets and Evaluation Metrics. | arXiv:2605.21768v1 HTML — §5 Conclusion; §Appendix D Limitations and Future Work | https://arxiv.org/html/2605.21768v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21768 | complete |
| SF-2026-ARXIV-2605-21779 | RP-fec479e5e05a9e29 | deep | arXiv:2605.21779v1 | SRC-ARXIV@arXiv:2605.21779v1 | arXiv:2605.21779v1 HTML — §3 FuzzingBrain V2 Architecture | arXiv:2605.21779v1 HTML — §5 Evaluation | arXiv:2605.21779v1 HTML — §6.1 Limitations | https://arxiv.org/html/2605.21779v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21779 | complete |
| SF-2026-ARXIV-2605-21800 | RP-c0a3e8251ce537c7 | deep | arXiv:2605.21800v1 | SRC-ARXIV@arXiv:2605.21800v1 | arXiv:2605.21800v1 HTML — §3 stable-worldmodel Platform | arXiv:2605.21800v1 HTML — §4 Case Studies | arXiv:2605.21800v1 HTML — §6 Conclusion and Future Work | https://arxiv.org/html/2605.21800v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21800 | complete |
| SF-2026-ARXIV-2605-21801 | RP-e20f2a7609541c11 | deep | arXiv:2605.21801v1 | SRC-ARXIV@arXiv:2605.21801v1 | arXiv:2605.21801v1 HTML — §E.3 Training Details | arXiv:2605.21801v1 HTML — §4 Experiments; §4.1 Experiment Setup; §4.2 Main Experiment | arXiv:2605.21801v1 HTML — §5 Conclusion; §Conclusion.; §D.8 Discussion: Dataset-dependent Effects | https://arxiv.org/html/2605.21801v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21801 | complete |
| SF-2026-ARXIV-2605-21803 | RP-d1d250ebab119a51 | deep | arXiv:2605.21803v1 | SRC-ARXIV@arXiv:2605.21803v1 | arXiv:2605.21803v1 HTML — §Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws; §Architecture–optimizer interaction.; §3 Methodology | arXiv:2605.21803v1 HTML — §Experimental setup; §Appendix A Experimental Setup; §Appendix C Rényi Effective Rank Analysis: Where Optimizer-Induced Capacity Forms | arXiv:2605.21803v1 HTML — §5 Discussion and Conclusion | https://arxiv.org/html/2605.21803v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21803 | complete |
| SF-2026-ARXIV-2605-21847 | RP-172fe52bc1cab11d | deep | arXiv:2605.21847v1 | SRC-ARXIV@arXiv:2605.21847v1 | arXiv:2605.21847v1 HTML — §3 Component-Level Power Control | arXiv:2605.21847v1 HTML — §6 Evaluation | arXiv:2605.21847v1 HTML — §7 Conclusion and evaluated-GPU boundary | https://arxiv.org/html/2605.21847v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21847 | complete |
| SF-2026-ARXIV-2605-21850 | RP-1b7b40febca5e56b | deep | arXiv:2605.21850v1 | SRC-ARXIV@arXiv:2605.21850v1 | arXiv:2605.21850v1 HTML — §3 Agent-Trajectory Compilation | arXiv:2605.21850v1 HTML — §4 Experiments | arXiv:2605.21850v1 HTML — §6 Limitations and Social Impacts | https://arxiv.org/html/2605.21850v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21850 | complete |
| SF-2026-ARXIV-2605-22882 | RP-edf8a3836d174361 | deep | arXiv:2605.22882v1 | SRC-ARXIV@arXiv:2605.22882v1 | arXiv:2605.22882v1 HTML — §3.1 Problem Formulation; §3.3 Adaptive Inverse Dynamic System | arXiv:2605.22882v1 HTML — §4 Experiments; §Quantitative Experiment; §Qualitative Experiment | arXiv:2605.22882v1 HTML — §5 Conclusion | https://arxiv.org/html/2605.22882v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22882 | complete |
| SF-2026-ARXIV-2605-22883 | RP-200c8aca489405ce | deep | arXiv:2605.22883v1 | SRC-ARXIV@arXiv:2605.22883v1 | arXiv:2605.22883v1 HTML — §4 Energy-per-Successful-Goal Metric | arXiv:2605.22883v1 HTML — §8 Failure-Injection Experiments | arXiv:2605.22883v1 HTML — §10.1 Limitations | https://arxiv.org/html/2605.22883v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22883 | complete |
| SF-2026-ARXIV-2605-22884 | RP-3cfb78fecc04c716 | deep | arXiv:2605.22884v1 | SRC-ARXIV@arXiv:2605.22884v1 | arXiv:2605.22884v1 HTML — §KV cache systems and eviction.; §Training-side considerations.; §Other long-context methods. | arXiv:2605.22884v1 HTML — §4 Experiments; §4.1 Experimental Setup; §Results. | arXiv:2605.22884v1 HTML — §5 Discussion and Limitations; §6 Conclusion | https://arxiv.org/html/2605.22884v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22884 | complete |
| SF-2026-ARXIV-2605-24022 | RP-b37dab8934926779 | deep | arXiv:2605.24022v1 | SRC-ARXIV@arXiv:2605.24022v1 | arXiv:2605.24022v1 HTML — §3 CacheTune Adaptive KV Reuse | arXiv:2605.24022v1 HTML — §5 Evaluation | arXiv:2605.24022v1 HTML — §5.5 Limitations; §6 Conclusion | https://arxiv.org/html/2605.24022v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-24022 | complete |
| SF-2026-ARXIV-2605-26128 | RP-05c52662d53cb2ec | deep | arXiv:2605.26128v1 | SRC-ARXIV@arXiv:2605.26128v1 | arXiv:2605.26128v1 HTML — §2.2 Structured Decoding as a Serving-System Interface | arXiv:2605.26128v1 HTML — §5 Experimental Protocol; §6 Empirical Results; §7.4 What the Result Establishes | arXiv:2605.26128v1 HTML — §7 Discussion; §10 Conclusion | https://arxiv.org/html/2605.26128v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-26128 | complete |
| SF-2026-ARXIV-2605-26132 | RP-e21e2a628b925565 | deep | arXiv:2605.26132v1 | SRC-ARXIV@arXiv:2605.26132v1 | arXiv:2605.26132v1 HTML — §4.5 Training vs. Test-Time Compute; §C.1.2 Training | arXiv:2605.26132v1 HTML — §4 Experiments; §Appendix C Experimental Details; §C.1.3 Evaluation | arXiv:2605.26132v1 HTML — §5 Discussion | https://arxiv.org/html/2605.26132v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-26132 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-20616:start -->
#### Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents

**问题与机制。** Inspired by complementary learning systems theory, we propose Auto-Dreamer, a learned offline consolidator for language-agent memory. 系统 owner=`AGENT-MEMORY`。

**Exact-v1。** Method=`§4 Offline Memory Consolidation`；Evaluation=`§5 Experiments`；Limitations/Counterevidence=`Appendix A Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20616:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20616:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20616:end -->

<!-- review:SF-2026-ARXIV-2605-20630:start -->
#### Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute Pipelines

**问题与机制。** We propose two complementary optimization layers for AOB plan-execute pipelines: a temporal semantic cache and a set of MCP workflow optimizations combining disk-backed tool-discovery caching and dependency-aware parallel step execution. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 Optimization Framework`；Evaluation=`§4 Results`；Limitations/Counterevidence=`§5 Limitations and Failure Modes`。

<!-- claim:SF-2026-ARXIV-2605-20630:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20630:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20630:end -->

<!-- review:SF-2026-ARXIV-2605-20641:start -->
#### Trusted Weights, Treacherous Optimizations? Optimization-Triggered Backdoor Attacks on LLMs

**问题与机制。** We propose a unified optimization-triggered attack framework comprising two complementary strategies. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 Optimization-Triggered Attack Design`；Evaluation=`§4 Implementation and Evaluation`；Limitations/Counterevidence=`Appendix C Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20641:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20641:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20641:end -->

<!-- review:SF-2026-ARXIV-2605-20696:start -->
#### Distributed Direct Preference Optimization

**问题与机制。** For federated DPO, we derive convergence rates that quantify the impact of client drift, communication frequency, and preference heterogeneity; for decentralized DPO, we establish convergence over general communication graphs and show how spectral connectivity governs optimization speed and consensus. 系统 owner=`TRAIN-DPO`。

**Exact-v1。** Method=`§3 Problem Formulation and Preliminaries`；Evaluation=`§7 Numerical Results; §Appendix E Additional Detail for Experimental Setup; §Appendix F Additional Results`；Limitations/Counterevidence=`§8 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20696:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20696:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20696:end -->

<!-- review:SF-2026-ARXIV-2605-20704:start -->
#### Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms

**问题与机制。** We present Heartbeat-Bound Hierarchical Credentials (HBHC), a cryptographic protocol that binds credential validity to periodic parent liveness proofs. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§4.1–§4.6 Heartbeat-Bound Credential Protocol`；Evaluation=`§6 Evaluation`；Limitations/Counterevidence=`§7 Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-20704:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20704:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20704:end -->

<!-- review:SF-2026-ARXIV-2605-20706:start -->
#### Llamas on the Web: Memory-Efficient, Performance-Portable, and Multi-Precision LLM Inference with WebGPU

**问题与机制。** To realize this opportunity, we present Llamas on the Web (LlamaWeb), a WebGPU backend for llama$.$cpp that enables memory-efficient and performance-portable LLM inference across a wide range of model weight formats in the browser. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§3 LlamaWeb Architecture`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§6 Discussion and WebGPU portability boundary`。

<!-- claim:SF-2026-ARXIV-2605-20706:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20706:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20706:end -->

<!-- review:SF-2026-ARXIV-2605-20734:start -->
#### An Application-Layer Multi-Modal Covert-Channel Reference Monitor for LLM Agent Egress

**问题与机制。** A large language model (LLM) agent that sends messages can leak data inside them. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§4 Multi-Modal Reference Monitor`；Evaluation=`§7 Evaluation`；Limitations/Counterevidence=`§8 Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-20734:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20734:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20734:end -->

<!-- review:SF-2026-ARXIV-2605-20744:start -->
#### Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale

**问题与机制。** In this work, we introduce a new evaluation paradigm for measuring reward hacking. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Hack-Verifiable Environment Construction`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§7 Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-20744:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20744:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20744:end -->

<!-- review:SF-2026-ARXIV-2605-20749:start -->
#### The Devil is in the Condition Numbers: Why is GLU Better than non-GLU Structure?

**问题与机制。** In this work, we study GLU by analyzing two-layer networks in the neural tangent kernel (NTK) regime. 系统 owner=`MODEL-FFN`。

**Exact-v1。** Method=`§4 Training Dynamics in the Kernel Regime: From NTK Spectrum to Loss Crossing`；Evaluation=`§3.3 Experimental Verification; §5 Generalization Gap Analysis; §Appendix C Proof of Loss Crossing Results`；Limitations/Counterevidence=`§6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20749:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20749:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20749:end -->

<!-- review:SF-2026-ARXIV-2605-20752:start -->
#### GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation

**问题与机制。** To address this, we propose \textbf{GaussianDream}, a feed-forward 3D Gaussian world-model plug-in. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3 Method; §3.4 GaussianDream Training and Efficient Inference; §Stage I: GaussianDream pretraining.`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §Simulation benchmarks.`；Limitations/Counterevidence=`§5 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20752:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20752:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20752:end -->

<!-- review:SF-2026-ARXIV-2605-20756:start -->
#### Correcting Stochastic Update Bias in Preconditioned Language Model Optimizers

**问题与机制。** We show that this view misses two finite-sample biases. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§5 Proposed method; §7.1 Main pretraining results; §Appendix A Algorithm and instantiations`；Evaluation=`§6 Convergence analysis; §7 Experiments; §7.1 Main pretraining results`；Limitations/Counterevidence=`§8 Limitations; §9 Conclusion; §Appendix C Discussion`。

<!-- claim:SF-2026-ARXIV-2605-20756:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20756:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20756:end -->

<!-- review:SF-2026-ARXIV-2605-20767:start -->
#### The Illusion of Intervention: Your LLM-Simulated Experiment is an Observational Study

**问题与机制。** Large language models (LLMs) show potential as simulators of human behavior, offering a scalable way to study responses to interventions. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Causal Estimands for LLM-Simulated Interventions`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§6 Discussion and observational-study boundary`。

<!-- claim:SF-2026-ARXIV-2605-20767:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20767:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20767:end -->

<!-- review:SF-2026-ARXIV-2605-20774:start -->
#### VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models

**问题与机制。** We introduce VLA-REPLICA, a low-cost, easily reproducible real-world benchmark for evaluating VLA models. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§4.1 Algorithms; §Appendix F Training Details`；Evaluation=`§VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models; §3 The VLA-Replica Benchmark; §3.3 Task Suite and Evaluation Protocols`；Limitations/Counterevidence=`§5 Conclusion &amp; Limitation`。

<!-- claim:SF-2026-ARXIV-2605-20774:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20774:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20774:end -->

<!-- review:SF-2026-ARXIV-2605-20798:start -->
#### Most Transformer Modifications Still Do Not Transfer at 1-3B: A 2020-2026 Update to Narang et al. (2021) with Downstream Evaluation and a Noise Floor

**问题与机制。** Narang et al. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Experimental Methodology; §3.1 Methods and taxonomy; §3.2 Training setup`；Evaluation=`§Most Transformer Modifications Still Do Not Transfer at 1–3B: A 2020–2026 Update to Narang et al. (2021) with Downstream Evaluation and a Noise Floor; §3 Experimental Methodology; §3.4 Downstream evaluation suite`；Limitations/Counterevidence=`§6 Discussion; §Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20798:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20798:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20798:end -->

<!-- review:SF-2026-ARXIV-2605-20799:start -->
#### Instant GPU Efficiency Visibility at Fleet Scale

**问题与机制。** We present Overall FLOP Utilization (OFU), a hardware-level, precision-agnostic GPU efficiency metric for AI workloads on HPC systems, derived from two on-chip performance counters: Tensor Pipe Activity and SM clock frequency. 系统 owner=`PLATFORM-MONITORING`。

**Exact-v1。** Method=`§III Overall FLOP Utilization`；Evaluation=`§IV Validation`；Limitations/Counterevidence=`§VI Conclusion and approximation boundary`。

<!-- claim:SF-2026-ARXIV-2605-20799:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20799:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20799:end -->

<!-- review:SF-2026-ARXIV-2605-20833:start -->
#### MemGym: a Long-Horizon Memory Environment for LLM Agents

**问题与机制。** We present MemGym, a benchmark for agentic memory that unifies existing agent gyms and in-house memory-grounded pipelines behind one memory-reasoning interface. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 MemGym : A Memory-Centric Evaluation and Training Framework; §B.1 Agentic Memory Systems (Detailed); §Appendix H MemRM Training Details`；Evaluation=`§3 MemGym : A Memory-Centric Evaluation and Training Framework; §3.3 MemRM as a Lightweight Evaluation Signal; §3.4 Constructed Pipelines for Memory-Grounded Evaluation`；Limitations/Counterevidence=`§5 Conclusion; §Appendix J Discussion, Limitations, and Future Work; §J.1 Discussion`。

<!-- claim:SF-2026-ARXIV-2605-20833:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20833:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20833:end -->

<!-- review:SF-2026-ARXIV-2605-20834:start -->
#### Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment

**问题与机制。** We characterize when this assumption is violated, show the existence of an undesirable solution space, and prove that DPO and RLHF optimize fundamentally different objectives in such cases. 系统 owner=`TRAIN-DPO`。

**Exact-v1。** Method=`§3 Conditional Equivalence and Failure Modes`；Evaluation=`§5 Experiments`；Limitations/Counterevidence=`§6 Conclusion and disclosed assumptions`。

<!-- claim:SF-2026-ARXIV-2605-20834:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20834:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20834:end -->

<!-- review:SF-2026-ARXIV-2605-20863:start -->
#### PlexRL: Cluster-Level Orchestration of Serviceized LLM Execution for RLVR

**问题与机制。** However, RLVR training is notoriously inefficient: long-tailed rollouts, tool-induced stalls, and asymmetric resource requirements between rollout and training introduce substantial idle time that cannot be eliminated by job-local optimizations such as synchronous pipelining, asynchronous rollout, or colocated execution. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 PlexRL Cluster-Level Orchestration`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§6 Conclusion and cluster/workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-20863:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20863:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20863:end -->

<!-- review:SF-2026-ARXIV-2605-20866:start -->
#### LOSCAR-SGD: Local SGD with Communication-Computation Overlap and Delay-Corrected Sparse Model Averaging

**问题与机制。** We study a heterogeneous-compute setting in which different workers may take different numbers of local steps, and we propose LOSCAR-SGD, a Local SGD method that communicates only a sparse subset of model coordinates and continues optimizing while communication is in flight. 系统 owner=`TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1。** Method=`§Local training; §Asynchronous methods`；Evaluation=`§5 Experiments; §Appendix B Additional Experimental Details; §Experimental organization.`；Limitations/Counterevidence=`§6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20866:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20866:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20866:end -->

<!-- review:SF-2026-ARXIV-2605-20868:start -->
#### Runtime-Certified Bounded-Error Quantized Attention

**问题与机制。** We present a tiered KV cache architecture that enables runtime-certified attention: INT8 keys and INT4 values are stored in GPU memory, while FP16 originals are retained in system RAM for deterministic fallback. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§4 Tiered Runtime-Certified Attention`；Evaluation=`§9 Evaluation`；Limitations/Counterevidence=`§11 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20868:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20868:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20868:end -->

<!-- review:SF-2026-ARXIV-2605-20874:start -->
#### Governance by Construction for Generalist Agents

**问题与机制。** We present a runtime governance architecture that enforces policy interventions at every critical stage of execution. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 Policy-as-Code Architecture`；Evaluation=`§4 Demonstration and Evaluation`；Limitations/Counterevidence=`§5 Conclusion and demo-scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-20874:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20874:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20874:end -->

<!-- review:SF-2026-ARXIV-2605-20876:start -->
#### Terminal-World: Scaling Terminal-Agent Environments via Agent Skills

**问题与机制。** To address these limitations, we introduce Terminal-World, a fully automated pipeline that uses agent skills as the central synthesis primitive, which jointly encode what to accomplish, when to apply (preconditions and environment state), and how to execute, enabling task instructions, environments, and teacher trajectories to be co-derived. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§B.4 Training Compute Details Back to ToC`；Evaluation=`§4 Experiments; §4.1 Experiment Setting; §Benchmarks`；Limitations/Counterevidence=`§6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20876:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20876:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20876:end -->

<!-- review:SF-2026-ARXIV-2605-20923:start -->
#### Causal Past Logic for Runtime Verification of Distributed LLM Agent Workflows

**问题与机制。** Distributed LLM agent workflows should not be monitored as if they produced a single sequential log. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 Causal Past Logic`；Evaluation=`§5 Runtime Verification Evaluation`；Limitations/Counterevidence=`§6 Conclusion and workflow-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-20923:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20923:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20923:end -->

<!-- review:SF-2026-ARXIV-2605-20926:start -->
#### MemConflict: Evaluating Long-Term Memory Systems Under Memory Conflicts

**问题与机制。** To address this gap, we propose MemConflict, a diagnostic framework that treats memory validity as a query-conditioned fitness-for-use problem. 系统 owner=`AGENT-MEMORY`。

**Exact-v1。** Method=`§3 MemConflict Framework`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§5 Conclusion and benchmark limits`。

<!-- claim:SF-2026-ARXIV-2605-20926:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20926:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20926:end -->

<!-- review:SF-2026-ARXIV-2605-20948:start -->
#### Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory

**问题与机制。** We propose Memory Grafting, a conditional memory scaling method that utilizes frozen hidden states from a grafting model as conditional n-gram memory. 系统 owner=`MODEL-MOE`。

**Exact-v1。** Method=`§Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory; §3 Method; §A.1 Model Architecture and Hyper Parameters`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Main Results`；Limitations/Counterevidence=`§5 Conclusion; §Appendix C Limitations & Discussion; §C.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20948:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20948:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20948:end -->

<!-- review:SF-2026-ARXIV-2605-21061:start -->
#### Grounding Driving VLA via Inverse Kinematics

**问题与机制。** We show that trajectory recovery, when viewed through the lens of inverse kinematics, requires both a current and a future visual state as boundary conditions; existing VLAs supply only the former, which encourages the model to shortcut through ego status and text commands alone. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§2.2 Phenomena due to Formulation of Existing VLA; §3 Methods; §Appendix B Architecture Details`；Evaluation=`§4 Experiments; §4.2 Main Experiments; §4.2.1 Experiments on NAVSIM.`；Limitations/Counterevidence=`§5 Conclusion; §Appendix O Limitations and future work.`。

<!-- claim:SF-2026-ARXIV-2605-21061:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21061:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21061:end -->

<!-- review:SF-2026-ARXIV-2605-21100:start -->
#### NanoCP: Request-Level Dynamic Context Parallelism for Data-Expert Parallel Decoding

**问题与机制。** We present \work, which decouples MoE communication from KV cache placement and achieves dual balance through dynamic context parallelism (DCP). 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§3 NanoCP Request-Level Context Parallelism`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§6 Conclusion and topology boundary`。

<!-- claim:SF-2026-ARXIV-2605-21100:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21100:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21100:end -->

<!-- review:SF-2026-ARXIV-2605-21103:start -->
#### A Typed Tensor Language for Federated Learning

**问题与机制。** We introduce a typed tensor language that formalizes this structure. 系统 owner=`TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1。** Method=`§2 Typed Tensor Language; §3 Shared-State Factorization`；Evaluation=`§4 Differentiable Programs; §5 Discussion`；Limitations/Counterevidence=`§5 Discussion — formal one-round/shared-state scope`。

<!-- claim:SF-2026-ARXIV-2605-21103:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21103:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21103:end -->

<!-- review:SF-2026-ARXIV-2605-21125:start -->
#### Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation

**问题与机制。** To address this, we introduce the Advantage Collapse Rate (ACR), the first diagnostic metric quantifying the proportion of training batches with ineffective gradients. 系统 owner=`TRAIN-GRPO`。

**Exact-v1。** Method=`§3 Advantage-Collapse Diagnosis; §4 Mitigation`；Evaluation=`§5 Experiments`；Limitations/Counterevidence=`§6 Conclusion and GRPO-scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-21125:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21125:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21125:end -->

<!-- review:SF-2026-ARXIV-2605-21127:start -->
#### Reasoning-Trace Collapse: Evaluating the Loss of Explicit Reasoning During Fine-Tuning

**问题与机制。** We show that this mismatch can induce reasoning-trace collapse: a fine-tuned model continues to produce plausible final answers while losing the structurally valid explicit reasoning traces that made it a reasoning model in the first place. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§Tools and frameworks for reasoning models.; §3 Reasoning-Trace Collapse: Definition & Evaluation Framework; §A structural evaluation framework.`；Evaluation=`§3 Reasoning-Trace Collapse: Definition & Evaluation Framework; §A structural evaluation framework.; §4 ThinkPack : Operationalising Structural Reasoning Evaluation`；Limitations/Counterevidence=`§6 Discussion; §7 Limitations; §8 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21127:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21127:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21127:end -->

<!-- review:SF-2026-ARXIV-2605-21177:start -->
#### ChunkFT: Byte-Streamed Optimization for Memory-Efficient Full Fine-Tuning

**问题与机制。** The results demonstrate the effectiveness of \textsc{ChunkFT} in memory usage, running time, and optimization quality. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§3 Method; §3.1 Algorithm Description`；Evaluation=`§Convergence result.; §3.2 BP Time Analysis; §3.3 Memory Consumption Analysis`；Limitations/Counterevidence=`§5 Conclusion; §Appendix H Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21177:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21177:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21177:end -->

<!-- review:SF-2026-ARXIV-2605-21187:start -->
#### High-speed Networking for Giga-Scale AI Factories

**问题与机制。** We describe the motivation, design principles, evaluation methodology and performance on state-of-the-art benchmarks, as well as the lessons we learned from deploying and debugging Spectrum-X networks in large-scale systems. 系统 owner=`TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1。** Method=`§III Spectrum-X Multiplane Architecture`；Evaluation=`§IV Evaluation`；Limitations/Counterevidence=`§V Deployment Evidence; §VI Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21187:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21187:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21187:end -->

<!-- review:SF-2026-ARXIV-2605-21266:start -->
#### How Much Online RL is Enough? Informative Rollouts for Offline Preference Optimization in RLVR

**问题与机制。** We introduce G2D (GRPO to DPO)}, a three-stage pipeline that performs a short GRPO warm-up, constructs a static preference dataset, and fine-tunes a model offline with DPO. 系统 owner=`TRAIN-DPO`。

**Exact-v1。** Method=`§Iterative and hybrid methods.`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Main Results`；Limitations/Counterevidence=`§6 Conclusion; §Appendix B Discussion; §Limitations.`。

<!-- claim:SF-2026-ARXIV-2605-21266:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21266:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21266:end -->

<!-- review:SF-2026-ARXIV-2605-21273:start -->
#### DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions

**问题与机制。** Driving Vision-Language-Action Models (Driving VLAs) commonly introduce natural-language reasoning as an intermediate interface for end-to-end planning, but reasoning-centric interfaces face three practical bottlenecks: obtaining high-quality reasoning annotations is difficult, generating and understanding long reasoning chains is challenging for compact models, and inference latency is substantially increased. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§3.3 Action-Centric Supervised Training; §Driving Action Alignment Pretraining.; §4.5 Ablation Study of Training Strategy`；Evaluation=`§4 Experiments; §4.1 Experiments Setup; §4.2 Main Results`；Limitations/Counterevidence=`§5 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21273:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21273:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21273:end -->

<!-- review:SF-2026-ARXIV-2605-21312:start -->
#### Frontier: Towards Comprehensive and Accurate LLM Inference Simulation

**问题与机制。** Simulation is attractive for exploring this growing design space, yet existing simulators lack the architectural completeness and decision-grade fidelity it demands. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§3 Frontier Simulator Architecture`；Evaluation=`§5 Fidelity Evaluation`；Limitations/Counterevidence=`§6 Workload Studies; §7 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21312:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21312:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21312:end -->

<!-- review:SF-2026-ARXIV-2605-21347:start -->
#### Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents

**问题与机制。** We present the Insights Generator (IG), a multi-agent system that answers diagnostic questions by proposing and testing hypotheses across the trace corpus to produce an evidence-backed insights report. 系统 owner=`PLATFORM-TRACE`。

**Exact-v1。** Method=`§Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents; §3.1 System Overview; §A.1 Agent System Prompts`；Evaluation=`§3.6 Iterative Analysis Loop; §4 Evaluation; §A.4 Benchmark and Corpus Statistics`；Limitations/Counterevidence=`§5 Discussion; §5.3 Limitations and Future Work; §6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21347:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21347:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21347:end -->

<!-- review:SF-2026-ARXIV-2605-21384:start -->
#### SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents

**问题与机制。** We study this reward hacking phenomenon by decompose software engineering tasks into three parts: (i) a natural language description of the specification (ii) visible validation tests that exercise specified features in isolation, and (iii) held-out tests that compose those same features to simulate real-world usage. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2 Benchmark Design`；Evaluation=`§3 Experiments; §4 Analysis`；Limitations/Counterevidence=`§Appendix A Limitations and Broader Impacts`。

<!-- claim:SF-2026-ARXIV-2605-21384:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21384:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21384:end -->

<!-- review:SF-2026-ARXIV-2605-21392:start -->
#### VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers

**问题与机制。** In this paper, we present VIPER-MCP, the first end-to-end automated vulnerability auditing framework for MCP servers that not only detects taint-style vulnerabilities but also dynamically confirms their exploitability by producing concrete proof-of-concept prompts. 系统 owner=`AGENT-MCP`。

**Exact-v1。** Method=`§III VIPER-MCP Taint Analysis`；Evaluation=`§V Evaluation`；Limitations/Counterevidence=`§VII Conclusion; Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-21392:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21392:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21392:end -->

<!-- review:SF-2026-ARXIV-2605-21427:start -->
#### PALS: Power-Aware LLM Serving for Mixture-of-Experts Models

**问题与机制。** In this paper, we present a power-aware runtime for LLM serving, PALS, that treats GPU power caps as a first-class control knob and jointly optimizes them with software parameters such as batch size. 系统 owner=`PLATFORM-COST`。

**Exact-v1。** Method=`§3 PALS Joint Power/Batch Controller`；Evaluation=`§7 Evaluation`；Limitations/Counterevidence=`§8 Conclusion and GPU/MoE scope`。

<!-- claim:SF-2026-ARXIV-2605-21427:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21427:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21427:end -->

<!-- review:SF-2026-ARXIV-2605-21434:start -->
#### Agentic Model Checking

**问题与机制。** We propose agentic model checking, a paradigm that couples LLM agents with a bounded model checking backend under the principle agents propose, solvers verify: agents handle tasks requiring semantic judgment (spec inference, check selection, counterexample classification, refinement proposal) while BMC discharges every soundness-relevant decision. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Agent-Propose/Solver-Verify Workflow`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§6 Limitations and bounded-model-checking scope`。

<!-- claim:SF-2026-ARXIV-2605-21434:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21434:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21434:end -->

<!-- review:SF-2026-ARXIV-2605-21446:start -->
#### Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs

**问题与机制。** In this paper we present a controlled perturbation study of Vision-Language-Action (VLA) robustness in autonomous driving, evaluating Alpamayo R1 (10B parameters) across 1,996 scenarios under eight sensor perturbations (Gaussian noise at four intensities, two lighting extremes, and two fog levels; ${\sim}18{,}000$ inference trials). 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§3 Controlled Sensor-Perturbation Protocol`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§5.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21446:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21446:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21446:end -->

<!-- review:SF-2026-ARXIV-2605-21467:start -->
#### DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from Verifiable Rewards

**问题与机制。** We introduce a discriminator view of RLVR updates, showing that the policy-gradient update direction implicitly acts as a linear discriminator over token-gradient vectors and thereby determines which token probabilities are increased or decreased during learning. 系统 owner=`TRAIN-GRPO`。

**Exact-v1。** Method=`§3 Method; §4.3 Training Dynamics; §Use in training.`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Main Results`；Limitations/Counterevidence=`§7 Conclusion; §Appendix A Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21467:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21467:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21467:end -->

<!-- review:SF-2026-ARXIV-2605-21468:start -->
#### You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories

**问题与机制。** In this work, we demonstrate that RLVR weight trajectories are extremely low-rank and highly predictable. 系统 owner=`TRAIN-CHECKPOINT`。

**Exact-v1。** Method=`§You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories; §3 Method; §Zero training cost.`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §RLVR training and evaluation.`；Limitations/Counterevidence=`§6 Discussion; §Limitations.; §7 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21468:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21468:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21468:end -->

<!-- review:SF-2026-ARXIV-2605-21470:start -->
#### Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling

**问题与机制。** We present agent just-in-time (JIT) compilation, a system that compiles task descriptions directly into executable code that may include LLM calls, tool calls, and parallelization. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 Methods`；Evaluation=`§4 Evaluation; §5 Results`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21470:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21470:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21470:end -->

<!-- review:SF-2026-ARXIV-2605-21482:start -->
#### DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation

**问题与机制。** We introduce DeepWeb-Bench, a deep research benchmark that is substantially harder than existing benchmarks for the current frontier. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 DeepWeb-Bench; §3.4 Evaluation Protocol`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§Appendix K Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21482:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21482:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21482:end -->

<!-- review:SF-2026-ARXIV-2605-21486:start -->
#### Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate

**问题与机制。** In this paper, we first develop a framework to quantify hyperparameter transfer through three metrics: (1) the quality of the scaling law fit, (2) the robustness to extrapolation errors, and (3) the asymptotic loss penalty due to choice of parameterization. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§4.1 Methodology; §6 The Effect of Weight Decay and Compute Optimal Training; §H.2 Model Architecture`；Evaluation=`§Appendix A Experimental Details; §H.3 Design Principles for Scaling Analysis`；Limitations/Counterevidence=`§8 Discussion and Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21486:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21486:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21486:end -->

<!-- review:SF-2026-ARXIV-2605-21543:start -->
#### Provable Joint Decontamination for Benchmarking Multiple Large Language Models

**问题与机制。** In this work, we formalize multi-model benchmark decontamination as a joint selection problem and propose Joint Envelope Conformal Selection (JECS), a conformal procedure that enables global contamination rate (GCR) control under stated assumptions. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Joint Decontamination Procedure`；Evaluation=`§4 Controlled Experiments`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21543:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21543:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21543:end -->

<!-- review:SF-2026-ARXIV-2605-21602:start -->
#### Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs

**问题与机制。** We systematically study whether LLM monitoring pipelines can detect these OOD alignment failures by introducing a benchmark called Misalignment Out Of Distribution (MOOD). 系统 owner=`PLATFORM-MONITORING`。

**Exact-v1。** Method=`§3 MOOD Benchmark and Monitor Design`；Evaluation=`§5 Experiments`；Limitations/Counterevidence=`§6 Conclusion and stated monitor limitations`。

<!-- claim:SF-2026-ARXIV-2605-21602:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21602:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21602:end -->

<!-- review:SF-2026-ARXIV-2605-21603:start -->
#### DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling

**问题与机制。** To address this, we propose DynaFlow, a framework that enables the transparent and flexible integration of intra-device parallelism by decoupling the logical model definition from the physical execution schedule. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§3 Programmable Operator Scheduling`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§7 Conclusion and evaluated-hardware boundary`。

<!-- claim:SF-2026-ARXIV-2605-21603:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21603:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21603:end -->

<!-- review:SF-2026-ARXIV-2605-21606:start -->
#### When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning

**问题与机制。** To identify this phenomenon, we introduce a branch-viability diagnostic. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§3 Method; §Appendix F Adaptive-loss template and method comparison; §Appendix G PW-OPSD training pseudocode`；Evaluation=`§4 Experiments; §Evaluation.; §4.2 Main results on Qwen3-4B`；Limitations/Counterevidence=`§5 Conclusion, Limitations, and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-21606:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21606:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21606:end -->

<!-- review:SF-2026-ARXIV-2605-21642:start -->
#### Ablate-to-Validate: Are Vision-Language Models Really Using Continuous Thought Tokens?

**问题与机制。** Vision-language models (VLMs) are increasingly augmented with continuous or latent non-textual tokens intended to support "visual thinking." Despite improved task accuracy, this alone does not show that models actually use these tokens for reasoning -- gains may arise from confounds such as added context length, special-token anchoring, or training-time regularization. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Method; §Training objective.; §4.2 Training and implementation details`；Evaluation=`§4 Experiments; §4.1 Task and evaluation protocol; §Depth reasoning benchmark.`；Limitations/Counterevidence=`§5 Discussion`。

<!-- claim:SF-2026-ARXIV-2605-21642:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21642:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21642:end -->

<!-- review:SF-2026-ARXIV-2605-21648:start -->
#### Dropout Universality: Scaling Laws and Optimal Scheduling at the Edge-of-Chaos

**问题与机制。** We develop a mean-field theory of dropout as a perturbation of critical signal propagation at the edge of chaos, and show that it predicts a simple, no-cost change to standard practice: \emph{front-loaded} dropout schedules cut test loss by \(18\)--\(35\%\) over constant dropout in MLPs and Vision Transformers at fixed budget. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§1 Introduction — exact-v1 disclosed mechanism`；Evaluation=`§Appendix D Experimental Details and Additional Figures; §D.2 Dropout Scheduling Experiments`；Limitations/Counterevidence=`§4 Conclusions and further scope for research; §5 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21648:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21648:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21648:end -->

<!-- review:SF-2026-ARXIV-2605-21649:start -->
#### EntmaxKV: Support-Aware Decoding for Entmax Attention

**问题与机制。** In this work, we introduce EntmaxKV, an entmax-native sparse decoding framework that exploits sparsity before KV pages are loaded. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§4 EntmaxKV`；Evaluation=`§5 Experiments; §5.1 Approximation Error Analysis`；Limitations/Counterevidence=`§7 Conclusion — exact-v1 workload/model boundary`。

<!-- claim:SF-2026-ARXIV-2605-21649:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21649:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21649:end -->

<!-- review:SF-2026-ARXIV-2605-21768:start -->
#### Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents

**问题与机制。** To address this challenge, we introduce Memory-R2, a training framework for long-horizon memory-augmented LLM agents. 系统 owner=`AGENT-MEMORY`。

**Exact-v1。** Method=`§2.1 Memory Agent Architectures; §3 Method; §3.1 Problem Formulation: Multi-step Memory Bank Construction`；Evaluation=`§4 Experiments; §4.1 Experiment Setup; §Datasets and Evaluation Metrics.`；Limitations/Counterevidence=`§5 Conclusion; §Appendix D Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-21768:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21768:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21768:end -->

<!-- review:SF-2026-ARXIV-2605-21779:start -->
#### FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction

**问题与机制。** While Large Language Models (LLMs) show promise for automated vulnerability detection, three key challenges remain. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 FuzzingBrain V2 Architecture`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§6.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21779:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21779:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21779:end -->

<!-- review:SF-2026-ARXIV-2605-21800:start -->
#### stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation

**问题与机制。** We present stable-worldmodel (swm), an open-source platform for standardized and reproducible world modeling research and evaluation. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3 stable-worldmodel Platform`；Evaluation=`§4 Case Studies`；Limitations/Counterevidence=`§6 Conclusion and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-21800:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21800:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21800:end -->

<!-- review:SF-2026-ARXIV-2605-21801:start -->
#### Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization

**问题与机制。** Based on both empirical and theoretical analysis, we identify two critical gaps of current entropy-based estimators: The anisotropic gap and The calibration gap. 系统 owner=`TRAIN-GRPO`。

**Exact-v1。** Method=`§E.3 Training Details`；Evaluation=`§4 Experiments; §4.1 Experiment Setup; §4.2 Main Experiment`；Limitations/Counterevidence=`§5 Conclusion; §Conclusion.; §D.8 Discussion: Dataset-dependent Effects`。

<!-- claim:SF-2026-ARXIV-2605-21801:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21801:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21801:end -->

<!-- review:SF-2026-ARXIV-2605-21803:start -->
#### Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws

**问题与机制。** We show that this assumption misses a fundamental axis of representation scaling: how effectively the optimizer converts added FFN width into utilized spectral capacity. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws; §Architecture–optimizer interaction.; §3 Methodology`；Evaluation=`§Experimental setup; §Appendix A Experimental Setup; §Appendix C Rényi Effective Rank Analysis: Where Optimizer-Induced Capacity Forms`；Limitations/Counterevidence=`§5 Discussion and Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21803:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21803:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21803:end -->

<!-- review:SF-2026-ARXIV-2605-21847:start -->
#### CompPow: A Case for Component-level GPU Power Management

**问题与机制。** We demonstrate for a variety of ML operations and execution patterns, CompPow has the potential to deliver higher energy efficiency (10%) and even improved performance (5%). 系统 owner=`PLATFORM-COST`。

**Exact-v1。** Method=`§3 Component-Level Power Control`；Evaluation=`§6 Evaluation`；Limitations/Counterevidence=`§7 Conclusion and evaluated-GPU boundary`。

<!-- claim:SF-2026-ARXIV-2605-21847:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21847:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21847:end -->

<!-- review:SF-2026-ARXIV-2605-21850:start -->
#### ACC: Compiling Agent Trajectories for Long-Context Training

**问题与机制。** We propose Agent Context Compilation (ACC), which converts trajectories from search, software engineering, and database querying agents into long-context QA pairs that combine the original question with tool responses and environment observations gathered across multiple turns, training the model to answer directly without tool use. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§3 Agent-Trajectory Compilation`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§6 Limitations and Social Impacts`。

<!-- claim:SF-2026-ARXIV-2605-21850:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21850:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21850:end -->

<!-- review:SF-2026-ARXIV-2605-22882:start -->
#### GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation

**问题与机制。** We present GEM-4D, a geometry-grounded video world model that resolves this limitation by injecting dense 4D correspondence supervision distilled from a pretrained geometry foundation model into the video generative backbone during training. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3.1 Problem Formulation; §3.3 Adaptive Inverse Dynamic System`；Evaluation=`§4 Experiments; §Quantitative Experiment; §Qualitative Experiment`；Limitations/Counterevidence=`§5 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-22882:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22882:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22882:end -->

<!-- review:SF-2026-ARXIV-2605-22883:start -->
#### Energy per Successful Goal: Goal-Level Energy Accounting for Agentic AI Systems

**问题与机制。** We present A-LEMS (Agentic LLM Energy Measurement System), a cross-layer measurement framework that redefines the unit of AI energy accounting from energy per inference to Energy per Successful Goal (EpG). 系统 owner=`PLATFORM-COST`。

**Exact-v1。** Method=`§4 Energy-per-Successful-Goal Metric`；Evaluation=`§8 Failure-Injection Experiments`；Limitations/Counterevidence=`§10.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-22883:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22883:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22883:end -->

<!-- review:SF-2026-ARXIV-2605-22884:start -->
#### Tensor Cache: Eviction-conditioned Associative Memory for Transformers

**问题与机制。** We introduce \emph{Tensor Cache}, a two-level cache that pairs sliding-window softmax attention as a first-level cache (L1) with a fixed-size outer-product fast-weight memory as a second-level cache (L2) fed by KV pairs evicted from the window. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§KV cache systems and eviction.; §Training-side considerations.; §Other long-context methods.`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §Results.`；Limitations/Counterevidence=`§5 Discussion and Limitations; §6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-22884:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22884:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22884:end -->

<!-- review:SF-2026-ARXIV-2605-24022:start -->
#### Adaptive KV Cache Reuse for Fast Long-Context LLM Serving

**问题与机制。** Evaluations on mainstream LLMs and long-context tasks show that CacheTune achieves 3.72x-4.86x TTFT speedup and 3.93x-6.21x higher throughput while maintaining generation quality close to full recompute. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§3 CacheTune Adaptive KV Reuse`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§5.5 Limitations; §6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-24022:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-24022:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-24022:end -->

<!-- review:SF-2026-ARXIV-2605-26128:start -->
#### The Constraint Tax: Measuring Validity-Correctness Tradeoffs in Structured Outputs for Small Language Models

**问题与机制。** We show that this assumption is unsafe for small models. 系统 owner=`AGENT-TOOL-CALLING`。

**Exact-v1。** Method=`§2.2 Structured Decoding as a Serving-System Interface`；Evaluation=`§5 Experimental Protocol; §6 Empirical Results; §7.4 What the Result Establishes`；Limitations/Counterevidence=`§7 Discussion; §10 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-26128:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-26128:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-26128:end -->

<!-- review:SF-2026-ARXIV-2605-26132:start -->
#### Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline

**问题与机制。** We study this setting starting only from unlabeled seed questions with no ground-truth solutions, across three reasoning domains: math, science, and coding. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§4.5 Training vs. Test-Time Compute; §C.1.2 Training`；Evaluation=`§4 Experiments; §Appendix C Experimental Details; §C.1.3 Evaluation`；Limitations/Counterevidence=`§5 Discussion`。

<!-- claim:SF-2026-ARXIV-2605-26132:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-26132:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-26132:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-20616 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20616 |
| SF-2026-ARXIV-2605-20630 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20630 |
| SF-2026-ARXIV-2605-20641 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20641 |
| SF-2026-ARXIV-2605-20696 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20696 |
| SF-2026-ARXIV-2605-20704 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20704 |
| SF-2026-ARXIV-2605-20706 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20706 |
| SF-2026-ARXIV-2605-20734 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20734 |
| SF-2026-ARXIV-2605-20744 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20744 |
| SF-2026-ARXIV-2605-20749 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20749 |
| SF-2026-ARXIV-2605-20752 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20752 |
| SF-2026-ARXIV-2605-20756 | score_7_9; forced_review; potential_books_delta | selected | DA-PRECONDITIONER-BIAS-CONTRACT | — | 跨层改变训练或安全控制契约 | analysis:DA-PRECONDITIONER-BIAS-CONTRACT |
| SF-2026-ARXIV-2605-20767 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20767 |
| SF-2026-ARXIV-2605-20774 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20774 |
| SF-2026-ARXIV-2605-20798 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20798 |
| SF-2026-ARXIV-2605-20799 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20799 |
| SF-2026-ARXIV-2605-20833 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20833 |
| SF-2026-ARXIV-2605-20834 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20834 |
| SF-2026-ARXIV-2605-20863 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20863 |
| SF-2026-ARXIV-2605-20866 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20866 |
| SF-2026-ARXIV-2605-20868 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20868 |
| SF-2026-ARXIV-2605-20874 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20874 |
| SF-2026-ARXIV-2605-20876 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20876 |
| SF-2026-ARXIV-2605-20923 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20923 |
| SF-2026-ARXIV-2605-20926 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20926 |
| SF-2026-ARXIV-2605-20948 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20948 |
| SF-2026-ARXIV-2605-21061 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21061 |
| SF-2026-ARXIV-2605-21100 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21100 |
| SF-2026-ARXIV-2605-21103 | score_7_9; forced_review; potential_books_delta | selected | DA-TYPED-FEDERATED-STATE | — | 跨层改变训练或安全控制契约 | analysis:DA-TYPED-FEDERATED-STATE |
| SF-2026-ARXIV-2605-21125 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21125 |
| SF-2026-ARXIV-2605-21127 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21127 |
| SF-2026-ARXIV-2605-21177 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21177 |
| SF-2026-ARXIV-2605-21187 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21187 |
| SF-2026-ARXIV-2605-21266 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21266 |
| SF-2026-ARXIV-2605-21273 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21273 |
| SF-2026-ARXIV-2605-21312 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21312 |
| SF-2026-ARXIV-2605-21347 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21347 |
| SF-2026-ARXIV-2605-21384 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21384 |
| SF-2026-ARXIV-2605-21392 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21392 |
| SF-2026-ARXIV-2605-21427 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21427 |
| SF-2026-ARXIV-2605-21434 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21434 |
| SF-2026-ARXIV-2605-21446 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21446 |
| SF-2026-ARXIV-2605-21467 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21467 |
| SF-2026-ARXIV-2605-21468 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21468 |
| SF-2026-ARXIV-2605-21470 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21470 |
| SF-2026-ARXIV-2605-21482 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21482 |
| SF-2026-ARXIV-2605-21486 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21486 |
| SF-2026-ARXIV-2605-21543 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21543 |
| SF-2026-ARXIV-2605-21602 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21602 |
| SF-2026-ARXIV-2605-21603 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21603 |
| SF-2026-ARXIV-2605-21606 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21606 |
| SF-2026-ARXIV-2605-21642 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21642 |
| SF-2026-ARXIV-2605-21648 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21648 |
| SF-2026-ARXIV-2605-21649 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21649 |
| SF-2026-ARXIV-2605-21768 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21768 |
| SF-2026-ARXIV-2605-21779 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21779 |
| SF-2026-ARXIV-2605-21800 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21800 |
| SF-2026-ARXIV-2605-21801 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21801 |
| SF-2026-ARXIV-2605-21803 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21803 |
| SF-2026-ARXIV-2605-21847 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21847 |
| SF-2026-ARXIV-2605-21850 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-21850 |
| SF-2026-ARXIV-2605-22882 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-22882 |
| SF-2026-ARXIV-2605-22883 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-22883 |
| SF-2026-ARXIV-2605-22884 | score_7_9; forced_review; potential_books_delta | selected | DA-EVICTED-KV-STATE | — | 跨层改变训练或安全控制契约 | analysis:DA-EVICTED-KV-STATE |
| SF-2026-ARXIV-2605-24022 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24022 |
| SF-2026-ARXIV-2605-26128 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-26128 |
| SF-2026-ARXIV-2605-26132 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-26132 |

<!-- analysis:DA-PRECONDITIONER-BIAS-CONTRACT:start -->
### DA-PRECONDITIONER-BIAS-CONTRACT

把 stochastic preconditioner 直接当 population update 的旧路径简单且复用既有 optimizer state，但 gradient 与 preconditioner 来自同一 minibatch 会产生 coupling bias，inverse/inverse-root 的非线性又会把无偏统计量变成有偏更新。cross-fitted microbatch groups 分离 numerator 与 preconditioner，variance correction 再减去领先 inversion bias；收益是让 update 更接近声明的 population operator，代价是 microbatch 切分、方差估计、额外 state 与更复杂的数值稳定性。证据只覆盖 Qwen2.5-0.5B 与论文 AdamW/Sophia/Shampoo 设置，不能外推 frontier-scale 通用收益；batch 足够大、bias 低于噪声或额外估计不稳定时，原 optimizer 仍是合理 fallback。
<!-- analysis:DA-PRECONDITIONER-BIAS-CONTRACT:end -->

<!-- analysis:DA-TYPED-FEDERATED-STATE:start -->
### DA-TYPED-FEDERATED-STATE

把 federated learning 表达成一组协议在实现上直接，却隐藏了哪些 tensor 仍是 client-local、哪些 state 已可全局 merge。typed tensor language 将 record axis、federated/shared identity 与 encode→merge→decode factorization 纳入类型语义；收益是让通信和跨轮状态可证明，代价是表达能力受可分解 shared state 限制，复杂交互仍需更一般协议。
<!-- analysis:DA-TYPED-FEDERATED-STATE:end -->

<!-- analysis:DA-EVICTED-KV-STATE:start -->
### DA-EVICTED-KV-STATE

固定 sliding window 的旧路径把显存设为硬上限，执行简单且 recent-token attention 精确，但窗口外证据永久丢失。Tensor Cache 保留 exact L1 window，并把 evicted KV 逐 token 写入固定大小 outer-product fast-weight L2，future query 以一次矩阵乘读取，再由 learned gate 合并两路输出；它把 eviction 从删除改为有损状态转写，代价是 decay/write/gate 训练、矩阵状态漂移和额外读写。chunked-mean shortcut 会产生跨 token 伪 outer products，因此 parallel weighted-sum scan、float32 误差与写入顺序必须成为 cache contract；超出校准域、L2 污染或模型不支持时回退 exact window/full KV。
<!-- analysis:DA-EVICTED-KV-STATE:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20616:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20616:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20630:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20630:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20641:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20641:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20696:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20696:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20704:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20704:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20706:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20706:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20734:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20734:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20744:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20744:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20749:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20749:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20752:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20752:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20767:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20767:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20774:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20774:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20798:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20798:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20799:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20799:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20833:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20833:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20834:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20834:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20863:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20863:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20866:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20866:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20868:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20868:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20874:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20874:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20876:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20876:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20923:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20923:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20926:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20926:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20948:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20948:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21061:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21061:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21100:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21100:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21125:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21125:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21127:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21127:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21177:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21177:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21187:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21187:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21266:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21266:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21273:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21273:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21312:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21312:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21347:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21347:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21384:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21384:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21392:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21392:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21427:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21427:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21434:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21434:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21446:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21446:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21467:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21467:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21468:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21468:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21470:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21470:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21482:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21482:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21486:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21486:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21543:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21543:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21602:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21602:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21603:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21603:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21606:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21606:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21642:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21642:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21648:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21648:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21649:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21649:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21768:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21768:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21779:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21779:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21800:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21800:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21801:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21801:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21803:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21803:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21847:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21847:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21850:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-21850:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-22882:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-22882:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-22883:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-22883:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24022:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-24022:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-26128:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-26128:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-26132:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-26132:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-20616 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-20616 | delta:SF-2026-ARXIV-2605-20616 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20616 |
| SF-2026-ARXIV-2605-20630 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-20630 | delta:SF-2026-ARXIV-2605-20630 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20630 |
| SF-2026-ARXIV-2605-20641 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-20641 | delta:SF-2026-ARXIV-2605-20641 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20641 |
| SF-2026-ARXIV-2605-20696 | TRAIN-DPO | books/part-04-training-system/34-dpo.md#chapter-34 | books/part-04-training-system/33-grpo.md#chapter-33;books/part-04-training-system/35-checkpoint.md#chapter-35 | existing:SF-2026-ARXIV-2605-20696 | delta:SF-2026-ARXIV-2605-20696 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20696 |
| SF-2026-ARXIV-2605-20704 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20704 | delta:SF-2026-ARXIV-2605-20704 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20704 |
| SF-2026-ARXIV-2605-20706 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-20706 | delta:SF-2026-ARXIV-2605-20706 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20706 |
| SF-2026-ARXIV-2605-20734 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-20734 | delta:SF-2026-ARXIV-2605-20734 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20734 |
| SF-2026-ARXIV-2605-20744 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20744 | delta:SF-2026-ARXIV-2605-20744 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20744 |
| SF-2026-ARXIV-2605-20749 | MODEL-FFN | books/part-02-model/16-feed-forward-mlp.md#chapter-16 | books/part-02-model/15-multi-head-attention.md#chapter-15;books/part-02-model/17-transformer-layer.md#chapter-17 | existing:SF-2026-ARXIV-2605-20749 | delta:SF-2026-ARXIV-2605-20749 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20749 |
| SF-2026-ARXIV-2605-20752 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-20752 | delta:SF-2026-ARXIV-2605-20752 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20752 |
| SF-2026-ARXIV-2605-20756 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-20756 | delta:SF-2026-ARXIV-2605-20756 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20756 |
| SF-2026-ARXIV-2605-20767 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20767 | delta:SF-2026-ARXIV-2605-20767 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20767 |
| SF-2026-ARXIV-2605-20774 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20774 | delta:SF-2026-ARXIV-2605-20774 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20774 |
| SF-2026-ARXIV-2605-20798 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20798 | delta:SF-2026-ARXIV-2605-20798 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20798 |
| SF-2026-ARXIV-2605-20799 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-20799 | delta:SF-2026-ARXIV-2605-20799 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20799 |
| SF-2026-ARXIV-2605-20833 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20833 | delta:SF-2026-ARXIV-2605-20833 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20833 |
| SF-2026-ARXIV-2605-20834 | TRAIN-DPO | books/part-04-training-system/34-dpo.md#chapter-34 | books/part-04-training-system/33-grpo.md#chapter-33;books/part-04-training-system/35-checkpoint.md#chapter-35 | existing:SF-2026-ARXIV-2605-20834 | delta:SF-2026-ARXIV-2605-20834 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20834 |
| SF-2026-ARXIV-2605-20863 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-20863 | delta:SF-2026-ARXIV-2605-20863 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20863 |
| SF-2026-ARXIV-2605-20866 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-20866 | delta:SF-2026-ARXIV-2605-20866 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20866 |
| SF-2026-ARXIV-2605-20868 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-20868 | delta:SF-2026-ARXIV-2605-20868 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20868 |
| SF-2026-ARXIV-2605-20874 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20874 | delta:SF-2026-ARXIV-2605-20874 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20874 |
| SF-2026-ARXIV-2605-20876 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-20876 | delta:SF-2026-ARXIV-2605-20876 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20876 |
| SF-2026-ARXIV-2605-20923 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-20923 | delta:SF-2026-ARXIV-2605-20923 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20923 |
| SF-2026-ARXIV-2605-20926 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-20926 | delta:SF-2026-ARXIV-2605-20926 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20926 |
| SF-2026-ARXIV-2605-20948 | MODEL-MOE | books/part-02-model/21-moe.md#chapter-21 | books/part-02-model/20-sampling.md#chapter-20;books/part-02-model/22-long-context.md#chapter-22 | existing:SF-2026-ARXIV-2605-20948 | delta:SF-2026-ARXIV-2605-20948 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20948 |
| SF-2026-ARXIV-2605-21061 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-21061 | delta:SF-2026-ARXIV-2605-21061 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21061 |
| SF-2026-ARXIV-2605-21100 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-21100 | delta:SF-2026-ARXIV-2605-21100 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21100 |
| SF-2026-ARXIV-2605-21103 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-21103 | delta:SF-2026-ARXIV-2605-21103 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21103 |
| SF-2026-ARXIV-2605-21125 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-21125 | delta:SF-2026-ARXIV-2605-21125 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21125 |
| SF-2026-ARXIV-2605-21127 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-21127 | delta:SF-2026-ARXIV-2605-21127 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21127 |
| SF-2026-ARXIV-2605-21177 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-21177 | delta:SF-2026-ARXIV-2605-21177 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21177 |
| SF-2026-ARXIV-2605-21187 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-21187 | delta:SF-2026-ARXIV-2605-21187 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21187 |
| SF-2026-ARXIV-2605-21266 | TRAIN-DPO | books/part-04-training-system/34-dpo.md#chapter-34 | books/part-04-training-system/33-grpo.md#chapter-33;books/part-04-training-system/35-checkpoint.md#chapter-35 | existing:SF-2026-ARXIV-2605-21266 | delta:SF-2026-ARXIV-2605-21266 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21266 |
| SF-2026-ARXIV-2605-21273 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-21273 | delta:SF-2026-ARXIV-2605-21273 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21273 |
| SF-2026-ARXIV-2605-21312 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-21312 | delta:SF-2026-ARXIV-2605-21312 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21312 |
| SF-2026-ARXIV-2605-21347 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#chapter-69 | books/part-06-ai-infrastructure/68-logging.md#chapter-68;books/part-06-ai-infrastructure/70-cost.md#chapter-70 | existing:SF-2026-ARXIV-2605-21347 | delta:SF-2026-ARXIV-2605-21347 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21347 |
| SF-2026-ARXIV-2605-21384 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-21384 | delta:SF-2026-ARXIV-2605-21384 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21384 |
| SF-2026-ARXIV-2605-21392 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82;books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-21392 | delta:SF-2026-ARXIV-2605-21392 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21392 |
| SF-2026-ARXIV-2605-21427 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69;books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605-21427 | delta:SF-2026-ARXIV-2605-21427 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21427 |
| SF-2026-ARXIV-2605-21434 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-21434 | delta:SF-2026-ARXIV-2605-21434 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21434 |
| SF-2026-ARXIV-2605-21446 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-21446 | delta:SF-2026-ARXIV-2605-21446 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21446 |
| SF-2026-ARXIV-2605-21467 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-21467 | delta:SF-2026-ARXIV-2605-21467 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21467 |
| SF-2026-ARXIV-2605-21468 | TRAIN-CHECKPOINT | books/part-04-training-system/35-checkpoint.md#chapter-35 | books/part-04-training-system/34-dpo.md#chapter-34;books/part-04-training-system/36-distributed-training.md#chapter-36 | existing:SF-2026-ARXIV-2605-21468 | delta:SF-2026-ARXIV-2605-21468 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21468 |
| SF-2026-ARXIV-2605-21470 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-21470 | delta:SF-2026-ARXIV-2605-21470 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21470 |
| SF-2026-ARXIV-2605-21482 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-21482 | delta:SF-2026-ARXIV-2605-21482 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21482 |
| SF-2026-ARXIV-2605-21486 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-21486 | delta:SF-2026-ARXIV-2605-21486 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21486 |
| SF-2026-ARXIV-2605-21543 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-21543 | delta:SF-2026-ARXIV-2605-21543 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21543 |
| SF-2026-ARXIV-2605-21602 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-21602 | delta:SF-2026-ARXIV-2605-21602 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21602 |
| SF-2026-ARXIV-2605-21603 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-21603 | delta:SF-2026-ARXIV-2605-21603 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21603 |
| SF-2026-ARXIV-2605-21606 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-21606 | delta:SF-2026-ARXIV-2605-21606 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21606 |
| SF-2026-ARXIV-2605-21642 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-21642 | delta:SF-2026-ARXIV-2605-21642 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21642 |
| SF-2026-ARXIV-2605-21648 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-21648 | delta:SF-2026-ARXIV-2605-21648 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21648 |
| SF-2026-ARXIV-2605-21649 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-21649 | delta:SF-2026-ARXIV-2605-21649 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21649 |
| SF-2026-ARXIV-2605-21768 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-21768 | delta:SF-2026-ARXIV-2605-21768 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21768 |
| SF-2026-ARXIV-2605-21779 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-21779 | delta:SF-2026-ARXIV-2605-21779 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21779 |
| SF-2026-ARXIV-2605-21800 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-21800 | delta:SF-2026-ARXIV-2605-21800 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21800 |
| SF-2026-ARXIV-2605-21801 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-21801 | delta:SF-2026-ARXIV-2605-21801 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21801 |
| SF-2026-ARXIV-2605-21803 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-21803 | delta:SF-2026-ARXIV-2605-21803 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21803 |
| SF-2026-ARXIV-2605-21847 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69;books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605-21847 | delta:SF-2026-ARXIV-2605-21847 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21847 |
| SF-2026-ARXIV-2605-21850 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-21850 | delta:SF-2026-ARXIV-2605-21850 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21850 |
| SF-2026-ARXIV-2605-22882 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-22882 | delta:SF-2026-ARXIV-2605-22882 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22882 |
| SF-2026-ARXIV-2605-22883 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69;books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605-22883 | delta:SF-2026-ARXIV-2605-22883 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22883 |
| SF-2026-ARXIV-2605-22884 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-22884 | delta:SF-2026-ARXIV-2605-22884 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22884 |
| SF-2026-ARXIV-2605-24022 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-24022 | delta:SF-2026-ARXIV-2605-24022 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24022 |
| SF-2026-ARXIV-2605-26128 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-26128 | delta:SF-2026-ARXIV-2605-26128 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26128 |
| SF-2026-ARXIV-2605-26132 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-26132 | delta:SF-2026-ARXIV-2605-26132 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26132 |
<!-- books-review:SF-2026-ARXIV-2605-20616:start -->
<!-- existing:SF-2026-ARXIV-2605-20616:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。第77章已明确 memory admission、credit、provenance、transaction、rollback 与派生状态不能获得事实权威。`Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents` 的 source-specific 机制是：Inspired by complementary learning systems theory, we propose Auto-Dreamer, a learned offline consolidator for language-agent memory.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20616:end -->
<!-- delta:SF-2026-ARXIV-2605-20616:start -->Inspired by complementary learning systems theory, we propose Auto-Dreamer, a learned offline consolidator for language-agent memory.<!-- delta:SF-2026-ARXIV-2605-20616:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20616:end -->
<!-- books-review:SF-2026-ARXIV-2605-20630:start -->
<!-- existing:SF-2026-ARXIV-2605-20630:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']。第81章已拥有 versioned DAG、durable state、parallel commit、编译式 procedure 与 recovery contract。`Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute Pipelines` 的 source-specific 机制是：We propose two complementary optimization layers for AOB plan-execute pipelines: a temporal semantic cache and a set of MCP workflow optimizations combining disk-backed tool-discovery caching and dependency-aware parallel step execution.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20630:end -->
<!-- delta:SF-2026-ARXIV-2605-20630:start -->We propose two complementary optimization layers for AOB plan-execute pipelines: a temporal semantic cache and a set of MCP workflow optimizations combining disk-backed tool-discovery caching and dependency-aware parallel step execution.<!-- delta:SF-2026-ARXIV-2605-20630:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20630:end -->
<!-- books-review:SF-2026-ARXIV-2605-20641:start -->
<!-- existing:SF-2026-ARXIV-2605-20641:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。第72章已拥有 supply-chain、runtime optimization、taint、bounded verification、exploit evidence 与 fail-closed authority；但 `Trusted Weights, Treacherous Optimizations? Optimization-Triggered Backdoor Attacks on LLMs` 所暴露的以下缺口尚未显式进入正文：把可信 base weights 之后的量化、剪枝或其他 optimization pass 视为新的 security revision；optimizer/serving pipeline 只能提出变换，独立 integrity gate 比较优化前后触发行为并拥有发布权。<!-- existing:SF-2026-ARXIV-2605-20641:end -->
<!-- delta:SF-2026-ARXIV-2605-20641:start -->把可信 base weights 之后的量化、剪枝或其他 optimization pass 视为新的 security revision；optimizer/serving pipeline 只能提出变换，独立 integrity gate 比较优化前后触发行为并拥有发布权。<!-- delta:SF-2026-ARXIV-2605-20641:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20641:end -->
<!-- books-review:SF-2026-ARXIV-2605-20696:start -->
<!-- existing:SF-2026-ARXIV-2605-20696:start -->已顺读 `books/part-04-training-system/34-dpo.md` 与相邻章节 ['books/part-04-training-system/33-grpo.md', 'books/part-04-training-system/35-checkpoint.md']。第34章已拥有离线 pair objective、reference/beta/data coverage 与 online RL fallback，但尚未完整承载 federated/decentralized DPO 或最小 online warm-up 到 offline DPO 的 handoff；但 `Distributed Direct Preference Optimization` 所暴露的以下缺口尚未显式进入正文：DPO 进入 federated/decentralized topology 后，client preference distribution、reference/policy revision、local drift、communication round 与 graph connectivity 共同构成 objective/run identity；聚合不再只是搬运普通梯度。<!-- existing:SF-2026-ARXIV-2605-20696:end -->
<!-- delta:SF-2026-ARXIV-2605-20696:start -->DPO 进入 federated/decentralized topology 后，client preference distribution、reference/policy revision、local drift、communication round 与 graph connectivity 共同构成 objective/run identity；聚合不再只是搬运普通梯度。<!-- delta:SF-2026-ARXIV-2605-20696:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20696:end -->
<!-- books-review:SF-2026-ARXIV-2605-20704:start -->
<!-- existing:SF-2026-ARXIV-2605-20704:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']。第84章已拥有 Agent runtime 的 credential、policy、lifecycle 与 commit authority。`Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms` 的 source-specific 机制是：We present Heartbeat-Bound Hierarchical Credentials (HBHC), a cryptographic protocol that binds credential validity to periodic parent liveness proofs.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20704:end -->
<!-- delta:SF-2026-ARXIV-2605-20704:start -->We present Heartbeat-Bound Hierarchical Credentials (HBHC), a cryptographic protocol that binds credential validity to periodic parent liveness proofs.<!-- delta:SF-2026-ARXIV-2605-20704:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20704:end -->
<!-- books-review:SF-2026-ARXIV-2605-20706:start -->
<!-- existing:SF-2026-ARXIV-2605-20706:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']。第49章已把 logical graph、physical execution plan、operator schedule 与 hardware control state 分离。`Llamas on the Web: Memory-Efficient, Performance-Portable, and Multi-Precision LLM Inference with WebGPU` 的 source-specific 机制是：To realize this opportunity, we present Llamas on the Web (LlamaWeb), a WebGPU backend for llama$.$cpp that enables memory-efficient and performance-portable LLM inference across a wide range of model weight formats in the browser.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20706:end -->
<!-- delta:SF-2026-ARXIV-2605-20706:start -->To realize this opportunity, we present Llamas on the Web (LlamaWeb), a WebGPU backend for llama$.$cpp that enables memory-efficient and performance-portable LLM inference across a wide range of model weight formats in the browser.<!-- delta:SF-2026-ARXIV-2605-20706:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20706:end -->
<!-- books-review:SF-2026-ARXIV-2605-20734:start -->
<!-- existing:SF-2026-ARXIV-2605-20734:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。第72章已拥有 supply-chain、runtime optimization、taint、bounded verification、exploit evidence 与 fail-closed authority。`An Application-Layer Multi-Modal Covert-Channel Reference Monitor for LLM Agent Egress` 的 source-specific 机制是：A large language model (LLM) agent that sends messages can leak data inside them.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20734:end -->
<!-- delta:SF-2026-ARXIV-2605-20734:start -->A large language model (LLM) agent that sends messages can leak data inside them.<!-- delta:SF-2026-ARXIV-2605-20734:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20734:end -->
<!-- books-review:SF-2026-ARXIV-2605-20744:start -->
<!-- existing:SF-2026-ARXIV-2605-20744:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale` 的 source-specific 机制是：In this work, we introduce a new evaluation paradigm for measuring reward hacking.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20744:end -->
<!-- delta:SF-2026-ARXIV-2605-20744:start -->In this work, we introduce a new evaluation paradigm for measuring reward hacking.<!-- delta:SF-2026-ARXIV-2605-20744:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20744:end -->
<!-- books-review:SF-2026-ARXIV-2605-20749:start -->
<!-- existing:SF-2026-ARXIV-2605-20749:start -->已顺读 `books/part-02-model/16-feed-forward-mlp.md` 与相邻章节 ['books/part-02-model/15-multi-head-attention.md', 'books/part-02-model/17-transformer-layer.md']。第16章已解释 GLU/SwiGLU 的内容分支、gate 分支、预算与 kernel 边界，但没有解释 conditioning 为何可能改变可训练性；但 `The Devil is in the Condition Numbers: Why is GLU Better than non-GLU Structure?` 所暴露的以下缺口尚未显式进入正文：GLU 的收益不能只描述为多一个 gate；两分支乘法改变局部 kernel/conditioning，使训练可达性与非 gated FFN 不同，同时保留 NTK、两层网络和作者规模的证据边界。<!-- existing:SF-2026-ARXIV-2605-20749:end -->
<!-- delta:SF-2026-ARXIV-2605-20749:start -->GLU 的收益不能只描述为多一个 gate；两分支乘法改变局部 kernel/conditioning，使训练可达性与非 gated FFN 不同，同时保留 NTK、两层网络和作者规模的证据边界。<!-- delta:SF-2026-ARXIV-2605-20749:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20749:end -->
<!-- books-review:SF-2026-ARXIV-2605-20752:start -->
<!-- existing:SF-2026-ARXIV-2605-20752:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。第25章已覆盖 projective 4D predictive state、geometry-motion consistency、action-conditioned transition 与真实观测回滚。`GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation` 的 source-specific 机制是：To address this, we propose \textbf{GaussianDream}, a feed-forward 3D Gaussian world-model plug-in.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20752:end -->
<!-- delta:SF-2026-ARXIV-2605-20752:start -->To address this, we propose \textbf{GaussianDream}, a feed-forward 3D Gaussian world-model plug-in.<!-- delta:SF-2026-ARXIV-2605-20752:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20752:end -->
<!-- books-review:SF-2026-ARXIV-2605-20756:start -->
<!-- existing:SF-2026-ARXIV-2605-20756:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。第28章已覆盖 parameterization、preconditioner geometry、layer-wise LR、noise floor、spectral diagnostics 与训练稳定性，但尚未写明同批 gradient/preconditioner 的两类有限样本偏差；但 `Correcting Stochastic Update Bias in Preconditioned Language Model Optimizers` 所暴露的以下缺口尚未显式进入正文：preconditioner 与 gradient 来自同一 minibatch 会产生 coupling bias，非线性 inverse/root 即使输入估计无偏也会产生 inversion bias；cross-fit 与 variance correction 改变 microbatch/state 账本并增加估计成本。<!-- existing:SF-2026-ARXIV-2605-20756:end -->
<!-- delta:SF-2026-ARXIV-2605-20756:start -->preconditioner 与 gradient 来自同一 minibatch 会产生 coupling bias，非线性 inverse/root 即使输入估计无偏也会产生 inversion bias；cross-fit 与 variance correction 改变 microbatch/state 账本并增加估计成本。<!-- delta:SF-2026-ARXIV-2605-20756:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20756:end -->
<!-- books-review:SF-2026-ARXIV-2605-20767:start -->
<!-- existing:SF-2026-ARXIV-2605-20767:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`The Illusion of Intervention: Your LLM-Simulated Experiment is an Observational Study` 的 source-specific 机制是：Large language models (LLMs) show potential as simulators of human behavior, offering a scalable way to study responses to interventions.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20767:end -->
<!-- delta:SF-2026-ARXIV-2605-20767:start -->Large language models (LLMs) show potential as simulators of human behavior, offering a scalable way to study responses to interventions.<!-- delta:SF-2026-ARXIV-2605-20767:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20767:end -->
<!-- books-review:SF-2026-ARXIV-2605-20774:start -->
<!-- existing:SF-2026-ARXIV-2605-20774:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models` 的 source-specific 机制是：We introduce VLA-REPLICA, a low-cost, easily reproducible real-world benchmark for evaluating VLA models.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20774:end -->
<!-- delta:SF-2026-ARXIV-2605-20774:start -->We introduce VLA-REPLICA, a low-cost, easily reproducible real-world benchmark for evaluating VLA models.<!-- delta:SF-2026-ARXIV-2605-20774:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20774:end -->
<!-- books-review:SF-2026-ARXIV-2605-20798:start -->
<!-- existing:SF-2026-ARXIV-2605-20798:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`Most Transformer Modifications Still Do Not Transfer at 1-3B: A 2020-2026 Update to Narang et al. (2021) with Downstream Evaluation and a Noise Floor` 的 source-specific 机制是：Narang et al.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20798:end -->
<!-- delta:SF-2026-ARXIV-2605-20798:start -->Narang et al.<!-- delta:SF-2026-ARXIV-2605-20798:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20798:end -->
<!-- books-review:SF-2026-ARXIV-2605-20799:start -->
<!-- existing:SF-2026-ARXIV-2605-20799:start -->已顺读 `books/part-06-ai-infrastructure/67-monitoring.md` 与相邻章节 ['books/part-06-ai-infrastructure/66-evaluation-system.md', 'books/part-06-ai-infrastructure/68-logging.md']。第67章已区分 raw utilization、有效进展、sensor/health/attestation、漂移与独立 red-team；但 `Instant GPU Efficiency Visibility at Fleet Scale` 所暴露的以下缺口尚未显式进入正文：GPU busy 之外增加 precision-agnostic counter-derived FLOP-progress sensor，并把 counter mapping、clock、kernel coverage 与 calibration revision 纳入 metric identity；它仍不能单独证明 useful work 或 SLO。<!-- existing:SF-2026-ARXIV-2605-20799:end -->
<!-- delta:SF-2026-ARXIV-2605-20799:start -->GPU busy 之外增加 precision-agnostic counter-derived FLOP-progress sensor，并把 counter mapping、clock、kernel coverage 与 calibration revision 纳入 metric identity；它仍不能单独证明 useful work 或 SLO。<!-- delta:SF-2026-ARXIV-2605-20799:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20799:end -->
<!-- books-review:SF-2026-ARXIV-2605-20833:start -->
<!-- existing:SF-2026-ARXIV-2605-20833:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`MemGym: a Long-Horizon Memory Environment for LLM Agents` 的 source-specific 机制是：We present MemGym, a benchmark for agentic memory that unifies existing agent gyms and in-house memory-grounded pipelines behind one memory-reasoning interface.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20833:end -->
<!-- delta:SF-2026-ARXIV-2605-20833:start -->We present MemGym, a benchmark for agentic memory that unifies existing agent gyms and in-house memory-grounded pipelines behind one memory-reasoning interface.<!-- delta:SF-2026-ARXIV-2605-20833:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20833:end -->
<!-- books-review:SF-2026-ARXIV-2605-20834:start -->
<!-- existing:SF-2026-ARXIV-2605-20834:start -->已顺读 `books/part-04-training-system/34-dpo.md` 与相邻章节 ['books/part-04-training-system/33-grpo.md', 'books/part-04-training-system/35-checkpoint.md']。第34章已拥有离线 pair objective、reference/beta/data coverage 与 online RL fallback，但尚未完整承载 federated/decentralized DPO 或最小 online warm-up 到 offline DPO 的 handoff。`Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment` 的 source-specific 机制是：We characterize when this assumption is violated, show the existence of an undesirable solution space, and prove that DPO and RLHF optimize fundamentally different objectives in such cases.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20834:end -->
<!-- delta:SF-2026-ARXIV-2605-20834:start -->We characterize when this assumption is violated, show the existence of an undesirable solution space, and prove that DPO and RLHF optimize fundamentally different objectives in such cases.<!-- delta:SF-2026-ARXIV-2605-20834:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20834:end -->
<!-- books-review:SF-2026-ARXIV-2605-20863:start -->
<!-- existing:SF-2026-ARXIV-2605-20863:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']。第31章已覆盖 rollout/training runtime 解耦、staleness、resource asymmetry 与 cluster pipeline。`PlexRL: Cluster-Level Orchestration of Serviceized LLM Execution for RLVR` 的 source-specific 机制是：However, RLVR training is notoriously inefficient: long-tailed rollouts, tool-induced stalls, and asymmetric resource requirements between rollout and training introduce substantial idle time that cannot be eliminated by job-local optimizations such as synchronous pipelining, asynchronous rollout, or colocated execution.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20863:end -->
<!-- delta:SF-2026-ARXIV-2605-20863:start -->However, RLVR training is notoriously inefficient: long-tailed rollouts, tool-induced stalls, and asymmetric resource requirements between rollout and training introduce substantial idle time that cannot be eliminated by job-local optimizations such as synchronous pipelining, asynchronous rollout, or colocated execution.<!-- delta:SF-2026-ARXIV-2605-20863:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20863:end -->
<!-- books-review:SF-2026-ARXIV-2605-20866:start -->
<!-- existing:SF-2026-ARXIV-2605-20866:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']。第36章已覆盖 typed state transition、Context/Expert Parallel、异构/稀疏通信、bounded staleness、local work 与同步 fallback。`LOSCAR-SGD: Local SGD with Communication-Computation Overlap and Delay-Corrected Sparse Model Averaging` 的 source-specific 机制是：We study a heterogeneous-compute setting in which different workers may take different numbers of local steps, and we propose LOSCAR-SGD, a Local SGD method that communicates only a sparse subset of model coordinates and continues optimizing while communication is in flight.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20866:end -->
<!-- delta:SF-2026-ARXIV-2605-20866:start -->We study a heterogeneous-compute setting in which different workers may take different numbers of local steps, and we propose LOSCAR-SGD, a Local SGD method that communicates only a sparse subset of model coordinates and continues optimizing while communication is in flight.<!-- delta:SF-2026-ARXIV-2605-20866:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20866:end -->
<!-- books-review:SF-2026-ARXIV-2605-20868:start -->
<!-- existing:SF-2026-ARXIV-2605-20868:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']。第45章已覆盖 sparse selection、tiering、prefetch、eviction、reuse identity、误差预算与 exact recompute fallback。`Runtime-Certified Bounded-Error Quantized Attention` 的 source-specific 机制是：We present a tiered KV cache architecture that enables runtime-certified attention: INT8 keys and INT4 values are stored in GPU memory, while FP16 originals are retained in system RAM for deterministic fallback.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20868:end -->
<!-- delta:SF-2026-ARXIV-2605-20868:start -->We present a tiered KV cache architecture that enables runtime-certified attention: INT8 keys and INT4 values are stored in GPU memory, while FP16 originals are retained in system RAM for deterministic fallback.<!-- delta:SF-2026-ARXIV-2605-20868:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20868:end -->
<!-- books-review:SF-2026-ARXIV-2605-20874:start -->
<!-- existing:SF-2026-ARXIV-2605-20874:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']。第84章已拥有 Agent runtime 的 credential、policy、lifecycle 与 commit authority。`Governance by Construction for Generalist Agents` 的 source-specific 机制是：We present a runtime governance architecture that enforces policy interventions at every critical stage of execution.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20874:end -->
<!-- delta:SF-2026-ARXIV-2605-20874:start -->We present a runtime governance architecture that enforces policy interventions at every critical stage of execution.<!-- delta:SF-2026-ARXIV-2605-20874:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20874:end -->
<!-- books-review:SF-2026-ARXIV-2605-20876:start -->
<!-- existing:SF-2026-ARXIV-2605-20876:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']。第27章已把 synthetic generation、executable filtering、trajectory compilation、lineage、coverage 与真实环境 authority 连接成数据控制面。`Terminal-World: Scaling Terminal-Agent Environments via Agent Skills` 的 source-specific 机制是：To address these limitations, we introduce Terminal-World, a fully automated pipeline that uses agent skills as the central synthesis primitive, which jointly encode what to accomplish, when to apply (preconditions and environment state), and how to execute, enabling task instructions, environments, and teacher trajectories to be co-derived.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20876:end -->
<!-- delta:SF-2026-ARXIV-2605-20876:start -->To address these limitations, we introduce Terminal-World, a fully automated pipeline that uses agent skills as the central synthesis primitive, which jointly encode what to accomplish, when to apply (preconditions and environment state), and how to execute, enabling task instructions, environments, and teacher trajectories to be co-derived.<!-- delta:SF-2026-ARXIV-2605-20876:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20876:end -->
<!-- books-review:SF-2026-ARXIV-2605-20923:start -->
<!-- existing:SF-2026-ARXIV-2605-20923:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']。第81章已拥有 versioned DAG、durable state、parallel commit、编译式 procedure 与 recovery contract；但 `Causal Past Logic for Runtime Verification of Distributed LLM Agent Workflows` 所暴露的以下缺口尚未显式进入正文：分布式 Agent workflow 的事件不是单一线性日志；runtime verifier 应在 partial-order/causal-past 上判定 temporal predicate，并保存 event identity、happens-before 与 unknown 边界。<!-- existing:SF-2026-ARXIV-2605-20923:end -->
<!-- delta:SF-2026-ARXIV-2605-20923:start -->分布式 Agent workflow 的事件不是单一线性日志；runtime verifier 应在 partial-order/causal-past 上判定 temporal predicate，并保存 event identity、happens-before 与 unknown 边界。<!-- delta:SF-2026-ARXIV-2605-20923:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20923:end -->
<!-- books-review:SF-2026-ARXIV-2605-20926:start -->
<!-- existing:SF-2026-ARXIV-2605-20926:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。第77章已明确 memory admission、credit、provenance、transaction、rollback 与派生状态不能获得事实权威。`MemConflict: Evaluating Long-Term Memory Systems Under Memory Conflicts` 的 source-specific 机制是：To address this gap, we propose MemConflict, a diagnostic framework that treats memory validity as a query-conditioned fitness-for-use problem.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20926:end -->
<!-- delta:SF-2026-ARXIV-2605-20926:start -->To address this gap, we propose MemConflict, a diagnostic framework that treats memory validity as a query-conditioned fitness-for-use problem.<!-- delta:SF-2026-ARXIV-2605-20926:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20926:end -->
<!-- books-review:SF-2026-ARXIV-2605-20948:start -->
<!-- existing:SF-2026-ARXIV-2605-20948:start -->已顺读 `books/part-02-model/21-moe.md` 与相邻章节 ['books/part-02-model/20-sampling.md', 'books/part-02-model/22-long-context.md']。第21章已拥有 conditional routing、retrieval memory、expert state、placement 与 fallback；离线 hidden-state memory 只是受限实现分支。`Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory` 的 source-specific 机制是：We propose Memory Grafting, a conditional memory scaling method that utilizes frozen hidden states from a grafting model as conditional n-gram memory.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20948:end -->
<!-- delta:SF-2026-ARXIV-2605-20948:start -->We propose Memory Grafting, a conditional memory scaling method that utilizes frozen hidden states from a grafting model as conditional n-gram memory.<!-- delta:SF-2026-ARXIV-2605-20948:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20948:end -->
<!-- books-review:SF-2026-ARXIV-2605-21061:start -->
<!-- existing:SF-2026-ARXIV-2605-21061:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']。第26章已覆盖坐标系、action/trajectory schema、sensor freshness、闭环 correction、sim-to-real 与 safety envelope；但 `Grounding Driving VLA via Inverse Kinematics` 所暴露的以下缺口尚未显式进入正文：trajectory proposal 需要把当前视觉状态与目标/未来视觉状态作为 inverse-kinematics 边界条件，显式隔离可观测几何、未来 proposal 与低层 controller 的 action commit。<!-- existing:SF-2026-ARXIV-2605-21061:end -->
<!-- delta:SF-2026-ARXIV-2605-21061:start -->trajectory proposal 需要把当前视觉状态与目标/未来视觉状态作为 inverse-kinematics 边界条件，显式隔离可观测几何、未来 proposal 与低层 controller 的 action commit。<!-- delta:SF-2026-ARXIV-2605-21061:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21061:end -->
<!-- books-review:SF-2026-ARXIV-2605-21100:start -->
<!-- existing:SF-2026-ARXIV-2605-21100:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']。第56章已拥有 request/KV/topology/SLO 联合 placement、routing 与 state-aware scheduling；但 `NanoCP: Request-Level Dynamic Context Parallelism for Data-Expert Parallel Decoding` 所暴露的以下缺口尚未显式进入正文：MoE decode 中动态 Context Parallel 应分离 expert-communication pressure 与 KV placement pressure；request-level plan 绑定 topology/KV/collective epoch，收益用重规划与迁移成本交换。<!-- existing:SF-2026-ARXIV-2605-21100:end -->
<!-- delta:SF-2026-ARXIV-2605-21100:start -->MoE decode 中动态 Context Parallel 应分离 expert-communication pressure 与 KV placement pressure；request-level plan 绑定 topology/KV/collective epoch，收益用重规划与迁移成本交换。<!-- delta:SF-2026-ARXIV-2605-21100:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21100:end -->
<!-- books-review:SF-2026-ARXIV-2605-21103:start -->
<!-- existing:SF-2026-ARXIV-2605-21103:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']。第36章已覆盖 typed state transition、Context/Expert Parallel、异构/稀疏通信、bounded staleness、local work 与同步 fallback；但 `A Typed Tensor Language for Federated Learning` 所暴露的以下缺口尚未显式进入正文：federated tensor type 区分 client-record axis 与 shared state，并把一轮计算限制为 encode→merge→decode 的固定维 shared-state factorization；类型系统拥有可表达通信边界，而非任意协议标签。<!-- existing:SF-2026-ARXIV-2605-21103:end -->
<!-- delta:SF-2026-ARXIV-2605-21103:start -->federated tensor type 区分 client-record axis 与 shared state，并把一轮计算限制为 encode→merge→decode 的固定维 shared-state factorization；类型系统拥有可表达通信边界，而非任意协议标签。<!-- delta:SF-2026-ARXIV-2605-21103:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21103:end -->
<!-- books-review:SF-2026-ARXIV-2605-21125:start -->
<!-- existing:SF-2026-ARXIV-2605-21125:start -->已顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。第33章已覆盖 group variance、token credit、uncertainty/reward proxy 与 PPO/DPO 分支边界。`Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation` 的 source-specific 机制是：To address this, we introduce the Advantage Collapse Rate (ACR), the first diagnostic metric quantifying the proportion of training batches with ineffective gradients.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21125:end -->
<!-- delta:SF-2026-ARXIV-2605-21125:start -->To address this, we introduce the Advantage Collapse Rate (ACR), the first diagnostic metric quantifying the proportion of training batches with ineffective gradients.<!-- delta:SF-2026-ARXIV-2605-21125:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21125:end -->
<!-- books-review:SF-2026-ARXIV-2605-21127:start -->
<!-- existing:SF-2026-ARXIV-2605-21127:start -->已顺读 `books/part-04-training-system/29-sft.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md', 'books/part-04-training-system/30-lora.md']。第29章已覆盖 on-policy/self-distillation、teacher reliability、state/token selection、full/PEFT 与 reasoning distribution，但尚未承载 reasoning-trace collapse 的独立验收信号；但 `Reasoning-Trace Collapse: Evaluating the Loss of Explicit Reasoning During Fine-Tuning` 所暴露的以下缺口尚未显式进入正文：SFT 不能只验收最终答案；reasoning-trace structure 可能在 answer accuracy 尚未下降时先 collapse，因而 trace validity、final outcome 与 latent capability 必须分别版本化和验收。<!-- existing:SF-2026-ARXIV-2605-21127:end -->
<!-- delta:SF-2026-ARXIV-2605-21127:start -->SFT 不能只验收最终答案；reasoning-trace structure 可能在 answer accuracy 尚未下降时先 collapse，因而 trace validity、final outcome 与 latent capability 必须分别版本化和验收。<!-- delta:SF-2026-ARXIV-2605-21127:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21127:end -->
<!-- books-review:SF-2026-ARXIV-2605-21177:start -->
<!-- existing:SF-2026-ARXIV-2605-21177:start -->已顺读 `books/part-04-training-system/29-sft.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md', 'books/part-04-training-system/30-lora.md']。第29章已覆盖 on-policy/self-distillation、teacher reliability、state/token selection、full/PEFT 与 reasoning distribution，但尚未承载 reasoning-trace collapse 的独立验收信号。`ChunkFT: Byte-Streamed Optimization for Memory-Efficient Full Fine-Tuning` 的 source-specific 机制是：The results demonstrate the effectiveness of \textsc{ChunkFT} in memory usage, running time, and optimization quality.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21177:end -->
<!-- delta:SF-2026-ARXIV-2605-21177:start -->The results demonstrate the effectiveness of \textsc{ChunkFT} in memory usage, running time, and optimization quality.<!-- delta:SF-2026-ARXIV-2605-21177:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21177:end -->
<!-- books-review:SF-2026-ARXIV-2605-21187:start -->
<!-- existing:SF-2026-ARXIV-2605-21187:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']。第36章已覆盖 typed state transition、Context/Expert Parallel、异构/稀疏通信、bounded staleness、local work 与同步 fallback。`High-speed Networking for Giga-Scale AI Factories` 的 source-specific 机制是：We describe the motivation, design principles, evaluation methodology and performance on state-of-the-art benchmarks, as well as the lessons we learned from deploying and debugging Spectrum-X networks in large-scale systems.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21187:end -->
<!-- delta:SF-2026-ARXIV-2605-21187:start -->We describe the motivation, design principles, evaluation methodology and performance on state-of-the-art benchmarks, as well as the lessons we learned from deploying and debugging Spectrum-X networks in large-scale systems.<!-- delta:SF-2026-ARXIV-2605-21187:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21187:end -->
<!-- books-review:SF-2026-ARXIV-2605-21266:start -->
<!-- existing:SF-2026-ARXIV-2605-21266:start -->已顺读 `books/part-04-training-system/34-dpo.md` 与相邻章节 ['books/part-04-training-system/33-grpo.md', 'books/part-04-training-system/35-checkpoint.md']。第34章已拥有离线 pair objective、reference/beta/data coverage 与 online RL fallback，但尚未完整承载 federated/decentralized DPO 或最小 online warm-up 到 offline DPO 的 handoff；但 `How Much Online RL is Enough? Informative Rollouts for Offline Preference Optimization in RLVR` 所暴露的以下缺口尚未显式进入正文：online GRPO 可以只负责发现 informative state/rollout，再冻结 provenance-complete preference dataset 交给 offline DPO；handoff 以更少在线成本换 selection bias、staleness 与二阶段 objective mismatch。<!-- existing:SF-2026-ARXIV-2605-21266:end -->
<!-- delta:SF-2026-ARXIV-2605-21266:start -->online GRPO 可以只负责发现 informative state/rollout，再冻结 provenance-complete preference dataset 交给 offline DPO；handoff 以更少在线成本换 selection bias、staleness 与二阶段 objective mismatch。<!-- delta:SF-2026-ARXIV-2605-21266:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21266:end -->
<!-- books-review:SF-2026-ARXIV-2605-21273:start -->
<!-- existing:SF-2026-ARXIV-2605-21273:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']。第26章已覆盖坐标系、action/trajectory schema、sensor freshness、闭环 correction、sim-to-real 与 safety envelope；但 `DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions` 所暴露的以下缺口尚未显式进入正文：自然语言 reasoning 作为 driving action interface 会引入标注、延迟和 grounding bottleneck；one-step meta-action 将高层语义压成可执行 action schema，但必须保留坐标、低层控制和安全 envelope。<!-- existing:SF-2026-ARXIV-2605-21273:end -->
<!-- delta:SF-2026-ARXIV-2605-21273:start -->自然语言 reasoning 作为 driving action interface 会引入标注、延迟和 grounding bottleneck；one-step meta-action 将高层语义压成可执行 action schema，但必须保留坐标、低层控制和安全 envelope。<!-- delta:SF-2026-ARXIV-2605-21273:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21273:end -->
<!-- books-review:SF-2026-ARXIV-2605-21312:start -->
<!-- existing:SF-2026-ARXIV-2605-21312:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']。第56章已拥有 request/KV/topology/SLO 联合 placement、routing 与 state-aware scheduling。`Frontier: Towards Comprehensive and Accurate LLM Inference Simulation` 的 source-specific 机制是：Simulation is attractive for exploring this growing design space, yet existing simulators lack the architectural completeness and decision-grade fidelity it demands.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21312:end -->
<!-- delta:SF-2026-ARXIV-2605-21312:start -->Simulation is attractive for exploring this growing design space, yet existing simulators lack the architectural completeness and decision-grade fidelity it demands.<!-- delta:SF-2026-ARXIV-2605-21312:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21312:end -->
<!-- books-review:SF-2026-ARXIV-2605-21347:start -->
<!-- existing:SF-2026-ARXIV-2605-21347:start -->已顺读 `books/part-06-ai-infrastructure/69-trace.md` 与相邻章节 ['books/part-06-ai-infrastructure/68-logging.md', 'books/part-06-ai-infrastructure/70-cost.md']。第69章已把 linear trace 演进为 root-cause graph，并分离 trace evidence、diagnostic hypothesis、repair authority 与 rerun evidence。`Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents` 的 source-specific 机制是：We present the Insights Generator (IG), a multi-agent system that answers diagnostic questions by proposing and testing hypotheses across the trace corpus to produce an evidence-backed insights report.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21347:end -->
<!-- delta:SF-2026-ARXIV-2605-21347:start -->We present the Insights Generator (IG), a multi-agent system that answers diagnostic questions by proposing and testing hypotheses across the trace corpus to produce an evidence-backed insights report.<!-- delta:SF-2026-ARXIV-2605-21347:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21347:end -->
<!-- books-review:SF-2026-ARXIV-2605-21384:start -->
<!-- existing:SF-2026-ARXIV-2605-21384:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents` 的 source-specific 机制是：We study this reward hacking phenomenon by decompose software engineering tasks into three parts: (i) a natural language description of the specification (ii) visible validation tests that exercise specified features in isolation, and (iii) held-out tests that compose those same features to simulate real-world usage.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21384:end -->
<!-- delta:SF-2026-ARXIV-2605-21384:start -->We study this reward hacking phenomenon by decompose software engineering tasks into three parts: (i) a natural language description of the specification (ii) visible validation tests that exercise specified features in isolation, and (iii) held-out tests that compose those same features to simulate real-world usage.<!-- delta:SF-2026-ARXIV-2605-21384:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21384:end -->
<!-- books-review:SF-2026-ARXIV-2605-21392:start -->
<!-- existing:SF-2026-ARXIV-2605-21392:start -->已顺读 `books/part-07-agent/83-mcp.md` 与相邻章节 ['books/part-07-agent/82-multi-agent.md', 'books/part-07-agent/84-agent-platform.md']。第83章已把多 Server 权限提升为带 principal、server identity 与 taint 的端到端 information-flow contract，并保留 effect-time authorizer 与隔离 fallback。`VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers` 的 source-specific 机制是：In this paper, we present VIPER-MCP, the first end-to-end automated vulnerability auditing framework for MCP servers that not only detects taint-style vulnerabilities but also dynamically confirms their exploitability by producing concrete proof-of-concept prompts.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21392:end -->
<!-- delta:SF-2026-ARXIV-2605-21392:start -->In this paper, we present VIPER-MCP, the first end-to-end automated vulnerability auditing framework for MCP servers that not only detects taint-style vulnerabilities but also dynamically confirms their exploitability by producing concrete proof-of-concept prompts.<!-- delta:SF-2026-ARXIV-2605-21392:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21392:end -->
<!-- books-review:SF-2026-ARXIV-2605-21427:start -->
<!-- existing:SF-2026-ARXIV-2605-21427:start -->已顺读 `books/part-06-ai-infrastructure/70-cost.md` 与相邻章节 ['books/part-06-ai-infrastructure/69-trace.md', 'books/part-06-ai-infrastructure/71-multi-tenant.md']。第70章已区分 resource time、effective utilization、quality/SLO 合格工作、agent state-dependent work 与 deployable power。`PALS: Power-Aware LLM Serving for Mixture-of-Experts Models` 的 source-specific 机制是：In this paper, we present a power-aware runtime for LLM serving, PALS, that treats GPU power caps as a first-class control knob and jointly optimizes them with software parameters such as batch size.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21427:end -->
<!-- delta:SF-2026-ARXIV-2605-21427:start -->In this paper, we present a power-aware runtime for LLM serving, PALS, that treats GPU power caps as a first-class control knob and jointly optimizes them with software parameters such as batch size.<!-- delta:SF-2026-ARXIV-2605-21427:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21427:end -->
<!-- books-review:SF-2026-ARXIV-2605-21434:start -->
<!-- existing:SF-2026-ARXIV-2605-21434:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`Agentic Model Checking` 的 source-specific 机制是：We propose agentic model checking, a paradigm that couples LLM agents with a bounded model checking backend under the principle agents propose, solvers verify: agents handle tasks requiring semantic judgment (spec inference, check selection, counterexample classification, refinement proposal) while BMC discharges every soundness-relevant decision.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21434:end -->
<!-- delta:SF-2026-ARXIV-2605-21434:start -->We propose agentic model checking, a paradigm that couples LLM agents with a bounded model checking backend under the principle agents propose, solvers verify: agents handle tasks requiring semantic judgment (spec inference, check selection, counterexample classification, refinement proposal) while BMC discharges every soundness-relevant decision.<!-- delta:SF-2026-ARXIV-2605-21434:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21434:end -->
<!-- books-review:SF-2026-ARXIV-2605-21446:start -->
<!-- existing:SF-2026-ARXIV-2605-21446:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']。第26章已覆盖坐标系、action/trajectory schema、sensor freshness、闭环 correction、sim-to-real 与 safety envelope。`Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs` 的 source-specific 机制是：In this paper we present a controlled perturbation study of Vision-Language-Action (VLA) robustness in autonomous driving, evaluating Alpamayo R1 (10B parameters) across 1,996 scenarios under eight sensor perturbations (Gaussian noise at four intensities, two lighting extremes, and two fog levels; ${\sim}18{,}000$ inference trials).；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21446:end -->
<!-- delta:SF-2026-ARXIV-2605-21446:start -->In this paper we present a controlled perturbation study of Vision-Language-Action (VLA) robustness in autonomous driving, evaluating Alpamayo R1 (10B parameters) across 1,996 scenarios under eight sensor perturbations (Gaussian noise at four intensities, two lighting extremes, and two fog levels; ${\sim}18{,}000$ inference trials).<!-- delta:SF-2026-ARXIV-2605-21446:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21446:end -->
<!-- books-review:SF-2026-ARXIV-2605-21467:start -->
<!-- existing:SF-2026-ARXIV-2605-21467:start -->已顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。第33章已覆盖 group variance、token credit、uncertainty/reward proxy 与 PPO/DPO 分支边界。`DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from Verifiable Rewards` 的 source-specific 机制是：We introduce a discriminator view of RLVR updates, showing that the policy-gradient update direction implicitly acts as a linear discriminator over token-gradient vectors and thereby determines which token probabilities are increased or decreased during learning.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21467:end -->
<!-- delta:SF-2026-ARXIV-2605-21467:start -->We introduce a discriminator view of RLVR updates, showing that the policy-gradient update direction implicitly acts as a linear discriminator over token-gradient vectors and thereby determines which token probabilities are increased or decreased during learning.<!-- delta:SF-2026-ARXIV-2605-21467:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21467:end -->
<!-- books-review:SF-2026-ARXIV-2605-21468:start -->
<!-- existing:SF-2026-ARXIV-2605-21468:start -->已顺读 `books/part-04-training-system/35-checkpoint.md` 与相邻章节 ['books/part-04-training-system/34-dpo.md', 'books/part-04-training-system/36-distributed-training.md']。第35章已拥有一致 checkpoint identity、commit/recovery 与可验证 artifact；尚未承载从短 RLVR 轨迹外推权重状态的条件分支；但 `You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories` 所暴露的以下缺口尚未显式进入正文：短 RLVR weight trajectory 可作为低秩状态序列拟合并外推 checkpoint proposal；proposal 不能获得 artifact commit，必须由 held-out training/eval、数值稳定性和完整 checkpoint fallback 验收。<!-- existing:SF-2026-ARXIV-2605-21468:end -->
<!-- delta:SF-2026-ARXIV-2605-21468:start -->短 RLVR weight trajectory 可作为低秩状态序列拟合并外推 checkpoint proposal；proposal 不能获得 artifact commit，必须由 held-out training/eval、数值稳定性和完整 checkpoint fallback 验收。<!-- delta:SF-2026-ARXIV-2605-21468:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21468:end -->
<!-- books-review:SF-2026-ARXIV-2605-21470:start -->
<!-- existing:SF-2026-ARXIV-2605-21470:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']。第81章已拥有 versioned DAG、durable state、parallel commit、编译式 procedure 与 recovery contract。`Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling` 的 source-specific 机制是：We present agent just-in-time (JIT) compilation, a system that compiles task descriptions directly into executable code that may include LLM calls, tool calls, and parallelization.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21470:end -->
<!-- delta:SF-2026-ARXIV-2605-21470:start -->We present agent just-in-time (JIT) compilation, a system that compiles task descriptions directly into executable code that may include LLM calls, tool calls, and parallelization.<!-- delta:SF-2026-ARXIV-2605-21470:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21470:end -->
<!-- books-review:SF-2026-ARXIV-2605-21482:start -->
<!-- existing:SF-2026-ARXIV-2605-21482:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation` 的 source-specific 机制是：We introduce DeepWeb-Bench, a deep research benchmark that is substantially harder than existing benchmarks for the current frontier.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21482:end -->
<!-- delta:SF-2026-ARXIV-2605-21482:start -->We introduce DeepWeb-Bench, a deep research benchmark that is substantially harder than existing benchmarks for the current frontier.<!-- delta:SF-2026-ARXIV-2605-21482:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21482:end -->
<!-- books-review:SF-2026-ARXIV-2605-21486:start -->
<!-- existing:SF-2026-ARXIV-2605-21486:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。第28章已覆盖 parameterization、preconditioner geometry、layer-wise LR、noise floor、spectral diagnostics 与训练稳定性，但尚未写明同批 gradient/preconditioner 的两类有限样本偏差。`Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate` 的 source-specific 机制是：In this paper, we first develop a framework to quantify hyperparameter transfer through three metrics: (1) the quality of the scaling law fit, (2) the robustness to extrapolation errors, and (3) the asymptotic loss penalty due to choice of parameterization.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21486:end -->
<!-- delta:SF-2026-ARXIV-2605-21486:start -->In this paper, we first develop a framework to quantify hyperparameter transfer through three metrics: (1) the quality of the scaling law fit, (2) the robustness to extrapolation errors, and (3) the asymptotic loss penalty due to choice of parameterization.<!-- delta:SF-2026-ARXIV-2605-21486:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21486:end -->
<!-- books-review:SF-2026-ARXIV-2605-21543:start -->
<!-- existing:SF-2026-ARXIV-2605-21543:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`Provable Joint Decontamination for Benchmarking Multiple Large Language Models` 的 source-specific 机制是：In this work, we formalize multi-model benchmark decontamination as a joint selection problem and propose Joint Envelope Conformal Selection (JECS), a conformal procedure that enables global contamination rate (GCR) control under stated assumptions.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21543:end -->
<!-- delta:SF-2026-ARXIV-2605-21543:start -->In this work, we formalize multi-model benchmark decontamination as a joint selection problem and propose Joint Envelope Conformal Selection (JECS), a conformal procedure that enables global contamination rate (GCR) control under stated assumptions.<!-- delta:SF-2026-ARXIV-2605-21543:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21543:end -->
<!-- books-review:SF-2026-ARXIV-2605-21602:start -->
<!-- existing:SF-2026-ARXIV-2605-21602:start -->已顺读 `books/part-06-ai-infrastructure/67-monitoring.md` 与相邻章节 ['books/part-06-ai-infrastructure/66-evaluation-system.md', 'books/part-06-ai-infrastructure/68-logging.md']。第67章已区分 raw utilization、有效进展、sensor/health/attestation、漂移与独立 red-team。`Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs` 的 source-specific 机制是：We systematically study whether LLM monitoring pipelines can detect these OOD alignment failures by introducing a benchmark called Misalignment Out Of Distribution (MOOD).；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21602:end -->
<!-- delta:SF-2026-ARXIV-2605-21602:start -->We systematically study whether LLM monitoring pipelines can detect these OOD alignment failures by introducing a benchmark called Misalignment Out Of Distribution (MOOD).<!-- delta:SF-2026-ARXIV-2605-21602:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21602:end -->
<!-- books-review:SF-2026-ARXIV-2605-21603:start -->
<!-- existing:SF-2026-ARXIV-2605-21603:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']。第49章已把 logical graph、physical execution plan、operator schedule 与 hardware control state 分离。`DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling` 的 source-specific 机制是：To address this, we propose DynaFlow, a framework that enables the transparent and flexible integration of intra-device parallelism by decoupling the logical model definition from the physical execution schedule.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21603:end -->
<!-- delta:SF-2026-ARXIV-2605-21603:start -->To address this, we propose DynaFlow, a framework that enables the transparent and flexible integration of intra-device parallelism by decoupling the logical model definition from the physical execution schedule.<!-- delta:SF-2026-ARXIV-2605-21603:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21603:end -->
<!-- books-review:SF-2026-ARXIV-2605-21606:start -->
<!-- existing:SF-2026-ARXIV-2605-21606:start -->已顺读 `books/part-04-training-system/29-sft.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md', 'books/part-04-training-system/30-lora.md']。第29章已覆盖 on-policy/self-distillation、teacher reliability、state/token selection、full/PEFT 与 reasoning distribution，但尚未承载 reasoning-trace collapse 的独立验收信号。`When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning` 的 source-specific 机制是：To identify this phenomenon, we introduce a branch-viability diagnostic.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21606:end -->
<!-- delta:SF-2026-ARXIV-2605-21606:start -->To identify this phenomenon, we introduce a branch-viability diagnostic.<!-- delta:SF-2026-ARXIV-2605-21606:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21606:end -->
<!-- books-review:SF-2026-ARXIV-2605-21642:start -->
<!-- existing:SF-2026-ARXIV-2605-21642:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`Ablate-to-Validate: Are Vision-Language Models Really Using Continuous Thought Tokens?` 的 source-specific 机制是：Vision-language models (VLMs) are increasingly augmented with continuous or latent non-textual tokens intended to support "visual thinking." Despite improved task accuracy, this alone does not show that models actually use these tokens for reasoning -- gains may arise from confounds such as added context length, special-token anchoring, or training-time regularization.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21642:end -->
<!-- delta:SF-2026-ARXIV-2605-21642:start -->Vision-language models (VLMs) are increasingly augmented with continuous or latent non-textual tokens intended to support "visual thinking." Despite improved task accuracy, this alone does not show that models actually use these tokens for reasoning -- gains may arise from confounds such as added context length, special-token anchoring, or training-time regularization.<!-- delta:SF-2026-ARXIV-2605-21642:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21642:end -->
<!-- books-review:SF-2026-ARXIV-2605-21648:start -->
<!-- existing:SF-2026-ARXIV-2605-21648:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。第28章已覆盖 parameterization、preconditioner geometry、layer-wise LR、noise floor、spectral diagnostics 与训练稳定性，但尚未写明同批 gradient/preconditioner 的两类有限样本偏差。`Dropout Universality: Scaling Laws and Optimal Scheduling at the Edge-of-Chaos` 的 source-specific 机制是：We develop a mean-field theory of dropout as a perturbation of critical signal propagation at the edge of chaos, and show that it predicts a simple, no-cost change to standard practice: \emph{front-loaded} dropout schedules cut test loss by \(18\)--\(35\%\) over constant dropout in MLPs and Vision Transformers at fixed budget.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21648:end -->
<!-- delta:SF-2026-ARXIV-2605-21648:start -->We develop a mean-field theory of dropout as a perturbation of critical signal propagation at the edge of chaos, and show that it predicts a simple, no-cost change to standard practice: \emph{front-loaded} dropout schedules cut test loss by \(18\)--\(35\%\) over constant dropout in MLPs and Vision Transformers at fixed budget.<!-- delta:SF-2026-ARXIV-2605-21648:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21648:end -->
<!-- books-review:SF-2026-ARXIV-2605-21649:start -->
<!-- existing:SF-2026-ARXIV-2605-21649:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']。第45章已覆盖 sparse selection、tiering、prefetch、eviction、reuse identity、误差预算与 exact recompute fallback。`EntmaxKV: Support-Aware Decoding for Entmax Attention` 的 source-specific 机制是：In this work, we introduce EntmaxKV, an entmax-native sparse decoding framework that exploits sparsity before KV pages are loaded.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21649:end -->
<!-- delta:SF-2026-ARXIV-2605-21649:start -->In this work, we introduce EntmaxKV, an entmax-native sparse decoding framework that exploits sparsity before KV pages are loaded.<!-- delta:SF-2026-ARXIV-2605-21649:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21649:end -->
<!-- books-review:SF-2026-ARXIV-2605-21768:start -->
<!-- existing:SF-2026-ARXIV-2605-21768:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。第77章已明确 memory admission、credit、provenance、transaction、rollback 与派生状态不能获得事实权威。`Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents` 的 source-specific 机制是：To address this challenge, we introduce Memory-R2, a training framework for long-horizon memory-augmented LLM agents.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21768:end -->
<!-- delta:SF-2026-ARXIV-2605-21768:start -->To address this challenge, we introduce Memory-R2, a training framework for long-horizon memory-augmented LLM agents.<!-- delta:SF-2026-ARXIV-2605-21768:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21768:end -->
<!-- books-review:SF-2026-ARXIV-2605-21779:start -->
<!-- existing:SF-2026-ARXIV-2605-21779:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。第72章已拥有 supply-chain、runtime optimization、taint、bounded verification、exploit evidence 与 fail-closed authority。`FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction` 的 source-specific 机制是：While Large Language Models (LLMs) show promise for automated vulnerability detection, three key challenges remain.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21779:end -->
<!-- delta:SF-2026-ARXIV-2605-21779:start -->While Large Language Models (LLMs) show promise for automated vulnerability detection, three key challenges remain.<!-- delta:SF-2026-ARXIV-2605-21779:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21779:end -->
<!-- books-review:SF-2026-ARXIV-2605-21800:start -->
<!-- existing:SF-2026-ARXIV-2605-21800:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。第25章已覆盖 projective 4D predictive state、geometry-motion consistency、action-conditioned transition 与真实观测回滚。`stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation` 的 source-specific 机制是：We present stable-worldmodel (swm), an open-source platform for standardized and reproducible world modeling research and evaluation.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21800:end -->
<!-- delta:SF-2026-ARXIV-2605-21800:start -->We present stable-worldmodel (swm), an open-source platform for standardized and reproducible world modeling research and evaluation.<!-- delta:SF-2026-ARXIV-2605-21800:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21800:end -->
<!-- books-review:SF-2026-ARXIV-2605-21801:start -->
<!-- existing:SF-2026-ARXIV-2605-21801:start -->已顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。第33章已覆盖 group variance、token credit、uncertainty/reward proxy 与 PPO/DPO 分支边界。`Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization` 的 source-specific 机制是：Based on both empirical and theoretical analysis, we identify two critical gaps of current entropy-based estimators: The anisotropic gap and The calibration gap.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21801:end -->
<!-- delta:SF-2026-ARXIV-2605-21801:start -->Based on both empirical and theoretical analysis, we identify two critical gaps of current entropy-based estimators: The anisotropic gap and The calibration gap.<!-- delta:SF-2026-ARXIV-2605-21801:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21801:end -->
<!-- books-review:SF-2026-ARXIV-2605-21803:start -->
<!-- existing:SF-2026-ARXIV-2605-21803:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。第28章已覆盖 parameterization、preconditioner geometry、layer-wise LR、noise floor、spectral diagnostics 与训练稳定性，但尚未写明同批 gradient/preconditioner 的两类有限样本偏差。`Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws` 的 source-specific 机制是：We show that this assumption misses a fundamental axis of representation scaling: how effectively the optimizer converts added FFN width into utilized spectral capacity.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21803:end -->
<!-- delta:SF-2026-ARXIV-2605-21803:start -->We show that this assumption misses a fundamental axis of representation scaling: how effectively the optimizer converts added FFN width into utilized spectral capacity.<!-- delta:SF-2026-ARXIV-2605-21803:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21803:end -->
<!-- books-review:SF-2026-ARXIV-2605-21847:start -->
<!-- existing:SF-2026-ARXIV-2605-21847:start -->已顺读 `books/part-06-ai-infrastructure/70-cost.md` 与相邻章节 ['books/part-06-ai-infrastructure/69-trace.md', 'books/part-06-ai-infrastructure/71-multi-tenant.md']。第70章已区分 resource time、effective utilization、quality/SLO 合格工作、agent state-dependent work 与 deployable power。`CompPow: A Case for Component-level GPU Power Management` 的 source-specific 机制是：We demonstrate for a variety of ML operations and execution patterns, CompPow has the potential to deliver higher energy efficiency (10%) and even improved performance (5%).；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21847:end -->
<!-- delta:SF-2026-ARXIV-2605-21847:start -->We demonstrate for a variety of ML operations and execution patterns, CompPow has the potential to deliver higher energy efficiency (10%) and even improved performance (5%).<!-- delta:SF-2026-ARXIV-2605-21847:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21847:end -->
<!-- books-review:SF-2026-ARXIV-2605-21850:start -->
<!-- existing:SF-2026-ARXIV-2605-21850:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']。第27章已把 synthetic generation、executable filtering、trajectory compilation、lineage、coverage 与真实环境 authority 连接成数据控制面。`ACC: Compiling Agent Trajectories for Long-Context Training` 的 source-specific 机制是：We propose Agent Context Compilation (ACC), which converts trajectories from search, software engineering, and database querying agents into long-context QA pairs that combine the original question with tool responses and environment observations gathered across multiple turns, training the model to answer directly without tool use.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21850:end -->
<!-- delta:SF-2026-ARXIV-2605-21850:start -->We propose Agent Context Compilation (ACC), which converts trajectories from search, software engineering, and database querying agents into long-context QA pairs that combine the original question with tool responses and environment observations gathered across multiple turns, training the model to answer directly without tool use.<!-- delta:SF-2026-ARXIV-2605-21850:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21850:end -->
<!-- books-review:SF-2026-ARXIV-2605-22882:start -->
<!-- existing:SF-2026-ARXIV-2605-22882:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。第25章已覆盖 projective 4D predictive state、geometry-motion consistency、action-conditioned transition 与真实观测回滚。`GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation` 的 source-specific 机制是：We present GEM-4D, a geometry-grounded video world model that resolves this limitation by injecting dense 4D correspondence supervision distilled from a pretrained geometry foundation model into the video generative backbone during training.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-22882:end -->
<!-- delta:SF-2026-ARXIV-2605-22882:start -->We present GEM-4D, a geometry-grounded video world model that resolves this limitation by injecting dense 4D correspondence supervision distilled from a pretrained geometry foundation model into the video generative backbone during training.<!-- delta:SF-2026-ARXIV-2605-22882:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-22882:end -->
<!-- books-review:SF-2026-ARXIV-2605-22883:start -->
<!-- existing:SF-2026-ARXIV-2605-22883:start -->已顺读 `books/part-06-ai-infrastructure/70-cost.md` 与相邻章节 ['books/part-06-ai-infrastructure/69-trace.md', 'books/part-06-ai-infrastructure/71-multi-tenant.md']。第70章已区分 resource time、effective utilization、quality/SLO 合格工作、agent state-dependent work 与 deployable power；但 `Energy per Successful Goal: Goal-Level Energy Accounting for Agentic AI Systems` 所暴露的以下缺口尚未显式进入正文：Agent 能耗从 per-token/per-request 上移到 per-successful-goal：同一 goal 的模型调用、tool、retry、idle 与失败 run 进入同一 lineage；成功谓词/evaluator 版本决定分母。<!-- existing:SF-2026-ARXIV-2605-22883:end -->
<!-- delta:SF-2026-ARXIV-2605-22883:start -->Agent 能耗从 per-token/per-request 上移到 per-successful-goal：同一 goal 的模型调用、tool、retry、idle 与失败 run 进入同一 lineage；成功谓词/evaluator 版本决定分母。<!-- delta:SF-2026-ARXIV-2605-22883:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-22883:end -->
<!-- books-review:SF-2026-ARXIV-2605-22884:start -->
<!-- existing:SF-2026-ARXIV-2605-22884:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']。第45章已覆盖 sparse selection、tiering、prefetch、eviction、reuse identity、误差预算与 exact recompute fallback；但 `Tensor Cache: Eviction-conditioned Associative Memory for Transformers` 所暴露的以下缺口尚未显式进入正文：sliding-window eviction 不再等于丢弃：exact recent KV 作为 L1，已驱逐 KV 以 outer-product fast-weight matrix 形成固定大小 L2；写入顺序、decay/gate、数值 scan 与 exact-window fallback 成为新 cache identity。<!-- existing:SF-2026-ARXIV-2605-22884:end -->
<!-- delta:SF-2026-ARXIV-2605-22884:start -->sliding-window eviction 不再等于丢弃：exact recent KV 作为 L1，已驱逐 KV 以 outer-product fast-weight matrix 形成固定大小 L2；写入顺序、decay/gate、数值 scan 与 exact-window fallback 成为新 cache identity。<!-- delta:SF-2026-ARXIV-2605-22884:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-22884:end -->
<!-- books-review:SF-2026-ARXIV-2605-24022:start -->
<!-- existing:SF-2026-ARXIV-2605-24022:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']。第45章已覆盖 sparse selection、tiering、prefetch、eviction、reuse identity、误差预算与 exact recompute fallback。`Adaptive KV Cache Reuse for Fast Long-Context LLM Serving` 的 source-specific 机制是：Evaluations on mainstream LLMs and long-context tasks show that CacheTune achieves 3.72x-4.86x TTFT speedup and 3.93x-6.21x higher throughput while maintaining generation quality close to full recompute.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-24022:end -->
<!-- delta:SF-2026-ARXIV-2605-24022:start -->Evaluations on mainstream LLMs and long-context tasks show that CacheTune achieves 3.72x-4.86x TTFT speedup and 3.93x-6.21x higher throughput while maintaining generation quality close to full recompute.<!-- delta:SF-2026-ARXIV-2605-24022:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24022:end -->
<!-- books-review:SF-2026-ARXIV-2605-26128:start -->
<!-- existing:SF-2026-ARXIV-2605-26128:start -->已顺读 `books/part-07-agent/78-tool-calling.md` 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']。第78章已拥有 structured output、tool proposal、schema validation 与 effect receipt 的边界。`The Constraint Tax: Measuring Validity-Correctness Tradeoffs in Structured Outputs for Small Language Models` 的 source-specific 机制是：We show that this assumption is unsafe for small models.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-26128:end -->
<!-- delta:SF-2026-ARXIV-2605-26128:start -->We show that this assumption is unsafe for small models.<!-- delta:SF-2026-ARXIV-2605-26128:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26128:end -->
<!-- books-review:SF-2026-ARXIV-2605-26132:start -->
<!-- existing:SF-2026-ARXIV-2605-26132:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']。第27章已把 synthetic generation、executable filtering、trajectory compilation、lineage、coverage 与真实环境 authority 连接成数据控制面。`Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline` 的 source-specific 机制是：We study this setting starting only from unlabeled seed questions with no ground-truth solutions, across three reasoning domains: math, science, and coding.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-26132:end -->
<!-- delta:SF-2026-ARXIV-2605-26132:start -->We study this setting starting only from unlabeled seed questions with no ground-truth solutions, across three reasoning domains: math, science, and coding.<!-- delta:SF-2026-ARXIV-2605-26132:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26132:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260521-COVERAGE | fresh-context:may2026-day02 | coverage | coverage:SRC-ARXIV:20260521 | none | full 629 replay removed 3 false positives and recovered 33 false negatives | passed |
| SA-20260521-EVIDENCE | fresh-context:may2026-day02 | evidence | review:SF-2026-ARXIV-2605-20616 | none | 66/66 source-specific exact-v1 reviews completed | passed |
| SA-20260521-SELECTION | fresh-context:may2026-day02 | deep_analysis_selection | analysis:DA-PRECONDITIONER-BIAS-CONTRACT | none | three cross-layer design deltas selected after denominator reconciliation | passed |
| SA-20260521-BOOKS | fresh-context:root-non-author-non-writer | books | books-review:SF-2026-ARXIV-2605-20641; books-review:SF-2026-ARXIV-2605-22884 | none | day02 froze the 15-item queue after owner/adjacent comparison；root independently verified 15/15 post-write canonical owner placement, evolution chain, trade-off, failure, fallback and exact-v1 boundary；receipt=`post-write-semantic-audit.json` | passed |

## 8. Ignored Noise

563 条 family-specific pre-denominator closure 保存于 `screening-ledger-independent-final.json`；理由唯一数=563。

## 9. Recommended Action

本日不再有待执行动作。15 项正文已由未参与写入的 reviewer 完成 post-write semantic audit，机制位置、owner 唯一性、演进链、trade-off、failure、fallback 与 exact-v1 boundary 全部通过。

## 10. Repository Changes

- 更新 2026-05-21 date-local Books queue，状态为 `post_write_semantic_audit_passed`。
- 15 项机制已分别写入 13 个 canonical owner 章节的既有正文主线，均位于自检、小结和 H2 `Review notes` 之前；未 stage、commit 或 push。
- 新增 date-local `post-write-semantic-audit.json`，记录 15/15 独立写后语义验收结果。

## 11. Open Questions

- 无。本日 15/15 机制已确认在 canonical main body 中顺读成立，未形成重复 owner、越界结论或章末堆砌。

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 12. Sources

- [Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents](https://arxiv.org/html/2605.20616v1) — arXiv:2605.20616v1；first-public 2026-05-20；accessed 2026-09-01
- [Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute Pipelines](https://arxiv.org/html/2605.20630v1) — arXiv:2605.20630v1；first-public 2026-05-20；accessed 2026-09-01
- [Trusted Weights, Treacherous Optimizations? Optimization-Triggered Backdoor Attacks on LLMs](https://arxiv.org/html/2605.20641v1) — arXiv:2605.20641v1；first-public 2026-05-20；accessed 2026-09-01
- [Distributed Direct Preference Optimization](https://arxiv.org/html/2605.20696v1) — arXiv:2605.20696v1；first-public 2026-05-20；accessed 2026-09-01
- [Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms](https://arxiv.org/html/2605.20704v1) — arXiv:2605.20704v1；first-public 2026-05-20；accessed 2026-09-01
- [Llamas on the Web: Memory-Efficient, Performance-Portable, and Multi-Precision LLM Inference with WebGPU](https://arxiv.org/html/2605.20706v1) — arXiv:2605.20706v1；first-public 2026-05-20；accessed 2026-09-01
- [An Application-Layer Multi-Modal Covert-Channel Reference Monitor for LLM Agent Egress](https://arxiv.org/html/2605.20734v1) — arXiv:2605.20734v1；first-public 2026-05-20；accessed 2026-09-01
- [Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale](https://arxiv.org/html/2605.20744v1) — arXiv:2605.20744v1；first-public 2026-05-20；accessed 2026-09-01
- [The Devil is in the Condition Numbers: Why is GLU Better than non-GLU Structure?](https://arxiv.org/html/2605.20749v1) — arXiv:2605.20749v1；first-public 2026-05-20；accessed 2026-09-01
- [GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation](https://arxiv.org/html/2605.20752v1) — arXiv:2605.20752v1；first-public 2026-05-20；accessed 2026-09-01
- [Correcting Stochastic Update Bias in Preconditioned Language Model Optimizers](https://arxiv.org/html/2605.20756v1) — arXiv:2605.20756v1；first-public 2026-05-20；accessed 2026-09-01
- [The Illusion of Intervention: Your LLM-Simulated Experiment is an Observational Study](https://arxiv.org/html/2605.20767v1) — arXiv:2605.20767v1；first-public 2026-05-20；accessed 2026-09-01
- [VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models](https://arxiv.org/html/2605.20774v1) — arXiv:2605.20774v1；first-public 2026-05-20；accessed 2026-09-01
- [Most Transformer Modifications Still Do Not Transfer at 1-3B: A 2020-2026 Update to Narang et al. (2021) with Downstream Evaluation and a Noise Floor](https://arxiv.org/html/2605.20798v1) — arXiv:2605.20798v1；first-public 2026-05-20；accessed 2026-09-01
- [Instant GPU Efficiency Visibility at Fleet Scale](https://arxiv.org/html/2605.20799v1) — arXiv:2605.20799v1；first-public 2026-05-20；accessed 2026-09-01
- [MemGym: a Long-Horizon Memory Environment for LLM Agents](https://arxiv.org/html/2605.20833v1) — arXiv:2605.20833v1；first-public 2026-05-20；accessed 2026-09-01
- [Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment](https://arxiv.org/html/2605.20834v1) — arXiv:2605.20834v1；first-public 2026-05-20；accessed 2026-09-01
- [PlexRL: Cluster-Level Orchestration of Serviceized LLM Execution for RLVR](https://arxiv.org/html/2605.20863v1) — arXiv:2605.20863v1；first-public 2026-05-20；accessed 2026-09-01
- [LOSCAR-SGD: Local SGD with Communication-Computation Overlap and Delay-Corrected Sparse Model Averaging](https://arxiv.org/html/2605.20866v1) — arXiv:2605.20866v1；first-public 2026-05-20；accessed 2026-09-01
- [Runtime-Certified Bounded-Error Quantized Attention](https://arxiv.org/html/2605.20868v1) — arXiv:2605.20868v1；first-public 2026-05-20；accessed 2026-09-01
- [Governance by Construction for Generalist Agents](https://arxiv.org/html/2605.20874v1) — arXiv:2605.20874v1；first-public 2026-05-20；accessed 2026-09-01
- [Terminal-World: Scaling Terminal-Agent Environments via Agent Skills](https://arxiv.org/html/2605.20876v1) — arXiv:2605.20876v1；first-public 2026-05-20；accessed 2026-09-01
- [Causal Past Logic for Runtime Verification of Distributed LLM Agent Workflows](https://arxiv.org/html/2605.20923v1) — arXiv:2605.20923v1；first-public 2026-05-20；accessed 2026-09-01
- [MemConflict: Evaluating Long-Term Memory Systems Under Memory Conflicts](https://arxiv.org/html/2605.20926v1) — arXiv:2605.20926v1；first-public 2026-05-20；accessed 2026-09-01
- [Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory](https://arxiv.org/html/2605.20948v1) — arXiv:2605.20948v1；first-public 2026-05-20；accessed 2026-09-01
- [Grounding Driving VLA via Inverse Kinematics](https://arxiv.org/html/2605.21061v1) — arXiv:2605.21061v1；first-public 2026-05-20；accessed 2026-09-01
- [NanoCP: Request-Level Dynamic Context Parallelism for Data-Expert Parallel Decoding](https://arxiv.org/html/2605.21100v1) — arXiv:2605.21100v1；first-public 2026-05-20；accessed 2026-09-01
- [A Typed Tensor Language for Federated Learning](https://arxiv.org/html/2605.21103v1) — arXiv:2605.21103v1；first-public 2026-05-20；accessed 2026-09-01
- [Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation](https://arxiv.org/html/2605.21125v1) — arXiv:2605.21125v1；first-public 2026-05-20；accessed 2026-09-01
- [Reasoning-Trace Collapse: Evaluating the Loss of Explicit Reasoning During Fine-Tuning](https://arxiv.org/html/2605.21127v1) — arXiv:2605.21127v1；first-public 2026-05-20；accessed 2026-09-01
- [ChunkFT: Byte-Streamed Optimization for Memory-Efficient Full Fine-Tuning](https://arxiv.org/html/2605.21177v1) — arXiv:2605.21177v1；first-public 2026-05-20；accessed 2026-09-01
- [High-speed Networking for Giga-Scale AI Factories](https://arxiv.org/html/2605.21187v1) — arXiv:2605.21187v1；first-public 2026-05-20；accessed 2026-09-01
- [How Much Online RL is Enough? Informative Rollouts for Offline Preference Optimization in RLVR](https://arxiv.org/html/2605.21266v1) — arXiv:2605.21266v1；first-public 2026-05-20；accessed 2026-09-01
- [DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions](https://arxiv.org/html/2605.21273v1) — arXiv:2605.21273v1；first-public 2026-05-20；accessed 2026-09-01
- [Frontier: Towards Comprehensive and Accurate LLM Inference Simulation](https://arxiv.org/html/2605.21312v1) — arXiv:2605.21312v1；first-public 2026-05-20；accessed 2026-09-01
- [Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents](https://arxiv.org/html/2605.21347v1) — arXiv:2605.21347v1；first-public 2026-05-20；accessed 2026-09-01
- [SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents](https://arxiv.org/html/2605.21384v1) — arXiv:2605.21384v1；first-public 2026-05-20；accessed 2026-09-01
- [VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers](https://arxiv.org/html/2605.21392v1) — arXiv:2605.21392v1；first-public 2026-05-20；accessed 2026-09-01
- [PALS: Power-Aware LLM Serving for Mixture-of-Experts Models](https://arxiv.org/html/2605.21427v1) — arXiv:2605.21427v1；first-public 2026-05-20；accessed 2026-09-01
- [Agentic Model Checking](https://arxiv.org/html/2605.21434v1) — arXiv:2605.21434v1；first-public 2026-05-20；accessed 2026-09-01
- [Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs](https://arxiv.org/html/2605.21446v1) — arXiv:2605.21446v1；first-public 2026-05-20；accessed 2026-09-01
- [DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from Verifiable Rewards](https://arxiv.org/html/2605.21467v1) — arXiv:2605.21467v1；first-public 2026-05-20；accessed 2026-09-01
- [You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories](https://arxiv.org/html/2605.21468v1) — arXiv:2605.21468v1；first-public 2026-05-20；accessed 2026-09-01
- [Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling](https://arxiv.org/html/2605.21470v1) — arXiv:2605.21470v1；first-public 2026-05-20；accessed 2026-09-01
- [DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation](https://arxiv.org/html/2605.21482v1) — arXiv:2605.21482v1；first-public 2026-05-20；accessed 2026-09-01
- [Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate](https://arxiv.org/html/2605.21486v1) — arXiv:2605.21486v1；first-public 2026-05-20；accessed 2026-09-01
- [Provable Joint Decontamination for Benchmarking Multiple Large Language Models](https://arxiv.org/html/2605.21543v1) — arXiv:2605.21543v1；first-public 2026-05-20；accessed 2026-09-01
- [Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs](https://arxiv.org/html/2605.21602v1) — arXiv:2605.21602v1；first-public 2026-05-20；accessed 2026-09-01
- [DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling](https://arxiv.org/html/2605.21603v1) — arXiv:2605.21603v1；first-public 2026-05-20；accessed 2026-09-01
- [When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning](https://arxiv.org/html/2605.21606v1) — arXiv:2605.21606v1；first-public 2026-05-20；accessed 2026-09-01
- [Ablate-to-Validate: Are Vision-Language Models Really Using Continuous Thought Tokens?](https://arxiv.org/html/2605.21642v1) — arXiv:2605.21642v1；first-public 2026-05-20；accessed 2026-09-01
- [Dropout Universality: Scaling Laws and Optimal Scheduling at the Edge-of-Chaos](https://arxiv.org/html/2605.21648v1) — arXiv:2605.21648v1；first-public 2026-05-20；accessed 2026-09-01
- [EntmaxKV: Support-Aware Decoding for Entmax Attention](https://arxiv.org/html/2605.21649v1) — arXiv:2605.21649v1；first-public 2026-05-20；accessed 2026-09-01
- [Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents](https://arxiv.org/html/2605.21768v1) — arXiv:2605.21768v1；first-public 2026-05-20；accessed 2026-09-01
- [FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction](https://arxiv.org/html/2605.21779v1) — arXiv:2605.21779v1；first-public 2026-05-20；accessed 2026-09-01
- [stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation](https://arxiv.org/html/2605.21800v1) — arXiv:2605.21800v1；first-public 2026-05-20；accessed 2026-09-01
- [Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization](https://arxiv.org/html/2605.21801v1) — arXiv:2605.21801v1；first-public 2026-05-20；accessed 2026-09-01
- [Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws](https://arxiv.org/html/2605.21803v1) — arXiv:2605.21803v1；first-public 2026-05-20；accessed 2026-09-01
- [CompPow: A Case for Component-level GPU Power Management](https://arxiv.org/html/2605.21847v1) — arXiv:2605.21847v1；first-public 2026-05-20；accessed 2026-09-01
- [ACC: Compiling Agent Trajectories for Long-Context Training](https://arxiv.org/html/2605.21850v1) — arXiv:2605.21850v1；first-public 2026-05-20；accessed 2026-09-01
- [GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation](https://arxiv.org/html/2605.22882v1) — arXiv:2605.22882v1；first-public 2026-05-20；accessed 2026-09-01
- [Energy per Successful Goal: Goal-Level Energy Accounting for Agentic AI Systems](https://arxiv.org/html/2605.22883v1) — arXiv:2605.22883v1；first-public 2026-05-20；accessed 2026-09-01
- [Tensor Cache: Eviction-conditioned Associative Memory for Transformers](https://arxiv.org/html/2605.22884v1) — arXiv:2605.22884v1；first-public 2026-05-20；accessed 2026-09-01
- [Adaptive KV Cache Reuse for Fast Long-Context LLM Serving](https://arxiv.org/html/2605.24022v1) — arXiv:2605.24022v1；first-public 2026-05-20；accessed 2026-09-01
- [The Constraint Tax: Measuring Validity-Correctness Tradeoffs in Structured Outputs for Small Language Models](https://arxiv.org/html/2605.26128v1) — arXiv:2605.26128v1；first-public 2026-05-20；accessed 2026-09-01
- [Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline](https://arxiv.org/html/2605.26132v1) — arXiv:2605.26132v1；first-public 2026-05-20；accessed 2026-09-01

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

独立 pre-write audit 已闭合；ordinary pending=0。15 项 Books 串行写回及不同 reviewer 的 post-write semantic audit 均已完成，15/15 通过，Daily 全链路闭合。
