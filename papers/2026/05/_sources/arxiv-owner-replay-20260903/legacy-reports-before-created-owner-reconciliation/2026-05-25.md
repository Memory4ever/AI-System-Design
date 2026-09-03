# Daily Research — 2026-05-25

**Research Date:** 2026-05-25

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-24 09:00:00 ～ 2026-05-25 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；technical claims bind official arXiv exact-v1 HTML/PDF。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。16/16 项已写入 canonical owner 正文，并通过独立 post-write semantic audit。

## Executive Summary

从 91,841 条月度 raw records 中恢复并逐项语义筛选 287/287 个窗口身份。独立审计把 author denominator 24 调整为 41：重开 18 个 false negative，降级 1 个 false positive；pre-denominator closures 263→246，exact-v1 41/41，blocked=0。current owner+adjacent Books 对照把 final Integrate 收敛为 16；16/16 项已写入 canonical owner 的机制演进正文，并通过独立 post-write semantic audit。审计发现的两处标题归属问题已仅移动原段并复验通过。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-25 |
| Window End | 2026-05-25 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260525-V2-INDEPENDENT-FINAL |
| Denominator Frozen At | 2026-09-01T18:30:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-24T09:00:00+08:00 | 2026-05-25T09:00:00+08:00 | 2026-09-01T18:30:00+08:00 | DataCite v2 00..99 + 287/287 semantic replay + official exact-v1 HTML/PDF | checked | 287 | SF-2026-ARXIV-2606-20615;SF-2026-ARXIV-2605-24817;SF-2026-ARXIV-2605-24818;SF-2026-ARXIV-2605-24823;SF-2026-ARXIV-2605-24832;SF-2026-ARXIV-2605-24870;SF-2026-ARXIV-2605-24879;SF-2026-ARXIV-2605-24883;SF-2026-ARXIV-2605-24892;SF-2026-ARXIV-2605-24914;SF-2026-ARXIV-2605-24922;SF-2026-ARXIV-2605-24930;SF-2026-ARXIV-2605-24941;SF-2026-ARXIV-2605-24973;SF-2026-ARXIV-2605-25002;SF-2026-ARXIV-2605-25052;SF-2026-ARXIV-2605-25073;SF-2026-ARXIV-2605-25077;SF-2026-ARXIV-2605-25085;SF-2026-ARXIV-2605-25092;SF-2026-ARXIV-2605-25133;SF-2026-ARXIV-2605-25160;SF-2026-ARXIV-2605-25188;SF-2026-ARXIV-2605-25189;SF-2026-ARXIV-2605-25233;SF-2026-ARXIV-2605-25240;SF-2026-ARXIV-2605-25244;SF-2026-ARXIV-2605-25247;SF-2026-ARXIV-2605-25252;SF-2026-ARXIV-2605-25272;SF-2026-ARXIV-2605-25284;SF-2026-ARXIV-2605-25292;SF-2026-ARXIV-2605-25298;SF-2026-ARXIV-2605-25313;SF-2026-ARXIV-2605-26154;SF-2026-ARXIV-2605-26156;SF-2026-ARXIV-2605-26158;SF-2026-ARXIV-2605-26159;SF-2026-ARXIV-2605-26161;SF-2026-ARXIV-2605-26162;SF-2026-ARXIV-2605-26165 | pages=300;final_cursor=end;raw=91841;registered=287;screened=287;retained=41;closure=246 | 2026-05-25T00:59:59Z | screening-ledger-independent-final.json#sha256=c95977ea7df24a7ba6226660ccd1c303cf06388f6fcd45369ee8cda16fa8d5b9 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260525:start -->Registered in-window identities 已 287/287 完整语义筛选；独立 reviewer 重放 false-positive/false-negative 后未留下 Coverage blocker。Discovery backstop 不是本报告确定性 Gate 的必需分母。<!-- coverage:SRC-ARXIV:20260525:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-20615 | arXiv:2606.20615v1 | paper-v1:2606.20615 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20615 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20615 | no |
| SF-2026-ARXIV-2605-24817 | arXiv:2605.24817v1 | paper-v1:2605.24817 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24817 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-24817 | no |
| SF-2026-ARXIV-2605-24818 | arXiv:2605.24818v1 | paper-v1:2605.24818 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24818 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24818 | no |
| SF-2026-ARXIV-2605-24823 | arXiv:2605.24823v1 | paper-v1:2605.24823 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24823 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24823 | no |
| SF-2026-ARXIV-2605-24832 | arXiv:2605.24832v1 | paper-v1:2605.24832 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24832 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-24832 | no |
| SF-2026-ARXIV-2605-24870 | arXiv:2605.24870v1 | paper-v1:2605.24870 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24870 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Integrate | books-review:SF-2026-ARXIV-2605-24870 | no |
| SF-2026-ARXIV-2605-24879 | arXiv:2605.24879v1 | paper-v1:2605.24879 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24879 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-24879 | no |
| SF-2026-ARXIV-2605-24883 | arXiv:2605.24883v1 | paper-v1:2605.24883 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24883 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24883 | no |
| SF-2026-ARXIV-2605-24892 | arXiv:2605.24892v1 | paper-v1:2605.24892 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24892 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24892 | no |
| SF-2026-ARXIV-2605-24914 | arXiv:2605.24914v1 | paper-v1:2605.24914 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24914 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24914 | no |
| SF-2026-ARXIV-2605-24922 | arXiv:2605.24922v1 | paper-v1:2605.24922 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24922 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-24922 | no |
| SF-2026-ARXIV-2605-24930 | arXiv:2605.24930v1 | paper-v1:2605.24930 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24930 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24930 | no |
| SF-2026-ARXIV-2605-24941 | arXiv:2605.24941v1 | paper-v1:2605.24941 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24941 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24941 | no |
| SF-2026-ARXIV-2605-24973 | arXiv:2605.24973v1 | paper-v1:2605.24973 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24973 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-24973 | no |
| SF-2026-ARXIV-2605-25002 | arXiv:2605.25002v1 | paper-v1:2605.25002 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25002 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-25002 | no |
| SF-2026-ARXIV-2605-25052 | arXiv:2605.25052v1 | paper-v1:2605.25052 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25052 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25052 | no |
| SF-2026-ARXIV-2605-25073 | arXiv:2605.25073v1 | paper-v1:2605.25073 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25073 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25073 | no |
| SF-2026-ARXIV-2605-25077 | arXiv:2605.25077v1 | paper-v1:2605.25077 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25077 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25077 | no |
| SF-2026-ARXIV-2605-25085 | arXiv:2605.25085v1 | paper-v1:2605.25085 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25085 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-25085 | no |
| SF-2026-ARXIV-2605-25092 | arXiv:2605.25092v1 | paper-v1:2605.25092 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25092 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25092 | no |
| SF-2026-ARXIV-2605-25133 | arXiv:2605.25133v1 | paper-v1:2605.25133 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25133 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25133 | no |
| SF-2026-ARXIV-2605-25160 | arXiv:2605.25160v1 | paper-v1:2605.25160 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25160 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25160 | no |
| SF-2026-ARXIV-2605-25188 | arXiv:2605.25188v1 | paper-v1:2605.25188 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25188 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25188 | no |
| SF-2026-ARXIV-2605-25189 | arXiv:2605.25189v1 | paper-v1:2605.25189 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25189 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-25189 | no |
| SF-2026-ARXIV-2605-25233 | arXiv:2605.25233v1 | paper-v1:2605.25233 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25233 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25233 | no |
| SF-2026-ARXIV-2605-25240 | arXiv:2605.25240v1 | paper-v1:2605.25240 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25240 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-25240 | no |
| SF-2026-ARXIV-2605-25244 | arXiv:2605.25244v1 | paper-v1:2605.25244 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25244 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25244 | no |
| SF-2026-ARXIV-2605-25247 | arXiv:2605.25247v1 | paper-v1:2605.25247 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25247 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25247 | no |
| SF-2026-ARXIV-2605-25252 | arXiv:2605.25252v1 | paper-v1:2605.25252 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25252 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-25252 | no |
| SF-2026-ARXIV-2605-25272 | arXiv:2605.25272v1 | paper-v1:2605.25272 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25272 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-25272 | no |
| SF-2026-ARXIV-2605-25284 | arXiv:2605.25284v1 | paper-v1:2605.25284 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25284 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25284 | no |
| SF-2026-ARXIV-2605-25292 | arXiv:2605.25292v1 | paper-v1:2605.25292 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25292 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25292 | no |
| SF-2026-ARXIV-2605-25298 | arXiv:2605.25298v1 | paper-v1:2605.25298 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-25298 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-25298 | no |
| SF-2026-ARXIV-2605-25313 | arXiv:2605.25313v1 | paper-v1:2605.25313 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-25313 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25313 | no |
| SF-2026-ARXIV-2605-26154 | arXiv:2605.26154v1 | paper-v1:2605.26154 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26154 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26154 | no |
| SF-2026-ARXIV-2605-26156 | arXiv:2605.26156v1 | paper-v1:2605.26156 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26156 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26156 | no |
| SF-2026-ARXIV-2605-26158 | arXiv:2605.26158v1 | paper-v1:2605.26158 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26158 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26158 | no |
| SF-2026-ARXIV-2605-26159 | arXiv:2605.26159v1 | paper-v1:2605.26159 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26159 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26159 | no |
| SF-2026-ARXIV-2605-26161 | arXiv:2605.26161v1 | paper-v1:2605.26161 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26161 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26161 | no |
| SF-2026-ARXIV-2605-26162 | arXiv:2605.26162v1 | paper-v1:2605.26162 | 2026-W21 | 2026-05-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26162 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-26162 | no |
| SF-2026-ARXIV-2605-26165 | arXiv:2605.26165v1 | paper-v1:2605.26165 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26165 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26165 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-20615 | RP-58d123b6c8eae6e0 | deep | arXiv:2606.20615v1 | SRC-ARXIV@arXiv:2606.20615v1 | arXiv:2606.20615v1 HTML — §4 Formal Language Specification, especially §4.5 Runtime State and Tokens and §4.10 Enforcement Invariants | arXiv:2606.20615v1 HTML — §4.8 Failure Rate Bounds; §5 Implementation | arXiv:2606.20615v1 HTML — §6.1 Limitations; §6.2 What the Language Does Not Solve; empirical evaluation is future work | arXiv:2606.20615v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-20615 | complete |
| SF-2026-ARXIV-2605-24817 | RP-d376f013b687760b | deep | arXiv:2605.24817v1 | SRC-ARXIV@arXiv:2605.24817v1 | arXiv:2605.24817v1 HTML — §5 Method: request-level telemetry, hybrid scoring and calibrated detector | arXiv:2605.24817v1 HTML — §6 Evaluation, including §6.3–§6.5 transfer and privacy-boundary tests | arXiv:2605.24817v1 HTML — §8 Discussion; §10 Ethical Concern; no dedicated Limitations section | arXiv:2605.24817v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24817 | complete |
| SF-2026-ARXIV-2605-24818 | RP-7fe610b7d1de0184 | deep | arXiv:2605.24818v1 | SRC-ARXIV@arXiv:2605.24818v1 | arXiv:2605.24818v1 HTML — §3 Simulating contamination; §3.1 Estimators and predictors; §3.2 Data generation | arXiv:2605.24818v1 HTML — §4 Benchmarking predictors; §5 Practical considerations; Appendix B Experimental details | arXiv:2605.24818v1 HTML — §5 Practical considerations; §6 Discussion: controlled Hubble-8B/test-set setting, training-data access and counterfactual-model assumptions | arXiv:2605.24818v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24818 | complete |
| SF-2026-ARXIV-2605-24823 | RP-26c3b77b3995ecf6 | deep | arXiv:2605.24823v1 | SRC-ARXIV@arXiv:2605.24823v1 | arXiv:2605.24823v1 HTML — §3 Definition and Decomposition of Industrial Cognition; §4 thin versus thick autonomy | arXiv:2605.24823v1 HTML — §5 The Factory as a Cognitive Ecosystem: A Worked Example | arXiv:2605.24823v1 HTML — §8 Research Agenda; §9 Conclusion; position paper and near-future composite, not deployed-system validation | arXiv:2605.24823v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24823 | complete |
| SF-2026-ARXIV-2605-24832 | RP-51979a1f86135445 | deep | arXiv:2605.24832v1 | SRC-ARXIV@arXiv:2605.24832v1 | arXiv:2605.24832v1 HTML — §4 Streaming Chunked Decoding; §5 Saturation-aware Elastic Scheduling | arXiv:2605.24832v1 HTML — §7 Evaluation, especially §7.3–§7.7 throughput, serving and ablation results | arXiv:2605.24832v1 HTML — §9 Conclusion; no dedicated Limitations section; evidence is bounded to evaluated DLLMs, A100 and disclosed loads | arXiv:2605.24832v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24832 | complete |
| SF-2026-ARXIV-2605-24870 | RP-cc4dd36dd2966dd4 | deep | arXiv:2605.24870v1 | SRC-ARXIV@arXiv:2605.24870v1 | arXiv:2605.24870v1 HTML — §2 Problem Formulation; §3.1 Local Statistical Calibration; §3.2 Trajectory-Consistent Prior Estimation | arXiv:2605.24870v1 HTML — §4.1–§4.3 PixArt-alpha/DiT-XL/2 experiments and ablations; Appendix B.1–B.8 latency, prompt-count and compute details | arXiv:2605.24870v1 HTML — Appendix C Limitations and Broader Impact; offline priors, selected sites/windows, representative-prompt and tested-model boundary | arXiv:2605.24870v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24870 | complete |
| SF-2026-ARXIV-2605-24879 | RP-7ecc15008e367834 | deep | arXiv:2605.24879v1 | SRC-ARXIV@arXiv:2605.24879v1 | arXiv:2605.24879v1 HTML — §4 Proposed Method; §5 Privacy Analysis and Accounting; Appendix B.9 randomized-clipping accountant | arXiv:2605.24879v1 HTML — §6 Experiments; §6.1 Memory, Compute and Latency Gains; Appendix D hyperparameters | arXiv:2605.24879v1 HTML — §7 Conclusion and experiment scope: Llama-3.2-1B, sequence length 4096, selected full/LoRA fine-tuning tasks and randomized norm-estimation assumptions | arXiv:2605.24879v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24879 | complete |
| SF-2026-ARXIV-2605-24883 | RP-4a6636ab3f7e0857 | deep | arXiv:2605.24883v1 | SRC-ARXIV@arXiv:2605.24883v1 | arXiv:2605.24883v1 HTML — §3 Methodology: policy-to-FOL translation, semantic policy graph and graph-guided query instantiation | arXiv:2605.24883v1 HTML — §4 Evaluation: policy coverage and attack efficacy | arXiv:2605.24883v1 HTML — § Limitations: policy-quality dependency, static single-turn scope, no multi-turn or agent-state coverage | arXiv:2605.24883v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24883 | complete |
| SF-2026-ARXIV-2605-24892 | RP-4206eab193a94322 | deep | arXiv:2605.24892v1 | SRC-ARXIV@arXiv:2605.24892v1 | arXiv:2605.24892v1 HTML — §3.1 Large Drive Model, especially §3.1.3 chunk-wise prediction/CLEF/TIS; §3.2 Vision Renderer; §3.3 training and interleaved inference pipeline | arXiv:2605.24892v1 HTML — §4.1 Large Drive Model and §4.2 Vision Renderer, including horizon/CL-CLEF-TIS ablations and production-scale comparison | arXiv:2605.24892v1 HTML — §5 Conclusion/future directions; private driving-data distribution, learned renderer and offline/closed-loop evaluation boundary; no dedicated limitations section | arXiv:2605.24892v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24892 | complete |
| SF-2026-ARXIV-2605-24914 | RP-4348aa5c762412a2 | deep | arXiv:2605.24914v1 | SRC-ARXIV@arXiv:2605.24914v1 | arXiv:2605.24914v1 HTML — §3 MVR-cache multi-vector retrieval and prompt segmentation | arXiv:2605.24914v1 HTML — §5 semantic-cache evaluation | arXiv:2605.24914v1 HTML — §6 limitations and workload/encoder boundary | arXiv:2605.24914v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24914 | complete |
| SF-2026-ARXIV-2605-24922 | RP-dcb3537ebca19467 | deep | arXiv:2605.24922v1 | SRC-ARXIV@arXiv:2605.24922v1 | arXiv:2605.24922v1 HTML — §3 System Design and API; §3.1 Design boundary; §3.2 Persistent pool ownership; §3.3 Runtime primitives; §3.4 Reset-time randomization | arXiv:2605.24922v1 HTML — §4 Validation and Benchmarks: parity, rollout throughput, reset and Jacobian measurements | arXiv:2605.24922v1 HTML — §6 Discussion; §6.1 Runtime boundary and trade-offs; §6.3 Reproducibility | arXiv:2605.24922v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24922 | complete |
| SF-2026-ARXIV-2605-24930 | RP-84515d6b9347b564 | deep | arXiv:2605.24930v1 | SRC-ARXIV@arXiv:2605.24930v1 | arXiv:2605.24930v1 HTML — §3 Methodology; §3.1 Semantic tree construction; §3.2 Memory-token construction; §3.3 Hierarchical inference; §3.4 Objectives | arXiv:2605.24930v1 HTML — §4 Experiments: LongBench/structured-document quality, TTFT and memory | arXiv:2605.24930v1 HTML — §5 Conclusion and discussion: hierarchy dependency, heuristic-tree error propagation, rare-evidence attenuation and routing-prune risk | arXiv:2605.24930v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24930 | complete |
| SF-2026-ARXIV-2605-24941 | RP-186ba8bfb236198f | deep | arXiv:2605.24941v1 | SRC-ARXIV@arXiv:2605.24941v1 | arXiv:2605.24941v1 HTML — PDF §3 memory-induced tool-drift mechanism | arXiv:2605.24941v1 HTML — PDF §4 agent/tool evaluation | arXiv:2605.24941v1 HTML — PDF §5 limitations and memory/task boundary | arXiv:2605.24941v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24941 | complete |
| SF-2026-ARXIV-2605-24973 | RP-6b7efaccae6f1dec | deep | arXiv:2605.24973v1 | SRC-ARXIV@arXiv:2605.24973v1 | arXiv:2605.24973v1 HTML — §3 Problem formulation; §4.1 Task-oriented data engine; §4.2 Dynamic chunking and synchronization; §4.3 Document enrichment | arXiv:2605.24973v1 HTML — §5 Experiments: five OCR backends and downstream RAG/QA | arXiv:2605.24973v1 HTML — §5 evaluation scope and §6 conclusion: OCR/model/workload boundary; cross-page summaries can suppress fine-grained evidence | arXiv:2605.24973v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-24973 | complete |
| SF-2026-ARXIV-2605-25002 | RP-4772cc1089fbe596 | deep | arXiv:2605.25002v1 | SRC-ARXIV@arXiv:2605.25002v1 | arXiv:2605.25002v1 HTML — §3 Problem Formulation; §4 MemMark, including distribution-preserving watermark and cryptographic audit trace | arXiv:2605.25002v1 HTML — §5 Experiments, RQ1–RQ5 | arXiv:2605.25002v1 HTML — §7 Limitations; Appendix G memory-lifecycle attacks and backend diagnostics | arXiv:2605.25002v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25002 | complete |
| SF-2026-ARXIV-2605-25052 | RP-54bb474635658972 | deep | arXiv:2605.25052v1 | SRC-ARXIV@arXiv:2605.25052v1 | arXiv:2605.25052v1 HTML — §2 faithfulness definitions; §3 ground-truth elicitation; §4 BonaFide labeling pipeline | arXiv:2605.25052v1 HTML — §5 Experiments and §5.2 Results | arXiv:2605.25052v1 HTML — §5.3 Discussion — Limitations; task/model and metric-cost boundary | arXiv:2605.25052v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25052 | complete |
| SF-2026-ARXIV-2605-25073 | RP-6d565967c6c643fa | deep | arXiv:2605.25073v1 | SRC-ARXIV@arXiv:2605.25073v1 | arXiv:2605.25073v1 HTML — §2 Evaluation Substrate and Threat Model; §3–§5 pre/during/post-tuning lifecycle taxonomy; §6 unified cross-phase evaluation | arXiv:2605.25073v1 HTML — §6.2–§6.6 shared models/tasks, reproduced attacks and cross-phase defense combinations | arXiv:2605.25073v1 HTML — §7 Discussion and §8 Future Directions; reproduced small-model/task configurations, method-compatibility substitutions and lifecycle-survey boundary | arXiv:2605.25073v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25073 | complete |
| SF-2026-ARXIV-2605-25077 | RP-d17d901b4fbc012c | deep | arXiv:2605.25077v1 | SRC-ARXIV@arXiv:2605.25077v1 | arXiv:2605.25077v1 HTML — §3 Method: NWT, Spatial-Pathway LoRA and Trajectory-Anchored State Persistence | arXiv:2605.25077v1 HTML — §4 Experiments, including camera/object control and state-persistence ablations | arXiv:2605.25077v1 HTML — Appendix D Limitations; pixel-world and trajectory-action boundary | arXiv:2605.25077v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25077 | complete |
| SF-2026-ARXIV-2605-25085 | RP-e201832217ab23ac | deep | arXiv:2605.25085v1 | SRC-ARXIV@arXiv:2605.25085v1 | arXiv:2605.25085v1 HTML — §3 formulation; §4 Main Theoretical Results on sequential Wyner–Ziv and suffix-only policies | arXiv:2605.25085v1 HTML — §5 Empirical Validation; §6 Connections to Deployed Compression Schemes | arXiv:2605.25085v1 HTML — §7 Limitations, including architecture, rate-convergence and heavy-hitter boundaries | arXiv:2605.25085v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25085 | complete |
| SF-2026-ARXIV-2605-25092 | RP-83a156192aaafae0 | deep | arXiv:2605.25092v1 | SRC-ARXIV@arXiv:2605.25092v1 | arXiv:2605.25092v1 HTML — §3 System Design; §4 Optimizations; §5.9 Agent Memory Benchmark cascade router | arXiv:2605.25092v1 HTML — §5 Evaluation, especially §5.9 LongMemEval and LoCoMo | arXiv:2605.25092v1 HTML — §6 Threats to validity and limitations; Appendix N Threats to Validity | arXiv:2605.25092v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25092 | complete |
| SF-2026-ARXIV-2605-25133 | RP-85b3dd2e1a91df73 | deep | arXiv:2605.25133v1 | SRC-ARXIV@arXiv:2605.25133v1 | arXiv:2605.25133v1 HTML — §3 Prover-Verifier Deliberation protocol and algorithm | arXiv:2605.25133v1 HTML — §4 Experiments; §5 Results on coverage-precision operating points | arXiv:2605.25133v1 HTML — §7 Limitations; verifier effective-region and no-formal-guarantee boundary | arXiv:2605.25133v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25133 | complete |
| SF-2026-ARXIV-2605-25160 | RP-c5e4ef7c48bd47a1 | deep | arXiv:2605.25160v1 | SRC-ARXIV@arXiv:2605.25160v1 | arXiv:2605.25160v1 HTML — §3 SimuWoB; §3.1 Environment generation; §3.2 Task and validator generation | arXiv:2605.25160v1 HTML — §4 Experiments: app fidelity, task feasibility and GUI-agent evaluation | arXiv:2605.25160v1 HTML — §5 Limitations: visual-only interface, single-app tasks, no accessibility tree or cross-app workflow | arXiv:2605.25160v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25160 | complete |
| SF-2026-ARXIV-2605-25188 | RP-b305173282f7d3b8 | deep | arXiv:2605.25188v1 | SRC-ARXIV@arXiv:2605.25188v1 | arXiv:2605.25188v1 HTML — §3 DarkForest Design: calibrated belief, controlled disclosure and guardrail | arXiv:2605.25188v1 HTML — §4 Evaluation; Appendix D ablations | arXiv:2605.25188v1 HTML — §6 Conclusion; no dedicated Limitations section; benchmark/model and coordinator boundary | arXiv:2605.25188v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25188 | complete |
| SF-2026-ARXIV-2605-25189 | RP-52a5ec545d41d6d8 | deep | arXiv:2605.25189v1 | SRC-ARXIV@arXiv:2605.25189v1 | arXiv:2605.25189v1 HTML — §3–§5 dominant update directions, directional shift and trusted-direction method | arXiv:2605.25189v1 HTML — §6 Experimental Setting; §7 Results | arXiv:2605.25189v1 HTML — Appendix A.1 Future Work; manuscript explicitly identifies itself as a preliminary study | arXiv:2605.25189v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25189 | complete |
| SF-2026-ARXIV-2605-25233 | RP-21c9028918989b7a | deep | arXiv:2605.25233v1 | SRC-ARXIV@arXiv:2605.25233v1 | arXiv:2605.25233v1 HTML — §3 Method, especially §3.2 verification loop and error attribution | arXiv:2605.25233v1 HTML — §4 Experiments and ablation study | arXiv:2605.25233v1 HTML — §4.5 Discussions; §5 Conclusion; no dedicated Limitations section | arXiv:2605.25233v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25233 | complete |
| SF-2026-ARXIV-2605-25240 | RP-84b6513eca9689f1 | deep | arXiv:2605.25240v1 | SRC-ARXIV@arXiv:2605.25240v1 | arXiv:2605.25240v1 HTML — §3.1 Dataset; §3.2 Constructed quality levels; §3.3 Rubric and pairwise-preference expert annotation | arXiv:2605.25240v1 HTML — §4 Empirical comparison of rubric scoring and comparative judgment | arXiv:2605.25240v1 HTML — Appendix A.1 Limitations: legal-domain scope, prompt-induced quality confounds, style cues and mixed-trade-off cases | arXiv:2605.25240v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25240 | complete |
| SF-2026-ARXIV-2605-25244 | RP-976230abd615e47e | deep | arXiv:2605.25244v1 | SRC-ARXIV@arXiv:2605.25244v1 | arXiv:2605.25244v1 HTML — §3 Confidence Trajectories and Confidence Dynamic Gain voting | arXiv:2605.25244v1 HTML — §5 Empirical Results and §5.3–§5.4 ablations/score analysis | arXiv:2605.25244v1 HTML — §6 Conclusion; Appendix A.2 simplified-training-model assumption; no dedicated Limitations section | arXiv:2605.25244v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25244 | complete |
| SF-2026-ARXIV-2605-25247 | RP-590dd99b68d0dceb | deep | arXiv:2605.25247v1 | SRC-ARXIV@arXiv:2605.25247v1 | arXiv:2605.25247v1 HTML — §4 Design of Kavier and cache-aware simulation modules | arXiv:2605.25247v1 HTML — §6 Trace-Based Experiments with Kavier | arXiv:2605.25247v1 HTML — §6.7 Discussion; §7.2 Future Work; bachelor-thesis prototype and simulator-calibration boundary | arXiv:2605.25247v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25247 | complete |
| SF-2026-ARXIV-2605-25252 | RP-b5b5c1f3ea612a06 | deep | arXiv:2605.25252v1 | SRC-ARXIV@arXiv:2605.25252v1 | arXiv:2605.25252v1 HTML — §3 Methodology: controlled false-positive/false-negative verifier noise and rollout scaling | arXiv:2605.25252v1 HTML — §4 Results on compute-supervision tradeoffs | arXiv:2605.25252v1 HTML — §5 Conclusion; narrow Qwen2.5/GSM8K/GRPO setting and no dedicated Limitations section | arXiv:2605.25252v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25252 | complete |
| SF-2026-ARXIV-2605-25272 | RP-b63243167e8852a5 | deep | arXiv:2605.25272v1 | SRC-ARXIV@arXiv:2605.25272v1 | arXiv:2605.25272v1 HTML — §2 Variance decomposition, confirmatory factor analysis, bifactor model and mixed-effects latent regression; §3 Experiment and data | arXiv:2605.25272v1 HTML — §4 Results across six benchmark ecosystems | arXiv:2605.25272v1 HTML — § Limitations: one snapshot/six benchmarks, observational design, noisy metadata, non-representative sample and temporal instability | arXiv:2605.25272v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25272 | complete |
| SF-2026-ARXIV-2605-25284 | RP-c6c6bf12ec7a5516 | deep | arXiv:2605.25284v1 | SRC-ARXIV@arXiv:2605.25284v1 | arXiv:2605.25284v1 HTML — §3 ambiguity-recognition and clarification protocol | arXiv:2605.25284v1 HTML — §4 evaluation | arXiv:2605.25284v1 HTML — §5 limitations and prompt/model boundary | arXiv:2605.25284v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25284 | complete |
| SF-2026-ARXIV-2605-25292 | RP-f1b52d80595cf9e3 | deep | arXiv:2605.25292v1 | SRC-ARXIV@arXiv:2605.25292v1 | arXiv:2605.25292v1 HTML — §II Work Package Structure and Contributions: IAIS data flow, formal workflow mapping, Kubernetes/Slurm control manager and Digital Twin state | arXiv:2605.25292v1 HTML — §III Evaluation Results: 10–5000 job/node scalability and solver/heuristic workflow comparison | arXiv:2605.25292v1 HTML — §IV Conclusion and project-report scope; component-level evaluation, heterogeneous project artifacts and no controlled end-to-end production SLO comparison | arXiv:2605.25292v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25292 | complete |
| SF-2026-ARXIV-2605-25298 | RP-5116ff1c466a2d6b | deep | arXiv:2605.25298v1 | SRC-ARXIV@arXiv:2605.25298v1 | arXiv:2605.25298v1 HTML — §III Design; §IV-A eBPF metric collection; §IV-C Selective Thread Tracking and Algorithm 1 | arXiv:2605.25298v1 HTML — §V–§VI six data-intensive applications and CPU/disk/lock/external-service contention; Artifact Description/Evaluation | arXiv:2605.25298v1 HTML — §IV-C optimistic entry-point propagation assumption; §V single x86/Linux 6.8.12 host and six-application workload boundary | arXiv:2605.25298v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25298 | complete |
| SF-2026-ARXIV-2605-25313 | RP-5f4bec245d79794d | deep | arXiv:2605.25313v1 | SRC-ARXIV@arXiv:2605.25313v1 | arXiv:2605.25313v1 HTML — §3 UWM-JEPA belief-space dynamics | arXiv:2605.25313v1 HTML — §4 world-model evaluation | arXiv:2605.25313v1 HTML — §5 limitations and environment/action boundary | arXiv:2605.25313v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-25313 | complete |
| SF-2026-ARXIV-2605-26154 | RP-a85ec357fb35c24c | deep | arXiv:2605.26154v1 | SRC-ARXIV@arXiv:2605.26154v1 | arXiv:2605.26154v1 HTML — §3 MemMorph memory-poisoning and tool-hijack attack | arXiv:2605.26154v1 HTML — §5 agent evaluation | arXiv:2605.26154v1 HTML — §6 limitations and memory/tool boundary | arXiv:2605.26154v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26154 | complete |
| SF-2026-ARXIV-2605-26156 | RP-37b6b283a7459e71 | deep | arXiv:2605.26156v1 | SRC-ARXIV@arXiv:2605.26156v1 | arXiv:2605.26156v1 HTML — §3 Threat model; §4 Contextual-bandit black-box style attack; §5 Analysis | arXiv:2605.26156v1 HTML — §6 Evaluation on chatbot leaderboards and automated peer review, including stealth and mitigation | arXiv:2605.26156v1 HTML — §7 Conclusion and Appendix experiments: tested-judge/task/style scope; semantic-preservation proxy and adaptive-query-budget boundary | arXiv:2605.26156v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26156 | complete |
| SF-2026-ARXIV-2605-26158 | RP-b367918348f7313d | deep | arXiv:2605.26158v1 | SRC-ARXIV@arXiv:2605.26158v1 | arXiv:2605.26158v1 HTML — §3 Safety Instability external/internal diagnostics; §4 fragmented scene-anchored probing and synthesis | arXiv:2605.26158v1 HTML — §5 HarmBench/MM-SafetyBench experiments, ablations and classical-defense checks; Appendix B.7 human judge validation | arXiv:2605.26158v1 HTML — § Impact Statement: instability band remains diagnostic, thresholds are not calibrated per input, and cross-fragment evidence requires future context-aware defense | arXiv:2605.26158v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26158 | complete |
| SF-2026-ARXIV-2605-26159 | RP-f5f75c1fa4bd5977 | deep | arXiv:2605.26159v1 | SRC-ARXIV@arXiv:2605.26159v1 | arXiv:2605.26159v1 HTML — §3 Device Context Protocol safety architecture | arXiv:2605.26159v1 HTML — §5 constrained-device evaluation | arXiv:2605.26159v1 HTML — §6 limitations and device-capability boundary | arXiv:2605.26159v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26159 | complete |
| SF-2026-ARXIV-2605-26161 | RP-543f0c20e6bda927 | deep | arXiv:2605.26161v1 | SRC-ARXIV@arXiv:2605.26161v1 | arXiv:2605.26161v1 HTML — §3 Problem formulation; §4 TSFMAudit; §4.1 adaptation traces; §4.2 reference-model debiasing; §4.3 calibration and decision | arXiv:2605.26161v1 HTML — §5 Experiments on six TSFMs/187 datasets; §5.5 practical deployment; Appendix B audit protocol | arXiv:2605.26161v1 HTML — Appendix A contamination labels and transformed-duplicate semantics; proxy labels depend on incomplete official corpus documentation | arXiv:2605.26161v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26161 | complete |
| SF-2026-ARXIV-2605-26162 | RP-45970fe3e3649800 | deep | arXiv:2605.26162v1 | SRC-ARXIV@arXiv:2605.26162v1 | arXiv:2605.26162v1 HTML — §4 PushCen-ADFL; §4.2 centroid regularization; §4.3 compression; §4.4 push-sum aggregation; §4.5 buffered updates; Appendix C event-driven state accounting | arXiv:2605.26162v1 HTML — §5 Experiments; §5.1.4 delayed-client protocol; §5.2 accuracy/communication/overhead; §5.3 delayed clients | arXiv:2605.26162v1 HTML — §4.6 assumptions and Appendix C: bounded staleness, directed mixing, bounded compression error and simulated event-driven network | arXiv:2605.26162v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26162 | complete |
| SF-2026-ARXIV-2605-26165 | RP-f17aa139de5900d4 | deep | arXiv:2605.26165v1 | SRC-ARXIV@arXiv:2605.26165v1 | arXiv:2605.26165v1 HTML — §3 tool-schema compression | arXiv:2605.26165v1 HTML — §4 agentic-RAG evaluation | arXiv:2605.26165v1 HTML — §5 limitations and context/tool-library boundary | arXiv:2605.26165v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26165 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-20615:start -->
#### Specifying AI-SDLC Processes: A Protocol Language for Human-Agent Boundaries

