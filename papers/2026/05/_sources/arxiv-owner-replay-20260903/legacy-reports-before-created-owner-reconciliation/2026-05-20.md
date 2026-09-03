# Daily Research — 2026-05-20

**Research Date:** 2026-05-20

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-19 09:00:00 ～ 2026-05-20 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；技术结论绑定 official arXiv exact-v1。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。47 项 root 串行写回已通过非写作者 post-write semantic audit。

## Executive Summary

从 91,841 条月度 raw records 中注册并独立重放 665/665 identity。author denominator 59 经审计移除 14 个 false positive、恢复 14 个 false negative，最终 59 项（8.87%），606 项以逐 family 唯一理由在分母前闭合。59/59 exact-v1 完成 source-specific Review，blocked=0。current owner 与相邻章节比较后冻结的 47 项 Books queue 已按 owner 合并写入正文，并通过非写作者 47/47 post-write semantic audit；`2605.22868` 继续作为 Structural Candidate，未被强塞进现有章节。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-20 |
| Window End | 2026-05-20 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260520-V2-INDEPENDENT |
| Denominator Frozen At | 2026-09-01T01:26:33.304643+00:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-19T09:00:00+08:00 | 2026-05-20T09:00:00+08:00 | 2026-09-01T01:26:33.304643+00:00 | DataCite v2 00..99 + independent 665/665 semantic replay + official exact-v1 | checked | 665 | SF-2026-ARXIV-2605-19240;SF-2026-ARXIV-2605-19242;SF-2026-ARXIV-2605-19262;SF-2026-ARXIV-2605-19269;SF-2026-ARXIV-2605-19276;SF-2026-ARXIV-2605-19282;SF-2026-ARXIV-2605-19314;SF-2026-ARXIV-2605-19319;SF-2026-ARXIV-2605-19321;SF-2026-ARXIV-2605-19328;SF-2026-ARXIV-2605-19335;SF-2026-ARXIV-2605-19341;SF-2026-ARXIV-2605-19407;SF-2026-ARXIV-2605-19444;SF-2026-ARXIV-2605-19447;SF-2026-ARXIV-2605-19461;SF-2026-ARXIV-2605-19478;SF-2026-ARXIV-2605-19481;SF-2026-ARXIV-2605-19537;SF-2026-ARXIV-2605-19576;SF-2026-ARXIV-2605-19593;SF-2026-ARXIV-2605-19604;SF-2026-ARXIV-2605-19722;SF-2026-ARXIV-2605-19769;SF-2026-ARXIV-2605-19775;SF-2026-ARXIV-2605-19779;SF-2026-ARXIV-2605-19811;SF-2026-ARXIV-2605-19847;SF-2026-ARXIV-2605-19893;SF-2026-ARXIV-2605-19932;SF-2026-ARXIV-2605-19945;SF-2026-ARXIV-2605-19952;SF-2026-ARXIV-2605-19999;SF-2026-ARXIV-2605-20005;SF-2026-ARXIV-2605-20022;SF-2026-ARXIV-2605-20023;SF-2026-ARXIV-2605-20051;SF-2026-ARXIV-2605-20061;SF-2026-ARXIV-2605-20084;SF-2026-ARXIV-2605-20179;SF-2026-ARXIV-2605-20295;SF-2026-ARXIV-2605-20296;SF-2026-ARXIV-2605-20312;SF-2026-ARXIV-2605-20314;SF-2026-ARXIV-2605-20315;SF-2026-ARXIV-2605-20402;SF-2026-ARXIV-2605-20477;SF-2026-ARXIV-2605-20485;SF-2026-ARXIV-2605-20490;SF-2026-ARXIV-2605-20520;SF-2026-ARXIV-2605-20544;SF-2026-ARXIV-2605-20548;SF-2026-ARXIV-2605-20563;SF-2026-ARXIV-2605-22863;SF-2026-ARXIV-2605-22866;SF-2026-ARXIV-2605-22868;SF-2026-ARXIV-2605-24004;SF-2026-ARXIV-2605-24006;SF-2026-ARXIV-2606-28330 | pages=300;final_cursor=end;raw=91841;registered=665;screened=665;retained=59;closure=606 | 2026-05-20T00:59:59Z | screening-ledger-independent-final.json#sha256=013fe33dc0ea5e363eb585cb7e7086d34516c2ae55a0509d28cd08cd2d92a1e8 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260520:start -->665/665 identity 已独立重放；606 个 closure reason 全部唯一。Coverage=Closed。所有 retained family 均完成 exact-v1；没有 access blocker。<!-- coverage:SRC-ARXIV:20260520:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-19240 | arXiv:2605.19240v1 | paper-v1:2605.19240 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19240 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19240 | no |
| SF-2026-ARXIV-2605-19242 | arXiv:2605.19242v1 | paper-v1:2605.19242 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19242 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19242 | no |
| SF-2026-ARXIV-2605-19262 | arXiv:2605.19262v1 | paper-v1:2605.19262 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19262 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19262 | no |
| SF-2026-ARXIV-2605-19269 | arXiv:2605.19269v1 | paper-v1:2605.19269 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19269 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-19269 | no |
| SF-2026-ARXIV-2605-19276 | arXiv:2605.19276v1 | paper-v1:2605.19276 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19276 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19276 | no |
| SF-2026-ARXIV-2605-19282 | arXiv:2605.19282v1 | paper-v1:2605.19282 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19282 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-19282 | no |
| SF-2026-ARXIV-2605-19314 | arXiv:2605.19314v1 | paper-v1:2605.19314 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19314 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-19314 | no |
| SF-2026-ARXIV-2605-19319 | arXiv:2605.19319v1 | paper-v1:2605.19319 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19319 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2605-19319 | no |
| SF-2026-ARXIV-2605-19321 | arXiv:2605.19321v1 | paper-v1:2605.19321 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19321 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19321 | no |
| SF-2026-ARXIV-2605-19328 | arXiv:2605.19328v1 | paper-v1:2605.19328 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19328 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19328 | no |
| SF-2026-ARXIV-2605-19335 | arXiv:2605.19335v1 | paper-v1:2605.19335 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19335 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-19335 | no |
| SF-2026-ARXIV-2605-19341 | arXiv:2605.19341v1 | paper-v1:2605.19341 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19341 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19341 | no |
| SF-2026-ARXIV-2605-19407 | arXiv:2605.19407v1 | paper-v1:2605.19407 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19407 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-19407 | no |
| SF-2026-ARXIV-2605-19444 | arXiv:2605.19444v1 | paper-v1:2605.19444 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19444 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-19444 | no |
| SF-2026-ARXIV-2605-19447 | arXiv:2605.19447v1 | paper-v1:2605.19447 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19447 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-19447 | no |
| SF-2026-ARXIV-2605-19461 | arXiv:2605.19461v1 | paper-v1:2605.19461 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19461 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-19461 | no |
| SF-2026-ARXIV-2605-19478 | arXiv:2605.19478v1 | paper-v1:2605.19478 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19478 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19478 | no |
| SF-2026-ARXIV-2605-19481 | arXiv:2605.19481v1 | paper-v1:2605.19481 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19481 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Integrate | books-review:SF-2026-ARXIV-2605-19481 | no |
| SF-2026-ARXIV-2605-19537 | arXiv:2605.19537v1 | paper-v1:2605.19537 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19537 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-19537 | no |
| SF-2026-ARXIV-2605-19576 | arXiv:2605.19576v1 | paper-v1:2605.19576 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19576 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-19576 | no |
| SF-2026-ARXIV-2605-19593 | arXiv:2605.19593v1 | paper-v1:2605.19593 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19593 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-19593 | no |
| SF-2026-ARXIV-2605-19604 | arXiv:2605.19604v1 | paper-v1:2605.19604 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19604 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-19604 | no |
| SF-2026-ARXIV-2605-19722 | arXiv:2605.19722v1 | paper-v1:2605.19722 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19722 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19722 | no |
| SF-2026-ARXIV-2605-19769 | arXiv:2605.19769v1 | paper-v1:2605.19769 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19769 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19769 | no |
| SF-2026-ARXIV-2605-19775 | arXiv:2605.19775v1 | paper-v1:2605.19775 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19775 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19775 | no |
| SF-2026-ARXIV-2605-19779 | arXiv:2605.19779v1 | paper-v1:2605.19779 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19779 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-19779 | no |
| SF-2026-ARXIV-2605-19811 | arXiv:2605.19811v1 | paper-v1:2605.19811 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19811 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-19811 | no |
| SF-2026-ARXIV-2605-19847 | arXiv:2605.19847v1 | paper-v1:2605.19847 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19847 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19847 | no |
| SF-2026-ARXIV-2605-19893 | arXiv:2605.19893v1 | paper-v1:2605.19893 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19893 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-19893 | no |
| SF-2026-ARXIV-2605-19932 | arXiv:2605.19932v1 | paper-v1:2605.19932 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19932 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-19932 | no |
| SF-2026-ARXIV-2605-19945 | arXiv:2605.19945v1 | paper-v1:2605.19945 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19945 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-19945 | no |
| SF-2026-ARXIV-2605-19952 | arXiv:2605.19952v1 | paper-v1:2605.19952 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19952 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-19952 | no |
| SF-2026-ARXIV-2605-19999 | arXiv:2605.19999v1 | paper-v1:2605.19999 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19999 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19999 | no |
| SF-2026-ARXIV-2605-20005 | arXiv:2605.20005v1 | paper-v1:2605.20005 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20005 | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-ARXIV-2605-20005 | no |
| SF-2026-ARXIV-2605-20022 | arXiv:2605.20022v1 | paper-v1:2605.20022 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20022 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-20022 | no |
| SF-2026-ARXIV-2605-20023 | arXiv:2605.20023v1 | paper-v1:2605.20023 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20023 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20023 | no |
| SF-2026-ARXIV-2605-20051 | arXiv:2605.20051v1 | paper-v1:2605.20051 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20051 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-20051 | no |
| SF-2026-ARXIV-2605-20061 | arXiv:2605.20061v1 | paper-v1:2605.20061 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20061 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-20061 | no |
| SF-2026-ARXIV-2605-20084 | arXiv:2605.20084v1 | paper-v1:2605.20084 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20084 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-20084 | no |
| SF-2026-ARXIV-2605-20179 | arXiv:2605.20179v1 | paper-v1:2605.20179 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20179 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-20179 | no |
| SF-2026-ARXIV-2605-20295 | arXiv:2605.20295v1 | paper-v1:2605.20295 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20295 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-20295 | no |
| SF-2026-ARXIV-2605-20296 | arXiv:2605.20296v1 | paper-v1:2605.20296 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20296 | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-ARXIV-2605-20296 | no |
| SF-2026-ARXIV-2605-20312 | arXiv:2605.20312v1 | paper-v1:2605.20312 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20312 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2605-20312 | no |
| SF-2026-ARXIV-2605-20314 | arXiv:2605.20314v1 | paper-v1:2605.20314 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20314 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-20314 | no |
| SF-2026-ARXIV-2605-20315 | arXiv:2605.20315v1 | paper-v1:2605.20315 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20315 | self | — | new_in_window | INFER-PD-DISAGGREGATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20315 | no |
| SF-2026-ARXIV-2605-20402 | arXiv:2605.20402v1 | paper-v1:2605.20402 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20402 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-20402 | no |
| SF-2026-ARXIV-2605-20477 | arXiv:2605.20477v1 | paper-v1:2605.20477 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20477 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-20477 | no |
| SF-2026-ARXIV-2605-20485 | arXiv:2605.20485v1 | paper-v1:2605.20485 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20485 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-20485 | no |
| SF-2026-ARXIV-2605-20490 | arXiv:2605.20490v1 | paper-v1:2605.20490 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20490 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-20490 | no |
| SF-2026-ARXIV-2605-20520 | arXiv:2605.20520v1 | paper-v1:2605.20520 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20520 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-20520 | no |
| SF-2026-ARXIV-2605-20544 | arXiv:2605.20544v1 | paper-v1:2605.20544 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20544 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-20544 | no |
| SF-2026-ARXIV-2605-20548 | arXiv:2605.20548v1 | paper-v1:2605.20548 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20548 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20548 | no |
| SF-2026-ARXIV-2605-20563 | arXiv:2605.20563v1 | paper-v1:2605.20563 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20563 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-20563 | no |
| SF-2026-ARXIV-2605-22863 | arXiv:2605.22863v1 | paper-v1:2605.22863 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22863 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-22863 | no |
| SF-2026-ARXIV-2605-22866 | arXiv:2605.22866v1 | paper-v1:2605.22866 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22866 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-22866 | no |
| SF-2026-ARXIV-2605-22868 | arXiv:2605.22868v1 | paper-v1:2605.22868 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22868 | self | — | new_in_window | — | Structural Candidate | books-review:SF-2026-ARXIV-2605-22868 | no |
| SF-2026-ARXIV-2605-24004 | arXiv:2605.24004v1 | paper-v1:2605.24004 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24004 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-24004 | no |
| SF-2026-ARXIV-2605-24006 | arXiv:2605.24006v1 | paper-v1:2605.24006 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24006 | self | — | new_in_window | TRAIN-PIPELINE-PARALLEL | Integrate | books-review:SF-2026-ARXIV-2605-24006 | no |
| SF-2026-ARXIV-2606-28330 | arXiv:2606.28330v1 | paper-v1:2606.28330 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-28330 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-28330 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-19240 | RP-4de7916633823656 | deep | arXiv:2605.19240v1 | SRC-ARXIV@arXiv:2605.19240v1 | arXiv:2605.19240v1 HTML — §4.1–4.4 causal cross-channel monitoring | arXiv:2605.19240v1 HTML — §5 detection and attribution evaluation | arXiv:2605.19240v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19240v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19240 | complete |
| SF-2026-ARXIV-2605-19242 | RP-bc66eb851cc20588 | deep | arXiv:2605.19242v1 | SRC-ARXIV@arXiv:2605.19242v1 | arXiv:2605.19242v1 HTML — §3 physics-faithful data and objective | arXiv:2605.19242v1 HTML — §4 controlled video/world-model evaluation | arXiv:2605.19242v1 HTML — §5 Conclusion and inherited generator biases | https://arxiv.org/html/2605.19242v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19242 | complete |
| SF-2026-ARXIV-2605-19262 | RP-5a772c65a8c3c199 | deep | arXiv:2605.19262v1 | SRC-ARXIV@arXiv:2605.19262v1 | arXiv:2605.19262v1 HTML — §4 masked-diffusion backdoor construction | arXiv:2605.19262v1 HTML — §5 attack and defense experiments | arXiv:2605.19262v1 HTML — Appendix A Limitations | https://arxiv.org/html/2605.19262v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19262 | complete |
| SF-2026-ARXIV-2605-19269 | RP-c96f6605cb2f6e46 | deep | arXiv:2605.19269v1 | SRC-ARXIV@arXiv:2605.19269v1 | arXiv:2605.19269v1 HTML — §3 GEMM-epilogue program representation | arXiv:2605.19269v1 HTML — §4 kernel and end-to-end evaluation | arXiv:2605.19269v1 HTML — §5 limitations and portability boundary | https://arxiv.org/html/2605.19269v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19269 | complete |
| SF-2026-ARXIV-2605-19276 | RP-bbd40a725e79e647 | deep | arXiv:2605.19276v1 | SRC-ARXIV@arXiv:2605.19276v1 | arXiv:2605.19276v1 HTML — §3.1–3.5 evaluation-platform architecture | arXiv:2605.19276v1 HTML — §4 benchmark execution and comparison | arXiv:2605.19276v1 HTML — §5 Future Works | https://arxiv.org/html/2605.19276v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19276 | complete |
| SF-2026-ARXIV-2605-19282 | RP-2a2084963c482440 | deep | arXiv:2605.19282v1 | SRC-ARXIV@arXiv:2605.19282v1 | arXiv:2605.19282v1 HTML — §3 spectral failure analysis; §4 high-pass remedy | arXiv:2605.19282v1 HTML — §5 VLA/RLVR optimization experiments | arXiv:2605.19282v1 HTML — Appendix M Limitations | https://arxiv.org/html/2605.19282v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19282 | complete |
| SF-2026-ARXIV-2605-19314 | RP-2cbc2c4c9f3e9bf9 | deep | arXiv:2605.19314v1 | SRC-ARXIV@arXiv:2605.19314v1 | arXiv:2605.19314v1 HTML — §3 hierarchical task-state alignment | arXiv:2605.19314v1 HTML — §4.1–4.4 long-horizon embodied evaluation | arXiv:2605.19314v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19314v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19314 | complete |
| SF-2026-ARXIV-2605-19319 | RP-5e77ad5261b0bf4f | deep | arXiv:2605.19319v1 | SRC-ARXIV@arXiv:2605.19319v1 | arXiv:2605.19319v1 HTML — §3 sparse keyframe world-model planner and goal-conditioned action predictor | arXiv:2605.19319v1 HTML — §4 real-robot and simulation experiments | arXiv:2605.19319v1 HTML — §5 Limitations: short horizon, annotations and edited-image domain gap | https://arxiv.org/html/2605.19319v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19319 | complete |
| SF-2026-ARXIV-2605-19321 | RP-d33cdabd99e9957c | deep | arXiv:2605.19321v1 | SRC-ARXIV@arXiv:2605.19321v1 | arXiv:2605.19321v1 HTML — §3 draft-model pre-guard design | arXiv:2605.19321v1 HTML — §6 jailbreak and latency evaluation | arXiv:2605.19321v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19321v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19321 | complete |
| SF-2026-ARXIV-2605-19328 | RP-a5c0a05c1cd5ca31 | deep | arXiv:2605.19328v1 | SRC-ARXIV@arXiv:2605.19328v1 | arXiv:2605.19328v1 HTML — §3 embodied-agent threat and benchmark protocol | arXiv:2605.19328v1 HTML — §4 attacks and defenses | arXiv:2605.19328v1 HTML — §5 Limitations | https://arxiv.org/html/2605.19328v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19328 | complete |
| SF-2026-ARXIV-2605-19335 | RP-4d11184eb7d065fd | deep | arXiv:2605.19335v1 | SRC-ARXIV@arXiv:2605.19335v1 | arXiv:2605.19335v1 HTML — §4 LIOS update decomposition, overrun-bounded budgeting and feedback control | arXiv:2605.19335v1 HTML — §6 search/update evaluation on FreshDiskANN and OdinANN | arXiv:2605.19335v1 HTML — §8 Conclusion; disk ANNS and measured hardware scope | https://arxiv.org/html/2605.19335v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19335 | complete |
| SF-2026-ARXIV-2605-19341 | RP-38bfb8462e1788ff | deep | arXiv:2605.19341v1 | SRC-ARXIV@arXiv:2605.19341v1 | arXiv:2605.19341v1 HTML — §3.1–3.3 controlled reference-world benchmark | arXiv:2605.19341v1 HTML — §4 cross-context hallucination experiments | arXiv:2605.19341v1 HTML — §5 Discussion; controlled-world boundary | https://arxiv.org/html/2605.19341v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19341 | complete |
| SF-2026-ARXIV-2605-19407 | RP-231b13021875ae63 | deep | arXiv:2605.19407v1 | SRC-ARXIV@arXiv:2605.19407v1 | arXiv:2605.19407v1 HTML — §3–§6 compute/data/filter scaling design | arXiv:2605.19407v1 HTML — §6–§7 scaling experiments | arXiv:2605.19407v1 HTML — §8 Discussion and scope boundary | https://arxiv.org/html/2605.19407v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19407 | complete |
| SF-2026-ARXIV-2605-19444 | RP-e2adfa9f6bdc8469 | deep | arXiv:2605.19444v1 | SRC-ARXIV@arXiv:2605.19444v1 | arXiv:2605.19444v1 HTML — §2 extinction-window dynamics; §3 TTRL-Guard | arXiv:2605.19444v1 HTML — §4 model/benchmark experiments and per-problem migration | arXiv:2605.19444v1 HTML — §6 Breadth of evaluation; signal quality at the extremes | https://arxiv.org/html/2605.19444v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19444 | complete |
| SF-2026-ARXIV-2605-19447 | RP-79adcf64a80e6d6d | deep | arXiv:2605.19447v1 | SRC-ARXIV@arXiv:2605.19447v1 | arXiv:2605.19447v1 HTML — §3 selective hindsight placement and environment-guided advantage reweighting | arXiv:2605.19447v1 HTML — §4 ALFWorld/WebShop experiments and ablations | arXiv:2605.19447v1 HTML — Appendix C Limitations | https://arxiv.org/html/2605.19447v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19447 | complete |
| SF-2026-ARXIV-2605-19461 | RP-487abf8826107f40 | deep | arXiv:2605.19461v1 | SRC-ARXIV@arXiv:2605.19461v1 | arXiv:2605.19461v1 HTML — §3 forward/group distribution-matching policy optimization | arXiv:2605.19461v1 HTML — §4–§5 reasoning experiments and ablations | arXiv:2605.19461v1 HTML — Appendix B Limitations; group-local coverage does not prove global target matching | https://arxiv.org/html/2605.19461v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19461 | complete |
| SF-2026-ARXIV-2605-19478 | RP-364a9e53a3f33227 | deep | arXiv:2605.19478v1 | SRC-ARXIV@arXiv:2605.19478v1 | arXiv:2605.19478v1 HTML — §4 threat model; §5–§6 dynamic-prompt functional fusion | arXiv:2605.19478v1 HTML — §7 attack, pruning and transfer evaluation | arXiv:2605.19478v1 HTML — §8 Conclusion; ViT/VPT threat-model boundary | https://arxiv.org/html/2605.19478v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19478 | complete |
| SF-2026-ARXIV-2605-19481 | RP-c5cf1a54d2cf261f | deep | arXiv:2605.19481v1 | SRC-ARXIV@arXiv:2605.19481v1 | arXiv:2605.19481v1 HTML — §III–V C2C weight/state movement design | arXiv:2605.19481v1 HTML — §VI MIG/serverless serving evaluation | arXiv:2605.19481v1 HTML — §VII Conclusion and hardware boundary | https://arxiv.org/html/2605.19481v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19481 | complete |
| SF-2026-ARXIV-2605-19537 | RP-7c3307e883eee92e | deep | arXiv:2605.19537v1 | SRC-ARXIV@arXiv:2605.19537v1 | arXiv:2605.19537v1 HTML — §3 backend-reproducibility protocol | arXiv:2605.19537v1 HTML — §4 backend/model benchmark deltas | arXiv:2605.19537v1 HTML — §5 Discussion and reproducibility boundary | https://arxiv.org/html/2605.19537v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19537 | complete |
| SF-2026-ARXIV-2605-19576 | RP-a9ccb737bed9e193 | deep | arXiv:2605.19576v1 | SRC-ARXIV@arXiv:2605.19576v1 | arXiv:2605.19576v1 HTML — §3–§5 lifecycle-managed skill library | arXiv:2605.19576v1 HTML — §6 library-drift evaluation | arXiv:2605.19576v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19576v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19576 | complete |
| SF-2026-ARXIV-2605-19593 | RP-0f47708fa3dff185 | deep | arXiv:2605.19593v1 | SRC-ARXIV@arXiv:2605.19593v1 | arXiv:2605.19593v1 HTML — §3 multi-model offload/preemption methodology | arXiv:2605.19593v1 HTML — §4–§5 heterogeneous-serving measurements | arXiv:2605.19593v1 HTML — §6 Conclusion; interconnect and hardware constraints | https://arxiv.org/html/2605.19593v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19593 | complete |
| SF-2026-ARXIV-2605-19604 | RP-fccbad05e0667a78 | deep | arXiv:2605.19604v1 | SRC-ARXIV@arXiv:2605.19604v1 | arXiv:2605.19604v1 HTML — §3 programmable runtime skill contract | arXiv:2605.19604v1 HTML — §4 execution and accuracy evaluation | arXiv:2605.19604v1 HTML — §5 Conclusion; language/runtime boundary | https://arxiv.org/html/2605.19604v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19604 | complete |
| SF-2026-ARXIV-2605-19722 | RP-5fd2a3cffdd101d8 | deep | arXiv:2605.19722v1 | SRC-ARXIV@arXiv:2605.19722v1 | arXiv:2605.19722v1 HTML — §3 trace-based autonomous security-agent protocol | arXiv:2605.19722v1 HTML — §4–§5 sandbox/tool-use evaluation | arXiv:2605.19722v1 HTML — §6 Limitations | https://arxiv.org/html/2605.19722v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19722 | complete |
| SF-2026-ARXIV-2605-19769 | RP-abeedde730e8f1d5 | deep | arXiv:2605.19769v1 | SRC-ARXIV@arXiv:2605.19769v1 | arXiv:2605.19769v1 HTML — §2–§3 verifier-grounded software worlds | arXiv:2605.19769v1 HTML — §4.1 computer-use agent evaluation | arXiv:2605.19769v1 HTML — § unnumbered exact heading ‘Limitations and Future Work’ | https://arxiv.org/html/2605.19769v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19769 | complete |
| SF-2026-ARXIV-2605-19775 | RP-cb624bce171b6667 | deep | arXiv:2605.19775v1 | SRC-ARXIV@arXiv:2605.19775v1 | arXiv:2605.19775v1 HTML — §2–§3 inference-scaling model | arXiv:2605.19775v1 HTML — §4–§5 reasoning-workload measurements | arXiv:2605.19775v1 HTML — §6 Conclusions and disclosed scope | https://arxiv.org/html/2605.19775v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19775 | complete |
| SF-2026-ARXIV-2605-19779 | RP-9170e3bce78cea00 | deep | arXiv:2605.19779v1 | SRC-ARXIV@arXiv:2605.19779v1 | arXiv:2605.19779v1 HTML — §2–§3 conformal continuous-agent UQ | arXiv:2605.19779v1 HTML — §4 longitudinal agent studies | arXiv:2605.19779v1 HTML — §5 Limitations: bounded shift and dependence | https://arxiv.org/html/2605.19779v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19779 | complete |
| SF-2026-ARXIV-2605-19811 | RP-73b18d970281f078 | deep | arXiv:2605.19811v1 | SRC-ARXIV@arXiv:2605.19811v1 | arXiv:2605.19811v1 HTML — §3 optimizer geometry; §4 LionMuon alternating spectral/sign descent | arXiv:2605.19811v1 HTML — §5 language-model training experiments and ablations | arXiv:2605.19811v1 HTML — §6 Limitations and optimizer/workload boundary | https://arxiv.org/html/2605.19811v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19811 | complete |
| SF-2026-ARXIV-2605-19847 | RP-1aad2db51346f336 | deep | arXiv:2605.19847v1 | SRC-ARXIV@arXiv:2605.19847v1 | arXiv:2605.19847v1 HTML — §2–§3 collusion threat model and tenant accounting | arXiv:2605.19847v1 HTML — §4 privacy audit; §5 protocol | arXiv:2605.19847v1 HTML — §7.1 Limitations: retrieval only, not generation | https://arxiv.org/html/2605.19847v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19847 | complete |
| SF-2026-ARXIV-2605-19893 | RP-443e8b0329a419a2 | deep | arXiv:2605.19893v1 | SRC-ARXIV@arXiv:2605.19893v1 | arXiv:2605.19893v1 HTML — §3–§4 sparse speculative verification | arXiv:2605.19893v1 HTML — §5 long-context evaluation | arXiv:2605.19893v1 HTML — §6 Conclusion and sparse-attention boundary | https://arxiv.org/html/2605.19893v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19893 | complete |
| SF-2026-ARXIV-2605-19932 | RP-26b2069b16f34d38 | deep | arXiv:2605.19932v1 | SRC-ARXIV@arXiv:2605.19932v1 | arXiv:2605.19932v1 HTML — §3 orientation-cache representation | arXiv:2605.19932v1 HTML — §4 recurring-context agent evaluation | arXiv:2605.19932v1 HTML — §5 Limitations | https://arxiv.org/html/2605.19932v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19932 | complete |
| SF-2026-ARXIV-2605-19945 | RP-3896ccf40dc4ab6d | deep | arXiv:2605.19945v1 | SRC-ARXIV@arXiv:2605.19945v1 | arXiv:2605.19945v1 HTML — §3–§4 variability-aware expert placement | arXiv:2605.19945v1 HTML — §5 heterogeneous-GPU evaluation | arXiv:2605.19945v1 HTML — §6 Limitations | https://arxiv.org/html/2605.19945v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19945 | complete |
| SF-2026-ARXIV-2605-19952 | RP-a53c47202f099e7a | deep | arXiv:2605.19952v1 | SRC-ARXIV@arXiv:2605.19952v1 | arXiv:2605.19952v1 HTML — §3 trace/chunk memory representation | arXiv:2605.19952v1 HTML — §4 lifelong-memory evaluation | arXiv:2605.19952v1 HTML — Appendix C.1 Limitations | https://arxiv.org/html/2605.19952v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19952 | complete |
| SF-2026-ARXIV-2605-19999 | RP-f5326dc8eaa49252 | deep | arXiv:2605.19999v1 | SRC-ARXIV@arXiv:2605.19999v1 | arXiv:2605.19999v1 HTML — §3–§4 contamination-resistant benchmark construction | arXiv:2605.19999v1 HTML — §5 benchmark analysis | arXiv:2605.19999v1 HTML — § unnumbered exact heading ‘Limitations’: contamination detection and task scope | https://arxiv.org/html/2605.19999v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19999 | complete |
| SF-2026-ARXIV-2605-20005 | RP-11cbff9a3b48da86 | deep | arXiv:2605.20005v1 | SRC-ARXIV@arXiv:2605.20005v1 | arXiv:2605.20005v1 HTML — §3 per-step forgetting bound and loss-adaptive learning rate | arXiv:2605.20005v1 HTML — §4–§5 task/forgetting, factuality and calibration experiments | arXiv:2605.20005v1 HTML — §6 Conclusion, Limitations, and Future Work | https://arxiv.org/html/2605.20005v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20005 | complete |
| SF-2026-ARXIV-2605-20022 | RP-8ea859d9af48ceee | deep | arXiv:2605.20022v1 | SRC-ARXIV@arXiv:2605.20022v1 | arXiv:2605.20022v1 HTML — §3–§4 asynchronous flexible drafting | arXiv:2605.20022v1 HTML — §5 end-to-end evaluation | arXiv:2605.20022v1 HTML — §6 Conclusion: bonus-token and accepted-length uncertainty | https://arxiv.org/html/2605.20022v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20022 | complete |
| SF-2026-ARXIV-2605-20023 | RP-bf3892f84b15bf42 | deep | arXiv:2605.20023v1 | SRC-ARXIV@arXiv:2605.20023v1 | arXiv:2605.20023v1 HTML — §3 procedural-skill intervention and tool-grounded agent protocol | arXiv:2605.20023v1 HTML — §4 offensive-cybersecurity experiments | arXiv:2605.20023v1 HTML — §5 Limitations; negative result is workload/model specific | https://arxiv.org/html/2605.20023v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20023 | complete |
| SF-2026-ARXIV-2605-20051 | RP-6480603c921c3a94 | deep | arXiv:2605.20051v1 | SRC-ARXIV@arXiv:2605.20051v1 | arXiv:2605.20051v1 HTML — §3–§4 reference-driven variant detection | arXiv:2605.20051v1 HTML — §5 AI-infra repository measurement | arXiv:2605.20051v1 HTML — §6 Discussion and false-positive boundary | https://arxiv.org/html/2605.20051v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20051 | complete |
| SF-2026-ARXIV-2605-20061 | RP-0d3da93c05663e30 | deep | arXiv:2605.20061v1 | SRC-ARXIV@arXiv:2605.20061v1 | arXiv:2605.20061v1 HTML — §3 belief-consistency credit assignment | arXiv:2605.20061v1 HTML — §4 long-horizon agent evaluation | arXiv:2605.20061v1 HTML — Appendix C Limitations | https://arxiv.org/html/2605.20061v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20061 | complete |
| SF-2026-ARXIV-2605-20084 | RP-d18ad7b1d473540d | deep | arXiv:2605.20084v1 | SRC-ARXIV@arXiv:2605.20084v1 | arXiv:2605.20084v1 HTML — §3–§4 joint escalation/abstention calibration | arXiv:2605.20084v1 HTML — §5 cascaded-RAG evaluation | arXiv:2605.20084v1 HTML — § unnumbered exact heading ‘Limitations’: distribution shift and calibration | https://arxiv.org/html/2605.20084v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20084 | complete |
| SF-2026-ARXIV-2605-20179 | RP-ac18ffca87654a07 | deep | arXiv:2605.20179v1 | SRC-ARXIV@arXiv:2605.20179v1 | arXiv:2605.20179v1 HTML — §3 I/O-aware MoE expert-offload design | arXiv:2605.20179v1 HTML — §4 LLaDA2.0 experiments | arXiv:2605.20179v1 HTML — §5 Conclusion: block-only activation and limited hardware | https://arxiv.org/html/2605.20179v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20179 | complete |
| SF-2026-ARXIV-2605-20295 | RP-7907d828a266cdc4 | deep | arXiv:2605.20295v1 | SRC-ARXIV@arXiv:2605.20295v1 | arXiv:2605.20295v1 HTML — §4 fully static NPU quantization | arXiv:2605.20295v1 HTML — §5 on-device NPU evaluation | arXiv:2605.20295v1 HTML — Appendix H Limitations | https://arxiv.org/html/2605.20295v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20295 | complete |
| SF-2026-ARXIV-2605-20296 | RP-a78d40cdbfd9bec7 | deep | arXiv:2605.20296v1 | SRC-ARXIV@arXiv:2605.20296v1 | arXiv:2605.20296v1 HTML — §3 checkpoint-delta spectral repair | arXiv:2605.20296v1 HTML — §4 fourteen-cell recovery/preservation evaluation | arXiv:2605.20296v1 HTML — §5 Limitations and conclusion | https://arxiv.org/html/2605.20296v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20296 | complete |
| SF-2026-ARXIV-2605-20312 | RP-d161bf7e0fb42648 | deep | arXiv:2605.20312v1 | SRC-ARXIV@arXiv:2605.20312v1 | arXiv:2605.20312v1 HTML — §2 claim primitives; §3 protocol composition | arXiv:2605.20312v1 HTML — §5 pilot; §6 formal properties | arXiv:2605.20312v1 HTML — §8 Limitations | https://arxiv.org/html/2605.20312v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20312 | complete |
| SF-2026-ARXIV-2605-20314 | RP-a0ae0ea6977a8b48 | deep | arXiv:2605.20314v1 | SRC-ARXIV@arXiv:2605.20314v1 | arXiv:2605.20314v1 HTML — §2 reuse setup; §3–§5 sampling-bias and relative-norm mechanism | arXiv:2605.20314v1 HTML — §5 empirical interventions; Appendix B | arXiv:2605.20314v1 HTML — §6 discussion: when data repetition is and is not helpful | https://arxiv.org/html/2605.20314v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20314 | complete |
| SF-2026-ARXIV-2605-20315 | RP-ee48aa55a836d1af | deep | arXiv:2605.20315v1 | SRC-ARXIV@arXiv:2605.20315v1 | arXiv:2605.20315v1 HTML — §3 quantized-prefill/precise-decode split | arXiv:2605.20315v1 HTML — §4 Experiments | arXiv:2605.20315v1 HTML — §5 Conclusion and hardware boundary | https://arxiv.org/html/2605.20315v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20315 | complete |
| SF-2026-ARXIV-2605-20402 | RP-b412da617cab60db | deep | arXiv:2605.20402v1 | SRC-ARXIV@arXiv:2605.20402v1 | arXiv:2605.20402v1 HTML — §5 MXFP4 error decomposition | arXiv:2605.20402v1 HTML — §6 RL quantization experiments | arXiv:2605.20402v1 HTML — §7 Limitations | https://arxiv.org/html/2605.20402v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20402 | complete |
| SF-2026-ARXIV-2605-20477 | RP-cc0b2ab7beac44c0 | deep | arXiv:2605.20477v1 | SRC-ARXIV@arXiv:2605.20477v1 | arXiv:2605.20477v1 HTML — §3–§4 reflection-learning pipeline | arXiv:2605.20477v1 HTML — §5 MiniHack/ALFWorld evaluation | arXiv:2605.20477v1 HTML — §5.3 Limitations | https://arxiv.org/html/2605.20477v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20477 | complete |
| SF-2026-ARXIV-2605-20485 | RP-cdd729450155237c | deep | arXiv:2605.20485v1 | SRC-ARXIV@arXiv:2605.20485v1 | arXiv:2605.20485v1 HTML — §3 budgeted model-orchestration policy | arXiv:2605.20485v1 HTML — §4–§5 zero-shot allocation evaluation | arXiv:2605.20485v1 HTML — §6 Limitations | https://arxiv.org/html/2605.20485v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20485 | complete |
| SF-2026-ARXIV-2605-20490 | RP-af05659cd7b58278 | deep | arXiv:2605.20490v1 | SRC-ARXIV@arXiv:2605.20490v1 | arXiv:2605.20490v1 HTML — §2–§3 ECUAS decision-theoretic metric family | arXiv:2605.20490v1 HTML — §4 evaluator and QA studies | arXiv:2605.20490v1 HTML — § unnumbered exact heading ‘Limitations’: equivalence evaluator and utility assumptions | https://arxiv.org/html/2605.20490v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20490 | complete |
| SF-2026-ARXIV-2605-20520 | RP-2557e71bb9ec40af | deep | arXiv:2605.20520v1 | SRC-ARXIV@arXiv:2605.20520v1 | arXiv:2605.20520v1 HTML — §2 open-world evaluation framework | arXiv:2605.20520v1 HTML — §3 case studies and capability evidence | arXiv:2605.20520v1 HTML — §2.4 Limitations: complements, not replaces, benchmarks | https://arxiv.org/html/2605.20520v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20520 | complete |
| SF-2026-ARXIV-2605-20544 | RP-5b9c06b480604db5 | deep | arXiv:2605.20544v1 | SRC-ARXIV@arXiv:2605.20544v1 | arXiv:2605.20544v1 HTML — §3 grounded abstention taxonomy and deterministic constraint pipeline | arXiv:2605.20544v1 HTML — §4 6,069-instruction embodied VLM evaluation | arXiv:2605.20544v1 HTML — §5 Discussion; guarantees remain conditional on scene extraction | https://arxiv.org/html/2605.20544v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20544 | complete |
| SF-2026-ARXIV-2605-20548 | RP-ea7bc358093853e1 | deep | arXiv:2605.20548v1 | SRC-ARXIV@arXiv:2605.20548v1 | arXiv:2605.20548v1 HTML — §3–§4 communication-content instrumentation | arXiv:2605.20548v1 HTML — §5 and Appendix C.2 occlusion evaluation | arXiv:2605.20548v1 HTML — §6 Limitations | https://arxiv.org/html/2605.20548v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20548 | complete |
| SF-2026-ARXIV-2605-20563 | RP-d3759ea7faaeb585 | deep | arXiv:2605.20563v1 | SRC-ARXIV@arXiv:2605.20563v1 | arXiv:2605.20563v1 HTML — §3–§4 state-management and annotation protocol | arXiv:2605.20563v1 HTML — §5 evaluation; Appendix A setup | arXiv:2605.20563v1 HTML — Appendix E Limitations | https://arxiv.org/html/2605.20563v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20563 | complete |
| SF-2026-ARXIV-2605-22863 | RP-cf5cd47f9c923eaf | deep | arXiv:2605.22863v1 | SRC-ARXIV@arXiv:2605.22863v1 | arXiv:2605.22863v1 HTML — §3 latent-cache communication interface | arXiv:2605.22863v1 HTML — §4 evaluation; Appendix C statistics | arXiv:2605.22863v1 HTML — §5 Limitations: checkpoint-specific retained layers | https://arxiv.org/html/2605.22863v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22863 | complete |
| SF-2026-ARXIV-2605-22866 | RP-2715d5653259d793 | deep | arXiv:2605.22866v1 | SRC-ARXIV@arXiv:2605.22866v1 | arXiv:2605.22866v1 HTML — §3 hierarchical online attribution | arXiv:2605.22866v1 HTML — §4 and Appendix A experiments | arXiv:2605.22866v1 HTML — §6 limitations and binary-outcome boundary | https://arxiv.org/html/2605.22866v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22866 | complete |
| SF-2026-ARXIV-2605-22868 | RP-d41dfe99a6de313e | deep | arXiv:2605.22868v1 | SRC-ARXIV@arXiv:2605.22868v1 | arXiv:2605.22868v1 HTML — §3 tri-stage near-sensor/fusion/edge control | arXiv:2605.22868v1 HTML — §4 quality–data–energy evaluation | arXiv:2605.22868v1 HTML — §5 Conclusion; dual-modality SynDrone boundary | https://arxiv.org/html/2605.22868v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22868 | complete |
| SF-2026-ARXIV-2605-24004 | RP-d1801b370072c775 | deep | arXiv:2605.24004v1 | SRC-ARXIV@arXiv:2605.24004v1 | arXiv:2605.24004v1 HTML — §III Reason–Imagine–Act world-model verification loop | arXiv:2605.24004v1 HTML — §IV CARLA closed-loop evaluation | arXiv:2605.24004v1 HTML — §V Conclusion; simulator and discrete-action-template boundary | https://arxiv.org/html/2605.24004v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-24004 | complete |
| SF-2026-ARXIV-2605-24006 | RP-a25cb3acf89adb37 | deep | arXiv:2605.24006v1 | SRC-ARXIV@arXiv:2605.24006v1 | arXiv:2605.24006v1 HTML — §III tabular schedule abstraction | arXiv:2605.24006v1 HTML — §IV communication-aware schedule experiments | arXiv:2605.24006v1 HTML — §V Conclusion and simulator boundary | https://arxiv.org/html/2605.24006v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-24006 | complete |
| SF-2026-ARXIV-2606-28330 | RP-1c328763fc6324f8 | deep | arXiv:2606.28330v1 | SRC-ARXIV@arXiv:2606.28330v1 | arXiv:2606.28330v1 HTML — PDF §II–§III concentration and retrieval metrics | arXiv:2606.28330v1 HTML — PDF §IV–§V synthetic and simplified RAG experiments | arXiv:2606.28330v1 HTML — PDF §VI–§VII: synthetic-only evidence and no production embedding validation | https://arxiv.org/html/2606.28330v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2606-28330 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-19240:start -->
#### CASPIAN: Online Detection and Attribution of Cascade Attacks in LLM Multi-Agent Systems via Cross-Channel Causal Monitoring

