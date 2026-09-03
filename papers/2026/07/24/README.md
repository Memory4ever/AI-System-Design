# Daily Research — 2026-07-24

**Research Date:** 2026-07-24

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-23 09:00:00 ～ 2026-07-24 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **555** 个 identity；全量 title + abstract 筛选后冻结 **113** 个候选与 **442** 个 family-specific closure，retain rate **20.36%**。exact-v1 Review 为 113/113：Deep 44、Standard 69、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-24 |
| Window End | 2026-07-24 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-24-0900-v2.1-sha256:af7d7c186284e7efd593606bc721f440a68e3daa98eb67a557250b4ebc4c0fe0 |
| Denominator Frozen At | 2026-09-04T13:30:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260724:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-23T09:00:00+08:00 | 2026-07-24T09:00:00+08:00 | 2026-09-04T13:30:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 555 | SF-2026-ARXIV-2607-20426;SF-2026-ARXIV-2607-20427;SF-2026-ARXIV-2607-20432;SF-2026-ARXIV-2607-20433;SF-2026-ARXIV-2607-20434;SF-2026-ARXIV-2607-20436;SF-2026-ARXIV-2607-20437;SF-2026-ARXIV-2607-20438;SF-2026-ARXIV-2607-20457;SF-2026-ARXIV-2607-20464;SF-2026-ARXIV-2607-20465;SF-2026-ARXIV-2607-20466;SF-2026-ARXIV-2607-20467;SF-2026-ARXIV-2607-20468;SF-2026-ARXIV-2607-20473;SF-2026-ARXIV-2607-20475;SF-2026-ARXIV-2607-20478;SF-2026-ARXIV-2607-20481;SF-2026-ARXIV-2607-20483;SF-2026-ARXIV-2607-20488;SF-2026-ARXIV-2607-20490;SF-2026-ARXIV-2607-20495;SF-2026-ARXIV-2607-20501;SF-2026-ARXIV-2607-20507;SF-2026-ARXIV-2607-20512;SF-2026-ARXIV-2607-20518;SF-2026-ARXIV-2607-20524;SF-2026-ARXIV-2607-20526;SF-2026-ARXIV-2607-20527;SF-2026-ARXIV-2607-20531;SF-2026-ARXIV-2607-20536;SF-2026-ARXIV-2607-20538;SF-2026-ARXIV-2607-20543;SF-2026-ARXIV-2607-20548;SF-2026-ARXIV-2607-20553;SF-2026-ARXIV-2607-20558;SF-2026-ARXIV-2607-20560;SF-2026-ARXIV-2607-20594;SF-2026-ARXIV-2607-20596;SF-2026-ARXIV-2607-20652;SF-2026-ARXIV-2607-20653;SF-2026-ARXIV-2607-20668;SF-2026-ARXIV-2607-20709;SF-2026-ARXIV-2607-20712;SF-2026-ARXIV-2607-20723;SF-2026-ARXIV-2607-20729;SF-2026-ARXIV-2607-20730;SF-2026-ARXIV-2607-20734;SF-2026-ARXIV-2607-20739;SF-2026-ARXIV-2607-20757;SF-2026-ARXIV-2607-20759;SF-2026-ARXIV-2607-20764;SF-2026-ARXIV-2607-20768;SF-2026-ARXIV-2607-20771;SF-2026-ARXIV-2607-20791;SF-2026-ARXIV-2607-20792;SF-2026-ARXIV-2607-20827;SF-2026-ARXIV-2607-20852;SF-2026-ARXIV-2607-20860;SF-2026-ARXIV-2607-20864;SF-2026-ARXIV-2607-20887;SF-2026-ARXIV-2607-20891;SF-2026-ARXIV-2607-20908;SF-2026-ARXIV-2607-20911;SF-2026-ARXIV-2607-20918;SF-2026-ARXIV-2607-20940;SF-2026-ARXIV-2607-20950;SF-2026-ARXIV-2607-20972;SF-2026-ARXIV-2607-20982;SF-2026-ARXIV-2607-20999;SF-2026-ARXIV-2607-21000;SF-2026-ARXIV-2607-21005;SF-2026-ARXIV-2607-21042;SF-2026-ARXIV-2607-21051;SF-2026-ARXIV-2607-21090;SF-2026-ARXIV-2607-21106;SF-2026-ARXIV-2607-21120;SF-2026-ARXIV-2607-21130;SF-2026-ARXIV-2607-21143;SF-2026-ARXIV-2607-21151;SF-2026-ARXIV-2607-21162;SF-2026-ARXIV-2607-21179;SF-2026-ARXIV-2607-21217;SF-2026-ARXIV-2607-21224;SF-2026-ARXIV-2607-21273;SF-2026-ARXIV-2607-21291;SF-2026-ARXIV-2607-21325;SF-2026-ARXIV-2607-21351;SF-2026-ARXIV-2607-21356;SF-2026-ARXIV-2607-21372;SF-2026-ARXIV-2607-21401;SF-2026-ARXIV-2607-21404;SF-2026-ARXIV-2607-21405;SF-2026-ARXIV-2607-21419;SF-2026-ARXIV-2607-21433;SF-2026-ARXIV-2607-21453;SF-2026-ARXIV-2607-21475;SF-2026-ARXIV-2607-21480;SF-2026-ARXIV-2607-21482;SF-2026-ARXIV-2607-21503;SF-2026-ARXIV-2607-21522;SF-2026-ARXIV-2607-21530;SF-2026-ARXIV-2607-21535;SF-2026-ARXIV-2607-21550;SF-2026-ARXIV-2607-21553;SF-2026-ARXIV-2607-21557;SF-2026-ARXIV-2607-21571;SF-2026-ARXIV-2607-21576;SF-2026-ARXIV-2607-21582;SF-2026-ARXIV-2607-21585;SF-2026-ARXIV-2607-21588;SF-2026-ARXIV-2607-21591;SF-2026-ARXIV-2607-21594 | all registered category pages; cross-category dedup complete | 2026-07-24T09:00:00+08:00 | sha256:af7d7c186284e7efd593606bc721f440a68e3daa98eb67a557250b4ebc4c0fe0 | — |
<!-- coverage:SRC-ARXIV:20260724:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-20426 | arXiv:2607.20426v1 | paper-v1:2607.20426 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20426 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20427 | arXiv:2607.20427v1 | paper-v1:2607.20427 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20427 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20432 | arXiv:2607.20432v1 | paper-v1:2607.20432 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20432 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20433 | arXiv:2607.20433v1 | paper-v1:2607.20433 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20433 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20434 | arXiv:2607.20434v1 | paper-v1:2607.20434 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20434 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20436 | arXiv:2607.20436v1 | paper-v1:2607.20436 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20436 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20437 | arXiv:2607.20437v1 | paper-v1:2607.20437 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20437 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20438 | arXiv:2607.20438v1 | paper-v1:2607.20438 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20438 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20457 | arXiv:2607.20457v1 | paper-v1:2607.20457 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20457 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20464 | arXiv:2607.20464v1 | paper-v1:2607.20464 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20464 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20465 | arXiv:2607.20465v1 | paper-v1:2607.20465 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20465 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20466 | arXiv:2607.20466v1 | paper-v1:2607.20466 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20466 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20467 | arXiv:2607.20467v1 | paper-v1:2607.20467 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20467 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20468 | arXiv:2607.20468v1 | paper-v1:2607.20468 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20468 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20473 | arXiv:2607.20473v1 | paper-v1:2607.20473 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20473 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20475 | arXiv:2607.20475v1 | paper-v1:2607.20475 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20475 | self | — | new_in_window | INFER-DECODE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20478 | arXiv:2607.20478v1 | paper-v1:2607.20478 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20478 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20481 | arXiv:2607.20481v1 | paper-v1:2607.20481 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20481 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20483 | arXiv:2607.20483v1 | paper-v1:2607.20483 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20483 | self | — | new_in_window | MODEL-SAMPLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20488 | arXiv:2607.20488v1 | paper-v1:2607.20488 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20488 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20490 | arXiv:2607.20490v1 | paper-v1:2607.20490 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20490 | self | — | new_in_window | PLATFORM-FOUNDATIONS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20495 | arXiv:2607.20495v1 | paper-v1:2607.20495 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20495 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20501 | arXiv:2607.20501v1 | paper-v1:2607.20501 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20501 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20507 | arXiv:2607.20507v1 | paper-v1:2607.20507 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20507 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20512 | arXiv:2607.20512v1 | paper-v1:2607.20512 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20512 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20518 | arXiv:2607.20518v1 | paper-v1:2607.20518 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20518 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20524 | arXiv:2607.20524v1 | paper-v1:2607.20524 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20524 | self | — | new_in_window | MODEL-SELF-ATTENTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20526 | arXiv:2607.20526v1 | paper-v1:2607.20526 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20526 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20527 | arXiv:2607.20527v1 | paper-v1:2607.20527 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20527 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20531 | arXiv:2607.20531v1 | paper-v1:2607.20531 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20531 | self | — | new_in_window | AGENT-MCP | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20536 | arXiv:2607.20536v1 | paper-v1:2607.20536 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20536 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20538 | arXiv:2607.20538v1 | paper-v1:2607.20538 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20538 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20543 | arXiv:2607.20543v1 | paper-v1:2607.20543 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20543 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20548 | arXiv:2607.20548v1 | paper-v1:2607.20548 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20548 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20553 | arXiv:2607.20553v1 | paper-v1:2607.20553 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20553 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20558 | arXiv:2607.20558v1 | paper-v1:2607.20558 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20558 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20560 | arXiv:2607.20560v1 | paper-v1:2607.20560 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20560 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20594 | arXiv:2607.20594v1 | paper-v1:2607.20594 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20594 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20596 | arXiv:2607.20596v1 | paper-v1:2607.20596 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20596 | self | — | new_in_window | WORLDVIEW-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20652 | arXiv:2607.20652v1 | paper-v1:2607.20652 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20652 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20653 | arXiv:2607.20653v1 | paper-v1:2607.20653 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20653 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20668 | arXiv:2607.20668v1 | paper-v1:2607.20668 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20668 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20709 | arXiv:2607.20709v1 | paper-v1:2607.20709 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20709 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20712 | arXiv:2607.20712v1 | paper-v1:2607.20712 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20712 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20723 | arXiv:2607.20723v1 | paper-v1:2607.20723 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20723 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20729 | arXiv:2607.20729v1 | paper-v1:2607.20729 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20729 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20730 | arXiv:2607.20730v1 | paper-v1:2607.20730 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20730 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20734 | arXiv:2607.20734v1 | paper-v1:2607.20734 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20734 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20739 | arXiv:2607.20739v1 | paper-v1:2607.20739 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20739 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20757 | arXiv:2607.20757v1 | paper-v1:2607.20757 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20757 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20759 | arXiv:2607.20759v1 | paper-v1:2607.20759 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20759 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20764 | arXiv:2607.20764v1 | paper-v1:2607.20764 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20764 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20768 | arXiv:2607.20768v1 | paper-v1:2607.20768 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20768 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20771 | arXiv:2607.20771v1 | paper-v1:2607.20771 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20771 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20791 | arXiv:2607.20791v1 | paper-v1:2607.20791 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20791 | self | — | new_in_window | MODEL-SAMPLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20792 | arXiv:2607.20792v1 | paper-v1:2607.20792 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20792 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20827 | arXiv:2607.20827v1 | paper-v1:2607.20827 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20827 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20852 | arXiv:2607.20852v1 | paper-v1:2607.20852 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20852 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20860 | arXiv:2607.20860v1 | paper-v1:2607.20860 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20860 | self | — | new_in_window | PLATFORM-GATEWAY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20864 | arXiv:2607.20864v1 | paper-v1:2607.20864 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20864 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20887 | arXiv:2607.20887v1 | paper-v1:2607.20887 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20887 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20891 | arXiv:2607.20891v1 | paper-v1:2607.20891 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20891 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20908 | arXiv:2607.20908v1 | paper-v1:2607.20908 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20908 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20911 | arXiv:2607.20911v1 | paper-v1:2607.20911 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20911 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20918 | arXiv:2607.20918v1 | paper-v1:2607.20918 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20918 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20940 | arXiv:2607.20940v1 | paper-v1:2607.20940 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20940 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20950 | arXiv:2607.20950v1 | paper-v1:2607.20950 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20950 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20972 | arXiv:2607.20972v1 | paper-v1:2607.20972 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20972 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20982 | arXiv:2607.20982v1 | paper-v1:2607.20982 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20982 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-20999 | arXiv:2607.20999v1 | paper-v1:2607.20999 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20999 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21000 | arXiv:2607.21000v1 | paper-v1:2607.21000 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21000 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21005 | arXiv:2607.21005v1 | paper-v1:2607.21005 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21005 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21042 | arXiv:2607.21042v1 | paper-v1:2607.21042 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21042 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21051 | arXiv:2607.21051v1 | paper-v1:2607.21051 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21051 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21090 | arXiv:2607.21090v1 | paper-v1:2607.21090 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21090 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21106 | arXiv:2607.21106v1 | paper-v1:2607.21106 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21106 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21120 | arXiv:2607.21120v1 | paper-v1:2607.21120 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21120 | self | — | new_in_window | TRAIN-PPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21130 | arXiv:2607.21130v1 | paper-v1:2607.21130 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21130 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21143 | arXiv:2607.21143v1 | paper-v1:2607.21143 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21143 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21151 | arXiv:2607.21151v1 | paper-v1:2607.21151 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21151 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21162 | arXiv:2607.21162v1 | paper-v1:2607.21162 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21162 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21179 | arXiv:2607.21179v1 | paper-v1:2607.21179 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21179 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21217 | arXiv:2607.21217v1 | paper-v1:2607.21217 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21217 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21224 | arXiv:2607.21224v1 | paper-v1:2607.21224 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21224 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21273 | arXiv:2607.21273v1 | paper-v1:2607.21273 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21273 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21291 | arXiv:2607.21291v1 | paper-v1:2607.21291 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21291 | self | — | new_in_window | INFER-DECODE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21325 | arXiv:2607.21325v1 | paper-v1:2607.21325 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21325 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21351 | arXiv:2607.21351v1 | paper-v1:2607.21351 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21351 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21356 | arXiv:2607.21356v1 | paper-v1:2607.21356 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21356 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21372 | arXiv:2607.21372v1 | paper-v1:2607.21372 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21372 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21401 | arXiv:2607.21401v1 | paper-v1:2607.21401 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21401 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21404 | arXiv:2607.21404v1 | paper-v1:2607.21404 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21404 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21405 | arXiv:2607.21405v1 | paper-v1:2607.21405 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21405 | self | — | new_in_window | MODEL-POSITION-ENCODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21419 | arXiv:2607.21419v1 | paper-v1:2607.21419 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21419 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21433 | arXiv:2607.21433v1 | paper-v1:2607.21433 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21433 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21453 | arXiv:2607.21453v1 | paper-v1:2607.21453 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21453 | self | — | new_in_window | MODEL-SAMPLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21475 | arXiv:2607.21475v1 | paper-v1:2607.21475 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21475 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21480 | arXiv:2607.21480v1 | paper-v1:2607.21480 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21480 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21482 | arXiv:2607.21482v1 | paper-v1:2607.21482 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21482 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21503 | arXiv:2607.21503v1 | paper-v1:2607.21503 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21503 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21522 | arXiv:2607.21522v1 | paper-v1:2607.21522 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21522 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21530 | arXiv:2607.21530v1 | paper-v1:2607.21530 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21530 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21535 | arXiv:2607.21535v1 | paper-v1:2607.21535 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21535 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21550 | arXiv:2607.21550v1 | paper-v1:2607.21550 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21550 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21553 | arXiv:2607.21553v1 | paper-v1:2607.21553 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21553 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21557 | arXiv:2607.21557v1 | paper-v1:2607.21557 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21557 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21571 | arXiv:2607.21571v1 | paper-v1:2607.21571 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21571 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21576 | arXiv:2607.21576v1 | paper-v1:2607.21576 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21576 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21582 | arXiv:2607.21582v1 | paper-v1:2607.21582 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21582 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21585 | arXiv:2607.21585v1 | paper-v1:2607.21585 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21585 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21588 | arXiv:2607.21588v1 | paper-v1:2607.21588 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21588 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21591 | arXiv:2607.21591v1 | paper-v1:2607.21591 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21591 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21594 | arXiv:2607.21594v1 | paper-v1:2607.21594 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21594 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-20426 | RP-e7aac2dc90c63c83 | standard | arXiv:2607.20426v1 | SRC-ARXIV@arXiv:2607.20426v1 | https://arxiv.org/html/2607.20426v1#A2 — Appendix B Malicious System Prompt in RQ2; https://arxiv.org/html/2607.20426v1#S4 — 4 Method | https://arxiv.org/html/2607.20426v1#A5 — Appendix E Significance Test of Experimental Results; https://arxiv.org/html/2607.20426v1#A10 — Appendix J Dataset-level Analysis of “Knowledge Injection” in MoE models | https://arxiv.org/html/2607.20426v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.20426v1#S7 — 7 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20426 | complete |
| SF-2026-ARXIV-2607-20427 | RP-a2e663b7c53952c8 | standard | arXiv:2607.20427v1 | SRC-ARXIV@arXiv:2607.20427v1 | https://arxiv.org/html/2607.20427v1#A1 — Appendix A Model Architecture Details; https://arxiv.org/html/2607.20427v1#A2 — Appendix B Architecture-Specific Routing Patterns: Extended Discussion | https://arxiv.org/html/2607.20427v1#A4 — Appendix D Qwen3.5-35B-A3B Expert Functional Profile Analysis; https://arxiv.org/html/2607.20427v1#S3 — 3 Temporal Expert Combination Encoding: Information-Theoretic Analysis | https://arxiv.org/html/2607.20427v1#A11 — Appendix K Limitations; https://arxiv.org/html/2607.20427v1#A2 — Appendix B Architecture-Specific Routing Patterns: Extended Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20427 | complete |
| SF-2026-ARXIV-2607-20432 | RP-d9a2f8874294b38a | standard | arXiv:2607.20432v1 | SRC-ARXIV@arXiv:2607.20432v1 | https://arxiv.org/html/2607.20432v1#S3 — 3 Formal Framework | https://arxiv.org/html/2607.20432v1#S4 — 4 Case Study: Image Generation and Other Modalities | https://arxiv.org/html/2607.20432v1#S5 — 5 Implications and Future Directions; https://arxiv.org/html/2607.20432v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20432 | complete |
| SF-2026-ARXIV-2607-20433 | RP-6e42c600394e5c3c | standard | arXiv:2607.20433v1 | SRC-ARXIV@arXiv:2607.20433v1 | https://arxiv.org/html/2607.20433v1#A1 — Appendix A Extended Methodology; https://arxiv.org/html/2607.20433v1#A3.SS1 — C.1 Models, Editors, and Hyperparameters | https://arxiv.org/html/2607.20433v1#A3 — Appendix C Experimental Setup and Baselines; https://arxiv.org/html/2607.20433v1#A3.SS3 — C.3 Evaluation Metrics | https://arxiv.org/html/2607.20433v1#S7 — 7 Discussion | Exact v1 links https://github.com/togethercomputer/RedPajama-Data, https://github.com/opencv/opencv, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20433 | complete |
| SF-2026-ARXIV-2607-20434 | RP-d4a7af4cde330869 | deep | arXiv:2607.20434v1 | SRC-ARXIV@arXiv:2607.20434v1 | https://arxiv.org/html/2607.20434v1#S4 — 4 Diagonal Adhesive Method; https://arxiv.org/html/2607.20434v1#S5.SS3 — 5.3 Verification of the Diagonal Adhesive Method | https://arxiv.org/html/2607.20434v1#A7 — Appendix G Supplementary experimental results; https://arxiv.org/html/2607.20434v1#A7.SS1 — G.1 Experimental results of other models | https://arxiv.org/html/2607.20434v1#A1.SSx6 — Final Conclusion; https://arxiv.org/html/2607.20434v1#A8 — Appendix H Discussion on different compression orders | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20434 | complete |
| SF-2026-ARXIV-2607-20436 | RP-a23040404fadff25 | deep | arXiv:2607.20436v1 | SRC-ARXIV@arXiv:2607.20436v1 | https://arxiv.org/html/2607.20436v1#S2 — 2 Methodology; https://arxiv.org/html/2607.20436v1#S2.SS2 — 2.2 Localization Method | https://arxiv.org/html/2607.20436v1#A5 — Appendix E Per-item intervention agreement analysis; https://arxiv.org/html/2607.20436v1#S3 — 3 Results | https://arxiv.org/html/2607.20436v1#A7 — Appendix G E4 Adjacent-Window Depth Sweep and Typed-Failure Remediation; https://arxiv.org/html/2607.20436v1#S4 — 4 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20436 | complete |
| SF-2026-ARXIV-2607-20437 | RP-fdc1db1f1a0479ee | deep | arXiv:2607.20437v1 | SRC-ARXIV@arXiv:2607.20437v1 | https://arxiv.org/html/2607.20437v1#S4.SS1 — 4.1 Methods and Baselines; https://arxiv.org/html/2607.20437v1#A1 — Appendix A Threat Model Validation | https://arxiv.org/html/2607.20437v1#A1.SS1 — A.1 Experimental Setup; https://arxiv.org/html/2607.20437v1#A6 — Appendix F Evaluation on PoisonedRAG Attacks | https://arxiv.org/html/2607.20437v1#A1 — Appendix A Threat Model Validation; https://arxiv.org/html/2607.20437v1#S6 — 6 Conclusion | Exact v1 links https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard3/8B/MODEL_CARD.md, https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard2/MODEL_CARD.md, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20437 | complete |
| SF-2026-ARXIV-2607-20438 | RP-0f68c79df4ad11d9 | standard | arXiv:2607.20438v1 | SRC-ARXIV@arXiv:2607.20438v1 | https://arxiv.org/html/2607.20438v1#S4.SS2 — 4.2 Generality Across Models and Training Regimes | https://arxiv.org/html/2607.20438v1#A2.SS1 — B.1 Experimental Setup; https://arxiv.org/html/2607.20438v1#A3.SS4 — C.4 Evaluation and Scoring | https://arxiv.org/html/2607.20438v1#S7 — 7 Discussion and Limitations; https://arxiv.org/html/2607.20438v1#S7.SS2 — 7.2 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20438 | complete |
| SF-2026-ARXIV-2607-20457 | RP-a38e86ce689d5ac4 | deep | arXiv:2607.20457v1 | SRC-ARXIV@arXiv:2607.20457v1 | https://arxiv.org/html/2607.20457v1#S3 — 3 Methodology | https://arxiv.org/html/2607.20457v1#S4 — 4 Experiments; https://arxiv.org/html/2607.20457v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.20457v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20457 | complete |
| SF-2026-ARXIV-2607-20464 | RP-f17191ad5ab64f24 | deep | arXiv:2607.20464v1 | SRC-ARXIV@arXiv:2607.20464v1 | https://arxiv.org/html/2607.20464v1#A3.SS1 — C.1 Method; https://arxiv.org/html/2607.20464v1#S2 — 2 Method | https://arxiv.org/html/2607.20464v1#A2.SS1 — B.1 Parallel Analysis; https://arxiv.org/html/2607.20464v1#A2.SS3 — B.3 Shannon Effective Rank: Definition and Extended Analysis | https://arxiv.org/html/2607.20464v1#S5 — 5 Limitations and Future Work; https://arxiv.org/html/2607.20464v1#S4 — 4 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20464 | complete |
| SF-2026-ARXIV-2607-20465 | RP-7d7f79dcab108876 | deep | arXiv:2607.20465v1 | SRC-ARXIV@arXiv:2607.20465v1 | https://arxiv.org/html/2607.20465v1#S3 — 3 Benchmark Design; https://arxiv.org/html/2607.20465v1#S4 — 4 Methods | https://arxiv.org/html/2607.20465v1#S3.SS5 — 3.5 Downstream Evaluation Benchmarks; https://arxiv.org/html/2607.20465v1#S5.SS3 — 5.3 Results of Data Quality Evaluation | https://arxiv.org/html/2607.20465v1#S6 — 6 Conclusion | Exact v1 links https://github.com/haolpku/Data-Preparation-Bench, https://huggingface.co/datasets/lhpku20010120/Data-Prep-Bench, https://huggingface.co/HuggingFaceFW/fineweb-edu-classifier; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20465 | complete |
| SF-2026-ARXIV-2607-20466 | RP-cc44a43c92255186 | standard | arXiv:2607.20466v1 | SRC-ARXIV@arXiv:2607.20466v1 | https://arxiv.org/html/2607.20466v1#S2 — 2 Methodology; https://arxiv.org/html/2607.20466v1#S2.SS1 — 2.1 Design Principles | https://arxiv.org/html/2607.20466v1#A1 — Appendix A Per-Benchmark Results; https://arxiv.org/html/2607.20466v1#S3 — 3 Results | https://arxiv.org/html/2607.20466v1#S4 — 4 Discussion and Future Work; https://arxiv.org/html/2607.20466v1#S5 — 5 Conclusion | Exact v1 links https://github.com/AI-Hypercomputer/accelerator-agents/tree/main/JAXBench, https://github.com/AI-Hypercomputer/maxtext, https://github.com/openxla/tokamax; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20466 | complete |
| SF-2026-ARXIV-2607-20467 | RP-c9f6d1c757e3ecfd | standard | arXiv:2607.20467v1 | SRC-ARXIV@arXiv:2607.20467v1 | https://arxiv.org/html/2607.20467v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20467v1#A1 — Appendix A Algorithm of DC-Leap | https://arxiv.org/html/2607.20467v1#A6 — Appendix F More Results and Analysis; https://arxiv.org/html/2607.20467v1#A6.SS1 — F.1 More Results of Ablations | https://arxiv.org/html/2607.20467v1#A5.SS4 — E.4 Observations and Discussions; https://arxiv.org/html/2607.20467v1#S5 — 5 Conclusion | Exact v1 links https://github.com/ffh-wyls/DC-Leap, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20467 | complete |
| SF-2026-ARXIV-2607-20468 | RP-9ce22d1881e93d5c | standard | arXiv:2607.20468v1 | SRC-ARXIV@arXiv:2607.20468v1 | https://arxiv.org/html/2607.20468v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20468v1#S2 — 2 Related Works | https://arxiv.org/html/2607.20468v1#A1 — Appendix A Full Benchmark Specification and Environment; https://arxiv.org/html/2607.20468v1#A4 — Appendix D Full Results and Cost | https://arxiv.org/html/2607.20468v1#S6 — 6 Discussion and Conclusion; https://arxiv.org/html/2607.20468v1#A5 — Appendix E Behavioral Metrics and Failure Modes | Exact v1 links https://github.com/aisa-group/InferenceBench, https://opencode.ai/, https://code.claude.com/docs; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20468 | complete |
| SF-2026-ARXIV-2607-20473 | RP-56f237918cf04f94 | standard | arXiv:2607.20473v1 | SRC-ARXIV@arXiv:2607.20473v1 | https://arxiv.org/html/2607.20473v1#A2.SS2 — B.2 Target Models and Chat Template; https://arxiv.org/html/2607.20473v1#A2.SS6 — B.6 Base Model Behavior Under Complete Prompts | https://arxiv.org/html/2607.20473v1#A2 — Appendix B IPJ Attack Results; https://arxiv.org/html/2607.20473v1#A2.SS1 — B.1 Evaluation Prompt | https://arxiv.org/html/2607.20473v1#S6 — 6 Discussion; https://arxiv.org/html/2607.20473v1#S7 — 7 Conclusion | Exact v1 links https://huggingface.co/datasets/leo-bjpark/incomplete-prompt-jailbreak, https://github.com/yeonjea/incomplete-prompt-jailbreaks, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20473 | complete |
| SF-2026-ARXIV-2607-20475 | RP-aa081459a6760f96 | deep | arXiv:2607.20475v1 | SRC-ARXIV@arXiv:2607.20475v1 | https://arxiv.org/html/2607.20475v1#A5 — Appendix E Supplementary Algorithms; https://arxiv.org/html/2607.20475v1#A6 — Appendix F Baseline Implementation Details | https://arxiv.org/html/2607.20475v1#A7 — Appendix G Additional Top- Results; https://arxiv.org/html/2607.20475v1#A8 — Appendix H Additional Accuracy Results | https://arxiv.org/html/2607.20475v1#S5 — 5 Conclusion and Future Directions | Exact v1 links https://github.com/modular/modular, https://github.com/NVIDIA/TensorRT-LLM, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20475 | complete |
| SF-2026-ARXIV-2607-20478 | RP-7f654c5e5cfa91e7 | standard | arXiv:2607.20478v1 | SRC-ARXIV@arXiv:2607.20478v1 | https://arxiv.org/html/2607.20478v1#A4 — Appendix D Statistical Methods; https://arxiv.org/html/2607.20478v1#S3 — 3 Benchmark and Methodology | https://arxiv.org/html/2607.20478v1#S2.SS1 — 2.1 IaC Benchmarks and Evaluation; https://arxiv.org/html/2607.20478v1#S2.SS5 — 2.5 Agentic Evaluation and Observability | https://arxiv.org/html/2607.20478v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.20478v1#S4.SS2 — 4.2 RQ1: Active Retrieval Reduces Schema Failures | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20478 | complete |
| SF-2026-ARXIV-2607-20481 | RP-716327188acd0391 | deep | arXiv:2607.20481v1 | SRC-ARXIV@arXiv:2607.20481v1 | https://arxiv.org/html/2607.20481v1#A4 — Appendix D Prompt Design for Evaluation Signals | https://arxiv.org/html/2607.20481v1#S4.SS1 — 4.1 Experimental Results; https://arxiv.org/html/2607.20481v1#A3 — Appendix C Additional Experiments | https://arxiv.org/html/2607.20481v1#S5 — 5 Conclusion, Future Work, and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20481 | complete |
| SF-2026-ARXIV-2607-20483 | RP-859e1d0f9785df3e | standard | arXiv:2607.20483v1 | SRC-ARXIV@arXiv:2607.20483v1 | https://arxiv.org/html/2607.20483v1#A1 — Appendix A Dynamic Programming Algorithms; https://arxiv.org/html/2607.20483v1#A1.SS1 — A.1 Algorithm 1 | https://arxiv.org/html/2607.20483v1#S6 — 6 Experiments | https://arxiv.org/html/2607.20483v1#S8 — 8 Future areas of research; https://arxiv.org/html/2607.20483v1#S8.SS2 — 8.2 Other future areas of research | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20483 | complete |
| SF-2026-ARXIV-2607-20488 | RP-6bbe3ee75a85d365 | standard | arXiv:2607.20488v1 | SRC-ARXIV@arXiv:2607.20488v1 | https://arxiv.org/html/2607.20488v1#S3 — 3. ATM System Architecture; https://arxiv.org/html/2607.20488v1#S4 — 4. Algorithms | https://arxiv.org/html/2607.20488v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.20488v1#S6.SS2 — 6.2. Main Results: Success and Exposure (Q1, Q2) | https://arxiv.org/html/2607.20488v1#S5.SS2 — 5.2. Failure Modes and Bounded Damage; https://arxiv.org/html/2607.20488v1#S7 — 7. Conclusion | Exact v1 links https://github.com/sidikbro/jiuwen_atm, https://github.com/crewAIInc/crewAI, https://github.com/openJiuwen-ai/jiuwenswarm; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20488 | complete |
| SF-2026-ARXIV-2607-20490 | RP-76b7d17bc6048224 | deep | arXiv:2607.20490v1 | SRC-ARXIV@arXiv:2607.20490v1 | https://arxiv.org/html/2607.20490v1#S4.SS1 — 4.1 Architecture; https://arxiv.org/html/2607.20490v1#S7.SS3 — 7.3 Experimental design | https://arxiv.org/html/2607.20490v1#S7 — 7 Evaluation; https://arxiv.org/html/2607.20490v1#S7.SS1 — 7.1 Evaluation metrics | https://arxiv.org/html/2607.20490v1#S7.SS6 — 7.6 Discussion; https://arxiv.org/html/2607.20490v1#S8 — 8 Conclusion | Exact v1 links https://github.com/kubernetes-sigs/kubebuilder, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20490 | complete |
| SF-2026-ARXIV-2607-20495 | RP-66a7ba73154a2522 | standard | arXiv:2607.20495v1 | SRC-ARXIV@arXiv:2607.20495v1 | https://arxiv.org/html/2607.20495v1#S2.SS3 — II-C Multi-Agent System Orchestration and Optimization; https://arxiv.org/html/2607.20495v1#S3 — III Design | https://arxiv.org/html/2607.20495v1#S4 — IV Evaluation; https://arxiv.org/html/2607.20495v1#S4.SS1 — IV-A Experimental Setup | https://arxiv.org/html/2607.20495v1#S5 — V Limitations and Future Work; https://arxiv.org/html/2607.20495v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20495 | complete |
| SF-2026-ARXIV-2607-20501 | RP-7ee10a93ff8c2471 | standard | arXiv:2607.20501v1 | SRC-ARXIV@arXiv:2607.20501v1 | https://arxiv.org/html/2607.20501v1#S3 — 3 Methodology | https://arxiv.org/html/2607.20501v1#A1 — Appendix A Additional Experiment Details; https://arxiv.org/html/2607.20501v1#A3 — Appendix C Example Second Seed Results | https://arxiv.org/html/2607.20501v1#S5 — 5 Conclusion | Exact v1 links https://github.com/amazon-science/ModularKernelEvolution, https://huggingface.co/facebook/KernelLLM, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20501 | complete |
| SF-2026-ARXIV-2607-20507 | RP-429dd11232b96689 | deep | arXiv:2607.20507v1 | SRC-ARXIV@arXiv:2607.20507v1 | https://arxiv.org/html/2607.20507v1#S3 — 3 Method | https://arxiv.org/html/2607.20507v1#A1.SS7 — A.7 Detailed Main Result Analysis; https://arxiv.org/html/2607.20507v1#A1 — Appendix A Additional Experimental Details | https://arxiv.org/html/2607.20507v1#A1.SS2 — A.2 Cache Generation and Failure Handling Details; https://arxiv.org/html/2607.20507v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20507 | complete |
| SF-2026-ARXIV-2607-20512 | RP-365bfcae3727f855 | standard | arXiv:2607.20512v1 | SRC-ARXIV@arXiv:2607.20512v1 | https://arxiv.org/html/2607.20512v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20512v1#S1.SS0.SSS0.Px1 — Contributions. | https://arxiv.org/html/2607.20512v1#S3 — 3 Ablation: Which Ingredient? | https://arxiv.org/html/2607.20512v1#S6 — 6 Limitations and Conclusion | Exact v1 links https://github.com/louiswang524/muon-grokking-frontier, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20512 | complete |
| SF-2026-ARXIV-2607-20518 | RP-dfcc4e999404636d | standard | arXiv:2607.20518v1 | SRC-ARXIV@arXiv:2607.20518v1 | https://arxiv.org/html/2607.20518v1#S2.SS3 — 2.3 Test-Case Design Methodology; https://arxiv.org/html/2607.20518v1#S2.SS1 — 2.1 Design Principles | https://arxiv.org/html/2607.20518v1#S1.SS1 — 1.1 Why an Ascend-Oriented Benchmark Now; https://arxiv.org/html/2607.20518v1#S1.SS2 — 1.2 Six Criteria for an Ascend-Oriented Benchmark | https://arxiv.org/html/2607.20518v1#S4 — 4 Conclusion | Exact v1 links https://gitcode.com/cann/cann-bench, https://gitcode.com/cann/opbase, https://github.com/ScalingIntelligence/KernelBench/issues/74; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20518 | complete |
| SF-2026-ARXIV-2607-20524 | RP-3ef47f987f712eb0 | standard | arXiv:2607.20524v1 | SRC-ARXIV@arXiv:2607.20524v1 | https://arxiv.org/html/2607.20524v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20524v1#S5.SS1 — 5.1 The Architecture-Dependent Relay Chain | https://arxiv.org/html/2607.20524v1#A1 — Appendix A Full Experiment 1 Degradation Tables; https://arxiv.org/html/2607.20524v1#S3.SS4 — 3.4 Experiment 1: Baseline Attention Degradation | https://arxiv.org/html/2607.20524v1#S5 — 5 Discussion; https://arxiv.org/html/2607.20524v1#S6 — 6 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20524 | complete |
| SF-2026-ARXIV-2607-20526 | RP-554f2ef23a7b81b6 | standard | arXiv:2607.20526v1 | SRC-ARXIV@arXiv:2607.20526v1 | https://arxiv.org/html/2607.20526v1#S3 — 3 Benchmark Design and Methodology | https://arxiv.org/html/2607.20526v1#A1 — Appendix A Full Results and Run-to-Run Stability; https://arxiv.org/html/2607.20526v1#S3 — 3 Benchmark Design and Methodology | https://arxiv.org/html/2607.20526v1#S6 — 6 Discussion and Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20526 | complete |
| SF-2026-ARXIV-2607-20527 | RP-63d4abeb0e709154 | deep | arXiv:2607.20527v1 | SRC-ARXIV@arXiv:2607.20527v1 | https://arxiv.org/html/2607.20527v1#S2.SS2 — 2.2. Evaluating and benchmarking agentic systems; https://arxiv.org/html/2607.20527v1#S4 — 4. Method | https://arxiv.org/html/2607.20527v1#A3 — Appendix S3 Conformal calibration-size ablation; https://arxiv.org/html/2607.20527v1#S2.SS2 — 2.2. Evaluating and benchmarking agentic systems | https://arxiv.org/html/2607.20527v1#S6 — 6. Discussion; https://arxiv.org/html/2607.20527v1#S7 — 7. Limitations | Exact v1 links https://github.com/GooTec/citation-guard, https://dx.doi.org/10.18653/v1/2024.eacl-demo.16, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20527 | complete |
| SF-2026-ARXIV-2607-20531 | RP-ca7d278e552ef4ec | standard | arXiv:2607.20531v1 | SRC-ARXIV@arXiv:2607.20531v1 | https://arxiv.org/html/2607.20531v1#A4 — Appendix D Framework Configuration; https://arxiv.org/html/2607.20531v1#S3.SS1 — 3.1 Design principles | https://arxiv.org/html/2607.20531v1#S4 — 4 Results & Analysis; https://arxiv.org/html/2607.20531v1#A11 — Appendix K Failure Analysis | https://arxiv.org/html/2607.20531v1#A11 — Appendix K Failure Analysis; https://arxiv.org/html/2607.20531v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/blog/smollm3, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20531 | complete |
| SF-2026-ARXIV-2607-20536 | RP-75ab2e894ad3546c | standard | arXiv:2607.20536v1 | SRC-ARXIV@arXiv:2607.20536v1 | https://arxiv.org/html/2607.20536v1#A2 — Appendix B Interaction Metric Design; https://arxiv.org/html/2607.20536v1#S4.SS2 — 4.2 Simulated User Design | https://arxiv.org/html/2607.20536v1#A1 — Appendix A Experiment Results; https://arxiv.org/html/2607.20536v1#A3 — Appendix C Benchmark Task Examples | https://arxiv.org/html/2607.20536v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20536 | complete |
| SF-2026-ARXIV-2607-20538 | RP-a8c492b514d62744 | standard | arXiv:2607.20538v1 | SRC-ARXIV@arXiv:2607.20538v1 | https://arxiv.org/html/2607.20538v1#Sx4 — Method and Evaluation Design; https://arxiv.org/html/2607.20538v1#Sx4.SSx4 — Evaluation Design | https://arxiv.org/html/2607.20538v1#Sx4 — Method and Evaluation Design; https://arxiv.org/html/2607.20538v1#Sx4.SSx4 — Evaluation Design | https://arxiv.org/html/2607.20538v1#Sx6 — Discussion and Limitations; https://arxiv.org/html/2607.20538v1#Sx7 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20538 | complete |
| SF-2026-ARXIV-2607-20543 | RP-174b8e4552e10b79 | deep | arXiv:2607.20543v1 | SRC-ARXIV@arXiv:2607.20543v1 | https://arxiv.org/html/2607.20543v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20543v1#S2 — 2 Related Work | https://arxiv.org/html/2607.20543v1#S7 — 7 Experiments | https://arxiv.org/html/2607.20543v1#S4 — 4 Pass@ Inversion Is a Boundary-Regime Failure; https://arxiv.org/html/2607.20543v1#S8 — 8 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20543 | complete |
| SF-2026-ARXIV-2607-20548 | RP-9961344ec49e68ae | deep | arXiv:2607.20548v1 | SRC-ARXIV@arXiv:2607.20548v1 | https://arxiv.org/html/2607.20548v1#S4.SS2 — 4.2 Systems to enable higher-order optimizers; https://arxiv.org/html/2607.20548v1#S3.SS1 — 3.1 Batch Size Scaling for Mixture-of-Experts Models | https://arxiv.org/html/2607.20548v1#S5 — 5 Pretraining Experiments with Muon and SOAP | https://arxiv.org/html/2607.20548v1#S7 — 7 Conclusions and Future Work | Exact v1 links https://github.com/nikhilvyas/SOAP, https://github.com/KellerJordan/cifar10-airbench/tree/master, https://github.com/NVIDIA/Megatron-LM/blob/main/megatron/core/optimizer/layer_wise_optimizer.py; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20548 | complete |
| SF-2026-ARXIV-2607-20553 | RP-41cf168f31141925 | deep | arXiv:2607.20553v1 | SRC-ARXIV@arXiv:2607.20553v1 | https://arxiv.org/html/2607.20553v1#A7.SS5 — G.5 Action Space Design Rationale; https://arxiv.org/html/2607.20553v1#S3 — 3 Method | https://arxiv.org/html/2607.20553v1#S4.SS2 — 4.2 Results and Analysis; https://arxiv.org/html/2607.20553v1#S4.SS3 — 4.3 Ablation Experiments | https://arxiv.org/html/2607.20553v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.20553v1#Sx1 — Limitations | Exact v1 links https://github.com/Wyb0627/CMIMem, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20553 | complete |
| SF-2026-ARXIV-2607-20558 | RP-be34da20e09a79ed | standard | arXiv:2607.20558v1 | SRC-ARXIV@arXiv:2607.20558v1 | https://arxiv.org/html/2607.20558v1#S2.SS1 — 2.1 Frontier Evaluation Methods; https://arxiv.org/html/2607.20558v1#S3 — 3 Methodology | https://arxiv.org/html/2607.20558v1#A1 — Appendix A Benchmarks.; https://arxiv.org/html/2607.20558v1#A5 — Appendix E Supplemental Results | https://arxiv.org/html/2607.20558v1#S5 — 5 Conclusion | Exact v1 links https://github.com/ekmpa/StabilityBench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20558 | complete |
| SF-2026-ARXIV-2607-20560 | RP-160a2adf53536493 | deep | arXiv:2607.20560v1 | SRC-ARXIV@arXiv:2607.20560v1 | https://arxiv.org/html/2607.20560v1#S3 — III The Chronofy Framework | https://arxiv.org/html/2607.20560v1#S4 — IV Experimental Evaluation; https://arxiv.org/html/2607.20560v1#S4.SS4 — IV-D Experiment 4: Clinical Sensitivity Analysis | https://arxiv.org/html/2607.20560v1#S5 — V Discussion; https://arxiv.org/html/2607.20560v1#S5.SS2 — V-B Limitations | Exact v1 links https://pypi.org/project/chronofy/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20560 | complete |
| SF-2026-ARXIV-2607-20594 | RP-6b9898fb9f64d715 | standard | arXiv:2607.20594v1 | SRC-ARXIV@arXiv:2607.20594v1 | https://arxiv.org/html/2607.20594v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20594v1#S2 — 2 Related work | https://arxiv.org/html/2607.20594v1#A4 — Appendix D Training and experiment details; https://arxiv.org/html/2607.20594v1#S9 — 9 Open-benchmark validation | https://arxiv.org/html/2607.20594v1#S10 — 10 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20594 | complete |
| SF-2026-ARXIV-2607-20596 | RP-0d809f9f8b3b10d4 | standard | arXiv:2607.20596v1 | SRC-ARXIV@arXiv:2607.20596v1 | https://arxiv.org/html/2607.20596v1#A1.SS5 — A.5 Multi-Architecture Comparison; https://arxiv.org/html/2607.20596v1#S3 — 3 Methods | https://arxiv.org/html/2607.20596v1#A2.SS6 — B.6 Full-Layer Causal Ablation Results; https://arxiv.org/html/2607.20596v1#A1.SS2 — A.2 Expansion Factor Analysis | https://arxiv.org/html/2607.20596v1#S5 — 5 Discussion; https://arxiv.org/html/2607.20596v1#S6 — 6 Conclusion | Exact v1 links https://github.com/jbloomAus/SAELens, https://transformer-circuits.pub/2024/crosscoders/index.html, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20596 | complete |
| SF-2026-ARXIV-2607-20652 | RP-4bafca3252ae659d | standard | arXiv:2607.20652v1 | SRC-ARXIV@arXiv:2607.20652v1 | https://arxiv.org/html/2607.20652v1#A1.SS4 — A.4 Concrete implementation; https://arxiv.org/html/2607.20652v1#A3.SS3 — C.3 Greedy Feature Editing Algorithm | https://arxiv.org/html/2607.20652v1#A2.SS1 — B.1 Poisoned-Document Retrieval Experiment Details; https://arxiv.org/html/2607.20652v1#A2.SS5 — B.5 Additional Poisoned-Document Retrieval Results | https://arxiv.org/html/2607.20652v1#S4 — 4 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20652 | complete |
| SF-2026-ARXIV-2607-20653 | RP-280e2ed3b564bf79 | deep | arXiv:2607.20653v1 | SRC-ARXIV@arXiv:2607.20653v1 | https://arxiv.org/html/2607.20653v1#A2 — Appendix B MfM Architecture and Hyperparameters; https://arxiv.org/html/2607.20653v1#A3 — Appendix C RfD Architecture and Hyperparameters | https://arxiv.org/html/2607.20653v1#S5 — 5 Experiments; https://arxiv.org/html/2607.20653v1#S5.SS1 — 5.1 Experimental Setup | https://arxiv.org/html/2607.20653v1#S5.SS2 — 5.2 Future Prediction; https://arxiv.org/html/2607.20653v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20653 | complete |
| SF-2026-ARXIV-2607-20668 | RP-72a984687a2f4089 | deep | arXiv:2607.20668v1 | SRC-ARXIV@arXiv:2607.20668v1 | https://arxiv.org/html/2607.20668v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20668v1#S2 — 2 Related Work | https://arxiv.org/html/2607.20668v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.20668v1#S5 — 5 Results | https://arxiv.org/html/2607.20668v1#S6 — 6 Discussion; https://arxiv.org/html/2607.20668v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20668 | complete |
| SF-2026-ARXIV-2607-20709 | RP-2f94c9ed40abf65b | standard | arXiv:2607.20709v1 | SRC-ARXIV@arXiv:2607.20709v1 | https://arxiv.org/html/2607.20709v1#A1.SS3 — A.3 Microsoft Agent Framework; https://arxiv.org/html/2607.20709v1#A3 — Appendix C Appendix: Memory-System Details | https://arxiv.org/html/2607.20709v1#S4.SSx1 — Experimental Results on Agentic Benchmarks; https://arxiv.org/html/2607.20709v1#S4 — 4 Evaluation | https://arxiv.org/html/2607.20709v1#A4.SS3 — D.3 World-model usage evidence and failure modes; https://arxiv.org/html/2607.20709v1#S7 — 7 Conclusion | Exact v1 links https://github.com/NVIDIA-NeMo/labs-OO-Agents, https://github.com/letta-ai/letta, https://github.com/anomalyco/opencode; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20709 | complete |
| SF-2026-ARXIV-2607-20712 | RP-72c24903d1fed65b | standard | arXiv:2607.20712v1 | SRC-ARXIV@arXiv:2607.20712v1 | https://arxiv.org/html/2607.20712v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20712v1#S2 — 2 Background | https://arxiv.org/html/2607.20712v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20712v1#S2 — 2 Background | https://arxiv.org/html/2607.20712v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20712v1#S2 — 2 Background | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20712 | complete |
| SF-2026-ARXIV-2607-20723 | RP-9ae8cb4c5ad46c4a | deep | arXiv:2607.20723v1 | SRC-ARXIV@arXiv:2607.20723v1 | https://arxiv.org/html/2607.20723v1#A2 — Appendix B Additional Details on Leaking Model Architecture Attack; https://arxiv.org/html/2607.20723v1#S2.SS1 — 2.1. Transformer Architecture | https://arxiv.org/html/2607.20723v1#A1.SS2 — A.2. Remote Black-Box Model Results; https://arxiv.org/html/2607.20723v1#S4.SS4 — 4.4. Experimental Setup | https://arxiv.org/html/2607.20723v1#S3 — 3. Threat Model; https://arxiv.org/html/2607.20723v1#S8 — 8. Conclusion | Exact v1 links https://github.com/feifeibear/LLMSpeculativeSampling, https://huggingface.co/timdettmers/guanaco-13b, https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20723 | complete |
| SF-2026-ARXIV-2607-20729 | RP-aa9520bb5604e764 | standard | arXiv:2607.20729v1 | SRC-ARXIV@arXiv:2607.20729v1 | https://arxiv.org/html/2607.20729v1#S8.SS4 — 8.4 AI-System Identity and Governance | https://arxiv.org/html/2607.20729v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20729v1#S1.SS1 — 1.1 Two Answers to One Question | https://arxiv.org/html/2607.20729v1#S10 — 10 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20729 | complete |
| SF-2026-ARXIV-2607-20730 | RP-4b7bccd3fa5eac9e | deep | arXiv:2607.20730v1 | SRC-ARXIV@arXiv:2607.20730v1 | https://arxiv.org/html/2607.20730v1#S4 — IV Evaluation Framework | https://arxiv.org/html/2607.20730v1#S5.SS2 — V-B Results and Analysis; https://arxiv.org/html/2607.20730v1#S3 — III GPE Benchmark | https://arxiv.org/html/2607.20730v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20730 | complete |
| SF-2026-ARXIV-2607-20734 | RP-1722d4e78c893d66 | deep | arXiv:2607.20734v1 | SRC-ARXIV@arXiv:2607.20734v1 | https://arxiv.org/html/2607.20734v1#A2.SS1 — B.1 Model Details; https://arxiv.org/html/2607.20734v1#A6.SS3 — F.3 Effect of Model Capacity | https://arxiv.org/html/2607.20734v1#A6 — Appendix F Additional Experiments and Analysis; https://arxiv.org/html/2607.20734v1#A2 — Appendix B Experimental Setup Details | https://arxiv.org/html/2607.20734v1#Sx1 — Limitations and Future Directions; https://arxiv.org/html/2607.20734v1#S5.SS3 — 5.3 Additional Analysis and Discussion | Exact v1 links https://github.com/microsoft/evolving-intent/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20734 | complete |
| SF-2026-ARXIV-2607-20739 | RP-1e619782f543c0a3 | standard | arXiv:2607.20739v1 | SRC-ARXIV@arXiv:2607.20739v1 | https://arxiv.org/html/2607.20739v1#S6.SS1 — VI-A Implementation | https://arxiv.org/html/2607.20739v1#S4.SS2 — IV-B Convergence Analysis; https://arxiv.org/html/2607.20739v1#S5.SS3 — V-C Convergence Analysis | https://arxiv.org/html/2607.20739v1#S7 — VII Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20739 | complete |
| SF-2026-ARXIV-2607-20757 | RP-d6abd96590220ff2 | deep | arXiv:2607.20757v1 | SRC-ARXIV@arXiv:2607.20757v1 | https://arxiv.org/html/2607.20757v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20757v1#S2 — 2 Background and related Work | https://arxiv.org/html/2607.20757v1#S5.SS1 — 5.1 Results | https://arxiv.org/html/2607.20757v1#S6 — 6 Discussion and Broader Implications; https://arxiv.org/html/2607.20757v1#S7 — 7 Limitations | Exact v1 links https://github.com/MPedraBento/gauge-quant, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20757 | complete |
| SF-2026-ARXIV-2607-20759 | RP-671431cda4d591ae | standard | arXiv:2607.20759v1 | SRC-ARXIV@arXiv:2607.20759v1 | https://arxiv.org/html/2607.20759v1#S3 — III Methodology; https://arxiv.org/html/2607.20759v1#S3.SS1 — III-A Threat Model | https://arxiv.org/html/2607.20759v1#S5 — V Evaluation Results; https://arxiv.org/html/2607.20759v1#S4 — IV Evaluation Setup | https://arxiv.org/html/2607.20759v1#S7 — VII Conclusion and Future Work; https://arxiv.org/html/2607.20759v1#S3.SS1 — III-A Threat Model | Exact v1 links https://code.claude.com/docs/en/overview, https://developers.openai.com/codex/concepts/sandboxing, https://openai.com/index/gpt-5-3-codex-system-card/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20759 | complete |
| SF-2026-ARXIV-2607-20764 | RP-f205429461f7cbfc | standard | arXiv:2607.20764v1 | SRC-ARXIV@arXiv:2607.20764v1 | https://arxiv.org/html/2607.20764v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20764v1#S3.SS5 — 3.5 Models and Inference Settings | https://arxiv.org/html/2607.20764v1#A1 — Appendix A Experimental Setup Details; https://arxiv.org/html/2607.20764v1#S2 — 2 The ArbiGraph Benchmark Generator | https://arxiv.org/html/2607.20764v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.20764v1#S7 — 7 Conclusion | Exact v1 links https://github.com/pavelgolikov/ArbiGraph.git, https://huggingface.co/Qwen/Qwen3.5-27B, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20764 | complete |
| SF-2026-ARXIV-2607-20768 | RP-397d939d619c253b | standard | arXiv:2607.20768v1 | SRC-ARXIV@arXiv:2607.20768v1 | https://arxiv.org/html/2607.20768v1#A1 — Appendix A Model roster and parsing audit; https://arxiv.org/html/2607.20768v1#A1.SS1 — A.1 Model roster and full-sample filtering statistics | https://arxiv.org/html/2607.20768v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.20768v1#S5 — 5 Results | https://arxiv.org/html/2607.20768v1#S5.SS4 — 5.4 A residual pairwise co-failure association remains; https://arxiv.org/html/2607.20768v1#S6 — 6 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20768 | complete |
| SF-2026-ARXIV-2607-20771 | RP-c158e527226d2432 | standard | arXiv:2607.20771v1 | SRC-ARXIV@arXiv:2607.20771v1 | https://arxiv.org/html/2607.20771v1#S2 — 2 Approach | https://arxiv.org/html/2607.20771v1#S3 — 3 Experimental Results; https://arxiv.org/html/2607.20771v1#S3.SS1 — 3.1 Qualitative Analysis of Expert Skills | https://arxiv.org/html/2607.20771v1#S4 — 4 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20771 | complete |
| SF-2026-ARXIV-2607-20791 | RP-2e4c84a977099c22 | standard | arXiv:2607.20791v1 | SRC-ARXIV@arXiv:2607.20791v1 | https://arxiv.org/html/2607.20791v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20791v1#S2 — 2 Related Work | https://arxiv.org/html/2607.20791v1#A2 — Appendix B Ablation: Impact of the Refusal Prefix Compatibility Gate; https://arxiv.org/html/2607.20791v1#A3 — Appendix C Ablation: Soft Compatibility Gate | https://arxiv.org/html/2607.20791v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/meta-llama/Llama-Guard-4-12B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20791 | complete |
| SF-2026-ARXIV-2607-20792 | RP-0f329ee86bb91f8b | deep | arXiv:2607.20792v1 | SRC-ARXIV@arXiv:2607.20792v1 | https://arxiv.org/html/2607.20792v1#S3 — 3 Method; https://arxiv.org/html/2607.20792v1#S4 — 4 Implementation | https://arxiv.org/html/2607.20792v1#S5 — 5 Experimental Evaluation | https://arxiv.org/html/2607.20792v1#S3.SS3 — 3.3 Future-latent and energy objectives; https://arxiv.org/html/2607.20792v1#S6 — 6 Limitations | Exact v1 links https://github.com/RightNow-AI/Memoir, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20792 | complete |
| SF-2026-ARXIV-2607-20827 | RP-5967791f153c8c81 | standard | arXiv:2607.20827v1 | SRC-ARXIV@arXiv:2607.20827v1 | https://arxiv.org/html/2607.20827v1#Sx2 — Method; https://arxiv.org/html/2607.20827v1#A10.SSx1 — Experiment–Model Matrix | https://arxiv.org/html/2607.20827v1#A10.SSx1 — Experiment–Model Matrix; https://arxiv.org/html/2607.20827v1#A2 — Appendix B Additional Matched, Behavioral, and Anchor Results | https://arxiv.org/html/2607.20827v1#A1 — Appendix A Limitations and Scope; https://arxiv.org/html/2607.20827v1#Sx6 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20827 | complete |
| SF-2026-ARXIV-2607-20852 | RP-d43106b4a5b787ec | standard | arXiv:2607.20852v1 | SRC-ARXIV@arXiv:2607.20852v1 | https://arxiv.org/html/2607.20852v1#A2.SS6 — B.6 CodeWorkflow Construction Protocol and Oracle Design; https://arxiv.org/html/2607.20852v1#S2.SS2 — 2.2 Threat Model and Information Boundary | https://arxiv.org/html/2607.20852v1#A1.SS1 — A.1 Code Generation and Execution Benchmarks; https://arxiv.org/html/2607.20852v1#S2.SS3 — 2.3 Benchmark Construction | https://arxiv.org/html/2607.20852v1#A8 — Appendix H Sample-Mix and Failure Taxonomy; https://arxiv.org/html/2607.20852v1#A8.SS2 — H.2 Failure Taxonomy | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20852 | complete |
| SF-2026-ARXIV-2607-20860 | RP-5fe80e14cddf7f0e | deep | arXiv:2607.20860v1 | SRC-ARXIV@arXiv:2607.20860v1 | https://arxiv.org/html/2607.20860v1#S15 — S15 Extended Method Comparison; https://arxiv.org/html/2607.20860v1#S6.SS2 — 6.2 Commercial models via OpenRouter | https://arxiv.org/html/2607.20860v1#S6 — 6 Experiments | https://arxiv.org/html/2607.20860v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20860 | complete |
| SF-2026-ARXIV-2607-20864 | RP-e887ff653ff16c0f | standard | arXiv:2607.20864v1 | SRC-ARXIV@arXiv:2607.20864v1 | https://arxiv.org/html/2607.20864v1#S2 — 2 The permutation diagnostic — design; https://arxiv.org/html/2607.20864v1#S4.SS1 — 4.1 Sweep design | https://arxiv.org/html/2607.20864v1#S4 — 4 Results; https://arxiv.org/html/2607.20864v1#S5.SS1 — 5.1 Calibrating a benchmark to a model tier | https://arxiv.org/html/2607.20864v1#S6 — 6 Conclusion | Exact v1 links https://github.com/TambaClan/inspect_permute, https://github.com/UKGovernmentBEIS/inspect_ai, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20864 | complete |
| SF-2026-ARXIV-2607-20887 | RP-8e2dc0053aa0c797 | standard | arXiv:2607.20887v1 | SRC-ARXIV@arXiv:2607.20887v1 | https://arxiv.org/html/2607.20887v1#S3.SS5 — 3.5 Natural-data and architecture boundary; https://arxiv.org/html/2607.20887v1#A3 — Appendix C Full algorithm and diagnostics | https://arxiv.org/html/2607.20887v1#A5 — Appendix E Secondary experiments; https://arxiv.org/html/2607.20887v1#S2.SS1 — 2.1 Status of the mathematical results | https://arxiv.org/html/2607.20887v1#A4 — Appendix D Geometric discussion; https://arxiv.org/html/2607.20887v1#S4 — 4 Limitations and decisive next tests | Exact v1 links https://github.com/tinggong9/TwistedMerge, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20887 | complete |
| SF-2026-ARXIV-2607-20891 | RP-4c418356f5a778b4 | standard | arXiv:2607.20891v1 | SRC-ARXIV@arXiv:2607.20891v1 | https://arxiv.org/html/2607.20891v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20891v1#S4.SS5 — 4.5 How Do Framework and LLM Choices Shape FCAR? | https://arxiv.org/html/2607.20891v1#A5.SS5 — E.5 FCAR Evaluation; https://arxiv.org/html/2607.20891v1#S4 — 4 Experiments | https://arxiv.org/html/2607.20891v1#S3.SS2 — 3.2 Threat Model; https://arxiv.org/html/2607.20891v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20891 | complete |
| SF-2026-ARXIV-2607-20908 | RP-69be6ae4f2ce8331 | deep | arXiv:2607.20908v1 | SRC-ARXIV@arXiv:2607.20908v1 | https://arxiv.org/html/2607.20908v1#A1.SS13 — A.13 MLP Ranker Architecture; https://arxiv.org/html/2607.20908v1#S2 — 2 Methodology | https://arxiv.org/html/2607.20908v1#S3 — 3 Experimental Results; https://arxiv.org/html/2607.20908v1#A1.SS16 — A.16 Results | https://arxiv.org/html/2607.20908v1#S5 — 5 Limitations; https://arxiv.org/html/2607.20908v1#S6 — 6 Conclusion | Exact v1 links https://atcoder.jp/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20908 | complete |
| SF-2026-ARXIV-2607-20911 | RP-c8f03e551f11ff60 | standard | arXiv:2607.20911v1 | SRC-ARXIV@arXiv:2607.20911v1 | https://arxiv.org/html/2607.20911v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20911v1#S2 — 2 Task Construction | https://arxiv.org/html/2607.20911v1#S3 — 3 The Benchmark; https://arxiv.org/html/2607.20911v1#S4 — 4 Evaluation Harness and Scoring | https://arxiv.org/html/2607.20911v1#S7 — 7 Limitations and Conclusion | Exact v1 links https://github.com/laude-institute/harbor, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20911 | complete |
| SF-2026-ARXIV-2607-20918 | RP-c2fe1d2536512e95 | standard | arXiv:2607.20918v1 | SRC-ARXIV@arXiv:2607.20918v1 | https://arxiv.org/html/2607.20918v1#Sx1 — Introduction; https://arxiv.org/html/2607.20918v1#Sx2 — Related Work | https://arxiv.org/html/2607.20918v1#Sx4 — Experiments; https://arxiv.org/html/2607.20918v1#Sx4.SSx1 — Experimental Setup | https://arxiv.org/html/2607.20918v1#Sx5 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20918 | complete |
| SF-2026-ARXIV-2607-20940 | RP-8d31e6102b35527e | standard | arXiv:2607.20940v1 | SRC-ARXIV@arXiv:2607.20940v1 | https://arxiv.org/html/2607.20940v1#S4 — 4 Methodology; https://arxiv.org/html/2607.20940v1#S3.SS1 — 3.1 Preliminary: Autoregressive video diffusion models | https://arxiv.org/html/2607.20940v1#S5 — 5 Experiments; https://arxiv.org/html/2607.20940v1#S5.SS2 — 5.2 Qualitative Results | https://arxiv.org/html/2607.20940v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/gdhe17/Self-Forcing/blob/main/checkpoints/ode_init.pt, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20940 | complete |
| SF-2026-ARXIV-2607-20950 | RP-8517bb212ab4be64 | standard | arXiv:2607.20950v1 | SRC-ARXIV@arXiv:2607.20950v1 | https://arxiv.org/html/2607.20950v1#S5.SS1 — 5.1 Benchmark design; https://arxiv.org/html/2607.20950v1#A1.SS1 — A.1 Formal Partial-Verification Model | https://arxiv.org/html/2607.20950v1#S5.SS2 — 5.2 Benchmark results; https://arxiv.org/html/2607.20950v1#A2 — Appendix B Experimental Details and Additional Diagnostics | https://arxiv.org/html/2607.20950v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20950 | complete |
| SF-2026-ARXIV-2607-20972 | RP-0e94fb5361dcdc36 | deep | arXiv:2607.20972v1 | SRC-ARXIV@arXiv:2607.20972v1 | https://arxiv.org/html/2607.20972v1#S3 — 3 The cue-anchored memory model; https://arxiv.org/html/2607.20972v1#S4 — 4 Implementation surface | https://arxiv.org/html/2607.20972v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.20972v1#S7 — 7 Threats to validity; https://arxiv.org/html/2607.20972v1#S8 — 8 Conclusion | Exact v1 links https://github.com/swapnanil/vectr, https://github.com/anthropics/claude-code/issues/34556, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20972 | complete |
| SF-2026-ARXIV-2607-20982 | RP-31fef8fd61bd135e | deep | arXiv:2607.20982v1 | SRC-ARXIV@arXiv:2607.20982v1 | https://arxiv.org/html/2607.20982v1#S4 — 4 Guardrails Design | https://arxiv.org/html/2607.20982v1#S5.SS2 — 5.2 Results and Analysis; https://arxiv.org/html/2607.20982v1#A2.SS3 — B.3 Agent Evaluation | https://arxiv.org/html/2607.20982v1#S6 — 6 Conclusion | Exact v1 links https://github.com/langchain-ai/langchain, https://github.com/run-llama/llama_index, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20982 | complete |
| SF-2026-ARXIV-2607-20999 | RP-b876596362d97298 | standard | arXiv:2607.20999v1 | SRC-ARXIV@arXiv:2607.20999v1 | https://arxiv.org/html/2607.20999v1#S4.SS5 — 4.5 Algorithm and Prototype Instantiation | https://arxiv.org/html/2607.20999v1#S5 — 5 Experimental Setup; https://arxiv.org/html/2607.20999v1#S6 — 6 Results | https://arxiv.org/html/2607.20999v1#S7 — 7 Limitations and Ethical Considerations; https://arxiv.org/html/2607.20999v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-20999 | complete |
| SF-2026-ARXIV-2607-21000 | RP-c9ed2ecafb3c620d | deep | arXiv:2607.21000v1 | SRC-ARXIV@arXiv:2607.21000v1 | https://arxiv.org/html/2607.21000v1#S2.SS3 — 2.3 Hybrid and Long-Context Architectures; https://arxiv.org/html/2607.21000v1#S3 — 3 Method: Naju, a Native Discrete SSM | https://arxiv.org/html/2607.21000v1#A2 — Appendix B Per-Task Results with Length Extrapolation; https://arxiv.org/html/2607.21000v1#S4 — 4 Memory-Kernel and Pole-Gain Analysis | https://arxiv.org/html/2607.21000v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21000 | complete |
| SF-2026-ARXIV-2607-21005 | RP-caea6ff262845377 | deep | arXiv:2607.21005v1 | SRC-ARXIV@arXiv:2607.21005v1 | https://arxiv.org/html/2607.21005v1#S6 — 6 Training Instability in Large Language Models and Module-wise Dynamics | https://arxiv.org/html/2607.21005v1#A1.SS1 — A.1 Experimental Details; https://arxiv.org/html/2607.21005v1#A1.SS3 — A.3 Ablation Study: Weight Decay Applied Only to Non-Scale-Invariant Layers | https://arxiv.org/html/2607.21005v1#S7 — 7 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21005 | complete |
| SF-2026-ARXIV-2607-21042 | RP-9d83424370d15096 | standard | arXiv:2607.21042v1 | SRC-ARXIV@arXiv:2607.21042v1 | https://arxiv.org/html/2607.21042v1#S2 — II System Design; https://arxiv.org/html/2607.21042v1#S2.SS2 — II-B System Overview | https://arxiv.org/html/2607.21042v1#S3 — III Experiments; https://arxiv.org/html/2607.21042v1#S3.SS1 — III-A Experimental Setup | https://arxiv.org/html/2607.21042v1#S4 — IV Conclusion | Exact v1 links https://github.com/NVIDIA/TensorRT-LLM, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21042 | complete |
| SF-2026-ARXIV-2607-21051 | RP-be512e4b20ab74fc | deep | arXiv:2607.21051v1 | SRC-ARXIV@arXiv:2607.21051v1 | https://arxiv.org/html/2607.21051v1#A1.SS3 — A.3 TaleSuite Frontier-Model Reference Results; https://arxiv.org/html/2607.21051v1#A1.SS5 — A.5 Observed Errors in Model-Based Rollouts | https://arxiv.org/html/2607.21051v1#A1 — Appendix A Additional Experimental Details and Results; https://arxiv.org/html/2607.21051v1#A1.SS3 — A.3 TaleSuite Frontier-Model Reference Results | https://arxiv.org/html/2607.21051v1#A3.SS11 — C.11 Cross-Case Findings and Limitations; https://arxiv.org/html/2607.21051v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21051 | complete |
| SF-2026-ARXIV-2607-21090 | RP-f4a1881ec096bd92 | standard | arXiv:2607.21090v1 | SRC-ARXIV@arXiv:2607.21090v1 | https://arxiv.org/html/2607.21090v1#S3 — 3 Method; https://arxiv.org/html/2607.21090v1#S3.SS2 — 3.2 Reinforcement Learning framework for improving faithfulness of self-explanations | https://arxiv.org/html/2607.21090v1#A1.SS3 — A.3 Results; https://arxiv.org/html/2607.21090v1#S3.SS1 — 3.1 Faithfulness of self-explanation: definition and evaluation | https://arxiv.org/html/2607.21090v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.21090v1#S7 — 7 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21090 | complete |
| SF-2026-ARXIV-2607-21106 | RP-37d051fafd01c7fc | deep | arXiv:2607.21106v1 | SRC-ARXIV@arXiv:2607.21106v1 | https://arxiv.org/html/2607.21106v1#A1 — Appendix A ContextCite Methodology Details; https://arxiv.org/html/2607.21106v1#S3.SS1 — 3.1 Memory Architecture | https://arxiv.org/html/2607.21106v1#S5 — 5 Experiments; https://arxiv.org/html/2607.21106v1#S5.SS1 — 5.1 Experimental Setup | https://arxiv.org/html/2607.21106v1#S6 — 6 Discussion and Future Work; https://arxiv.org/html/2607.21106v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21106 | complete |
| SF-2026-ARXIV-2607-21120 | RP-51a24e80112d3432 | standard | arXiv:2607.21120v1 | SRC-ARXIV@arXiv:2607.21120v1 | https://arxiv.org/html/2607.21120v1#S5.SS1 — 5.1 Network Architecture; https://arxiv.org/html/2607.21120v1#A6 — Appendix F The Use of Large Language Models (LLMs) | https://arxiv.org/html/2607.21120v1#A3 — Appendix C Variance Analysis of the Relative Policy Gradient; https://arxiv.org/html/2607.21120v1#A5 — Appendix E Ablation on Pair Sampling | https://arxiv.org/html/2607.21120v1#S7 — 7 Limitations; https://arxiv.org/html/2607.21120v1#S8 — 8 Conclusion | Exact v1 links https://github.com/Hauf3n/relative-value-learning, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21120 | complete |
| SF-2026-ARXIV-2607-21130 | RP-525406b49652ae78 | standard | arXiv:2607.21130v1 | SRC-ARXIV@arXiv:2607.21130v1 | https://arxiv.org/html/2607.21130v1#S2.SS1 — 2.1 Framework architecture; https://arxiv.org/html/2607.21130v1#S2.SS2 — 2.2 Framework evaluation | https://arxiv.org/html/2607.21130v1#S2.SS2 — 2.2 Framework evaluation | https://arxiv.org/html/2607.21130v1#S4 — 4 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21130 | complete |
| SF-2026-ARXIV-2607-21143 | RP-d0883092a7eb67cf | standard | arXiv:2607.21143v1 | SRC-ARXIV@arXiv:2607.21143v1 | https://arxiv.org/html/2607.21143v1#A3 — Appendix C Clarification Methods; https://arxiv.org/html/2607.21143v1#S5.SS2 — 5.2 Which Models Behave Like Good Clarification Policies | https://arxiv.org/html/2607.21143v1#S2.SS3 — 2.3 Grounded Evaluation of Clarification; https://arxiv.org/html/2607.21143v1#S5 — 5 Experiments | https://arxiv.org/html/2607.21143v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.21143v1#Sx1 — Limitations | Exact v1 links https://github.com/ngocminhta/RegretBench, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21143 | complete |
| SF-2026-ARXIV-2607-21151 | RP-2a60ac73bace90d4 | standard | arXiv:2607.21151v1 | SRC-ARXIV@arXiv:2607.21151v1 | https://arxiv.org/html/2607.21151v1#S3 — 3 Framework and Experimental Setup; https://arxiv.org/html/2607.21151v1#S3.SS1 — 3.1 Diagnostic Framework | https://arxiv.org/html/2607.21151v1#A3.SS7 — C.7 Summary evaluation results; https://arxiv.org/html/2607.21151v1#A5.SS1 — E.1 Experimental task and evaluation protocol | https://arxiv.org/html/2607.21151v1#A6 — Appendix F Additional Discussion; https://arxiv.org/html/2607.21151v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21151 | complete |
| SF-2026-ARXIV-2607-21162 | RP-083c1f05857939dc | deep | arXiv:2607.21162v1 | SRC-ARXIV@arXiv:2607.21162v1 | https://arxiv.org/html/2607.21162v1#S3.SS2 — 3.2 Threat Model; https://arxiv.org/html/2607.21162v1#as1 — Supporting Information for Agree on the Model, Verify the Inference: GKR Protocols for HND-Based Transformer Inference | https://arxiv.org/html/2607.21162v1#S6 — 6 Experimental Analysis; https://arxiv.org/html/2607.21162v1#S3.SS3 — 3.3 Evaluation Commitment Backend | https://arxiv.org/html/2607.21162v1#S3.SS2 — 3.2 Threat Model; https://arxiv.org/html/2607.21162v1#S6.SS6 — 6.6 Robustness and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21162 | complete |
| SF-2026-ARXIV-2607-21179 | RP-f62b54351108dafb | standard | arXiv:2607.21179v1 | SRC-ARXIV@arXiv:2607.21179v1 | https://arxiv.org/html/2607.21179v1#S4 — 4 Method; https://arxiv.org/html/2607.21179v1#A1 — Appendix A ReMo Algorithm | https://arxiv.org/html/2607.21179v1#S5.SS2 — 5.2 Experimental Results; https://arxiv.org/html/2607.21179v1#A2 — Appendix B Further Analysis | https://arxiv.org/html/2607.21179v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.21179v1#Sx1 — Limitations | Exact v1 links https://huggingface.co/Ultralytics/YOLOv8, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21179 | complete |
| SF-2026-ARXIV-2607-21217 | RP-8bc02aa310845ecb | standard | arXiv:2607.21217v1 | SRC-ARXIV@arXiv:2607.21217v1 | https://arxiv.org/html/2607.21217v1#A9 — Appendix I Critic Model for Agentic Evaluation | https://arxiv.org/html/2607.21217v1#A9 — Appendix I Critic Model for Agentic Evaluation; https://arxiv.org/html/2607.21217v1#S2.SS1 — II-A Software-Agent Benchmarks | https://arxiv.org/html/2607.21217v1#S6 — VI Conclusion and Future Work; https://arxiv.org/html/2607.21217v1#S5 — V Discussion | Exact v1 links https://github.com/ALEX-nlp/ICAE-EVAL, https://github.com/anthropics/claude-agent-sdk-python, https://github.com/openclaw/openclaw; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21217 | complete |
| SF-2026-ARXIV-2607-21224 | RP-1f9e6097b5961348 | deep | arXiv:2607.21224v1 | SRC-ARXIV@arXiv:2607.21224v1 | https://arxiv.org/html/2607.21224v1#S2.SS3 — 2.3 Advanced Communication Frameworks and Runtimes; https://arxiv.org/html/2607.21224v1#S2.SS4 — 2.4 Local SGD and Periodic Averaging Methods | https://arxiv.org/html/2607.21224v1#A1 — Appendix A Additional Experimental Results; https://arxiv.org/html/2607.21224v1#S5 — 5 Experimental Setup | https://arxiv.org/html/2607.21224v1#S6 — 6 Results and Discussion; https://arxiv.org/html/2607.21224v1#S6.SS7 — 6.7 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21224 | complete |
| SF-2026-ARXIV-2607-21273 | RP-12e69fcb3a179da8 | deep | arXiv:2607.21273v1 | SRC-ARXIV@arXiv:2607.21273v1 | https://arxiv.org/html/2607.21273v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21273v1#S2 — 2 Related Work | https://arxiv.org/html/2607.21273v1#S3 — 3 Experimental Setting; https://arxiv.org/html/2607.21273v1#S4.SS3 — 4.3 Analysis: bounded returns, unbounded advantages | https://arxiv.org/html/2607.21273v1#S4 — 4 The Failure: Predictability Hacking; https://arxiv.org/html/2607.21273v1#S6 — 6 Controlled Separation of Failure Axes | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21273 | complete |
| SF-2026-ARXIV-2607-21291 | RP-97a4034a6e32b924 | standard | arXiv:2607.21291v1 | SRC-ARXIV@arXiv:2607.21291v1 | https://arxiv.org/html/2607.21291v1#S3 — 3 Methods; https://arxiv.org/html/2607.21291v1#S3.SS2 — 3.2 Problem Formulation and Framework Overview | https://arxiv.org/html/2607.21291v1#S4 — 4 Experiments; https://arxiv.org/html/2607.21291v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.21291v1#S4.SS4 — 4.4 Discussion; https://arxiv.org/html/2607.21291v1#S4.SS5 — 4.5 Future Work | Exact v1 links https://huggingface.co/datasets/teknium/OpenHermes-2.5, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21291 | complete |
| SF-2026-ARXIV-2607-21325 | RP-1f2432c1805a730b | deep | arXiv:2607.21325v1 | SRC-ARXIV@arXiv:2607.21325v1 | https://arxiv.org/html/2607.21325v1#S3.SS1 — 3.1. System and Request Model; https://arxiv.org/html/2607.21325v1#S3 — 3. Preliminary Formal Model | https://arxiv.org/html/2607.21325v1#S1 — 1. Introduction; https://arxiv.org/html/2607.21325v1#S2 — 2. Related Work and Positioning | https://arxiv.org/html/2607.21325v1#S3.SS4 — 3.4. Threat Model; https://arxiv.org/html/2607.21325v1#S6 — 6. Discussion and Research Agenda | Exact v1 links https://github.com/Imari91/zk-auth-agent-demo, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21325 | complete |
| SF-2026-ARXIV-2607-21351 | RP-7e8445deb7adf36d | standard | arXiv:2607.21351v1 | SRC-ARXIV@arXiv:2607.21351v1 | https://arxiv.org/html/2607.21351v1#Sx4.SSx1 — Plateaus, far below the full-model line | https://arxiv.org/html/2607.21351v1#Sx1 — Introduction; https://arxiv.org/html/2607.21351v1#Sx2 — Related Work | https://arxiv.org/html/2607.21351v1#Sx7 — Discussion; https://arxiv.org/html/2607.21351v1#Sx8 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21351 | complete |
| SF-2026-ARXIV-2607-21356 | RP-73a830a9f7eab77d | deep | arXiv:2607.21356v1 | SRC-ARXIV@arXiv:2607.21356v1 | https://arxiv.org/html/2607.21356v1#A2.SS6 — B.6 The paired design; https://arxiv.org/html/2607.21356v1#A7.SS1 — G.1 Design | https://arxiv.org/html/2607.21356v1#A11 — Appendix K Complete numerical results; https://arxiv.org/html/2607.21356v1#A13.SS5 — M.5 Two 2026 results | https://arxiv.org/html/2607.21356v1#A9.SS7 — I.7 Failure modes; https://arxiv.org/html/2607.21356v1#S11 — 11 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21356 | complete |
| SF-2026-ARXIV-2607-21372 | RP-135d7234ed314371 | standard | arXiv:2607.21372v1 | SRC-ARXIV@arXiv:2607.21372v1 | https://arxiv.org/html/2607.21372v1#S4 — 4 Methodology; https://arxiv.org/html/2607.21372v1#A2 — Appendix B Algorithms | https://arxiv.org/html/2607.21372v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.21372v1#A3.SS1 — C.1 MNIST Experiments | https://arxiv.org/html/2607.21372v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21372 | complete |
| SF-2026-ARXIV-2607-21401 | RP-ddd79bdefebd3b2f | standard | arXiv:2607.21401v1 | SRC-ARXIV@arXiv:2607.21401v1 | https://arxiv.org/html/2607.21401v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21401v1#S2 — 2 Related Work | https://arxiv.org/html/2607.21401v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.21401v1#S4 — 4 Experimental Setup | https://arxiv.org/html/2607.21401v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.21401v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21401 | complete |
| SF-2026-ARXIV-2607-21404 | RP-2507cbd4605634ed | standard | arXiv:2607.21404v1 | SRC-ARXIV@arXiv:2607.21404v1 | https://arxiv.org/html/2607.21404v1#S3 — 3 System Design; https://arxiv.org/html/2607.21404v1#S3.SS4 — 3.4 Framework Usage | https://arxiv.org/html/2607.21404v1#A2 — Appendix B Evaluation Protocols and Benchmarks; https://arxiv.org/html/2607.21404v1#A3.SS3 — C.3 Adding New Protocols and Benchmarks | https://arxiv.org/html/2607.21404v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.21404v1#Sx1 — Limitations | Exact v1 links https://github.com/JJJAYYYZhao/MemTools-public, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21404 | complete |
| SF-2026-ARXIV-2607-21405 | RP-8827bb95c492f5c0 | standard | arXiv:2607.21405v1 | SRC-ARXIV@arXiv:2607.21405v1 | https://arxiv.org/html/2607.21405v1#S4 — 4 Method: Hybrid and Ladder Head Allocation; https://arxiv.org/html/2607.21405v1#S5.SS4 — 5.4 Scaling to 410M-class models (405M parameters) | https://arxiv.org/html/2607.21405v1#S5.SS5 — 5.5 Ladder ablation: a negative result at 160M, and a confirmed reversal at 410M; https://arxiv.org/html/2607.21405v1#S5 — 5 Experiments | https://arxiv.org/html/2607.21405v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.21405v1#S7 — 7 Conclusion | Exact v1 links https://github.com/gkamradt/needle-in-a-haystack, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21405 | complete |
| SF-2026-ARXIV-2607-21419 | RP-1c8996d3e293c382 | standard | arXiv:2607.21419v1 | SRC-ARXIV@arXiv:2607.21419v1 | https://arxiv.org/html/2607.21419v1#S3 — 3 Method | https://arxiv.org/html/2607.21419v1#A1.SS1 — A.1 Training and Evaluation Configuration; https://arxiv.org/html/2607.21419v1#A2 — Appendix B Stage 1 Details and Supplementary Results | https://arxiv.org/html/2607.21419v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21419 | complete |
| SF-2026-ARXIV-2607-21433 | RP-93f53df7d5e0a63f | standard | arXiv:2607.21433v1 | SRC-ARXIV@arXiv:2607.21433v1 | https://arxiv.org/html/2607.21433v1#S5.SS3 — 5.3 Toward practical early-exit systems | https://arxiv.org/html/2607.21433v1#S3.SS1 — 3.1 Experimental setup; https://arxiv.org/html/2607.21433v1#S3.SS2 — 3.2 Results | https://arxiv.org/html/2607.21433v1#S2.SS2 — 2.2 Reasoning failure modes; https://arxiv.org/html/2607.21433v1#S5 — 5 Discussion | Exact v1 links https://huggingface.co/datasets/gneubig/aime-1983-2024, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21433 | complete |
| SF-2026-ARXIV-2607-21453 | RP-f87404546c107955 | standard | arXiv:2607.21453v1 | SRC-ARXIV@arXiv:2607.21453v1 | https://arxiv.org/html/2607.21453v1#S4 — 4 Methodology; https://arxiv.org/html/2607.21453v1#S5 — 5 The TTEL Algorithm | https://arxiv.org/html/2607.21453v1#A3 — Appendix C Detailed Results for Scaling Experiments; https://arxiv.org/html/2607.21453v1#S8 — 8 Experimental Results | https://arxiv.org/html/2607.21453v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21453v1#S2 — 2 Related Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21453 | complete |
| SF-2026-ARXIV-2607-21475 | RP-633c74f5912ecff1 | deep | arXiv:2607.21475v1 | SRC-ARXIV@arXiv:2607.21475v1 | https://arxiv.org/html/2607.21475v1#S3.SS3 — 3.3 Design: certainty plus Poisson tail, Hájek by logit offset; https://arxiv.org/html/2607.21475v1#S6.SS1 — 6.1 Design | https://arxiv.org/html/2607.21475v1#A2 — Appendix B Experimental details; https://arxiv.org/html/2607.21475v1#S6 — 6 Pre-registered study on real workloads, at two scales | https://arxiv.org/html/2607.21475v1#S5 — 5 From attention error to task failure: synthetic suites; https://arxiv.org/html/2607.21475v1#S6.SS3 — 6.3 The silent-failure panel | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21475 | complete |
| SF-2026-ARXIV-2607-21480 | RP-7e3c82e4d34bbb73 | deep | arXiv:2607.21480v1 | SRC-ARXIV@arXiv:2607.21480v1 | https://arxiv.org/html/2607.21480v1#A1.SS1 — A.1 Proof of the finite-class design bound; https://arxiv.org/html/2607.21480v1#A1.SS2 — A.2 Proof of the VC-class design bound | https://arxiv.org/html/2607.21480v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21480v1#S1.SS1 — 1.1 Motivating examples | https://arxiv.org/html/2607.21480v1#S9 — 9 Conclusion and future directions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21480 | complete |
| SF-2026-ARXIV-2607-21482 | RP-2432954eed96e8ae | standard | arXiv:2607.21482v1 | SRC-ARXIV@arXiv:2607.21482v1 | https://arxiv.org/pdf/2607.21482v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.21482v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.21482v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.21482v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.21482v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.21482v1#page=10 — PDF page 10 | Exact v1 links https://github.com/UCL-ARC/RRBench, https://github.com/cls-data/ns_core, https://github.com/CLS-Data/ns_core; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21482 | complete |
| SF-2026-ARXIV-2607-21503 | RP-5d8a339141b90ddd | deep | arXiv:2607.21503v1 | SRC-ARXIV@arXiv:2607.21503v1 | https://arxiv.org/html/2607.21503v1#A2 — Appendix B Retrieval-study methodology (motivating study, Section 3.3); https://arxiv.org/html/2607.21503v1#S4 — 4 The Maximem Synap System | https://arxiv.org/html/2607.21503v1#S6 — 6 Evaluation; https://arxiv.org/html/2607.21503v1#S6.SS2 — 6.2 Results | https://arxiv.org/html/2607.21503v1#S6.SS3 — 6.3 Scope and limitations of this evaluation; https://arxiv.org/html/2607.21503v1#S8 — 8 Future Directions: Decision-Level and Organization-Scale Context | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21503 | complete |
| SF-2026-ARXIV-2607-21522 | RP-46b024ca911e9836 | deep | arXiv:2607.21522v1 | SRC-ARXIV@arXiv:2607.21522v1 | https://arxiv.org/html/2607.21522v1#S3 — 3 GS-Agent: A Multi-Agent Framework with Generative Simulation in the Loop; https://arxiv.org/html/2607.21522v1#A2 — Appendix B Additional Implementation Details | https://arxiv.org/html/2607.21522v1#S4.SS4 — 4.4 Ablation and Backbone Analysis; https://arxiv.org/html/2607.21522v1#A3 — Appendix C Additional Experiment Details | https://arxiv.org/html/2607.21522v1#A3.SS3 — C.3 Failure Analysis; https://arxiv.org/html/2607.21522v1#S5 — 5 Discussions | Exact v1 links https://github.com/Genesis-Embodied-AI/Genesis, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21522 | complete |
| SF-2026-ARXIV-2607-21530 | RP-748fb784b915ecb4 | standard | arXiv:2607.21530v1 | SRC-ARXIV@arXiv:2607.21530v1 | https://arxiv.org/html/2607.21530v1#S2.SS1 — 2.1. Bug Model; https://arxiv.org/html/2607.21530v1#S3 — 3. Formal Model | https://arxiv.org/html/2607.21530v1#S8 — 8. Evaluation and Results | https://arxiv.org/html/2607.21530v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.21530v1#S8.SS6 — 8.6. Threats to Validity | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21530 | complete |
| SF-2026-ARXIV-2607-21535 | RP-35afe235f065adab | deep | arXiv:2607.21535v1 | SRC-ARXIV@arXiv:2607.21535v1 | https://arxiv.org/html/2607.21535v1#S2.SS0.SSS0.Px4 — Serving systems.; https://arxiv.org/html/2607.21535v1#S4 — 4 Method: Windowed-MTP | https://arxiv.org/html/2607.21535v1#A4 — Appendix D Full results tables; https://arxiv.org/html/2607.21535v1#S6 — 6 Experiments | https://arxiv.org/html/2607.21535v1#S7 — 7 Discussion and limitations; https://arxiv.org/html/2607.21535v1#S7.SS0.SSS0.Px9 — Limitations. | Exact v1 links https://github.com/avalliappan-nvidia/windowed-mtp-b200, https://github.com/deepseek-ai/DeepSpec, https://github.com/sgl-project/sglang/pull/22077; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21535 | complete |
| SF-2026-ARXIV-2607-21550 | RP-8fe9f0e69d4dc243 | standard | arXiv:2607.21550v1 | SRC-ARXIV@arXiv:2607.21550v1 | https://arxiv.org/html/2607.21550v1#S4 — 4 Method; https://arxiv.org/html/2607.21550v1#S2.SS1 — 2.1 Reasoning in Large Audio Language Models | https://arxiv.org/html/2607.21550v1#A1 — Appendix A Additional Experiment Details; https://arxiv.org/html/2607.21550v1#A3 — Appendix C Ablation Study | https://arxiv.org/html/2607.21550v1#S3.SS2 — 3.2 Offline Distillation and its Limitation; https://arxiv.org/html/2607.21550v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21550 | complete |
| SF-2026-ARXIV-2607-21553 | RP-8715fcd11af1a443 | deep | arXiv:2607.21553v1 | SRC-ARXIV@arXiv:2607.21553v1 | https://arxiv.org/html/2607.21553v1#A5.SS3 — E.3 Qualitative Comparison with Other Methods; https://arxiv.org/html/2607.21553v1#S3.SS2 — 3.2 Hybrid Attention Design | https://arxiv.org/html/2607.21553v1#A4 — Appendix D Evaluation and Measurement Protocols; https://arxiv.org/html/2607.21553v1#A4.SS1 — D.1 Sampling and VBench Evaluation | https://arxiv.org/html/2607.21553v1#S8 — 8 Conclusion | Exact v1 links https://github.com/NVlabs/Sana, https://github.com/Wan-Video/Wan2.2, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21553 | complete |
| SF-2026-ARXIV-2607-21557 | RP-9bfb0b10753ff1c0 | deep | arXiv:2607.21557v1 | SRC-ARXIV@arXiv:2607.21557v1 | https://arxiv.org/html/2607.21557v1#S3 — 3 Methods | https://arxiv.org/html/2607.21557v1#A3 — Appendix C Evaluation Details; https://arxiv.org/html/2607.21557v1#A3.SS1 — C.1 ClawEval and QwenClawBench Evaluation Details | https://arxiv.org/html/2607.21557v1#S5 — 5 Discussion; https://arxiv.org/html/2607.21557v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/datasets/zai-org/ZClawBench, https://code.claude.com/docs/en/overview, https://github.com/MiniMax-AI/MiniMax-M2.5; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21557 | complete |
| SF-2026-ARXIV-2607-21571 | RP-c10758e959a3f6c8 | deep | arXiv:2607.21571v1 | SRC-ARXIV@arXiv:2607.21571v1 | https://arxiv.org/html/2607.21571v1#S1 — I Introduction; https://arxiv.org/html/2607.21571v1#S2 — II Related Work | https://arxiv.org/html/2607.21571v1#S5 — V Experimental Results and Analysis; https://arxiv.org/html/2607.21571v1#S6.SS2 — VI-B Results and Analysis | https://arxiv.org/html/2607.21571v1#S7 — VII Conclusion | Exact v1 links https://github.com/jangablox/sequential-eqa, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21571 | complete |
| SF-2026-ARXIV-2607-21576 | RP-9cb900f4fdc9fe37 | standard | arXiv:2607.21576v1 | SRC-ARXIV@arXiv:2607.21576v1 | https://arxiv.org/html/2607.21576v1#S2 — 2 Method; https://arxiv.org/html/2607.21576v1#A1.SS8 — A.8 Supervised model evaluation | https://arxiv.org/html/2607.21576v1#S3.SS5 — 3.5 Analysis and Ablation Studies; https://arxiv.org/html/2607.21576v1#A1 — Appendix A Dataset and Evaluation Details | https://arxiv.org/html/2607.21576v1#A3 — Appendix C Limitations; https://arxiv.org/html/2607.21576v1#S5 — 5 Conclusion | Exact v1 links https://lukasknobel.github.io/projects/StructuredDynamics, https://github.com/facebookresearch/dinov2/blob/7b187bd4df8efce2cbcbbb67bd01532c19bf4c9c/LICENSE, https://huggingface.co/facebook/vit-mae-base; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21576 | complete |
| SF-2026-ARXIV-2607-21582 | RP-9673c41f9b433062 | standard | arXiv:2607.21582v1 | SRC-ARXIV@arXiv:2607.21582v1 | https://arxiv.org/html/2607.21582v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21582v1#S2 — 2 Related Works | https://arxiv.org/html/2607.21582v1#A3.SS4 — C.4 Simulation experiment results; https://arxiv.org/html/2607.21582v1#A1 — Appendix A Factor Evaluation Space | https://arxiv.org/html/2607.21582v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21582 | complete |
| SF-2026-ARXIV-2607-21585 | RP-dcb84cc991b84f8c | standard | arXiv:2607.21585v1 | SRC-ARXIV@arXiv:2607.21585v1 | https://arxiv.org/html/2607.21585v1#S11 — 11 Discrete Sequence Implementation Details; https://arxiv.org/html/2607.21585v1#S12 — 12 Discrete Graph Implementation Details | https://arxiv.org/html/2607.21585v1#S13 — 13 Experiment Details; https://arxiv.org/html/2607.21585v1#S6 — 6 Experiments | https://arxiv.org/html/2607.21585v1#S8 — 8 Limitations and Future Work; https://arxiv.org/html/2607.21585v1#S7 — 7 Conclusion | Exact v1 links https://github.com/sophtang/ExpandingFlowMaps, https://huggingface.co/ChatterjeeLab/ExpandingFlowMaps, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21585 | complete |
| SF-2026-ARXIV-2607-21588 | RP-a05de6d96c938ff1 | standard | arXiv:2607.21588v1 | SRC-ARXIV@arXiv:2607.21588v1 | https://arxiv.org/html/2607.21588v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21588v1#S2 — 2 Related Work | https://arxiv.org/html/2607.21588v1#S5 — 5 Experiments; https://arxiv.org/html/2607.21588v1#S5.SS1 — 5.1 Experimental Setup | https://arxiv.org/html/2607.21588v1#S6 — 6 Discussion; https://arxiv.org/html/2607.21588v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21588 | complete |
| SF-2026-ARXIV-2607-21591 | RP-529c32b482677357 | standard | arXiv:2607.21591v1 | SRC-ARXIV@arXiv:2607.21591v1 | https://arxiv.org/html/2607.21591v1#S4.SS1 — 4.1 Backbone Models; https://arxiv.org/html/2607.21591v1#S4.SS7 — 4.7 Comparison to Finetuned Models | https://arxiv.org/html/2607.21591v1#S0.SS1 — S1 Analysis of Intermediate Rewards; https://arxiv.org/html/2607.21591v1#S0.SS10 — S10 Human Evaluations | https://arxiv.org/html/2607.21591v1#S5 — 5 Discussion | Exact v1 links https://github.com/rogerioagjr/psp, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21591 | complete |
| SF-2026-ARXIV-2607-21594 | RP-c039ee01e940ed41 | deep | arXiv:2607.21594v1 | SRC-ARXIV@arXiv:2607.21594v1 | https://arxiv.org/html/2607.21594v1#S3 — 3 Method; https://arxiv.org/html/2607.21594v1#S4.SS4 — 4.4 Analysis of Model Architecture | https://arxiv.org/html/2607.21594v1#S4 — 4 Experiments; https://arxiv.org/html/2607.21594v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.21594v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21594 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-20426:start -->
### Knowledge Injection Exists in MoE? Exploring Expert-Aware Contrast Decoding in MoE for Mitigating LLMs'Hallucinations