**问题与机制。** We propose a domain-specific language for specifying AI-SDLC processes as protocols, with formal abstract syntax, well-formedness conditions, operational semantics, and enforcement invariants, organised around a separation of policy (declared intent) from mechanism (structural enforcement). 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1 路径。** Method=`§4 Formal Language Specification, especially §4.5 Runtime State and Tokens and §4.10 Enforcement Invariants`；Evaluation=`§4.8 Failure Rate Bounds; §5 Implementation`；Limitations/Counterevidence=`§6.1 Limitations; §6.2 What the Language Does Not Solve; empirical evaluation is future work`。

<!-- claim:SF-2026-ARXIV-2606-20615:start -->Specifying AI-SDLC Processes: A Protocol Language for Human-Agent Boundaries 的 exact-v1 只支持该文披露机制：We propose a domain-specific language for specifying AI-SDLC processes as protocols, with formal abstract syntax, well-formedness conditions, operational semantics, and enforcement invariants, organised around a separation of policy (declared intent) from mechanism (structural enforcement). 其未证明边界由 `§6.1 Limitations; §6.2 What the Language Does Not Solve; empirical evaluation is future work` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2606-20615:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2606-20615:end -->

<!-- review:SF-2026-ARXIV-2605-24817:start -->
#### RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry

**问题与机制。** Inspired by this observation, we propose RouteScan, a non-intrusive auditing framework for detecting harmful behaviors through such routing-induced GPU telemetry. 系统 owner=`PLATFORM-MONITORING`。

**Exact-v1 路径。** Method=`§5 Method: request-level telemetry, hybrid scoring and calibrated detector`；Evaluation=`§6 Evaluation, including §6.3–§6.5 transfer and privacy-boundary tests`；Limitations/Counterevidence=`§8 Discussion; §10 Ethical Concern; no dedicated Limitations section`。

<!-- claim:SF-2026-ARXIV-2605-24817:start -->RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry 的 exact-v1 只支持该文披露机制：Inspired by this observation, we propose RouteScan, a non-intrusive auditing framework for detecting harmful behaviors through such routing-induced GPU telemetry. 其未证明边界由 `§8 Discussion; §10 Ethical Concern; no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-24817:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24817:end -->

<!-- review:SF-2026-ARXIV-2605-24818:start -->
#### Spiking the training data to correct for test set contamination

**问题与机制。** 在已知比例主动注入 benchmark 样本并拟合 contamination-response curve，把污染校正从事后猜测变成带干预记录的 evaluation protocol。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 Simulating contamination; §3.1 Estimators and predictors; §3.2 Data generation`；Evaluation=`§4 Benchmarking predictors; §5 Practical considerations; Appendix B Experimental details`；Limitations/Counterevidence=`§5 Practical considerations; §6 Discussion: controlled Hubble-8B/test-set setting, training-data access and counterfactual-model assumptions`。

<!-- claim:SF-2026-ARXIV-2605-24818:start -->只证明论文披露的 Hubble-8B、五类 benchmark 与模拟污染设置；需要训练数据写权限和未污染 counterfactual 假设，不能外推成任意闭源模型的通用校正器。<!-- claim:SF-2026-ARXIV-2605-24818:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24818:end -->

<!-- review:SF-2026-ARXIV-2605-24823:start -->
#### Agent Manufacturing: Foundation-Model Agents as First-Class Industrial Entities

**问题与机制。** Manufacturing has passed through four widely recognized paradigms - mechanization, electrification, programmable automation, and Smart Manufacturing - each defined by the kind of work it shifted from humans to machines. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§3 Definition and Decomposition of Industrial Cognition; §4 thin versus thick autonomy`；Evaluation=`§5 The Factory as a Cognitive Ecosystem: A Worked Example`；Limitations/Counterevidence=`§8 Research Agenda; §9 Conclusion; position paper and near-future composite, not deployed-system validation`。

<!-- claim:SF-2026-ARXIV-2605-24823:start -->Agent Manufacturing: Foundation-Model Agents as First-Class Industrial Entities 的 exact-v1 只支持该文披露机制：Manufacturing has passed through four widely recognized paradigms - mechanization, electrification, programmable automation, and Smart Manufacturing - each defined by the kind of work it shifted from humans to machines. 其未证明边界由 `§8 Research Agenda; §9 Conclusion; position paper and near-future composite, not deployed-system validation` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-24823:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24823:end -->

<!-- review:SF-2026-ARXIV-2605-24832:start -->
#### Optimus: Elastic Decoding for Efficient Diffusion LLM Serving

**问题与机制。** We present Optimus, a serving system that enables elastic decoding for diffusion LLMs by dynamically adapting decoding granularity to runtime load. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1 路径。** Method=`§4 Streaming Chunked Decoding; §5 Saturation-aware Elastic Scheduling`；Evaluation=`§7 Evaluation, especially §7.3–§7.7 throughput, serving and ablation results`；Limitations/Counterevidence=`§9 Conclusion; no dedicated Limitations section; evidence is bounded to evaluated DLLMs, A100 and disclosed loads`。

<!-- claim:SF-2026-ARXIV-2605-24832:start -->Optimus: Elastic Decoding for Efficient Diffusion LLM Serving 的 exact-v1 只支持该文披露机制：We present Optimus, a serving system that enables elastic decoding for diffusion LLMs by dynamically adapting decoding granularity to runtime load. 其未证明边界由 `§9 Conclusion; no dedicated Limitations section; evidence is bounded to evaluated DLLMs, A100 and disclosed loads` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-24832:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24832:end -->

<!-- review:SF-2026-ARXIV-2605-24870:start -->
#### Trajectory-Consistent Calibration for Cache-Accelerated Diffusion Models

**问题与机制。** 把 diffusion cache 的误差从单点 representation mismatch 扩展为会被先前校准继续改写的 trajectory state，并沿 corrected history 逐步拟合 site-local calibration prior。 系统 owner=`MULTIMODAL-GENERATIVE-PARADIGMS`。

**Exact-v1 路径。** Method=`§2 Problem Formulation; §3.1 Local Statistical Calibration; §3.2 Trajectory-Consistent Prior Estimation`；Evaluation=`§4.1–§4.3 PixArt-alpha/DiT-XL/2 experiments and ablations; Appendix B.1–B.8 latency, prompt-count and compute details`；Limitations/Counterevidence=`Appendix C Limitations and Broader Impact; offline priors, selected sites/windows, representative-prompt and tested-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-24870:start -->只验证 PixArt-alpha、DiT-XL/2、FORA/ToCa/L2C 与披露的离线 prior、采样步数和 H800 路径；prior 漂移、未测 cache policy、在线并发与分布外 prompt 不受该结果保证，失配时应回退 base cache 或 full computation。<!-- claim:SF-2026-ARXIV-2605-24870:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24870:end -->

<!-- review:SF-2026-ARXIV-2605-24879:start -->
#### Efficient DP-SGD for LLMs with Randomized Clipping

**问题与机制。** 用 Hutchinson/Hutch++ 随机 trace estimation 近似 per-sample gradient norm，把 DP clipping 的显存复杂度从显式 T×T 或 d×d 中间量改为受投影维度控制的 estimator，并为随机 clipping 单独建立 privacy accountant。 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§4 Proposed Method; §5 Privacy Analysis and Accounting; Appendix B.9 randomized-clipping accountant`；Evaluation=`§6 Experiments; §6.1 Memory, Compute and Latency Gains; Appendix D hyperparameters`；Limitations/Counterevidence=`§7 Conclusion and experiment scope: Llama-3.2-1B, sequence length 4096, selected full/LoRA fine-tuning tasks and randomized norm-estimation assumptions`。

<!-- claim:SF-2026-ARXIV-2605-24879:start -->形式保证依赖论文的随机 clipping mechanism 与 accountant 被原样实现；实验只覆盖 Llama-3.2-1B、固定 4096 长度和三类任务，未证明大模型、分布式 microbatch、任意 epsilon 或任意投影维度下同时保持 utility 与成本优势。<!-- claim:SF-2026-ARXIV-2605-24879:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24879:end -->

<!-- review:SF-2026-ARXIV-2605-24883:start -->
#### Inverting the Shield: Systematically Generating Safety Tests from Policy Specifications

**问题与机制。** 把自然语言 safety policy 编译为形式化谓词和语义图，再从未覆盖路径生成可追踪测试，使 policy revision、test identity 与 coverage evidence 成为同一评估对象。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 Methodology: policy-to-FOL translation, semantic policy graph and graph-guided query instantiation`；Evaluation=`§4 Evaluation: policy coverage and attack efficacy`；Limitations/Counterevidence=`§ Limitations: policy-quality dependency, static single-turn scope, no multi-turn or agent-state coverage`。

<!-- claim:SF-2026-ARXIV-2605-24883:start -->垃圾输入 policy 会直接产生错误测试；exact-v1 只覆盖静态单轮交互，未证明多轮 Agent state、生产 policy 漂移或自动生成测试的完备性。<!-- claim:SF-2026-ARXIV-2605-24883:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24883:end -->

<!-- review:SF-2026-ARXIV-2605-24892:start -->
#### X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling

**问题与机制。** 把低熵相邻帧预测改成跨语义时间块的自回归 future-state 预测：块内保留稠密瞬时动态、块间保留稀疏长程因果，并把 action/latent prediction 与多视角 renderer 分责。 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1 路径。** Method=`§3.1 Large Drive Model, especially §3.1.3 chunk-wise prediction/CLEF/TIS; §3.2 Vision Renderer; §3.3 training and interleaved inference pipeline`；Evaluation=`§4.1 Large Drive Model and §4.2 Vision Renderer, including horizon/CL-CLEF-TIS ablations and production-scale comparison`；Limitations/Counterevidence=`§5 Conclusion/future directions; private driving-data distribution, learned renderer and offline/closed-loop evaluation boundary; no dedicated limitations section`。

<!-- claim:SF-2026-ARXIV-2605-24892:start -->证据绑定作者私有驾驶数据、4 Hz 七相机 rollout、learned renderer 与披露的闭环设置；视觉一致性和 planning gain 不证明真实道路安全、因果识别或跨 embodiment 泛化。Ch25 已有 transition-token/reasoner/renderer 分责和多时间尺度状态边界，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-24892:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24892:end -->

<!-- review:SF-2026-ARXIV-2605-24914:start -->
#### MVR-cache: Optimizing Semantic Caching via Multi-Vector Retrieval and Learned Prompt Segmentation

**问题与机制。** To reduce LLM costs and latency, semantic caching systems must accurately identify when a new prompt matches a cached one. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1 路径。** Method=`§3 MVR-cache multi-vector retrieval and prompt segmentation`；Evaluation=`§5 semantic-cache evaluation`；Limitations/Counterevidence=`§6 limitations and workload/encoder boundary`。

<!-- claim:SF-2026-ARXIV-2605-24914:start -->MVR-cache: Optimizing Semantic Caching via Multi-Vector Retrieval and Learned Prompt Segmentation 的 exact-v1 只支持该文披露机制：To reduce LLM costs and latency, semantic caching systems must accurately identify when a new prompt matches a cached one. 其未证明边界由 `§6 limitations and workload/encoder boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-24914:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24914:end -->

<!-- review:SF-2026-ARXIV-2605-24922:start -->
#### MuJoCoUni:Persistent Batched Runtime Primitives for MuJoCo

**问题与机制。** 把 stateless rollout 调用提升为 executor-owned persistent environment pool，使 per-environment model/data、reset、step 与 Jacobian state 在 batched robot-learning loop 中保持可寻址。 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1 路径。** Method=`§3 System Design and API; §3.1 Design boundary; §3.2 Persistent pool ownership; §3.3 Runtime primitives; §3.4 Reset-time randomization`；Evaluation=`§4 Validation and Benchmarks: parity, rollout throughput, reset and Jacobian measurements`；Limitations/Counterevidence=`§6 Discussion; §6.1 Runtime boundary and trade-offs; §6.3 Reproducibility`。

<!-- claim:SF-2026-ARXIV-2605-24922:start -->证据绑定 MuJoCo 与论文测试硬件/任务；persistent pool 增加生命周期、隔离和复现责任，未证明真实机器人、分布式故障或硬实时控制语义。<!-- claim:SF-2026-ARXIV-2605-24922:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24922:end -->

<!-- review:SF-2026-ARXIV-2605-24930:start -->
#### H$^{2}$MT: Semantic Hierarchy-Aware Hierarchical Memory Transformer

**问题与机制。** 先把长文档组织成语义树，再用层级 memory tokens 与 query-aware routing 在粗摘要和细粒度节点间分配注意力预算。 系统 owner=`MODEL-LONG-CONTEXT`。

**Exact-v1 路径。** Method=`§3 Methodology; §3.1 Semantic tree construction; §3.2 Memory-token construction; §3.3 Hierarchical inference; §3.4 Objectives`；Evaluation=`§4 Experiments: LongBench/structured-document quality, TTFT and memory`；Limitations/Counterevidence=`§5 Conclusion and discussion: hierarchy dependency, heuristic-tree error propagation, rare-evidence attenuation and routing-prune risk`。

<!-- claim:SF-2026-ARXIV-2605-24930:start -->收益依赖可恢复的文档层级；错误树和过度压缩会丢失稀有证据。当前 Ch22 已拥有 query-aware hierarchical selection、coarse summary 与 dense fallback，因此不重复写入。<!-- claim:SF-2026-ARXIV-2605-24930:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24930:end -->

<!-- review:SF-2026-ARXIV-2605-24941:start -->
#### Memory-Induced Tool-Drift in LLM Agents

**问题与机制。** We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they are not applicable. 系统 owner=`AGENT-TOOL-CALLING`。

**Exact-v1 路径。** Method=`PDF §3 memory-induced tool-drift mechanism`；Evaluation=`PDF §4 agent/tool evaluation`；Limitations/Counterevidence=`PDF §5 limitations and memory/task boundary`。

<!-- claim:SF-2026-ARXIV-2605-24941:start -->Memory-Induced Tool-Drift in LLM Agents 的 exact-v1 只支持该文披露机制：We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they are not applicable. 其未证明边界由 `PDF §5 limitations and memory/task boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-24941:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24941:end -->