**问题与机制。** Therefore, we propose CASPIAN, the first framework that provides a unified, cross-channel causal analysis of cascade behavior in LLM-MAS through online monitoring of dynamic influence propagation across agents. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§4.1–4.4 causal cross-channel monitoring`；Evaluation=`§5 detection and attribution evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19240:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19240:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19240:end -->

<!-- review:SF-2026-ARXIV-2605-19242:start -->
#### PhyWorld: Physics-Faithful World Model for Video Generation

**问题与机制。** We propose PhyWorld, a video generation world model designed to produce temporally coherent and physically faithful scene continuations through two-stage post-training. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3 physics-faithful data and objective`；Evaluation=`§4 controlled video/world-model evaluation`；Limitations/Counterevidence=`§5 Conclusion and inherited generator biases`。

<!-- claim:SF-2026-ARXIV-2605-19242:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19242:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19242:end -->

<!-- review:SF-2026-ARXIV-2605-19262:start -->
#### Backdooring Masked Diffusion Language Models

**问题与机制。** In this work, we present the first systematic study of training-time backdoor attacks on MDLMs. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§4 masked-diffusion backdoor construction`；Evaluation=`§5 attack and defense experiments`；Limitations/Counterevidence=`Appendix A Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19262:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19262:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19262:end -->

<!-- review:SF-2026-ARXIV-2605-19269:start -->
#### CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs

**问题与机制。** We introduce CODA, a GPU kernel abstraction that expresses these computations as GEMM-plus-epilogue programs. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§3 GEMM-epilogue program representation`；Evaluation=`§4 kernel and end-to-end evaluation`；Limitations/Counterevidence=`§5 limitations and portability boundary`。