<!-- claim:SF-2026-ARXIV-2607-20426:start -->Existing LLM hallucination mitigation methods, including prompt engineering and model optimization, either hardly alter models'internal knowledge or have poor cross-domain generalization. Contrastive decoding mitigates hallucinations by using layer-wise differences in LLMs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20426:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing LLM hallucination mitigation methods, including prompt engineering and model optimization, either hardly alter models'internal knowledge or have poor cross-domain generalization.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** However, prior studies only explore transformer-based models (e.g., GPT), ignoring other effective frameworks like mixture-of-experts (MoE) models.

**证据证明什么。** Our results show that they do not exist in MoE with shared experts; nevertheless, across different MoEs, higher layers exhibit distinct expert activation patterns between factual and non-factual outputs.

**证据没有证明什么。** If MoE architectures do not remain mainstream in the future, the direct applicability of our method may be limited. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20426v1#A2 — Appendix B Malicious System Prompt in RQ2; https://arxiv.org/html/2607.20426v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.20426v1#A5 — Appendix E Significance Test of Experimental Results; https://arxiv.org/html/2607.20426v1#A10 — Appendix J Dataset-level Analysis of “Knowledge Injection” in MoE models。Limitations / counterevidence：https://arxiv.org/html/2607.20426v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.20426v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：If MoE architectures do not remain mainstream in the future, the direct applicability of our method may be limited.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20426:end -->