<!-- review:SF-2026-ARXIV-2605-24973:start -->
#### MinerU-Popo: Universal Post-Processing Model for Structured Document Parsing

**问题与机制。** 在 page OCR 之后增加 document-level state owner，跨页合并段落/表格并同步 chunk 与结构索引，使 ingestion 输出可被 RAG 以同一 document revision 消费。 系统 owner=`AGENT-RAG`。

**Exact-v1 路径。** Method=`§3 Problem formulation; §4.1 Task-oriented data engine; §4.2 Dynamic chunking and synchronization; §4.3 Document enrichment`；Evaluation=`§5 Experiments: five OCR backends and downstream RAG/QA`；Limitations/Counterevidence=`§5 evaluation scope and §6 conclusion: OCR/model/workload boundary; cross-page summaries can suppress fine-grained evidence`。

<!-- claim:SF-2026-ARXIV-2605-24973:start -->作者结果绑定披露的 OCR/VLM、H200 与文档集合；跨页修复可能合并错误或隐藏细粒度 locator，不能替代原页、region provenance 与独立 evidence check。<!-- claim:SF-2026-ARXIV-2605-24973:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-24973:end -->

<!-- review:SF-2026-ARXIV-2605-25002:start -->
#### MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems

**问题与机制。** We propose MemMark, a state-evolution attribution watermark that embeds an owner-controlled signal into latent memory-write decisions. 系统 owner=`AGENT-MEMORY`。

**Exact-v1 路径。** Method=`§3 Problem Formulation; §4 MemMark, including distribution-preserving watermark and cryptographic audit trace`；Evaluation=`§5 Experiments, RQ1–RQ5`；Limitations/Counterevidence=`§7 Limitations; Appendix G memory-lifecycle attacks and backend diagnostics`。

<!-- claim:SF-2026-ARXIV-2605-25002:start -->MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems 的 exact-v1 只支持该文披露机制：We propose MemMark, a state-evolution attribution watermark that embeds an owner-controlled signal into latent memory-write decisions. 其未证明边界由 `§7 Limitations; Appendix G memory-lifecycle attacks and backend diagnostics` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25002:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25002:end -->

<!-- review:SF-2026-ARXIV-2605-25052:start -->
#### Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth

**问题与机制。** Building on this methodology, we present BonaFide, a benchmark of 3,066 labeled CoTs across 13 tasks and 10 models, and use it to conduct the first systematic evaluation of prominent faithfulness metrics. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§2 faithfulness definitions; §3 ground-truth elicitation; §4 BonaFide labeling pipeline`；Evaluation=`§5 Experiments and §5.2 Results`；Limitations/Counterevidence=`§5.3 Discussion — Limitations; task/model and metric-cost boundary`。

<!-- claim:SF-2026-ARXIV-2605-25052:start -->Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth 的 exact-v1 只支持该文披露机制：Building on this methodology, we present BonaFide, a benchmark of 3,066 labeled CoTs across 13 tasks and 10 models, and use it to conduct the first systematic evaluation of prominent faithfulness metrics. 其未证明边界由 `§5.3 Discussion — Limitations; task/model and metric-cost boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25052:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25052:end -->

<!-- review:SF-2026-ARXIV-2605-25073:start -->
#### Security in the Fine-Tuning Lifecycle of Large Language Models: Threats, Defenses,Evaluation, and Future Directions

**问题与机制。** 把 fine-tuning attack surface 按 pre-tuning input/supply chain、during-tuning optimizer/update 与 post-tuning adapter/artifact 三个 intervention phase 组织，并用同一基座和协议检查跨 phase 防御组合。 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§2 Evaluation Substrate and Threat Model; §3–§5 pre/during/post-tuning lifecycle taxonomy; §6 unified cross-phase evaluation`；Evaluation=`§6.2–§6.6 shared models/tasks, reproduced attacks and cross-phase defense combinations`；Limitations/Counterevidence=`§7 Discussion and §8 Future Directions; reproduced small-model/task configurations, method-compatibility substitutions and lifecycle-survey boundary`。

<!-- claim:SF-2026-ARXIV-2605-25073:start -->survey taxonomy 与复现实验只能支持披露的 Llama/Qwen 1B–4B、SST-2/AGNews/agent subsets 和选定 attack-defense pairs；不能证明未复现方法、生产 adapter registry 或 RLHF/DPO 路径已被覆盖。Ch72 已拥有 data→update→artifact→runtime 的安全与 release contract，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-25073:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25073:end -->

<!-- review:SF-2026-ARXIV-2605-25077:start -->
#### WorldCraft: From Camera Navigation to Object Manipulation in Interactive Video World Models

**问题与机制。** We present WorldCraft, a framework that expands interactive video world models from camera navigation to object-level trajectory actions. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1 路径。** Method=`§3 Method: NWT, Spatial-Pathway LoRA and Trajectory-Anchored State Persistence`；Evaluation=`§4 Experiments, including camera/object control and state-persistence ablations`；Limitations/Counterevidence=`Appendix D Limitations; pixel-world and trajectory-action boundary`。

<!-- claim:SF-2026-ARXIV-2605-25077:start -->WorldCraft: From Camera Navigation to Object Manipulation in Interactive Video World Models 的 exact-v1 只支持该文披露机制：We present WorldCraft, a framework that expands interactive video world models from camera navigation to object-level trajectory actions. 其未证明边界由 `Appendix D Limitations; pixel-world and trajectory-action boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25077:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25077:end -->

<!-- review:SF-2026-ARXIV-2605-25085:start -->
#### Polynomial Context-Truncation Sensitivity in Autoregressive Language Models: Sequential Wyner-Ziv Bounds for KV Cache Compression

**问题与机制。** We study the rate-distortion limits of online KV cache compression in autoregressive language models, formulating it as sequential Wyner-Ziv source coding on the filtration induced by the model, with the next-step query as decoder side information. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1 路径。** Method=`§3 formulation; §4 Main Theoretical Results on sequential Wyner–Ziv and suffix-only policies`；Evaluation=`§5 Empirical Validation; §6 Connections to Deployed Compression Schemes`；Limitations/Counterevidence=`§7 Limitations, including architecture, rate-convergence and heavy-hitter boundaries`。

<!-- claim:SF-2026-ARXIV-2605-25085:start -->Polynomial Context-Truncation Sensitivity in Autoregressive Language Models: Sequential Wyner-Ziv Bounds for KV Cache Compression 的 exact-v1 只支持该文披露机制：We study the rate-distortion limits of online KV cache compression in autoregressive language models, formulating it as sequential Wyner-Ziv source coding on the filtration induced by the model, with the next-step query as decoder side information. 其未证明边界由 `§7 Limitations, including architecture, rate-convergence and heavy-hitter boundaries` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25085:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25085:end -->

<!-- review:SF-2026-ARXIV-2605-25092:start -->
#### AgentIR: A Workload-Adaptive Cascade Retrieval Substrate for Long-Term Conversational Memory

**问题与机制。** Long-term conversational memory is a retrieval workload classical IR was not built for: the index grows during the query stream, query types shift intra-session, and the latency budget per retrieval is sub-10 ms. 系统 owner=`AGENT-MEMORY`。

**Exact-v1 路径。** Method=`§3 System Design; §4 Optimizations; §5.9 Agent Memory Benchmark cascade router`；Evaluation=`§5 Evaluation, especially §5.9 LongMemEval and LoCoMo`；Limitations/Counterevidence=`§6 Threats to validity and limitations; Appendix N Threats to Validity`。

<!-- claim:SF-2026-ARXIV-2605-25092:start -->AgentIR: A Workload-Adaptive Cascade Retrieval Substrate for Long-Term Conversational Memory 的 exact-v1 只支持该文披露机制：Long-term conversational memory is a retrieval workload classical IR was not built for: the index grows during the query stream, query types shift intra-session, and the latency budget per retrieval is sub-10 ms. 其未证明边界由 `§6 Threats to validity and limitations; Appendix N Threats to Validity` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25092:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25092:end -->

<!-- review:SF-2026-ARXIV-2605-25133:start -->
#### Trust but Verify: Prover-Verifier Deliberation for Selective LLM Prediction

**问题与机制。** We introduce prover-verifier deliberation (PVD), an inference-time protocol grounded in interactive proof theory, as a mechanism for selective prediction: the protocol produces both an answer and a structured confidence verdict, allowing a system to report high-confidence answers while abstaining on uncertain cases. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 Prover-Verifier Deliberation protocol and algorithm`；Evaluation=`§4 Experiments; §5 Results on coverage-precision operating points`；Limitations/Counterevidence=`§7 Limitations; verifier effective-region and no-formal-guarantee boundary`。

<!-- claim:SF-2026-ARXIV-2605-25133:start -->Trust but Verify: Prover-Verifier Deliberation for Selective LLM Prediction 的 exact-v1 只支持该文披露机制：We introduce prover-verifier deliberation (PVD), an inference-time protocol grounded in interactive proof theory, as a mechanism for selective prediction: the protocol produces both an answer and a structured confidence verdict, allowing a system to report high-confidence answers while abstaining on uncertain cases. 其未证明边界由 `§7 Limitations; verifier effective-region and no-formal-guarantee boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25133:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25133:end -->

<!-- review:SF-2026-ARXIV-2605-25160:start -->
#### SimuWoB: Simulating Real-World Mobile Apps for Fast and Faithful GUI Agent Benchmarking

**问题与机制。** 由 coding agent 合成可执行 mobile-app simulator，再独立生成 task 与 state validator，把 GUI agent benchmark 的 environment 和 outcome evidence 版本化。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 SimuWoB; §3.1 Environment generation; §3.2 Task and validator generation`；Evaluation=`§4 Experiments: app fidelity, task feasibility and GUI-agent evaluation`；Limitations/Counterevidence=`§5 Limitations: visual-only interface, single-app tasks, no accessibility tree or cross-app workflow`。

<!-- claim:SF-2026-ARXIV-2605-25160:start -->只覆盖视觉单应用 simulator；不等于真实 backend、跨应用状态或 accessibility-tree 行为。当前 Ch66/Ch81 已明确 environment generation、task constraint、validator 与 durable marker 分责，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-25160:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25160:end -->

<!-- review:SF-2026-ARXIV-2605-25188:start -->
#### DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs

**问题与机制。** Multi-agent LLM systems improve reasoning by combining outputs from multiple agents, but interaction-heavy methods can introduce error propagation and high communication overhead. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1 路径。** Method=`§3 DarkForest Design: calibrated belief, controlled disclosure and guardrail`；Evaluation=`§4 Evaluation; Appendix D ablations`；Limitations/Counterevidence=`§6 Conclusion; no dedicated Limitations section; benchmark/model and coordinator boundary`。

<!-- claim:SF-2026-ARXIV-2605-25188:start -->DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs 的 exact-v1 只支持该文披露机制：Multi-agent LLM systems improve reasoning by combining outputs from multiple agents, but interaction-heavy methods can introduce error propagation and high communication overhead. 其未证明边界由 `§6 Conclusion; no dedicated Limitations section; benchmark/model and coordinator boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25188:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25188:end -->

<!-- review:SF-2026-ARXIV-2605-25189:start -->
#### Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models

**问题与机制。** We study this failure mode through the geometry of reinforcement learning updates in language models and argue that hacking emerges when optimization drifts away from a stable low-dimensional learning trajectory. 系统 owner=`TRAIN-RLHF`。

**Exact-v1 路径。** Method=`§3–§5 dominant update directions, directional shift and trusted-direction method`；Evaluation=`§6 Experimental Setting; §7 Results`；Limitations/Counterevidence=`Appendix A.1 Future Work; manuscript explicitly identifies itself as a preliminary study`。

<!-- claim:SF-2026-ARXIV-2605-25189:start -->Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models 的 exact-v1 只支持该文披露机制：We study this failure mode through the geometry of reinforcement learning updates in language models and argue that hacking emerges when optimization drifts away from a stable low-dimensional learning trajectory. 其未证明边界由 `Appendix A.1 Future Work; manuscript explicitly identifies itself as a preliminary study` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25189:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25189:end -->

<!-- review:SF-2026-ARXIV-2605-25233:start -->
#### Meta-Agent: From Task Descriptions to Verified Multi-Agent Systems

**问题与机制。** We present Meta-Agent, a two-phase framework that automatically constructs and executes specialized multi-agent systems from natural-language task descriptions. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1 路径。** Method=`§3 Method, especially §3.2 verification loop and error attribution`；Evaluation=`§4 Experiments and ablation study`；Limitations/Counterevidence=`§4.5 Discussions; §5 Conclusion; no dedicated Limitations section`。

<!-- claim:SF-2026-ARXIV-2605-25233:start -->Meta-Agent: From Task Descriptions to Verified Multi-Agent Systems 的 exact-v1 只支持该文披露机制：We present Meta-Agent, a two-phase framework that automatically constructs and executes specialized multi-agent systems from natural-language task descriptions. 其未证明边界由 `§4.5 Discussions; §5 Conclusion; no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25233:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25233:end -->

<!-- review:SF-2026-ARXIV-2605-25240:start -->
#### JudgmentBench: Comparing Rubric and Preference Evaluation for Quality Assessment

**问题与机制。** 把 rubric score 与 pairwise preference 作为不同 measurement operators，在同一受控质量阶梯上比较各自一致性与区分力，而不是默认二者可互换。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3.1 Dataset; §3.2 Constructed quality levels; §3.3 Rubric and pairwise-preference expert annotation`；Evaluation=`§4 Empirical comparison of rubric scoring and comparative judgment`；Limitations/Counterevidence=`Appendix A.1 Limitations: legal-domain scope, prompt-induced quality confounds, style cues and mixed-trade-off cases`。

<!-- claim:SF-2026-ARXIV-2605-25240:start -->证据主要来自法律文本和 prompt 构造的质量层级，质量与表达风格可能共变；不能据此规定所有 evaluator 都应采用同一判断形式。<!-- claim:SF-2026-ARXIV-2605-25240:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25240:end -->

<!-- review:SF-2026-ARXIV-2605-25244:start -->
#### Inference Time Optimization with Confidence Dynamics

**问题与机制。** In this paper, we investigate the dynamics of confidence along reasoning trajectories and for first time reveal a surprising and unique pattern: correct answer traces tend to exhibit confidence improvement over time (positive confidence gain), while incorrect traces show attenuated or declining confidence as reasoning proceeds. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1 路径。** Method=`§3 Confidence Trajectories and Confidence Dynamic Gain voting`；Evaluation=`§5 Empirical Results and §5.3–§5.4 ablations/score analysis`；Limitations/Counterevidence=`§6 Conclusion; Appendix A.2 simplified-training-model assumption; no dedicated Limitations section`。

<!-- claim:SF-2026-ARXIV-2605-25244:start -->Inference Time Optimization with Confidence Dynamics 的 exact-v1 只支持该文披露机制：In this paper, we investigate the dynamics of confidence along reasoning trajectories and for first time reveal a surprising and unique pattern: correct answer traces tend to exhibit confidence improvement over time (positive confidence gain), while incorrect traces show attenuated or declining confidence as reasoning proceeds. 其未证明边界由 `§6 Conclusion; Appendix A.2 simplified-training-model assumption; no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25244:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25244:end -->

<!-- review:SF-2026-ARXIV-2605-25247:start -->
#### Kavier: Exploring Performance, Sustainability, and Efficiency of LLM Ecosystems under Inference through Cache-Aware Discrete-Event Simulation

**问题与机制。** To improve the design and operation of LLM ecosystems, we envision simulators and simulation-based digital twins becoming primary decision-making tools. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1 路径。** Method=`§4 Design of Kavier and cache-aware simulation modules`；Evaluation=`§6 Trace-Based Experiments with Kavier`；Limitations/Counterevidence=`§6.7 Discussion; §7.2 Future Work; bachelor-thesis prototype and simulator-calibration boundary`。

<!-- claim:SF-2026-ARXIV-2605-25247:start -->Kavier: Exploring Performance, Sustainability, and Efficiency of LLM Ecosystems under Inference through Cache-Aware Discrete-Event Simulation 的 exact-v1 只支持该文披露机制：To improve the design and operation of LLM ecosystems, we envision simulators and simulation-based digital twins becoming primary decision-making tools. 其未证明边界由 `§6.7 Discussion; §7.2 Future Work; bachelor-thesis prototype and simulator-calibration boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25247:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25247:end -->