<!-- claim:SF-2026-ARXIV-2605-19269:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19269:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19269:end -->

<!-- review:SF-2026-ARXIV-2605-19276:start -->
#### OpenCompass: A Universal Evaluation Platform for Large Language Models

**问题与机制。** Adhering to the design philosophy of modularization and component decoupling, the platform boasts three core advantages: high compatibility, flexibility, and high concurrency. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3.1–3.5 evaluation-platform architecture`；Evaluation=`§4 benchmark execution and comparison`；Limitations/Counterevidence=`§5 Future Works`。

<!-- claim:SF-2026-ARXIV-2605-19276:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19276:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19276:end -->

<!-- review:SF-2026-ARXIV-2605-19282:start -->
#### Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR

**问题与机制。** While this uniform spectral whitening enhances exploration and outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA) training, where inherently low-rank action-module gradients cause amplification of noisy tail directions, and (ii) reinforcement learning with verifiable rewards (RLVR), where low-SNR gradients and the need to preserve per-head specialization from prior training make whitening unstable. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§3 spectral failure analysis; §4 high-pass remedy`；Evaluation=`§5 VLA/RLVR optimization experiments`；Limitations/Counterevidence=`Appendix M Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19282:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19282:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19282:end -->

<!-- review:SF-2026-ARXIV-2605-19314:start -->
#### ContextFlow: Hierarchical Task-State Alignment for Long-Horizon Embodied Agents

**问题与机制。** We study task-state misalignment, a task-level consistency failure in which the planner's active stage, runtime evidence, remembered context, and delegated executor no longer justify the same next-step decision. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 hierarchical task-state alignment`；Evaluation=`§4.1–4.4 long-horizon embodied evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19314:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19314:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19314:end -->

<!-- review:SF-2026-ARXIV-2605-19319:start -->
#### SWEET: Sparse World Modeling with Image Editing for Embodied Task Execution

**问题与机制。** In this work, we study whether image editing models can serve as sparse visual world models for robot manipulation by predicting task-level future states without dense video rollout. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3 sparse keyframe world-model planner and goal-conditioned action predictor`；Evaluation=`§4 real-robot and simulation experiments`；Limitations/Counterevidence=`§5 Limitations: short horizon, annotations and edited-image domain gap`。

<!-- claim:SF-2026-ARXIV-2605-19319:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19319:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19319:end -->

<!-- review:SF-2026-ARXIV-2605-19321:start -->
#### Exploring and Developing a Pre-Model Safeguard with Draft Models

**问题与机制。** In this paper, we introduce a safeguard design that leverages the transferability of jailbreak attacks to enforce prompt safety before target model inference. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 draft-model pre-guard design`；Evaluation=`§6 jailbreak and latency evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19321:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19321:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19321:end -->

<!-- review:SF-2026-ARXIV-2605-19328:start -->
#### RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents

**问题与机制。** We introduce an intent contrast dataset pipeline that augments existing datasets with paired adversarial and benign goals to measure both security and utility. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 embodied-agent threat and benchmark protocol`；Evaluation=`§4 attacks and defenses`；Limitations/Counterevidence=`§5 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19328:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19328:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19328:end -->

<!-- review:SF-2026-ARXIV-2605-19335:start -->
#### Leveraging I/O Stalls for Efficient Scheduling in ANNS

**问题与机制。** We present LIOS(Leverage I/O Stall), a framework that executes index updates inside search-side I/O stall windows. 系统 owner=`AGENT-RAG`。

**Exact-v1。** Method=`§4 LIOS update decomposition, overrun-bounded budgeting and feedback control`；Evaluation=`§6 search/update evaluation on FreshDiskANN and OdinANN`；Limitations/Counterevidence=`§8 Conclusion; disk ANNS and measured hardware scope`。

<!-- claim:SF-2026-ARXIV-2605-19335:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19335:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19335:end -->

<!-- review:SF-2026-ARXIV-2605-19341:start -->
#### HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models

**问题与机制。** To study root causes, we introduce HalluWorld, an extensible benchmark grounded in an explicit reference-world formulation: a model hallucinates when it produces an observable claim that is false with respect to this world. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3.1–3.3 controlled reference-world benchmark`；Evaluation=`§4 cross-context hallucination experiments`；Limitations/Counterevidence=`§5 Discussion; controlled-world boundary`。

<!-- claim:SF-2026-ARXIV-2605-19341:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19341:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19341:end -->

<!-- review:SF-2026-ARXIV-2605-19407:start -->
#### A Bitter Lesson for Data Filtering

**问题与机制。** We investigate data filtering for large model pretraining via new scaling studies that target the high compute, data-scarce regime. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§3–§6 compute/data/filter scaling design`；Evaluation=`§6–§7 scaling experiments`；Limitations/Counterevidence=`§8 Discussion and scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-19407:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19407:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19407:end -->

<!-- review:SF-2026-ARXIV-2605-19444:start -->
#### Detecting and Mitigating the Correct-Answer Extinction Window in Test-Time Reinforcement Learning with Majority Voting

**问题与机制。** We argue these gains are systematically misinterpreted: most reflect sharpening of already-solvable problems rather than genuine learning, while problems corrupted from correct to incorrect outnumber truly learned ones, and this damage is irreversible once majority vote locks onto a wrong answer. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§2 extinction-window dynamics; §3 TTRL-Guard`；Evaluation=`§4 model/benchmark experiments and per-problem migration`；Limitations/Counterevidence=`§6 Breadth of evaluation; signal quality at the extremes`。

<!-- claim:SF-2026-ARXIV-2605-19444:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19444:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19444:end -->

<!-- review:SF-2026-ARXIV-2605-19447:start -->
#### What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents

**问题与机制。** We systematically study five feedback sources and two insertion granularities and introduce SERL, a selective environment-reweighted learning framework. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 selective hindsight placement and environment-guided advantage reweighting`；Evaluation=`§4 ALFWorld/WebShop experiments and ablations`；Limitations/Counterevidence=`Appendix C Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19447:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19447:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19447:end -->

<!-- review:SF-2026-ARXIV-2605-19461:start -->
#### Beyond Mode Collapse: Distribution Matching for Diverse Reasoning

**问题与机制。** We show this stems from reverse KL minimization's mode-seeking behavior, which reinforces the first high-reward trajectory found rather than maintaining a distribution over multiple diverse solutions. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 forward/group distribution-matching policy optimization`；Evaluation=`§4–§5 reasoning experiments and ablations`；Limitations/Counterevidence=`Appendix B Limitations; group-local coverage does not prove global target matching`。

<!-- claim:SF-2026-ARXIV-2605-19461:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19461:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19461:end -->

<!-- review:SF-2026-ARXIV-2605-19478:start -->
#### Exposing Functional Fusion: A New Class of Strategic Backdoor in Dynamic Prompt Architectures

**问题与机制。** While adapter security has seen initial study, the risks of the burgeoning prompt-based ecosystem remain critically unexplored. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§4 threat model; §5–§6 dynamic-prompt functional fusion`；Evaluation=`§7 attack, pruning and transfer evaluation`；Limitations/Counterevidence=`§8 Conclusion; ViT/VPT threat-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-19478:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19478:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19478:end -->

<!-- review:SF-2026-ARXIV-2605-19481:start -->
#### C2CServe: Leveraging NVLink-C2C for Elastic Serverless LLM Serving on MIG

**问题与机制。** Leveraging this capability, we present C2CServe, a request-granularity serverless LLM serving system that allows MIG instances to switch models across requests without reloading weights into HBM. 系统 owner=`INFER-PD-DISAGGREGATION`。

**Exact-v1。** Method=`§III–V C2C weight/state movement design`；Evaluation=`§VI MIG/serverless serving evaluation`；Limitations/Counterevidence=`§VII Conclusion and hardware boundary`。

<!-- claim:SF-2026-ARXIV-2605-19481:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19481:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19481:end -->

<!-- review:SF-2026-ARXIV-2605-19537:start -->
#### The Silent Hyperparameter: Quantifying the Impact of Inference Backends on LLM Reproducibility

**问题与机制。** While critical for scalability, system-level optimizations, such as custom CUDA kernels and reduced-precision arithmetic, can alter token probabilities and introduce non-determinism, possibly cascading into divergent generation. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 backend-reproducibility protocol`；Evaluation=`§4 backend/model benchmark deltas`；Limitations/Counterevidence=`§5 Discussion and reproducibility boundary`。

<!-- claim:SF-2026-ARXIV-2605-19537:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19537:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19537:end -->

<!-- review:SF-2026-ARXIV-2605-19576:start -->
#### Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries

**问题与机制。** Self-evolving skill libraries face a silent failure mode we term \emph{library drift}: unbounded skill accumulation without outcome-driven lifecycle management causes retrieval degradation, false-positive injections, and performance stagnation. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3–§5 lifecycle-managed skill library`；Evaluation=`§6 library-drift evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19576:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19576:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19576:end -->

<!-- review:SF-2026-ARXIV-2605-19593:start -->
#### Towards Multi-Model LLM Schedulers: Empirical Insights into Offloading and Preemption

**问题与机制。** In this paper, we present an empirical study of how different LLMs behave across hardware platforms, focusing on the performance implications of layer offloading and preemption. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§3 multi-model offload/preemption methodology`；Evaluation=`§4–§5 heterogeneous-serving measurements`；Limitations/Counterevidence=`§6 Conclusion; interconnect and hardware constraints`。

<!-- claim:SF-2026-ARXIV-2605-19593:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19593:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19593:end -->

<!-- review:SF-2026-ARXIV-2605-19604:start -->
#### Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents

**问题与机制。** We introduce Formal Skill, a runtime-native abstraction that represents reusable capability with JSON metadata and action schemas, reliable Python executors, hook-governed control logic, Formal Skill routing, and skill-local runtime state. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 programmable runtime skill contract`；Evaluation=`§4 execution and accuracy evaluation`；Limitations/Counterevidence=`§5 Conclusion; language/runtime boundary`。

<!-- claim:SF-2026-ARXIV-2605-19604:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19604:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19604:end -->

<!-- review:SF-2026-ARXIV-2605-19722:start -->
#### Measuring Safety Alignment Effects in Autonomous Security Agents

**问题与机制。** We present a trace-based benchmark of 30 local vulnerability-analysis tasks with fixed tools, deterministic success predicates, redaction rules, and grounding checks, and compare four stock models against uncensored or abliterated derivatives: Gemma 4 31B, Gemma 4 26B A4B, Qwen2.5-Coder 7B, and Llama 3.1 8B. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 trace-based autonomous security-agent protocol`；Evaluation=`§4–§5 sandbox/tool-use evaluation`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19722:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19722:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19722:end -->

<!-- review:SF-2026-ARXIV-2605-19769:start -->
#### OpenComputer: Verifiable Software Worlds for Computer-Use Agents

**问题与机制。** We present OpenComputer, a verifier-grounded framework for constructing verifiable software worlds for computer-use agents. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2–§3 verifier-grounded software worlds`；Evaluation=`§4.1 computer-use agent evaluation`；Limitations/Counterevidence=`§ unnumbered exact heading ‘Limitations and Future Work’`。

<!-- claim:SF-2026-ARXIV-2605-19769:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19769:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19769:end -->

<!-- review:SF-2026-ARXIV-2605-19775:start -->
#### Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles

**问题与机制。** By systematically exploring the interplay between Data, Tensor, and Pipeline parallelism, we identify critical bottlenecks that defy standard scaling heuristics. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§2–§3 inference-scaling model`；Evaluation=`§4–§5 reasoning-workload measurements`；Limitations/Counterevidence=`§6 Conclusions and disclosed scope`。

<!-- claim:SF-2026-ARXIV-2605-19775:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19775:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19775:end -->

<!-- review:SF-2026-ARXIV-2605-19779:start -->
#### Distribution-Free Uncertainty Quantification for Continuous AI Agent Evaluation

**问题与机制。** We further develop compositional uncertainty bounds for multi-agent pipelines (validated via simulation across inter-stage correlations rho in [-0.5, 0.9]), a conformal abstention rule for pairwise rankings with controlled false-ranking rate, and FDR-corrected abstention for leaderboard-scale multiple testing. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2–§3 conformal continuous-agent UQ`；Evaluation=`§4 longitudinal agent studies`；Limitations/Counterevidence=`§5 Limitations: bounded shift and dependence`。

<!-- claim:SF-2026-ARXIV-2605-19779:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19779:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19779:end -->

<!-- review:SF-2026-ARXIV-2605-19811:start -->
#### LionMuon: Alternating Spectral and Sign Descent for Efficient Training

**问题与机制。** In this work, we propose LionMuon, which retains the effectiveness of Muon steps while considerably cutting the averaged iteration cost, similar to sign-based methods. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§3 optimizer geometry; §4 LionMuon alternating spectral/sign descent`；Evaluation=`§5 language-model training experiments and ablations`；Limitations/Counterevidence=`§6 Limitations and optimizer/workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-19811:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19811:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19811:end -->

<!-- review:SF-2026-ARXIV-2605-19847:start -->
#### Auditing Privacy in Multi-Tenant RAG under Account Collusion

**问题与机制。** We show that this framing understates leakage under same-index account collusion. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§2–§3 collusion threat model and tenant accounting`；Evaluation=`§4 privacy audit; §5 protocol`；Limitations/Counterevidence=`§7.1 Limitations: retrieval only, not generation`。

<!-- claim:SF-2026-ARXIV-2605-19847:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19847:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19847:end -->

<!-- review:SF-2026-ARXIV-2605-19893:start -->
#### SSV: Sparse Speculative Verification for Efficient LLM Inference

**问题与机制。** We present SSV, a sparse speculative-verification framework that turns dynamic sparse attention into a verification-oriented workload. 系统 owner=`INFER-SPECULATIVE-DECODING`。

**Exact-v1。** Method=`§3–§4 sparse speculative verification`；Evaluation=`§5 long-context evaluation`；Limitations/Counterevidence=`§6 Conclusion and sparse-attention boundary`。

<!-- claim:SF-2026-ARXIV-2605-19893:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19893:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19893:end -->

<!-- review:SF-2026-ARXIV-2605-19932:start -->
#### PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents

**问题与机制。** We introduce PEEK, a system that caches and maintains this orientation knowledge as a context map: a small, constant-sized artifact in the agent's prompt that gives it a persistent peek into the external context. 系统 owner=`AGENT-CONTEXT`。

**Exact-v1。** Method=`§3 orientation-cache representation`；Evaluation=`§4 recurring-context agent evaluation`；Limitations/Counterevidence=`§5 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19932:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19932:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19932:end -->

<!-- review:SF-2026-ARXIV-2605-19945:start -->
#### GEM: GPU-Variability-Aware Expert to GPU Mapping for MoE Systems

**问题与机制。** We propose GEM, GPU-variability-aware Expert Mapping, a framework for GPU variability-aware expert to GPU mapping for MoE models. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§3–§4 variability-aware expert placement`；Evaluation=`§5 heterogeneous-GPU evaluation`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19945:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19945:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19945:end -->

<!-- review:SF-2026-ARXIV-2605-19952:start -->
#### Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory

**问题与机制。** To address these limitations, we propose TriMem, which maintains three coexisting representation granularities, including raw dialogue segments anchored by source identifiers for storage fidelity, extracted atomic facts for efficient memory retrieval, synthesized profiles that aggregate dispersed facts into holistic semantic understanding for deep reasoning. 系统 owner=`AGENT-MEMORY`。

**Exact-v1。** Method=`§3 trace/chunk memory representation`；Evaluation=`§4 lifelong-memory evaluation`；Limitations/Counterevidence=`Appendix C.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19952:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19952:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19952:end -->

<!-- review:SF-2026-ARXIV-2605-19999:start -->
#### LLM Benchmark Datasets Should Be Contamination-Resistant

**问题与机制。** Benchmark datasets are critical for reproducible, reliable, and discriminative evaluation of LLMs. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3–§4 contamination-resistant benchmark construction`；Evaluation=`§5 benchmark analysis`；Limitations/Counterevidence=`§ unnumbered exact heading ‘Limitations’: contamination detection and task scope`。

<!-- claim:SF-2026-ARXIV-2605-19999:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19999:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19999:end -->

<!-- review:SF-2026-ARXIV-2605-20005:start -->
#### Fine-Tuning Without Forgetting via Loss-Adaptive Learning Rates

**问题与机制。** We identify a simple mechanism for doing so: per-step forgetting is bounded by the product of the learning rate and the square root of the current training loss. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§3 per-step forgetting bound and loss-adaptive learning rate`；Evaluation=`§4–§5 task/forgetting, factuality and calibration experiments`；Limitations/Counterevidence=`§6 Conclusion, Limitations, and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-20005:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20005:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20005:end -->

<!-- review:SF-2026-ARXIV-2605-20022:start -->
#### FlexDraft: Flexible Speculative Decoding via Attention Tuning and Bonus-Guided Calibration

**问题与机制。** Speculative decoding accelerates memory-bound LLM inference without quality degradation by using a fast drafter to propose multiple candidate tokens and the target model to verify them in parallel. 系统 owner=`INFER-SPECULATIVE-DECODING`。

**Exact-v1。** Method=`§3–§4 asynchronous flexible drafting`；Evaluation=`§5 end-to-end evaluation`；Limitations/Counterevidence=`§6 Conclusion: bonus-token and accepted-length uncertainty`。

<!-- claim:SF-2026-ARXIV-2605-20022:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20022:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20022:end -->

<!-- review:SF-2026-ARXIV-2605-20023:start -->
#### When Skills Don't Help: A Negative Result on Procedural Knowledge for Tool-Grounded Agents in Offensive Cybersecurity

**问题与机制。** Yet the same benchmarks show wide variance, with 16 of 84 tasks suffering negative deltas when Skills are introduced. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 procedural-skill intervention and tool-grounded agent protocol`；Evaluation=`§4 offensive-cybersecurity experiments`；Limitations/Counterevidence=`§5 Limitations; negative result is workload/model specific`。

<!-- claim:SF-2026-ARXIV-2605-20023:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20023:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20023:end -->

<!-- review:SF-2026-ARXIV-2605-20051:start -->
#### Hunting Vulnerability Variants in AI Infra: Measurement and Reference-Driven Detection

**问题与机制。** Because many projects reimplement similar model-centric workflows, a vulnerability disclosed in one repository can recur as a variant in another repository with a related design. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3–§4 reference-driven variant detection`；Evaluation=`§5 AI-infra repository measurement`；Limitations/Counterevidence=`§6 Discussion and false-positive boundary`。

<!-- claim:SF-2026-ARXIV-2605-20051:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20051:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20051:end -->

<!-- review:SF-2026-ARXIV-2605-20061:start -->
#### Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents

**问题与机制。** To address this, we propose ReBel (Reward Belief), a process-level reinforcement learning algorithm that explicitly models structured belief states to summarize interaction history and guide subsequent policy learning. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 belief-consistency credit assignment`；Evaluation=`§4 long-horizon agent evaluation`；Limitations/Counterevidence=`Appendix C Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20061:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20061:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20061:end -->

<!-- review:SF-2026-ARXIV-2605-20084:start -->
#### BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation

**问题与机制。** In this work, we develop BalanceRAG to certify threshold pairs at a target risk level. 系统 owner=`AGENT-RAG`。

**Exact-v1。** Method=`§3–§4 joint escalation/abstention calibration`；Evaluation=`§5 cascaded-RAG evaluation`；Limitations/Counterevidence=`§ unnumbered exact heading ‘Limitations’: distribution shift and calibration`。

<!-- claim:SF-2026-ARXIV-2605-20084:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20084:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20084:end -->

<!-- review:SF-2026-ARXIV-2605-20179:start -->
#### TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload

**问题与机制。** In this work, we propose TIDE, a novel resource-efficient inference system that leverages the temporal stability of expert activations during the diffusion process within the block. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§3 I/O-aware MoE expert-offload design`；Evaluation=`§4 LLaDA2.0 experiments`；Limitations/Counterevidence=`§5 Conclusion: block-only activation and limited hardware`。

<!-- claim:SF-2026-ARXIV-2605-20179:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20179:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20179:end -->

<!-- review:SF-2026-ARXIV-2605-20295:start -->
#### Quant.npu: Enabling Efficient Mobile NPU Inference for on-device LLMs via Fully Static Quantization

**问题与机制。** To bridge the gap between high-fidelity PTQ and NPU-constrained inference, we propose Quant.npu, a integer-only fully static quantization framework. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§4 fully static NPU quantization`；Evaluation=`§5 on-device NPU evaluation`；Limitations/Counterevidence=`Appendix H Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20295:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20295:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20295:end -->

<!-- review:SF-2026-ARXIV-2605-20296:start -->
#### Spectral Unforgetting: Post-Hoc Recovery of Damaged Capabilities Without Retraining

**问题与机制。** We study this phenomenon, known as catastrophic forgetting, and propose a post-hoc repair solution that uses only the pretrained checkpoint $W_{\mathrm{base}}$ and its fine-tuned descendant $W_{\mathrm{ft}}$. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§3 checkpoint-delta spectral repair`；Evaluation=`§4 fourteen-cell recovery/preservation evaluation`；Limitations/Counterevidence=`§5 Limitations and conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20296:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20296:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20296:end -->

<!-- review:SF-2026-ARXIV-2605-20312:start -->
#### Pramana: A Protocol-Layer Treatment of Claim Verification in Autonomous Agent Networks

**问题与机制。** Autonomous agents deployed in regulated domains must produce a verification artifact per consequential output: a record an auditor can re-execute offline, capturing what was claimed, against what source, by whom, when, and how. 系统 owner=`AGENT-MCP`。

**Exact-v1。** Method=`§2 claim primitives; §3 protocol composition`；Evaluation=`§5 pilot; §6 formal properties`；Limitations/Counterevidence=`§8 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20312:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20312:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20312:end -->

<!-- review:SF-2026-ARXIV-2605-20314:start -->
#### Less Data, Faster Training: repeating smaller datasets speeds up learning via sampling biases