<!-- review:SF-2026-ARXIV-2607-20427:start -->
### Is MoE Routing a Huffman Code? Discovering the Frequency-Diversity Law in Chain-of-Thought

<!-- claim:SF-2026-ARXIV-2607-20427:start -->Mixture-of-Experts architectures have revolutionized scaling, yet the underlying logic of their routing remains a black box. In this paper, we uncover a fundamental governing principle: MoE routing is not merely selection, but a manifestation of Huffman Coding. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20427:end -->

**为什么进入候选分母。** 摘要首要问题为“Mixture-of-Experts architectures have revolutionized scaling, yet the underlying logic of their routing remains a black box.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To bridge this gap, we propose Subset Difference Pruning, a surgical strategy to eliminate functional duplicates.

**证据证明什么。** We demonstrate that pruning does not degrade reasoning; instead, it unleashes the model's latent Huffman efficiency, forcing the logic to collapse into streamlined, high-density paths.

**证据没有证明什么。** With only categories, the Pearson correlation in the Huffman scatter is estimated from four points per model; the result is not statistically significant for Qwen’s baseline ( ) and only marginally so for the two Huffman-compliant models ( ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20427v1#A1 — Appendix A Model Architecture Details; https://arxiv.org/html/2607.20427v1#A2 — Appendix B Architecture-Specific Routing Patterns: Extended Discussion。Evaluation：https://arxiv.org/html/2607.20427v1#A4 — Appendix D Qwen3.5-35B-A3B Expert Functional Profile Analysis; https://arxiv.org/html/2607.20427v1#S3 — 3 Temporal Expert Combination Encoding: Information-Theoretic Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.20427v1#A11 — Appendix K Limitations; https://arxiv.org/html/2607.20427v1#A2 — Appendix B Architecture-Specific Routing Patterns: Extended Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：With only categories, the Pearson correlation in the Huffman scatter is estimated from four points per model; the result is not statistically significant for Qwen’s baseline ( ) and only marginally so for the two Huffman-compliant models ( ).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20427:end -->

<!-- review:SF-2026-ARXIV-2607-20432:start -->
### Position: Natural Language Should Not Fully Replace Formal Languages

<!-- claim:SF-2026-ARXIV-2607-20432:start -->Recent advances in large language models and their widespread adoption have prompted claims that natural language could entirely replace formal languages, such as programming languages for software design. In this position paper, we argue that this perspective overlooks fundamental linguistic properties of natural language, specifically that it is optimized for underspecification in open-ended contexts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20432:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in large language models and their widespread adoption have prompted claims that natural language could entirely replace formal languages, such as programming languages for software design.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce a formal framework centered on *task specificity*, defining it as the information-theoretic reduction of uncertainty in an output space -- such as all possible images -- given a user's specific requirements.

**证据证明什么。** We prove a *specificity crossover theorem*, showing the existence of a threshold beyond which the cost to express formal requirements into natural language exceeds the cost of direct formal specification.

**证据没有证明什么。** However, we argue that the role of domain experts—such as programmers and artists—will not become obsolete. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20432v1#S3 — 3 Formal Framework。Evaluation：https://arxiv.org/html/2607.20432v1#S4 — 4 Case Study: Image Generation and Other Modalities。Limitations / counterevidence：https://arxiv.org/html/2607.20432v1#S5 — 5 Implications and Future Directions; https://arxiv.org/html/2607.20432v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：However, we argue that the role of domain experts—such as programmers and artists—will not become obsolete.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20432:end -->

<!-- review:SF-2026-ARXIV-2607-20433:start -->
### Moir: Let the Model Direct Its Own Story for Robust Cross-Domain Knowledge Editing

<!-- claim:SF-2026-ARXIV-2607-20433:start -->While language models remain frozen at their training state, the world evolves continuously. Knowledge editing has emerged as a key alternative to full retraining, but its deployment is bottlenecked by the erosion of core capabilities: mathematical and programmatic reasoning collapse while encyclopedic recall remains intact. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20433:end -->

**为什么进入候选分母。** 摘要首要问题为“While language models remain frozen at their training state, the world evolves continuously.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose Moir, which estimates the preservation covariance $C$ directly from the model itself by sampling from its own decoding distribution.

**证据证明什么。** These results suggest that aligning the preservation distribution with the model's operative distribution is a key factor in non-destructive editing, and that the model itself may be the most accessible source of that distribution for deployed systems.

**证据没有证明什么。** In contrast, self-generation provides a dynamic map of this evolved geometry that static external corpora cannot replicate. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20433v1#A1 — Appendix A Extended Methodology; https://arxiv.org/html/2607.20433v1#A3.SS1 — C.1 Models, Editors, and Hyperparameters。Evaluation：https://arxiv.org/html/2607.20433v1#A3 — Appendix C Experimental Setup and Baselines; https://arxiv.org/html/2607.20433v1#A3.SS3 — C.3 Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.20433v1#S7 — 7 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/togethercomputer/RedPajama-Data, https://github.com/opencv/opencv, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：In contrast, self-generation provides a dynamic map of this evolved geometry that static external corpora cannot replicate.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20433:end -->

<!-- review:SF-2026-ARXIV-2607-20434:start -->
### Break Through the Compression Bottleneck: From Theory to Practice

<!-- claim:SF-2026-ARXIV-2607-20434:start -->As the parameter size of language models continues to grow, effective model compression is required to reduce their computational and memory overhead. Existing compression methods suffer from bottleneck issues: when the compression ratio is increased, performance degrades significantly. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20434:end -->

**为什么进入候选分母。** 摘要首要问题为“As the parameter size of language models continues to grow, effective model compression is required to reduce their computational and memory overhead.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Importantly, we propose a novel approach Diagonal Adhesive Method (DAM), which can effectively combine the two methods and mitigate the performance loss.

**证据证明什么。** Our results demonstrate that these methods are non-orthogonal, and their combination leads to significant performance degradation.

**证据没有证明什么。** However, the compression order of performing quantization first and then low-rank decomposition is still meaningful. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20434v1#S4 — 4 Diagonal Adhesive Method; https://arxiv.org/html/2607.20434v1#S5.SS3 — 5.3 Verification of the Diagonal Adhesive Method。Evaluation：https://arxiv.org/html/2607.20434v1#A7 — Appendix G Supplementary experimental results; https://arxiv.org/html/2607.20434v1#A7.SS1 — G.1 Experimental results of other models。Limitations / counterevidence：https://arxiv.org/html/2607.20434v1#A1.SSx6 — Final Conclusion; https://arxiv.org/html/2607.20434v1#A8 — Appendix H Discussion on different compression orders。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：However, the compression order of performing quantization first and then low-rank decomposition is still meaningful.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`layering_dependency`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20434:end -->

<!-- review:SF-2026-ARXIV-2607-20436:start -->
### Routing Subspaces: Auditing Evaluation-to-Deployment Mismatch in Fine-Tuned Language Models

<!-- claim:SF-2026-ARXIV-2607-20436:start -->Safety evaluations often assume that behavior observed during testing reflects behavior in ordinary use, but fine-tuning can break this assumption. A checkpoint can appear fixed under evaluation-style prompts while the same behavior persists under ordinary-use prompts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20436:end -->

**为什么进入候选分母。** 摘要首要问题为“Safety evaluations often assume that behavior observed during testing reflects behavior in ordinary use, but fine-tuning can break this assumption.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** A checkpoint can appear fixed under evaluation-style prompts while the same behavior persists under ordinary-use prompts.

**证据证明什么。** The audit is a diagnostic for fine-tuned checkpoints, not a training-time defense or a guarantee of deployment safety.

**证据没有证明什么。** For Gemma-2-9B, depth (layers – ) closes the gap by , while the default heuristic at closes it by only , consistent with a type-1 failure (heuristic close but off by one window step). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20436v1#S2 — 2 Methodology; https://arxiv.org/html/2607.20436v1#S2.SS2 — 2.2 Localization Method。Evaluation：https://arxiv.org/html/2607.20436v1#A5 — Appendix E Per-item intervention agreement analysis; https://arxiv.org/html/2607.20436v1#S3 — 3 Results。Limitations / counterevidence：https://arxiv.org/html/2607.20436v1#A7 — Appendix G E4 Adjacent-Window Depth Sweep and Typed-Failure Remediation; https://arxiv.org/html/2607.20436v1#S4 — 4 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：For Gemma-2-9B, depth (layers – ) closes the gap by , while the default heuristic at closes it by only , consistent with a type-1 failure (heuristic close but off by one window step).

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20436:end -->

<!-- review:SF-2026-ARXIV-2607-20437:start -->
### TopoGuard: Graph Theory Based Defenses Against Split-Knowledge Attacks on RAG

<!-- claim:SF-2026-ARXIV-2607-20437:start -->Production Retrieval Augmented Generation (RAG) systems rely on aggregating multiple external documents to answer complex queries. However, the retrieved documents introduce a new threat surface that can be exploited to launch split-knowledge attacks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20437:end -->

**为什么进入候选分母。** 摘要首要问题为“Production Retrieval Augmented Generation (RAG) systems rely on aggregating multiple external documents to answer complex queries.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Extensive experiments are conducted on two retrieval datasets and compared with multiple baseline methods.

**证据证明什么。** This paper shows that the new attack is structurally invisible to existing per-document filters, like LlamaGuard.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20437v1#S4.SS1 — 4.1 Methods and Baselines; https://arxiv.org/html/2607.20437v1#A1 — Appendix A Threat Model Validation。Evaluation：https://arxiv.org/html/2607.20437v1#A1.SS1 — A.1 Experimental Setup; https://arxiv.org/html/2607.20437v1#A6 — Appendix F Evaluation on PoisonedRAG Attacks。Limitations / counterevidence：https://arxiv.org/html/2607.20437v1#A1 — Appendix A Threat Model Validation; https://arxiv.org/html/2607.20437v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard3/8B/MODEL_CARD.md, https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard2/MODEL_CARD.md, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20437:end -->

<!-- review:SF-2026-ARXIV-2607-20438:start -->
### Preference Tuning as Spectral Update Reorganization

<!-- claim:SF-2026-ARXIV-2607-20438:start -->Preference-based post-training is usually understood through endpoint behavior, yet the learned update that produces this behavior remains largely opaque. We study RLHF and related preference optimization through the spectral structure of their induced parameter updates. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20438:end -->

**为什么进入候选分母。** 摘要首要问题为“Preference-based post-training is usually understood through endpoint behavior, yet the learned update that produces this behavior remains largely opaque.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We study RLHF and related preference optimization through the spectral structure of their induced parameter updates.

**证据证明什么。** Plug-in intervention shows that the head accounts for the visible behavioral departure from the base model, while the tail is weak in isolation.

**证据没有证明什么。** Our analysis identifies structure in learned updates, not the circuits that implement the resulting behavior. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20438v1#S4.SS2 — 4.2 Generality Across Models and Training Regimes。Evaluation：https://arxiv.org/html/2607.20438v1#A2.SS1 — B.1 Experimental Setup; https://arxiv.org/html/2607.20438v1#A3.SS4 — C.4 Evaluation and Scoring。Limitations / counterevidence：https://arxiv.org/html/2607.20438v1#S7 — 7 Discussion and Limitations; https://arxiv.org/html/2607.20438v1#S7.SS2 — 7.2 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Our analysis identifies structure in learned updates, not the circuits that implement the resulting behavior.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20438:end -->

<!-- review:SF-2026-ARXIV-2607-20457:start -->
### Dropping the Anchor: Statistical Context Summarization for Distributed Systems via Pulsar Attention

<!-- claim:SF-2026-ARXIV-2607-20457:start -->Inference with large language models (LLMs) on long sequences is computationally expensive due to the quadratic complexity of self-attention. Distributed blockwise methods such as Star Attention reduce this cost by sharding context across hosts, but rely on prepending a static, content-blind copy of the first block to every host. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20457:end -->

**为什么进入候选分母。** 摘要首要问题为“Inference with large language models (LLMs) on long sequences is computationally expensive due to the quadratic complexity of self-attention.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Distributed blockwise methods such as Star Attention reduce this cost by sharding context across hosts, but rely on prepending a static, content-blind copy of the first block to every host.

**证据证明什么。** This reduces the Phase 1 per-GPU FLOPs by up to 3.3x over Star Attention while retaining an identical KV cache footprint.

**证据没有证明什么。** Future work will address this through query-aware or multi-score selection strategies, and validate the FLOPs-based speedup estimates with end-to-end wall-clock profiling. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20457v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.20457v1#S4 — 4 Experiments; https://arxiv.org/html/2607.20457v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.20457v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Future work will address this through query-aware or multi-score selection strategies, and validate the FLOPs-based speedup estimates with end-to-end wall-clock profiling.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20457:end -->

<!-- review:SF-2026-ARXIV-2607-20464:start -->
### Stochastic Sampling is Epistemically Shallow: The Dimensionality Gap Between Temperature Variation and Model Diversity in LLMs

<!-- claim:SF-2026-ARXIV-2607-20464:start -->When a language model gives different answers on repeated runs, does that variation reveal what it does not know? Self-consistency turns the variation into a per-question uncertainty estimate via majority voting. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20464:end -->

**为什么进入候选分母。** 摘要首要问题为“When a language model gives different answers on repeated runs, does that variation reveal what it does not know?”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Self-consistency turns the variation into a per-question uncertainty estimate via majority voting.

**证据证明什么。** Self-consistency gives accurate per-question uncertainty but no detectable cross-question structure; only a diverse ensemble surfaces what a model does not know.

**证据没有证明什么。** 5 Limitations and Future Work • Binary correctness. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20464v1#A3.SS1 — C.1 Method; https://arxiv.org/html/2607.20464v1#S2 — 2 Method。Evaluation：https://arxiv.org/html/2607.20464v1#A2.SS1 — B.1 Parallel Analysis; https://arxiv.org/html/2607.20464v1#A2.SS3 — B.3 Shannon Effective Rank: Definition and Extended Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.20464v1#S5 — 5 Limitations and Future Work; https://arxiv.org/html/2607.20464v1#S4 — 4 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：5 Limitations and Future Work • Binary correctness.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20464:end -->

<!-- review:SF-2026-ARXIV-2607-20465:start -->
### DataPrep-Bench: Benchmarking LLMs as Training Data Preparators

<!-- claim:SF-2026-ARXIV-2607-20465:start -->The quality of training data fundamentally determines the capabilities of large language models (LLMs), yet no unified benchmark exists to measure how well LLMs, agents, and data-centric workflows actually prepare training data end to end. We view LLM-driven data preparation as comprising two complementary capabilities: data construction, which transforms raw sources into supervised training data, and data quality evaluation, which predicts the training value of candidate datasets before downstream training; throughout, "quality" refers to downstream training utility rather than surface-level textual properties. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20465:end -->

**为什么进入候选分母。** 摘要首要问题为“The quality of training data fundamentally determines the capabilities of large language models (LLMs), yet no unified benchmark exists to measure how well LLMs, agents, and data-centric workflows actually prepare training data end to end.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** DataPrep-Bench provides a unified, downstream-grounded framework for measuring progress on both capabilities as co-equal targets of LLM-driven data preparation.

**证据证明什么。** DAS attains the strongest cross-model correlation in four of six domains and is the only metric clearing r &gt; 0.70 simultaneously in Math, Science, and Medical, outperforming existing quality-, diversity-, and heuristic-based evaluators.

**证据没有证明什么。** First, adding synthesized domain data on top of the Dolly-15k instruction-following corpus frequently degrades the Dolly-only baseline across construction methods and model architectures, a finding that surface-level quality metrics would not have anticipated, underscoring the necessity of end-to-end, downstream-grounded evaluation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20465v1#S3 — 3 Benchmark Design; https://arxiv.org/html/2607.20465v1#S4 — 4 Methods。Evaluation：https://arxiv.org/html/2607.20465v1#S3.SS5 — 3.5 Downstream Evaluation Benchmarks; https://arxiv.org/html/2607.20465v1#S5.SS3 — 5.3 Results of Data Quality Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.20465v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/haolpku/Data-Preparation-Bench, https://huggingface.co/datasets/lhpku20010120/Data-Prep-Bench, https://huggingface.co/HuggingFaceFW/fineweb-edu-classifier; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：First, adding synthesized domain data on top of the Dolly-15k instruction-following corpus frequently degrades the Dolly-only baseline across construction methods and model architectures, a finding that surface-level quality metrics would not have anticipated, underscoring the necessity of end-to-end, downstream-grounded evaluation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20465:end -->

<!-- review:SF-2026-ARXIV-2607-20466:start -->
### JAXBench: Benchmarking Autonomous TPU Kernel Optimization

<!-- claim:SF-2026-ARXIV-2607-20466:start -->Rigorous benchmarks have driven progress in autonomous GPU kernel performance optimization by establishing a shared target to hillclimb on, but no equivalent exists for TPUs. We present JAXBench, a TPU-native benchmark suite for AI-generated kernel optimization on Google Cloud TPUs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20466:end -->

**为什么进入候选分母。** 摘要首要问题为“Rigorous benchmarks have driven progress in autonomous GPU kernel performance optimization by establishing a shared target to hillclimb on, but no equivalent exists for TPUs.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We evaluate four feedback-driven methods on generating candidate Pallas kernels for JAXBench.

**证据证明什么。** Across the full suite with Gemini 3 Flash, we find that target-specific context matters more than model scale on a sparsely-documented DSL like Pallas.

**证据没有证明什么。** 5 Conclusion Hand-optimized accelerator kernels remain a persistent bottleneck for ML systems, and the pool of engineers fluent in both ML and low-level systems programming cannot keep pace with new architectures and hardware revisions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20466v1#S2 — 2 Methodology; https://arxiv.org/html/2607.20466v1#S2.SS1 — 2.1 Design Principles。Evaluation：https://arxiv.org/html/2607.20466v1#A1 — Appendix A Per-Benchmark Results; https://arxiv.org/html/2607.20466v1#S3 — 3 Results。Limitations / counterevidence：https://arxiv.org/html/2607.20466v1#S4 — 4 Discussion and Future Work; https://arxiv.org/html/2607.20466v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/AI-Hypercomputer/accelerator-agents/tree/main/JAXBench, https://github.com/AI-Hypercomputer/maxtext, https://github.com/openxla/tokamax; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：5 Conclusion Hand-optimized accelerator kernels remain a persistent bottleneck for ML systems, and the pool of engineers fluent in both ML and low-level systems programming cannot keep pace with new architectures and hardware revisions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20466:end -->

<!-- review:SF-2026-ARXIV-2607-20467:start -->
### DC-Leap: Training-Free Acceleration of dLLMs via Draft-Guided Contiguous Leaping Decoding

<!-- claim:SF-2026-ARXIV-2607-20467:start -->While parallel decoding is central to the efficiency of Diffusion Large Language Models (dLLMs), current strategies are often hindered by overly conservative confidence thresholds. These thresholds, necessitated by the Joint Probability Dependence Error (JPDE), result in redundant denoising iterations and suboptimal inference speeds. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20467:end -->

**为什么进入候选分母。** 摘要首要问题为“While parallel decoding is central to the efficiency of Diffusion Large Language Models (dLLMs), current strategies are often hindered by overly conservative confidence thresholds.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To overcome this, we propose DC-Leap, a training-free framework that enables reliable acceleration of dLLMs in the moderate-confidence regime.

**证据证明什么。** Extensive experiments on standard benchmarks demonstrate that DC-Leap achieves substantial speedups, up to 53.19x on MBPP for long-sequence generation, and up to 105.02x when combined with KV-Cache with comparable generation quality.

**证据没有证明什么。** 5 Conclusion In this work, we identify the strict thresholding driven by the conditional independence assumption in non-contiguous decoding as a critical bottleneck limiting inference speed. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20467v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20467v1#A1 — Appendix A Algorithm of DC-Leap。Evaluation：https://arxiv.org/html/2607.20467v1#A6 — Appendix F More Results and Analysis; https://arxiv.org/html/2607.20467v1#A6.SS1 — F.1 More Results of Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.20467v1#A5.SS4 — E.4 Observations and Discussions; https://arxiv.org/html/2607.20467v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ffh-wyls/DC-Leap, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：5 Conclusion In this work, we identify the strict thresholding driven by the conditional independence assumption in non-contiguous decoding as a critical bottleneck limiting inference speed.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20467:end -->

<!-- review:SF-2026-ARXIV-2607-20468:start -->
### InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents

<!-- claim:SF-2026-ARXIV-2607-20468:start -->AI agents are increasingly used to automate research and development tasks, yet existing benchmarks typically evaluate them on prescribed workflows or narrow action spaces. Even nominally open-ended tasks can often be solved by retrieving a well-known recipe and tuning a few hyperparameters, making it unclear whether strong results reflect genuine optimization or memorized solutions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20468:end -->

**为什么进入候选分母。** 摘要首要问题为“AI agents are increasingly used to automate research and development tasks, yet existing benchmarks typically evaluate them on prescribed workflows or narrow action spaces.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce InferenceBench, where an agent must deploy an OpenAI-compatible inference server and optimize the speed of LLM inference.

**证据证明什么。** Overall, InferenceBench reflects the ability of agents to operate in an open-ended AI engineering setting, where memorized solutions lead to limited improvements.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20468v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20468v1#S2 — 2 Related Works。Evaluation：https://arxiv.org/html/2607.20468v1#A1 — Appendix A Full Benchmark Specification and Environment; https://arxiv.org/html/2607.20468v1#A4 — Appendix D Full Results and Cost。Limitations / counterevidence：https://arxiv.org/html/2607.20468v1#S6 — 6 Discussion and Conclusion; https://arxiv.org/html/2607.20468v1#A5 — Appendix E Behavioral Metrics and Failure Modes。

**Artifact boundary。** Exact v1 links https://github.com/aisa-group/InferenceBench, https://opencode.ai/, https://code.claude.com/docs; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20468:end -->

<!-- review:SF-2026-ARXIV-2607-20473:start -->
### Incomplete Prompt Jailbreaks in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-20473:start -->Large language models (LLMs) are increasingly released as open-weight models with safeguards against harmful requests. Nevertheless, sentence completion remains vulnerable to incomplete harmful prompts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20473:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) are increasingly released as open-weight models with safeguards against harmful requests.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We analyze diverse attractor types associated with incomplete sentence continuation and show that LLMs systematically delay refusal until sentence termination.

**证据证明什么。** We analyze diverse attractor types associated with incomplete sentence continuation and show that LLMs systematically delay refusal until sentence termination.

**证据没有证明什么。** We further show that refusal tuning based on attractors and refusal phrases does not reliably generalize well. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20473v1#A2.SS2 — B.2 Target Models and Chat Template; https://arxiv.org/html/2607.20473v1#A2.SS6 — B.6 Base Model Behavior Under Complete Prompts。Evaluation：https://arxiv.org/html/2607.20473v1#A2 — Appendix B IPJ Attack Results; https://arxiv.org/html/2607.20473v1#A2.SS1 — B.1 Evaluation Prompt。Limitations / counterevidence：https://arxiv.org/html/2607.20473v1#S6 — 6 Discussion; https://arxiv.org/html/2607.20473v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/leo-bjpark/incomplete-prompt-jailbreak, https://github.com/yeonjea/incomplete-prompt-jailbreaks, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：We further show that refusal tuning based on attractors and refusal phrases does not reliably generalize well.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20473:end -->

<!-- review:SF-2026-ARXIV-2607-20475:start -->
### SonicSampler: Unified Tile-Aware Kernels for LLM Sampling and Speculative Verification

<!-- claim:SF-2026-ARXIV-2607-20475:start -->Sampling in LLM inference comprises a combinatorial set of logit processing, token selection, and verification operations for speculative decoding. However, existing implementations either accelerate only subsets of this pipeline, rely on multiple kernel launches, or assume homogeneous sampling behavior across a batch, limiting support for dynamic serving workloads and preventing efficient CUDA Graph execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20475:end -->

**为什么进入候选分母。** 摘要首要问题为“Sampling in LLM inference comprises a combinatorial set of logit processing, token selection, and verification operations for speculative decoding.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present $\textbf{SonicSampler}$, a unified suite of tile-aware Triton kernels that vertically fuses the complete sampling pipeline into a fixed, workload-aware execution model.

**证据证明什么。** Across heterogeneous speculative decoding workloads, SonicSampler achieves up to $\textbf{16x speedup}$ over state-of-the-art baselines while preserving flexible batched execution.

**证据没有证明什么。** Future work includes extending to beam search and deeper integration with upstream and downstream components. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20475v1#A5 — Appendix E Supplementary Algorithms; https://arxiv.org/html/2607.20475v1#A6 — Appendix F Baseline Implementation Details。Evaluation：https://arxiv.org/html/2607.20475v1#A7 — Appendix G Additional Top- Results; https://arxiv.org/html/2607.20475v1#A8 — Appendix H Additional Accuracy Results。Limitations / counterevidence：https://arxiv.org/html/2607.20475v1#S5 — 5 Conclusion and Future Directions。

**Artifact boundary。** Exact v1 links https://github.com/modular/modular, https://github.com/NVIDIA/TensorRT-LLM, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Future work includes extending to beam search and deeper integration with upstream and downstream components.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-DECODE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20475:end -->

<!-- review:SF-2026-ARXIV-2607-20478:start -->
### Verifier-First Evaluation of Agentic LLMs for Infrastructure-as-Code Generation

<!-- claim:SF-2026-ARXIV-2607-20478:start -->Infrastructure-as-Code (IaC) generation from natural language requires satisfying provider schemas, dependency planning, and organizational policy constraints, not merely producing syntactically plausible configurations. We present a verifier-first empirical study of seven agentic strategies for Terraform generation evaluated on IaC-Eval v2, a modernized 186-task AWS/Terraform benchmark with Rego v1 intent policies. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20478:end -->

**为什么进入候选分母。** 摘要首要问题为“Infrastructure-as-Code (IaC) generation from natural language requires satisfying provider schemas, dependency planning, and organizational policy constraints, not merely producing syntactically plausible configurations.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present a verifier-first empirical study of seven agentic strategies for Terraform generation evaluated on IaC-Eval v2, a modernized 186-task AWS/Terraform benchmark with Rego v1 intent policies.

**证据证明什么。** Our evaluation separates failures into three verifier stages (terraform validate, terraform plan, opa eval) and applies McNemar's test with Wilson confidence intervals on all pairwise comparisons (n=186, alpha=0.05).

**证据没有证明什么。** Active MCP raises GPT-4o from 41.4% to 70.4% (+29.0 pp), reducing OPA_FAIL to only 9 tasks (4.8%). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20478v1#A4 — Appendix D Statistical Methods; https://arxiv.org/html/2607.20478v1#S3 — 3 Benchmark and Methodology。Evaluation：https://arxiv.org/html/2607.20478v1#S2.SS1 — 2.1 IaC Benchmarks and Evaluation; https://arxiv.org/html/2607.20478v1#S2.SS5 — 2.5 Agentic Evaluation and Observability。Limitations / counterevidence：https://arxiv.org/html/2607.20478v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.20478v1#S4.SS2 — 4.2 RQ1: Active Retrieval Reduces Schema Failures。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Active MCP raises GPT-4o from 41.4% to 70.4% (+29.0 pp), reducing OPA_FAIL to only 9 tasks (4.8%).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20478:end -->

<!-- review:SF-2026-ARXIV-2607-20481:start -->
### Routing Without Training: Controllable-Ratio LLM Offloading via Reliability Gating

<!-- claim:SF-2026-ARXIV-2607-20481:start -->Local-cloud collaboration is a practical way to deploy large language models under resource constraints, but existing methods often rely on trained routers or collaboration-aware finetuning that tie routing behavior to a particular operating regime. In this work, we show that such training may be unnecessary: the local model's own inference-time agreement across sampled responses already provides a strong signal for deciding when to trust local execution and when to offload to a stronger cloud model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20481:end -->

**为什么进入候选分母。** 摘要首要问题为“Local-cloud collaboration is a practical way to deploy large language models under resource constraints, but existing methods often rely on trained routers or collaboration-aware finetuning that tie routing behavior to a particular operating regime.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We propose CARGO, a training-free routing framework that estimates this agreement through prompt-varied sampling, applies Bayesian early stopping for sample-efficient uncertainty control, and supports arbitrary target collaboration ratios through lightweight deployment-time calibration.

**证据证明什么。** These results suggest that effective and adaptable local-cloud collaboration can emerge directly from the local model's intrinsic response behavior, without requiring an additional trained router.

**证据没有证明什么。** 5 Conclusion, Future Work, and Limitations We developed CARGO, a training-free routing framework for local-cloud collaboration that uses prompt-varied agreement for reliability estimation, Bayesian early stopping for sample efficiency, and lightweight calibration for controllable collaboration ratios. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20481v1#A4 — Appendix D Prompt Design for Evaluation Signals。Evaluation：https://arxiv.org/html/2607.20481v1#S4.SS1 — 4.1 Experimental Results; https://arxiv.org/html/2607.20481v1#A3 — Appendix C Additional Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20481v1#S5 — 5 Conclusion, Future Work, and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：5 Conclusion, Future Work, and Limitations We developed CARGO, a training-free routing framework for local-cloud collaboration that uses prompt-varied agreement for reliability estimation, Bayesian early stopping for sample efficiency, and lightweight calibration for controllable collaboration ratios.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20481:end -->

<!-- review:SF-2026-ARXIV-2607-20483:start -->
### Tractable Hierarchical Control of Autoregressive Language Models

<!-- claim:SF-2026-ARXIV-2607-20483:start -->Constraining the generation of autoregressive large language models (LLMs) is an important component of integrating language models into formal systems. In the generation of code and data for tasks like program synthesis, ensuring that language models produce syntactically valid output is a prerequisite for processing such output. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20483:end -->

**为什么进入候选分母。** 摘要首要问题为“Constraining the generation of autoregressive large language models (LLMs) is an important component of integrating language models into formal systems.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Constraining the generation of autoregressive large language models (LLMs) is an important component of integrating language models into formal systems.

**证据证明什么。** This paper demonstrates that the satisfaction of any $LR(k)$ grammar of finite duration can be calculated in polynomial time, an improvement over the exponential time of applying previous methods to such grammars.

**证据没有证明什么。** The extension of this work to other formal automata is an open area of future research. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20483v1#A1 — Appendix A Dynamic Programming Algorithms; https://arxiv.org/html/2607.20483v1#A1.SS1 — A.1 Algorithm 1。Evaluation：https://arxiv.org/html/2607.20483v1#S6 — 6 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20483v1#S8 — 8 Future areas of research; https://arxiv.org/html/2607.20483v1#S8.SS2 — 8.2 Other future areas of research。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The extension of this work to other formal automata is an open area of future research.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SAMPLING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20483:end -->

<!-- review:SF-2026-ARXIV-2607-20488:start -->
### Autonomous Topology Mutation: Safe Runtime Restructuring for Multi-Agent LLM Systems with Capability, State, and Shadow Invariants

<!-- claim:SF-2026-ARXIV-2607-20488:start -->Multi-agent LLM frameworks typically fix their team topology at boot time. When an individual agent becomes overloaded at runtime, for example by mixing too many action categories, accumulating tool errors, or queueing behind too many calls, the system has no mechanism to restructure itself. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20488:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent LLM frameworks typically fix their team topology at boot time.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce Autonomous Topology Mutation (ATM), a runtime team-mutation mechanism for multi-agent LLM frameworks.

**证据证明什么。** The full rail-and-distillation system reduces detected high-privacy memory exposure under a regex classifier from 2.0 to 0.0 events per task while preserving task quality.

**证据没有证明什么。** The controlled-telemetry signal ablation (Section 6.5 ) confirms that each of the six signals contributes independent information, with (role entropy) carrying the largest aggregate weight. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20488v1#S3 — 3. ATM System Architecture; https://arxiv.org/html/2607.20488v1#S4 — 4. Algorithms。Evaluation：https://arxiv.org/html/2607.20488v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.20488v1#S6.SS2 — 6.2. Main Results: Success and Exposure (Q1, Q2)。Limitations / counterevidence：https://arxiv.org/html/2607.20488v1#S5.SS2 — 5.2. Failure Modes and Bounded Damage; https://arxiv.org/html/2607.20488v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/sidikbro/jiuwen_atm, https://github.com/crewAIInc/crewAI, https://github.com/openJiuwen-ai/jiuwenswarm; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The controlled-telemetry signal ablation (Section 6.5 ) confirms that each of the six signals contributes independent information, with (role entropy) carrying the largest aggregate weight.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20488:end -->

<!-- review:SF-2026-ARXIV-2607-20490:start -->
### CRAWO: Custom Resources for Adaptive Workload Orchestration

<!-- claim:SF-2026-ARXIV-2607-20490:start -->Edge Intelligence has emerged as a key paradigm for enabling real-time applications in smart cities by shifting computation from centralized cloud data centers to the network edge, thereby reducing latency and bandwidth consumption. However, deploying Artificial Intelligence (AI) pipelines across heterogeneous edge infrastructures remains challenging due to the wide range of device capabilities, from low-power microcontrollers to accelerator-equipped systems. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20490:end -->

**为什么进入候选分母。** 摘要首要问题为“Edge Intelligence has emerged as a key paradigm for enabling real-time applications in smart cities by shifting computation from centralized cloud data centers to the network edge, thereby reducing latency and bandwidth consumption.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** The framework incorporates a hardware-aware allocator with a pluggable multi-criteria decision layer that leverages real-time infrastructure metrics to enable adaptive workload placement.

**证据证明什么。** Evaluation in a vehicle surveillance scenario using license plate recognition demonstrates improved workload distribution and reduced reliance on centralized cloud processing in latency-sensitive environments.

**证据没有证明什么。** 8 Conclusion The expansion of smart city applications, particularly real-time AI video processing, exposes the critical limitations of cloud-only architectures regarding prohibitive latency and significant pressure on network bandwidth. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20490v1#S4.SS1 — 4.1 Architecture; https://arxiv.org/html/2607.20490v1#S7.SS3 — 7.3 Experimental design。Evaluation：https://arxiv.org/html/2607.20490v1#S7 — 7 Evaluation; https://arxiv.org/html/2607.20490v1#S7.SS1 — 7.1 Evaluation metrics。Limitations / counterevidence：https://arxiv.org/html/2607.20490v1#S7.SS6 — 7.6 Discussion; https://arxiv.org/html/2607.20490v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/kubernetes-sigs/kubebuilder, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：8 Conclusion The expansion of smart city applications, particularly real-time AI video processing, exposes the critical limitations of cloud-only architectures regarding prohibitive latency and significant pressure on network bandwidth.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-FOUNDATIONS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20490:end -->

<!-- review:SF-2026-ARXIV-2607-20495:start -->
### Workload-Aware Caching for Multi-Agent Systems

<!-- claim:SF-2026-ARXIV-2607-20495:start -->Multi-agent systems decompose complex tasks into directed acyclic graphs (DAGs) of specialized agent executions, creating natural opportunities for caching intermediate results across queries. However, existing cache eviction policies treat all cached entries uniformly based on access history, ignoring structural and workload signals uniquely available in agentic execution environments. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20495:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent systems decompose complex tasks into directed acyclic graphs (DAGs) of specialized agent executions, creating natural opportunities for caching intermediate results across queries.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We further show that workload-aware content caching is complementary to other agentic system optimization methods, including plan-level caching and parallel agent execution, with each technique targeting a distinct efficiency bottleneck in multi-agent pipelines.

**证据证明什么。** Evaluated across three multi-agent benchmarks spanning diverse reuse regimes, our policy reduces latency by up to 64.7% relative to the uncached baseline and achieves on average a 31.1% latency reduction over the next best finite-capacity baseline, while approaching the performance of an unbounded cache and maintaining accuracy on par with or exceeding all competing finite-capacity methods.

**证据没有证明什么。** Another interesting future direction is cache-aware planning, where the planning agent is informed of the current cache state when generating execution plans. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20495v1#S2.SS3 — II-C Multi-Agent System Orchestration and Optimization; https://arxiv.org/html/2607.20495v1#S3 — III Design。Evaluation：https://arxiv.org/html/2607.20495v1#S4 — IV Evaluation; https://arxiv.org/html/2607.20495v1#S4.SS1 — IV-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.20495v1#S5 — V Limitations and Future Work; https://arxiv.org/html/2607.20495v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Another interesting future direction is cache-aware planning, where the planning agent is informed of the current cache state when generating execution plans.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`layering_dependency`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20495:end -->

<!-- review:SF-2026-ARXIV-2607-20501:start -->
### MKEvolve: A Modular Multi-Agent Framework for Kernel Code Generation

<!-- claim:SF-2026-ARXIV-2607-20501:start -->Despite rapid progress in LLM-based code generation, writing correct and performant kernels for hardware accelerators remains a key bottleneck in scaling modern ML workloads. We present MKEvolve (Modular Kernel Evolve), a framework that iteratively co-evolves a modular decomposition of complex PyTorch modules and the LLM-generated kernel for each submodule, refining the decomposition by splitting and fusing across iterations while independently improving each subkernel via LLM-driven beam search. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20501:end -->

**为什么进入候选分母。** 摘要首要问题为“Despite rapid progress in LLM-based code generation, writing correct and performant kernels for hardware accelerators remains a key bottleneck in scaling modern ML workloads.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present MKEvolve (Modular Kernel Evolve), a framework that iteratively co-evolves a modular decomposition of complex PyTorch modules and the LLM-generated kernel for each submodule, refining the decomposition by splitting and fusing across iterations while independently improving each subkernel via LLM-driven beam search.

**证据证明什么。** Experiments with Triton on KernelBench L2 and L3, spanning multi-operator sequences and full model architectures, show that MKEvolve improves both correctness and speedup over end-to-end direct synthesis baselines while reducing LLM token usage by up to 35%.

**证据没有证明什么。** 5 Conclusion We introduced MKEvolve , a modular kernel code generation framework that iteratively decomposes complex PyTorch modules into subproblems, independently solves them, and composes the resulting subkernels into a complete, end-to-end solution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20501v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.20501v1#A1 — Appendix A Additional Experiment Details; https://arxiv.org/html/2607.20501v1#A3 — Appendix C Example Second Seed Results。Limitations / counterevidence：https://arxiv.org/html/2607.20501v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/amazon-science/ModularKernelEvolution, https://huggingface.co/facebook/KernelLLM, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：5 Conclusion We introduced MKEvolve , a modular kernel code generation framework that iteratively decomposes complex PyTorch modules into subproblems, independently solves them, and composes the resulting subkernels into a complete, end-to-end solution.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20501:end -->

<!-- review:SF-2026-ARXIV-2607-20507:start -->
### CacheSpec: Finding the Sweet Spot for Small Models in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-20507:start -->Large language models (LLMs) are increasingly used for program-aided reasoning, agentic decision making, and structured task execution, but these settings often incur substantial inference cost. Many such requests share similar computational structures while differing in variables, constraints, or contexts, creating opportunities for program-level caching. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20507:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) are increasingly used for program-aided reasoning, agentic decision making, and structured task execution, but these settings often incur substantial inference cost.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose CacheSpec, an inference optimization framework centered on reusable program caches.

**证据证明什么。** Experiments on shopping-style request datasets, WebShop, Formula, and CodeTAT-QA show that CacheSpec reduces inference latency and improves effective cache reuse while preserving comparable or better task quality than existing caching and generation baselines, achieving up to about 3.1$\times$ latency speedup; in parallel serving experiments, it improves throughput by about 2.8$\times$ over PoT-style methods.

**证据没有证明什么。** Overall, our findings suggest that the sweet spot for small models in large-model inference systems lies not in solving complex tasks independently, but in performing lightweight, structured, and verifiable auxiliary operations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20507v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.20507v1#A1.SS7 — A.7 Detailed Main Result Analysis; https://arxiv.org/html/2607.20507v1#A1 — Appendix A Additional Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.20507v1#A1.SS2 — A.2 Cache Generation and Failure Handling Details; https://arxiv.org/html/2607.20507v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Overall, our findings suggest that the sweet spot for small models in large-model inference systems lies not in solving complex tasks independently, but in performing lightweight, structured, and verifiable auxiliary operations.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20507:end -->

<!-- review:SF-2026-ARXIV-2607-20512:start -->
### The Active Ingredient in Muon's Grokking

<!-- claim:SF-2026-ARXIV-2607-20512:start -->The Muon optimizer reaches the grokking threshold on modular arithmetic faster than AdamW. Prior work attributes this to "spectral-norm constraints plus orthogonalized momentum" but does not isolate which mechanism matters. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20512:end -->

**为什么进入候选分母。** 摘要首要问题为“The Muon optimizer reaches the grokking threshold on modular arithmetic faster than AdamW.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** A methodological thread runs throughout: under a stability-aware metric, "faster" claims about grokking optimizers can invert, so we report both first-crossing and sustained-grok times.

**证据证明什么。** We also show spectral scaling can be dropped at no measured cost.

**证据没有证明什么。** Spectral scaling, however, can be dropped for free. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20512v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20512v1#S1.SS0.SSS0.Px1 — Contributions.。Evaluation：https://arxiv.org/html/2607.20512v1#S3 — 3 Ablation: Which Ingredient?。Limitations / counterevidence：https://arxiv.org/html/2607.20512v1#S6 — 6 Limitations and Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/louiswang524/muon-grokking-frontier, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Spectral scaling, however, can be dropped for free.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20512:end -->

<!-- review:SF-2026-ARXIV-2607-20518:start -->
### CANN Bench: Benchmarking Agent Generated Kernels against Real NPU and Algorithmic Limits

<!-- claim:SF-2026-ARXIV-2607-20518:start -->AI agents are now capable of writing, compiling, and iteratively optimizing low-level operator kernels on different hardware platforms. Existing benchmarks, however, focus almost exclusively on CUDA and Triton, leaving hardware ecosystems with less-exposed programming models without a common evaluation baseline. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20518:end -->

**为什么进入候选分母。** 摘要首要问题为“AI agents are now capable of writing, compiling, and iteratively optimizing low-level operator kernels on different hardware platforms.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present CANN Bench, an open benchmark for AI-generated operator code on Huawei's Ascend NPU.

**证据证明什么。** CANN Bench is versioned within the official CANN repository and is designed for long-term community co-construction, providing the Ascend ecosystem with a quantitative, reproducible, and sustainably maintained yardstick for AI operator-authoring capability.

**证据没有证明什么。** Performance is graded between a PyTorch-on-Ascend baseline and an analytically derived per-case HAP limit, so absolute scores carry a hardware-grounded meaning rather than only a relative ranking. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20518v1#S2.SS3 — 2.3 Test-Case Design Methodology; https://arxiv.org/html/2607.20518v1#S2.SS1 — 2.1 Design Principles。Evaluation：https://arxiv.org/html/2607.20518v1#S1.SS1 — 1.1 Why an Ascend-Oriented Benchmark Now; https://arxiv.org/html/2607.20518v1#S1.SS2 — 1.2 Six Criteria for an Ascend-Oriented Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.20518v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://gitcode.com/cann/cann-bench, https://gitcode.com/cann/opbase, https://github.com/ScalingIntelligence/KernelBench/issues/74; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Performance is graded between a PyTorch-on-Ascend baseline and an analytically derived per-case HAP limit, so absolute scores carry a hardware-grounded meaning rather than only a relative ranking.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20518:end -->

<!-- review:SF-2026-ARXIV-2607-20524:start -->
### Attention Degradation, Function Token Anchoring, and the Limits of Attention-Based Intervention in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-20524:start -->Mean cross-positional attention degradation is widely reported in transformer interpretability, yet whether it causally limits contextual retrieval remains untested. We present six coordinated experiments across GPT-2, LLaMA-3.2-1B/3B, OPT-1.3B, and distilgpt2. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20524:end -->

**为什么进入候选分母。** 摘要首要问题为“Mean cross-positional attention degradation is widely reported in transformer interpretability, yet whether it causally limits contextual retrieval remains untested.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present six coordinated experiments across GPT-2, LLaMA-3.2-1B/3B, OPT-1.3B, and distilgpt2.

**证据证明什么。** Multi-fact retrieval probes further show that degradation rate does not predict retrieval accuracy across models.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20524v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20524v1#S5.SS1 — 5.1 The Architecture-Dependent Relay Chain。Evaluation：https://arxiv.org/html/2607.20524v1#A1 — Appendix A Full Experiment 1 Degradation Tables; https://arxiv.org/html/2607.20524v1#S3.SS4 — 3.4 Experiment 1: Baseline Attention Degradation。Limitations / counterevidence：https://arxiv.org/html/2607.20524v1#S5 — 5 Discussion; https://arxiv.org/html/2607.20524v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SELF-ATTENTION`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20524:end -->

<!-- review:SF-2026-ARXIV-2607-20526:start -->
### ConfidenceBench: Evaluating Confidence Calibration in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-20526:start -->Large language models (LLMs) are increasingly deployed in settings where fluent but incorrect answers can be costly. In these settings, accuracy alone is insufficient: models must also know when they are likely to be wrong. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20526:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) are increasingly deployed in settings where fluent but incorrect answers can be costly.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Confidence is elicited via prompting, requiring no access to model logits and making the framework applicable to both closed-source and open-source systems.

**证据证明什么。** These results show that verbalized confidence calibration is a distinct and practically important axis of LLM reliability, complementary to standard accuracy-based evaluation.

**证据没有证明什么。** Reasoning effort and model scale generally improve calibration, but newer models are not always better calibrated. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20526v1#S3 — 3 Benchmark Design and Methodology。Evaluation：https://arxiv.org/html/2607.20526v1#A1 — Appendix A Full Results and Run-to-Run Stability; https://arxiv.org/html/2607.20526v1#S3 — 3 Benchmark Design and Methodology。Limitations / counterevidence：https://arxiv.org/html/2607.20526v1#S6 — 6 Discussion and Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Reasoning effort and model scale generally improve calibration, but newer models are not always better calibrated.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20526:end -->

<!-- review:SF-2026-ARXIV-2607-20527:start -->
### Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis

<!-- claim:SF-2026-ARXIV-2607-20527:start -->Agentic LLM systems such as OpenScholar and PaperQA2 read the scientific literature and return cited answers, and both they and their benchmarks already check whether those citations hold, with a fixed attribution model or human graders. Neither audits the reliability of that check itself. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20527:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic LLM systems such as OpenScholar and PaperQA2 read the scientific literature and return cited answers, and both they and their benchmarks already check whether those citations hold, with a fixed attribution model or human graders.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present a gold-anchored evaluation protocol and a deployable guard that make this behavior measurable and bounded.

**证据证明什么。** We show it is not reliable, and that this matters.

**证据没有证明什么。** Limitations The unsupported-citation rate is relative to a verifier’s operating point, so our numbers and any others in this literature are interpretable only together with the verifier and protocol that produced them. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20527v1#S2.SS2 — 2.2. Evaluating and benchmarking agentic systems; https://arxiv.org/html/2607.20527v1#S4 — 4. Method。Evaluation：https://arxiv.org/html/2607.20527v1#A3 — Appendix S3 Conformal calibration-size ablation; https://arxiv.org/html/2607.20527v1#S2.SS2 — 2.2. Evaluating and benchmarking agentic systems。Limitations / counterevidence：https://arxiv.org/html/2607.20527v1#S6 — 6. Discussion; https://arxiv.org/html/2607.20527v1#S7 — 7. Limitations。

**Artifact boundary。** Exact v1 links https://github.com/GooTec/citation-guard, https://dx.doi.org/10.18653/v1/2024.eacl-demo.16, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Limitations The unsupported-citation rate is relative to a verifier’s operating point, so our numbers and any others in this literature are interpretable only together with the verifier and protocol that produced them.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20527:end -->

<!-- review:SF-2026-ARXIV-2607-20531:start -->
### DynamicMCPBench: A Trace-Grounded, Effect-Scored Benchmark for LLM Agents over Live MCP Servers

<!-- claim:SF-2026-ARXIV-2607-20531:start -->Large language model (LLM) agents are increasingly deployed over Model Context Protocol (MCP) servers, yet the benchmarks used to evaluate them score the final answer or a fixed "ground-truth" list of tools, both of which are fragile once the underlying data is live and stateful. We present DynamicMCPBench, a reusable framework rather than a fixed dataset. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20531:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents are increasingly deployed over Model Context Protocol (MCP) servers, yet the benchmarks used to evaluate them score the final answer or a fixed "ground-truth" list of tools, both of which are fragile once the underlying data is live and stateful.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present DynamicMCPBench, a reusable framework rather than a fixed dataset.

**证据证明什么。** To show what the framework reveals, we run it at scale: 24 models over 121 servers and 750 tasks spread evenly over 15 task categories (50 each), where each category targets a distinct tool-use challenge of the generated questions.

**证据没有证明什么。** Because every tool in a task was actually used to reach its goal, an “unnecessary tool” cannot appear, and because scoring reads effects rather than the reply, the benchmark survives live, changing data. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20531v1#A4 — Appendix D Framework Configuration; https://arxiv.org/html/2607.20531v1#S3.SS1 — 3.1 Design principles。Evaluation：https://arxiv.org/html/2607.20531v1#S4 — 4 Results & Analysis; https://arxiv.org/html/2607.20531v1#A11 — Appendix K Failure Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.20531v1#A11 — Appendix K Failure Analysis; https://arxiv.org/html/2607.20531v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/blog/smollm3, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Because every tool in a task was actually used to reach its goal, an “unnecessary tool” cannot appear, and because scoring reads effects rather than the reply, the benchmark survives live, changing data.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MCP`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20531:end -->

<!-- review:SF-2026-ARXIV-2607-20536:start -->
### AppWorld-UL: Benchmarking Diverse Agent-User Interactions for Tool-Use

<!-- claim:SF-2026-ARXIV-2607-20536:start -->Tool-use agents that address day-to-day digital tasks such as ordering groceries must not only operate applications, but also interact with the user, e.g., to ask clarification questions, prompt for confirmation, and inform the user when the instruction is infeasible. However, current benchmarks for evaluating agent-user interactions do not capture the diversity of such interactions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20536:end -->

**为什么进入候选分母。** 摘要首要问题为“Tool-use agents that address day-to-day digital tasks such as ordering groceries must not only operate applications, but also interact with the user, e.g., to ask clarification questions, prompt for confirmation, and inform the user when the instruction is infeasible.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Building upon the AppWorld framework with 9 popular simulated apps like Amazon and Spotify, we systematically modify original tasks to introduce ambiguities and constraints that necessitate various types of agent-user interaction.

**证据证明什么。** This demonstrates the benchmark's difficulty and its potential to advance research on user-in-the-loop tool-use agents.

**证据没有证明什么。** Experiments with state-of-the-art LLM agents reveal substantial room for improvement with the best system achieving only 48.6% success on the task level metric and only 30.2% on the scenario level metric. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20536v1#A2 — Appendix B Interaction Metric Design; https://arxiv.org/html/2607.20536v1#S4.SS2 — 4.2 Simulated User Design。Evaluation：https://arxiv.org/html/2607.20536v1#A1 — Appendix A Experiment Results; https://arxiv.org/html/2607.20536v1#A3 — Appendix C Benchmark Task Examples。Limitations / counterevidence：https://arxiv.org/html/2607.20536v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Experiments with state-of-the-art LLM agents reveal substantial room for improvement with the best system achieving only 48.6% success on the task level metric and only 30.2% on the scenario level metric.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20536:end -->

<!-- review:SF-2026-ARXIV-2607-20538:start -->
### Codec-Gauge: Learning Compression-Friendly Gauges for Transformer KV Caches

<!-- claim:SF-2026-ARXIV-2607-20538:start -->Long-context Transformer inference increasingly relies on KV-cache compression or quantization. Prior rotation and transform-coding results suggest that the channel basis of each key/value vector affects how faithfully a fixed backend preserves model behavior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20538:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-context Transformer inference increasingly relies on KV-cache compression or quantization.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We introduce Codec-Gauge, a post-training cache-coordinate layer that learns small orthogonal channel transforms around existing compression and quantization backends.

**证据证明什么。** Across six models at $3$, $4$, and $6$ bits/value, learned gauges reduce zfp KL divergence by $44.0\%$ on average relative to raw coordinates and outperform random, Hadamard, DCT, and PCA/KLT controls.

**证据没有证明什么。** The broader conclusion is that KV-cache compressibility is not only a property of the backend or the checkpoint in its original basis: the coordinates exposed to a codec or quantizer are an actionable variable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20538v1#Sx4 — Method and Evaluation Design; https://arxiv.org/html/2607.20538v1#Sx4.SSx4 — Evaluation Design。Evaluation：https://arxiv.org/html/2607.20538v1#Sx4 — Method and Evaluation Design; https://arxiv.org/html/2607.20538v1#Sx4.SSx4 — Evaluation Design。Limitations / counterevidence：https://arxiv.org/html/2607.20538v1#Sx6 — Discussion and Limitations; https://arxiv.org/html/2607.20538v1#Sx7 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The broader conclusion is that KV-cache compressibility is not only a property of the backend or the checkpoint in its original basis: the coordinates exposed to a codec or quantizer are an actionable variable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20538:end -->

<!-- review:SF-2026-ARXIV-2607-20543:start -->
### When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k Inversion

<!-- claim:SF-2026-ARXIV-2607-20543:start -->Reinforcement learning with verifiable rewards (RLVR) can improve one-sample accuracy while making a model worse under repeated sampling. We study this pass@k inversion: after training, the policy may solve fewer distinct problems than its base model at large $k$. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20543:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning with verifiable rewards (RLVR) can improve one-sample accuracy while making a model worse under repeated sampling.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We study this pass@k inversion: after training, the policy may solve fewer distinct problems than its base model at large $k$.

**证据证明什么。** Reinforcement learning with verifiable rewards (RLVR) can improve one-sample accuracy while making a model worse under repeated sampling.

**证据没有证明什么。** 6 uses only base-rollout rewards for the corresponding training prompt. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20543v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20543v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.20543v1#S7 — 7 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20543v1#S4 — 4 Pass@ Inversion Is a Boundary-Regime Failure; https://arxiv.org/html/2607.20543v1#S8 — 8 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：6 uses only base-rollout rewards for the corresponding training prompt.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20543:end -->

<!-- review:SF-2026-ARXIV-2607-20548:start -->
### SOAP, Muon, and Beyond: Pushing LLM Pretraining Scales

<!-- claim:SF-2026-ARXIV-2607-20548:start -->Higher-order optimizers such as Muon and SOAP offer faster convergence than AdamW, but their computational cost and numerical stability challenges have limited adoption at scale. In this work, we adapt and enhance preconditioned gradient methods to overcome the practical challenges of large-scale LLM pretraining. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20548:end -->

**为什么进入候选分母。** 摘要首要问题为“Higher-order optimizers such as Muon and SOAP offer faster convergence than AdamW, but their computational cost and numerical stability challenges have limited adoption at scale.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To enable efficient training at large scale, we introduce a layer-wise distributed optimizer compatible with Megatron-LM.

**证据证明什么。** Additionally, we identify and build specific system-level improvements to further accelerate our layer-wise implementation.

**证据没有证明什么。** Furthermore, the KL-SOAP variant emerged as the most effective approach overall; therefore, in scenarios where memory footprint is not a limiting factor, we recommend KL-SOAP over Muon. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20548v1#S4.SS2 — 4.2 Systems to enable higher-order optimizers; https://arxiv.org/html/2607.20548v1#S3.SS1 — 3.1 Batch Size Scaling for Mixture-of-Experts Models。Evaluation：https://arxiv.org/html/2607.20548v1#S5 — 5 Pretraining Experiments with Muon and SOAP。Limitations / counterevidence：https://arxiv.org/html/2607.20548v1#S7 — 7 Conclusions and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/nikhilvyas/SOAP, https://github.com/KellerJordan/cifar10-airbench/tree/master, https://github.com/NVIDIA/Megatron-LM/blob/main/megatron/core/optimizer/layer_wise_optimizer.py; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Furthermore, the KL-SOAP variant emerged as the most effective approach overall; therefore, in scenarios where memory footprint is not a limiting factor, we recommend KL-SOAP over Muon.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20548:end -->

<!-- review:SF-2026-ARXIV-2607-20553:start -->
### CMI-Mem: Toward Generalizable Long-Term Memory Management via CMI-Augmented Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-20553:start -->Memory Manager models are pivotal in agent systems. Existing reinforcement-learning methods commonly use LLM-judged synthetic question-answer (QA) pairs: this provides useful downstream task grounding, but values memory through a sampled query distribution and a fixed reader. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20553:end -->

**为什么进入候选分母。** 摘要首要问题为“Memory Manager models are pivotal in agent systems.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Memory Manager models are pivotal in agent systems.

**证据证明什么。** Experiments demonstrate improved transfer across memory-use scenarios, together with more efficient training and inference from the per-operation CMI signal.

**证据没有证明什么。** Due to the scarcity of direct metrics for evaluating memory quality independent of QA, the full potential of our method cannot be adequately demonstrated. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20553v1#A7.SS5 — G.5 Action Space Design Rationale; https://arxiv.org/html/2607.20553v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.20553v1#S4.SS2 — 4.2 Results and Analysis; https://arxiv.org/html/2607.20553v1#S4.SS3 — 4.3 Ablation Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20553v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.20553v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Wyb0627/CMIMem, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Due to the scarcity of direct metrics for evaluating memory quality independent of QA, the full potential of our method cannot be adequately demonstrated.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20553:end -->

<!-- review:SF-2026-ARXIV-2607-20558:start -->
### StabilityBench: Benchmarking Instability in LLMs

<!-- claim:SF-2026-ARXIV-2607-20558:start -->AI Assistants are increasingly deployed in high-stakes settings, such as healthcare or government services. Yet their real-world behavior remains poorly understood due to strong context dependence. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20558:end -->

**为什么进入候选分母。** 摘要首要问题为“AI Assistants are increasingly deployed in high-stakes settings, such as healthcare or government services.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose StabilityBench, a principled, general and model-agnostic benchmark operator that transforms single-turn benchmark queries into multi-turn interaction histories.

**证据证明什么。** Our results show that model performance is consistently unstable under these injections, with considerable performance degradations on three out of four benchmarks studied.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20558v1#S2.SS1 — 2.1 Frontier Evaluation Methods; https://arxiv.org/html/2607.20558v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.20558v1#A1 — Appendix A Benchmarks.; https://arxiv.org/html/2607.20558v1#A5 — Appendix E Supplemental Results。Limitations / counterevidence：https://arxiv.org/html/2607.20558v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ekmpa/StabilityBench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20558:end -->

<!-- review:SF-2026-ARXIV-2607-20560:start -->
### Chronofy: A Temporal-Logical Decay Architecture for Information Validity in Time-Aware Retrieval-Augmented Generation

<!-- claim:SF-2026-ARXIV-2607-20560:start -->Retrieval-Augmented Generation (RAG) systems retrieve and integrate external knowledge to ground large language model (LLM) outputs. However, current RAG architectures treat all retrieved facts as equally valid regardless of temporal provenance, leading to temporal hallucination, where plausible but obsolete facts corrupt the output. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20560:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-Augmented Generation (RAG) systems retrieve and integrate external knowledge to ground large language model (LLM) outputs.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present Chronofy, a three-layer neuro-symbolic framework implementing the Temporal-Logical Decay Architecture (TLDA) that embeds temporal validity directly into the representation, retrieval, and reasoning layers of RAG systems.

**证据证明什么。** We evaluate Chronofy on temporal knowledge graph forecasting benchmarks, the TimE temporal QA benchmark, and a domain-specific sensitivity analysis, demonstrating that explicit temporal decay modeling improves retrieval precision, reduces temporal hallucination, and enables principled data re-acquisition triggers when temporal context is insufficient.

**证据没有证明什么。** The exponential form cannot capture non-monotonic lifecycles or sudden regime shifts; skew-normal [ 7 ] or non-parametric [ 17 ] alternatives address these at the cost of computational overhead. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20560v1#S3 — III The Chronofy Framework。Evaluation：https://arxiv.org/html/2607.20560v1#S4 — IV Experimental Evaluation; https://arxiv.org/html/2607.20560v1#S4.SS4 — IV-D Experiment 4: Clinical Sensitivity Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.20560v1#S5 — V Discussion; https://arxiv.org/html/2607.20560v1#S5.SS2 — V-B Limitations。

**Artifact boundary。** Exact v1 links https://pypi.org/project/chronofy/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The exponential form cannot capture non-monotonic lifecycles or sudden regime shifts; skew-normal [ 7 ] or non-parametric [ 17 ] alternatives address these at the cost of computational overhead.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20560:end -->

<!-- review:SF-2026-ARXIV-2607-20594:start -->
### When Does Recurrence Become an Algorithm? Convergence Selection in Weight-Tied Looped Transformers

<!-- claim:SF-2026-ARXIV-2607-20594:start -->When does a weight-tied looped transformer -- one block applied T times -- implement an actual algorithm? We answer with four findings from controlled populations on group word problems. (1) The budget law: free training installs a linear computation frontier, a mechanism that solves v positions per loop, whose speed is priced by the training contract: v ~ n_train/T_train (exponent 0.98 +/- 0.04, R^2=0.99), exactly unity under T=n training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20594:end -->

**为什么进入候选分母。** 摘要首要问题为“When does a weight-tied looped transformer -- one block applied T times -- implement an actual algorithm?”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce a head instrument, the convergence-time scaling tau(n,i), validate it causally via damage cones whose slope reproduces v, and show in-distribution head measurements predict out-of-distribution fate where tail metrics do not.

**证据证明什么。** Results replicate on the public easy-to-hard benchmark.

**证据没有证明什么。** The result is a statement about optimization cost of the composition operator at , not an impossibility claim; the separation is conditional and forces only super-constant depth. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20594v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20594v1#S2 — 2 Related work。Evaluation：https://arxiv.org/html/2607.20594v1#A4 — Appendix D Training and experiment details; https://arxiv.org/html/2607.20594v1#S9 — 9 Open-benchmark validation。Limitations / counterevidence：https://arxiv.org/html/2607.20594v1#S10 — 10 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The result is a statement about optimization cost of the composition operator at , not an impossibility claim; the separation is conditional and forces only super-constant depth.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20594:end -->

<!-- review:SF-2026-ARXIV-2607-20596:start -->
### Are Single-Token Sparse Autoencoder Features Causally Necessary? Layer-Depth and SAE-Family Effects

<!-- claim:SF-2026-ARXIV-2607-20596:start -->Sparse autoencoder (SAE) features are used to interpret and steer large language models, yet nobody has tested whether a feature's causal role is stable across SAE families. Single-token features fire on one vocabulary item, so ground truth permits direct comparison. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20596:end -->

**为什么进入候选分母。** 摘要首要问题为“Sparse autoencoder (SAE) features are used to interpret and steer large language models, yet nobody has tested whether a feature's causal role is stable across SAE families.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Changing only the activation function reverses the sign of that difference, so the training recipe is the remaining candidate: cross-family claims are sensitive to training methodology, not just activation function or scale.

**证据证明什么。** Changing only the activation function reverses the sign of that difference, so the training recipe is the remaining candidate: cross-family claims are sensitive to training methodology, not just activation function or scale.

**证据没有证明什么。** Re-verify causal claims when switching SAE families: a feature’s necessity under one family cannot be assumed to transfer, even on the same base model, so steering and editing pipelines should re-run ablation checks under the family they deploy. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20596v1#A1.SS5 — A.5 Multi-Architecture Comparison; https://arxiv.org/html/2607.20596v1#S3 — 3 Methods。Evaluation：https://arxiv.org/html/2607.20596v1#A2.SS6 — B.6 Full-Layer Causal Ablation Results; https://arxiv.org/html/2607.20596v1#A1.SS2 — A.2 Expansion Factor Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.20596v1#S5 — 5 Discussion; https://arxiv.org/html/2607.20596v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/jbloomAus/SAELens, https://transformer-circuits.pub/2024/crosscoders/index.html, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Re-verify causal claims when switching SAE families: a feature’s necessity under one family cannot be assumed to transfer, even on the same base model, so steering and editing pipelines should re-run ablation checks under the family they deploy.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-REPRESENTATION`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20596:end -->

<!-- review:SF-2026-ARXIV-2607-20652:start -->
### Scaling Interpretable Transformers with Parity Bottleneck Layers

<!-- claim:SF-2026-ARXIV-2607-20652:start -->Language models are thought to exhibit the phenomenon of superposition, representing many more features than dimensions in their residual streams. Sparse autoencoders (SAEs) are designed to recover such features post-hoc, but training models that are interpretable by construction has remained impractical, as a per-layer over-complete bottleneck is prohibitively expensive in both memory and compute. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20652:end -->

**为什么进入候选分母。** 摘要首要问题为“Language models are thought to exhibit the phenomenon of superposition, representing many more features than dimensions in their residual streams.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To overcome this issue, we introduce the ParityTransformer, a GPT-2-scale architecture whose intermediate representations are efficient and wide / sparse by design.

**证据证明什么。** We see this as a step toward training models whose internal representations are interpretable by design rather than recovered post hoc.

**证据没有证明什么。** We look forward to closing the remaining gap in future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20652v1#A1.SS4 — A.4 Concrete implementation; https://arxiv.org/html/2607.20652v1#A3.SS3 — C.3 Greedy Feature Editing Algorithm。Evaluation：https://arxiv.org/html/2607.20652v1#A2.SS1 — B.1 Poisoned-Document Retrieval Experiment Details; https://arxiv.org/html/2607.20652v1#A2.SS5 — B.5 Additional Poisoned-Document Retrieval Results。Limitations / counterevidence：https://arxiv.org/html/2607.20652v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：We look forward to closing the remaining gap in future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20652:end -->

<!-- review:SF-2026-ARXIV-2607-20653:start -->
### PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics

<!-- claim:SF-2026-ARXIV-2607-20653:start -->Predicting how deformable objects evolve under robotic manipulation is a longstanding challenge. Existing approaches typically rely on per-object optimization to fit material parameters, which can be slow and cannot generalize, while end-to-end learned alternatives extrapolate poorly and often violate basic physical structure. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20653:end -->

**为什么进入候选分母。** 摘要首要问题为“Predicting how deformable objects evolve under robotic manipulation is a longstanding challenge.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present PhysCoRe, a physics-corrected residual world model that couples a differentiable Material Point Method (MPM) simulator with two feed-forward neural networks.

**证据证明什么。** Experiments on real deformable-object manipulation sequences show that PhysCoRe outperforms state-of-the-art baselines in prediction accuracy, and that its predicted confidence forms a reliable distribution across the object's geometry, providing a natural signal for future confidence-guided exploration.

**证据没有证明什么。** Compared with PhysTwin, PhysCoRe predicts future dynamics that more closely match the real observations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20653v1#A2 — Appendix B MfM Architecture and Hyperparameters; https://arxiv.org/html/2607.20653v1#A3 — Appendix C RfD Architecture and Hyperparameters。Evaluation：https://arxiv.org/html/2607.20653v1#S5 — 5 Experiments; https://arxiv.org/html/2607.20653v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.20653v1#S5.SS2 — 5.2 Future Prediction; https://arxiv.org/html/2607.20653v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Compared with PhysTwin, PhysCoRe predicts future dynamics that more closely match the real observations.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20653:end -->

<!-- review:SF-2026-ARXIV-2607-20668:start -->
### From Agent Failures to Text Policies: What Works and What Breaks

<!-- claim:SF-2026-ARXIV-2607-20668:start -->TextGrad improves language-model systems by revising text from feedback. Its core thesis is that natural-language feedback can act as a gradient for optimizing text components without changing model weights. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20668:end -->

**为什么进入候选分母。** 摘要首要问题为“TextGrad improves language-model systems by revising text from feedback.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** TextGrad improves language-model systems by revising text from feedback.

**证据证明什么。** Human-written policies improve two frozen 7B agents on TextWorldExpress by 5.0 success points, showing that useful policy text exists.

**证据没有证明什么。** Because the human rules are only 15–38 words each, the 80-word limit alone does not explain this gap. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20668v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20668v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.20668v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.20668v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.20668v1#S6 — 6 Discussion; https://arxiv.org/html/2607.20668v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Because the human rules are only 15–38 words each, the 80-word limit alone does not explain this gap.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20668:end -->

<!-- review:SF-2026-ARXIV-2607-20709:start -->
### NVIDIA-labs OO Agents: Native Python Object-Oriented Agents

<!-- claim:SF-2026-ARXIV-2607-20709:start -->Traditional agent development is split across prompt templates, tool schemas, callback code, and workflow graphs. We present NVIDIA Object-Oriented Agents (NOOA), a model-agnostic Python framework for building reliable AI agents. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20709:end -->

**为什么进入候选分母。** 摘要首要问题为“Traditional agent development is split across prompt templates, tool schemas, callback code, and workflow graphs.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present NVIDIA Object-Oriented Agents (NOOA), a model-agnostic Python framework for building reliable AI agents.

**证据证明什么。** We find the community already converging on several of these ideas--often as experimental or partial features--and present the comparison to encourage further adoption. (3) We demonstrate that current models use this interface effectively, both in targeted capability tests and on agentic and reasoning benchmarks such as SWE-bench Verified and Terminal-Bench 2.0 and ARC-AGI-3.

**证据没有证明什么。** Taken together, these directions suggest that progress in agent capability will come not only from larger models or better prompts, but from the co-development of model and harness. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20709v1#A1.SS3 — A.3 Microsoft Agent Framework; https://arxiv.org/html/2607.20709v1#A3 — Appendix C Appendix: Memory-System Details。Evaluation：https://arxiv.org/html/2607.20709v1#S4.SSx1 — Experimental Results on Agentic Benchmarks; https://arxiv.org/html/2607.20709v1#S4 — 4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.20709v1#A4.SS3 — D.3 World-model usage evidence and failure modes; https://arxiv.org/html/2607.20709v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/NVIDIA-NeMo/labs-OO-Agents, https://github.com/letta-ai/letta, https://github.com/anomalyco/opencode; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Taken together, these directions suggest that progress in agent capability will come not only from larger models or better prompts, but from the co-development of model and harness.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20709:end -->

<!-- review:SF-2026-ARXIV-2607-20712:start -->
### Evaluating Large Language Models for Symbolic Security Protocol Analysis

<!-- claim:SF-2026-ARXIV-2607-20712:start -->Security protocol verification relies on formal tools such as ProVerif and OFMC. This study evaluates whether Large Language Models (LLMs) can perform comparable analysis. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20712:end -->

**为什么进入候选分母。** 摘要首要问题为“Security protocol verification relies on formal tools such as ProVerif and OFMC.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** This study evaluates whether Large Language Models (LLMs) can perform comparable analysis.

**证据证明什么。** Self-reported confidence is uniformly high yet shows no meaningful correlation with correctness.

**证据没有证明什么。** These tools are highly effective, yet each carries practical limitations in termination, boundedness, or state-space explosion. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20712v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20712v1#S2 — 2 Background。Evaluation：https://arxiv.org/html/2607.20712v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20712v1#S2 — 2 Background。Limitations / counterevidence：https://arxiv.org/html/2607.20712v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20712v1#S2 — 2 Background。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：These tools are highly effective, yet each carries practical limitations in termination, boundedness, or state-space explosion.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20712:end -->

<!-- review:SF-2026-ARXIV-2607-20723:start -->
### Leaky Language Models: Stealing Architecture and Inference Optimizations via Per-Token Timing

<!-- claim:SF-2026-ARXIV-2607-20723:start -->This work presents LeakyLMs, a set of attacks that leak proprietary model, architecture, and deployment information from production language models. LeakyLMs is the first to demonstrate that key model and deployment details can be inferred using only token generation timing, even when interacting through remote APIs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20723:end -->

**为什么进入候选分母。** 摘要首要问题为“This work presents LeakyLMs, a set of attacks that leak proprietary model, architecture, and deployment information from production language models.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** LeakyLMs is the first to demonstrate that key model and deployment details can be inferred using only token generation timing, even when interacting through remote APIs.

**证据证明什么。** Our measurements show that Google Gemini Flash 2.5 uses speculative decoding with a draft context window of approximately 128K tokens.

**证据没有证明什么。** The attack further assumes a single-GPU inference setting and does not model multi-GPU execution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20723v1#A2 — Appendix B Additional Details on Leaking Model Architecture Attack; https://arxiv.org/html/2607.20723v1#S2.SS1 — 2.1. Transformer Architecture。Evaluation：https://arxiv.org/html/2607.20723v1#A1.SS2 — A.2. Remote Black-Box Model Results; https://arxiv.org/html/2607.20723v1#S4.SS4 — 4.4. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.20723v1#S3 — 3. Threat Model; https://arxiv.org/html/2607.20723v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/feifeibear/LLMSpeculativeSampling, https://huggingface.co/timdettmers/guanaco-13b, https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The attack further assumes a single-GPU inference setting and does not model multi-GPU execution.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20723:end -->

<!-- review:SF-2026-ARXIV-2607-20729:start -->
### Operational Identity: A Finite Audit of Declared and Implemented Rules of Sameness

<!-- claim:SF-2026-ARXIV-2607-20729:start -->A record system declares when two records refer to the same entity, occurrence, scope, or rule. Its disclosed implementation mechanisms induce a corresponding operational identity relation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20729:end -->

**为什么进入候选分母。** 摘要首要问题为“A record system declares when two records refer to the same entity, occurrence, scope, or rule.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** A record system declares when two records refer to the same entity, occurrence, scope, or rule.

**证据证明什么。** A passing verdict is non-monotone because extending the transformation history can merge declared classes and create a witness among records already examined.

**证据没有证明什么。** Each level carries a completeness claim that the procedure cannot discharge and a finite witness that refutes it. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20729v1#S8.SS4 — 8.4 AI-System Identity and Governance。Evaluation：https://arxiv.org/html/2607.20729v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20729v1#S1.SS1 — 1.1 Two Answers to One Question。Limitations / counterevidence：https://arxiv.org/html/2607.20729v1#S10 — 10 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Each level carries a completeness claim that the procedure cannot discharge and a finite witness that refutes it.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20729:end -->

<!-- review:SF-2026-ARXIV-2607-20730:start -->
### GPE: Evaluating Robust Evidence Aggregation for Fact Verification under Controllable GEO-Style Poisoning

<!-- claim:SF-2026-ARXIV-2607-20730:start -->Large language models increasingly use search tools to retrieve up-to-date information, introducing a new attack surface in which retrieved documents can be manipulated. This risk is amplified by the development of generative engine optimization, which can make selected content more likely to be retrieved, cited, and adopted by models. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20730:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models increasingly use search tools to retrieve up-to-date information, introducing a new attack surface in which retrieved documents can be manipulated.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Existing fact-verification benchmarks and evaluation frameworks do not provide the controlled evidence environments needed to assess robustness against GEO poisoning.

**证据证明什么。** Experiments across multiple verification methods and poisoning attacks demonstrate that GPE exposes robustness degradation and efficiency trade-offs that cannot be observed through clean evaluation alone, confirming the need to evaluate fact verification under adversarial evidence environments.

**证据没有证明什么。** The experiments reveal attack-dependent degradation: ATA is strongest on average, no verifier is consistently robust, and resistance to instruction injection does not imply resistance to content tampering. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20730v1#S4 — IV Evaluation Framework。Evaluation：https://arxiv.org/html/2607.20730v1#S5.SS2 — V-B Results and Analysis; https://arxiv.org/html/2607.20730v1#S3 — III GPE Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.20730v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The experiments reveal attack-dependent degradation: ATA is strongest on average, no verifier is consistently robust, and resistance to instruction injection does not imply resistance to content tampering.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20730:end -->

<!-- review:SF-2026-ARXIV-2607-20734:start -->
### LLMs Get Lost in Evolving User Intent

<!-- claim:SF-2026-ARXIV-2607-20734:start -->As LLMs become more capable, they are increasingly deployed as collaborative agents, taking on user-delegated tasks through iterative interaction. Yet genuine interaction is inherently dynamic: users rarely specify their intent upfront, instead disclosing, revising, and reshaping it as the conversation unfolds. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20734:end -->

**为什么进入候选分母。** 摘要首要问题为“As LLMs become more capable, they are increasingly deployed as collaborative agents, taking on user-delegated tasks through iterative interaction.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To study this, we introduce a framework that transforms static, single-turn tasks into dynamic multi-turn conversations in which the user's intent evolves across turns--incrementally revealed, revised, and at times redirected mid-conversation--while preserving each task's original evaluation protocol, enabling existing benchmarks to be reused as controlled testbeds without new annotation.

**证据证明什么。** Our findings point to a fundamental gap: today's LLMs do not yet faithfully track and act on the user's evolving intent, a capability invisible to static evaluation yet critical for future collaborative agents.

**证据没有证明什么。** Limitations and Future Directions Our framework focuses on intent evolution, but does not model finer grained variation in user behavior, such as persona, communication style, typos, or grammatical errors Sun et al. (2025) ; Naous et al. (2026) . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20734v1#A2.SS1 — B.1 Model Details; https://arxiv.org/html/2607.20734v1#A6.SS3 — F.3 Effect of Model Capacity。Evaluation：https://arxiv.org/html/2607.20734v1#A6 — Appendix F Additional Experiments and Analysis; https://arxiv.org/html/2607.20734v1#A2 — Appendix B Experimental Setup Details。Limitations / counterevidence：https://arxiv.org/html/2607.20734v1#Sx1 — Limitations and Future Directions; https://arxiv.org/html/2607.20734v1#S5.SS3 — 5.3 Additional Analysis and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/microsoft/evolving-intent/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations and Future Directions Our framework focuses on intent evolution, but does not model finer grained variation in user behavior, such as persona, communication style, typos, or grammatical errors Sun et al. (2025) ; Naous et al. (2026) .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20734:end -->

<!-- review:SF-2026-ARXIV-2607-20739:start -->
### Pipelined Gradient Coding

<!-- claim:SF-2026-ARXIV-2607-20739:start -->In large-scale machine learning, distributed training commonly involves multiple workers evaluating the gradients of the model on different dataset partitions. A common challenge is the presence of straggling workers, which may significantly slow down training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20739:end -->

**为什么进入候选分母。** 摘要首要问题为“In large-scale machine learning, distributed training commonly involves multiple workers evaluating the gradients of the model on different dataset partitions.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In this paper, we propose to pipeline GC, such that gradient evaluation is segmented across multiple steps and each worker evaluates gradients on just a single dataset partition per step.

**证据证明什么。** Through extensive simulations and experiments on cloud infrastructure, our schemes not only significantly reduce training time but also accelerate convergence compared to GC and other baselines.

**证据没有证明什么。** VII Conclusion We proposed pipelined gradient coding (PGC), which overcomes the -fold computation overhead of gradient coding by pipelining: each worker evaluates only one partition per step and reuses stale gradients to form coded gradients. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20739v1#S6.SS1 — VI-A Implementation。Evaluation：https://arxiv.org/html/2607.20739v1#S4.SS2 — IV-B Convergence Analysis; https://arxiv.org/html/2607.20739v1#S5.SS3 — V-C Convergence Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.20739v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：VII Conclusion We proposed pipelined gradient coding (PGC), which overcomes the -fold computation overhead of gradient coding by pipelining: each worker evaluates only one partition per step and reuses stale gradients to form coded gradients.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20739:end -->

<!-- review:SF-2026-ARXIV-2607-20757:start -->
### GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries

<!-- claim:SF-2026-ARXIV-2607-20757:start -->Transformers are known to have internal continuous symmetries that leave outputs invariant, while modifying quantization. GaugeQuant leverages this in-training by introducing a LogSumExp term to the loss that breaks the symmetries, thus selecting a basis that minimizes activation outliers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20757:end -->

**为什么进入候选分母。** 摘要首要问题为“Transformers are known to have internal continuous symmetries that leave outputs invariant, while modifying quantization.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** With the LLaMA-2 7B model under W4A4 quantization with group size 128, perplexity drops from 8.22 to 6.73, competing with post-training methods that require frozen models and calibration datasets.

**证据证明什么。** Code is available at https://github.com/MPedraBento/gauge-quant.

**证据没有证明什么。** Another limitation is that The LogSumExp proxy suppresses all large activations indiscriminately, which may reduce the model’s capability to encode distinctions between similar outputs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20757v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20757v1#S2 — 2 Background and related Work。Evaluation：https://arxiv.org/html/2607.20757v1#S5.SS1 — 5.1 Results。Limitations / counterevidence：https://arxiv.org/html/2607.20757v1#S6 — 6 Discussion and Broader Implications; https://arxiv.org/html/2607.20757v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/MPedraBento/gauge-quant, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Another limitation is that The LogSumExp proxy suppresses all large activations indiscriminately, which may reduce the model’s capability to encode distinctions between similar outputs.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20757:end -->

<!-- review:SF-2026-ARXIV-2607-20759:start -->
### IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests

<!-- claim:SF-2026-ARXIV-2607-20759:start -->AI coding agents powered by LLMs are increasingly integrated into real-world software development, where they generate, edit, and execute code with autonomous access to local files and tools. Coding agents inherit security risks from both the LLM backbone, where adversarial prompts, poisoned training data, and backdoor triggers can cause models to emit insecure or attacker-chosen code, and their agentic architecture, where tool-using autonomy enables induced misuse of external APIs, data exfiltration, and persistent compromise of development environments. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20759:end -->

**为什么进入候选分母。** 摘要首要问题为“AI coding agents powered by LLMs are increasingly integrated into real-world software development, where they generate, edit, and execute code with autonomous access to local files and tools.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Our further analysis shows that rejection is almost entirely from LLMs rather than the agent frameworks, with GPT models broadly vulnerable and Sonnet 4.6 exhibiting more selective, risk-aware blocking of high-impact actions.

**证据证明什么。** Our results reveal critical vulnerabilities in the as-deployed modern coding agents, i.e., 66.5% of the malicious issues from IssueTrojanBench penetrate all the guardrails (agent- and LLM-level) of coding agents.

**证据没有证明什么。** We also find that the current defense strategy adds limited protection to coding agents. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20759v1#S3 — III Methodology; https://arxiv.org/html/2607.20759v1#S3.SS1 — III-A Threat Model。Evaluation：https://arxiv.org/html/2607.20759v1#S5 — V Evaluation Results; https://arxiv.org/html/2607.20759v1#S4 — IV Evaluation Setup。Limitations / counterevidence：https://arxiv.org/html/2607.20759v1#S7 — VII Conclusion and Future Work; https://arxiv.org/html/2607.20759v1#S3.SS1 — III-A Threat Model。

**Artifact boundary。** Exact v1 links https://code.claude.com/docs/en/overview, https://developers.openai.com/codex/concepts/sandboxing, https://openai.com/index/gpt-5-3-codex-system-card/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：We also find that the current defense strategy adds limited protection to coding agents.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20759:end -->

<!-- review:SF-2026-ARXIV-2607-20764:start -->
### ArbiGraph: Arbitrarily Scalable Verifiable Task Graphs for Evaluating Context Management

<!-- claim:SF-2026-ARXIV-2607-20764:start -->We introduce ARBIGRAPH, a benchmark generator for evaluating whether tool-assisted language agents can retain, update, compose, and discard task-relevant context across extended reasoning workflows. ARBIGRAPH represents each task as a natural-language problem with an executable Python solver, and composes tasks through typed intermediate states, instantiated here as scalar and list values. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20764:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce ARBIGRAPH, a benchmark generator for evaluating whether tool-assisted language agents can retain, update, compose, and discard task-relevant context across extended reasoning workflows.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce ARBIGRAPH, a benchmark generator for evaluating whether tool-assisted language agents can retain, update, compose, and discard task-relevant context across extended reasoning workflows.

**证据证明什么。** The results show high accuracy on isolated tasks but substantial degradation on more complex dependent tasks: accuracy drops by up to 33.3% on branching chains of dependent math tasks.

**证据没有证明什么。** 6 Limitations and Future Work We plan two concrete extensions to ArbiGraph . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20764v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20764v1#S3.SS5 — 3.5 Models and Inference Settings。Evaluation：https://arxiv.org/html/2607.20764v1#A1 — Appendix A Experimental Setup Details; https://arxiv.org/html/2607.20764v1#S2 — 2 The ArbiGraph Benchmark Generator。Limitations / counterevidence：https://arxiv.org/html/2607.20764v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.20764v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/pavelgolikov/ArbiGraph.git, https://huggingface.co/Qwen/Qwen3.5-27B, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：6 Limitations and Future Work We plan two concrete extensions to ArbiGraph .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20764:end -->

<!-- review:SF-2026-ARXIV-2607-20768:start -->
### Are Diversity Metrics Measuring Diversity? A Capability-Controlled Audit of Majority-Vote Gain in LLM Ensembles

<!-- claim:SF-2026-ARXIV-2607-20768:start -->Majority voting over LLMs is widely assumed to benefit from diversity, and diversity measures are used to choose which models to combine. We ask whether five such measures track diversity or mainly re-express capability, auditing them as predictors of majority-vote gain over the best member across 31,900 subsets of 30 LLMs on MMLU-Pro (29 on TruthfulQA) under explicit capability controls. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20768:end -->

**为什么进入候选分母。** 摘要首要问题为“Majority voting over LLMs is widely assumed to benefit from diversity, and diversity measures are used to choose which models to combine.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We ask whether five such measures track diversity or mainly re-express capability, auditing them as predictors of majority-vote gain over the best member across 31,900 subsets of 30 LLMs on MMLU-Pro (29 on TruthfulQA) under explicit capability controls.

**证据证明什么。** Joint rawspace linear regressions treating strict diversity, disagreement, and double-fault as independent predictors are rank-deficient by construction.

**证据没有证明什么。** 5.4 A residual pairwise co-failure association remains The contingency-table statistics do not provide several independent linear signals. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20768v1#A1 — Appendix A Model roster and parsing audit; https://arxiv.org/html/2607.20768v1#A1.SS1 — A.1 Model roster and full-sample filtering statistics。Evaluation：https://arxiv.org/html/2607.20768v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.20768v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.20768v1#S5.SS4 — 5.4 A residual pairwise co-failure association remains; https://arxiv.org/html/2607.20768v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：5.4 A residual pairwise co-failure association remains The contingency-table statistics do not provide several independent linear signals.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20768:end -->

<!-- review:SF-2026-ARXIV-2607-20771:start -->
### Emergent Compositional Skills in Mixture-of-Experts VLAs

<!-- claim:SF-2026-ARXIV-2607-20771:start -->We consider the problem of learning compositional robot policies end-to-end from expert demonstrations, without any pre-specified notion of task decomposition or hierarchy. We ask whether a VLA trained with a simplified Mixture-of-Experts (MoE) action head can emergently learn to decompose tasks into reusable, interpretable primitives. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20771:end -->

**为什么进入候选分母。** 摘要首要问题为“We consider the problem of learning compositional robot policies end-to-end from expert demonstrations, without any pre-specified notion of task decomposition or hierarchy.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We ask whether a VLA trained with a simplified Mixture-of-Experts (MoE) action head can emergently learn to decompose tasks into reusable, interpretable primitives.

**证据证明什么。** We find that learned experts are heavily reused across tasks and consistently correspond to qualitatively distinct low-level behaviors, suggesting that the router implicitly learns to perform high-level sequencing while experts serve as compositional primitives.

**证据没有证明什么。** Also, experts can sometimes perform behaviors unrelated to their associated primitives, suggesting that the mapping from experts to primitives is not fully precise/discernable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20771v1#S2 — 2 Approach。Evaluation：https://arxiv.org/html/2607.20771v1#S3 — 3 Experimental Results; https://arxiv.org/html/2607.20771v1#S3.SS1 — 3.1 Qualitative Analysis of Expert Skills。Limitations / counterevidence：https://arxiv.org/html/2607.20771v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Also, experts can sometimes perform behaviors unrelated to their associated primitives, suggesting that the mapping from experts to primitives is not fully precise/discernable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20771:end -->

<!-- review:SF-2026-ARXIV-2607-20791:start -->
### Refusal-Gated Decoding: Preserving Refusal Behavior Under High-Temperature Sampling

<!-- claim:SF-2026-ARXIV-2607-20791:start -->High-temperature sampling is one of the primary mechanisms for increasing diversity in LLMs. Recent advances in truncation-based sampling techniques have helped mitigate drawbacks of high-temperature sampling such as neural text degeneration, thereby enabling greater diversity in LLM outputs without sacrificing coherence. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20791:end -->

**为什么进入候选分母。** 摘要首要问题为“High-temperature sampling is one of the primary mechanisms for increasing diversity in LLMs.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this gap, we systematically study how temperature influences refusal behavior in LLMs and propose an efficient sequential decoding approach which preserves a model's greedy decoding refusal response at high temperatures while incurring minimal additional latency.

**证据证明什么。** Our work demonstrates how refusal behavior can be maintained in an efficient manner for applications which require high-temperature sampling.

**证据没有证明什么。** Our work demonstrates how unlocking greater diversity in LLMs via high-temperature sampling does not need to come at the cost of reduced safety in terms of a model’s refusal behavior. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20791v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20791v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.20791v1#A2 — Appendix B Ablation: Impact of the Refusal Prefix Compatibility Gate; https://arxiv.org/html/2607.20791v1#A3 — Appendix C Ablation: Soft Compatibility Gate。Limitations / counterevidence：https://arxiv.org/html/2607.20791v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/meta-llama/Llama-Guard-4-12B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Our work demonstrates how unlocking greater diversity in LLMs via high-temperature sampling does not need to come at the cost of reduced safety in terms of a model’s refusal behavior.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SAMPLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20791:end -->

<!-- review:SF-2026-ARXIV-2607-20792:start -->
### Memoir: Should a Model Write to Its Memory While It Thinks?

<!-- claim:SF-2026-ARXIV-2607-20792:start -->Memoir combines per-sample fast memory, shared slow parameters, variable-depth latent recurrence, and a future-latent energy objective. We test its riskiest coupling: each pondering iteration may rewrite the fast tier that the same iteration reads. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20792:end -->

**为什么进入候选分母。** 摘要首要问题为“Memoir combines per-sample fast memory, shared slow parameters, variable-depth latent recurrence, and a future-latent energy objective.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We test its riskiest coupling: each pondering iteration may rewrite the fast tier that the same iteration reads.

**证据证明什么。** Kernel restructuring also reduced delta-rule forward time from 0.907 ms to 0.351 ms on the stated device.

**证据没有证明什么。** 6 Limitations The most important limitation is that our ablation does not isolate the variable its name suggests. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20792v1#S3 — 3 Method; https://arxiv.org/html/2607.20792v1#S4 — 4 Implementation。Evaluation：https://arxiv.org/html/2607.20792v1#S5 — 5 Experimental Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.20792v1#S3.SS3 — 3.3 Future-latent and energy objectives; https://arxiv.org/html/2607.20792v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/RightNow-AI/Memoir, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：6 Limitations The most important limitation is that our ablation does not isolate the variable its name suggests.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20792:end -->

<!-- review:SF-2026-ARXIV-2607-20827:start -->
### Auditing Provenance Sensitivity in LLM Agent Action Selection

<!-- claim:SF-2026-ARXIV-2607-20827:start -->LLM agents choose tools and arguments from context that mixes user requests, tool outputs, retrieved records, memory, and untrusted text. Evidence can be relevant without being authorized to determine a decision, so a correct action need not be grounded only in permitted evidence. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20827:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents choose tools and arguments from context that mixes user requests, tool outputs, retrieved records, memory, and untrusted text.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce a target-specific authorization audit that labels context factors separately for each tool and argument target.

**证据证明什么。** The models respond to textual source-authority cues, but this does not prevent untrusted evidence from influencing their actions.

**证据没有证明什么。** Agent evaluation should test provenance dependence alongside correctness; limitations appear in Appendix A . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20827v1#Sx2 — Method; https://arxiv.org/html/2607.20827v1#A10.SSx1 — Experiment–Model Matrix。Evaluation：https://arxiv.org/html/2607.20827v1#A10.SSx1 — Experiment–Model Matrix; https://arxiv.org/html/2607.20827v1#A2 — Appendix B Additional Matched, Behavioral, and Anchor Results。Limitations / counterevidence：https://arxiv.org/html/2607.20827v1#A1 — Appendix A Limitations and Scope; https://arxiv.org/html/2607.20827v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Agent evaluation should test provenance dependence alongside correctness; limitations appear in Appendix A .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20827:end -->

<!-- review:SF-2026-ARXIV-2607-20852:start -->
### Code Monitor Red Teaming for Public-Test-Passing Code

<!-- claim:SF-2026-ARXIV-2607-20852:start -->Visible tests are a common gate for LLM-generated code, but passing them does not certify specification correctness. We study a deployment-like monitoring problem: after code has passed public tests, can a weaker LLM verifier identify the residual hidden bugs? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20852:end -->

**为什么进入候选分母。** 摘要首要问题为“Visible tests are a common gate for LLM-generated code, but passing them does not certify specification correctness.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce Code Monitor Red Teaming, a monitor-red-teaming protocol that fixes a public-check information boundary while varying generator pressure, verifier scaffolding, and weak-to-strong capability.

**证据证明什么。** Weak verifiers improve with scaffolding and model family, but still miss most hidden bugs at 5% false-positive rate.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20852v1#A2.SS6 — B.6 CodeWorkflow Construction Protocol and Oracle Design; https://arxiv.org/html/2607.20852v1#S2.SS2 — 2.2 Threat Model and Information Boundary。Evaluation：https://arxiv.org/html/2607.20852v1#A1.SS1 — A.1 Code Generation and Execution Benchmarks; https://arxiv.org/html/2607.20852v1#S2.SS3 — 2.3 Benchmark Construction。Limitations / counterevidence：https://arxiv.org/html/2607.20852v1#A8 — Appendix H Sample-Mix and Failure Taxonomy; https://arxiv.org/html/2607.20852v1#A8.SS2 — H.2 Failure Taxonomy。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20852:end -->

<!-- review:SF-2026-ARXIV-2607-20860:start -->
### Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways

<!-- claim:SF-2026-ARXIV-2607-20860:start -->Commercial LLM gateways mediate access to hosted models, but the served backend may not match the advertised one: it may substitute a cheaper model on every request or route only a fraction $ε$ of requests to it. Prior black-box auditors often need a privileged signal (log-probabilities, token ranks, or reference samples) or a target-specific probe, fix the query budget in advance, and return a yes/no verdict. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20860:end -->

**为什么进入候选分母。** 摘要首要问题为“Commercial LLM gateways mediate access to hosted models, but the served backend may not match the advertised one: it may substitute a cheaper model on every request or route only a fraction $ε$ of requests to it.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present $\mathrm{IRIS}$, an audit that needs only the returned text: it asks endpoints to generate random numbers or strings, fingerprints the backend, and is the first to combine, in one text-only audit, detection of whole-stream substitution and fractional dilution, attribution of the served backend, routing-fraction ($ε$) estimation, and a query budget it sizes itself.

**证据证明什么。** Further experiments cover adversarial gateways, knob identifiability, unseen diluents, and false-positive control.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20860v1#S15 — S15 Extended Method Comparison; https://arxiv.org/html/2607.20860v1#S6.SS2 — 6.2 Commercial models via OpenRouter。Evaluation：https://arxiv.org/html/2607.20860v1#S6 — 6 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20860v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-GATEWAY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20860:end -->

<!-- review:SF-2026-ARXIV-2607-20864:start -->
### Position Bias is Hidden Behind Ceiling Effects: A Permutation Diagnostic for LLM Benchmarks

<!-- claim:SF-2026-ARXIV-2607-20864:start -->Position bias in multiple-choice LLM evaluation is widely cited as a confound in capability comparisons, but published measurements rely on single answer-order shuffles whose results confound the bias signal with content-level noise and sampling stochasticity. I introduce inspect_permute, an open-source extension to the inspect_ai evaluation framework that runs exhaustive answer-order permutations per question and reports the chi-squared / Cramer V signature of position bias with bootstrap confidence intervals. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20864:end -->

**为什么进入候选分母。** 摘要首要问题为“Position bias in multiple-choice LLM evaluation is widely cited as a confound in capability comparisons, but published measurements rely on single answer-order shuffles whose results confound the bias signal with content-level noise and sampling stochasticity.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** I introduce inspect_permute, an open-source extension to the inspect_ai evaluation framework that runs exhaustive answer-order permutations per question and reports the chi-squared / Cramer V signature of position bias with bootstrap confidence intervals.

**证据证明什么。** Position bias in multiple-choice LLM evaluation is widely cited as a confound in capability comparisons, but published measurements rely on single answer-order shuffles whose results confound the bias signal with content-level noise and sampling stochasticity.

**证据没有证明什么。** Most consequentially, a flagship-tier validation against models that current public benchmarks cannot resolve — GPT-5, Claude Opus 4.8, Gemini 3 Pro, Grok 4, and pre-release variants accessible only through pre-deployment evaluation channels — would close the question of whether the absence of detected bias in the present sweep reflects ceiling saturation or genuine bias mitigation in the frontier tier. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20864v1#S2 — 2 The permutation diagnostic — design; https://arxiv.org/html/2607.20864v1#S4.SS1 — 4.1 Sweep design。Evaluation：https://arxiv.org/html/2607.20864v1#S4 — 4 Results; https://arxiv.org/html/2607.20864v1#S5.SS1 — 5.1 Calibrating a benchmark to a model tier。Limitations / counterevidence：https://arxiv.org/html/2607.20864v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/TambaClan/inspect_permute, https://github.com/UKGovernmentBEIS/inspect_ai, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Most consequentially, a flagship-tier validation against models that current public benchmarks cannot resolve — GPT-5, Claude Opus 4.8, Gemini 3 Pro, Grok 4, and pre-release variants accessible only through pre-deployment evaluation channels — would close the question of whether the absence of detected bias in the present sweep reflects ceiling saturation or genuine bias mitigation in the frontier tier.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20864:end -->

<!-- review:SF-2026-ARXIV-2607-20887:start -->
### TwistedMerge: Certified Higher-Order Diagnostics and Abstention for Model Merging

<!-- claim:SF-2026-ARXIV-2607-20887:start -->Model merging combines independently trained or fine-tuned models, but pairwise alignability does not imply globally consistent alignment. We formulate merging as a finite descent problem in which checkpoints are local objects, alignment maps are transitions, and cycle products are residuals. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20887:end -->

**为什么进入候选分母。** 摘要首要问题为“Model merging combines independently trained or fine-tuned models, but pairwise alignability does not imply globally consistent alignment.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** The results position descent theory as a falsifiable certification and abstention framework.

**证据证明什么。** The results position descent theory as a falsifiable certification and abstention framework.

**证据没有证明什么。** It is not a multilayer LoRA stack on a transformer or vision transformer. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20887v1#S3.SS5 — 3.5 Natural-data and architecture boundary; https://arxiv.org/html/2607.20887v1#A3 — Appendix C Full algorithm and diagnostics。Evaluation：https://arxiv.org/html/2607.20887v1#A5 — Appendix E Secondary experiments; https://arxiv.org/html/2607.20887v1#S2.SS1 — 2.1 Status of the mathematical results。Limitations / counterevidence：https://arxiv.org/html/2607.20887v1#A4 — Appendix D Geometric discussion; https://arxiv.org/html/2607.20887v1#S4 — 4 Limitations and decisive next tests。

**Artifact boundary。** Exact v1 links https://github.com/tinggong9/TwistedMerge, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：It is not a multilayer LoRA stack on a transformer or vision transformer.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20887:end -->

<!-- review:SF-2026-ARXIV-2607-20891:start -->
### Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions

<!-- claim:SF-2026-ARXIV-2607-20891:start -->Deep Research agents conduct long-horizon investigations by iteratively planning, retrieving evidence, and generating reports. However, it remains unclear whether they can resist apparently credible but factually false information introduced into these workflows. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20891:end -->

**为什么进入候选分母。** 摘要首要问题为“Deep Research agents conduct long-horizon investigations by iteratively planning, retrieving evidence, and generating reports.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** To study this failure mode, we introduce MisKnow-Agent, a controlled evaluation framework that constructs task-specific documents supporting manually audited false conclusions with controlled authority cues and source styles.

**证据证明什么。** Pre- and post-research defenses reduce FCAR but do not eliminate adoption, motivating continuous verification when evidence enters intermediate research states and final synthesis.

**证据没有证明什么。** Susceptibility is shaped not only by the backbone LLM, but also by framework design, source presentation, and, most critically, the stage at which misleading evidence enters the workflow. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20891v1#S3 — 3 Methodology; https://arxiv.org/html/2607.20891v1#S4.SS5 — 4.5 How Do Framework and LLM Choices Shape FCAR?。Evaluation：https://arxiv.org/html/2607.20891v1#A5.SS5 — E.5 FCAR Evaluation; https://arxiv.org/html/2607.20891v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.20891v1#S3.SS2 — 3.2 Threat Model; https://arxiv.org/html/2607.20891v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Susceptibility is shaped not only by the backbone LLM, but also by framework design, source presentation, and, most critically, the stage at which misleading evidence enters the workflow.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20891:end -->

<!-- review:SF-2026-ARXIV-2607-20908:start -->
### Multi-turn RL with Structural and Performance Aware Rewards for CUDA Kernel Generation

<!-- claim:SF-2026-ARXIV-2607-20908:start -->Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a powerful technique to enhance the reasoning capacity of LLMs for optimized code generation. However, existing RLVR approaches primarily rely on outcome-based signals such as correctness and speedup, overlooking performance-critical structural properties of programs that are essential for generating optimized code. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20908:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a powerful technique to enhance the reasoning capacity of LLMs for optimized code generation.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In this work, we propose CudaPerf, a reflective RL framework that incorporates both verifiable execution rewards and structural code-aware rewards derived from parallelization features (e.g., memory coalescing, occupancy, Arithmatic Intensity, and synchronization patterns).

**证据证明什么。** Empirical findings suggest that CudaPerf significantly outperforms strong baselines, including Qwen-3-32B (for C to CUDA) and CUDA Agent (for PyTorch to CUDA) by achieving up to 5X &amp; 3.32X improvements in speedup, and 17% &amp; 7% improvements in correctness, respectively.

**证据没有证明什么。** Another point worth mentioning is that CUDAPerf includes iterative refinement; it remains limited by the model and reward design, which can restrict its ability to discover optimization strategies beyond observed patterns. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20908v1#A1.SS13 — A.13 MLP Ranker Architecture; https://arxiv.org/html/2607.20908v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.20908v1#S3 — 3 Experimental Results; https://arxiv.org/html/2607.20908v1#A1.SS16 — A.16 Results。Limitations / counterevidence：https://arxiv.org/html/2607.20908v1#S5 — 5 Limitations; https://arxiv.org/html/2607.20908v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://atcoder.jp/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Another point worth mentioning is that CUDAPerf includes iterative refinement; it remains limited by the model and reward design, which can restrict its ability to discover optimization strategies beyond observed patterns.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20908:end -->

<!-- review:SF-2026-ARXIV-2607-20911:start -->
### Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction

<!-- claim:SF-2026-ARXIV-2607-20911:start -->We introduce Tencent WorkBuddy Bench, a multi-domain evaluation suite for coding agents; this report documents its construction methodology, scoring protocol, and a cross-model leaderboard. At its core is a unified evaluation framework for constructing and running distribution-informed coding-agent tasks across four work domains - Code, Web, Office, and Security. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20911:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce Tencent WorkBuddy Bench, a multi-domain evaluation suite for coding agents; this report documents its construction methodology, scoring protocol, and a cross-model leaderboard.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce Tencent WorkBuddy Bench, a multi-domain evaluation suite for coding agents; this report documents its construction methodology, scoring protocol, and a cross-model leaderboard.

**证据证明什么。** We report a cross-model leaderboard across several model families.

**证据没有证明什么。** Office retains rule-check outcomes independently, so the Judge cannot alter them, but its semantic-rubric scores remain subject to model-judge bias. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20911v1#S1 — 1 Introduction; https://arxiv.org/html/2607.20911v1#S2 — 2 Task Construction。Evaluation：https://arxiv.org/html/2607.20911v1#S3 — 3 The Benchmark; https://arxiv.org/html/2607.20911v1#S4 — 4 Evaluation Harness and Scoring。Limitations / counterevidence：https://arxiv.org/html/2607.20911v1#S7 — 7 Limitations and Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/laude-institute/harbor, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Office retains rule-check outcomes independently, so the Judge cannot alter them, but its semantic-rubric scores remain subject to model-judge bias.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20911:end -->

<!-- review:SF-2026-ARXIV-2607-20918:start -->
### OPOD: On-Policy Omni Distillation

<!-- claim:SF-2026-ARXIV-2607-20918:start -->Omni-modal models provide a unified interface for text, images, and audio. However, improving these abilities together remains difficult, as post-training on pooled multimodal data often fails to preserve the strengths of modality teachers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20918:end -->

**为什么进入候选分母。** 摘要首要问题为“Omni-modal models provide a unified interface for text, images, and audio.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address these challenges, we propose On-Policy Omni Distillation (OPOD), which consolidates text, image, and audio teachers into one omni model.

**证据证明什么。** Extensive experiments on twelve benchmarks show that OPOD achieves the best average at three model scales, reaching 70.8, 51.7, and 46.2 and outperforming the strongest comparator by 2.1, 1.8, and 1.7 points.

**证据没有证明什么。** The controller analysis further reveals distinct calibrated budgets and independently emerging teacher-weight trajectories, providing direct evidence that the three teachers require different guidance schedules. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20918v1#Sx1 — Introduction; https://arxiv.org/html/2607.20918v1#Sx2 — Related Work。Evaluation：https://arxiv.org/html/2607.20918v1#Sx4 — Experiments; https://arxiv.org/html/2607.20918v1#Sx4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.20918v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The controller analysis further reveals distinct calibrated budgets and independently emerging teacher-weight trajectories, providing direct evidence that the three teachers require different guidance schedules.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20918:end -->

<!-- review:SF-2026-ARXIV-2607-20940:start -->
### Ms. Forcing: Efficient Streaming Video Generation with Multi-Scale Patchification and Attention

<!-- claim:SF-2026-ARXIV-2607-20940:start -->Streaming video diffusion models have made substantial progress toward interactive and dynamic world simulation, but the nested autoregressive and denoising loops of conventional next-frame generation hinder real-time deployment. Recent rolling-window methods pipeline denoising across multiple consecutive frames at different noise levels, improving throughput and long-horizon stability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20940:end -->

**为什么进入候选分母。** 摘要首要问题为“Streaming video diffusion models have made substantial progress toward interactive and dynamic world simulation, but the nested autoregressive and denoising loops of conventional next-frame generation hinder real-time deployment.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose Ms.Forcing, an efficient streaming video generation paradigm that adapts spatial granularity to each state's noise level.

**证据证明什么。** We include both quantitative and qualitative experiments to show that Ms.Forcing reaches 22.84 FPS on a single H200 GPU, 39.6% faster than Rolling Forcing, while significantly improving VBench scores in both short video and long video generation setting.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20940v1#S4 — 4 Methodology; https://arxiv.org/html/2607.20940v1#S3.SS1 — 3.1 Preliminary: Autoregressive video diffusion models。Evaluation：https://arxiv.org/html/2607.20940v1#S5 — 5 Experiments; https://arxiv.org/html/2607.20940v1#S5.SS2 — 5.2 Qualitative Results。Limitations / counterevidence：https://arxiv.org/html/2607.20940v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/gdhe17/Self-Forcing/blob/main/checkpoints/ode_init.pt, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20940:end -->

<!-- review:SF-2026-ARXIV-2607-20950:start -->
### Best-of-Evidence: Best-of-N Selection under Partial Verification

<!-- claim:SF-2026-ARXIV-2607-20950:start -->BoN improves model outputs by sampling several candidates and selecting one with a proxy score, but it assumes that complete candidates can be evaluated reliably. Many vision-language tasks instead provide only partial verification: a finding, span, value, region, or relation may be checkable even when no dependable whole-response verifier exists. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20950:end -->

**为什么进入候选分母。** 摘要首要问题为“BoN improves model outputs by sampling several candidates and selecting one with a proxy score, but it assumes that complete candidates can be evaluated reliably.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce Best-of-Evidence (BoE), an inference-time selection framework that keeps the BoN candidate pool fixed, represents reusable claims with a signed candidate--factor graph, and allocates a limited budget to evidence actions that can change the final choice.

**证据证明什么。** Theoretically, we show that residual evidence capacity limits any evidence-driven improvement and that shared factor queries can achieve an O(log K) versus Θ(K) query separation in a factor-code model.

**证据没有证明什么。** BoE keeps the BoN candidate pool fixed, represents reusable local claims with a signed candidate–factor graph, and allocates a limited evidence budget according to estimated selection value. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20950v1#S5.SS1 — 5.1 Benchmark design; https://arxiv.org/html/2607.20950v1#A1.SS1 — A.1 Formal Partial-Verification Model。Evaluation：https://arxiv.org/html/2607.20950v1#S5.SS2 — 5.2 Benchmark results; https://arxiv.org/html/2607.20950v1#A2 — Appendix B Experimental Details and Additional Diagnostics。Limitations / counterevidence：https://arxiv.org/html/2607.20950v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：BoE keeps the BoN candidate pool fixed, represents reusable local claims with a signed candidate–factor graph, and allocates a limited evidence budget according to estimated selection value.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20950:end -->

<!-- review:SF-2026-ARXIV-2607-20972:start -->
### Delivery, Not Storage: Cue-Anchored Working Memory as a Harness Property for Coding Agents

<!-- claim:SF-2026-ARXIV-2607-20972:start -->Coding agents ship with one kind of memory: documents. Instruction files, plan artifacts, and auto-written memory directories are deliberately authored and deliberately retrieved: the agent must choose to write them and choose to read them back. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20972:end -->

**为什么进入候选分母。** 摘要首要问题为“Coding agents ship with one kind of memory: documents.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Instruction files, plan artifacts, and auto-written memory directories are deliberately authored and deliberately retrieved: the agent must choose to write them and choose to read them back.

**证据证明什么。** Delivery, not storage, is the product: the reliable memory channel for agents is the one the agent never has to think about.

**证据没有证明什么。** Capture is the unevaluated half (§ 2 ’s open half): the probe’s ten fact notes were seeded by the harness, and § 5 ’s voluntary-write counts measure initiative, not capture quality; capture-side automation is future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20972v1#S3 — 3 The cue-anchored memory model; https://arxiv.org/html/2607.20972v1#S4 — 4 Implementation surface。Evaluation：https://arxiv.org/html/2607.20972v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.20972v1#S7 — 7 Threats to validity; https://arxiv.org/html/2607.20972v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/swapnanil/vectr, https://github.com/anthropics/claude-code/issues/34556, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Capture is the unevaluated half (§ 2 ’s open half): the probe’s ten fact notes were seeded by the harness, and § 5 ’s voluntary-write counts measure initiative, not capture quality; capture-side automation is future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20972:end -->

<!-- review:SF-2026-ARXIV-2607-20982:start -->
### GuardianAgentBench: Where Agents Fail and How to Guard Them

<!-- claim:SF-2026-ARXIV-2607-20982:start -->As large language model agents increasingly operate autonomously with access to tools and external environments, ensuring their safe and reliable behavior becomes critical. We present GuardianAgentBench (GABench), a benchmark of 580 scenarios across six domains evaluated on three production-ready frameworks: LangChain, LlamaIndex, and Vectara. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20982:end -->

**为什么进入候选分母。** 摘要首要问题为“As large language model agents increasingly operate autonomously with access to tools and external environments, ensuring their safe and reliable behavior becomes critical.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present GuardianAgentBench (GABench), a benchmark of 580 scenarios across six domains evaluated on three production-ready frameworks: LangChain, LlamaIndex, and Vectara.

**证据证明什么。** These results demonstrate that execution-time structural intervention improves safety without disrupting correct agent behavior.

**证据没有证明什么。** Experiments with six state-of-the-art models show that even the strongest configuration achieves only 74.8 overall accuracy, with failure analysis revealing two distinct regimes: stronger models under-call tools (MTC 52–57%) while weaker models mis-select and over-call (ITS up to 25%, RTC 29–33%). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20982v1#S4 — 4 Guardrails Design。Evaluation：https://arxiv.org/html/2607.20982v1#S5.SS2 — 5.2 Results and Analysis; https://arxiv.org/html/2607.20982v1#A2.SS3 — B.3 Agent Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.20982v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/langchain-ai/langchain, https://github.com/run-llama/llama_index, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Experiments with six state-of-the-art models show that even the strongest configuration achieves only 74.8 overall accuracy, with failure analysis revealing two distinct regimes: stronger models under-call tools (MTC 52–57%) while weaker models mis-select and over-call (ITS up to 25%, RTC 29–33%).

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20982:end -->

<!-- review:SF-2026-ARXIV-2607-20999:start -->
### Workflow-Localized Mechanism Learning: Attribution-Guided Repair and Knowledge Reuse for Structured Agent Skills

<!-- claim:SF-2026-ARXIV-2607-20999:start -->Agent Skills package reusable procedural knowledge as external artifacts for frozen language-model agents, yet existing optimizers do not jointly resolve where a failure occurs in a workflow, which mechanism caused it, and how relevant knowledge from third-party Skills should be reused locally. We introduce Workflow-Localized Mechanism Learning (WML). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-20999:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent Skills package reusable procedural knowledge as external artifacts for frozen language-model agents, yet existing optimizers do not jointly resolve where a failure occurs in a workflow, which mechanism caused it, and how relevant knowledge from third-party Skills should be reused locally.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce Workflow-Localized Mechanism Learning (WML).

**证据证明什么。** On Compiler-Supported50, WML attains both the highest hard-PASS rate and the lowest cost per successful task; compiled execution sharply reduces tokens and calls relative to a direct SkillAgent while retaining most of its successful tasks.

**证据没有证明什么。** The current post-patch gate uses same-batch comparison; an independent long-horizon regression set is important future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.20999v1#S4.SS5 — 4.5 Algorithm and Prototype Instantiation。Evaluation：https://arxiv.org/html/2607.20999v1#S5 — 5 Experimental Setup; https://arxiv.org/html/2607.20999v1#S6 — 6 Results。Limitations / counterevidence：https://arxiv.org/html/2607.20999v1#S7 — 7 Limitations and Ethical Considerations; https://arxiv.org/html/2607.20999v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The current post-patch gate uses same-batch comparison; an independent long-horizon regression set is important future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-20999:end -->

<!-- review:SF-2026-ARXIV-2607-21000:start -->
### Naju: A Native Discrete State-Space Model with Independent Retention and Writing for Long-Sequence Memory

<!-- claim:SF-2026-ARXIV-2607-21000:start -->Long-sequence memory tracking places two opposing demands on a recurrent state: near-lossless retention of stored bindings over long horizons, and active overwriting of stale ones. In our diagnostic suite, the strongest efficient baselines tend to solve only one side well. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21000:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-sequence memory tracking places two opposing demands on a recurrent state: near-lossless retention of stored bindings over long horizons, and active overwriting of stale ones.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Continuous-time-parameterized state-space models (SSMs) such as Mamba obtain their discrete recurrence by zero-order-hold discretization of a continuous-time system; we argue that this detour is unnecessary for memory tracking and parameterize the discrete transition directly.

**证据证明什么。** Naju (Native Adaptive Junction Unit) factorizes the recurrent update, schematically $x_n = f_n\odot x_{n-1} + i_n\odot(B_n u_n)$, into an explicit discrete pole (a learned forget gate $f_n$), an independent write gain $i_n$, and input-dependent write/read maps.

**证据没有证明什么。** Thus, the observed advantage does not increase uniformly with model scale, and the relative ordering depends on context length, model width, state size, and optimization. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21000v1#S2.SS3 — 2.3 Hybrid and Long-Context Architectures; https://arxiv.org/html/2607.21000v1#S3 — 3 Method: Naju, a Native Discrete SSM。Evaluation：https://arxiv.org/html/2607.21000v1#A2 — Appendix B Per-Task Results with Length Extrapolation; https://arxiv.org/html/2607.21000v1#S4 — 4 Memory-Kernel and Pole-Gain Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.21000v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Thus, the observed advantage does not increase uniformly with model scale, and the relative ordering depends on context length, model width, state size, and optimization.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21000:end -->

<!-- review:SF-2026-ARXIV-2607-21005:start -->
### Weight-norm Criticality: A Mechanism for Loss Spikes Induced by the Normalization and Weight Decay

<!-- claim:SF-2026-ARXIV-2607-21005:start -->Most explanations of training instability focus on \emph{learning-rate criticality}, typically characterized by the Edge of Stability, beyond which optimization becomes unstable. We argue that, in practical deep neural network training, there is an additional and often overlooked \emph{weight-norm criticality}. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21005:end -->

**为什么进入候选分母。** 摘要首要问题为“Most explanations of training instability focus on \emph{learning-rate criticality}, typically characterized by the Edge of Stability, beyond which optimization becomes unstable.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We argue that, in practical deep neural network training, there is an additional and often overlooked \emph{weight-norm criticality}.

**证据证明什么。** This perspective provides a rationale for why weight penalties can improve generalization yet cannot be made arbitrarily strong: excessive decay drives scale-invariant weight norms past a critical boundary and destabilizes training.

**证据没有证明什么。** While existing explanations commonly attribute loss spikes to factors such as data, loss landscape geometry, or optimization—often unified through the notion of learning-rate criticality. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21005v1#S6 — 6 Training Instability in Large Language Models and Module-wise Dynamics。Evaluation：https://arxiv.org/html/2607.21005v1#A1.SS1 — A.1 Experimental Details; https://arxiv.org/html/2607.21005v1#A1.SS3 — A.3 Ablation Study: Weight Decay Applied Only to Non-Scale-Invariant Layers。Limitations / counterevidence：https://arxiv.org/html/2607.21005v1#S7 — 7 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：While existing explanations commonly attribute loss spikes to factors such as data, loss landscape geometry, or optimization—often unified through the notion of learning-rate criticality.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21005:end -->

<!-- review:SF-2026-ARXIV-2607-21042:start -->
### Faster IndexTTS-2: Accelerating and Streaming Autoregressive Zero-Shot Text-to-Speech Synthesis on GPUs

<!-- claim:SF-2026-ARXIV-2607-21042:start -->Autoregressive text-to-speech models achieve strong naturalness but suffer from slow inference due to sequential token generation, limiting their deployment in production applications that require low latency. IndexTTS-2 is a state-of-the-art autoregressive TTS model consisting of a GPT, a flow-matching Diffusion Transformer, and a vocoder. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21042:end -->

**为什么进入候选分母。** 摘要首要问题为“Autoregressive text-to-speech models achieve strong naturalness but suffer from slow inference due to sequential token generation, limiting their deployment in production applications that require low latency.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Our methodology provides a practical reference for efficiently accelerating similar autoregressive speech models on GPUs.

**证据证明什么。** Autoregressive text-to-speech models achieve strong naturalness but suffer from slow inference due to sequential token generation, limiting their deployment in production applications that require low latency.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21042v1#S2 — II System Design; https://arxiv.org/html/2607.21042v1#S2.SS2 — II-B System Overview。Evaluation：https://arxiv.org/html/2607.21042v1#S3 — III Experiments; https://arxiv.org/html/2607.21042v1#S3.SS1 — III-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.21042v1#S4 — IV Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/NVIDIA/TensorRT-LLM, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21042:end -->

<!-- review:SF-2026-ARXIV-2607-21051:start -->
### Sample-Efficient Learning from Agent Experience

<!-- claim:SF-2026-ARXIV-2607-21051:start -->Real-world agent learning is often constrained by costly environment interactions, such as running time-consuming experiments or obtaining human feedback. In-context learning offers a highly sample-efficient way for agents to learn from their own interaction histories, but its gains disappear once that experience is removed from the context. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21051:end -->

**为什么进入候选分母。** 摘要首要问题为“Real-world agent learning is often constrained by costly environment interactions, such as running time-consuming experiments or obtaining human feedback.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In-context learning offers a highly sample-efficient way for agents to learn from their own interaction histories, but its gains disappear once that experience is removed from the context.

**证据证明什么。** Experiments on 749 curated software-engineering tasks and six text-adventure games show that it retains at least 64.8\% of the gains from in-context learning across both domains, whereas direct supervised fine-tuning on the collected experience recovers only 3.8\%.

**证据没有证明什么。** The ten issue-and-repository-only samples for each case do not produce an accepted repair, whereas the experience-conditioned ICL samples implement the task-specific behavior summarized in Table 24 . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21051v1#A1.SS3 — A.3 TaleSuite Frontier-Model Reference Results; https://arxiv.org/html/2607.21051v1#A1.SS5 — A.5 Observed Errors in Model-Based Rollouts。Evaluation：https://arxiv.org/html/2607.21051v1#A1 — Appendix A Additional Experimental Details and Results; https://arxiv.org/html/2607.21051v1#A1.SS3 — A.3 TaleSuite Frontier-Model Reference Results。Limitations / counterevidence：https://arxiv.org/html/2607.21051v1#A3.SS11 — C.11 Cross-Case Findings and Limitations; https://arxiv.org/html/2607.21051v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The ten issue-and-repository-only samples for each case do not produce an accepted repair, whereas the experience-conditioned ICL samples implement the task-specific behavior summarized in Table 24 .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21051:end -->

<!-- review:SF-2026-ARXIV-2607-21090:start -->
### Training Large Language Models for Self-Explanation Faithfulness

<!-- claim:SF-2026-ARXIV-2607-21090:start -->We propose a Reinforcement Learning (RL) method to directly optimize the faithfulness of self-explanations - the extent to which a model's generated reasoning accurately reflects its internal decision-making process. While existing work focuses on evaluating faithfulness or using inference-time prompting frameworks to improve an LLM's self-explanation's tractability, these approaches do not provide a mechanism to directly optimize a model's parameters to generate faithful self-explanations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21090:end -->

**为什么进入候选分母。** 摘要首要问题为“We propose a Reinforcement Learning (RL) method to directly optimize the faithfulness of self-explanations - the extent to which a model's generated reasoning accurately reflects its internal decision-making process.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose a Reinforcement Learning (RL) method to directly optimize the faithfulness of self-explanations - the extent to which a model's generated reasoning accurately reflects its internal decision-making process.

**证据证明什么。** RL fine-tuned Llama3.1-8B and Qwen3-8B show substantial improvements on the Phi-CCT faithfulness metric, with in-distribution scores rising from near-zero to as high as 0.664, and out-of-distribution scores reaching up to 0.691 on held-out tasks such as StrategyQA.

**证据没有证明什么。** This offers a scalable path toward models that not only reason correctly but transparently disclose the actual drivers of their decisions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21090v1#S3 — 3 Method; https://arxiv.org/html/2607.21090v1#S3.SS2 — 3.2 Reinforcement Learning framework for improving faithfulness of self-explanations。Evaluation：https://arxiv.org/html/2607.21090v1#A1.SS3 — A.3 Results; https://arxiv.org/html/2607.21090v1#S3.SS1 — 3.1 Faithfulness of self-explanation: definition and evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.21090v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.21090v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：This offers a scalable path toward models that not only reason correctly but transparently disclose the actual drivers of their decisions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21090:end -->

<!-- review:SF-2026-ARXIV-2607-21106:start -->
### AttriMem: Attribution-Guided Process Feedback for Agent Memory Construction

<!-- claim:SF-2026-ARXIV-2607-21106:start -->Effective memory is crucial for LLM agents, yet constructing it effectively remains challenging. A memory-construction policy decides what information to extract, store, update, compress, or discard as interactions accumulate. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21106:end -->

**为什么进入候选分母。** 摘要首要问题为“Effective memory is crucial for LLM agents, yet constructing it effectively remains challenging.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose AttriMem, an attribution-guided process-feedback framework for learning memory-construction policies with RL.

**证据证明什么。** Experiments on long-horizon dialogue question answering show that AttriMem outperforms retrieval-based, heuristic, and RL-based baselines, generalizes across benchmarks and answer models, stabilizes RL optimization.

**证据没有证明什么。** In our setting, this risk is limited because final answers usually rely on only a few retrieved records and their associated memory operations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21106v1#A1 — Appendix A ContextCite Methodology Details; https://arxiv.org/html/2607.21106v1#S3.SS1 — 3.1 Memory Architecture。Evaluation：https://arxiv.org/html/2607.21106v1#S5 — 5 Experiments; https://arxiv.org/html/2607.21106v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.21106v1#S6 — 6 Discussion and Future Work; https://arxiv.org/html/2607.21106v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：In our setting, this risk is limited because final answers usually rely on only a few retrieved records and their associated memory operations.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21106:end -->

<!-- review:SF-2026-ARXIV-2607-21120:start -->
### Relative Value Learning

<!-- claim:SF-2026-ARXIV-2607-21120:start -->In reinforcement learning, critics typically estimate absolute state values $V(s)$, estimating how good a particular situation is in isolation. However, it turns out that only differences in value are relevant for control. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21120:end -->

**为什么进入候选分母。** 摘要首要问题为“In reinforcement learning, critics typically estimate absolute state values $V(s)$, estimating how good a particular situation is in isolation.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Motivated by this, we propose Relative Value Learning (RV), a framework that learns value differences directly via an antisymmetric function $Δ(s_i, s_j) = V(s_i) - V(s_j)$.

**证据证明什么。** Beyond theoretical results, we integrate RV with PPO and achieve competitive performance on the Atari benchmark (49 ALE games) compared to standard PPO, indicating that relative value estimation is an effective alternative to absolute critics.

**证据没有证明什么。** 7 Limitations Gauge fixing induces a trajectory-constant baseline in R-GAE that inflates variance for long horizons or when , but it is only partially reduced by relative value initialization. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21120v1#S5.SS1 — 5.1 Network Architecture; https://arxiv.org/html/2607.21120v1#A6 — Appendix F The Use of Large Language Models (LLMs)。Evaluation：https://arxiv.org/html/2607.21120v1#A3 — Appendix C Variance Analysis of the Relative Policy Gradient; https://arxiv.org/html/2607.21120v1#A5 — Appendix E Ablation on Pair Sampling。Limitations / counterevidence：https://arxiv.org/html/2607.21120v1#S7 — 7 Limitations; https://arxiv.org/html/2607.21120v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Hauf3n/relative-value-learning, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：7 Limitations Gauge fixing induces a trajectory-constant baseline in R-GAE that inflates variance for long horizons or when , but it is only partially reduced by relative value initialization.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21120:end -->

<!-- review:SF-2026-ARXIV-2607-21130:start -->
### Hardware-Software Co-Design for Float16 On-Device Training on RISC-V Single-Core

<!-- claim:SF-2026-ARXIV-2607-21130:start -->By leveraging standard RISC-V extensions, namely Zfh (scalar float16) and Zvfh (vector float16), this work proposes an open-source framework to enable complete on-device training on resource-constrained RISC-V single-core. Our approach allows memory footprint reduction by about 50% as compared to using float32 and with minimal model performance degradation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21130:end -->

**为什么进入候选分母。** 摘要首要问题为“By leveraging standard RISC-V extensions, namely Zfh (scalar float16) and Zvfh (vector float16), this work proposes an open-source framework to enable complete on-device training on resource-constrained RISC-V single-core.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Our work builds onto AIfES, an open-source, modular and generic DNN training and inference framework for embedded systems that can be extended with custom hardware-specific functions.

**证据证明什么。** Finally, we discuss the architecture of a Zvfh implementation within the same RISC-V core.

**证据没有证明什么。** Future work will focus on evaluating the performance gains brought by vector kernels on our VPU-enhanced NaxRiscv FPGA target, to complement with current results focused on validating the ODT pipeline through the RISC-V ISA Simulator and evaluating the implementation cost of RISC-V Zfh into our target. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21130v1#S2.SS1 — 2.1 Framework architecture; https://arxiv.org/html/2607.21130v1#S2.SS2 — 2.2 Framework evaluation。Evaluation：https://arxiv.org/html/2607.21130v1#S2.SS2 — 2.2 Framework evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.21130v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work will focus on evaluating the performance gains brought by vector kernels on our VPU-enhanced NaxRiscv FPGA target, to complement with current results focused on validating the ODT pipeline through the RISC-V ISA Simulator and evaluating the implementation cost of RISC-V Zfh into our target.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21130:end -->

<!-- review:SF-2026-ARXIV-2607-21143:start -->
### One More Turn, Less Regret: A Regret-Based Multi-Turn Benchmark for LLMs' Clarification Policies

<!-- claim:SF-2026-ARXIV-2607-21143:start -->Ambiguous user requests make clarification a sequential decision problem for conversational LLM assistants: they must decide whether to ask, what to ask, when to stop, and when to answer. We introduce RegretBench, a multi-turn benchmark that evaluates clarification as policy behavior rather than isolated question quality. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21143:end -->

**为什么进入候选分母。** 摘要首要问题为“Ambiguous user requests make clarification a sequential decision problem for conversational LLM assistants: they must decide whether to ask, what to ask, when to stop, and when to answer.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce RegretBench, a multi-turn benchmark that evaluates clarification as policy behavior rather than isolated question quality.

**证据证明什么。** Our results show that effective clarification requires more than plausible questions: models must ask the right question at the right time and stop once the user's intended meaning is clear.

**证据没有证明什么。** Limitations RegretBench depends on the quality of its semantic clarification interaction graphs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21143v1#A3 — Appendix C Clarification Methods; https://arxiv.org/html/2607.21143v1#S5.SS2 — 5.2 Which Models Behave Like Good Clarification Policies。Evaluation：https://arxiv.org/html/2607.21143v1#S2.SS3 — 2.3 Grounded Evaluation of Clarification; https://arxiv.org/html/2607.21143v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.21143v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.21143v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/ngocminhta/RegretBench, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations RegretBench depends on the quality of its semantic clarification interaction graphs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21143:end -->

<!-- review:SF-2026-ARXIV-2607-21151:start -->
### V-DEAL: Diagnosing Video Safety De-Calibration as an Understanding-Refusal Coupling Failure

<!-- claim:SF-2026-ARXIV-2607-21151:start -->As Video Large Language Models are increasingly deployed in real-world applications, ensuring their safety alignment has become critical. Counterintuitively, we find that harmful videos paired with benign queries achieve higher attack success rates than the same videos paired with explicitly harmful queries. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21151:end -->

**为什么进入候选分母。** 摘要首要问题为“As Video Large Language Models are increasingly deployed in real-world applications, ensuring their safety alignment has become critical.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To understand the underlying mechanism of this vulnerability, we present V-DEAL, a three-level diagnostic framework that jointly analyzes this failure across model behaviour, understanding, and internal representations.

**证据证明什么。** Counterintuitively, we find that harmful videos paired with benign queries achieve higher attack success rates than the same videos paired with explicitly harmful queries.

**证据没有证明什么。** Our analyses suggest that this vulnerability is not fully explained by weak video understanding alone, but is more consistent with a failure to reliably translate harmful visual evidence into refusal behaviour. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21151v1#S3 — 3 Framework and Experimental Setup; https://arxiv.org/html/2607.21151v1#S3.SS1 — 3.1 Diagnostic Framework。Evaluation：https://arxiv.org/html/2607.21151v1#A3.SS7 — C.7 Summary evaluation results; https://arxiv.org/html/2607.21151v1#A5.SS1 — E.1 Experimental task and evaluation protocol。Limitations / counterevidence：https://arxiv.org/html/2607.21151v1#A6 — Appendix F Additional Discussion; https://arxiv.org/html/2607.21151v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Our analyses suggest that this vulnerability is not fully explained by weak video understanding alone, but is more consistent with a failure to reliably translate harmful visual evidence into refusal behaviour.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21151:end -->

<!-- review:SF-2026-ARXIV-2607-21162:start -->
### Agree on the Model, Verify the Inference: GKR Protocols for HND-Based Transformer Inference

<!-- claim:SF-2026-ARXIV-2607-21162:start -->Outsourced Transformer inference exposes clients to model substitution and incomplete execution, while direct replay removes the computational benefit of delegation. We present GKR-HND, a registered-model protocol for verifying the polynomial backbone of Homomorphic--Nonhomomorphic Decomposition Transformers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21162:end -->

**为什么进入候选分母。** 摘要首要问题为“Outsourced Transformer inference exposes clients to model substitution and incomplete execution, while direct replay removes the computational benefit of delegation.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present GKR-HND, a registered-model protocol for verifying the polynomial backbone of Homomorphic--Nonhomomorphic Decomposition Transformers.

**证据证明什么。** Experiments with pretrained HND models validate the proof path and the delegated public computation without dense-matrix replay.

**证据没有证明什么。** The other two prefixes provide all-block numerical evidence only. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21162v1#S3.SS2 — 3.2 Threat Model; https://arxiv.org/html/2607.21162v1#as1 — Supporting Information for Agree on the Model, Verify the Inference: GKR Protocols for HND-Based Transformer Inference。Evaluation：https://arxiv.org/html/2607.21162v1#S6 — 6 Experimental Analysis; https://arxiv.org/html/2607.21162v1#S3.SS3 — 3.3 Evaluation Commitment Backend。Limitations / counterevidence：https://arxiv.org/html/2607.21162v1#S3.SS2 — 3.2 Threat Model; https://arxiv.org/html/2607.21162v1#S6.SS6 — 6.6 Robustness and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The other two prefixes provide all-block numerical evidence only.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21162:end -->

<!-- review:SF-2026-ARXIV-2607-21179:start -->
### Out of Sight, Still in Mind: Token Compression for Omni-LLMs

<!-- claim:SF-2026-ARXIV-2607-21179:start -->The goal of this paper is to reduce the input token cost of Omni-modal large language models (Omni-LLMs) at inference time. Omni-LLMs reason jointly over audio, video and text, but the cost of the three streams is highly unbalanced: visual tokens account for the vast majority of the input, and are highly redundant. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21179:end -->

**为什么进入候选分母。** 摘要首要问题为“The goal of this paper is to reduce the input token cost of Omni-modal large language models (Omni-LLMs) at inference time.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this paper, we propose ReMo, a training-free framework that compresses visual tokens by redistributing their information across modalities: a visual token is kept only if its information appears nowhere else.

**证据证明什么。** The goal of this paper is to reduce the input token cost of Omni-modal large language models (Omni-LLMs) at inference time.

**证据没有证明什么。** Limitations Although ReMo introduces significant improvements, it has several limitations that present opportunities for future research. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21179v1#S4 — 4 Method; https://arxiv.org/html/2607.21179v1#A1 — Appendix A ReMo Algorithm。Evaluation：https://arxiv.org/html/2607.21179v1#S5.SS2 — 5.2 Experimental Results; https://arxiv.org/html/2607.21179v1#A2 — Appendix B Further Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.21179v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.21179v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/Ultralytics/YOLOv8, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Limitations Although ReMo introduces significant improvements, it has several limitations that present opportunities for future research.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21179:end -->

<!-- review:SF-2026-ARXIV-2607-21217:start -->
### ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders

<!-- claim:SF-2026-ARXIV-2607-21217:start -->The recent emergence of vibe-coding workflows is changing what coding agents are expected to do. Instead of merely completing code under fully specified instructions, agents are increasingly expected to transform incomplete product intent into working software by combining various abilities including planning, requirement clarification, tool use, debugging, and repository-level construction. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21217:end -->

**为什么进入候选分母。** 摘要首要问题为“The recent emergence of vibe-coding workflows is changing what coding agents are expected to do.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this paper, we introduce ICAE-Bench, a benchmark for evaluating coding agents under interactive project-building settings.

**证据证明什么。** Third, to evaluate open-ended repositories fairly, ICAE-Bench uses standardized black-box tests together with multi-dimensional diagnostics, including functional correctness, semantic and API similarity, structural fidelity, design quality, and interaction quality.

**证据没有证明什么。** Future work will expand ICAE-Bench into end-to-end, multi-modal real-world scenarios. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21217v1#A9 — Appendix I Critic Model for Agentic Evaluation。Evaluation：https://arxiv.org/html/2607.21217v1#A9 — Appendix I Critic Model for Agentic Evaluation; https://arxiv.org/html/2607.21217v1#S2.SS1 — II-A Software-Agent Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.21217v1#S6 — VI Conclusion and Future Work; https://arxiv.org/html/2607.21217v1#S5 — V Discussion。

**Artifact boundary。** Exact v1 links https://github.com/ALEX-nlp/ICAE-EVAL, https://github.com/anthropics/claude-agent-sdk-python, https://github.com/openclaw/openclaw; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work will expand ICAE-Bench into end-to-end, multi-modal real-world scenarios.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21217:end -->

<!-- review:SF-2026-ARXIV-2607-21224:start -->
### Controlled Periodic Synchronization for Efficient Data-Parallel Training

<!-- claim:SF-2026-ARXIV-2607-21224:start -->Data-parallel training relies on frequent gradient synchronization across workers. Standard DDP synchronizes gradients at every iteration, which is effective on fast local-area networks but increasingly sensitive to communication latency and network variability in geographically distributed environments. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21224:end -->

**为什么进入候选分母。** 摘要首要问题为“Data-parallel training relies on frequent gradient synchronization across workers.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** This paper studies synchronization frequency as a systems parameter for communication-constrained distributed training.

**证据证明什么。** Direct profiling shows that exposed synchronization time at K=4 is roughly half that of DDP, explaining the improved WAN accuracy-time trade-off.

**证据没有证明什么。** This confirms that the best synchronization period is environment-dependent rather than fixed a priori. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21224v1#S2.SS3 — 2.3 Advanced Communication Frameworks and Runtimes; https://arxiv.org/html/2607.21224v1#S2.SS4 — 2.4 Local SGD and Periodic Averaging Methods。Evaluation：https://arxiv.org/html/2607.21224v1#A1 — Appendix A Additional Experimental Results; https://arxiv.org/html/2607.21224v1#S5 — 5 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.21224v1#S6 — 6 Results and Discussion; https://arxiv.org/html/2607.21224v1#S6.SS7 — 6.7 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：This confirms that the best synchronization period is environment-dependent rather than fixed a priori.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21224:end -->

<!-- review:SF-2026-ARXIV-2607-21273:start -->
### The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and The Channel, Not the Content, Decides What Works

<!-- claim:SF-2026-ARXIV-2607-21273:start -->Dense per-step supervision is the standard remedy for sparse-reward long-horizon LLM agents: reward the policy for predicting its next observation, which looks provably safe under potential-based shaping. No ALFWorld or WebShop reward-channel variant measurably beats its matched-normalization baseline and no gold signal measurably outperforms its content-free placebo: the delivery channel, not the content, decides; which channel is safe is regime-dependent. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21273:end -->

**为什么进入候选分母。** 摘要首要问题为“Dense per-step supervision is the standard remedy for sparse-reward long-horizon LLM agents: reward the policy for predicting its next observation, which looks provably safe under potential-based shaping.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** No ALFWorld or WebShop reward-channel variant measurably beats its matched-normalization baseline and no gold signal measurably outperforms its content-free placebo: the delivery channel, not the content, decides; which channel is safe is regime-dependent.

**证据证明什么。** No ALFWorld or WebShop reward-channel variant measurably beats its matched-normalization baseline and no gold signal measurably outperforms its content-free placebo: the delivery channel, not the content, decides; which channel is safe is regime-dependent.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21273v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21273v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.21273v1#S3 — 3 Experimental Setting; https://arxiv.org/html/2607.21273v1#S4.SS3 — 4.3 Analysis: bounded returns, unbounded advantages。Limitations / counterevidence：https://arxiv.org/html/2607.21273v1#S4 — 4 The Failure: Predictability Hacking; https://arxiv.org/html/2607.21273v1#S6 — 6 Controlled Separation of Failure Axes。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21273:end -->

<!-- review:SF-2026-ARXIV-2607-21291:start -->
### Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs

<!-- claim:SF-2026-ARXIV-2607-21291:start -->Large language models (LLMs) achieve strong generation and reasoning performance, but the Transformer architecture incurs high inference cost. Existing acceleration methods often rely on task-specific fine-tuning or training from scratch, increasing adaptation cost and limiting cross-task usability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21291:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) achieve strong generation and reasoning performance, but the Transformer architecture incurs high inference cost.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present an Adaptive Depth Sparse Framework (AdaDSF) that converts off-the-shelf pre-trained LLMs into depth-sparse models without full retraining.