<!-- review:SF-2026-ARXIV-2605-25252:start -->
#### Quantifying Empirical Compute-Supervision Tradeoffs in RLVR

**问题与机制。** Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training language models, but in practice, verifiers are rarely perfect. 系统 owner=`TRAIN-RLHF`。

**Exact-v1 路径。** Method=`§3 Methodology: controlled false-positive/false-negative verifier noise and rollout scaling`；Evaluation=`§4 Results on compute-supervision tradeoffs`；Limitations/Counterevidence=`§5 Conclusion; narrow Qwen2.5/GSM8K/GRPO setting and no dedicated Limitations section`。

<!-- claim:SF-2026-ARXIV-2605-25252:start -->Quantifying Empirical Compute-Supervision Tradeoffs in RLVR 的 exact-v1 只支持该文披露机制：Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training language models, but in practice, verifiers are rarely perfect. 其未证明边界由 `§5 Conclusion; narrow Qwen2.5/GSM8K/GRPO setting and no dedicated Limitations section` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25252:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25252:end -->

<!-- review:SF-2026-ARXIV-2605-25272:start -->
#### AI Cartography: Mapping the Latent Landscape of AI Benchmark Ecosystems

**问题与机制。** 用 latent measurement model 分解 benchmark 共同因子与 task-specific variance，使 release evidence 能区分能力构念、数据生态和 leaderboard 聚合造成的相关性。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§2 Variance decomposition, confirmatory factor analysis, bifactor model and mixed-effects latent regression; §3 Experiment and data`；Evaluation=`§4 Results across six benchmark ecosystems`；Limitations/Counterevidence=`§ Limitations: one snapshot/six benchmarks, observational design, noisy metadata, non-representative sample and temporal instability`。

<!-- claim:SF-2026-ARXIV-2605-25272:start -->只是一轮六 benchmark 的观察性快照；latent factor 不是能力本体，也不证明因果。模型、数据与提交策略变化后必须重新拟合而不能复用旧 factor。<!-- claim:SF-2026-ARXIV-2605-25272:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25272:end -->

<!-- review:SF-2026-ARXIV-2605-25284:start -->
#### Knowing but Not Showing: LLMs Recognize Ambiguity but Rarely Ask Clarifying Questions

**问题与机制。** To study these abilities, we evaluate models on ambiguous, unambiguous, and disambiguated questions in three settings: standard question answering, explicit ambiguity judgment, and behavioral analysis, where a judge model classifies responses as direct answers, refusals, or clarifying questions. 系统 owner=`AGENT-PLANNING`。

**Exact-v1 路径。** Method=`§3 ambiguity-recognition and clarification protocol`；Evaluation=`§4 evaluation`；Limitations/Counterevidence=`§5 limitations and prompt/model boundary`。

<!-- claim:SF-2026-ARXIV-2605-25284:start -->Knowing but Not Showing: LLMs Recognize Ambiguity but Rarely Ask Clarifying Questions 的 exact-v1 只支持该文披露机制：To study these abilities, we evaluate models on ambiguous, unambiguous, and disambiguated questions in three settings: standard question answering, explicit ambiguity judgment, and behavioral analysis, where a judge model classifies responses as direct answers, refusals, or clarifying questions. 其未证明边界由 `§5 limitations and prompt/model boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25284:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25284:end -->

<!-- review:SF-2026-ARXIV-2605-25292:start -->
#### DECICE: AI-Driven Scheduling and Digital Twin Integration for the Cloud-HPC-Edge Compute Continuum

**问题与机制。** 让 scheduler 消费由 Digital Twin 维护的 node power/carbon/anomaly state，并把 heterogeneous workflow 先转成正式 dependency/resource model，再输出 Kubernetes/Slurm placement。 系统 owner=`PLATFORM-GPU-SCHEDULER`。

**Exact-v1 路径。** Method=`§II Work Package Structure and Contributions: IAIS data flow, formal workflow mapping, Kubernetes/Slurm control manager and Digital Twin state`；Evaluation=`§III Evaluation Results: 10–5000 job/node scalability and solver/heuristic workflow comparison`；Limitations/Counterevidence=`§IV Conclusion and project-report scope; component-level evaluation, heterogeneous project artifacts and no controlled end-to-end production SLO comparison`。

<!-- claim:SF-2026-ARXIV-2605-25292:start -->论文是 DECICE 项目架构与组件结果汇总；5000×5000 scalability、solver runtime 和 production-like use cases 不是同一 end-to-end SLO 实验，也未证明 RNN/RL 优于所有启发式。Ch63–65 已覆盖 state-aware placement、carbon/energy signal、workflow dependency 与 Slurm/Kubernetes 边界，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-25292:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25292:end -->

<!-- review:SF-2026-ARXIV-2605-25298:start -->
#### Beyond Thread States: Diagnosing Performance Degradation with eBPF and Thread Dynamics

**问题与机制。** 从 thread-state 时间占比继续下钻到带 backing-resource identity 的 futex/pipe/socket/VFS/block-I/O dependency graph，并从 request entry thread 反向追踪 contention propagation。 系统 owner=`PLATFORM-MONITORING`。

**Exact-v1 路径。** Method=`§III Design; §IV-A eBPF metric collection; §IV-C Selective Thread Tracking and Algorithm 1`；Evaluation=`§V–§VI six data-intensive applications and CPU/disk/lock/external-service contention; Artifact Description/Evaluation`；Limitations/Counterevidence=`§IV-C optimistic entry-point propagation assumption; §V single x86/Linux 6.8.12 host and six-application workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-25298:start -->选择性算法假设 degradation 能传播到可识别 entry thread；证据绑定单机 x86/Linux 6.8.12、六类应用与人工注入 contention，不能证明跨 kernel、GPU collective、容器隔离或无 socket entry 的训练作业同样可诊断。<!-- claim:SF-2026-ARXIV-2605-25298:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25298:end -->

<!-- review:SF-2026-ARXIV-2605-25313:start -->
#### UWM-JEPA: Predictive World Models That Imagine in Belief Space

**问题与机制。** We introduce the Unitary World Model JEPA (UWM-JEPA), a JEPA world model with a density-matrix latent on a joint system-environment space and a learned unitary predictor. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1 路径。** Method=`§3 UWM-JEPA belief-space dynamics`；Evaluation=`§4 world-model evaluation`；Limitations/Counterevidence=`§5 limitations and environment/action boundary`。

<!-- claim:SF-2026-ARXIV-2605-25313:start -->UWM-JEPA: Predictive World Models That Imagine in Belief Space 的 exact-v1 只支持该文披露机制：We introduce the Unitary World Model JEPA (UWM-JEPA), a JEPA world model with a density-matrix latent on a joint system-environment space and a learned unitary predictor. 其未证明边界由 `§5 limitations and environment/action boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-25313:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-25313:end -->

<!-- review:SF-2026-ARXIV-2605-26154:start -->
#### MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning

**问题与机制。** Experiments across 3 benchmarks, 10 agent backbones, and 3 memory-module implementations show that MemMorph achieves up to 85.9% attack success rate with only three injected records, outperforming the strongest baseline by up to 25% while retaining potency under 3 representative defenses. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§3 MemMorph memory-poisoning and tool-hijack attack`；Evaluation=`§5 agent evaluation`；Limitations/Counterevidence=`§6 limitations and memory/tool boundary`。

<!-- claim:SF-2026-ARXIV-2605-26154:start -->MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning 的 exact-v1 只支持该文披露机制：Experiments across 3 benchmarks, 10 agent backbones, and 3 memory-module implementations show that MemMorph achieves up to 85.9% attack success rate with only three injected records, outperforming the strongest baseline by up to 25% while retaining potency under 3 representative defenses. 其未证明边界由 `§6 limitations and memory/tool boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-26154:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26154:end -->

<!-- review:SF-2026-ARXIV-2605-26156:start -->
#### Turning Bias into Bugs: Bandit-Guided Style Manipulation Attacks on LLM Judges

**问题与机制。** 把 judge 的 style sensitivity 暴露为可自适应搜索的黑盒攻击面，并同时测 utility、stealth 与 query budget。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 Threat model; §4 Contextual-bandit black-box style attack; §5 Analysis`；Evaluation=`§6 Evaluation on chatbot leaderboards and automated peer review, including stealth and mitigation`；Limitations/Counterevidence=`§7 Conclusion and Appendix experiments: tested-judge/task/style scope; semantic-preservation proxy and adaptive-query-budget boundary`。

<!-- claim:SF-2026-ARXIV-2605-26156:start -->攻击只覆盖给定 judge、任务和 style transformations，语义保持依赖 LLM/embedding proxy。Ch66 已把 position/style/self-preference 与受控不变性 intervention 写入 construct-validity contract，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-26156:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26156:end -->

<!-- review:SF-2026-ARXIV-2605-26158:start -->
#### Furina: Fragmented Uncertainty-Driven Refusal Instability Attack

**问题与机制。** 把 refusal 从单一二元阈值改写为可重复采样的 instability band，并把分散于多个 benign-looking probes/视觉片段中的意图在最终 synthesis 时重新组合为跨 turn 攻击。 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§3 Safety Instability external/internal diagnostics; §4 fragmented scene-anchored probing and synthesis`；Evaluation=`§5 HarmBench/MM-SafetyBench experiments, ablations and classical-defense checks; Appendix B.7 human judge validation`；Limitations/Counterevidence=`§ Impact Statement: instability band remains diagnostic, thresholds are not calibrated per input, and cross-fragment evidence requires future context-aware defense`。

<!-- claim:SF-2026-ARXIV-2605-26158:start -->论文没有提供对单个输入校准 tau-/tau+ 的方法；ASR 绑定选定采样参数、HarmBench/MM-SafetyBench、judge 和模型版本。Ch72 已要求 run-centric multi-turn evidence 聚合、cumulative intent 与 sensor/authority 分离，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-26158:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26158:end -->

<!-- review:SF-2026-ARXIV-2605-26159:start -->
#### Device Context Protocol: A Compact, Safety-First Architecture for LLM-Driven Control of Constrained Devices

**问题与机制。** We present the Device Context Protocol (DCP): a sub-50-byte typical frame (6-byte header + CBOR payload + optional 16-byte HMAC), a manifest schema in which capability scoping, range and type checks, dry-run evaluation, and units-as-types are protocol-layer primitives, and a host-side Bridge that rejects malformed or hallucinated calls before any byte reaches the device. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§3 Device Context Protocol safety architecture`；Evaluation=`§5 constrained-device evaluation`；Limitations/Counterevidence=`§6 limitations and device-capability boundary`。

<!-- claim:SF-2026-ARXIV-2605-26159:start -->Device Context Protocol: A Compact, Safety-First Architecture for LLM-Driven Control of Constrained Devices 的 exact-v1 只支持该文披露机制：We present the Device Context Protocol (DCP): a sub-50-byte typical frame (6-byte header + CBOR payload + optional 16-byte HMAC), a manifest schema in which capability scoping, range and type checks, dry-run evaluation, and units-as-types are protocol-layer primitives, and a host-side Bridge that rejects malformed or hallucinated calls before any byte reaches the device. 其未证明边界由 `§6 limitations and device-capability boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-26159:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26159:end -->

<!-- review:SF-2026-ARXIV-2605-26161:start -->
#### TSFMAudit: Data Contamination Auditing in Forecasting Time Series Foundation Models

**问题与机制。** 用 fine-tuning loss drop、backbone displacement 与 reference-model debiasing构成 dataset-level contamination-risk sensor，处理连续时序的缩放/重采样重复。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 Problem formulation; §4 TSFMAudit; §4.1 adaptation traces; §4.2 reference-model debiasing; §4.3 calibration and decision`；Evaluation=`§5 Experiments on six TSFMs/187 datasets; §5.5 practical deployment; Appendix B audit protocol`；Limitations/Counterevidence=`Appendix A contamination labels and transformed-duplicate semantics; proxy labels depend on incomplete official corpus documentation`。

<!-- claim:SF-2026-ARXIV-2605-26161:start -->标签来自不完整训练来源文档，参考模型与 probe protocol 会影响 verdict；结论绑定 TSFM/time-series。Ch27/Ch66 已拥有 contamination identity、transformed duplicate 与受限 sensor/release boundary，故不扩写领域特例。<!-- claim:SF-2026-ARXIV-2605-26161:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26161:end -->

<!-- review:SF-2026-ARXIV-2605-26162:start -->
#### On the Push-Based Asynchronous Federated Learning: A Bias-Correction Aggregation Approach

**问题与机制。** 在无中心异步联邦训练中用 push-sum numerator/denominator、in-flight mass 与 buffered message state 修正有向图聚合偏差，并以 centroid dictionary 压缩通信。 系统 owner=`TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1 路径。** Method=`§4 PushCen-ADFL; §4.2 centroid regularization; §4.3 compression; §4.4 push-sum aggregation; §4.5 buffered updates; Appendix C event-driven state accounting`；Evaluation=`§5 Experiments; §5.1.4 delayed-client protocol; §5.2 accuracy/communication/overhead; §5.3 delayed clients`；Limitations/Counterevidence=`§4.6 assumptions and Appendix C: bounded staleness, directed mixing, bounded compression error and simulated event-driven network`。

<!-- claim:SF-2026-ARXIV-2605-26162:start -->实验用 event-driven simulator、vision models 和受控 client delay；收敛依赖 bounded staleness/mixing/compression-error 假设，不能证明真实 WAN、Byzantine client 或大模型训练。<!-- claim:SF-2026-ARXIV-2605-26162:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26162:end -->

<!-- review:SF-2026-ARXIV-2605-26165:start -->
#### Tool-Schema Compression Enables Agentic RAG Under Constrained Context Budgets

**问题与机制。** We present the first systematic study of this tool-context trade-off, evaluating 14 models spanning 1.5B-32B local models plus one frontier API model across 6,566 controlled API calls at three context budgets (8K, 16K, 32K) with 28 tool definitions. 系统 owner=`AGENT-CONTEXT`。

**Exact-v1 路径。** Method=`§3 tool-schema compression`；Evaluation=`§4 agentic-RAG evaluation`；Limitations/Counterevidence=`§5 limitations and context/tool-library boundary`。

