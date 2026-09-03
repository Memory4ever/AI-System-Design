# Daily Research — 2026-07-28

**Research Date:** 2026-07-28

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-27 09:00:00 ～ 2026-07-28 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **1022** 个 identity；全量 title + abstract 筛选后冻结 **199** 个候选与 **823** 个 family-specific closure，retain rate **19.47%**。exact-v1 Review 为 199/199：Deep 49、Standard 150、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-28 |
| Window End | 2026-07-28 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-28-0900-v2.1-sha256:894ed6d94d94d7e49d3fa6a2bcaa31fd636b80ea39ef7ec4b074903e0f89cba9 |
| Denominator Frozen At | 2026-09-03T21:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260728:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-27T09:00:00+08:00 | 2026-07-28T09:00:00+08:00 | 2026-09-03T21:00:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 1022 | SF-2026-ARXIV-2607-22545;SF-2026-ARXIV-2607-22554;SF-2026-ARXIV-2607-22556;SF-2026-ARXIV-2607-22561;SF-2026-ARXIV-2607-22562;SF-2026-ARXIV-2607-22569;SF-2026-ARXIV-2607-22570;SF-2026-ARXIV-2607-22577;SF-2026-ARXIV-2607-22578;SF-2026-ARXIV-2607-22584;SF-2026-ARXIV-2607-22585;SF-2026-ARXIV-2607-22586;SF-2026-ARXIV-2607-22595;SF-2026-ARXIV-2607-22600;SF-2026-ARXIV-2607-22610;SF-2026-ARXIV-2607-22611;SF-2026-ARXIV-2607-22614;SF-2026-ARXIV-2607-22625;SF-2026-ARXIV-2607-22629;SF-2026-ARXIV-2607-22634;SF-2026-ARXIV-2607-22643;SF-2026-ARXIV-2607-22648;SF-2026-ARXIV-2607-22651;SF-2026-ARXIV-2607-22661;SF-2026-ARXIV-2607-22662;SF-2026-ARXIV-2607-22663;SF-2026-ARXIV-2607-22671;SF-2026-ARXIV-2607-22676;SF-2026-ARXIV-2607-22688;SF-2026-ARXIV-2607-22689;SF-2026-ARXIV-2607-22690;SF-2026-ARXIV-2607-22695;SF-2026-ARXIV-2607-22697;SF-2026-ARXIV-2607-22708;SF-2026-ARXIV-2607-22711;SF-2026-ARXIV-2607-22716;SF-2026-ARXIV-2607-22724;SF-2026-ARXIV-2607-22726;SF-2026-ARXIV-2607-22758;SF-2026-ARXIV-2607-22766;SF-2026-ARXIV-2607-22769;SF-2026-ARXIV-2607-22781;SF-2026-ARXIV-2607-22785;SF-2026-ARXIV-2607-22790;SF-2026-ARXIV-2607-22798;SF-2026-ARXIV-2607-22807;SF-2026-ARXIV-2607-22832;SF-2026-ARXIV-2607-22854;SF-2026-ARXIV-2607-22868;SF-2026-ARXIV-2607-22872;SF-2026-ARXIV-2607-22880;SF-2026-ARXIV-2607-22883;SF-2026-ARXIV-2607-22898;SF-2026-ARXIV-2607-22917;SF-2026-ARXIV-2607-22925;SF-2026-ARXIV-2607-22926;SF-2026-ARXIV-2607-22927;SF-2026-ARXIV-2607-22949;SF-2026-ARXIV-2607-22951;SF-2026-ARXIV-2607-22953;SF-2026-ARXIV-2607-22962;SF-2026-ARXIV-2607-22997;SF-2026-ARXIV-2607-22999;SF-2026-ARXIV-2607-23002;SF-2026-ARXIV-2607-23012;SF-2026-ARXIV-2607-23015;SF-2026-ARXIV-2607-23045;SF-2026-ARXIV-2607-23046;SF-2026-ARXIV-2607-23047;SF-2026-ARXIV-2607-23050;SF-2026-ARXIV-2607-23054;SF-2026-ARXIV-2607-23055;SF-2026-ARXIV-2607-23089;SF-2026-ARXIV-2607-23099;SF-2026-ARXIV-2607-23115;SF-2026-ARXIV-2607-23123;SF-2026-ARXIV-2607-23147;SF-2026-ARXIV-2607-23159;SF-2026-ARXIV-2607-23193;SF-2026-ARXIV-2607-23226;SF-2026-ARXIV-2607-23250;SF-2026-ARXIV-2607-23263;SF-2026-ARXIV-2607-23264;SF-2026-ARXIV-2607-23265;SF-2026-ARXIV-2607-23332;SF-2026-ARXIV-2607-23361;SF-2026-ARXIV-2607-23364;SF-2026-ARXIV-2607-23366;SF-2026-ARXIV-2607-23373;SF-2026-ARXIV-2607-23379;SF-2026-ARXIV-2607-23386;SF-2026-ARXIV-2607-23390;SF-2026-ARXIV-2607-23394;SF-2026-ARXIV-2607-23402;SF-2026-ARXIV-2607-23425;SF-2026-ARXIV-2607-23438;SF-2026-ARXIV-2607-23444;SF-2026-ARXIV-2607-23445;SF-2026-ARXIV-2607-23458;SF-2026-ARXIV-2607-23472;SF-2026-ARXIV-2607-23478;SF-2026-ARXIV-2607-23496;SF-2026-ARXIV-2607-23504;SF-2026-ARXIV-2607-23514;SF-2026-ARXIV-2607-23517;SF-2026-ARXIV-2607-23532;SF-2026-ARXIV-2607-23545;SF-2026-ARXIV-2607-23581;SF-2026-ARXIV-2607-23586;SF-2026-ARXIV-2607-23588;SF-2026-ARXIV-2607-23602;SF-2026-ARXIV-2607-23605;SF-2026-ARXIV-2607-23624;SF-2026-ARXIV-2607-23670;SF-2026-ARXIV-2607-23693;SF-2026-ARXIV-2607-23700;SF-2026-ARXIV-2607-23702;SF-2026-ARXIV-2607-23704;SF-2026-ARXIV-2607-23710;SF-2026-ARXIV-2607-23711;SF-2026-ARXIV-2607-23722;SF-2026-ARXIV-2607-23731;SF-2026-ARXIV-2607-23765;SF-2026-ARXIV-2607-23771;SF-2026-ARXIV-2607-23782;SF-2026-ARXIV-2607-23783;SF-2026-ARXIV-2607-23802;SF-2026-ARXIV-2607-23809;SF-2026-ARXIV-2607-23815;SF-2026-ARXIV-2607-23838;SF-2026-ARXIV-2607-23844;SF-2026-ARXIV-2607-23870;SF-2026-ARXIV-2607-23884;SF-2026-ARXIV-2607-23909;SF-2026-ARXIV-2607-23927;SF-2026-ARXIV-2607-23929;SF-2026-ARXIV-2607-23933;SF-2026-ARXIV-2607-23955;SF-2026-ARXIV-2607-23969;SF-2026-ARXIV-2607-23991;SF-2026-ARXIV-2607-23999;SF-2026-ARXIV-2607-24008;SF-2026-ARXIV-2607-24010;SF-2026-ARXIV-2607-24027;SF-2026-ARXIV-2607-24054;SF-2026-ARXIV-2607-24063;SF-2026-ARXIV-2607-24097;SF-2026-ARXIV-2607-24112;SF-2026-ARXIV-2607-24117;SF-2026-ARXIV-2607-24148;SF-2026-ARXIV-2607-24157;SF-2026-ARXIV-2607-24159;SF-2026-ARXIV-2607-24162;SF-2026-ARXIV-2607-24165;SF-2026-ARXIV-2607-24167;SF-2026-ARXIV-2607-24174;SF-2026-ARXIV-2607-24223;SF-2026-ARXIV-2607-24260;SF-2026-ARXIV-2607-24267;SF-2026-ARXIV-2607-24268;SF-2026-ARXIV-2607-24280;SF-2026-ARXIV-2607-24300;SF-2026-ARXIV-2607-24306;SF-2026-ARXIV-2607-24331;SF-2026-ARXIV-2607-24343;SF-2026-ARXIV-2607-24368;SF-2026-ARXIV-2607-24377;SF-2026-ARXIV-2607-24392;SF-2026-ARXIV-2607-24407;SF-2026-ARXIV-2607-24434;SF-2026-ARXIV-2607-24440;SF-2026-ARXIV-2607-24459;SF-2026-ARXIV-2607-24471;SF-2026-ARXIV-2607-24481;SF-2026-ARXIV-2607-24484;SF-2026-ARXIV-2607-24485;SF-2026-ARXIV-2607-24507;SF-2026-ARXIV-2607-24516;SF-2026-ARXIV-2607-24539;SF-2026-ARXIV-2607-24555;SF-2026-ARXIV-2607-24562;SF-2026-ARXIV-2607-24570;SF-2026-ARXIV-2607-24582;SF-2026-ARXIV-2607-24585;SF-2026-ARXIV-2607-24586;SF-2026-ARXIV-2607-24593;SF-2026-ARXIV-2607-24604;SF-2026-ARXIV-2607-24625;SF-2026-ARXIV-2607-24645;SF-2026-ARXIV-2607-24647;SF-2026-ARXIV-2607-24651;SF-2026-ARXIV-2607-24653;SF-2026-ARXIV-2607-24663;SF-2026-ARXIV-2607-24665;SF-2026-ARXIV-2607-24667;SF-2026-ARXIV-2607-24692;SF-2026-ARXIV-2607-24717;SF-2026-ARXIV-2607-24720;SF-2026-ARXIV-2607-24731 | all registered category pages; cross-category dedup complete | 2026-07-28T09:00:00+08:00 | sha256:894ed6d94d94d7e49d3fa6a2bcaa31fd636b80ea39ef7ec4b074903e0f89cba9 | — |
<!-- coverage:SRC-ARXIV:20260728:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-22545 | arXiv:2607.22545v1 | paper-v1:2607.22545 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22545 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22554 | arXiv:2607.22554v1 | paper-v1:2607.22554 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22554 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22556 | arXiv:2607.22556v1 | paper-v1:2607.22556 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22556 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22561 | arXiv:2607.22561v1 | paper-v1:2607.22561 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22561 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22562 | arXiv:2607.22562v1 | paper-v1:2607.22562 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22562 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22569 | arXiv:2607.22569v1 | paper-v1:2607.22569 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22569 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22570 | arXiv:2607.22570v1 | paper-v1:2607.22570 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22570 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22577 | arXiv:2607.22577v1 | paper-v1:2607.22577 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22577 | self | — | new_in_window | PLATFORM-COST | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22578 | arXiv:2607.22578v1 | paper-v1:2607.22578 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22578 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22584 | arXiv:2607.22584v1 | paper-v1:2607.22584 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22584 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22585 | arXiv:2607.22585v1 | paper-v1:2607.22585 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22585 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22586 | arXiv:2607.22586v1 | paper-v1:2607.22586 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22586 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22595 | arXiv:2607.22595v1 | paper-v1:2607.22595 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22595 | self | — | new_in_window | PLATFORM-TRACE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22600 | arXiv:2607.22600v1 | paper-v1:2607.22600 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22600 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22610 | arXiv:2607.22610v1 | paper-v1:2607.22610 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22610 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22611 | arXiv:2607.22611v1 | paper-v1:2607.22611 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22611 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22614 | arXiv:2607.22614v1 | paper-v1:2607.22614 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22614 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22625 | arXiv:2607.22625v1 | paper-v1:2607.22625 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22625 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22629 | arXiv:2607.22629v1 | paper-v1:2607.22629 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22629 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22634 | arXiv:2607.22634v1 | paper-v1:2607.22634 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22634 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22643 | arXiv:2607.22643v1 | paper-v1:2607.22643 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22643 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22648 | arXiv:2607.22648v1 | paper-v1:2607.22648 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22648 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22651 | arXiv:2607.22651v1 | paper-v1:2607.22651 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22651 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22661 | arXiv:2607.22661v1 | paper-v1:2607.22661 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22661 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22662 | arXiv:2607.22662v1 | paper-v1:2607.22662 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22662 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22663 | arXiv:2607.22663v1 | paper-v1:2607.22663 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22663 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22671 | arXiv:2607.22671v1 | paper-v1:2607.22671 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22671 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22676 | arXiv:2607.22676v1 | paper-v1:2607.22676 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22676 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22688 | arXiv:2607.22688v1 | paper-v1:2607.22688 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22688 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22689 | arXiv:2607.22689v1 | paper-v1:2607.22689 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22689 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22690 | arXiv:2607.22690v1 | paper-v1:2607.22690 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22690 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22695 | arXiv:2607.22695v1 | paper-v1:2607.22695 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22695 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22697 | arXiv:2607.22697v1 | paper-v1:2607.22697 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22697 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22708 | arXiv:2607.22708v1 | paper-v1:2607.22708 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22708 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22711 | arXiv:2607.22711v1 | paper-v1:2607.22711 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22711 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22716 | arXiv:2607.22716v1 | paper-v1:2607.22716 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22716 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22724 | arXiv:2607.22724v1 | paper-v1:2607.22724 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22724 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22726 | arXiv:2607.22726v1 | paper-v1:2607.22726 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22726 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22758 | arXiv:2607.22758v1 | paper-v1:2607.22758 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22758 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22766 | arXiv:2607.22766v1 | paper-v1:2607.22766 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22766 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22769 | arXiv:2607.22769v1 | paper-v1:2607.22769 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22769 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22781 | arXiv:2607.22781v1 | paper-v1:2607.22781 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22781 | self | — | new_in_window | MODEL-SELF-ATTENTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22785 | arXiv:2607.22785v1 | paper-v1:2607.22785 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22785 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22790 | arXiv:2607.22790v1 | paper-v1:2607.22790 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22790 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22798 | arXiv:2607.22798v1 | paper-v1:2607.22798 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22798 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22807 | arXiv:2607.22807v1 | paper-v1:2607.22807 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22807 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22832 | arXiv:2607.22832v1 | paper-v1:2607.22832 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22832 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22854 | arXiv:2607.22854v1 | paper-v1:2607.22854 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22854 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22868 | arXiv:2607.22868v1 | paper-v1:2607.22868 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22868 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22872 | arXiv:2607.22872v1 | paper-v1:2607.22872 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22872 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22880 | arXiv:2607.22880v1 | paper-v1:2607.22880 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22880 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22883 | arXiv:2607.22883v1 | paper-v1:2607.22883 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22883 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22898 | arXiv:2607.22898v1 | paper-v1:2607.22898 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22898 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22917 | arXiv:2607.22917v1 | paper-v1:2607.22917 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22917 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22925 | arXiv:2607.22925v1 | paper-v1:2607.22925 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22925 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22926 | arXiv:2607.22926v1 | paper-v1:2607.22926 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22926 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22927 | arXiv:2607.22927v1 | paper-v1:2607.22927 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22927 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22949 | arXiv:2607.22949v1 | paper-v1:2607.22949 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22949 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22951 | arXiv:2607.22951v1 | paper-v1:2607.22951 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22951 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22953 | arXiv:2607.22953v1 | paper-v1:2607.22953 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22953 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22962 | arXiv:2607.22962v1 | paper-v1:2607.22962 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22962 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22997 | arXiv:2607.22997v1 | paper-v1:2607.22997 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22997 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22999 | arXiv:2607.22999v1 | paper-v1:2607.22999 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22999 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23002 | arXiv:2607.23002v1 | paper-v1:2607.23002 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23002 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23012 | arXiv:2607.23012v1 | paper-v1:2607.23012 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23012 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23015 | arXiv:2607.23015v1 | paper-v1:2607.23015 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23015 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23045 | arXiv:2607.23045v1 | paper-v1:2607.23045 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23045 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23046 | arXiv:2607.23046v1 | paper-v1:2607.23046 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23046 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23047 | arXiv:2607.23047v1 | paper-v1:2607.23047 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23047 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23050 | arXiv:2607.23050v1 | paper-v1:2607.23050 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23050 | self | — | new_in_window | MODEL-SELF-ATTENTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23054 | arXiv:2607.23054v1 | paper-v1:2607.23054 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23054 | self | — | new_in_window | MODEL-MULTI-HEAD-ATTENTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23055 | arXiv:2607.23055v1 | paper-v1:2607.23055 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23055 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23089 | arXiv:2607.23089v1 | paper-v1:2607.23089 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23089 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23099 | arXiv:2607.23099v1 | paper-v1:2607.23099 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23099 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23115 | arXiv:2607.23115v1 | paper-v1:2607.23115 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23115 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23123 | arXiv:2607.23123v1 | paper-v1:2607.23123 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23123 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23147 | arXiv:2607.23147v1 | paper-v1:2607.23147 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23147 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23159 | arXiv:2607.23159v1 | paper-v1:2607.23159 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23159 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23193 | arXiv:2607.23193v1 | paper-v1:2607.23193 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23193 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23226 | arXiv:2607.23226v1 | paper-v1:2607.23226 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23226 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23250 | arXiv:2607.23250v1 | paper-v1:2607.23250 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23250 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23263 | arXiv:2607.23263v1 | paper-v1:2607.23263 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23263 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23264 | arXiv:2607.23264v1 | paper-v1:2607.23264 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23264 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23265 | arXiv:2607.23265v1 | paper-v1:2607.23265 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23265 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23332 | arXiv:2607.23332v1 | paper-v1:2607.23332 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23332 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23361 | arXiv:2607.23361v1 | paper-v1:2607.23361 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23361 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23364 | arXiv:2607.23364v1 | paper-v1:2607.23364 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23364 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23366 | arXiv:2607.23366v1 | paper-v1:2607.23366 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23366 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23373 | arXiv:2607.23373v1 | paper-v1:2607.23373 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23373 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23379 | arXiv:2607.23379v1 | paper-v1:2607.23379 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23379 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23386 | arXiv:2607.23386v1 | paper-v1:2607.23386 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23386 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23390 | arXiv:2607.23390v1 | paper-v1:2607.23390 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23390 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23394 | arXiv:2607.23394v1 | paper-v1:2607.23394 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23394 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23402 | arXiv:2607.23402v1 | paper-v1:2607.23402 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23402 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23425 | arXiv:2607.23425v1 | paper-v1:2607.23425 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23425 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23438 | arXiv:2607.23438v1 | paper-v1:2607.23438 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23438 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23444 | arXiv:2607.23444v1 | paper-v1:2607.23444 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23444 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23445 | arXiv:2607.23445v1 | paper-v1:2607.23445 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23445 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23458 | arXiv:2607.23458v1 | paper-v1:2607.23458 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23458 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23472 | arXiv:2607.23472v1 | paper-v1:2607.23472 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23472 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23478 | arXiv:2607.23478v1 | paper-v1:2607.23478 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23478 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23496 | arXiv:2607.23496v1 | paper-v1:2607.23496 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23496 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23504 | arXiv:2607.23504v1 | paper-v1:2607.23504 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23504 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23514 | arXiv:2607.23514v1 | paper-v1:2607.23514 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23514 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23517 | arXiv:2607.23517v1 | paper-v1:2607.23517 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23517 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23532 | arXiv:2607.23532v1 | paper-v1:2607.23532 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23532 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23545 | arXiv:2607.23545v1 | paper-v1:2607.23545 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23545 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23581 | arXiv:2607.23581v1 | paper-v1:2607.23581 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23581 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23586 | arXiv:2607.23586v1 | paper-v1:2607.23586 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23586 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23588 | arXiv:2607.23588v1 | paper-v1:2607.23588 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23588 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23602 | arXiv:2607.23602v1 | paper-v1:2607.23602 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23602 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23605 | arXiv:2607.23605v1 | paper-v1:2607.23605 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23605 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23624 | arXiv:2607.23624v1 | paper-v1:2607.23624 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23624 | self | — | new_in_window | PLATFORM-COST | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23670 | arXiv:2607.23670v1 | paper-v1:2607.23670 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23670 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23693 | arXiv:2607.23693v1 | paper-v1:2607.23693 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23693 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23700 | arXiv:2607.23700v1 | paper-v1:2607.23700 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23700 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23702 | arXiv:2607.23702v1 | paper-v1:2607.23702 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23702 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23704 | arXiv:2607.23704v1 | paper-v1:2607.23704 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23704 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23710 | arXiv:2607.23710v1 | paper-v1:2607.23710 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23710 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23711 | arXiv:2607.23711v1 | paper-v1:2607.23711 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23711 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23722 | arXiv:2607.23722v1 | paper-v1:2607.23722 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23722 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23731 | arXiv:2607.23731v1 | paper-v1:2607.23731 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23731 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23765 | arXiv:2607.23765v1 | paper-v1:2607.23765 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23765 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23771 | arXiv:2607.23771v1 | paper-v1:2607.23771 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23771 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23782 | arXiv:2607.23782v1 | paper-v1:2607.23782 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23782 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23783 | arXiv:2607.23783v1 | paper-v1:2607.23783 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23783 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23802 | arXiv:2607.23802v1 | paper-v1:2607.23802 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23802 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23809 | arXiv:2607.23809v1 | paper-v1:2607.23809 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23809 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23815 | arXiv:2607.23815v1 | paper-v1:2607.23815 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23815 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23838 | arXiv:2607.23838v1 | paper-v1:2607.23838 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23838 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23844 | arXiv:2607.23844v1 | paper-v1:2607.23844 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23844 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23870 | arXiv:2607.23870v1 | paper-v1:2607.23870 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23870 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23884 | arXiv:2607.23884v1 | paper-v1:2607.23884 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23884 | self | — | new_in_window | AGENT-MCP | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23909 | arXiv:2607.23909v1 | paper-v1:2607.23909 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23909 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23927 | arXiv:2607.23927v1 | paper-v1:2607.23927 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23927 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23929 | arXiv:2607.23929v1 | paper-v1:2607.23929 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23929 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23933 | arXiv:2607.23933v1 | paper-v1:2607.23933 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23933 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23955 | arXiv:2607.23955v1 | paper-v1:2607.23955 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23955 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23969 | arXiv:2607.23969v1 | paper-v1:2607.23969 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23969 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23991 | arXiv:2607.23991v1 | paper-v1:2607.23991 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23991 | self | — | new_in_window | AGENT-PROMPT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-23999 | arXiv:2607.23999v1 | paper-v1:2607.23999 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23999 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24008 | arXiv:2607.24008v1 | paper-v1:2607.24008 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24008 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24010 | arXiv:2607.24010v1 | paper-v1:2607.24010 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24010 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24027 | arXiv:2607.24027v1 | paper-v1:2607.24027 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24027 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24054 | arXiv:2607.24054v1 | paper-v1:2607.24054 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24054 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24063 | arXiv:2607.24063v1 | paper-v1:2607.24063 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24063 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24097 | arXiv:2607.24097v1 | paper-v1:2607.24097 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24097 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24112 | arXiv:2607.24112v1 | paper-v1:2607.24112 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24112 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24117 | arXiv:2607.24117v1 | paper-v1:2607.24117 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24117 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24148 | arXiv:2607.24148v1 | paper-v1:2607.24148 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24148 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24157 | arXiv:2607.24157v1 | paper-v1:2607.24157 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24157 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24159 | arXiv:2607.24159v1 | paper-v1:2607.24159 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24159 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24162 | arXiv:2607.24162v1 | paper-v1:2607.24162 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24162 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24165 | arXiv:2607.24165v1 | paper-v1:2607.24165 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24165 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24167 | arXiv:2607.24167v1 | paper-v1:2607.24167 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24167 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24174 | arXiv:2607.24174v1 | paper-v1:2607.24174 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24174 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24223 | arXiv:2607.24223v1 | paper-v1:2607.24223 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24223 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24260 | arXiv:2607.24260v1 | paper-v1:2607.24260 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24260 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24267 | arXiv:2607.24267v1 | paper-v1:2607.24267 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24267 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24268 | arXiv:2607.24268v1 | paper-v1:2607.24268 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24268 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24280 | arXiv:2607.24280v1 | paper-v1:2607.24280 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24280 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24300 | arXiv:2607.24300v1 | paper-v1:2607.24300 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24300 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24306 | arXiv:2607.24306v1 | paper-v1:2607.24306 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24306 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24331 | arXiv:2607.24331v1 | paper-v1:2607.24331 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24331 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24343 | arXiv:2607.24343v1 | paper-v1:2607.24343 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24343 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24368 | arXiv:2607.24368v1 | paper-v1:2607.24368 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24368 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24377 | arXiv:2607.24377v1 | paper-v1:2607.24377 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24377 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24392 | arXiv:2607.24392v1 | paper-v1:2607.24392 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24392 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24407 | arXiv:2607.24407v1 | paper-v1:2607.24407 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24407 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24434 | arXiv:2607.24434v1 | paper-v1:2607.24434 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24434 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24440 | arXiv:2607.24440v1 | paper-v1:2607.24440 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24440 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24459 | arXiv:2607.24459v1 | paper-v1:2607.24459 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24459 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24471 | arXiv:2607.24471v1 | paper-v1:2607.24471 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24471 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24481 | arXiv:2607.24481v1 | paper-v1:2607.24481 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24481 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24484 | arXiv:2607.24484v1 | paper-v1:2607.24484 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24484 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24485 | arXiv:2607.24485v1 | paper-v1:2607.24485 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24485 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24507 | arXiv:2607.24507v1 | paper-v1:2607.24507 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24507 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24516 | arXiv:2607.24516v1 | paper-v1:2607.24516 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24516 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24539 | arXiv:2607.24539v1 | paper-v1:2607.24539 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24539 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24555 | arXiv:2607.24555v1 | paper-v1:2607.24555 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24555 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24562 | arXiv:2607.24562v1 | paper-v1:2607.24562 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24562 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24570 | arXiv:2607.24570v1 | paper-v1:2607.24570 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24570 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24582 | arXiv:2607.24582v1 | paper-v1:2607.24582 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24582 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24585 | arXiv:2607.24585v1 | paper-v1:2607.24585 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24585 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24586 | arXiv:2607.24586v1 | paper-v1:2607.24586 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24586 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24593 | arXiv:2607.24593v1 | paper-v1:2607.24593 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24593 | self | — | new_in_window | MODEL-SELF-ATTENTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24604 | arXiv:2607.24604v1 | paper-v1:2607.24604 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24604 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24625 | arXiv:2607.24625v1 | paper-v1:2607.24625 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24625 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24645 | arXiv:2607.24645v1 | paper-v1:2607.24645 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24645 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24647 | arXiv:2607.24647v1 | paper-v1:2607.24647 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24647 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24651 | arXiv:2607.24651v1 | paper-v1:2607.24651 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24651 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24653 | arXiv:2607.24653v1 | paper-v1:2607.24653 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24653 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24663 | arXiv:2607.24663v1 | paper-v1:2607.24663 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24663 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24665 | arXiv:2607.24665v1 | paper-v1:2607.24665 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24665 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24667 | arXiv:2607.24667v1 | paper-v1:2607.24667 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24667 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24692 | arXiv:2607.24692v1 | paper-v1:2607.24692 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24692 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24717 | arXiv:2607.24717v1 | paper-v1:2607.24717 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24717 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24720 | arXiv:2607.24720v1 | paper-v1:2607.24720 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24720 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24731 | arXiv:2607.24731v1 | paper-v1:2607.24731 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24731 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-22545 | RP-6a9ddd54406eb48c | standard | arXiv:2607.22545v1 | SRC-ARXIV@arXiv:2607.22545v1 | https://arxiv.org/html/2607.22545v1#S3 — 3 Method; https://arxiv.org/html/2607.22545v1#S3.SS1 — 3.1 Architecture | https://arxiv.org/html/2607.22545v1#S4.SS2 — 4.2 Held-out OOD evaluation suite (22 benchmarks); https://arxiv.org/html/2607.22545v1#S4 — 4 Results | https://arxiv.org/html/2607.22545v1#S5 — 5 Discussion; https://arxiv.org/html/2607.22545v1#S6 — 6 Limitations | Exact v1 links https://github.com/anonymous/semalith-eval-harness, https://huggingface.co/meta-llama/Llama-Guard-3-8B, https://huggingface.co/meta-llama/Prompt-Guard-2-86M; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22545 | complete |
| SF-2026-ARXIV-2607-22554 | RP-21b2d11790dc7b5f | standard | arXiv:2607.22554v1 | SRC-ARXIV@arXiv:2607.22554v1 | https://arxiv.org/html/2607.22554v1#A5.SS2 — E.2 Multi-Judge Evaluation Framework; https://arxiv.org/html/2607.22554v1#S3 — 3 A Framework for Fine-Grained Evaluation of Consistency and Reliability | https://arxiv.org/html/2607.22554v1#S5.SS1 — 5.1 Implications for Benchmark Design and Evaluation; https://arxiv.org/html/2607.22554v1#A10 — Appendix J Detailed Result Tables and Figures | https://arxiv.org/html/2607.22554v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.22554v1#A8 — Appendix H Additional Discussion | Exact v1 links https://github.com/kazemf78/llm-consistency-study.git, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22554 | complete |
| SF-2026-ARXIV-2607-22556 | RP-540a388afcdd4379 | standard | arXiv:2607.22556v1 | SRC-ARXIV@arXiv:2607.22556v1 | https://arxiv.org/html/2607.22556v1#A2 — Appendix B Extended Methodology; https://arxiv.org/html/2607.22556v1#S3 — 3 Methodology | https://arxiv.org/html/2607.22556v1#A1 — Appendix A Theoretical Analysis; https://arxiv.org/html/2607.22556v1#A3 — Appendix C Experimental Details | https://arxiv.org/html/2607.22556v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.22556v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22556 | complete |
| SF-2026-ARXIV-2607-22561 | RP-c78152a3f2cd2dd1 | standard | arXiv:2607.22561v1 | SRC-ARXIV@arXiv:2607.22561v1 | https://arxiv.org/html/2607.22561v1#S3 — 3 Framework; https://arxiv.org/html/2607.22561v1#S3.SS3 — 3.3 Modeling Programmatic Judges | https://arxiv.org/html/2607.22561v1#A4 — Appendix D Experimental Results; https://arxiv.org/html/2607.22561v1#A1.SS2 — A.2 A Curated Set of Evaluation Rubrics | https://arxiv.org/html/2607.22561v1#A5 — Appendix E Discussion; https://arxiv.org/html/2607.22561v1#S5 — 5 Conclusion | Exact v1 links https://github.com/SprocketLab/PAJAMA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22561 | complete |
| SF-2026-ARXIV-2607-22562 | RP-994d527023092c91 | standard | arXiv:2607.22562v1 | SRC-ARXIV@arXiv:2607.22562v1 | https://arxiv.org/html/2607.22562v1#S3.SS1 — 3.1 Framework Philosophy and System Architecture; https://arxiv.org/html/2607.22562v1#S2.SS3 — 2.3 System Level and Dynamic Memory Management Frameworks | https://arxiv.org/html/2607.22562v1#A2 — Appendix B Additional Experiments and Analysis; https://arxiv.org/html/2607.22562v1#S4 — 4 Experiments | https://arxiv.org/html/2607.22562v1#S5 — 5 Conclusions | Exact v1 links https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22562 | complete |
| SF-2026-ARXIV-2607-22569 | RP-6d3c2a8c1186b2ba | deep | arXiv:2607.22569v1 | SRC-ARXIV@arXiv:2607.22569v1 | https://arxiv.org/html/2607.22569v1#S4 — 4. Methodology | https://arxiv.org/html/2607.22569v1#S5.SS4 — 5.4. Experimental Results; https://arxiv.org/html/2607.22569v1#S2.SS2 — 2.2. Agent Security Risks and Benchmarks | https://arxiv.org/html/2607.22569v1#S6 — 6. Limitations; https://arxiv.org/html/2607.22569v1#S7 — 7. Conclusion | Exact v1 links https://docs.anthropic.com/en/docs/claude-code/overview, https://huggingface.co/deepseek-ai/DeepSeek-V3-Base, https://openai.com/codex; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22569 | complete |
| SF-2026-ARXIV-2607-22570 | RP-0099829cc41ba540 | standard | arXiv:2607.22570v1 | SRC-ARXIV@arXiv:2607.22570v1 | https://arxiv.org/html/2607.22570v1#A9 — Appendix I N-way Model Diffing in the Shared Coordinate System; https://arxiv.org/html/2607.22570v1#A2 — Appendix B Implementation Details | https://arxiv.org/html/2607.22570v1#A6 — Appendix F Audit Experiment Hyperparameters and Protocols; https://arxiv.org/html/2607.22570v1#A7 — Appendix G Atlas-Coordinate Refusal Steering: Per-Target Results | https://arxiv.org/html/2607.22570v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.22570v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22570 | complete |
| SF-2026-ARXIV-2607-22577 | RP-10b404d4962dae9a | standard | arXiv:2607.22577v1 | SRC-ARXIV@arXiv:2607.22577v1 | https://arxiv.org/html/2607.22577v1#S4 — 4 Method: cMoLLM; https://arxiv.org/html/2607.22577v1#S4.SS2 — 4.2 cMoLLM Block Design | https://arxiv.org/html/2607.22577v1#S4.SS7 — 4.7 Computational Complexity Analysis; https://arxiv.org/html/2607.22577v1#S5 — 5 Experiments | https://arxiv.org/html/2607.22577v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22577 | complete |
| SF-2026-ARXIV-2607-22578 | RP-6efc9cff38b9cb2c | deep | arXiv:2607.22578v1 | SRC-ARXIV@arXiv:2607.22578v1 | https://arxiv.org/html/2607.22578v1#S3 — 3 Method; https://arxiv.org/html/2607.22578v1#S3.SS2 — 3.2 System Overview | https://arxiv.org/html/2607.22578v1#A2 — Appendix B Theoretical Analysis; https://arxiv.org/html/2607.22578v1#A2.SS3 — B.3 Complexity Analysis | https://arxiv.org/html/2607.22578v1#A2.SS4 — B.4 Limitations; https://arxiv.org/html/2607.22578v1#S5 — 5 Conclusion | Exact v1 links https://github.com/langchain-ai/langchain, https://github.com/pgvector/pgvector, https://github.com/run-llama/llama_index; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22578 | complete |
| SF-2026-ARXIV-2607-22584 | RP-91b98cd4ab5b5ccd | standard | arXiv:2607.22584v1 | SRC-ARXIV@arXiv:2607.22584v1 | https://arxiv.org/html/2607.22584v1#S3.SS1 — 3.1 System Architecture; https://arxiv.org/html/2607.22584v1#S3 — 3 Implementation | https://arxiv.org/html/2607.22584v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.22584v1#S4 — 4 Experimentation | https://arxiv.org/html/2607.22584v1#S7 — 7 Future Work; https://arxiv.org/html/2607.22584v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22584 | complete |
| SF-2026-ARXIV-2607-22585 | RP-c48b29f34edb849d | deep | arXiv:2607.22585v1 | SRC-ARXIV@arXiv:2607.22585v1 | https://arxiv.org/html/2607.22585v1#S3.SS2 — 3.2 Models; https://arxiv.org/html/2607.22585v1#S4.SS7 — 4.7 Summary of Harness vs. Model Effects | https://arxiv.org/html/2607.22585v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.22585v1#S4 — 4 Results | https://arxiv.org/html/2607.22585v1#A1 — Appendix A Failure Classification Decision Tree; https://arxiv.org/html/2607.22585v1#A3 — Appendix C Failure Examples (One per Category) | Exact v1 links https://github.com/alibaba/terminal-bench-pro, https://github.com/aaif-goose/goose, https://github.com/harbor-framework/harbor; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22585 | complete |
| SF-2026-ARXIV-2607-22586 | RP-cdec9cbdba6aedfc | deep | arXiv:2607.22586v1 | SRC-ARXIV@arXiv:2607.22586v1 | https://arxiv.org/html/2607.22586v1#S3 — 3 Method; https://arxiv.org/html/2607.22586v1#A2 — Appendix B Implementation Details | https://arxiv.org/html/2607.22586v1#A1 — Appendix A Theoretical Analysis of Prefill–Decode Scale Mismatch; https://arxiv.org/html/2607.22586v1#A3 — Appendix C Additional Visualization Results | https://arxiv.org/html/2607.22586v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.22586v1#S8 — 8 Limitations | Exact v1 links https://github.com/zjuDBxAI/MM-ShiftKV, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22586 | complete |
| SF-2026-ARXIV-2607-22595 | RP-9a5efe88dbd14402 | standard | arXiv:2607.22595v1 | SRC-ARXIV@arXiv:2607.22595v1 | https://arxiv.org/html/2607.22595v1#A2 — Appendix B Cuda graph support on other frameworks; https://arxiv.org/html/2607.22595v1#S4 — 4 Design and Implementation | https://arxiv.org/html/2607.22595v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.22595v1#S4.SS4 — 4.4 Current Scope and Limitations; https://arxiv.org/html/2607.22595v1#S6 — 6 Conclusion | Exact v1 links https://github.com/ZJU-REAL/EasySteer-vllm-v1/pull/3, https://github.com/TransformerLensOrg/TransformerLens, https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22595 | complete |
| SF-2026-ARXIV-2607-22600 | RP-0bc57a5b70805143 | standard | arXiv:2607.22600v1 | SRC-ARXIV@arXiv:2607.22600v1 | https://arxiv.org/html/2607.22600v1#S2.SS2 — II-B Misleading Visual Designs; https://arxiv.org/html/2607.22600v1#S3.SS1 — III-A Taxonomy Design | https://arxiv.org/html/2607.22600v1#S5 — V Result Analysis; https://arxiv.org/html/2607.22600v1#S3 — III The VisDeception Benchmark | https://arxiv.org/html/2607.22600v1#S7 — VII Conclusion and Future Work; https://arxiv.org/html/2607.22600v1#S6 — VI Discussion | Exact v1 links https://github.com/vis-nlp/visDeception, https://github.com/highcharts/highcharts, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22600 | complete |
| SF-2026-ARXIV-2607-22610 | RP-62ea97724c646701 | standard | arXiv:2607.22610v1 | SRC-ARXIV@arXiv:2607.22610v1 | https://arxiv.org/html/2607.22610v1#S4.SS2 — 4.2 Design choices; https://arxiv.org/html/2607.22610v1#A1.SS1 — A.1 Implementation Details | https://arxiv.org/html/2607.22610v1#A1 — Appendix A Experiment Details; https://arxiv.org/html/2607.22610v1#A1.SS2 — A.2 Additional Model Results | https://arxiv.org/html/2607.22610v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.22610v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22610 | complete |
| SF-2026-ARXIV-2607-22611 | RP-114aac574360c80a | deep | arXiv:2607.22611v1 | SRC-ARXIV@arXiv:2607.22611v1 | https://arxiv.org/html/2607.22611v1#S3 — III Architecture; https://arxiv.org/html/2607.22611v1#S3.SS1 — III-A Design Principles | https://arxiv.org/html/2607.22611v1#S5 — V Evaluation | https://arxiv.org/html/2607.22611v1#S2 — II Threat Model and Problem Statement; https://arxiv.org/html/2607.22611v1#S2.SS2 — II-B OWASP LLM Application Threats | Exact v1 links https://owasp.org/www-project-top-10-for-large-language-model-applications/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22611 | complete |
| SF-2026-ARXIV-2607-22614 | RP-0dbfcaa2e1d8c07b | deep | arXiv:2607.22614v1 | SRC-ARXIV@arXiv:2607.22614v1 | https://arxiv.org/html/2607.22614v1#S3 — 3. DynaResize ’s Design; https://arxiv.org/html/2607.22614v1#S4 — 4. Implementation | https://arxiv.org/html/2607.22614v1#S5 — 5. Evaluation | https://arxiv.org/html/2607.22614v1#S6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22614 | complete |
| SF-2026-ARXIV-2607-22625 | RP-0850f92269bdc988 | standard | arXiv:2607.22625v1 | SRC-ARXIV@arXiv:2607.22625v1 | https://arxiv.org/html/2607.22625v1#S3 — 3 Method | https://arxiv.org/html/2607.22625v1#A4 — Appendix D Generation Efficiency: CoT Length Analysis; https://arxiv.org/html/2607.22625v1#S4 — 4 Experiments | https://arxiv.org/html/2607.22625v1#S5 — 5 Discussion; https://arxiv.org/html/2607.22625v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22625 | complete |
| SF-2026-ARXIV-2607-22629 | RP-0e2707fdc8a8aa71 | standard | arXiv:2607.22629v1 | SRC-ARXIV@arXiv:2607.22629v1 | https://arxiv.org/html/2607.22629v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22629v1#S2 — 2 Background | https://arxiv.org/html/2607.22629v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.22629v1#S5 — 5 Results and Discussion | https://arxiv.org/html/2607.22629v1#S5 — 5 Results and Discussion; https://arxiv.org/html/2607.22629v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/datasets/math-ai/aime25, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22629 | complete |
| SF-2026-ARXIV-2607-22634 | RP-6e017806a8eccf2f | deep | arXiv:2607.22634v1 | SRC-ARXIV@arXiv:2607.22634v1 | https://arxiv.org/html/2607.22634v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22634v1#S2 — 2 Preliminaries | https://arxiv.org/html/2607.22634v1#S5.SS2 — 5.2 Experiment Results; https://arxiv.org/html/2607.22634v1#A4 — Appendix D End-to-End Throughput Results for dFlash | https://arxiv.org/html/2607.22634v1#S6 — 6 Discussions and Ablations; https://arxiv.org/html/2607.22634v1#S8 — 8 Conclusion | Exact v1 links https://github.com/tatsu-lab/stanford_alpaca, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22634 | complete |
| SF-2026-ARXIV-2607-22643 | RP-638cd1163a8b8a92 | standard | arXiv:2607.22643v1 | SRC-ARXIV@arXiv:2607.22643v1 | https://arxiv.org/html/2607.22643v1#S3 — 3 MM-R2 Framework | https://arxiv.org/html/2607.22643v1#S6 — 6 Experiments Results; https://arxiv.org/html/2607.22643v1#A6 — Appendix F Two-Axis Evaluation for Agentic RAG | https://arxiv.org/html/2607.22643v1#S7 — 7 Conclusion | Exact v1 links https://github.com/huggingface/trl, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22643 | complete |
| SF-2026-ARXIV-2607-22648 | RP-d1fa8974f2900a06 | deep | arXiv:2607.22648v1 | SRC-ARXIV@arXiv:2607.22648v1 | https://arxiv.org/html/2607.22648v1#S4.SS1 — 4.1 Design Principles; https://arxiv.org/html/2607.22648v1#S6.SS1 — 6.1 Methodology | https://arxiv.org/html/2607.22648v1#S6 — 6 Experimental evaluation | https://arxiv.org/html/2607.22648v1#S7 — 7 Conclusions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22648 | complete |
| SF-2026-ARXIV-2607-22651 | RP-4a43ba7378b5bf9a | standard | arXiv:2607.22651v1 | SRC-ARXIV@arXiv:2607.22651v1 | https://arxiv.org/html/2607.22651v1#S3 — 3. System Architecture and Implementation; https://arxiv.org/html/2607.22651v1#S2 — 2. Conceptual framework | https://arxiv.org/html/2607.22651v1#S4 — 4. Technical evaluation | https://arxiv.org/html/2607.22651v1#S5 — 5. Discussion and Limitations; https://arxiv.org/html/2607.22651v1#S6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22651 | complete |
| SF-2026-ARXIV-2607-22661 | RP-8fa283263cb8e51c | standard | arXiv:2607.22661v1 | SRC-ARXIV@arXiv:2607.22661v1 | https://arxiv.org/html/2607.22661v1#A3.SS2 — C.2 Model Backbones; https://arxiv.org/html/2607.22661v1#A3.SS4 — C.4 Implementation Details | https://arxiv.org/html/2607.22661v1#A4 — Appendix D Additional Experimental Results; https://arxiv.org/html/2607.22661v1#S5.SS2 — 5.2 Results and Analysis | https://arxiv.org/html/2607.22661v1#A5 — Appendix E Limitations and Broader Impacts; https://arxiv.org/html/2607.22661v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22661 | complete |
| SF-2026-ARXIV-2607-22662 | RP-d30ca013fe9c9fc8 | deep | arXiv:2607.22662v1 | SRC-ARXIV@arXiv:2607.22662v1 | https://arxiv.org/html/2607.22662v1#S3 — 3 The CuraWeb Curation Framework; https://arxiv.org/html/2607.22662v1#S3.SS3 — 3.3 Data Understanding System | https://arxiv.org/html/2607.22662v1#S4 — 4 Experiments; https://arxiv.org/html/2607.22662v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.22662v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22662 | complete |
| SF-2026-ARXIV-2607-22663 | RP-a1df927185525a6c | standard | arXiv:2607.22663v1 | SRC-ARXIV@arXiv:2607.22663v1 | https://arxiv.org/html/2607.22663v1#S3 — 3 Method; https://arxiv.org/html/2607.22663v1#S2.SS1 — 2.1 Discrete diffusion large language models | https://arxiv.org/html/2607.22663v1#S4 — 4 Experiments; https://arxiv.org/html/2607.22663v1#S4.SS1 — 4.1 Experimental Setting | https://arxiv.org/html/2607.22663v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22663 | complete |
| SF-2026-ARXIV-2607-22671 | RP-958298ec9b769444 | standard | arXiv:2607.22671v1 | SRC-ARXIV@arXiv:2607.22671v1 | https://arxiv.org/html/2607.22671v1#S2 — 2 Methods | https://arxiv.org/html/2607.22671v1#S3.SS3 — 3.3 Cross-Benchmark Evaluation; https://arxiv.org/html/2607.22671v1#S3 — 3 Results | https://arxiv.org/html/2607.22671v1#S4 — 4 Discussion; https://arxiv.org/html/2607.22671v1#S4.SS2 — 4.2 Limitations | Exact v1 links https://github.com/rnaphade-afk/AIR-BENCH-Auto-Update, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22671 | complete |
| SF-2026-ARXIV-2607-22676 | RP-1482f40b150714ce | standard | arXiv:2607.22676v1 | SRC-ARXIV@arXiv:2607.22676v1 | https://arxiv.org/html/2607.22676v1#A1 — Appendix A Task-Adaptation Post-Training Methods; https://arxiv.org/html/2607.22676v1#A2 — Appendix B Training Hyperparameters and Implementation Details | https://arxiv.org/html/2607.22676v1#A3 — Appendix C Evaluation Details; https://arxiv.org/html/2607.22676v1#A3.SS2 — C.2 Behavioral Evaluation Protocol | https://arxiv.org/html/2607.22676v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.22676v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22676 | complete |
| SF-2026-ARXIV-2607-22688 | RP-f930b8a5aef61650 | standard | arXiv:2607.22688v1 | SRC-ARXIV@arXiv:2607.22688v1 | https://arxiv.org/html/2607.22688v1#S3 — Method; https://arxiv.org/html/2607.22688v1#S3.SS2 — Dual-Loop Co-Evolution Architecture | https://arxiv.org/html/2607.22688v1#A6 — Appendix F Extended Analysis; https://arxiv.org/html/2607.22688v1#A7 — Appendix G Co-Evolution Trajectory Analysis | https://arxiv.org/html/2607.22688v1#S3.SS3 — HarnessCritic: Evolving the Harness from Failure Trajectories; https://arxiv.org/html/2607.22688v1#S5 — Analysis and Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22688 | complete |
| SF-2026-ARXIV-2607-22689 | RP-549772d1aa87e352 | standard | arXiv:2607.22689v1 | SRC-ARXIV@arXiv:2607.22689v1 | https://arxiv.org/html/2607.22689v1#S3.SS3 — III-C Evaluation System | https://arxiv.org/html/2607.22689v1#A1 — Appendix A Extended Experimental Analysis; https://arxiv.org/html/2607.22689v1#S5 — V Experiments and Analysis | https://arxiv.org/html/2607.22689v1#A1.SS2 — A-B Extended Ablation Discussion; https://arxiv.org/html/2607.22689v1#S5.SS4 — V-D RQ3: Failure Modes | Exact v1 links https://github.com/pkgunboat/ParaGUIBench, https://huggingface.co/Hcompany/Holo3-35B-A3B, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22689 | complete |
| SF-2026-ARXIV-2607-22690 | RP-bf25291acf8013f0 | deep | arXiv:2607.22690v1 | SRC-ARXIV@arXiv:2607.22690v1 | https://arxiv.org/html/2607.22690v1#S3 — 3 Method; https://arxiv.org/html/2607.22690v1#A2 — Appendix B Effect of Retrieval Depth and Model Scale in Nano Memory | https://arxiv.org/html/2607.22690v1#A3 — Appendix C Efficiency and Ablation: Details and Additional Results; https://arxiv.org/html/2607.22690v1#A6.SS3 — F.3 Human Evaluation and Judge Noise Analysis | https://arxiv.org/html/2607.22690v1#S5 — 5 Conclusion | Exact v1 links https://github.com/allacnobug/LazyMem, https://github.com/dorianbrown/rank_bm25, https://huggingface.co/BAAI/bge-reranker-v2-m3; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22690 | complete |
| SF-2026-ARXIV-2607-22695 | RP-714d314658b61141 | standard | arXiv:2607.22695v1 | SRC-ARXIV@arXiv:2607.22695v1 | https://arxiv.org/html/2607.22695v1#A1 — Appendix A System Prompt Construction Process; https://arxiv.org/html/2607.22695v1#S3 — III PANOPTICON: Methodology & Evaluation | https://arxiv.org/html/2607.22695v1#S4 — IV Experimental Case Study and Results; https://arxiv.org/html/2607.22695v1#S4.SS3 — IV-C Experiment Results | https://arxiv.org/html/2607.22695v1#S5 — V Discussion and Limitation; https://arxiv.org/html/2607.22695v1#S6 — VI Conclusion and Future Directions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22695 | complete |
| SF-2026-ARXIV-2607-22697 | RP-bb595bfc9609a087 | standard | arXiv:2607.22697v1 | SRC-ARXIV@arXiv:2607.22697v1 | https://arxiv.org/html/2607.22697v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22697v1#S2 — 2 Related Works | https://arxiv.org/html/2607.22697v1#A2 — Appendix B Atlas Ablations; https://arxiv.org/html/2607.22697v1#A2.SS4 — B.4 Additional coverage analysis | https://arxiv.org/html/2607.22697v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.22697v1#S7 — 7 Limitations | Exact v1 links https://github.com/OpenDriveLab/OpenScene, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22697 | complete |
| SF-2026-ARXIV-2607-22708 | RP-37903c3b81128144 | standard | arXiv:2607.22708v1 | SRC-ARXIV@arXiv:2607.22708v1 | https://arxiv.org/html/2607.22708v1#S2 — 2 StepX-Edge: Method Overview; https://arxiv.org/html/2607.22708v1#S2.SS1 — 2.1 Model Architecture | https://arxiv.org/html/2607.22708v1#S3 — 3 Experiments and Evaluation; https://arxiv.org/html/2607.22708v1#S3.SS1 — 3.1 Experimental Setup | https://arxiv.org/html/2607.22708v1#S4 — 4 Conclusion | Exact v1 links https://huggingface.co/datasets/pixparse/idl-wds, https://huggingface.co/datasets/agentsea/wave-ui-25k, https://github.com/mobile-viz/MobileViews; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22708 | complete |
| SF-2026-ARXIV-2607-22711 | RP-692160aca2861bc1 | standard | arXiv:2607.22711v1 | SRC-ARXIV@arXiv:2607.22711v1 | https://arxiv.org/html/2607.22711v1#S5 — 5 Implementation | https://arxiv.org/html/2607.22711v1#A1 — Appendix A Experiments Compute Resources; https://arxiv.org/html/2607.22711v1#A2 — Appendix B Task-Type Analysis | https://arxiv.org/html/2607.22711v1#S7 — 7 Discussion; https://arxiv.org/html/2607.22711v1#S8 — 8 Conclusion | Exact v1 links https://claude.com/product/claude-code, https://huggingface.co/datasets/AmazonScience/SWE-PolyBench_Verified, https://qwenlm.github.io/blog/qwen3-coder/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22711 | complete |
| SF-2026-ARXIV-2607-22716 | RP-23223072b296d975 | standard | arXiv:2607.22716v1 | SRC-ARXIV@arXiv:2607.22716v1 | https://arxiv.org/html/2607.22716v1#A1.SS5 — A.5. Robust-Pruning Layers with FastV Method; https://arxiv.org/html/2607.22716v1#A2.SS2 — B.2. Cross-Architecture Generalization with a Fixed Pruning Layer | https://arxiv.org/html/2607.22716v1#A1 — Appendix A Supplementary Experimental Details; https://arxiv.org/html/2607.22716v1#A1.SS2 — A.2. Evaluation Protocol and Metric Reliability | https://arxiv.org/html/2607.22716v1#S4.SS3 — 4.3. Performance on General Datasets and Efficiency Discussion; https://arxiv.org/html/2607.22716v1#S5 — 5. Conclusion | Exact v1 links https://github.com/Eurek001/OOD-VTP, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22716 | complete |
| SF-2026-ARXIV-2607-22724 | RP-856813c720a7e445 | deep | arXiv:2607.22724v1 | SRC-ARXIV@arXiv:2607.22724v1 | https://arxiv.org/html/2607.22724v1#S13 — 13 Use of Large Language Models; https://arxiv.org/html/2607.22724v1#S8 — 8 Implementation Details | https://arxiv.org/html/2607.22724v1#S10 — 10 Additional Results; https://arxiv.org/html/2607.22724v1#S10.SS2 — 10.2 Per-Category Breakdown of Signal-Analysis Variants | https://arxiv.org/html/2607.22724v1#S12 — 12 Limitations and Broader Impact; https://arxiv.org/html/2607.22724v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22724 | complete |
| SF-2026-ARXIV-2607-22726 | RP-3057deeb4a7887ce | standard | arXiv:2607.22726v1 | SRC-ARXIV@arXiv:2607.22726v1 | https://arxiv.org/html/2607.22726v1#S3 — 3. Method; https://arxiv.org/html/2607.22726v1#S3.SS2 — 3.2. Framework Overview | https://arxiv.org/html/2607.22726v1#S4 — 4. Experiments; https://arxiv.org/html/2607.22726v1#S4.SS4 — 4.4. Results | https://arxiv.org/html/2607.22726v1#S6 — 6. Conclusion | Exact v1 links https://github.com/Heisenberg10110/PCA, https://doi.org/10.18653/v1/2023.emnlp-demo.49, https://dx.doi.org/10.18653/V1/2023.EMNLP-DEMO.49; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22726 | complete |
| SF-2026-ARXIV-2607-22758 | RP-03852afea0d4e848 | standard | arXiv:2607.22758v1 | SRC-ARXIV@arXiv:2607.22758v1 | https://arxiv.org/html/2607.22758v1#S2.SS1 — 2.1 Multi-Agent LLM Frameworks in Clinical NLP; https://arxiv.org/html/2607.22758v1#S3 — 3 Methodology | https://arxiv.org/html/2607.22758v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.22758v1#S4.SS3 — 4.3 Simulation Horizons and Evaluation Metrics | https://arxiv.org/html/2607.22758v1#S6 — 6 Discussion; https://arxiv.org/html/2607.22758v1#S6.SS4 — 6.4 Limitations and Computational Overhead | Exact v1 links https://github.com/amribanerjee/spectral-semantic-cascade, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22758 | complete |
| SF-2026-ARXIV-2607-22766 | RP-de0f0fecbd75d0b2 | standard | arXiv:2607.22766v1 | SRC-ARXIV@arXiv:2607.22766v1 | https://arxiv.org/html/2607.22766v1#S3 — 3 Methodology; https://arxiv.org/html/2607.22766v1#A3 — Appendix C Ablation of Pipeline Models | https://arxiv.org/html/2607.22766v1#A3 — Appendix C Ablation of Pipeline Models; https://arxiv.org/html/2607.22766v1#A4 — Appendix D Hyperparameter Sensitivity Analysis | https://arxiv.org/html/2607.22766v1#S5 — 5 Conclusion and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22766 | complete |
| SF-2026-ARXIV-2607-22769 | RP-67a266597e3ff48f | standard | arXiv:2607.22769v1 | SRC-ARXIV@arXiv:2607.22769v1 | https://arxiv.org/html/2607.22769v1#S2.SS4 — 2.4 Framework Portability; https://arxiv.org/html/2607.22769v1#S3 — 3 Methodology | https://arxiv.org/html/2607.22769v1#S4.SS3 — 4.3 Evaluation Benchmarks; https://arxiv.org/html/2607.22769v1#S4 — 4 Experiment | https://arxiv.org/html/2607.22769v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22769 | complete |
| SF-2026-ARXIV-2607-22781 | RP-aa69a88fdbdfe59a | deep | arXiv:2607.22781v1 | SRC-ARXIV@arXiv:2607.22781v1 | https://arxiv.org/html/2607.22781v1#S3.SS3 — III-C Implementation | https://arxiv.org/html/2607.22781v1#S4 — IV Evaluation Principles and Protocol; https://arxiv.org/html/2607.22781v1#S4.SS2 — IV-B Separating Power Selection from Evaluation | https://arxiv.org/html/2607.22781v1#S7.SS5 — VII-E Limitations; https://arxiv.org/html/2607.22781v1#S8 — VIII Conclusion | Exact v1 links https://huggingface.co/datasets/easytpp/stackoverflow, https://huggingface.co/datasets/easytpp/retweet, https://github.com/ss15859/EarthquakeNPP; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22781 | complete |
| SF-2026-ARXIV-2607-22785 | RP-d95e6a78e661a3bc | deep | arXiv:2607.22785v1 | SRC-ARXIV@arXiv:2607.22785v1 | https://arxiv.org/html/2607.22785v1#S4 — 4 FusionML Design; https://arxiv.org/html/2607.22785v1#S5.SS3 — 5.3 Full Model Depth | https://arxiv.org/html/2607.22785v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.22785v1#S7 — 7 Limitations; https://arxiv.org/html/2607.22785v1#S8 — 8 Conclusion | Exact v1 links https://github.com/ommo007/FusionML, https://github.com/ml-explore/mlx, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22785 | complete |
| SF-2026-ARXIV-2607-22790 | RP-880aca678d2e71c5 | standard | arXiv:2607.22790v1 | SRC-ARXIV@arXiv:2607.22790v1 | https://arxiv.org/html/2607.22790v1#S2 — II Proposed Architectures; https://arxiv.org/html/2607.22790v1#S2.SS1 — II-A SIMD architecture | https://arxiv.org/html/2607.22790v1#S3 — III Experimental results; https://arxiv.org/html/2607.22790v1#S3.SS1 — III-A Experimental Setup | https://arxiv.org/html/2607.22790v1#S4 — IV Conclusion | Exact v1 links https://github.com/stnolting/neorv32, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22790 | complete |
| SF-2026-ARXIV-2607-22798 | RP-e4f4118f7232b693 | deep | arXiv:2607.22798v1 | SRC-ARXIV@arXiv:2607.22798v1 | https://arxiv.org/html/2607.22798v1#S5.SS4 — 5.4 Additional designs | https://arxiv.org/html/2607.22798v1#S5 — 5 Experiments; https://arxiv.org/html/2607.22798v1#S5.SS1 — 5.1 Experimental setup | https://arxiv.org/html/2607.22798v1#S6 — 6 Discussion; https://arxiv.org/html/2607.22798v1#S6.SS1 — 6.1 Why State-Grounding Helps: A Failure Analysis | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22798 | complete |
| SF-2026-ARXIV-2607-22807 | RP-843ee2bd94179910 | standard | arXiv:2607.22807v1 | SRC-ARXIV@arXiv:2607.22807v1 | https://arxiv.org/html/2607.22807v1#A6 — Appendix F System Prompt; https://arxiv.org/html/2607.22807v1#S3 — 3 Methods | https://arxiv.org/html/2607.22807v1#A4 — Appendix D Proprietary Model Results; https://arxiv.org/html/2607.22807v1#S2.SS1 — 2.1 Multilingual Code Evaluation | https://arxiv.org/html/2607.22807v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.22807v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22807 | complete |
| SF-2026-ARXIV-2607-22832 | RP-336eb45dfc511cbd | standard | arXiv:2607.22832v1 | SRC-ARXIV@arXiv:2607.22832v1 | https://arxiv.org/html/2607.22832v1#S3 — 3 Methodology | https://arxiv.org/html/2607.22832v1#A3 — Appendix C Additional Results; https://arxiv.org/html/2607.22832v1#A3.SS1 — C.1 Evaluator Evolution Results | https://arxiv.org/html/2607.22832v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.22832v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22832 | complete |
| SF-2026-ARXIV-2607-22854 | RP-70387f0078591c5a | standard | arXiv:2607.22854v1 | SRC-ARXIV@arXiv:2607.22854v1 | https://arxiv.org/html/2607.22854v1#S3.SS1 — 3.1 Base System Pipeline Design; https://arxiv.org/html/2607.22854v1#S4.SS4 — 4.4 System Architecture | https://arxiv.org/html/2607.22854v1#S8 — 8 Performance Evaluation; https://arxiv.org/html/2607.22854v1#S8.SS1 — 8.1 Evaluation Setup | https://arxiv.org/html/2607.22854v1#S9 — 9 Discussion and Future Work; https://arxiv.org/html/2607.22854v1#S11 — 11 Conclusion | Exact v1 links https://github.com/agent-network-protocol/AgentNetworkProtocol, https://github.com/ggml-org/llama.cpp, https://github.com/a2aproject/A2A; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22854 | complete |
| SF-2026-ARXIV-2607-22868 | RP-710b583166a78b10 | deep | arXiv:2607.22868v1 | SRC-ARXIV@arXiv:2607.22868v1 | https://arxiv.org/html/2607.22868v1#S3 — 3 The Enforcement Model | https://arxiv.org/html/2607.22868v1#A2 — Appendix B Extended Experiments and Reproducibility; https://arxiv.org/html/2607.22868v1#A2.SSx4 — B.4 AgentDojo benchmark | https://arxiv.org/html/2607.22868v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.22868v1#A2.SSx15 — B.15 Threats to validity | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22868 | complete |
| SF-2026-ARXIV-2607-22872 | RP-036f7439d6a6e20b | standard | arXiv:2607.22872v1 | SRC-ARXIV@arXiv:2607.22872v1 | https://arxiv.org/html/2607.22872v1#S2 — 2 Methodology; https://arxiv.org/html/2607.22872v1#S2.SS2 — 2.2 Models | https://arxiv.org/html/2607.22872v1#S2.SS5 — 2.5 Evaluation Metrics; https://arxiv.org/html/2607.22872v1#S3 — 3 Results and Discussion | https://arxiv.org/html/2607.22872v1#S3 — 3 Results and Discussion; https://arxiv.org/html/2607.22872v1#S4 — 4 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22872 | complete |
| SF-2026-ARXIV-2607-22880 | RP-96efaa749b3bb926 | standard | arXiv:2607.22880v1 | SRC-ARXIV@arXiv:2607.22880v1 | https://arxiv.org/html/2607.22880v1#S3 — 3. Methodology; https://arxiv.org/html/2607.22880v1#S3.SS3 — 3.3. Models | https://arxiv.org/html/2607.22880v1#S3.SS2 — 3.2. Benchmark; https://arxiv.org/html/2607.22880v1#S3.SS7 — 3.7. Correlation Analysis | https://arxiv.org/html/2607.22880v1#S9 — 9. Conclusion and Future Work; https://arxiv.org/html/2607.22880v1#S7 — 7. Discussion | Exact v1 links https://github.com/drixs2050/Cov_mut_bug_detect_correlation, http://codecover.org/, https://qwenlm.github.io/blog/qwen3-coder/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22880 | complete |
| SF-2026-ARXIV-2607-22883 | RP-42b97d3e6f008505 | standard | arXiv:2607.22883v1 | SRC-ARXIV@arXiv:2607.22883v1 | https://arxiv.org/html/2607.22883v1#S2 — 2. Study Design; https://arxiv.org/html/2607.22883v1#S2.SS5 — 2.5. Mitigation Methodology and Baselines | https://arxiv.org/html/2607.22883v1#S2.SS2 — 2.2. Benchmark; https://arxiv.org/html/2607.22883v1#S2 — 2. Study Design | https://arxiv.org/html/2607.22883v1#S6 — 6. Threats to Validity and Limitations; https://arxiv.org/html/2607.22883v1#S8 — 8. Conclusion and Future Work | Exact v1 links https://github.com/drixs2050/EvalAndMitigate, https://qwenlm.github.io/blog/qwen3-coder/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22883 | complete |
| SF-2026-ARXIV-2607-22898 | RP-ed319544ec83e967 | standard | arXiv:2607.22898v1 | SRC-ARXIV@arXiv:2607.22898v1 | https://arxiv.org/html/2607.22898v1#A3.SS1 — C-A Novel Task Design; https://arxiv.org/html/2607.22898v1#A5.SS1 — E-A Architecture and Components | https://arxiv.org/html/2607.22898v1#A3 — Appendix C Benchmark Construction Details; https://arxiv.org/html/2607.22898v1#A6.SS2 — F-B Running the Experiments | https://arxiv.org/html/2607.22898v1#S6.SS7 — VI-G Discussion; https://arxiv.org/html/2607.22898v1#S8 — VIII Threats to Validity | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22898 | complete |
| SF-2026-ARXIV-2607-22917 | RP-396ef8cdbb8ad5c1 | standard | arXiv:2607.22917v1 | SRC-ARXIV@arXiv:2607.22917v1 | https://arxiv.org/html/2607.22917v1#S4 — 4 Design Philosophy; https://arxiv.org/html/2607.22917v1#A1.SS1 — A.1 Large Language Models | https://arxiv.org/html/2607.22917v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22917v1#S2 — 2 Background: Claude Code, Subagents, and Agent Teams | https://arxiv.org/html/2607.22917v1#S12 — 12 Limitations and Future Work; https://arxiv.org/html/2607.22917v1#S10 — 10 Failure Modes and Hardening | Exact v1 links https://github.com/SR-A-W/agent-team-work-zone, https://code.claude.com/docs/en/agent-teams, https://code.claude.com/docs/en/memory; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22917 | complete |
| SF-2026-ARXIV-2607-22925 | RP-020597da056d3386 | standard | arXiv:2607.22925v1 | SRC-ARXIV@arXiv:2607.22925v1 | https://arxiv.org/html/2607.22925v1#S3 — 3 Methodology; https://arxiv.org/html/2607.22925v1#S6 — 6 What Training Methodologies Elicit Invisible Reasoning? | https://arxiv.org/html/2607.22925v1#A6 — Appendix F RL Experiment Results; https://arxiv.org/html/2607.22925v1#A1 — Appendix A Invisible Reasoning Evaluation Details | https://arxiv.org/html/2607.22925v1#S7 — 7 Conclusion | Exact v1 links https://github.com/togethercomputer/xorl, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22925 | complete |
| SF-2026-ARXIV-2607-22926 | RP-653dae4870b7d100 | deep | arXiv:2607.22926v1 | SRC-ARXIV@arXiv:2607.22926v1 | https://arxiv.org/html/2607.22926v1#S4 — 4 SAGE Formal Framework; https://arxiv.org/html/2607.22926v1#S5 — 5 Reference Architecture and Implementation | https://arxiv.org/html/2607.22926v1#S6 — 6 Experimental Design; https://arxiv.org/html/2607.22926v1#S7 — 7 Results | https://arxiv.org/html/2607.22926v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.22926v1#S8 — 8 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22926 | complete |
| SF-2026-ARXIV-2607-22927 | RP-526fa98574a33379 | standard | arXiv:2607.22927v1 | SRC-ARXIV@arXiv:2607.22927v1 | https://arxiv.org/html/2607.22927v1#S7.SS2 — 7.2 Relationship to centering and natural-gradient methods | https://arxiv.org/html/2607.22927v1#S5 — 5 Experimental Setup; https://arxiv.org/html/2607.22927v1#S6 — 6 Results | https://arxiv.org/html/2607.22927v1#S7 — 7 Discussion; https://arxiv.org/html/2607.22927v1#S8 — 8 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22927 | complete |
| SF-2026-ARXIV-2607-22949 | RP-75f2a4bb58fd773c | standard | arXiv:2607.22949v1 | SRC-ARXIV@arXiv:2607.22949v1 | https://arxiv.org/html/2607.22949v1#S2.SS2 — II-B Evaluation Methodology in Information Extraction; https://arxiv.org/html/2607.22949v1#S4 — IV Experimental Methodology | https://arxiv.org/html/2607.22949v1#S2.SS2 — II-B Evaluation Methodology in Information Extraction; https://arxiv.org/html/2607.22949v1#S2.SS3 — II-C Ground Truth Quality in Public Benchmarks | https://arxiv.org/html/2607.22949v1#S6 — VI Discussion; https://arxiv.org/html/2607.22949v1#S6.SS3 — VI-C Ground Truth Noise as a Structural Limitation | Exact v1 links https://github.com/a-dwivedi/llm-product-attribute-extraction, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22949 | complete |
| SF-2026-ARXIV-2607-22951 | RP-1854ed34554b9f43 | standard | arXiv:2607.22951v1 | SRC-ARXIV@arXiv:2607.22951v1 | https://arxiv.org/html/2607.22951v1#S3.SS1 — III-A Domain-Specific Hidden Markov Model; https://arxiv.org/html/2607.22951v1#S3.SS2 — III-B Modeling Assumptions and Practical Considerations | https://arxiv.org/html/2607.22951v1#S4 — IV Evaluation; https://arxiv.org/html/2607.22951v1#S4.SS2 — IV-B Numerical Results | https://arxiv.org/html/2607.22951v1#S5 — V Discussion and conclusion | Exact v1 links https://github.com/llmReliability/hmm-llm-reliability-proof, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22951 | complete |
| SF-2026-ARXIV-2607-22953 | RP-1329eb3df22ebd48 | standard | arXiv:2607.22953v1 | SRC-ARXIV@arXiv:2607.22953v1 | https://arxiv.org/html/2607.22953v1#S4 — 4. Framework Design; https://arxiv.org/html/2607.22953v1#S6.SS1 — 6.1. Threat Model | https://arxiv.org/html/2607.22953v1#S1 — 1. Introduction; https://arxiv.org/html/2607.22953v1#S2 — 2. Background | https://arxiv.org/html/2607.22953v1#S6.SS1 — 6.1. Threat Model; https://arxiv.org/html/2607.22953v1#S7 — 7. Conclusion | Exact v1 links https://solidproject.org/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22953 | complete |
| SF-2026-ARXIV-2607-22962 | RP-df925484914c0256 | deep | arXiv:2607.22962v1 | SRC-ARXIV@arXiv:2607.22962v1 | https://arxiv.org/html/2607.22962v1#S4.SS1 — 4.1 Core Algorithm; https://arxiv.org/html/2607.22962v1#S6.SS3 — 6.3 Cross-Model Generalization | https://arxiv.org/html/2607.22962v1#A1 — Appendix A Full Ablation Results; https://arxiv.org/html/2607.22962v1#A5 — Appendix E Benchmark Dataset Details | https://arxiv.org/html/2607.22962v1#S7 — 7 Failure Modes and Operating Regime; https://arxiv.org/html/2607.22962v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22962 | complete |
| SF-2026-ARXIV-2607-22997 | RP-5f42912928e9acb2 | standard | arXiv:2607.22997v1 | SRC-ARXIV@arXiv:2607.22997v1 | https://arxiv.org/html/2607.22997v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22997v1#S2 — 2 Demo 1: Sim-to-Real Manipulation [ 6 ] | https://arxiv.org/html/2607.22997v1#S2.SS0.SSS0.Px1 — Analysis.; https://arxiv.org/html/2607.22997v1#S3.SS0.SSS0.Px1 — Analysis. | https://arxiv.org/html/2607.22997v1#S7 — 7 Conclusion | Exact v1 links https://github.com/AMD-AIM/Physical_AI_Challenge, https://github.com/huggingface/lerobot, https://huggingface.co/blog/smolvla; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22997 | complete |
| SF-2026-ARXIV-2607-22999 | RP-5e411384c311e57a | deep | arXiv:2607.22999v1 | SRC-ARXIV@arXiv:2607.22999v1 | https://arxiv.org/html/2607.22999v1#S2.SS1 — II-A System Architecture and Runtime; https://arxiv.org/html/2607.22999v1#S2 — II Method: The World-Cognition Model | https://arxiv.org/html/2607.22999v1#A2 — Appendix B Performance Comparison Results; https://arxiv.org/html/2607.22999v1#A3 — Appendix C Ablations | https://arxiv.org/html/2607.22999v1#S4 — IV Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22999 | complete |
| SF-2026-ARXIV-2607-23002 | RP-f74fe290de4ccf58 | standard | arXiv:2607.23002v1 | SRC-ARXIV@arXiv:2607.23002v1 | https://arxiv.org/html/2607.23002v1#Sx1.SSx4 — 3. Method | https://arxiv.org/html/2607.23002v1#Sx1.SSx5 — 4. Results | https://arxiv.org/html/2607.23002v1#Sx1.SSx6 — 5. Discussion; https://arxiv.org/html/2607.23002v1#Sx1.SSx7 — 6. Threats to Validity | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23002 | complete |
| SF-2026-ARXIV-2607-23012 | RP-2ff2ab8c88a2b5c0 | standard | arXiv:2607.23012v1 | SRC-ARXIV@arXiv:2607.23012v1 | https://arxiv.org/pdf/2607.23012v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23012v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.23012v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23012v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.23012v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23012v1#page=10 — PDF page 10 | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23012 | complete |
| SF-2026-ARXIV-2607-23015 | RP-136aac6a4fdad38a | standard | arXiv:2607.23015v1 | SRC-ARXIV@arXiv:2607.23015v1 | https://arxiv.org/html/2607.23015v1#A1.SS1 — A-A System-Prompt Diversification; https://arxiv.org/html/2607.23015v1#S3 — III Method | https://arxiv.org/html/2607.23015v1#S4 — IV Experimental Results; https://arxiv.org/html/2607.23015v1#S4.SS2 — IV-B Evaluation Metrics | https://arxiv.org/html/2607.23015v1#S3.SS1 — III-A Threat Model; https://arxiv.org/html/2607.23015v1#S5 — V Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23015 | complete |
| SF-2026-ARXIV-2607-23045 | RP-1db50d7d9b78da44 | standard | arXiv:2607.23045v1 | SRC-ARXIV@arXiv:2607.23045v1 | https://arxiv.org/pdf/2607.23045v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23045v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.23045v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23045v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.23045v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23045v1#page=10 — PDF page 10 | Exact v1 links https://github.com/pic-ai-robotic-chemistry/LabBench; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23045 | complete |
| SF-2026-ARXIV-2607-23046 | RP-0ac2b92f8b5b2957 | standard | arXiv:2607.23046v1 | SRC-ARXIV@arXiv:2607.23046v1 | https://arxiv.org/html/2607.23046v1#S2.SS1 — 2.1 Vision Token Pruning Methods; https://arxiv.org/html/2607.23046v1#S2.SS2 — 2.2 Ridge Leverage Score in Neural Architectures | https://arxiv.org/html/2607.23046v1#S4 — 4 Experiments; https://arxiv.org/html/2607.23046v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.23046v1#S5 — 5 Conclusion | Exact v1 links https://github.com/cvsp-lab/SFPruner, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23046 | complete |
| SF-2026-ARXIV-2607-23047 | RP-6058dd7f7668eb20 | deep | arXiv:2607.23047v1 | SRC-ARXIV@arXiv:2607.23047v1 | https://arxiv.org/html/2607.23047v1#S4 — 4 Method | https://arxiv.org/html/2607.23047v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.23047v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23047 | complete |
| SF-2026-ARXIV-2607-23050 | RP-41388375aa5a062e | standard | arXiv:2607.23050v1 | SRC-ARXIV@arXiv:2607.23050v1 | https://arxiv.org/html/2607.23050v1#A3.SS3 — C.3 Student models | https://arxiv.org/html/2607.23050v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.23050v1#A4 — Appendix D Spectral-Gap Ablation | https://arxiv.org/html/2607.23050v1#S7 — 7 Discussion, Limitations, and Open Problems | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23050 | complete |
| SF-2026-ARXIV-2607-23054 | RP-747778696a2e0743 | deep | arXiv:2607.23054v1 | SRC-ARXIV@arXiv:2607.23054v1 | https://arxiv.org/html/2607.23054v1#S3.SS1 — 3.1 Model Architecture; https://arxiv.org/html/2607.23054v1#S5.SS3 — 5.3 Implications for MLA Design | https://arxiv.org/html/2607.23054v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.23054v1#S3.SS3 — 3.3 Experiments Overview | https://arxiv.org/html/2607.23054v1#S5 — 5 Discussion; https://arxiv.org/html/2607.23054v1#S5.SS4 — 5.4 Limitations | Exact v1 links https://github.com/Dhruvil-sr24/Small-Language-Model-From-Scratch/tree/main/interp, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23054 | complete |
| SF-2026-ARXIV-2607-23055 | RP-ed09c7528aca0f20 | standard | arXiv:2607.23055v1 | SRC-ARXIV@arXiv:2607.23055v1 | https://arxiv.org/html/2607.23055v1#A9 — Appendix I System Prompts; https://arxiv.org/html/2607.23055v1#S4.SS2 — 4.2 Methods and Baselines | https://arxiv.org/html/2607.23055v1#A2 — Appendix B Cross-Model Results on LGP-10 (Sonnet); https://arxiv.org/html/2607.23055v1#A5 — Appendix E AQUA-RAT: Domain Boundary Analysis | https://arxiv.org/html/2607.23055v1#S8 — 8 Limitations and Future Work; https://arxiv.org/html/2607.23055v1#S6 — 6 Analysis and Discussion | Exact v1 links https://github.com/Zangir/SymStep, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23055 | complete |
| SF-2026-ARXIV-2607-23089 | RP-5187c92417a63720 | deep | arXiv:2607.23089v1 | SRC-ARXIV@arXiv:2607.23089v1 | https://arxiv.org/html/2607.23089v1#S2.SS2 — 2.2 Limitations of Existing Approaches; https://arxiv.org/html/2607.23089v1#S3 — 3 System Overview | https://arxiv.org/html/2607.23089v1#S4.SS3 — 4.3 Compiler-Grounded Analysis; https://arxiv.org/html/2607.23089v1#S6 — 6 Evaluation | https://arxiv.org/html/2607.23089v1#S2.SS2 — 2.2 Limitations of Existing Approaches; https://arxiv.org/html/2607.23089v1#S8 — 8 Discussion | Exact v1 links https://gitcode.com/cann/cannbot-skills, https://github.com/Ascend/triton-ascend-ops, https://github.com/flagos-ai/awesome-LLM-driven-kernel-generation; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23089 | complete |
| SF-2026-ARXIV-2607-23099 | RP-d69f8fe9e191ed42 | deep | arXiv:2607.23099v1 | SRC-ARXIV@arXiv:2607.23099v1 | https://arxiv.org/html/2607.23099v1#S2.SS2 — II-B NVIDIA GPU Microarchitecture; https://arxiv.org/html/2607.23099v1#S2.SS1 — II-A Mixture-of-Experts Models | https://arxiv.org/html/2607.23099v1#S3 — III Modeling and Benchmarking; https://arxiv.org/html/2607.23099v1#S5 — V Evaluation | https://arxiv.org/html/2607.23099v1#S6 — VI Discussion & Architectural Implications; https://arxiv.org/html/2607.23099v1#S8 — VIII Conclusion | Exact v1 links https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/hipgraph.html, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23099 | complete |
| SF-2026-ARXIV-2607-23115 | RP-6f4723921c0a6ead | deep | arXiv:2607.23115v1 | SRC-ARXIV@arXiv:2607.23115v1 | https://arxiv.org/html/2607.23115v1#S3 — 3 Framework Overview; https://arxiv.org/html/2607.23115v1#A1.SS1 — A.1 Implementation Details | https://arxiv.org/html/2607.23115v1#A1.SS2 — A.2 Experiment Supplement; https://arxiv.org/html/2607.23115v1#A1.SS3 — A.3 Analysis for Gleam Scheduling | https://arxiv.org/html/2607.23115v1#A1.SS4 — A.4 Discussion; https://arxiv.org/html/2607.23115v1#S9 — 9 Conclusion | Exact v1 links https://github.com/ggml-org/ggml, https://github.com/grpc/grpc.io, https://github.com/ggml-org/llama.cpp; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23115 | complete |
| SF-2026-ARXIV-2607-23123 | RP-2d6043810e54543d | standard | arXiv:2607.23123v1 | SRC-ARXIV@arXiv:2607.23123v1 | https://arxiv.org/html/2607.23123v1#S3.SS1 — 3.1 Design principles; https://arxiv.org/html/2607.23123v1#A3 — Appendix C Model Invocation and Cost Records | https://arxiv.org/html/2607.23123v1#A5 — Appendix E Supplementary Results; https://arxiv.org/html/2607.23123v1#S1.SS1 — 1.1 Why existing evaluations do not fully capture production-oriented delivery | https://arxiv.org/html/2607.23123v1#S6 — 6 Limitations; https://arxiv.org/html/2607.23123v1#S7 — 7 Conclusion | Exact v1 links https://github.com/shaqiu-ai/SQBench, https://github.com/shaqiu-ai/SQBench/releases/tag/v1.0-paper-20260720, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23123 | complete |
| SF-2026-ARXIV-2607-23147 | RP-e23ed51390fff118 | standard | arXiv:2607.23147v1 | SRC-ARXIV@arXiv:2607.23147v1 | https://arxiv.org/html/2607.23147v1#S2.SS1 — 2.1. World Models; https://arxiv.org/html/2607.23147v1#S2.SS2 — 2.2. World Models as Environment Simulators | https://arxiv.org/html/2607.23147v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.23147v1#S5.SS1 — 5.1. Experimental Setup. | https://arxiv.org/html/2607.23147v1#S3.SS1 — 3.1. Threat Model; https://arxiv.org/html/2607.23147v1#S7 — 7. Conclusion | Exact v1 links https://github.com/mlsec-group/worldmodel-security, https://web.archive.org/web/20260716110416/https://opencode.ai/docs/zen/#pricing, https://huggingface.co/collections/XiaomiMiMo/mimo-v25; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23147 | complete |
| SF-2026-ARXIV-2607-23159 | RP-fe558377a5854db2 | standard | arXiv:2607.23159v1 | SRC-ARXIV@arXiv:2607.23159v1 | https://arxiv.org/html/2607.23159v1#S3 — 3 Method; https://arxiv.org/html/2607.23159v1#S5.SS2 — 5.2 Ranking preservation across published caching methods | https://arxiv.org/html/2607.23159v1#S5 — 5 Analysis and Ablations; https://arxiv.org/html/2607.23159v1#A4 — Appendix D Additional Experiments | https://arxiv.org/html/2607.23159v1#A10 — Appendix J Limitations; https://arxiv.org/html/2607.23159v1#A7 — Appendix G Scaling discussion | Exact v1 links https://github.com/shreshthsaini/CachedSearch, https://github.com/Wan-Video/Wan2.2, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23159 | complete |
| SF-2026-ARXIV-2607-23193 | RP-2eb7b121c0cc1dd9 | standard | arXiv:2607.23193v1 | SRC-ARXIV@arXiv:2607.23193v1 | https://arxiv.org/pdf/2607.23193v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23193v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.23193v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23193v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.23193v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23193v1#page=10 — PDF page 10 | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23193 | complete |
| SF-2026-ARXIV-2607-23226 | RP-8ad9492b0bc58617 | standard | arXiv:2607.23226v1 | SRC-ARXIV@arXiv:2607.23226v1 | https://arxiv.org/html/2607.23226v1#S2.SS1 — 2.1 Sampling Theory for Diffusion Models; https://arxiv.org/html/2607.23226v1#S3 — 3 Score-based diffusion models | https://arxiv.org/html/2607.23226v1#S4 — 4 Main results: Generalization and convergence properties of SDMs; https://arxiv.org/html/2607.23226v1#S4.SS1 — 4.1 Assumptions and preliminary results | https://arxiv.org/html/2607.23226v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23226 | complete |
| SF-2026-ARXIV-2607-23250 | RP-dc83694a062a78c8 | deep | arXiv:2607.23250v1 | SRC-ARXIV@arXiv:2607.23250v1 | https://arxiv.org/html/2607.23250v1#S4 — 4. Design; https://arxiv.org/html/2607.23250v1#S5 — 5. Implementation | https://arxiv.org/html/2607.23250v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.23250v1#S6.SS1 — 6.1. Experimental Setup | https://arxiv.org/html/2607.23250v1#S8 — 8. Conclusion | Exact v1 links https://github.com/SandAI-org/MagiAttention/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23250 | complete |
| SF-2026-ARXIV-2607-23263 | RP-83504e1b6de550f6 | standard | arXiv:2607.23263v1 | SRC-ARXIV@arXiv:2607.23263v1 | https://arxiv.org/html/2607.23263v1#S3 — 3 Method; https://arxiv.org/html/2607.23263v1#S3.SS1 — 3.1 The SeekJudge Framework | https://arxiv.org/html/2607.23263v1#S4.SS4 — 4.4 Offline Reward Benchmark Evaluation; https://arxiv.org/html/2607.23263v1#S2.SS2 — 2.2 From Rule-Based to Model-Based Evaluation | https://arxiv.org/html/2607.23263v1#S5 — 5 Conclusion | Exact v1 links https://github.com/McGill-NLP/agent-reward-bench/issues/9, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23263 | complete |
| SF-2026-ARXIV-2607-23264 | RP-aee873b72b21f185 | deep | arXiv:2607.23264v1 | SRC-ARXIV@arXiv:2607.23264v1 | https://arxiv.org/html/2607.23264v1#S4 — 4. X-Stage-Aware Kernel Design; https://arxiv.org/html/2607.23264v1#S4.SS1 — 4.1. A Design Test with Two Actions | https://arxiv.org/html/2607.23264v1#S3.SS1 — 3.1. Remote-Store Microbenchmarks; https://arxiv.org/html/2607.23264v1#S5 — 5. Evaluation | https://arxiv.org/html/2607.23264v1#S6 — 6. Discussion and Limitations; https://arxiv.org/html/2607.23264v1#S8 — 8. Conclusion | Exact v1 links https://github.com/deepseek-ai/EPLB, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23264 | complete |
| SF-2026-ARXIV-2607-23265 | RP-0f3c6b6c7c6a07a7 | standard | arXiv:2607.23265v1 | SRC-ARXIV@arXiv:2607.23265v1 | https://arxiv.org/html/2607.23265v1#S3 — 3 Method | https://arxiv.org/html/2607.23265v1#A1 — Appendix A Supplemental Experimental Protocol; https://arxiv.org/html/2607.23265v1#A2 — Appendix B Controlled Wavelet Ablations | https://arxiv.org/html/2607.23265v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23265 | complete |
| SF-2026-ARXIV-2607-23332 | RP-4574fae0ba0002c3 | standard | arXiv:2607.23332v1 | SRC-ARXIV@arXiv:2607.23332v1 | https://arxiv.org/html/2607.23332v1#A2.SS4 — B.4 Models and generation settings; https://arxiv.org/html/2607.23332v1#A4 — Appendix D Supplementary Frontier-Model Results | https://arxiv.org/html/2607.23332v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.23332v1#A1 — Appendix A Benchmark Theory and Preregistration | https://arxiv.org/html/2607.23332v1#S4.SS1 — 4.1 Abstract competence but tool-budgeting failure; https://arxiv.org/html/2607.23332v1#S5 — 5 Discussion | Exact v1 links https://github.com/DragonWrangler25/AlloBench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23332 | complete |
| SF-2026-ARXIV-2607-23361 | RP-a7f104d1d3c1acb3 | standard | arXiv:2607.23361v1 | SRC-ARXIV@arXiv:2607.23361v1 | https://arxiv.org/html/2607.23361v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23361v1#S1.SS1 — 1.1 Related Work | https://arxiv.org/html/2607.23361v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23361v1#S1.SS1 — 1.1 Related Work | https://arxiv.org/html/2607.23361v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23361v1#S1.SS1 — 1.1 Related Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23361 | complete |
| SF-2026-ARXIV-2607-23364 | RP-317eef87f1214343 | deep | arXiv:2607.23364v1 | SRC-ARXIV@arXiv:2607.23364v1 | https://arxiv.org/html/2607.23364v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23364v1#S2 — 2 Preliminaries | https://arxiv.org/html/2607.23364v1#S3 — 3 Main Result: Impossibility Theorem; https://arxiv.org/html/2607.23364v1#S4 — 4 Corollaries and Analysis | https://arxiv.org/html/2607.23364v1#S5 — 5 Discussion; https://arxiv.org/html/2607.23364v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23364 | complete |
| SF-2026-ARXIV-2607-23366 | RP-062dc2d5e380f0e3 | standard | arXiv:2607.23366v1 | SRC-ARXIV@arXiv:2607.23366v1 | https://arxiv.org/html/2607.23366v1#A1 — Appendix A Architecture Hyperparameters; https://arxiv.org/html/2607.23366v1#S3 — 3 Method | https://arxiv.org/html/2607.23366v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.23366v1#S5 — 5 Results | https://arxiv.org/html/2607.23366v1#S6 — 6 Discussion; https://arxiv.org/html/2607.23366v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23366 | complete |
| SF-2026-ARXIV-2607-23373 | RP-0e26e9c8add44638 | deep | arXiv:2607.23373v1 | SRC-ARXIV@arXiv:2607.23373v1 | https://arxiv.org/html/2607.23373v1#Pt0.A2.SS4 — 0.B.4 On-device measurements methodology; https://arxiv.org/html/2607.23373v1#S3 — 3 Architecture optimization | https://arxiv.org/html/2607.23373v1#Pt0.A2 — Appendix 0.B Additional Experiments; https://arxiv.org/html/2607.23373v1#Pt0.A2.SS1 — 0.B.1 Extended OCR retrieval results | https://arxiv.org/html/2607.23373v1#S7 — 7 Conclusion | Exact v1 links https://huggingface.co/google/siglip2-base-patch16-naflex, https://huggingface.co/google/siglip2-so400m-patch16-512, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23373 | complete |
| SF-2026-ARXIV-2607-23379 | RP-63e311e3bb15dcd8 | standard | arXiv:2607.23379v1 | SRC-ARXIV@arXiv:2607.23379v1 | https://arxiv.org/html/2607.23379v1#A2 — Appendix B Subject Model and Activation Oracle Training; https://arxiv.org/html/2607.23379v1#S4.SS1 — 4.1 Subject models and Taboo fine-tuning | https://arxiv.org/html/2607.23379v1#A10.SS1 — J.1 Detailed behavioural evaluation results; https://arxiv.org/html/2607.23379v1#A10 — Appendix J Detailed Results | https://arxiv.org/html/2607.23379v1#A1 — Appendix A Limitations and Future Work; https://arxiv.org/html/2607.23379v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23379 | complete |
| SF-2026-ARXIV-2607-23386 | RP-89db727ff2b48662 | standard | arXiv:2607.23386v1 | SRC-ARXIV@arXiv:2607.23386v1 | https://arxiv.org/html/2607.23386v1#Sx3.SSx5 — 3.5 Neuro-Symbolic Architectures and LLM + Formal Method Hybrids; https://arxiv.org/html/2607.23386v1#Sx13 — Technical Appendix A: Benchmark Methodology | https://arxiv.org/html/2607.23386v1#Sx13 — Technical Appendix A: Benchmark Methodology; https://arxiv.org/html/2607.23386v1#Sx3.SSx2 — 3.2 LLM Benchmarks for Legal and Logical Reasoning | https://arxiv.org/html/2607.23386v1#Sx10 — 10. Limitations and Future Work; https://arxiv.org/html/2607.23386v1#Sx10.SSx1 — 10.1 Current Limitations | Exact v1 links https://github.com/Aethis-ai/confidently-wrong-benchmark, https://github.com/Aethis-ai/confidently-wrong-benchmark/tree/main/legalbench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23386 | complete |
| SF-2026-ARXIV-2607-23390 | RP-52def6fa75f5eae0 | standard | arXiv:2607.23390v1 | SRC-ARXIV@arXiv:2607.23390v1 | https://arxiv.org/html/2607.23390v1#A1.SS6 — A.6 Architecture specialization: Transformer and routed-MoE execution; https://arxiv.org/html/2607.23390v1#A5 — Appendix E Rational Certificate Methodology for the Matrix-Valued Example | https://arxiv.org/html/2607.23390v1#A6 — Appendix F Additional Experimental and Search Details; https://arxiv.org/html/2607.23390v1#A8 — Appendix H Pretrained DistilBERT Study | https://arxiv.org/html/2607.23390v1#S12 — 12 Discussion and Limitations; https://arxiv.org/html/2607.23390v1#S13 — 13 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23390 | complete |
| SF-2026-ARXIV-2607-23394 | RP-a0f5d48c4baa59ca | standard | arXiv:2607.23394v1 | SRC-ARXIV@arXiv:2607.23394v1 | https://arxiv.org/html/2607.23394v1#S3 — 3 Method; https://arxiv.org/html/2607.23394v1#A4 — Appendix D Setting 1 pilot with eight reference models | https://arxiv.org/html/2607.23394v1#A5 — Appendix E Experimental details; https://arxiv.org/html/2607.23394v1#S4 — 4 Results | https://arxiv.org/html/2607.23394v1#S5 — 5 Discussion | Exact v1 links https://github.com/AdhyyanNarang/consensus-aggregation, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23394 | complete |
| SF-2026-ARXIV-2607-23402 | RP-4ca3f5cc11110760 | standard | arXiv:2607.23402v1 | SRC-ARXIV@arXiv:2607.23402v1 | https://arxiv.org/html/2607.23402v1#S1 — I Introduction; https://arxiv.org/html/2607.23402v1#S2 — II Background | https://arxiv.org/html/2607.23402v1#S3 — III Experimental Setup | https://arxiv.org/html/2607.23402v1#S6 — VI Discussion; https://arxiv.org/html/2607.23402v1#S8 — VIII Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23402 | complete |
| SF-2026-ARXIV-2607-23425 | RP-e711940e34dda95c | standard | arXiv:2607.23425v1 | SRC-ARXIV@arXiv:2607.23425v1 | https://arxiv.org/html/2607.23425v1#A11 — Appendix A11 Exact Prompts Given to the Language Models; https://arxiv.org/html/2607.23425v1#S2.SS1 — 2.1. TLA + and Model Checking | https://arxiv.org/html/2607.23425v1#A3 — Appendix A3 A Benchmark Instance; https://arxiv.org/html/2607.23425v1#S2.SS2 — 2.2. Specification and Code Generation Benchmarks | https://arxiv.org/html/2607.23425v1#A6 — Appendix A6 A Worked Failure in Full; https://arxiv.org/html/2607.23425v1#S10 — 10. Future Work | Exact v1 links https://github.com/LUC-AI4FM/tla_benchmark/tree/reviewer-release, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23425 | complete |
| SF-2026-ARXIV-2607-23438 | RP-0ddc46b225b7c5d3 | standard | arXiv:2607.23438v1 | SRC-ARXIV@arXiv:2607.23438v1 | https://arxiv.org/pdf/2607.23438v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23438v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.23438v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23438v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.23438v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23438v1#page=10 — PDF page 10 | Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary. | claim:SF-2026-ARXIV-2607-23438 | complete |
| SF-2026-ARXIV-2607-23444 | RP-90195221e36aa746 | deep | arXiv:2607.23444v1 | SRC-ARXIV@arXiv:2607.23444v1 | https://arxiv.org/html/2607.23444v1#A6 — Appendix F LTM framework; https://arxiv.org/html/2607.23444v1#S2.SS2 — 2.2 Data Extraction against RAG-Based Systems | https://arxiv.org/html/2607.23444v1#A7 — Appendix G Experimental Result; https://arxiv.org/html/2607.23444v1#S5.SS2 — 5.2 Experimental Evaluation | https://arxiv.org/html/2607.23444v1#S3.SS1 — 3.1 Threat Model; https://arxiv.org/html/2607.23444v1#S8 — 8 Discussion | Exact v1 links https://huggingface.co/datasets/wangrongsheng/HealthCareMagic-100k-en, https://github.com/snap-research/LoCoMo, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23444 | complete |
| SF-2026-ARXIV-2607-23445 | RP-c38801f5037e54b0 | standard | arXiv:2607.23445v1 | SRC-ARXIV@arXiv:2607.23445v1 | https://arxiv.org/html/2607.23445v1#S3 — 3 Method; https://arxiv.org/html/2607.23445v1#A3 — Appendix C Notation and Implementation Details | https://arxiv.org/html/2607.23445v1#A1 — Appendix A More Experimental Results; https://arxiv.org/html/2607.23445v1#S4 — 4 Experiments | https://arxiv.org/html/2607.23445v1#A6 — Appendix F Discussion; https://arxiv.org/html/2607.23445v1#S5 — 5 Conclusion | Exact v1 links https://github.com/kimberlyii/Omni-Prune, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23445 | complete |
| SF-2026-ARXIV-2607-23458 | RP-78d5c096ce20ebf3 | standard | arXiv:2607.23458v1 | SRC-ARXIV@arXiv:2607.23458v1 | https://arxiv.org/html/2607.23458v1#S7.SS1 — 7.1 Instructed construction: 7 models | https://arxiv.org/html/2607.23458v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23458v1#S2 — 2 Related Work | https://arxiv.org/html/2607.23458v1#S8 — 8 Discussion; https://arxiv.org/html/2607.23458v1#S9 — 9 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23458 | complete |
| SF-2026-ARXIV-2607-23472 | RP-1e670b3c150e5eb7 | standard | arXiv:2607.23472v1 | SRC-ARXIV@arXiv:2607.23472v1 | https://arxiv.org/html/2607.23472v1#S4 — 4 Method | https://arxiv.org/html/2607.23472v1#A3 — Appendix C Ablation on the Number of Learnable Queries; https://arxiv.org/html/2607.23472v1#A4 — Appendix D Evaluation Details | https://arxiv.org/html/2607.23472v1#A6 — Appendix F Limitations and Failure Cases; https://arxiv.org/html/2607.23472v1#S6 — 6 Discussion | Exact v1 links https://github.com/Genesis-Embodied-AI/Genesis, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23472 | complete |
| SF-2026-ARXIV-2607-23478 | RP-4b65f1e5428df1f3 | standard | arXiv:2607.23478v1 | SRC-ARXIV@arXiv:2607.23478v1 | https://arxiv.org/html/2607.23478v1#S5.SS2 — 5.2. FHE Inference System Design; https://arxiv.org/html/2607.23478v1#A2 — Appendix B FHE Inference System Implementation | https://arxiv.org/html/2607.23478v1#A6 — Appendix F Extended Experimental Results; https://arxiv.org/html/2607.23478v1#A2.SS1 — B.1. Polynomial Evaluation with Paterson–Stockmeyer Method | https://arxiv.org/html/2607.23478v1#S2.SS4 — 2.4. Threat Model | Exact v1 links https://github.com/Microsoft/SEAL, https://github.com/timzsu/NEXUS-End2End, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23478 | complete |
| SF-2026-ARXIV-2607-23496 | RP-0d3a871194670c27 | standard | arXiv:2607.23496v1 | SRC-ARXIV@arXiv:2607.23496v1 | https://arxiv.org/html/2607.23496v1#A3.SS2 — C.2. Fixed-Template Methods; https://arxiv.org/html/2607.23496v1#A3.SS3 — C.3. LLM-Generated Methods | https://arxiv.org/html/2607.23496v1#A1 — Appendix A Steering Experiments with Predefined Scenarios; https://arxiv.org/html/2607.23496v1#S2.SS2 — 2.2. Safety Mechanistic Analysis | https://arxiv.org/html/2607.23496v1#S6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23496 | complete |
| SF-2026-ARXIV-2607-23504 | RP-8c1fffa4fb848cc1 | standard | arXiv:2607.23504v1 | SRC-ARXIV@arXiv:2607.23504v1 | https://arxiv.org/html/2607.23504v1#S3 — 3 Method; https://arxiv.org/html/2607.23504v1#S2.SS1 — 2.1 Large Vision-and-Language Models | https://arxiv.org/html/2607.23504v1#A4 — Appendix D Qualitative Results; https://arxiv.org/html/2607.23504v1#S4 — 4 Experiment | https://arxiv.org/html/2607.23504v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.23504v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23504 | complete |
| SF-2026-ARXIV-2607-23514 | RP-20c371b26c7580ee | standard | arXiv:2607.23514v1 | SRC-ARXIV@arXiv:2607.23514v1 | https://arxiv.org/html/2607.23514v1#S1 — 1. Introduction; https://arxiv.org/html/2607.23514v1#S2 — 2. Related Work | https://arxiv.org/html/2607.23514v1#S3.SS3 — 3.3. Evaluated MAFC Benchmarks; https://arxiv.org/html/2607.23514v1#S4 — 4. Experiments | https://arxiv.org/html/2607.23514v1#S5 — 5. Conclusion | Exact v1 links https://ifcncodeofprinciples.poynter.org/signatories, https://huggingface.co/google/embeddinggemma-300m, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23514 | complete |
| SF-2026-ARXIV-2607-23517 | RP-b02c3b038f42d58e | standard | arXiv:2607.23517v1 | SRC-ARXIV@arXiv:2607.23517v1 | https://arxiv.org/html/2607.23517v1#S3 — 3. Method; https://arxiv.org/html/2607.23517v1#S2.SS2 — 2.2. Interactive World Modeling | https://arxiv.org/html/2607.23517v1#S4 — 4. Experiments; https://arxiv.org/html/2607.23517v1#S4.SS4 — 4.4. Ablation Study | https://arxiv.org/html/2607.23517v1#S5 — 5. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23517 | complete |
| SF-2026-ARXIV-2607-23532 | RP-579cb221a37a430c | deep | arXiv:2607.23532v1 | SRC-ARXIV@arXiv:2607.23532v1 | https://arxiv.org/html/2607.23532v1#S3 — 3 Background, System Model, and Notation; https://arxiv.org/html/2607.23532v1#S5 — 5 Three-Tier Distributed Architecture over the RV-Fabric | https://arxiv.org/html/2607.23532v1#S7 — 7 Evaluation | https://arxiv.org/html/2607.23532v1#S7.SS6 — 7.6 Threats to Validity; https://arxiv.org/html/2607.23532v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23532 | complete |
| SF-2026-ARXIV-2607-23545 | RP-5ad5c10c8b4c31b4 | standard | arXiv:2607.23545v1 | SRC-ARXIV@arXiv:2607.23545v1 | https://arxiv.org/html/2607.23545v1#A1.SS2 — A.2 Implementation Details; https://arxiv.org/html/2607.23545v1#A2 — Appendix B Detailed implementation of XIH-Bench | https://arxiv.org/html/2607.23545v1#A1.SS1 — A.1 Code and Benchmark Release; https://arxiv.org/html/2607.23545v1#A2.SS6 — B.6 Benchmark Size and Instance Composition | https://arxiv.org/html/2607.23545v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.23545v1#Sx1 — Limitations | Exact v1 links https://github.com/g1moon/Language-Shapes-IH, https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23545 | complete |
| SF-2026-ARXIV-2607-23581 | RP-0d217fe408988bc8 | standard | arXiv:2607.23581v1 | SRC-ARXIV@arXiv:2607.23581v1 | https://arxiv.org/html/2607.23581v1#Sx4 — Method | https://arxiv.org/html/2607.23581v1#Sx5 — Experiments; https://arxiv.org/html/2607.23581v1#Sx5.SSx1 — Experimental Setup | https://arxiv.org/html/2607.23581v1#Sx6 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23581 | complete |
| SF-2026-ARXIV-2607-23586 | RP-ed061de43972853f | deep | arXiv:2607.23586v1 | SRC-ARXIV@arXiv:2607.23586v1 | https://arxiv.org/html/2607.23586v1#S3 — III System and Threat Model; https://arxiv.org/html/2607.23586v1#A1 — Appendix A Detailed Structured Model | https://arxiv.org/html/2607.23586v1#S8 — VIII Evaluation Path and Limitations | https://arxiv.org/html/2607.23586v1#A2 — Appendix B Expanded Limitations and Open Problems; https://arxiv.org/html/2607.23586v1#S3 — III System and Threat Model | Exact v1 links https://owasp.org/www-project-agentic-skills-top-10/, https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23586 | complete |
| SF-2026-ARXIV-2607-23588 | RP-83193871a390521e | standard | arXiv:2607.23588v1 | SRC-ARXIV@arXiv:2607.23588v1 | https://arxiv.org/html/2607.23588v1#S2 — 2 Method | https://arxiv.org/html/2607.23588v1#S3 — 3 Experiments; https://arxiv.org/html/2607.23588v1#S3.SS1 — 3.1 Experimental Setup | https://arxiv.org/html/2607.23588v1#S5 — 5 Conclusion and Limitations; https://arxiv.org/html/2607.23588v1#S4 — 4 Discussion | Exact v1 links https://github.com/LYL1015/JarvisHub, https://github.com/libtv-labs/libtv-skills, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23588 | complete |
| SF-2026-ARXIV-2607-23602 | RP-6dc8dde46a86275e | standard | arXiv:2607.23602v1 | SRC-ARXIV@arXiv:2607.23602v1 | https://arxiv.org/html/2607.23602v1#A6.SS3 — F.3 Method Development and Confirmatory Evaluation Protocol; https://arxiv.org/html/2607.23602v1#A11 — Appendix K Replication with an Independently Trained World Model | https://arxiv.org/html/2607.23602v1#A10 — Appendix J Cube Results Stratified by Task Conditions; https://arxiv.org/html/2607.23602v1#A12 — Appendix L Joint Latent and Action Neighborhood Results and Controls | https://arxiv.org/html/2607.23602v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.23602v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23602 | complete |
| SF-2026-ARXIV-2607-23605 | RP-6db1cfd4897375d9 | standard | arXiv:2607.23605v1 | SRC-ARXIV@arXiv:2607.23605v1 | https://arxiv.org/html/2607.23605v1#S4 — 4 Method | https://arxiv.org/html/2607.23605v1#A1 — Appendix A Theoretical Analysis for Section 4; https://arxiv.org/html/2607.23605v1#A2 — Appendix B Experiment Details | https://arxiv.org/html/2607.23605v1#S6 — 6 Conclusion | Exact v1 links https://github.com/mpSchrader/gym-sokoban, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23605 | complete |
| SF-2026-ARXIV-2607-23624 | RP-01a3ae5315241ac6 | standard | arXiv:2607.23624v1 | SRC-ARXIV@arXiv:2607.23624v1 | https://arxiv.org/html/2607.23624v1#S3 — 3 Study Design; https://arxiv.org/html/2607.23624v1#S3.SS4 — 3.4 Experimental Framework: SIDEL | https://arxiv.org/html/2607.23624v1#S5 — 5 Results Analysis; https://arxiv.org/html/2607.23624v1#A2.SS3 — B.3 Comparative Rewrite Outcomes and Analysis | https://arxiv.org/html/2607.23624v1#S6 — 6 Threats to Validity; https://arxiv.org/html/2607.23624v1#S7 — 7 Conclusion | Exact v1 links https://github.com/Riyasushin/SIDE, https://github.com/BerriAI/litellm, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23624 | complete |
| SF-2026-ARXIV-2607-23670 | RP-fb9acf017d800399 | standard | arXiv:2607.23670v1 | SRC-ARXIV@arXiv:2607.23670v1 | https://arxiv.org/html/2607.23670v1#A0.SS1 — -A Relation of Design Features to Existing Plan Modes; https://arxiv.org/html/2607.23670v1#S3.SS3 — III-C Design Features | https://arxiv.org/html/2607.23670v1#S4.SS4 — IV-D Data Collection and Analysis; https://arxiv.org/html/2607.23670v1#S5 — V Results | https://arxiv.org/html/2607.23670v1#S6 — VI Discussion; https://arxiv.org/html/2607.23670v1#S7 — VII Conclusion | Exact v1 links https://code.claude.com/docs/en/permission-modes, https://code.visualstudio.com/docs/copilot/agents/planning, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23670 | complete |
| SF-2026-ARXIV-2607-23693 | RP-bf135f7c642c1a60 | deep | arXiv:2607.23693v1 | SRC-ARXIV@arXiv:2607.23693v1 | https://arxiv.org/html/2607.23693v1#A5 — Appendix E Decoy design and scoring conventions; https://arxiv.org/html/2607.23693v1#A3 — Appendix C Legacy-model diagnostics | https://arxiv.org/html/2607.23693v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23693v1#S2 — 2 The serving contract | https://arxiv.org/html/2607.23693v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.23693v1#S9 — 9 Limitations and scope | Exact v1 links https://github.com/oklen/Compute-Globally-Materialize-Locally, https://huggingface.co/Qwen/Qwen3.6-27B, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23693 | complete |
| SF-2026-ARXIV-2607-23700 | RP-01e954e82d9b800c | standard | arXiv:2607.23700v1 | SRC-ARXIV@arXiv:2607.23700v1 | https://arxiv.org/html/2607.23700v1#S4 — 4 Method | https://arxiv.org/html/2607.23700v1#S5 — 5 Experiments; https://arxiv.org/html/2607.23700v1#S15 — 15 Case Study | https://arxiv.org/html/2607.23700v1#S7 — 7 Conclusion | Exact v1 links https://github.com/OpenBMB/MiniCPM-o, https://github.com/yuh-zha/Vision-G1, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23700 | complete |
| SF-2026-ARXIV-2607-23702 | RP-e078da02c35541a1 | standard | arXiv:2607.23702v1 | SRC-ARXIV@arXiv:2607.23702v1 | https://arxiv.org/html/2607.23702v1#S3 — III Method | https://arxiv.org/html/2607.23702v1#S4 — IV Experiments; https://arxiv.org/html/2607.23702v1#S4.SS2 — IV-B Results | https://arxiv.org/html/2607.23702v1#S5 — V Conclusion | Exact v1 links https://huggingface.co/moka-ai/m3e-small, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23702 | complete |
| SF-2026-ARXIV-2607-23704 | RP-516dc04326b4631a | standard | arXiv:2607.23704v1 | SRC-ARXIV@arXiv:2607.23704v1 | https://arxiv.org/html/2607.23704v1#Sx4.SSx2 — Architecture and Hybrid Fine-tuning | https://arxiv.org/html/2607.23704v1#Sx5.SSx2 — Quantitative Experimental Results; https://arxiv.org/html/2607.23704v1#A3 — Appendix C Experiment Details | https://arxiv.org/html/2607.23704v1#Sx6 — Conclusion and Limitations; https://arxiv.org/html/2607.23704v1#A2.SSx1 — Safety Failure | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23704 | complete |
| SF-2026-ARXIV-2607-23710 | RP-822a940ab82bfc27 | standard | arXiv:2607.23710v1 | SRC-ARXIV@arXiv:2607.23710v1 | https://arxiv.org/html/2607.23710v1#S3 — 3 Methodology; https://arxiv.org/html/2607.23710v1#S4.SS4 — 4.4 Cross-Framework Translation of Security Context | https://arxiv.org/html/2607.23710v1#S3.SS1 — 3.1 Experimental Prompt Formulations; https://arxiv.org/html/2607.23710v1#S4 — 4 Results | https://arxiv.org/html/2607.23710v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.23710v1#S5 — 5 Discussion | Exact v1 links https://github.com/ipa-lab/hackingBuddyGPT, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23710 | complete |
| SF-2026-ARXIV-2607-23711 | RP-07068bd993ef1b6b | standard | arXiv:2607.23711v1 | SRC-ARXIV@arXiv:2607.23711v1 | https://arxiv.org/html/2607.23711v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23711v1#S2 — 2 Theory: an exactness ladder | https://arxiv.org/html/2607.23711v1#S2.SS3 — 2.3 The evaluation point and its sensitivity | https://arxiv.org/html/2607.23711v1#S7 — 7 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23711 | complete |
| SF-2026-ARXIV-2607-23722 | RP-0a6471f40a115cfd | standard | arXiv:2607.23722v1 | SRC-ARXIV@arXiv:2607.23722v1 | https://arxiv.org/html/2607.23722v1#A1.SS2 — A.2 Per-Model Effect of Code Execution; https://arxiv.org/html/2607.23722v1#S4.SS5 — 4.5 When Do Models Choose to Code? Per-Task Analysis | https://arxiv.org/html/2607.23722v1#A1 — Appendix A More Benchmark Results Analysis; https://arxiv.org/html/2607.23722v1#A1.SS4 — A.4 API Cost-Efficiency Analysis | https://arxiv.org/html/2607.23722v1#S5 — 5 Conclusion and Future Work | Exact v1 links https://doi.org/10.18653/v1/2025.emnlp-demos.27, https://aclanthology.org/2025.emnlp-demos.27/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23722 | complete |
| SF-2026-ARXIV-2607-23731 | RP-f7c9e1bfc798bb26 | standard | arXiv:2607.23731v1 | SRC-ARXIV@arXiv:2607.23731v1 | https://arxiv.org/html/2607.23731v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23731v1#S2 — 2 Setting: Dense Supervision on Student Prefixes | https://arxiv.org/html/2607.23731v1#A1 — Appendix A Additional Experimental Details and Tables | https://arxiv.org/html/2607.23731v1#S9 — 9 Limitations and Conclusion; https://arxiv.org/html/2607.23731v1#A1.SS5 — A.5 Illustrative agreement-on-failure trace | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23731 | complete |
| SF-2026-ARXIV-2607-23765 | RP-cdf4af524b9c4464 | standard | arXiv:2607.23765v1 | SRC-ARXIV@arXiv:2607.23765v1 | https://arxiv.org/html/2607.23765v1#S4 — 4 Our Method; https://arxiv.org/html/2607.23765v1#A8.SS2 — H.2 Baseline Implementation | https://arxiv.org/html/2607.23765v1#A8.SS5 — H.5 WR-Offline Experiment Result on SWE-Bench; https://arxiv.org/html/2607.23765v1#A8 — Appendix H Experimental Details | https://arxiv.org/html/2607.23765v1#S7 — 7 Conclusions and Limitations; https://arxiv.org/html/2607.23765v1#A1 — Appendix A Discussion of Assumptions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23765 | complete |
| SF-2026-ARXIV-2607-23771 | RP-afa835cfe32f7d7f | deep | arXiv:2607.23771v1 | SRC-ARXIV@arXiv:2607.23771v1 | https://arxiv.org/html/2607.23771v1#A2.SS3 — B.3 System Prompt Format; https://arxiv.org/html/2607.23771v1#A2.SS2 — B.2 Controller implementations | https://arxiv.org/html/2607.23771v1#S6 — 6 Experiments; https://arxiv.org/html/2607.23771v1#S6.SS1 — 6.1 Experimental Setup | https://arxiv.org/html/2607.23771v1#A5.SS1 — E.1 Quality-Diversity: Final Decision Agent recovers from unanimous CoT failure; https://arxiv.org/html/2607.23771v1#S7 — 7 Conclusion | Exact v1 links https://huggingface.co/datasets/math-ai/amc23, https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23771 | complete |
| SF-2026-ARXIV-2607-23782 | RP-1d6f6a9b80a0df3e | standard | arXiv:2607.23782v1 | SRC-ARXIV@arXiv:2607.23782v1 | https://arxiv.org/html/2607.23782v1#S2.SS1 — 2.1 Base Architecture; https://arxiv.org/html/2607.23782v1#S2 — 2 Model | https://arxiv.org/html/2607.23782v1#A5 — Appendix E Per-Task Results and Scoring Rubrics; https://arxiv.org/html/2607.23782v1#S5 — 5 Experiments | https://arxiv.org/html/2607.23782v1#S8 — 8 Conclusion | Exact v1 links https://github.com/neoteai/N0-VTLA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23782 | complete |
| SF-2026-ARXIV-2607-23783 | RP-621570fa3dbb7d98 | standard | arXiv:2607.23783v1 | SRC-ARXIV@arXiv:2607.23783v1 | https://arxiv.org/html/2607.23783v1#S2.SS1 — 2.1 Model architecture; https://arxiv.org/html/2607.23783v1#S2 — 2 Model | https://arxiv.org/html/2607.23783v1#A1 — Appendix A Per-task ablation results; https://arxiv.org/html/2607.23783v1#A2 — Appendix B Per-task tactile-realism results | https://arxiv.org/html/2607.23783v1#S6 — 6 Conclusion | Exact v1 links https://github.com/neoteai/N0-TWAM, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23783 | complete |
| SF-2026-ARXIV-2607-23802 | RP-316b2972de91ec50 | standard | arXiv:2607.23802v1 | SRC-ARXIV@arXiv:2607.23802v1 | https://arxiv.org/html/2607.23802v1#A3.SS5 — C.5 Prompt Design and Configurations; https://arxiv.org/html/2607.23802v1#A3 — Appendix C Implementation Details | https://arxiv.org/html/2607.23802v1#A4 — Appendix D Additional Experiments; https://arxiv.org/html/2607.23802v1#A4.SS4 — D.4 Evaluation with an Alternative LLM Judge | https://arxiv.org/html/2607.23802v1#S5 — 5 Conclusion | Exact v1 links https://github.com/wangqinsi1/SpyRL, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23802 | complete |
| SF-2026-ARXIV-2607-23809 | RP-61f6d29f7bd08508 | deep | arXiv:2607.23809v1 | SRC-ARXIV@arXiv:2607.23809v1 | https://arxiv.org/html/2607.23809v1#A2.SS1 — B.1 Agent system prompt; https://arxiv.org/html/2607.23809v1#S3 — 3 Agentic Context Management Framework | https://arxiv.org/html/2607.23809v1#A3.SS3 — C.3 Results and Analysis; https://arxiv.org/html/2607.23809v1#A3 — Appendix C Exploration Diversity Analysis | https://arxiv.org/html/2607.23809v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.23809v1#Sx1 — Limitations | Exact v1 links https://github.com/lixiaochuan2020/agentic-context-management, https://www.anthropic.com/claude-code, https://github.com/openai/codex; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23809 | complete |
| SF-2026-ARXIV-2607-23815 | RP-5874c840ff86db24 | deep | arXiv:2607.23815v1 | SRC-ARXIV@arXiv:2607.23815v1 | https://arxiv.org/html/2607.23815v1#S5.SS3 — 5.3. The Kalypso Scheduling Algorithm; https://arxiv.org/html/2607.23815v1#S7.SS2 — 7.2. Workloads and Implementations | https://arxiv.org/html/2607.23815v1#S7 — 7. Evaluation; https://arxiv.org/html/2607.23815v1#S7.SS1 — 7.1. Experimental Setup | https://arxiv.org/html/2607.23815v1#S9 — 9. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23815 | complete |
| SF-2026-ARXIV-2607-23838 | RP-0d9aa5e422e9b31f | standard | arXiv:2607.23838v1 | SRC-ARXIV@arXiv:2607.23838v1 | https://arxiv.org/html/2607.23838v1#S5 — V Proposed TriShieldRAG Framework; https://arxiv.org/html/2607.23838v1#S3 — III Threat Model | https://arxiv.org/html/2607.23838v1#S9 — IX Experimental Results; https://arxiv.org/html/2607.23838v1#S8 — VIII Experimental Setup | https://arxiv.org/html/2607.23838v1#S10 — X Discussion and Limitations; https://arxiv.org/html/2607.23838v1#S11 — XI Conclusion and Future Work | Exact v1 links https://github.com/SPriTLab-iitj/TriShieldRAG, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23838 | complete |
| SF-2026-ARXIV-2607-23844 | RP-bcda4c3a620cf528 | standard | arXiv:2607.23844v1 | SRC-ARXIV@arXiv:2607.23844v1 | https://arxiv.org/html/2607.23844v1#S3 — 3 Methods; https://arxiv.org/html/2607.23844v1#S4.SS2 — 4.2 Design Choices | https://arxiv.org/html/2607.23844v1#A1.SS1 — A.1 Performance Evaluation of Triton Kernels; https://arxiv.org/html/2607.23844v1#S4 — 4 Experiments | https://arxiv.org/html/2607.23844v1#S5 — 5 Limitations; https://arxiv.org/html/2607.23844v1#S6 — 6 Conclusion | Exact v1 links https://github.com/hpcaitech/Open-Sora/tree/main, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23844 | complete |
| SF-2026-ARXIV-2607-23870 | RP-b60d707619823f18 | standard | arXiv:2607.23870v1 | SRC-ARXIV@arXiv:2607.23870v1 | https://arxiv.org/html/2607.23870v1#S3.SS1 — III-A Hierarchical Task Design; https://arxiv.org/html/2607.23870v1#S4.SS5 — IV-E Model Comparison | https://arxiv.org/html/2607.23870v1#S2.SS4 — II-D Benchmark Boundary Analysis; https://arxiv.org/html/2607.23870v1#S4 — IV Experiments and Analysis | https://arxiv.org/html/2607.23870v1#S4.SS7 — IV-G Discussion; https://arxiv.org/html/2607.23870v1#S4.SS8 — IV-H Limitations | Exact v1 links https://huggingface.co/HuggingFaceTB/SmolVLM2-2.2B-Instruct, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23870 | complete |
| SF-2026-ARXIV-2607-23884 | RP-09dc7b3a926317d6 | standard | arXiv:2607.23884v1 | SRC-ARXIV@arXiv:2607.23884v1 | https://arxiv.org/html/2607.23884v1#S3 — 3 Methodology; https://arxiv.org/html/2607.23884v1#S2.SS2 — 2.2 Model Context Protocol (MCP) | https://arxiv.org/html/2607.23884v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.23884v1#S5.SS1 — 5.1 Analysis of Implementation and Coordination Complexity | https://arxiv.org/html/2607.23884v1#S6 — 6 Conclusions | Exact v1 links https://github.com/AlDanial/cloc, https://github.com/modelcontextprotocol/inspector, https://github.com/arize-ai/phoenix; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23884 | complete |
| SF-2026-ARXIV-2607-23909 | RP-946fce9aae88ec39 | deep | arXiv:2607.23909v1 | SRC-ARXIV@arXiv:2607.23909v1 | https://arxiv.org/html/2607.23909v1#S2 — 2 Method | https://arxiv.org/html/2607.23909v1#S3 — 3 Experiments; https://arxiv.org/html/2607.23909v1#S3.SS2 — 3.2 Results | https://arxiv.org/html/2607.23909v1#S4 — 4 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23909 | complete |
| SF-2026-ARXIV-2607-23927 | RP-0fca2ab51bd3b54d | standard | arXiv:2607.23927v1 | SRC-ARXIV@arXiv:2607.23927v1 | https://arxiv.org/html/2607.23927v1#S5 — 5 Methods; https://arxiv.org/html/2607.23927v1#Sx14 — Prompt Architecture | https://arxiv.org/html/2607.23927v1#S5.SS4 — 5.4 Experiment 1: Data Analysis; https://arxiv.org/html/2607.23927v1#S5.SS5 — 5.5 Experiment 2: Data Analysis | https://arxiv.org/html/2607.23927v1#S3 — 3 Discussion; https://arxiv.org/html/2607.23927v1#S4 — 4 Conclusion | Exact v1 links https://github.com/saurabhr/LLM-RM/, https://github.com/saurabhr/psychscanner_v_0_1_0, https://CRAN.R-project.org/package=ordinal; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23927 | complete |
| SF-2026-ARXIV-2607-23929 | RP-fe869a0d7e46d09d | deep | arXiv:2607.23929v1 | SRC-ARXIV@arXiv:2607.23929v1 | https://arxiv.org/html/2607.23929v1#A1.SS1 — A.1 Sweep Design; https://arxiv.org/html/2607.23929v1#S3.SS1 — 3.1 Data Model and Belief Lifecycle | https://arxiv.org/html/2607.23929v1#A1.SS2 — A.2 Results; https://arxiv.org/html/2607.23929v1#A8 — Appendix H Benchmark Composition | https://arxiv.org/html/2607.23929v1#S6 — 6 Conclusion | Exact v1 links https://github.com/lxy1134/MEMTX_, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23929 | complete |
| SF-2026-ARXIV-2607-23933 | RP-77321d788d85b45b | deep | arXiv:2607.23933v1 | SRC-ARXIV@arXiv:2607.23933v1 | https://arxiv.org/html/2607.23933v1#S3 — 3. Design of SpecBox; https://arxiv.org/html/2607.23933v1#S4 — 4. Implementation | https://arxiv.org/html/2607.23933v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.23933v1#S5.SS1 — 5.1. Experiment Setup | https://arxiv.org/html/2607.23933v1#S6 — 6. Discussion; https://arxiv.org/html/2607.23933v1#S8 — 8. Conclusions | Exact v1 links https://github.com/datalayer/jupyter-mcp-server, https://github.com/mcp, https://github.com/microsoft/playwright#playwright-mcp; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23933 | complete |
| SF-2026-ARXIV-2607-23955 | RP-d9053a9f64701ca1 | standard | arXiv:2607.23955v1 | SRC-ARXIV@arXiv:2607.23955v1 | https://arxiv.org/html/2607.23955v1#S3 — 3 Methodology; https://arxiv.org/html/2607.23955v1#S3.SSx2 — Method Overview | https://arxiv.org/html/2607.23955v1#S4 — 4 Experiments; https://arxiv.org/html/2607.23955v1#S4.SSx1 — Experimental Setup | https://arxiv.org/html/2607.23955v1#S5 — 5 Discussion and Limitations; https://arxiv.org/html/2607.23955v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23955 | complete |
| SF-2026-ARXIV-2607-23969 | RP-2ec3e65db6716bb0 | standard | arXiv:2607.23969v1 | SRC-ARXIV@arXiv:2607.23969v1 | https://arxiv.org/html/2607.23969v1#Sx3 — Methodology; https://arxiv.org/html/2607.23969v1#Sx3.SSx1 — Framework Overview | https://arxiv.org/html/2607.23969v1#Sx4 — Experiments; https://arxiv.org/html/2607.23969v1#Sx4.SSx1 — Experimental Setup | https://arxiv.org/html/2607.23969v1#Sx5 — Conclusion and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23969 | complete |
| SF-2026-ARXIV-2607-23991 | RP-e053888258aaad8e | standard | arXiv:2607.23991v1 | SRC-ARXIV@arXiv:2607.23991v1 | https://arxiv.org/html/2607.23991v1#S3 — 3 Method; https://arxiv.org/html/2607.23991v1#A3 — Appendix C Training and Decoding Algorithms | https://arxiv.org/html/2607.23991v1#A4 — Appendix D Extended Analyses and Ablations; https://arxiv.org/html/2607.23991v1#A5 — Appendix E Token-wise Analysis | https://arxiv.org/html/2607.23991v1#Sx1 — Limitations and Future Work; https://arxiv.org/html/2607.23991v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/datasets/argilla/OpenHermesPreferences, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23991 | complete |
| SF-2026-ARXIV-2607-23999 | RP-bdeb760400837b63 | deep | arXiv:2607.23999v1 | SRC-ARXIV@arXiv:2607.23999v1 | https://arxiv.org/html/2607.23999v1#S3.SS1 — 3.1. System Model; https://arxiv.org/html/2607.23999v1#S4.SS1 — 4.1. Design Goals | https://arxiv.org/html/2607.23999v1#S2.SS1 — 2.1. Outcome-Oriented Prompt-Injection Benchmarks; https://arxiv.org/html/2607.23999v1#S6 — 6. Experimental Protocol | https://arxiv.org/html/2607.23999v1#S8 — 8. Discussion and Limitations; https://arxiv.org/html/2607.23999v1#S10 — 10. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-23999 | complete |
| SF-2026-ARXIV-2607-24008 | RP-5866134965ef734f | standard | arXiv:2607.24008v1 | SRC-ARXIV@arXiv:2607.24008v1 | https://arxiv.org/html/2607.24008v1#Sx4 — Methodology; https://arxiv.org/html/2607.24008v1#Sx8.SSx2 — Task Design | https://arxiv.org/html/2607.24008v1#Sx5.SSx2 — Ablation and Analysis; https://arxiv.org/html/2607.24008v1#Sx10 — Ablation Study | https://arxiv.org/html/2607.24008v1#Sx11 — Limitations; https://arxiv.org/html/2607.24008v1#Sx6 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24008 | complete |
| SF-2026-ARXIV-2607-24010 | RP-db1e1ca6086e90b9 | standard | arXiv:2607.24010v1 | SRC-ARXIV@arXiv:2607.24010v1 | https://arxiv.org/html/2607.24010v1#S3.SS0.SSS0.Px2 — Cost model.; https://arxiv.org/html/2607.24010v1#S4.SS0.SSS0.Px2 — Models and retrieval. | https://arxiv.org/html/2607.24010v1#S4 — 4. Experimental Setup; https://arxiv.org/html/2607.24010v1#S5 — 5. Results | https://arxiv.org/html/2607.24010v1#S5.SS0.SSS0.Px3 — RQ3: Do calibrated thresholds meet future budgets?; https://arxiv.org/html/2607.24010v1#S5.SS0.SSS0.Px5 — RQ5: How does cost accounting change the conclusion? | Exact v1 links https://huggingface.co/ibm-granite/granite-3.1-2b-instruct, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24010 | complete |
| SF-2026-ARXIV-2607-24027 | RP-0ca63deb507020c2 | standard | arXiv:2607.24027v1 | SRC-ARXIV@arXiv:2607.24027v1 | https://arxiv.org/html/2607.24027v1#S3 — 3 Methodology | https://arxiv.org/html/2607.24027v1#A1 — Appendix A Additional Experimental Details; https://arxiv.org/html/2607.24027v1#A2 — Appendix B Derivations and Error Analysis | https://arxiv.org/html/2607.24027v1#S6 — 6 Conclusion | Exact v1 links https://github.com/NVlabs/Sana/tree/sol-engine, https://huggingface.co/Lightricks/LTX-2.3, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24027 | complete |
| SF-2026-ARXIV-2607-24054 | RP-2a358a6f86ab7179 | standard | arXiv:2607.24054v1 | SRC-ARXIV@arXiv:2607.24054v1 | https://arxiv.org/html/2607.24054v1#Sx3 — AcquaBench Design; https://arxiv.org/html/2607.24054v1#A2.SS6 — B.6 Bootstrap and Model Common Support | https://arxiv.org/html/2607.24054v1#A1.SS1 — A.1 Matched Evaluation Unit; https://arxiv.org/html/2607.24054v1#A3 — Appendix C Complete Frozen Results | https://arxiv.org/html/2607.24054v1#Sx6 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24054 | complete |
| SF-2026-ARXIV-2607-24063 | RP-432ff8733fd2fef3 | standard | arXiv:2607.24063v1 | SRC-ARXIV@arXiv:2607.24063v1 | https://arxiv.org/html/2607.24063v1#Sx3 — MAS-HQ Framework and Reference Architecture; https://arxiv.org/html/2607.24063v1#Sx4.SSx3 — Resource-Efficient Behavior and Frontier-Model Comparisons | https://arxiv.org/html/2607.24063v1#A3 — Appendix C More Ablation Studies; https://arxiv.org/html/2607.24063v1#A4 — Appendix D Prompts and Other Results | https://arxiv.org/html/2607.24063v1#Sx5 — Conclusion | Exact v1 links https://huggingface.co/vectara/hallucination_evaluation_model, https://huggingface.co/datasets/vectara/leaderboard_results, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24063 | complete |
| SF-2026-ARXIV-2607-24097 | RP-b22cbd9840f487c7 | standard | arXiv:2607.24097v1 | SRC-ARXIV@arXiv:2607.24097v1 | https://arxiv.org/html/2607.24097v1#S4 — 4 Method | https://arxiv.org/html/2607.24097v1#S5.SS2 — 5.2 Results and Analysis; https://arxiv.org/html/2607.24097v1#A1 — Appendix A Experimental Details and Additional Analyses | https://arxiv.org/html/2607.24097v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.24097v1#S7 — 7 Limitations | Exact v1 links https://github.com/mayiwen0212/MemChain, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24097 | complete |
| SF-2026-ARXIV-2607-24112 | RP-dab1ea7eb4bef1fc | standard | arXiv:2607.24112v1 | SRC-ARXIV@arXiv:2607.24112v1 | https://arxiv.org/html/2607.24112v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24112v1#S2 — 2 State Transition Pretraining for GUI Agents | https://arxiv.org/html/2607.24112v1#S3 — 3 Experiments; https://arxiv.org/html/2607.24112v1#S3.SS1 — 3.1 Experimental Setup | https://arxiv.org/html/2607.24112v1#S5 — 5 Limitations; https://arxiv.org/html/2607.24112v1#S7 — 7 Conclusion | Exact v1 links https://github.com/xyliugo/gui-state-transition-pretraining, https://github.com/bytedance-seed/BAGEL, https://openai.com/index/codex-for-almost-everything/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24112 | complete |
| SF-2026-ARXIV-2607-24117 | RP-8476d83bc2f7d95f | standard | arXiv:2607.24117v1 | SRC-ARXIV@arXiv:2607.24117v1 | https://arxiv.org/html/2607.24117v1#S0.SSx2.SSSx3 — 2.3 Multi-agent knowledge systems and the provenance state of the art; https://arxiv.org/html/2607.24117v1#S0.SSx4 — 4. The Isnād–Rijāl Framework | https://arxiv.org/html/2607.24117v1#S0.SSx8 — 8. Evaluation; https://arxiv.org/html/2607.24117v1#S0.SSx6 — 6. Case study: the matn-criticism substrate on real texts | https://arxiv.org/html/2607.24117v1#S0.SSx3 — 3. Threat model and scope; https://arxiv.org/html/2607.24117v1#S0.SSx7 — 7. Limitations and ethical considerations | Exact v1 links https://github.com/alizahidraja/isnad, https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24117 | complete |
| SF-2026-ARXIV-2607-24148 | RP-fb12a7b115a8fff8 | standard | arXiv:2607.24148v1 | SRC-ARXIV@arXiv:2607.24148v1 | https://arxiv.org/html/2607.24148v1#S2.SS3 — 2.3. VLA Accelerator Design; https://arxiv.org/html/2607.24148v1#S6 — 6. Architecture | https://arxiv.org/html/2607.24148v1#S7 — 7. Evaluation; https://arxiv.org/html/2607.24148v1#S7.SS2 — 7.2. VQVLA Algorithm Evaluation | https://arxiv.org/html/2607.24148v1#S9 — 9. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24148 | complete |
| SF-2026-ARXIV-2607-24157 | RP-84ca04d1814f8853 | standard | arXiv:2607.24157v1 | SRC-ARXIV@arXiv:2607.24157v1 | https://arxiv.org/html/2607.24157v1#A4.SS4 — D.4 Ablation Study on Design of Ref Tokens; https://arxiv.org/html/2607.24157v1#S3 — 3 Method | https://arxiv.org/html/2607.24157v1#S4 — 4 Experimental Evaluations; https://arxiv.org/html/2607.24157v1#A4 — Appendix D Additional Evaluations | https://arxiv.org/html/2607.24157v1#S4.SS5 — 4.5 Limitation and Future Work; https://arxiv.org/html/2607.24157v1#A2 — Appendix B Failure Mode | Exact v1 links https://zpbao.github.io/projects/unigenar, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24157 | complete |
| SF-2026-ARXIV-2607-24159 | RP-891de578b6657433 | standard | arXiv:2607.24159v1 | SRC-ARXIV@arXiv:2607.24159v1 | https://arxiv.org/html/2607.24159v1#A1.SS1 — A.1 Video Expert Architecture; https://arxiv.org/html/2607.24159v1#A1.SS2 — A.2 Action Expert Architecture | https://arxiv.org/html/2607.24159v1#A3.SS2 — C.2 Evaluation Score Criteria; https://arxiv.org/html/2607.24159v1#A3.SS4 — C.4 Robustness Analysis for DeVA | https://arxiv.org/html/2607.24159v1#S6 — 6 Limitation; https://arxiv.org/html/2607.24159v1#S7 — 7 Conclusion | Exact v1 links https://github.com/nvidia-cosmos/cosmos-predict2, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24159 | complete |
| SF-2026-ARXIV-2607-24162 | RP-26ca79ae3ae7fbf6 | standard | arXiv:2607.24162v1 | SRC-ARXIV@arXiv:2607.24162v1 | https://arxiv.org/html/2607.24162v1#Sx3 — Method | https://arxiv.org/html/2607.24162v1#Sx4 — Experiments; https://arxiv.org/html/2607.24162v1#Sx4.SSx1 — Experimental Setup | https://arxiv.org/html/2607.24162v1#Sx5 — Discussion and Limitations; https://arxiv.org/html/2607.24162v1#Sx6 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24162 | complete |
| SF-2026-ARXIV-2607-24165 | RP-08938fe05f7e8967 | standard | arXiv:2607.24165v1 | SRC-ARXIV@arXiv:2607.24165v1 | https://arxiv.org/html/2607.24165v1#S3 — 3 Study Design; https://arxiv.org/html/2607.24165v1#S3.SS3 — 3.3 Systems and controlled interventions | https://arxiv.org/html/2607.24165v1#S4 — 4 Results; https://arxiv.org/html/2607.24165v1#as1_S10.SS6 — 10.6 Effect on Evaluation | https://arxiv.org/html/2607.24165v1#S7 — 7 Scope, Limitations, and Release; https://arxiv.org/html/2607.24165v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24165 | complete |
| SF-2026-ARXIV-2607-24167 | RP-d9fc82ed331525f8 | standard | arXiv:2607.24167v1 | SRC-ARXIV@arXiv:2607.24167v1 | https://arxiv.org/html/2607.24167v1#S5 — 5 The Proposed Method; https://arxiv.org/html/2607.24167v1#A2 — Appendix B Implementation Details | https://arxiv.org/html/2607.24167v1#A2.SS6 — B.6 Dataset Split and Evaluation Protocol; https://arxiv.org/html/2607.24167v1#A3 — Appendix C Complementary Experiments | https://arxiv.org/html/2607.24167v1#A1 — Appendix A Discussion; https://arxiv.org/html/2607.24167v1#A2.SS4 — B.4 Implementation Details of the Failure-Repair Library | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24167 | complete |
| SF-2026-ARXIV-2607-24174 | RP-a3aa1bba97961bee | standard | arXiv:2607.24174v1 | SRC-ARXIV@arXiv:2607.24174v1 | https://arxiv.org/html/2607.24174v1#S3.SS2 — 3.2. Threat Model | https://arxiv.org/html/2607.24174v1#S4 — 4. Experiments | https://arxiv.org/html/2607.24174v1#S3.SS2 — 3.2. Threat Model; https://arxiv.org/html/2607.24174v1#S5 — 5. Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24174 | complete |
| SF-2026-ARXIV-2607-24223 | RP-c6d32cf3084a2f21 | standard | arXiv:2607.24223v1 | SRC-ARXIV@arXiv:2607.24223v1 | https://arxiv.org/html/2607.24223v1#A1.SS1 — A.1 System Prompt of BC+; https://arxiv.org/html/2607.24223v1#A1.SS2 — A.2 System Prompt of BRIGHT | https://arxiv.org/html/2607.24223v1#S4 — 4 Experiments; https://arxiv.org/html/2607.24223v1#S4.SS1 — 4.1 Experiment Setup | https://arxiv.org/html/2607.24223v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.24223v1#Sx1 — Limitations | Exact v1 links https://github.com/LeqsNaN/RARG, https://github.com/texttron/RISE, https://github.com/NVIDIA/NeMo-Retriever/tree/main/retrieval-bench; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24223 | complete |
| SF-2026-ARXIV-2607-24260 | RP-e6713ec7966942ad | deep | arXiv:2607.24260v1 | SRC-ARXIV@arXiv:2607.24260v1 | https://arxiv.org/html/2607.24260v1#S2.SS2 — 2.2 KAP compiler–executor architecture; https://arxiv.org/html/2607.24260v1#S4 — 4 Cost Model and Phase-Boundary Analysis | https://arxiv.org/html/2607.24260v1#S4 — 4 Cost Model and Phase-Boundary Analysis; https://arxiv.org/html/2607.24260v1#S5 — 5 Experiments | https://arxiv.org/html/2607.24260v1#S7 — 7 Limitations; https://arxiv.org/html/2607.24260v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24260 | complete |
| SF-2026-ARXIV-2607-24267 | RP-c6126fbd3f10e6f3 | standard | arXiv:2607.24267v1 | SRC-ARXIV@arXiv:2607.24267v1 | https://arxiv.org/html/2607.24267v1#S3 — III Method; https://arxiv.org/html/2607.24267v1#S2.SS1 — II-A Action-Conditioned World Models | https://arxiv.org/html/2607.24267v1#S4 — IV Experiments; https://arxiv.org/html/2607.24267v1#S4.SS1 — IV-A Experimental Setup | https://arxiv.org/html/2607.24267v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24267 | complete |
| SF-2026-ARXIV-2607-24268 | RP-0f8c3d30ce4f20e2 | standard | arXiv:2607.24268v1 | SRC-ARXIV@arXiv:2607.24268v1 | https://arxiv.org/html/2607.24268v1#S3 — III Measurement Design; https://arxiv.org/html/2607.24268v1#S3.SS2 — III-B Questions, Models, and Prompts | https://arxiv.org/html/2607.24268v1#S4 — IV Results | https://arxiv.org/html/2607.24268v1#S4.SS1 — IV-A Failure Mixtures Vary across Studied Configurations; https://arxiv.org/html/2607.24268v1#S5 — V Implications and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24268 | complete |
| SF-2026-ARXIV-2607-24280 | RP-24338b626e9924ca | standard | arXiv:2607.24280v1 | SRC-ARXIV@arXiv:2607.24280v1 | https://arxiv.org/html/2607.24280v1#S3 — 3 Methodology; https://arxiv.org/html/2607.24280v1#S3.SS2 — 3.2 Multi-Agent System Generation Pipeline | https://arxiv.org/html/2607.24280v1#S4 — 4 Experiments and Analysis; https://arxiv.org/html/2607.24280v1#S4.SS2 — 4.2 Results and Analysis | https://arxiv.org/html/2607.24280v1#S6 — 6 Conclusion | Exact v1 links https://github.com/AaronLiu0702/MAPD, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24280 | complete |
| SF-2026-ARXIV-2607-24300 | RP-f492bef78bedd4a0 | standard | arXiv:2607.24300v1 | SRC-ARXIV@arXiv:2607.24300v1 | https://arxiv.org/html/2607.24300v1#Sx3.SSx4 — Design Conditions | https://arxiv.org/html/2607.24300v1#Sx4 — Experiments; https://arxiv.org/html/2607.24300v1#Sx4.SSx1 — Experimental Setup | https://arxiv.org/html/2607.24300v1#Sx5 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24300 | complete |
| SF-2026-ARXIV-2607-24306 | RP-0b1a8ef5ab1dd241 | standard | arXiv:2607.24306v1 | SRC-ARXIV@arXiv:2607.24306v1 | https://arxiv.org/html/2607.24306v1#S2.SS2 — 2.2 Sampling Methods for MDMs; https://arxiv.org/html/2607.24306v1#A3.SS1 — C.1 Model Checkpoints | https://arxiv.org/html/2607.24306v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.24306v1#A3.SS4 — C.4 Benchmarks | https://arxiv.org/html/2607.24306v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.24306v1#Sx1 — Limitations | Exact v1 links https://github.com/EleutherAI/lm-evaluation-harness, https://huggingface.co/Efficient-Large-Model/Fast_dLLM_v2_7B, https://huggingface.co/JetLM/SDAR-8B-Chat-b32; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24306 | complete |
| SF-2026-ARXIV-2607-24331 | RP-2326d5798d4a4720 | deep | arXiv:2607.24331v1 | SRC-ARXIV@arXiv:2607.24331v1 | https://arxiv.org/html/2607.24331v1#S3 — III Methodology | https://arxiv.org/html/2607.24331v1#S4 — IV Experiments; https://arxiv.org/html/2607.24331v1#S4.SS1 — IV-A Experimental Settings | https://arxiv.org/html/2607.24331v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24331 | complete |
| SF-2026-ARXIV-2607-24343 | RP-4b63b957696340cc | standard | arXiv:2607.24343v1 | SRC-ARXIV@arXiv:2607.24343v1 | https://arxiv.org/html/2607.24343v1#Sx5 — Method: Role-Stratified Per-Field CRC; https://arxiv.org/html/2607.24343v1#Sx3 — Problem Setup and Threat Model | https://arxiv.org/html/2607.24343v1#A3 — Appendix C Certifiability and Deployable-Detector Results; https://arxiv.org/html/2607.24343v1#Sx6 — Experiments | https://arxiv.org/html/2607.24343v1#Sx7 — Discussion and Limitations; https://arxiv.org/html/2607.24343v1#A2 — Appendix B The Aggregate-Budget Failure: Full Evidence | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24343 | complete |
| SF-2026-ARXIV-2607-24368 | RP-5a6aa74b7c1aec40 | standard | arXiv:2607.24368v1 | SRC-ARXIV@arXiv:2607.24368v1 | https://arxiv.org/html/2607.24368v1#S12 — 12 Representative System Responses; https://arxiv.org/html/2607.24368v1#S15 — 15 System Hyperparameters | https://arxiv.org/html/2607.24368v1#S10 — 10 Memory-Benchmark Taxonomy; https://arxiv.org/html/2607.24368v1#S14 — 14 Automatic Evaluation Prompts | https://arxiv.org/html/2607.24368v1#S4 — 4 Experiments: Locating the Failure; https://arxiv.org/html/2607.24368v1#S7 — 7 Limitations | Exact v1 links https://github.com/imlrz/InMind, https://abc.xyz/investor/board-and-governance/google-code-of-conduct/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24368 | complete |
| SF-2026-ARXIV-2607-24377 | RP-3615e3765c9cc2cf | deep | arXiv:2607.24377v1 | SRC-ARXIV@arXiv:2607.24377v1 | https://arxiv.org/html/2607.24377v1#S5.SS6 — 5.6 Algorithmic Overhead and Kernel Integration | https://arxiv.org/html/2607.24377v1#S5 — 5 Experiments; https://arxiv.org/html/2607.24377v1#S5.SS1 — 5.1 Experimental Setup | https://arxiv.org/html/2607.24377v1#S3 — 3 Failure Modes of Standard MXFP4 Attention; https://arxiv.org/html/2607.24377v1#S6 — 6 Conclusion | Exact v1 links https://gitcode.com/Ascend/MindIE-SD/tree/master/mindiesd, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24377 | complete |
| SF-2026-ARXIV-2607-24392 | RP-6de4e76cd73e3d3d | standard | arXiv:2607.24392v1 | SRC-ARXIV@arXiv:2607.24392v1 | https://arxiv.org/html/2607.24392v1#S3 — 3 Methodology; https://arxiv.org/html/2607.24392v1#S2.SS3 — 2.3 Threat Model | https://arxiv.org/html/2607.24392v1#S4.SS2 — 4.2 Results; https://arxiv.org/html/2607.24392v1#S5.SS2 — 5.2 Results | https://arxiv.org/html/2607.24392v1#A3 — Appendix C Limitations; https://arxiv.org/html/2607.24392v1#S2.SS3 — 2.3 Threat Model | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24392 | complete |
| SF-2026-ARXIV-2607-24407 | RP-3f9ce9133e2ddc42 | standard | arXiv:2607.24407v1 | SRC-ARXIV@arXiv:2607.24407v1 | https://arxiv.org/html/2607.24407v1#S3 — 3 Methodology | https://arxiv.org/html/2607.24407v1#A1 — Appendix A In-Depth Analysis; https://arxiv.org/html/2607.24407v1#A1.SS2 — A.2 Efficiency Analysis | https://arxiv.org/html/2607.24407v1#S5 — 5 Conclusion | Exact v1 links https://github.com/TG0110/Motto, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24407 | complete |
| SF-2026-ARXIV-2607-24434 | RP-079681b283f46470 | deep | arXiv:2607.24434v1 | SRC-ARXIV@arXiv:2607.24434v1 | https://arxiv.org/html/2607.24434v1#Sx3 — DraftExpert Method | https://arxiv.org/html/2607.24434v1#Sx4 — Experimental Evaluation; https://arxiv.org/html/2607.24434v1#Sx4.SSx5 — Training Objective Ablation | https://arxiv.org/html/2607.24434v1#Sx6 — Conclusion | Exact v1 links https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf, https://github.com/ggerganov/llama.cpp, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24434 | complete |
| SF-2026-ARXIV-2607-24440 | RP-9b390e124cd71bac | standard | arXiv:2607.24440v1 | SRC-ARXIV@arXiv:2607.24440v1 | https://arxiv.org/html/2607.24440v1#S3 — 3 Method; https://arxiv.org/html/2607.24440v1#S3.SS1 — 3.1 Experimental design | https://arxiv.org/html/2607.24440v1#S3.SS1 — 3.1 Experimental design; https://arxiv.org/html/2607.24440v1#S3.SS8 — 3.8 Selective prediction analysis | https://arxiv.org/html/2607.24440v1#S5 — 5 Discussion; https://arxiv.org/html/2607.24440v1#S6 — 6 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24440 | complete |
| SF-2026-ARXIV-2607-24459 | RP-6d1a10f27fb8fbd7 | standard | arXiv:2607.24459v1 | SRC-ARXIV@arXiv:2607.24459v1 | https://arxiv.org/html/2607.24459v1#A1 — Appendix A Additional Method Details; https://arxiv.org/html/2607.24459v1#A2.SS4 — B.4 Runtime Procedure Effects Across Model Groups | https://arxiv.org/html/2607.24459v1#A2 — Appendix B Additional Experiment Diagnostics; https://arxiv.org/html/2607.24459v1#A2.SS6 — B.6 Diagnostic Takeaways from Fine-Grained Results | https://arxiv.org/html/2607.24459v1#S6 — 6 Conclusion and Limitations; https://arxiv.org/html/2607.24459v1#A1.SS2 — A.2 Failure-Mode Induction and Skill-Distillation Prompts | Exact v1 links https://github.com/ScienceOne-AI/SciConsolidate, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24459 | complete |
| SF-2026-ARXIV-2607-24471 | RP-cc4e4a2af4312e47 | standard | arXiv:2607.24471v1 | SRC-ARXIV@arXiv:2607.24471v1 | https://arxiv.org/html/2607.24471v1#S4 — 4 Benchmark and experimental design; https://arxiv.org/html/2607.24471v1#S3 — 3 Grounding latent algorithm routing | https://arxiv.org/html/2607.24471v1#A3 — Appendix C Additional experimental results; https://arxiv.org/html/2607.24471v1#S4 — 4 Benchmark and experimental design | https://arxiv.org/html/2607.24471v1#S7 — 7 Conclusion | Exact v1 links https://github.com/xiangbo05/RouteBench, https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-35/issue-1/Robust-Estimation-of-a-Location-Parameter/10.1214/aoms/1177703732.full, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24471 | complete |
| SF-2026-ARXIV-2607-24481 | RP-210b12ec0a6ddb74 | standard | arXiv:2607.24481v1 | SRC-ARXIV@arXiv:2607.24481v1 | https://arxiv.org/html/2607.24481v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24481v1#S2 — 2 Related Work | https://arxiv.org/html/2607.24481v1#S3.SS2 — 3.2 Running an evaluation; https://arxiv.org/html/2607.24481v1#S4 — 4 The ArmnetBench Benchmark | https://arxiv.org/html/2607.24481v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.24481v1#S7 — 7 Future Work | Exact v1 links https://github.com/TheRobotStudio/SO-ARM100/tree/main/Optional/Overhead_Cam_Mount_Webcam, https://huggingface.co/collections/armnet/armnetbench-v01, https://github.com/huggingface/lerobot; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24481 | complete |
| SF-2026-ARXIV-2607-24484 | RP-6b90b88a40e01168 | standard | arXiv:2607.24484v1 | SRC-ARXIV@arXiv:2607.24484v1 | https://arxiv.org/pdf/2607.24484v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24484v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.24484v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24484v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.24484v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24484v1#page=10 — PDF page 10 | Exact v1 links https://github.com/ioverho/rm-shortcuts; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24484 | complete |
| SF-2026-ARXIV-2607-24485 | RP-63c30de41241bb8d | standard | arXiv:2607.24485v1 | SRC-ARXIV@arXiv:2607.24485v1 | https://arxiv.org/html/2607.24485v1#Sx3.SSx1 — Model Architecture; https://arxiv.org/html/2607.24485v1#Sx3 — The Model | https://arxiv.org/html/2607.24485v1#Sx4 — Experiments; https://arxiv.org/html/2607.24485v1#Sx4.SSx1 — Experimental Setups | https://arxiv.org/html/2607.24485v1#Sx5 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24485 | complete |
| SF-2026-ARXIV-2607-24507 | RP-aa29af42392e1c09 | standard | arXiv:2607.24507v1 | SRC-ARXIV@arXiv:2607.24507v1 | https://arxiv.org/html/2607.24507v1#S3 — 3 Methodology; https://arxiv.org/html/2607.24507v1#S3.SS2 — 3.2 Method | https://arxiv.org/html/2607.24507v1#A3 — Appendix C Additional experimental details; https://arxiv.org/html/2607.24507v1#A3.SS4 — C.4 Downstream Evaluation | https://arxiv.org/html/2607.24507v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24507 | complete |
| SF-2026-ARXIV-2607-24516 | RP-c36aa7e13b48fbfc | standard | arXiv:2607.24516v1 | SRC-ARXIV@arXiv:2607.24516v1 | https://arxiv.org/html/2607.24516v1#S2 — 2 Methodology | https://arxiv.org/html/2607.24516v1#S4 — 4 Experiment Results and Analysis; https://arxiv.org/html/2607.24516v1#A1 — Appendix A Detailed Evaluation Metrics | https://arxiv.org/html/2607.24516v1#S6 — 6 Limitations; https://arxiv.org/html/2607.24516v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24516 | complete |
| SF-2026-ARXIV-2607-24539 | RP-802e53fe1d760412 | standard | arXiv:2607.24539v1 | SRC-ARXIV@arXiv:2607.24539v1 | https://arxiv.org/html/2607.24539v1#S2 — II Methodology; https://arxiv.org/html/2607.24539v1#S2.SS5 — II-E Implementation and Adaptation | https://arxiv.org/html/2607.24539v1#S3.SS1 — III-A Subcase A: Cross-Model Validation and Ablation; https://arxiv.org/html/2607.24539v1#S3 — III Case Study | https://arxiv.org/html/2607.24539v1#S4 — IV Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24539 | complete |
| SF-2026-ARXIV-2607-24555 | RP-0fd91f7d064e5217 | deep | arXiv:2607.24555v1 | SRC-ARXIV@arXiv:2607.24555v1 | https://arxiv.org/html/2607.24555v1#S3.SS1 — C.1 Per-method budget accounting | https://arxiv.org/html/2607.24555v1#S3a — C Extended Results; https://arxiv.org/html/2607.24555v1#S5 — 5 Evaluation: Measuring Every Link | https://arxiv.org/html/2607.24555v1#S7 — 7 Conclusion | Exact v1 links https://github.com/Js-Hwang1/locks.git, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24555 | complete |
| SF-2026-ARXIV-2607-24562 | RP-cf7cd77d7e12d23f | standard | arXiv:2607.24562v1 | SRC-ARXIV@arXiv:2607.24562v1 | https://arxiv.org/html/2607.24562v1#S3 — 3 Method: Hierarchical Group-Conditional CRC; https://arxiv.org/html/2607.24562v1#A2 — Appendix B Extended E5: All Models | https://arxiv.org/html/2607.24562v1#A1 — Appendix A Extended Results: MMLU-Pro; https://arxiv.org/html/2607.24562v1#A4 — Appendix D Ablation: Sensitivity (A3) | https://arxiv.org/html/2607.24562v1#S8 — 8 Discussion; https://arxiv.org/html/2607.24562v1#S8.SS3 — 8.3 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24562 | complete |
| SF-2026-ARXIV-2607-24570 | RP-77374ab40e809f85 | standard | arXiv:2607.24570v1 | SRC-ARXIV@arXiv:2607.24570v1 | https://arxiv.org/html/2607.24570v1#A4 — Appendix D Model Scaling Analysis; https://arxiv.org/html/2607.24570v1#A6 — Appendix F Implementation Details | https://arxiv.org/html/2607.24570v1#A3 — Appendix C Complete Experimental Results; https://arxiv.org/html/2607.24570v1#A4 — Appendix D Model Scaling Analysis | https://arxiv.org/html/2607.24570v1#S6 — 6 Discussion; https://arxiv.org/html/2607.24570v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24570 | complete |
| SF-2026-ARXIV-2607-24582 | RP-9b9f3f15360c14d9 | standard | arXiv:2607.24582v1 | SRC-ARXIV@arXiv:2607.24582v1 | https://arxiv.org/html/2607.24582v1#Sx3 — Method | https://arxiv.org/html/2607.24582v1#Ax4 — D Reflection Depth Analysis; https://arxiv.org/html/2607.24582v1#Sx4 — Experiments | https://arxiv.org/html/2607.24582v1#Sx5 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24582 | complete |
| SF-2026-ARXIV-2607-24585 | RP-a170d03d47feb891 | deep | arXiv:2607.24585v1 | SRC-ARXIV@arXiv:2607.24585v1 | https://arxiv.org/html/2607.24585v1#S2.SS1 — 2.1 German and German-Capable Language Models | https://arxiv.org/html/2607.24585v1#S5 — 5 Post-training Experiments | https://arxiv.org/html/2607.24585v1#S6 — 6 Summary and Conclusion; https://arxiv.org/html/2607.24585v1#Sx1 — Limitations | Exact v1 links https://huggingface.co/collections/fraunhofer-iis/elmod-27b, https://huggingface.co/datasets/codeparrot/github-code-clean, https://github.com/explosion/spaCy/blob/master/spacy/lang/de/stop_words.py; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24585 | complete |
| SF-2026-ARXIV-2607-24586 | RP-6234f9720a20ccf7 | deep | arXiv:2607.24586v1 | SRC-ARXIV@arXiv:2607.24586v1 | https://arxiv.org/html/2607.24586v1#S3 — 3 Methodology; https://arxiv.org/html/2607.24586v1#A2 — Appendix B Algorithmic Details | https://arxiv.org/html/2607.24586v1#S4 — 4 Experimental Evaluation; https://arxiv.org/html/2607.24586v1#S4.SS1 — 4.1 Experimental protocol | https://arxiv.org/html/2607.24586v1#S5 — 5 Discussion, Limitations, and Future Work; https://arxiv.org/html/2607.24586v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24586 | complete |
| SF-2026-ARXIV-2607-24593 | RP-c78114bcd0b39e2a | deep | arXiv:2607.24593v1 | SRC-ARXIV@arXiv:2607.24593v1 | https://arxiv.org/html/2607.24593v1#Sx4 — Method; https://arxiv.org/html/2607.24593v1#A1.SSx5 — E Algorithm | https://arxiv.org/html/2607.24593v1#A1.SSx3 — C Per-layer analysis of query locality in indexer top- selection; https://arxiv.org/html/2607.24593v1#A1.SSx6 — F Full Ablations | https://arxiv.org/html/2607.24593v1#Sx6 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24593 | complete |
| SF-2026-ARXIV-2607-24604 | RP-175977da2f389660 | standard | arXiv:2607.24604v1 | SRC-ARXIV@arXiv:2607.24604v1 | https://arxiv.org/html/2607.24604v1#S2.SS2 — 2.2. Agentic Software Engineering Systems; https://arxiv.org/html/2607.24604v1#S4 — 4. Study Design | https://arxiv.org/html/2607.24604v1#S5 — 5. Results; https://arxiv.org/html/2607.24604v1#S4 — 4. Study Design | https://arxiv.org/html/2607.24604v1#S7 — 7. Discussion; https://arxiv.org/html/2607.24604v1#S8 — 8. Threats to Validity | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24604 | complete |
| SF-2026-ARXIV-2607-24625 | RP-0ad6abcdd87846e7 | standard | arXiv:2607.24625v1 | SRC-ARXIV@arXiv:2607.24625v1 | https://arxiv.org/html/2607.24625v1#S2.SS0.SSS0.Px2 — Semantic, memory, and provenance systems.; https://arxiv.org/html/2607.24625v1#S7.SS0.SSS0.Px7 — Methodological scope. | https://arxiv.org/html/2607.24625v1#S7.SS0.SSS0.Px5 — Results and comparative analysis.; https://arxiv.org/html/2607.24625v1#A2 — Appendix B Benchmark Prompts | https://arxiv.org/html/2607.24625v1#S8 — 8. Limitations and Future Agenda; https://arxiv.org/html/2607.24625v1#S3.SS0.SSS0.Px1 — Threat model. | Exact v1 links https://github.com/NVIDIA/NeMo-Guardrails, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24625 | complete |
| SF-2026-ARXIV-2607-24645 | RP-d7fb2148326bf067 | standard | arXiv:2607.24645v1 | SRC-ARXIV@arXiv:2607.24645v1 | https://arxiv.org/html/2607.24645v1#S4.SS3 — 4.3 Feature Discovery Across SAE Architectures; https://arxiv.org/html/2607.24645v1#A6 — Appendix F Directional Mixtures and Model Selection | https://arxiv.org/html/2607.24645v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.24645v1#S4.SS5 — 4.5 Causal Contribution via Ablation | https://arxiv.org/html/2607.24645v1#S7 — 7 Discussion and Conclusion; https://arxiv.org/html/2607.24645v1#S8 — 8 Limitations and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24645 | complete |
| SF-2026-ARXIV-2607-24647 | RP-fd7c51d3bb311294 | standard | arXiv:2607.24647v1 | SRC-ARXIV@arXiv:2607.24647v1 | https://arxiv.org/html/2607.24647v1#A1 — Appendix A The fluid Search Algorithm | https://arxiv.org/html/2607.24647v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24647v1#S2 — 2 Related work | https://arxiv.org/html/2607.24647v1#S7 — 7 Discussion | Exact v1 links https://github.com/HaiqianYang-MechE/AREK, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24647 | complete |
| SF-2026-ARXIV-2607-24651 | RP-93be061df7051c7d | standard | arXiv:2607.24651v1 | SRC-ARXIV@arXiv:2607.24651v1 | https://arxiv.org/html/2607.24651v1#A10.SS1 — J.1 Coordinate-interface system prompt; https://arxiv.org/html/2607.24651v1#A10.SS2 — J.2 Language-interface system prompt (ours) | https://arxiv.org/html/2607.24651v1#A10.SS3 — J.3 Evaluation judge prompt: answer accuracy; https://arxiv.org/html/2607.24651v1#A10.SS4 — J.4 Evaluation judge prompt: evidence relevance | https://arxiv.org/html/2607.24651v1#S6 — 6 Discussion; https://arxiv.org/html/2607.24651v1#S7 — 7 Conclusion | Exact v1 links https://github.com/hiyouga/EasyR1, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24651 | complete |
| SF-2026-ARXIV-2607-24653 | RP-895678ad2e15c9c6 | deep | arXiv:2607.24653v1 | SRC-ARXIV@arXiv:2607.24653v1 | https://arxiv.org/html/2607.24653v1#S5.SS1 — 5.1 Algorithm-System Co-Design for KDA; https://arxiv.org/html/2607.24653v1#S2 — 2 Model Architecture | https://arxiv.org/html/2607.24653v1#S6 — 6 Evaluations; https://arxiv.org/html/2607.24653v1#S6.SS1 — 6.1 Main Results | https://arxiv.org/html/2607.24653v1#S8 — 8 Conclusion | Exact v1 links https://huggingface.co/moonshotai/Kimi-K3, https://github.com/fla-org/flash-linear-attention/pull/691, https://github.com/MoonshotAI/MoonEP; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24653 | complete |
| SF-2026-ARXIV-2607-24663 | RP-a1186f67b6abf0e5 | standard | arXiv:2607.24663v1 | SRC-ARXIV@arXiv:2607.24663v1 | https://arxiv.org/html/2607.24663v1#S3 — III The APS-RAG platform and system architecture; https://arxiv.org/html/2607.24663v1#S3.SS3 — III.3 APS-RAG architecture overview | https://arxiv.org/html/2607.24663v1#S4 — IV Benchmarks and evaluation methodology; https://arxiv.org/html/2607.24663v1#S4.SS1 — IV.1 Real operations data benchmark | https://arxiv.org/html/2607.24663v1#S5 — V Results and discussion; https://arxiv.org/html/2607.24663v1#S5.SS8 — V.8 Limitations | Exact v1 links https://github.com/rajatsainju2025/aps-rag, https://github.com/pymupdf/pymupdf, https://huggingface.co/vectara/hallucination_evaluation_model; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24663 | complete |
| SF-2026-ARXIV-2607-24665 | RP-9226801615196996 | standard | arXiv:2607.24665v1 | SRC-ARXIV@arXiv:2607.24665v1 | https://arxiv.org/html/2607.24665v1#S3 — III Method; https://arxiv.org/html/2607.24665v1#S2.SS1 — II-A Diffusion Models and Flow Matching | https://arxiv.org/html/2607.24665v1#S4 — IV Experiments; https://arxiv.org/html/2607.24665v1#S4.SS1 — IV-A Experiment Settings | https://arxiv.org/html/2607.24665v1#S6 — VI Discussion and Limitations; https://arxiv.org/html/2607.24665v1#S7 — VII Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24665 | complete |
| SF-2026-ARXIV-2607-24667 | RP-b5d65bad027502d0 | deep | arXiv:2607.24667v1 | SRC-ARXIV@arXiv:2607.24667v1 | https://arxiv.org/html/2607.24667v1#S2.SS0.SSS0.Px5 — Memory in learning systems.; https://arxiv.org/html/2607.24667v1#S3.SS0.SSS0.Px2 — The commit lag is a design axis. | https://arxiv.org/html/2607.24667v1#S2.SS0.SSS0.Px6 — Benchmarks and harnesses.; https://arxiv.org/html/2607.24667v1#S7 — 7 Controlled experiments | https://arxiv.org/html/2607.24667v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.24667v1#S2.SS0.SSS0.Px2 — Learned predictors that decide from a guessed future. | Exact v1 links https://github.com/NVIDIA/kvpress, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24667 | complete |
| SF-2026-ARXIV-2607-24692 | RP-981edd403a423088 | deep | arXiv:2607.24692v1 | SRC-ARXIV@arXiv:2607.24692v1 | https://arxiv.org/html/2607.24692v1#S2 — 2. Two-System Inference Pipelines; https://arxiv.org/html/2607.24692v1#S2.SS2 — 2.2. Architecture and execution semantics | https://arxiv.org/html/2607.24692v1#S4 — 4. Evaluations | https://arxiv.org/html/2607.24692v1#S6 — 6. Discussion and Future Work; https://arxiv.org/html/2607.24692v1#S3.SS1 — 3.1. Threat Model | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24692 | complete |
| SF-2026-ARXIV-2607-24717 | RP-248e0fca334c53d9 | standard | arXiv:2607.24717v1 | SRC-ARXIV@arXiv:2607.24717v1 | https://arxiv.org/html/2607.24717v1#S3 — 3 Methods; https://arxiv.org/html/2607.24717v1#S3.SS2 — 3.2 DataOrchestra Framework | https://arxiv.org/html/2607.24717v1#S5 — 5 Analysis and Ablations; https://arxiv.org/html/2607.24717v1#A4 — Appendix D Details of Evaluation | https://arxiv.org/html/2607.24717v1#S6 — 6 Conclusion | Exact v1 links https://github.com/GAIR-NLP/DataOrchestra, https://huggingface.co/datasets/HuggingFaceTB/cosmopedia, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24717 | complete |
| SF-2026-ARXIV-2607-24720 | RP-0e02f58fbedacb08 | standard | arXiv:2607.24720v1 | SRC-ARXIV@arXiv:2607.24720v1 | https://arxiv.org/html/2607.24720v1#A1.SS1 — A.1 Pre-trained Model Configuration; https://arxiv.org/html/2607.24720v1#S4.SS1 — 4.1 Planning with Internalized World Model | https://arxiv.org/html/2607.24720v1#S3.SS3 — 3.3 Evaluation | https://arxiv.org/html/2607.24720v1#S8 — 8 Conclusion | Exact v1 links https://github.com/Quester-one/PlanPhysCode, https://huggingface.co/MultimodalAgent/TianyiMen_PlanPhys_Models, https://huggingface.co/datasets/MultimodalAgent/TianyiMen_PlanPhys_Datasets; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24720 | complete |
| SF-2026-ARXIV-2607-24731 | RP-dac6ef63dda9479d | standard | arXiv:2607.24731v1 | SRC-ARXIV@arXiv:2607.24731v1 | https://arxiv.org/html/2607.24731v1#S2.SS1 — 2.1 On-Policy Distillation for Diffusion Models; https://arxiv.org/html/2607.24731v1#S5.SS1 — 5.1 Diffusion Model Distillation | https://arxiv.org/html/2607.24731v1#S4 — 4 Experiments; https://arxiv.org/html/2607.24731v1#S4.SS3 — 4.3 Ablation Studies | https://arxiv.org/html/2607.24731v1#S6 — 6 Conclusions and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24731 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-22545:start -->
### Semalith v1.4: A Calibrated 184M Safety Classifier Achieving State-of-the-Art Prompt-Injection Detection at 44x Fewer Parameters than Llama-Guard-3-8B

<!-- claim:SF-2026-ARXIV-2607-22545:start -->Deploying large language models in financial-services and agentic settings requires safety classifiers that simultaneously handle prompt injection, regulatory compliance, and general harm, a combination no existing open guardrail addresses in a single inference pass. Semalith v1.4 is a 184M-parameter DeBERTa-v3-base classifier performing simultaneous three-axis safety classification including prompt injection, general harm, and financial-services regulatory compliance, in a single forward pass. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22545:end -->

**为什么进入候选分母。** 摘要首要问题为“Deploying large language models in financial-services and agentic settings requires safety classifiers that simultaneously handle prompt injection, regulatory compliance, and general harm, a combination no existing open guardrail addresses in a single inference pass.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Semalith v1.4 is a 184M-parameter DeBERTa-v3-base classifier performing simultaneous three-axis safety classification including prompt injection, general harm, and financial-services regulatory compliance, in a single forward pass.

**证据证明什么。** Deployment guidance: v1.3 is recommended for conversational moderation deployments (ToxicChat F1 0.624); v1.4 is recommended when BFSI label coverage or zero-FPR on benign agentic prompts is the priority.

**证据没有证明什么。** 6 Limitations Six measured weak spots are documented for v1.4, in descending order of severity. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22545v1#S3 — 3 Method; https://arxiv.org/html/2607.22545v1#S3.SS1 — 3.1 Architecture。Evaluation：https://arxiv.org/html/2607.22545v1#S4.SS2 — 4.2 Held-out OOD evaluation suite (22 benchmarks); https://arxiv.org/html/2607.22545v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.22545v1#S5 — 5 Discussion; https://arxiv.org/html/2607.22545v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/anonymous/semalith-eval-harness, https://huggingface.co/meta-llama/Llama-Guard-3-8B, https://huggingface.co/meta-llama/Prompt-Guard-2-86M; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：6 Limitations Six measured weak spots are documented for v1.4, in descending order of severity.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22545:end -->

<!-- review:SF-2026-ARXIV-2607-22554:start -->
### Same Question, Different Answers: Evaluating LLM Reliability Beyond Accuracy

<!-- claim:SF-2026-ARXIV-2607-22554:start -->Large language models (LLMs) often achieve strong accuracy on benchmarks, yet it remains unclear how reliably they apply this knowledge when the same question is phrased in different but equivalent ways. In this work, we study how model answers change under meaning-preserving paraphrases across factual question answering and mathematical reasoning tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22554:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) often achieve strong accuracy on benchmarks, yet it remains unclear how reliably they apply this knowledge when the same question is phrased in different but equivalent ways.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this work, we study how model answers change under meaning-preserving paraphrases across factual question answering and mathematical reasoning tasks.

**证据证明什么。** Building on this observation, we show that a simple self-paraphrasing strategy can partially recover this latent knowledge and improve performance at inference time.

**证据没有证明什么。** Finally, our experiments are limited to a finite set of datasets and models, and broader evaluation across additional domains, languages, modalities, and multimodal settings remains an important direction for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22554v1#A5.SS2 — E.2 Multi-Judge Evaluation Framework; https://arxiv.org/html/2607.22554v1#S3 — 3 A Framework for Fine-Grained Evaluation of Consistency and Reliability。Evaluation：https://arxiv.org/html/2607.22554v1#S5.SS1 — 5.1 Implications for Benchmark Design and Evaluation; https://arxiv.org/html/2607.22554v1#A10 — Appendix J Detailed Result Tables and Figures。Limitations / counterevidence：https://arxiv.org/html/2607.22554v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.22554v1#A8 — Appendix H Additional Discussion。

**Artifact boundary。** Exact v1 links https://github.com/kazemf78/llm-consistency-study.git, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Finally, our experiments are limited to a finite set of datasets and models, and broader evaluation across additional domains, languages, modalities, and multimodal settings remains an important direction for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22554:end -->

<!-- review:SF-2026-ARXIV-2607-22556:start -->
### MIITA: Memory-Induced Inference-Time Adaptation for Continual Learning with Small Language Models

<!-- claim:SF-2026-ARXIV-2607-22556:start -->Continual learning (CL) is essential for small language models (SLMs) to adapt to evolving real-world needs in resource-constrained deployments. However, directly updating their limited parameter space causes catastrophic forgetting. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22556:end -->

**为什么进入候选分母。** 摘要首要问题为“Continual learning (CL) is essential for small language models (SLMs) to adapt to evolving real-world needs in resource-constrained deployments.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address these challenges, we propose MIITA, a Memory-Induced Inference-Time Adaptation framework for supervised CL under constrained storage.

**证据证明什么。** Extensive experiments across diverse supervised CL settings show that MIITA consistently improves final performance and mitigates forgetting under fixed memory budgets.

**证据没有证明什么。** Because the backbone remains frozen and adaptation is applied only as a temporary hidden-state perturbation, MIITA cannot recover capabilities that are absent from the base model or fully replace parameter updates when new tasks require substantial new reasoning skills or knowledge that is poorly represented in the existing hidden space. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22556v1#A2 — Appendix B Extended Methodology; https://arxiv.org/html/2607.22556v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.22556v1#A1 — Appendix A Theoretical Analysis; https://arxiv.org/html/2607.22556v1#A3 — Appendix C Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.22556v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.22556v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Because the backbone remains frozen and adaptation is applied only as a temporary hidden-state perturbation, MIITA cannot recover capabilities that are absent from the base model or fully replace parameter updates when new tasks require substantial new reasoning skills or knowledge that is poorly represented in the existing hidden space.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22556:end -->

<!-- review:SF-2026-ARXIV-2607-22561:start -->
### Codifying the Judge: Scalable Evaluation via Program Distillation

<!-- claim:SF-2026-ARXIV-2607-22561:start -->LLM-as-a-judge has become the standard for automated evaluation, but it suffers from high cost, significant latency, and opaque decisions -- limitations that undermine its scalability and reliability. We address these with a simple, efficient alternative: program distillation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22561:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-as-a-judge has become the standard for automated evaluation, but it suffers from high cost, significant latency, and opaque decisions -- limitations that undermine its scalability and reliability.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Building on this notion, we introduce PAJAMA, a system that synthesizes programs as judges, aggregates their decisions into a joint verdict, and incorporates a fallback mechanism to selectively escalate low-confidence cases to an LLM.

**证据证明什么。** When using program outputs as routing signals, PAJAMA improves both accuracy and throughput and advances the Pareto frontier.

**证据没有证明什么。** We discuss two potential limitations in Pajama . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22561v1#S3 — 3 Framework; https://arxiv.org/html/2607.22561v1#S3.SS3 — 3.3 Modeling Programmatic Judges。Evaluation：https://arxiv.org/html/2607.22561v1#A4 — Appendix D Experimental Results; https://arxiv.org/html/2607.22561v1#A1.SS2 — A.2 A Curated Set of Evaluation Rubrics。Limitations / counterevidence：https://arxiv.org/html/2607.22561v1#A5 — Appendix E Discussion; https://arxiv.org/html/2607.22561v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/SprocketLab/PAJAMA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We discuss two potential limitations in Pajama .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22561:end -->

<!-- review:SF-2026-ARXIV-2607-22562:start -->
### SF-AMS: Strategic Forgetting for Structured Memory in LLM Agent

<!-- claim:SF-2026-ARXIV-2607-22562:start -->Managing long-context dependencies remains a primary bottleneck in LLM agents, as redundant and irrelevant information can degrade multi-step reasoning. Strategic Forgetting for Agent Memory Systems (SF-AMS) is proposed as a framework for maintaining compact high-utility memory by modeling the long-term importance of memory units. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22562:end -->

**为什么进入候选分母。** 摘要首要问题为“Managing long-context dependencies remains a primary bottleneck in LLM agents, as redundant and irrelevant information can degrade multi-step reasoning.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Strategic Forgetting for Agent Memory Systems (SF-AMS) is proposed as a framework for maintaining compact high-utility memory by modeling the long-term importance of memory units.

**证据证明什么。** These results show that modeling memory importance as a dynamic utility signal is critical for reliable long-context reasoning.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22562v1#S3.SS1 — 3.1 Framework Philosophy and System Architecture; https://arxiv.org/html/2607.22562v1#S2.SS3 — 2.3 System Level and Dynamic Memory Management Frameworks。Evaluation：https://arxiv.org/html/2607.22562v1#A2 — Appendix B Additional Experiments and Analysis; https://arxiv.org/html/2607.22562v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.22562v1#S5 — 5 Conclusions。

**Artifact boundary。** Exact v1 links https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22562:end -->

<!-- review:SF-2026-ARXIV-2607-22569:start -->
### Execution-Grounded Security Testing for Coding Agents in Software Engineering Pipelines

<!-- claim:SF-2026-ARXIV-2607-22569:start -->Coding agents are increasingly integrated into system operations, where their tool use can directly modify project artifacts, execution environments, and the underlying system. For example, if a coding agent inserts a hook into a system startup or configuration script, that change can persist after the interaction, be triggered later, and abuse delegated user or system privileges to modify the system. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22569:end -->

**为什么进入候选分母。** 摘要首要问题为“Coding agents are increasingly integrated into system operations, where their tool use can directly modify project artifacts, execution environments, and the underlying system.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present an execution-grounded red-team testing framework for probing this execution-layer security boundary using observable sandbox evidence, including tool invocations, runtime traces, and file-system diffs.

**证据证明什么。** These results show that coding agents in system operations remain insecure under task disguise: once risky intent is hidden inside plausible engineering tasks, the agent can be induced to carry out unsafe actions on the surrounding system.

**证据没有证明什么。** When an operation causes only limited or superficial environment-level impact, agents may be less likely to refuse it even under direct prompting, which can affect baseline difficulty and cross-domain comparisons. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22569v1#S4 — 4. Methodology。Evaluation：https://arxiv.org/html/2607.22569v1#S5.SS4 — 5.4. Experimental Results; https://arxiv.org/html/2607.22569v1#S2.SS2 — 2.2. Agent Security Risks and Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.22569v1#S6 — 6. Limitations; https://arxiv.org/html/2607.22569v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://docs.anthropic.com/en/docs/claude-code/overview, https://huggingface.co/deepseek-ai/DeepSeek-V3-Base, https://openai.com/codex; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：When an operation causes only limited or superficial environment-level impact, agents may be less likely to refuse it even under direct prompting, which can affect baseline difficulty and cross-domain comparisons.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22569:end -->

<!-- review:SF-2026-ARXIV-2607-22570:start -->
### Reference Feature Atlases for Mechanistic Auditing of Language Models

<!-- claim:SF-2026-ARXIV-2607-22570:start -->Auditing a new language model usually means relearning and reinterpreting its internal features from scratch. We propose a reference feature atlas: a sparse feature library trained once on a reference panel and reused for new targets, which attach by fitting only a linear decoder. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22570:end -->

**为什么进入候选分母。** 摘要首要问题为“Auditing a new language model usually means relearning and reinterpreting its internal features from scratch.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** The atlas channel reads the target on already interpreted panel features, providing a stable coordinate system across models.

**证据证明什么。** On Qwen-2.5, the same channel additionally reveals a panel-relative political-framing cluster; steering it shifts the audited framing metrics while out-of-domain controls remain unchanged.

**证据没有证明什么。** Limitations The method requires activation access and is most applicable to open-weight or internally accessible models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22570v1#A9 — Appendix I N-way Model Diffing in the Shared Coordinate System; https://arxiv.org/html/2607.22570v1#A2 — Appendix B Implementation Details。Evaluation：https://arxiv.org/html/2607.22570v1#A6 — Appendix F Audit Experiment Hyperparameters and Protocols; https://arxiv.org/html/2607.22570v1#A7 — Appendix G Atlas-Coordinate Refusal Steering: Per-Target Results。Limitations / counterevidence：https://arxiv.org/html/2607.22570v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.22570v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations The method requires activation access and is most applicable to open-weight or internally accessible models.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22570:end -->

<!-- review:SF-2026-ARXIV-2607-22577:start -->
### cMoLLM at Scale: Horizontal Scaling Laws for Mixture-of-LLMs

<!-- claim:SF-2026-ARXIV-2607-22577:start -->Scaling large language models (LLMs) has driven their success, yet dense Transformers couple capacity and computation: every parameter is activated for every token, making training and inference costs grow linearly with model size-a critical bottleneck as models approach trillion-parameter regimes. We aim to scale capacity through MoE-style mixture throughout the LLM pipeline rather than only the FFN. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22577:end -->

**为什么进入候选分母。** 摘要首要问题为“Scaling large language models (LLMs) has driven their success, yet dense Transformers couple capacity and computation: every parameter is activated for every token, making training and inference costs grow linearly with model size-a critical bottleneck as models approach trillion-parameter regimes.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Building on this equivalence, we introduce cMoLLM: a convolutionally gated mixture-of-LLMs that routes over end-to-end streams through fully differentiable dynamic convolution.

**证据证明什么。** In GPT-2-style models trained on FineWeb, cMoLLM improves language modeling perplexity and downstream GLUE and SQuAD accuracy under matched compute, with better stream utilization, more stable optimization, and favorable scaling compared to ParaScale- and AltUp-style baselines.

**证据没有证明什么。** Future work: (i) scale cMoLLM to larger models and distributed training; (ii) extend the MoE–convolution equivalence to attention; (iii) combine with retrieval or other conditional compute mechanisms. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22577v1#S4 — 4 Method: cMoLLM; https://arxiv.org/html/2607.22577v1#S4.SS2 — 4.2 cMoLLM Block Design。Evaluation：https://arxiv.org/html/2607.22577v1#S4.SS7 — 4.7 Computational Complexity Analysis; https://arxiv.org/html/2607.22577v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.22577v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work: (i) scale cMoLLM to larger models and distributed training; (ii) extend the MoE–convolution equivalence to attention; (iii) combine with retrieval or other conditional compute mechanisms.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-COST`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22577:end -->

<!-- review:SF-2026-ARXIV-2607-22578:start -->
### HeraSys: Collaborative Serving of Multiple LLM Workflows via Fine-Grained End-to-End Optimization

<!-- claim:SF-2026-ARXIV-2607-22578:start -->The proliferation of Large Language Models (LLMs) has shifted serving systems from processing isolated requests to orchestrating high-concurrency, multi-tenant agentic workflows. However, existing solutions typically prioritize intra-workflow optimization, largely neglecting the significant potential for inter-workflow optimization. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22578:end -->

**为什么进入候选分母。** 摘要首要问题为“The proliferation of Large Language Models (LLMs) has shifted serving systems from processing isolated requests to orchestrating high-concurrency, multi-tenant agentic workflows.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we propose HeraSys, an LLM serving system designed to optimize the end-to-end performance of concurrent workflows.

**证据证明什么。** Extensive experiments demonstrate that HeraSys reduces P99 latency by up to 2.17$\times$ and increases serving throughput by up to 1.85$\times$ under strict latency guarantees.

**证据没有证明什么。** Dependency on Estimation: The algorithm relies on for SRTF. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22578v1#S3 — 3 Method; https://arxiv.org/html/2607.22578v1#S3.SS2 — 3.2 System Overview。Evaluation：https://arxiv.org/html/2607.22578v1#A2 — Appendix B Theoretical Analysis; https://arxiv.org/html/2607.22578v1#A2.SS3 — B.3 Complexity Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.22578v1#A2.SS4 — B.4 Limitations; https://arxiv.org/html/2607.22578v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/langchain-ai/langchain, https://github.com/pgvector/pgvector, https://github.com/run-llama/llama_index; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Dependency on Estimation: The algorithm relies on for SRTF.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22578:end -->

<!-- review:SF-2026-ARXIV-2607-22584:start -->
### Source-Aware Reranking for Retrieval-Augmented Generation: A Reliability Prior Approach

<!-- claim:SF-2026-ARXIV-2607-22584:start -->Standard Retrieval-Augmented Generation pipelines rank retrieved documents by semantic similarity alone, without accounting for source provenance or credibility. This work evaluates a simple and interpretable modification to RAG retrieval ranking that incorporates domain-informed source reliability priors. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22584:end -->

**为什么进入候选分母。** 摘要首要问题为“Standard Retrieval-Augmented Generation pipelines rank retrieved documents by semantic similarity alone, without accounting for source provenance or credibility.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** The framework is evaluated against a similarity-only baseline on a 120-document health-domain corpus.

**证据证明什么。** In this controlled setting, source-aware reranking improves Precision@5 from 0.48 to 0.72 and reduces average adversarial document retrieval under the evaluated threat model, where low-credibility sources are identifiable via metadata.

**证据没有证明什么。** The method’s limitations—manual priors, oracle feedback, small-scale evaluation, and a specific threat model—are acknowledged explicitly and point to concrete directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22584v1#S3.SS1 — 3.1 System Architecture; https://arxiv.org/html/2607.22584v1#S3 — 3 Implementation。Evaluation：https://arxiv.org/html/2607.22584v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.22584v1#S4 — 4 Experimentation。Limitations / counterevidence：https://arxiv.org/html/2607.22584v1#S7 — 7 Future Work; https://arxiv.org/html/2607.22584v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The method’s limitations—manual priors, oracle feedback, small-scale evaluation, and a specific threat model—are acknowledged explicitly and point to concrete directions for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22584:end -->

<!-- review:SF-2026-ARXIV-2607-22585:start -->
### The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation

<!-- claim:SF-2026-ARXIV-2607-22585:start -->Public leaderboards for coding agents typically rank systems by model name and pass rate, while the surrounding harness (the scaffold that issues tools, manages context, and decides when to stop) is often under-specified. Model-to-model comparison is valid when the harness is fixed; when it varies, performance and efficiency conflate model and scaffold effects. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22585:end -->

**为什么进入候选分母。** 摘要首要问题为“Public leaderboards for coding agents typically rank systems by model name and pass rate, while the surrounding harness (the scaffold that issues tools, manages context, and decides when to stop) is often under-specified.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Public leaderboards for coding agents typically rank systems by model name and pass rate, while the surrounding harness (the scaffold that issues tools, manages context, and decides when to stop) is often under-specified.

**证据证明什么。** We release anonymized configs, raw trial logs, aggregated snapshots, and analysis scripts.

**证据没有证明什么。** Else if hit_turn_budget true MAX_TURNS . ( hit_turn_budget is turns_used max_turns ; only Goose and OpenHands-SDK pass a turn cap to Harbor, so OpenCode never produces this category.) 4. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22585v1#S3.SS2 — 3.2 Models; https://arxiv.org/html/2607.22585v1#S4.SS7 — 4.7 Summary of Harness vs. Model Effects。Evaluation：https://arxiv.org/html/2607.22585v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.22585v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.22585v1#A1 — Appendix A Failure Classification Decision Tree; https://arxiv.org/html/2607.22585v1#A3 — Appendix C Failure Examples (One per Category)。

**Artifact boundary。** Exact v1 links https://github.com/alibaba/terminal-bench-pro, https://github.com/aaif-goose/goose, https://github.com/harbor-framework/harbor; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Else if hit_turn_budget true MAX_TURNS . ( hit_turn_budget is turns_used max_turns ; only Goose and OpenHands-SDK pass a turn cap to Harbor, so OpenCode never produces this category.) 4.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22585:end -->

<!-- review:SF-2026-ARXIV-2607-22586:start -->
### MM-ShiftKV: Decode-Aware Prefill-Stage KV Selection for Multimodal Large Language Models

<!-- claim:SF-2026-ARXIV-2607-22586:start -->Key-Value (KV) caching is essential for efficient inference in multimodal large language models (MLLMs), yet its memory footprint grows linearly with context length and becomes a major bottleneck due to the large number of visual tokens. Recent prefill-stage KV selection methods estimate KV importance from prefilling statistics, implicitly assuming that prefilling-time queries are representative of those encountered during decoding. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22586:end -->

**为什么进入候选分母。** 摘要首要问题为“Key-Value (KV) caching is essential for efficient inference in multimodal large language models (MLLMs), yet its memory footprint grows linearly with context length and becomes a major bottleneck due to the large number of visual tokens.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose MM-ShiftKV, a training-free, decode-aware and strictly prefill-only KV selection method.

**证据证明什么。** Experiments on multimodal benchmarks demonstrate that MM-ShiftKV consistently outperforms existing methods under strict KV-cache budgets.

**证据没有证明什么。** Second, MM-ShiftKV performs KV eviction only in the prefilling phase. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22586v1#S3 — 3 Method; https://arxiv.org/html/2607.22586v1#A2 — Appendix B Implementation Details。Evaluation：https://arxiv.org/html/2607.22586v1#A1 — Appendix A Theoretical Analysis of Prefill–Decode Scale Mismatch; https://arxiv.org/html/2607.22586v1#A3 — Appendix C Additional Visualization Results。Limitations / counterevidence：https://arxiv.org/html/2607.22586v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.22586v1#S8 — 8 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/zjuDBxAI/MM-ShiftKV, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Second, MM-ShiftKV performs KV eviction only in the prefilling phase.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22586:end -->

<!-- review:SF-2026-ARXIV-2607-22595:start -->
### xMIx: High-Performance Serving-Time Platform for Mechanistic Interpretability Apps

<!-- claim:SF-2026-ARXIV-2607-22595:start -->Mechanistic interpretability (MI) has emerged as a powerful approach for analyzing and intervening in inference computations, with a growing number of applications such as jailbreak attempt detection, truthfulness evaluation, and hallucination detection. Unfortunately, MI deployment in production model-serving systems is currently not practical, as most existing MI frameworks introduce prohibitively high runtime overheads. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22595:end -->

**为什么进入候选分母。** 摘要首要问题为“Mechanistic interpretability (MI) has emerged as a powerful approach for analyzing and intervening in inference computations, with a growing number of applications such as jailbreak attempt detection, truthfulness evaluation, and hallucination detection.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Unfortunately, MI deployment in production model-serving systems is currently not practical, as most existing MI frameworks introduce prohibitively high runtime overheads.

**证据证明什么。** We integrate xMIx with the vLLM serving system and evaluate it across three major models and seven diverse MI applications. xMIx achieves performance comparable to native vLLM execution, incurring a slowdown of 1.3% mean inter-token latency (ITL), 1.2% for tail P99 ITL, 2.6% for mean time to first token (TTFT), and 1.6% for mean total token throughput (TTT).

**证据没有证明什么。** As a result, xMIx does not support intra-component or intra-kernel manipulations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22595v1#A2 — Appendix B Cuda graph support on other frameworks; https://arxiv.org/html/2607.22595v1#S4 — 4 Design and Implementation。Evaluation：https://arxiv.org/html/2607.22595v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22595v1#S4.SS4 — 4.4 Current Scope and Limitations; https://arxiv.org/html/2607.22595v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ZJU-REAL/EasySteer-vllm-v1/pull/3, https://github.com/TransformerLensOrg/TransformerLens, https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：As a result, xMIx does not support intra-component or intra-kernel manipulations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-TRACE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22595:end -->

<!-- review:SF-2026-ARXIV-2607-22600:start -->
### Chart Deception in Vision-Language Models: From Vulnerability to Mitigation

<!-- claim:SF-2026-ARXIV-2607-22600:start -->Information visualizations are widely used to communicate patterns, trends, and outliers, yet deceptive design choices-such as truncated or inverted axes, distorted aspect ratios, inappropriate encodings, and misleading color mappings-can systematically alter interpretation while preserving the underlying data. As Vision-Language Models (VLMs) are increasingly used for chart understanding and analytical reasoning, assessing their robustness to such deceptive visualizations has become critical for trustworthy data analysis. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22600:end -->

**为什么进入候选分母。** 摘要首要问题为“Information visualizations are widely used to communicate patterns, trends, and outliers, yet deceptive design choices-such as truncated or inverted axes, distorted aspect ratios, inappropriate encodings, and misleading color mappings-can systematically alter interpretation while preserving the underlying data.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce VisDeception, the first controlled paired benchmark for evaluating the robustness of VLMs to misleading chart designs.

**证据证明什么。** To improve robustness, we further propose an inference-time multi-agent mitigation framework that grounds reasoning in structured chart metadata extracted from the visualization before answer generation, enabling models to reduce the influence of deceptive visual cues without requiring explicit user instructions.

**证据没有证明什么。** These findings indicate that future mitigation strategies should focus not only on reasoning but also on improving the reliability of chart interpretation and structured representation learning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22600v1#S2.SS2 — II-B Misleading Visual Designs; https://arxiv.org/html/2607.22600v1#S3.SS1 — III-A Taxonomy Design。Evaluation：https://arxiv.org/html/2607.22600v1#S5 — V Result Analysis; https://arxiv.org/html/2607.22600v1#S3 — III The VisDeception Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.22600v1#S7 — VII Conclusion and Future Work; https://arxiv.org/html/2607.22600v1#S6 — VI Discussion。

**Artifact boundary。** Exact v1 links https://github.com/vis-nlp/visDeception, https://github.com/highcharts/highcharts, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：These findings indicate that future mitigation strategies should focus not only on reasoning but also on improving the reliability of chart interpretation and structured representation learning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22600:end -->

<!-- review:SF-2026-ARXIV-2607-22610:start -->
### Tokengeist: Multi-Turn Attribution Tracing in Agentic Conversations

<!-- claim:SF-2026-ARXIV-2607-22610:start -->When a language model produces a response in a multi-turn conversation, which tokens from prior turns shaped that answer, and how did those dependencies propagate across prior turns? Existing context attribution methods process the full context in a single pass, recovering surface-level dependencies but missing the layered, non-linear structure of real-world dialogues and multi-step reasoning tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22610:end -->

**为什么进入候选分母。** 摘要首要问题为“When a language model produces a response in a multi-turn conversation, which tokens from prior turns shaped that answer, and how did those dependencies propagate across prior turns?”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We propose Tokengeist, an attribution-method-agnostic and scalable framework that recovers full dependency paths by casting attribution as a recursive traversal of a directed acyclic graph (DAG) over conversation turns.

**证据证明什么。** Our results reveal systematic failure modes of single-pass attribution -- which we term provenance collapse -- and motivate attribution methods that reason recursively across turns.

**证据没有证明什么。** Limitations We outline the main limitations of Tokengeist and MTCABench . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22610v1#S4.SS2 — 4.2 Design choices; https://arxiv.org/html/2607.22610v1#A1.SS1 — A.1 Implementation Details。Evaluation：https://arxiv.org/html/2607.22610v1#A1 — Appendix A Experiment Details; https://arxiv.org/html/2607.22610v1#A1.SS2 — A.2 Additional Model Results。Limitations / counterevidence：https://arxiv.org/html/2607.22610v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.22610v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Limitations We outline the main limitations of Tokengeist and MTCABench .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22610:end -->

<!-- review:SF-2026-ARXIV-2607-22611:start -->
### Decentralized Granular Access Control for Agentic AI Systems in Critical Infrastructure

<!-- claim:SF-2026-ARXIV-2607-22611:start -->The deployment of autonomous AI agents in production infrastructure introduces fundamental security challenges that traditional role-based access control (RBAC) models cannot address. Unlike deterministic automation, AI agents exhibit stochastic behavior, making conventional trust models insufficient for governing their access to critical systems. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22611:end -->

**为什么进入候选分母。** 摘要首要问题为“The deployment of autonomous AI agents in production infrastructure introduces fundamental security challenges that traditional role-based access control (RBAC) models cannot address.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Our framework introduces four key innovations: (1) a compound identity model that binds agent actions to delegated human authority, (2) a hierarchical permission system spanning five granularity levels from global platform access to per-parameter constraints, (3) a decentralized policy ownership model where tool teams independently govern their authorization boundaries, and (4) progressive trust escalation with safety interlocks that prevent autonomous agents from executing high-risk operations.

**证据证明什么。** We ground our design in the OWASP Top 10 for LLM Applications (2025) threat taxonomy and demonstrate how each architectural decision mitigates specific attack vectors.

**证据没有证明什么。** ID Threat Agent Manifestation Mitigation LLM01 Prompt Injection Adversarial data in incident descriptions triggering unauthorized commands Input sanitization, tool-level parameter validation LLM02 Info Disclosure Agent leaking infrastructure topology or credentials Output filtering, compound identity scoping LLM06 Excessive Agency Agent executing writes beyond intended scope Five-layer RBAC, deny-by-default LLM10 Unbounded Consumption Agent entering infinite tool-calling loops Rate limiting, execution quotas, circuit breakers 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22611v1#S3 — III Architecture; https://arxiv.org/html/2607.22611v1#S3.SS1 — III-A Design Principles。Evaluation：https://arxiv.org/html/2607.22611v1#S5 — V Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22611v1#S2 — II Threat Model and Problem Statement; https://arxiv.org/html/2607.22611v1#S2.SS2 — II-B OWASP LLM Application Threats。

**Artifact boundary。** Exact v1 links https://owasp.org/www-project-top-10-for-large-language-model-applications/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：ID Threat Agent Manifestation Mitigation LLM01 Prompt Injection Adversarial data in incident descriptions triggering unauthorized commands Input sanitization, tool-level parameter validation LLM02 Info Disclosure Agent leaking infrastructure topology or credentials Output filtering, compound identity scoping LLM06 Excessive Agency Agent executing writes beyond intended scope Five-layer RBAC, deny-by-default LLM10 Unbounded Consumption Agent entering infinite tool-calling loops Rate limiting, execution quotas, circuit breakers

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22611:end -->

<!-- review:SF-2026-ARXIV-2607-22614:start -->
### DynaResize: Runtime GPU Reallocation for Disaggregated LLM Post-Training

<!-- claim:SF-2026-ARXIV-2607-22614:start -->RL-based LLM post-training increasingly disaggregates Rollout and Training across separate GPU resources, but static GPU partitioning suffers from severe pipeline bubbles under long-tail rollout latency. We present DynaResize, a runtime GPU reallocation system that dynamically switches GPUs between Rollout and Training to balance stage execution times without changing RL semantics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22614:end -->

**为什么进入候选分母。** 摘要首要问题为“RL-based LLM post-training increasingly disaggregates Rollout and Training across separate GPU resources, but static GPU partitioning suffers from severe pipeline bubbles under long-tail rollout latency.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present DynaResize, a runtime GPU reallocation system that dynamically switches GPUs between Rollout and Training to balance stage execution times without changing RL semantics.

**证据证明什么。** Experimental results show that DynaResize can improve end-to-end throughput by 66.5% and reduce total execution time by 33% over the optimal static configuration, while hiding 27% of role-switching overhead.

**证据没有证明什么。** Although pre-warming and on-demand loading only moderately reduce the critical-path resizing latency, this reduction is sufficient to yield substantial end-to-end gains in pipeline-stall-dominated post-training workloads. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22614v1#S3 — 3. DynaResize ’s Design; https://arxiv.org/html/2607.22614v1#S4 — 4. Implementation。Evaluation：https://arxiv.org/html/2607.22614v1#S5 — 5. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22614v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Although pre-warming and on-demand loading only moderately reduce the critical-path resizing latency, this reduction is sufficient to yield substantial end-to-end gains in pipeline-stall-dominated post-training workloads.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22614:end -->

<!-- review:SF-2026-ARXIV-2607-22625:start -->
### TokenMem: Faithful Knowledge Injection for Frozen LLMs

<!-- claim:SF-2026-ARXIV-2607-22625:start -->Retrieval-augmented generation (RAG) enhances large language models (LLMs) with external knowledge, but suffers from knowledge conflicts: when retrieved information contradicts parametric memory, the shared self-attention pathway produces unpredictable outputs. We present TokenMem, a lightweight memory system that injects knowledge into frozen LLMs through a dedicated cross-attention channel, bypassing competition with parametric memory in the residual stream. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22625:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-augmented generation (RAG) enhances large language models (LLMs) with external knowledge, but suffers from knowledge conflicts: when retrieved information contradicts parametric memory, the shared self-attention pathway produces unpredictable outputs.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present TokenMem, a lightweight memory system that injects knowledge into frozen LLMs through a dedicated cross-attention channel, bypassing competition with parametric memory in the residual stream.

**证据证明什么。** Ablation studies show that the two-phase curriculum is critical: removing Phase 2 collapses KC to near-zero.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22625v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.22625v1#A4 — Appendix D Generation Efficiency: CoT Length Analysis; https://arxiv.org/html/2607.22625v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.22625v1#S5 — 5 Discussion; https://arxiv.org/html/2607.22625v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22625:end -->

<!-- review:SF-2026-ARXIV-2607-22629:start -->
### Masked Distillation: Internalizing the Chain-of-Thought in Language Models

<!-- claim:SF-2026-ARXIV-2607-22629:start -->Large Reasoning Models (LRMs) produce long, explicit chains of intermediate steps before generating a final answer at inference time. These intermediate traces dominate latency, memory usage, and serving cost, even though the final answer correctness is not causally related to the trace correctness and the trace length is not a reliable indicator of the problem complexity. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22629:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Reasoning Models (LRMs) produce long, explicit chains of intermediate steps before generating a final answer at inference time.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce \textit{masked distillation}, a knowledge-distillation framework in which a student LLM is trained to predict only the solution tokens conditioned on the question, while a reasoning teacher provides feedback on the student's responses after conditioning on the question and its own CoT trace.

**证据证明什么。** We evaluate the framework through controlled experiments on two reasoning domains: GSM8K (grade-school arithmetic) and Countdown (a number-puzzle search task).

**证据没有证明什么。** Sweeping the suffix-scaffold parameter , our results show that the ability to fully internalize the information present in intermediate tokens is task-dependent: it succeeds on GSM8K, where base student has prior exposure to the domain, but fails on Countdown. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22629v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22629v1#S2 — 2 Background。Evaluation：https://arxiv.org/html/2607.22629v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.22629v1#S5 — 5 Results and Discussion。Limitations / counterevidence：https://arxiv.org/html/2607.22629v1#S5 — 5 Results and Discussion; https://arxiv.org/html/2607.22629v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/math-ai/aime25, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Sweeping the suffix-scaffold parameter , our results show that the ability to fully internalize the information present in intermediate tokens is task-dependent: it succeeds on GSM8K, where base student has prior exposure to the domain, but fails on Countdown.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22629:end -->

<!-- review:SF-2026-ARXIV-2607-22634:start -->
### PRESTO: Prefix-Aligned Tree Drafting for Diffusion Speculative Decoding

<!-- claim:SF-2026-ARXIV-2607-22634:start -->Diffusion Large Language Models (dLLMs) have emerged as a promising alternative to autoregressive (AR) LLMs, generating tokens in parallel. This makes them effective draft models for speculative decoding (SD), producing an entire block of draft tokens in a single forward pass. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22634:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion Large Language Models (dLLMs) have emerged as a promising alternative to autoregressive (AR) LLMs, generating tokens in parallel.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose PRESTO, a principled framework that extends tree-based drafting to diffusion drafters while resolving the fundamental mismatch between diffusion draft confidence and prefix-based AR verification through PREfix-aligned Scoring and priority-based Tree search for diffusion speculative decOding.

**证据证明什么。** Extensive experiments show that PRESTO achieves up to an average of $1.5\times$ end-to-end throughput speedup on the state-of-the-art dedicated diffusion drafter SD and an average of $1.12\times$ on self-speculative diffusion LLMs across diverse benchmarks.

**证据没有证明什么。** Target-model verification dominates the overall decoding cost, while tree-related operations introduce only negligible overhead. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22634v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22634v1#S2 — 2 Preliminaries。Evaluation：https://arxiv.org/html/2607.22634v1#S5.SS2 — 5.2 Experiment Results; https://arxiv.org/html/2607.22634v1#A4 — Appendix D End-to-End Throughput Results for dFlash。Limitations / counterevidence：https://arxiv.org/html/2607.22634v1#S6 — 6 Discussions and Ablations; https://arxiv.org/html/2607.22634v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/tatsu-lab/stanford_alpaca, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Target-model verification dominates the overall decoding cost, while tree-related operations introduce only negligible overhead.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22634:end -->

<!-- review:SF-2026-ARXIV-2607-22643:start -->
### Reason Before You Retrieve: Agentic Planning for Multi-modal RAG

<!-- claim:SF-2026-ARXIV-2607-22643:start -->Multimodal retrieval-augmented generation (mRAG) aims to answer image-text queries with external knowledge, but most existing systems still retrieve directly from raw multimodal input over a flat evidence space. This design often struggles with two key challenges: the retrieval target is under-specified because the question intent must be grounded to the correct visual referent, and the search space is weakly structured, forcing semantically distinct evidence to compete in a single global ranking step. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22643:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal retrieval-augmented generation (mRAG) aims to answer image-text queries with external knowledge, but most existing systems still retrieve directly from raw multimodal input over a flat evidence space.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose MM-R2, a multimodal agentic retrieval framework that reasons before retrieval by explicitly modeling both what to retrieve and where to search.

**证据证明什么。** Experiments on Infoseek and Encyclopedic VQA datasets show that MM-R2 substantially outperforms strong baselines on answer accuracy while also yielding more interpretable and verifiable retrieval trajectories.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22643v1#S3 — 3 MM-R2 Framework。Evaluation：https://arxiv.org/html/2607.22643v1#S6 — 6 Experiments Results; https://arxiv.org/html/2607.22643v1#A6 — Appendix F Two-Axis Evaluation for Agentic RAG。Limitations / counterevidence：https://arxiv.org/html/2607.22643v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/huggingface/trl, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22643:end -->

<!-- review:SF-2026-ARXIV-2607-22648:start -->
### PTStore (Prefix Tensor Store): Distributed Prefix Caching and Replication for High Throughput Inference Serving

<!-- claim:SF-2026-ARXIV-2607-22648:start -->Inspired by the design of client caching in Content Delivery Networks (CDNs), PTStore distributes and replicates popular tensors that form reusable KV cache prefixes, which are the main technique used by state of art approaches to accelerate inferences. This reduces the latency of accessing the KV cache and alleviates load imbalance caused by a disproportionately large number of requests on servers containing popular tensors. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22648:end -->

**为什么进入候选分母。** 摘要首要问题为“Inspired by the design of client caching in Content Delivery Networks (CDNs), PTStore distributes and replicates popular tensors that form reusable KV cache prefixes, which are the main technique used by state of art approaches to accelerate inferences.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** This reduces the latency of accessing the KV cache and alleviates load imbalance caused by a disproportionately large number of requests on servers containing popular tensors.

**证据证明什么。** This reduces the latency of accessing the KV cache and alleviates load imbalance caused by a disproportionately large number of requests on servers containing popular tensors.

**证据没有证明什么。** By addressing the limitations of existing systems that lack support for aggregating distributed memory tiers, PTStore enables the efficient reuse of KV cache prefixes across many GPUs and compute nodes. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22648v1#S4.SS1 — 4.1 Design Principles; https://arxiv.org/html/2607.22648v1#S6.SS1 — 6.1 Methodology。Evaluation：https://arxiv.org/html/2607.22648v1#S6 — 6 Experimental evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22648v1#S7 — 7 Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：By addressing the limitations of existing systems that lack support for aggregating distributed memory tiers, PTStore enables the efficient reuse of KV cache prefixes across many GPUs and compute nodes.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22648:end -->

<!-- review:SF-2026-ARXIV-2607-22651:start -->
### ARdena: Scenario-driven control of real-time LLM agents

<!-- claim:SF-2026-ARXIV-2607-22651:start -->Large language models (LLMs) have enabled increasingly capable conversational agents, but reliably controlling their behavior in real-time interactive environments remains a significant challenge. Existing approaches often rely on model fine-tuning or alignment procedures that are difficult to adapt to changing interaction requirements. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22651:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) have enabled increasingly capable conversational agents, but reliably controlling their behavior in real-time interactive environments remains a significant challenge.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** This paper introduces layered scenario-driven LLM control, a framework that enables runtime behavior control through structured prompting.

**证据证明什么。** The results demonstrate that scenario definitions alone can produce substantially different interaction behaviors while maintaining stable real-time operation, highlighting the effectiveness of scenario-driven prompting for controlling LLM agents.

**证据没有证明什么。** Although no deviations were observed in the evaluated scenarios, prompt-based control cannot guarantee perfect compliance in all situations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22651v1#S3 — 3. System Architecture and Implementation; https://arxiv.org/html/2607.22651v1#S2 — 2. Conceptual framework。Evaluation：https://arxiv.org/html/2607.22651v1#S4 — 4. Technical evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22651v1#S5 — 5. Discussion and Limitations; https://arxiv.org/html/2607.22651v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Although no deviations were observed in the evaluated scenarios, prompt-based control cannot guarantee perfect compliance in all situations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22651:end -->

<!-- review:SF-2026-ARXIV-2607-22661:start -->
### TRE: Training-Free Hallucination Detection for Diffusion Language Models

<!-- claim:SF-2026-ARXIV-2607-22661:start -->Diffusion large language models (D-LLMs) have recently gained increasing attention, yet their reliability is significantly hindered by the hallucination problem. Existing hallucination detection approaches for D-LLMs mainly follow a training-based paradigm, relying on data-driven training to optimize the detector. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22661:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion large language models (D-LLMs) have recently gained increasing attention, yet their reliability is significantly hindered by the hallucination problem.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address these limitations, we propose TRE, a training-free hallucination detection metric for D-LLMs.

**证据证明什么。** Extensive experiments on multiple D-LLMs and QA datasets demonstrate that TRE achieves competitive performance, while enjoying strong generalizability, efficiency, and robustness.

**证据没有证明什么。** This paper releases only an anonymized supplementary code package for the detector and does not release new datasets, model checkpoints, or high-risk generative models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22661v1#A3.SS2 — C.2 Model Backbones; https://arxiv.org/html/2607.22661v1#A3.SS4 — C.4 Implementation Details。Evaluation：https://arxiv.org/html/2607.22661v1#A4 — Appendix D Additional Experimental Results; https://arxiv.org/html/2607.22661v1#S5.SS2 — 5.2 Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.22661v1#A5 — Appendix E Limitations and Broader Impacts; https://arxiv.org/html/2607.22661v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This paper releases only an anonymized supplementary code package for the detector and does not release new datasets, model checkpoints, or high-risk generative models.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22661:end -->

<!-- review:SF-2026-ARXIV-2607-22662:start -->
### CuraWeb: Joint Optimization of Quality, Redundancy, and Diversity for Web-Scale Pretraining Data

<!-- claim:SF-2026-ARXIV-2607-22662:start -->Open-web corpora curated via highly selective filters, such as FineWeb-Edu and DCLM, constitute the core of LLM pretraining data and have significantly advanced LLM performance. However, these pipelines typically rely on singular optimization objectives, which inevitably narrows distributional diversity and marginalizes long-tail knowledge, thereby restricting data coverage and underutilizing the vast potential of the open web. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22662:end -->

**为什么进入候选分母。** 摘要首要问题为“Open-web corpora curated via highly selective filters, such as FineWeb-Edu and DCLM, constitute the core of LLM pretraining data and have significantly advanced LLM performance.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Applying this framework to Common Crawl, we construct CuraWeb, a 2T-token English corpus.

**证据证明什么。** Experimental evaluations at the 3B scale demonstrate that CuraWeb significantly outperforms state-of-the-art baselines, yielding an average performance gain of 1.8\% across a wide range of benchmarks, particularly in knowledge-intensive and reasoning tasks.

**证据没有证明什么。** We hope our dataset and methods can serve as a practical guide for future open-source data curation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22662v1#S3 — 3 The CuraWeb Curation Framework; https://arxiv.org/html/2607.22662v1#S3.SS3 — 3.3 Data Understanding System。Evaluation：https://arxiv.org/html/2607.22662v1#S4 — 4 Experiments; https://arxiv.org/html/2607.22662v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.22662v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：We hope our dataset and methods can serve as a practical guide for future open-source data curation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22662:end -->

<!-- review:SF-2026-ARXIV-2607-22663:start -->
### Beyond Block Boundaries: Multi-Block Editing for Diffusion Large Language Models

<!-- claim:SF-2026-ARXIV-2607-22663:start -->Block diffusion is the dominant approach for scaling discrete diffusion language models (dLLMs), as fixed-size blocks preserve parallel decoding while keeping quadratic attention costs tractable. Yet blockwise generation creates a structural weakness: tokens near a block boundary lack future cross-block context, and errors in finalized blocks become irreversible context for later generation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22663:end -->

**为什么进入候选分母。** 摘要首要问题为“Block diffusion is the dominant approach for scaling discrete diffusion language models (dLLMs), as fixed-size blocks preserve parallel decoding while keeping quadratic attention costs tractable.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose Multi-Block Editing (MBE), which revises decoded tokens using cross-block context.

**证据证明什么。** Training-Free MBE improves or matches standard decoding on every benchmark.

**证据没有证明什么。** 6 Conclusion Block diffusion suffers from the block boundary problem , in which tokens near block ends are generated without access to future cross-block context, and once finalized, their uncertain predictions become irreversible for subsequent generation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22663v1#S3 — 3 Method; https://arxiv.org/html/2607.22663v1#S2.SS1 — 2.1 Discrete diffusion large language models。Evaluation：https://arxiv.org/html/2607.22663v1#S4 — 4 Experiments; https://arxiv.org/html/2607.22663v1#S4.SS1 — 4.1 Experimental Setting。Limitations / counterevidence：https://arxiv.org/html/2607.22663v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：6 Conclusion Block diffusion suffers from the block boundary problem , in which tokens near block ends are generated without access to future cross-block context, and once finalized, their uncertain predictions become irreversible for subsequent generation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22663:end -->

<!-- review:SF-2026-ARXIV-2607-22671:start -->
### AIR-BENCH Live: An Evolving Safety Benchmark for Foundation Models

<!-- claim:SF-2026-ARXIV-2607-22671:start -->Foundation-model safety benchmarks capture the AI risks of their time of publication: as models improve and governments pass new AI-safety legislation, their risk taxonomies become incomprehensive and their attack prompts become ineffective. We present AIR-BENCH Live, a self-evolving successor to AIR-BENCH 2024. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22671:end -->

**为什么进入候选分母。** 摘要首要问题为“Foundation-model safety benchmarks capture the AI risks of their time of publication: as models improve and governments pass new AI-safety legislation, their risk taxonomies become incomprehensive and their attack prompts become ineffective.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present AIR-BENCH Live, a self-evolving successor to AIR-BENCH 2024.

**证据证明什么。** Then, a multi-agent, persona-driven prompt generation algorithm generates realistic, multilingual prompts with minimal human review, leaving room for improvement with modern jail breaking techniques.

**证据没有证明什么。** 4.2 Limitations We presented an evaluation exclusively performed using a GPT-5.4-mini judge. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22671v1#S2 — 2 Methods。Evaluation：https://arxiv.org/html/2607.22671v1#S3.SS3 — 3.3 Cross-Benchmark Evaluation; https://arxiv.org/html/2607.22671v1#S3 — 3 Results。Limitations / counterevidence：https://arxiv.org/html/2607.22671v1#S4 — 4 Discussion; https://arxiv.org/html/2607.22671v1#S4.SS2 — 4.2 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/rnaphade-afk/AIR-BENCH-Auto-Update, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：4.2 Limitations We presented an evaluation exclusively performed using a GPT-5.4-mini judge.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22671:end -->

<!-- review:SF-2026-ARXIV-2607-22676:start -->
### How LLM Task-Adaptation Reshapes Alignment: A Multi-dimensional Study of Behavioral and Representational Drift

<!-- claim:SF-2026-ARXIV-2607-22676:start -->Post-training is a key mechanism for adapting large language models to downstream tasks. While prior work suggests that task adaptation can alter a model's pre-existing alignment, especially its safety behavior, its broader effects across alignment domains remain poorly understood. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22676:end -->

**为什么进入候选分母。** 摘要首要问题为“Post-training is a key mechanism for adapting large language models to downstream tasks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We address this gap through a systematic evaluation of representative task-adaptation methods, including supervised fine-tuning (SFT), KL-regularized SFT, and reinforcement learning with verifiable rewards (RLVR) across 15 alignment aspects spanning six key domains: safety, factuality, stance stability, social harm, controllability, and instructability.

**证据证明什么。** Together, these results show that task adaptation is not merely a capability-improving step, but an alignment intervention in its own right, motivating multi-dimensional alignment evaluation as a standard component of post-training pipelines.

**证据没有证明什么。** We leave the evaluation of other emerging task adaptation methods, along with investigating the potential impact of varying verifier qualities, to future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22676v1#A1 — Appendix A Task-Adaptation Post-Training Methods; https://arxiv.org/html/2607.22676v1#A2 — Appendix B Training Hyperparameters and Implementation Details。Evaluation：https://arxiv.org/html/2607.22676v1#A3 — Appendix C Evaluation Details; https://arxiv.org/html/2607.22676v1#A3.SS2 — C.2 Behavioral Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.22676v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.22676v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We leave the evaluation of other emerging task adaptation methods, along with investigating the potential impact of varying verifier qualities, to future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22676:end -->

<!-- review:SF-2026-ARXIV-2607-22688:start -->
### Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents

<!-- claim:SF-2026-ARXIV-2607-22688:start -->Post-training agents for automated AI research requires optimizing not only model parameters, but also the runtime harness that shapes how research trajectories are generated, evaluated, and learned from. Existing pipelines typically train models under a fixed harness, including prompts, tools, skills, middleware, and memory, while leaving the data-generating process outside the optimization objective. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22688:end -->

**为什么进入候选分母。** 摘要首要问题为“Post-training agents for automated AI research requires optimizing not only model parameters, but also the runtime harness that shapes how research trajectories are generated, evaluated, and learned from.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce Co-Harness, a framework that jointly optimizes the agent harness and model parameters during post-training.

**证据证明什么。** These results suggest that joint harness and model optimization is an effective way to improve agents beyond fixed-harness post-training.

**证据没有证明什么。** HarnessCritic: Evolving the Harness from Failure Trajectories HarnessCritic, denoted , converts raw failed trajectories into structured evidence for Harness repair. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22688v1#S3 — Method; https://arxiv.org/html/2607.22688v1#S3.SS2 — Dual-Loop Co-Evolution Architecture。Evaluation：https://arxiv.org/html/2607.22688v1#A6 — Appendix F Extended Analysis; https://arxiv.org/html/2607.22688v1#A7 — Appendix G Co-Evolution Trajectory Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.22688v1#S3.SS3 — HarnessCritic: Evolving the Harness from Failure Trajectories; https://arxiv.org/html/2607.22688v1#S5 — Analysis and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：HarnessCritic: Evolving the Harness from Failure Trajectories HarnessCritic, denoted , converts raw failed trajectories into structured evidence for Harness repair.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22688:end -->

<!-- review:SF-2026-ARXIV-2607-22689:start -->
### Beyond Sequential Interaction: Benchmarking Parallel Execution and Coordination for GUI Agents

<!-- claim:SF-2026-ARXIV-2607-22689:start -->Graphical user interface (GUI) agents are systems powered by large multimodal models (LMMs). They perceive screen state and execute user instructions through GUI actions such as clicking, typing, and scrolling on desktops and mobile devices. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22689:end -->

**为什么进入候选分母。** 摘要首要问题为“Graphical user interface (GUI) agents are systems powered by large multimodal models (LMMs).”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Graphical user interface (GUI) agents are systems powered by large multimodal models (LMMs).

**证据证明什么。** These results show that parallel execution can improve both success rate and efficiency on decomposable, long-horizon GUI tasks, pointing to a direction worth further study.

**证据没有证明什么。** Two opposing mechanisms are visible. (i) Extra parallel branches incur additional dispatch errors that cost the three -only tasks: the planner has to split a coherent trajectory across workers, and any single dispatch boundary error fails the whole task. (ii) The same parallelism unlocks decompositions that a single worker cannot complete within the 25-step per-invocation cap: an under-budgeted serial trajectory simply runs out of room. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22689v1#S3.SS3 — III-C Evaluation System。Evaluation：https://arxiv.org/html/2607.22689v1#A1 — Appendix A Extended Experimental Analysis; https://arxiv.org/html/2607.22689v1#S5 — V Experiments and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.22689v1#A1.SS2 — A-B Extended Ablation Discussion; https://arxiv.org/html/2607.22689v1#S5.SS4 — V-D RQ3: Failure Modes。

**Artifact boundary。** Exact v1 links https://github.com/pkgunboat/ParaGUIBench, https://huggingface.co/Hcompany/Holo3-35B-A3B, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Two opposing mechanisms are visible. (i) Extra parallel branches incur additional dispatch errors that cost the three -only tasks: the planner has to split a coherent trajectory across workers, and any single dispatch boundary error fails the whole task. (ii) The same parallelism unlocks decompositions that a single worker cannot complete within the 25-step per-invocation cap: an under-budgeted serial trajectory simply runs out of room.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22689:end -->

<!-- review:SF-2026-ARXIV-2607-22690:start -->
### LazyMem: Retrieve Broadly, Construct Selectively for Efficient Long-Term Agent Memory

<!-- claim:SF-2026-ARXIV-2607-22690:start -->Long-term memory enables LLM agents to leverage past interactions, but dialogue histories quickly exceed the context window, forcing agents to retrieve relevant subsets at query time. Because useful evidence is sparse and scattered across verbose conversations, retrieval faces a fundamental tension: broadening recall improves coverage but floods downstream reasoning with noise, while compressing memories at write time eases retrieval but irreversibly discards details that future queries may need. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22690:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-term memory enables LLM agents to leverage past interactions, but dialogue histories quickly exceed the context window, forcing agents to retrieve relevant subsets at query time.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce LazyMem, which resolves this tension by deferring all memory construction to query time.

**证据证明什么。** On LongMemEval, LazyMem-4B achieves an LLM-judge accuracy of 0.85, outperforming the strongest non-oracle baseline while using only 213 answer-context memory tokens, 21.0 times fewer than the baseline.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22690v1#S3 — 3 Method; https://arxiv.org/html/2607.22690v1#A2 — Appendix B Effect of Retrieval Depth and Model Scale in Nano Memory。Evaluation：https://arxiv.org/html/2607.22690v1#A3 — Appendix C Efficiency and Ablation: Details and Additional Results; https://arxiv.org/html/2607.22690v1#A6.SS3 — F.3 Human Evaluation and Judge Noise Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.22690v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/allacnobug/LazyMem, https://github.com/dorianbrown/rank_bm25, https://huggingface.co/BAAI/bge-reranker-v2-m3; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22690:end -->

<!-- review:SF-2026-ARXIV-2607-22695:start -->
### PANOPTICON: A PII-Based Assemblage of Naturalistic Output Tokens for Investigating Privacy Leakage Within LLM Context Window

<!-- claim:SF-2026-ARXIV-2607-22695:start -->Large Language Models (LLMs) are capable of generalizing human language for the completion of never-before-seen tasks, leading to widespread deployment. While this automation provides clear utility, completing these tasks often requires the insertion of Personally Identifiable Information (PII), strings of information that uniquely identify some individual, raising privacy concerns. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22695:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) are capable of generalizing human language for the completion of never-before-seen tasks, leading to widespread deployment.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Thus, we introduce the PANOPTICON pipeline and dataset.

**证据证明什么。** Finally, we present a case study showcasing the utility of PANOPTICON data for understanding Prompt Inversion Attacks (PIAs).

**证据没有证明什么。** While this proxy does not reproduce state-of-the-art white-box inversion performance, it provides a consistent, repeatable leakage measurement framework that can be applied across PANOPTICON slices and future model targets. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22695v1#A1 — Appendix A System Prompt Construction Process; https://arxiv.org/html/2607.22695v1#S3 — III PANOPTICON: Methodology & Evaluation。Evaluation：https://arxiv.org/html/2607.22695v1#S4 — IV Experimental Case Study and Results; https://arxiv.org/html/2607.22695v1#S4.SS3 — IV-C Experiment Results。Limitations / counterevidence：https://arxiv.org/html/2607.22695v1#S5 — V Discussion and Limitation; https://arxiv.org/html/2607.22695v1#S6 — VI Conclusion and Future Directions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：While this proxy does not reproduce state-of-the-art white-box inversion performance, it provides a consistent, repeatable leakage measurement framework that can be applied across PANOPTICON slices and future model targets.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22695:end -->

<!-- review:SF-2026-ARXIV-2607-22697:start -->
### Test-Time Coverage: Test-Conditioned Data Curation for Deployment-Aware Learning

<!-- claim:SF-2026-ARXIV-2607-22697:start -->Deployed AI systems are often trained from broad candidate data pools, necessitating data curation towards the deployment test distribution. However, standard data curation methods score training-side criteria rather than directly optimizing deployment match. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22697:end -->

**为什么进入候选分母。** 摘要首要问题为“Deployed AI systems are often trained from broad candidate data pools, necessitating data curation towards the deployment test distribution.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce TTCov (Test-Time Coverage), a data-level test-conditioned curation method that uses test-side information before training instead of updating model weights at inference.

**证据证明什么。** We apply TTCov towards autonomous driving (AD), keeping adaptation off the inference path while selecting data with greater deployment-relevant coverage, closer K-Atlas matching, and stronger downstream end-to-end driving performance than data-curation baselines, including seamless adaptability to novel domains via city-to-city expansion.

**证据没有证明什么。** Thus, TTCov cannot capture information for extremely rare cases that do not exist in the test set nor in open-world knowledge. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22697v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22697v1#S2 — 2 Related Works。Evaluation：https://arxiv.org/html/2607.22697v1#A2 — Appendix B Atlas Ablations; https://arxiv.org/html/2607.22697v1#A2.SS4 — B.4 Additional coverage analysis。Limitations / counterevidence：https://arxiv.org/html/2607.22697v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.22697v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/OpenDriveLab/OpenScene, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Thus, TTCov cannot capture information for extremely rare cases that do not exist in the test set nor in open-world knowledge.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22697:end -->

<!-- review:SF-2026-ARXIV-2607-22708:start -->
### StepX-Edge: An On-Device UI Vision-Language Model via Architecture-Training-Deployment Co-Design

<!-- claim:SF-2026-ARXIV-2607-22708:start -->Deploying a vision-language model with full UI understanding on end devices has long been trapped between accuracy and efficiency: on one side is the accuracy bar for OCR, screen understanding, visual question answering, and element grounding; on the other is the strict compute, memory, and power budget of mobile chips. Existing work either trades one for the other, or stops at simulation without real-device validation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22708:end -->

**为什么进入候选分母。** 摘要首要问题为“Deploying a vision-language model with full UI understanding on end devices has long been trapped between accuracy and efficiency: on one side is the accuracy bar for OCR, screen understanding, visual question answering, and element grounding; on the other is the strict compute, memory, and power budget of mobile chips.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present StepX-Edge, a 0.9B-parameter on-device UI vision-language model that resolves this tension through three-layer co-design of architecture, training, and deployment.

**证据证明什么。** StepX-Edge achieves the strongest overall UI understanding among &lt;=1B models, surpassing all 2B-2.3B baselines on ScreenQA (88.76 F1) and Chinese OCRBench v2 (57.25), and matching 1.3B-2.3B general VLMs on RefCOCO (92.0%) and OCRBench v1 (831) with far fewer parameters.

**证据没有证明什么。** Experimental results show that, with only 0.9B parameters, StepX-Edge achieves the strongest overall UI-understanding performance in the 1B tier: it attains the highest scores among all baselines (including larger 2B–2.3B models) on ScreenQA and Chinese OCRBench v2, and matches 1.3B–2.3B general-purpose VLMs on benchmarks such as RefCOCO and OCRBench v1 with a smaller parameter count. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22708v1#S2 — 2 StepX-Edge: Method Overview; https://arxiv.org/html/2607.22708v1#S2.SS1 — 2.1 Model Architecture。Evaluation：https://arxiv.org/html/2607.22708v1#S3 — 3 Experiments and Evaluation; https://arxiv.org/html/2607.22708v1#S3.SS1 — 3.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.22708v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/pixparse/idl-wds, https://huggingface.co/datasets/agentsea/wave-ui-25k, https://github.com/mobile-viz/MobileViews; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Experimental results show that, with only 0.9B parameters, StepX-Edge achieves the strongest overall UI-understanding performance in the 1B tier: it attains the highest scores among all baselines (including larger 2B–2.3B models) on ScreenQA and Chinese OCRBench v2, and matches 1.3B–2.3B general-purpose VLMs on benchmarks such as RefCOCO and OCRBench v1 with a smaller parameter count.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22708:end -->

<!-- review:SF-2026-ARXIV-2607-22711:start -->
### CORVUS: Context Optimization and Reduction Via Underlying Synchronization for LLM Coding Agents

<!-- claim:SF-2026-ARXIV-2607-22711:start -->LLM coding agents operate by constructing trajectories that accumulate reasoning, tool calls, and results to enable multi-step decision-making. However, the conventional append-only trajectory architecture found in practice tightly couples file-read actions with their observations, capturing snapshots that become permanently fixed in the chronological history. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22711:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM coding agents operate by constructing trajectories that accumulate reasoning, tool calls, and results to enable multi-step decision-making.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To mitigate this, we propose CORVUS, a novel trajectory architecture that decouples file-read actions from their observations by maintaining a synchronized registry of relevant files and injecting only their current contents at each reasoning cycle.

**证据证明什么。** LLM coding agents operate by constructing trajectories that accumulate reasoning, tool calls, and results to enable multi-step decision-making.

**证据没有证明什么。** However, synced context may change across cycles, and long-running operations such as tests or builds may exceed cache TTLs, limiting cache reuse for dynamic prompt components [ 33 ] . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22711v1#S5 — 5 Implementation。Evaluation：https://arxiv.org/html/2607.22711v1#A1 — Appendix A Experiments Compute Resources; https://arxiv.org/html/2607.22711v1#A2 — Appendix B Task-Type Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.22711v1#S7 — 7 Discussion; https://arxiv.org/html/2607.22711v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://claude.com/product/claude-code, https://huggingface.co/datasets/AmazonScience/SWE-PolyBench_Verified, https://qwenlm.github.io/blog/qwen3-coder/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：However, synced context may change across cycles, and long-running operations such as tests or builds may exceed cache TTLs, limiting cache reuse for dynamic prompt components [ 33 ] .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22711:end -->

<!-- review:SF-2026-ARXIV-2607-22716:start -->
### Visual Token Compression Enhances Robustness of MLLMs

<!-- claim:SF-2026-ARXIV-2607-22716:start -->In this paper, we show for the first time that visual token pruning enhances the robustness of Multimodal Large Language Models (MLLMs), mitigating vulnerabilities such as jailbreak attacks and hallucinations. Given that vision and language modalities cannot be perfectly aligned, the misaligned visual tokens might act as out-of-distribution (OOD) inputs, leading to unpredictable outputs and introducing potential vulnerabilities. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22716:end -->

**为什么进入候选分母。** 摘要首要问题为“In this paper, we show for the first time that visual token pruning enhances the robustness of Multimodal Large Language Models (MLLMs), mitigating vulnerabilities such as jailbreak attacks and hallucinations.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To demonstrate the effectiveness of our method, we evaluate it on seven diverse popular benchmarks.

**证据证明什么。** Notably, our method yields an average improvement of 13.29\% in defending jailbreak attacks, consistently achieves competitive performance in mitigating hallucinations, and maintains strong results on general datasets like MME.

**证据没有证明什么。** Considering that vision and language modalities cannot always be perfectly aligned, the misaligned visual tokens would serve as out-of-distribution (OOD) inputs and thus lead to uncertainty in model responses, resulting in high risks to vulnerabilities, like jailbreaks and hallucinations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22716v1#A1.SS5 — A.5. Robust-Pruning Layers with FastV Method; https://arxiv.org/html/2607.22716v1#A2.SS2 — B.2. Cross-Architecture Generalization with a Fixed Pruning Layer。Evaluation：https://arxiv.org/html/2607.22716v1#A1 — Appendix A Supplementary Experimental Details; https://arxiv.org/html/2607.22716v1#A1.SS2 — A.2. Evaluation Protocol and Metric Reliability。Limitations / counterevidence：https://arxiv.org/html/2607.22716v1#S4.SS3 — 4.3. Performance on General Datasets and Efficiency Discussion; https://arxiv.org/html/2607.22716v1#S5 — 5. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Eurek001/OOD-VTP, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Considering that vision and language modalities cannot always be perfectly aligned, the misaligned visual tokens would serve as out-of-distribution (OOD) inputs and thus lead to uncertainty in model responses, resulting in high risks to vulnerabilities, like jailbreaks and hallucinations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22716:end -->

<!-- review:SF-2026-ARXIV-2607-22724:start -->
### Progress-conditioned Group Policy Optimization for Long-Horizon Agentic Tasks

<!-- claim:SF-2026-ARXIV-2607-22724:start -->Group-based policy optimization has been increasingly used to train large language model (LLM) agents from sparse outcome rewards by comparing trajectories or steps within a group. However, on difficult long-horizon tasks, this comparison can suffer from a sampling imbalance: repeated or low-effect actions dominate the high-probability region of the policy while useful state-changing actions remain under-sampled. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22724:end -->

**为什么进入候选分母。** 摘要首要问题为“Group-based policy optimization has been increasingly used to train large language model (LLM) agents from sparse outcome rewards by comparing trajectories or steps within a group.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To break this loop, we propose Progress-conditioned Group Policy Optimization (ProGPO), which uses first-visit observation coverage only when all samples in a group receive zero outcome reward.

**证据证明什么。** Experiments on two challenging agentic benchmarks, ALFWorld and WebShop with Qwen2.5-1.5/7B-Instruct, show that ProGPO consistently improves over group-based baselines, with particularly large gains on hard tasks.

**证据没有证明什么。** When every trajectory in a rollout group shares the same failure outcome, the group-relative advantage collapses to zero and the sampling imbalance that produced the group cannot be corrected. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22724v1#S13 — 13 Use of Large Language Models; https://arxiv.org/html/2607.22724v1#S8 — 8 Implementation Details。Evaluation：https://arxiv.org/html/2607.22724v1#S10 — 10 Additional Results; https://arxiv.org/html/2607.22724v1#S10.SS2 — 10.2 Per-Category Breakdown of Signal-Analysis Variants。Limitations / counterevidence：https://arxiv.org/html/2607.22724v1#S12 — 12 Limitations and Broader Impact; https://arxiv.org/html/2607.22724v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：When every trajectory in a rollout group shares the same failure outcome, the group-relative advantage collapses to zero and the sampling imbalance that produced the group cannot be corrected.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22724:end -->

<!-- review:SF-2026-ARXIV-2607-22726:start -->
### PCA: Persistence-Aware Compression and Aggregation for Fast Video Large Language Models

<!-- claim:SF-2026-ARXIV-2607-22726:start -->Despite advances in Video Large Language Models (VLLMs) that have displayed promising outcomes in video understanding, the redundancy in the long-duration frames remains a hindrance to efficient reasoning. This paper introduces a training-free $\mathbf{P}$ersistence-Aware $\mathbf{C}$ompression and $\mathbf{A}$ggregation (PCA) method designed to preserve high-fidelity raw visual information before the encoding stage. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22726:end -->

**为什么进入候选分母。** 摘要首要问题为“Despite advances in Video Large Language Models (VLLMs) that have displayed promising outcomes in video understanding, the redundancy in the long-duration frames remains a hindrance to efficient reasoning.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** This paper introduces a training-free $\mathbf{P}$ersistence-Aware $\mathbf{C}$ompression and $\mathbf{A}$ggregation (PCA) method designed to preserve high-fidelity raw visual information before the encoding stage.

**证据证明什么。** Extensive experiments demonstrate that PCA consistently outperforms existing state-of-the-art approaches in both efficiency and accuracy, achieving a speedup of 1.8$\times$ to 2.5$\times$ compared to the baseline VLLM.

**证据没有证明什么。** In future work, we will explore persistence-aware motion enhancement during training and study how it interacts with learned temporal representations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22726v1#S3 — 3. Method; https://arxiv.org/html/2607.22726v1#S3.SS2 — 3.2. Framework Overview。Evaluation：https://arxiv.org/html/2607.22726v1#S4 — 4. Experiments; https://arxiv.org/html/2607.22726v1#S4.SS4 — 4.4. Results。Limitations / counterevidence：https://arxiv.org/html/2607.22726v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Heisenberg10110/PCA, https://doi.org/10.18653/v1/2023.emnlp-demo.49, https://dx.doi.org/10.18653/V1/2023.EMNLP-DEMO.49; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：In future work, we will explore persistence-aware motion enhancement during training and study how it interacts with learned temporal representations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22726:end -->

<!-- review:SF-2026-ARXIV-2607-22758:start -->
### Spectral Dynamics of Semantic Drift in Clinical Multi-Agent Language Model Networks

<!-- claim:SF-2026-ARXIV-2607-22758:start -->The integration of iterative LLMs within multi-agent diagnostic frameworks requires a rigorous quantitative reevaluation of underlying communication topologies. Frequently used architectural paradigms depend on scale-free or small-world networks, assuming optimal communication efficiency. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22758:end -->

**为什么进入候选分母。** 摘要首要问题为“The integration of iterative LLMs within multi-agent diagnostic frameworks requires a rigorous quantitative reevaluation of underlying communication topologies.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Instead of reducing errors, hub-centric systems autonomously compound localized hallucinations.

**证据证明什么。** Securing the reliability of autonomous medical diagnostics necessitates treating topological stability as a non-negotiable quantitative imperative.

**证据没有证明什么。** Future work will extend this framework to directionally constrained covariance matrices. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22758v1#S2.SS1 — 2.1 Multi-Agent LLM Frameworks in Clinical NLP; https://arxiv.org/html/2607.22758v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.22758v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.22758v1#S4.SS3 — 4.3 Simulation Horizons and Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.22758v1#S6 — 6 Discussion; https://arxiv.org/html/2607.22758v1#S6.SS4 — 6.4 Limitations and Computational Overhead。

**Artifact boundary。** Exact v1 links https://github.com/amribanerjee/spectral-semantic-cascade, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work will extend this framework to directionally constrained covariance matrices.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22758:end -->

<!-- review:SF-2026-ARXIV-2607-22766:start -->
### Beyond Shapley: An Influence-Based Data Auditing Pipeline for LLM Alignment and Evaluation

<!-- claim:SF-2026-ARXIV-2607-22766:start -->The alignment of Large Language Models (LLMs) is increasingly bottlenecked by data quality. As datasets scale, massive preference and instruction-tuning corpora inevitably accumulate hidden structural contradictions, safety risks, and systemic human annotation errors. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22766:end -->

**为什么进入候选分母。** 摘要首要问题为“The alignment of Large Language Models (LLMs) is increasingly bottlenecked by data quality.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** To address this, we introduce a scalable, inference-only data valuation pipeline that approximates the Shapley value without iterative model retraining.

**证据证明什么。** We demonstrate the pipeline's efficacy in sanitizing two heavily vetted alignment datasets.

**证据没有证明什么。** 5 Conclusion and Limitations This work presents an inference-only data valuation pipeline that approximates Data Shapley for LLMs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22766v1#S3 — 3 Methodology; https://arxiv.org/html/2607.22766v1#A3 — Appendix C Ablation of Pipeline Models。Evaluation：https://arxiv.org/html/2607.22766v1#A3 — Appendix C Ablation of Pipeline Models; https://arxiv.org/html/2607.22766v1#A4 — Appendix D Hyperparameter Sensitivity Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.22766v1#S5 — 5 Conclusion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：5 Conclusion and Limitations This work presents an inference-only data valuation pipeline that approximates Data Shapley for LLMs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22766:end -->

<!-- review:SF-2026-ARXIV-2607-22769:start -->
### DomainPilot: Domain-Level Loss-Guided Two-Stage Data Mixture Optimization for Efficient Language Model Fine-Tuning

<!-- claim:SF-2026-ARXIV-2607-22769:start -->The training efficacy of large language models (LLMs) is fundamentally constrained by the quality and composition of training data. Existing dynamic data scheduling methods face critical limitations in industrial-scale pretraining and supervised fine-tuning (SFT): data selection incurs prohibitive O(N) costs on terabyte-scale corpora, mixture optimization schemes introduce severe I/O bottlenecks or require training auxiliary reference models, and sample-level reweighting strategies rely on loss signals that conflate noise, difficulty, and novelty. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22769:end -->

**为什么进入候选分母。** 摘要首要问题为“The training efficacy of large language models (LLMs) is fundamentally constrained by the quality and composition of training data.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present DomainPilot, a domain-level loss-guided two-stage data mixture optimization framework.

**证据证明什么。** These results demonstrate that domain-level training signals provide an effective, lightweight alternative to expensive data selection or auxiliary model training for mixture optimization.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22769v1#S2.SS4 — 2.4 Framework Portability; https://arxiv.org/html/2607.22769v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.22769v1#S4.SS3 — 4.3 Evaluation Benchmarks; https://arxiv.org/html/2607.22769v1#S4 — 4 Experiment。Limitations / counterevidence：https://arxiv.org/html/2607.22769v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22769:end -->

<!-- review:SF-2026-ARXIV-2607-22781:start -->
### What Softmax Throws Away: Mass-Aware Attention for Evidence Accumulation

<!-- claim:SF-2026-ARXIV-2607-22781:start -->High task performance does not show whether a model retains prediction-relevant structural information in its internal representation. Temporal graph models, for example, can achieve high future-link AUC while basic graph statistics remain difficult to recover from the same representation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22781:end -->

**为什么进入候选分母。** 摘要首要问题为“High task performance does not show whether a model retains prediction-relevant structural information in its internal representation.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose Mass-Aware Attention (MAA), which generalizes standard L1 normalization to an Lp family.

**证据证明什么。** Across four continuous-time dynamic graph models and three datasets, MAA improves future-link AUC in 11 of 12 model-dataset cells.

**证据没有证明什么。** Future-link AUC also increases in 11 of 12 cells. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22781v1#S3.SS3 — III-C Implementation。Evaluation：https://arxiv.org/html/2607.22781v1#S4 — IV Evaluation Principles and Protocol; https://arxiv.org/html/2607.22781v1#S4.SS2 — IV-B Separating Power Selection from Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22781v1#S7.SS5 — VII-E Limitations; https://arxiv.org/html/2607.22781v1#S8 — VIII Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/easytpp/stackoverflow, https://huggingface.co/datasets/easytpp/retweet, https://github.com/ss15859/EarthquakeNPP; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future-link AUC also increases in 11 of 12 cells.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-SELF-ATTENTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22781:end -->

<!-- review:SF-2026-ARXIV-2607-22785:start -->
### FusionML: Prefill, Not Decode - Mechanism and Boundaries of CPU+GPU Co-Execution on Unified-Memory Apple Silicon

<!-- claim:SF-2026-ARXIV-2607-22785:start -->Apple-Silicon SoCs share CPU, GPU, and Neural Engine over one unified memory system, raising the question of whether transformer inference can be accelerated by splitting single operators across units. Prior attempts, including our own, failed or produced precision-confounded wins. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22785:end -->

**为什么进入候选分母。** 摘要首要问题为“Apple-Silicon SoCs share CPU, GPU, and Neural Engine over one unified memory system, raising the question of whether transformer inference can be accelerated by splitting single operators across units.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Apple-Silicon SoCs share CPU, GPU, and Neural Engine over one unified memory system, raising the question of whether transformer inference can be accelerated by splitting single operators across units.

**证据证明什么。** Code, raw results, and generation transcripts are released.

**证据没有证明什么。** 7 Limitations Our transformer measurements use decoder-block geometries with synthetic weights for controlled experiments (latency is weight-value-independent; correctness is separately verified) and one real 7B checkpoint end-to-end; broader model coverage (MoE, multimodal) is future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22785v1#S4 — 4 FusionML Design; https://arxiv.org/html/2607.22785v1#S5.SS3 — 5.3 Full Model Depth。Evaluation：https://arxiv.org/html/2607.22785v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22785v1#S7 — 7 Limitations; https://arxiv.org/html/2607.22785v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ommo007/FusionML, https://github.com/ml-explore/mlx, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：7 Limitations Our transformer measurements use decoder-block geometries with synthetic weights for controlled experiments (latency is weight-value-independent; correctness is separately verified) and one real 7B checkpoint end-to-end; broader model coverage (MoE, multimodal) is future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22785:end -->

<!-- review:SF-2026-ARXIV-2607-22790:start -->
### The Sparsity Tax: Weight Sparsity Trade-offs in Event-Driven SIMD and SIMT Neuromorphic Cores

<!-- claim:SF-2026-ARXIV-2607-22790:start -->Event-driven neuromorphic inference exploits activation sparsity by updating neuron state only on spikes. However, weight sparsity introduces irregular gather-style updates that undermine lockstep Single Instruction Multiple Data (SIMD) execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22790:end -->

**为什么进入候选分母。** 摘要首要问题为“Event-driven neuromorphic inference exploits activation sparsity by updating neuron state only on spikes.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** However, weight sparsity introduces irregular gather-style updates that undermine lockstep Single Instruction Multiple Data (SIMD) execution.

**证据证明什么。** Results show that total core area changes are insignificant because SRAM dominates area, while performance and energy strongly depend on how sparsity is handled: SIMD and Sparse-SIMD exhibit near-constant throughput, Sparse-SIMD achieves limited energy savings due to bitmap and dense-storage overheads, and SIMT provides the strongest energy scaling and substantial speedups at high sparsity, albeit with sublinear gains due to metadata reads, load imbalance, and sparsity-independent phases.

**证据没有证明什么。** Sparse-SIMD offers a low-disruption option for energy optimization when the storage format cannot be altered, and SIMT proves most effective for high, irregular sparsity, especially if future research can reduce metadata overhead and improve load balancing and handling of sparse layouts, such as convolution boundaries. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22790v1#S2 — II Proposed Architectures; https://arxiv.org/html/2607.22790v1#S2.SS1 — II-A SIMD architecture。Evaluation：https://arxiv.org/html/2607.22790v1#S3 — III Experimental results; https://arxiv.org/html/2607.22790v1#S3.SS1 — III-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.22790v1#S4 — IV Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/stnolting/neorv32, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Sparse-SIMD offers a low-disruption option for energy optimization when the storage format cannot be altered, and SIMT proves most effective for high, irregular sparsity, especially if future research can reduce metadata overhead and improve load balancing and handling of sparse layouts, such as convolution boundaries.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22790:end -->

<!-- review:SF-2026-ARXIV-2607-22798:start -->
### StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents

<!-- claim:SF-2026-ARXIV-2607-22798:start -->Computer-use agents are usually improved by strengthening perception: better models for reading a screenshot and choosing where to click. Yet a screenshot is only a lossy rendering of the underlying program state, e.g., the files, application backends, and DOM that hold the task data. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22798:end -->

**为什么进入候选分母。** 摘要首要问题为“Computer-use agents are usually improved by strengthening perception: better models for reading a screenshot and choosing where to click.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Yet a screenshot is only a lossy rendering of the underlying program state, e.g., the files, application backends, and DOM that hold the task data.

**证据证明什么。** Computer-use agents are usually improved by strengthening perception: better models for reading a screenshot and choosing where to click.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22798v1#S5.SS4 — 5.4 Additional designs。Evaluation：https://arxiv.org/html/2607.22798v1#S5 — 5 Experiments; https://arxiv.org/html/2607.22798v1#S5.SS1 — 5.1 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.22798v1#S6 — 6 Discussion; https://arxiv.org/html/2607.22798v1#S6.SS1 — 6.1 Why State-Grounding Helps: A Failure Analysis。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22798:end -->

<!-- review:SF-2026-ARXIV-2607-22807:start -->
### The Best Programming Language for Tokenmaxxing: An Investigation of Coding Agent Behavior Across Programming Languages

<!-- claim:SF-2026-ARXIV-2607-22807:start -->Although coding agents are now very effective in a variety of programming languages, this paper first shows that the cost (in tokens) can very significantly by programming language. We evaluate five recent models on programming problems in Python, Java, Rust, and OCaml. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22807:end -->

**为什么进入候选分母。** 摘要首要问题为“Although coding agents are now very effective in a variety of programming languages, this paper first shows that the cost (in tokens) can very significantly by programming language.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We evaluate five recent models on programming problems in Python, Java, Rust, and OCaml.

**证据证明什么。** Our results show that by-language token efficiency is a metric that should be considered when benchmarking and developing multilingual agents, and, for the tokenmaxxer, a guide to the most expensive language to work in.

**证据没有证明什么。** Limitations Our study covers four programming languages and five models; the behaviors we identify may not generalize to other models, and the language-specific effects we observe may change as future models improve pretraining coverage of lower-resource languages. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22807v1#A6 — Appendix F System Prompt; https://arxiv.org/html/2607.22807v1#S3 — 3 Methods。Evaluation：https://arxiv.org/html/2607.22807v1#A4 — Appendix D Proprietary Model Results; https://arxiv.org/html/2607.22807v1#S2.SS1 — 2.1 Multilingual Code Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22807v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.22807v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations Our study covers four programming languages and five models; the behaviors we identify may not generalize to other models, and the language-specific effects we observe may change as future models improve pretraining coverage of lower-resource languages.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22807:end -->

<!-- review:SF-2026-ARXIV-2607-22832:start -->
### MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution

<!-- claim:SF-2026-ARXIV-2607-22832:start -->Long-horizon embodied tasks require policies that execute many dependent actions before task success can be observed. Representing policies as executable control pro- grams (code-as-policy) enables their decision logic to be inspected and revised after rollout evaluation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22832:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-horizon embodied tasks require policies that execute many dependent actions before task success can be observed.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce MEMENTO, a memory-guided single-elite memetic framework for code-as-policy evolution.

**证据证明什么。** Ablations show that zero-shot generation and unevolved evaluators fail to solve either domain, and that removing policy-search branches reduces performance.

**证据没有证明什么。** 6 Limitations and Future Work The experiments use two task formulations: four-cube Tower-of-Hanoi manipulation in Robosuite and a long-horizon household-interaction task in AI2-THOR. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22832v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.22832v1#A3 — Appendix C Additional Results; https://arxiv.org/html/2607.22832v1#A3.SS1 — C.1 Evaluator Evolution Results。Limitations / counterevidence：https://arxiv.org/html/2607.22832v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.22832v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：6 Limitations and Future Work The experiments use two task formulations: four-cube Tower-of-Hanoi manipulation in Robosuite and a long-horizon household-interaction task in AI2-THOR.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22832:end -->

<!-- review:SF-2026-ARXIV-2607-22854:start -->
### Coordinated Networking for On-Device Agent-Augmented Real-Time Communication

<!-- claim:SF-2026-ARXIV-2607-22854:start -->AI agents are enabling a new paradigm of agent-augmented real-time communication (RTC), where humans focus on high-level collaboration, while agents autonomously retrieve, analyze, and generate information in real time to support their interactions. These apps enable new experiences across various domains: for example, when corporate employees co-author a legal document, their agents can discuss and draft on their behalf, sparing them the burden of manually reviewing each other's work. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22854:end -->

**为什么进入候选分母。** 摘要首要问题为“AI agents are enabling a new paradigm of agent-augmented real-time communication (RTC), where humans focus on high-level collaboration, while agents autonomously retrieve, analyze, and generate information in real time to support their interactions.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We design HFS, a framework to ensure both high live video quality and low agent response latency in agent-augmented RTC apps.

**证据证明什么。** Our prototype built atop WebRTC and llama.cpp demonstrates that HAFS outperforms baselines, achieving 1.5x higher video quality while reducing agent response time by 31%.

**证据没有证明什么。** In particular, each flow’s buffer size may become constrained by available memory, leading to a throughput drop because SCTP cannot maintain a sufficiently large congestion window. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22854v1#S3.SS1 — 3.1 Base System Pipeline Design; https://arxiv.org/html/2607.22854v1#S4.SS4 — 4.4 System Architecture。Evaluation：https://arxiv.org/html/2607.22854v1#S8 — 8 Performance Evaluation; https://arxiv.org/html/2607.22854v1#S8.SS1 — 8.1 Evaluation Setup。Limitations / counterevidence：https://arxiv.org/html/2607.22854v1#S9 — 9 Discussion and Future Work; https://arxiv.org/html/2607.22854v1#S11 — 11 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/agent-network-protocol/AgentNetworkProtocol, https://github.com/ggml-org/llama.cpp, https://github.com/a2aproject/A2A; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：In particular, each flow’s buffer size may become constrained by available memory, leading to a throughput drop because SCTP cannot maintain a sufficiently large congestion window.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22854:end -->

<!-- review:SF-2026-ARXIV-2607-22868:start -->
### What Can Be Enforced? A Theory of Certified Runtime Safety for Tool-Using Agents

<!-- claim:SF-2026-ARXIV-2607-22868:start -->Runtime guardrails act before irreversible tool calls, but their guarantees depend on what policy state is representable, what a judge observes, and whether intervention changes future behavior. First, relative to fixed oracle predicates, a deterministic gate enforces exactly the nonempty safety policies whose good prefixes its register model recognizes; policy nontriviality is undecidable with two decrementable counters but in PSPACE for a separable monotone fragment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22868:end -->

**为什么进入候选分母。** 摘要首要问题为“Runtime guardrails act before irreversible tool calls, but their guarantees depend on what policy state is representable, what a judge observes, and whether intervention changes future behavior.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** First, relative to fixed oracle predicates, a deterministic gate enforces exactly the nonempty safety policies whose good prefixes its register model recognizes; policy nontriviality is undecidable with two decrementable counters but in PSPACE for a separable monotone fragment.

**证据证明什么。** Experiments target these distinctions through static diagnostics, controlled-model enumeration, representation rewrites, and paired closed-loop reruns.

**证据没有证明什么。** The margin-dependent bound covers only the declared bounded representation adversary, not arbitrary shift. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22868v1#S3 — 3 The Enforcement Model。Evaluation：https://arxiv.org/html/2607.22868v1#A2 — Appendix B Extended Experiments and Reproducibility; https://arxiv.org/html/2607.22868v1#A2.SSx4 — B.4 AgentDojo benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.22868v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.22868v1#A2.SSx15 — B.15 Threats to validity。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The margin-dependent bound covers only the declared bounded representation adversary, not arbitrary shift.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22868:end -->

<!-- review:SF-2026-ARXIV-2607-22872:start -->
### Same Predictions, Different Reasons: The Effect of Quantization on Model Explanations

<!-- claim:SF-2026-ARXIV-2607-22872:start -->Post-training quantization (PTQ) has become a practical solution for deploying deep learning models on resource-constrained edge devices by compressing high-precision floating-point weights into low-precision representations without requiring retraining. Past research has demonstrated that quantization largely preserves classification accuracy; however, whether it also preserves the model's internal reasoning remains an open question. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22872:end -->

**为什么进入候选分母。** 摘要首要问题为“Post-training quantization (PTQ) has become a practical solution for deploying deep learning models on resource-constrained edge devices by compressing high-precision floating-point weights into low-precision representations without requiring retraining.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We employ a dual interpretability framework that combines Grad-CAM for spatial attention analysis with LIME for input-level feature attribution, and systematically compare full-precision and quantized models on two binary classification datasets.

**证据证明什么。** The results show that classification accuracy is not a reliable indicator of interpretability stability under reduced precision.

**证据没有证明什么。** Even though its Grad-CAM performance remains acceptable, with only moderate changes, LIME attribution deteriorates completely at INT4 precision, a subtle issue that cannot be identified by accuracy metrics alone. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22872v1#S2 — 2 Methodology; https://arxiv.org/html/2607.22872v1#S2.SS2 — 2.2 Models。Evaluation：https://arxiv.org/html/2607.22872v1#S2.SS5 — 2.5 Evaluation Metrics; https://arxiv.org/html/2607.22872v1#S3 — 3 Results and Discussion。Limitations / counterevidence：https://arxiv.org/html/2607.22872v1#S3 — 3 Results and Discussion; https://arxiv.org/html/2607.22872v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Even though its Grad-CAM performance remains acceptable, with only moderate changes, LIME attribution deteriorates completely at INT4 precision, a subtle issue that cannot be identified by accuracy metrics alone.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22872:end -->

<!-- review:SF-2026-ARXIV-2607-22880:start -->
### Do Coverage and Mutation Scores of LLM-Generated Test Suites Correlate with Their Effectiveness? (Replicability Study)

<!-- claim:SF-2026-ARXIV-2607-22880:start -->Recent advances in large language models (LLMs) have driven growing interest in using LLMs to automate test generation. Prior work commonly evaluates generated test suites using proxy metrics such as code coverage and mutation score. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22880:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in large language models (LLMs) have driven growing interest in using LLMs to automate test generation.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Prior work commonly evaluates generated test suites using proxy metrics such as code coverage and mutation score.

**证据证明什么。** Our findings diverge substantially from prior results.

**证据没有证明什么。** In our results, correlations between coverage criteria are only moderate to strong depending on the particular pair, and this pattern is primarily observed under the average aggregation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22880v1#S3 — 3. Methodology; https://arxiv.org/html/2607.22880v1#S3.SS3 — 3.3. Models。Evaluation：https://arxiv.org/html/2607.22880v1#S3.SS2 — 3.2. Benchmark; https://arxiv.org/html/2607.22880v1#S3.SS7 — 3.7. Correlation Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.22880v1#S9 — 9. Conclusion and Future Work; https://arxiv.org/html/2607.22880v1#S7 — 7. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/drixs2050/Cov_mut_bug_detect_correlation, http://codecover.org/, https://qwenlm.github.io/blog/qwen3-coder/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：In our results, correlations between coverage criteria are only moderate to strong depending on the particular pair, and this pattern is primarily observed under the average aggregation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22880:end -->

<!-- review:SF-2026-ARXIV-2607-22883:start -->
### Evaluating and Mitigating the Misguidance Effect of Buggy Code in LLM-Generated Unit Tests

<!-- claim:SF-2026-ARXIV-2607-22883:start -->While Large Language Models (LLMs) show great promise for automating unit test generation, recent studies suggest that the quality of generated tests can be negatively impacted when models are prompted with buggy code. This paper presents a new metric to quantitatively measure the "misguidance effect," a phenomenon where buggy code steers LLMs toward generating tests that validate its erroneous behavior rather than expose it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22883:end -->

**为什么进入候选分母。** 摘要首要问题为“While Large Language Models (LLMs) show great promise for automating unit test generation, recent studies suggest that the quality of generated tests can be negatively impacted when models are prompted with buggy code.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To counter this, we introduce and validate a specification-based unit test generation paradigm that replaces the code under test in the prompt with an LLM-generated specification docstring.

**证据证明什么。** Our results show that this paradigm effectively reduces misguided tests while substantially increasing effective tests, improves multi-round, feedback-driven test generation pipelines, and remains applicable to both buggy and bug-free code.

**证据没有证明什么。** We thank Yuliang Song for serving as an external annotator in our qualitative analysis. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22883v1#S2 — 2. Study Design; https://arxiv.org/html/2607.22883v1#S2.SS5 — 2.5. Mitigation Methodology and Baselines。Evaluation：https://arxiv.org/html/2607.22883v1#S2.SS2 — 2.2. Benchmark; https://arxiv.org/html/2607.22883v1#S2 — 2. Study Design。Limitations / counterevidence：https://arxiv.org/html/2607.22883v1#S6 — 6. Threats to Validity and Limitations; https://arxiv.org/html/2607.22883v1#S8 — 8. Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/drixs2050/EvalAndMitigate, https://qwenlm.github.io/blog/qwen3-coder/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We thank Yuliang Song for serving as an external annotator in our qualitative analysis.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22883:end -->

<!-- review:SF-2026-ARXIV-2607-22898:start -->
### AssumptionMiner: Extracting, Tracing, and Revising Implicit Assumptions in LLM Code Generation

<!-- claim:SF-2026-ARXIV-2607-22898:start -->Large language models (LLMs) generate code from natural-language prompts, yet real-world prompts rarely provide complete specifications. When prompts leave input formats, error handling, or design decisions unspecified, LLMs fill these gaps with implicit assumptions that shape the generated code's behavior and correctness. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22898:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) generate code from natural-language prompts, yet real-world prompts rarely provide complete specifications.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present AssumptionMiner, a framework that makes implicit assumptions a first-class artifact of LLM-based code generation.

**证据证明什么。** These results demonstrate that making assumptions explicit improves the transparency and controllability of LLM-based code generation.

**证据没有证明什么。** Agreement was high on the two judgments that do not depend on line numbers: validity reached 99.1% raw agreement ( , and both raters independently rejected only a single candidate that restates an explicit prompt requirement), and category reached 88.3% raw agreement ( , “almost perfect” [ 42 ] ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22898v1#A3.SS1 — C-A Novel Task Design; https://arxiv.org/html/2607.22898v1#A5.SS1 — E-A Architecture and Components。Evaluation：https://arxiv.org/html/2607.22898v1#A3 — Appendix C Benchmark Construction Details; https://arxiv.org/html/2607.22898v1#A6.SS2 — F-B Running the Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.22898v1#S6.SS7 — VI-G Discussion; https://arxiv.org/html/2607.22898v1#S8 — VIII Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Agreement was high on the two judgments that do not depend on line numbers: validity reached 99.1% raw agreement ( , and both raters independently rejected only a single candidate that restates an explicit prompt requirement), and category reached 88.3% raw agreement ( , “almost perfect” [ 42 ] ).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22898:end -->

<!-- review:SF-2026-ARXIV-2607-22917:start -->
### Agent Team Work Zone: An Automated, Persistent Workspace for Long-Lived Claude Code Agent Teams

<!-- claim:SF-2026-ARXIV-2607-22917:start -->Large Language Model (LLM) agents have significantly improved coding and programming workflows. Claude Code, in particular, is one of the most powerful LLM coding agents and is capable of conducting complex coding tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22917:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Model (LLM) agents have significantly improved coding and programming workflows.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose ATWZ (Agent Team Work Zone), a filesystem-based operations layer built around Claude Code's native Agent Teams that addresses these problems.

**证据证明什么。** Large Language Model (LLM) agents have significantly improved coding and programming workflows.

**证据没有证明什么。** 12 Limitations and Future Work The design has edges we know about; stating them is part of the same posture as the rest of the manual. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22917v1#S4 — 4 Design Philosophy; https://arxiv.org/html/2607.22917v1#A1.SS1 — A.1 Large Language Models。Evaluation：https://arxiv.org/html/2607.22917v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22917v1#S2 — 2 Background: Claude Code, Subagents, and Agent Teams。Limitations / counterevidence：https://arxiv.org/html/2607.22917v1#S12 — 12 Limitations and Future Work; https://arxiv.org/html/2607.22917v1#S10 — 10 Failure Modes and Hardening。

**Artifact boundary。** Exact v1 links https://github.com/SR-A-W/agent-team-work-zone, https://code.claude.com/docs/en/agent-teams, https://code.claude.com/docs/en/memory; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：12 Limitations and Future Work The design has edges we know about; stating them is part of the same posture as the rest of the manual.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22917:end -->

<!-- review:SF-2026-ARXIV-2607-22925:start -->
### Not All LLM Reasoning is Visible in the Chain-of-Thought

<!-- claim:SF-2026-ARXIV-2607-22925:start -->A key question for AI safety is whether a language model expresses all of its reasoning in its output tokens. We demonstrate a concrete failure mode where frontier models exhibit invisible reasoning by leveraging semantically irrelevant filler tokens to improve performance on synthetic reasoning tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22925:end -->

**为什么进入候选分母。** 摘要首要问题为“A key question for AI safety is whether a language model expresses all of its reasoning in its output tokens.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We demonstrate a concrete failure mode where frontier models exhibit invisible reasoning by leveraging semantically irrelevant filler tokens to improve performance on synthetic reasoning tasks.

**证据证明什么。** We demonstrate a concrete failure mode where frontier models exhibit invisible reasoning by leveraging semantically irrelevant filler tokens to improve performance on synthetic reasoning tasks.

**证据没有证明什么。** A model that shifts test-time compute from decode into prefill could therefore serve responses more cheaply, though realized savings depend on batching, context length, and serving configuration. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22925v1#S3 — 3 Methodology; https://arxiv.org/html/2607.22925v1#S6 — 6 What Training Methodologies Elicit Invisible Reasoning?。Evaluation：https://arxiv.org/html/2607.22925v1#A6 — Appendix F RL Experiment Results; https://arxiv.org/html/2607.22925v1#A1 — Appendix A Invisible Reasoning Evaluation Details。Limitations / counterevidence：https://arxiv.org/html/2607.22925v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/togethercomputer/xorl, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A model that shifts test-time compute from decode into prefill could therefore serve responses more cheaply, though realized savings depend on batching, context length, and serving configuration.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22925:end -->

<!-- review:SF-2026-ARXIV-2607-22926:start -->
### SAGE: Safety-First Defense-in-Depth Guardrails for Verified Lifecycle Control of High-Impact Generative AI

<!-- claim:SF-2026-ARXIV-2607-22926:start -->High-impact generative AI makes catastrophic misuse a lifecycle-control problem, not merely a prompt-filtering problem. SAGE is a safety-first, authorization-separated architecture in which credible catastrophic-enablement risk constrains admissibility before utility, latency, or commercial objectives are considered. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22926:end -->

**为什么进入候选分母。** 摘要首要问题为“High-impact generative AI makes catastrophic misuse a lifecycle-control problem, not merely a prompt-filtering problem.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** SAGE is a safety-first, authorization-separated architecture in which credible catastrophic-enablement risk constrains admissibility before utility, latency, or commercial objectives are considered.

**证据证明什么。** Formal results establish safety priority, conservative detector bounds, monotone release gating, tamper-evident records, and an authorization cut; two PRISM abstractions verify authorization separation and lifecycle invariants under explicit assumptions.

**证据没有证明什么。** Component scores and conservative uncertainty bounds therefore inform, but cannot satisfy, a catastrophic-risk release threshold. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22926v1#S4 — 4 SAGE Formal Framework; https://arxiv.org/html/2607.22926v1#S5 — 5 Reference Architecture and Implementation。Evaluation：https://arxiv.org/html/2607.22926v1#S6 — 6 Experimental Design; https://arxiv.org/html/2607.22926v1#S7 — 7 Results。Limitations / counterevidence：https://arxiv.org/html/2607.22926v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.22926v1#S8 — 8 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Component scores and conservative uncertainty bounds therefore inform, but cannot satisfy, a catastrophic-risk release threshold.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22926:end -->

<!-- review:SF-2026-ARXIV-2607-22927:start -->
### Hidden Boundary Motion in Transformer Optimization: Function-Space Orthogonalization of Affine Weight and Bias Updates

<!-- claim:SF-2026-ARXIV-2607-22927:start -->Weights and biases are normally optimized as separate parameter tensors, yet they do not represent separate functions when the input to an affine layer has nonzero mean. For an affine map $z=Wx+b$ with input mean $μ$, a weight update contains a sample-independent displacement $ΔWμ$ that is functionally indistinguishable from a bias update. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22927:end -->

**为什么进入候选分母。** 摘要首要问题为“Weights and biases are normally optimized as separate parameter tensors, yet they do not represent separate functions when the input to an affine layer has nonzero mean.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** For an affine map $z=Wx+b$ with input mean $μ$, a weight update contains a sample-independent displacement $ΔWμ$ that is functionally indistinguishable from a bias update.

**证据证明什么。** However, the moving-batch-center compensation produces severe bias-coordinate drift and strongly reduces boundary energy.

**证据没有证明什么。** 8 Limitations The study has several substantial limitations. • Only one seed, one dataset, and one small Transformer are evaluated. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22927v1#S7.SS2 — 7.2 Relationship to centering and natural-gradient methods。Evaluation：https://arxiv.org/html/2607.22927v1#S5 — 5 Experimental Setup; https://arxiv.org/html/2607.22927v1#S6 — 6 Results。Limitations / counterevidence：https://arxiv.org/html/2607.22927v1#S7 — 7 Discussion; https://arxiv.org/html/2607.22927v1#S8 — 8 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：8 Limitations The study has several substantial limitations. • Only one seed, one dataset, and one small Transformer are evaluated.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22927:end -->

<!-- review:SF-2026-ARXIV-2607-22949:start -->
### Beyond Exact Match: How Evaluation Methodology Dominates Model Choice in LLM-Based Product Attribute Extraction

<!-- claim:SF-2026-ARXIV-2607-22949:start -->Large language models (LLMs) have become a default choice for structured product attribute extraction in e-commerce pipelines, with practitioners reporting widely varying performance across models, datasets, and prompting strategies. This paper presents a controlled empirical study comparing four prompting strategies -- zero-shot, few-shot, schema-guided, and definition-augmented -- across two production-grade LLMs (GPT-4o-mini and Gemini 2.5 Flash) on the MAVE benchmark. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22949:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) have become a default choice for structured product attribute extraction in e-commerce pipelines, with practitioners reporting widely varying performance across models, datasets, and prompting strategies.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We conclude that for production attribute extraction pipelines, evaluation methodology and data quality dominate the impact of model selection and prompt engineering.

**证据证明什么。** We conclude that for production attribute extraction pipelines, evaluation methodology and data quality dominate the impact of model selection and prompt engineering.

**证据没有证明什么。** We do not claim fuzzy matching is the final solution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22949v1#S2.SS2 — II-B Evaluation Methodology in Information Extraction; https://arxiv.org/html/2607.22949v1#S4 — IV Experimental Methodology。Evaluation：https://arxiv.org/html/2607.22949v1#S2.SS2 — II-B Evaluation Methodology in Information Extraction; https://arxiv.org/html/2607.22949v1#S2.SS3 — II-C Ground Truth Quality in Public Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.22949v1#S6 — VI Discussion; https://arxiv.org/html/2607.22949v1#S6.SS3 — VI-C Ground Truth Noise as a Structural Limitation。

**Artifact boundary。** Exact v1 links https://github.com/a-dwivedi/llm-product-attribute-extraction, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We do not claim fuzzy matching is the final solution.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22949:end -->

<!-- review:SF-2026-ARXIV-2607-22951:start -->
### Modeling Memory-Dependent Reliability of LLMs: A Hidden Markov Model

<!-- claim:SF-2026-ARXIV-2607-22951:start -->Reliability assessment of large language models (LLMs) seeks to estimate the probability that a model produces correct responses under a specified operational profile. Conventional benchmark-based evaluation, often summarized by aggregate accuracy, provides a point estimate of performance but does not characterize the uncertainty associated with reliability claims. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22951:end -->

**为什么进入候选分母。** 摘要首要问题为“Reliability assessment of large language models (LLMs) seeks to estimate the probability that a model produces correct responses under a specified operational profile.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Currently, statistical inference methods for LLM reliability assessment are emerging.

**证据证明什么。** The results suggest that ignoring sequential dependence may lead to overconfident reliability estimates.

**证据没有证明什么。** Future work will investigate deployment-derived and instance-specific OPs, real user interaction traces, cross-domain dependence, time-varying transition dynamics, adaptive task-arrival processes, and a broader range of LLMs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22951v1#S3.SS1 — III-A Domain-Specific Hidden Markov Model; https://arxiv.org/html/2607.22951v1#S3.SS2 — III-B Modeling Assumptions and Practical Considerations。Evaluation：https://arxiv.org/html/2607.22951v1#S4 — IV Evaluation; https://arxiv.org/html/2607.22951v1#S4.SS2 — IV-B Numerical Results。Limitations / counterevidence：https://arxiv.org/html/2607.22951v1#S5 — V Discussion and conclusion。

**Artifact boundary。** Exact v1 links https://github.com/llmReliability/hmm-llm-reliability-proof, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work will investigate deployment-derived and instance-specific OPs, real user interaction traces, cross-domain dependence, time-varying transition dynamics, adaptive task-arrival processes, and a broader range of LLMs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22951:end -->

<!-- review:SF-2026-ARXIV-2607-22953:start -->
### Share No More Than the Request Requires: Federated Disclosure for Perspective-Aware AI

<!-- claim:SF-2026-ARXIV-2607-22953:start -->Modern AI systems bring societal risks such as mass surveillance, extreme concentrations of power, and loss of user autonomy---calling into question a model where third-parties collect and control massive amounts of user data. Users require a sovereign system to securely own, govern, and disclose their context while remaining compliant across regulated domains with strict provenance, interpretability, and policy adherence. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22953:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern AI systems bring societal risks such as mass surveillance, extreme concentrations of power, and loss of user autonomy---calling into question a model where third-parties collect and control massive amounts of user data.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Users require a sovereign system to securely own, govern, and disclose their context while remaining compliant across regulated domains with strict provenance, interpretability, and policy adherence.

**证据证明什么。** We frame the problem, map gaps in blockchain, P2P, and holder-sovereign designs, define the core constructs, and sketch the protocol with an explicit threat model.

**证据没有证明什么。** Out of scope (as assumptions or open problems): a coordinator we assume honest-but-curious, seeing only compiled, already-authorized and alignment metadata (a Byzantine coordinator is future work); forged credentials , since we assume the verifiable-presentation/DID layer (§ 6 ) is sound; holder collusion to reconstruct denied data; provenance-reference leakage , treating Phase-1 IDs as opaque capability handles that reveal nothing without an authorized Phase-2 release (proving this is open); and prompt injection into the planner , a malicious steering over-broad—a live risk, since the planner gates soundness (§ 4.2 ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22953v1#S4 — 4. Framework Design; https://arxiv.org/html/2607.22953v1#S6.SS1 — 6.1. Threat Model。Evaluation：https://arxiv.org/html/2607.22953v1#S1 — 1. Introduction; https://arxiv.org/html/2607.22953v1#S2 — 2. Background。Limitations / counterevidence：https://arxiv.org/html/2607.22953v1#S6.SS1 — 6.1. Threat Model; https://arxiv.org/html/2607.22953v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://solidproject.org/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Out of scope (as assumptions or open problems): a coordinator we assume honest-but-curious, seeing only compiled, already-authorized and alignment metadata (a Byzantine coordinator is future work); forged credentials , since we assume the verifiable-presentation/DID layer (§ 6 ) is sound; holder collusion to reconstruct denied data; provenance-reference leakage , treating Phase-1 IDs as opaque capability handles that reveal nothing without an authorized Phase-2 release (proving this is open); and prompt injection into the planner , a malicious steering over-broad—a live risk, since the planner gates soundness (§ 4.2 ).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22953:end -->

<!-- review:SF-2026-ARXIV-2607-22962:start -->
### ConsistencyGate: Preventing Memory Contamination in LLM Agents via Self-Consistency Admission Control

<!-- claim:SF-2026-ARXIV-2607-22962:start -->LLM agents that operate over many turns accumulate facts in an external memory store and reuse them as premises for downstream reasoning. A hallucinated fact written at one step therefore persists as a false premise for every subsequent step, a failure mode we call memory contamination. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22962:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents that operate over many turns accumulate facts in an external memory store and reuse them as premises for downstream reasoning.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose ConsistencyGate, a write-time admission gate that, before committing a candidate fact m extracted from context c, queries the LLM K times for a soft support score and admits m only when the average exceeds a threshold.

**证据证明什么。** The mechanism is model-agnostic, requires no fine-tuning, and reduces to a single forward pass in a log-probability variant for latency-sensitive deployments.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22962v1#S4.SS1 — 4.1 Core Algorithm; https://arxiv.org/html/2607.22962v1#S6.SS3 — 6.3 Cross-Model Generalization。Evaluation：https://arxiv.org/html/2607.22962v1#A1 — Appendix A Full Ablation Results; https://arxiv.org/html/2607.22962v1#A5 — Appendix E Benchmark Dataset Details。Limitations / counterevidence：https://arxiv.org/html/2607.22962v1#S7 — 7 Failure Modes and Operating Regime; https://arxiv.org/html/2607.22962v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22962:end -->

<!-- review:SF-2026-ARXIV-2607-22997:start -->
### Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline

<!-- claim:SF-2026-ARXIV-2607-22997:start -->Physical AI -- the integration of large vision-language-action (VLA) models with embodied agents that act in the real world -- has emerged as the next major frontier for AI, echoed by industry leaders such as Jensen Huang (``the next big thing is Physical AI, AI with a body,'' GTC Paris, June 2025) and Dr. Lisa Su (`we're entering the world of Physical AI ... this is where AI enters the real world,' CES 2026). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22997:end -->

**为什么进入候选分母。** 摘要首要问题为“Physical AI -- the integration of large vision-language-action (VLA) models with embodied agents that act in the real world -- has emerged as the next major frontier for AI, echoed by industry leaders such as Jensen Huang (``the next big thing is Physical AI, AI with a body,'' GTC Paris, June 2025) and Dr.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We demonstrate that training and deploying VLA-based manipulation policies does not require a CUDA-locked ecosystem.

**证据证明什么。** We demonstrate that training and deploying VLA-based manipulation policies does not require a CUDA-locked ecosystem.

**证据没有证明什么。** Taken together, these four demonstrations are not four isolated capabilities but four stages of one continuous pipeline: simulate, manipulate, reconstruct, and generalize. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22997v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22997v1#S2 — 2 Demo 1: Sim-to-Real Manipulation [ 6 ]。Evaluation：https://arxiv.org/html/2607.22997v1#S2.SS0.SSS0.Px1 — Analysis.; https://arxiv.org/html/2607.22997v1#S3.SS0.SSS0.Px1 — Analysis.。Limitations / counterevidence：https://arxiv.org/html/2607.22997v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/AMD-AIM/Physical_AI_Challenge, https://github.com/huggingface/lerobot, https://huggingface.co/blog/smolvla; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Taken together, these four demonstrations are not four isolated capabilities but four stages of one continuous pipeline: simulate, manipulate, reconstruct, and generalize.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22997:end -->

<!-- review:SF-2026-ARXIV-2607-22999:start -->
### WCM: World-Cognition Model for Generalizable Human-Robot Interaction

<!-- claim:SF-2026-ARXIV-2607-22999:start -->Language agents can now interact fluently with users in software, but robots still struggle to bring comparable interaction to physical tasks. Current robot-control paradigms, including vision-language-action policies and world-model-based planners, are mainly optimized for instruction execution, leaving users with little visibility into why an action is chosen and few mechanisms to redirect, correct, or teach the robot through interaction. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22999:end -->

**为什么进入候选分母。** 摘要首要问题为“Language agents can now interact fluently with users in software, but robots still struggle to bring comparable interaction to physical tasks.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To solve this problem, we present the World-Cognition Model (WCM), a human-centered embodied agent built on the SLAK architecture (Sensing, Logic, Action, and Knowledge) and an asynchronous runtime.

**证据证明什么。** Teaching episodes and autonomous task rollouts are refined into chain-of-thought supervision to continually improve the model.

**证据没有证明什么。** While currently limited by hardware and a case-study evaluation, WCM points toward robots that can act, explain, be corrected, and improve with people in the loop. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22999v1#S2.SS1 — II-A System Architecture and Runtime; https://arxiv.org/html/2607.22999v1#S2 — II Method: The World-Cognition Model。Evaluation：https://arxiv.org/html/2607.22999v1#A2 — Appendix B Performance Comparison Results; https://arxiv.org/html/2607.22999v1#A3 — Appendix C Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.22999v1#S4 — IV Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：While currently limited by hardware and a case-study evaluation, WCM points toward robots that can act, explain, be corrected, and improve with people in the loop.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22999:end -->

<!-- review:SF-2026-ARXIV-2607-23002:start -->
### Adversarial Test-Hardening for AI-Written Code: An Instrument Autopsy and a Pre-Registered Causal Estimate of the Critic Loop

<!-- claim:SF-2026-ARXIV-2607-23002:start -->Large language models increasingly write both code and the tests meant to check it; coverage records what ran, not what was verified. We study an adversarial test-hardening loop under a mechanical oracle: a Tester model writes tests, mutation testing names surviving injected defects, and a Critic model writes tests to kill exactly those, with every verdict decided mechanically, so no model judges another's output. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23002:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models increasingly write both code and the tests meant to check it; coverage records what ran, not what was verified.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We study an adversarial test-hardening loop under a mechanical oracle: a Tester model writes tests, mutation testing names surviving injected defects, and a Critic model writes tests to kill exactly those, with every verdict decided mechanically, so no model judges another's output.

**证据证明什么。** Under a pre-registered frozen-shared-round-0 design (five replicates on each of four subjects, seeds committed in advance), same-lineage Critic rounds killed 78% of the survivors the frozen initial suite left standing (mean incremental kill rate 0.783, 95% cluster-bootstrap interval [0.592, 0.935]), a within-replicate causal estimate; the cross-provider configuration showed a positive pilot difference (rate gap 0.178, 95% interval [0.039, 0.347]; magnitude dominated by a single replicate) at 5.5x lower arm cost.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23002v1#Sx1.SSx4 — 3. Method。Evaluation：https://arxiv.org/html/2607.23002v1#Sx1.SSx5 — 4. Results。Limitations / counterevidence：https://arxiv.org/html/2607.23002v1#Sx1.SSx6 — 5. Discussion; https://arxiv.org/html/2607.23002v1#Sx1.SSx7 — 6. Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23002:end -->

<!-- review:SF-2026-ARXIV-2607-23012:start -->
### Mini-batch Noise Lowers Sharpness via Dominant-Subspace Fluctuations

<!-- claim:SF-2026-ARXIV-2607-23012:start -->During SGD training, the gradients often align strongly with the dominant subspace spanned by the top-$k$ eigenvectors of the Hessian of the loss. While this seems to naturally imply that loss reduction mainly occurs within this space, prior work has shown that updates within this dominant subspace make no meaningful progress in reducing the loss. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23012:end -->

**为什么进入候选分母。** 摘要首要问题为“During SGD training, the gradients often align strongly with the dominant subspace spanned by the top-$k$ eigenvectors of the Hessian of the loss.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** While this seems to naturally imply that loss reduction mainly occurs within this space, prior work has shown that updates within this dominant subspace make no meaningful progress in reducing the loss.

**证据证明什么。** Experimental results show that adding the derived correction term to GD brings the sharpness evolution of GD closer to that of SGD.

**证据没有证明什么。** Does the dominant subspace therefore contribute nothing to training? 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.23012v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23012v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.23012v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23012v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.23012v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23012v1#page=10 — PDF page 10。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Does the dominant subspace therefore contribute nothing to training?

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23012:end -->

<!-- review:SF-2026-ARXIV-2607-23015:start -->
### Mask2Shield: Strengthening LLM Safety against Neuron-Pruning Attacks

<!-- claim:SF-2026-ARXIV-2607-23015:start -->Large language models (LLMs) are safety-aligned before deployment to reduce harmful content generation. Yet neuron-level pruning attacks show that refusal can depend on a small set of removable units: disabling them can remove safety behavior while leaving much of the model usable. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23015:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) are safety-aligned before deployment to reduce harmful content generation.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this problem, we introduce Mask2Shield (M2S), a masked-forward alignment method that trains a model under this functional pruning.

**证据证明什么。** Together, these results show that M2S makes targeted pruning less effective by reducing reliance on a small, removable safety-neuron set.

**证据没有证明什么。** We limit the attack to sparse channel removal. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23015v1#A1.SS1 — A-A System-Prompt Diversification; https://arxiv.org/html/2607.23015v1#S3 — III Method。Evaluation：https://arxiv.org/html/2607.23015v1#S4 — IV Experimental Results; https://arxiv.org/html/2607.23015v1#S4.SS2 — IV-B Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.23015v1#S3.SS1 — III-A Threat Model; https://arxiv.org/html/2607.23015v1#S5 — V Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：We limit the attack to sparse channel removal.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23015:end -->

<!-- review:SF-2026-ARXIV-2607-23045:start -->
### Stress-testing large language model agents in a robotic chemistry laboratory

<!-- claim:SF-2026-ARXIV-2607-23045:start -->AI is evaluated through knowledge, reasoning and plan generation, yet scientific agency requires reliable physical action and adaptation to evidence. Here, we use a robotic chemistry laboratory as a physical-world testbed to make scientific agency measurable. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23045:end -->

**为什么进入候选分母。** 摘要首要问题为“AI is evaluated through knowledge, reasoning and plan generation, yet scientific agency requires reliable physical action and adaptation to evidence.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Only 3.3% of trials produced expert-assessed executable workflows under laboratory constraints; even the best system achieved 28.1%.

**证据证明什么。** Only 3.3% of trials produced expert-assessed executable workflows under laboratory constraints; even the best system achieved 28.1%.

**证据没有证明什么。** Only 3.3% of trials produced expert-assessed executable workflows under laboratory constraints; even the best system achieved 28.1%. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.23045v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23045v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.23045v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23045v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.23045v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23045v1#page=10 — PDF page 10。

**Artifact boundary。** Exact v1 links https://github.com/pic-ai-robotic-chemistry/LabBench; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Only 3.3% of trials produced expert-assessed executable workflows under laboratory constraints; even the best system achieved 28.1%.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23045:end -->

<!-- review:SF-2026-ARXIV-2607-23046:start -->
### Structured Redundancy Modeling for Efficient Visual Token Pruning in High-Resolution MLLMs

<!-- claim:SF-2026-ARXIV-2607-23046:start -->Recent high-resolution Multimodal Large Language Models (MLLMs) generate thousands of visual tokens per input, leading to a visual token explosion that introduces severe latency bottlenecks. While token pruning mitigates this issue, state-of-the-art subset-optimization methods typically rely on iterative subset construction to jointly capture visual diversity and instruction relevance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23046:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent high-resolution Multimodal Large Language Models (MLLMs) generate thousands of visual tokens per input, leading to a visual token explosion that introduces severe latency bottlenecks.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** First, to attenuate redundancy at the covariance level, we introduce a semantics-guided ridge leverage scheme.

**证据证明什么。** Our non-iterative framework achieves redundancy-aware importance selection in a single forward pass through two complementary mechanisms.

**证据没有证明什么。** This formulation enables structured redundancy control while avoiding iterative dependency in the pruning process. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23046v1#S2.SS1 — 2.1 Vision Token Pruning Methods; https://arxiv.org/html/2607.23046v1#S2.SS2 — 2.2 Ridge Leverage Score in Neural Architectures。Evaluation：https://arxiv.org/html/2607.23046v1#S4 — 4 Experiments; https://arxiv.org/html/2607.23046v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.23046v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/cvsp-lab/SFPruner, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：This formulation enables structured redundancy control while avoiding iterative dependency in the pruning process.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23046:end -->

<!-- review:SF-2026-ARXIV-2607-23047:start -->
### MixQuant: Adaptive Mixed-Precision Quantization for Large Language Models

<!-- claim:SF-2026-ARXIV-2607-23047:start -->Mixed-precision quantization improves the accuracy of post-training quantization by allocating higher bitwidths to sensitive layers, but existing methods solve the allocation for a single fixed memory budget. In practice the budget varies across deployments and is unknown at calibration time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23047:end -->

**为什么进入候选分母。** 摘要首要问题为“Mixed-precision quantization improves the accuracy of post-training quantization by allocating higher bitwidths to sensitive layers, but existing methods solve the allocation for a single fixed memory budget.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose MixQuant, a technique-agnostic adaptive framework that wraps any base quantizer.

**证据证明什么。** We show that a layer's sensitivity depends strongly on the bitwidths of its upstream layers and that this dependence shifts the resulting preferred bit allocation.

**证据没有证明什么。** Future work includes extending MixQuant to jointly allocate precision across weights, activations, and KV-cache, toward maximizing efficiency in adaptive settings on the edge. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23047v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.23047v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.23047v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Future work includes extending MixQuant to jointly allocate precision across weights, activations, and KV-cache, toward maximizing efficiency in adaptive settings on the edge.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23047:end -->

<!-- review:SF-2026-ARXIV-2607-23050:start -->
### The Entropic Bound for Transformers: Why Static Rank Fails and Attention-Native Rank Recovers

<!-- claim:SF-2026-ARXIV-2607-23050:start -->Neural scaling laws describe how loss decreases as models, data, and compute grow, but they do not answer a prior question: for a fixed task, what is the minimum model capacity required to solve it? We study this through the Entropic Bound, a spectral notion of task-intrinsic capacity for Transformers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23050:end -->

**为什么进入候选分母。** 摘要首要问题为“Neural scaling laws describe how loss decreases as models, data, and compute grow, but they do not answer a prior question: for a fixed task, what is the minimum model capacity required to solve it?”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Motivated by this, we introduce an attention-native intrinsic rank -- the minimum query-key kernel rank realizing the task within the attention class -- and show that under this definition the full Entropic Bound structure (deficiency, achievability, recovery) is restored for both linear and softmax attention, with the energy effective rank as the estimator robust to softmax distortion.

**证据证明什么。** Our results reframe the Entropic Bound from a post-hoc descriptor into an attention-native capacity measure with a precisely characterized predictability frontier.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23050v1#A3.SS3 — C.3 Student models。Evaluation：https://arxiv.org/html/2607.23050v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.23050v1#A4 — Appendix D Spectral-Gap Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.23050v1#S7 — 7 Discussion, Limitations, and Open Problems。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SELF-ATTENTION`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23050:end -->

<!-- review:SF-2026-ARXIV-2607-23054:start -->
### Through the Bottleneck: How Multi-head Latent Attention Separates Content from Position in Language Models

<!-- claim:SF-2026-ARXIV-2607-23054:start -->Multi-head Latent Attention (MLA), introduced in DeepSeek-V2, compresses key-value pairs through a shared low-rank bottleneck (cKV), achieving 81% KV-cache reduction during inference. Despite its adoption in massive production models, no prior work has studied what information this bottleneck preserves or discards, nor how it reshapes internal transformer circuits. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23054:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-head Latent Attention (MLA), introduced in DeepSeek-V2, compresses key-value pairs through a shared low-rank bottleneck (cKV), achieving 81% KV-cache reduction during inference.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present the first comprehensive mechanistic interpretability study of MLA, training a 114M-parameter transformer (pretrained on a web/code/math mixture, fine-tuned on TinyStories) and analyzing its representations through SVD, attention head taxonomy, linear probing, and a disruption-attribution analysis.

**证据证明什么。** We view this as an initial data point and detail scope limitations in Section 5.

**证据没有证明什么。** 5.4 Limitations We are explicit about the scope of what this study does and does not establish. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23054v1#S3.SS1 — 3.1 Model Architecture; https://arxiv.org/html/2607.23054v1#S5.SS3 — 5.3 Implications for MLA Design。Evaluation：https://arxiv.org/html/2607.23054v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.23054v1#S3.SS3 — 3.3 Experiments Overview。Limitations / counterevidence：https://arxiv.org/html/2607.23054v1#S5 — 5 Discussion; https://arxiv.org/html/2607.23054v1#S5.SS4 — 5.4 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Dhruvil-sr24/Small-Language-Model-From-Scratch/tree/main/interp, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：5.4 Limitations We are explicit about the scope of what this study does and does not establish.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-MULTI-HEAD-ATTENTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23054:end -->

<!-- review:SF-2026-ARXIV-2607-23055:start -->
### SymStep: Symbolic Step Verification for Logical Reasoning

<!-- claim:SF-2026-ARXIV-2607-23055:start -->Chain-of-thought (CoT) prompting can fail severely on constraint-dense logical reasoning tasks, where unverified errors accumulate silently across steps. We introduce SymStep: an LLM makes one atomic claim at a time (DEDUCE: Alice, pet, Cat), then a lightweight constraint propagator checks the claim for consistency with prior accepted deductions, rejects contradictions, and cascades implied facts automatically. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23055:end -->

**为什么进入候选分母。** 摘要首要问题为“Chain-of-thought (CoT) prompting can fail severely on constraint-dense logical reasoning tasks, where unverified errors accumulate silently across steps.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce SymStep: an LLM makes one atomic claim at a time (DEDUCE: Alice, pet, Cat), then a lightweight constraint propagator checks the claim for consistency with prior accepted deductions, rejects contradictions, and cascades implied facts automatically.

**证据证明什么。** On AR-LSAT analytical reasoning problems, SymStep achieves 100% vs.

**证据没有证明什么。** 8 Limitations and Future Work Scaling and model coverage. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23055v1#A9 — Appendix I System Prompts; https://arxiv.org/html/2607.23055v1#S4.SS2 — 4.2 Methods and Baselines。Evaluation：https://arxiv.org/html/2607.23055v1#A2 — Appendix B Cross-Model Results on LGP-10 (Sonnet); https://arxiv.org/html/2607.23055v1#A5 — Appendix E AQUA-RAT: Domain Boundary Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.23055v1#S8 — 8 Limitations and Future Work; https://arxiv.org/html/2607.23055v1#S6 — 6 Analysis and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/Zangir/SymStep, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：8 Limitations and Future Work Scaling and model coverage.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23055:end -->

<!-- review:SF-2026-ARXIV-2607-23089:start -->
### Compiler-Grounded Hierarchical Diagnosis for LLM-Based Triton Kernel Optimization

<!-- claim:SF-2026-ARXIV-2607-23089:start -->Recent advances in large language models (LLMs) have enabled automated kernel generation and optimization, but most existing approaches rely on surface signals such as compilation feedback and profiling metrics. These signals reveal that a kernel is slow, but not why the backend compiler fails to realize a profitable optimization, especially on emerging accelerators such as NPUs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23089:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in large language models (LLMs) have enabled automated kernel generation and optimization, but most existing approaches rely on surface signals such as compilation feedback and profiling metrics.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Based on this insight, we present our system, a compiler-grounded and hierarchical optimization framework for Triton kernels. the system escalates from lightweight pattern triage and profiling diagnosis to IR attribution and compiler-grounded analysis only when deeper evidence is needed, then proposes evidence-backed source-level rewrites.

**证据证明什么。** The complete distribution ranges from near-baseline entries to large wins, motivating transparent reporting of the current system's scope and limitations.

**证据没有证明什么。** The optimization accounting also shows why the workflow should not be summarized only by its final speedup table. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23089v1#S2.SS2 — 2.2 Limitations of Existing Approaches; https://arxiv.org/html/2607.23089v1#S3 — 3 System Overview。Evaluation：https://arxiv.org/html/2607.23089v1#S4.SS3 — 4.3 Compiler-Grounded Analysis; https://arxiv.org/html/2607.23089v1#S6 — 6 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.23089v1#S2.SS2 — 2.2 Limitations of Existing Approaches; https://arxiv.org/html/2607.23089v1#S8 — 8 Discussion。

**Artifact boundary。** Exact v1 links https://gitcode.com/cann/cannbot-skills, https://github.com/Ascend/triton-ascend-ops, https://github.com/flagos-ai/awesome-LLM-driven-kernel-generation; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The optimization accounting also shows why the workflow should not be summarized only by its final speedup table.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23089:end -->

<!-- review:SF-2026-ARXIV-2607-23099:start -->
### Decoding the Skew: Distribution-Aware MoE Inference with Adaptive Kernel Dispatch

<!-- claim:SF-2026-ARXIV-2607-23099:start -->Mixture-of-Experts (MoE) inference consists of sparse expert GEMMs whose shapes vary with the runtime routing distribution. Existing serving systems typically select fused-MoE kernels using static token-count buckets, ignoring the per-expert routing distribution that determines tile padding, memory reuse, and kernel efficiency. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23099:end -->

**为什么进入候选分母。** 摘要首要问题为“Mixture-of-Experts (MoE) inference consists of sparse expert GEMMs whose shapes vary with the runtime routing distribution.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We introduce a distribution-aware framework for modeling and benchmarking MoE inference.

**证据证明什么。** Using it, we show that the best fused-MoE kernel changes with routing skew and token count.

**证据没有证明什么。** VIII Conclusion This paper demonstrates that MoE inference performance depends not only on the token-count bucket, but also on the runtime routing distribution within each bucket. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23099v1#S2.SS2 — II-B NVIDIA GPU Microarchitecture; https://arxiv.org/html/2607.23099v1#S2.SS1 — II-A Mixture-of-Experts Models。Evaluation：https://arxiv.org/html/2607.23099v1#S3 — III Modeling and Benchmarking; https://arxiv.org/html/2607.23099v1#S5 — V Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.23099v1#S6 — VI Discussion & Architectural Implications; https://arxiv.org/html/2607.23099v1#S8 — VIII Conclusion。

**Artifact boundary。** Exact v1 links https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/hipgraph.html, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：VIII Conclusion This paper demonstrates that MoE inference performance depends not only on the token-count bucket, but also on the runtime routing distribution within each bucket.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23099:end -->

<!-- review:SF-2026-ARXIV-2607-23115:start -->
### Gleam: Adaptive Network-Efficient CUDA API Remoting for Cross-Device GPU Sharing over LANs

<!-- claim:SF-2026-ARXIV-2607-23115:start -->This paper aims to enable computation- and communication-efficient GPU sharing across devices within local area networks (LANs), facilitating ubiquitous AI inference on heterogeneous personal devices. We achieve distributed task offloading via CUDA API remoting. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23115:end -->

**为什么进入候选分母。** 摘要首要问题为“This paper aims to enable computation- and communication-efficient GPU sharing across devices within local area networks (LANs), facilitating ubiquitous AI inference on heterogeneous personal devices.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To address these challenges, we propose Gleam, a novel and network-efficient framework for task-generic GPU sharing across local-area CUDA devices, with three key contributions.

**证据证明什么。** Extensive experiments on heterogeneous NVIDIA GPUs and diverse AI workloads show Gleam consistently outperforms state-of-the-art baselines, achieving 1.4-24.2 times improvements in API remoting efficiency and up to 1.79 times higher system throughput.

**证据没有证明什么。** Our future work will extend to addressing the data security concerns during edge GPU sharing and developing general collaborative inference techniques with distributed edge GPUs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23115v1#S3 — 3 Framework Overview; https://arxiv.org/html/2607.23115v1#A1.SS1 — A.1 Implementation Details。Evaluation：https://arxiv.org/html/2607.23115v1#A1.SS2 — A.2 Experiment Supplement; https://arxiv.org/html/2607.23115v1#A1.SS3 — A.3 Analysis for Gleam Scheduling。Limitations / counterevidence：https://arxiv.org/html/2607.23115v1#A1.SS4 — A.4 Discussion; https://arxiv.org/html/2607.23115v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ggml-org/ggml, https://github.com/grpc/grpc.io, https://github.com/ggml-org/llama.cpp; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Our future work will extend to addressing the data security concerns during edge GPU sharing and developing general collaborative inference techniques with distributed edge GPUs.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23115:end -->

<!-- review:SF-2026-ARXIV-2607-23123:start -->
### SQBench: A Benchmark for Evaluating Task Delivery by Language-Model Agents in Production-Oriented Workflows

<!-- claim:SF-2026-ARXIV-2607-23123:start -->Existing evaluations of large language models cover knowledge, reasoning, coding, and tool use, but they rarely treat a verifiable deliverable produced within a constrained workflow as the unit of evaluation. We introduce SQBench, a benchmark for evaluating production-oriented task delivery by language-model agents. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23123:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing evaluations of large language models cover knowledge, reasoning, coding, and tool use, but they rarely treat a verifiable deliverable produced within a constrained workflow as the unit of evaluation.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce SQBench, a benchmark for evaluating production-oriented task delivery by language-model agents.

**证据证明什么。** These results show that functional completion alone does not fully characterize delivery quality and that risk determinations should be reported separately.

**证据没有证明什么。** We have not completed an independent validation of scoring validity. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23123v1#S3.SS1 — 3.1 Design principles; https://arxiv.org/html/2607.23123v1#A3 — Appendix C Model Invocation and Cost Records。Evaluation：https://arxiv.org/html/2607.23123v1#A5 — Appendix E Supplementary Results; https://arxiv.org/html/2607.23123v1#S1.SS1 — 1.1 Why existing evaluations do not fully capture production-oriented delivery。Limitations / counterevidence：https://arxiv.org/html/2607.23123v1#S6 — 6 Limitations; https://arxiv.org/html/2607.23123v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/shaqiu-ai/SQBench, https://github.com/shaqiu-ai/SQBench/releases/tag/v1.0-paper-20260720, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We have not completed an independent validation of scoring validity.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23123:end -->

<!-- review:SF-2026-ARXIV-2607-23147:start -->
### False Prophets: On the Security of World Models in Agentic Systems

<!-- claim:SF-2026-ARXIV-2607-23147:start -->Large language models now power autonomous agents capable of complex, multi-step tasks in different environments. Accurate and reliable execution of these tasks requires the agent to predict the results of its actions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23147:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models now power autonomous agents capable of complex, multi-step tasks in different environments.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In this paper, we raise security concerns regarding the usage of world models in agentic systems.

**证据证明什么。** Accurate and reliable execution of these tasks requires the agent to predict the results of its actions.

**证据没有证明什么。** Given that, we do not consider the proposed countermeasures to be exhaustive, and hope that our study is only the first step towards designing a new generation of reliable agents with planning capabilities. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23147v1#S2.SS1 — 2.1. World Models; https://arxiv.org/html/2607.23147v1#S2.SS2 — 2.2. World Models as Environment Simulators。Evaluation：https://arxiv.org/html/2607.23147v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.23147v1#S5.SS1 — 5.1. Experimental Setup.。Limitations / counterevidence：https://arxiv.org/html/2607.23147v1#S3.SS1 — 3.1. Threat Model; https://arxiv.org/html/2607.23147v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/mlsec-group/worldmodel-security, https://web.archive.org/web/20260716110416/https://opencode.ai/docs/zen/#pricing, https://huggingface.co/collections/XiaomiMiMo/mimo-v25; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Given that, we do not consider the proposed countermeasures to be exhaustive, and hope that our study is only the first step towards designing a new generation of reliable agents with planning capabilities.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23147:end -->

<!-- review:SF-2026-ARXIV-2607-23159:start -->
### CachedSearch: Training-Free Cached Exploration for Test-Time Search in Video Diffusion

<!-- claim:SF-2026-ARXIV-2607-23159:start -->Test-time search lets small video diffusion models rival larger ones, but costs 2-10x more. All candidates are fully denoised, although most are discarded. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23159:end -->

**为什么进入候选分母。** 摘要首要问题为“Test-time search lets small video diffusion models rival larger ones, but costs 2-10x more.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present the first study of whether caching corrupts candidate ranking in video test-time search.

**证据证明什么。** Ports to other model families require recalibrating a single parameter, showing that fidelity tracks architecture rather than parameter count.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23159v1#S3 — 3 Method; https://arxiv.org/html/2607.23159v1#S5.SS2 — 5.2 Ranking preservation across published caching methods。Evaluation：https://arxiv.org/html/2607.23159v1#S5 — 5 Analysis and Ablations; https://arxiv.org/html/2607.23159v1#A4 — Appendix D Additional Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.23159v1#A10 — Appendix J Limitations; https://arxiv.org/html/2607.23159v1#A7 — Appendix G Scaling discussion。

**Artifact boundary。** Exact v1 links https://github.com/shreshthsaini/CachedSearch, https://github.com/Wan-Video/Wan2.2, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23159:end -->

<!-- review:SF-2026-ARXIV-2607-23193:start -->
### OmniScope: Modality-Decoupled Token Compression for Omnimodal Large Language Models

<!-- claim:SF-2026-ARXIV-2607-23193:start -->Existing token compression methods for omnimodal large language models typically rely on one modality to determine what to retain in the other. We show that this assumption often breaks down: for the same query, audio and video relevance often peaks at different moments. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23193:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing token compression methods for omnimodal large language models typically rely on one modality to determine what to retain in the other.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose OmniScope, a training-free token compression framework that uses the query as a shared semantic anchor while estimating relevance separately for audio and video.

**证据证明什么。** We show that this assumption often breaks down: for the same query, audio and video relevance often peaks at different moments.

**证据没有证明什么。** However, these methods target purely visual settings and cannot directly address the joint compression of audio and video tokens. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.23193v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23193v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.23193v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23193v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.23193v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23193v1#page=10 — PDF page 10。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：However, these methods target purely visual settings and cannot directly address the joint compression of audio and video tokens.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23193:end -->

<!-- review:SF-2026-ARXIV-2607-23226:start -->
### From Score Learning to Discretized Sampling: An End-to-End Generalization Analysis of Diffusion Models

<!-- claim:SF-2026-ARXIV-2607-23226:start -->Despite the empirical success of score-based diffusion models, a complete theoretical understanding of how finite-sample learning, network parameterization, and numerical discretization jointly dictate generative quality remains underdeveloped. Existing sampling analyses often evaluate the generative performance conditional on an oracle score or a pre-specified error threshold. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23226:end -->

**为什么进入候选分母。** 摘要首要问题为“Despite the empirical success of score-based diffusion models, a complete theoretical understanding of how finite-sample learning, network parameterization, and numerical discretization jointly dictate generative quality remains underdeveloped.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this work, we establish a unified convergence and generalization framework for score-based diffusion models parameterized by practical ResNet-type architectures.

**证据证明什么。** Our results quantitatively characterize how the training sample size, temporal discretization grids, and optimization accuracy jointly control the final fidelity of samples generated by diffusion models.

**证据没有证明什么。** We leave the rigorous characterization of these non-convex training dynamics and the explicit bounding of the optimization error as an important direction for future research. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23226v1#S2.SS1 — 2.1 Sampling Theory for Diffusion Models; https://arxiv.org/html/2607.23226v1#S3 — 3 Score-based diffusion models。Evaluation：https://arxiv.org/html/2607.23226v1#S4 — 4 Main results: Generalization and convergence properties of SDMs; https://arxiv.org/html/2607.23226v1#S4.SS1 — 4.1 Assumptions and preliminary results。Limitations / counterevidence：https://arxiv.org/html/2607.23226v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：We leave the rigorous characterization of these non-convex training dynamics and the explicit bounding of the optimization error as an important direction for future research.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23226:end -->

<!-- review:SF-2026-ARXIV-2607-23250:start -->
### Libra: Taming Attention Workload Skew in Long-Context LLM Training with Bounded Sequence Pool

<!-- claim:SF-2026-ARXIV-2607-23250:start -->Long-context LLM training suffers from a load-balancing problem that sequence packing does not solve. Packing samples into fixed-token sequences balances memory and linear-cost operators, but the dominant attention cost scales with the sum of squared sequence lengths. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23250:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-context LLM training suffers from a load-balancing problem that sequence packing does not solve.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present Libra, which operationalizes the law of large numbers (LLN) as a scaling principle for load balancing: the attention-balancing pool need not grow with the DP degree.

**证据证明什么。** Variance-Reduced Sequence Placement makes this effective for finite, long-tailed workloads by co-locating sequences with complementary attention workloads to reduce residual inter-pool skew.

**证据没有证明什么。** Specifically, Libra presents three innovations to address attention FLOPs imbalance: 1) using the law of large numbers as a scaling principle so that the sequence-pool size need not grow with the DP degree, 2) introducing Variance-Reduced Sequence Placement to balance the sequence-pool instances formed in each optimizer-step window, and 3) developing Tiled Attention Pooling to balance sequence head SH-Tiles within each pool, together with the TAP Pipeliner to overlap the resulting tensor movement with attention computation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23250v1#S4 — 4. Design; https://arxiv.org/html/2607.23250v1#S5 — 5. Implementation。Evaluation：https://arxiv.org/html/2607.23250v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.23250v1#S6.SS1 — 6.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.23250v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/SandAI-org/MagiAttention/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Specifically, Libra presents three innovations to address attention FLOPs imbalance: 1) using the law of large numbers as a scaling principle so that the sequence-pool size need not grow with the DP degree, 2) introducing Variance-Reduced Sequence Placement to balance the sequence-pool instances formed in each optimizer-step window, and 3) developing Tiled Attention Pooling to balance sequence head SH-Tiles within each pool, together with the TAP Pipeliner to overlap the resulting tensor movement with attention computation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23250:end -->

<!-- review:SF-2026-ARXIV-2607-23263:start -->
### SeekJudge: A Practical Reward Framework for Reinforcement Learning in Computer-Use Agents

<!-- claim:SF-2026-ARXIV-2607-23263:start -->Deciding whether a trajectory actually fulfills its instruction governs how we measure computer-use agents on long-horizon graphical-user-interface tasks and how we train them with reinforcement learning. This judgment has long relied on rule-based evaluation, which struggles to align with human intention and goes stale when an app updates or its online content drifts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23263:end -->

**为什么进入候选分母。** 摘要首要问题为“Deciding whether a trajectory actually fulfills its instruction governs how we measure computer-use agents on long-horizon graphical-user-interface tasks and how we train them with reinforcement learning.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose the \textbf{SeekJudge} framework, in which four role-specialized agents, a Condense, a Ground, a Seek and an Analyze agent, reach a verdict through a Seek--Analyze loop over the trajectory.

**证据证明什么。** We further contribute a general architectural improvement to the reward server that speeds up judging in RL.

**证据没有证明什么。** Together with CUAStepBench and the rollout-overlapped reward server, these results make model-based reward a practical substitute for rules and extend reinforcement learning for computer-use agents to environments that rules cannot instrument. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23263v1#S3 — 3 Method; https://arxiv.org/html/2607.23263v1#S3.SS1 — 3.1 The SeekJudge Framework。Evaluation：https://arxiv.org/html/2607.23263v1#S4.SS4 — 4.4 Offline Reward Benchmark Evaluation; https://arxiv.org/html/2607.23263v1#S2.SS2 — 2.2 From Rule-Based to Model-Based Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.23263v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/McGill-NLP/agent-reward-bench/issues/9, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Together with CUAStepBench and the rollout-overlapped reward server, these results make model-based reward a practical substitute for rules and extend reinforcement learning for computer-use agents to environments that rules cannot instrument.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23263:end -->

<!-- review:SF-2026-ARXIV-2607-23264:start -->
### X-Stage: An Overlooked Pipeline Stage for Communication-Computation Overlap in DiT Inference

<!-- claim:SF-2026-ARXIV-2607-23264:start -->Fine-grained, device-initiated communication lets persistent GPU kernels in distributed diffusion transformer (DiT) inference issue remote stores and overlap data movement with Tensor Core computation. Existing systems schedule when communication is issued and when received data becomes consumable, but omit post-issue progress before remote-visible completion, making sender backpressure hard to predict. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23264:end -->

**为什么进入候选分母。** 摘要首要问题为“Fine-grained, device-initiated communication lets persistent GPU kernels in distributed diffusion transformer (DiT) inference issue remote stores and overlap data movement with Tensor Core computation.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Existing systems schedule when communication is issued and when received data becomes consumable, but omit post-issue progress before remote-visible completion, making sender backpressure hard to predict.

**证据证明什么。** These results establish post-issue progress as a measurable scheduling lever for shaping bursts, avoiding backpressure, and hiding sender-side overhead.

**证据没有证明什么。** X-Stage complements tile dependencies and remote-readiness protocols by exposing a missing scheduling dimension: the rate and capacity of accepted but not yet completed remote stores. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23264v1#S4 — 4. X-Stage-Aware Kernel Design; https://arxiv.org/html/2607.23264v1#S4.SS1 — 4.1. A Design Test with Two Actions。Evaluation：https://arxiv.org/html/2607.23264v1#S3.SS1 — 3.1. Remote-Store Microbenchmarks; https://arxiv.org/html/2607.23264v1#S5 — 5. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.23264v1#S6 — 6. Discussion and Limitations; https://arxiv.org/html/2607.23264v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/deepseek-ai/EPLB, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：X-Stage complements tile dependencies and remote-readiness protocols by exposing a missing scheduling dimension: the rate and capacity of accepted but not yet completed remote stores.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23264:end -->

<!-- review:SF-2026-ARXIV-2607-23265:start -->
### WaveZip: Wavelet-Driven Space-Time Decoupling for Video Token Condensation

<!-- claim:SF-2026-ARXIV-2607-23265:start -->Existing Large Vision-Language Models (LVLMs) struggle with long-form video understanding due to the quadratic computational cost of visual tokens. While recent efficient methods attempt to compress tokens via hard pruning or uniform merging, they operate strictly in the spatial feature domain, where robust structural context and discriminative semantic details are inherently entangled. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23265:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing Large Vision-Language Models (LVLMs) struggle with long-form video understanding due to the quadratic computational cost of visual tokens.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this work, we propose WaveZip, a joint signal-frequency-domain framework for efficient video inference.

**证据证明什么。** Extensive experiments on long video understanding benchmarks demonstrate that WaveZip retains 99.6% of the full performance under an extreme 10x compression ratio, consistently outperforming state-of-the-art methods.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23265v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.23265v1#A1 — Appendix A Supplemental Experimental Protocol; https://arxiv.org/html/2607.23265v1#A2 — Appendix B Controlled Wavelet Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.23265v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23265:end -->

<!-- review:SF-2026-ARXIV-2607-23332:start -->
### AllocBench: Measuring Online Tool Allocation Capability in LLM Agents

<!-- claim:SF-2026-ARXIV-2607-23332:start -->Creating a reusable tool is an investment: an agent pays a fixed cost now in exchange for the potential of future reuse. Therefore, a user should prefer an agent that creates a small number of highly reusable tools, rather than many one-offs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23332:end -->

**为什么进入候选分母。** 摘要首要问题为“Creating a reusable tool is an investment: an agent pays a fixed cost now in exchange for the potential of future reuse.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce a paired benchmark that tests whether LLM agents exhibit conscious allocation behavior under a fixed budget in two contexts: an abstract text-based formulation and a code-construction task.

**证据证明什么。** Together, these results establish online tool allocation as a significant capability boundary, even for modern frontier models.

**证据没有证明什么。** Let me use it for this LCG type which may recur. ) The models do not consider waiting for recurrence evidence at all, and scripts are reused only reactively when a class later returns. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23332v1#A2.SS4 — B.4 Models and generation settings; https://arxiv.org/html/2607.23332v1#A4 — Appendix D Supplementary Frontier-Model Results。Evaluation：https://arxiv.org/html/2607.23332v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.23332v1#A1 — Appendix A Benchmark Theory and Preregistration。Limitations / counterevidence：https://arxiv.org/html/2607.23332v1#S4.SS1 — 4.1 Abstract competence but tool-budgeting failure; https://arxiv.org/html/2607.23332v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/DragonWrangler25/AlloBench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Let me use it for this LCG type which may recur. ) The models do not consider waiting for recurrence evidence at all, and scripts are reused only reactively when a class later returns.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23332:end -->

<!-- review:SF-2026-ARXIV-2607-23361:start -->
### Hallucination Rates in Language Generation

<!-- claim:SF-2026-ARXIV-2607-23361:start -->Language generation in the limit is an elegant model introduced by Kleinberg and Mullainathan [KM24] to formally study language generation by an algorithm that learns solely based on example strings. In this model, an algorithm is said to correctly generate from a language if it never makes an error after some finite time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23361:end -->

**为什么进入候选分母。** 摘要首要问题为“Language generation in the limit is an elegant model introduced by Kleinberg and Mullainathan [KM24] to formally study language generation by an algorithm that learns solely based on example strings.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this model, an algorithm is said to correctly generate from a language if it never makes an error after some finite time.

**证据证明什么。** Once again, we demonstrate a strict hierarchy at every hallucination rate and breadth.

**证据没有证明什么。** There exists a collection that is generatable in the limit with finite error and upper density , but it cannot be -generated with upper density strictly greater than even with arbitrary . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23361v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23361v1#S1.SS1 — 1.1 Related Work。Evaluation：https://arxiv.org/html/2607.23361v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23361v1#S1.SS1 — 1.1 Related Work。Limitations / counterevidence：https://arxiv.org/html/2607.23361v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23361v1#S1.SS1 — 1.1 Related Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：There exists a collection that is generatable in the limit with finite error and upper density , but it cannot be -generated with upper density strictly greater than even with arbitrary .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23361:end -->

<!-- review:SF-2026-ARXIV-2607-23364:start -->
### On the Impossibility of Unbiased and Length-Invariant Policy Optimization with Outcome Rewards

<!-- claim:SF-2026-ARXIV-2607-23364:start -->Group Relative Policy Optimization (GRPO) is the dominant reinforcement learning algorithm for training reasoning capabilities in large language models, notably adopted by DeepSeek-R1. GRPO (COLM 2025) identifies the response-level length bias caused by per-trajectory length normalization in GRPO and proposes removing this normalization, claiming the resulting optimizer is "unbiased." We show that this claim is incomplete. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23364:end -->

**为什么进入候选分母。** 摘要首要问题为“Group Relative Policy Optimization (GRPO) is the dominant reinforcement learning algorithm for training reasoning capabilities in large language models, notably adopted by DeepSeek-R1.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** GRPO (COLM 2025) identifies the response-level length bias caused by per-trajectory length normalization in GRPO and proposes removing this normalization, claiming the resulting optimizer is "unbiased." We show that this claim is incomplete.

**证据证明什么。** GRPO, and provide quantitative analysis showing that Dr.

**证据没有证明什么。** 6 Conclusion We have established a fundamental impossibility result for group-based policy optimization under outcome rewards: gradient unbiasedness and length invariance cannot coexist. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23364v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23364v1#S2 — 2 Preliminaries。Evaluation：https://arxiv.org/html/2607.23364v1#S3 — 3 Main Result: Impossibility Theorem; https://arxiv.org/html/2607.23364v1#S4 — 4 Corollaries and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.23364v1#S5 — 5 Discussion; https://arxiv.org/html/2607.23364v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：6 Conclusion We have established a fundamental impossibility result for group-based policy optimization under outcome rewards: gradient unbiasedness and length invariance cannot coexist.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23364:end -->

<!-- review:SF-2026-ARXIV-2607-23366:start -->
### Codebook Capacity Governs Perceptual Quality Across Resolutions in Hierarchical Discrete Video Compression

<!-- claim:SF-2026-ARXIV-2607-23366:start -->Learned video codecs based on continuous latent representations typically require resolution-specific retraining or rate-distortion (RD) recalibration when scaling to new spatial resolutions, because entropy models and Lagrangian weights are tightly coupled to the operating point. We investigate whether hierarchical discrete latent codecs exhibit the same sensitivity. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23366:end -->

**为什么进入候选分母。** 摘要首要问题为“Learned video codecs based on continuous latent representations typically require resolution-specific retraining or rate-distortion (RD) recalibration when scaling to new spatial resolutions, because entropy models and Lagrangian weights are tightly coupled to the operating point.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We investigate whether hierarchical discrete latent codecs exhibit the same sensitivity.

**证据证明什么。** Across all resolutions and codebook sizes, our models outperform H.264 on LPIPS at matched or lower bitrate, with gains of 25-52% at $128\times128$ and 21-37% over H.265 at $256\times256$.

**证据没有证明什么。** Our central finding is that perceptual quality (LPIPS) depends strongly and significantly on codebook capacity ( , ) while exhibiting negligible and statistically insignificant dependence on spatial resolution ( , ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23366v1#A1 — Appendix A Architecture Hyperparameters; https://arxiv.org/html/2607.23366v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.23366v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.23366v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.23366v1#S6 — 6 Discussion; https://arxiv.org/html/2607.23366v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Our central finding is that perceptual quality (LPIPS) depends strongly and significantly on codebook capacity ( , ) while exhibiting negligible and statistically insignificant dependence on spatial resolution ( , ).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23366:end -->

<!-- review:SF-2026-ARXIV-2607-23373:start -->
### UltraViT: Latency-Optimized On-device Vision Encoder for Large Vision-Language Models

<!-- claim:SF-2026-ARXIV-2607-23373:start -->Large Vision-Language Models (LVLMs) remain bottlenecked by massive computational footprints, precluding their deployment on resource-constrained edge devices. While efforts to compress LVLMs focus heavily on vision token reduction or smaller language models, the vision encoder is largely overlooked, typically deployed as a monolithic, computationally heavy feature extractor. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23373:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Vision-Language Models (LVLMs) remain bottlenecked by massive computational footprints, precluding their deployment on resource-constrained edge devices.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we present UltraViT, a vision encoder for LVLMs, explicitly designed and optimized for on-device performance.

**证据证明什么。** Extensive experiments demonstrate that our on-device latency-informed design combined with our tailored training strategy establishes a new state-of-the-art for efficient LVLM encoding, significantly outperforming existing encoder-centric baselines while operating on-device at nearly 1.7xthe speed.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23373v1#Pt0.A2.SS4 — 0.B.4 On-device measurements methodology; https://arxiv.org/html/2607.23373v1#S3 — 3 Architecture optimization。Evaluation：https://arxiv.org/html/2607.23373v1#Pt0.A2 — Appendix 0.B Additional Experiments; https://arxiv.org/html/2607.23373v1#Pt0.A2.SS1 — 0.B.1 Extended OCR retrieval results。Limitations / counterevidence：https://arxiv.org/html/2607.23373v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/google/siglip2-base-patch16-naflex, https://huggingface.co/google/siglip2-so400m-patch16-512, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23373:end -->

<!-- review:SF-2026-ARXIV-2607-23379:start -->
### When Activation Oracles Learn Not to Read: Concept-Specific Blind Spots in Fine-Tuned Oracles

<!-- claim:SF-2026-ARXIV-2607-23379:start -->Activation Oracles (AOs) are language models trained to answer natural-language questions about another model's internal activations. They offer a flexible interface for reading hidden information from model states, especially when relevant information is internally represented but absent or incomplete in visible behavior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23379:end -->

**为什么进入候选分母。** 摘要首要问题为“Activation Oracles (AOs) are language models trained to answer natural-language questions about another model's internal activations.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** However, AOs are themselves learned systems: their answers are shaped by training data, objectives, and learned reporting behavior, rather than being neutral readouts of represented information.

**证据证明什么。** Our results show that behavioral leakage, representation-level decodability, and AO-verbalizability can come apart, raising a reliability concern for learned interpretability interfaces.

**证据没有证明什么。** Future work on activation-reading tools should therefore evaluate not only whether hidden information is represented, but whether the reader has learned to report it. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23379v1#A2 — Appendix B Subject Model and Activation Oracle Training; https://arxiv.org/html/2607.23379v1#S4.SS1 — 4.1 Subject models and Taboo fine-tuning。Evaluation：https://arxiv.org/html/2607.23379v1#A10.SS1 — J.1 Detailed behavioural evaluation results; https://arxiv.org/html/2607.23379v1#A10 — Appendix J Detailed Results。Limitations / counterevidence：https://arxiv.org/html/2607.23379v1#A1 — Appendix A Limitations and Future Work; https://arxiv.org/html/2607.23379v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work on activation-reading tools should therefore evaluate not only whether hidden information is represented, but whether the reader has learned to report it.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23379:end -->

<!-- review:SF-2026-ARXIV-2607-23386:start -->
### Confidently Wrong: Exception Chain Collapse in Frontier LLM Rule Evaluation

<!-- claim:SF-2026-ARXIV-2607-23386:start -->We document a failure class in frontier large language models -- exception chain collapse -- observed in eligibility evaluation under nested conditional rules of the form "A is required UNLESS B applies, UNLESS C overrides B". The failure reproduces at first observation, but its empirical surface is unstable: between March and April 2026 several failure cells closed silently under the same model alias, with no version bump (GPT-5.4 on construction insurance moved from 96.6% to 100%, same prompt and harness). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23386:end -->

**为什么进入候选分母。** 摘要首要问题为“We document a failure class in frontier large language models -- exception chain collapse -- observed in eligibility evaluation under nested conditional rules of the form "A is required UNLESS B applies, UNLESS C overrides B".”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present the Aethis Eligibility Module, a neuro-symbolic architecture in which LLMs author rules from authoritative sources and an SMT-based layer executes them deterministically, consistent with the authored specification regardless of model drift, reasoning-effort defaults, or prompt format.

**证据证明什么。** All scenarios, rule encodings, and results are public and reproducible.

**证据没有证明什么。** Independent human review of generated rules against authoritative legal interpretations has not been performed. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23386v1#Sx3.SSx5 — 3.5 Neuro-Symbolic Architectures and LLM + Formal Method Hybrids; https://arxiv.org/html/2607.23386v1#Sx13 — Technical Appendix A: Benchmark Methodology。Evaluation：https://arxiv.org/html/2607.23386v1#Sx13 — Technical Appendix A: Benchmark Methodology; https://arxiv.org/html/2607.23386v1#Sx3.SSx2 — 3.2 LLM Benchmarks for Legal and Logical Reasoning。Limitations / counterevidence：https://arxiv.org/html/2607.23386v1#Sx10 — 10. Limitations and Future Work; https://arxiv.org/html/2607.23386v1#Sx10.SSx1 — 10.1 Current Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Aethis-ai/confidently-wrong-benchmark, https://github.com/Aethis-ai/confidently-wrong-benchmark/tree/main/legalbench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Independent human review of generated rules against authoritative legal interpretations has not been performed.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23386:end -->

<!-- review:SF-2026-ARXIV-2607-23390:start -->
### When Can Depth Replace Precision? A Resource Theory of Quantized Neural Computation

<!-- claim:SF-2026-ARXIV-2607-23390:start -->When can additional low-bit residual computation replace missing numerical precision for a fixed input-output map? We model a quantized residual system over a fixed horizon as a pure schedule selecting fields from a declared low-bit operation library, and use relaxed controls to characterize its infinite-depth limit. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23390:end -->

**为什么进入候选分母。** 摘要首要问题为“When can additional low-bit residual computation replace missing numerical precision for a fixed input-output map?”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We model a quantized residual system over a fixed horizon as a pure schedule selecting fields from a declared low-bit operation library, and use relaxed controls to characterize its infinite-depth limit.

**证据证明什么。** Depth replaces precision only relative to a declared library, horizon, execution semantics, and routing model.

**证据没有证明什么。** 13 Conclusion Depth can replace missing numerical precision, but only in a specific sense and only under identifiable conditions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23390v1#A1.SS6 — A.6 Architecture specialization: Transformer and routed-MoE execution; https://arxiv.org/html/2607.23390v1#A5 — Appendix E Rational Certificate Methodology for the Matrix-Valued Example。Evaluation：https://arxiv.org/html/2607.23390v1#A6 — Appendix F Additional Experimental and Search Details; https://arxiv.org/html/2607.23390v1#A8 — Appendix H Pretrained DistilBERT Study。Limitations / counterevidence：https://arxiv.org/html/2607.23390v1#S12 — 12 Discussion and Limitations; https://arxiv.org/html/2607.23390v1#S13 — 13 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：13 Conclusion Depth can replace missing numerical precision, but only in a specific sense and only under identifiable conditions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23390:end -->

<!-- review:SF-2026-ARXIV-2607-23394:start -->
### Inference-Time Consensus for Mitigating Hidden Behaviors from LLM Fine-Tuning

<!-- claim:SF-2026-ARXIV-2607-23394:start -->Recent work shows that fine-tuning language models on even a small amount of poisoned data can install targeted misbehavior, and ostensibly benign data can transmit hidden preferences that generalize broadly. Standard defenses, such as data filtering, mixing in harmless data, and regularization, attenuate these effects but do not eliminate them. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23394:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent work shows that fine-tuning language models on even a small amount of poisoned data can install targeted misbehavior, and ostensibly benign data can transmit hidden preferences that generalize broadly.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce two consensus decoders: a token-wise minimum, which caps each token at the lowest probability any source assigns, and a base-relative variant, which reverts to the base probability on any token the sources move in opposing directions.

**证据证明什么。** Recent work shows that fine-tuning language models on even a small amount of poisoned data can install targeted misbehavior, and ostensibly benign data can transmit hidden preferences that generalize broadly.

**证据没有证明什么。** Below, we discuss limitations of the current results, and exciting directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23394v1#S3 — 3 Method; https://arxiv.org/html/2607.23394v1#A4 — Appendix D Setting 1 pilot with eight reference models。Evaluation：https://arxiv.org/html/2607.23394v1#A5 — Appendix E Experimental details; https://arxiv.org/html/2607.23394v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.23394v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/AdhyyanNarang/consensus-aggregation, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Below, we discuss limitations of the current results, and exciting directions for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23394:end -->

<!-- review:SF-2026-ARXIV-2607-23402:start -->
### Characterizing Warp Divergence from Pascal to Blackwell

<!-- claim:SF-2026-ARXIV-2607-23402:start -->Since Volta introduced Independent Thread Scheduling (ITS), NVIDIA GPUs have been widely assumed to handle warp divergence in a fixed manner. We test this assumption across Ampere, Hopper, and datacenter and consumer Blackwell GPUs, using pre-ITS Pascal as a baseline. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23402:end -->

**为什么进入候选分母。** 摘要首要问题为“Since Volta introduced Independent Thread Scheduling (ITS), NVIDIA GPUs have been widely assumed to handle warp divergence in a fixed manner.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We test this assumption across Ampere, Hopper, and datacenter and consumer Blackwell GPUs, using pre-ITS Pascal as a baseline.

**证据证明什么。** The same behavior appears on Pascal, showing that this programmer-visible cost model predates ITS.

**证据没有证明什么。** VIII Conclusion We asked whether Independent Thread Scheduling has stood still since Volta. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23402v1#S1 — I Introduction; https://arxiv.org/html/2607.23402v1#S2 — II Background。Evaluation：https://arxiv.org/html/2607.23402v1#S3 — III Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.23402v1#S6 — VI Discussion; https://arxiv.org/html/2607.23402v1#S8 — VIII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：VIII Conclusion We asked whether Independent Thread Scheduling has stood still since Volta.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23402:end -->

<!-- review:SF-2026-ARXIV-2607-23425:start -->
### TLA+-Bench: An Execution-Grounded Benchmark and Dataset for Natural-Language to TLA Specification Generation

<!-- claim:SF-2026-ARXIV-2607-23425:start -->Large language models increasingly write TLA$^{+}$ formal specifications from natural-language descriptions, but progress is hard to measure: existing resources grade by resemblance to a reference or by whether the output parses, neither of which shows correctness. We present TLA$^{+}$-Bench, a dataset and benchmark that grades by execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23425:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models increasingly write TLA$^{+}$ formal specifications from natural-language descriptions, but progress is hard to measure: existing resources grade by resemblance to a reference or by whether the output parses, neither of which shows correctness.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present TLA$^{+}$-Bench, a dataset and benchmark that grades by execution.

**证据证明什么。** Large language models increasingly write TLA$^{+}$ formal specifications from natural-language descriptions, but progress is hard to measure: existing resources grade by resemblance to a reference or by whether the output parses, neither of which shows correctness.

**证据没有证明什么。** Reference-mutation grading would extend the pass-quality probes by perturbing the reference and requiring the checker to detect the change, crediting correctness only to specifications that constrain behavior against an independently varied ground truth ( Beer et al., 2001 ; Ye et al., 2026 ) , lifting the restriction that makes our mutation test a lower bound. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23425v1#A11 — Appendix A11 Exact Prompts Given to the Language Models; https://arxiv.org/html/2607.23425v1#S2.SS1 — 2.1. TLA + and Model Checking。Evaluation：https://arxiv.org/html/2607.23425v1#A3 — Appendix A3 A Benchmark Instance; https://arxiv.org/html/2607.23425v1#S2.SS2 — 2.2. Specification and Code Generation Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.23425v1#A6 — Appendix A6 A Worked Failure in Full; https://arxiv.org/html/2607.23425v1#S10 — 10. Future Work。

**Artifact boundary。** Exact v1 links https://github.com/LUC-AI4FM/tla_benchmark/tree/reviewer-release, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Reference-mutation grading would extend the pass-quality probes by perturbing the reference and requiring the checker to detect the change, crediting correctness only to specifications that constrain behavior against an independently varied ground truth ( Beer et al., 2001 ; Ye et al., 2026 ) , lifting the restriction that makes our mutation test a lower bound.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23425:end -->

<!-- review:SF-2026-ARXIV-2607-23438:start -->
### Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels

<!-- claim:SF-2026-ARXIV-2607-23438:start -->As AI systems increasingly exhibit agentic behavior, discussions of autonomy often conflate what systems are technically capable of doing with what they should be permitted to do in practice. This paper introduces a governance framework that explicitly separates Allowed Autonomy Levels (AAL), which define the degree of autonomy an AI agent is authorized to exercise given risk, oversight, and accountability considerations, from Autonomous Capability Levels (ACL), which characterize an agent's inherent technical abilities. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23438:end -->

**为什么进入候选分母。** 摘要首要问题为“As AI systems increasingly exhibit agentic behavior, discussions of autonomy often conflate what systems are technically capable of doing with what they should be permitted to do in practice.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To operationalize this framework, we propose a risk-aware decision process for assigning allowed autonomy, analyze how risk and accountability evolve across autonomy levels, and demonstrate its application through a deployed enterprise data engineering agent, illustrating how a system assessed at a high capability level can be deliberately constrained to a lower allowed autonomy based on risk, reversibility, and organizational readiness.

**证据证明什么。** To operationalize this framework, we propose a risk-aware decision process for assigning allowed autonomy, analyze how risk and accountability evolve across autonomy levels, and demonstrate its application through a deployed enterprise data engineering agent, illustrating how a system assessed at a high capability level can be deliberately constrained to a lower allowed autonomy based on risk, reversibility, and organizational readiness.

**证据没有证明什么。** However, existing work on auton-omy classification for AI systems remains limited, in part because such distinctions were not practically necessary un-til recently. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.23438v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23438v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.23438v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23438v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.23438v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.23438v1#page=10 — PDF page 10。

**Artifact boundary。** Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：However, existing work on auton-omy classification for AI systems remains limited, in part because such distinctions were not practically necessary un-til recently.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23438:end -->

<!-- review:SF-2026-ARXIV-2607-23444:start -->
### Isolated but Exposed: Persistence-Based Memory Extraction Attack on LLM Agents

<!-- claim:SF-2026-ARXIV-2607-23444:start -->LLM-based agents extend large language models with long-term memory (LTM) that persists privacy-sensitive user data across sessions. Production systems mitigate extraction risks through memory isolation, binding each user's LTM to a unique identifier. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23444:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based agents extend large language models with long-term memory (LTM) that persists privacy-sensitive user data across sessions.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present SPORE, the first extraction attack designed for this threat model.

**证据证明什么。** These results demonstrate that memory isolation alone is insufficient and call for reexamining tool-side trust boundaries in agent architectures.

**证据没有证明什么。** This setting approximates the unlimited-query assumption adopted in prior user-side extraction attacks and serves as an upper-bound baseline. • Sparse Triggering with Session Continuity (Scenario 2): The malicious tool is triggered only occasionally, potentially only once. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23444v1#A6 — Appendix F LTM framework; https://arxiv.org/html/2607.23444v1#S2.SS2 — 2.2 Data Extraction against RAG-Based Systems。Evaluation：https://arxiv.org/html/2607.23444v1#A7 — Appendix G Experimental Result; https://arxiv.org/html/2607.23444v1#S5.SS2 — 5.2 Experimental Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.23444v1#S3.SS1 — 3.1 Threat Model; https://arxiv.org/html/2607.23444v1#S8 — 8 Discussion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/wangrongsheng/HealthCareMagic-100k-en, https://github.com/snap-research/LoCoMo, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：This setting approximates the unlimited-query assumption adopted in prior user-side extraction attacks and serves as an upper-bound baseline. • Sparse Triggering with Session Continuity (Scenario 2): The malicious tool is triggered only occasionally, potentially only once.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23444:end -->

<!-- review:SF-2026-ARXIV-2607-23445:start -->
### Omni-Prune: Query-Aware Unified Token Pruning for Efficient Omnimodal Large Language Models

<!-- claim:SF-2026-ARXIV-2607-23445:start -->Omnimodal large language models (OmniLLMs) are rapidly extending multimodal reasoning to cover synchronized audio and video. However, the resulting audio-video token sequences are long, leading to high prefill latency and GPU memory usage at inference time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23445:end -->

**为什么进入候选分母。** 摘要首要问题为“Omnimodal large language models (OmniLLMs) are rapidly extending multimodal reasoning to cover synchronized audio and video.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To bridge this gap, we present Omni-Prune, a training-free, query-aware audio-visual token pruning framework that jointly removes redundancy from both modalities while keeping task-relevant cross-modal evidence.

**证据证明什么。** Extensive experiments demonstrate that Omni-Prune outperforms established baseline methods, delivering up to 3.25x prefill speedup and 1.3x memory reduction while retaining over 99% of full-model performance.

**证据没有证明什么。** Notably, our method achieves significant memory reduction and prefill speedup while maintaining comparable accuracy. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23445v1#S3 — 3 Method; https://arxiv.org/html/2607.23445v1#A3 — Appendix C Notation and Implementation Details。Evaluation：https://arxiv.org/html/2607.23445v1#A1 — Appendix A More Experimental Results; https://arxiv.org/html/2607.23445v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.23445v1#A6 — Appendix F Discussion; https://arxiv.org/html/2607.23445v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/kimberlyii/Omni-Prune, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Notably, our method achieves significant memory reduction and prefill speedup while maintaining comparable accuracy.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23445:end -->

<!-- review:SF-2026-ARXIV-2607-23458:start -->
### Two Regimes of Chain-of-Thought Unfaithfulness: Metric-Based Detection Fails Where Models Are Wrong

<!-- claim:SF-2026-ARXIV-2607-23458:start -->Chain-of-thought (CoT) explanations support oversight only if they are faithful: the stated reasoning must actually produce the answer. Auditing black-box (behavioral) detection of unfaithful CoT against FaithCoT-Bench's human annotations, we find answer correctness structures the problem at every level. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23458:end -->

**为什么进入候选分母。** 摘要首要问题为“Chain-of-thought (CoT) explanations support oversight only if they are faithful: the stated reasoning must actually produce the answer.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Auditing black-box (behavioral) detection of unfaithful CoT against FaithCoT-Bench's human annotations, we find answer correctness structures the problem at every level.

**证据证明什么。** Auditing black-box (behavioral) detection of unfaithful CoT against FaithCoT-Bench's human annotations, we find answer correctness structures the problem at every level.

**证据没有证明什么。** 9 Limitations Our annotated-label results rest on one human-annotated benchmark (FaithCoT-Bench; regimes / , per-model minority classes as small as ft4 ); to our knowledge it is the only instance-level faithfulness benchmark with expert annotations, which is itself part of the problem we highlight (the counterfactual hint testbeds provide partial independent corroboration: the inversion and decodability replicate there); its label semantics required verification against the raw data (§ 3 ), and our regime findings inherit whatever noise remains in the annotations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23458v1#S7.SS1 — 7.1 Instructed construction: 7 models。Evaluation：https://arxiv.org/html/2607.23458v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23458v1#S2 — 2 Related Work。Limitations / counterevidence：https://arxiv.org/html/2607.23458v1#S8 — 8 Discussion; https://arxiv.org/html/2607.23458v1#S9 — 9 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：9 Limitations Our annotated-label results rest on one human-annotated benchmark (FaithCoT-Bench; regimes / , per-model minority classes as small as ft4 ); to our knowledge it is the only instance-level faithfulness benchmark with expert annotations, which is itself part of the problem we highlight (the counterfactual hint testbeds provide partial independent corroboration: the inversion and decodability replicate there); its label semantics required verification against the raw data (§ 3 ), and our regime findings inherit whatever noise remains in the annotations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23458:end -->

<!-- review:SF-2026-ARXIV-2607-23472:start -->
### VIPER: Visual In-Context Physics Reasoning for Physically Plausible Video Generation

<!-- claim:SF-2026-ARXIV-2607-23472:start -->Modern video generation models can synthesize visually compelling and temporally coherent clips, yet controlling their physical behavior remains difficult with standard text and image conditions. The core challenge is a conditioning bottleneck: material response, contact interaction, deformation, and motion trajectory are continuous and relational physical cues that are hard to specify exhaustively in language but can be demonstrated naturally by video. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23472:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern video generation models can synthesize visually compelling and temporally coherent clips, yet controlling their physical behavior remains difficult with standard text and image conditions.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose VIPER, a Visual In-Context Physics Reasoning framework for reference-guided image-to-video generation.

**证据证明什么。** Qualitative results further demonstrate that VIPER can transfer reference-derived physical behavior to new target scenes without requiring carefully engineered prompts.

**证据没有证明什么。** These cases suggest that reference-guided physical transfer can still be limited by coarse data annotations and challenging reference-target mismatches. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23472v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.23472v1#A3 — Appendix C Ablation on the Number of Learnable Queries; https://arxiv.org/html/2607.23472v1#A4 — Appendix D Evaluation Details。Limitations / counterevidence：https://arxiv.org/html/2607.23472v1#A6 — Appendix F Limitations and Failure Cases; https://arxiv.org/html/2607.23472v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/Genesis-Embodied-AI/Genesis, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：These cases suggest that reference-guided physical transfer can still be limited by coarse data annotations and challenging reference-target mismatches.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23472:end -->

<!-- review:SF-2026-ARXIV-2607-23478:start -->
### ATLAS: Automated Approximation of Transformers for Efficient Homomorphic Inference in One Hour

<!-- claim:SF-2026-ARXIV-2607-23478:start -->Fully homomorphic encryption (FHE) lets a server run inference on encrypted data with strong privacy guarantees, but running a Transformer under FHE is expensive. Its non-linear operations, such as softmax, normalization, and activation, must be replaced with polynomial approximations that the CKKS scheme supports, and the depth of these approximations dominates inference cost. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23478:end -->

**为什么进入候选分母。** 摘要首要问题为“Fully homomorphic encryption (FHE) lets a server run inference on encrypted data with strong privacy guarantees, but running a Transformer under FHE is expensive.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present ATLAS, a training-free framework that automates this search by treating each layer's approximation setting as a multi-objective optimization over latency and accuracy.

**证据证明什么。** Compared to an iterative softmax baseline, ATLAS cuts multiplicative depth and end-to-end latency by about 35 percent with little accuracy loss, and works across encoder-only, decoder-only, and vision Transformers, complementing parallel work on packing and matrix multiplication.

**证据没有证明什么。** Under this model, the Cloud provider cannot access the sensitive information contained in the customer’s input or output data, while the client remains unaware of the details of neural networks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23478v1#S5.SS2 — 5.2. FHE Inference System Design; https://arxiv.org/html/2607.23478v1#A2 — Appendix B FHE Inference System Implementation。Evaluation：https://arxiv.org/html/2607.23478v1#A6 — Appendix F Extended Experimental Results; https://arxiv.org/html/2607.23478v1#A2.SS1 — B.1. Polynomial Evaluation with Paterson–Stockmeyer Method。Limitations / counterevidence：https://arxiv.org/html/2607.23478v1#S2.SS4 — 2.4. Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/Microsoft/SEAL, https://github.com/timzsu/NEXUS-End2End, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Under this model, the Cloud provider cannot access the sensitive information contained in the customer’s input or output data, while the client remains unaware of the details of neural networks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23478:end -->

<!-- review:SF-2026-ARXIV-2607-23496:start -->
### Do LLMs Know Their Vulnerable Scenarios?

<!-- claim:SF-2026-ARXIV-2607-23496:start -->Safety-aligned large language models are trained to refuse harmful requests, yet embedding the same requests in particular scenarios can bypass their safeguards. Existing red-teaming methods empirically identify effective scenarios through observed attack outcomes, but why particular scenarios weaken refusal remains mechanistically unclear. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23496:end -->

**为什么进入候选分母。** 摘要首要问题为“Safety-aligned large language models are trained to refuse harmful requests, yet embedding the same requests in particular scenarios can bypass their safeguards.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Building on this finding, we propose \textsc{Concept2Scenario}, a concept-based attribution framework for vulnerable scenario discovery.

**证据证明什么。** In this work, we show that scenario-wrapped prompts activate internal scenario directions whose causal steering consistently reduces refusal scores.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23496v1#A3.SS2 — C.2. Fixed-Template Methods; https://arxiv.org/html/2607.23496v1#A3.SS3 — C.3. LLM-Generated Methods。Evaluation：https://arxiv.org/html/2607.23496v1#A1 — Appendix A Steering Experiments with Predefined Scenarios; https://arxiv.org/html/2607.23496v1#S2.SS2 — 2.2. Safety Mechanistic Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.23496v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23496:end -->

<!-- review:SF-2026-ARXIV-2607-23504:start -->
### MemVLN: Episodic and Procedural Memory for Vision-and-Language Navigation

<!-- claim:SF-2026-ARXIV-2607-23504:start -->Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires agents to maintain long-horizon visual history for trajectory consistency while executing actions with low latency. Existing video-based VLN approaches typically struggle to satisfy both demands simultaneously. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23504:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires agents to maintain long-horizon visual history for trajectory consistency while executing actions with low latency.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address these challenges, we propose MemVLN, a novel VLN framework that achieves state-of-the-art performance with real-time inference efficiency (14 FPS).

**证据证明什么。** To address these challenges, we propose MemVLN, a novel VLN framework that achieves state-of-the-art performance with real-time inference efficiency (14 FPS).

**证据没有证明什么。** Future work will explore model quantization and edge-optimized deployment to address these hardware constraints. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23504v1#S3 — 3 Method; https://arxiv.org/html/2607.23504v1#S2.SS1 — 2.1 Large Vision-and-Language Models。Evaluation：https://arxiv.org/html/2607.23504v1#A4 — Appendix D Qualitative Results; https://arxiv.org/html/2607.23504v1#S4 — 4 Experiment。Limitations / counterevidence：https://arxiv.org/html/2607.23504v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.23504v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Future work will explore model quantization and edge-optimized deployment to address these hardware constraints.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23504:end -->

<!-- review:SF-2026-ARXIV-2607-23514:start -->
### Novel Claim or Déjà Vu? Rethinking "Contamination-Free'' Dynamic Evaluation for Multimodal Automated Fact-Checking

<!-- claim:SF-2026-ARXIV-2607-23514:start -->Multimodal automated fact-checking (MAFC) verifies claims by retrieving and reasoning over external evidence. However, most existing static benchmarks risk contamination: they primarily consist of outdated claims verifiable using an LLM's internal knowledge without external evidence. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23514:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal automated fact-checking (MAFC) verifies claims by retrieving and reasoning over external evidence.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Our experiments yield 16 findings, highlighting three key results: (1) Dynamic evaluation reduces but does not eliminate contamination risks, as 17.09\%--29.30\% of post-cut-off claims remain potentially contaminated; (2) Many newly published claims can be verified either directly or by synthesizing multiple pieces of public knowledge available before the cut-off; and (3) Contamination can induce statistically significant inflation in MAFC performance, increasing Macro-F1 by up to 11.34 points and distorting system rankings.

**证据证明什么。** Our experiments yield 16 findings, highlighting three key results: (1) Dynamic evaluation reduces but does not eliminate contamination risks, as 17.09\%--29.30\% of post-cut-off claims remain potentially contaminated; (2) Many newly published claims can be verified either directly or by synthesizing multiple pieces of public knowledge available before the cut-off; and (3) Contamination can induce statistically significant inflation in MAFC performance, increasing Macro-F1 by up to 11.34 points and distorting system rankings.

**证据没有证明什么。** First, dynamic benchmarks reduce contamination, but they do not fully eliminate it. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23514v1#S1 — 1. Introduction; https://arxiv.org/html/2607.23514v1#S2 — 2. Related Work。Evaluation：https://arxiv.org/html/2607.23514v1#S3.SS3 — 3.3. Evaluated MAFC Benchmarks; https://arxiv.org/html/2607.23514v1#S4 — 4. Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.23514v1#S5 — 5. Conclusion。

**Artifact boundary。** Exact v1 links https://ifcncodeofprinciples.poynter.org/signatories, https://huggingface.co/google/embeddinggemma-300m, https://huggingface.co/Qwen/Qwen3-Embedding-0.6B; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：First, dynamic benchmarks reduce contamination, but they do not fully eliminate it.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23514:end -->

<!-- review:SF-2026-ARXIV-2607-23517:start -->
### Real-Time Human-Centric World Modeling for Upper-Body Human-Object Interaction

<!-- claim:SF-2026-ARXIV-2607-23517:start -->We present a real-time human-centric world model for upper-body interactive generation, aiming to synthesize coherent local world dynamics centered on a person, where coordinated body, hand, and facial motions evolve jointly with controllable human-object discrete interaction. To this end, we adopt a continuous-discrete joint control scheme with two complementary components: a continuous human state and a discrete interaction state. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23517:end -->

**为什么进入候选分母。** 摘要首要问题为“We present a real-time human-centric world model for upper-body interactive generation, aiming to synthesize coherent local world dynamics centered on a person, where coordinated body, hand, and facial motions evolve jointly with controllable human-object discrete interaction.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** For continuous human-state control, we introduce a unified implicit representation based on multi-scale motion encoding, in which motion latents from the upper body, hands, and face are fused into a shared latent space.

**证据证明什么。** Experiments demonstrate improved fine-grained motion fidelity, more realistic hand-object coordination, and effective real-time interaction, establishing a practical step beyond motion reproduction toward real-time human-centric world modeling.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23517v1#S3 — 3. Method; https://arxiv.org/html/2607.23517v1#S2.SS2 — 2.2. Interactive World Modeling。Evaluation：https://arxiv.org/html/2607.23517v1#S4 — 4. Experiments; https://arxiv.org/html/2607.23517v1#S4.SS4 — 4.4. Ablation Study。Limitations / counterevidence：https://arxiv.org/html/2607.23517v1#S5 — 5. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23517:end -->

<!-- review:SF-2026-ARXIV-2607-23532:start -->
### Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric

<!-- claim:SF-2026-ARXIV-2607-23532:start -->Swarms of LLM-assisted autonomous robots are increasingly proposed for cooperative intelligence, surveillance, and reconnaissance (ISR) in contested environments. A growing class of their assurance failures arises not within any single platform but across the swarm: individually-compliant actions compose into a mission-level violation: a prohibited objective split across platforms to evade per-platform lim- its, or a collective budget quietly exceeded. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23532:end -->

**为什么进入候选分母。** 摘要首要问题为“Swarms of LLM-assisted autonomous robots are increasingly proposed for cooperative intelligence, surveillance, and reconnaissance (ISR) in contested environments.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present a three-tier (platfor- m/squad/mission) compositional runtime-verification framework that de- composes a mission policy into per-agent and cross-agent aspects, aggre- gates per-platform verdicts over a verification-aware messaging fabric, and fuses them with an evidence-aware, two-axis (security x complete- ness) algebra whose provenance names the platforms that jointly trig- gered a violation.

**证据证明什么。** On a simulated ISR mission, an indirect prompt injection that causes real LLM planners to split a prohibited collection task across four platforms is invisible to every per-platform monitor yet detected compositionally with full prove- nance; under an injected fault campaign a best-effort central monitor emits silent false all-clears while the verification-aware fabric emits none

**证据没有证明什么。** The semantic-extraction path is deliberately secondary; text-only violations depend on classifier quality. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23532v1#S3 — 3 Background, System Model, and Notation; https://arxiv.org/html/2607.23532v1#S5 — 5 Three-Tier Distributed Architecture over the RV-Fabric。Evaluation：https://arxiv.org/html/2607.23532v1#S7 — 7 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.23532v1#S7.SS6 — 7.6 Threats to Validity; https://arxiv.org/html/2607.23532v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The semantic-extraction path is deliberately secondary; text-only violations depend on classifier quality.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23532:end -->

<!-- review:SF-2026-ARXIV-2607-23545:start -->
### Language Shapes Instruction Hierarchy Compliance in Multilingual LLMs

<!-- claim:SF-2026-ARXIV-2607-23545:start -->Instruction hierarchy (IH) requires models to prioritize instructions by source, ensuring that higher-priority instructions override lower-priority ones. Despite its importance for safe and controllable deployment, existing evaluations have focused almost exclusively on English, leaving it unclear whether IH compliance remains stable in multilingual settings. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23545:end -->

**为什么进入候选分母。** 摘要首要问题为“Instruction hierarchy (IH) requires models to prioritize instructions by source, ensuring that higher-priority instructions override lower-priority ones.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce XIH-Bench, a benchmark for multilingual IH evaluation with both same-language and cross-language conflicts across six languages, four domains, and three IH settings.

**证据证明什么。** Across models, we find two consistent patterns.

**证据没有证明什么。** Taken together, these findings show that English-only IH evaluation provides an incomplete picture and motivate future work on multilingual alignment and more consistent IH across languages and settings. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23545v1#A1.SS2 — A.2 Implementation Details; https://arxiv.org/html/2607.23545v1#A2 — Appendix B Detailed implementation of XIH-Bench。Evaluation：https://arxiv.org/html/2607.23545v1#A1.SS1 — A.1 Code and Benchmark Release; https://arxiv.org/html/2607.23545v1#A2.SS6 — B.6 Benchmark Size and Instance Composition。Limitations / counterevidence：https://arxiv.org/html/2607.23545v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.23545v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/g1moon/Language-Shapes-IH, https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Taken together, these findings show that English-only IH evaluation provides an incomplete picture and motivate future work on multilingual alignment and more consistent IH across languages and settings.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23545:end -->

<!-- review:SF-2026-ARXIV-2607-23581:start -->
### Verification-Notebook Learning for Source-Aware Multimodal Misinformation Detection

<!-- claim:SF-2026-ARXIV-2607-23581:start -->Multimodal misinformation verification is challenging because misleading signals may come from different parts of a post and require different forms of evidence. LVLMs are well suited to this task, but their verification performance often depends on the inference procedure applied to each instance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23581:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal misinformation verification is challenging because misleading signals may come from different parts of a post and require different forms of evidence.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We propose Verification-Notebook Learning (VNL), a non-parametric framework that learns an external verification procedure for a frozen LVLM before inference.

**证据证明什么。** Experiments show that VNL consistently outperforms a range of competitive baselines.

**证据没有证明什么。** Conclusion We presented Verification-Notebook Learning, a non-parametric framework for source-aware multimodal misinformation detection with frozen LVLMs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23581v1#Sx4 — Method。Evaluation：https://arxiv.org/html/2607.23581v1#Sx5 — Experiments; https://arxiv.org/html/2607.23581v1#Sx5.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.23581v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Conclusion We presented Verification-Notebook Learning, a non-parametric framework for source-aware multimodal misinformation detection with frozen LVLMs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23581:end -->

<!-- review:SF-2026-ARXIV-2607-23586:start -->
### Are You Still the Agent I Authorized? Earned Authority under a Fixed Ceiling for Evolving Agents

<!-- claim:SF-2026-ARXIV-2607-23586:start -->Long-lived AI agents increasingly evolve after deployment by retaining experience, acquiring skills and tools, revising workflows, delegating work, and moving across task phases. This improves adaptation but creates a distinct authorization problem. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23586:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-lived AI agents increasingly evolve after deployment by retaining experience, acquiring skills and tools, revising workflows, delegating work, and moving across task phases.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** This improves adaptation but creates a distinct authorization problem.

**证据证明什么。** This improves adaptation but creates a distinct authorization problem.

**证据没有证明什么。** This section expands those limitations and records further open problems exposed by the structured model. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23586v1#S3 — III System and Threat Model; https://arxiv.org/html/2607.23586v1#A1 — Appendix A Detailed Structured Model。Evaluation：https://arxiv.org/html/2607.23586v1#S8 — VIII Evaluation Path and Limitations。Limitations / counterevidence：https://arxiv.org/html/2607.23586v1#A2 — Appendix B Expanded Limitations and Open Problems; https://arxiv.org/html/2607.23586v1#S3 — III System and Threat Model。

**Artifact boundary。** Exact v1 links https://owasp.org/www-project-agentic-skills-top-10/, https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：This section expands those limitations and records further open problems exposed by the structured model.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23586:end -->

<!-- review:SF-2026-ARXIV-2607-23588:start -->
### JarvisHub: An Open Harness for Canvas-Native Multimodal Creative Agents

<!-- claim:SF-2026-ARXIV-2607-23588:start -->Creative AI is moving from single-step asset generation toward long-horizon multimodal production. Although recent generative models can synthesize high-quality images, videos, audio clips, UI elements, storyboards, slides, and other creative assets, real-world creative work requires more than isolated prompt-output interactions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23588:end -->

**为什么进入候选分母。** 摘要首要问题为“Creative AI is moving from single-step asset generation toward long-horizon multimodal production.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address this gap, we introduce JarvisHub, a canvas-native creative agent harness for long-horizon multimodal creation.

**证据证明什么。** This design moves creative agents beyond isolated tool use toward sustained, human-steerable creative automation, where agents can progressively plan, generate, revise, and organize multimodal projects while users remain able to inspect, guide, and intervene throughout the process.

**证据没有证明什么。** 5 Conclusion and Limitations We presented JarvisHub, a canvas-native agent harness for long-horizon multimodal creation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23588v1#S2 — 2 Method。Evaluation：https://arxiv.org/html/2607.23588v1#S3 — 3 Experiments; https://arxiv.org/html/2607.23588v1#S3.SS1 — 3.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.23588v1#S5 — 5 Conclusion and Limitations; https://arxiv.org/html/2607.23588v1#S4 — 4 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/LYL1015/JarvisHub, https://github.com/libtv-labs/libtv-skills, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：5 Conclusion and Limitations We presented JarvisHub, a canvas-native agent harness for long-horizon multimodal creation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23588:end -->

<!-- review:SF-2026-ARXIV-2607-23602:start -->
### Action from Adjacent Set in Physical Space Outperforms the Best Prediction in World Models

<!-- claim:SF-2026-ARXIV-2607-23602:start -->Controllers based on sampling and latent world models assign a predicted terminal cost to each candidate action sequence, choose the minimum, execute its first action block, and replan. This rule can fail even when the terminal cost perfectly and accurately reflects the true task objective in the physical world. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23602:end -->

**为什么进入候选分母。** 摘要首要问题为“Controllers based on sampling and latent world models assign a predicted terminal cost to each candidate action sequence, choose the minimum, execute its first action block, and replan.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce Adjacent Set Action Reconstruction (ASAR).

**证据证明什么。** On a Carry and Release evaluation set of 75 queries, Kernel ASAR improves event completion success over matching selection by 28.0, 24.0, and 18.7 percentage points under latent cost and by 18.7, 20.0, and 17.3 points under a trajectory reachability cost at 72, 144, and 288 proposals.

**证据没有证明什么。** If a query requires several distinct behaviors that are absent from one local neighborhood, averaging that neighborhood cannot create the missing sequence. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23602v1#A6.SS3 — F.3 Method Development and Confirmatory Evaluation Protocol; https://arxiv.org/html/2607.23602v1#A11 — Appendix K Replication with an Independently Trained World Model。Evaluation：https://arxiv.org/html/2607.23602v1#A10 — Appendix J Cube Results Stratified by Task Conditions; https://arxiv.org/html/2607.23602v1#A12 — Appendix L Joint Latent and Action Neighborhood Results and Controls。Limitations / counterevidence：https://arxiv.org/html/2607.23602v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.23602v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：If a query requires several distinct behaviors that are absent from one local neighborhood, averaging that neighborhood cannot create the missing sequence.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23602:end -->

<!-- review:SF-2026-ARXIV-2607-23605:start -->
### Hybrid Advantage Estimation with Unified Critic for VLM Agentic Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-23605:start -->Large Vision-Language Models (VLMs) now act as agents in interactive environments, where success requires coherent reasoning and decision-making across turns. Although end-to-end training in agentic environments can improve such multi-turn decision-making abilities, current methods mainly rely on either token-wise optimization over concatenated token trajectories or turn-wise optimization with uniform within-turn credit. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23605:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Vision-Language Models (VLMs) now act as agents in interactive environments, where success requires coherent reasoning and decision-making across turns.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** As such, we propose HyGAE, an actor-critic framework that jointly optimizes token- and turn-level objectives with the hybrid advantage and unified critic.

**证据证明什么。** We conduct extensive evaluations of HyGAE across five multi-turn decision-making environments, where it achieves an average success rate of 91% and a significant improvement of 10% over other methods.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23605v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.23605v1#A1 — Appendix A Theoretical Analysis for Section 4; https://arxiv.org/html/2607.23605v1#A2 — Appendix B Experiment Details。Limitations / counterevidence：https://arxiv.org/html/2607.23605v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/mpSchrader/gym-sokoban, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23605:end -->

<!-- review:SF-2026-ARXIV-2607-23624:start -->
### Where Is the Cost of Third-Party API Routers in Agentic Software Development?

<!-- claim:SF-2026-ARXIV-2607-23624:start -->Third-party API routers have become a common layer that unifies access across increasingly diverse LLM providers. In coding-agent workflows, high-autonomy operation is widely adopted because it reduces interaction overhead. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23624:end -->

**为什么进入候选分母。** 摘要首要问题为“Third-party API routers have become a common layer that unifies access across increasingly diverse LLM providers.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Moreover, we develop SIDEL, a framework for trace recording, replay, injection, and defense evaluation, with a curated dataset of 400 samples.

**证据证明什么。** In coding-agent workflows, high-autonomy operation is widely adopted because it reduces interaction overhead.

**证据没有证明什么。** The remaining threats to validity mainly come from run-to-run instability, measurement scope, and generalizability beyond the evaluated settings. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23624v1#S3 — 3 Study Design; https://arxiv.org/html/2607.23624v1#S3.SS4 — 3.4 Experimental Framework: SIDEL。Evaluation：https://arxiv.org/html/2607.23624v1#S5 — 5 Results Analysis; https://arxiv.org/html/2607.23624v1#A2.SS3 — B.3 Comparative Rewrite Outcomes and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.23624v1#S6 — 6 Threats to Validity; https://arxiv.org/html/2607.23624v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Riyasushin/SIDE, https://github.com/BerriAI/litellm, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：The remaining threats to validity mainly come from run-to-run instability, measurement scope, and generalizability beyond the evaluated settings.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-COST`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23624:end -->

<!-- review:SF-2026-ARXIV-2607-23670:start -->
### Plans Work in Mysterious Ways: Evaluating a Plan Mode for Spreadsheet Agents

<!-- claim:SF-2026-ARXIV-2607-23670:start -->Plan Modes have become standard features in agentic programming tools, allowing users to gain transparency and control by working with the agent to develop a plan before task execution. However, it remains unclear whether the benefits of this feature translate to end-user programming environments such as spreadsheets. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23670:end -->

**为什么进入候选分母。** 摘要首要问题为“Plan Modes have become standard features in agentic programming tools, allowing users to gain transparency and control by working with the agent to develop a plan before task execution.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** However, it remains unclear whether the benefits of this feature translate to end-user programming environments such as spreadsheets.

**证据证明什么。** We discuss the implications of these results for the future design of Plan Modes, and for the broader role of human-AI planning in end-user programming.

**证据没有证明什么。** In this section, we discuss potential design interventions that might allow Plan Mode to engender higher quality outputs for users (§ VI-A ), why participants may have preferred Plan Mode despite the similarity in outputs (§ VI-B ), and future research directions for the design and personalization of Plan Mode for end-user programming (§ VI-C ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23670v1#A0.SS1 — -A Relation of Design Features to Existing Plan Modes; https://arxiv.org/html/2607.23670v1#S3.SS3 — III-C Design Features。Evaluation：https://arxiv.org/html/2607.23670v1#S4.SS4 — IV-D Data Collection and Analysis; https://arxiv.org/html/2607.23670v1#S5 — V Results。Limitations / counterevidence：https://arxiv.org/html/2607.23670v1#S6 — VI Discussion; https://arxiv.org/html/2607.23670v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://code.claude.com/docs/en/permission-modes, https://code.visualstudio.com/docs/copilot/agents/planning, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：In this section, we discuss potential design interventions that might allow Plan Mode to engender higher quality outputs for users (§ VI-A ), why participants may have preferred Plan Mode despite the similarity in outputs (§ VI-B ), and future research directions for the design and personalization of Plan Mode for end-user programming (§ VI-C ).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23670:end -->

<!-- review:SF-2026-ARXIV-2607-23693:start -->
### Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV

<!-- claim:SF-2026-ARXIV-2607-23693:start -->Long-horizon agents increasingly reuse their KV cache as memory: a serving system keeps a subset of cached entries and drops the rest. Eviction and episodic-memory schemes therefore rest on a premise rarely tested directly, that a retained event is still informative once the observations that produced it are gone. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23693:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-horizon agents increasingly reuse their KV cache as memory: a serving system keeps a subset of cached entries and drops the rest.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Long-horizon agents increasingly reuse their KV cache as memory: a serving system keeps a subset of cached entries and drops the rest.

**证据证明什么。** For anyone who evicts the corollary is that dropping a source event and observing no accuracy loss does not show the source was unnecessary.

**证据没有证明什么。** 9 Limitations and scope The donor swaps certify a causal channel for compact state only: verbatim payloads rarely transfer ( ), exact numeric payloads are not natively recovered, derived conclusions need a write-time prompt that itself costs full-context accuracy ( ), and the flat multi-hop curve uses oracle row selection, making it a mechanism ceiling rather than a deployed number. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23693v1#A5 — Appendix E Decoy design and scoring conventions; https://arxiv.org/html/2607.23693v1#A3 — Appendix C Legacy-model diagnostics。Evaluation：https://arxiv.org/html/2607.23693v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23693v1#S2 — 2 The serving contract。Limitations / counterevidence：https://arxiv.org/html/2607.23693v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.23693v1#S9 — 9 Limitations and scope。

**Artifact boundary。** Exact v1 links https://github.com/oklen/Compute-Globally-Materialize-Locally, https://huggingface.co/Qwen/Qwen3.6-27B, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：9 Limitations and scope The donor swaps certify a causal channel for compact state only: verbatim payloads rarely transfer ( ), exact numeric payloads are not natively recovered, derived conclusions need a write-time prompt that itself costs full-context accuracy ( ), and the flat multi-hop curve uses oracle row selection, making it a mechanism ceiling rather than a deployed number.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23693:end -->

<!-- review:SF-2026-ARXIV-2607-23700:start -->
### Offline-Online Curriculum RL for Multimodal Reasoning

<!-- claim:SF-2026-ARXIV-2607-23700:start -->Multimodal large language models exhibit capabilities on reasoning tasks, yet often produce flawed intermediate steps while yielding correct final answers. This behavior undermines interpretability and reliability, suggesting reliance on spurious shortcuts rather than faithful reasoning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23700:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal large language models exhibit capabilities on reasoning tasks, yet often produce flawed intermediate steps while yielding correct final answers.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose $O^2$-CritiCuRL, a novel curriculum reinforcement learning framework that introduces critical-step awareness through an iterative offline-online paradigm.

**证据证明什么。** Extensive experiments on multimodal reasoning benchmarks show that our method achieves state-of-the-art performance while delivering superior training and inference efficiency.

**证据没有证明什么。** We expect that the principle of critical-step awareness is not limited to mathematical reasoning, but can be broadly applied to domains that demand transparent and trustworthy decision-making, such as scientific discovery, legal analysis, and medical diagnosis. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23700v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.23700v1#S5 — 5 Experiments; https://arxiv.org/html/2607.23700v1#S15 — 15 Case Study。Limitations / counterevidence：https://arxiv.org/html/2607.23700v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/OpenBMB/MiniCPM-o, https://github.com/yuh-zha/Vision-G1, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：We expect that the principle of critical-step awareness is not limited to mathematical reasoning, but can be broadly applied to domains that demand transparent and trustworthy decision-making, such as scientific discovery, legal analysis, and medical diagnosis.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23700:end -->

<!-- review:SF-2026-ARXIV-2607-23702:start -->
### Try Once, Then Optimal: De-Redundified Procedure Memory for Cross-Episode Exploration Amortization

<!-- claim:SF-2026-ARXIV-2607-23702:start -->Manipulating objects with hidden internal state, such as a latched microwave, forces a robot to probe before it can act. Yet a robot that has solved an instance once re-runs the same probes whenever it encounters that instance again, because existing cross-episode memories target task success and organize reuse around states, not the object or the cost of re-exploring it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23702:end -->

**为什么进入候选分母。** 摘要首要问题为“Manipulating objects with hidden internal state, such as a latched microwave, forces a robot to probe before it can act.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present Instance-Oriented Memory (IOM), an object-centric framework that amortizes this exploration: from a single encounter that uncovers the hidden state, whether or not it succeeds, IOM records a short procedure for manipulating that instance, keys it on the object's identifiable features, and injects it as a soft bias on a procedure-conditioned policy.

**证据证明什么。** Across all tasks the benefit is purely one of efficiency: success never regresses, and on the real robot even improves.

**证据没有证明什么。** Storing several procedures under one key and selecting among them at runtime would only defer this ambiguity rather than resolve it. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23702v1#S3 — III Method。Evaluation：https://arxiv.org/html/2607.23702v1#S4 — IV Experiments; https://arxiv.org/html/2607.23702v1#S4.SS2 — IV-B Results。Limitations / counterevidence：https://arxiv.org/html/2607.23702v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/moka-ai/m3e-small, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Storing several procedures under one key and selecting among them at runtime would only defer this ambiguity rather than resolve it.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23702:end -->

<!-- review:SF-2026-ARXIV-2607-23704:start -->
### LabRobFail: A Benchmark for Robotic Failure Analysis in Chemical Self-driving Laboratory

<!-- claim:SF-2026-ARXIV-2607-23704:start -->The deployment of embodied agents in self-driving laboratories could accelerate scientific discovery, yet their reliability is constrained by the irreversible and safety-critical nature of chemical experiments. Progress is further hindered by scarce failure data and the lack of fine-grained evaluation protocols. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23704:end -->

**为什么进入候选分母。** 摘要首要问题为“The deployment of embodied agents in self-driving laboratories could accelerate scientific discovery, yet their reliability is constrained by the irreversible and safety-critical nature of chemical experiments.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address these challenges, we introduce LabRobFail, a failure-centric framework for learning and evaluating robotic failure analysis in chemical laboratories.

**证据证明什么。** On seen environments, it achieves 90.83% failure-detection accuracy and 77.21% temporal-localization accuracy, substantially outperforming general-purpose VLMs.

**证据没有证明什么。** While LabRobFail demonstrates robust capabilities in real-time failure detection and fine-grained correction, several limitations remain. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23704v1#Sx4.SSx2 — Architecture and Hybrid Fine-tuning。Evaluation：https://arxiv.org/html/2607.23704v1#Sx5.SSx2 — Quantitative Experimental Results; https://arxiv.org/html/2607.23704v1#A3 — Appendix C Experiment Details。Limitations / counterevidence：https://arxiv.org/html/2607.23704v1#Sx6 — Conclusion and Limitations; https://arxiv.org/html/2607.23704v1#A2.SSx1 — Safety Failure。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：While LabRobFail demonstrates robust capabilities in real-time failure detection and fine-grained correction, several limitations remain.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23704:end -->

<!-- review:SF-2026-ARXIV-2607-23710:start -->
### The Illusion of Secure LLM Code: Closing the Security Gap via Iterative Reprompting

<!-- claim:SF-2026-ARXIV-2607-23710:start -->Large Language Models (LLMs) are increasingly integrated into software development workflows, yet their ability to autonomously generate secure authentication code remains uncertain. This paper evaluates the security architecture of authentication systems generated by five prominent AI coding assistants through a bi-modal assessment framework combining static code analysis and dynamic penetration testing, mapped to NIST SP 800-63B guidelines. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23710:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) are increasingly integrated into software development workflows, yet their ability to autonomously generate secure authentication code remains uncertain.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** This paper evaluates the security architecture of authentication systems generated by five prominent AI coding assistants through a bi-modal assessment framework combining static code analysis and dynamic penetration testing, mapped to NIST SP 800-63B guidelines.

**证据证明什么。** Empirical results demonstrate that code generated from functional or generically secure prompts consistently omits critical protections, particularly concerning brute-force resistance, session management, and robust password handling.

**证据没有证明什么。** A generic request for a “secure and clean” system was not enough to consistently trigger rate limiting, timeout enforcement, password blocklisting, or cookie hardening. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23710v1#S3 — 3 Methodology; https://arxiv.org/html/2607.23710v1#S4.SS4 — 4.4 Cross-Framework Translation of Security Context。Evaluation：https://arxiv.org/html/2607.23710v1#S3.SS1 — 3.1 Experimental Prompt Formulations; https://arxiv.org/html/2607.23710v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.23710v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.23710v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/ipa-lab/hackingBuddyGPT, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：A generic request for a “secure and clean” system was not enough to consistently trigger rate limiting, timeout enforcement, password blocklisting, or cookie hardening.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23710:end -->

<!-- review:SF-2026-ARXIV-2607-23711:start -->
### The Intruder Threshold: A Spectral Law for LoRA Fine-Tuning

<!-- claim:SF-2026-ARXIV-2607-23711:start -->LoRA fine-tuning can create intruder dimensions: new leading singular vectors of the updated weight matrix $W+BA$ that are nearly orthogonal to all pretrained singular vectors and that drive catastrophic forgetting. Since their discovery, no theory has predicted, layer by layer on measured spectra, when they appear. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23711:end -->

**为什么进入候选分母。** 摘要首要问题为“LoRA fine-tuning can create intruder dimensions: new leading singular vectors of the updated weight matrix $W+BA$ that are nearly orthogonal to all pretrained singular vectors and that drive catastrophic forgetting.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Since their discovery, no theory has predicted, layer by layer on measured spectra, when they appear.

**证据证明什么。** Norm-matched interventions confirm that threshold-crossing layers, rather than update magnitude, carry the forgetting, and a spike-budget rule derived from the thresholds, requiring one SVD and no validation sweeps, reduces forgetting by $62\%$ on the most fragile model at no task cost.

**证据没有证明什么。** 7 Limitations The falsifier covers seven base models plus six third-party adapters (unknown recipes, including QLoRA) on which the law holds unchanged, but our own adapters use a single recipe ( ), five of the seven base models are tested on a single task family, and each configuration is a single training run apart from the two three-seed stability checks; bootstrap intervals and seed variance are reported in § 3 . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23711v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23711v1#S2 — 2 Theory: an exactness ladder。Evaluation：https://arxiv.org/html/2607.23711v1#S2.SS3 — 2.3 The evaluation point and its sensitivity。Limitations / counterevidence：https://arxiv.org/html/2607.23711v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：7 Limitations The falsifier covers seven base models plus six third-party adapters (unknown recipes, including QLoRA) on which the law holds unchanged, but our own adapters use a single recipe ( ), five of the seven base models are tested on a single task family, and each configuration is a single training run apart from the two three-seed stability checks; bootstrap intervals and seed variance are reported in § 3 .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23711:end -->

<!-- review:SF-2026-ARXIV-2607-23722:start -->
### E-Bench: Benchmarking Multi-Step Tool-Use Agents in Real-World Product Scenarios

<!-- claim:SF-2026-ARXIV-2607-23722:start -->Large Language Models (LLMs) are increasingly deployed as agents that interact with stateful environments over multiple steps: gathering hidden information, composing tool calls, and committing state changes. We refer to this capability as multi-step tool use. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23722:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) are increasingly deployed as agents that interact with stateful environments over multiple steps: gathering hidden information, composing tool calls, and committing state changes.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce E-Bench, a fully synthetic benchmark with 323 state-changing tasks across three product domains: Honor of Kings, QQ Music, and Tencent Meeting.

**证据证明什么。** Benchmarking 11 cutting-edge LLMs shows that multi-step tool use remains challenging: Pass^3 stays below 60% for the strongest models, and even with code execution in the E-Bench-Code extension, reliability (Pass^3) remains below 70%.

**证据没有证明什么。** The best model reaches only Avg@3, and Pass 3 remains below on E-Bench . exec_code within E-Bench -Code improves every model, but even the best Pass 3 stays below . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23722v1#A1.SS2 — A.2 Per-Model Effect of Code Execution; https://arxiv.org/html/2607.23722v1#S4.SS5 — 4.5 When Do Models Choose to Code? Per-Task Analysis。Evaluation：https://arxiv.org/html/2607.23722v1#A1 — Appendix A More Benchmark Results Analysis; https://arxiv.org/html/2607.23722v1#A1.SS4 — A.4 API Cost-Efficiency Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.23722v1#S5 — 5 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://doi.org/10.18653/v1/2025.emnlp-demos.27, https://aclanthology.org/2025.emnlp-demos.27/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The best model reaches only Avg@3, and Pass 3 remains below on E-Bench . exec_code within E-Bench -Code improves every model, but even the best Pass 3 stays below .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23722:end -->

<!-- review:SF-2026-ARXIV-2607-23731:start -->
### Outcome-Confounded Local Supervision in On-Policy Distillation

<!-- claim:SF-2026-ARXIV-2607-23731:start -->On-policy distillation (OPD) trains a student on its own trajectories while a teacher supplies dense token-level likelihoods at student-visited prefixes. These likelihoods are often read locally: agreement appears safe to imitate, whereas disagreement appears to identify an error. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23731:end -->

**为什么进入候选分母。** 摘要首要问题为“On-policy distillation (OPD) trains a student on its own trajectories while a teacher supplies dense token-level likelihoods at student-visited prefixes.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Our contribution is therefore diagnostic rather than a new training method.

**证据证明什么。** We show that both readings are confounded by the outcome of the completed trajectory.

**证据没有证明什么。** The example is illustrative rather than a causal token annotation: it shows that a failed trajectory can be locally compatible with the teacher over most of its length. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23731v1#S1 — 1 Introduction; https://arxiv.org/html/2607.23731v1#S2 — 2 Setting: Dense Supervision on Student Prefixes。Evaluation：https://arxiv.org/html/2607.23731v1#A1 — Appendix A Additional Experimental Details and Tables。Limitations / counterevidence：https://arxiv.org/html/2607.23731v1#S9 — 9 Limitations and Conclusion; https://arxiv.org/html/2607.23731v1#A1.SS5 — A.5 Illustrative agreement-on-failure trace。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The example is illustrative rather than a causal token annotation: it shows that a failed trajectory can be locally compatible with the teacher over most of its length.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23731:end -->

<!-- review:SF-2026-ARXIV-2607-23765:start -->
### WISERouter: LLM Routing with Workload Budget Constraint

<!-- claim:SF-2026-ARXIV-2607-23765:start -->Large language models (LLMs) achieve impressive performance across multiple domains, but using the most capable model for every query is prohibitive at scale. LLM routing exploits diversity in model capability and cost by assigning each query to a suitable model to balance utility and budget. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23765:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) achieve impressive performance across multiple domains, but using the most capable model for every query is prohibitive at scale.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To address these challenges, we formulate LLM routing as a constrained contextual multi-armed bandit problem and introduce WISERouter (WR for short), a framework that supports offline learning from historical interactions as well as online learning with exploration.

**证据证明什么。** Empirical results on RouterBench and SWE-Bench demonstrate that (i) WR-Offline surpasses existing baselines in performance under a fixed budget and adheres more closely to budget constraints, and (ii) WR-Online achieves comparable performance to the baselines, while using substantially less exploration data.

**证据没有证明什么。** We only explored monetary cost as the constraint on two datasets; extending to other cost definitions and benchmarks with larger model pools is a natural direction for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23765v1#S4 — 4 Our Method; https://arxiv.org/html/2607.23765v1#A8.SS2 — H.2 Baseline Implementation。Evaluation：https://arxiv.org/html/2607.23765v1#A8.SS5 — H.5 WR-Offline Experiment Result on SWE-Bench; https://arxiv.org/html/2607.23765v1#A8 — Appendix H Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.23765v1#S7 — 7 Conclusions and Limitations; https://arxiv.org/html/2607.23765v1#A1 — Appendix A Discussion of Assumptions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：We only explored monetary cost as the constraint on two datasets; extending to other cost definitions and benchmarks with larger model pools is a natural direction for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23765:end -->

<!-- review:SF-2026-ARXIV-2607-23771:start -->
### Training Language Models to Cooperate with Inference-Time Controllers

<!-- claim:SF-2026-ARXIV-2607-23771:start -->Large language model (LLM) performance increasingly depends not only on the base model, but also on the inference-time controller used to organize reasoning. Existing post-training methods, however, typically optimize for a single fixed interaction pattern, despite real deployments relying on diverse controllers such as Chain-of-Thought, self-consistency, debate, planning, and verification pipelines. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23771:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) performance increasingly depends not only on the base model, but also on the inference-time controller used to organize reasoning.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce CALM (Controller-Aware Language Models), a post-training framework that explicitly places controllers in the training loop.

**证据证明什么。** We evaluate CALM on held-out controller compositions and broader controller shifts, showing that controller-aware post-training improves generalization across inference-time workflows beyond single-controller optimization.

**证据没有证明什么。** However, this is the total distance covered by each train in two days, not the individual distances covered in each direction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23771v1#A2.SS3 — B.3 System Prompt Format; https://arxiv.org/html/2607.23771v1#A2.SS2 — B.2 Controller implementations。Evaluation：https://arxiv.org/html/2607.23771v1#S6 — 6 Experiments; https://arxiv.org/html/2607.23771v1#S6.SS1 — 6.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.23771v1#A5.SS1 — E.1 Quality-Diversity: Final Decision Agent recovers from unanimous CoT failure; https://arxiv.org/html/2607.23771v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/math-ai/amc23, https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：However, this is the total distance covered by each train in two days, not the individual distances covered in each direction.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23771:end -->

<!-- review:SF-2026-ARXIV-2607-23782:start -->
### $N_0$-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens

<!-- claim:SF-2026-ARXIV-2607-23782:start -->We present $N_0$-VTLA, a vision-tactile-language-action (VTLA) foundation model capable of (1) fine-grained contact-rich manipulation with tactile perception and tactile-feedback control, and (2) offline policy improvement from stored deployment data. Building on current vision-based backbones, we propose a training recipe for tactile integration consisting of visuo-tactile pre-training, staged tactile-pathway integration, and advantage-conditioned offline policy improvement. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23782:end -->

**为什么进入候选分母。** 摘要首要问题为“We present $N_0$-VTLA, a vision-tactile-language-action (VTLA) foundation model capable of (1) fine-grained contact-rich manipulation with tactile perception and tactile-feedback control, and (2) offline policy improvement from stored deployment data.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** For offline policy improvement, we introduce ALTER, an advantage-conditioned offline reinforcement learning method that converts relative progress and trajectory-event comparisons into binary advantage labels for policy training on a fixed deployment corpus, further improving task-specific learning on contact-rich skills such as deformable object manipulation.

**证据证明什么。** These results lay a foundation for versatile tactile-driven manipulation policies.

**证据没有证明什么。** After Stage 1, the latent tokens retrieve their matching future-tactile target at top-1 accuracy, far above the chance level. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23782v1#S2.SS1 — 2.1 Base Architecture; https://arxiv.org/html/2607.23782v1#S2 — 2 Model。Evaluation：https://arxiv.org/html/2607.23782v1#A5 — Appendix E Per-Task Results and Scoring Rubrics; https://arxiv.org/html/2607.23782v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.23782v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/neoteai/N0-VTLA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：After Stage 1, the latent tokens retrieve their matching future-tactile target at top-1 accuracy, far above the chance level.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23782:end -->

<!-- review:SF-2026-ARXIV-2607-23783:start -->
### $N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation

<!-- claim:SF-2026-ARXIV-2607-23783:start -->We present $N_0$-TWAM, a tactile-native world-action model for contact-rich manipulation that predicts both future vision and future contact. To our knowledge, it is the first tactile world-action model trained at large scale, and it shows strong capability on contact-rich tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23783:end -->

**为什么进入候选分母。** 摘要首要问题为“We present $N_0$-TWAM, a tactile-native world-action model for contact-rich manipulation that predicts both future vision and future contact.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present $N_0$-TWAM, a tactile-native world-action model for contact-rich manipulation that predicts both future vision and future contact.

**证据证明什么。** To our knowledge, it is the first tactile world-action model trained at large scale, and it shows strong capability on contact-rich tasks.

**证据没有证明什么。** 6 Conclusion We presented -TWAM , a tactile-native world-model policy that brings touch into the predicted future of a video world-action model. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23783v1#S2.SS1 — 2.1 Model architecture; https://arxiv.org/html/2607.23783v1#S2 — 2 Model。Evaluation：https://arxiv.org/html/2607.23783v1#A1 — Appendix A Per-task ablation results; https://arxiv.org/html/2607.23783v1#A2 — Appendix B Per-task tactile-realism results。Limitations / counterevidence：https://arxiv.org/html/2607.23783v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/neoteai/N0-TWAM, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：6 Conclusion We presented -TWAM , a tactile-native world-model policy that brings touch into the predicted future of a video world-action model.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23783:end -->

<!-- review:SF-2026-ARXIV-2607-23802:start -->
### From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement

<!-- claim:SF-2026-ARXIV-2607-23802:start -->Reinforcement Learning with Verifiable Rewards (RLVR) has driven recent progress in reasoning-oriented large language models (LLMs) by enabling large-scale optimization. However, its applicability remains largely limited to domains such as mathematics and coding, where correctness can be deterministically verifiable. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23802:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement Learning with Verifiable Rewards (RLVR) has driven recent progress in reasoning-oriented large language models (LLMs) by enabling large-scale optimization.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We instantiate RLSVR with SpyRL, a Self-PlaY Reinforcement Learning method inspired by social deduction game Who Is the Spy?.

**证据证明什么。** These results demonstrate that task transformation can extend scalable RLVR-based self-improvement beyond inherently verifiable domains.

**证据没有证明什么。** Beyond the specific game, our results suggest a broader takeaway: verifiability need not be an intrinsic property of a task, but can be engineered through task transformation—opening a path toward scalable, verifier-free self-improvement on general open-ended capabilities. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23802v1#A3.SS5 — C.5 Prompt Design and Configurations; https://arxiv.org/html/2607.23802v1#A3 — Appendix C Implementation Details。Evaluation：https://arxiv.org/html/2607.23802v1#A4 — Appendix D Additional Experiments; https://arxiv.org/html/2607.23802v1#A4.SS4 — D.4 Evaluation with an Alternative LLM Judge。Limitations / counterevidence：https://arxiv.org/html/2607.23802v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/wangqinsi1/SpyRL, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Beyond the specific game, our results suggest a broader takeaway: verifiability need not be an intrinsic property of a task, but can be engineered through task transformation—opening a path toward scalable, verifier-free self-improvement on general open-ended capabilities.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23802:end -->

<!-- review:SF-2026-ARXIV-2607-23809:start -->
### ACM: Agentic Context Management for Long Horizon Tasks

<!-- claim:SF-2026-ARXIV-2607-23809:start -->Agentic tasks are inherently long-horizon and multi-turn, constantly accumulating context through interactions with the environment. Existing context compression methods inevitably incur information loss and are triggered by rigid heuristic rules, leaving them misaligned with the agent's evolving reasoning focus. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23809:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic tasks are inherently long-horizon and multi-turn, constantly accumulating context through interactions with the environment.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose Agentic Context Management (ACM), a framework that equips agents with purpose-built context editing tools for lossless context management.

**证据证明什么。** Further analysis reveals that effective context management reduces peak token pressure, enables extended explorations, and yields more consistent solutions across independent trials.

**证据没有证明什么。** Second, because prior context-compression baselines have not been evaluated on the three benchmarks we use, we re-implemented them ourselves; despite our best efforts to follow the original designs, minor implementation differences may exist. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23809v1#A2.SS1 — B.1 Agent system prompt; https://arxiv.org/html/2607.23809v1#S3 — 3 Agentic Context Management Framework。Evaluation：https://arxiv.org/html/2607.23809v1#A3.SS3 — C.3 Results and Analysis; https://arxiv.org/html/2607.23809v1#A3 — Appendix C Exploration Diversity Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.23809v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.23809v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/lixiaochuan2020/agentic-context-management, https://www.anthropic.com/claude-code, https://github.com/openai/codex; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Second, because prior context-compression baselines have not been evaluated on the three benchmarks we use, we re-implemented them ourselves; despite our best efforts to follow the original designs, minor implementation differences may exist.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23809:end -->

<!-- review:SF-2026-ARXIV-2607-23815:start -->
### Kalypso: Relational LLM Serving

<!-- claim:SF-2026-ARXIV-2607-23815:start -->Large language models are increasingly used as semantic operators for filtering, extracting, ranking, joining, and transforming unstructured data. Existing semantic query processing systems invoke request-centric LLM serving systems that are unaware of the query plan, leaving substantial performance opportunities unused. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23815:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models are increasingly used as semantic operators for filtering, extracting, ranking, joining, and transforming unstructured data.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present Kalypso, a relational LLM serving system that exposes an API for semantic query plans and executes them using an adaptive, memory-aware scheduling algorithm.

**证据证明什么。** Our evaluation shows that Kalypso improves query completion time over baselines using request-centric LLM serving, with speedups up to 4.57x across diverse workloads, demonstrating that query-aware LLM serving can substantially improve the efficiency of semantic query execution.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23815v1#S5.SS3 — 5.3. The Kalypso Scheduling Algorithm; https://arxiv.org/html/2607.23815v1#S7.SS2 — 7.2. Workloads and Implementations。Evaluation：https://arxiv.org/html/2607.23815v1#S7 — 7. Evaluation; https://arxiv.org/html/2607.23815v1#S7.SS1 — 7.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.23815v1#S9 — 9. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23815:end -->

<!-- review:SF-2026-ARXIV-2607-23838:start -->
### TriShieldRAG: 3 Rings, One Blind Spot in Layered Defenses for Retrieval-Augmented Generation

<!-- claim:SF-2026-ARXIV-2607-23838:start -->Retrieval-Augmented Generation (RAG) grounds LLM answers in query-time retrieved documents, so reliability depends on what the retriever returns. PoisonedRAG (Zou et al., USENIX Security'25) showed five crafted documents mislead an undefended system in nearly 90% of cases, and that single-stage defenses give limited robustness. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23838:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-Augmented Generation (RAG) grounds LLM answers in query-time retrieved documents, so reliability depends on what the retriever returns.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We release the framework, the evasion-certification methodology and artifacts.

**证据证明什么。** PoisonedRAG (Zou et al., USENIX Security'25) showed five crafted documents mislead an undefended system in nearly 90% of cases, and that single-stage defenses give limited robustness.

**证据没有证明什么。** The minority-poison assumption is derived, not yet independently confirmed. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23838v1#S5 — V Proposed TriShieldRAG Framework; https://arxiv.org/html/2607.23838v1#S3 — III Threat Model。Evaluation：https://arxiv.org/html/2607.23838v1#S9 — IX Experimental Results; https://arxiv.org/html/2607.23838v1#S8 — VIII Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.23838v1#S10 — X Discussion and Limitations; https://arxiv.org/html/2607.23838v1#S11 — XI Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/SPriTLab-iitj/TriShieldRAG, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The minority-poison assumption is derived, not yet independently confirmed.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23838:end -->

<!-- review:SF-2026-ARXIV-2607-23844:start -->
### OmniCache: Multidimensional Hierarchical Feature Caching For Diffusion Models

<!-- claim:SF-2026-ARXIV-2607-23844:start -->High-resolution image and video diffusion models, including SD3, FLUX, and recent video diffusion transformers, have substantially improved generative quality but remain expensive at inference time because they repeatedly evaluate attention-heavy denoisers over many sampling steps. We address this inefficiency by exploiting redundancy in intermediate diffusion features rather than changing model weights or retraining. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23844:end -->

**为什么进入候选分母。** 摘要首要问题为“High-resolution image and video diffusion models, including SD3, FLUX, and recent video diffusion transformers, have substantially improved generative quality but remain expensive at inference time because they repeatedly evaluate attention-heavy denoisers over many sampling steps.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Based on this analysis, we propose OmniCache, a unified hierarchical caching framework that performs multidimensional feature reuse through Token Cache, Frame Cache, Block Cache, and Layered Cache.

**证据证明什么。** Across SD3, SVD-XT, and Latte, OmniCache reduces inference latency by up to 35%, 25%, and 28%, respectively, while maintaining visual fidelity and motion coherence in a training-free setting.

**证据没有证明什么。** We formulate cache placement as a benefit-cost tradeoff and refine the resulting schedule with graph dependencies, yet we do not claim global optimality. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23844v1#S3 — 3 Methods; https://arxiv.org/html/2607.23844v1#S4.SS2 — 4.2 Design Choices。Evaluation：https://arxiv.org/html/2607.23844v1#A1.SS1 — A.1 Performance Evaluation of Triton Kernels; https://arxiv.org/html/2607.23844v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.23844v1#S5 — 5 Limitations; https://arxiv.org/html/2607.23844v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/hpcaitech/Open-Sora/tree/main, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：We formulate cache placement as a benefit-cost tradeoff and refine the resulting schedule with graph dependencies, yet we do not claim global optimality.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23844:end -->

<!-- review:SF-2026-ARXIV-2607-23870:start -->
### MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents

<!-- claim:SF-2026-ARXIV-2607-23870:start -->Smart-city airspace is transforming Uncrewed Aerial Vehicles (UAVs) from passive sensing platforms into cyber-physical decision makers that must follow operational rules under degraded observations and ambiguous language. Existing UAV and multimodal benchmarks evaluate perception, navigation, collaboration, and reasoning, but few assess whether physical evidence, protocol constraints, and action risk remain coupled during critical decisions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23870:end -->

**为什么进入候选分母。** 摘要首要问题为“Smart-city airspace is transforming Uncrewed Aerial Vehicles (UAVs) from passive sensing platforms into cyber-physical decision makers that must follow operational rules under degraded observations and ambiguous language.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce MulRobBench, an offline, protocol-conditioned benchmark for Vision-Language-Action (VLA) UAV agents in smart-city environments.

**证据证明什么。** MulRobBench provides a reproducible benchmark for trustworthy multimodal UAV decision making under realistic operational constraints.

**证据没有证明什么。** Future work should extend this reference through formal inter-rater agreement reporting, adjudication protocols, and larger or complete-set expert annotation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23870v1#S3.SS1 — III-A Hierarchical Task Design; https://arxiv.org/html/2607.23870v1#S4.SS5 — IV-E Model Comparison。Evaluation：https://arxiv.org/html/2607.23870v1#S2.SS4 — II-D Benchmark Boundary Analysis; https://arxiv.org/html/2607.23870v1#S4 — IV Experiments and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.23870v1#S4.SS7 — IV-G Discussion; https://arxiv.org/html/2607.23870v1#S4.SS8 — IV-H Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/HuggingFaceTB/SmolVLM2-2.2B-Instruct, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work should extend this reference through formal inter-rater agreement reporting, adjudication protocols, and larger or complete-set expert annotation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23870:end -->

<!-- review:SF-2026-ARXIV-2607-23884:start -->
### A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems

<!-- claim:SF-2026-ARXIV-2607-23884:start -->Recent industry practice has seen the rapid emergence of agentic systems composed of heterogeneous, tool- and LLM-mediated agent components, raising practical questions about inter-agent coordination and protocol design. This paper presents an implementation-grounded comparison of the Model Context Protocol (MCP) and the Agent2Agent (A2A) protocol, from a multi-agent systems engineering perspective, using an inter-agent coordination scenario involving LLM-based agents. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23884:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent industry practice has seen the rapid emergence of agentic systems composed of heterogeneous, tool- and LLM-mediated agent components, raising practical questions about inter-agent coordination and protocol design.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Recent industry practice has seen the rapid emergence of agentic systems composed of heterogeneous, tool- and LLM-mediated agent components, raising practical questions about inter-agent coordination and protocol design.

**证据证明什么。** The results evidence that MCP can support inter-agent coordination in constrained LLM-based systems through a comparatively lightweight implementation model with lower coordination complexity, although coordination concerns such as conversational state management and task lifecycle handling must be implemented explicitly at the application layer.

**证据没有证明什么。** As future work, we plan to investigate dynamic, LLM-driven inter-agent coordination, in which coordination structures are synthesised or adapted at runtime rather than fixed a priori. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23884v1#S3 — 3 Methodology; https://arxiv.org/html/2607.23884v1#S2.SS2 — 2.2 Model Context Protocol (MCP)。Evaluation：https://arxiv.org/html/2607.23884v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.23884v1#S5.SS1 — 5.1 Analysis of Implementation and Coordination Complexity。Limitations / counterevidence：https://arxiv.org/html/2607.23884v1#S6 — 6 Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/AlDanial/cloc, https://github.com/modelcontextprotocol/inspector, https://github.com/arize-ai/phoenix; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：As future work, we plan to investigate dynamic, LLM-driven inter-agent coordination, in which coordination structures are synthesised or adapted at runtime rather than fixed a priori.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MCP`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23884:end -->

<!-- review:SF-2026-ARXIV-2607-23909:start -->
### WorldDiT: A Unified Diffusion Architecture for World and Action Modeling

<!-- claim:SF-2026-ARXIV-2607-23909:start -->Many recent robot policies pursue stronger control by using large pretrained vision-language models (VLMs) as the action backbone. We introduce WorldDiT, a unified diffusion transformer architecture that couples action generation with visual world modeling and achieves strong performance without a large pretrained VLM action backbone. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23909:end -->

**为什么进入候选分母。** 摘要首要问题为“Many recent robot policies pursue stronger control by using large pretrained vision-language models (VLMs) as the action backbone.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Across four LIBERO simulation suites, WorldDiT lies on the reported Pareto frontier for total model parameters and mean success among methods reporting all four suites.

**证据证明什么。** These results provide a strong sub-billion-parameter baseline for future scaling studies.

**证据没有证明什么。** 4 Discussion WorldDiT shows that a single diffusion transformer can couple continuous action generation with future visual prediction while retaining an action-only deployment path. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23909v1#S2 — 2 Method。Evaluation：https://arxiv.org/html/2607.23909v1#S3 — 3 Experiments; https://arxiv.org/html/2607.23909v1#S3.SS2 — 3.2 Results。Limitations / counterevidence：https://arxiv.org/html/2607.23909v1#S4 — 4 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：4 Discussion WorldDiT shows that a single diffusion transformer can couple continuous action generation with future visual prediction while retaining an action-only deployment path.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23909:end -->

<!-- review:SF-2026-ARXIV-2607-23927:start -->
### Reality Monitoring in Large Language Models: Self-Knowledge That Transforms with Conversation Memory

<!-- claim:SF-2026-ARXIV-2607-23927:start -->A conversational AI that cannot tell its own output from what a user said will treat its own mistakes as user-provided facts. In humans, this capacity is called reality monitoring, and its failures are linked to hallucinations, delusions, and confabulation, yet whether LLMs possess it remains untested. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23927:end -->

**为什么进入候选分母。** 摘要首要问题为“A conversational AI that cannot tell its own output from what a user said will treat its own mistakes as user-provided facts.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** This suggests that as AI systems take on autonomous, multi-turn roles, evaluating what they know is not enough: tracking where that knowledge came from may matter equally.

**证据证明什么。** Feedback exposes two failures: in some models, internal and external judgments swap; in others, accuracy improves while confidence decouples from correctness, dissociations invisible to existing benchmarks.

**证据没有证明什么。** Models were not entirely blind to this failure, however: reading hallucinations independently reduced expressed confidence in Experiment 1, so some metacognitive signal tracking encoding fidelity survives. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23927v1#S5 — 5 Methods; https://arxiv.org/html/2607.23927v1#Sx14 — Prompt Architecture。Evaluation：https://arxiv.org/html/2607.23927v1#S5.SS4 — 5.4 Experiment 1: Data Analysis; https://arxiv.org/html/2607.23927v1#S5.SS5 — 5.5 Experiment 2: Data Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.23927v1#S3 — 3 Discussion; https://arxiv.org/html/2607.23927v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/saurabhr/LLM-RM/, https://github.com/saurabhr/psychscanner_v_0_1_0, https://CRAN.R-project.org/package=ordinal; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Models were not entirely blind to this failure, however: reading hallucinations independently reduced expressed confidence in Experiment 1, so some metacognitive signal tracking encoding fidelity survives.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23927:end -->

<!-- review:SF-2026-ARXIV-2607-23929:start -->
### MemTX: Transactional Belief Commit for Stateful Agent Memory

<!-- claim:SF-2026-ARXIV-2607-23929:start -->LLM agents increasingly coordinate through persistent shared memory: one agent's write becomes another agent's premise, and eventually a tool call with real side effects. Current agent memory systems treat every accepted write as immediately actionable truth, so a polluted tool result, a stale update, or a teammate's half-finished note can silently drive an irreversible action. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23929:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents increasingly coordinate through persistent shared memory: one agent's write becomes another agent's premise, and eventually a tool call with real side effects.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present MemTX, a transactional belief-commit protocol.

**证据证明什么。** Backbone capability does not substitute for commit discipline.

**证据没有证明什么。** 6 Conclusion A memory write is not a belief commit. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23929v1#A1.SS1 — A.1 Sweep Design; https://arxiv.org/html/2607.23929v1#S3.SS1 — 3.1 Data Model and Belief Lifecycle。Evaluation：https://arxiv.org/html/2607.23929v1#A1.SS2 — A.2 Results; https://arxiv.org/html/2607.23929v1#A8 — Appendix H Benchmark Composition。Limitations / counterevidence：https://arxiv.org/html/2607.23929v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/lxy1134/MEMTX_, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：6 Conclusion A memory write is not a belief commit.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23929:end -->

<!-- review:SF-2026-ARXIV-2607-23933:start -->
### SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving

<!-- claim:SF-2026-ARXIV-2607-23933:start -->As LLM agents increasingly rely on the Model Context Protocol (MCP) to invoke isolated external sandboxes, disaggregated sandbox deployment introduces a fundamental tension between resource utilization and interactive tail latency. Persistent long-lived sandbox reservations incur excessive memory overhead at scale, while lazy on-demand instantiation generates severe cold-start penalties that degrade response performance under multi-tenant, multi-turn agent workloads. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23933:end -->

**为什么进入候选分母。** 摘要首要问题为“As LLM agents increasingly rely on the Model Context Protocol (MCP) to invoke isolated external sandboxes, disaggregated sandbox deployment introduces a fundamental tension between resource utilization and interactive tail latency.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To resolve this dilemma, we present SpecBox, a runtime built around speculative sandbox preallocation tailored for dynamic LLM agent execution pipelines.

**证据证明什么。** Evaluated on high-concurrency multi-turn agent traces, our prototype demonstrates that SpecBox cuts P99 end-to-end latency by up to $2.9\times$ relative to the on-demand sandbox baseline, while slashing peak memory consumption by $45.9\%$ compared to permanently reserved sandbox deployments.

**证据没有证明什么。** Future work will investigate online Graph Neural Networks (GNNs) to adaptively capture non-linear transition patterns. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23933v1#S3 — 3. Design of SpecBox; https://arxiv.org/html/2607.23933v1#S4 — 4. Implementation。Evaluation：https://arxiv.org/html/2607.23933v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.23933v1#S5.SS1 — 5.1. Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.23933v1#S6 — 6. Discussion; https://arxiv.org/html/2607.23933v1#S8 — 8. Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/datalayer/jupyter-mcp-server, https://github.com/mcp, https://github.com/microsoft/playwright#playwright-mcp; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Future work will investigate online Graph Neural Networks (GNNs) to adaptively capture non-linear transition patterns.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23933:end -->

<!-- review:SF-2026-ARXIV-2607-23955:start -->
### EviBack: Search-Agent Reinforcement Learning via Evidence-Constrained Teacher Backoff

<!-- claim:SF-2026-ARXIV-2607-23955:start -->Reinforcement learning enables Agentic RAG systems to learn multi-turn search from verifiable outcome rewards, but all- zero rollout groups provide no comparative signal and may hide useful search behavior. We present EviBack, an evidence- constrained Teacher backoff that supplies auxiliary super- vision to such groups while preserving verifiable Actor re- wards. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23955:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning enables Agentic RAG systems to learn multi-turn search from verifiable outcome rewards, but all- zero rollout groups provide no comparative signal and may hide useful search behavior.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present EviBack, an evidence- constrained Teacher backoff that supplies auxiliary super- vision to such groups while preserving verifiable Actor re- wards.

**证据证明什么。** Across seven open-domain QA benchmarks and three Qwen3 scales, EviBack improves F1 over Search-R1 and raises both single- and multi-hop macro F1.

**证据没有证明什么。** Consequently, the reported results do not directly establish performance on the complete datasets. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23955v1#S3 — 3 Methodology; https://arxiv.org/html/2607.23955v1#S3.SSx2 — Method Overview。Evaluation：https://arxiv.org/html/2607.23955v1#S4 — 4 Experiments; https://arxiv.org/html/2607.23955v1#S4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.23955v1#S5 — 5 Discussion and Limitations; https://arxiv.org/html/2607.23955v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Consequently, the reported results do not directly establish performance on the complete datasets.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23955:end -->

<!-- review:SF-2026-ARXIV-2607-23969:start -->
### LeapBot-WA: World-Anchor Action Models via Predictive Latent Alignments

<!-- claim:SF-2026-ARXIV-2607-23969:start -->World Action Models (WAMs) have emerged as a powerful paradigm for embodied intelligence, yet the prevailing reliance on pixel-level video generation creates a fundamental bottleneck. Forcing models to reconstruct task-irrelevant visual details dissipates representational capacity and renders policies vulnerable to visual distractors. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23969:end -->

**为什么进入候选分母。** 摘要首要问题为“World Action Models (WAMs) have emerged as a powerful paradigm for embodied intelligence, yet the prevailing reliance on pixel-level video generation creates a fundamental bottleneck.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this paper, we propose LeapBot-WA, which establishes a novel Predictive-Latent paradigm for WAMs by operationalizing the Joint-Embedding Predictive Architecture (JEPA) as a World-Anchor.

**证据证明什么。** LeapBot-WA achieves state-of-the-art performance among predictive models on LIBERO and matches top-tier generative WAMs on RoboTwin 2.0 without requiring large-scale trajectory pre-training.

**证据没有证明什么。** Future research will explore the integration of multi-modal foundation models to incorporate audio-visual or haptic priors into the world-anchor space. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23969v1#Sx3 — Methodology; https://arxiv.org/html/2607.23969v1#Sx3.SSx1 — Framework Overview。Evaluation：https://arxiv.org/html/2607.23969v1#Sx4 — Experiments; https://arxiv.org/html/2607.23969v1#Sx4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.23969v1#Sx5 — Conclusion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future research will explore the integration of multi-modal foundation models to incorporate audio-visual or haptic priors into the world-anchor space.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23969:end -->

<!-- review:SF-2026-ARXIV-2607-23991:start -->
### SyRuP: Enhancing System-Prompt Following via Reward-Guided Prediction in LLM Decoding

<!-- claim:SF-2026-ARXIV-2607-23991:start -->Large Language Models (LLMs) are increasingly controlled through system prompts that specify roles, formats, and safety requirements. However, models follow these prompts only implicitly through in-context learning, which can be insufficient for complex or compositional prompts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23991:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) are increasingly controlled through system prompts that specify roles, formats, and safety requirements.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce SyRuP, a decoding-time framework for improving system-prompt adherence while keeping the base LM frozen.

**证据证明什么。** Experiments on system-prompt following benchmarks show that SyRuP consistently outperforms prompting and decoding-time baselines with moderate inference overhead.

**证据没有证明什么。** Limitations and Future Work While SyRuP improves system-prompt adherence without updating the base LM, it has several limitations that suggest directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23991v1#S3 — 3 Method; https://arxiv.org/html/2607.23991v1#A3 — Appendix C Training and Decoding Algorithms。Evaluation：https://arxiv.org/html/2607.23991v1#A4 — Appendix D Extended Analyses and Ablations; https://arxiv.org/html/2607.23991v1#A5 — Appendix E Token-wise Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.23991v1#Sx1 — Limitations and Future Work; https://arxiv.org/html/2607.23991v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/argilla/OpenHermesPreferences, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Limitations and Future Work While SyRuP improves system-prompt adherence without updating the base LM, it has several limitations that suggest directions for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PROMPT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23991:end -->

<!-- review:SF-2026-ARXIV-2607-23999:start -->
### ContainmentBench: Trace-Based Evaluation of Post-Exposure Containment in Tool-Using LLM Agents

<!-- claim:SF-2026-ARXIV-2607-23999:start -->Tool-using large language model (LLM) agents read untrusted content, maintain memory, delegate tasks, and invoke tools with external side effects. Terminal attack-success or policy-violation rates do not show what happens between exposure and commit or whether a defense also suppresses authorized actions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-23999:end -->

**为什么进入候选分母。** 摘要首要问题为“Tool-using large language model (LLM) agents read untrusted content, maintain memory, delegate tasks, and invoke tools with external side effects.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce ContainmentBench, a sandboxed benchmark comprising a 504-scenario specification dataset, a shared rollout-trace schema, and stage-scoped metrics for endpoint violations, logged propagation, and explicitly authorized taint-exposed proposals that commit.

**证据证明什么。** Terminal attack-success or policy-violation rates do not show what happens between exposure and commit or whether a defense also suppresses authorized actions.

**证据没有证明什么。** This decomposition exposes a secure-looking taint-only policy that disables authorized work, an intent-aware repair that remains below a strong tool boundary on utility, and propagation rankings that depend on stage and denominator. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.23999v1#S3.SS1 — 3.1. System Model; https://arxiv.org/html/2607.23999v1#S4.SS1 — 4.1. Design Goals。Evaluation：https://arxiv.org/html/2607.23999v1#S2.SS1 — 2.1. Outcome-Oriented Prompt-Injection Benchmarks; https://arxiv.org/html/2607.23999v1#S6 — 6. Experimental Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.23999v1#S8 — 8. Discussion and Limitations; https://arxiv.org/html/2607.23999v1#S10 — 10. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：This decomposition exposes a secure-looking taint-only policy that disables authorized work, an intent-aware repair that remains below a strong tool boundary on utility, and propagation rankings that depend on stage and denominator.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-23999:end -->

<!-- review:SF-2026-ARXIV-2607-24008:start -->
### FutureRTC: Real-Time Robot Execution with Anticipatory-Conditioned Action Chunking

<!-- claim:SF-2026-ARXIV-2607-24008:start -->Real-time deployment of Vision-Language-Action (VLA) policies necessitates asynchronous execution, wherein subsequent action chunks are computed concurrently with the execution of the current chunk, leading to prediction-execution misalignment and manifesting as inter-chunk discontinuities. Existing methods either superficially smooth chunk boundaries, require costly policy optimization, or exclusively forward-predict proprioceptive states yet neglect critical visual observations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24008:end -->

**为什么进入候选分母。** 摘要首要问题为“Real-time deployment of Vision-Language-Action (VLA) policies necessitates asynchronous execution, wherein subsequent action chunks are computed concurrently with the execution of the current chunk, leading to prediction-execution misalignment and manifesting as inter-chunk discontinuities.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we propose \textbf{FutureRTC}, a plug-and-play adaptation framework that predicts execution-time observations and states for asynchronous VLA control without modifying the underlying policy.

**证据证明什么。** Extensive experiments across simulated and real-world environments demonstrate that FutureRTC achieves superior robustness to inference delays, resulting in smoother trajectories, faster execution, and consistently higher task success rates.

**证据没有证明什么。** Limitations While FutureRTC substantially improves the robustness of asynchronous VLA execution, it still has several limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24008v1#Sx4 — Methodology; https://arxiv.org/html/2607.24008v1#Sx8.SSx2 — Task Design。Evaluation：https://arxiv.org/html/2607.24008v1#Sx5.SSx2 — Ablation and Analysis; https://arxiv.org/html/2607.24008v1#Sx10 — Ablation Study。Limitations / counterevidence：https://arxiv.org/html/2607.24008v1#Sx11 — Limitations; https://arxiv.org/html/2607.24008v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Limitations While FutureRTC substantially improves the robustness of asynchronous VLA execution, it still has several limitations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24008:end -->

<!-- review:SF-2026-ARXIV-2607-24010:start -->
### When Should Active RAG Retrieve? A Budget-Aware Evaluation of Utility, Calibration, and Cost

<!-- claim:SF-2026-ARXIV-2607-24010:start -->Active RAG systems decide when to retrieve external knowledge during generation, making them a budget-sensitive case of agentic RAG and self-adaptive retrieval. Yet evaluations often leave the operating point underspecified: two systems may both claim a 50% evidence-usage budget while realizing different held-out usage rates, so higher accuracy can reflect a looser budget rather than a better retrieval policy. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24010:end -->

**为什么进入候选分母。** 摘要首要问题为“Active RAG systems decide when to retrieve external knowledge during generation, making them a budget-sensitive case of agentic RAG and self-adaptive retrieval.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Active RAG systems decide when to retrieve external knowledge during generation, making them a budget-sensitive case of agentic RAG and self-adaptive retrieval.

**证据证明什么。** Budget-aware Active RAG evaluations should therefore report frontiers, realized usage, threshold-transfer error, harm rates, and cost decompositions alongside accuracy.

**证据没有证明什么。** Thus retrieval harm is not only an indexing problem: even relevant evidence can pull the generator toward the wrong relation or entity. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24010v1#S3.SS0.SSS0.Px2 — Cost model.; https://arxiv.org/html/2607.24010v1#S4.SS0.SSS0.Px2 — Models and retrieval.。Evaluation：https://arxiv.org/html/2607.24010v1#S4 — 4. Experimental Setup; https://arxiv.org/html/2607.24010v1#S5 — 5. Results。Limitations / counterevidence：https://arxiv.org/html/2607.24010v1#S5.SS0.SSS0.Px3 — RQ3: Do calibrated thresholds meet future budgets?; https://arxiv.org/html/2607.24010v1#S5.SS0.SSS0.Px5 — RQ5: How does cost accounting change the conclusion?。

**Artifact boundary。** Exact v1 links https://huggingface.co/ibm-granite/granite-3.1-2b-instruct, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Thus retrieval harm is not only an indexing problem: even relevant evidence can pull the generator toward the wrong relation or entity.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24010:end -->

<!-- review:SF-2026-ARXIV-2607-24027:start -->
### Sol-Attn: Accelerating Video Generation Inference via On-the-Fly Attention Sparsification

<!-- claim:SF-2026-ARXIV-2607-24027:start -->Diffusion transformers are essential for high-fidelity video generation, but long token sequences make attention a dominant inference bottleneck. Training-free dynamic sparse attention alleviates this bottleneck by computing only selected key-value blocks, yet existing methods struggle to sparsify attention both efficiently and accurately for two reasons: (1) Rigid, unpredictable, and costly routing: selecting a fixed fraction of top-ranked blocks by proxy score imposes fixed budgets, whereas retaining blocks to reach a target cumulative proxy probability mass yields dynamic but potentially imbalanced budgets; both incur non-negligible overhead from computing and materializing proxy scores. (2) Lossy keep-or-drop sparsification: unselected blocks are discarded entirely, degrading accuracy under aggressive sparsity. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24027:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion transformers are essential for high-fidelity video generation, but long token sequences make attention a dominant inference bottleneck.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we introduce training-free Sol-Attn (Sparsifying online attention), which unifies dynamic routing, sparse computation, and approximation correction in a single online-softmax pass, achieving a better accuracy-efficiency trade-off in sparse attention.

**证据证明什么。** Experiments across image and video generation tasks show that Sol-Attn advances the quality-efficiency frontier of training-free sparse attention, delivering 2.1 times and 2.3 times end-to-end speedups for video generation and editing, respectively, while preserving visual quality.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24027v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.24027v1#A1 — Appendix A Additional Experimental Details; https://arxiv.org/html/2607.24027v1#A2 — Appendix B Derivations and Error Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.24027v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/NVlabs/Sana/tree/sol-engine, https://huggingface.co/Lightricks/LTX-2.3, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24027:end -->

<!-- review:SF-2026-ARXIV-2607-24054:start -->
### Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation

<!-- claim:SF-2026-ARXIV-2607-24054:start -->A correct answer can conceal why an agent succeeded. Once agents change their information state during evaluation, correctness no longer distinguishes intended reasoning from answer acquisition. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24054:end -->

**为什么进入候选分母。** 摘要首要问题为“A correct answer can conceal why an agent succeeded.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Once agents change their information state during evaluation, correctness no longer distinguishes intended reasoning from answer acquisition.

**证据证明什么。** In D0, GOLD exceeds SHAM by 19.1 to 25.9 percentage points, showing that success follows the correct value.

**证据没有证明什么。** Conclusion Correctness establishes the outcome, not why it became possible. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24054v1#Sx3 — AcquaBench Design; https://arxiv.org/html/2607.24054v1#A2.SS6 — B.6 Bootstrap and Model Common Support。Evaluation：https://arxiv.org/html/2607.24054v1#A1.SS1 — A.1 Matched Evaluation Unit; https://arxiv.org/html/2607.24054v1#A3 — Appendix C Complete Frozen Results。Limitations / counterevidence：https://arxiv.org/html/2607.24054v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Conclusion Correctness establishes the outcome, not why it became possible.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24054:end -->

<!-- review:SF-2026-ARXIV-2607-24063:start -->
### The Cost of Knowing: A Resource-Aware Protocol for Benchmarking Hallucination Beyond Static Leaderboards

<!-- claim:SF-2026-ARXIV-2607-24063:start -->On standard factuality tasks, frontier models now cluster near the top of the scale. The question is therefore shifting from how factual a system is toward how much compute that factuality costs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24063:end -->

**为什么进入候选分母。** 摘要首要问题为“On standard factuality tasks, frontier models now cluster near the top of the scale.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To make this trade-off visible, we introduce MAS-HQ (Multi-Agent System Hallucination Quest), a resource-aware evaluation protocol.

**证据证明什么。** MAS-HQ provides a reproducible way to measure how much a factual answer costs.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24063v1#Sx3 — MAS-HQ Framework and Reference Architecture; https://arxiv.org/html/2607.24063v1#Sx4.SSx3 — Resource-Efficient Behavior and Frontier-Model Comparisons。Evaluation：https://arxiv.org/html/2607.24063v1#A3 — Appendix C More Ablation Studies; https://arxiv.org/html/2607.24063v1#A4 — Appendix D Prompts and Other Results。Limitations / counterevidence：https://arxiv.org/html/2607.24063v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/vectara/hallucination_evaluation_model, https://huggingface.co/datasets/vectara/leaderboard_results, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24063:end -->

<!-- review:SF-2026-ARXIV-2607-24097:start -->
### MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents

<!-- claim:SF-2026-ARXIV-2607-24097:start -->Memory-augmented LLM agents typically answer queries by retrieving relevant memories and feeding them directly to an answer model. This retrieval-as-evidence paradigm assumes retrieved memories are already suitable for reasoning, leaving the answer model to resolve redundancy, conflicts, and weak relevance while incurring substantial context overhead in long-term memory tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24097:end -->

**为什么进入候选分母。** 摘要首要问题为“Memory-augmented LLM agents typically answer queries by retrieving relevant memories and feeding them directly to an answer model.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To train the mediator, we introduce a two-stage learning framework.

**证据证明什么。** Experiments on LoCoMo and LongMemEval-S demonstrate that MemChain consistently achieves state-of-the-art performance across both closed-source and open-weight frozen answer models while substantially reducing the memory context passed to the answer model.

**证据没有证明什么。** 7 Limitations MemChain operates within the retrieved candidate boundary and cannot recover evidence omitted by the upstream retriever. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24097v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.24097v1#S5.SS2 — 5.2 Results and Analysis; https://arxiv.org/html/2607.24097v1#A1 — Appendix A Experimental Details and Additional Analyses。Limitations / counterevidence：https://arxiv.org/html/2607.24097v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.24097v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/mayiwen0212/MemChain, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：7 Limitations MemChain operates within the retrieved candidate boundary and cannot recover evidence omitted by the upstream retriever.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24097:end -->

<!-- review:SF-2026-ARXIV-2607-24112:start -->
### Scaling GUI Agents with Visual State Transitions

<!-- claim:SF-2026-ARXIV-2607-24112:start -->We introduce State Transition Pretraining (STP) as a new scaling axis for GUI agents. During the STP stage, we continually pretrain a unified multimodal model on visual state transitions by jointly optimizing inverse dynamics (predicting actions from state changes) and forward dynamics (predicting next states from current states and actions). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24112:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce State Transition Pretraining (STP) as a new scaling axis for GUI agents.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce State Transition Pretraining (STP) as a new scaling axis for GUI agents.

**证据证明什么。** Further empirical studies show that joint dynamics optimization yields stable improvements over single-objective training, and downstream performance scales steadily with the volume of transition data.

**证据没有证明什么。** Taken together, these findings position step-level visual state transitions as an underexploited scaling axis for GUI agents, complementary to trajectory fine-tuning and potentially to reinforcement learning, and suggest that future work on large-scale automated transition collection could unlock further gains without incurring the cost of full trajectory annotation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24112v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24112v1#S2 — 2 State Transition Pretraining for GUI Agents。Evaluation：https://arxiv.org/html/2607.24112v1#S3 — 3 Experiments; https://arxiv.org/html/2607.24112v1#S3.SS1 — 3.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24112v1#S5 — 5 Limitations; https://arxiv.org/html/2607.24112v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/xyliugo/gui-state-transition-pretraining, https://github.com/bytedance-seed/BAGEL, https://openai.com/index/codex-for-almost-everything/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Taken together, these findings position step-level visual state transitions as an underexploited scaling axis for GUI agents, complementary to trajectory fine-tuning and potentially to reinforcement learning, and suggest that future work on large-scale automated transition collection could unlock further gains without incurring the cost of full trajectory annotation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24112:end -->

<!-- review:SF-2026-ARXIV-2607-24117:start -->
### Grading the Narrators: An Isnad-Rijal Framework for Claim-Level Provenance in Multi-Agent Knowledge Systems

<!-- claim:SF-2026-ARXIV-2607-24117:start -->Modern multi-agent knowledge systems increasingly accumulate knowledge through chains of autonomous transformations rather than direct retrieval. Existing provenance work records what happened - execution traces, tool calls, evidence links - and source-reliability estimation is long established (truth discovery, reputation systems). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24117:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern multi-agent knowledge systems increasingly accumulate knowledge through chains of autonomous transformations rather than direct retrieval.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** This paper transfers that methodology to AI system design.

**证据证明什么。** The paper is explicit throughout about which claims the evidence does and does not yet support.

**证据没有证明什么。** Classical scholars faced a structurally identical problem in the madār (the pivot narrator through which ostensibly independent chains converge), and treated such convergence as reducing, not confirming, independence. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24117v1#S0.SSx2.SSSx3 — 2.3 Multi-agent knowledge systems and the provenance state of the art; https://arxiv.org/html/2607.24117v1#S0.SSx4 — 4. The Isnād–Rijāl Framework。Evaluation：https://arxiv.org/html/2607.24117v1#S0.SSx8 — 8. Evaluation; https://arxiv.org/html/2607.24117v1#S0.SSx6 — 6. Case study: the matn-criticism substrate on real texts。Limitations / counterevidence：https://arxiv.org/html/2607.24117v1#S0.SSx3 — 3. Threat model and scope; https://arxiv.org/html/2607.24117v1#S0.SSx7 — 7. Limitations and ethical considerations。

**Artifact boundary。** Exact v1 links https://github.com/alizahidraja/isnad, https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Classical scholars faced a structurally identical problem in the madār (the pivot narrator through which ostensibly independent chains converge), and treated such convergence as reducing, not confirming, independence.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24117:end -->

<!-- review:SF-2026-ARXIV-2607-24148:start -->
### A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference

<!-- claim:SF-2026-ARXIV-2607-24148:start -->Vision-Language-Action (VLA) models have demonstrated strong potential for embodied AI, yet their high inference latency on GPUs limits real-time deployment. Existing accelerators, such as Dadu-Corki, improve efficiency but treat VLA models as full-precision workloads, leaving substantial redundancy in both memory and computation underexploited. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24148:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language-Action (VLA) models have demonstrated strong potential for embodied AI, yet their high inference latency on GPUs limits real-time deployment.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we propose VQVLA, an algorithm-hardware co-design framework that accelerates VLA inference by exploiting weight similarity and execution dynamics.

**证据证明什么。** Experimental results show that VQVLA achieves 6.5x, 2.8x, 1.9x, 3.3x, and 4.3x speedup over the A100 GPU, Dadu-Corki, LUT-DLA, CodeGEMM, and ShiftAddLLM, respectively, with negligible accuracy degradation.

**证据没有证明什么。** By analyzing the execution characteristics of robotic systems, we observe that VLA models exhibit state-dependent sensitivity and substantial centroid redundancy after VQ. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24148v1#S2.SS3 — 2.3. VLA Accelerator Design; https://arxiv.org/html/2607.24148v1#S6 — 6. Architecture。Evaluation：https://arxiv.org/html/2607.24148v1#S7 — 7. Evaluation; https://arxiv.org/html/2607.24148v1#S7.SS2 — 7.2. VQVLA Algorithm Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.24148v1#S9 — 9. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：By analyzing the execution characteristics of robotic systems, we observe that VLA models exhibit state-dependent sensitivity and substantial centroid redundancy after VQ.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24148:end -->

<!-- review:SF-2026-ARXIV-2607-24157:start -->
### UniGen-AR: Unifying Visual Generation with Auto-Regressive Modeling

<!-- claim:SF-2026-ARXIV-2607-24157:start -->Modern computer vision pipelines remain fragmented, with tasks such as text-to-image generation, editing, restoration, and classical perception handled by separate models. We study Unified Visual Generation (UVG), where a single model produces diverse image-valued outputs through a unified multimodal interface. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24157:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern computer vision pipelines remain fragmented, with tasks such as text-to-image generation, editing, restoration, and classical perception handled by separate models.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To address these limitations, we propose UniGen-AR, a framework that pairs a general-purpose multi-modal language model (MLLM) with an efficient next-scale visual auto-regressive (VAR) decoder.

**证据证明什么。** These results establish visual auto-regressive modeling as a compelling and efficient backbone for unified visual generation.

**证据没有证明什么。** Addressing these limitations is an important direction for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24157v1#A4.SS4 — D.4 Ablation Study on Design of Ref Tokens; https://arxiv.org/html/2607.24157v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.24157v1#S4 — 4 Experimental Evaluations; https://arxiv.org/html/2607.24157v1#A4 — Appendix D Additional Evaluations。Limitations / counterevidence：https://arxiv.org/html/2607.24157v1#S4.SS5 — 4.5 Limitation and Future Work; https://arxiv.org/html/2607.24157v1#A2 — Appendix B Failure Mode。

**Artifact boundary。** Exact v1 links https://zpbao.github.io/projects/unigenar, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Addressing these limitations is an important direction for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24157:end -->

<!-- review:SF-2026-ARXIV-2607-24159:start -->
### DeVA: Decoupled Video-Action Model with physical guidance for robot policy learning

<!-- claim:SF-2026-ARXIV-2607-24159:start -->Generalizable robot manipulation requires policies that can anticipate how visual scenes evolve while executing language instructions. While recent Vision-Language-Action models benefit from large-scale pretraining, their predominantly static pretraining objectives provide limited supervision for physical dynamics and temporal causality, leaving control-relevant knowledge to be learned from downstream robot demonstrations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24159:end -->

**为什么进入候选分母。** 摘要首要问题为“Generalizable robot manipulation requires policies that can anticipate how visual scenes evolve while executing language instructions.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this work, we introduce DeVA, a Decoupled Video-Action model with specialized video and action experts, multi-level feature transfer, and physically salient guidance.

**证据证明什么。** Experiments on both simulation benchmarks and real-world deployment demonstrate strong performance with limited data, faster convergence than a unified architecture, and clear performance gains from physical guidance.

**证据没有证明什么。** Training spatiotemporal attention over future observations remains more expensive than action-only policy learning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24159v1#A1.SS1 — A.1 Video Expert Architecture; https://arxiv.org/html/2607.24159v1#A1.SS2 — A.2 Action Expert Architecture。Evaluation：https://arxiv.org/html/2607.24159v1#A3.SS2 — C.2 Evaluation Score Criteria; https://arxiv.org/html/2607.24159v1#A3.SS4 — C.4 Robustness Analysis for DeVA。Limitations / counterevidence：https://arxiv.org/html/2607.24159v1#S6 — 6 Limitation; https://arxiv.org/html/2607.24159v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/nvidia-cosmos/cosmos-predict2, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Training spatiotemporal attention over future observations remains more expensive than action-only policy learning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24159:end -->

<!-- review:SF-2026-ARXIV-2607-24162:start -->
### Agent-UCT: Upper Confidence Bounds Applied to Trees for Agentic Workflow Optimization with Cost-Awareness

<!-- claim:SF-2026-ARXIV-2607-24162:start -->Optimizing agentic workflows, such as retrieval-augmented generation (RAG) pipelines, requires navigating a combinatorial space of discrete component choices under tight evaluation budgets. Existing approaches - heuristic search, black-box optimization, and standard tree search methods - do not explicitly exploit the compositional structure of these workflows, leading to redundant computation and inefficient budget allocation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24162:end -->

**为什么进入候选分母。** 摘要首要问题为“Optimizing agentic workflows, such as retrieval-augmented generation (RAG) pipelines, requires navigating a combinatorial space of discrete component choices under tight evaluation budgets.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Our framework, RAGSpace, unifies heterogeneous RAG components from LongRAG, LightRAG, and Self-RAG into a five-dimensional configuration space, enabling systematic cross-framework recombination.

**证据证明什么。** Compared with full-pool evaluation, sampling-based evaluation further achieves a 4.2x wall-clock speedup.

**证据没有证明什么。** However, the current experiments do not fully exercise WTB’s support for more complex file-system-like execution structures. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24162v1#Sx3 — Method。Evaluation：https://arxiv.org/html/2607.24162v1#Sx4 — Experiments; https://arxiv.org/html/2607.24162v1#Sx4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24162v1#Sx5 — Discussion and Limitations; https://arxiv.org/html/2607.24162v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：However, the current experiments do not fully exercise WTB’s support for more complex file-system-like execution structures.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24162:end -->

<!-- review:SF-2026-ARXIV-2607-24165:start -->
### Do Current Retrievers Cover All the Evidence? A Controlled Study of Conjunctive Cross-Page Retrieval

<!-- claim:SF-2026-ARXIV-2607-24165:start -->Finding a long document relevant to a multi-part request is not the same as establishing that it contains every requested piece of evidence. We study this gap for conjunctive document retrieval, where two or three explicit conditions must be supported on different pages of one document. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24165:end -->

**为什么进入候选分母。** 摘要首要问题为“Finding a long document relevant to a multi-part request is not the same as establishing that it contains every requested piece of evidence.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Finally, page-aware visual systems surface stored support for every condition on only 5.1--5.3\% of queries.

**证据证明什么。** Across 70 configurations, condition-wise decomposition improves two dense backbones by 6.8--7.3 points and lexical--visual fusion adds 8.7, while four generic rerankers all reduce Gold-NDCG; these directions replicate on a four-source stress set.

**证据没有证明什么。** Sampled quote-backed repair and promotion sensitivity reduce, but cannot eliminate, false-negative risk. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24165v1#S3 — 3 Study Design; https://arxiv.org/html/2607.24165v1#S3.SS3 — 3.3 Systems and controlled interventions。Evaluation：https://arxiv.org/html/2607.24165v1#S4 — 4 Results; https://arxiv.org/html/2607.24165v1#as1_S10.SS6 — 10.6 Effect on Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.24165v1#S7 — 7 Scope, Limitations, and Release; https://arxiv.org/html/2607.24165v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Sampled quote-backed repair and promotion sensitivity reduce, but cannot eliminate, false-negative risk.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24165:end -->

<!-- review:SF-2026-ARXIV-2607-24167:start -->
### Falsifiable Commitment Planning for Self-Correcting Web Agents

<!-- claim:SF-2026-ARXIV-2607-24167:start -->Long-horizon web agents often go off track before final failure: a trajectory can remain locally plausible even after the current state, reused skill, or plan assumption no longer supports the user instruction. Existing agents can plan, reflect, or reuse experience, but their plans rarely specify the evidence under which an active step should still be trusted. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24167:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-horizon web agents often go off track before final failure: a trajectory can remain locally plausible even after the current state, reused skill, or plan assumption no longer supports the user instruction.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose FCPAgent, a falsifiable commitment planning framework for robust long-horizon web agents.

**证据证明什么。** On WebArena, FCPAgent achieves a 13.8% relative improvement in average success over the strongest baseline, with especially large gains on long-horizon tasks.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24167v1#S5 — 5 The Proposed Method; https://arxiv.org/html/2607.24167v1#A2 — Appendix B Implementation Details。Evaluation：https://arxiv.org/html/2607.24167v1#A2.SS6 — B.6 Dataset Split and Evaluation Protocol; https://arxiv.org/html/2607.24167v1#A3 — Appendix C Complementary Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.24167v1#A1 — Appendix A Discussion; https://arxiv.org/html/2607.24167v1#A2.SS4 — B.4 Implementation Details of the Failure-Repair Library。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24167:end -->

<!-- review:SF-2026-ARXIV-2607-24174:start -->
### Just Testing, Move Along: Evasion of LLM-based System Log Interpretation by Prompt Injection

<!-- claim:SF-2026-ARXIV-2607-24174:start -->Large Language Models (LLMs) are increasingly integrated into Security Operations Center (SOC) workflows, where they support analysts in tasks such as the interpretation of system logs. However, the ability of LLMs to directly process untrusted textual input also introduces new attack surfaces. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24174:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) are increasingly integrated into Security Operations Center (SOC) workflows, where they support analysts in tasks such as the interpretation of system logs.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this gap, this paper presents a framework for evaluating prompt injection attacks against LLM-based log interpretation.

**证据证明什么。** Our evaluation across multiple state-of-the-art LLMs shows that these injections can cause malicious log traces to be classified as benign despite containing clear indicators of compromise.

**证据没有证明什么。** A notable characteristic of the injections considered in this paper is that they may not only influence the LLM, but could also appear plausible to human analysts. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24174v1#S3.SS2 — 3.2. Threat Model。Evaluation：https://arxiv.org/html/2607.24174v1#S4 — 4. Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.24174v1#S3.SS2 — 3.2. Threat Model; https://arxiv.org/html/2607.24174v1#S5 — 5. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：A notable characteristic of the injections considered in this paper is that they may not only influence the LLM, but could also appear plausible to human analysts.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24174:end -->

<!-- review:SF-2026-ARXIV-2607-24223:start -->
### A New Role for Relevance: Guiding Corpus Interaction in Agentic Search

<!-- claim:SF-2026-ARXIV-2607-24223:start -->Relevance is a query-dependent estimate of whether a document or excerpt contains useful evidence. Existing retrieval agents use relevance to select top-$k$ content, but document relevance alone cannot localize, compose, or verify the evidence required by complex questions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24223:end -->

**为什么进入候选分母。** 摘要首要问题为“Relevance is a query-dependent estimate of whether a document or excerpt contains useful evidence.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce the Relevance-Aware RipGrep Search Agent (RARG), which turns relevance into an execution prior for corpus interaction.

**证据证明什么。** These results demonstrate that relevance-aware interaction enables faster and more reliable search convergence.

**证据没有证明什么。** Limitations RARG’s effectiveness depends on the quality of the relevance signal from the embedding model, and the two guidance levels place different demands on it: document-level ranking must score long documents, whereas match-level reranking must score short local excerpts. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24223v1#A1.SS1 — A.1 System Prompt of BC+; https://arxiv.org/html/2607.24223v1#A1.SS2 — A.2 System Prompt of BRIGHT。Evaluation：https://arxiv.org/html/2607.24223v1#S4 — 4 Experiments; https://arxiv.org/html/2607.24223v1#S4.SS1 — 4.1 Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24223v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.24223v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/LeqsNaN/RARG, https://github.com/texttron/RISE, https://github.com/NVIDIA/NeMo-Retriever/tree/main/retrieval-bench; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Limitations RARG’s effectiveness depends on the quality of the relevance signal from the embedding model, and the two guidance levels place different demands on it: document-level ranking must score long documents, whereas match-level reranking must score short local excerpts.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24223:end -->

<!-- review:SF-2026-ARXIV-2607-24260:start -->
### KAP: Bridging the Knowledge Selection-Runtime Consumption Gap in LLM Systems

<!-- claim:SF-2026-ARXIV-2607-24260:start -->Modern LLM systems increasingly rely on knowledge-selection processes that produce high-value structured priors, such as ranked evidence, graph topology, multimodal alignment, and confidence signals. Yet LLM serving remains fundamentally oblivious to this rich structure: once such signals are serialized into a prompt, the backend observes only a flat token sequence, forcing dense and uniform consumption of the full key-value (KV) state during decoding. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24260:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern LLM systems increasingly rely on knowledge-selection processes that produce high-value structured priors, such as ranked evidence, graph topology, multimodal alignment, and confidence signals.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Modern LLM systems increasingly rely on knowledge-selection processes that produce high-value structured priors, such as ranked evidence, graph topology, multimodal alignment, and confidence signals.

**证据证明什么。** Across 4K-128K long-context QA workloads, GraphSpec maintains answer quality comparable to full-context decoding while decoupling physical KV consumption from prompt length, reducing proposal-time KV access to 5.5% of source KV state at 128K, and fundamentally shifting the scaling trajectory of long-context generation.

**证据没有证明什么。** Therefore, our empirical evidence does not exhaust the broader design space of runtime knowledge consumption. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24260v1#S2.SS2 — 2.2 KAP compiler–executor architecture; https://arxiv.org/html/2607.24260v1#S4 — 4 Cost Model and Phase-Boundary Analysis。Evaluation：https://arxiv.org/html/2607.24260v1#S4 — 4 Cost Model and Phase-Boundary Analysis; https://arxiv.org/html/2607.24260v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.24260v1#S7 — 7 Limitations; https://arxiv.org/html/2607.24260v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Therefore, our empirical evidence does not exhaust the broader design space of runtime knowledge consumption.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24260:end -->

<!-- review:SF-2026-ARXIV-2607-24267:start -->
### FeelWorld: Visuo-Tactile World Model for Hierarchical Contact Prediction and Planning

<!-- claim:SF-2026-ARXIV-2607-24267:start -->Humans plan physical interactions by imagining the possible outcomes of candidate actions. However, existing visual world models primarily capture appearance dynamics while overlooking the tactile states that govern contact-rich interactions, potentially producing imagined futures that appear visually plausible but violate physical dynamics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24267:end -->

**为什么进入候选分母。** 摘要首要问题为“Humans plan physical interactions by imagining the possible outcomes of candidate actions.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce FeelWorld, a hierarchical visuo-tactile world model that jointly predicts future visual latents and three tactile states.

**证据证明什么。** Experiments on chip grasping, fruit grasping, and USB insertion show that FeelWorld reduces 10-step LPIPS from 0.084 to 0.058 and maintains an LPIPS that is 61% lower than that of the visual baseline after an 80-step autoregressive rollout.

**证据没有证明什么。** Despite these results, CEM-based planning remains computationally expensive and is not suitable for high-frequency real-time control. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24267v1#S3 — III Method; https://arxiv.org/html/2607.24267v1#S2.SS1 — II-A Action-Conditioned World Models。Evaluation：https://arxiv.org/html/2607.24267v1#S4 — IV Experiments; https://arxiv.org/html/2607.24267v1#S4.SS1 — IV-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24267v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Despite these results, CEM-based planning remains computationally expensive and is not suitable for high-frequency real-time control.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24267:end -->

<!-- review:SF-2026-ARXIV-2607-24268:start -->
### Accuracy Hides How Language Models Fail: Measuring Failure States Under Matched Output Budgets

<!-- claim:SF-2026-ARXIV-2607-24268:start -->Language-model benchmarks collapse two distinct measurement questions into a single accuracy score: whether a response reached an evaluable state, and whether its answer was judged correct. We introduce a two-layer evaluation framework that separates scorer-independent execution evidence, including termination, answer exposure, parseability, and completion length, from scorer-dependent correctness. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24268:end -->

**为什么进入候选分母。** 摘要首要问题为“Language-model benchmarks collapse two distinct measurement questions into a single accuracy score: whether a response reached an evaluable state, and whether its answer was judged correct.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce a two-layer evaluation framework that separates scorer-independent execution evidence, including termination, answer exposure, parseability, and completion length, from scorer-dependent correctness.

**证据证明什么。** These results demonstrate that accuracy conflates execution case mix with verification policy.

**证据没有证明什么。** The Qwen Natural ledger did not retain complete response bodies; its later scoring analysis relies on parsed answers and response hashes rather than independent raw-text reparse. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24268v1#S3 — III Measurement Design; https://arxiv.org/html/2607.24268v1#S3.SS2 — III-B Questions, Models, and Prompts。Evaluation：https://arxiv.org/html/2607.24268v1#S4 — IV Results。Limitations / counterevidence：https://arxiv.org/html/2607.24268v1#S4.SS1 — IV-A Failure Mixtures Vary across Studied Configurations; https://arxiv.org/html/2607.24268v1#S5 — V Implications and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The Qwen Natural ledger did not retain complete response bodies; its later scoring analysis relies on parsed answers and response hashes rather than independent raw-text reparse.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24268:end -->

<!-- review:SF-2026-ARXIV-2607-24280:start -->
### From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent Protocol Distillation in Agentic Search

<!-- claim:SF-2026-ARXIV-2607-24280:start -->Agentic search enables large language models to solve knowledge-intensive tasks by interleaving multi-step reasoning with retrieval, yet optimizing this with outcome-based reinforcement learning (RL) provides only sparse supervision. Knowledge distillation can supply denser guidance, and advanced proprietary models with their strong reasoning capabilities are promising teachers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24280:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic search enables large language models to solve knowledge-intensive tasks by interleaving multi-step reasoning with retrieval, yet optimizing this with outcome-based reinforcement learning (RL) provides only sparse supervision.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address the heterogeneous distillation problem and bridge the distribution gap, we propose Multi-Agent Protocol Distillation (MAPD), a joint distillation and RL framework uses a structured, style-normalized protocol as an intermediate representation.

**证据证明什么。** Extensive evaluations across seven QA benchmarks demonstrate that MAPD consistently outperforms competitive distillation and RL, achieving average success rates of 39.4\% on Qwen3-1.7B and 44.4\% on Qwen3-4B.

**证据没有证明什么。** Extensive evaluations across seven knowledge-intensive QA benchmarks demonstrate that MAPD not only consistently outperforms all evaluated baselines, but also generalizes seamlessly across different proprietary teachers without retuning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24280v1#S3 — 3 Methodology; https://arxiv.org/html/2607.24280v1#S3.SS2 — 3.2 Multi-Agent System Generation Pipeline。Evaluation：https://arxiv.org/html/2607.24280v1#S4 — 4 Experiments and Analysis; https://arxiv.org/html/2607.24280v1#S4.SS2 — 4.2 Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.24280v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/AaronLiu0702/MAPD, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Extensive evaluations across seven knowledge-intensive QA benchmarks demonstrate that MAPD not only consistently outperforms all evaluated baselines, but also generalizes seamlessly across different proprietary teachers without retuning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24280:end -->

<!-- review:SF-2026-ARXIV-2607-24300:start -->
### Self-Authored Verification Is Unreliable in Heuristic Self-Improving Agents

<!-- claim:SF-2026-ARXIV-2607-24300:start -->Self-improving agents accumulate capability by repeatedly rewriting procedural policies, controllers, or heuristic rules. They typically rely on self-authored tests or metrics to decide whether to accept subsequent edits. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24300:end -->

**为什么进入候选分母。** 摘要首要问题为“Self-improving agents accumulate capability by repeatedly rewriting procedural policies, controllers, or heuristic rules.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this problem, we introduce a Sealed Exogenous Acceptance Loop (SEAL).

**证据证明什么。** Our experiments show that this problem often appears in heuristic learning settings.

**证据没有证明什么。** The results suggest that reliable self-improvement requires a low-leakage exogenous acceptance signal that the agent cannot write, observe, or directly optimize. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24300v1#Sx3.SSx4 — Design Conditions。Evaluation：https://arxiv.org/html/2607.24300v1#Sx4 — Experiments; https://arxiv.org/html/2607.24300v1#Sx4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24300v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The results suggest that reliable self-improvement requires a low-leakage exogenous acceptance signal that the agent cannot write, observe, or directly optimize.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24300:end -->

<!-- review:SF-2026-ARXIV-2607-24306:start -->
### Rethinking the Generation Order of Block Diffusion Language Models

<!-- claim:SF-2026-ARXIV-2607-24306:start -->Diffusion language models enable flexible arbitrary-order generation, but existing sampling methods are mostly designed for early masked diffusion models (MDMs). In this work, we study sampling for recent block diffusion language models (BDLMs). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24306:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion language models enable flexible arbitrary-order generation, but existing sampling methods are mostly designed for early masked diffusion models (MDMs).”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Based on this observation, we propose Parallel Autoregressive Decoding (PARD), a simple training-free sampling method that preserves left-to-right unmasking structure while allowing parallel token commitment.

**证据证明什么。** Extensive experiments show that PARD consistently outperforms existing parallel samplers in generation quality, while achieving substantial speedups over pure AR decoding with only a small quality gap.

**证据没有证明什么。** Limitations Our study focuses on inference-time sampling for recent block diffusion language models, and does not modify the training objective. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24306v1#S2.SS2 — 2.2 Sampling Methods for MDMs; https://arxiv.org/html/2607.24306v1#A3.SS1 — C.1 Model Checkpoints。Evaluation：https://arxiv.org/html/2607.24306v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.24306v1#A3.SS4 — C.4 Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.24306v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.24306v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/EleutherAI/lm-evaluation-harness, https://huggingface.co/Efficient-Large-Model/Fast_dLLM_v2_7B, https://huggingface.co/JetLM/SDAR-8B-Chat-b32; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Limitations Our study focuses on inference-time sampling for recent block diffusion language models, and does not modify the training objective.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24306:end -->

<!-- review:SF-2026-ARXIV-2607-24331:start -->
### DynaCalKV: Key-Value Cache Compression via Head Grouping and Adaptive Rank Allocation

<!-- claim:SF-2026-ARXIV-2607-24331:start -->As the inference phase of Large Language Models (LLMs) requires handling long context windows, the Key-Value (KV) cache initially appears to address this challenge but eventually becomes a significant bottleneck as the context window continues to grow. Low-rank compression has recently been studied as an effective approach to reduce KV cache memory while maintaining model performance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24331:end -->

**为什么进入候选分母。** 摘要首要问题为“As the inference phase of Large Language Models (LLMs) requires handling long context windows, the Key-Value (KV) cache initially appears to address this challenge but eventually becomes a significant bottleneck as the context window continues to grow.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we propose an improved low-rank KV cache compression framework.

**证据证明什么。** Experimental results on three instruction-tuned LLMs show that our method reduces the number of Key cache parameters while maintaining competitive accuracy.

**证据没有证明什么。** Experimental results on three instruction-tuned LLMs reveal that the effectiveness of DynaCalKV depends heavily on the underlying architecture: it is particularly well-suited for standard MHA architectures, whereas it should be applied more conservatively on models already utilizing GQA during long-context tasks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24331v1#S3 — III Methodology。Evaluation：https://arxiv.org/html/2607.24331v1#S4 — IV Experiments; https://arxiv.org/html/2607.24331v1#S4.SS1 — IV-A Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.24331v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Experimental results on three instruction-tuned LLMs reveal that the effectiveness of DynaCalKV depends heavily on the underlying architecture: it is particularly well-suited for standard MHA architectures, whereas it should be applied more conservatively on models already utilizing GQA during long-context tasks.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24331:end -->

<!-- review:SF-2026-ARXIV-2607-24343:start -->
### Beyond Aggregate Risk: Role-Stratified Conformal Risk Control for LLM Tool Calls

<!-- claim:SF-2026-ARXIV-2607-24343:start -->Language-model agents act through structured tool calls whose arguments carry very different risks: untrusted content may legitimately shape an email body but should never set a recipient, account, command, or credential. Existing conformal risk control methods certify a tool call as a whole, so a failure in one rare high-risk field can be averaged away by the many benign arguments around it, leaving the argument that causes harm uncertified. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24343:end -->

**为什么进入候选分母。** 摘要首要问题为“Language-model agents act through structured tool calls whose arguments carry very different risks: untrusted content may legitimately shape an email body but should never set a recipient, account, command, or credential.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce role-stratified per-field conformal risk control, a calibration layer that wraps any per-field detector and assigns a separate threshold and risk budget to each semantic argument role.

**证据证明什么。** These results suggest that structured tool calls should be certified at the semantic-role level, not the whole action.

**证据没有证明什么。** Aggregate CRC satisfies the global budget while target violation remains above its role-specific limit. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24343v1#Sx5 — Method: Role-Stratified Per-Field CRC; https://arxiv.org/html/2607.24343v1#Sx3 — Problem Setup and Threat Model。Evaluation：https://arxiv.org/html/2607.24343v1#A3 — Appendix C Certifiability and Deployable-Detector Results; https://arxiv.org/html/2607.24343v1#Sx6 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.24343v1#Sx7 — Discussion and Limitations; https://arxiv.org/html/2607.24343v1#A2 — Appendix B The Aggregate-Budget Failure: Full Evidence。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Aggregate CRC satisfies the global budget while target violation remains above its role-specific limit.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24343:end -->

<!-- review:SF-2026-ARXIV-2607-24368:start -->
### Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory

<!-- claim:SF-2026-ARXIV-2607-24368:start -->Long-term memory systems store what a user says in an external store and retrieve it when a related query arrives. This interface rests on an assumption so natural that it is rarely stated: a memory that is needed will resemble the query that needs it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24368:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-term memory systems store what a user says in an external store and retrieve it when a related query arrives.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Long-term memory systems store what a user says in an external store and retrieve it when a related query arrives.

**证据证明什么。** A minimal diagnostic probe that keeps memory visible before the query arrives recovers most of the gap, locating the failure in the query-conditioned interface itself and pointing to routing, deciding which facts must stay visible, as the open problem InMind is built to score.

**证据没有证明什么。** The bias applies to the backbone control and the retrieval systems alike and cannot manufacture the gap between them, and the expert audit in Appendix 14.2 bounds the error of each judge; still, an independent judge model remains the most significant methodological gap. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24368v1#S12 — 12 Representative System Responses; https://arxiv.org/html/2607.24368v1#S15 — 15 System Hyperparameters。Evaluation：https://arxiv.org/html/2607.24368v1#S10 — 10 Memory-Benchmark Taxonomy; https://arxiv.org/html/2607.24368v1#S14 — 14 Automatic Evaluation Prompts。Limitations / counterevidence：https://arxiv.org/html/2607.24368v1#S4 — 4 Experiments: Locating the Failure; https://arxiv.org/html/2607.24368v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/imlrz/InMind, https://abc.xyz/investor/board-and-governance/google-code-of-conduct/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The bias applies to the backbone control and the retrieval systems alike and cannot manufacture the gap between them, and the expert audit in Appendix 14.2 bounds the error of each judge; still, an independent judge model remains the most significant methodological gap.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24368:end -->

<!-- review:SF-2026-ARXIV-2607-24377:start -->
### MXAttention: Data-Free Optimal Scaling and Pre-Normalization Quantization for MXFP4 Attention

<!-- claim:SF-2026-ARXIV-2607-24377:start -->The quadratic cost of attention is a major bottleneck in diffusion-based video generation models. MXFP4 attention provides a promising path toward efficient inference, but direct MXFP4 quantization often degrades generation quality due to two numerical issues: the clipping-underflow trade-off from power-of-two scaling and the row-wise normalization error introduced in the softmax loop. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24377:end -->

**为什么进入候选分母。** 摘要首要问题为“The quadratic cost of attention is a major bottleneck in diffusion-based video generation models.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose MXAttention, a data-free post-training quantization framework for MXFP4 attention.

**证据证明什么。** Experiments on Wan2.2 and HunyuanVideo show that MXAttention closes at least 95% of the VBench Imaging Quality gap between OCP MXFP4 and FP16, substantially improves frame-level similarity, and preserves FP16-level generation quality with less than 0.01 absolute degradation on all reported VBench metrics.

**证据没有证明什么。** UOS changes only the shared-scale selection, and PNQ reuses the quantized exponential tiles already required by the low-precision output path; neither requires an additional pass over the attention matrix. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24377v1#S5.SS6 — 5.6 Algorithmic Overhead and Kernel Integration。Evaluation：https://arxiv.org/html/2607.24377v1#S5 — 5 Experiments; https://arxiv.org/html/2607.24377v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24377v1#S3 — 3 Failure Modes of Standard MXFP4 Attention; https://arxiv.org/html/2607.24377v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://gitcode.com/Ascend/MindIE-SD/tree/master/mindiesd, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：UOS changes only the shared-scale selection, and PNQ reuses the quantized exponential tiles already required by the low-precision output path; neither requires an additional pass over the attention matrix.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24377:end -->

<!-- review:SF-2026-ARXIV-2607-24392:start -->
### When LLM Defenses Backfire: Characterizing Safety, Performance, and Cost Trade-offs

<!-- claim:SF-2026-ARXIV-2607-24392:start -->Jailbreak defenses are essential for protecting large language models (LLMs), but they can also introduce secondary costs that weaken model utility. We present a systematic study of these defense trade-offs along three dimensions: performance impact, over-refusal on benign inputs, and inference cost. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24392:end -->

**为什么进入候选分母。** 摘要首要问题为“Jailbreak defenses are essential for protecting large language models (LLMs), but they can also introduce secondary costs that weaken model utility.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present a systematic study of these defense trade-offs along three dimensions: performance impact, over-refusal on benign inputs, and inference cost.

**证据证明什么。** Across state-of-the-art defense methods, widely used benchmark datasets, and representative open-source LLMs, we find that defenses rarely improve downstream capability, but instead vary in how they trade safety gains against usability and efficiency.

**证据没有证明什么。** Finally, our findings are a snapshot against today’s jailbreak corpora and may not generalize to stronger future attacks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24392v1#S3 — 3 Methodology; https://arxiv.org/html/2607.24392v1#S2.SS3 — 2.3 Threat Model。Evaluation：https://arxiv.org/html/2607.24392v1#S4.SS2 — 4.2 Results; https://arxiv.org/html/2607.24392v1#S5.SS2 — 5.2 Results。Limitations / counterevidence：https://arxiv.org/html/2607.24392v1#A3 — Appendix C Limitations; https://arxiv.org/html/2607.24392v1#S2.SS3 — 2.3 Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Finally, our findings are a snapshot against today’s jailbreak corpora and may not generalize to stronger future attacks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24392:end -->

<!-- review:SF-2026-ARXIV-2607-24407:start -->
### Mixture-of-Thought-Tokens: Unifying Perception and Reasoning for Free-form Multimodal Grounding

<!-- claim:SF-2026-ARXIV-2607-24407:start -->Multimodal Large Language Models have made great progress in grounding tasks, yet existing methods still struggle to unify precise localization and complex reasoning. For one thing, text-based methods rely on coordinates or index prediction, severely limiting the perceptual capabilities of the model for dense visual objects. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24407:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal Large Language Models have made great progress in grounding tasks, yet existing methods still struggle to unify precise localization and complex reasoning.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To address this, we propose Mixture-of-Thought-Tokens (Motto), a new free-form multimodal grounding method that bridges the perception-reasoning gap, enabling MLLMs to empower diverse, arbitrary grounding queries.

**证据证明什么。** Extensive experiments demonstrate that Motto achieves state-of-the-art performance across diverse free-form grounding tasks.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24407v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.24407v1#A1 — Appendix A In-Depth Analysis; https://arxiv.org/html/2607.24407v1#A1.SS2 — A.2 Efficiency Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.24407v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/TG0110/Motto, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24407:end -->

<!-- review:SF-2026-ARXIV-2607-24434:start -->
### DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference

<!-- claim:SF-2026-ARXIV-2607-24434:start -->Large Mixture-of-Experts (MoE) language models are attractive for end-device deployment because only a small subset of experts is active per token, but their routed expert weights often exceed accelerator memory. We target latency-critical single-user settings where routed experts are staged on demand from CPU memory to a GPU or from Flash to a mobile NPU. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24434:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Mixture-of-Experts (MoE) language models are attractive for end-device deployment because only a small subset of experts is active per token, but their routed expert weights often exceed accelerator memory.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose DraftExpert, an expansion-aware self-speculative decoding framework for expert-offloaded MoE inference.

**证据证明什么。** On DeepSeek-V2-Lite and Moonlight-16B-A3B across CPU-GPU and Flash-NPU offload, DraftExpert improves decode throughput by 1.45x on average, raises draft acceptance to 84~87%, and achieves 86~88% prefetch hit rates.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24434v1#Sx3 — DraftExpert Method。Evaluation：https://arxiv.org/html/2607.24434v1#Sx4 — Experimental Evaluation; https://arxiv.org/html/2607.24434v1#Sx4.SSx5 — Training Objective Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.24434v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf, https://github.com/ggerganov/llama.cpp, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24434:end -->

<!-- review:SF-2026-ARXIV-2607-24440:start -->
### Bigger or Cheaper? Scale and Quantization Effects on Uncertainty Signals in Vision-Language Models Under Image Degradation

<!-- claim:SF-2026-ARXIV-2607-24440:start -->Vision-language models (VLMs) deployed on consumer hardware must decide when to answer and when to defer, and that decision depends on having a confidence signal that tracks correctness. A practitioner with a fixed memory budget faces a choice between a small model at full precision, the same small model quantized, and a larger model quantized into the same footprint -- three configurations that push the confidence signal in opposing directions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24440:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language models (VLMs) deployed on consumer hardware must decide when to answer and when to defer, and that decision depends on having a confidence signal that tracks correctness.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** A practitioner with a fixed memory budget faces a choice between a small model at full precision, the same small model quantized, and a larger model quantized into the same footprint -- three configurations that push the confidence signal in opposing directions.

**证据证明什么。** Across 5,700 predictions spanning six realistic photographic degradations at three severities, we find that scale sharply improves the model's internal uncertainty signal (mean error-detection AUROC 0.80 to 0.98 from 2B to 7B) while its verbalized confidence stays weak and often at chance (mean 0.61 to 0.69): the gap between what the model knows and what it says widens rather than closes with size.

**证据没有证明什么。** 6 Limitations Two scale points give a direction, not a scaling law, and cannot locate an emergence threshold. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24440v1#S3 — 3 Method; https://arxiv.org/html/2607.24440v1#S3.SS1 — 3.1 Experimental design。Evaluation：https://arxiv.org/html/2607.24440v1#S3.SS1 — 3.1 Experimental design; https://arxiv.org/html/2607.24440v1#S3.SS8 — 3.8 Selective prediction analysis。Limitations / counterevidence：https://arxiv.org/html/2607.24440v1#S5 — 5 Discussion; https://arxiv.org/html/2607.24440v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：6 Limitations Two scale points give a direction, not a scaling law, and cannot locate an emergence threshold.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24440:end -->

<!-- review:SF-2026-ARXIV-2607-24459:start -->
### From Execution to Capability: Scientific Experience Consolidation via Procedural Knowledge Synthesis

<!-- claim:SF-2026-ARXIV-2607-24459:start -->Large language models increasingly solve scientific-computing tasks, but executable feedback from one problem rarely becomes durable capability on subsequent problems. We study scientific-computing experience consolidation: converting verified runtime experience into transferable procedural knowledge and persistent model improvement. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24459:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models increasingly solve scientific-computing tasks, but executable feedback from one problem rarely becomes durable capability on subsequent problems.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce SciConsolidate, which contrasts verified successes and failures to induce cross-task procedures, selects them through a development-validation gate, and uses failure-informed, answer-free query synthesis to expand the consolidation data without requiring pre-existing reference answers.

**证据证明什么。** We study scientific-computing experience consolidation: converting verified runtime experience into transferable procedural knowledge and persistent model improvement.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24459v1#A1 — Appendix A Additional Method Details; https://arxiv.org/html/2607.24459v1#A2.SS4 — B.4 Runtime Procedure Effects Across Model Groups。Evaluation：https://arxiv.org/html/2607.24459v1#A2 — Appendix B Additional Experiment Diagnostics; https://arxiv.org/html/2607.24459v1#A2.SS6 — B.6 Diagnostic Takeaways from Fine-Grained Results。Limitations / counterevidence：https://arxiv.org/html/2607.24459v1#S6 — 6 Conclusion and Limitations; https://arxiv.org/html/2607.24459v1#A1.SS2 — A.2 Failure-Mode Induction and Skill-Distillation Prompts。

**Artifact boundary。** Exact v1 links https://github.com/ScienceOne-AI/SciConsolidate, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24459:end -->

<!-- review:SF-2026-ARXIV-2607-24471:start -->
### Grounding latent algorithm routing in transformer reasoning

<!-- claim:SF-2026-ARXIV-2607-24471:start -->A central question in the in-context learning literature is whether transformers can organize episode-level adaptation around different inductive-bias families. We study this question in a controlled setting through latent algorithm routing: route-like behavior in which the solver-family preference changes with the latent data-generating regime while prompt form is held fixed, remains stable under nuisance perturbations, and is selectively influenced by targeted activation interventions without large losses in answer quality. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24471:end -->

**为什么进入候选分母。** 摘要首要问题为“A central question in the in-context learning literature is whether transformers can organize episode-level adaptation around different inductive-bias families.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce ROUTEBENCH, a diagnostic benchmark whose regimes differentially favor global shrinkage, sparsity, robustness, and locality, operationalized by ridge-like, lasso-like, Huber-like, and kNN-like family representatives.

**证据证明什么。** Across dense decoder-only transformers trained from scratch at 44M-612M parameters, a 306M model closes 80.9 percent of the oracle-routing gap and achieves route F1 of 84.1.

**证据没有证明什么。** Probe permutation controls, margin-filtered analyses, and matched patching controls indicate that route-relevant information is not merely a formatting artifact or arbitrary post-hoc label. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24471v1#S4 — 4 Benchmark and experimental design; https://arxiv.org/html/2607.24471v1#S3 — 3 Grounding latent algorithm routing。Evaluation：https://arxiv.org/html/2607.24471v1#A3 — Appendix C Additional experimental results; https://arxiv.org/html/2607.24471v1#S4 — 4 Benchmark and experimental design。Limitations / counterevidence：https://arxiv.org/html/2607.24471v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/xiangbo05/RouteBench, https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-35/issue-1/Robust-Estimation-of-a-Location-Parameter/10.1214/aoms/1177703732.full, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Probe permutation controls, margin-filtered analyses, and matched patching controls indicate that route-relevant information is not merely a formatting artifact or arbitrary post-hoc label.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24471:end -->

<!-- review:SF-2026-ARXIV-2607-24481:start -->
### ArmnetBench v0.1: Parallel Real-World Evaluation of Manipulation Policies on a Low-Cost Arm Farm

<!-- claim:SF-2026-ARXIV-2607-24481:start -->Real-world evaluation is a bottleneck in developing generalist robot manipulation policies. Each rollout requires physical hardware and an operator to set up, reset, and score it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24481:end -->

**为什么进入候选分母。** 摘要首要问题为“Real-world evaluation is a bottleneck in developing generalist robot manipulation policies.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce ArmnetBench v0.1, a benchmark run on a fleet of low-cost SO-101 cells under light on-site supervision. v0.1 validates this arm farm end to end and compares 7 policies across 12 tasks with both single-arm and bimanual configurations.

**证据证明什么。** We release the 3,118 core episodes in LeRobot v3.0 and RoboMeter formats.

**证据没有证明什么。** Unknown training distributions may also preclude strict in- versus out-of-distribution classification. • Unstandardised rollout duration. v0.1 did not enforce fixed per-task wall-clock limits. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24481v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24481v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.24481v1#S3.SS2 — 3.2 Running an evaluation; https://arxiv.org/html/2607.24481v1#S4 — 4 The ArmnetBench Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.24481v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.24481v1#S7 — 7 Future Work。

**Artifact boundary。** Exact v1 links https://github.com/TheRobotStudio/SO-ARM100/tree/main/Optional/Overhead_Cam_Mount_Webcam, https://huggingface.co/collections/armnet/armnetbench-v01, https://github.com/huggingface/lerobot; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Unknown training distributions may also preclude strict in- versus out-of-distribution classification. • Unstandardised rollout duration. v0.1 did not enforce fixed per-task wall-clock limits.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24481:end -->

<!-- review:SF-2026-ARXIV-2607-24484:start -->
### What do Reward Models Memorize?

<!-- claim:SF-2026-ARXIV-2607-24484:start -->This paper studies what discriminatively trained reward models (RMs) memorize by measuring counterfactual memorization on two human preference datasets. We show that RMs 1) misallocate memorization to easy, high margin preference pairs, 2) memorize dataset-specific shortcuts (e.g., model identity, user sampling strategy), and 3) overgeneralize simple heuristic correlates of human preference (e.g., length, compliance) when confronted with unseen preference pairs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24484:end -->

**为什么进入候选分母。** 摘要首要问题为“This paper studies what discriminatively trained reward models (RMs) memorize by measuring counterfactual memorization on two human preference datasets.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We show that RMs 1) misallocate memorization to easy, high margin preference pairs, 2) memorize dataset-specific shortcuts (e.g., model identity, user sampling strategy), and 3) overgeneralize simple heuristic correlates of human preference (e.g., length, compliance) when confronted with unseen preference pairs.

**证据证明什么。** Overall, our findings indicate that discriminative training of RMs from human preference data results in biased RMs not yet capable of judging response quality in context-dependent scenarios.

**证据没有证明什么。** For example, the RM might overfit to the training data and memorize dataset-dependent heuristic shortcut features that correlate but do not cause human preference. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.24484v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24484v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.24484v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24484v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.24484v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24484v1#page=10 — PDF page 10。

**Artifact boundary。** Exact v1 links https://github.com/ioverho/rm-shortcuts; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：For example, the RM might overfit to the training data and memorize dataset-dependent heuristic shortcut features that correlate but do not cause human preference.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24484:end -->

<!-- review:SF-2026-ARXIV-2607-24485:start -->
### τ: Learning Touch-Augmented Vision-Language-Action Models from Future Visual Supervision

<!-- claim:SF-2026-ARXIV-2607-24485:start -->Incorporating tactile sensing into Vision-Language-Action (VLA) models holds promise for contact-rich manipulation, where visual observations alone often fail to capture critical cues about physical interactions. However, learning informative tactile representation while effectively adapting it to pretrained VLA models remains challenging under limited task-specific data. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24485:end -->

**为什么进入候选分母。** 摘要首要问题为“Incorporating tactile sensing into Vision-Language-Action (VLA) models holds promise for contact-rich manipulation, where visual observations alone often fail to capture critical cues about physical interactions.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To address these challenges, we present τ, a touch-augmented VLA framework that learns an action-conditioned spatiotemporal tactile representation from future visual supervision inspired by the Joint-Embedding Predictive Architecture (JEPA), and fuses it with vision-language features for action generation.

**证据证明什么。** Experiments show that τ outperforms existing models and generalizes to unseen objects and scenes, delivering improved manipulation performance and robustness.

**证据没有证明什么。** Furthermore, we proposed an auxiliary JEPA-style predictive self-supervised branch that learns temporally consistent multimodal representations through latent future prediction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24485v1#Sx3.SSx1 — Model Architecture; https://arxiv.org/html/2607.24485v1#Sx3 — The Model。Evaluation：https://arxiv.org/html/2607.24485v1#Sx4 — Experiments; https://arxiv.org/html/2607.24485v1#Sx4.SSx1 — Experimental Setups。Limitations / counterevidence：https://arxiv.org/html/2607.24485v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Furthermore, we proposed an auxiliary JEPA-style predictive self-supervised branch that learns temporally consistent multimodal representations through latent future prediction.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24485:end -->

<!-- review:SF-2026-ARXIV-2607-24507:start -->
### UNIFUSION: Adapting Autoregressive Language Models into Discrete Diffusion under a Unified Reverse-Rate Objective

<!-- claim:SF-2026-ARXIV-2607-24507:start -->Existing methods mainly adapt pretrained autoregressive (AR) language models to masked diffusion, whereas we directly adapt them to uniform-noise diffusion, where every token remains editable during sampling. However, adapting AR checkpoints across corruption kernels remains challenging because existing DLMs use different objectives and prediction parameterizations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24507:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing methods mainly adapt pretrained autoregressive (AR) language models to masked diffusion, whereas we directly adapt them to uniform-noise diffusion, where every token remains editable during sampling.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Building on these connections, we propose \ours{}, a simple continual pre-training approach for directly adapting pretrained GPT2 checkpoints to uniform-noise diffusion.

**证据证明什么。** At 256 steps, \ours{}-S and \ours{}-M achieve GenPPL/entropy pairs of \(97.783/5.2626\) and \(71.516/5.6669\), respectively; no evaluated model at the same scale simultaneously outperforms \ours{} on both metrics.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24507v1#S3 — 3 Methodology; https://arxiv.org/html/2607.24507v1#S3.SS2 — 3.2 Method。Evaluation：https://arxiv.org/html/2607.24507v1#A3 — Appendix C Additional experimental details; https://arxiv.org/html/2607.24507v1#A3.SS4 — C.4 Downstream Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.24507v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24507:end -->

<!-- review:SF-2026-ARXIV-2607-24516:start -->
### DecoupleMix: Decoupled Ratio Search and Convex Allocation for Scalable VLM Data Recipes

<!-- claim:SF-2026-ARXIV-2607-24516:start -->While data curation for Vision Language Models (VLMs) is increasingly active, public practice for constructing pretraining mixtures remains largely heuristic: practitioners stack datasets that pass quality filters, set cross-domain ratios by intuition, and lack a principled, attributable criterion for admitting new data, while frontier recipes remain undisclosed. We formulate data construction as a systematic mixture-optimization problem and turn it into a reproducible engineering discipline by decoupling the mixture into two orthogonal sub-problems: inter-class ratios across capabilities and intra-class ratios within a category. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24516:end -->

**为什么进入候选分母。** 摘要首要问题为“While data curation for Vision Language Models (VLMs) is increasingly active, public practice for constructing pretraining mixtures remains largely heuristic: practitioners stack datasets that pass quality filters, set cross-domain ratios by intuition, and lack a principled, attributable criterion for admitting new data, while frontier recipes remain undisclosed.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** The DecoupleMix framework delivers two critical capabilities: guiding what data to collect next and rendering dataset validation a controlled, attributable experiment.

**证据证明什么。** Experiments show our approach consistently surpasses heuristic baselines.

**证据没有证明什么。** 6 Limitations Several limitations remain and point to future work. (1) Scaling scope: our study spans 2.5B–10B tokens with model-scale transfer evaluated at 32B parameters; we have not released the trend at the much larger token budgets of frontier industrial pretraining. (2) Optimization algorithms: the single-variable inter-class search and convex intra-class program are deliberately tractable but likely suboptimal—richer joint search or more expressive objectives could improve the recipes. (3) Modality coverage: we validate only on vision–language models, leaving the extension to fully omni-modal models (audio, video, etc.) untested. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24516v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.24516v1#S4 — 4 Experiment Results and Analysis; https://arxiv.org/html/2607.24516v1#A1 — Appendix A Detailed Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.24516v1#S6 — 6 Limitations; https://arxiv.org/html/2607.24516v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：6 Limitations Several limitations remain and point to future work. (1) Scaling scope: our study spans 2.5B–10B tokens with model-scale transfer evaluated at 32B parameters; we have not released the trend at the much larger token budgets of frontier industrial pretraining. (2) Optimization algorithms: the single-variable inter-class search and convex intra-class program are deliberately tractable but likely suboptimal—richer joint search or more expressive objectives could improve the recipes. (3) Modality coverage: we validate only on vision–language models, leaving the extension to fully omni-modal models (audio, video, etc.) untested.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24516:end -->

<!-- review:SF-2026-ARXIV-2607-24539:start -->
### Task-Conditional Faithfulness Auditing of Multimodal LLMs for Grid Diagnosis

<!-- claim:SF-2026-ARXIV-2607-24539:start -->Multimodal large language models (LLMs) can combine topology, measurements, and incident text for grid diagnosis, yet answer accuracy does not establish that task-appropriate evidence was used. This letter proposes a general framework in order to conduct task-conditional faithfulness audit. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24539:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal large language models (LLMs) can combine topology, measurements, and incident text for grid diagnosis, yet answer accuracy does not establish that task-appropriate evidence was used.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** This letter proposes a general framework in order to conduct task-conditional faithfulness audit.

**证据证明什么。** These results validate the framework ability to detect, diagnose, and correct task-conditional faithfulness failures.

**证据没有证明什么。** Future work will evaluate the audit in utility-scale grid workflows. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24539v1#S2 — II Methodology; https://arxiv.org/html/2607.24539v1#S2.SS5 — II-E Implementation and Adaptation。Evaluation：https://arxiv.org/html/2607.24539v1#S3.SS1 — III-A Subcase A: Cross-Model Validation and Ablation; https://arxiv.org/html/2607.24539v1#S3 — III Case Study。Limitations / counterevidence：https://arxiv.org/html/2607.24539v1#S4 — IV Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work will evaluate the audit in utility-scale grid workflows.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24539:end -->

<!-- review:SF-2026-ARXIV-2607-24555:start -->
### LOCKS: Page-Local Compact Key Summaries for Efficient Long-Context Decoding

<!-- claim:SF-2026-ARXIV-2607-24555:start -->Serving large language models at long context is bottlenecked by the key-value (KV) cache, which is read in full at every decode step. Attention keys are locally low-rank though globally high-rank: a fixed low-rank sketch shared across pages is provably blind to page-specific directions, while at the same summary size a page's own basis ranks pages and keeps carriers far better. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24555:end -->

**为什么进入候选分母。** 摘要首要问题为“Serving large language models at long context is bottlenecked by the key-value (KV) cache, which is read in full at every decode step.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Attention keys are locally low-rank though globally high-rank: a fixed low-rank sketch shared across pages is provably blind to page-specific directions, while at the same summary size a page's own basis ranks pages and keeps carriers far better.

**证据证明什么。** LOCKS ships as a drop-in plugin for unmodified vLLM, with batched decode running in full CUDA graphs.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24555v1#S3.SS1 — C.1 Per-method budget accounting。Evaluation：https://arxiv.org/html/2607.24555v1#S3a — C Extended Results; https://arxiv.org/html/2607.24555v1#S5 — 5 Evaluation: Measuring Every Link。Limitations / counterevidence：https://arxiv.org/html/2607.24555v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Js-Hwang1/locks.git, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24555:end -->

<!-- review:SF-2026-ARXIV-2607-24562:start -->
### Hierarchical Group-Conditional Conformal Risk Control for Selective Prediction in Language Models

<!-- claim:SF-2026-ARXIV-2607-24562:start -->Large language models serve heterogeneous populations structured by domain, topic difficulty, and linguistic style. Conformal risk control (CRC) gives rigorous marginal risk guarantees for selective prediction with abstention, but marginal guarantees do not imply per-group ones: a model can meet the population budget while systematically over-exposing subgroups to errors. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24562:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models serve heterogeneous populations structured by domain, topic difficulty, and linguistic style.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose HG-CRC (Hierarchical Group-Conditional CRC), a post-hoc calibration framework enforcing simultaneous risk guarantees across all nodes of a user-defined group hierarchy.

**证据证明什么。** Results are benchmark-specific: on MMLU-Pro these models abstain entirely or (Llama) retain WGER=0.014.

**证据没有证明什么。** The residual limitation is that our exogenous signal is still a model-derived score rather than a human difficulty label, which the loaded allenai/ai2_arc distribution does not provide; a comparison against human grade-level labels from the original ARC release remains future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24562v1#S3 — 3 Method: Hierarchical Group-Conditional CRC; https://arxiv.org/html/2607.24562v1#A2 — Appendix B Extended E5: All Models。Evaluation：https://arxiv.org/html/2607.24562v1#A1 — Appendix A Extended Results: MMLU-Pro; https://arxiv.org/html/2607.24562v1#A4 — Appendix D Ablation: Sensitivity (A3)。Limitations / counterevidence：https://arxiv.org/html/2607.24562v1#S8 — 8 Discussion; https://arxiv.org/html/2607.24562v1#S8.SS3 — 8.3 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The residual limitation is that our exogenous signal is still a model-derived score rather than a human difficulty label, which the loaded allenai/ai2_arc distribution does not provide; a comparison against human grade-level labels from the original ARC release remains future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24562:end -->

<!-- review:SF-2026-ARXIV-2607-24570:start -->
### The Visual Bottleneck: Sparse-Frame Adaptation of MLLMs for Joint Spatial-Temporal Video Grounding

<!-- claim:SF-2026-ARXIV-2607-24570:start -->Large-scale video platforms process millions of uploads hourly, requiring moderation systems that can localize when and where policy violations occur within each video. Processing every frame is infeasible at scale, so systems are constrained to sparse inputs of 8 to 16 frames per video. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24570:end -->

**为什么进入候选分母。** 摘要首要问题为“Large-scale video platforms process millions of uploads hourly, requiring moderation systems that can localize when and where policy violations occur within each video.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present a systematic empirical study of training strategies to close this gap for spatial-temporal video grounding.

**证据证明什么。** Our results suggest that visual feature extraction is the dominant bottleneck under sparse-frame inputs.

**证据没有证明什么。** Adapting only the final three ViT layers surpasses language model fine-tuning by a factor of three and outperforms a zero-shot model four times larger. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24570v1#A4 — Appendix D Model Scaling Analysis; https://arxiv.org/html/2607.24570v1#A6 — Appendix F Implementation Details。Evaluation：https://arxiv.org/html/2607.24570v1#A3 — Appendix C Complete Experimental Results; https://arxiv.org/html/2607.24570v1#A4 — Appendix D Model Scaling Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.24570v1#S6 — 6 Discussion; https://arxiv.org/html/2607.24570v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Adapting only the final three ViT layers surpasses language model fine-tuning by a factor of three and outperforms a zero-shot model four times larger.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24570:end -->

<!-- review:SF-2026-ARXIV-2607-24582:start -->
### CADER: Confidence-Aware Dynamic Evidence Reasoning for Long-Video Understanding

<!-- claim:SF-2026-ARXIV-2607-24582:start -->Long-video understanding increasingly relies on large vision-language models and tool-augmented reasoning, but most systems apply the same inference procedure to every example regardless of difficulty. This uniform strategy invokes unnecessary tool-assisted processing for easy questions and provides limited control when difficult questions require fine-grained temporal evidence. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24582:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-video understanding increasingly relies on large vision-language models and tool-augmented reasoning, but most systems apply the same inference procedure to every example regardless of difficulty.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose CADER (Confidence-Aware Dynamic Evidence Reasoning), a training-free framework for adaptive and reliable long-video reasoning.

**证据证明什么。** Experiments on multiple VideoQA benchmarks show that CADER improves long-video reasoning while bypassing Stage~2 for high-confidence samples.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24582v1#Sx3 — Method。Evaluation：https://arxiv.org/html/2607.24582v1#Ax4 — D Reflection Depth Analysis; https://arxiv.org/html/2607.24582v1#Sx4 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.24582v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24582:end -->

<!-- review:SF-2026-ARXIV-2607-24585:start -->
### From Data to Device: ELMOD An Efficient German-First 2.7B Language Model for Mobile Inference

<!-- claim:SF-2026-ARXIV-2607-24585:start -->We present ELMOD - Efficient Language Model for On-Device Deployment - a compact (2.7B) German language model designed for efficient inference on resource-constrained hardware. ELMOD was trained on a limited computational budget (55k H100 GPU hours) using exclusively publicly available data. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24585:end -->

**为什么进入候选分母。** 摘要首要问题为“We present ELMOD - Efficient Language Model for On-Device Deployment - a compact (2.7B) German language model designed for efficient inference on resource-constrained hardware.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present ELMOD - Efficient Language Model for On-Device Deployment - a compact (2.7B) German language model designed for efficient inference on resource-constrained hardware.

**证据证明什么。** Furthermore, we introduced a quality filtering and rephrasing step, which increased the instructional quality of the data, improved performance during the annealing phase, and reduced overall compute requirements.

**证据没有证明什么。** Our experimental design, focused on on-device deployment, resulted in a model that not only outperforms all comparably sized German models, but also matches the performance of models trained on twice as much data. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24585v1#S2.SS1 — 2.1 German and German-Capable Language Models。Evaluation：https://arxiv.org/html/2607.24585v1#S5 — 5 Post-training Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.24585v1#S6 — 6 Summary and Conclusion; https://arxiv.org/html/2607.24585v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/collections/fraunhofer-iis/elmod-27b, https://huggingface.co/datasets/codeparrot/github-code-clean, https://github.com/explosion/spaCy/blob/master/spacy/lang/de/stop_words.py; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Our experimental design, focused on on-device deployment, resulted in a model that not only outperforms all comparably sized German models, but also matches the performance of models trained on twice as much data.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24585:end -->

<!-- review:SF-2026-ARXIV-2607-24586:start -->
### D-Score: A Spectral Hidden-State Signal for Hallucination Detection in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-24586:start -->Large Language Models can produce fluent text that is false, unsupported by the available evidence, or inconsistent with information that appears to be internally represented by the model. We study hallucination detection from the geometry of hidden activations and introduce the D-Score, a simple spectral statistic computed from a single forward pass. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24586:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models can produce fluent text that is false, unsupported by the available evidence, or inconsistent with information that appears to be internally represented by the model.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We study hallucination detection from the geometry of hidden activations and introduce the D-Score, a simple spectral statistic computed from a single forward pass.

**证据证明什么。** The experiments indicate that the D-Score is a strong hidden-state signal for hallucination detection, while requiring no external verifier, no retrieval step, and no multiple generations.

**证据没有证明什么。** The method requires white-box access to hidden activations, so it cannot be directly applied to closed models unless such activations are exposed. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24586v1#S3 — 3 Methodology; https://arxiv.org/html/2607.24586v1#A2 — Appendix B Algorithmic Details。Evaluation：https://arxiv.org/html/2607.24586v1#S4 — 4 Experimental Evaluation; https://arxiv.org/html/2607.24586v1#S4.SS1 — 4.1 Experimental protocol。Limitations / counterevidence：https://arxiv.org/html/2607.24586v1#S5 — 5 Discussion, Limitations, and Future Work; https://arxiv.org/html/2607.24586v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The method requires white-box access to hidden activations, so it cannot be directly applied to closed models unless such activations are exposed.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24586:end -->

<!-- review:SF-2026-ARXIV-2607-24593:start -->
### PIVOT: Efficient Query-Group Indexing for Token-Level Sparse Attention

<!-- claim:SF-2026-ARXIV-2607-24593:start -->Token-level sparse attention, as implemented by DeepSeek Sparse Attention (DSA) in production systems, makes the downstream attention efficient but shifts the bottleneck to the indexer that feeds it. To select the top-k tokens for each query, the indexer must still score every preceding token, incurring a cost of O(L^2) per layer for a sequence of length L. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24593:end -->

**为什么进入候选分母。** 摘要首要问题为“Token-level sparse attention, as implemented by DeepSeek Sparse Attention (DSA) in production systems, makes the downstream attention efficient but shifts the bottleneck to the indexer that feeds it.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Token-level sparse attention, as implemented by DeepSeek Sparse Attention (DSA) in production systems, makes the downstream attention efficient but shifts the bottleneck to the indexer that feeds it.

**证据证明什么。** On DeepSeek-V3.2 and GLM-5.1 across LongBench and RULER, PIVOT matches the accuracy of the dense DSA indexer while accelerating it by up to 4x and reducing end-to-end latency by up to 1.6x at long context.

**证据没有证明什么。** Combining the query axis with the token, head, and layer axes, and extending to broader model families, is promising future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24593v1#Sx4 — Method; https://arxiv.org/html/2607.24593v1#A1.SSx5 — E Algorithm。Evaluation：https://arxiv.org/html/2607.24593v1#A1.SSx3 — C Per-layer analysis of query locality in indexer top- selection; https://arxiv.org/html/2607.24593v1#A1.SSx6 — F Full Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.24593v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Combining the query axis with the token, head, and layer axes, and extending to broader model families, is promising future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-SELF-ATTENTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24593:end -->

<!-- review:SF-2026-ARXIV-2607-24604:start -->
### Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair

<!-- claim:SF-2026-ARXIV-2607-24604:start -->Generate--test--revise loops are common in coding agents, but repetition alone provides no reliability guarantee. We study the gap between finding a correct patch and retaining, verifying, and submitting it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24604:end -->

**为什么进入候选分母。** 摘要首要问题为“Generate--test--revise loops are common in coding agents, but repetition alone provides no reliability guarantee.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We study the gap between finding a correct patch and retaining, verifying, and submitting it.

**证据证明什么。** A prospective 540-rollout policy eliminates observed correct-start harm but reduces wrong-start repair and fails its joint criterion.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24604v1#S2.SS2 — 2.2. Agentic Software Engineering Systems; https://arxiv.org/html/2607.24604v1#S4 — 4. Study Design。Evaluation：https://arxiv.org/html/2607.24604v1#S5 — 5. Results; https://arxiv.org/html/2607.24604v1#S4 — 4. Study Design。Limitations / counterevidence：https://arxiv.org/html/2607.24604v1#S7 — 7. Discussion; https://arxiv.org/html/2607.24604v1#S8 — 8. Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24604:end -->

<!-- review:SF-2026-ARXIV-2607-24625:start -->
### APPA: Recoverable Information-Flow Control for Real-World LLM Agents

<!-- claim:SF-2026-ARXIV-2607-24625:start -->LLM agents deployed in practical workflows routinely mix private context, untrusted tool and web outputs, and external side effects. While information-flow control (IFC) provides structural defenses against prompt injection, data exfiltration, and confused-deputy attacks, conventional IFC relies on monotone taint tracking that either over-blocks benign operations or permanently strands downstream execution once an agent ingests unvetted data. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24625:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents deployed in practical workflows routinely mix private context, untrusted tool and web outputs, and external side effects.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present APPA (Agentic Permissions Policy Algebra), which turns agent IFC from an abort-only barrier into a policy-governed recovery system.

**证据证明什么。** Across 6,600 controlled benchmark episodes spanning OWASP AgentThreatBench and enterprise workflows (Bench-Corp), APPA sustains 64.2-91% utility with zero observed attacks across 1,320 guarded episodes, establishing a practical defense for deployed tool-using agents.

**证据没有证明什么。** We assume a durable, append-only event log, ensuring that policy checks evaluate against a consistent history. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24625v1#S2.SS0.SSS0.Px2 — Semantic, memory, and provenance systems.; https://arxiv.org/html/2607.24625v1#S7.SS0.SSS0.Px7 — Methodological scope.。Evaluation：https://arxiv.org/html/2607.24625v1#S7.SS0.SSS0.Px5 — Results and comparative analysis.; https://arxiv.org/html/2607.24625v1#A2 — Appendix B Benchmark Prompts。Limitations / counterevidence：https://arxiv.org/html/2607.24625v1#S8 — 8. Limitations and Future Agenda; https://arxiv.org/html/2607.24625v1#S3.SS0.SSS0.Px1 — Threat model.。

**Artifact boundary。** Exact v1 links https://github.com/NVIDIA/NeMo-Guardrails, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：We assume a durable, append-only event log, ensuring that policy checks evaluate against a consistent history.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24625:end -->

<!-- review:SF-2026-ARXIV-2607-24645:start -->
### Sparse Autoencoders Encode Both Concepts and Functions: The Downstream Geometry of Feature Effects

<!-- claim:SF-2026-ARXIV-2607-24645:start -->The wide-scale use of sparse autoencoders (SAEs) as interpretability tools is limited by inconsistent links between SAE features and model behavior. Features with clear activation descriptions may have weak or unexpected causal effects; steering can vary across prompts or oppose the intended direction; and activation-based feature selection can miss features that produce the desired output change. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24645:end -->

**为什么进入候选分母。** 摘要首要问题为“The wide-scale use of sparse autoencoders (SAEs) as interpretability tools is limited by inconsistent links between SAE features and model behavior.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce Feature-Effect Geometry Analysis (FEGA), an unsupervised framework that removes the same active SAE feature across contexts and analyzes the resulting cloud of logit changes.

**证据证明什么。** Our results show that a feature can be interpretable and causally relevant without providing a stable direction for steering.

**证据没有证明什么。** Stability analyses measure sensitivity within this sample but cannot eliminate the underlying selection boundary. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24645v1#S4.SS3 — 4.3 Feature Discovery Across SAE Architectures; https://arxiv.org/html/2607.24645v1#A6 — Appendix F Directional Mixtures and Model Selection。Evaluation：https://arxiv.org/html/2607.24645v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.24645v1#S4.SS5 — 4.5 Causal Contribution via Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.24645v1#S7 — 7 Discussion and Conclusion; https://arxiv.org/html/2607.24645v1#S8 — 8 Limitations and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Stability analyses measure sensitivity within this sample but cannot eliminate the underlying selection boundary.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24645:end -->

<!-- review:SF-2026-ARXIV-2607-24647:start -->
### Efficiency Matters in Autonomous Research

<!-- claim:SF-2026-ARXIV-2607-24647:start -->AI-driven autonomous research (AR) systems are becoming increasingly effective across a broad range of tasks. Their performance, however, is still evaluated primarily by the quality of the final outcome. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24647:end -->

**为什么进入候选分母。** 摘要首要问题为“AI-driven autonomous research (AR) systems are becoming increasingly effective across a broad range of tasks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To capture this dimension, we propose evaluating AR systems using the area under the curve (AUC) of the Pareto frontier, alongside final outcome quality.

**证据证明什么。** We also show that search efficiency and final outcome quality are distinct performance dimensions: a method that eventually achieves the best result may nevertheless improve slowly and consume substantially more evaluation budget before reaching that result.

**证据没有证明什么。** In its current form, however, fluid adapts only the allocation among a predefined set of hill-climbing chains. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24647v1#A1 — Appendix A The fluid Search Algorithm。Evaluation：https://arxiv.org/html/2607.24647v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24647v1#S2 — 2 Related work。Limitations / counterevidence：https://arxiv.org/html/2607.24647v1#S7 — 7 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/HaiqianYang-MechE/AREK, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：In its current form, however, fluid adapts only the allocation among a predefined set of hill-climbing chains.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24647:end -->

<!-- review:SF-2026-ARXIV-2607-24651:start -->
### Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels

<!-- claim:SF-2026-ARXIV-2607-24651:start -->Reliable visual document understanding requires a model to attribute each answer to the evidence regions that support it. Recent benchmarks and systems express this step through a coordinate interface: the model outputs the coordinates of bounding boxes that mark the evidence regions in the document. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24651:end -->

**为什么进入候选分母。** 摘要首要问题为“Reliable visual document understanding requires a model to attribute each answer to the evidence regions that support it.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present a study that investigates whether this failure is partially limited by what the model can express through coordinates.

**证据证明什么。** These findings indicate a practical path to improve attribution"without a coordinate interface and without costly region-level supervision.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24651v1#A10.SS1 — J.1 Coordinate-interface system prompt; https://arxiv.org/html/2607.24651v1#A10.SS2 — J.2 Language-interface system prompt (ours)。Evaluation：https://arxiv.org/html/2607.24651v1#A10.SS3 — J.3 Evaluation judge prompt: answer accuracy; https://arxiv.org/html/2607.24651v1#A10.SS4 — J.4 Evaluation judge prompt: evidence relevance。Limitations / counterevidence：https://arxiv.org/html/2607.24651v1#S6 — 6 Discussion; https://arxiv.org/html/2607.24651v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/hiyouga/EasyR1, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24651:end -->

<!-- review:SF-2026-ARXIV-2607-24653:start -->
### Kimi K3: Open Frontier Intelligence

<!-- claim:SF-2026-ARXIV-2607-24653:start -->We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24653:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window.

**证据证明什么。** Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24653v1#S5.SS1 — 5.1 Algorithm-System Co-Design for KDA; https://arxiv.org/html/2607.24653v1#S2 — 2 Model Architecture。Evaluation：https://arxiv.org/html/2607.24653v1#S6 — 6 Evaluations; https://arxiv.org/html/2607.24653v1#S6.SS1 — 6.1 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.24653v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/moonshotai/Kimi-K3, https://github.com/fla-org/flash-linear-attention/pull/691, https://github.com/MoonshotAI/MoonEP; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24653:end -->

<!-- review:SF-2026-ARXIV-2607-24663:start -->
### A corrective agentic hybrid RAG and an operations-grounded evaluation for a scientific facility

<!-- claim:SF-2026-ARXIV-2607-24663:start -->Scientific user facilities accumulate decades of operational knowledge that no single search index covers: electronic logbooks, technical documents, internal wikis, operations chat messages, maintenance records, and live control-system data. We present APS-RAG, Advanced Photon Source Retrieval Augmented Generation, a deployed platform that makes the institutional knowledge at the Advanced Photon Source (APS) accessible to staff through natural-language queries, along with an operations-grounded evaluation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24663:end -->

**为什么进入候选分母。** 摘要首要问题为“Scientific user facilities accumulate decades of operational knowledge that no single search index covers: electronic logbooks, technical documents, internal wikis, operations chat messages, maintenance records, and live control-system data.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We release the APS-Bench construction methodology, the six-layer evaluation harness, and the underlying codebase, along with the '/aps-rag' retrieval agent skill framework, to support reproduction and adoption at other facilities.

**证据证明什么。** The cross-encoder reranker contributes significantly to answer quality: removing it and allowing the LLM to score relevance drastically reduces strict vital recall by 32.8%.

**证据没有证明什么。** These limitations do not detract from the main contributions of this work: the establishment of a benchmark and metric suite for institutional knowledge, a systematic comparison of five systems, and a reranker result that remains robust after correction for multiple comparisons. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24663v1#S3 — III The APS-RAG platform and system architecture; https://arxiv.org/html/2607.24663v1#S3.SS3 — III.3 APS-RAG architecture overview。Evaluation：https://arxiv.org/html/2607.24663v1#S4 — IV Benchmarks and evaluation methodology; https://arxiv.org/html/2607.24663v1#S4.SS1 — IV.1 Real operations data benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.24663v1#S5 — V Results and discussion; https://arxiv.org/html/2607.24663v1#S5.SS8 — V.8 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/rajatsainju2025/aps-rag, https://github.com/pymupdf/pymupdf, https://huggingface.co/vectara/hallucination_evaluation_model; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：These limitations do not detract from the main contributions of this work: the establishment of a benchmark and metric suite for institutional knowledge, a systematic comparison of five systems, and a reranker result that remains robust after correction for multiple comparisons.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24663:end -->

<!-- review:SF-2026-ARXIV-2607-24665:start -->
### MMOE: Modernizing Diffusion Transformers with Efficient Expert Design

<!-- claim:SF-2026-ARXIV-2607-24665:start -->Modern large language models scale successfully by pairing capacity growth with efficiency, keeping per-token and deployment costs under control as capacity grows. AIGC Foundation Models (AFMs), especially diffusion-transformer backbones, have begun to adopt sparse experts, but recent efforts mostly enlarge total parameter counts and sparsity ratios without importing the efficiency mechanisms that made LLM scaling practical, so generation quality is seldom balanced against training and deployment cost. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24665:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern large language models scale successfully by pairing capacity growth with efficiency, keeping per-token and deployment costs under control as capacity grows.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce ModernMOE (MMOE), a modernization of SiT-style diffusion transformers that systematically adapts routed experts, shared and lightweight experts, gate-residual routing, and attention-residual information reuse to AIGC generation.

**证据证明什么。** Routing analysis further shows stable expert specialization across depth, substantial use of lightweight routes, and modest step-to-step routing changes during denoising.

**证据没有证明什么。** Finally, sparse expert models introduce distributed-training overheads that block-level memory profiling and single-run wall-clock time do not fully capture; our profiling indicates that the current multi-GPU training is communication bound, so the reported training times reflect a communication-limited regime. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24665v1#S3 — III Method; https://arxiv.org/html/2607.24665v1#S2.SS1 — II-A Diffusion Models and Flow Matching。Evaluation：https://arxiv.org/html/2607.24665v1#S4 — IV Experiments; https://arxiv.org/html/2607.24665v1#S4.SS1 — IV-A Experiment Settings。Limitations / counterevidence：https://arxiv.org/html/2607.24665v1#S6 — VI Discussion and Limitations; https://arxiv.org/html/2607.24665v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Finally, sparse expert models introduce distributed-training overheads that block-level memory profiling and single-run wall-clock time do not fully capture; our profiling indicates that the current multi-GPU training is communication bound, so the reported training times reflect a communication-limited regime.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24665:end -->

<!-- review:SF-2026-ARXIV-2607-24667:start -->
### Eviction as Estimation: A Fixed-Lag Smoothing View of Test-Time Memory, and When Measuring Beats Accumulating

<!-- claim:SF-2026-ARXIV-2607-24667:start -->A language model with a bounded working memory must repeatedly decide which stored items to keep. Every deployed method decides the moment an item arrives, from the past (StreamingLLM, H2O) or from a guess about the future (SnapKV). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24667:end -->

**为什么进入候选分母。** 摘要首要问题为“A language model with a bounded working memory must repeatedly decide which stored items to keep.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Our contribution is the framework and an honest map of when measuring beats accumulating, not a new state of the art.

**证据证明什么。** This measurement, demonstrated utility, turns Belady's unobservable future request into something we read off the model itself.

**证据没有证明什么。** On independent benchmarks the advantage collapses, because correctness-weighted attention and raw accumulated attention coincide unless reuse is sharp and endogenous, which standard benchmarks do not contain. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24667v1#S2.SS0.SSS0.Px5 — Memory in learning systems.; https://arxiv.org/html/2607.24667v1#S3.SS0.SSS0.Px2 — The commit lag is a design axis.。Evaluation：https://arxiv.org/html/2607.24667v1#S2.SS0.SSS0.Px6 — Benchmarks and harnesses.; https://arxiv.org/html/2607.24667v1#S7 — 7 Controlled experiments。Limitations / counterevidence：https://arxiv.org/html/2607.24667v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.24667v1#S2.SS0.SSS0.Px2 — Learned predictors that decide from a guessed future.。

**Artifact boundary。** Exact v1 links https://github.com/NVIDIA/kvpress, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：On independent benchmarks the advantage collapses, because correctness-weighted attention and raw accumulated attention coincide unless reuse is sharp and endogenous, which standard benchmarks do not contain.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24667:end -->

<!-- review:SF-2026-ARXIV-2607-24692:start -->
### Denial of Deadline: Network-Driven Accuracy Collapse in Distributed Inference Pipelines

<!-- claim:SF-2026-ARXIV-2607-24692:start -->Inference systems increasingly combine a fast path that returns predictions within the application's latency deadline together with a higher-accuracy slow path that runs higher-compute methods on stronger, remote hardware, so its results can be returned on time and combined with the fast path predictions. Across several application domains, we abstract this inference architecture as a fast path, a slow path, and a coordination layer with two functions: a router that invokes the slow path and a merger that decides whether to incorporate its returned predictions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24692:end -->

**为什么进入候选分母。** 摘要首要问题为“Inference systems increasingly combine a fast path that returns predictions within the application's latency deadline together with a higher-accuracy slow path that runs higher-compute methods on stronger, remote hardware, so its results can be returned on time and combined with the fast path predictions.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Inference systems increasingly combine a fast path that returns predictions within the application's latency deadline together with a higher-accuracy slow path that runs higher-compute methods on stronger, remote hardware, so its results can be returned on time and combined with the fast path predictions.

**证据证明什么。** These results show that workload attacks can degrade prediction quality without needing either access to model weights or victim data, and motivate research on attacks and defenses for routing, merging, scheduling, and resource isolation in these emerging inference pipeline architectures.

**证据没有证明什么。** It cannot inspect or modify other users’ traffic or compromise any component of the inference pipeline. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24692v1#S2 — 2. Two-System Inference Pipelines; https://arxiv.org/html/2607.24692v1#S2.SS2 — 2.2. Architecture and execution semantics。Evaluation：https://arxiv.org/html/2607.24692v1#S4 — 4. Evaluations。Limitations / counterevidence：https://arxiv.org/html/2607.24692v1#S6 — 6. Discussion and Future Work; https://arxiv.org/html/2607.24692v1#S3.SS1 — 3.1. Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：It cannot inspect or modify other users’ traffic or compromise any component of the inference pipeline.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24692:end -->

<!-- review:SF-2026-ARXIV-2607-24717:start -->
### DataOrchestra: Learning to Orchestrate Per-Example Curation of Pretraining Data

<!-- claim:SF-2026-ARXIV-2607-24717:start -->Pretraining data processing is critical to the downstream performance of Large Language Models (LLMs). However, many existing approaches define a fixed processing strategy at the corpus or domain level and apply it uniformly to many examples, without adapting to the needs of each example. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24717:end -->

**为什么进入候选分母。** 摘要首要问题为“Pretraining data processing is critical to the downstream performance of Large Language Models (LLMs).”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose DataOrchestra, a framework that unifies different processing operations and orchestrates an example-specific pipeline for each example.

**证据证明什么。** DataOrchestra is also effective for math continued pretraining and outperforms stronger processing baselines, while reducing processing compute by skipping unnecessary downstream operations.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24717v1#S3 — 3 Methods; https://arxiv.org/html/2607.24717v1#S3.SS2 — 3.2 DataOrchestra Framework。Evaluation：https://arxiv.org/html/2607.24717v1#S5 — 5 Analysis and Ablations; https://arxiv.org/html/2607.24717v1#A4 — Appendix D Details of Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.24717v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/GAIR-NLP/DataOrchestra, https://huggingface.co/datasets/HuggingFaceTB/cosmopedia, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24717:end -->

<!-- review:SF-2026-ARXIV-2607-24720:start -->
### The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation

<!-- claim:SF-2026-ARXIV-2607-24720:start -->Multi-turn long-horizon planning is critical for foundation model agents, yet how to fundamentally improve it remains unclear. Existing models are trained on uncontrollable and opaque Internet data, making it difficult to identify how planning ability is acquired, shaped, and integrated. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24720:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-turn long-horizon planning is critical for foundation model agents, yet how to fundamentally improve it remains unclear.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this challenge, we introduce a unified and controlled multi-turn environment that enables precise control.

**证据证明什么。** Multi-turn long-horizon planning is critical for foundation model agents, yet how to fundamentally improve it remains unclear.

**证据没有证明什么。** At the pre-training stage, we show that explicit world model internalization, limited long-horizon data, and high-quality trajectories are critical for robust long-horizon planning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24720v1#A1.SS1 — A.1 Pre-trained Model Configuration; https://arxiv.org/html/2607.24720v1#S4.SS1 — 4.1 Planning with Internalized World Model。Evaluation：https://arxiv.org/html/2607.24720v1#S3.SS3 — 3.3 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.24720v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Quester-one/PlanPhysCode, https://huggingface.co/MultimodalAgent/TianyiMen_PlanPhys_Models, https://huggingface.co/datasets/MultimodalAgent/TianyiMen_PlanPhys_Datasets; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：At the pre-training stage, we show that explicit world model internalization, limited long-horizon data, and high-quality trajectories are critical for robust long-horizon planning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24720:end -->

<!-- review:SF-2026-ARXIV-2607-24731:start -->
### Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation

<!-- claim:SF-2026-ARXIV-2607-24731:start -->On-policy distillation (OPD) adapts diffusion models by querying a teacher along trajectories generated by the current student, but how it should behave under classifier-free guidance (CFG), a default component of modern diffusion systems, remains poorly understood. Existing OPD methods naturally extend velocity matching to the CFG-composed prediction, directly matching teacher and student guided velocities. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24731:end -->

**为什么进入候选分母。** 摘要首要问题为“On-policy distillation (OPD) adapts diffusion models by querying a teacher along trajectories generated by the current student, but how it should behave under classifier-free guidance (CFG), a default component of modern diffusion systems, remains poorly understood.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Existing OPD methods naturally extend velocity matching to the CFG-composed prediction, directly matching teacher and student guided velocities.

**证据证明什么。** We show that this objective is under-identified at the branch level: positive- and negative-branch errors can compensate in the guided prediction.

**证据没有证明什么。** 6 Conclusions and Limitations We show that CFG-composed OPD is under-identified at the branch level, but that this ambiguity does not always cause failure. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24731v1#S2.SS1 — 2.1 On-Policy Distillation for Diffusion Models; https://arxiv.org/html/2607.24731v1#S5.SS1 — 5.1 Diffusion Model Distillation。Evaluation：https://arxiv.org/html/2607.24731v1#S4 — 4 Experiments; https://arxiv.org/html/2607.24731v1#S4.SS3 — 4.3 Ablation Studies。Limitations / counterevidence：https://arxiv.org/html/2607.24731v1#S6 — 6 Conclusions and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：6 Conclusions and Limitations We show that CFG-composed OPD is under-identified at the branch level, but that this ambiguity does not always cause failure.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24731:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-22569 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22569 |
| SF-2026-ARXIV-2607-22578 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22578 |
| SF-2026-ARXIV-2607-22585 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22585 |
| SF-2026-ARXIV-2607-22586 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22586 |
| SF-2026-ARXIV-2607-22611 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22611 |
| SF-2026-ARXIV-2607-22614 | score_7_9 | selected | DA-20260728-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260728-01 |
| SF-2026-ARXIV-2607-22634 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22634 |
| SF-2026-ARXIV-2607-22648 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22648 |
| SF-2026-ARXIV-2607-22662 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22662 |
| SF-2026-ARXIV-2607-22690 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22690 |
| SF-2026-ARXIV-2607-22724 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22724 |
| SF-2026-ARXIV-2607-22781 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22781 |
| SF-2026-ARXIV-2607-22785 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22785 |
| SF-2026-ARXIV-2607-22798 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22798 |
| SF-2026-ARXIV-2607-22868 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22868 |
| SF-2026-ARXIV-2607-22926 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22926 |
| SF-2026-ARXIV-2607-22962 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22962 |
| SF-2026-ARXIV-2607-22999 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22999 |
| SF-2026-ARXIV-2607-23047 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23047 |
| SF-2026-ARXIV-2607-23054 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23054 |
| SF-2026-ARXIV-2607-23089 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23089 |
| SF-2026-ARXIV-2607-23099 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23099 |
| SF-2026-ARXIV-2607-23115 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23115 |
| SF-2026-ARXIV-2607-23250 | score_7_9 | selected | DA-20260728-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260728-02 |
| SF-2026-ARXIV-2607-23264 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23264 |
| SF-2026-ARXIV-2607-23364 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23364 |
| SF-2026-ARXIV-2607-23373 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23373 |
| SF-2026-ARXIV-2607-23444 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23444 |
| SF-2026-ARXIV-2607-23532 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23532 |
| SF-2026-ARXIV-2607-23586 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23586 |
| SF-2026-ARXIV-2607-23693 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23693 |
| SF-2026-ARXIV-2607-23771 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23771 |
| SF-2026-ARXIV-2607-23809 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23809 |
| SF-2026-ARXIV-2607-23815 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23815 |
| SF-2026-ARXIV-2607-23909 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23909 |
| SF-2026-ARXIV-2607-23929 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23929 |
| SF-2026-ARXIV-2607-23933 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23933 |
| SF-2026-ARXIV-2607-23999 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-23999 |
| SF-2026-ARXIV-2607-24260 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24260 |
| SF-2026-ARXIV-2607-24331 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24331 |
| SF-2026-ARXIV-2607-24377 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24377 |
| SF-2026-ARXIV-2607-24434 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24434 |
| SF-2026-ARXIV-2607-24555 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24555 |
| SF-2026-ARXIV-2607-24585 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24585 |
| SF-2026-ARXIV-2607-24586 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24586 |
| SF-2026-ARXIV-2607-24593 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24593 |
| SF-2026-ARXIV-2607-24653 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24653 |
| SF-2026-ARXIV-2607-24667 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24667 |
| SF-2026-ARXIV-2607-24692 | score_7_9 | selected | DA-20260728-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260728-03 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-22569:start -->
`SF-2026-ARXIV-2607-22569` 的 exact-v1 Deep Review 已保留。其机制为：We present an execution-grounded red-team testing framework for probing this execution-layer security boundary using observable sandbox evidence, including tool invocations, runtime traces, and file-system diffs. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22569:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22578:start -->
`SF-2026-ARXIV-2607-22578` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we propose HeraSys, an LLM serving system designed to optimize the end-to-end performance of concurrent workflows. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22578:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22585:start -->
`SF-2026-ARXIV-2607-22585` 的 exact-v1 Deep Review 已保留。其机制为：Public leaderboards for coding agents typically rank systems by model name and pass rate, while the surrounding harness (the scaffold that issues tools, manages context, and decides when to stop) is often under-specified. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22585:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22586:start -->
`SF-2026-ARXIV-2607-22586` 的 exact-v1 Deep Review 已保留。其机制为：We propose MM-ShiftKV, a training-free, decode-aware and strictly prefill-only KV selection method. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22586:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22611:start -->
`SF-2026-ARXIV-2607-22611` 的 exact-v1 Deep Review 已保留。其机制为：Our framework introduces four key innovations: (1) a compound identity model that binds agent actions to delegated human authority, (2) a hierarchical permission system spanning five granularity levels from global platform access to per-parameter constraints, (3) a decentralized policy ownership model where tool teams independently govern their authorization boundaries, and (4) progressive trust escalation with safety interlocks that prevent autonomous agents from executing high-risk operations. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22611:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22634:start -->
`SF-2026-ARXIV-2607-22634` 的 exact-v1 Deep Review 已保留。其机制为：We propose PRESTO, a principled framework that extends tree-based drafting to diffusion drafters while resolving the fundamental mismatch between diffusion draft confidence and prefix-based AR verification through PREfix-aligned Scoring and priority-based Tree search for diffusion speculative decOding. 为避免挤压 `INFER-SPECULATIVE-DECODING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22634:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22648:start -->
`SF-2026-ARXIV-2607-22648` 的 exact-v1 Deep Review 已保留。其机制为：This reduces the latency of accessing the KV cache and alleviates load imbalance caused by a disproportionately large number of requests on servers containing popular tensors. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22648:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22662:start -->
`SF-2026-ARXIV-2607-22662` 的 exact-v1 Deep Review 已保留。其机制为：Applying this framework to Common Crawl, we construct CuraWeb, a 2T-token English corpus. 为避免挤压 `TRAIN-DATA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22662:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22690:start -->
`SF-2026-ARXIV-2607-22690` 的 exact-v1 Deep Review 已保留。其机制为：We introduce LazyMem, which resolves this tension by deferring all memory construction to query time. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22690:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22724:start -->
`SF-2026-ARXIV-2607-22724` 的 exact-v1 Deep Review 已保留。其机制为：To break this loop, we propose Progress-conditioned Group Policy Optimization (ProGPO), which uses first-visit observation coverage only when all samples in a group receive zero outcome reward. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22724:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22781:start -->
`SF-2026-ARXIV-2607-22781` 的 exact-v1 Deep Review 已保留。其机制为：We propose Mass-Aware Attention (MAA), which generalizes standard L1 normalization to an Lp family. 为避免挤压 `MODEL-SELF-ATTENTION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22781:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22785:start -->
`SF-2026-ARXIV-2607-22785` 的 exact-v1 Deep Review 已保留。其机制为：Apple-Silicon SoCs share CPU, GPU, and Neural Engine over one unified memory system, raising the question of whether transformer inference can be accelerated by splitting single operators across units. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22785:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22798:start -->
`SF-2026-ARXIV-2607-22798` 的 exact-v1 Deep Review 已保留。其机制为：Yet a screenshot is only a lossy rendering of the underlying program state, e.g., the files, application backends, and DOM that hold the task data. 为避免挤压 `AGENT-TOOL-CALLING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22798:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22868:start -->
`SF-2026-ARXIV-2607-22868` 的 exact-v1 Deep Review 已保留。其机制为：First, relative to fixed oracle predicates, a deterministic gate enforces exactly the nonempty safety policies whose good prefixes its register model recognizes; policy nontriviality is undecidable with two decrementable counters but in PSPACE for a separable monotone fragment. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22868:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22926:start -->
`SF-2026-ARXIV-2607-22926` 的 exact-v1 Deep Review 已保留。其机制为：SAGE is a safety-first, authorization-separated architecture in which credible catastrophic-enablement risk constrains admissibility before utility, latency, or commercial objectives are considered. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22926:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22962:start -->
`SF-2026-ARXIV-2607-22962` 的 exact-v1 Deep Review 已保留。其机制为：We propose ConsistencyGate, a write-time admission gate that, before committing a candidate fact m extracted from context c, queries the LLM K times for a soft support score and admits m only when the average exceeds a threshold. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22962:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22999:start -->
`SF-2026-ARXIV-2607-22999` 的 exact-v1 Deep Review 已保留。其机制为：To solve this problem, we present the World-Cognition Model (WCM), a human-centered embodied agent built on the SLAK architecture (Sensing, Logic, Action, and Knowledge) and an asynchronous runtime. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22999:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23047:start -->
`SF-2026-ARXIV-2607-23047` 的 exact-v1 Deep Review 已保留。其机制为：We propose MixQuant, a technique-agnostic adaptive framework that wraps any base quantizer. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23047:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23054:start -->
`SF-2026-ARXIV-2607-23054` 的 exact-v1 Deep Review 已保留。其机制为：We present the first comprehensive mechanistic interpretability study of MLA, training a 114M-parameter transformer (pretrained on a web/code/math mixture, fine-tuned on TinyStories) and analyzing its representations through SVD, attention head taxonomy, linear probing, and a disruption-attribution analysis. 为避免挤压 `MODEL-MULTI-HEAD-ATTENTION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23054:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23089:start -->
`SF-2026-ARXIV-2607-23089` 的 exact-v1 Deep Review 已保留。其机制为：Based on this insight, we present our system, a compiler-grounded and hierarchical optimization framework for Triton kernels. the system escalates from lightweight pattern triage and profiling diagnosis to IR attribution and compiler-grounded analysis only when deeper evidence is needed, then proposes evidence-backed source-level rewrites. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23089:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23099:start -->
`SF-2026-ARXIV-2607-23099` 的 exact-v1 Deep Review 已保留。其机制为：We introduce a distribution-aware framework for modeling and benchmarking MoE inference. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23099:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23115:start -->
`SF-2026-ARXIV-2607-23115` 的 exact-v1 Deep Review 已保留。其机制为：To address these challenges, we propose Gleam, a novel and network-efficient framework for task-generic GPU sharing across local-area CUDA devices, with three key contributions. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23115:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23264:start -->
`SF-2026-ARXIV-2607-23264` 的 exact-v1 Deep Review 已保留。其机制为：Existing systems schedule when communication is issued and when received data becomes consumable, but omit post-issue progress before remote-visible completion, making sender backpressure hard to predict. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23264:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23364:start -->
`SF-2026-ARXIV-2607-23364` 的 exact-v1 Deep Review 已保留。其机制为：GRPO (COLM 2025) identifies the response-level length bias caused by per-trajectory length normalization in GRPO and proposes removing this normalization, claiming the resulting optimizer is "unbiased." We show that this claim is incomplete. 为避免挤压 `TRAIN-RLHF` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23364:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23373:start -->
`SF-2026-ARXIV-2607-23373` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we present UltraViT, a vision encoder for LVLMs, explicitly designed and optimized for on-device performance. 为避免挤压 `MULTIMODAL-REPRESENTATION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23373:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23444:start -->
`SF-2026-ARXIV-2607-23444` 的 exact-v1 Deep Review 已保留。其机制为：We present SPORE, the first extraction attack designed for this threat model. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23444:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23532:start -->
`SF-2026-ARXIV-2607-23532` 的 exact-v1 Deep Review 已保留。其机制为：We present a three-tier (platfor- m/squad/mission) compositional runtime-verification framework that de- composes a mission policy into per-agent and cross-agent aspects, aggre- gates per-platform verdicts over a verification-aware messaging fabric, and fuses them with an evidence-aware, two-axis (security x complete- ness) algebra whose provenance names the platforms that jointly trig- gered a violation. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23532:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23586:start -->
`SF-2026-ARXIV-2607-23586` 的 exact-v1 Deep Review 已保留。其机制为：This improves adaptation but creates a distinct authorization problem. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23586:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23693:start -->
`SF-2026-ARXIV-2607-23693` 的 exact-v1 Deep Review 已保留。其机制为：Long-horizon agents increasingly reuse their KV cache as memory: a serving system keeps a subset of cached entries and drops the rest. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23693:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23771:start -->
`SF-2026-ARXIV-2607-23771` 的 exact-v1 Deep Review 已保留。其机制为：We introduce CALM (Controller-Aware Language Models), a post-training framework that explicitly places controllers in the training loop. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23771:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23809:start -->
`SF-2026-ARXIV-2607-23809` 的 exact-v1 Deep Review 已保留。其机制为：We propose Agentic Context Management (ACM), a framework that equips agents with purpose-built context editing tools for lossless context management. 为避免挤压 `AGENT-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23809:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23815:start -->
`SF-2026-ARXIV-2607-23815` 的 exact-v1 Deep Review 已保留。其机制为：We present Kalypso, a relational LLM serving system that exposes an API for semantic query plans and executes them using an adaptive, memory-aware scheduling algorithm. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23815:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23909:start -->
`SF-2026-ARXIV-2607-23909` 的 exact-v1 Deep Review 已保留。其机制为：Across four LIBERO simulation suites, WorldDiT lies on the reported Pareto frontier for total model parameters and mean success among methods reporting all four suites. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23909:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23929:start -->
`SF-2026-ARXIV-2607-23929` 的 exact-v1 Deep Review 已保留。其机制为：We present MemTX, a transactional belief-commit protocol. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23929:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23933:start -->
`SF-2026-ARXIV-2607-23933` 的 exact-v1 Deep Review 已保留。其机制为：To resolve this dilemma, we present SpecBox, a runtime built around speculative sandbox preallocation tailored for dynamic LLM agent execution pipelines. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23933:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23999:start -->
`SF-2026-ARXIV-2607-23999` 的 exact-v1 Deep Review 已保留。其机制为：We introduce ContainmentBench, a sandboxed benchmark comprising a 504-scenario specification dataset, a shared rollout-trace schema, and stage-scoped metrics for endpoint violations, logged propagation, and explicitly authorized taint-exposed proposals that commit. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-23999:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24260:start -->
`SF-2026-ARXIV-2607-24260` 的 exact-v1 Deep Review 已保留。其机制为：Modern LLM systems increasingly rely on knowledge-selection processes that produce high-value structured priors, such as ranked evidence, graph topology, multimodal alignment, and confidence signals. 为避免挤压 `AGENT-RAG` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24260:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24331:start -->
`SF-2026-ARXIV-2607-24331` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we propose an improved low-rank KV cache compression framework. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24331:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24377:start -->
`SF-2026-ARXIV-2607-24377` 的 exact-v1 Deep Review 已保留。其机制为：We propose MXAttention, a data-free post-training quantization framework for MXFP4 attention. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24377:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24434:start -->
`SF-2026-ARXIV-2607-24434` 的 exact-v1 Deep Review 已保留。其机制为：We propose DraftExpert, an expansion-aware self-speculative decoding framework for expert-offloaded MoE inference. 为避免挤压 `INFER-SPECULATIVE-DECODING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24434:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24555:start -->
`SF-2026-ARXIV-2607-24555` 的 exact-v1 Deep Review 已保留。其机制为：Attention keys are locally low-rank though globally high-rank: a fixed low-rank sketch shared across pages is provably blind to page-specific directions, while at the same summary size a page's own basis ranks pages and keeps carriers far better. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24555:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24585:start -->
`SF-2026-ARXIV-2607-24585` 的 exact-v1 Deep Review 已保留。其机制为：We present ELMOD - Efficient Language Model for On-Device Deployment - a compact (2.7B) German language model designed for efficient inference on resource-constrained hardware. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24585:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24586:start -->
`SF-2026-ARXIV-2607-24586` 的 exact-v1 Deep Review 已保留。其机制为：We study hallucination detection from the geometry of hidden activations and introduce the D-Score, a simple spectral statistic computed from a single forward pass. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24586:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24593:start -->
`SF-2026-ARXIV-2607-24593` 的 exact-v1 Deep Review 已保留。其机制为：Token-level sparse attention, as implemented by DeepSeek Sparse Attention (DSA) in production systems, makes the downstream attention efficient but shifts the bottleneck to the indexer that feeds it. 为避免挤压 `MODEL-SELF-ATTENTION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24593:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24653:start -->
`SF-2026-ARXIV-2607-24653` 的 exact-v1 Deep Review 已保留。其机制为：We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. 为避免挤压 `MODEL-MOE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24653:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24667:start -->
`SF-2026-ARXIV-2607-24667` 的 exact-v1 Deep Review 已保留。其机制为：Our contribution is the framework and an honest map of when measuring beats accumulating, not a new state of the art. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24667:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260728-01:start -->
### DynaResize: Runtime GPU Reallocation for Disaggregated LLM Post-Training

**约束变化与机制。** We present DynaResize, a runtime GPU reallocation system that dynamically switches GPUs between Rollout and Training to balance stage execution times without changing RL semantics.

**证明与未证明。** Experimental results show that DynaResize can improve end-to-end throughput by 66.5% and reduce total execution time by 33% over the optimal static configuration, while hiding 27% of role-switching overhead. 但 Although pre-warming and on-demand loading only moderately reduce the critical-path resizing latency, this reduction is sufficient to yield substantial end-to-end gains in pipeline-stall-dominated post-training workloads. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Although pre-warming and on-demand loading only moderately reduce the critical-path resizing latency, this reduction is sufficient to yield substantial end-to-end gains in pipeline-stall-dominated post-training workloads. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-22614`。
<!-- analysis:DA-20260728-01:end -->

<!-- analysis:DA-20260728-02:start -->
### Libra: Taming Attention Workload Skew in Long-Context LLM Training with Bounded Sequence Pool

**约束变化与机制。** We present Libra, which operationalizes the law of large numbers (LLN) as a scaling principle for load balancing: the attention-balancing pool need not grow with the DP degree.

**证明与未证明。** Variance-Reduced Sequence Placement makes this effective for finite, long-tailed workloads by co-locating sequences with complementary attention workloads to reduce residual inter-pool skew. 但 Specifically, Libra presents three innovations to address attention FLOPs imbalance: 1) using the law of large numbers as a scaling principle so that the sequence-pool size need not grow with the DP degree, 2) introducing Variance-Reduced Sequence Placement to balance the sequence-pool instances formed in each optimizer-step window, and 3) developing Tiled Attention Pooling to balance sequence head SH-Tiles within each pool, together with the TAP Pipeliner to overlap the resulting tensor movement with attention computation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Specifically, Libra presents three innovations to address attention FLOPs imbalance: 1) using the law of large numbers as a scaling principle so that the sequence-pool size need not grow with the DP degree, 2) introducing Variance-Reduced Sequence Placement to balance the sequence-pool instances formed in each optimizer-step window, and 3) developing Tiled Attention Pooling to balance sequence head SH-Tiles within each pool, together with the TAP Pipeliner to overlap the resulting tensor movement with attention computation. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-23250`。
<!-- analysis:DA-20260728-02:end -->

<!-- analysis:DA-20260728-03:start -->
### Denial of Deadline: Network-Driven Accuracy Collapse in Distributed Inference Pipelines

**约束变化与机制。** Inference systems increasingly combine a fast path that returns predictions within the application's latency deadline together with a higher-accuracy slow path that runs higher-compute methods on stronger, remote hardware, so its results can be returned on time and combined with the fast path predictions.

**证明与未证明。** These results show that workload attacks can degrade prediction quality without needing either access to model weights or victim data, and motivate research on attacks and defenses for routing, merging, scheduling, and resource isolation in these emerging inference pipeline architectures. 但 It cannot inspect or modify other users’ traffic or compromise any component of the inference pipeline. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：It cannot inspect or modify other users’ traffic or compromise any component of the inference pipeline. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-24692`。
<!-- analysis:DA-20260728-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260728-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260728 | GAP-20260728-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260728-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260728-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260728-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260728-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260728-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260728-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

823 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：46
- `incremental_method_without_durable_system_delta`：652
- `local_benchmark_without_release_delta`：25
- `prior_retained_candidate`：1
- `theory_without_ai_system_contract`：11
- `vertical_application_without_system_delta`：88

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 49、No Change 150、Structural 0；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/28/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [Semalith v1.4: A Calibrated 184M Safety Classifier Achieving State-of-the-Art Prompt-Injection Detection at 44x Fewer Parameters than Llama-Guard-3-8B](https://arxiv.org/html/2607.22545v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Same Question, Different Answers: Evaluating LLM Reliability Beyond Accuracy](https://arxiv.org/html/2607.22554v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [MIITA: Memory-Induced Inference-Time Adaptation for Continual Learning with Small Language Models](https://arxiv.org/html/2607.22556v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Codifying the Judge: Scalable Evaluation via Program Distillation](https://arxiv.org/html/2607.22561v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [SF-AMS: Strategic Forgetting for Structured Memory in LLM Agent](https://arxiv.org/html/2607.22562v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Execution-Grounded Security Testing for Coding Agents in Software Engineering Pipelines](https://arxiv.org/html/2607.22569v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Reference Feature Atlases for Mechanistic Auditing of Language Models](https://arxiv.org/html/2607.22570v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [cMoLLM at Scale: Horizontal Scaling Laws for Mixture-of-LLMs](https://arxiv.org/html/2607.22577v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [HeraSys: Collaborative Serving of Multiple LLM Workflows via Fine-Grained End-to-End Optimization](https://arxiv.org/html/2607.22578v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Source-Aware Reranking for Retrieval-Augmented Generation: A Reliability Prior Approach](https://arxiv.org/html/2607.22584v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation](https://arxiv.org/html/2607.22585v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [MM-ShiftKV: Decode-Aware Prefill-Stage KV Selection for Multimodal Large Language Models](https://arxiv.org/html/2607.22586v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [xMIx: High-Performance Serving-Time Platform for Mechanistic Interpretability Apps](https://arxiv.org/html/2607.22595v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Chart Deception in Vision-Language Models: From Vulnerability to Mitigation](https://arxiv.org/html/2607.22600v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Tokengeist: Multi-Turn Attribution Tracing in Agentic Conversations](https://arxiv.org/html/2607.22610v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Decentralized Granular Access Control for Agentic AI Systems in Critical Infrastructure](https://arxiv.org/html/2607.22611v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [DynaResize: Runtime GPU Reallocation for Disaggregated LLM Post-Training](https://arxiv.org/html/2607.22614v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [TokenMem: Faithful Knowledge Injection for Frozen LLMs](https://arxiv.org/html/2607.22625v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Masked Distillation: Internalizing the Chain-of-Thought in Language Models](https://arxiv.org/html/2607.22629v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [PRESTO: Prefix-Aligned Tree Drafting for Diffusion Speculative Decoding](https://arxiv.org/html/2607.22634v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Reason Before You Retrieve: Agentic Planning for Multi-modal RAG](https://arxiv.org/html/2607.22643v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [PTStore (Prefix Tensor Store): Distributed Prefix Caching and Replication for High Throughput Inference Serving](https://arxiv.org/html/2607.22648v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [ARdena: Scenario-driven control of real-time LLM agents](https://arxiv.org/html/2607.22651v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [TRE: Training-Free Hallucination Detection for Diffusion Language Models](https://arxiv.org/html/2607.22661v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [CuraWeb: Joint Optimization of Quality, Redundancy, and Diversity for Web-Scale Pretraining Data](https://arxiv.org/html/2607.22662v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Beyond Block Boundaries: Multi-Block Editing for Diffusion Large Language Models](https://arxiv.org/html/2607.22663v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [AIR-BENCH Live: An Evolving Safety Benchmark for Foundation Models](https://arxiv.org/html/2607.22671v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [How LLM Task-Adaptation Reshapes Alignment: A Multi-dimensional Study of Behavioral and Representational Drift](https://arxiv.org/html/2607.22676v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](https://arxiv.org/html/2607.22688v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Beyond Sequential Interaction: Benchmarking Parallel Execution and Coordination for GUI Agents](https://arxiv.org/html/2607.22689v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [LazyMem: Retrieve Broadly, Construct Selectively for Efficient Long-Term Agent Memory](https://arxiv.org/html/2607.22690v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [PANOPTICON: A PII-Based Assemblage of Naturalistic Output Tokens for Investigating Privacy Leakage Within LLM Context Window](https://arxiv.org/html/2607.22695v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Test-Time Coverage: Test-Conditioned Data Curation for Deployment-Aware Learning](https://arxiv.org/html/2607.22697v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [StepX-Edge: An On-Device UI Vision-Language Model via Architecture-Training-Deployment Co-Design](https://arxiv.org/html/2607.22708v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [CORVUS: Context Optimization and Reduction Via Underlying Synchronization for LLM Coding Agents](https://arxiv.org/html/2607.22711v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Visual Token Compression Enhances Robustness of MLLMs](https://arxiv.org/html/2607.22716v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Progress-conditioned Group Policy Optimization for Long-Horizon Agentic Tasks](https://arxiv.org/html/2607.22724v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [PCA: Persistence-Aware Compression and Aggregation for Fast Video Large Language Models](https://arxiv.org/html/2607.22726v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Spectral Dynamics of Semantic Drift in Clinical Multi-Agent Language Model Networks](https://arxiv.org/html/2607.22758v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Beyond Shapley: An Influence-Based Data Auditing Pipeline for LLM Alignment and Evaluation](https://arxiv.org/html/2607.22766v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [DomainPilot: Domain-Level Loss-Guided Two-Stage Data Mixture Optimization for Efficient Language Model Fine-Tuning](https://arxiv.org/html/2607.22769v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [What Softmax Throws Away: Mass-Aware Attention for Evidence Accumulation](https://arxiv.org/html/2607.22781v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [FusionML: Prefill, Not Decode - Mechanism and Boundaries of CPU+GPU Co-Execution on Unified-Memory Apple Silicon](https://arxiv.org/html/2607.22785v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [The Sparsity Tax: Weight Sparsity Trade-offs in Event-Driven SIMD and SIMT Neuromorphic Cores](https://arxiv.org/html/2607.22790v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents](https://arxiv.org/html/2607.22798v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [The Best Programming Language for Tokenmaxxing: An Investigation of Coding Agent Behavior Across Programming Languages](https://arxiv.org/html/2607.22807v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution](https://arxiv.org/html/2607.22832v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Coordinated Networking for On-Device Agent-Augmented Real-Time Communication](https://arxiv.org/html/2607.22854v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [What Can Be Enforced? A Theory of Certified Runtime Safety for Tool-Using Agents](https://arxiv.org/html/2607.22868v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Same Predictions, Different Reasons: The Effect of Quantization on Model Explanations](https://arxiv.org/html/2607.22872v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Do Coverage and Mutation Scores of LLM-Generated Test Suites Correlate with Their Effectiveness? (Replicability Study)](https://arxiv.org/html/2607.22880v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Evaluating and Mitigating the Misguidance Effect of Buggy Code in LLM-Generated Unit Tests](https://arxiv.org/html/2607.22883v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [AssumptionMiner: Extracting, Tracing, and Revising Implicit Assumptions in LLM Code Generation](https://arxiv.org/html/2607.22898v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Agent Team Work Zone: An Automated, Persistent Workspace for Long-Lived Claude Code Agent Teams](https://arxiv.org/html/2607.22917v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Not All LLM Reasoning is Visible in the Chain-of-Thought](https://arxiv.org/html/2607.22925v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [SAGE: Safety-First Defense-in-Depth Guardrails for Verified Lifecycle Control of High-Impact Generative AI](https://arxiv.org/html/2607.22926v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Hidden Boundary Motion in Transformer Optimization: Function-Space Orthogonalization of Affine Weight and Bias Updates](https://arxiv.org/html/2607.22927v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Beyond Exact Match: How Evaluation Methodology Dominates Model Choice in LLM-Based Product Attribute Extraction](https://arxiv.org/html/2607.22949v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Modeling Memory-Dependent Reliability of LLMs: A Hidden Markov Model](https://arxiv.org/html/2607.22951v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Share No More Than the Request Requires: Federated Disclosure for Perspective-Aware AI](https://arxiv.org/html/2607.22953v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [ConsistencyGate: Preventing Memory Contamination in LLM Agents via Self-Consistency Admission Control](https://arxiv.org/html/2607.22962v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline](https://arxiv.org/html/2607.22997v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [WCM: World-Cognition Model for Generalizable Human-Robot Interaction](https://arxiv.org/html/2607.22999v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Adversarial Test-Hardening for AI-Written Code: An Instrument Autopsy and a Pre-Registered Causal Estimate of the Critic Loop](https://arxiv.org/html/2607.23002v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Mini-batch Noise Lowers Sharpness via Dominant-Subspace Fluctuations](https://arxiv.org/pdf/2607.23012v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Mask2Shield: Strengthening LLM Safety against Neuron-Pruning Attacks](https://arxiv.org/html/2607.23015v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Stress-testing large language model agents in a robotic chemistry laboratory](https://arxiv.org/pdf/2607.23045v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Structured Redundancy Modeling for Efficient Visual Token Pruning in High-Resolution MLLMs](https://arxiv.org/html/2607.23046v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [MixQuant: Adaptive Mixed-Precision Quantization for Large Language Models](https://arxiv.org/html/2607.23047v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [The Entropic Bound for Transformers: Why Static Rank Fails and Attention-Native Rank Recovers](https://arxiv.org/html/2607.23050v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Through the Bottleneck: How Multi-head Latent Attention Separates Content from Position in Language Models](https://arxiv.org/html/2607.23054v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [SymStep: Symbolic Step Verification for Logical Reasoning](https://arxiv.org/html/2607.23055v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Compiler-Grounded Hierarchical Diagnosis for LLM-Based Triton Kernel Optimization](https://arxiv.org/html/2607.23089v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Decoding the Skew: Distribution-Aware MoE Inference with Adaptive Kernel Dispatch](https://arxiv.org/html/2607.23099v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Gleam: Adaptive Network-Efficient CUDA API Remoting for Cross-Device GPU Sharing over LANs](https://arxiv.org/html/2607.23115v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [SQBench: A Benchmark for Evaluating Task Delivery by Language-Model Agents in Production-Oriented Workflows](https://arxiv.org/html/2607.23123v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [False Prophets: On the Security of World Models in Agentic Systems](https://arxiv.org/html/2607.23147v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [CachedSearch: Training-Free Cached Exploration for Test-Time Search in Video Diffusion](https://arxiv.org/html/2607.23159v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [OmniScope: Modality-Decoupled Token Compression for Omnimodal Large Language Models](https://arxiv.org/pdf/2607.23193v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [From Score Learning to Discretized Sampling: An End-to-End Generalization Analysis of Diffusion Models](https://arxiv.org/html/2607.23226v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Libra: Taming Attention Workload Skew in Long-Context LLM Training with Bounded Sequence Pool](https://arxiv.org/html/2607.23250v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [SeekJudge: A Practical Reward Framework for Reinforcement Learning in Computer-Use Agents](https://arxiv.org/html/2607.23263v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [X-Stage: An Overlooked Pipeline Stage for Communication-Computation Overlap in DiT Inference](https://arxiv.org/html/2607.23264v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [WaveZip: Wavelet-Driven Space-Time Decoupling for Video Token Condensation](https://arxiv.org/html/2607.23265v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [AllocBench: Measuring Online Tool Allocation Capability in LLM Agents](https://arxiv.org/html/2607.23332v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Hallucination Rates in Language Generation](https://arxiv.org/html/2607.23361v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [On the Impossibility of Unbiased and Length-Invariant Policy Optimization with Outcome Rewards](https://arxiv.org/html/2607.23364v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Codebook Capacity Governs Perceptual Quality Across Resolutions in Hierarchical Discrete Video Compression](https://arxiv.org/html/2607.23366v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [UltraViT: Latency-Optimized On-device Vision Encoder for Large Vision-Language Models](https://arxiv.org/html/2607.23373v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [When Activation Oracles Learn Not to Read: Concept-Specific Blind Spots in Fine-Tuned Oracles](https://arxiv.org/html/2607.23379v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Confidently Wrong: Exception Chain Collapse in Frontier LLM Rule Evaluation](https://arxiv.org/html/2607.23386v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [When Can Depth Replace Precision? A Resource Theory of Quantized Neural Computation](https://arxiv.org/html/2607.23390v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Inference-Time Consensus for Mitigating Hidden Behaviors from LLM Fine-Tuning](https://arxiv.org/html/2607.23394v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Characterizing Warp Divergence from Pascal to Blackwell](https://arxiv.org/html/2607.23402v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [TLA+-Bench: An Execution-Grounded Benchmark and Dataset for Natural-Language to TLA Specification Generation](https://arxiv.org/html/2607.23425v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels](https://arxiv.org/pdf/2607.23438v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Isolated but Exposed: Persistence-Based Memory Extraction Attack on LLM Agents](https://arxiv.org/html/2607.23444v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Omni-Prune: Query-Aware Unified Token Pruning for Efficient Omnimodal Large Language Models](https://arxiv.org/html/2607.23445v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Two Regimes of Chain-of-Thought Unfaithfulness: Metric-Based Detection Fails Where Models Are Wrong](https://arxiv.org/html/2607.23458v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [VIPER: Visual In-Context Physics Reasoning for Physically Plausible Video Generation](https://arxiv.org/html/2607.23472v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [ATLAS: Automated Approximation of Transformers for Efficient Homomorphic Inference in One Hour](https://arxiv.org/html/2607.23478v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Do LLMs Know Their Vulnerable Scenarios?](https://arxiv.org/html/2607.23496v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [MemVLN: Episodic and Procedural Memory for Vision-and-Language Navigation](https://arxiv.org/html/2607.23504v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Novel Claim or Déjà Vu? Rethinking "Contamination-Free'' Dynamic Evaluation for Multimodal Automated Fact-Checking](https://arxiv.org/html/2607.23514v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Real-Time Human-Centric World Modeling for Upper-Body Human-Object Interaction](https://arxiv.org/html/2607.23517v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric](https://arxiv.org/html/2607.23532v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Language Shapes Instruction Hierarchy Compliance in Multilingual LLMs](https://arxiv.org/html/2607.23545v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Verification-Notebook Learning for Source-Aware Multimodal Misinformation Detection](https://arxiv.org/html/2607.23581v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Are You Still the Agent I Authorized? Earned Authority under a Fixed Ceiling for Evolving Agents](https://arxiv.org/html/2607.23586v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [JarvisHub: An Open Harness for Canvas-Native Multimodal Creative Agents](https://arxiv.org/html/2607.23588v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Action from Adjacent Set in Physical Space Outperforms the Best Prediction in World Models](https://arxiv.org/html/2607.23602v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Hybrid Advantage Estimation with Unified Critic for VLM Agentic Reinforcement Learning](https://arxiv.org/html/2607.23605v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Where Is the Cost of Third-Party API Routers in Agentic Software Development?](https://arxiv.org/html/2607.23624v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Plans Work in Mysterious Ways: Evaluating a Plan Mode for Spreadsheet Agents](https://arxiv.org/html/2607.23670v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV](https://arxiv.org/html/2607.23693v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Offline-Online Curriculum RL for Multimodal Reasoning](https://arxiv.org/html/2607.23700v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Try Once, Then Optimal: De-Redundified Procedure Memory for Cross-Episode Exploration Amortization](https://arxiv.org/html/2607.23702v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [LabRobFail: A Benchmark for Robotic Failure Analysis in Chemical Self-driving Laboratory](https://arxiv.org/html/2607.23704v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [The Illusion of Secure LLM Code: Closing the Security Gap via Iterative Reprompting](https://arxiv.org/html/2607.23710v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [The Intruder Threshold: A Spectral Law for LoRA Fine-Tuning](https://arxiv.org/html/2607.23711v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [E-Bench: Benchmarking Multi-Step Tool-Use Agents in Real-World Product Scenarios](https://arxiv.org/html/2607.23722v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Outcome-Confounded Local Supervision in On-Policy Distillation](https://arxiv.org/html/2607.23731v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [WISERouter: LLM Routing with Workload Budget Constraint](https://arxiv.org/html/2607.23765v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Training Language Models to Cooperate with Inference-Time Controllers](https://arxiv.org/html/2607.23771v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [$N_0$-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens](https://arxiv.org/html/2607.23782v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [$N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation](https://arxiv.org/html/2607.23783v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement](https://arxiv.org/html/2607.23802v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [ACM: Agentic Context Management for Long Horizon Tasks](https://arxiv.org/html/2607.23809v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Kalypso: Relational LLM Serving](https://arxiv.org/html/2607.23815v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [TriShieldRAG: 3 Rings, One Blind Spot in Layered Defenses for Retrieval-Augmented Generation](https://arxiv.org/html/2607.23838v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [OmniCache: Multidimensional Hierarchical Feature Caching For Diffusion Models](https://arxiv.org/html/2607.23844v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents](https://arxiv.org/html/2607.23870v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems](https://arxiv.org/html/2607.23884v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [WorldDiT: A Unified Diffusion Architecture for World and Action Modeling](https://arxiv.org/html/2607.23909v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Reality Monitoring in Large Language Models: Self-Knowledge That Transforms with Conversation Memory](https://arxiv.org/html/2607.23927v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [MemTX: Transactional Belief Commit for Stateful Agent Memory](https://arxiv.org/html/2607.23929v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving](https://arxiv.org/html/2607.23933v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [EviBack: Search-Agent Reinforcement Learning via Evidence-Constrained Teacher Backoff](https://arxiv.org/html/2607.23955v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [LeapBot-WA: World-Anchor Action Models via Predictive Latent Alignments](https://arxiv.org/html/2607.23969v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [SyRuP: Enhancing System-Prompt Following via Reward-Guided Prediction in LLM Decoding](https://arxiv.org/html/2607.23991v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [ContainmentBench: Trace-Based Evaluation of Post-Exposure Containment in Tool-Using LLM Agents](https://arxiv.org/html/2607.23999v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [FutureRTC: Real-Time Robot Execution with Anticipatory-Conditioned Action Chunking](https://arxiv.org/html/2607.24008v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [When Should Active RAG Retrieve? A Budget-Aware Evaluation of Utility, Calibration, and Cost](https://arxiv.org/html/2607.24010v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Sol-Attn: Accelerating Video Generation Inference via On-the-Fly Attention Sparsification](https://arxiv.org/html/2607.24027v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation](https://arxiv.org/html/2607.24054v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [The Cost of Knowing: A Resource-Aware Protocol for Benchmarking Hallucination Beyond Static Leaderboards](https://arxiv.org/html/2607.24063v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents](https://arxiv.org/html/2607.24097v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Scaling GUI Agents with Visual State Transitions](https://arxiv.org/html/2607.24112v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Grading the Narrators: An Isnad-Rijal Framework for Claim-Level Provenance in Multi-Agent Knowledge Systems](https://arxiv.org/html/2607.24117v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference](https://arxiv.org/html/2607.24148v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [UniGen-AR: Unifying Visual Generation with Auto-Regressive Modeling](https://arxiv.org/html/2607.24157v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [DeVA: Decoupled Video-Action Model with physical guidance for robot policy learning](https://arxiv.org/html/2607.24159v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Agent-UCT: Upper Confidence Bounds Applied to Trees for Agentic Workflow Optimization with Cost-Awareness](https://arxiv.org/html/2607.24162v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Do Current Retrievers Cover All the Evidence? A Controlled Study of Conjunctive Cross-Page Retrieval](https://arxiv.org/html/2607.24165v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Falsifiable Commitment Planning for Self-Correcting Web Agents](https://arxiv.org/html/2607.24167v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Just Testing, Move Along: Evasion of LLM-based System Log Interpretation by Prompt Injection](https://arxiv.org/html/2607.24174v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [A New Role for Relevance: Guiding Corpus Interaction in Agentic Search](https://arxiv.org/html/2607.24223v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [KAP: Bridging the Knowledge Selection-Runtime Consumption Gap in LLM Systems](https://arxiv.org/html/2607.24260v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [FeelWorld: Visuo-Tactile World Model for Hierarchical Contact Prediction and Planning](https://arxiv.org/html/2607.24267v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Accuracy Hides How Language Models Fail: Measuring Failure States Under Matched Output Budgets](https://arxiv.org/html/2607.24268v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent Protocol Distillation in Agentic Search](https://arxiv.org/html/2607.24280v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Self-Authored Verification Is Unreliable in Heuristic Self-Improving Agents](https://arxiv.org/html/2607.24300v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Rethinking the Generation Order of Block Diffusion Language Models](https://arxiv.org/html/2607.24306v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [DynaCalKV: Key-Value Cache Compression via Head Grouping and Adaptive Rank Allocation](https://arxiv.org/html/2607.24331v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Beyond Aggregate Risk: Role-Stratified Conformal Risk Control for LLM Tool Calls](https://arxiv.org/html/2607.24343v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory](https://arxiv.org/html/2607.24368v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [MXAttention: Data-Free Optimal Scaling and Pre-Normalization Quantization for MXFP4 Attention](https://arxiv.org/html/2607.24377v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [When LLM Defenses Backfire: Characterizing Safety, Performance, and Cost Trade-offs](https://arxiv.org/html/2607.24392v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Mixture-of-Thought-Tokens: Unifying Perception and Reasoning for Free-form Multimodal Grounding](https://arxiv.org/html/2607.24407v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference](https://arxiv.org/html/2607.24434v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Bigger or Cheaper? Scale and Quantization Effects on Uncertainty Signals in Vision-Language Models Under Image Degradation](https://arxiv.org/html/2607.24440v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [From Execution to Capability: Scientific Experience Consolidation via Procedural Knowledge Synthesis](https://arxiv.org/html/2607.24459v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Grounding latent algorithm routing in transformer reasoning](https://arxiv.org/html/2607.24471v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [ArmnetBench v0.1: Parallel Real-World Evaluation of Manipulation Policies on a Low-Cost Arm Farm](https://arxiv.org/html/2607.24481v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [What do Reward Models Memorize?](https://arxiv.org/pdf/2607.24484v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [τ: Learning Touch-Augmented Vision-Language-Action Models from Future Visual Supervision](https://arxiv.org/html/2607.24485v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [UNIFUSION: Adapting Autoregressive Language Models into Discrete Diffusion under a Unified Reverse-Rate Objective](https://arxiv.org/html/2607.24507v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [DecoupleMix: Decoupled Ratio Search and Convex Allocation for Scalable VLM Data Recipes](https://arxiv.org/html/2607.24516v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Task-Conditional Faithfulness Auditing of Multimodal LLMs for Grid Diagnosis](https://arxiv.org/html/2607.24539v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [LOCKS: Page-Local Compact Key Summaries for Efficient Long-Context Decoding](https://arxiv.org/html/2607.24555v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Hierarchical Group-Conditional Conformal Risk Control for Selective Prediction in Language Models](https://arxiv.org/html/2607.24562v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [The Visual Bottleneck: Sparse-Frame Adaptation of MLLMs for Joint Spatial-Temporal Video Grounding](https://arxiv.org/html/2607.24570v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [CADER: Confidence-Aware Dynamic Evidence Reasoning for Long-Video Understanding](https://arxiv.org/html/2607.24582v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [From Data to Device: ELMOD An Efficient German-First 2.7B Language Model for Mobile Inference](https://arxiv.org/html/2607.24585v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [D-Score: A Spectral Hidden-State Signal for Hallucination Detection in Large Language Models](https://arxiv.org/html/2607.24586v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [PIVOT: Efficient Query-Group Indexing for Token-Level Sparse Attention](https://arxiv.org/html/2607.24593v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair](https://arxiv.org/html/2607.24604v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [APPA: Recoverable Information-Flow Control for Real-World LLM Agents](https://arxiv.org/html/2607.24625v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Sparse Autoencoders Encode Both Concepts and Functions: The Downstream Geometry of Feature Effects](https://arxiv.org/html/2607.24645v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Efficiency Matters in Autonomous Research](https://arxiv.org/html/2607.24647v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels](https://arxiv.org/html/2607.24651v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Kimi K3: Open Frontier Intelligence](https://arxiv.org/html/2607.24653v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [A corrective agentic hybrid RAG and an operations-grounded evaluation for a scientific facility](https://arxiv.org/html/2607.24663v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [MMOE: Modernizing Diffusion Transformers with Efficient Expert Design](https://arxiv.org/html/2607.24665v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Eviction as Estimation: A Fixed-Lag Smoothing View of Test-Time Memory, and When Measuring Beats Accumulating](https://arxiv.org/html/2607.24667v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Denial of Deadline: Network-Driven Accuracy Collapse in Distributed Inference Pipelines](https://arxiv.org/html/2607.24692v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [DataOrchestra: Learning to Orchestrate Per-Example Curation of Pretraining Data](https://arxiv.org/html/2607.24717v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation](https://arxiv.org/html/2607.24720v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04
- [Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation](https://arxiv.org/html/2607.24731v1) — first-public（Asia/Shanghai）：2026-07-28；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、199/199 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