**证据证明什么。** Large language models (LLMs) achieve strong generation and reasoning performance, but the Transformer architecture incurs high inference cost.

**证据没有证明什么。** 4.5 Future Work Although our experiments are limited to models up to 1.5B parameters, the proposed method is inherently scalable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21291v1#S3 — 3 Methods; https://arxiv.org/html/2607.21291v1#S3.SS2 — 3.2 Problem Formulation and Framework Overview。Evaluation：https://arxiv.org/html/2607.21291v1#S4 — 4 Experiments; https://arxiv.org/html/2607.21291v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.21291v1#S4.SS4 — 4.4 Discussion; https://arxiv.org/html/2607.21291v1#S4.SS5 — 4.5 Future Work。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/teknium/OpenHermes-2.5, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：4.5 Future Work Although our experiments are limited to models up to 1.5B parameters, the proposed method is inherently scalable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-DECODE`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21291:end -->

<!-- review:SF-2026-ARXIV-2607-21325:start -->
### Cryptographically verifiable authorization for autonomous AI agents: A falsifiable hypothesis and proof-of-concept

<!-- claim:SF-2026-ARXIV-2607-21325:start -->Autonomous AI agents increasingly execute actions, invoke tools, and operate on protected resources with limited human oversight. Existing authentication and authorization mechanisms establish identity and delegate authority, but do not inherently provide cryptographic evidence that a concrete request issued by a specific agent satisfies the applicable policy in a specific execution context. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21325:end -->