**问题与机制。** We argue that the speedup comes from appropriate layer-wise growth enabled by sampling biases, which is more pronounced when the dataset size is smaller. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§2 reuse setup; §3–§5 sampling-bias and relative-norm mechanism`；Evaluation=`§5 empirical interventions; Appendix B`；Limitations/Counterevidence=`§6 discussion: when data repetition is and is not helpful`。

<!-- claim:SF-2026-ARXIV-2605-20314:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20314:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20314:end -->

<!-- review:SF-2026-ARXIV-2605-20315:start -->
#### Mix-Quant: Quantized Prefilling, Precise Decoding for Agentic LLMs

**问题与机制。** However, these agentic workflows often introduce substantial input-side overhead, making the compute-intensive prefilling stage a key bottleneck in long-context, multi-turn inference. 系统 owner=`INFER-PD-DISAGGREGATION`。

**Exact-v1。** Method=`§3 quantized-prefill/precise-decode split`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§5 Conclusion and hardware boundary`。

<!-- claim:SF-2026-ARXIV-2605-20315:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20315:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20315:end -->

<!-- review:SF-2026-ARXIV-2605-20402:start -->
#### Decomposing MXFP4 quantization error for LLM reinforcement learning: reducible bias, recoverable deadzone, and an irreducible floor

**问题与机制。** We prove an exact three-way decomposition of quantization error and show how each component dominates a distinct RL training pathway. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§5 MXFP4 error decomposition`；Evaluation=`§6 RL quantization experiments`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20402:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20402:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20402:end -->

<!-- review:SF-2026-ARXIV-2605-20477:start -->
#### Training Language Agents to Learn from Experience

**问题与机制。** We then propose an RL-based training pipeline for learning such reflections directly from experience, without human-provided examples. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3–§4 reflection-learning pipeline`；Evaluation=`§5 MiniHack/ALFWorld evaluation`；Limitations/Counterevidence=`§5.3 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20477:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20477:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20477:end -->

<!-- review:SF-2026-ARXIV-2605-20485:start -->
#### ZEBRA: Zero-shot Budgeted Resource Allocation for LLM Orchestration

**问题与机制。** We propose ZEBRA, a zero-shot framework that reduces multi-phase budget allocation to a continuous nonlinear knapsack problem: an LLM controller estimates per-phase utility curves, and a water-filling search on the Lagrange multiplier returns the per-phase split. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1。** Method=`§3 budgeted model-orchestration policy`；Evaluation=`§4–§5 zero-shot allocation evaluation`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20485:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20485:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20485:end -->

<!-- review:SF-2026-ARXIV-2605-20490:start -->
#### ECUAS$_n$: A family of metrics for principled evaluation of uncertainty-augmented systems

**问题与机制。** We argue that these evaluation approaches are inadequate for assessing overall performance of the UA system for decision making under uncertainty and propose a novel family of metrics, ECUAS$_n$, formulated as proper scoring rules for the task of interest. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2–§3 ECUAS decision-theoretic metric family`；Evaluation=`§4 evaluator and QA studies`；Limitations/Counterevidence=`§ unnumbered exact heading ‘Limitations’: equivalence evaluator and utility assumptions`。

<!-- claim:SF-2026-ARXIV-2605-20490:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20490:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20490:end -->

<!-- review:SF-2026-ARXIV-2605-20520:start -->
#### Open-World Evaluations for Measuring Frontier AI Capabilities

**问题与机制。** In this paper we survey recent open-world evaluations, identify their strengths and limitations, and introduce CRUX (Collaborative Research for Updating AI eXpectations), a project for conducting such evaluations regularly. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2 open-world evaluation framework`；Evaluation=`§3 case studies and capability evidence`；Limitations/Counterevidence=`§2.4 Limitations: complements, not replaces, benchmarks`。

<!-- claim:SF-2026-ARXIV-2605-20520:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20520:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20520:end -->

<!-- review:SF-2026-ARXIV-2605-20544:start -->
#### The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents

**问题与机制。** To address this gap, we introduce a taxonomy to categorize abstention in the context of embodied robotics and present RoboAbstention, a scalable and auditable framework for generating abstention instructions grounded in images gathered from five robotics datasets. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§3 grounded abstention taxonomy and deterministic constraint pipeline`；Evaluation=`§4 6,069-instruction embodied VLM evaluation`；Limitations/Counterevidence=`§5 Discussion; guarantees remain conditional on scene extraction`。

<!-- claim:SF-2026-ARXIV-2605-20544:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20544:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20544:end -->

<!-- review:SF-2026-ARXIV-2605-20548:start -->
#### What Do Agents Communicate? Characterizing Information Exchange in Multi-Agent Systems

**问题与机制。** To address this, we conduct a systematic analysis of inter-agent communication to identify which information drives MA performance. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1。** Method=`§3–§4 communication-content instrumentation`；Evaluation=`§5 and Appendix C.2 occlusion evaluation`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20548:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20548:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20548:end -->

<!-- review:SF-2026-ARXIV-2605-20563:start -->
#### Multi-agent Collaboration with State Management

**问题与机制。** In this paper, we propose STORM, i.e., STate-ORiented Management for multi-agent collaboration. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1。** Method=`§3–§4 state-management and annotation protocol`；Evaluation=`§5 evaluation; Appendix A setup`；Limitations/Counterevidence=`Appendix E Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20563:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20563:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20563:end -->

<!-- review:SF-2026-ARXIV-2605-22863:start -->
#### Latent Cache Flow: Model-to-Model Communication Without Text

**问题与机制。** We introduce Latent Cache Flow (LCF). 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1。** Method=`§3 latent-cache communication interface`；Evaluation=`§4 evaluation; Appendix C statistics`；Limitations/Counterevidence=`§5 Limitations: checkpoint-specific retained layers`。

<!-- claim:SF-2026-ARXIV-2605-22863:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22863:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22863:end -->

<!-- review:SF-2026-ARXIV-2605-22866:start -->
#### BOHM: Zero-Cost Hierarchical Attribution for Compound AI Systems

**问题与机制。** We introduce BOHM, which extracts a hierarchical attribution tree directly from the routing weights such systems already maintain: leaf attribution is the path product of root-to-leaf routing weights; level-k attribution is the induced distribution over depth-k nodes. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 hierarchical online attribution`；Evaluation=`§4 and Appendix A experiments`；Limitations/Counterevidence=`§6 limitations and binary-outcome boundary`。

<!-- claim:SF-2026-ARXIV-2605-22866:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22866:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22866:end -->

<!-- review:SF-2026-ARXIV-2605-22868:start -->
#### FusionSense: Tri-Stage Near-Sensor Learning for Runtime-Adaptive Multimodal Edge Intelligence

**问题与机制。** We present FusionSense, a fusion-aware intelligent sensing framework for energy-constrained autonomous edge systems. 系统 owner=`PLATFORM-PRODUCTION`。

**Exact-v1。** Method=`§3 tri-stage near-sensor/fusion/edge control`；Evaluation=`§4 quality–data–energy evaluation`；Limitations/Counterevidence=`§5 Conclusion; dual-modality SynDrone boundary`。

<!-- claim:SF-2026-ARXIV-2605-22868:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22868:end -->

Books Decision=`Structural Candidate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22868:end -->

<!-- review:SF-2026-ARXIV-2605-24004:start -->
#### Reason--Imagine--Act: Closed-Loop LLM Decision Making with World Models for Autonomous Driving

**问题与机制。** We propose Reason--Imagine--Act (RIA), a closed-loop framework that couples an LLM reasoner with an action-conditioned world model for online safety verification. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§III Reason–Imagine–Act world-model verification loop`；Evaluation=`§IV CARLA closed-loop evaluation`；Limitations/Counterevidence=`§V Conclusion; simulator and discrete-action-template boundary`。

<!-- claim:SF-2026-ARXIV-2605-24004:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-24004:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-24004:end -->

<!-- review:SF-2026-ARXIV-2605-24006:start -->
#### A Tabular Schedule Abstraction for Communication-Aware Evaluation of Pipeline-Parallel LLM Training

**问题与机制。** In this work, we introduce a tabular schedule abstraction and a unified multi-abstraction methodology that connects formula-based reasoning, idealized schedule tables, and communication-aware execution simulation. 系统 owner=`TRAIN-PIPELINE-PARALLEL`。

**Exact-v1。** Method=`§III tabular schedule abstraction`；Evaluation=`§IV communication-aware schedule experiments`；Limitations/Counterevidence=`§V Conclusion and simulator boundary`。

<!-- claim:SF-2026-ARXIV-2605-24006:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-24006:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-24006:end -->

<!-- review:SF-2026-ARXIV-2606-28330:start -->
#### High-Dimensional Concentration and Retrieval Instability in Embedding Spaces: Implications for Retrieval-Augmented Generation

**问题与机制。** The results show that similarity signals progressively lose contrast as dimension increases, leading to unstable retrieval behavior and structural bias in nearest-neighbor selection. 系统 owner=`AGENT-RAG`。

**Exact-v1。** Method=`PDF §II–§III concentration and retrieval metrics`；Evaluation=`PDF §IV–§V synthetic and simplified RAG experiments`；Limitations/Counterevidence=`PDF §VI–§VII: synthetic-only evidence and no production embedding validation`。

<!-- claim:SF-2026-ARXIV-2606-28330:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2606-28330:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2606-28330:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-19240 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19240 |
| SF-2026-ARXIV-2605-19242 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19242 |
| SF-2026-ARXIV-2605-19262 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19262 |
| SF-2026-ARXIV-2605-19269 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19269 |
| SF-2026-ARXIV-2605-19276 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19276 |
| SF-2026-ARXIV-2605-19282 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19282 |
| SF-2026-ARXIV-2605-19314 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19314 |
| SF-2026-ARXIV-2605-19319 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19319 |
| SF-2026-ARXIV-2605-19321 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19321 |
| SF-2026-ARXIV-2605-19328 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19328 |
| SF-2026-ARXIV-2605-19335 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19335 |
| SF-2026-ARXIV-2605-19341 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19341 |
| SF-2026-ARXIV-2605-19407 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19407 |
| SF-2026-ARXIV-2605-19444 | score_7_9; forced_review; potential_books_delta | selected | DA-EXTINCTION-WINDOW | — | 跨层改变训练或安全控制契约 | analysis:DA-EXTINCTION-WINDOW |
| SF-2026-ARXIV-2605-19447 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19447 |
| SF-2026-ARXIV-2605-19461 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19461 |
| SF-2026-ARXIV-2605-19478 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19478 |
| SF-2026-ARXIV-2605-19481 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19481 |
| SF-2026-ARXIV-2605-19537 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19537 |
| SF-2026-ARXIV-2605-19576 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19576 |
| SF-2026-ARXIV-2605-19593 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19593 |
| SF-2026-ARXIV-2605-19604 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19604 |
| SF-2026-ARXIV-2605-19722 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19722 |
| SF-2026-ARXIV-2605-19769 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19769 |
| SF-2026-ARXIV-2605-19775 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19775 |
| SF-2026-ARXIV-2605-19779 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19779 |
| SF-2026-ARXIV-2605-19811 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19811 |
| SF-2026-ARXIV-2605-19847 | score_7_9; forced_review; potential_books_delta | selected | DA-TENANT-PRIVACY-ACCOUNTING | — | 跨层改变训练或安全控制契约 | analysis:DA-TENANT-PRIVACY-ACCOUNTING |
| SF-2026-ARXIV-2605-19893 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19893 |
| SF-2026-ARXIV-2605-19932 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19932 |
| SF-2026-ARXIV-2605-19945 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19945 |
| SF-2026-ARXIV-2605-19952 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19952 |
| SF-2026-ARXIV-2605-19999 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-19999 |
| SF-2026-ARXIV-2605-20005 | score_7_9; forced_review; potential_books_delta | selected | DA-LOSS-ADAPTIVE-FORGETTING | — | 跨层改变训练或安全控制契约 | analysis:DA-LOSS-ADAPTIVE-FORGETTING |
| SF-2026-ARXIV-2605-20022 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20022 |
| SF-2026-ARXIV-2605-20023 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20023 |
| SF-2026-ARXIV-2605-20051 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20051 |
| SF-2026-ARXIV-2605-20061 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20061 |
| SF-2026-ARXIV-2605-20084 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20084 |
| SF-2026-ARXIV-2605-20179 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20179 |
| SF-2026-ARXIV-2605-20295 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20295 |
| SF-2026-ARXIV-2605-20296 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20296 |
| SF-2026-ARXIV-2605-20312 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20312 |
| SF-2026-ARXIV-2605-20314 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20314 |
| SF-2026-ARXIV-2605-20315 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20315 |
| SF-2026-ARXIV-2605-20402 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20402 |
| SF-2026-ARXIV-2605-20477 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20477 |
| SF-2026-ARXIV-2605-20485 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20485 |
| SF-2026-ARXIV-2605-20490 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20490 |
| SF-2026-ARXIV-2605-20520 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20520 |
| SF-2026-ARXIV-2605-20544 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20544 |
| SF-2026-ARXIV-2605-20548 | score_7_9 | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20548 |
| SF-2026-ARXIV-2605-20563 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-20563 |
| SF-2026-ARXIV-2605-22863 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-22863 |
| SF-2026-ARXIV-2605-22866 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-22866 |
| SF-2026-ARXIV-2605-22868 | score_7_9; forced_review; potential_structural_gap | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-22868 |
| SF-2026-ARXIV-2605-24004 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24004 |
| SF-2026-ARXIV-2605-24006 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24006 |
| SF-2026-ARXIV-2606-28330 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2606-28330 |

<!-- analysis:DA-EXTINCTION-WINDOW:start -->
### DA-EXTINCTION-WINDOW

多数投票在初始多数正确时是低成本伪标签；当弱样本的少数正确轨迹会被训练永久压灭时，aggregate pass@1 掩盖了能力损伤。Extinction Window 将 per-problem label migration 变成控制状态，再用 flip-rate、minority preservation 与 risk-conditioned sparse update 决定何时停止更新。收益是保住短暂正确信号；代价是额外轨迹统计、阈值和样本级状态，且作者范围不证明开放任务中的伪标签真值。
<!-- analysis:DA-EXTINCTION-WINDOW:end -->

<!-- analysis:DA-TENANT-PRIVACY-ACCOUNTING:start -->
### DA-TENANT-PRIVACY-ACCOUNTING

per-account 隐私预算在账号与主体一一对应时合理；同一租户能创建多个账号并合谋时，噪声预算被重复消费，真实 owner 必须上移到 tenant/index。collusion-aware accounting 改善审计，却增加关联、预算与拒绝成本；论文只证明 retrieval IDs/noisy scores，不证明后续生成满足同一 DP 保证。
<!-- analysis:DA-TENANT-PRIVACY-ACCOUNTING:end -->

<!-- analysis:DA-LOSS-ADAPTIVE-FORGETTING:start -->
### DA-LOSS-ADAPTIVE-FORGETTING