<!-- claim:SF-2026-ARXIV-2605-26165:start -->Tool-Schema Compression Enables Agentic RAG Under Constrained Context Budgets 的 exact-v1 只支持该文披露机制：We present the first systematic study of this tool-context trade-off, evaluating 14 models spanning 1.5B-32B local models plus one frontier API model across 6,566 controlled API calls at three context budgets (8K, 16K, 32K) with 28 tool definitions. 其未证明边界由 `§5 limitations and context/tool-library boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-26165:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26165:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-20615 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2606-20615 |
| SF-2026-ARXIV-2605-24817 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24817 |
| SF-2026-ARXIV-2605-24818 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24818 |
| SF-2026-ARXIV-2605-24823 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24823 |
| SF-2026-ARXIV-2605-24832 | score_7_9; forced_review; potential_books_delta | selected | DA-DIFFUSION-ELASTIC-SERVING | — | 跨层改变 runtime/evaluation/memory ownership，且 current Books 存在可定位长期缺口 | analysis:DA-DIFFUSION-ELASTIC-SERVING |
| SF-2026-ARXIV-2605-24870 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24870 |
| SF-2026-ARXIV-2605-24879 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24879 |
| SF-2026-ARXIV-2605-24883 | score_7_9; forced_review; potential_books_delta | selected | DA-POLICY-TO-SAFETY-TEST | — | 跨层改变 runtime/evaluation/memory ownership，且 current Books 存在可定位长期缺口 | analysis:DA-POLICY-TO-SAFETY-TEST |
| SF-2026-ARXIV-2605-24892 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24892 |
| SF-2026-ARXIV-2605-24914 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24914 |
| SF-2026-ARXIV-2605-24922 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24922 |
| SF-2026-ARXIV-2605-24930 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24930 |
| SF-2026-ARXIV-2605-24941 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24941 |
| SF-2026-ARXIV-2605-24973 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-24973 |
| SF-2026-ARXIV-2605-25002 | score_7_9; forced_review; potential_books_delta | selected | DA-MEMORY-ATTRIBUTION-WATERMARK | — | 跨层改变 runtime/evaluation/memory ownership，且 current Books 存在可定位长期缺口 | analysis:DA-MEMORY-ATTRIBUTION-WATERMARK |
| SF-2026-ARXIV-2605-25052 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25052 |
| SF-2026-ARXIV-2605-25073 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25073 |
| SF-2026-ARXIV-2605-25077 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25077 |
| SF-2026-ARXIV-2605-25085 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25085 |
| SF-2026-ARXIV-2605-25092 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25092 |
| SF-2026-ARXIV-2605-25133 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25133 |
| SF-2026-ARXIV-2605-25160 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25160 |
| SF-2026-ARXIV-2605-25188 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25188 |
| SF-2026-ARXIV-2605-25189 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25189 |
| SF-2026-ARXIV-2605-25233 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25233 |
| SF-2026-ARXIV-2605-25240 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25240 |
| SF-2026-ARXIV-2605-25244 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25244 |
| SF-2026-ARXIV-2605-25247 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25247 |
| SF-2026-ARXIV-2605-25252 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25252 |
| SF-2026-ARXIV-2605-25272 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25272 |
| SF-2026-ARXIV-2605-25284 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25284 |
| SF-2026-ARXIV-2605-25292 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25292 |
| SF-2026-ARXIV-2605-25298 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25298 |
| SF-2026-ARXIV-2605-25313 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-25313 |
| SF-2026-ARXIV-2605-26154 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-26154 |
| SF-2026-ARXIV-2605-26156 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-26156 |
| SF-2026-ARXIV-2605-26158 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-26158 |
| SF-2026-ARXIV-2605-26159 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-26159 |
| SF-2026-ARXIV-2605-26161 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-26161 |
| SF-2026-ARXIV-2605-26162 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-26162 |
| SF-2026-ARXIV-2605-26165 | score_7_9 | not_selected | — | — | exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束 | analysis-decision:SF-2026-ARXIV-2605-26165 |

<!-- analysis:DA-DIFFUSION-ELASTIC-SERVING:start -->
### DA-DIFFUSION-ELASTIC-SERVING

固定 diffusion step 在请求同质、质量阈值稳定时最简单；负载与请求难度变化后，固定步数同时制造短请求浪费和难请求欠算。Optimus 把剩余 refinement step、质量状态与 batching 交给 runtime controller，以弹性 decoding granularity 换取更复杂的校准、service-time variance 和 admission/scheduling。证据只覆盖作者披露的 diffusion-LM、硬件与 SLO；控制器失准时回退固定步数。
<!-- analysis:DA-DIFFUSION-ELASTIC-SERVING:end -->

<!-- analysis:DA-POLICY-TO-SAFETY-TEST:start -->
### DA-POLICY-TO-SAFETY-TEST

人工 benchmark 适合稳定 policy，却难证明每条规则和组合路径都被覆盖；无约束 red-team 又难回溯到哪条 policy 缺口。POLARIS 把 policy 编译为 predicate graph，再从未覆盖路径实例化 tests，使 policy revision、test identity 和 coverage evidence 同步演进。收益是系统化覆盖，代价是 policy formalization error、生成成本与单轮范围；规则不完整或进入多轮 state 时回退人工 threat modeling 与独立 red team。
<!-- analysis:DA-POLICY-TO-SAFETY-TEST:end -->

<!-- analysis:DA-MEMORY-ATTRIBUTION-WATERMARK:start -->
### DA-MEMORY-ATTRIBUTION-WATERMARK

普通 memory watermark 标记存储内容，却难判断某段 latent memory state 经哪次 write/update 演化而来。MemMark 把 owner-controlled signal 写入 memory-write decision，用 attribution robustness 换取写入扰动、检测校准和 adaptive attacker 风险。它是 ownership sensor，不是真值或 authorization；信号冲突时保留原始 episode、write receipt 与独立 provenance。
<!-- analysis:DA-MEMORY-ATTRIBUTION-WATERMARK:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-20615:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2606-20615:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24817:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-24817:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24818:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-24818:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24823:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-24823:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24870:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-24870:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24879:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-24879:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24892:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-24892:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24914:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-24914:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24922:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-24922:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24930:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-24930:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24941:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-24941:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24973:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-24973:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25052:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25052:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25073:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25073:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25077:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25077:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25085:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25085:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25092:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25092:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25133:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25133:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25160:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25160:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25188:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25188:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25189:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25189:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25233:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25233:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25240:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25240:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25244:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25244:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25247:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25247:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25252:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25252:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25272:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25272:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25284:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25284:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25292:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25292:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25298:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25298:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-25313:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-25313:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-26154:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-26154:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-26156:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-26156:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-26158:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-26158:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-26159:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-26159:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-26161:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-26161:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-26162:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-26162:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-26165:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:SF-2026-ARXIV-2605-26165:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-20615 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2606-20615 | delta:SF-2026-ARXIV-2606-20615 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20615 |
| SF-2026-ARXIV-2605-24817 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-24817 | delta:SF-2026-ARXIV-2605-24817 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24817 |
| SF-2026-ARXIV-2605-24818 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24818 | delta:SF-2026-ARXIV-2605-24818 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24818 |
| SF-2026-ARXIV-2605-24823 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-24823 | delta:SF-2026-ARXIV-2605-24823 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24823 |
| SF-2026-ARXIV-2605-24832 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-24832 | delta:SF-2026-ARXIV-2605-24832 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24832 |
| SF-2026-ARXIV-2605-24870 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-24870 | delta:SF-2026-ARXIV-2605-24870 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24870 |
| SF-2026-ARXIV-2605-24879 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24879 | delta:SF-2026-ARXIV-2605-24879 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24879 |
| SF-2026-ARXIV-2605-24883 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24883 | delta:SF-2026-ARXIV-2605-24883 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24883 |
| SF-2026-ARXIV-2605-24892 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-24892 | delta:SF-2026-ARXIV-2605-24892 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24892 |
| SF-2026-ARXIV-2605-24914 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-24914 | delta:SF-2026-ARXIV-2605-24914 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24914 |
| SF-2026-ARXIV-2605-24922 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-24922 | delta:SF-2026-ARXIV-2605-24922 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24922 |
| SF-2026-ARXIV-2605-24930 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#chapter-22 | books/part-02-model/21-moe.md#chapter-21;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-24930 | delta:SF-2026-ARXIV-2605-24930 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24930 |
| SF-2026-ARXIV-2605-24941 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-24941 | delta:SF-2026-ARXIV-2605-24941 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24941 |
| SF-2026-ARXIV-2605-24973 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-24973 | delta:SF-2026-ARXIV-2605-24973 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24973 |
| SF-2026-ARXIV-2605-25002 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-25002 | delta:SF-2026-ARXIV-2605-25002 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25002 |
| SF-2026-ARXIV-2605-25052 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25052 | delta:SF-2026-ARXIV-2605-25052 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25052 |
| SF-2026-ARXIV-2605-25073 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-25073 | delta:SF-2026-ARXIV-2605-25073 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25073 |
| SF-2026-ARXIV-2605-25077 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-25077 | delta:SF-2026-ARXIV-2605-25077 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25077 |
| SF-2026-ARXIV-2605-25085 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-25085 | delta:SF-2026-ARXIV-2605-25085 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25085 |
| SF-2026-ARXIV-2605-25092 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-25092 | delta:SF-2026-ARXIV-2605-25092 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25092 |
| SF-2026-ARXIV-2605-25133 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25133 | delta:SF-2026-ARXIV-2605-25133 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25133 |
| SF-2026-ARXIV-2605-25160 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25160 | delta:SF-2026-ARXIV-2605-25160 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25160 |
| SF-2026-ARXIV-2605-25188 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-25188 | delta:SF-2026-ARXIV-2605-25188 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25188 |
| SF-2026-ARXIV-2605-25189 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-25189 | delta:SF-2026-ARXIV-2605-25189 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25189 |
| SF-2026-ARXIV-2605-25233 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-25233 | delta:SF-2026-ARXIV-2605-25233 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25233 |
| SF-2026-ARXIV-2605-25240 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25240 | delta:SF-2026-ARXIV-2605-25240 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25240 |
| SF-2026-ARXIV-2605-25244 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-05-inference-system/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25244 | delta:SF-2026-ARXIV-2605-25244 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25244 |
| SF-2026-ARXIV-2605-25247 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-05-inference-system/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-25247 | delta:SF-2026-ARXIV-2605-25247 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25247 |
| SF-2026-ARXIV-2605-25252 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-25252 | delta:SF-2026-ARXIV-2605-25252 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25252 |
| SF-2026-ARXIV-2605-25272 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-25272 | delta:SF-2026-ARXIV-2605-25272 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25272 |
| SF-2026-ARXIV-2605-25284 | AGENT-PLANNING | books/part-07-agent/79-planning.md#chapter-79 | books/part-07-agent/78-tool-calling.md#chapter-78;books/part-07-agent/80-reflection.md#chapter-80 | existing:SF-2026-ARXIV-2605-25284 | delta:SF-2026-ARXIV-2605-25284 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25284 |
| SF-2026-ARXIV-2605-25292 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#chapter-63 | books/part-06-ai-infrastructure/62-gateway.md#chapter-62;books/part-06-ai-infrastructure/64-volcano.md#chapter-64 | existing:SF-2026-ARXIV-2605-25292 | delta:SF-2026-ARXIV-2605-25292 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25292 |
| SF-2026-ARXIV-2605-25298 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-25298 | delta:SF-2026-ARXIV-2605-25298 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-25298 |
| SF-2026-ARXIV-2605-25313 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-25313 | delta:SF-2026-ARXIV-2605-25313 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-25313 |
| SF-2026-ARXIV-2605-26154 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26154 | delta:SF-2026-ARXIV-2605-26154 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26154 |
| SF-2026-ARXIV-2605-26156 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26156 | delta:SF-2026-ARXIV-2605-26156 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26156 |
| SF-2026-ARXIV-2605-26158 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26158 | delta:SF-2026-ARXIV-2605-26158 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26158 |
| SF-2026-ARXIV-2605-26159 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-26159 | delta:SF-2026-ARXIV-2605-26159 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26159 |
| SF-2026-ARXIV-2605-26161 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26161 | delta:SF-2026-ARXIV-2605-26161 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26161 |
| SF-2026-ARXIV-2605-26162 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-26162 | delta:SF-2026-ARXIV-2605-26162 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26162 |
| SF-2026-ARXIV-2605-26165 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-26165 | delta:SF-2026-ARXIV-2605-26165 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26165 |
<!-- books-review:SF-2026-ARXIV-2606-20615:start -->
<!-- existing:SF-2026-ARXIV-2606-20615:start -->已顺读 `books/part-07-agent/81-workflow.md` 及相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；当前主干=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2606-20615:end -->
<!-- delta:SF-2026-ARXIV-2606-20615:start -->We propose a domain-specific language for specifying AI-SDLC processes as protocols, with formal abstract syntax, well-formedness conditions, operational semantics, and enforcement invariants, organised around a separation of policy (declared intent) from mechanism (structural enforcement).<!-- delta:SF-2026-ARXIV-2606-20615:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2606-20615:end -->
<!-- books-review:SF-2026-ARXIV-2605-24817:start -->
<!-- existing:SF-2026-ARXIV-2605-24817:start -->已顺读 `books/part-06-ai-infrastructure/67-monitoring.md` 及相邻章节 ['books/part-06-ai-infrastructure/66-evaluation-system.md', 'books/part-06-ai-infrastructure/68-logging.md']；当前主干=['本章要回答的问题', '先定义目标，再选择可测信号', 'Context generator 是 pre-failure sensor identity 的一部分', 'Review notes', '四层指标', 'Autonomy 不是一个纯模型指标', '从单次 Query 指标到 Session-level Search Trajectory Sensor', 'Rate、Errors、Duration 与 Saturation']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-24817:end -->
<!-- delta:SF-2026-ARXIV-2605-24817:start -->Inspired by this observation, we propose RouteScan, a non-intrusive auditing framework for detecting harmful behaviors through such routing-induced GPU telemetry.<!-- delta:SF-2026-ARXIV-2605-24817:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24817:end -->
<!-- books-review:SF-2026-ARXIV-2605-24818:start -->
<!-- existing:SF-2026-ARXIV-2605-24818:start -->Ch27/Ch66 已有 contamination identity、decontamination 与 release evidence，但没有用主动已知污染率拟合 score-correction curve。<!-- existing:SF-2026-ARXIV-2605-24818:end -->
<!-- delta:SF-2026-ARXIV-2605-24818:start -->在已知比例主动注入 benchmark 样本并拟合 contamination-response curve，把污染校正从事后猜测变成带干预记录的 evaluation protocol。<!-- delta:SF-2026-ARXIV-2605-24818:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24818:end -->
<!-- books-review:SF-2026-ARXIV-2605-24823:start -->
<!-- existing:SF-2026-ARXIV-2605-24823:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-24823:end -->
<!-- delta:SF-2026-ARXIV-2605-24823:start -->Manufacturing has passed through four widely recognized paradigms - mechanization, electrification, programmable automation, and Smart Manufacturing - each defined by the kind of work it shifted from humans to machines.<!-- delta:SF-2026-ARXIV-2605-24823:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24823:end -->
<!-- books-review:SF-2026-ARXIV-2605-24832:start -->
<!-- existing:SF-2026-ARXIV-2605-24832:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 及相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前主干=['本章要回答的问题', '从计算图开始', '三类基础优化', 'Execution Plan 可以修订，但只能在安全边界 Commit', '异步工作不必永久绑定固定 Physical Core', '从粗粒度 Offload 到负载观测的 Tensor Placement', 'Backend Choice 必须携带 Previous-backend State', 'Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-24832:end -->
<!-- delta:SF-2026-ARXIV-2605-24832:start -->We present Optimus, a serving system that enables elastic decoding for diffusion LLMs by dynamically adapting decoding granularity to runtime load.<!-- delta:SF-2026-ARXIV-2605-24832:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24832:end -->
<!-- books-review:SF-2026-ARXIV-2605-24870:start -->
<!-- existing:SF-2026-ARXIV-2605-24870:start -->Ch24 已有 sensitivity/error-budget cache 与 recompute fallback，但没有把 calibration prior 绑定到被先前 correction 改写后的 denoising trajectory。<!-- existing:SF-2026-ARXIV-2605-24870:end -->
<!-- delta:SF-2026-ARXIV-2605-24870:start -->把 diffusion cache 的误差从单点 representation mismatch 扩展为会被先前校准继续改写的 trajectory state，并沿 corrected history 逐步拟合 site-local calibration prior。<!-- delta:SF-2026-ARXIV-2605-24870:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24870:end -->
<!-- books-review:SF-2026-ARXIV-2605-24879:start -->
<!-- existing:SF-2026-ARXIV-2605-24879:start -->Ch72 已要求 DP sampling/clipping/noise/accounting 实现等价，却没有覆盖 randomized norm estimator 改变 clipping mechanism 后必须配套重建 accountant 与资源合同。<!-- existing:SF-2026-ARXIV-2605-24879:end -->
<!-- delta:SF-2026-ARXIV-2605-24879:start -->用 Hutchinson/Hutch++ 随机 trace estimation 近似 per-sample gradient norm，把 DP clipping 的显存复杂度从显式 T×T 或 d×d 中间量改为受投影维度控制的 estimator，并为随机 clipping 单独建立 privacy accountant。<!-- delta:SF-2026-ARXIV-2605-24879:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24879:end -->
<!-- books-review:SF-2026-ARXIV-2605-24883:start -->
<!-- existing:SF-2026-ARXIV-2605-24883:start -->Ch66/Ch72 已有 red-team、policy revision 与独立 guard，但没有从 policy predicate graph 生成 coverage-traceable tests。<!-- existing:SF-2026-ARXIV-2605-24883:end -->
<!-- delta:SF-2026-ARXIV-2605-24883:start -->把自然语言 safety policy 编译为形式化谓词和语义图，再从未覆盖路径生成可追踪测试，使 policy revision、test identity 与 coverage evidence 成为同一评估对象。<!-- delta:SF-2026-ARXIV-2605-24883:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24883:end -->
<!-- books-review:SF-2026-ARXIV-2605-24892:start -->
<!-- existing:SF-2026-ARXIV-2605-24892:start -->Ch25 已有 transition-token reasoner、appearance renderer、多时间尺度状态和 closed-loop evidence boundary。<!-- existing:SF-2026-ARXIV-2605-24892:end -->
<!-- delta:SF-2026-ARXIV-2605-24892:start -->把低熵相邻帧预测改成跨语义时间块的自回归 future-state 预测：块内保留稠密瞬时动态、块间保留稀疏长程因果，并把 action/latent prediction 与多视角 renderer 分责。<!-- delta:SF-2026-ARXIV-2605-24892:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24892:end -->
<!-- books-review:SF-2026-ARXIV-2605-24914:start -->
<!-- existing:SF-2026-ARXIV-2605-24914:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前主干=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-24914:end -->
<!-- delta:SF-2026-ARXIV-2605-24914:start -->To reduce LLM costs and latency, semantic caching systems must accurately identify when a new prompt matches a cached one.<!-- delta:SF-2026-ARXIV-2605-24914:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24914:end -->
<!-- books-review:SF-2026-ARXIV-2605-24922:start -->
<!-- existing:SF-2026-ARXIV-2605-24922:start -->Ch25/Ch26 已有 simulator/observed-state authority 与 rollback，但没有 executor-owned per-environment persistent batched runtime lifecycle。<!-- existing:SF-2026-ARXIV-2605-24922:end -->
<!-- delta:SF-2026-ARXIV-2605-24922:start -->把 stateless rollout 调用提升为 executor-owned persistent environment pool，使 per-environment model/data、reset、step 与 Jacobian state 在 batched robot-learning loop 中保持可寻址。<!-- delta:SF-2026-ARXIV-2605-24922:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24922:end -->
<!-- books-review:SF-2026-ARXIV-2605-24930:start -->
<!-- existing:SF-2026-ARXIV-2605-24930:start -->Ch22 已有 coarse global summary、query-aware hierarchical sparse selection、selector miss 与 dense fallback。<!-- existing:SF-2026-ARXIV-2605-24930:end -->
<!-- delta:SF-2026-ARXIV-2605-24930:start -->先把长文档组织成语义树，再用层级 memory tokens 与 query-aware routing 在粗摘要和细粒度节点间分配注意力预算。<!-- delta:SF-2026-ARXIV-2605-24930:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24930:end -->
<!-- books-review:SF-2026-ARXIV-2605-24941:start -->
<!-- existing:SF-2026-ARXIV-2605-24941:start -->已顺读 `books/part-07-agent/78-tool-calling.md` 及相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前主干=['本章要回答的问题', '从生成文本到环境转移', 'Tool Contract', '模型输出只是 Proposal', '编译器反馈可以前移，但仍是受限 Authority', 'Tool Discovery 与选择', 'Interface Granularity：不是 Tool 越多越有能力', 'Agent-friendly Tool 不等于把 CLI 包一层']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-24941:end -->
<!-- delta:SF-2026-ARXIV-2605-24941:start -->We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they are not applicable.<!-- delta:SF-2026-ARXIV-2605-24941:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-24941:end -->
<!-- books-review:SF-2026-ARXIV-2605-24973:start -->
<!-- existing:SF-2026-ARXIV-2605-24973:start -->Ch76 已有 document/page/region provenance 与 ingestion identity，但没有跨页结构修复、chunk synchronization 及原页 fallback 的同一 lifecycle。<!-- existing:SF-2026-ARXIV-2605-24973:end -->
<!-- delta:SF-2026-ARXIV-2605-24973:start -->在 page OCR 之后增加 document-level state owner，跨页合并段落/表格并同步 chunk 与结构索引，使 ingestion 输出可被 RAG 以同一 document revision 消费。<!-- delta:SF-2026-ARXIV-2605-24973:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-24973:end -->
<!-- books-review:SF-2026-ARXIV-2605-25002:start -->
<!-- existing:SF-2026-ARXIV-2605-25002:start -->已顺读 `books/part-07-agent/77-memory.md` 及相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前主干=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25002:end -->
<!-- delta:SF-2026-ARXIV-2605-25002:start -->We propose MemMark, a state-evolution attribution watermark that embeds an owner-controlled signal into latent memory-write decisions.<!-- delta:SF-2026-ARXIV-2605-25002:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25002:end -->
<!-- books-review:SF-2026-ARXIV-2605-25052:start -->
<!-- existing:SF-2026-ARXIV-2605-25052:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25052:end -->
<!-- delta:SF-2026-ARXIV-2605-25052:start -->Building on this methodology, we present BonaFide, a benchmark of 3,066 labeled CoTs across 13 tasks and 10 models, and use it to conduct the first systematic evaluation of prominent faithfulness metrics.<!-- delta:SF-2026-ARXIV-2605-25052:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25052:end -->
<!-- books-review:SF-2026-ARXIV-2605-25073:start -->
<!-- existing:SF-2026-ARXIV-2605-25073:start -->Ch72 已沿 data/supply-chain、training update、adapter artifact、runtime monitor 与 release Gate 组织 fine-tuning security lifecycle。<!-- existing:SF-2026-ARXIV-2605-25073:end -->
<!-- delta:SF-2026-ARXIV-2605-25073:start -->把 fine-tuning attack surface 按 pre-tuning input/supply chain、during-tuning optimizer/update 与 post-tuning adapter/artifact 三个 intervention phase 组织，并用同一基座和协议检查跨 phase 防御组合。<!-- delta:SF-2026-ARXIV-2605-25073:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25073:end -->
<!-- books-review:SF-2026-ARXIV-2605-25077:start -->
<!-- existing:SF-2026-ARXIV-2605-25077:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前主干=['本章要回答的问题', '从三个容易混淆的对象开始', 'Video generation', 'Predictive environment model', 'Controllable world model', '在谈 State 之前，先声明预测 Channel', '为什么旧的 Simulator 仍然合理', '演进路线']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25077:end -->
<!-- delta:SF-2026-ARXIV-2605-25077:start -->We present WorldCraft, a framework that expands interactive video world models from camera navigation to object-level trajectory actions.<!-- delta:SF-2026-ARXIV-2605-25077:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25077:end -->
<!-- books-review:SF-2026-ARXIV-2605-25085:start -->
<!-- existing:SF-2026-ARXIV-2605-25085:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前主干=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25085:end -->
<!-- delta:SF-2026-ARXIV-2605-25085:start -->We study the rate-distortion limits of online KV cache compression in autoregressive language models, formulating it as sequential Wyner-Ziv source coding on the filtration induced by the model, with the next-step query as decoder side information.<!-- delta:SF-2026-ARXIV-2605-25085:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25085:end -->
<!-- books-review:SF-2026-ARXIV-2605-25092:start -->
<!-- existing:SF-2026-ARXIV-2605-25092:start -->已顺读 `books/part-07-agent/77-memory.md` 及相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前主干=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25092:end -->
<!-- delta:SF-2026-ARXIV-2605-25092:start -->Long-term conversational memory is a retrieval workload classical IR was not built for: the index grows during the query stream, query types shift intra-session, and the latency budget per retrieval is sub-10 ms.<!-- delta:SF-2026-ARXIV-2605-25092:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25092:end -->
<!-- books-review:SF-2026-ARXIV-2605-25133:start -->
<!-- existing:SF-2026-ARXIV-2605-25133:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25133:end -->
<!-- delta:SF-2026-ARXIV-2605-25133:start -->We introduce prover-verifier deliberation (PVD), an inference-time protocol grounded in interactive proof theory, as a mechanism for selective prediction: the protocol produces both an answer and a structured confidence verdict, allowing a system to report high-confidence answers while abstaining on uncertain cases.<!-- delta:SF-2026-ARXIV-2605-25133:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25133:end -->
<!-- books-review:SF-2026-ARXIV-2605-25160:start -->
<!-- existing:SF-2026-ARXIV-2605-25160:start -->Ch66/Ch81 已把 generated environment、task constraint、validator、marker 与真实 backend authority 分开。<!-- existing:SF-2026-ARXIV-2605-25160:end -->
<!-- delta:SF-2026-ARXIV-2605-25160:start -->由 coding agent 合成可执行 mobile-app simulator，再独立生成 task 与 state validator，把 GUI agent benchmark 的 environment 和 outcome evidence 版本化。<!-- delta:SF-2026-ARXIV-2605-25160:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25160:end -->
<!-- books-review:SF-2026-ARXIV-2605-25188:start -->
<!-- existing:SF-2026-ARXIV-2605-25188:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 及相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前主干=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25188:end -->
<!-- delta:SF-2026-ARXIV-2605-25188:start -->Multi-agent LLM systems improve reasoning by combining outputs from multiple agents, but interaction-heavy methods can introduce error propagation and high communication overhead.<!-- delta:SF-2026-ARXIV-2605-25188:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25188:end -->
<!-- books-review:SF-2026-ARXIV-2605-25189:start -->
<!-- existing:SF-2026-ARXIV-2605-25189:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 及相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前主干=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25189:end -->
<!-- delta:SF-2026-ARXIV-2605-25189:start -->We study this failure mode through the geometry of reinforcement learning updates in language models and argue that hacking emerges when optimization drifts away from a stable low-dimensional learning trajectory.<!-- delta:SF-2026-ARXIV-2605-25189:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25189:end -->
<!-- books-review:SF-2026-ARXIV-2605-25233:start -->
<!-- existing:SF-2026-ARXIV-2605-25233:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 及相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前主干=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25233:end -->
<!-- delta:SF-2026-ARXIV-2605-25233:start -->We present Meta-Agent, a two-phase framework that automatically constructs and executes specialized multi-agent systems from natural-language task descriptions.<!-- delta:SF-2026-ARXIV-2605-25233:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25233:end -->
<!-- books-review:SF-2026-ARXIV-2605-25240:start -->
<!-- existing:SF-2026-ARXIV-2605-25240:start -->Ch66 已比较 judge/metric 风险，但没有把 rubric 与 pairwise preference 作为不同 measurement operator 做受控同台选择。<!-- existing:SF-2026-ARXIV-2605-25240:end -->
<!-- delta:SF-2026-ARXIV-2605-25240:start -->把 rubric score 与 pairwise preference 作为不同 measurement operators，在同一受控质量阶梯上比较各自一致性与区分力，而不是默认二者可互换。<!-- delta:SF-2026-ARXIV-2605-25240:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25240:end -->
<!-- books-review:SF-2026-ARXIV-2605-25244:start -->
<!-- existing:SF-2026-ARXIV-2605-25244:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-05-inference-system/README.md']；当前主干=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25244:end -->
<!-- delta:SF-2026-ARXIV-2605-25244:start -->In this paper, we investigate the dynamics of confidence along reasoning trajectories and for first time reveal a surprising and unique pattern: correct answer traces tend to exhibit confidence improvement over time (positive confidence gain), while incorrect traces show attenuated or declining confidence as reasoning proceeds.<!-- delta:SF-2026-ARXIV-2605-25244:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25244:end -->
<!-- books-review:SF-2026-ARXIV-2605-25247:start -->
<!-- existing:SF-2026-ARXIV-2605-25247:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-05-inference-system/README.md']；当前主干=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25247:end -->
<!-- delta:SF-2026-ARXIV-2605-25247:start -->To improve the design and operation of LLM ecosystems, we envision simulators and simulation-based digital twins becoming primary decision-making tools.<!-- delta:SF-2026-ARXIV-2605-25247:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25247:end -->
<!-- books-review:SF-2026-ARXIV-2605-25252:start -->
<!-- existing:SF-2026-ARXIV-2605-25252:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 及相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前主干=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25252:end -->
<!-- delta:SF-2026-ARXIV-2605-25252:start -->Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training language models, but in practice, verifiers are rarely perfect.<!-- delta:SF-2026-ARXIV-2605-25252:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25252:end -->
<!-- books-review:SF-2026-ARXIV-2605-25272:start -->
<!-- existing:SF-2026-ARXIV-2605-25272:start -->Ch66 已要求 construct validity 和 slice/uncertainty，但没有用 latent measurement model 分离共同构念与 benchmark-specific variance。<!-- existing:SF-2026-ARXIV-2605-25272:end -->
<!-- delta:SF-2026-ARXIV-2605-25272:start -->用 latent measurement model 分解 benchmark 共同因子与 task-specific variance，使 release evidence 能区分能力构念、数据生态和 leaderboard 聚合造成的相关性。<!-- delta:SF-2026-ARXIV-2605-25272:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25272:end -->
<!-- books-review:SF-2026-ARXIV-2605-25284:start -->
<!-- existing:SF-2026-ARXIV-2605-25284:start -->已顺读 `books/part-07-agent/79-planning.md` 及相邻章节 ['books/part-07-agent/78-tool-calling.md', 'books/part-07-agent/80-reflection.md']；当前主干=['本章要回答的问题', 'Plan 不是解释文本', '从目标到状态图', 'Decomposition 的价值与代价', '依赖、并行与 Critical Path', 'Subtask Parallelism 与 Trial Parallelism 解决的不是同一个等待', 'Replanning 的触发条件', 'Search-based Planning 的边界']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25284:end -->
<!-- delta:SF-2026-ARXIV-2605-25284:start -->To study these abilities, we evaluate models on ambiguous, unambiguous, and disambiguated questions in three settings: standard question answering, explicit ambiguity judgment, and behavioral analysis, where a judge model classifies responses as direct answers, refusals, or clarifying questions.<!-- delta:SF-2026-ARXIV-2605-25284:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25284:end -->
<!-- books-review:SF-2026-ARXIV-2605-25292:start -->
<!-- existing:SF-2026-ARXIV-2605-25292:start -->Ch63–65 已让 dependency、resource/topology、energy/carbon/telemetry state 进入 Kubernetes/Slurm placement owner，并保留 heuristic fallback。<!-- existing:SF-2026-ARXIV-2605-25292:end -->
<!-- delta:SF-2026-ARXIV-2605-25292:start -->让 scheduler 消费由 Digital Twin 维护的 node power/carbon/anomaly state，并把 heterogeneous workflow 先转成正式 dependency/resource model，再输出 Kubernetes/Slurm placement。<!-- delta:SF-2026-ARXIV-2605-25292:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25292:end -->
<!-- books-review:SF-2026-ARXIV-2605-25298:start -->
<!-- existing:SF-2026-ARXIV-2605-25298:start -->Ch67/69 已区分 metrics 与 trace/dependency graph，但没有从 request entry thread 沿 backing-resource identity 追踪 kernel-level contention propagation。<!-- existing:SF-2026-ARXIV-2605-25298:end -->
<!-- delta:SF-2026-ARXIV-2605-25298:start -->从 thread-state 时间占比继续下钻到带 backing-resource identity 的 futex/pipe/socket/VFS/block-I/O dependency graph，并从 request entry thread 反向追踪 contention propagation。<!-- delta:SF-2026-ARXIV-2605-25298:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-25298:end -->
<!-- books-review:SF-2026-ARXIV-2605-25313:start -->
<!-- existing:SF-2026-ARXIV-2605-25313:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前主干=['本章要回答的问题', '从三个容易混淆的对象开始', 'Video generation', 'Predictive environment model', 'Controllable world model', '在谈 State 之前，先声明预测 Channel', '为什么旧的 Simulator 仍然合理', '演进路线']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-25313:end -->
<!-- delta:SF-2026-ARXIV-2605-25313:start -->We introduce the Unitary World Model JEPA (UWM-JEPA), a JEPA world model with a density-matrix latent on a joint system-environment space and a learned unitary predictor.<!-- delta:SF-2026-ARXIV-2605-25313:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-25313:end -->
<!-- books-review:SF-2026-ARXIV-2605-26154:start -->
<!-- existing:SF-2026-ARXIV-2605-26154:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26154:end -->
<!-- delta:SF-2026-ARXIV-2605-26154:start -->Experiments across 3 benchmarks, 10 agent backbones, and 3 memory-module implementations show that MemMorph achieves up to 85.9% attack success rate with only three injected records, outperforming the strongest baseline by up to 25% while retaining potency under 3 representative defenses.<!-- delta:SF-2026-ARXIV-2605-26154:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26154:end -->
<!-- books-review:SF-2026-ARXIV-2605-26156:start -->
<!-- existing:SF-2026-ARXIV-2605-26156:start -->Ch66 已把 position/style/self-preference 及 irrelevant-style intervention 写入 judge construct-validity contract。<!-- existing:SF-2026-ARXIV-2605-26156:end -->
<!-- delta:SF-2026-ARXIV-2605-26156:start -->把 judge 的 style sensitivity 暴露为可自适应搜索的黑盒攻击面，并同时测 utility、stealth 与 query budget。<!-- delta:SF-2026-ARXIV-2605-26156:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26156:end -->
<!-- books-review:SF-2026-ARXIV-2605-26158:start -->
<!-- existing:SF-2026-ARXIV-2605-26158:start -->Ch72 已要求 run-centric multi-turn/multimodal campaign、跨 turn cumulative intent 聚合和 sensor/authority 分离。<!-- existing:SF-2026-ARXIV-2605-26158:end -->
<!-- delta:SF-2026-ARXIV-2605-26158:start -->把 refusal 从单一二元阈值改写为可重复采样的 instability band，并把分散于多个 benign-looking probes/视觉片段中的意图在最终 synthesis 时重新组合为跨 turn 攻击。<!-- delta:SF-2026-ARXIV-2605-26158:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26158:end -->
<!-- books-review:SF-2026-ARXIV-2605-26159:start -->
<!-- existing:SF-2026-ARXIV-2605-26159:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26159:end -->
<!-- delta:SF-2026-ARXIV-2605-26159:start -->We present the Device Context Protocol (DCP): a sub-50-byte typical frame (6-byte header + CBOR payload + optional 16-byte HMAC), a manifest schema in which capability scoping, range and type checks, dry-run evaluation, and units-as-types are protocol-layer primitives, and a host-side Bridge that rejects malformed or hallucinated calls before any byte reaches the device.<!-- delta:SF-2026-ARXIV-2605-26159:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26159:end -->
<!-- books-review:SF-2026-ARXIV-2605-26161:start -->
<!-- existing:SF-2026-ARXIV-2605-26161:start -->Ch27/Ch66 已保存 contamination source identity、transformed duplicates、sensor uncertainty 与 clean/contaminated slices。<!-- existing:SF-2026-ARXIV-2605-26161:end -->
<!-- delta:SF-2026-ARXIV-2605-26161:start -->用 fine-tuning loss drop、backbone displacement 与 reference-model debiasing构成 dataset-level contamination-risk sensor，处理连续时序的缩放/重采样重复。<!-- delta:SF-2026-ARXIV-2605-26161:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26161:end -->
<!-- books-review:SF-2026-ARXIV-2605-26162:start -->
<!-- existing:SF-2026-ARXIV-2605-26162:start -->Ch36 已有 asynchronous arrival bias、staleness、client weighting 与 compression，但没有把 push-sum numerator/denominator 和 in-flight mass 写成恢复/收敛状态。<!-- existing:SF-2026-ARXIV-2605-26162:end -->
<!-- delta:SF-2026-ARXIV-2605-26162:start -->在无中心异步联邦训练中用 push-sum numerator/denominator、in-flight mass 与 buffered message state 修正有向图聚合偏差，并以 centroid dictionary 压缩通信。<!-- delta:SF-2026-ARXIV-2605-26162:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26162:end -->
<!-- books-review:SF-2026-ARXIV-2605-26165:start -->
<!-- existing:SF-2026-ARXIV-2605-26165:start -->已顺读 `books/part-07-agent/75-context.md` 及相邻章节 ['books/part-07-agent/74-prompt.md', 'books/part-07-agent/76-rag.md']；当前主干=['本章要回答的问题', 'Context 是一次调用的可见状态', 'Token Budget 是容量约束', '为什么“全塞进去”会失败', 'Context Assembly Pipeline', 'Context Serving 是派生视图生命周期', 'Semantic Policy 与 Recoverable Bookkeeping 应分 Owner', 'Context Compression 的损失']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26165:end -->
<!-- delta:SF-2026-ARXIV-2605-26165:start -->We present the first systematic study of this tool-context trade-off, evaluating 14 models spanning 1.5B-32B local models plus one frontier API model across 6,566 controlled API calls at three context budgets (8K, 16K, 32K) with 28 tool definitions.<!-- delta:SF-2026-ARXIV-2605-26165:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26165:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260525-COVERAGE | fresh-context:isolated-prewrite-reviewer | coverage | coverage:SRC-ARXIV:20260525 | none | fresh-context-independent-audit.json#changes records denominator 24→41 and closures 263→246 | passed |
| SA-20260525-EVIDENCE | fresh-context:isolated-prewrite-reviewer | evidence | review:SF-2026-ARXIV-2606-20615 | none | exact-v1-review-packet-independent-final.json records 41/41 complete and blocked=0 | passed |
| SA-20260525-SELECTION | fresh-context:isolated-prewrite-reviewer | deep_analysis_selection | analysis:DA-DIFFUSION-ELASTIC-SERVING | none | fresh-context-independent-audit.json records the final Optimus, POLARIS and MemMark selection | passed |
| SA-20260525-BOOKS | fresh-context:may2026-day02-postwrite | books | books-review:SF-2026-ARXIV-2606-20615 | none | pre-write queue=16；post-write-semantic-audit.json records two resolved placement findings and 16/16 semantic acceptance | passed |

## 8. Ignored Noise

246 条逐 family pre-denominator closure 保存在 `screening-ledger-independent-final.json`。独立审计重开 18 条系统级 false negative，并把 2605.25310 以具体机制边界降回 closure；每条 closure 保留 family-specific 机制、证据、排除边界和重开条件。

## 9. Recommended Action

16 项 root 串行写回与独立 post-write semantic audit 均已完成；继续保留 exact-v1 evidence boundary，并在后续章节顺读中维护唯一 owner 与相邻衔接。

## 10. Repository Changes

- 新增 2026-05-25 独立 final screening ledger、exact-v1 packet、Books comparison、final queue 与 fresh-context audit。
- 16/16 项已写入 11 个 canonical owner 章节；marker、owner 路径、`Review notes` 前 placement 与 scoped `git diff --check` 已通过。
- 独立 post-write audit 首轮发现 2 处 placement 问题；Ch49 的 diffusion runtime scheduling 与 Ch67 的 thread/resource diagnosis 已仅移动原段，复验后 16/16 通过。
- 更新本 Daily canonical README 到 Coverage/Evidence/Books 全部闭合；未 stage、commit 或 push。

## 11. Open Questions

- 无当日 Gate 阻塞项；后续只需在新证据改变 owner 或结论时重开对应 Source Family。

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 12. Sources

- [Specifying AI-SDLC Processes: A Protocol Language for Human-Agent Boundaries](https://arxiv.org/html/2606.20615v1) — arXiv:2606.20615v1；first-public 2026-05-24；accessed 2026-09-01
- [RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry](https://arxiv.org/html/2605.24817v1) — arXiv:2605.24817v1；first-public 2026-05-24；accessed 2026-09-01
- [Spiking the training data to correct for test set contamination](https://arxiv.org/html/2605.24818v1) — arXiv:2605.24818v1；first-public 2026-05-24；accessed 2026-09-01
- [Agent Manufacturing: Foundation-Model Agents as First-Class Industrial Entities](https://arxiv.org/html/2605.24823v1) — arXiv:2605.24823v1；first-public 2026-05-24；accessed 2026-09-01
- [Optimus: Elastic Decoding for Efficient Diffusion LLM Serving](https://arxiv.org/html/2605.24832v1) — arXiv:2605.24832v1；first-public 2026-05-24；accessed 2026-09-01
- [Trajectory-Consistent Calibration for Cache-Accelerated Diffusion Models](https://arxiv.org/html/2605.24870v1) — arXiv:2605.24870v1；first-public 2026-05-24；accessed 2026-09-01
- [Efficient DP-SGD for LLMs with Randomized Clipping](https://arxiv.org/html/2605.24879v1) — arXiv:2605.24879v1；first-public 2026-05-24；accessed 2026-09-01
- [Inverting the Shield: Systematically Generating Safety Tests from Policy Specifications](https://arxiv.org/html/2605.24883v1) — arXiv:2605.24883v1；first-public 2026-05-24；accessed 2026-09-01
- [X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling](https://arxiv.org/html/2605.24892v1) — arXiv:2605.24892v1；first-public 2026-05-24；accessed 2026-09-01
- [MVR-cache: Optimizing Semantic Caching via Multi-Vector Retrieval and Learned Prompt Segmentation](https://arxiv.org/html/2605.24914v1) — arXiv:2605.24914v1；first-public 2026-05-24；accessed 2026-09-01
- [MuJoCoUni:Persistent Batched Runtime Primitives for MuJoCo](https://arxiv.org/html/2605.24922v1) — arXiv:2605.24922v1；first-public 2026-05-24；accessed 2026-09-01
- [H$^{2}$MT: Semantic Hierarchy-Aware Hierarchical Memory Transformer](https://arxiv.org/html/2605.24930v1) — arXiv:2605.24930v1；first-public 2026-05-24；accessed 2026-09-01
- [Memory-Induced Tool-Drift in LLM Agents](https://arxiv.org/html/2605.24941v1) — arXiv:2605.24941v1；first-public 2026-05-24；accessed 2026-09-01
- [MinerU-Popo: Universal Post-Processing Model for Structured Document Parsing](https://arxiv.org/html/2605.24973v1) — arXiv:2605.24973v1；first-public 2026-05-24；accessed 2026-09-01
- [MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems](https://arxiv.org/html/2605.25002v1) — arXiv:2605.25002v1；first-public 2026-05-24；accessed 2026-09-01
- [Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth](https://arxiv.org/html/2605.25052v1) — arXiv:2605.25052v1；first-public 2026-05-24；accessed 2026-09-01
- [Security in the Fine-Tuning Lifecycle of Large Language Models: Threats, Defenses,Evaluation, and Future Directions](https://arxiv.org/html/2605.25073v1) — arXiv:2605.25073v1；first-public 2026-05-24；accessed 2026-09-01
- [WorldCraft: From Camera Navigation to Object Manipulation in Interactive Video World Models](https://arxiv.org/html/2605.25077v1) — arXiv:2605.25077v1；first-public 2026-05-24；accessed 2026-09-01
- [Polynomial Context-Truncation Sensitivity in Autoregressive Language Models: Sequential Wyner-Ziv Bounds for KV Cache Compression](https://arxiv.org/html/2605.25085v1) — arXiv:2605.25085v1；first-public 2026-05-24；accessed 2026-09-01
- [AgentIR: A Workload-Adaptive Cascade Retrieval Substrate for Long-Term Conversational Memory](https://arxiv.org/html/2605.25092v1) — arXiv:2605.25092v1；first-public 2026-05-24；accessed 2026-09-01
- [Trust but Verify: Prover-Verifier Deliberation for Selective LLM Prediction](https://arxiv.org/html/2605.25133v1) — arXiv:2605.25133v1；first-public 2026-05-24；accessed 2026-09-01
- [SimuWoB: Simulating Real-World Mobile Apps for Fast and Faithful GUI Agent Benchmarking](https://arxiv.org/html/2605.25160v1) — arXiv:2605.25160v1；first-public 2026-05-24；accessed 2026-09-01
- [DarkForest: Less Talk, Higher Accuracy for Multi-Agent LLMs](https://arxiv.org/html/2605.25188v1) — arXiv:2605.25188v1；first-public 2026-05-24；accessed 2026-09-01
- [Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models](https://arxiv.org/html/2605.25189v1) — arXiv:2605.25189v1；first-public 2026-05-24；accessed 2026-09-01
- [Meta-Agent: From Task Descriptions to Verified Multi-Agent Systems](https://arxiv.org/html/2605.25233v1) — arXiv:2605.25233v1；first-public 2026-05-24；accessed 2026-09-01
- [JudgmentBench: Comparing Rubric and Preference Evaluation for Quality Assessment](https://arxiv.org/html/2605.25240v1) — arXiv:2605.25240v1；first-public 2026-05-24；accessed 2026-09-01
- [Inference Time Optimization with Confidence Dynamics](https://arxiv.org/html/2605.25244v1) — arXiv:2605.25244v1；first-public 2026-05-24；accessed 2026-09-01
- [Kavier: Exploring Performance, Sustainability, and Efficiency of LLM Ecosystems under Inference through Cache-Aware Discrete-Event Simulation](https://arxiv.org/html/2605.25247v1) — arXiv:2605.25247v1；first-public 2026-05-24；accessed 2026-09-01
- [Quantifying Empirical Compute-Supervision Tradeoffs in RLVR](https://arxiv.org/html/2605.25252v1) — arXiv:2605.25252v1；first-public 2026-05-24；accessed 2026-09-01
- [AI Cartography: Mapping the Latent Landscape of AI Benchmark Ecosystems](https://arxiv.org/html/2605.25272v1) — arXiv:2605.25272v1；first-public 2026-05-24；accessed 2026-09-01
- [Knowing but Not Showing: LLMs Recognize Ambiguity but Rarely Ask Clarifying Questions](https://arxiv.org/html/2605.25284v1) — arXiv:2605.25284v1；first-public 2026-05-24；accessed 2026-09-01
- [DECICE: AI-Driven Scheduling and Digital Twin Integration for the Cloud-HPC-Edge Compute Continuum](https://arxiv.org/html/2605.25292v1) — arXiv:2605.25292v1；first-public 2026-05-24；accessed 2026-09-01
- [Beyond Thread States: Diagnosing Performance Degradation with eBPF and Thread Dynamics](https://arxiv.org/html/2605.25298v1) — arXiv:2605.25298v1；first-public 2026-05-24；accessed 2026-09-01
- [UWM-JEPA: Predictive World Models That Imagine in Belief Space](https://arxiv.org/html/2605.25313v1) — arXiv:2605.25313v1；first-public 2026-05-24；accessed 2026-09-01
- [MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning](https://arxiv.org/html/2605.26154v1) — arXiv:2605.26154v1；first-public 2026-05-24；accessed 2026-09-01
- [Turning Bias into Bugs: Bandit-Guided Style Manipulation Attacks on LLM Judges](https://arxiv.org/html/2605.26156v1) — arXiv:2605.26156v1；first-public 2026-05-24；accessed 2026-09-01
- [Furina: Fragmented Uncertainty-Driven Refusal Instability Attack](https://arxiv.org/html/2605.26158v1) — arXiv:2605.26158v1；first-public 2026-05-24；accessed 2026-09-01
- [Device Context Protocol: A Compact, Safety-First Architecture for LLM-Driven Control of Constrained Devices](https://arxiv.org/html/2605.26159v1) — arXiv:2605.26159v1；first-public 2026-05-24；accessed 2026-09-01
- [TSFMAudit: Data Contamination Auditing in Forecasting Time Series Foundation Models](https://arxiv.org/html/2605.26161v1) — arXiv:2605.26161v1；first-public 2026-05-24；accessed 2026-09-01
- [On the Push-Based Asynchronous Federated Learning: A Bias-Correction Aggregation Approach](https://arxiv.org/html/2605.26162v1) — arXiv:2605.26162v1；first-public 2026-05-24；accessed 2026-09-01
- [Tool-Schema Compression Enables Agentic RAG Under Constrained Context Budgets](https://arxiv.org/html/2605.26165v1) — arXiv:2605.26165v1；first-public 2026-05-24；accessed 2026-09-01

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

独立 pre-write audit、16/16 Books 写回与独立 post-write semantic audit 均已完成；两处 placement finding 已修复并复验通过。