**为什么进入候选分母。** 摘要首要问题为“Autonomous AI agents increasingly execute actions, invoke tools, and operate on protected resources with limited human oversight.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We further identify and formalize the structural separation among identity binding, authorization-request binding, and runtime execution binding as a central open problem in the design of secure agentic systems (a distinction {not explicitly addressed by} current agentic security frameworks) and present a falsifiable research agenda for its resolution.

**证据证明什么。** We further identify and formalize the structural separation among identity binding, authorization-request binding, and runtime execution binding as a central open problem in the design of secure agentic systems (a distinction {not explicitly addressed by} current agentic security frameworks) and present a falsifiable research agenda for its resolution.

**证据没有证明什么。** Operational viability consequently depends not only on the selected proof system, but also on the authorization frequency of the deployment model. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21325v1#S3.SS1 — 3.1. System and Request Model; https://arxiv.org/html/2607.21325v1#S3 — 3. Preliminary Formal Model。Evaluation：https://arxiv.org/html/2607.21325v1#S1 — 1. Introduction; https://arxiv.org/html/2607.21325v1#S2 — 2. Related Work and Positioning。Limitations / counterevidence：https://arxiv.org/html/2607.21325v1#S3.SS4 — 3.4. Threat Model; https://arxiv.org/html/2607.21325v1#S6 — 6. Discussion and Research Agenda。