固定或衰减 learning rate 假设不同 batch 的能力覆盖相近；高损失 batch 同时承载新知识与更高遗忘风险时，简单丢弃 hard token 会损害学习。FINCH 保留 objective，只让 step size 随 loss 的平方根反比变化；收益是控制 forgetting–adaptation trade-off，代价是 loss EMA、cap 与超参选择，理论上界也不证明最优 schedule。
<!-- analysis:DA-LOSS-ADAPTIVE-FORGETTING:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19240:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19240:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19242:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19242:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19262:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19262:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19269:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19269:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19276:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19276:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19282:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19282:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19314:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19314:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19319:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19319:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19321:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19321:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19328:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19328:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19335:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19335:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19341:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19341:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19407:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19407:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19447:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19447:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19461:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19461:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19478:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19478:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19481:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19481:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19537:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19537:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19576:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19576:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19593:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19593:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19604:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19604:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19722:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19722:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19769:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19769:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19775:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19775:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19779:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19779:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19811:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19811:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19893:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19893:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19932:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19932:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19945:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19945:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19952:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19952:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19999:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-19999:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20022:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20022:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20023:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20023:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20051:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20051:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20061:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20061:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20084:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20084:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20179:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20179:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20295:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20295:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20296:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20296:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20312:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20312:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20314:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20314:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20315:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20315:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20402:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20402:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20477:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20477:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20485:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20485:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20490:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20490:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20520:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20520:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20544:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20544:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20548:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20548:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20563:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-20563:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-22863:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-22863:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-22866:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-22866:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-22868:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-22868:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24004:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-24004:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24006:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2605-24006:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-28330:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:SF-2026-ARXIV-2606-28330:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-19240 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19240 | delta:SF-2026-ARXIV-2605-19240 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19240 |
| SF-2026-ARXIV-2605-19242 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-19242 | delta:SF-2026-ARXIV-2605-19242 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19242 |
| SF-2026-ARXIV-2605-19262 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19262 | delta:SF-2026-ARXIV-2605-19262 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19262 |
| SF-2026-ARXIV-2605-19269 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-19269 | delta:SF-2026-ARXIV-2605-19269 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19269 |
| SF-2026-ARXIV-2605-19276 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19276 | delta:SF-2026-ARXIV-2605-19276 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19276 |
| SF-2026-ARXIV-2605-19282 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-19282 | delta:SF-2026-ARXIV-2605-19282 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19282 |
| SF-2026-ARXIV-2605-19314 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-19314 | delta:SF-2026-ARXIV-2605-19314 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19314 |
| SF-2026-ARXIV-2605-19319 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-19319 | delta:SF-2026-ARXIV-2605-19319 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19319 |
| SF-2026-ARXIV-2605-19321 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19321 | delta:SF-2026-ARXIV-2605-19321 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19321 |
| SF-2026-ARXIV-2605-19328 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19328 | delta:SF-2026-ARXIV-2605-19328 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19328 |
| SF-2026-ARXIV-2605-19335 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-19335 | delta:SF-2026-ARXIV-2605-19335 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19335 |
| SF-2026-ARXIV-2605-19341 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19341 | delta:SF-2026-ARXIV-2605-19341 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19341 |
| SF-2026-ARXIV-2605-19407 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-19407 | delta:SF-2026-ARXIV-2605-19407 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19407 |
| SF-2026-ARXIV-2605-19444 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-19444 | delta:SF-2026-ARXIV-2605-19444 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19444 |
| SF-2026-ARXIV-2605-19447 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-19447 | delta:SF-2026-ARXIV-2605-19447 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19447 |
| SF-2026-ARXIV-2605-19461 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-19461 | delta:SF-2026-ARXIV-2605-19461 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19461 |
| SF-2026-ARXIV-2605-19478 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19478 | delta:SF-2026-ARXIV-2605-19478 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19478 |
| SF-2026-ARXIV-2605-19481 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | books/part-05-inference-system/54-gpu-memory.md#chapter-54;books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | existing:SF-2026-ARXIV-2605-19481 | delta:SF-2026-ARXIV-2605-19481 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19481 |
| SF-2026-ARXIV-2605-19537 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19537 | delta:SF-2026-ARXIV-2605-19537 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19537 |
| SF-2026-ARXIV-2605-19576 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-19576 | delta:SF-2026-ARXIV-2605-19576 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19576 |
| SF-2026-ARXIV-2605-19593 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-19593 | delta:SF-2026-ARXIV-2605-19593 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19593 |
| SF-2026-ARXIV-2605-19604 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-19604 | delta:SF-2026-ARXIV-2605-19604 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19604 |
| SF-2026-ARXIV-2605-19722 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19722 | delta:SF-2026-ARXIV-2605-19722 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19722 |
| SF-2026-ARXIV-2605-19769 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19769 | delta:SF-2026-ARXIV-2605-19769 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19769 |
| SF-2026-ARXIV-2605-19775 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-19775 | delta:SF-2026-ARXIV-2605-19775 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19775 |
| SF-2026-ARXIV-2605-19779 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19779 | delta:SF-2026-ARXIV-2605-19779 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19779 |
| SF-2026-ARXIV-2605-19811 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-19811 | delta:SF-2026-ARXIV-2605-19811 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19811 |
| SF-2026-ARXIV-2605-19847 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19847 | delta:SF-2026-ARXIV-2605-19847 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19847 |
| SF-2026-ARXIV-2605-19893 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47;books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-19893 | delta:SF-2026-ARXIV-2605-19893 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19893 |
| SF-2026-ARXIV-2605-19932 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-19932 | delta:SF-2026-ARXIV-2605-19932 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19932 |
| SF-2026-ARXIV-2605-19945 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-19945 | delta:SF-2026-ARXIV-2605-19945 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19945 |
| SF-2026-ARXIV-2605-19952 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-19952 | delta:SF-2026-ARXIV-2605-19952 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19952 |
| SF-2026-ARXIV-2605-19999 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19999 | delta:SF-2026-ARXIV-2605-19999 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19999 |
| SF-2026-ARXIV-2605-20005 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-20005 | delta:SF-2026-ARXIV-2605-20005 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20005 |
| SF-2026-ARXIV-2605-20022 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47;books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-20022 | delta:SF-2026-ARXIV-2605-20022 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20022 |
| SF-2026-ARXIV-2605-20023 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20023 | delta:SF-2026-ARXIV-2605-20023 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20023 |
| SF-2026-ARXIV-2605-20051 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-20051 | delta:SF-2026-ARXIV-2605-20051 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20051 |
| SF-2026-ARXIV-2605-20061 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-20061 | delta:SF-2026-ARXIV-2605-20061 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20061 |
| SF-2026-ARXIV-2605-20084 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-20084 | delta:SF-2026-ARXIV-2605-20084 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20084 |
| SF-2026-ARXIV-2605-20179 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-20179 | delta:SF-2026-ARXIV-2605-20179 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20179 |
| SF-2026-ARXIV-2605-20295 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-20295 | delta:SF-2026-ARXIV-2605-20295 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20295 |
| SF-2026-ARXIV-2605-20296 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-20296 | delta:SF-2026-ARXIV-2605-20296 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20296 |
| SF-2026-ARXIV-2605-20312 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82;books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-20312 | delta:SF-2026-ARXIV-2605-20312 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20312 |
| SF-2026-ARXIV-2605-20314 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-20314 | delta:SF-2026-ARXIV-2605-20314 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20314 |
| SF-2026-ARXIV-2605-20315 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | books/part-05-inference-system/54-gpu-memory.md#chapter-54;books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | existing:SF-2026-ARXIV-2605-20315 | delta:SF-2026-ARXIV-2605-20315 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20315 |
| SF-2026-ARXIV-2605-20402 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-20402 | delta:SF-2026-ARXIV-2605-20402 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20402 |
| SF-2026-ARXIV-2605-20477 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-20477 | delta:SF-2026-ARXIV-2605-20477 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20477 |
| SF-2026-ARXIV-2605-20485 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20485 | delta:SF-2026-ARXIV-2605-20485 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20485 |
| SF-2026-ARXIV-2605-20490 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20490 | delta:SF-2026-ARXIV-2605-20490 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20490 |
| SF-2026-ARXIV-2605-20520 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20520 | delta:SF-2026-ARXIV-2605-20520 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20520 |
| SF-2026-ARXIV-2605-20544 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-20544 | delta:SF-2026-ARXIV-2605-20544 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20544 |
| SF-2026-ARXIV-2605-20548 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20548 | delta:SF-2026-ARXIV-2605-20548 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20548 |
| SF-2026-ARXIV-2605-20563 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20563 | delta:SF-2026-ARXIV-2605-20563 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20563 |
| SF-2026-ARXIV-2605-22863 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22863 | delta:SF-2026-ARXIV-2605-22863 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22863 |
| SF-2026-ARXIV-2605-22866 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-22866 | delta:SF-2026-ARXIV-2605-22866 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22866 |
| SF-2026-ARXIV-2605-22868 | considered: PLATFORM-PRODUCTION, MULTIMODAL-REPRESENTATION | books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | books/part-06-ai-infrastructure/72-security.md#chapter-72 | existing:SF-2026-ARXIV-2605-22868 | delta:SF-2026-ARXIV-2605-22868 | Direct Evolution | Structural Candidate | books-review:SF-2026-ARXIV-2605-22868 |
| SF-2026-ARXIV-2605-24004 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-24004 | delta:SF-2026-ARXIV-2605-24004 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24004 |
| SF-2026-ARXIV-2605-24006 | TRAIN-PIPELINE-PARALLEL | books/part-04-training-system/38-pipeline-parallel.md#chapter-38 | books/part-04-training-system/37-tensor-parallel.md#chapter-37;books/part-04-training-system/39-zero.md#chapter-39 | existing:SF-2026-ARXIV-2605-24006 | delta:SF-2026-ARXIV-2605-24006 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24006 |
| SF-2026-ARXIV-2606-28330 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2606-28330 | delta:SF-2026-ARXIV-2606-28330 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28330 |
<!-- books-review:SF-2026-ARXIV-2605-19240:start -->
<!-- existing:SF-2026-ARXIV-2605-19240:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19240:end -->
<!-- delta:SF-2026-ARXIV-2605-19240:start -->Therefore, we propose CASPIAN, the first framework that provides a unified, cross-channel causal analysis of cascade behavior in LLM-MAS through online monitoring of dynamic influence propagation across agents.<!-- delta:SF-2026-ARXIV-2605-19240:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19240:end -->
<!-- books-review:SF-2026-ARXIV-2605-19242:start -->
<!-- existing:SF-2026-ARXIV-2605-19242:start -->`books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19242:end -->
<!-- delta:SF-2026-ARXIV-2605-19242:start -->We propose PhyWorld, a video generation world model designed to produce temporally coherent and physically faithful scene continuations through two-stage post-training.<!-- delta:SF-2026-ARXIV-2605-19242:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19242:end -->
<!-- books-review:SF-2026-ARXIV-2605-19262:start -->
<!-- existing:SF-2026-ARXIV-2605-19262:start -->`books/part-06-ai-infrastructure/72-security.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19262:end -->
<!-- delta:SF-2026-ARXIV-2605-19262:start -->In this work, we present the first systematic study of training-time backdoor attacks on MDLMs.<!-- delta:SF-2026-ARXIV-2605-19262:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19262:end -->
<!-- books-review:SF-2026-ARXIV-2605-19269:start -->
<!-- existing:SF-2026-ARXIV-2605-19269:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19269:end -->
<!-- delta:SF-2026-ARXIV-2605-19269:start -->We introduce CODA, a GPU kernel abstraction that expresses these computations as GEMM-plus-epilogue programs.<!-- delta:SF-2026-ARXIV-2605-19269:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19269:end -->
<!-- books-review:SF-2026-ARXIV-2605-19276:start -->
<!-- existing:SF-2026-ARXIV-2605-19276:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19276:end -->
<!-- delta:SF-2026-ARXIV-2605-19276:start -->Adhering to the design philosophy of modularization and component decoupling, the platform boasts three core advantages: high compatibility, flexibility, and high concurrency.<!-- delta:SF-2026-ARXIV-2605-19276:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19276:end -->
<!-- books-review:SF-2026-ARXIV-2605-19282:start -->
<!-- existing:SF-2026-ARXIV-2605-19282:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19282:end -->
<!-- delta:SF-2026-ARXIV-2605-19282:start -->While this uniform spectral whitening enhances exploration and outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA) training, where inherently low-rank action-module gradients cause amplification of noisy tail directions, and (ii) reinforcement learning with verifiable rewards (RLVR), where low-SNR gradients and the need to preserve per-head specialization from prior training make whitening unstable.<!-- delta:SF-2026-ARXIV-2605-19282:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19282:end -->
<!-- books-review:SF-2026-ARXIV-2605-19314:start -->
<!-- existing:SF-2026-ARXIV-2605-19314:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19314:end -->
<!-- delta:SF-2026-ARXIV-2605-19314:start -->We study task-state misalignment, a task-level consistency failure in which the planner's active stage, runtime evidence, remembered context, and delegated executor no longer justify the same next-step decision.<!-- delta:SF-2026-ARXIV-2605-19314:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19314:end -->
<!-- books-review:SF-2026-ARXIV-2605-19319:start -->
<!-- existing:SF-2026-ARXIV-2605-19319:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19319:end -->
<!-- delta:SF-2026-ARXIV-2605-19319:start -->In this work, we study whether image editing models can serve as sparse visual world models for robot manipulation by predicting task-level future states without dense video rollout.<!-- delta:SF-2026-ARXIV-2605-19319:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19319:end -->
<!-- books-review:SF-2026-ARXIV-2605-19321:start -->
<!-- existing:SF-2026-ARXIV-2605-19321:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19321:end -->
<!-- delta:SF-2026-ARXIV-2605-19321:start -->In this paper, we introduce a safeguard design that leverages the transferability of jailbreak attacks to enforce prompt safety before target model inference.<!-- delta:SF-2026-ARXIV-2605-19321:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19321:end -->
<!-- books-review:SF-2026-ARXIV-2605-19328:start -->
<!-- existing:SF-2026-ARXIV-2605-19328:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19328:end -->
<!-- delta:SF-2026-ARXIV-2605-19328:start -->We introduce an intent contrast dataset pipeline that augments existing datasets with paired adversarial and benign goals to measure both security and utility.<!-- delta:SF-2026-ARXIV-2605-19328:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19328:end -->
<!-- books-review:SF-2026-ARXIV-2605-19335:start -->
<!-- existing:SF-2026-ARXIV-2605-19335:start -->已顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19335:end -->
<!-- delta:SF-2026-ARXIV-2605-19335:start -->We present LIOS(Leverage I/O Stall), a framework that executes index updates inside search-side I/O stall windows.<!-- delta:SF-2026-ARXIV-2605-19335:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19335:end -->
<!-- books-review:SF-2026-ARXIV-2605-19341:start -->
<!-- existing:SF-2026-ARXIV-2605-19341:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19341:end -->
<!-- delta:SF-2026-ARXIV-2605-19341:start -->To study root causes, we introduce HalluWorld, an extensible benchmark grounded in an explicit reference-world formulation: a model hallucinates when it produces an observable claim that is false with respect to this world.<!-- delta:SF-2026-ARXIV-2605-19341:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19341:end -->
<!-- books-review:SF-2026-ARXIV-2605-19407:start -->
<!-- existing:SF-2026-ARXIV-2605-19407:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19407:end -->
<!-- delta:SF-2026-ARXIV-2605-19407:start -->We investigate data filtering for large model pretraining via new scaling studies that target the high compute, data-scarce regime.<!-- delta:SF-2026-ARXIV-2605-19407:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19407:end -->
<!-- books-review:SF-2026-ARXIV-2605-19444:start -->
<!-- existing:SF-2026-ARXIV-2605-19444:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19444:end -->
<!-- delta:SF-2026-ARXIV-2605-19444:start -->We argue these gains are systematically misinterpreted: most reflect sharpening of already-solvable problems rather than genuine learning, while problems corrupted from correct to incorrect outnumber truly learned ones, and this damage is irreversible once majority vote locks onto a wrong answer.<!-- delta:SF-2026-ARXIV-2605-19444:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19444:end -->
<!-- books-review:SF-2026-ARXIV-2605-19447:start -->
<!-- existing:SF-2026-ARXIV-2605-19447:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19447:end -->
<!-- delta:SF-2026-ARXIV-2605-19447:start -->We systematically study five feedback sources and two insertion granularities and introduce SERL, a selective environment-reweighted learning framework.<!-- delta:SF-2026-ARXIV-2605-19447:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19447:end -->
<!-- books-review:SF-2026-ARXIV-2605-19461:start -->
<!-- existing:SF-2026-ARXIV-2605-19461:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19461:end -->
<!-- delta:SF-2026-ARXIV-2605-19461:start -->We show this stems from reverse KL minimization's mode-seeking behavior, which reinforces the first high-reward trajectory found rather than maintaining a distribution over multiple diverse solutions.<!-- delta:SF-2026-ARXIV-2605-19461:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19461:end -->
<!-- books-review:SF-2026-ARXIV-2605-19478:start -->
<!-- existing:SF-2026-ARXIV-2605-19478:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19478:end -->
<!-- delta:SF-2026-ARXIV-2605-19478:start -->While adapter security has seen initial study, the risks of the burgeoning prompt-based ecosystem remain critically unexplored.<!-- delta:SF-2026-ARXIV-2605-19478:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19478:end -->
<!-- books-review:SF-2026-ARXIV-2605-19481:start -->
<!-- existing:SF-2026-ARXIV-2605-19481:start -->已顺读 `books/part-05-inference-system/55-pd-disaggregation.md` 与相邻章节 ['books/part-05-inference-system/54-gpu-memory.md', 'books/part-05-inference-system/56-inference-scheduling.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19481:end -->
<!-- delta:SF-2026-ARXIV-2605-19481:start -->Leveraging this capability, we present C2CServe, a request-granularity serverless LLM serving system that allows MIG instances to switch models across requests without reloading weights into HBM.<!-- delta:SF-2026-ARXIV-2605-19481:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19481:end -->
<!-- books-review:SF-2026-ARXIV-2605-19537:start -->
<!-- existing:SF-2026-ARXIV-2605-19537:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19537:end -->
<!-- delta:SF-2026-ARXIV-2605-19537:start -->While critical for scalability, system-level optimizations, such as custom CUDA kernels and reduced-precision arithmetic, can alter token probabilities and introduce non-determinism, possibly cascading into divergent generation.<!-- delta:SF-2026-ARXIV-2605-19537:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19537:end -->
<!-- books-review:SF-2026-ARXIV-2605-19576:start -->
<!-- existing:SF-2026-ARXIV-2605-19576:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19576:end -->
<!-- delta:SF-2026-ARXIV-2605-19576:start -->Self-evolving skill libraries face a silent failure mode we term \emph{library drift}: unbounded skill accumulation without outcome-driven lifecycle management causes retrieval degradation, false-positive injections, and performance stagnation.<!-- delta:SF-2026-ARXIV-2605-19576:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19576:end -->
<!-- books-review:SF-2026-ARXIV-2605-19593:start -->
<!-- existing:SF-2026-ARXIV-2605-19593:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19593:end -->
<!-- delta:SF-2026-ARXIV-2605-19593:start -->In this paper, we present an empirical study of how different LLMs behave across hardware platforms, focusing on the performance implications of layer offloading and preemption.<!-- delta:SF-2026-ARXIV-2605-19593:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19593:end -->
<!-- books-review:SF-2026-ARXIV-2605-19604:start -->
<!-- existing:SF-2026-ARXIV-2605-19604:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19604:end -->
<!-- delta:SF-2026-ARXIV-2605-19604:start -->We introduce Formal Skill, a runtime-native abstraction that represents reusable capability with JSON metadata and action schemas, reliable Python executors, hook-governed control logic, Formal Skill routing, and skill-local runtime state.<!-- delta:SF-2026-ARXIV-2605-19604:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19604:end -->
<!-- books-review:SF-2026-ARXIV-2605-19722:start -->
<!-- existing:SF-2026-ARXIV-2605-19722:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19722:end -->
<!-- delta:SF-2026-ARXIV-2605-19722:start -->We present a trace-based benchmark of 30 local vulnerability-analysis tasks with fixed tools, deterministic success predicates, redaction rules, and grounding checks, and compare four stock models against uncensored or abliterated derivatives: Gemma 4 31B, Gemma 4 26B A4B, Qwen2.5-Coder 7B, and Llama 3.1 8B.<!-- delta:SF-2026-ARXIV-2605-19722:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19722:end -->
<!-- books-review:SF-2026-ARXIV-2605-19769:start -->
<!-- existing:SF-2026-ARXIV-2605-19769:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19769:end -->
<!-- delta:SF-2026-ARXIV-2605-19769:start -->We present OpenComputer, a verifier-grounded framework for constructing verifiable software worlds for computer-use agents.<!-- delta:SF-2026-ARXIV-2605-19769:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19769:end -->
<!-- books-review:SF-2026-ARXIV-2605-19775:start -->
<!-- existing:SF-2026-ARXIV-2605-19775:start -->`books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19775:end -->
<!-- delta:SF-2026-ARXIV-2605-19775:start -->By systematically exploring the interplay between Data, Tensor, and Pipeline parallelism, we identify critical bottlenecks that defy standard scaling heuristics.<!-- delta:SF-2026-ARXIV-2605-19775:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19775:end -->
<!-- books-review:SF-2026-ARXIV-2605-19779:start -->
<!-- existing:SF-2026-ARXIV-2605-19779:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19779:end -->
<!-- delta:SF-2026-ARXIV-2605-19779:start -->We further develop compositional uncertainty bounds for multi-agent pipelines (validated via simulation across inter-stage correlations rho in [-0.5, 0.9]), a conformal abstention rule for pairwise rankings with controlled false-ranking rate, and FDR-corrected abstention for leaderboard-scale multiple testing.<!-- delta:SF-2026-ARXIV-2605-19779:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19779:end -->
<!-- books-review:SF-2026-ARXIV-2605-19811:start -->
<!-- existing:SF-2026-ARXIV-2605-19811:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19811:end -->
<!-- delta:SF-2026-ARXIV-2605-19811:start -->In this work, we propose LionMuon, which retains the effectiveness of Muon steps while considerably cutting the averaged iteration cost, similar to sign-based methods.<!-- delta:SF-2026-ARXIV-2605-19811:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19811:end -->
<!-- books-review:SF-2026-ARXIV-2605-19847:start -->
<!-- existing:SF-2026-ARXIV-2605-19847:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19847:end -->
<!-- delta:SF-2026-ARXIV-2605-19847:start -->We show that this framing understates leakage under same-index account collusion.<!-- delta:SF-2026-ARXIV-2605-19847:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19847:end -->
<!-- books-review:SF-2026-ARXIV-2605-19893:start -->
<!-- existing:SF-2026-ARXIV-2605-19893:start -->已顺读 `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19893:end -->
<!-- delta:SF-2026-ARXIV-2605-19893:start -->We present SSV, a sparse speculative-verification framework that turns dynamic sparse attention into a verification-oriented workload.<!-- delta:SF-2026-ARXIV-2605-19893:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19893:end -->
<!-- books-review:SF-2026-ARXIV-2605-19932:start -->
<!-- existing:SF-2026-ARXIV-2605-19932:start -->已顺读 `books/part-07-agent/75-context.md` 与相邻章节 ['books/part-07-agent/74-prompt.md', 'books/part-07-agent/76-rag.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19932:end -->
<!-- delta:SF-2026-ARXIV-2605-19932:start -->We introduce PEEK, a system that caches and maintains this orientation knowledge as a context map: a small, constant-sized artifact in the agent's prompt that gives it a persistent peek into the external context.<!-- delta:SF-2026-ARXIV-2605-19932:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19932:end -->
<!-- books-review:SF-2026-ARXIV-2605-19945:start -->
<!-- existing:SF-2026-ARXIV-2605-19945:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19945:end -->
<!-- delta:SF-2026-ARXIV-2605-19945:start -->We propose GEM, GPU-variability-aware Expert Mapping, a framework for GPU variability-aware expert to GPU mapping for MoE models.<!-- delta:SF-2026-ARXIV-2605-19945:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19945:end -->
<!-- books-review:SF-2026-ARXIV-2605-19952:start -->
<!-- existing:SF-2026-ARXIV-2605-19952:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19952:end -->
<!-- delta:SF-2026-ARXIV-2605-19952:start -->To address these limitations, we propose TriMem, which maintains three coexisting representation granularities, including raw dialogue segments anchored by source identifiers for storage fidelity, extracted atomic facts for efficient memory retrieval, synthesized profiles that aggregate dispersed facts into holistic semantic understanding for deep reasoning.<!-- delta:SF-2026-ARXIV-2605-19952:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19952:end -->
<!-- books-review:SF-2026-ARXIV-2605-19999:start -->
<!-- existing:SF-2026-ARXIV-2605-19999:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19999:end -->
<!-- delta:SF-2026-ARXIV-2605-19999:start -->Benchmark datasets are critical for reproducible, reliable, and discriminative evaluation of LLMs.<!-- delta:SF-2026-ARXIV-2605-19999:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19999:end -->
<!-- books-review:SF-2026-ARXIV-2605-20005:start -->
<!-- existing:SF-2026-ARXIV-2605-20005:start -->已顺读 `books/part-04-training-system/29-sft.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md', 'books/part-04-training-system/30-lora.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20005:end -->
<!-- delta:SF-2026-ARXIV-2605-20005:start -->We identify a simple mechanism for doing so: per-step forgetting is bounded by the product of the learning rate and the square root of the current training loss.<!-- delta:SF-2026-ARXIV-2605-20005:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20005:end -->
<!-- books-review:SF-2026-ARXIV-2605-20022:start -->
<!-- existing:SF-2026-ARXIV-2605-20022:start -->已顺读 `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20022:end -->
<!-- delta:SF-2026-ARXIV-2605-20022:start -->Speculative decoding accelerates memory-bound LLM inference without quality degradation by using a fast drafter to propose multiple candidate tokens and the target model to verify them in parallel.<!-- delta:SF-2026-ARXIV-2605-20022:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20022:end -->
<!-- books-review:SF-2026-ARXIV-2605-20023:start -->
<!-- existing:SF-2026-ARXIV-2605-20023:start -->`books/part-07-agent/84-agent-platform.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-20023:end -->
<!-- delta:SF-2026-ARXIV-2605-20023:start -->Yet the same benchmarks show wide variance, with 16 of 84 tasks suffering negative deltas when Skills are introduced.<!-- delta:SF-2026-ARXIV-2605-20023:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20023:end -->
<!-- books-review:SF-2026-ARXIV-2605-20051:start -->
<!-- existing:SF-2026-ARXIV-2605-20051:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20051:end -->
<!-- delta:SF-2026-ARXIV-2605-20051:start -->Because many projects reimplement similar model-centric workflows, a vulnerability disclosed in one repository can recur as a variant in another repository with a related design.<!-- delta:SF-2026-ARXIV-2605-20051:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20051:end -->
<!-- books-review:SF-2026-ARXIV-2605-20061:start -->
<!-- existing:SF-2026-ARXIV-2605-20061:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20061:end -->
<!-- delta:SF-2026-ARXIV-2605-20061:start -->To address this, we propose ReBel (Reward Belief), a process-level reinforcement learning algorithm that explicitly models structured belief states to summarize interaction history and guide subsequent policy learning.<!-- delta:SF-2026-ARXIV-2605-20061:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20061:end -->
<!-- books-review:SF-2026-ARXIV-2605-20084:start -->
<!-- existing:SF-2026-ARXIV-2605-20084:start -->已顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20084:end -->
<!-- delta:SF-2026-ARXIV-2605-20084:start -->In this work, we develop BalanceRAG to certify threshold pairs at a target risk level.<!-- delta:SF-2026-ARXIV-2605-20084:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20084:end -->
<!-- books-review:SF-2026-ARXIV-2605-20179:start -->
<!-- existing:SF-2026-ARXIV-2605-20179:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20179:end -->
<!-- delta:SF-2026-ARXIV-2605-20179:start -->In this work, we propose TIDE, a novel resource-efficient inference system that leverages the temporal stability of expert activations during the diffusion process within the block.<!-- delta:SF-2026-ARXIV-2605-20179:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20179:end -->
<!-- books-review:SF-2026-ARXIV-2605-20295:start -->
<!-- existing:SF-2026-ARXIV-2605-20295:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20295:end -->
<!-- delta:SF-2026-ARXIV-2605-20295:start -->To bridge the gap between high-fidelity PTQ and NPU-constrained inference, we propose Quant.npu, a integer-only fully static quantization framework.<!-- delta:SF-2026-ARXIV-2605-20295:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20295:end -->
<!-- books-review:SF-2026-ARXIV-2605-20296:start -->
<!-- existing:SF-2026-ARXIV-2605-20296:start -->已顺读 `books/part-04-training-system/29-sft.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md', 'books/part-04-training-system/30-lora.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20296:end -->
<!-- delta:SF-2026-ARXIV-2605-20296:start -->We study this phenomenon, known as catastrophic forgetting, and propose a post-hoc repair solution that uses only the pretrained checkpoint $W_{\mathrm{base}}$ and its fine-tuned descendant $W_{\mathrm{ft}}$.<!-- delta:SF-2026-ARXIV-2605-20296:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20296:end -->
<!-- books-review:SF-2026-ARXIV-2605-20312:start -->
<!-- existing:SF-2026-ARXIV-2605-20312:start -->已顺读 `books/part-07-agent/83-mcp.md` 与相邻章节 ['books/part-07-agent/82-multi-agent.md', 'books/part-07-agent/84-agent-platform.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20312:end -->
<!-- delta:SF-2026-ARXIV-2605-20312:start -->Autonomous agents deployed in regulated domains must produce a verification artifact per consequential output: a record an auditor can re-execute offline, capturing what was claimed, against what source, by whom, when, and how.<!-- delta:SF-2026-ARXIV-2605-20312:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20312:end -->
<!-- books-review:SF-2026-ARXIV-2605-20314:start -->
<!-- existing:SF-2026-ARXIV-2605-20314:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20314:end -->
<!-- delta:SF-2026-ARXIV-2605-20314:start -->We argue that the speedup comes from appropriate layer-wise growth enabled by sampling biases, which is more pronounced when the dataset size is smaller.<!-- delta:SF-2026-ARXIV-2605-20314:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20314:end -->
<!-- books-review:SF-2026-ARXIV-2605-20315:start -->
<!-- existing:SF-2026-ARXIV-2605-20315:start -->`books/part-05-inference-system/55-pd-disaggregation.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-20315:end -->
<!-- delta:SF-2026-ARXIV-2605-20315:start -->However, these agentic workflows often introduce substantial input-side overhead, making the compute-intensive prefilling stage a key bottleneck in long-context, multi-turn inference.<!-- delta:SF-2026-ARXIV-2605-20315:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20315:end -->
<!-- books-review:SF-2026-ARXIV-2605-20402:start -->
<!-- existing:SF-2026-ARXIV-2605-20402:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20402:end -->
<!-- delta:SF-2026-ARXIV-2605-20402:start -->We prove an exact three-way decomposition of quantization error and show how each component dominates a distinct RL training pathway.<!-- delta:SF-2026-ARXIV-2605-20402:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20402:end -->
<!-- books-review:SF-2026-ARXIV-2605-20477:start -->
<!-- existing:SF-2026-ARXIV-2605-20477:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20477:end -->
<!-- delta:SF-2026-ARXIV-2605-20477:start -->We then propose an RL-based training pipeline for learning such reflections directly from experience, without human-provided examples.<!-- delta:SF-2026-ARXIV-2605-20477:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20477:end -->
<!-- books-review:SF-2026-ARXIV-2605-20485:start -->
<!-- existing:SF-2026-ARXIV-2605-20485:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20485:end -->
<!-- delta:SF-2026-ARXIV-2605-20485:start -->We propose ZEBRA, a zero-shot framework that reduces multi-phase budget allocation to a continuous nonlinear knapsack problem: an LLM controller estimates per-phase utility curves, and a water-filling search on the Lagrange multiplier returns the per-phase split.<!-- delta:SF-2026-ARXIV-2605-20485:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20485:end -->
<!-- books-review:SF-2026-ARXIV-2605-20490:start -->
<!-- existing:SF-2026-ARXIV-2605-20490:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20490:end -->
<!-- delta:SF-2026-ARXIV-2605-20490:start -->We argue that these evaluation approaches are inadequate for assessing overall performance of the UA system for decision making under uncertainty and propose a novel family of metrics, ECUAS$_n$, formulated as proper scoring rules for the task of interest.<!-- delta:SF-2026-ARXIV-2605-20490:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20490:end -->
<!-- books-review:SF-2026-ARXIV-2605-20520:start -->
<!-- existing:SF-2026-ARXIV-2605-20520:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20520:end -->
<!-- delta:SF-2026-ARXIV-2605-20520:start -->In this paper we survey recent open-world evaluations, identify their strengths and limitations, and introduce CRUX (Collaborative Research for Updating AI eXpectations), a project for conducting such evaluations regularly.<!-- delta:SF-2026-ARXIV-2605-20520:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20520:end -->
<!-- books-review:SF-2026-ARXIV-2605-20544:start -->
<!-- existing:SF-2026-ARXIV-2605-20544:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20544:end -->
<!-- delta:SF-2026-ARXIV-2605-20544:start -->To address this gap, we introduce a taxonomy to categorize abstention in the context of embodied robotics and present RoboAbstention, a scalable and auditable framework for generating abstention instructions grounded in images gathered from five robotics datasets.<!-- delta:SF-2026-ARXIV-2605-20544:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20544:end -->
<!-- books-review:SF-2026-ARXIV-2605-20548:start -->
<!-- existing:SF-2026-ARXIV-2605-20548:start -->`books/part-07-agent/82-multi-agent.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-20548:end -->
<!-- delta:SF-2026-ARXIV-2605-20548:start -->To address this, we conduct a systematic analysis of inter-agent communication to identify which information drives MA performance.<!-- delta:SF-2026-ARXIV-2605-20548:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20548:end -->
<!-- books-review:SF-2026-ARXIV-2605-20563:start -->
<!-- existing:SF-2026-ARXIV-2605-20563:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20563:end -->
<!-- delta:SF-2026-ARXIV-2605-20563:start -->In this paper, we propose STORM, i.e., STate-ORiented Management for multi-agent collaboration.<!-- delta:SF-2026-ARXIV-2605-20563:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20563:end -->
<!-- books-review:SF-2026-ARXIV-2605-22863:start -->
<!-- existing:SF-2026-ARXIV-2605-22863:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-22863:end -->
<!-- delta:SF-2026-ARXIV-2605-22863:start -->We introduce Latent Cache Flow (LCF).<!-- delta:SF-2026-ARXIV-2605-22863:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-22863:end -->
<!-- books-review:SF-2026-ARXIV-2605-22866:start -->
<!-- existing:SF-2026-ARXIV-2605-22866:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-22866:end -->
<!-- delta:SF-2026-ARXIV-2605-22866:start -->We introduce BOHM, which extracts a hierarchical attribution tree directly from the routing weights such systems already maintain: leaf attribution is the path product of root-to-leaf routing weights; level-k attribution is the induced distribution over depth-k nodes.<!-- delta:SF-2026-ARXIV-2605-22866:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-22866:end -->
<!-- books-review:SF-2026-ARXIV-2605-22868:start -->
<!-- existing:SF-2026-ARXIV-2605-22868:start -->`books/part-06-ai-infrastructure/73-production-best-practice.md` 只可承载生产边界；near-sensor→edge→cloud 的长期 compute/data owner 尚无单一稳定节点，进入季度结构复核而不强塞正文。<!-- existing:SF-2026-ARXIV-2605-22868:end -->
<!-- delta:SF-2026-ARXIV-2605-22868:start -->We present FusionSense, a fusion-aware intelligent sensing framework for energy-constrained autonomous edge systems.<!-- delta:SF-2026-ARXIV-2605-22868:end --> Independent decision=`Structural Candidate`。
<!-- books-review:SF-2026-ARXIV-2605-22868:end -->
<!-- books-review:SF-2026-ARXIV-2605-24004:start -->
<!-- existing:SF-2026-ARXIV-2605-24004:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-24004:end -->
<!-- delta:SF-2026-ARXIV-2605-24004:start -->We propose Reason--Imagine--Act (RIA), a closed-loop framework that couples an LLM reasoner with an action-conditioned world model for online safety verification.<!-- delta:SF-2026-ARXIV-2605-24004:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24004:end -->
<!-- books-review:SF-2026-ARXIV-2605-24006:start -->
<!-- existing:SF-2026-ARXIV-2605-24006:start -->已顺读 `books/part-04-training-system/38-pipeline-parallel.md` 与相邻章节 ['books/part-04-training-system/37-tensor-parallel.md', 'books/part-04-training-system/39-zero.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-24006:end -->
<!-- delta:SF-2026-ARXIV-2605-24006:start -->In this work, we introduce a tabular schedule abstraction and a unified multi-abstraction methodology that connects formula-based reasoning, idealized schedule tables, and communication-aware execution simulation.<!-- delta:SF-2026-ARXIV-2605-24006:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24006:end -->
<!-- books-review:SF-2026-ARXIV-2606-28330:start -->
<!-- existing:SF-2026-ARXIV-2606-28330:start -->已顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2606-28330:end -->
<!-- delta:SF-2026-ARXIV-2606-28330:start -->The results show that similarity signals progressively lose contrast as dimension increases, leading to unstable retrieval behavior and structural bias in nearest-neighbor selection.<!-- delta:SF-2026-ARXIV-2606-28330:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2606-28330:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260520-COVERAGE | fresh-context:may2026-day02 | coverage | coverage:SRC-ARXIV:20260520 | none | full 665 replay removed 14 false positives and recovered 14 false negatives | passed |
| SA-20260520-EVIDENCE | fresh-context:may2026-day02 | evidence | review:SF-2026-ARXIV-2605-19240 | none | 59/59 source-specific exact-v1 reviews completed | passed |
| SA-20260520-SELECTION | fresh-context:may2026-day02 | deep_analysis_selection | analysis:DA-EXTINCTION-WINDOW | none | three cross-layer control deltas selected after denominator reconciliation | passed |
| SA-20260520-BOOKS-POST-WRITE | fresh-context:may2026-day03 | books | books-review:SF-2026-ARXIV-2605-19240 | none | pre-write freeze 与 47/47 post-write canonical owner、placement、semantic boundary、adjacent handoff 通过；receipt=papers/2026/05/_sources/daily-20260520/post-write-semantic-audit.json；Structural Candidate 未强塞 | passed |

## 8. Ignored Noise

606 条 family-specific pre-denominator closure 保存于 `screening-ledger-independent-final.json`；理由唯一数=606。

## 9. Recommended Action

47 项 Books queue 已由 root writer 按 owner 合并写回，并通过非写作者 47/47 post-write semantic audit。`2605.22868` 继续进入季度结构复核，未被强塞进现有章节。

## 10. Repository Changes

- 更新 2026-05-20 date-local queue 状态，并将 47 项机制按 canonical owner 合并进共享 Books 正文。
- 新增 `post-write-semantic-audit.json`；47/47 写回完成非写作者语义验收。
- 未 stage、commit 或 push。

## 11. Open Questions

- 无未解决 post-write finding；后续仅在 primary source correction、重要 revision 或章节 owner 变化时重开。

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 12. Sources

- [CASPIAN: Online Detection and Attribution of Cascade Attacks in LLM Multi-Agent Systems via Cross-Channel Causal Monitoring](https://arxiv.org/html/2605.19240v1) — arXiv:2605.19240v1；first-public 2026-05-19；accessed 2026-09-02
- [PhyWorld: Physics-Faithful World Model for Video Generation](https://arxiv.org/html/2605.19242v1) — arXiv:2605.19242v1；first-public 2026-05-19；accessed 2026-09-02
- [Backdooring Masked Diffusion Language Models](https://arxiv.org/html/2605.19262v1) — arXiv:2605.19262v1；first-public 2026-05-19；accessed 2026-09-02
- [CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs](https://arxiv.org/html/2605.19269v1) — arXiv:2605.19269v1；first-public 2026-05-19；accessed 2026-09-02
- [OpenCompass: A Universal Evaluation Platform for Large Language Models](https://arxiv.org/html/2605.19276v1) — arXiv:2605.19276v1；first-public 2026-05-19；accessed 2026-09-02
- [Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR](https://arxiv.org/html/2605.19282v1) — arXiv:2605.19282v1；first-public 2026-05-19；accessed 2026-09-02
- [ContextFlow: Hierarchical Task-State Alignment for Long-Horizon Embodied Agents](https://arxiv.org/html/2605.19314v1) — arXiv:2605.19314v1；first-public 2026-05-19；accessed 2026-09-02
- [SWEET: Sparse World Modeling with Image Editing for Embodied Task Execution](https://arxiv.org/html/2605.19319v1) — arXiv:2605.19319v1；first-public 2026-05-19；accessed 2026-09-02
- [Exploring and Developing a Pre-Model Safeguard with Draft Models](https://arxiv.org/html/2605.19321v1) — arXiv:2605.19321v1；first-public 2026-05-19；accessed 2026-09-02
- [RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents](https://arxiv.org/html/2605.19328v1) — arXiv:2605.19328v1；first-public 2026-05-19；accessed 2026-09-02
- [Leveraging I/O Stalls for Efficient Scheduling in ANNS](https://arxiv.org/html/2605.19335v1) — arXiv:2605.19335v1；first-public 2026-05-19；accessed 2026-09-02
- [HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models](https://arxiv.org/html/2605.19341v1) — arXiv:2605.19341v1；first-public 2026-05-19；accessed 2026-09-02
- [A Bitter Lesson for Data Filtering](https://arxiv.org/html/2605.19407v1) — arXiv:2605.19407v1；first-public 2026-05-19；accessed 2026-09-02
- [Detecting and Mitigating the Correct-Answer Extinction Window in Test-Time Reinforcement Learning with Majority Voting](https://arxiv.org/html/2605.19444v1) — arXiv:2605.19444v1；first-public 2026-05-19；accessed 2026-09-02
- [What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents](https://arxiv.org/html/2605.19447v1) — arXiv:2605.19447v1；first-public 2026-05-19；accessed 2026-09-02
- [Beyond Mode Collapse: Distribution Matching for Diverse Reasoning](https://arxiv.org/html/2605.19461v1) — arXiv:2605.19461v1；first-public 2026-05-19；accessed 2026-09-02
- [Exposing Functional Fusion: A New Class of Strategic Backdoor in Dynamic Prompt Architectures](https://arxiv.org/html/2605.19478v1) — arXiv:2605.19478v1；first-public 2026-05-19；accessed 2026-09-02
- [C2CServe: Leveraging NVLink-C2C for Elastic Serverless LLM Serving on MIG](https://arxiv.org/html/2605.19481v1) — arXiv:2605.19481v1；first-public 2026-05-19；accessed 2026-09-02
- [The Silent Hyperparameter: Quantifying the Impact of Inference Backends on LLM Reproducibility](https://arxiv.org/html/2605.19537v1) — arXiv:2605.19537v1；first-public 2026-05-19；accessed 2026-09-02
- [Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries](https://arxiv.org/html/2605.19576v1) — arXiv:2605.19576v1；first-public 2026-05-19；accessed 2026-09-02
- [Towards Multi-Model LLM Schedulers: Empirical Insights into Offloading and Preemption](https://arxiv.org/html/2605.19593v1) — arXiv:2605.19593v1；first-public 2026-05-19；accessed 2026-09-02
- [Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents](https://arxiv.org/html/2605.19604v1) — arXiv:2605.19604v1；first-public 2026-05-19；accessed 2026-09-02
- [Measuring Safety Alignment Effects in Autonomous Security Agents](https://arxiv.org/html/2605.19722v1) — arXiv:2605.19722v1；first-public 2026-05-19；accessed 2026-09-02
- [OpenComputer: Verifiable Software Worlds for Computer-Use Agents](https://arxiv.org/html/2605.19769v1) — arXiv:2605.19769v1；first-public 2026-05-19；accessed 2026-09-02
- [Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles](https://arxiv.org/html/2605.19775v1) — arXiv:2605.19775v1；first-public 2026-05-19；accessed 2026-09-02
- [Distribution-Free Uncertainty Quantification for Continuous AI Agent Evaluation](https://arxiv.org/html/2605.19779v1) — arXiv:2605.19779v1；first-public 2026-05-19；accessed 2026-09-02
- [LionMuon: Alternating Spectral and Sign Descent for Efficient Training](https://arxiv.org/html/2605.19811v1) — arXiv:2605.19811v1；first-public 2026-05-19；accessed 2026-09-02
- [Auditing Privacy in Multi-Tenant RAG under Account Collusion](https://arxiv.org/html/2605.19847v1) — arXiv:2605.19847v1；first-public 2026-05-19；accessed 2026-09-02
- [SSV: Sparse Speculative Verification for Efficient LLM Inference](https://arxiv.org/html/2605.19893v1) — arXiv:2605.19893v1；first-public 2026-05-19；accessed 2026-09-02
- [PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents](https://arxiv.org/html/2605.19932v1) — arXiv:2605.19932v1；first-public 2026-05-19；accessed 2026-09-02
- [GEM: GPU-Variability-Aware Expert to GPU Mapping for MoE Systems](https://arxiv.org/html/2605.19945v1) — arXiv:2605.19945v1；first-public 2026-05-19；accessed 2026-09-02
- [Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory](https://arxiv.org/html/2605.19952v1) — arXiv:2605.19952v1；first-public 2026-05-19；accessed 2026-09-02
- [LLM Benchmark Datasets Should Be Contamination-Resistant](https://arxiv.org/html/2605.19999v1) — arXiv:2605.19999v1；first-public 2026-05-19；accessed 2026-09-02
- [Fine-Tuning Without Forgetting via Loss-Adaptive Learning Rates](https://arxiv.org/html/2605.20005v1) — arXiv:2605.20005v1；first-public 2026-05-19；accessed 2026-09-02
- [FlexDraft: Flexible Speculative Decoding via Attention Tuning and Bonus-Guided Calibration](https://arxiv.org/html/2605.20022v1) — arXiv:2605.20022v1；first-public 2026-05-19；accessed 2026-09-02
- [When Skills Don't Help: A Negative Result on Procedural Knowledge for Tool-Grounded Agents in Offensive Cybersecurity](https://arxiv.org/html/2605.20023v1) — arXiv:2605.20023v1；first-public 2026-05-19；accessed 2026-09-02
- [Hunting Vulnerability Variants in AI Infra: Measurement and Reference-Driven Detection](https://arxiv.org/html/2605.20051v1) — arXiv:2605.20051v1；first-public 2026-05-19；accessed 2026-09-02
- [Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents](https://arxiv.org/html/2605.20061v1) — arXiv:2605.20061v1；first-public 2026-05-19；accessed 2026-09-02
- [BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation](https://arxiv.org/html/2605.20084v1) — arXiv:2605.20084v1；first-public 2026-05-19；accessed 2026-09-02
- [TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload](https://arxiv.org/html/2605.20179v1) — arXiv:2605.20179v1；first-public 2026-05-19；accessed 2026-09-02
- [Quant.npu: Enabling Efficient Mobile NPU Inference for on-device LLMs via Fully Static Quantization](https://arxiv.org/html/2605.20295v1) — arXiv:2605.20295v1；first-public 2026-05-19；accessed 2026-09-02
- [Spectral Unforgetting: Post-Hoc Recovery of Damaged Capabilities Without Retraining](https://arxiv.org/html/2605.20296v1) — arXiv:2605.20296v1；first-public 2026-05-19；accessed 2026-09-02
- [Pramana: A Protocol-Layer Treatment of Claim Verification in Autonomous Agent Networks](https://arxiv.org/html/2605.20312v1) — arXiv:2605.20312v1；first-public 2026-05-19；accessed 2026-09-02
- [Less Data, Faster Training: repeating smaller datasets speeds up learning via sampling biases](https://arxiv.org/html/2605.20314v1) — arXiv:2605.20314v1；first-public 2026-05-19；accessed 2026-09-02
- [Mix-Quant: Quantized Prefilling, Precise Decoding for Agentic LLMs](https://arxiv.org/html/2605.20315v1) — arXiv:2605.20315v1；first-public 2026-05-19；accessed 2026-09-02
- [Decomposing MXFP4 quantization error for LLM reinforcement learning: reducible bias, recoverable deadzone, and an irreducible floor](https://arxiv.org/html/2605.20402v1) — arXiv:2605.20402v1；first-public 2026-05-19；accessed 2026-09-02
- [Training Language Agents to Learn from Experience](https://arxiv.org/html/2605.20477v1) — arXiv:2605.20477v1；first-public 2026-05-19；accessed 2026-09-02
- [ZEBRA: Zero-shot Budgeted Resource Allocation for LLM Orchestration](https://arxiv.org/html/2605.20485v1) — arXiv:2605.20485v1；first-public 2026-05-19；accessed 2026-09-02
- [ECUAS$_n$: A family of metrics for principled evaluation of uncertainty-augmented systems](https://arxiv.org/html/2605.20490v1) — arXiv:2605.20490v1；first-public 2026-05-19；accessed 2026-09-02
- [Open-World Evaluations for Measuring Frontier AI Capabilities](https://arxiv.org/html/2605.20520v1) — arXiv:2605.20520v1；first-public 2026-05-19；accessed 2026-09-02
- [The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents](https://arxiv.org/html/2605.20544v1) — arXiv:2605.20544v1；first-public 2026-05-19；accessed 2026-09-02
- [What Do Agents Communicate? Characterizing Information Exchange in Multi-Agent Systems](https://arxiv.org/html/2605.20548v1) — arXiv:2605.20548v1；first-public 2026-05-19；accessed 2026-09-02
- [Multi-agent Collaboration with State Management](https://arxiv.org/html/2605.20563v1) — arXiv:2605.20563v1；first-public 2026-05-19；accessed 2026-09-02
- [Latent Cache Flow: Model-to-Model Communication Without Text](https://arxiv.org/html/2605.22863v1) — arXiv:2605.22863v1；first-public 2026-05-19；accessed 2026-09-02
- [BOHM: Zero-Cost Hierarchical Attribution for Compound AI Systems](https://arxiv.org/html/2605.22866v1) — arXiv:2605.22866v1；first-public 2026-05-19；accessed 2026-09-02
- [FusionSense: Tri-Stage Near-Sensor Learning for Runtime-Adaptive Multimodal Edge Intelligence](https://arxiv.org/html/2605.22868v1) — arXiv:2605.22868v1；first-public 2026-05-19；accessed 2026-09-02
- [Reason--Imagine--Act: Closed-Loop LLM Decision Making with World Models for Autonomous Driving](https://arxiv.org/html/2605.24004v1) — arXiv:2605.24004v1；first-public 2026-05-19；accessed 2026-09-02
- [A Tabular Schedule Abstraction for Communication-Aware Evaluation of Pipeline-Parallel LLM Training](https://arxiv.org/html/2605.24006v1) — arXiv:2605.24006v1；first-public 2026-05-19；accessed 2026-09-02
- [High-Dimensional Concentration and Retrieval Instability in Embedding Spaces: Implications for Retrieval-Augmented Generation](https://arxiv.org/html/2606.28330v1) — arXiv:2606.28330v1；first-public 2026-05-19；accessed 2026-09-02

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

独立 pre-write audit 与非写作者 post-write semantic audit 均已闭合；ordinary pending=0，47/47 写回在 canonical owner 正文中通过机制、边界、位置与相邻章验收。Coverage Closed、Evidence Passed、Books Passed，Completion Complete。