**Artifact boundary。** Exact v1 links https://github.com/Imari91/zk-auth-agent-demo, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Operational viability consequently depends not only on the selected proof system, but also on the authorization frequency of the deployment model.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21325:end -->

<!-- review:SF-2026-ARXIV-2607-21351:start -->
### How Many Bits Can an Adapter Write? Measuring the Capacity and Memorization of Parameter-Efficient Fine-Tuning

<!-- claim:SF-2026-ARXIV-2607-21351:start -->A LoRA adapter is a few megabytes that almost everyone treats as a skill rather than a record of the data behind it. Extending compression-based memorization analysis to the frozen-base setting, we measure directly, in bits, how much a low-rank adapter writes into a model it never changes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21351:end -->

**为什么进入候选分母。** 摘要首要问题为“A LoRA adapter is a few megabytes that almost everyone treats as a skill rather than a record of the data behind it.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Extending compression-based memorization analysis to the frozen-base setting, we measure directly, in bits, how much a low-rank adapter writes into a model it never changes.

**证据证明什么。** Applied to realistic fine-tunes of Qwen2.5, the same instrument shows privacy leakage rising with the bits an adapter writes rather than the parameters it nominally has, and it draws a clean line between supervised and reinforcement learning: the secrets that supervised fine-tuning copies down verbatim, an adapter trained on verifiable rewards never records.

**证据没有证明什么。** The harness we release measures, in bits and on any frozen base, what an adapter has written, and the three readings it returns are cheap enough to run before a checkpoint is shared, not only after it is attacked. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21351v1#Sx4.SSx1 — Plateaus, far below the full-model line。Evaluation：https://arxiv.org/html/2607.21351v1#Sx1 — Introduction; https://arxiv.org/html/2607.21351v1#Sx2 — Related Work。Limitations / counterevidence：https://arxiv.org/html/2607.21351v1#Sx7 — Discussion; https://arxiv.org/html/2607.21351v1#Sx8 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The harness we release measures, in bits and on any frozen base, what an adapter has written, and the three readings it returns are cheap enough to run before a checkpoint is shared, not only after it is attacked.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21351:end -->

<!-- review:SF-2026-ARXIV-2607-21356:start -->
### Emergent Misalignment Recruits a Pre-existing Persona Subspace

<!-- claim:SF-2026-ARXIV-2607-21356:start -->Fine-tuning an aligned language model on a narrow stream of bad advice can make it broadly misaligned on questions unrelated to the training data, a phenomenon called emergent misalignment. We ask why the narrow lesson generalizes at all, and we find that narrow fine-tuning recruits a persona structure that is present in the model before the fine-tune exists. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21356:end -->

**为什么进入候选分母。** 摘要首要问题为“Fine-tuning an aligned language model on a narrow stream of bad advice can make it broadly misaligned on questions unrelated to the training data, a phenomenon called emergent misalignment.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We ask why the narrow lesson generalizes at all, and we find that narrow fine-tuning recruits a persona structure that is present in the model before the fine-tune exists.

**证据证明什么。** We ask why the narrow lesson generalizes at all, and we find that narrow fine-tuning recruits a persona structure that is present in the model before the fine-tune exists.

**证据没有证明什么。** Broad misalignment and narrow adherence are both thresholds on the alignment score, at off-domain and at on-domain, so they are not independent readouts and an intervention that lifts the axis moves both by construction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21356v1#A2.SS6 — B.6 The paired design; https://arxiv.org/html/2607.21356v1#A7.SS1 — G.1 Design。Evaluation：https://arxiv.org/html/2607.21356v1#A11 — Appendix K Complete numerical results; https://arxiv.org/html/2607.21356v1#A13.SS5 — M.5 Two 2026 results。Limitations / counterevidence：https://arxiv.org/html/2607.21356v1#A9.SS7 — I.7 Failure modes; https://arxiv.org/html/2607.21356v1#S11 — 11 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Broad misalignment and narrow adherence are both thresholds on the alignment score, at off-domain and at on-domain, so they are not independent readouts and an intervention that lifts the axis moves both by construction.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21356:end -->

<!-- review:SF-2026-ARXIV-2607-21372:start -->
### Mean-to-Score Discrete Diffusion: Posterior-Mean Denoisers for Score Entropy

<!-- claim:SF-2026-ARXIV-2607-21372:start -->Score Entropy Discrete Diffusion (SEDD) parameterizes discrete reverse processes with unconstrained positive score ratios. While positivity guarantees nonnegative reverse jump rates, it does not ensure Bayes realizability: ratios at a noisy state need not be jointly induced by any clean-token posterior under the forward kernel. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21372:end -->

**为什么进入候选分母。** 摘要首要问题为“Score Entropy Discrete Diffusion (SEDD) parameterizes discrete reverse processes with unconstrained positive score ratios.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce \emph{mean-to-score} (M2S), which predicts a clean-token posterior mean and converts it to the score through an exact kernel-dependent linear map.

**证据证明什么。** Projecting raw scores onto the bridge polytope removes all observed negative weights and improves external generative PPL from $203.6$ to $175.1$ without changing the sampler.

**证据没有证明什么。** Positive SEDD scores define valid reverse CTMC rates, but the complete vector need not be induced by any clean-token posterior. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21372v1#S4 — 4 Methodology; https://arxiv.org/html/2607.21372v1#A2 — Appendix B Algorithms。Evaluation：https://arxiv.org/html/2607.21372v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.21372v1#A3.SS1 — C.1 MNIST Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.21372v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Positive SEDD scores define valid reverse CTMC rates, but the complete vector need not be induced by any clean-token posterior.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21372:end -->

<!-- review:SF-2026-ARXIV-2607-21401:start -->
### When Are Reasoning-Based Guardrails Not Efficient? ResponseGuard: A Fast Vision-Language Guard for Real-Time Moderation

<!-- claim:SF-2026-ARXIV-2607-21401:start -->A vision-language AI assistant returns its answer as a stream of generated tokens. Therefore, a safety guard that watches that answer has to keep up with the stream and stop a harmful reply before a user reads it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21401:end -->

**为什么进入候选分母。** 摘要首要问题为“A vision-language AI assistant returns its answer as a stream of generated tokens.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Therefore, a safety guard that watches that answer has to keep up with the stream and stop a harmful reply before a user reads it.

**证据证明什么。** Across a standard multimodal guardrail benchmark, our 2B ResponseGuard outperforms a recent 3B reasoning-based vision-language guard on response harmfulness detection, without any reasoning and at about 150 times lower time cost.

**证据没有证明什么。** A calibrated label-only encoder could be the natural default that a new vision-language guard is measured against, and a reasoning guard that reports a gain should show that the gain survives removing only the chain, and that the gain does not merely reflect a stronger backbone, more data, or a different objective. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21401v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21401v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.21401v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.21401v1#S4 — 4 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.21401v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.21401v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：A calibrated label-only encoder could be the natural default that a new vision-language guard is measured against, and a reasoning guard that reports a gain should show that the gain survives removing only the chain, and that the gain does not merely reflect a stronger backbone, more data, or a different objective.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21401:end -->

<!-- review:SF-2026-ARXIV-2607-21404:start -->
### MemTools: A Unified Research Framework for Interoperable Agent Memory

<!-- claim:SF-2026-ARXIV-2607-21404:start -->While memory systems are essential for agent architectures, pervasive architectural fragmentation restricts systematic research. Existing implementations typically couple different stages of the memory lifecycle, entangle evaluation logic with specific datasets, and provide limited support for the management of heterogeneous memory types. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21404:end -->

**为什么进入候选分母。** 摘要首要问题为“While memory systems are essential for agent architectures, pervasive architectural fragmentation restricts systematic research.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce MemTools, an interoperability research framework that decouples memory system components from their underlying deployment environments.

**证据证明什么。** Empirical evaluations on cross-system component integration, evaluation protocol reconfiguration, and heterogeneous memory coordination demonstrate that MemTools enables systematic isolation and analysis of memory design variables.

**证据没有证明什么。** Limitations While MemTools facilitates interoperability, its automatic matching engine only verifies the structural compatibility of data fields. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21404v1#S3 — 3 System Design; https://arxiv.org/html/2607.21404v1#S3.SS4 — 3.4 Framework Usage。Evaluation：https://arxiv.org/html/2607.21404v1#A2 — Appendix B Evaluation Protocols and Benchmarks; https://arxiv.org/html/2607.21404v1#A3.SS3 — C.3 Adding New Protocols and Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.21404v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.21404v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/JJJAYYYZhao/MemTools-public, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Limitations While MemTools facilitates interoperability, its automatic matching engine only verifies the structural compatibility of data fields.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21404:end -->

<!-- review:SF-2026-ARXIV-2607-21405:start -->
### Anti-Periodic Positional Encoding: Möbius Boundary Conditions Make In-Context Retrieval Reliable

<!-- claim:SF-2026-ARXIV-2607-21405:start -->Möbius RoPE is a rotary positional encoding built on the anti-periodic frequency ladder $θ_i=π(2i+1)/N$: every rotation plane advances by an odd multiple of $π$ across the training context, so the positional holonomy is $-1$ and the two ends of the sequence are deterministically coupled through a closed-form Dirichlet "dipole"; to our knowledge this is the first anti-periodic boundary condition in positional encoding. We verify the theory numerically to $\sim 10^{-6}$ and pretrain 48 models spanning six 160M-class and three 410M-class arms (2B FineWeb-Edu tokens each; the hybrid arm puts Möbius frequencies on 25% of heads). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21405:end -->

**为什么进入候选分母。** 摘要首要问题为“Möbius RoPE is a rotary positional encoding built on the anti-periodic frequency ladder $θ_i=π(2i+1)/N$: every rotation plane advances by an odd multiple of $π$ across the training context, so the positional holonomy is $-1$ and the two ends of the sequence are deterministically coupled through a closed-form Dirichlet "dipole"; to our knowledge this is the first anti-periodic boundary condition in positional encoding”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We verify the theory numerically to $\sim 10^{-6}$ and pretrain 48 models spanning six 160M-class and three 410M-class arms (2B FineWeb-Edu tokens each; the hybrid arm puts Möbius frequencies on 25% of heads).

**证据证明什么。** The effect is scoped to single-needle retrieval within the training window; a one-line frequency swap thus provides zero-cost insurance against the retrieval seed lottery.

**证据没有证明什么。** A multi-scale variant fails at 160M yet leads at 410M: a capacity-dependent allocation rule. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21405v1#S4 — 4 Method: Hybrid and Ladder Head Allocation; https://arxiv.org/html/2607.21405v1#S5.SS4 — 5.4 Scaling to 410M-class models (405M parameters)。Evaluation：https://arxiv.org/html/2607.21405v1#S5.SS5 — 5.5 Ladder ablation: a negative result at 160M, and a confirmed reversal at 410M; https://arxiv.org/html/2607.21405v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.21405v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.21405v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/gkamradt/needle-in-a-haystack, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：A multi-scale variant fails at 160M yet leads at 410M: a capacity-dependent allocation rule.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-POSITION-ENCODING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21405:end -->

<!-- review:SF-2026-ARXIV-2607-21419:start -->
### PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-21419:start -->In long-horizon LLM agent reinforcement learning, weak policies often repeat similar failures, producing uninformative rollout trajectories and limiting effective policy optimization. Existing skill-centric methods improve exploration by optimizing, filtering, or internalizing reusable skills. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21419:end -->

**为什么进入候选分母。** 摘要首要问题为“In long-horizon LLM agent reinforcement learning, weak policies often repeat similar failures, producing uninformative rollout trajectories and limiting effective policy optimization.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Existing skill-centric methods improve exploration by optimizing, filtering, or internalizing reusable skills.

**证据证明什么。** As policy improves, redundant context is revised or removed to reduce reliance on explicit guidance while preserving useful rollout variation.

**证据没有证明什么。** Our findings show that guidance optimized for immediate success is not necessarily the most useful training signal; effective support should instead preserve informative rollout contrast at each stage of learning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21419v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.21419v1#A1.SS1 — A.1 Training and Evaluation Configuration; https://arxiv.org/html/2607.21419v1#A2 — Appendix B Stage 1 Details and Supplementary Results。Limitations / counterevidence：https://arxiv.org/html/2607.21419v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Our findings show that guidance optimized for immediate success is not necessarily the most useful training signal; effective support should instead preserve informative rollout contrast at each stage of learning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21419:end -->

<!-- review:SF-2026-ARXIV-2607-21433:start -->
### Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence in Chain-of-Thought Models

<!-- claim:SF-2026-ARXIV-2607-21433:start -->Chain-of-thought reasoning models such as DeepSeek-R1-Distill-Qwen-7B exhibit a bimodal convergence pattern: generations either terminate within a token budget (converged) or exhaust it without reaching a conclusion (non-converged). We characterize this phenomenon empirically, showing that converged generations achieve 90.3% accuracy on AIME 1983-2024 while non-converged ones achieve only 6.6%, with an overall convergence rate of 62.0%. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21433:end -->

**为什么进入候选分母。** 摘要首要问题为“Chain-of-thought reasoning models such as DeepSeek-R1-Distill-Qwen-7B exhibit a bimodal convergence pattern: generations either terminate within a token budget (converged) or exhaust it without reaching a conclusion (non-converged).”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We characterize this phenomenon empirically, showing that converged generations achieve 90.3% accuracy on AIME 1983-2024 while non-converged ones achieve only 6.6%, with an overall convergence rate of 62.0%.

**证据证明什么。** Training linear probes on hidden-state activations at token positions 50-300, we find that layer-20 activations at token 150 achieve AUC 0.608 (+-0.080, 5-fold CV), reliably above chance even at token 50.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21433v1#S5.SS3 — 5.3 Toward practical early-exit systems。Evaluation：https://arxiv.org/html/2607.21433v1#S3.SS1 — 3.1 Experimental setup; https://arxiv.org/html/2607.21433v1#S3.SS2 — 3.2 Results。Limitations / counterevidence：https://arxiv.org/html/2607.21433v1#S2.SS2 — 2.2 Reasoning failure modes; https://arxiv.org/html/2607.21433v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/gneubig/aime-1983-2024, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21433:end -->

<!-- review:SF-2026-ARXIV-2607-21453:start -->
### Test-Time Scaling via Error Localization

<!-- claim:SF-2026-ARXIV-2607-21453:start -->Scaling inference-time computation has emerged as a reliable method to improve the performance of large language models on complex reasoning and programming tasks. However, standard approaches such as independent sampling and sequential multi-turn refinement operate without token-level credit assignment, resulting in computational inefficiency, since valid reasoning prefixes are frequently discarded. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21453:end -->

**为什么进入候选分母。** 摘要首要问题为“Scaling inference-time computation has emerged as a reliable method to improve the performance of large language models on complex reasoning and programming tasks.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Scaling inference-time computation has emerged as a reliable method to improve the performance of large language models on complex reasoning and programming tasks.

**证据证明什么。** Generalizing to math benchmarks AIME-2025 and HMMT-2025, TTEL cleanly outperforms competing test-time baselines across both Qwen3-8B and Qwen3-4B-Thinking-2507.

**证据没有证明什么。** The main approach for this is to generate multiple independent samples and select the best candidate via majority voting ( Wang et al., 2023 ) or verification against test cases ( Jain et al., 2024 ) . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21453v1#S4 — 4 Methodology; https://arxiv.org/html/2607.21453v1#S5 — 5 The TTEL Algorithm。Evaluation：https://arxiv.org/html/2607.21453v1#A3 — Appendix C Detailed Results for Scaling Experiments; https://arxiv.org/html/2607.21453v1#S8 — 8 Experimental Results。Limitations / counterevidence：https://arxiv.org/html/2607.21453v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21453v1#S2 — 2 Related Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The main approach for this is to generate multiple independent samples and select the best candidate via majority voting ( Wang et al., 2023 ) or verification against test cases ( Jain et al., 2024 ) .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SAMPLING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21453:end -->

<!-- review:SF-2026-ARXIV-2607-21475:start -->
### Error Certificates for KV-Cache Eviction via Randomized Design

<!-- claim:SF-2026-ARXIV-2607-21475:start -->Deterministic KV-cache eviction keeps the top-$k$ tokens under an importance score and deletes the rest, and after the deletion the serving system cannot know what the eviction cost it on the current query. We replace the deterministic tail with Poisson sampling at known inclusion probabilities, which makes the eviction error identifiable and turns a survey-sampling variance estimator over the retained set into a per-step error certificate at one extra scalar per retained token. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21475:end -->

**为什么进入候选分母。** 摘要首要问题为“Deterministic KV-cache eviction keeps the top-$k$ tokens under an importance score and deletes the rest, and after the deletion the serving system cannot know what the eviction cost it on the current query.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** On real long-term conversations the gated system returns the full-cache score inside the heavy-damage regime, and the rule that triggers it is the same across five model families.

**证据证明什么。** On real long-term conversations the gated system returns the full-cache score inside the heavy-damage regime, and the rule that triggers it is the same across five model families.

**证据没有证明什么。** Deterministic entropy and margin signals sit at chance; evicted mass is partially sighted; the certificate, which only a known randomized design can provide, leads by ten points. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21475v1#S3.SS3 — 3.3 Design: certainty plus Poisson tail, Hájek by logit offset; https://arxiv.org/html/2607.21475v1#S6.SS1 — 6.1 Design。Evaluation：https://arxiv.org/html/2607.21475v1#A2 — Appendix B Experimental details; https://arxiv.org/html/2607.21475v1#S6 — 6 Pre-registered study on real workloads, at two scales。Limitations / counterevidence：https://arxiv.org/html/2607.21475v1#S5 — 5 From attention error to task failure: synthetic suites; https://arxiv.org/html/2607.21475v1#S6.SS3 — 6.3 The silent-failure panel。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Deterministic entropy and margin signals sit at chance; evicted mass is partially sighted; the certificate, which only a known randomized design can provide, leads by ten points.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21475:end -->

<!-- review:SF-2026-ARXIV-2607-21480:start -->
### Finite-Sample Coverage Audits for High-Recall Candidate Generation: Certification and Learning-Theoretic Design

<!-- claim:SF-2026-ARXIV-2607-21480:start -->An initial high-recall stage in an empirical pipeline decides which items pass to later review, labelling, or modelling, and relevant items it misses are lost to every subsequent stage. We study how many audit labels are needed to certify, with finite-sample validity, that this missed relevant mass is small, and our main results characterise the label complexity of this problem. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21480:end -->

**为什么进入候选分母。** 摘要首要问题为“An initial high-recall stage in an empirical pipeline decides which items pass to later review, labelling, or modelling, and relevant items it misses are lost to every subsequent stage.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We study how many audit labels are needed to certify, with finite-sample validity, that this missed relevant mass is small, and our main results characterise the label complexity of this problem.

**证据证明什么。** We study how many audit labels are needed to certify, with finite-sample validity, that this missed relevant mass is small, and our main results characterise the label complexity of this problem.

**证据没有证明什么。** The central point is that the excluded pool is the only place where missed relevant items can occur. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21480v1#A1.SS1 — A.1 Proof of the finite-class design bound; https://arxiv.org/html/2607.21480v1#A1.SS2 — A.2 Proof of the VC-class design bound。Evaluation：https://arxiv.org/html/2607.21480v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21480v1#S1.SS1 — 1.1 Motivating examples。Limitations / counterevidence：https://arxiv.org/html/2607.21480v1#S9 — 9 Conclusion and future directions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The central point is that the excluded pool is the only place where missed relevant items can occur.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21480:end -->

<!-- review:SF-2026-ARXIV-2607-21482:start -->
### Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks

<!-- claim:SF-2026-ARXIV-2607-21482:start -->Large language models (LLMs) and agents are now widely used tools in code development, with data typically sent to third-party cloud-based models. Their adoption in research using personal data is constrained by governance requirements that typically prohibit data transmission to external services. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21482:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) and agents are now widely used tools in code development, with data typically sent to third-party cloud-based models.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce an open-source framework for evaluating the efficacy of AI agents powered by open-weight LLMs on one of the most persistent bottlenecks in research on longitudinal population studies: data preparation.

**证据证明什么。** The performance of open-weight LLMs running on consumer-grade hardware shows promise of a viable path toward AI-assisted data preparation in governance-restricted research settings.

**证据没有证明什么。** A task was considered fully completed only when all expected variables in the output dataset met the prespecified agreement threshold described above. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.21482v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.21482v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.21482v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.21482v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.21482v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.21482v1#page=10 — PDF page 10。

**Artifact boundary。** Exact v1 links https://github.com/UCL-ARC/RRBench, https://github.com/cls-data/ns_core, https://github.com/CLS-Data/ns_core; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A task was considered fully completed only when all expected variables in the output dataset met the prespecified agreement threshold described above.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21482:end -->

<!-- review:SF-2026-ARXIV-2607-21503:start -->
### Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems

<!-- claim:SF-2026-ARXIV-2607-21503:start -->Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs. Agents drown in their own accumulating history while paying a token cost that grows every turn, producing missing recalls within and across conversations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21503:end -->

**为什么进入候选分母。** 摘要首要问题为“Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Agents drown in their own accumulating history while paying a token cost that grows every turn, producing missing recalls within and across conversations.

**证据证明什么。** We then make the economic case: naive context accumulation grows token cost quadratically in conversation length, crude summarization buys linear cost at the price of an accuracy cliff, and only validated compaction achieves linear cost with preserved fidelity.

**证据没有证明什么。** 6.3 Scope and limitations of this evaluation We want to be explicit about what these results and the system do and do not establish. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21503v1#A2 — Appendix B Retrieval-study methodology (motivating study, Section 3.3); https://arxiv.org/html/2607.21503v1#S4 — 4 The Maximem Synap System。Evaluation：https://arxiv.org/html/2607.21503v1#S6 — 6 Evaluation; https://arxiv.org/html/2607.21503v1#S6.SS2 — 6.2 Results。Limitations / counterevidence：https://arxiv.org/html/2607.21503v1#S6.SS3 — 6.3 Scope and limitations of this evaluation; https://arxiv.org/html/2607.21503v1#S8 — 8 Future Directions: Decision-Level and Organization-Scale Context。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：6.3 Scope and limitations of this evaluation We want to be explicit about what these results and the system do and do not establish.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21503:end -->

<!-- review:SF-2026-ARXIV-2607-21522:start -->
### GS-Agent: Creating 4D Physical Worlds With Generative Simulation

<!-- claim:SF-2026-ARXIV-2607-21522:start -->Creating dynamic and physically realistic 4D worlds from natural language descriptions is both fascinating and challenging. Traditional computer graphics methods rely on manual creation, requiring extensive human effort to fine-tune materials, motions, and visual fidelity. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21522:end -->

**为什么进入候选分母。** 摘要首要问题为“Creating dynamic and physically realistic 4D worlds from natural language descriptions is both fascinating and challenging.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present GS-Agent, an end-to-end multi-agent framework that integrates physics engines in the loop to generate realistic, dynamic, and controllable 4D physical worlds from natural language.

**证据证明什么。** Experimental results show that GS-Agent effectively converts natural language into diverse and physically plausible 4D worlds exhibiting rich interactions among liquids, deformable objects, and rigid bodies, while achieving cinematic camera and lighting control.

**证据没有证明什么。** Reminders : - You are only responsible for one entity at a time . - Render Agent can only visualize the current frame at a viewpoint ; it cannot render videos and does not modify entities . - Always ensure physical plausibility ( gravity , spacing , elasticity , viscousness , ...). - Avoid overlapping entities to prevent collisions . - Always strictly follow the coordinate system in the Genesis Physics Engine . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21522v1#S3 — 3 GS-Agent: A Multi-Agent Framework with Generative Simulation in the Loop; https://arxiv.org/html/2607.21522v1#A2 — Appendix B Additional Implementation Details。Evaluation：https://arxiv.org/html/2607.21522v1#S4.SS4 — 4.4 Ablation and Backbone Analysis; https://arxiv.org/html/2607.21522v1#A3 — Appendix C Additional Experiment Details。Limitations / counterevidence：https://arxiv.org/html/2607.21522v1#A3.SS3 — C.3 Failure Analysis; https://arxiv.org/html/2607.21522v1#S5 — 5 Discussions。

**Artifact boundary。** Exact v1 links https://github.com/Genesis-Embodied-AI/Genesis, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Reminders : - You are only responsible for one entity at a time . - Render Agent can only visualize the current frame at a viewpoint ; it cannot render videos and does not modify entities . - Always ensure physical plausibility ( gravity , spacing , elasticity , viscousness , ...). - Avoid overlapping entities to prevent collisions . - Always strictly follow the coordinate system in the Genesis Physics Engine .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21522:end -->

<!-- review:SF-2026-ARXIV-2607-21530:start -->
### From Resource Flow to Executable Tests: Petri-Net-Guided LLM Test Generation for Concurrent Stateful Rust APIs

<!-- claim:SF-2026-ARXIV-2607-21530:start -->Concurrent stateful library APIs expose behavior through evolving resource ownership, lifecycle states, and competing interleavings. Large language models can synthesize executable Rust tests, but their outputs often violate API preconditions, remain shallow, or reduce concurrency to accidental sequential traces. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21530:end -->

**为什么进入候选分母。** 摘要首要问题为“Concurrent stateful library APIs expose behavior through evolving resource ownership, lifecycle states, and competing interleavings.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present a Petri-net-guided methodology for test generation over concurrent stateful Rust APIs.

**证据证明什么。** Large language models can synthesize executable Rust tests, but their outputs often violate API preconditions, remain shallow, or reduce concurrency to accidental sequential traces.

**证据没有证明什么。** Threats to Validity The main threat is scale. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21530v1#S2.SS1 — 2.1. Bug Model; https://arxiv.org/html/2607.21530v1#S3 — 3. Formal Model。Evaluation：https://arxiv.org/html/2607.21530v1#S8 — 8. Evaluation and Results。Limitations / counterevidence：https://arxiv.org/html/2607.21530v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.21530v1#S8.SS6 — 8.6. Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Threats to Validity The main threat is scale.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21530:end -->

<!-- review:SF-2026-ARXIV-2607-21535:start -->
### Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context

<!-- claim:SF-2026-ARXIV-2607-21535:start -->Speculative decoding accelerates autoregressive generation by having a cheap draft propose tokens that a target verifies in parallel. Frontier models increasingly ship a built-in Multi-Token-Prediction (MTP/NEXTN) draft head under the assumption that the draft is negligibly cheap. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21535:end -->

**为什么进入候选分母。** 摘要首要问题为“Speculative decoding accelerates autoregressive generation by having a cheap draft propose tokens that a target verifies in parallel.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Frontier models increasingly ship a built-in Multi-Token-Prediction (MTP/NEXTN) draft head under the assumption that the draft is negligibly cheap.

**证据证明什么。** Since per-token latency is this cost divided by acceptance length, at matched acceptance end-to-end decode latency improves by the same amount, and more where windowing also lifts acceptance, while preserving the target's verified output distribution.

**证据没有证明什么。** The exact percentages are, however, config-dependent—TP degree and the KV/compute balance shift them—so we do not claim they transfer verbatim across every regime. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21535v1#S2.SS0.SSS0.Px4 — Serving systems.; https://arxiv.org/html/2607.21535v1#S4 — 4 Method: Windowed-MTP。Evaluation：https://arxiv.org/html/2607.21535v1#A4 — Appendix D Full results tables; https://arxiv.org/html/2607.21535v1#S6 — 6 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.21535v1#S7 — 7 Discussion and limitations; https://arxiv.org/html/2607.21535v1#S7.SS0.SSS0.Px9 — Limitations.。

**Artifact boundary。** Exact v1 links https://github.com/avalliappan-nvidia/windowed-mtp-b200, https://github.com/deepseek-ai/DeepSpec, https://github.com/sgl-project/sglang/pull/22077; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The exact percentages are, however, config-dependent—TP degree and the KV/compute balance shift them—so we do not claim they transfer verbatim across every regime.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21535:end -->

<!-- review:SF-2026-ARXIV-2607-21550:start -->
### X$^3$-OPD: Distilling Reasoning into Large Audio-Language Models via On-Policy Alignment

<!-- claim:SF-2026-ARXIV-2607-21550:start -->While large audio-language models have achieved remarkable progress in auditory perception, they still lag behind text-based large language models in deep logical reasoning, primarily due to the scarcity of high-quality audio reasoning data. To bridge this gap, we propose X$^3$-OPD, a cross-modal on-policy distillation framework that transfers reasoning capabilities from a powerful text teacher to an audio-language student. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21550:end -->

**为什么进入候选分母。** 摘要首要问题为“While large audio-language models have achieved remarkable progress in auditory perception, they still lag behind text-based large language models in deep logical reasoning, primarily due to the scarcity of high-quality audio reasoning data.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To bridge this gap, we propose X$^3$-OPD, a cross-modal on-policy distillation framework that transfers reasoning capabilities from a powerful text teacher to an audio-language student.

**证据证明什么。** Experiments on MMSU, MMAU, BIG Bench Audio, and MMAR demonstrate that X$^3$-OPD substantially improves audio-grounded reasoning and chain-of-thought quality while largely preserving the model's existing capabilities under domain shift.

**证据没有证明什么。** 3.2 Offline Distillation and its Limitation The standard offline distillation objective trains the student to imitate teacher trajectories sampled once and held fixed: (1) In the unimodal text setting, where and , share an input space, Eq. ( 1 ) is a faithful proxy for the population KL between teacher and student. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21550v1#S4 — 4 Method; https://arxiv.org/html/2607.21550v1#S2.SS1 — 2.1 Reasoning in Large Audio Language Models。Evaluation：https://arxiv.org/html/2607.21550v1#A1 — Appendix A Additional Experiment Details; https://arxiv.org/html/2607.21550v1#A3 — Appendix C Ablation Study。Limitations / counterevidence：https://arxiv.org/html/2607.21550v1#S3.SS2 — 3.2 Offline Distillation and its Limitation; https://arxiv.org/html/2607.21550v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：3.2 Offline Distillation and its Limitation The standard offline distillation objective trains the student to imitate teacher trajectories sampled once and held fixed: (1) In the unimodal text setting, where and , share an input space, Eq. ( 1 ) is a faithful proxy for the population KL between teacher and student.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21550:end -->

<!-- review:SF-2026-ARXIV-2607-21553:start -->
### SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation

<!-- claim:SF-2026-ARXIV-2607-21553:start -->We introduce SANA-Video 2.0, a hybrid video diffusion transformer instantiated at 5B and 14B scales under a unified architecture. Designed to generate high-quality video up to 720p on a single GPU, SANA-Video 2.0 matches full-softmax video DiTs in quality while retaining the favorable long-sequence scaling of linear attention. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21553:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce SANA-Video 2.0, a hybrid video diffusion transformer instantiated at 5B and 14B scales under a unified architecture.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We introduce SANA-Video 2.0, a hybrid video diffusion transformer instantiated at 5B and 14B scales under a unified architecture.

**证据证明什么。** Overall, our hybrid design recovers softmax-level expressiveness at substantially reduced cost, unlocking scalable long, high resolution video generation.

**证据没有证明什么。** Second, our operator is bidirectional, whereas robotics, autonomous driving, and world models require streaming, action-conditioned rollouts: as noted in Section 2 , dropping the delta-rule update makes it a natural initialization for a causal Gated DeltaNet, so pairing a causal delta-rule linear operator in the Kimi-Linear [ 14 ] / Kimi K3 [ 16 ] family with the same hybrid-plus-AttnRes layout would carry this scratch-trained, kernel-friendly recipe into causal generation and closed-loop world models, complementing the Physical AI study in Section 6 . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21553v1#A5.SS3 — E.3 Qualitative Comparison with Other Methods; https://arxiv.org/html/2607.21553v1#S3.SS2 — 3.2 Hybrid Attention Design。Evaluation：https://arxiv.org/html/2607.21553v1#A4 — Appendix D Evaluation and Measurement Protocols; https://arxiv.org/html/2607.21553v1#A4.SS1 — D.1 Sampling and VBench Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.21553v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/NVlabs/Sana, https://github.com/Wan-Video/Wan2.2, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Second, our operator is bidirectional, whereas robotics, autonomous driving, and world models require streaming, action-conditioned rollouts: as noted in Section 2 , dropping the delta-rule update makes it a natural initialization for a causal Gated DeltaNet, so pairing a causal delta-rule linear operator in the Kimi-Linear [ 14 ] / Kimi K3 [ 16 ] family with the same hybrid-plus-AttnRes layout would carry this scratch-trained, kernel-friendly recipe into causal generation and closed-loop world models, complementing the Physical AI study in Section 6 .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21553:end -->

<!-- review:SF-2026-ARXIV-2607-21557:start -->
### OpenForgeRL: Train Harness-native Agents in Any Environment

<!-- claim:SF-2026-ARXIV-2607-21557:start -->Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems. While powerful, these complex harnesses also make agents hard to train end-to-end with open infrastructure, whose SFT/RL stacks cannot natively express stateful, multi-process harness inference. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21557:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To address this, we present OpenForgeRL, an open-source framework for training harness-based agents end-to-end in diverse environments.

**证据证明什么。** We find that some harnesses are substantially harder to learn than others, and that RL improves agentic reliability, such as self-verification, tool coverage, and completing multi-step plans, though critical abilities such as error recovery remain weak.

**证据没有证明什么。** Error recovery, however, remains weak even after RL, suggesting that some capabilities may need dedicated data. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21557v1#S3 — 3 Methods。Evaluation：https://arxiv.org/html/2607.21557v1#A3 — Appendix C Evaluation Details; https://arxiv.org/html/2607.21557v1#A3.SS1 — C.1 ClawEval and QwenClawBench Evaluation Details。Limitations / counterevidence：https://arxiv.org/html/2607.21557v1#S5 — 5 Discussion; https://arxiv.org/html/2607.21557v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/zai-org/ZClawBench, https://code.claude.com/docs/en/overview, https://github.com/MiniMax-AI/MiniMax-M2.5; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Error recovery, however, remains weak even after RL, suggesting that some capabilities may need dedicated data.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21557:end -->

<!-- review:SF-2026-ARXIV-2607-21571:start -->
### Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering

<!-- claim:SF-2026-ARXIV-2607-21571:start -->Embodied question answering (EQA) is traditionally evaluated under an episodic formulation, where agents solve each task independently and reset internal state between episodes. However, real-world robots operate continuously and must accumulate, retain, and selectively reuse information acquired from prior interactions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21571:end -->

**为什么进入候选分母。** 摘要首要问题为“Embodied question answering (EQA) is traditionally evaluated under an episodic formulation, where agents solve each task independently and reset internal state between episodes.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** However, real-world robots operate continuously and must accumulate, retain, and selectively reuse information acquired from prior interactions.

**证据证明什么。** We find that simply preserving existing memory is often insufficient.

**证据没有证明什么。** Our analysis reveals a critical architectural gap: memory persistence does not guarantee knowledge accumulation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21571v1#S1 — I Introduction; https://arxiv.org/html/2607.21571v1#S2 — II Related Work。Evaluation：https://arxiv.org/html/2607.21571v1#S5 — V Experimental Results and Analysis; https://arxiv.org/html/2607.21571v1#S6.SS2 — VI-B Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.21571v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/jangablox/sequential-eqa, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Our analysis reveals a critical architectural gap: memory persistence does not guarantee knowledge accumulation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21571:end -->

<!-- review:SF-2026-ARXIV-2607-21576:start -->
### Self-Supervised Learning of Structured Dynamics from Videos

<!-- claim:SF-2026-ARXIV-2607-21576:start -->Understanding motion in video is a fundamental challenge for visual learning, as frame-to-frame change entangles two sources of dynamics: camera motion and object motion. This decomposition has remained underexplored in representation learning, partly because these factors are tightly coupled in natural videos and difficult to supervise separately. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21576:end -->

**为什么进入候选分母。** 摘要首要问题为“Understanding motion in video is a fundamental challenge for visual learning, as frame-to-frame change entangles two sources of dynamics: camera motion and object motion.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose the Structured Dynamics Model (SDM), which explicitly separates the dominant source of temporal change from residual dynamics through future-feature prediction, rather than representing video change with a single entangled latent or with unstructured, spatially dense transition tokens.

**证据证明什么。** These results suggest that pretrained image models can be readily repurposed into structured video-dynamics representations, providing a useful inductive bias for learning and analyzing latent video dynamics.

**证据没有证明什么。** SDM learns structured primary/residual motion latents through future-feature prediction, using weak scene-level supervision on synthetic videos together with unlabeled real data. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21576v1#S2 — 2 Method; https://arxiv.org/html/2607.21576v1#A1.SS8 — A.8 Supervised model evaluation。Evaluation：https://arxiv.org/html/2607.21576v1#S3.SS5 — 3.5 Analysis and Ablation Studies; https://arxiv.org/html/2607.21576v1#A1 — Appendix A Dataset and Evaluation Details。Limitations / counterevidence：https://arxiv.org/html/2607.21576v1#A3 — Appendix C Limitations; https://arxiv.org/html/2607.21576v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://lukasknobel.github.io/projects/StructuredDynamics, https://github.com/facebookresearch/dinov2/blob/7b187bd4df8efce2cbcbbb67bd01532c19bf4c9c/LICENSE, https://huggingface.co/facebook/vit-mae-base; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：SDM learns structured primary/residual motion latents through future-feature prediction, using weak scene-level supervision on synthetic videos together with unlabeled real data.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21576:end -->

<!-- review:SF-2026-ARXIV-2607-21582:start -->
### Scale Up Strategically: Learning Compositional Generalization via Bias-Aware Evaluation and Data Collection for Robotic Manipulation

<!-- claim:SF-2026-ARXIV-2607-21582:start -->Compositional generalization is essential for robot to follow diverse instructions. However, pretrained policies are known to take shortcuts, deferring to salient cues rather than grounding language. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21582:end -->

**为什么进入候选分母。** 摘要首要问题为“Compositional generalization is essential for robot to follow diverse instructions.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce a diagnostic framework that localizes this failure to individual \textit{instruction factors}, \textit{e.g.,} reusable semantic components such as color, verb, object, size, and spatial attribute.

**证据证明什么。** We further show the diagnosis is actionable: a bias-aware data collection strategy that reallocates a fixed budget toward under-grounded factors outperforms baselines in simulation and on a real robot using half the demonstrations, thereby enabling more sample-efficient and generalizable policy learning.

**证据没有证明什么。** We show that policies often over-rely on dominant instruction factors while under-grounding others, limiting compositional generalization under out-of-distribution instructions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21582v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21582v1#S2 — 2 Related Works。Evaluation：https://arxiv.org/html/2607.21582v1#A3.SS4 — C.4 Simulation experiment results; https://arxiv.org/html/2607.21582v1#A1 — Appendix A Factor Evaluation Space。Limitations / counterevidence：https://arxiv.org/html/2607.21582v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We show that policies often over-rely on dominant instruction factors while under-grounding others, limiting compositional generalization under out-of-distribution instructions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21582:end -->

<!-- review:SF-2026-ARXIV-2607-21585:start -->
### Expanding Flow Maps

<!-- claim:SF-2026-ARXIV-2607-21585:start -->Flow-based generative models have enabled remarkable progress in fast and controllable generation across continuous and discrete state spaces, yet existing parameterizations are constrained to fixed dimensions or fixed sequence lengths. Here, we introduce Expanding Generative Flows (EFlows), which define flows between distributions of increasing dimensionality along an expanding interpolant that grows the state by augmenting it with conditional noise. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21585:end -->

**为什么进入候选分母。** 摘要首要问题为“Flow-based generative models have enabled remarkable progress in fast and controllable generation across continuous and discrete state spaces, yet existing parameterizations are constrained to fixed dimensions or fixed sequence lengths.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We further extend the framework to the discrete simplex, enabling variable-size graph generation and variable-length sequence generation.

**证据证明什么。** Across both continuous and discrete modalities, we establish EFlows and EFMs as a principled framework for settings in which output size is itself a learned, controllable degree of freedom.

**证据没有证明什么。** 8 Limitations and Future Work The current version of the paper validates EFlow and EFM on a diverse array of modalities, with GEOM-QM9 having a maximum of 29 atoms, GEOM-Drugs a maximum of 181 atoms, and LM1B capped at 128-length sequences. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21585v1#S11 — 11 Discrete Sequence Implementation Details; https://arxiv.org/html/2607.21585v1#S12 — 12 Discrete Graph Implementation Details。Evaluation：https://arxiv.org/html/2607.21585v1#S13 — 13 Experiment Details; https://arxiv.org/html/2607.21585v1#S6 — 6 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.21585v1#S8 — 8 Limitations and Future Work; https://arxiv.org/html/2607.21585v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/sophtang/ExpandingFlowMaps, https://huggingface.co/ChatterjeeLab/ExpandingFlowMaps, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：8 Limitations and Future Work The current version of the paper validates EFlow and EFM on a diverse array of modalities, with GEOM-QM9 having a maximum of 29 atoms, GEOM-Drugs a maximum of 181 atoms, and LM1B capped at 128-length sequences.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21585:end -->

<!-- review:SF-2026-ARXIV-2607-21588:start -->
### AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation

<!-- claim:SF-2026-ARXIV-2607-21588:start -->Learning effective robot manipulation policies requires diverse, high-quality demonstrations, yet existing data pipelines are often difficult to scale because they rely on specialized hardware, centralized operators, or fixed task suites. We present AXIS, a growable community-driven data engine and benchmark for scalable robot learning, which enables browser-based teleoperation for large-scale demonstration collection, automatically generates and validates new manipulation tasks, and transforms community-collected demonstrations into training-ready data through automated success checking, quality filtering, trajectory smoothing, and visual and physics-based augmentation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21588:end -->

**为什么进入候选分母。** 摘要首要问题为“Learning effective robot manipulation policies requires diverse, high-quality demonstrations, yet existing data pipelines are often difficult to scale because they rely on specialized hardware, centralized operators, or fixed task suites.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Meanwhile, AXIS organizes data into task snapshots and evaluates policies with a systematic held-out protocol.

**证据证明什么。** Continual pretraining on AXIS substantially improves the overall success rate of $π_{0.5}$ by 5.8%, outperforms the model pretrained on RoboCasa365 by 37.3%, and exhibits consistent scaling with increasing data volume, with the largest gains observed under layout, sensor-noise, and camera perturbations.

**证据没有证明什么。** Future work will expand AXIS to include more robot embodiments, richer sensing modalities, longer-horizon tasks, finer-grained annotations, and active failure-driven data collection to support more generalizable and scalable robot learning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21588v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21588v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.21588v1#S5 — 5 Experiments; https://arxiv.org/html/2607.21588v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.21588v1#S6 — 6 Discussion; https://arxiv.org/html/2607.21588v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Future work will expand AXIS to include more robot embodiments, richer sensing modalities, longer-horizon tasks, finer-grained annotations, and active failure-driven data collection to support more generalizable and scalable robot learning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21588:end -->

<!-- review:SF-2026-ARXIV-2607-21591:start -->
### Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning

<!-- claim:SF-2026-ARXIV-2607-21591:start -->Diffusion and flow-matching models dominate conditional image generation, yet inference-time scaling for these models is far less developed than for autoregressive language models. Because final quality is highly sensitive to the initial noise seed, many approaches spend extra compute on seed search or resampling under a black-box reward, but typically maintaining a constant memory footprint throughout inference. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21591:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion and flow-matching models dominate conditional image generation, yet inference-time scaling for these models is far less developed than for autoregressive language models.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Because final quality is highly sensitive to the initial noise seed, many approaches spend extra compute on seed search or resampling under a black-box reward, but typically maintaining a constant memory footprint throughout inference.

**证据证明什么。** Across diffusion and flow-matching backbones, \PSP \ consistently improves reward-guided selection and achieves higher GenEval scores (automated) and better human evaluation on prompt-alignment than best-of-$N$, importance-sampling, and tree-search baselines at matched compute.

**证据没有证明什么。** The deeper, shared limitation of such selection methods is the lack of directional guidance in space, which alternatives supply only with tradeoffs: ControlNet adds training, while gradient-based guidance requires a differentiable reward and far larger inference cost for backpropagation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21591v1#S4.SS1 — 4.1 Backbone Models; https://arxiv.org/html/2607.21591v1#S4.SS7 — 4.7 Comparison to Finetuned Models。Evaluation：https://arxiv.org/html/2607.21591v1#S0.SS1 — S1 Analysis of Intermediate Rewards; https://arxiv.org/html/2607.21591v1#S0.SS10 — S10 Human Evaluations。Limitations / counterevidence：https://arxiv.org/html/2607.21591v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/rogerioagjr/psp, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：The deeper, shared limitation of such selection methods is the lack of directional guidance in space, which alternatives supply only with tradeoffs: ControlNet adds training, while gradient-based guidance requires a differentiable reward and far larger inference cost for backpropagation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21591:end -->

<!-- review:SF-2026-ARXIV-2607-21594:start -->
### Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers

<!-- claim:SF-2026-ARXIV-2607-21594:start -->Multi-agent interactive world models should not only generate consistent observations, but also maintain world states that persist across agents and evolve across views. Existing autoregressive video diffusion pipelines carry forward observation history as conditioning context, which makes shared state difficult to maintain in multi-agent and multi-view settings. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21594:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent interactive world models should not only generate consistent observations, but also maintain world states that persist across agents and evolve across views.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present WorldWeaver (W^2), a streaming multi-agent video diffusion model that augments rollout with cross-agent world state registers: learnable tokens that store shared world information, track individual agent status, and are dynamically updated after each generated chunk.

**证据证明什么。** Extensive experiments in two-agent Minecraft video generation show that explicit world-state modeling improves logical consistency and generation quality.

**证据没有证明什么。** However, we believe this is a promising direction for future work, where a world model could be aware of more complex state information, e.g., from the low-level 3D consistent visual detail to the high-level semantic relationships across agents and players. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21594v1#S3 — 3 Method; https://arxiv.org/html/2607.21594v1#S4.SS4 — 4.4 Analysis of Model Architecture。Evaluation：https://arxiv.org/html/2607.21594v1#S4 — 4 Experiments; https://arxiv.org/html/2607.21594v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.21594v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：However, we believe this is a promising direction for future work, where a world model could be aware of more complex state information, e.g., from the low-level 3D consistent visual detail to the high-level semantic relationships across agents and players.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21594:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-20434 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20434 |
| SF-2026-ARXIV-2607-20436 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20436 |
| SF-2026-ARXIV-2607-20437 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20437 |
| SF-2026-ARXIV-2607-20457 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20457 |
| SF-2026-ARXIV-2607-20464 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20464 |
| SF-2026-ARXIV-2607-20465 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20465 |
| SF-2026-ARXIV-2607-20475 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20475 |
| SF-2026-ARXIV-2607-20481 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20481 |
| SF-2026-ARXIV-2607-20490 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20490 |
| SF-2026-ARXIV-2607-20507 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20507 |
| SF-2026-ARXIV-2607-20527 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20527 |
| SF-2026-ARXIV-2607-20543 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20543 |
| SF-2026-ARXIV-2607-20548 | score_7_9 | selected | DA-20260724-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260724-01 |
| SF-2026-ARXIV-2607-20553 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20553 |
| SF-2026-ARXIV-2607-20560 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20560 |
| SF-2026-ARXIV-2607-20653 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20653 |
| SF-2026-ARXIV-2607-20668 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20668 |
| SF-2026-ARXIV-2607-20723 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20723 |
| SF-2026-ARXIV-2607-20730 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20730 |
| SF-2026-ARXIV-2607-20734 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20734 |
| SF-2026-ARXIV-2607-20757 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20757 |
| SF-2026-ARXIV-2607-20792 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20792 |
| SF-2026-ARXIV-2607-20860 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20860 |
| SF-2026-ARXIV-2607-20908 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20908 |
| SF-2026-ARXIV-2607-20972 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20972 |
| SF-2026-ARXIV-2607-20982 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-20982 |
| SF-2026-ARXIV-2607-21000 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21000 |
| SF-2026-ARXIV-2607-21005 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21005 |
| SF-2026-ARXIV-2607-21051 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21051 |
| SF-2026-ARXIV-2607-21106 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21106 |
| SF-2026-ARXIV-2607-21162 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21162 |
| SF-2026-ARXIV-2607-21224 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21224 |
| SF-2026-ARXIV-2607-21273 | score_7_9 | selected | DA-20260724-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260724-02 |
| SF-2026-ARXIV-2607-21325 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21325 |
| SF-2026-ARXIV-2607-21356 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21356 |
| SF-2026-ARXIV-2607-21475 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21475 |
| SF-2026-ARXIV-2607-21480 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21480 |
| SF-2026-ARXIV-2607-21503 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21503 |
| SF-2026-ARXIV-2607-21522 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21522 |
| SF-2026-ARXIV-2607-21535 | score_7_9 | selected | DA-20260724-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260724-03 |
| SF-2026-ARXIV-2607-21553 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21553 |
| SF-2026-ARXIV-2607-21557 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21557 |
| SF-2026-ARXIV-2607-21571 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21571 |
| SF-2026-ARXIV-2607-21594 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21594 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-20434:start -->
`SF-2026-ARXIV-2607-20434` 的 exact-v1 Deep Review 已保留。其机制为：Importantly, we propose a novel approach Diagonal Adhesive Method (DAM), which can effectively combine the two methods and mitigate the performance loss. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20434:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20436:start -->
`SF-2026-ARXIV-2607-20436` 的 exact-v1 Deep Review 已保留。其机制为：A checkpoint can appear fixed under evaluation-style prompts while the same behavior persists under ordinary-use prompts. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20436:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20437:start -->
`SF-2026-ARXIV-2607-20437` 的 exact-v1 Deep Review 已保留。其机制为：Extensive experiments are conducted on two retrieval datasets and compared with multiple baseline methods. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20437:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20457:start -->
`SF-2026-ARXIV-2607-20457` 的 exact-v1 Deep Review 已保留。其机制为：Distributed blockwise methods such as Star Attention reduce this cost by sharding context across hosts, but rely on prepending a static, content-blind copy of the first block to every host. 为避免挤压 `MODEL-LONG-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20457:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20464:start -->
`SF-2026-ARXIV-2607-20464` 的 exact-v1 Deep Review 已保留。其机制为：Self-consistency turns the variation into a per-question uncertainty estimate via majority voting. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20464:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20465:start -->
`SF-2026-ARXIV-2607-20465` 的 exact-v1 Deep Review 已保留。其机制为：DataPrep-Bench provides a unified, downstream-grounded framework for measuring progress on both capabilities as co-equal targets of LLM-driven data preparation. 为避免挤压 `TRAIN-DATA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20465:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20475:start -->
`SF-2026-ARXIV-2607-20475` 的 exact-v1 Deep Review 已保留。其机制为：We present $\textbf{SonicSampler}$, a unified suite of tile-aware Triton kernels that vertically fuses the complete sampling pipeline into a fixed, workload-aware execution model. 为避免挤压 `INFER-DECODE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20475:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20481:start -->
`SF-2026-ARXIV-2607-20481` 的 exact-v1 Deep Review 已保留。其机制为：We propose CARGO, a training-free routing framework that estimates this agreement through prompt-varied sampling, applies Bayesian early stopping for sample-efficient uncertainty control, and supports arbitrary target collaboration ratios through lightweight deployment-time calibration. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20481:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20490:start -->
`SF-2026-ARXIV-2607-20490` 的 exact-v1 Deep Review 已保留。其机制为：The framework incorporates a hardware-aware allocator with a pluggable multi-criteria decision layer that leverages real-time infrastructure metrics to enable adaptive workload placement. 为避免挤压 `PLATFORM-FOUNDATIONS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20490:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20507:start -->
`SF-2026-ARXIV-2607-20507` 的 exact-v1 Deep Review 已保留。其机制为：We propose CacheSpec, an inference optimization framework centered on reusable program caches. 为避免挤压 `INFER-SPECULATIVE-DECODING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20507:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20527:start -->
`SF-2026-ARXIV-2607-20527` 的 exact-v1 Deep Review 已保留。其机制为：We present a gold-anchored evaluation protocol and a deployable guard that make this behavior measurable and bounded. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20527:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20543:start -->
`SF-2026-ARXIV-2607-20543` 的 exact-v1 Deep Review 已保留。其机制为：We study this pass@k inversion: after training, the policy may solve fewer distinct problems than its base model at large $k$. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20543:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20553:start -->
`SF-2026-ARXIV-2607-20553` 的 exact-v1 Deep Review 已保留。其机制为：Memory Manager models are pivotal in agent systems. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20553:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20560:start -->
`SF-2026-ARXIV-2607-20560` 的 exact-v1 Deep Review 已保留。其机制为：We present Chronofy, a three-layer neuro-symbolic framework implementing the Temporal-Logical Decay Architecture (TLDA) that embeds temporal validity directly into the representation, retrieval, and reasoning layers of RAG systems. 为避免挤压 `AGENT-RAG` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20560:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20653:start -->
`SF-2026-ARXIV-2607-20653` 的 exact-v1 Deep Review 已保留。其机制为：We present PhysCoRe, a physics-corrected residual world model that couples a differentiable Material Point Method (MPM) simulator with two feed-forward neural networks. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20653:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20668:start -->
`SF-2026-ARXIV-2607-20668` 的 exact-v1 Deep Review 已保留。其机制为：TextGrad improves language-model systems by revising text from feedback. 为避免挤压 `AGENT-REFLECTION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20668:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20723:start -->
`SF-2026-ARXIV-2607-20723` 的 exact-v1 Deep Review 已保留。其机制为：LeakyLMs is the first to demonstrate that key model and deployment details can be inferred using only token generation timing, even when interacting through remote APIs. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20723:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20730:start -->
`SF-2026-ARXIV-2607-20730` 的 exact-v1 Deep Review 已保留。其机制为：Existing fact-verification benchmarks and evaluation frameworks do not provide the controlled evidence environments needed to assess robustness against GEO poisoning. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20730:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20734:start -->
`SF-2026-ARXIV-2607-20734` 的 exact-v1 Deep Review 已保留。其机制为：To study this, we introduce a framework that transforms static, single-turn tasks into dynamic multi-turn conversations in which the user's intent evolves across turns--incrementally revealed, revised, and at times redirected mid-conversation--while preserving each task's original evaluation protocol, enabling existing benchmarks to be reused as controlled testbeds without new annotation. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20734:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20757:start -->
`SF-2026-ARXIV-2607-20757` 的 exact-v1 Deep Review 已保留。其机制为：With the LLaMA-2 7B model under W4A4 quantization with group size 128, perplexity drops from 8.22 to 6.73, competing with post-training methods that require frozen models and calibration datasets. 为避免挤压 `TRAIN-PRETRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20757:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20792:start -->
`SF-2026-ARXIV-2607-20792` 的 exact-v1 Deep Review 已保留。其机制为：We test its riskiest coupling: each pondering iteration may rewrite the fast tier that the same iteration reads. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20792:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20860:start -->
`SF-2026-ARXIV-2607-20860` 的 exact-v1 Deep Review 已保留。其机制为：We present $\mathrm{IRIS}$, an audit that needs only the returned text: it asks endpoints to generate random numbers or strings, fingerprints the backend, and is the first to combine, in one text-only audit, detection of whole-stream substitution and fractional dilution, attribution of the served backend, routing-fraction ($ε$) estimation, and a query budget it sizes itself. 为避免挤压 `PLATFORM-GATEWAY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20860:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20908:start -->
`SF-2026-ARXIV-2607-20908` 的 exact-v1 Deep Review 已保留。其机制为：In this work, we propose CudaPerf, a reflective RL framework that incorporates both verifiable execution rewards and structural code-aware rewards derived from parallelization features (e.g., memory coalescing, occupancy, Arithmatic Intensity, and synchronization patterns). 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20908:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20972:start -->
`SF-2026-ARXIV-2607-20972` 的 exact-v1 Deep Review 已保留。其机制为：Instruction files, plan artifacts, and auto-written memory directories are deliberately authored and deliberately retrieved: the agent must choose to write them and choose to read them back. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20972:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20982:start -->
`SF-2026-ARXIV-2607-20982` 的 exact-v1 Deep Review 已保留。其机制为：We present GuardianAgentBench (GABench), a benchmark of 580 scenarios across six domains evaluated on three production-ready frameworks: LangChain, LlamaIndex, and Vectara. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-20982:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21000:start -->
`SF-2026-ARXIV-2607-21000` 的 exact-v1 Deep Review 已保留。其机制为：Continuous-time-parameterized state-space models (SSMs) such as Mamba obtain their discrete recurrence by zero-order-hold discretization of a continuous-time system; we argue that this detour is unnecessary for memory tracking and parameterize the discrete transition directly. 为避免挤压 `MODEL-LONG-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21000:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21005:start -->
`SF-2026-ARXIV-2607-21005` 的 exact-v1 Deep Review 已保留。其机制为：We argue that, in practical deep neural network training, there is an additional and often overlooked \emph{weight-norm criticality}. 为避免挤压 `TRAIN-PRETRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21005:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21051:start -->
`SF-2026-ARXIV-2607-21051` 的 exact-v1 Deep Review 已保留。其机制为：In-context learning offers a highly sample-efficient way for agents to learn from their own interaction histories, but its gains disappear once that experience is removed from the context. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21051:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21106:start -->
`SF-2026-ARXIV-2607-21106` 的 exact-v1 Deep Review 已保留。其机制为：We propose AttriMem, an attribution-guided process-feedback framework for learning memory-construction policies with RL. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21106:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21162:start -->
`SF-2026-ARXIV-2607-21162` 的 exact-v1 Deep Review 已保留。其机制为：We present GKR-HND, a registered-model protocol for verifying the polynomial backbone of Homomorphic--Nonhomomorphic Decomposition Transformers. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21162:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21224:start -->
`SF-2026-ARXIV-2607-21224` 的 exact-v1 Deep Review 已保留。其机制为：This paper studies synchronization frequency as a systems parameter for communication-constrained distributed training. 为避免挤压 `TRAIN-DISTRIBUTED-TRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21224:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21325:start -->
`SF-2026-ARXIV-2607-21325` 的 exact-v1 Deep Review 已保留。其机制为：We further identify and formalize the structural separation among identity binding, authorization-request binding, and runtime execution binding as a central open problem in the design of secure agentic systems (a distinction {not explicitly addressed by} current agentic security frameworks) and present a falsifiable research agenda for its resolution. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21325:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21356:start -->
`SF-2026-ARXIV-2607-21356` 的 exact-v1 Deep Review 已保留。其机制为：We ask why the narrow lesson generalizes at all, and we find that narrow fine-tuning recruits a persona structure that is present in the model before the fine-tune exists. 为避免挤压 `TRAIN-SFT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21356:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21475:start -->
`SF-2026-ARXIV-2607-21475` 的 exact-v1 Deep Review 已保留。其机制为：On real long-term conversations the gated system returns the full-cache score inside the heavy-damage regime, and the rule that triggers it is the same across five model families. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21475:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21480:start -->
`SF-2026-ARXIV-2607-21480` 的 exact-v1 Deep Review 已保留。其机制为：We study how many audit labels are needed to certify, with finite-sample validity, that this missed relevant mass is small, and our main results characterise the label complexity of this problem. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21480:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21503:start -->
`SF-2026-ARXIV-2607-21503` 的 exact-v1 Deep Review 已保留。其机制为：Agents drown in their own accumulating history while paying a token cost that grows every turn, producing missing recalls within and across conversations. 为避免挤压 `AGENT-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21503:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21522:start -->
`SF-2026-ARXIV-2607-21522` 的 exact-v1 Deep Review 已保留。其机制为：We present GS-Agent, an end-to-end multi-agent framework that integrates physics engines in the loop to generate realistic, dynamic, and controllable 4D physical worlds from natural language. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21522:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21553:start -->
`SF-2026-ARXIV-2607-21553` 的 exact-v1 Deep Review 已保留。其机制为：We introduce SANA-Video 2.0, a hybrid video diffusion transformer instantiated at 5B and 14B scales under a unified architecture. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21553:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21557:start -->
`SF-2026-ARXIV-2607-21557` 的 exact-v1 Deep Review 已保留。其机制为：To address this, we present OpenForgeRL, an open-source framework for training harness-based agents end-to-end in diverse environments. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21557:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21571:start -->
`SF-2026-ARXIV-2607-21571` 的 exact-v1 Deep Review 已保留。其机制为：However, real-world robots operate continuously and must accumulate, retain, and selectively reuse information acquired from prior interactions. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21571:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21594:start -->
`SF-2026-ARXIV-2607-21594` 的 exact-v1 Deep Review 已保留。其机制为：We present WorldWeaver (W^2), a streaming multi-agent video diffusion model that augments rollout with cross-agent world state registers: learnable tokens that store shared world information, track individual agent status, and are dynamically updated after each generated chunk. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21594:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260724-01:start -->
### SOAP, Muon, and Beyond: Pushing LLM Pretraining Scales

**约束变化与机制。** To enable efficient training at large scale, we introduce a layer-wise distributed optimizer compatible with Megatron-LM.

**证明与未证明。** Additionally, we identify and build specific system-level improvements to further accelerate our layer-wise implementation. 但 Furthermore, the KL-SOAP variant emerged as the most effective approach overall; therefore, in scenarios where memory footprint is not a limiting factor, we recommend KL-SOAP over Muon. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Furthermore, the KL-SOAP variant emerged as the most effective approach overall; therefore, in scenarios where memory footprint is not a limiting factor, we recommend KL-SOAP over Muon. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-20548`。
<!-- analysis:DA-20260724-01:end -->

<!-- analysis:DA-20260724-02:start -->
### The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and The Channel, Not the Content, Decides What Works

**约束变化与机制。** No ALFWorld or WebShop reward-channel variant measurably beats its matched-normalization baseline and no gold signal measurably outperforms its content-free placebo: the delivery channel, not the content, decides; which channel is safe is regime-dependent.

**证明与未证明。** No ALFWorld or WebShop reward-channel variant measurably beats its matched-normalization baseline and no gold signal measurably outperforms its content-free placebo: the delivery channel, not the content, decides; which channel is safe is regime-dependent. 但 Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-21273`。
<!-- analysis:DA-20260724-02:end -->

<!-- analysis:DA-20260724-03:start -->
### Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context

**约束变化与机制。** Frontier models increasingly ship a built-in Multi-Token-Prediction (MTP/NEXTN) draft head under the assumption that the draft is negligibly cheap.

**证明与未证明。** Since per-token latency is this cost divided by acceptance length, at matched acceptance end-to-end decode latency improves by the same amount, and more where windowing also lifts acceptance, while preserving the target's verified output distribution. 但 The exact percentages are, however, config-dependent—TP degree and the KV/compute balance shift them—so we do not claim they transfer verbatim across every regime. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The exact percentages are, however, config-dependent—TP degree and the KV/compute balance shift them—so we do not claim they transfer verbatim across every regime. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-21535`。
<!-- analysis:DA-20260724-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260724-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260724 | GAP-20260724-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260724-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260724-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260724-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260724-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260724-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260724-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

442 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：23
- `incremental_method_without_durable_system_delta`：343
- `local_benchmark_without_release_delta`：14
- `prior_retained_candidate`：6
- `theory_without_ai_system_contract`：8
- `vertical_application_without_system_delta`：48

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 42、No Change 71、Structural 0；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/24/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [Knowledge Injection Exists in MoE? Exploring Expert-Aware Contrast Decoding in MoE for Mitigating LLMs'Hallucinations](https://arxiv.org/html/2607.20426v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Is MoE Routing a Huffman Code? Discovering the Frequency-Diversity Law in Chain-of-Thought](https://arxiv.org/html/2607.20427v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Position: Natural Language Should Not Fully Replace Formal Languages](https://arxiv.org/html/2607.20432v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Moir: Let the Model Direct Its Own Story for Robust Cross-Domain Knowledge Editing](https://arxiv.org/html/2607.20433v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Break Through the Compression Bottleneck: From Theory to Practice](https://arxiv.org/html/2607.20434v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Routing Subspaces: Auditing Evaluation-to-Deployment Mismatch in Fine-Tuned Language Models](https://arxiv.org/html/2607.20436v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [TopoGuard: Graph Theory Based Defenses Against Split-Knowledge Attacks on RAG](https://arxiv.org/html/2607.20437v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Preference Tuning as Spectral Update Reorganization](https://arxiv.org/html/2607.20438v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Dropping the Anchor: Statistical Context Summarization for Distributed Systems via Pulsar Attention](https://arxiv.org/html/2607.20457v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Stochastic Sampling is Epistemically Shallow: The Dimensionality Gap Between Temperature Variation and Model Diversity in LLMs](https://arxiv.org/html/2607.20464v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [DataPrep-Bench: Benchmarking LLMs as Training Data Preparators](https://arxiv.org/html/2607.20465v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [JAXBench: Benchmarking Autonomous TPU Kernel Optimization](https://arxiv.org/html/2607.20466v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [DC-Leap: Training-Free Acceleration of dLLMs via Draft-Guided Contiguous Leaping Decoding](https://arxiv.org/html/2607.20467v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents](https://arxiv.org/html/2607.20468v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Incomplete Prompt Jailbreaks in Large Language Models](https://arxiv.org/html/2607.20473v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [SonicSampler: Unified Tile-Aware Kernels for LLM Sampling and Speculative Verification](https://arxiv.org/html/2607.20475v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Verifier-First Evaluation of Agentic LLMs for Infrastructure-as-Code Generation](https://arxiv.org/html/2607.20478v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Routing Without Training: Controllable-Ratio LLM Offloading via Reliability Gating](https://arxiv.org/html/2607.20481v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Tractable Hierarchical Control of Autoregressive Language Models](https://arxiv.org/html/2607.20483v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Autonomous Topology Mutation: Safe Runtime Restructuring for Multi-Agent LLM Systems with Capability, State, and Shadow Invariants](https://arxiv.org/html/2607.20488v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [CRAWO: Custom Resources for Adaptive Workload Orchestration](https://arxiv.org/html/2607.20490v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Workload-Aware Caching for Multi-Agent Systems](https://arxiv.org/html/2607.20495v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [MKEvolve: A Modular Multi-Agent Framework for Kernel Code Generation](https://arxiv.org/html/2607.20501v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [CacheSpec: Finding the Sweet Spot for Small Models in Large Language Models](https://arxiv.org/html/2607.20507v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [The Active Ingredient in Muon's Grokking](https://arxiv.org/html/2607.20512v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [CANN Bench: Benchmarking Agent Generated Kernels against Real NPU and Algorithmic Limits](https://arxiv.org/html/2607.20518v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Attention Degradation, Function Token Anchoring, and the Limits of Attention-Based Intervention in Large Language Models](https://arxiv.org/html/2607.20524v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [ConfidenceBench: Evaluating Confidence Calibration in Large Language Models](https://arxiv.org/html/2607.20526v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis](https://arxiv.org/html/2607.20527v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [DynamicMCPBench: A Trace-Grounded, Effect-Scored Benchmark for LLM Agents over Live MCP Servers](https://arxiv.org/html/2607.20531v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [AppWorld-UL: Benchmarking Diverse Agent-User Interactions for Tool-Use](https://arxiv.org/html/2607.20536v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Codec-Gauge: Learning Compression-Friendly Gauges for Transformer KV Caches](https://arxiv.org/html/2607.20538v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k Inversion](https://arxiv.org/html/2607.20543v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [SOAP, Muon, and Beyond: Pushing LLM Pretraining Scales](https://arxiv.org/html/2607.20548v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [CMI-Mem: Toward Generalizable Long-Term Memory Management via CMI-Augmented Reinforcement Learning](https://arxiv.org/html/2607.20553v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [StabilityBench: Benchmarking Instability in LLMs](https://arxiv.org/html/2607.20558v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Chronofy: A Temporal-Logical Decay Architecture for Information Validity in Time-Aware Retrieval-Augmented Generation](https://arxiv.org/html/2607.20560v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [When Does Recurrence Become an Algorithm? Convergence Selection in Weight-Tied Looped Transformers](https://arxiv.org/html/2607.20594v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Are Single-Token Sparse Autoencoder Features Causally Necessary? Layer-Depth and SAE-Family Effects](https://arxiv.org/html/2607.20596v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Scaling Interpretable Transformers with Parity Bottleneck Layers](https://arxiv.org/html/2607.20652v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics](https://arxiv.org/html/2607.20653v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [From Agent Failures to Text Policies: What Works and What Breaks](https://arxiv.org/html/2607.20668v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [NVIDIA-labs OO Agents: Native Python Object-Oriented Agents](https://arxiv.org/html/2607.20709v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Evaluating Large Language Models for Symbolic Security Protocol Analysis](https://arxiv.org/html/2607.20712v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Leaky Language Models: Stealing Architecture and Inference Optimizations via Per-Token Timing](https://arxiv.org/html/2607.20723v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Operational Identity: A Finite Audit of Declared and Implemented Rules of Sameness](https://arxiv.org/html/2607.20729v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [GPE: Evaluating Robust Evidence Aggregation for Fact Verification under Controllable GEO-Style Poisoning](https://arxiv.org/html/2607.20730v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [LLMs Get Lost in Evolving User Intent](https://arxiv.org/html/2607.20734v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Pipelined Gradient Coding](https://arxiv.org/html/2607.20739v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries](https://arxiv.org/html/2607.20757v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests](https://arxiv.org/html/2607.20759v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [ArbiGraph: Arbitrarily Scalable Verifiable Task Graphs for Evaluating Context Management](https://arxiv.org/html/2607.20764v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Are Diversity Metrics Measuring Diversity? A Capability-Controlled Audit of Majority-Vote Gain in LLM Ensembles](https://arxiv.org/html/2607.20768v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Emergent Compositional Skills in Mixture-of-Experts VLAs](https://arxiv.org/html/2607.20771v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Refusal-Gated Decoding: Preserving Refusal Behavior Under High-Temperature Sampling](https://arxiv.org/html/2607.20791v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Memoir: Should a Model Write to Its Memory While It Thinks?](https://arxiv.org/html/2607.20792v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Auditing Provenance Sensitivity in LLM Agent Action Selection](https://arxiv.org/html/2607.20827v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Code Monitor Red Teaming for Public-Test-Passing Code](https://arxiv.org/html/2607.20852v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways](https://arxiv.org/html/2607.20860v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Position Bias is Hidden Behind Ceiling Effects: A Permutation Diagnostic for LLM Benchmarks](https://arxiv.org/html/2607.20864v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [TwistedMerge: Certified Higher-Order Diagnostics and Abstention for Model Merging](https://arxiv.org/html/2607.20887v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions](https://arxiv.org/html/2607.20891v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Multi-turn RL with Structural and Performance Aware Rewards for CUDA Kernel Generation](https://arxiv.org/html/2607.20908v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction](https://arxiv.org/html/2607.20911v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [OPOD: On-Policy Omni Distillation](https://arxiv.org/html/2607.20918v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Ms. Forcing: Efficient Streaming Video Generation with Multi-Scale Patchification and Attention](https://arxiv.org/html/2607.20940v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Best-of-Evidence: Best-of-N Selection under Partial Verification](https://arxiv.org/html/2607.20950v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Delivery, Not Storage: Cue-Anchored Working Memory as a Harness Property for Coding Agents](https://arxiv.org/html/2607.20972v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [GuardianAgentBench: Where Agents Fail and How to Guard Them](https://arxiv.org/html/2607.20982v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Workflow-Localized Mechanism Learning: Attribution-Guided Repair and Knowledge Reuse for Structured Agent Skills](https://arxiv.org/html/2607.20999v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Naju: A Native Discrete State-Space Model with Independent Retention and Writing for Long-Sequence Memory](https://arxiv.org/html/2607.21000v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Weight-norm Criticality: A Mechanism for Loss Spikes Induced by the Normalization and Weight Decay](https://arxiv.org/html/2607.21005v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Faster IndexTTS-2: Accelerating and Streaming Autoregressive Zero-Shot Text-to-Speech Synthesis on GPUs](https://arxiv.org/html/2607.21042v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Sample-Efficient Learning from Agent Experience](https://arxiv.org/html/2607.21051v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Training Large Language Models for Self-Explanation Faithfulness](https://arxiv.org/html/2607.21090v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [AttriMem: Attribution-Guided Process Feedback for Agent Memory Construction](https://arxiv.org/html/2607.21106v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Relative Value Learning](https://arxiv.org/html/2607.21120v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Hardware-Software Co-Design for Float16 On-Device Training on RISC-V Single-Core](https://arxiv.org/html/2607.21130v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [One More Turn, Less Regret: A Regret-Based Multi-Turn Benchmark for LLMs' Clarification Policies](https://arxiv.org/html/2607.21143v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [V-DEAL: Diagnosing Video Safety De-Calibration as an Understanding-Refusal Coupling Failure](https://arxiv.org/html/2607.21151v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Agree on the Model, Verify the Inference: GKR Protocols for HND-Based Transformer Inference](https://arxiv.org/html/2607.21162v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Out of Sight, Still in Mind: Token Compression for Omni-LLMs](https://arxiv.org/html/2607.21179v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders](https://arxiv.org/html/2607.21217v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Controlled Periodic Synchronization for Efficient Data-Parallel Training](https://arxiv.org/html/2607.21224v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and The Channel, Not the Content, Decides What Works](https://arxiv.org/html/2607.21273v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs](https://arxiv.org/html/2607.21291v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Cryptographically verifiable authorization for autonomous AI agents: A falsifiable hypothesis and proof-of-concept](https://arxiv.org/html/2607.21325v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [How Many Bits Can an Adapter Write? Measuring the Capacity and Memorization of Parameter-Efficient Fine-Tuning](https://arxiv.org/html/2607.21351v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Emergent Misalignment Recruits a Pre-existing Persona Subspace](https://arxiv.org/html/2607.21356v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Mean-to-Score Discrete Diffusion: Posterior-Mean Denoisers for Score Entropy](https://arxiv.org/html/2607.21372v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [When Are Reasoning-Based Guardrails Not Efficient? ResponseGuard: A Fast Vision-Language Guard for Real-Time Moderation](https://arxiv.org/html/2607.21401v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [MemTools: A Unified Research Framework for Interoperable Agent Memory](https://arxiv.org/html/2607.21404v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Anti-Periodic Positional Encoding: Möbius Boundary Conditions Make In-Context Retrieval Reliable](https://arxiv.org/html/2607.21405v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning](https://arxiv.org/html/2607.21419v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence in Chain-of-Thought Models](https://arxiv.org/html/2607.21433v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Test-Time Scaling via Error Localization](https://arxiv.org/html/2607.21453v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Error Certificates for KV-Cache Eviction via Randomized Design](https://arxiv.org/html/2607.21475v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Finite-Sample Coverage Audits for High-Recall Candidate Generation: Certification and Learning-Theoretic Design](https://arxiv.org/html/2607.21480v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks](https://arxiv.org/pdf/2607.21482v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems](https://arxiv.org/html/2607.21503v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [GS-Agent: Creating 4D Physical Worlds With Generative Simulation](https://arxiv.org/html/2607.21522v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [From Resource Flow to Executable Tests: Petri-Net-Guided LLM Test Generation for Concurrent Stateful Rust APIs](https://arxiv.org/html/2607.21530v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context](https://arxiv.org/html/2607.21535v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [X$^3$-OPD: Distilling Reasoning into Large Audio-Language Models via On-Policy Alignment](https://arxiv.org/html/2607.21550v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation](https://arxiv.org/html/2607.21553v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/html/2607.21557v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering](https://arxiv.org/html/2607.21571v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Self-Supervised Learning of Structured Dynamics from Videos](https://arxiv.org/html/2607.21576v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Scale Up Strategically: Learning Compositional Generalization via Bias-Aware Evaluation and Data Collection for Robotic Manipulation](https://arxiv.org/html/2607.21582v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Expanding Flow Maps](https://arxiv.org/html/2607.21585v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation](https://arxiv.org/html/2607.21588v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning](https://arxiv.org/html/2607.21591v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04
- [Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers](https://arxiv.org/html/2607.21594v1) — first-public（Asia/Shanghai）：2026-07-24；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、113/113 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
