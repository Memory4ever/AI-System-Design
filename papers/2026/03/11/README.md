# Daily Research — 2026-03-11

**Research Date:** 2026-03-11

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-10 09:00:00 ～ 2026-03-11 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。2026-09-03 fresh-context 反证审计已重开；当前机器结构和既有 retained Review 仍可复用，但 denominator completeness 尚未按“不得抽样、逐项判断”合同重新验收。


## Executive Summary

> **2026-09-03 Semantic Reopen：** 旧 `Complete` 声明已被 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 取代。在 `MAR26-FC-001/MAR26-FC-002/MAR26-FC-003` 与 `MAR26-FC-004` 关闭前，本日报不得恢复 `Complete`；validator 通过只表示机器接口自洽。

严格窗口 raw/registered/screened=656/656/656；denominator=41、pre-denominator closures=615。exact-v1 Review complete=41、blocked=0；Integrate 建议=3。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-11 |
| Window End | 2026-03-11 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260311-AUTHOR-41 |
| Denominator Frozen At | 2026-09-02T16:27:58.265174+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-10T09:00:00+08:00 | 2026-03-11T09:00:00+08:00 | 2026-09-02T16:27:58.265174+08:00 | official-schedule recovery receipt + 656/656 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 656 | SF-2026-ARXIV-2603-08727;SF-2026-ARXIV-2603-08739;SF-2026-ARXIV-2603-08743;SF-2026-ARXIV-2603-08747;SF-2026-ARXIV-2603-08755;SF-2026-ARXIV-2603-08761;SF-2026-ARXIV-2603-08797;SF-2026-ARXIV-2603-08806;SF-2026-ARXIV-2603-08835;SF-2026-ARXIV-2603-08852;SF-2026-ARXIV-2603-08960;SF-2026-ARXIV-2603-09023;SF-2026-ARXIV-2603-09046;SF-2026-ARXIV-2603-09079;SF-2026-ARXIV-2603-09086;SF-2026-ARXIV-2603-09117;SF-2026-ARXIV-2603-09121;SF-2026-ARXIV-2603-09127;SF-2026-ARXIV-2603-09157;SF-2026-ARXIV-2603-09180;SF-2026-ARXIV-2603-09192;SF-2026-ARXIV-2603-09216;SF-2026-ARXIV-2603-09221;SF-2026-ARXIV-2603-09241;SF-2026-ARXIV-2603-09290;SF-2026-ARXIV-2603-09297;SF-2026-ARXIV-2603-09435;SF-2026-ARXIV-2603-09453;SF-2026-ARXIV-2603-09488;SF-2026-ARXIV-2603-09513;SF-2026-ARXIV-2603-09555;SF-2026-ARXIV-2603-09619;SF-2026-ARXIV-2603-09657;SF-2026-ARXIV-2603-09692;SF-2026-ARXIV-2603-09716;SF-2026-ARXIV-2603-09730;SF-2026-ARXIV-2603-09756;SF-2026-ARXIV-2603-09821;SF-2026-ARXIV-2603-09877;SF-2026-ARXIV-2603-09891;SF-2026-ARXIV-2603-09892 | pages=100; prefixes=00..99; final_cursor=end; registered=656; screened=656; retained=41; closure=615 | 2026-03-11T01:00:00+00:00 | screening-ledger-final.json#sha256=c0913c0e14e85fd47b9b609acf4255de66818a1b7f7228df7069d2ed7838e99d; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260311:start -->作者侧已逐项筛选全部 656 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260311:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-08727 | arXiv:2603.08727v1 | paper-v1:2603.08727 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08727 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08727 | no |
| SF-2026-ARXIV-2603-08739 | arXiv:2603.08739v1 | paper-v1:2603.08739 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08739 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08739 | no |
| SF-2026-ARXIV-2603-08743 | arXiv:2603.08743v1 | paper-v1:2603.08743 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08743 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08743 | no |
| SF-2026-ARXIV-2603-08747 | arXiv:2603.08747v1 | paper-v1:2603.08747 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08747 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08747 | no |
| SF-2026-ARXIV-2603-08755 | arXiv:2603.08755v1 | paper-v1:2603.08755 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08755 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08755 | no |
| SF-2026-ARXIV-2603-08761 | arXiv:2603.08761v1 | paper-v1:2603.08761 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08761 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08761 | no |
| SF-2026-ARXIV-2603-08797 | arXiv:2603.08797v1 | paper-v1:2603.08797 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-08797 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2603-08797 | no |
| SF-2026-ARXIV-2603-08806 | arXiv:2603.08806v1 | paper-v1:2603.08806 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08806 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08806 | no |
| SF-2026-ARXIV-2603-08835 | arXiv:2603.08835v1 | paper-v1:2603.08835 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08835 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08835 | no |
| SF-2026-ARXIV-2603-08852 | arXiv:2603.08852v1 | paper-v1:2603.08852 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08852 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08852 | no |
| SF-2026-ARXIV-2603-08960 | arXiv:2603.08960v1 | paper-v1:2603.08960 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08960 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08960 | no |
| SF-2026-ARXIV-2603-09023 | arXiv:2603.09023v1 | paper-v1:2603.09023 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-09023 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2603-09023 | no |
| SF-2026-ARXIV-2603-09046 | arXiv:2603.09046v1 | paper-v1:2603.09046 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09046 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09046 | no |
| SF-2026-ARXIV-2603-09079 | arXiv:2603.09079v1 | paper-v1:2603.09079 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09079 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09079 | no |
| SF-2026-ARXIV-2603-09086 | arXiv:2603.09086v1 | paper-v1:2603.09086 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09086 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09086 | no |
| SF-2026-ARXIV-2603-09117 | arXiv:2603.09117v1 | paper-v1:2603.09117 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09117 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09117 | no |
| SF-2026-ARXIV-2603-09121 | arXiv:2603.09121v1 | paper-v1:2603.09121 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09121 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09121 | no |
| SF-2026-ARXIV-2603-09127 | arXiv:2603.09127v1 | paper-v1:2603.09127 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09127 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09127 | no |
| SF-2026-ARXIV-2603-09157 | arXiv:2603.09157v1 | paper-v1:2603.09157 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09157 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09157 | no |
| SF-2026-ARXIV-2603-09180 | arXiv:2603.09180v1 | paper-v1:2603.09180 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09180 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09180 | no |
| SF-2026-ARXIV-2603-09192 | arXiv:2603.09192v1 | paper-v1:2603.09192 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09192 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09192 | no |
| SF-2026-ARXIV-2603-09216 | arXiv:2603.09216v1 | paper-v1:2603.09216 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09216 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09216 | no |
| SF-2026-ARXIV-2603-09221 | arXiv:2603.09221v1 | paper-v1:2603.09221 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09221 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09221 | no |
| SF-2026-ARXIV-2603-09241 | arXiv:2603.09241v1 | paper-v1:2603.09241 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09241 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09241 | no |
| SF-2026-ARXIV-2603-09290 | arXiv:2603.09290v1 | paper-v1:2603.09290 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09290 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09290 | no |
| SF-2026-ARXIV-2603-09297 | arXiv:2603.09297v1 | paper-v1:2603.09297 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09297 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09297 | no |
| SF-2026-ARXIV-2603-09435 | arXiv:2603.09435v1 | paper-v1:2603.09435 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09435 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09435 | no |
| SF-2026-ARXIV-2603-09453 | arXiv:2603.09453v1 | paper-v1:2603.09453 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09453 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09453 | no |
| SF-2026-ARXIV-2603-09488 | arXiv:2603.09488v1 | paper-v1:2603.09488 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09488 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09488 | no |
| SF-2026-ARXIV-2603-09513 | arXiv:2603.09513v1 | paper-v1:2603.09513 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09513 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09513 | no |
| SF-2026-ARXIV-2603-09555 | arXiv:2603.09555v1 | paper-v1:2603.09555 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-09555 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2603-09555 | no |
| SF-2026-ARXIV-2603-09619 | arXiv:2603.09619v1 | paper-v1:2603.09619 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09619 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09619 | no |
| SF-2026-ARXIV-2603-09657 | arXiv:2603.09657v1 | paper-v1:2603.09657 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09657 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09657 | no |
| SF-2026-ARXIV-2603-09692 | arXiv:2603.09692v1 | paper-v1:2603.09692 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09692 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09692 | no |
| SF-2026-ARXIV-2603-09716 | arXiv:2603.09716v1 | paper-v1:2603.09716 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09716 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09716 | no |
| SF-2026-ARXIV-2603-09730 | arXiv:2603.09730v1 | paper-v1:2603.09730 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09730 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09730 | no |
| SF-2026-ARXIV-2603-09756 | arXiv:2603.09756v1 | paper-v1:2603.09756 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09756 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09756 | no |
| SF-2026-ARXIV-2603-09821 | arXiv:2603.09821v1 | paper-v1:2603.09821 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09821 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09821 | no |
| SF-2026-ARXIV-2603-09877 | arXiv:2603.09877v1 | paper-v1:2603.09877 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09877 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09877 | no |
| SF-2026-ARXIV-2603-09891 | arXiv:2603.09891v1 | paper-v1:2603.09891 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09891 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09891 | no |
| SF-2026-ARXIV-2603-09892 | arXiv:2603.09892v1 | paper-v1:2603.09892 | 2026-W11 | 2026-03-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09892 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09892 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-08727 | RP-90f1f92b6d3b31fe | standard | arXiv:2603.08727v1 | SRC-ARXIV@arXiv:2603.08727v1 | arXiv:2603.08727v1 HTML — §IV Methodology [facet=method]; https://arxiv.org/html/2603.08727v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08727v1.html; sha256:a1c8fb742c0fc5431b0004efd00e59b3fad35a6ca90f1da583ce9cd7d1e3b6b6 | arXiv:2603.08727v1 HTML — §V-D Evaluation Metrics and Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.08727v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08727v1.html; sha256:a1c8fb742c0fc5431b0004efd00e59b3fad35a6ca90f1da583ce9cd7d1e3b6b6 | arXiv:2603.08727v1 HTML — §VI Conclusion [facet=limitations]; https://arxiv.org/html/2603.08727v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08727v1.html; sha256:a1c8fb742c0fc5431b0004efd00e59b3fad35a6ca90f1da583ce9cd7d1e3b6b6 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08727v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08727 | complete |
| SF-2026-ARXIV-2603-08739 | RP-93e16dad686c3eaf | standard | arXiv:2603.08739v1 | SRC-ARXIV@arXiv:2603.08739v1 | arXiv:2603.08739v1 HTML — §4.1. Overview [facet=method]; https://arxiv.org/html/2603.08739v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08739v1.html; sha256:023c3d0a54ac2412cd6dc20eeebb3a1fcd53d0ca84f4ab8a8e3b17cdd46d7377 | arXiv:2603.08739v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.08739v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08739v1.html; sha256:023c3d0a54ac2412cd6dc20eeebb3a1fcd53d0ca84f4ab8a8e3b17cdd46d7377 | arXiv:2603.08739v1 HTML — §6. Conclusion [facet=limitations]; https://arxiv.org/html/2603.08739v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08739v1.html; sha256:023c3d0a54ac2412cd6dc20eeebb3a1fcd53d0ca84f4ab8a8e3b17cdd46d7377 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08739v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08739 | complete |
| SF-2026-ARXIV-2603-08743 | RP-ebe5bb85f5fdbb1e | standard | arXiv:2603.08743v1 | SRC-ARXIV@arXiv:2603.08743v1 | arXiv:2603.08743v1 HTML — §4 Method [facet=method]; https://arxiv.org/html/2603.08743v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08743v1.html; sha256:60ef65bb98b771ac8cb264ec20251f1e6b7c1e98d896caf45593c511d47c8256 | arXiv:2603.08743v1 HTML — §Appendix D Additional Information of Ablation Experiments [facet=evaluation]; https://arxiv.org/html/2603.08743v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08743v1.html; sha256:60ef65bb98b771ac8cb264ec20251f1e6b7c1e98d896caf45593c511d47c8256 | arXiv:2603.08743v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.08743v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08743v1.html; sha256:60ef65bb98b771ac8cb264ec20251f1e6b7c1e98d896caf45593c511d47c8256 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08743v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08743 | complete |
| SF-2026-ARXIV-2603-08747 | RP-5edc14b1ae423c8e | standard | arXiv:2603.08747v1 | SRC-ARXIV@arXiv:2603.08747v1 | arXiv:2603.08747v1 HTML — §3 Experimental Design [facet=method]; https://arxiv.org/html/2603.08747v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08747v1.html; sha256:8f14c85dedf6e5d6b759839d0c15b22bcb4ec0b7c03ca86b7244781b2be49185 | arXiv:2603.08747v1 HTML — §4 Results [facet=evaluation]; https://arxiv.org/html/2603.08747v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08747v1.html; sha256:8f14c85dedf6e5d6b759839d0c15b22bcb4ec0b7c03ca86b7244781b2be49185 | arXiv:2603.08747v1 HTML — §5 Conclusion and Discussion [facet=limitations]; https://arxiv.org/html/2603.08747v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08747v1.html; sha256:8f14c85dedf6e5d6b759839d0c15b22bcb4ec0b7c03ca86b7244781b2be49185 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08747v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08747 | complete |
| SF-2026-ARXIV-2603-08755 | RP-d27e013307f09759 | standard | arXiv:2603.08755v1 | SRC-ARXIV@arXiv:2603.08755v1 | arXiv:2603.08755v1 HTML — §2.1 Agent Frameworks [facet=method]; https://arxiv.org/html/2603.08755v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08755v1.html; sha256:07a14e3d28507e1f112da57c9a312decac152aa2a41efc4c7542c99e4d96d6ef | arXiv:2603.08755v1 HTML — §10 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.08755v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08755v1.html; sha256:07a14e3d28507e1f112da57c9a312decac152aa2a41efc4c7542c99e4d96d6ef | arXiv:2603.08755v1 HTML — §11.1 Limitations [facet=limitations]; https://arxiv.org/html/2603.08755v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08755v1.html; sha256:07a14e3d28507e1f112da57c9a312decac152aa2a41efc4c7542c99e4d96d6ef | arXiv exact-v1 identity https://arxiv.org/abs/2603.08755v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08755 | complete |
| SF-2026-ARXIV-2603-08761 | RP-78e52254ce4ee372 | standard | arXiv:2603.08761v1 | SRC-ARXIV@arXiv:2603.08761v1 | arXiv:2603.08761v1 HTML — §3 Formal Framework [facet=method]; https://arxiv.org/html/2603.08761v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08761v1.html; sha256:37ef1a43f18cddf638668fc6f94378fcc4568d3ce89146c2f4b19fdcf3798316 | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.08761v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08761v1.html; sha256:37ef1a43f18cddf638668fc6f94378fcc4568d3ce89146c2f4b19fdcf3798316 | arXiv:2603.08761v1 HTML — §8 Discussion [facet=limitations]; https://arxiv.org/html/2603.08761v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08761v1.html; sha256:37ef1a43f18cddf638668fc6f94378fcc4568d3ce89146c2f4b19fdcf3798316 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08761v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08761 | complete |
| SF-2026-ARXIV-2603-08797 | RP-f4d7206330f69280 | deep | arXiv:2603.08797v1 | SRC-ARXIV@arXiv:2603.08797v1 | arXiv:2603.08797v1 HTML — §3.1–§3.3 components, MILP, batching and early dropping [facet=method]; https://arxiv.org/html/2603.08797v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08797v1.html; sha256:db99c3e7ff897a61ac9892262013d46b4d9a917a5df17f137a6882748fc91d58 | arXiv:2603.08797v1 HTML — §4 Evaluation Methodology + §5 Results [facet=evaluation]; https://arxiv.org/html/2603.08797v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08797v1.html; sha256:db99c3e7ff897a61ac9892262013d46b4d9a917a5df17f137a6882748fc91d58 | arXiv:2603.08797v1 HTML — §7 Future Work and Conclusion [facet=limitations]; https://arxiv.org/html/2603.08797v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08797v1.html; sha256:db99c3e7ff897a61ac9892262013d46b4d9a917a5df17f137a6882748fc91d58 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08797v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08797 | complete |
| SF-2026-ARXIV-2603-08806 | RP-359bd74b59e413f0 | standard | arXiv:2603.08806v1 | SRC-ARXIV@arXiv:2603.08806v1 | arXiv:2603.08806v1 HTML — §3 The TDAD Methodology [facet=method]; https://arxiv.org/html/2603.08806v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08806v1.html; sha256:a0b317a87d934851bd7c68494ddd6aa7e674da36a31b1ead97b38164e09b99f4 | arXiv:2603.08806v1 HTML — §6 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.08806v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08806v1.html; sha256:a0b317a87d934851bd7c68494ddd6aa7e674da36a31b1ead97b38164e09b99f4 | arXiv:2603.08806v1 HTML — §8 Limitations [facet=limitations]; https://arxiv.org/html/2603.08806v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08806v1.html; sha256:a0b317a87d934851bd7c68494ddd6aa7e674da36a31b1ead97b38164e09b99f4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08806v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08806 | complete |
| SF-2026-ARXIV-2603-08835 | RP-45684d13f1d883ad | standard | arXiv:2603.08835v1 | SRC-ARXIV@arXiv:2603.08835v1 | arXiv:2603.08835v1 HTML — §3.2 Module Architecture [facet=method]; https://arxiv.org/html/2603.08835v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08835v1.html; sha256:dfad5d6c478a7daf4abb2148018cc5f74df0f55cdcbfa99858520d11a8e6dd63 | arXiv:2603.08835v1 HTML — §4.2 Results [facet=evaluation]; https://arxiv.org/html/2603.08835v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08835v1.html; sha256:dfad5d6c478a7daf4abb2148018cc5f74df0f55cdcbfa99858520d11a8e6dd63 | arXiv:2603.08835v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.08835v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08835v1.html; sha256:dfad5d6c478a7daf4abb2148018cc5f74df0f55cdcbfa99858520d11a8e6dd63 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08835v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08835 | complete |
| SF-2026-ARXIV-2603-08852 | RP-6b9a74f3c92aa3c3 | standard | arXiv:2603.08852v1 | SRC-ARXIV@arXiv:2603.08852v1 | arXiv:2603.08852v1 HTML — §5.6 Statistical Methodology [facet=method]; https://arxiv.org/html/2603.08852v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08852v1.html; sha256:74b0247eda27542b3d31ca5c7fe9f0cd32444d8ebd311ccbf728b20744a578d0 | arXiv:2603.08852v1 HTML — §5.4 LLM-as-Judge Evaluation [facet=evaluation]; https://arxiv.org/html/2603.08852v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08852v1.html; sha256:74b0247eda27542b3d31ca5c7fe9f0cd32444d8ebd311ccbf728b20744a578d0 | arXiv:2603.08852v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.08852v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08852v1.html; sha256:74b0247eda27542b3d31ca5c7fe9f0cd32444d8ebd311ccbf728b20744a578d0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08852v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08852 | complete |
| SF-2026-ARXIV-2603-08960 | RP-b0ecacc0edb9fb7a | standard | arXiv:2603.08960v1 | SRC-ARXIV@arXiv:2603.08960v1 | arXiv:2603.08960v1 HTML — §4 Evaluation Methodology [facet=method]; https://arxiv.org/html/2603.08960v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08960v1.html; sha256:2e01227172a0a7c9cb9f65f9bb7b22d0a727fee1c28253357b35e468e034daff | arXiv:2603.08960v1 HTML — §4 Evaluation Methodology [facet=evaluation]; https://arxiv.org/html/2603.08960v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08960v1.html; sha256:2e01227172a0a7c9cb9f65f9bb7b22d0a727fee1c28253357b35e468e034daff | arXiv:2603.08960v1 HTML — §7 Discussion [facet=limitations]; https://arxiv.org/html/2603.08960v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08960v1.html; sha256:2e01227172a0a7c9cb9f65f9bb7b22d0a727fee1c28253357b35e468e034daff | arXiv exact-v1 identity https://arxiv.org/abs/2603.08960v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08960 | complete |
| SF-2026-ARXIV-2603-09023 | RP-693110cfc0ae11a9 | deep | arXiv:2603.09023v1 | SRC-ARXIV@arXiv:2603.09023v1 | arXiv:2603.09023v1 HTML — §3. System Design [facet=method]; https://arxiv.org/html/2603.09023v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09023v1.html; sha256:bf2faa52a0ea9f55cb0ba33ed5db70bcec152a84a7e465e845c07a1f252b1108 | arXiv:2603.09023v1 HTML — §5. Results [facet=evaluation]; https://arxiv.org/html/2603.09023v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09023v1.html; sha256:bf2faa52a0ea9f55cb0ba33ed5db70bcec152a84a7e465e845c07a1f252b1108 | arXiv:2603.09023v1 HTML — §Failure modes. [facet=limitations]; https://arxiv.org/html/2603.09023v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09023v1.html; sha256:bf2faa52a0ea9f55cb0ba33ed5db70bcec152a84a7e465e845c07a1f252b1108 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09023v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09023 | complete |
| SF-2026-ARXIV-2603-09046 | RP-d7a7786368e8e50b | standard | arXiv:2603.09046v1 | SRC-ARXIV@arXiv:2603.09046v1 | arXiv:2603.09046v1 HTML — §3.3 System Overview [facet=method]; https://arxiv.org/html/2603.09046v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09046v1.html; sha256:9e0fe8f7548e5dc8422a39df86d22776a24d5b575206df8fc8753163bd963d5d | arXiv:2603.09046v1 HTML — §7.2 Micro-benchmarks [facet=evaluation]; https://arxiv.org/html/2603.09046v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09046v1.html; sha256:9e0fe8f7548e5dc8422a39df86d22776a24d5b575206df8fc8753163bd963d5d | arXiv:2603.09046v1 HTML — §2.2 ARM TrustZone and Its Limitations [facet=limitations]; https://arxiv.org/html/2603.09046v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09046v1.html; sha256:9e0fe8f7548e5dc8422a39df86d22776a24d5b575206df8fc8753163bd963d5d | arXiv exact-v1 identity https://arxiv.org/abs/2603.09046v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09046 | complete |
| SF-2026-ARXIV-2603-09079 | RP-f185d49cb37bf472 | standard | arXiv:2603.09079v1 | SRC-ARXIV@arXiv:2603.09079v1 | arXiv:2603.09079v1 HTML — §III Method [facet=method]; https://arxiv.org/html/2603.09079v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09079v1.html; sha256:64f190b0c5da03d9fdaeee46f3f65b3fe55db4a71ed03eb041e36f0392bc196c | arXiv:2603.09079v1 HTML — §IV-B Main Results [facet=evaluation]; https://arxiv.org/html/2603.09079v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09079v1.html; sha256:64f190b0c5da03d9fdaeee46f3f65b3fe55db4a71ed03eb041e36f0392bc196c | arXiv:2603.09079v1 HTML — §IV-D4 Failure Cases [facet=limitations]; https://arxiv.org/html/2603.09079v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09079v1.html; sha256:64f190b0c5da03d9fdaeee46f3f65b3fe55db4a71ed03eb041e36f0392bc196c | arXiv exact-v1 identity https://arxiv.org/abs/2603.09079v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09079 | complete |
| SF-2026-ARXIV-2603-09086 | RP-d467a8b1c38e7445 | standard | arXiv:2603.09086v1 | SRC-ARXIV@arXiv:2603.09086v1 | arXiv:2603.09086v1 HTML — §III INTERNAL MECHANICS: STRUCTURE, ALIGNMENT, AND DYNAMICS IN LATENT REPRESENTATIONS [facet=method]; https://arxiv.org/html/2603.09086v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09086v1.html; sha256:0f1858abac1678fb3a2899b6610377a4d2ee83a0c4baee0f914f4a1f216a9847 | arXiv:2603.09086v1 HTML — §IV-C Toward Unified Latent-Centric Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.09086v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09086v1.html; sha256:0f1858abac1678fb3a2899b6610377a4d2ee83a0c4baee0f914f4a1f216a9847 | arXiv:2603.09086v1 HTML — §VII Conclusion [facet=limitations]; https://arxiv.org/html/2603.09086v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09086v1.html; sha256:0f1858abac1678fb3a2899b6610377a4d2ee83a0c4baee0f914f4a1f216a9847 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09086v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09086 | complete |
| SF-2026-ARXIV-2603-09117 | RP-cdfaf0a3f83ae545 | standard | arXiv:2603.09117v1 | SRC-ARXIV@arXiv:2603.09117v1 | arXiv:2603.09117v1 HTML — §2.4 Calibration Optimization Methods [facet=method]; https://arxiv.org/html/2603.09117v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09117v1.html; sha256:2c79d6d9059fef7cb1703b8a78cd1089629461b286580776d3d74d89af8c1aa2 | arXiv:2603.09117v1 HTML — §6.2 Overall Results [facet=evaluation]; https://arxiv.org/html/2603.09117v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09117v1.html; sha256:2c79d6d9059fef7cb1703b8a78cd1089629461b286580776d3d74d89af8c1aa2 | arXiv:2603.09117v1 HTML — §6.3 Ablation Studies [facet=limitations]; https://arxiv.org/html/2603.09117v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09117v1.html; sha256:2c79d6d9059fef7cb1703b8a78cd1089629461b286580776d3d74d89af8c1aa2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09117v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09117 | complete |
| SF-2026-ARXIV-2603-09121 | RP-12428041e4bef60d | standard | arXiv:2603.09121v1 | SRC-ARXIV@arXiv:2603.09121v1 | arXiv:2603.09121v1 HTML — §III Method [facet=method]; https://arxiv.org/html/2603.09121v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09121v1.html; sha256:7c18247742d5c845661afbe93f57dccac9d75d28a7f9a1d3792a24a26121321e | arXiv:2603.09121v1 HTML — §IV EXPERIMENTS [facet=evaluation]; https://arxiv.org/html/2603.09121v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09121v1.html; sha256:7c18247742d5c845661afbe93f57dccac9d75d28a7f9a1d3792a24a26121321e | arXiv:2603.09121v1 HTML — §V CONCLUSION AND FUTURE WORK [facet=limitations]; https://arxiv.org/html/2603.09121v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09121v1.html; sha256:7c18247742d5c845661afbe93f57dccac9d75d28a7f9a1d3792a24a26121321e | arXiv exact-v1 identity https://arxiv.org/abs/2603.09121v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09121 | complete |
| SF-2026-ARXIV-2603-09127 | RP-417bba1eef9b90db | standard | arXiv:2603.09127v1 | SRC-ARXIV@arXiv:2603.09127v1 | arXiv:2603.09127v1 HTML — §Two design routes and non-additive interaction [facet=method]; https://arxiv.org/html/2603.09127v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09127v1.html; sha256:050f8e7858cf52585e6af357adcc685340ef9b6b1f08ccea3fdbe986f9cd5f06 | arXiv:2603.09127v1 HTML — §S4.3 Results [facet=evaluation]; https://arxiv.org/html/2603.09127v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09127v1.html; sha256:050f8e7858cf52585e6af357adcc685340ef9b6b1f08ccea3fdbe986f9cd5f06 | arXiv:2603.09127v1 HTML — §Discussion [facet=limitations]; https://arxiv.org/html/2603.09127v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09127v1.html; sha256:050f8e7858cf52585e6af357adcc685340ef9b6b1f08ccea3fdbe986f9cd5f06 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09127v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09127 | complete |
| SF-2026-ARXIV-2603-09157 | RP-7fe8cbf97a631123 | standard | arXiv:2603.09157v1 | SRC-ARXIV@arXiv:2603.09157v1 | arXiv:2603.09157v1 HTML — §Dual-Mode Architecture [facet=method]; https://arxiv.org/html/2603.09157v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09157v1.html; sha256:1a3035f6e0bd9c407b9b32ae0250889cd58f176e9421ed1a4cb1a4ca14bb980f | arXiv:2603.09157v1 HTML — §Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09157v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09157v1.html; sha256:1a3035f6e0bd9c407b9b32ae0250889cd58f176e9421ed1a4cb1a4ca14bb980f | arXiv:2603.09157v1 HTML — §Component Ablation [facet=limitations]; https://arxiv.org/html/2603.09157v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09157v1.html; sha256:1a3035f6e0bd9c407b9b32ae0250889cd58f176e9421ed1a4cb1a4ca14bb980f | arXiv exact-v1 identity https://arxiv.org/abs/2603.09157v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09157 | complete |
| SF-2026-ARXIV-2603-09180 | RP-fe7136a06e9772ab | standard | arXiv:2603.09180v1 | SRC-ARXIV@arXiv:2603.09180v1 | arXiv:2603.09180v1 HTML — §4.1 Implementation Details [facet=method]; https://arxiv.org/html/2603.09180v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09180v1.html; sha256:490943e4c62866a5811e1847f6c5e3578f4698188c992c5883c80b4cbb1d914c | arXiv:2603.09180v1 HTML — §4.2 Full-Duplex-Bench Results [facet=evaluation]; https://arxiv.org/html/2603.09180v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09180v1.html; sha256:490943e4c62866a5811e1847f6c5e3578f4698188c992c5883c80b4cbb1d914c | arXiv:2603.09180v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.09180v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09180v1.html; sha256:490943e4c62866a5811e1847f6c5e3578f4698188c992c5883c80b4cbb1d914c | arXiv exact-v1 identity https://arxiv.org/abs/2603.09180v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09180 | complete |
| SF-2026-ARXIV-2603-09192 | RP-a2ce8f462a230cb3 | standard | arXiv:2603.09192v1 | SRC-ARXIV@arXiv:2603.09192v1 | arXiv:2603.09192v1 HTML — §3 Methods [facet=method]; https://arxiv.org/html/2603.09192v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09192v1.html; sha256:da5469c40df336edc3d41066dfced935f213a36d82aa267a704de28d8a3d5615 | arXiv:2603.09192v1 HTML — §2.2 Retrieval Strategy, Reflection, and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09192v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09192v1.html; sha256:da5469c40df336edc3d41066dfced935f213a36d82aa267a704de28d8a3d5615 | arXiv:2603.09192v1 HTML — §4.5 Discussion [facet=limitations]; https://arxiv.org/html/2603.09192v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09192v1.html; sha256:da5469c40df336edc3d41066dfced935f213a36d82aa267a704de28d8a3d5615 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09192v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09192 | complete |
| SF-2026-ARXIV-2603-09216 | RP-35ef2bbf7f486b75 | standard | arXiv:2603.09216v1 | SRC-ARXIV@arXiv:2603.09216v1 | arXiv:2603.09216v1 HTML — §2.2 LPDDR-PIM architecture [facet=method]; https://arxiv.org/html/2603.09216v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09216v1.html; sha256:d4cc0ce8b948bf0c5144813351b92dfe1e1250e550102a3100358ca5d977e704 | arXiv:2603.09216v1 HTML — §6 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09216v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09216v1.html; sha256:d4cc0ce8b948bf0c5144813351b92dfe1e1250e550102a3100358ca5d977e704 | arXiv:2603.09216v1 HTML — §3.2 Current solutions and limitations [facet=limitations]; https://arxiv.org/html/2603.09216v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09216v1.html; sha256:d4cc0ce8b948bf0c5144813351b92dfe1e1250e550102a3100358ca5d977e704 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09216v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09216 | complete |
| SF-2026-ARXIV-2603-09221 | RP-003bf9e863e23382 | standard | arXiv:2603.09221v1 | SRC-ARXIV@arXiv:2603.09221v1 | arXiv:2603.09221v1 HTML — §3.3 Hardware Co-Design for TTC [facet=method]; https://arxiv.org/html/2603.09221v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09221v1.html; sha256:02893c0e8660b6453ebbf0092e3eab7c1329e7cd456c14906da992c56d228396 | arXiv:2603.09221v1 HTML — §Benchmark Evaluation. [facet=evaluation]; https://arxiv.org/html/2603.09221v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09221v1.html; sha256:02893c0e8660b6453ebbf0092e3eab7c1329e7cd456c14906da992c56d228396 | arXiv:2603.09221v1 HTML — §Limitations and Future Works. [facet=limitations]; https://arxiv.org/html/2603.09221v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09221v1.html; sha256:02893c0e8660b6453ebbf0092e3eab7c1329e7cd456c14906da992c56d228396 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09221v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09221 | complete |
| SF-2026-ARXIV-2603-09241 | RP-9bbdae60a6965fd0 | standard | arXiv:2603.09241v1 | SRC-ARXIV@arXiv:2603.09241v1 | arXiv:2603.09241v1 HTML — §Representation Space and Architecture. [facet=method]; https://arxiv.org/html/2603.09241v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09241v1.html; sha256:9d647271225c76da7b184922d943442502a0dabd60651d6fec2d27e0a82776b7 | arXiv:2603.09241v1 HTML — §Evaluation Metrics. [facet=evaluation]; https://arxiv.org/html/2603.09241v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09241v1.html; sha256:9d647271225c76da7b184922d943442502a0dabd60651d6fec2d27e0a82776b7 | arXiv:2603.09241v1 HTML — §6 Discussion and Limitations [facet=limitations]; https://arxiv.org/html/2603.09241v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09241v1.html; sha256:9d647271225c76da7b184922d943442502a0dabd60651d6fec2d27e0a82776b7 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09241v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09241 | complete |
| SF-2026-ARXIV-2603-09290 | RP-c29d23704e667c2d | standard | arXiv:2603.09290v1 | SRC-ARXIV@arXiv:2603.09290v1 | arXiv:2603.09290v1 HTML — §4 Methods [facet=method]; https://arxiv.org/html/2603.09290v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09290v1.html; sha256:769f80ae80888a4c1de4143cc9e2cfd33b3fa159defd9b5f0b3d711936028a20 | arXiv:2603.09290v1 HTML — §2.4.1 Case 1: Stroke Analysis [facet=evaluation]; https://arxiv.org/html/2603.09290v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09290v1.html; sha256:769f80ae80888a4c1de4143cc9e2cfd33b3fa159defd9b5f0b3d711936028a20 | arXiv:2603.09290v1 HTML — §3.1 Contributions and limitations [facet=limitations]; https://arxiv.org/html/2603.09290v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09290v1.html; sha256:769f80ae80888a4c1de4143cc9e2cfd33b3fa159defd9b5f0b3d711936028a20 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09290v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09290 | complete |
| SF-2026-ARXIV-2603-09297 | RP-85da452005ace3d2 | standard | arXiv:2603.09297v1 | SRC-ARXIV@arXiv:2603.09297v1 | arXiv:2603.09297v1 PDF — §III. METHODOLOGY [facet=method]; https://arxiv.org/pdf/2603.09297v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09297v1.pdf.txt; sha256:e4966991942a9f9c6eb3bf507bc92599d581b98f6c02a9377890dc37c3ece52f | Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/pdf/2603.09297v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09297v1.pdf.txt; sha256:e4966991942a9f9c6eb3bf507bc92599d581b98f6c02a9377890dc37c3ece52f | Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Limitations 章节 [facet=limitations]; https://arxiv.org/pdf/2603.09297v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09297v1.pdf.txt; sha256:e4966991942a9f9c6eb3bf507bc92599d581b98f6c02a9377890dc37c3ece52f | arXiv exact-v1 identity https://arxiv.org/abs/2603.09297v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09297 | complete |
| SF-2026-ARXIV-2603-09435 | RP-4556ad0605d962ea | standard | arXiv:2603.09435v1 | SRC-ARXIV@arXiv:2603.09435v1 | arXiv:2603.09435v1 HTML — §3.2 Methodology [facet=method]; https://arxiv.org/html/2603.09435v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09435v1.html; sha256:17eba511d989a51ce666ea4352e5871a0e142e0d0f8eab5ab30b0c2e31e30d69 | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.09435v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09435v1.html; sha256:17eba511d989a51ce666ea4352e5871a0e142e0d0f8eab5ab30b0c2e31e30d69 | arXiv:2603.09435v1 HTML — §6 Conclusions & Future Work [facet=limitations]; https://arxiv.org/html/2603.09435v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09435v1.html; sha256:17eba511d989a51ce666ea4352e5871a0e142e0d0f8eab5ab30b0c2e31e30d69 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09435v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09435 | complete |
| SF-2026-ARXIV-2603-09453 | RP-5d1138fe47f94013 | standard | arXiv:2603.09453v1 | SRC-ARXIV@arXiv:2603.09453v1 | arXiv:2603.09453v1 HTML — §Methodology [facet=method]; https://arxiv.org/html/2603.09453v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09453v1.html; sha256:5f4894957e4ee987cba696a312a697726ec3228699e8195c2c249e3fc338ae35 | arXiv:2603.09453v1 HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.09453v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09453v1.html; sha256:5f4894957e4ee987cba696a312a697726ec3228699e8195c2c249e3fc338ae35 | arXiv:2603.09453v1 HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.09453v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09453v1.html; sha256:5f4894957e4ee987cba696a312a697726ec3228699e8195c2c249e3fc338ae35 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09453v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09453 | complete |
| SF-2026-ARXIV-2603-09488 | RP-1361f407fcddabb2 | standard | arXiv:2603.09488v1 | SRC-ARXIV@arXiv:2603.09488v1 | arXiv:2603.09488v1 HTML — §H.2 Evaluation Methodology [facet=method]; https://arxiv.org/html/2603.09488v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09488v1.html; sha256:3c8856edacae2b87fe3e2bb33b6e6131c64e311bd6471b06c61f09cfb91086ca | arXiv:2603.09488v1 HTML — §4.4 Long Video Generation Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09488v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09488v1.html; sha256:3c8856edacae2b87fe3e2bb33b6e6131c64e311bd6471b06c61f09cfb91086ca | arXiv:2603.09488v1 HTML — §4.3 Ablation Studies [facet=limitations]; https://arxiv.org/html/2603.09488v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09488v1.html; sha256:3c8856edacae2b87fe3e2bb33b6e6131c64e311bd6471b06c61f09cfb91086ca | arXiv exact-v1 identity https://arxiv.org/abs/2603.09488v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09488 | complete |
| SF-2026-ARXIV-2603-09513 | RP-6966124a3d710eb3 | standard | arXiv:2603.09513v1 | SRC-ARXIV@arXiv:2603.09513v1 | arXiv:2603.09513v1 HTML — §LLM-Aided Lock Design [facet=method]; https://arxiv.org/html/2603.09513v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09513v1.html; sha256:cb86d71edfeacee89a7a675644b40b1fcace4bee4c12b260ac91ec7e7ab7ff7d | arXiv:2603.09513v1 HTML — §Main Results [facet=evaluation]; https://arxiv.org/html/2603.09513v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09513v1.html; sha256:cb86d71edfeacee89a7a675644b40b1fcace4bee4c12b260ac91ec7e7ab7ff7d | arXiv:2603.09513v1 HTML — §Possible Causes of Remaining Failures [facet=limitations]; https://arxiv.org/html/2603.09513v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09513v1.html; sha256:cb86d71edfeacee89a7a675644b40b1fcace4bee4c12b260ac91ec7e7ab7ff7d | arXiv exact-v1 identity https://arxiv.org/abs/2603.09513v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09513 | complete |
| SF-2026-ARXIV-2603-09555 | RP-feb715085ac6e5c0 | deep | arXiv:2603.09555v1 | SRC-ARXIV@arXiv:2603.09555v1 | arXiv:2603.09555v1 HTML — §3 Why SSD Is Compiler-Friendly [facet=method]; https://arxiv.org/html/2603.09555v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09555v1.html; sha256:f3e5e676e8285e2d659a16f16dee2f29d21c677b0ef275bb82be4e8184dd8809 | arXiv:2603.09555v1 HTML — §5.2–§5.7 numerical and performance validation [facet=evaluation]; https://arxiv.org/html/2603.09555v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09555v1.html; sha256:f3e5e676e8285e2d659a16f16dee2f29d21c677b0ef275bb82be4e8184dd8809 | arXiv:2603.09555v1 HTML — §5.8 Limitations [facet=limitations]; https://arxiv.org/html/2603.09555v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09555v1.html; sha256:f3e5e676e8285e2d659a16f16dee2f29d21c677b0ef275bb82be4e8184dd8809 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09555v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09555 | complete |
| SF-2026-ARXIV-2603-09619 | RP-15417b295d2245c1 | standard | arXiv:2603.09619v1 | SRC-ARXIV@arXiv:2603.09619v1 | arXiv:2603.09619v1 PDF — §6. Context Engineering as a Design Object [facet=method]; https://arxiv.org/pdf/2603.09619v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09619v1.pdf.txt; sha256:6912d5467e52b0e417610130e6dbd88e23cb0cff679f670f6b4e8c00d7de80e3 | Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/pdf/2603.09619v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09619v1.pdf.txt; sha256:6912d5467e52b0e417610130e6dbd88e23cb0cff679f670f6b4e8c00d7de80e3 | Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Limitations 章节 [facet=limitations]; https://arxiv.org/pdf/2603.09619v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09619v1.pdf.txt; sha256:6912d5467e52b0e417610130e6dbd88e23cb0cff679f670f6b4e8c00d7de80e3 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09619v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09619 | complete |
| SF-2026-ARXIV-2603-09657 | RP-1d34b9b5d334f635 | standard | arXiv:2603.09657v1 | SRC-ARXIV@arXiv:2603.09657v1 | arXiv:2603.09657v1 HTML — §B.1 Implementation Details [facet=method]; https://arxiv.org/html/2603.09657v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09657v1.html; sha256:ea6902dc8b1e595fe29f0338fcd8cec4db2d9c9b76a6b593f23e2ec8297b5824 | arXiv:2603.09657v1 HTML — §5.2 Results [facet=evaluation]; https://arxiv.org/html/2603.09657v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09657v1.html; sha256:ea6902dc8b1e595fe29f0338fcd8cec4db2d9c9b76a6b593f23e2ec8297b5824 | arXiv:2603.09657v1 HTML — §6 Conclusions [facet=limitations]; https://arxiv.org/html/2603.09657v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09657v1.html; sha256:ea6902dc8b1e595fe29f0338fcd8cec4db2d9c9b76a6b593f23e2ec8297b5824 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09657v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09657 | complete |
| SF-2026-ARXIV-2603-09692 | RP-edf6d1d723556e80 | standard | arXiv:2603.09692v1 | SRC-ARXIV@arXiv:2603.09692v1 | arXiv:2603.09692v1 HTML — §D.1 Scoring Methodology [facet=method]; https://arxiv.org/html/2603.09692v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09692v1.html; sha256:011516aad5bc77d0b4418cce9db2e36bf960e7a2cb2b681623a521f44aafbd0b | arXiv:2603.09692v1 HTML — §5 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09692v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09692v1.html; sha256:011516aad5bc77d0b4418cce9db2e36bf960e7a2cb2b681623a521f44aafbd0b | arXiv:2603.09692v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.09692v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09692v1.html; sha256:011516aad5bc77d0b4418cce9db2e36bf960e7a2cb2b681623a521f44aafbd0b | arXiv exact-v1 identity https://arxiv.org/abs/2603.09692v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09692 | complete |
| SF-2026-ARXIV-2603-09716 | RP-6e58f0dfcc94f834 | standard | arXiv:2603.09716v1 | SRC-ARXIV@arXiv:2603.09716v1 | arXiv:2603.09716v1 HTML — §3 The AutoAgent Framework: A Unified Architecture for Self-Evolution [facet=method]; https://arxiv.org/html/2603.09716v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09716v1.html; sha256:002a269298acdff7133209810976fcd4f92c4db78abf1c5adad5b7cc49a1151c | arXiv:2603.09716v1 HTML — §8 Experiments and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09716v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09716v1.html; sha256:002a269298acdff7133209810976fcd4f92c4db78abf1c5adad5b7cc49a1151c | arXiv:2603.09716v1 HTML — §9 Conclusion and Future Work [facet=limitations]; https://arxiv.org/html/2603.09716v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09716v1.html; sha256:002a269298acdff7133209810976fcd4f92c4db78abf1c5adad5b7cc49a1151c | arXiv exact-v1 identity https://arxiv.org/abs/2603.09716v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09716 | complete |
| SF-2026-ARXIV-2603-09730 | RP-74d2c8c1f01bf29e | standard | arXiv:2603.09730v1 | SRC-ARXIV@arXiv:2603.09730v1 | arXiv:2603.09730v1 HTML — §IV-B Design Rationale: Why Pluggability? [facet=method]; https://arxiv.org/html/2603.09730v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09730v1.html; sha256:f8e48fcf33cf2f2baf583a1ac87543f8916bf3a1d3db5c368c904d37552251f3 | arXiv:2603.09730v1 HTML — §V-D Physical Cluster Validation [facet=evaluation]; https://arxiv.org/html/2603.09730v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09730v1.html; sha256:f8e48fcf33cf2f2baf583a1ac87543f8916bf3a1d3db5c368c904d37552251f3 | arXiv:2603.09730v1 HTML — §VII Future Work [facet=limitations]; https://arxiv.org/html/2603.09730v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09730v1.html; sha256:f8e48fcf33cf2f2baf583a1ac87543f8916bf3a1d3db5c368c904d37552251f3 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09730v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09730 | complete |
| SF-2026-ARXIV-2603-09756 | RP-dd79340558dedbc5 | standard | arXiv:2603.09756v1 | SRC-ARXIV@arXiv:2603.09756v1 | arXiv:2603.09756v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2603.09756v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09756v1.html; sha256:e2254df70cad22526b2013d0b4bef09232470c36b1b9141f6b93b1bdd3090d2b | arXiv:2603.09756v1 HTML — §2 Results [facet=evaluation]; https://arxiv.org/html/2603.09756v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09756v1.html; sha256:e2254df70cad22526b2013d0b4bef09232470c36b1b9141f6b93b1bdd3090d2b | arXiv:2603.09756v1 HTML — §3 Discussion [facet=limitations]; https://arxiv.org/html/2603.09756v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09756v1.html; sha256:e2254df70cad22526b2013d0b4bef09232470c36b1b9141f6b93b1bdd3090d2b | arXiv exact-v1 identity https://arxiv.org/abs/2603.09756v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09756 | complete |
| SF-2026-ARXIV-2603-09821 | RP-544f9baa8f1c0785 | standard | arXiv:2603.09821v1 | SRC-ARXIV@arXiv:2603.09821v1 | arXiv:2603.09821v1 HTML — §3.1 Framework Overview [facet=method]; https://arxiv.org/html/2603.09821v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09821v1.html; sha256:284da23888be1cd2370a3965ac83ce3e85e40efa30d4db4eb2e9690dc3cb900e | arXiv:2603.09821v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.09821v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09821v1.html; sha256:284da23888be1cd2370a3965ac83ce3e85e40efa30d4db4eb2e9690dc3cb900e | arXiv:2603.09821v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.09821v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09821v1.html; sha256:284da23888be1cd2370a3965ac83ce3e85e40efa30d4db4eb2e9690dc3cb900e | arXiv exact-v1 identity https://arxiv.org/abs/2603.09821v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09821 | complete |
| SF-2026-ARXIV-2603-09877 | RP-1d7488ab10185cad | standard | arXiv:2603.09877v1 | SRC-ARXIV@arXiv:2603.09877v1 | arXiv:2603.09877v1 HTML — §3.1.1 Overall Design Principles [facet=method]; https://arxiv.org/html/2603.09877v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09877v1.html; sha256:d0ed98d6b58e6de71d01bc2b75a4dc7bfd2c2dde14bae07e8fd6a1b2824e89ce | arXiv:2603.09877v1 HTML — §A.2.2 Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.09877v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09877v1.html; sha256:d0ed98d6b58e6de71d01bc2b75a4dc7bfd2c2dde14bae07e8fd6a1b2824e89ce | arXiv:2603.09877v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.09877v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09877v1.html; sha256:d0ed98d6b58e6de71d01bc2b75a4dc7bfd2c2dde14bae07e8fd6a1b2824e89ce | arXiv exact-v1 identity https://arxiv.org/abs/2603.09877v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09877 | complete |
| SF-2026-ARXIV-2603-09891 | RP-45662bd107eaf6b5 | standard | arXiv:2603.09891v1 | SRC-ARXIV@arXiv:2603.09891v1 | arXiv:2603.09891v1 HTML — §2 Task Setup [facet=method]; https://arxiv.org/html/2603.09891v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09891v1.html; sha256:0803e041f5c0cbeb4cd2f3f9b386a8f1e674411e82921a587b4121d95e74a200 | arXiv:2603.09891v1 HTML — §3.3 Support Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09891v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09891v1.html; sha256:0803e041f5c0cbeb4cd2f3f9b386a8f1e674411e82921a587b4121d95e74a200 | arXiv:2603.09891v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.09891v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09891v1.html; sha256:0803e041f5c0cbeb4cd2f3f9b386a8f1e674411e82921a587b4121d95e74a200 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09891v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09891 | complete |
| SF-2026-ARXIV-2603-09892 | RP-9c9a373c80b480f2 | standard | arXiv:2603.09892v1 | SRC-ARXIV@arXiv:2603.09892v1 | arXiv:2603.09892v1 HTML — §Framework Overview. [facet=method]; https://arxiv.org/html/2603.09892v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09892v1.html; sha256:8d975eb1955578b3bd957d6b5bd736531b7cebfcdac2fc554cae7967b91fced1 | arXiv:2603.09892v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.09892v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09892v1.html; sha256:8d975eb1955578b3bd957d6b5bd736531b7cebfcdac2fc554cae7967b91fced1 | arXiv:2603.09892v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.09892v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09892v1.html; sha256:8d975eb1955578b3bd957d6b5bd736531b7cebfcdac2fc554cae7967b91fced1 | arXiv exact-v1 identity https://arxiv.org/abs/2603.09892v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09892 | complete |

### Source Reviews

### ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs

<!-- review:SF-2026-ARXIV-2603-08727:start -->
**问题**：长上下文 KV 在有限 HBM 中若按单一规则淘汰，会在容量、精度和请求并发间产生不可控尾延迟。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：ARKV 以请求/层级重要性和实时预算共同决定压缩、保留与迁移，把资源约束纳入 KV lifecycle。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.08727v1 HTML — §IV Methodology [facet=method]; https://arxiv.org/html/2603.08727v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08727v1.html; sha256:a1c8fb742c0fc5431b0004efd00e59b3fad35a6ca90f1da583ce9cd7d1e3b6b6`。

**Evaluation contract 与未证明部分**：结果绑定论文的模型、长度、预算与 workload；未披露条件不能用于生产容量承诺。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08727v1 HTML — §V-D Evaluation Metrics and Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.08727v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08727v1.html; sha256:a1c8fb742c0fc5431b0004efd00e59b3fad35a6ca90f1da583ce9cd7d1e3b6b6`。

**Trade-off / failure / coexistence**：自适应策略增加 metadata 和误判面；短上下文或 HBM 充足时完整 KV 更可预测。

<!-- claim:SF-2026-ARXIV-2603-08727:start -->**Claim Boundary**：只支持 arXiv:2603.08727v1 §IV Methodology 的机制与 §V-D Evaluation Metrics and Benchmarks 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08727:end -->
<!-- review:SF-2026-ARXIV-2603-08727:end -->
### Adaptive Multi-Objective Tiered Storage Configuration for KV Cache in LLM Service

<!-- review:SF-2026-ARXIV-2603-08739:start -->
**问题**：KV offload 有多个容量/延迟/成本目标，固定 tier 比例无法适应访问模式与资源价格变化。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：该系统搜索 Pareto 配置，并依据 KV block access 在线调节分层缓存 eviction 与容量。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.08739v1 HTML — §4.1. Overview [facet=method]; https://arxiv.org/html/2603.08739v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08739v1.html; sha256:023c3d0a54ac2412cd6dc20eeebb3a1fcd53d0ca84f4ab8a8e3b17cdd46d7377`。

**Evaluation contract 与未证明部分**：真实 trace 只支持所测存储层级中的条件收益；不证明控制器面对突发漂移仍稳定。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08739v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.08739v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08739v1.html; sha256:023c3d0a54ac2412cd6dc20eeebb3a1fcd53d0ca84f4ab8a8e3b17cdd46d7377`。

**Trade-off / failure / coexistence**：在线调优有探索损失和控制抖动；稳定 workload 仍可冻结已验证配置。

<!-- claim:SF-2026-ARXIV-2603-08739:start -->**Claim Boundary**：只支持 arXiv:2603.08739v1 §4.1. Overview 的机制与 §5. Evaluation 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08739:end -->
<!-- review:SF-2026-ARXIV-2603-08739:end -->
### Zipage: Maintain High Request Concurrency for LLM Reasoning through Compressed PagedAttention

<!-- review:SF-2026-ARXIV-2603-08743:start -->
**问题**：`Zipage: Maintain High Request Concurrency for LLM Reasoning through Compressed PagedAttention` 检查的是 `INFER-KV-CACHE` 中 长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。 是否会改变现有设计边界。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：exact-v1 的 `4 Method` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.08743v1 HTML — §4 Method [facet=method]; https://arxiv.org/html/2603.08743v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08743v1.html; sha256:60ef65bb98b771ac8cb264ec20251f1e6b7c1e98d896caf45593c511d47c8256`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Appendix D Additional Information of Ablation Experiments`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08743v1 HTML — §Appendix D Additional Information of Ablation Experiments [facet=evaluation]; https://arxiv.org/html/2603.08743v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08743v1.html; sha256:60ef65bb98b771ac8cb264ec20251f1e6b7c1e98d896caf45593c511d47c8256`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2603-08743:start -->**Claim Boundary**：只支持 arXiv:2603.08743v1 §4 Method 的机制与 §Appendix D Additional Information of Ablation Experiments 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08743:end -->
<!-- review:SF-2026-ARXIV-2603-08743:end -->
### Diagnosing FP4 inference: a layer-wise and block-wise sensitivity analysis of NVFP4 and MXFP4

<!-- review:SF-2026-ARXIV-2603-08747:start -->
**问题**：`Diagnosing FP4 inference: a layer-wise and block-wise sensitivity analysis of NVFP4 and MXFP4` 检查的是 `INFER-TENSORRT-LLM` 中 固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。 是否会改变现有设计边界。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：exact-v1 的 `3 Experimental Design` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.08747v1 HTML — §3 Experimental Design [facet=method]; https://arxiv.org/html/2603.08747v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08747v1.html; sha256:8f14c85dedf6e5d6b759839d0c15b22bcb4ec0b7c03ca86b7244781b2be49185`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4 Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08747v1 HTML — §4 Results [facet=evaluation]; https://arxiv.org/html/2603.08747v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08747v1.html; sha256:8f14c85dedf6e5d6b759839d0c15b22bcb4ec0b7c03ca86b7244781b2be49185`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion and Discussion`。模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。

<!-- claim:SF-2026-ARXIV-2603-08747:start -->**Claim Boundary**：只支持 arXiv:2603.08747v1 §3 Experimental Design 的机制与 §4 Results 的公开 workload；§5 Conclusion and Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08747:end -->
<!-- review:SF-2026-ARXIV-2603-08747:end -->
### Turn: A Language for Agentic Computation

<!-- review:SF-2026-ARXIV-2603-08755:start -->
**问题**：agent framework 把 bounded context、typed output、credential isolation 与 durable state 留给应用约定，编译期无法检查。

**旧路径为何合理**：应用代码直接持有 context、credential 和 workflow state，在小规模时路径最短。

**约束变化与机制**：Turn 把 LLM inference、actor mailbox、capability handle 与 schema absorption 提升为语言/VM 原语。

**State / data / control owner**：`AGENT-PLATFORM` 负责 agent definition、run identity、capability handle、mailbox 与持久状态；定位证据为 `arXiv:2603.08755v1 HTML — §2.1 Agent Frameworks [facet=method]; https://arxiv.org/html/2603.08755v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08755v1.html; sha256:07a14e3d28507e1f112da57c9a312decac152aa2a41efc4c7542c99e4d96d6ef`。

**Evaluation contract 与未证明部分**：开源 VM 与工作负载证明这些 invariant 可被执行；不证明新语言优于成熟 runtime 的生态和性能。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08755v1 HTML — §10 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.08755v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08755v1.html; sha256:07a14e3d28507e1f112da57c9a312decac152aa2a41efc4c7542c99e4d96d6ef`。

**Trade-off / failure / coexistence**：语言级保证减少应用漂移，却引入编译器、VM 与 FFI 信任根；简单 agent 仍可用通用语言加严格库。

<!-- claim:SF-2026-ARXIV-2603-08755:start -->**Claim Boundary**：只支持 arXiv:2603.08755v1 §2.1 Agent Frameworks 的机制与 §10 Evaluation 的公开 workload；§11.1 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08755:end -->
<!-- review:SF-2026-ARXIV-2603-08755:end -->
### No Certificate for Alignment: Two Independent Impossibilities and the Pareto Frontier of Achievable Safety Guarantees

<!-- review:SF-2026-ARXIV-2603-08761:start -->
**问题**：`No Certificate for Alignment: Two Independent Impossibilities and the Pareto Frontier of Achievable Safety Guarantees` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `3 Formal Framework` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.08761v1 HTML — §3 Formal Framework [facet=method]; https://arxiv.org/html/2603.08761v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08761v1.html; sha256:37ef1a43f18cddf638668fc6f94378fcc4568d3ce89146c2f4b19fdcf3798316`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.08761v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08761v1.html; sha256:37ef1a43f18cddf638668fc6f94378fcc4568d3ce89146c2f4b19fdcf3798316`。

**Trade-off / failure / coexistence**：限制与反证定位在 `8 Discussion`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-08761:start -->**Claim Boundary**：只支持 arXiv:2603.08761v1 §3 Formal Framework 的机制与 §Evaluation 的公开 workload；§8 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08761:end -->
<!-- review:SF-2026-ARXIV-2603-08761:end -->
### Serving Compound Inference Systems on Datacenter GPUs

<!-- review:SF-2026-ARXIV-2603-08797:start -->
**问题**：compound inference 的 latency、accuracy 与 GPU cost 跨 task/model variant 耦合，逐模型独立配置无法满足端到端 SLO。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：JigsawServe 注册 task graph、model variants 与 SLO，profile variant×batch×MIG/MPS segment，再由 MILP controller 选择 variants、replicas 与 spatial partitions；frontend/workers 在该配置内路由执行。

**State / data / control owner**：`INFER-SCHEDULING` 负责配置与重配置；registration、profiler、MILP controller 和 frontend/workers 的分工定位于 exact-v1 §3.1–§3.3。

**Evaluation contract 与未证明部分**：§4–§5 的数据中心 GPU 实验验证所测 compound workloads；未证明 runtime dependency frontier、中间 artifact residency、任意动态 Agent graph 或多租户策略。

**Trade-off / failure / coexistence**：依赖感知提高关键路径利用率，但要求精确 stage profile 与中间状态追踪；单模型独立请求仍可使用较简单的 continuous batching。

<!-- claim:SF-2026-ARXIV-2603-08797:start -->**Claim Boundary**：只支持 arXiv:2603.08797v1 §3.1–§3.3 的 graph/variant/profile/MILP configuration 与 §4–§5 的公开 workload，不支持运行时 DAG residency 语义。<!-- claim:SF-2026-ARXIV-2603-08797:end -->
<!-- review:SF-2026-ARXIV-2603-08797:end -->
### Test-Driven AI Agent Definition (TDAD): Compiling Tool-Using Agents from Behavioral Specifications

<!-- review:SF-2026-ARXIV-2603-08806:start -->
**问题**：`Test-Driven AI Agent Definition (TDAD): Compiling Tool-Using Agents from Behavioral Specifications` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `3 The TDAD Methodology` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.08806v1 HTML — §3 The TDAD Methodology [facet=method]; https://arxiv.org/html/2603.08806v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08806v1.html; sha256:a0b317a87d934851bd7c68494ddd6aa7e674da36a31b1ead97b38164e09b99f4`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6 Experimental Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08806v1 HTML — §6 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.08806v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08806v1.html; sha256:a0b317a87d934851bd7c68494ddd6aa7e674da36a31b1ead97b38164e09b99f4`。

**Trade-off / failure / coexistence**：限制与反证定位在 `8 Limitations`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-08806:start -->**Claim Boundary**：只支持 arXiv:2603.08806v1 §3 The TDAD Methodology 的机制与 §6 Experimental Results 的公开 workload；§8 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08806:end -->
<!-- review:SF-2026-ARXIV-2603-08806:end -->
### MASEval: Extending Multi-Agent Evaluation from Models to Systems

<!-- review:SF-2026-ARXIV-2603-08835:start -->
**问题**：`MASEval: Extending Multi-Agent Evaluation from Models to Systems` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `3.2 Module Architecture` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.08835v1 HTML — §3.2 Module Architecture [facet=method]; https://arxiv.org/html/2603.08835v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08835v1.html; sha256:dfad5d6c478a7daf4abb2148018cc5f74df0f55cdcbfa99858520d11a8e6dd63`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2 Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08835v1 HTML — §4.2 Results [facet=evaluation]; https://arxiv.org/html/2603.08835v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08835v1.html; sha256:dfad5d6c478a7daf4abb2148018cc5f74df0f55cdcbfa99858520d11a8e6dd63`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-08835:start -->**Claim Boundary**：只支持 arXiv:2603.08835v1 §3.2 Module Architecture 的机制与 §4.2 Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08835:end -->
<!-- review:SF-2026-ARXIV-2603-08835:end -->
### LDP: An Identity-Aware Protocol for Multi-Agent LLM Systems

<!-- review:SF-2026-ARXIV-2603-08852:start -->
**问题**：MCP/A2A 若不暴露 delegate identity、cost 和验证状态，跨 agent 路由只能依赖不透明 endpoint。

**旧路径为何合理**：把协议当作普通 tool adapter，部署和权限模型最简单。

**约束变化与机制**：LDP 把 identity card、payload negotiation、session state、provenance 与 trust domain写入协议。

**State / data / control owner**：`AGENT-MCP` 负责 协议身份、capability 声明、授权与审计状态；定位证据为 `arXiv:2603.08852v1 HTML — §5.6 Statistical Methodology [facet=method]; https://arxiv.org/html/2603.08852v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08852v1.html; sha256:74b0247eda27542b3d31ca5c7fe9f0cd32444d8ebd311ccbf728b20744a578d0`。

**Evaluation contract 与未证明部分**：小型本地模型池和部分模拟结果只提供初步证据；尤其模拟 attack/failure 数字不能当生产事实。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08852v1 HTML — §5.4 LLM-as-Judge Evaluation [facet=evaluation]; https://arxiv.org/html/2603.08852v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08852v1.html; sha256:74b0247eda27542b3d31ca5c7fe9f0cd32444d8ebd311ccbf728b20744a578d0`。

**Trade-off / failure / coexistence**：丰富 metadata 可能陈旧或被伪造，且增加协商成本；固定可信 agent 对仍可用更薄协议。

<!-- claim:SF-2026-ARXIV-2603-08852:start -->**Claim Boundary**：只支持 arXiv:2603.08852v1 §5.6 Statistical Methodology 的机制与 §5.4 LLM-as-Judge Evaluation 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08852:end -->
<!-- review:SF-2026-ARXIV-2603-08852:end -->
### The $qs$ Inequality: Quantifying the Double Penalty of Mixture-of-Experts at Inference

<!-- review:SF-2026-ARXIV-2603-08960:start -->
**问题**：`The $qs$ Inequality: Quantifying the Double Penalty of Mixture-of-Experts at Inference` 检查的是 `MODEL-MOE` 中 容量扩大后，激活成本和通信使全参数计算不可持续。 是否会改变现有设计边界。

**旧路径为何合理**：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

**约束变化与机制**：exact-v1 的 `4 Evaluation Methodology` 把论文方案定位到 expert 选择、capacity、placement 与通信；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MODEL-MOE` 负责 expert 选择、capacity、placement 与通信；定位证据为 `arXiv:2603.08960v1 HTML — §4 Evaluation Methodology [facet=method]; https://arxiv.org/html/2603.08960v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08960v1.html; sha256:2e01227172a0a7c9cb9f65f9bb7b22d0a727fee1c28253357b35e468e034daff`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4 Evaluation Methodology`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08960v1 HTML — §4 Evaluation Methodology [facet=evaluation]; https://arxiv.org/html/2603.08960v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.08960v1.html; sha256:2e01227172a0a7c9cb9f65f9bb7b22d0a727fee1c28253357b35e468e034daff`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Discussion`。规模较小、负载难预测或通信昂贵时 dense 仍可能占优。

<!-- claim:SF-2026-ARXIV-2603-08960:start -->**Claim Boundary**：只支持 arXiv:2603.08960v1 §4 Evaluation Methodology 的机制与 §4 Evaluation Methodology 的公开 workload；§7 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08960:end -->
<!-- review:SF-2026-ARXIV-2603-08960:end -->
### The Missing Memory Hierarchy: Demand Paging for LLM Context Windows

<!-- review:SF-2026-ARXIV-2603-09023:start -->
**问题**：Agent 的 message/tool-result 历史持续占用 prompt budget；不可恢复删除又会让后续重读丢失证据。

**旧路径为何合理**：完整携带 message history 最忠实，也不需要恢复协议。

**约束变化与机制**：Pichay 在 Messages-API proxy 中驱逐或压缩消息块，完整 conversation 留在 client backing store，以 retrieval handle、重复读取 fault 与 path/hash pinning 恢复内容。

**State / data / control owner**：`AGENT-CONTEXT` 负责 visible message working set、handle 与 pin state；client backing store 保留原始事实。该机制不管理 KV/HBM residency，定位于 exact-v1 §3。

**Evaluation contract 与未证明部分**：§5 只评测 L1 message eviction 与 L2 fault-driven pinning；L3 仅实现而未规模评测，L4 仅定义接口。

**Trade-off / failure / coexistence**：驱逐扩大 token working set，却引入 fault tail、错误驱逐与 path/hash 失效；短会话、不可寻址输出或高风险审计仍应完整携带。

<!-- claim:SF-2026-ARXIV-2603-09023:start -->**Claim Boundary**：只支持 arXiv:2603.09023v1 §3 的 Messages-API eviction/handle/fault/pinning 与 §5 的 L1/L2 实验；不外推为 KV/HBM paging 或已验证的 L3/L4。<!-- claim:SF-2026-ARXIV-2603-09023:end -->
<!-- review:SF-2026-ARXIV-2603-09023:end -->
### FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation

<!-- review:SF-2026-ARXIV-2603-09046:start -->
**问题**：`FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation` 检查的是 `INFER-SCHEDULING` 中 长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。 是否会改变现有设计边界。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：exact-v1 的 `3.3 System Overview` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.09046v1 HTML — §3.3 System Overview [facet=method]; https://arxiv.org/html/2603.09046v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09046v1.html; sha256:9e0fe8f7548e5dc8422a39df86d22776a24d5b575206df8fc8753163bd963d5d`。

**Evaluation contract 与未证明部分**：公开验证定位在 `7.2 Micro-benchmarks`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09046v1 HTML — §7.2 Micro-benchmarks [facet=evaluation]; https://arxiv.org/html/2603.09046v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09046v1.html; sha256:9e0fe8f7548e5dc8422a39df86d22776a24d5b575206df8fc8753163bd963d5d`。

**Trade-off / failure / coexistence**：限制与反证定位在 `2.2 ARM TrustZone and Its Limitations`。同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2603-09046:start -->**Claim Boundary**：只支持 arXiv:2603.09046v1 §3.3 System Overview 的机制与 §7.2 Micro-benchmarks 的公开 workload；§2.2 ARM TrustZone and Its Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09046:end -->
<!-- review:SF-2026-ARXIV-2603-09046:end -->
### GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models

<!-- review:SF-2026-ARXIV-2603-09079:start -->
**问题**：`GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models` 检查的是 `MULTIMODAL-EMBODIED-VLA` 中 物理闭环引入控制频率、感知延迟、动作安全和 edge/cloud placement 约束。 是否会改变现有设计边界。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：exact-v1 的 `III Method` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.09079v1 HTML — §III Method [facet=method]; https://arxiv.org/html/2603.09079v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09079v1.html; sha256:64f190b0c5da03d9fdaeee46f3f65b3fe55db4a71ed03eb041e36f0392bc196c`。

**Evaluation contract 与未证明部分**：公开验证定位在 `IV-B Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09079v1 HTML — §IV-B Main Results [facet=evaluation]; https://arxiv.org/html/2603.09079v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09079v1.html; sha256:64f190b0c5da03d9fdaeee46f3f65b3fe55db4a71ed03eb041e36f0392bc196c`。

**Trade-off / failure / coexistence**：限制与反证定位在 `IV-D4 Failure Cases`。低频、可人工接管或环境稳定时集中式 VLA 路径仍可成立。

<!-- claim:SF-2026-ARXIV-2603-09079:start -->**Claim Boundary**：只支持 arXiv:2603.09079v1 §III Method 的机制与 §IV-B Main Results 的公开 workload；§IV-D4 Failure Cases 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09079:end -->
<!-- review:SF-2026-ARXIV-2603-09079:end -->
### Latent World Models for Automated Driving: A Unified Taxonomy, Evaluation Framework, and Open Challenges

<!-- review:SF-2026-ARXIV-2603-09086:start -->
**问题**：`Latent World Models for Automated Driving: A Unified Taxonomy, Evaluation Framework, and Open Challenges` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `III INTERNAL MECHANICS: STRUCTURE, ALIGNMENT, AND DYNAMICS IN LATENT REPRESENTATIONS` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.09086v1 HTML — §III INTERNAL MECHANICS: STRUCTURE, ALIGNMENT, AND DYNAMICS IN LATENT REPRESENTATIONS [facet=method]; https://arxiv.org/html/2603.09086v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09086v1.html; sha256:0f1858abac1678fb3a2899b6610377a4d2ee83a0c4baee0f914f4a1f216a9847`。

**Evaluation contract 与未证明部分**：公开验证定位在 `IV-C Toward Unified Latent-Centric Evaluation Metrics`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09086v1 HTML — §IV-C Toward Unified Latent-Centric Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.09086v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09086v1.html; sha256:0f1858abac1678fb3a2899b6610377a4d2ee83a0c4baee0f914f4a1f216a9847`。

**Trade-off / failure / coexistence**：限制与反证定位在 `VII Conclusion`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-09086:start -->**Claim Boundary**：只支持 arXiv:2603.09086v1 §III INTERNAL MECHANICS: STRUCTURE, ALIGNMENT, AND DYNAMICS IN LATENT REPRESENTATIONS 的机制与 §IV-C Toward Unified Latent-Centric Evaluation Metrics 的公开 workload；§VII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09086:end -->
<!-- review:SF-2026-ARXIV-2603-09086:end -->
### Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards

<!-- review:SF-2026-ARXIV-2603-09117:start -->
**问题**：`Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards` 检查的是 `TRAIN-GRPO` 中 稀疏可验证奖励和 rollout 成本要求更有效地复用同组比较。 是否会改变现有设计边界。

**旧路径为何合理**：每条样本独立更新易实现，但难利用组内相对信号。

**约束变化与机制**：exact-v1 的 `2.4 Calibration Optimization Methods` 把论文方案定位到 prompt、rollout、group advantage 与 on-policy freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-GRPO` 负责 prompt、rollout、group advantage 与 on-policy freshness；定位证据为 `arXiv:2603.09117v1 HTML — §2.4 Calibration Optimization Methods [facet=method]; https://arxiv.org/html/2603.09117v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09117v1.html; sha256:2c79d6d9059fef7cb1703b8a78cd1089629461b286580776d3d74d89af8c1aa2`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6.2 Overall Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09117v1 HTML — §6.2 Overall Results [facet=evaluation]; https://arxiv.org/html/2603.09117v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09117v1.html; sha256:2c79d6d9059fef7cb1703b8a78cd1089629461b286580776d3d74d89af8c1aa2`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6.3 Ablation Studies`。高质量逐样本监督充足时 SFT/DPO 仍更简单。

<!-- claim:SF-2026-ARXIV-2603-09117:start -->**Claim Boundary**：只支持 arXiv:2603.09117v1 §2.4 Calibration Optimization Methods 的机制与 §6.2 Overall Results 的公开 workload；§6.3 Ablation Studies 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09117:end -->
<!-- review:SF-2026-ARXIV-2603-09117:end -->
### DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation

<!-- review:SF-2026-ARXIV-2603-09121:start -->
**问题**：`DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation` 检查的是 `MULTIMODAL-EMBODIED-VLA` 中 物理闭环引入控制频率、感知延迟、动作安全和 edge/cloud placement 约束。 是否会改变现有设计边界。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：exact-v1 的 `III Method` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.09121v1 HTML — §III Method [facet=method]; https://arxiv.org/html/2603.09121v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09121v1.html; sha256:7c18247742d5c845661afbe93f57dccac9d75d28a7f9a1d3792a24a26121321e`。

**Evaluation contract 与未证明部分**：公开验证定位在 `IV EXPERIMENTS`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09121v1 HTML — §IV EXPERIMENTS [facet=evaluation]; https://arxiv.org/html/2603.09121v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09121v1.html; sha256:7c18247742d5c845661afbe93f57dccac9d75d28a7f9a1d3792a24a26121321e`。

**Trade-off / failure / coexistence**：限制与反证定位在 `V CONCLUSION AND FUTURE WORK`。低频、可人工接管或环境稳定时集中式 VLA 路径仍可成立。

<!-- claim:SF-2026-ARXIV-2603-09121:start -->**Claim Boundary**：只支持 arXiv:2603.09121v1 §III Method 的机制与 §IV EXPERIMENTS 的公开 workload；§V CONCLUSION AND FUTURE WORK 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09121:end -->
<!-- review:SF-2026-ARXIV-2603-09121:end -->
### Collective AI can amplify tiny perturbations into divergent decisions

<!-- review:SF-2026-ARXIV-2603-09127:start -->
**问题**：`Collective AI can amplify tiny perturbations into divergent decisions` 检查的是 `AGENT-MULTI-AGENT` 中 任务并行、能力异质和跨信任域协作迫使系统显式管理委托与共享状态。 是否会改变现有设计边界。

**旧路径为何合理**：单 agent 持有完整上下文和控制流，规模小时最容易归因。

**约束变化与机制**：exact-v1 的 `Two design routes and non-additive interaction` 把论文方案定位到 agent identity、委托边、消息状态、协作协议与冲突处理；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MULTI-AGENT` 负责 agent identity、委托边、消息状态、协作协议与冲突处理；定位证据为 `arXiv:2603.09127v1 HTML — §Two design routes and non-additive interaction [facet=method]; https://arxiv.org/html/2603.09127v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09127v1.html; sha256:050f8e7858cf52585e6af357adcc685340ef9b6b1f08ccea3fdbe986f9cd5f06`。

**Evaluation contract 与未证明部分**：公开验证定位在 `S4.3 Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09127v1 HTML — §S4.3 Results [facet=evaluation]; https://arxiv.org/html/2603.09127v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09127v1.html; sha256:050f8e7858cf52585e6af357adcc685340ef9b6b1f08ccea3fdbe986f9cd5f06`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Discussion`。任务短且角色不需要隔离时，单 agent 仍有更低协调成本。

<!-- claim:SF-2026-ARXIV-2603-09127:start -->**Claim Boundary**：只支持 arXiv:2603.09127v1 §Two design routes and non-additive interaction 的机制与 §S4.3 Results 的公开 workload；§Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09127:end -->
<!-- review:SF-2026-ARXIV-2603-09127:end -->
### Real-Time Trust Verification for Safe Agentic Actions using TrustBench

<!-- review:SF-2026-ARXIV-2603-09157:start -->
**问题**：`Real-Time Trust Verification for Safe Agentic Actions using TrustBench` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `Dual-Mode Architecture` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.09157v1 HTML — §Dual-Mode Architecture [facet=method]; https://arxiv.org/html/2603.09157v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09157v1.html; sha256:1a3035f6e0bd9c407b9b32ae0250889cd58f176e9421ed1a4cb1a4ca14bb980f`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09157v1 HTML — §Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09157v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09157v1.html; sha256:1a3035f6e0bd9c407b9b32ae0250889cd58f176e9421ed1a4cb1a4ca14bb980f`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Component Ablation`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-09157:start -->**Claim Boundary**：只支持 arXiv:2603.09157v1 §Dual-Mode Architecture 的机制与 §Evaluation 的公开 workload；§Component Ablation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09157:end -->
<!-- review:SF-2026-ARXIV-2603-09157:end -->
### DuplexCascade: Full-Duplex Speech-to-Speech Dialogue with VAD-Free Cascaded ASR-LLM-TTS Pipeline and Micro-Turn Optimization

<!-- review:SF-2026-ARXIV-2603-09180:start -->
**问题**：`DuplexCascade: Full-Duplex Speech-to-Speech Dialogue with VAD-Free Cascaded ASR-LLM-TTS Pipeline and Micro-Turn Optimization` 检查的是 `INFER-SCHEDULING` 中 长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。 是否会改变现有设计边界。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：exact-v1 的 `4.1 Implementation Details` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.09180v1 HTML — §4.1 Implementation Details [facet=method]; https://arxiv.org/html/2603.09180v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09180v1.html; sha256:490943e4c62866a5811e1847f6c5e3578f4698188c992c5883c80b4cbb1d914c`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2 Full-Duplex-Bench Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09180v1 HTML — §4.2 Full-Duplex-Bench Results [facet=evaluation]; https://arxiv.org/html/2603.09180v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09180v1.html; sha256:490943e4c62866a5811e1847f6c5e3578f4698188c992c5883c80b4cbb1d914c`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion`。同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2603-09180:start -->**Claim Boundary**：只支持 arXiv:2603.09180v1 §4.1 Implementation Details 的机制与 §4.2 Full-Duplex-Bench Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09180:end -->
<!-- review:SF-2026-ARXIV-2603-09180:end -->
### Explainable Innovation Engine: Dual-Tree Agent-RAG with Methods-as-Nodes and Verifiable Write-Back

<!-- review:SF-2026-ARXIV-2603-09192:start -->
**问题**：`Explainable Innovation Engine: Dual-Tree Agent-RAG with Methods-as-Nodes and Verifiable Write-Back` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `3 Methods` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.09192v1 HTML — §3 Methods [facet=method]; https://arxiv.org/html/2603.09192v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09192v1.html; sha256:da5469c40df336edc3d41066dfced935f213a36d82aa267a704de28d8a3d5615`。

**Evaluation contract 与未证明部分**：公开验证定位在 `2.2 Retrieval Strategy, Reflection, and Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09192v1 HTML — §2.2 Retrieval Strategy, Reflection, and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09192v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09192v1.html; sha256:da5469c40df336edc3d41066dfced935f213a36d82aa267a704de28d8a3d5615`。

**Trade-off / failure / coexistence**：限制与反证定位在 `4.5 Discussion`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-09192:start -->**Claim Boundary**：只支持 arXiv:2603.09192v1 §3 Methods 的机制与 §2.2 Retrieval Strategy, Reflection, and Evaluation 的公开 workload；§4.5 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09192:end -->
<!-- review:SF-2026-ARXIV-2603-09192:end -->
### PIM-SHERPA: Software Method for On-device LLM Inference by Resolving PIM Memory Attribute and Layout Inconsistencies

<!-- review:SF-2026-ARXIV-2603-09216:start -->
**问题**：`PIM-SHERPA: Software Method for On-device LLM Inference by Resolving PIM Memory Attribute and Layout Inconsistencies` 检查的是 `INFER-TENSORRT-LLM` 中 固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。 是否会改变现有设计边界。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：exact-v1 的 `2.2 LPDDR-PIM architecture` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.09216v1 HTML — §2.2 LPDDR-PIM architecture [facet=method]; https://arxiv.org/html/2603.09216v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09216v1.html; sha256:d4cc0ce8b948bf0c5144813351b92dfe1e1250e550102a3100358ca5d977e704`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6 Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09216v1 HTML — §6 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09216v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09216v1.html; sha256:d4cc0ce8b948bf0c5144813351b92dfe1e1250e550102a3100358ca5d977e704`。

**Trade-off / failure / coexistence**：限制与反证定位在 `3.2 Current solutions and limitations`。模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。

<!-- claim:SF-2026-ARXIV-2603-09216:start -->**Claim Boundary**：只支持 arXiv:2603.09216v1 §2.2 LPDDR-PIM architecture 的机制与 §6 Evaluation 的公开 workload；§3.2 Current solutions and limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09216:end -->
<!-- review:SF-2026-ARXIV-2603-09216:end -->
### Beyond Test-Time Memory: State-Space Optimal Control for LLM Reasoning

<!-- review:SF-2026-ARXIV-2603-09221:start -->
**问题**：`Beyond Test-Time Memory: State-Space Optimal Control for LLM Reasoning` 检查的是 `AGENT-PLANNING` 中 自演化与长链任务需要区分已知、未知和可验证的下一步。 是否会改变现有设计边界。

**旧路径为何合理**：按当前 prompt 即时选择下一步，在短任务中无需维护额外 epistemic state。

**约束变化与机制**：exact-v1 的 `3.3 Hardware Co-Design for TTC` 把论文方案定位到 计划路由、证据需求与停止条件；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-PLANNING` 负责 计划路由、证据需求与停止条件；定位证据为 `arXiv:2603.09221v1 HTML — §3.3 Hardware Co-Design for TTC [facet=method]; https://arxiv.org/html/2603.09221v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09221v1.html; sha256:02893c0e8660b6453ebbf0092e3eab7c1329e7cd456c14906da992c56d228396`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Benchmark Evaluation.`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09221v1 HTML — §Benchmark Evaluation. [facet=evaluation]; https://arxiv.org/html/2603.09221v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09221v1.html; sha256:02893c0e8660b6453ebbf0092e3eab7c1329e7cd456c14906da992c56d228396`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations and Future Works.`。目标明确且一步可完成时直接执行仍更稳健。

<!-- claim:SF-2026-ARXIV-2603-09221:start -->**Claim Boundary**：只支持 arXiv:2603.09221v1 §3.3 Hardware Co-Design for TTC 的机制与 §Benchmark Evaluation. 的公开 workload；§Limitations and Future Works. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09221:end -->
<!-- review:SF-2026-ARXIV-2603-09221:end -->
### RAE-NWM: Navigation World Model in Dense Visual Representation Space

<!-- review:SF-2026-ARXIV-2603-09241:start -->
**问题**：`RAE-NWM: Navigation World Model in Dense Visual Representation Space` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `Representation Space and Architecture.` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.09241v1 HTML — §Representation Space and Architecture. [facet=method]; https://arxiv.org/html/2603.09241v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09241v1.html; sha256:9d647271225c76da7b184922d943442502a0dabd60651d6fec2d27e0a82776b7`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation Metrics.`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09241v1 HTML — §Evaluation Metrics. [facet=evaluation]; https://arxiv.org/html/2603.09241v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09241v1.html; sha256:9d647271225c76da7b184922d943442502a0dabd60651d6fec2d27e0a82776b7`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Discussion and Limitations`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-09241:start -->**Claim Boundary**：只支持 arXiv:2603.09241v1 §Representation Space and Architecture. 的机制与 §Evaluation Metrics. 的公开 workload；§6 Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09241:end -->
<!-- review:SF-2026-ARXIV-2603-09241:end -->
### ToolRosella: Translating Code Repositories into Standardized Tools for Scientific Agents

<!-- review:SF-2026-ARXIV-2603-09290:start -->
**问题**：`ToolRosella: Translating Code Repositories into Standardized Tools for Scientific Agents` 检查的是 `AGENT-TOOL-CALLING` 中 外部 action、side effect 和动态工具目录要求把提议与执行分离。 是否会改变现有设计边界。

**旧路径为何合理**：模型只输出文本时，错误影响停留在信息层。

**约束变化与机制**：exact-v1 的 `4 Methods` 把论文方案定位到 tool identity、argument validation、authorization、receipt 与 side-effect commit；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-TOOL-CALLING` 负责 tool identity、argument validation、authorization、receipt 与 side-effect commit；定位证据为 `arXiv:2603.09290v1 HTML — §4 Methods [facet=method]; https://arxiv.org/html/2603.09290v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09290v1.html; sha256:769f80ae80888a4c1de4143cc9e2cfd33b3fa159defd9b5f0b3d711936028a20`。

**Evaluation contract 与未证明部分**：公开验证定位在 `2.4.1 Case 1: Stroke Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09290v1 HTML — §2.4.1 Case 1: Stroke Analysis [facet=evaluation]; https://arxiv.org/html/2603.09290v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09290v1.html; sha256:769f80ae80888a4c1de4143cc9e2cfd33b3fa159defd9b5f0b3d711936028a20`。

**Trade-off / failure / coexistence**：限制与反证定位在 `3.1 Contributions and limitations`。只读、无副作用查询仍可使用较薄的调用适配层。

<!-- claim:SF-2026-ARXIV-2603-09290:start -->**Claim Boundary**：只支持 arXiv:2603.09290v1 §4 Methods 的机制与 §2.4.1 Case 1: Stroke Analysis 的公开 workload；§3.1 Contributions and limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09290:end -->
<!-- review:SF-2026-ARXIV-2603-09290:end -->
### TA-Mem: Tool-Augmented Autonomous Memory Retrieval for LLM in Long-Term Conversational QA

<!-- review:SF-2026-ARXIV-2603-09297:start -->
**问题**：`TA-Mem: Tool-Augmented Autonomous Memory Retrieval for LLM in Long-Term Conversational QA` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `III. METHODOLOGY` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.09297v1 PDF — §III. METHODOLOGY [facet=method]; https://arxiv.org/pdf/2603.09297v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09297v1.pdf.txt; sha256:e4966991942a9f9c6eb3bf507bc92599d581b98f6c02a9377890dc37c3ece52f`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/pdf/2603.09297v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09297v1.pdf.txt; sha256:e4966991942a9f9c6eb3bf507bc92599d581b98f6c02a9377890dc37c3ece52f`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-09297:start -->**Claim Boundary**：只支持 arXiv:2603.09297v1 §III. METHODOLOGY 的机制与 §Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09297:end -->
<!-- review:SF-2026-ARXIV-2603-09297:end -->
### AI Act Evaluation Benchmark: An Open, Transparent, and Reproducible Evaluation Dataset for NLP and RAG Systems

<!-- review:SF-2026-ARXIV-2603-09435:start -->
**问题**：`AI Act Evaluation Benchmark: An Open, Transparent, and Reproducible Evaluation Dataset for NLP and RAG Systems` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `3.2 Methodology` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.09435v1 HTML — §3.2 Methodology [facet=method]; https://arxiv.org/html/2603.09435v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09435v1.html; sha256:17eba511d989a51ce666ea4352e5871a0e142e0d0f8eab5ab30b0c2e31e30d69`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.09435v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09435v1.html; sha256:17eba511d989a51ce666ea4352e5871a0e142e0d0f8eab5ab30b0c2e31e30d69`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusions & Future Work`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-09435:start -->**Claim Boundary**：只支持 arXiv:2603.09435v1 §3.2 Methodology 的机制与 §Evaluation 的公开 workload；§6 Conclusions & Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09435:end -->
<!-- review:SF-2026-ARXIV-2603-09435:end -->
### Variational Routing: A Scalable Bayesian Framework for Calibrated Mixture-of-Experts Transformers

<!-- review:SF-2026-ARXIV-2603-09453:start -->
**问题**：`Variational Routing: A Scalable Bayesian Framework for Calibrated Mixture-of-Experts Transformers` 检查的是 `MODEL-MOE` 中 容量扩大后，激活成本和通信使全参数计算不可持续。 是否会改变现有设计边界。

**旧路径为何合理**：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

**约束变化与机制**：exact-v1 的 `Methodology` 把论文方案定位到 expert 选择、capacity、placement 与通信；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MODEL-MOE` 负责 expert 选择、capacity、placement 与通信；定位证据为 `arXiv:2603.09453v1 HTML — §Methodology [facet=method]; https://arxiv.org/html/2603.09453v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09453v1.html; sha256:5f4894957e4ee987cba696a312a697726ec3228699e8195c2c249e3fc338ae35`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5 Experiments`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09453v1 HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.09453v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09453v1.html; sha256:5f4894957e4ee987cba696a312a697726ec3228699e8195c2c249e3fc338ae35`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Conclusion`。规模较小、负载难预测或通信昂贵时 dense 仍可能占优。

<!-- claim:SF-2026-ARXIV-2603-09453:start -->**Claim Boundary**：只支持 arXiv:2603.09453v1 §Methodology 的机制与 §5 Experiments 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09453:end -->
<!-- review:SF-2026-ARXIV-2603-09453:end -->
### Streaming Autoregressive Video Generation via Diagonal Distillation

<!-- review:SF-2026-ARXIV-2603-09488:start -->
**问题**：`Streaming Autoregressive Video Generation via Diagonal Distillation` 检查的是 `MULTIMODAL-GENERATIVE-PARADIGMS` 中 图像、视频和并行文本生成需要重审 factorization、修正轮数和提交边界。 是否会改变现有设计边界。

**旧路径为何合理**：causal autoregression 提供明确顺序和简单缓存语义。

**约束变化与机制**：exact-v1 的 `H.2 Evaluation Methodology` 把论文方案定位到 生成顺序、proposal/correction 与终止状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-GENERATIVE-PARADIGMS` 负责 生成顺序、proposal/correction 与终止状态；定位证据为 `arXiv:2603.09488v1 HTML — §H.2 Evaluation Methodology [facet=method]; https://arxiv.org/html/2603.09488v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09488v1.html; sha256:3c8856edacae2b87fe3e2bb33b6e6131c64e311bd6471b06c61f09cfb91086ca`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.4 Long Video Generation Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09488v1 HTML — §4.4 Long Video Generation Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09488v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09488v1.html; sha256:3c8856edacae2b87fe3e2bb33b6e6131c64e311bd6471b06c61f09cfb91086ca`。

**Trade-off / failure / coexistence**：限制与反证定位在 `4.3 Ablation Studies`。需要严格流式输出和成熟 cache 时 autoregressive 路径仍可靠。

<!-- claim:SF-2026-ARXIV-2603-09488:start -->**Claim Boundary**：只支持 arXiv:2603.09488v1 §H.2 Evaluation Methodology 的机制与 §4.4 Long Video Generation Evaluation 的公开 workload；§4.3 Ablation Studies 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09488:end -->
<!-- review:SF-2026-ARXIV-2603-09488:end -->
### Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation in Non-Markovian Simulation Benchmarks

<!-- review:SF-2026-ARXIV-2603-09513:start -->
**问题**：`Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation in Non-Markovian Simulation Benchmarks` 检查的是 `MULTIMODAL-EMBODIED-VLA` 中 物理闭环引入控制频率、感知延迟、动作安全和 edge/cloud placement 约束。 是否会改变现有设计边界。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：exact-v1 的 `LLM-Aided Lock Design` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.09513v1 HTML — §LLM-Aided Lock Design [facet=method]; https://arxiv.org/html/2603.09513v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09513v1.html; sha256:cb86d71edfeacee89a7a675644b40b1fcace4bee4c12b260ac91ec7e7ab7ff7d`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09513v1 HTML — §Main Results [facet=evaluation]; https://arxiv.org/html/2603.09513v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09513v1.html; sha256:cb86d71edfeacee89a7a675644b40b1fcace4bee4c12b260ac91ec7e7ab7ff7d`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Possible Causes of Remaining Failures`。低频、可人工接管或环境稳定时集中式 VLA 路径仍可成立。

<!-- claim:SF-2026-ARXIV-2603-09513:start -->**Claim Boundary**：只支持 arXiv:2603.09513v1 §LLM-Aided Lock Design 的机制与 §Main Results 的公开 workload；§Possible Causes of Remaining Failures 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09513:end -->
<!-- review:SF-2026-ARXIV-2603-09513:end -->
### Compiler-First State Space Duality and Portable $O(1)$ Autoregressive Caching for Inference

<!-- review:SF-2026-ARXIV-2603-09555:start -->
**问题**：状态空间模型的 O(1) decode cache 常依赖手写模型特例，阻碍跨后端复用和正确性验证。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：该工作以 JAX/XLA 实现 Mamba-2 SSD 的 sequence/recurrent 路径，再用 token-for-token greedy decoding 与数值容差做 differential validation；它没有提供形式化 transformation verifier。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 sequence→recurrent→backend lowering 与 build/test contract；机制定位为 §3、§4.2–§4.3。

**Evaluation contract 与未证明部分**：§5.2–§5.7 支持数值和性能 validation；这不是 proof-producing verifier，不覆盖的精度、算子族和编译目标不能由此推断。

**Trade-off / failure / coexistence**：编译推导降低人工特化成本，却增加 IR 语义和数值等价验证责任；不满足 duality 的算子仍需原始序列执行。

<!-- claim:SF-2026-ARXIV-2603-09555:start -->**Claim Boundary**：只支持 arXiv:2603.09555v1 §3、§4.2–§4.3 与 §5.2–§5.7 的实现及 differential validation；不构成形式化等价证明，§5.8 之外不外推。<!-- claim:SF-2026-ARXIV-2603-09555:end -->
<!-- review:SF-2026-ARXIV-2603-09555:end -->
### Context Engineering: From Prompts to Corporate Multi-Agent Architecture

<!-- review:SF-2026-ARXIV-2603-09619:start -->
**问题**：`Context Engineering: From Prompts to Corporate Multi-Agent Architecture` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `6. Context Engineering as a Design Object` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.09619v1 PDF — §6. Context Engineering as a Design Object [facet=method]; https://arxiv.org/pdf/2603.09619v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09619v1.pdf.txt; sha256:6912d5467e52b0e417610130e6dbd88e23cb0cff679f670f6b4e8c00d7de80e3`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/pdf/2603.09619v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09619v1.pdf.txt; sha256:6912d5467e52b0e417610130e6dbd88e23cb0cff679f670f6b4e8c00d7de80e3`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-09619:start -->**Claim Boundary**：只支持 arXiv:2603.09619v1 §6. Context Engineering as a Design Object 的机制与 §Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09619:end -->
<!-- review:SF-2026-ARXIV-2603-09619:end -->
### When to Lock Attention: Training-Free KV Control in Video Diffusion

<!-- review:SF-2026-ARXIV-2603-09657:start -->
**问题**：`When to Lock Attention: Training-Free KV Control in Video Diffusion` 检查的是 `INFER-KV-CACHE` 中 长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。 是否会改变现有设计边界。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：exact-v1 的 `B.1 Implementation Details` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.09657v1 HTML — §B.1 Implementation Details [facet=method]; https://arxiv.org/html/2603.09657v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09657v1.html; sha256:ea6902dc8b1e595fe29f0338fcd8cec4db2d9c9b76a6b593f23e2ec8297b5824`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.2 Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09657v1 HTML — §5.2 Results [facet=evaluation]; https://arxiv.org/html/2603.09657v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09657v1.html; sha256:ea6902dc8b1e595fe29f0338fcd8cec4db2d9c9b76a6b593f23e2ec8297b5824`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusions`。小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2603-09657:start -->**Claim Boundary**：只支持 arXiv:2603.09657v1 §B.1 Implementation Details 的机制与 §5.2 Results 的公开 workload；§6 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09657:end -->
<!-- review:SF-2026-ARXIV-2603-09657:end -->
### ActiveUltraFeedback: Efficient Preference Data Generation using Active Learning

<!-- review:SF-2026-ARXIV-2603-09692:start -->
**问题**：`ActiveUltraFeedback: Efficient Preference Data Generation using Active Learning` 检查的是 `TRAIN-RLHF` 中 模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。 是否会改变现有设计边界。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：exact-v1 的 `D.1 Scoring Methodology` 把论文方案定位到 rollout、reward、policy/reference 与更新 freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.09692v1 HTML — §D.1 Scoring Methodology [facet=method]; https://arxiv.org/html/2603.09692v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09692v1.html; sha256:011516aad5bc77d0b4418cce9db2e36bf960e7a2cb2b681623a521f44aafbd0b`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5 Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09692v1 HTML — §5 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09692v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09692v1.html; sha256:011516aad5bc77d0b4418cce9db2e36bf960e7a2cb2b681623a521f44aafbd0b`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion`。反馈稳定、任务窄且分布固定时成熟配方仍可复用。

<!-- claim:SF-2026-ARXIV-2603-09692:start -->**Claim Boundary**：只支持 arXiv:2603.09692v1 §D.1 Scoring Methodology 的机制与 §5 Evaluation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09692:end -->
<!-- review:SF-2026-ARXIV-2603-09692:end -->
### AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents

<!-- review:SF-2026-ARXIV-2603-09716:start -->
**问题**：`AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `3 The AutoAgent Framework: A Unified Architecture for Self-Evolution` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.09716v1 HTML — §3 The AutoAgent Framework: A Unified Architecture for Self-Evolution [facet=method]; https://arxiv.org/html/2603.09716v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09716v1.html; sha256:002a269298acdff7133209810976fcd4f92c4db78abf1c5adad5b7cc49a1151c`。

**Evaluation contract 与未证明部分**：公开验证定位在 `8 Experiments and Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09716v1 HTML — §8 Experiments and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09716v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09716v1.html; sha256:002a269298acdff7133209810976fcd4f92c4db78abf1c5adad5b7cc49a1151c`。

**Trade-off / failure / coexistence**：限制与反证定位在 `9 Conclusion and Future Work`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-09716:start -->**Claim Boundary**：只支持 arXiv:2603.09716v1 §3 The AutoAgent Framework: A Unified Architecture for Self-Evolution 的机制与 §8 Experiments and Evaluation 的公开 workload；§9 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09716:end -->
<!-- review:SF-2026-ARXIV-2603-09716:end -->
### WVA: A Global Optimization Control Plane for llmd

<!-- review:SF-2026-ARXIV-2603-09730:start -->
**问题**：Kubernetes HPA 看不到 KV 饱和、SLO 与异构 variant，scale-down 还可能破坏 stateful inference。

**旧路径为何合理**：独占 GPU 提供最清晰的隔离和性能归因。

**约束变化与机制**：WVA 与 llm-d 联合使用 engine saturation、headroom 和 fragmentation 状态做 variant-aware 扩缩。

**State / data / control owner**：`PLATFORM-GPU-SCHEDULER` 负责 GPU slice、隔离、配额与抢占控制；定位证据为 `arXiv:2603.09730v1 HTML — §IV-B Design Rationale: Why Pluggability? [facet=method]; https://arxiv.org/html/2603.09730v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09730v1.html; sha256:f8e48fcf33cf2f2baf583a1ac87543f8916bf3a1d3db5c368c904d37552251f3`。

**Evaluation contract 与未证明部分**：作者实验只支持其 cluster、流量和 cost model；摘要中的吞吐/失败改善不能外推其他环境。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09730v1 HTML — §V-D Physical Cluster Validation [facet=evaluation]; https://arxiv.org/html/2603.09730v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09730v1.html; sha256:f8e48fcf33cf2f2baf583a1ac87543f8916bf3a1d3db5c368c904d37552251f3`。

**Trade-off / failure / coexistence**：全局 control plane 提高利用率却依赖遥测新鲜度和迁移策略；同质无状态服务仍可用 HPA。

<!-- claim:SF-2026-ARXIV-2603-09730:start -->**Claim Boundary**：只支持 arXiv:2603.09730v1 §IV-B Design Rationale: Why Pluggability? 的机制与 §V-D Physical Cluster Validation 的公开 workload；§VII Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09730:end -->
<!-- review:SF-2026-ARXIV-2603-09730:end -->
### Epistemic Closure: Autonomous Mechanism Completion for Physically Consistent Simulation

<!-- review:SF-2026-ARXIV-2603-09756:start -->
**问题**：`Epistemic Closure: Autonomous Mechanism Completion for Physically Consistent Simulation` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `4 Methodology` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.09756v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2603.09756v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09756v1.html; sha256:e2254df70cad22526b2013d0b4bef09232470c36b1b9141f6b93b1bdd3090d2b`。

**Evaluation contract 与未证明部分**：公开验证定位在 `2 Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09756v1 HTML — §2 Results [facet=evaluation]; https://arxiv.org/html/2603.09756v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09756v1.html; sha256:e2254df70cad22526b2013d0b4bef09232470c36b1b9141f6b93b1bdd3090d2b`。

**Trade-off / failure / coexistence**：限制与反证定位在 `3 Discussion`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-09756:start -->**Claim Boundary**：只支持 arXiv:2603.09756v1 §4 Methodology 的机制与 §2 Results 的公开 workload；§3 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09756:end -->
<!-- review:SF-2026-ARXIV-2603-09756:end -->
### One-Eval: An Agentic System for Automated and Traceable LLM Evaluation

<!-- review:SF-2026-ARXIV-2603-09821:start -->
**问题**：`One-Eval: An Agentic System for Automated and Traceable LLM Evaluation` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `3.1 Framework Overview` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.09821v1 HTML — §3.1 Framework Overview [facet=method]; https://arxiv.org/html/2603.09821v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09821v1.html; sha256:284da23888be1cd2370a3965ac83ce3e85e40efa30d4db4eb2e9690dc3cb900e`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4 Experiments`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09821v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.09821v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09821v1.html; sha256:284da23888be1cd2370a3965ac83ce3e85e40efa30d4db4eb2e9690dc3cb900e`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-09821:start -->**Claim Boundary**：只支持 arXiv:2603.09821v1 §3.1 Framework Overview 的机制与 §4 Experiments 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09821:end -->
<!-- review:SF-2026-ARXIV-2603-09821:end -->
### InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing

<!-- review:SF-2026-ARXIV-2603-09877:start -->
**问题**：`InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing` 检查的是 `MULTIMODAL-GENERATIVE-PARADIGMS` 中 图像、视频和并行文本生成需要重审 factorization、修正轮数和提交边界。 是否会改变现有设计边界。

**旧路径为何合理**：causal autoregression 提供明确顺序和简单缓存语义。

**约束变化与机制**：exact-v1 的 `3.1.1 Overall Design Principles` 把论文方案定位到 生成顺序、proposal/correction 与终止状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-GENERATIVE-PARADIGMS` 负责 生成顺序、proposal/correction 与终止状态；定位证据为 `arXiv:2603.09877v1 HTML — §3.1.1 Overall Design Principles [facet=method]; https://arxiv.org/html/2603.09877v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09877v1.html; sha256:d0ed98d6b58e6de71d01bc2b75a4dc7bfd2c2dde14bae07e8fd6a1b2824e89ce`。

**Evaluation contract 与未证明部分**：公开验证定位在 `A.2.2 Evaluation Metrics`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09877v1 HTML — §A.2.2 Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.09877v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09877v1.html; sha256:d0ed98d6b58e6de71d01bc2b75a4dc7bfd2c2dde14bae07e8fd6a1b2824e89ce`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion`。需要严格流式输出和成熟 cache 时 autoregressive 路径仍可靠。

<!-- claim:SF-2026-ARXIV-2603-09877:start -->**Claim Boundary**：只支持 arXiv:2603.09877v1 §3.1.1 Overall Design Principles 的机制与 §A.2.2 Evaluation Metrics 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09877:end -->
<!-- review:SF-2026-ARXIV-2603-09877:end -->
### Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track

<!-- review:SF-2026-ARXIV-2603-09891:start -->
**问题**：`Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track` 检查的是 `AGENT-RAG` 中 知识时效、私有数据和可引用证据要求在生成前建立可追踪的检索路径。 是否会改变现有设计边界。

**旧路径为何合理**：把训练权重或完整上下文视为唯一知识来源，链路短且状态少。

**约束变化与机制**：exact-v1 的 `2 Task Setup` 把论文方案定位到 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-RAG` 负责 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；定位证据为 `arXiv:2603.09891v1 HTML — §2 Task Setup [facet=method]; https://arxiv.org/html/2603.09891v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09891v1.html; sha256:0803e041f5c0cbeb4cd2f3f9b386a8f1e674411e82921a587b4121d95e74a200`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3.3 Support Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09891v1 HTML — §3.3 Support Evaluation [facet=evaluation]; https://arxiv.org/html/2603.09891v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09891v1.html; sha256:0803e041f5c0cbeb4cd2f3f9b386a8f1e674411e82921a587b4121d95e74a200`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion`。知识稳定且已被模型可靠覆盖时，直接生成仍具有更低延迟。

<!-- claim:SF-2026-ARXIV-2603-09891:start -->**Claim Boundary**：只支持 arXiv:2603.09891v1 §2 Task Setup 的机制与 §3.3 Support Evaluation 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09891:end -->
<!-- review:SF-2026-ARXIV-2603-09891:end -->
### MSSR: Memory-Aware Adaptive Replay for Continual LLM Fine-Tuning

<!-- review:SF-2026-ARXIV-2603-09892:start -->
**问题**：`MSSR: Memory-Aware Adaptive Replay for Continual LLM Fine-Tuning` 检查的是 `MODEL-LONG-CONTEXT` 中 序列增长令计算、显存和信息稀释同时恶化。 是否会改变现有设计边界。

**旧路径为何合理**：全量 attention 保留任意 token 交互，在中短序列上最直接。

**约束变化与机制**：exact-v1 的 `Framework Overview.` 把论文方案定位到 上下文选择、层次化表示和可访问记忆的语义边界；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MODEL-LONG-CONTEXT` 负责 上下文选择、层次化表示和可访问记忆的语义边界；定位证据为 `arXiv:2603.09892v1 HTML — §Framework Overview. [facet=method]; https://arxiv.org/html/2603.09892v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09892v1.html; sha256:8d975eb1955578b3bd957d6b5bd736531b7cebfcdac2fc554cae7967b91fced1`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09892v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.09892v1; papers/2026/03/_sources/daily-20260311/exact-v1-bodies/2603.09892v1.html; sha256:8d975eb1955578b3bd957d6b5bd736531b7cebfcdac2fc554cae7967b91fced1`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion`。任务确实依赖密集全局交互且长度可控时全量 attention 仍是基线。

<!-- claim:SF-2026-ARXIV-2603-09892:start -->**Claim Boundary**：只支持 arXiv:2603.09892v1 §Framework Overview. 的机制与 §4.2 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09892:end -->
<!-- review:SF-2026-ARXIV-2603-09892:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-08797 | score_7_9;potential_books_delta | selected | DA-20260311-07 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260311-07 |
| SF-2026-ARXIV-2603-09023 | score_7_9;potential_books_delta | selected | DA-20260311-12 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260311-12 |
| SF-2026-ARXIV-2603-09555 | score_7_9;potential_books_delta | selected | DA-20260311-31 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260311-31 |

<!-- analysis:DA-20260311-07:start -->
### Serving Compound Inference Systems on Datacenter GPUs

compound inference 把一次用户请求展开成模型、检索器和后处理 DAG，传统按单模型队列优化会错过关键路径。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：论文以 DAG readiness、GPU residency 与跨阶段依赖为调度对象，联合选择 stage placement 和执行次序，使资源决策服从端到端完成时间。 其公开验证边界为：数据中心 GPU 实验验证其公开 DAG 与负载下的端到端结果；未证明任意动态 agent graph 或多租户策略都保持同样收益。 新增代价与回退条件为：依赖感知提高关键路径利用率，但要求精确 stage profile 与中间状态追踪；单模型独立请求仍可使用较简单的 continuous batching。
<!-- analysis:DA-20260311-07:end -->
<!-- analysis:DA-20260311-12:start -->
### The Missing Memory Hierarchy: Demand Paging for LLM Context Windows

长 context 即使逻辑上可寻址，也可能无法全部常驻 GPU；静态截断把容量问题误当成语义选择。 旧路径在其原约束下仍合理：完整、逐 token 保存 KV，换取语义透明和最低重算风险。 本 family 的设计变化是：该系统将 context page 的驻留、换入、淘汰和故障恢复变成显式 memory-management state，由访问需求而非固定窗口决定物理位置。 其公开验证边界为：评测证明所测模型、介质和访问模式中的容量/延迟关系；它没有证明任意注意力访问都具有足够 locality。 新增代价与回退条件为：分页扩大可服务 context，但 page fault 会制造尾延迟和抖动；访问密集或上下文较短时完整常驻仍是更可预测的基线。
<!-- analysis:DA-20260311-12:end -->
<!-- analysis:DA-20260311-31:start -->
### Compiler-First State Space Duality and Portable $O(1)$ Autoregressive Caching for Inference

状态空间模型的 O(1) decode cache 常依赖手写模型特例，阻碍跨后端复用和正确性验证。 旧路径在其原约束下仍合理：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。 本 family 的设计变化是：Compiler-First State Space Duality 从算子语义推导等价 recurrent form，再由编译器生成固定大小的 autoregressive state 与更新程序。 其公开验证边界为：公开模型与后端实验支持等价变换和便携执行；不覆盖的数值精度、算子族和编译目标不能由此推断。 新增代价与回退条件为：编译推导降低人工特化成本，却增加 IR 语义和数值等价验证责任；不满足 duality 的算子仍需原始序列执行。
<!-- analysis:DA-20260311-31:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-08727 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#跨-turn-eviction-必须保留-surviving-row-identity (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08727 | delta:SF-2026-ARXIV-2603-08727 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08727 |
| SF-2026-ARXIV-2603-08739 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#小结 (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08739 | delta:SF-2026-ARXIV-2603-08739 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08739 |
| SF-2026-ARXIV-2603-08743 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-从生成私有状态演进为受约束的下游读出接口 (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08743 | delta:SF-2026-ARXIV-2603-08743 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08743 |
| SF-2026-ARXIV-2603-08747 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#低-batch-decode：当-all-reduce-barrier-成为执行瓶颈 (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08747 | delta:SF-2026-ARXIV-2603-08747 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08747 |
| SF-2026-ARXIV-2603-08755 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#agent-recovery-state-超出-transcript (section Ch-owner) | books/part-07-agent/83-mcp.md#第83章-mcp (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08755 | delta:SF-2026-ARXIV-2603-08755 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08755 |
| SF-2026-ARXIV-2603-08761 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#从-scalar-confidence-到-safe-commit-certificate (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08761 | delta:SF-2026-ARXIV-2603-08761 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08761 |
| SF-2026-ARXIV-2603-08797 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#从队列启发式到时间耦合的资源影子价格 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08797 | delta:SF-2026-ARXIV-2603-08797 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-08797 |
| SF-2026-ARXIV-2603-08806 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08806 | delta:SF-2026-ARXIV-2603-08806 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08806 |
| SF-2026-ARXIV-2603-08835 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08835 | delta:SF-2026-ARXIV-2603-08835 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08835 |
| SF-2026-ARXIV-2603-08852 | AGENT-MCP | books/part-07-agent/83-mcp.md#authorization-之前还需要可验证的-server-admission (section Ch-owner) | books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent); books/part-07-agent/84-agent-platform.md#第84章-agent-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08852 | delta:SF-2026-ARXIV-2603-08852 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08852 |
| SF-2026-ARXIV-2603-08960 | MODEL-MOE | books/part-02-model/21-moe.md#本章要回答的问题 (section Ch-owner) | books/part-02-model/20-sampling.md#第20章-sampling (section Ch-adjacent); books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08960 | delta:SF-2026-ARXIV-2603-08960 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08960 |
| SF-2026-ARXIV-2603-09023 | AGENT-CONTEXT | books/part-07-agent/75-context.md#context-identity-与-cache (section Ch-owner) | books/part-07-agent/74-prompt.md#第74章-prompt (section Ch-adjacent); books/part-07-agent/77-memory.md#第77章-memory (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09023 | delta:SF-2026-ARXIV-2603-09023 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-09023 |
| SF-2026-ARXIV-2603-09046 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#当前能放下，不等于未来可完成 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09046 | delta:SF-2026-ARXIV-2603-09046 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09046 |
| SF-2026-ARXIV-2603-09079 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09079 | delta:SF-2026-ARXIV-2603-09079 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09079 |
| SF-2026-ARXIV-2603-09086 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09086 | delta:SF-2026-ARXIV-2603-09086 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09086 |
| SF-2026-ARXIV-2603-09117 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#measurement-也是-reward-interface-的一部分 (section Ch-owner) | books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent); books/part-04-training-system/34-dpo.md#第34章-dpo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09117 | delta:SF-2026-ARXIV-2603-09117 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09117 |
| SF-2026-ARXIV-2603-09121 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#online-rl-应通过受限-action-interface-接入-vla (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09121 | delta:SF-2026-ARXIV-2603-09121 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09121 |
| SF-2026-ARXIV-2603-09127 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/81-workflow.md#第81章-workflow (section Ch-adjacent); books/part-07-agent/83-mcp.md#第83章-mcp (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09127 | delta:SF-2026-ARXIV-2603-09127 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09127 |
| SF-2026-ARXIV-2603-09157 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#skill-必须在真实-control-path-中评估 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09157 | delta:SF-2026-ARXIV-2603-09157 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09157 |
| SF-2026-ARXIV-2603-09180 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#低带宽拓扑要联合预算-hops、bytes-与-steps (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09180 | delta:SF-2026-ARXIV-2603-09180 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09180 |
| SF-2026-ARXIV-2603-09192 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09192 | delta:SF-2026-ARXIV-2603-09192 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09192 |
| SF-2026-ARXIV-2603-09216 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#异步工作不必永久绑定固定-physical-core (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09216 | delta:SF-2026-ARXIV-2603-09216 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09216 |
| SF-2026-ARXIV-2603-09221 | AGENT-PLANNING | books/part-07-agent/79-planning.md#从-project-brief-到可验证-task-contracts (section Ch-owner) | books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent); books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09221 | delta:SF-2026-ARXIV-2603-09221 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09221 |
| SF-2026-ARXIV-2603-09241 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#在谈-state-之前，先声明预测-channel (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09241 | delta:SF-2026-ARXIV-2603-09241 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09241 |
| SF-2026-ARXIV-2603-09290 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#interface-granularity：不是-tool-越多越有能力 (section Ch-owner) | books/part-07-agent/77-memory.md#第77章-memory (section Ch-adjacent); books/part-07-agent/79-planning.md#第79章-planning (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09290 | delta:SF-2026-ARXIV-2603-09290 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09290 |
| SF-2026-ARXIV-2603-09297 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09297 | delta:SF-2026-ARXIV-2603-09297 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09297 |
| SF-2026-ARXIV-2603-09435 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09435 | delta:SF-2026-ARXIV-2603-09435 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09435 |
| SF-2026-ARXIV-2603-09453 | MODEL-MOE | books/part-02-model/21-moe.md#先改变通信坐标，再扩大稀疏容量 (section Ch-owner) | books/part-02-model/20-sampling.md#第20章-sampling (section Ch-adjacent); books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09453 | delta:SF-2026-ARXIV-2603-09453 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09453 |
| SF-2026-ARXIV-2603-09488 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#从一次生成到-plan-→-generate-→-validate-→-retry (section Ch-owner) | books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent); books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09488 | delta:SF-2026-ARXIV-2603-09488 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09488 |
| SF-2026-ARXIV-2603-09513 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#fleet-学习必须把部署、干预与再部署组成版本循环 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09513 | delta:SF-2026-ARXIV-2603-09513 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09513 |
| SF-2026-ARXIV-2603-09555 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#execution-plan-先拥有-state再选择-kernel (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-vllm (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09555 | delta:SF-2026-ARXIV-2603-09555 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-09555 |
| SF-2026-ARXIV-2603-09619 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#failure-attribution、perception-routing-与-sticky-state-ownership (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09619 | delta:SF-2026-ARXIV-2603-09619 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09619 |
| SF-2026-ARXIV-2603-09657 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#稀疏-kv-保留的是派生状态，不只是被抽样的-token (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09657 | delta:SF-2026-ARXIV-2603-09657 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09657 |
| SF-2026-ARXIV-2603-09692 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09692 | delta:SF-2026-ARXIV-2603-09692 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09692 |
| SF-2026-ARXIV-2603-09716 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09716 | delta:SF-2026-ARXIV-2603-09716 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09716 |
| SF-2026-ARXIV-2603-09730 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/62-gateway.md#第62章-gateway (section Ch-adjacent); books/part-06-ai-infrastructure/64-volcano.md#第64章-gang-与队列调度：以-volcano-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09730 | delta:SF-2026-ARXIV-2603-09730 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09730 |
| SF-2026-ARXIV-2603-09756 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09756 | delta:SF-2026-ARXIV-2603-09756 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09756 |
| SF-2026-ARXIV-2603-09821 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09821 | delta:SF-2026-ARXIV-2603-09821 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09821 |
| SF-2026-ARXIV-2603-09877 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#exploration-是训练计算轴，不是新的生成真值 (section Ch-owner) | books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent); books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09877 | delta:SF-2026-ARXIV-2603-09877 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09877 |
| SF-2026-ARXIV-2603-09891 | AGENT-RAG | books/part-07-agent/76-rag.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/75-context.md#第75章-context (section Ch-adjacent); books/part-07-agent/77-memory.md#第77章-memory (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09891 | delta:SF-2026-ARXIV-2603-09891 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09891 |
| SF-2026-ARXIV-2603-09892 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#路线六：让模型在-test-time-更新内部记忆 (section Ch-owner) | books/part-02-model/21-moe.md#第21章-moe (section Ch-adjacent); books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09892 | delta:SF-2026-ARXIV-2603-09892 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09892 |

<!-- books-review:SF-2026-ARXIV-2603-08727:start -->
### ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08727:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：QueryMemory 不拥有事实或授权，只影响派生 cache retention；误判时必须能回退重算。新增 state 带来 intent drift、 slot-map correctness、metadata 和 eviction overhead。作者 Qwen3-8B/Qwen2.5-14B、BCP 与 8k budget 只支持所测 quality/memory slice，`8k` 不是 latency SLO，也不证明任意 prefix sharing 安全。<!-- existing:SF-2026-ARXIV-2603-08727:end -->

<!-- delta:SF-2026-ARXIV-2603-08727:start -->新证据差异：ARKV 以请求/层级重要性和实时预算共同决定压缩、保留与迁移，把资源约束纳入 KV lifecycle。<!-- delta:SF-2026-ARXIV-2603-08727:end -->

边界：只支持 arXiv:2603.08727v1 §IV Methodology 的机制与 §V-D Evaluation Metrics and Benchmarks 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08727:end -->
<!-- books-review:SF-2026-ARXIV-2603-08739:start -->
### Adaptive Multi-Objective Tiered Storage Configuration for KV Cache in LLM Service — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08739:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：KV Cache 是 LLM Serving 的核心状态契约：它以显存换取历史 computation reuse，让 Decode 只推进新位置。容量不足时先保护 prompt/modality 等结构边界，再在剩余预算中选择；换成 linear attention 后，状态形态与 IO pipeline 也必须重新定义，不能继续沿用 token-KV 的身份假设。<!-- existing:SF-2026-ARXIV-2603-08739:end -->

<!-- delta:SF-2026-ARXIV-2603-08739:start -->新证据差异：该系统搜索 Pareto 配置，并依据 KV block access 在线调节分层缓存 eviction 与容量。<!-- delta:SF-2026-ARXIV-2603-08739:end -->

边界：只支持 arXiv:2603.08739v1 §4.1. Overview 的机制与 §5. Evaluation 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08739:end -->
<!-- books-review:SF-2026-ARXIV-2603-08743:start -->
### Zipage: Maintain High Request Concurrency for LLM Reasoning through Compressed PagedAttention — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08743:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：这项优化改变了 KV identity contract。过去只需证明 cache 与当前 request 的 model、token、position 和 layout 相容；跨组件读取还必须绑定：<!-- existing:SF-2026-ARXIV-2603-08743:end -->

<!-- delta:SF-2026-ARXIV-2603-08743:start -->新证据差异：exact-v1 的 `4 Method` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08743:end -->

边界：只支持 arXiv:2603.08743v1 §4 Method 的机制与 §Appendix D Additional Information of Ablation Experiments 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08743:end -->
<!-- books-review:SF-2026-ARXIV-2603-08747:start -->
### Diagnosing FP4 inference: a layer-wise and block-wise sensitivity analysis of NVFP4 and MXFP4 — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08747:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：同步没有消失，而是从全量 readiness barrier 迁移到 buffer generation、memory ordering、validation 和 retry。负载不均会提高误判与重试；额外 buffers 增加 HBM 占用；switch reduction 与 Megakernel integration 也限制了 portability。作者 headline 绑定单节点 8×H200、NVSwitch、TP=8、FP8、ISL=1000、OSL=1000 的端到端配置，16K 只属于输入长度 sensitivity；不能把延迟和吞吐数字外推到跨节点 fabric、较大 batch 或其他 runtime。不支持该 commit protocol 时，传统 collective 仍是更稳健的分支；TP algebra 与 collective 语义回指第 36、37 章，本章只拥有 inference execution commit。<!-- existing:SF-2026-ARXIV-2603-08747:end -->

<!-- delta:SF-2026-ARXIV-2603-08747:start -->新证据差异：exact-v1 的 `3 Experimental Design` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08747:end -->

边界：只支持 arXiv:2603.08747v1 §3 Experimental Design 的机制与 §4 Results 的公开 workload；§5 Conclusion and Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08747:end -->
<!-- books-review:SF-2026-ARXIV-2603-08755:start -->
### Turn: A Language for Agentic Computation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08755:start -->已读 owner `books/part-07-agent/84-agent-platform.md` 与相邻章节。现有命题：只保存消息历史适用于无外部副作用的短会话；工具开始修改文件、启动进程或持有运行时 artifact 后，恢复点必须在 turn boundary 联合提交 conversation、filesystem、process、tool receipt 与 runtime identity。语义稀疏检测可以减少 checkpoint traffic，但会引入 eBPF/分类 false negative、co-location contention 与跨对象 restore consistency。因而平台应把“检测到变化”视为 checkpoint proposal，由可验证的提交清单拥有恢复 authority；检测证据不足时回退到更保守的全量或固定边界 checkpoint。<!-- existing:SF-2026-ARXIV-2603-08755:end -->

<!-- delta:SF-2026-ARXIV-2603-08755:start -->新证据差异：Turn 把 LLM inference、actor mailbox、capability handle 与 schema absorption 提升为语言/VM 原语。<!-- delta:SF-2026-ARXIV-2603-08755:end -->

边界：只支持 arXiv:2603.08755v1 §2.1 Agent Frameworks 的机制与 §10 Evaluation 的公开 workload；§11.1 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08755:end -->
<!-- books-review:SF-2026-ARXIV-2603-08761:start -->
### No Certificate for Alignment: Two Independent Impossibilities and the Pareto Frontier of Achievable Safety Guarantees — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08761:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：即使状态空间无法完整验证，高风险 action 也不应只凭一个“置信度”提交。运行时可以从 observation、Memory 与 tool evidence 构造一组仍 plausible 的 worlds；只有 action 在全部 retained worlds 中满足 safety predicate 时才颁发 commit certificate。若没有可认证 action，先选择低副作用 probe 缩小集合，预算耗尽后 abstain、escalate 或 defer：<!-- existing:SF-2026-ARXIV-2603-08761:end -->

<!-- delta:SF-2026-ARXIV-2603-08761:start -->新证据差异：exact-v1 的 `3 Formal Framework` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08761:end -->

边界：只支持 arXiv:2603.08761v1 §3 Formal Framework 的机制与 §Evaluation 的公开 workload；§8 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08761:end -->
<!-- books-review:SF-2026-ARXIV-2603-08797:start -->
### Serving Compound Inference Systems on Datacenter GPUs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08797:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：compound inference 的 graph、model variant、replica 与 spatial partition 必须在同一端到端 SLO contract 下决策。<!-- existing:SF-2026-ARXIV-2603-08797:end -->

<!-- delta:SF-2026-ARXIV-2603-08797:start -->新证据差异：JigsawServe 注册 task graph、model variants 与 SLO，profile variant×batch×MIG/MPS 配置，再由 MILP controller 选择 variant、replica 与 spatial partition。<!-- delta:SF-2026-ARXIV-2603-08797:end -->

边界：只支持 arXiv:2603.08797v1 §3.1–§3.3 的 graph/variant/profile/MILP configuration 与 §4–§5 的公开 workload；不支持 runtime dependency frontier 或 intermediate-artifact residency。已写回，等待非作者复核。
<!-- books-review:SF-2026-ARXIV-2603-08797:end -->
<!-- books-review:SF-2026-ARXIV-2603-08806:start -->
### Test-Driven AI Agent Definition (TDAD): Compiling Tool-Using Agents from Behavioral Specifications — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08806:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-08806:end -->

<!-- delta:SF-2026-ARXIV-2603-08806:start -->新证据差异：exact-v1 的 `3 The TDAD Methodology` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08806:end -->

边界：只支持 arXiv:2603.08806v1 §3 The TDAD Methodology 的机制与 §6 Experimental Results 的公开 workload；§8 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08806:end -->
<!-- books-review:SF-2026-ARXIV-2603-08835:start -->
### MASEval: Extending Multi-Agent Evaluation from Models to Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08835:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-08835:end -->

<!-- delta:SF-2026-ARXIV-2603-08835:start -->新证据差异：exact-v1 的 `3.2 Module Architecture` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08835:end -->

边界：只支持 arXiv:2603.08835v1 §3.2 Module Architecture 的机制与 §4.2 Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08835:end -->
<!-- books-review:SF-2026-ARXIV-2603-08852:start -->
### LDP: An Identity-Aware Protocol for Multi-Agent LLM Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08852:start -->已读 owner `books/part-07-agent/83-mcp.md` 与相邻章节。现有命题：在 server 数量少、由同一团队静态安装时，固定 allowlist、TLS endpoint 与 package review 足以建立初始信任；开放 catalog 或第三方 MCP server 动态加入后，连接成功和 OAuth scope 只能证明通信/委托成立，不能证明眼前 server identity、tool set、sensitivity 声明和受审 artifact 与批准对象相同。Host admission plane 应在注册时验证 server identity、tool allowlist、sensitivity metadata、attestation root 与 conformance vector，并把验证结果绑定到 protocol/version；effect-time authorization 仍按 principal、参数和业务 policy 独立执行。<!-- existing:SF-2026-ARXIV-2603-08852:end -->

<!-- delta:SF-2026-ARXIV-2603-08852:start -->新证据差异：LDP 把 identity card、payload negotiation、session state、provenance 与 trust domain写入协议。<!-- delta:SF-2026-ARXIV-2603-08852:end -->

边界：只支持 arXiv:2603.08852v1 §5.6 Statistical Methodology 的机制与 §5.4 LLM-as-Judge Evaluation 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08852:end -->
<!-- books-review:SF-2026-ARXIV-2603-08960:start -->
### The $qs$ Inequality: Quantifying the Double Penalty of Mixture-of-Experts at Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08960:start -->已读 owner `books/part-02-model/21-moe.md` 与相邻章节。现有命题：第 20 章已经闭合从 logits 到 next token 的生成主干。本章不是 Sampling 后新增一个执行阶段，而是回到第 16 章的 MLP 子层：保持 Transformer Layer 的外部 shape contract 不变，只替换其中的容量组织方式。<!-- existing:SF-2026-ARXIV-2603-08960:end -->

<!-- delta:SF-2026-ARXIV-2603-08960:start -->新证据差异：exact-v1 的 `4 Evaluation Methodology` 把论文方案定位到 expert 选择、capacity、placement 与通信；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08960:end -->

边界：只支持 arXiv:2603.08960v1 §4 Evaluation Methodology 的机制与 §4 Evaluation Methodology 的公开 workload；§7 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08960:end -->
<!-- books-review:SF-2026-ARXIV-2603-09023:start -->
### The Missing Memory Hierarchy: Demand Paging for LLM Context Windows — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09023:start -->已读 owner `books/part-07-agent/75-context.md` 与相邻章节。现有命题：Context 是从 backing state 选择出的运行时 working set，驱逐与恢复必须保留可寻址身份。<!-- existing:SF-2026-ARXIV-2603-09023:end -->

<!-- delta:SF-2026-ARXIV-2603-09023:start -->新证据差异：Pichay 在 Messages API 层驱逐或压缩消息/工具结果，以 retrieval handle、重复读取 fault 和 path/hash pinning 恢复 prompt working set；它不管理 KV tensor residency。<!-- delta:SF-2026-ARXIV-2603-09023:end -->

边界：只支持 arXiv:2603.09023v1 §3 与 §5 的 L1/L2；L3 未规模评测、L4 仅接口，不外推为 KV/HBM paging。已重路由 Ch75 并等待非作者复核。
<!-- books-review:SF-2026-ARXIV-2603-09023:end -->
<!-- books-review:SF-2026-ARXIV-2603-09046:start -->
### FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09046:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：LLM request 的 KV footprint 会随未知输出长度增长。因此 admission 只检查“现在还有 blocks”可能 接受一组稍后必然不可行的 requests。更强的不变量是：在明确的 output estimate、preemption 和 reserve 假设下，当前选择之后的 future KV growth 仍有可行路径。<!-- existing:SF-2026-ARXIV-2603-09046:end -->

<!-- delta:SF-2026-ARXIV-2603-09046:start -->新证据差异：exact-v1 的 `3.3 System Overview` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09046:end -->

边界：只支持 arXiv:2603.09046v1 §3.3 System Overview 的机制与 §7.2 Micro-benchmarks 的公开 workload；§2.2 ARM TrustZone and Its Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09046:end -->
<!-- books-review:SF-2026-ARXIV-2603-09079:start -->
### GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09079:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：模型能识别物体、理解指令并生成动作 token，为什么还不等于机器人系统？VLA 是把 “A” 接到 VLM 后面，还是改变了训练与 runtime contract？大模型推理慢、控制频率高时如何分层？video generation 形成的动作想象能否直接执行？<!-- existing:SF-2026-ARXIV-2603-09079:end -->

<!-- delta:SF-2026-ARXIV-2603-09079:start -->新证据差异：exact-v1 的 `III Method` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09079:end -->

边界：只支持 arXiv:2603.09079v1 §III Method 的机制与 §IV-B Main Results 的公开 workload；§IV-D4 Failure Cases 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09079:end -->
<!-- books-review:SF-2026-ARXIV-2603-09086:start -->
### Latent World Models for Automated Driving: A Unified Taxonomy, Evaluation Framework, and Open Challenges — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09086:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-09086:end -->

<!-- delta:SF-2026-ARXIV-2603-09086:start -->新证据差异：exact-v1 的 `III INTERNAL MECHANICS: STRUCTURE, ALIGNMENT, AND DYNAMICS IN LATENT REPRESENTATIONS` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09086:end -->

边界：只支持 arXiv:2603.09086v1 §III INTERNAL MECHANICS: STRUCTURE, ALIGNMENT, AND DYNAMICS IN LATENT REPRESENTATIONS 的机制与 §IV-C Toward Unified Latent-Centric Evaluation Metrics 的公开 workload；§VII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09086:end -->
<!-- books-review:SF-2026-ARXIV-2603-09117:start -->
### Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09117:start -->已读 owner `books/part-04-training-system/33-grpo.md` 与相邻章节。现有命题：《Reinforcement Learning for Code Optimization》在 code timing 场景中系统化展示了这条 路径，并报告 naive timing reward 会被 noise、sparsity 与 GRPO instability 淹没。其具体 数据集、reward recipe 与收益仍是单篇预印本的实验结论；本章吸收的长期原则是： **verifiable reward 的测量系统也是被优化接口，必须与 policy 一起设计和审计。**<!-- existing:SF-2026-ARXIV-2603-09117:end -->

<!-- delta:SF-2026-ARXIV-2603-09117:start -->新证据差异：exact-v1 的 `2.4 Calibration Optimization Methods` 把论文方案定位到 prompt、rollout、group advantage 与 on-policy freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09117:end -->

边界：只支持 arXiv:2603.09117v1 §2.4 Calibration Optimization Methods 的机制与 §6.2 Overall Results 的公开 workload；§6.3 Ablation Studies 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09117:end -->
<!-- books-review:SF-2026-ARXIV-2603-09121:start -->
### DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09121:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：较少可训练状态换来样本效率和可回滚性，却可能让 token 成为信息瓶颈、让 anchor 阻碍必要适应，或在 contact-rich phase 产生危险探索。作者证据限于几小时实践和四项真实机器人任务，并依赖上述 human-in-the-loop contract，不支持通用 online-RL 保证；任务需要表征重写时仍需更广 fine-tuning，安全证据不足时回退 frozen policy、离线数据或人工接管。<!-- existing:SF-2026-ARXIV-2603-09121:end -->

<!-- delta:SF-2026-ARXIV-2603-09121:start -->新证据差异：exact-v1 的 `III Method` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09121:end -->

边界：只支持 arXiv:2603.09121v1 §III Method 的机制与 §IV EXPERIMENTS 的公开 workload；§V CONCLUSION AND FUTURE WORK 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09121:end -->
<!-- books-review:SF-2026-ARXIV-2603-09127:start -->
### Collective AI can amplify tiny perturbations into divergent decisions — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09127:start -->已读 owner `books/part-07-agent/82-multi-agent.md` 与相邻章节。现有命题：本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**<!-- existing:SF-2026-ARXIV-2603-09127:end -->

<!-- delta:SF-2026-ARXIV-2603-09127:start -->新证据差异：exact-v1 的 `Two design routes and non-additive interaction` 把论文方案定位到 agent identity、委托边、消息状态、协作协议与冲突处理；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09127:end -->

边界：只支持 arXiv:2603.09127v1 §Two design routes and non-additive interaction 的机制与 §S4.3 Results 的公开 workload；§Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09127:end -->
<!-- books-review:SF-2026-ARXIV-2603-09157:start -->
### Real-Time Trust Verification for Safe Agentic Actions using TrustBench — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09157:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：Refinement 只能重组已有 evidence，不能从缺失知识中创造可靠 procedure；失败还可能低于 no-Skill baseline。 Agentic Skills in the Wild 的作者结果支持这一分层，不支持固定模型排名或特定 registry size 的通用结论。<!-- existing:SF-2026-ARXIV-2603-09157:end -->

<!-- delta:SF-2026-ARXIV-2603-09157:start -->新证据差异：exact-v1 的 `Dual-Mode Architecture` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09157:end -->

边界：只支持 arXiv:2603.09157v1 §Dual-Mode Architecture 的机制与 §Evaluation 的公开 workload；§Component Ablation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09157:end -->
<!-- books-review:SF-2026-ARXIV-2603-09180:start -->
### DuplexCascade: Full-Duplex Speech-to-Speech Dialogue with VAD-Free Cascaded ASR-LLM-TTS Pipeline and Micro-Turn Optimization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09180:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：联合优化可以在低带宽环境减少通信暴露，却把 host CPU memory、压缩/解压、dynamic-program cost、拓扑漂移和故障恢复带进 serving contract。高带宽同构集群、KV offload 反而更慢、压缩收益不足或 topology/SLO 无法准确建模时，固定 placement 与普通 pipeline 仍更可验证。论文结果只绑定其 internet-scale testbed、模型和公开配置，不证明通用去中心化服务优势。<!-- existing:SF-2026-ARXIV-2603-09180:end -->

<!-- delta:SF-2026-ARXIV-2603-09180:start -->新证据差异：exact-v1 的 `4.1 Implementation Details` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09180:end -->

边界：只支持 arXiv:2603.09180v1 §4.1 Implementation Details 的机制与 §4.2 Full-Duplex-Bench Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09180:end -->
<!-- books-review:SF-2026-ARXIV-2603-09192:start -->
### Explainable Innovation Engine: Dual-Tree Agent-RAG with Methods-as-Nodes and Verifiable Write-Back — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09192:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-09192:end -->

<!-- delta:SF-2026-ARXIV-2603-09192:start -->新证据差异：exact-v1 的 `3 Methods` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09192:end -->

边界：只支持 arXiv:2603.09192v1 §3 Methods 的机制与 §2.2 Retrieval Strategy, Reflection, and Evaluation 的公开 workload；§4.5 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09192:end -->
<!-- books-review:SF-2026-ARXIV-2603-09216:start -->
### PIM-SHERPA: Software Method for On-device LLM Inference by Resolving PIM Memory Attribute and Layout Inconsistencies — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09216:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这用更灵活的 occupancy 和 latency hiding 换 runtime scheduler、context/state storage、fairness、deadlock diagnosis 与 架构耦合；虚拟资源数量过大也可能制造 metadata 和 contention。规则 GEMM、graph capture 已稳定或 runtime 无法证明 suspend/resume state 时，固定硬件调度仍更容易验证。VDCores 的 exact-v1 结果绑定其四类 LLM inference workload 与 GH200/H100/RTX 6000 Pro 环境；本章只吸收 resource binding 变成 runtime decision 的机制，不外推 headline 吞吐。<!-- existing:SF-2026-ARXIV-2603-09216:end -->

<!-- delta:SF-2026-ARXIV-2603-09216:start -->新证据差异：exact-v1 的 `2.2 LPDDR-PIM architecture` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09216:end -->

边界：只支持 arXiv:2603.09216v1 §2.2 LPDDR-PIM architecture 的机制与 §6 Evaluation 的公开 workload；§3.2 Current solutions and limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09216:end -->
<!-- books-review:SF-2026-ARXIV-2603-09221:start -->
### Beyond Test-Time Memory: State-Space Optimal Control for LLM Reasoning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09221:start -->已读 owner `books/part-07-agent/79-planning.md` 与相邻章节。现有命题：Planner 拥有分解与 dependency graph，executor 只拥有被授予的 task，Workflow 才拥有 durable commit/retry。 Contract 过细会压制探索，过粗则重新引入 overlap；LLM judge 对 coherence 的评分也不能替代 artifact integration。 Project2Task 的 10 个 research briefs 只为该编译结构提供实验性证据，不证明一般科研质量。单人任务、强耦合探索 或目标仍高度不确定时，共享 working session 与少量人工 milestone 仍比过早 taskization 更合理。<!-- existing:SF-2026-ARXIV-2603-09221:end -->

<!-- delta:SF-2026-ARXIV-2603-09221:start -->新证据差异：exact-v1 的 `3.3 Hardware Co-Design for TTC` 把论文方案定位到 计划路由、证据需求与停止条件；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09221:end -->

边界：只支持 arXiv:2603.09221v1 §3.3 Hardware Co-Design for TTC 的机制与 §Benchmark Evaluation. 的公开 workload；§Limitations and Future Works. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09221:end -->
<!-- books-review:SF-2026-ARXIV-2603-09241:start -->
### RAE-NWM: Navigation World Model in Dense Visual Representation Space — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09241:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：现有证据给出了 environment、agent 与 joint channel 的形式化恒等式、support restriction 及有限 POMDP 示例；它澄清了 representation identity，却不是 learned world model 的开放世界经验性证明。工程上仍需用 action-conditioned outcome、counterfactual coverage 和 calibration 分别验证各 channel。<!-- existing:SF-2026-ARXIV-2603-09241:end -->

<!-- delta:SF-2026-ARXIV-2603-09241:start -->新证据差异：exact-v1 的 `Representation Space and Architecture.` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09241:end -->

边界：只支持 arXiv:2603.09241v1 §Representation Space and Architecture. 的机制与 §Evaluation Metrics. 的公开 workload；§6 Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09241:end -->
<!-- books-review:SF-2026-ARXIV-2603-09290:start -->
### ToolRosella: Translating Code Repositories into Standardized Tools for Scientific Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09290:start -->已读 owner `books/part-07-agent/78-tool-calling.md` 与相邻章节。现有命题：这是并存的 interface branches，不是单向升级。平台应根据 task risk、operation coverage、request volume 与 auditability 选择最窄且足够表达的 surface，并保持 canonical action、authorization 和 effect identity 不变。 Terminal Agents 的受限实验说明部分 enterprise gap 来自 interface granularity，不证明 shell 比 MCP、domain API 或 browser 普遍更好；benchmark sandbox、模型、tool catalog 与成本条件变化都会改变结论。<!-- existing:SF-2026-ARXIV-2603-09290:end -->

<!-- delta:SF-2026-ARXIV-2603-09290:start -->新证据差异：exact-v1 的 `4 Methods` 把论文方案定位到 tool identity、argument validation、authorization、receipt 与 side-effect commit；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09290:end -->

边界：只支持 arXiv:2603.09290v1 §4 Methods 的机制与 §2.4.1 Case 1: Stroke Analysis 的公开 workload；§3.1 Contributions and limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09290:end -->
<!-- books-review:SF-2026-ARXIV-2603-09297:start -->
### TA-Mem: Tool-Augmented Autonomous Memory Retrieval for LLM in Long-Term Conversational QA — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09297:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-09297:end -->

<!-- delta:SF-2026-ARXIV-2603-09297:start -->新证据差异：exact-v1 的 `III. METHODOLOGY` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09297:end -->

边界：只支持 arXiv:2603.09297v1 §III. METHODOLOGY 的机制与 §Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09297:end -->
<!-- books-review:SF-2026-ARXIV-2603-09435:start -->
### AI Act Evaluation Benchmark: An Open, Transparent, and Reproducible Evaluation Dataset for NLP and RAG Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09435:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：为什么训练 loss、benchmark 分数、用户点赞和系统 SLO 都不能单独证明一个 AI System “更好”？Evaluation 应评估模型、完整请求路径，还是 Agent trajectory？离线评估、线上实验与生产反馈怎样形成一个可审计的发布控制回路？<!-- existing:SF-2026-ARXIV-2603-09435:end -->

<!-- delta:SF-2026-ARXIV-2603-09435:start -->新证据差异：exact-v1 的 `3.2 Methodology` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09435:end -->

边界：只支持 arXiv:2603.09435v1 §3.2 Methodology 的机制与 §Evaluation 的公开 workload；§6 Conclusions & Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09435:end -->
<!-- books-review:SF-2026-ARXIV-2603-09453:start -->
### Variational Routing: A Scalable Bayesian Framework for Calibrated Mixture-of-Experts Transformers — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09453:start -->已读 owner `books/part-02-model/21-moe.md` 与相邻章节。现有命题：标准 MoE 在 `d_model` 维 token state 上 routing、dispatch 和 expert compute。增加 experts 可以扩大总容量，但每个 assignment 搬运的 payload 仍与 hidden width 绑定；当 All-to-All bytes 或低延迟下的 expert weight load 成为瓶颈时，仅继续增加 experts/top-k 会放大系统压力。<!-- existing:SF-2026-ARXIV-2603-09453:end -->

<!-- delta:SF-2026-ARXIV-2603-09453:start -->新证据差异：exact-v1 的 `Methodology` 把论文方案定位到 expert 选择、capacity、placement 与通信；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09453:end -->

边界：只支持 arXiv:2603.09453v1 §Methodology 的机制与 §5 Experiments 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09453:end -->
<!-- books-review:SF-2026-ARXIV-2603-09488:start -->
### Streaming Autoregressive Video Generation via Diagonal Distillation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09488:start -->已读 owner `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节。现有命题：这里的 plan 是 provisional control state，不是模型已经正确理解约束的证明；validator 也必须拥有版本、阈值、 false-positive/false-negative 与覆盖范围。Retry 若复用同一错误 plan 只会重复失败，若完全重建则增加 latency、 compute 和 output variance；streaming 一旦播放前缀，rollback boundary 还会变成用户可见协议。小模型、低风险、 严格 latency 或 validator 不可靠时，direct generation 与简单 post-filter 仍然成立。<!-- existing:SF-2026-ARXIV-2603-09488:end -->

<!-- delta:SF-2026-ARXIV-2603-09488:start -->新证据差异：exact-v1 的 `H.2 Evaluation Methodology` 把论文方案定位到 生成顺序、proposal/correction 与终止状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09488:end -->

边界：只支持 arXiv:2603.09488v1 §H.2 Evaluation Methodology 的机制与 §4.4 Long Video Generation Evaluation 的公开 workload；§4.3 Ablation Studies 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09488:end -->
<!-- books-review:SF-2026-ARXIV-2603-09513:start -->
### Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation in Non-Markovian Simulation Benchmarks — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09513:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：deployment owner 持有生效 revision，teleoperation/intervention service 持有接管事实，training run 只产生 candidate policy，controller 与 safety monitor 仍拥有动作提交和 veto。该循环获得更贴近失败前沿的数据，却引入 on-policy exploration risk、选择偏差、版本碎片和旧能力退化；干预稀疏、奖励不可信或物理 blast radius 无法隔离时，应停在离线更新、simulation/shadow evaluation 和人工审批，不把“来自真实 fleet”误写成安全证明。<!-- existing:SF-2026-ARXIV-2603-09513:end -->

<!-- delta:SF-2026-ARXIV-2603-09513:start -->新证据差异：exact-v1 的 `LLM-Aided Lock Design` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09513:end -->

边界：只支持 arXiv:2603.09513v1 §LLM-Aided Lock Design 的机制与 §Main Results 的公开 workload；§Possible Causes of Remaining Failures 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09513:end -->
<!-- books-review:SF-2026-ARXIV-2603-09555:start -->
### Compiler-First State Space Duality and Portable $O(1)$ Autoregressive Caching for Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09555:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：候选来源还可以更轻：不训练独立 drafter，也不新增原生 MTP head，而是从 target model 的 hidden state 在 embedding space 探测未来 token，再交给 target exact verification。它把 proposal-source 演进补成三条并列分支：<!-- existing:SF-2026-ARXIV-2603-09555:end -->

<!-- delta:SF-2026-ARXIV-2603-09555:start -->新证据差异：Compiler-First State Space Duality 从算子语义推导等价 recurrent form，再由编译器生成固定大小的 autoregressive state 与更新程序。<!-- delta:SF-2026-ARXIV-2603-09555:end -->

边界：只支持 arXiv:2603.09555v1 §3、§4.2–§4.3 和 §5.2–§5.7 的公开实现与验证；§5.8 之外不主张形式化等价证明或跨后端通用性。写回已完成，等待非作者 post-write 复核。
<!-- books-review:SF-2026-ARXIV-2603-09555:end -->
<!-- books-review:SF-2026-ARXIV-2603-09619:start -->
### Context Engineering: From Prompts to Corporate Multi-Agent Architecture — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09619:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。 ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。 StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。<!-- existing:SF-2026-ARXIV-2603-09619:end -->

<!-- delta:SF-2026-ARXIV-2603-09619:start -->新证据差异：exact-v1 的 `6. Context Engineering as a Design Object` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09619:end -->

边界：只支持 arXiv:2603.09619v1 §6. Context Engineering as a Design Object 的机制与 §Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09619:end -->
<!-- books-review:SF-2026-ARXIV-2603-09657:start -->
### When to Lock Attention: Training-Free KV Control in Video Diffusion — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09657:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：Full-context KV 把每个源 token 对应的派生表示都保留下来，最容易解释和回退；简单 token sampling 则默认“删除源 token 就删除了它的语义贡献”。Contextualized KV 打破了这个直觉：下游位置已经通过 attention 汇聚上游 observation， 因此一个被保留的 downstream row 可能仍携带某个已省略 event 的信息。稀疏 materialization 的对象于是从 token subset 演进为 **derived-state interface**：<!-- existing:SF-2026-ARXIV-2603-09657:end -->

<!-- delta:SF-2026-ARXIV-2603-09657:start -->新证据差异：exact-v1 的 `B.1 Implementation Details` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09657:end -->

边界：只支持 arXiv:2603.09657v1 §B.1 Implementation Details 的机制与 §5.2 Results 的公开 workload；§6 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09657:end -->
<!-- books-review:SF-2026-ARXIV-2603-09692:start -->
### ActiveUltraFeedback: Efficient Preference Data Generation using Active Learning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09692:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2603-09692:end -->

<!-- delta:SF-2026-ARXIV-2603-09692:start -->新证据差异：exact-v1 的 `D.1 Scoring Methodology` 把论文方案定位到 rollout、reward、policy/reference 与更新 freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09692:end -->

边界：只支持 arXiv:2603.09692v1 §D.1 Scoring Methodology 的机制与 §5 Evaluation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09692:end -->
<!-- books-review:SF-2026-ARXIV-2603-09716:start -->
### AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09716:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-09716:end -->

<!-- delta:SF-2026-ARXIV-2603-09716:start -->新证据差异：exact-v1 的 `3 The AutoAgent Framework: A Unified Architecture for Self-Evolution` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09716:end -->

边界：只支持 arXiv:2603.09716v1 §3 The AutoAgent Framework: A Unified Architecture for Self-Evolution 的机制与 §8 Experiments and Evaluation 的公开 workload；§9 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09716:end -->
<!-- books-review:SF-2026-ARXIV-2603-09730:start -->
### WVA: A Global Optimization Control Plane for llmd — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09730:start -->已读 owner `books/part-06-ai-infrastructure/63-gpu-scheduler.md` 与相邻章节。现有命题：本章的核心判断是：**GPU scheduling 是受硬约束的多维 placement 与时间分配问题。先保证设备、拓扑和 gang 可行，再在 queue、fairness、utilization 和 SLO 之间优化；任何单一利用率指标都会丢失关键约束。**第 36 章说明 collective algorithm 必须映射到真实 topology；本章从控制面回答 scheduler 怎样为这种映射保留可行的 device、node、switch 与 failure-domain placement。<!-- existing:SF-2026-ARXIV-2603-09730:end -->

<!-- delta:SF-2026-ARXIV-2603-09730:start -->新证据差异：WVA 与 llm-d 联合使用 engine saturation、headroom 和 fragmentation 状态做 variant-aware 扩缩。<!-- delta:SF-2026-ARXIV-2603-09730:end -->

边界：只支持 arXiv:2603.09730v1 §IV-B Design Rationale: Why Pluggability? 的机制与 §V-D Physical Cluster Validation 的公开 workload；§VII Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09730:end -->
<!-- books-review:SF-2026-ARXIV-2603-09756:start -->
### Epistemic Closure: Autonomous Mechanism Completion for Physically Consistent Simulation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09756:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-09756:end -->

<!-- delta:SF-2026-ARXIV-2603-09756:start -->新证据差异：exact-v1 的 `4 Methodology` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09756:end -->

边界：只支持 arXiv:2603.09756v1 §4 Methodology 的机制与 §2 Results 的公开 workload；§3 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09756:end -->
<!-- books-review:SF-2026-ARXIV-2603-09821:start -->
### One-Eval: An Agentic System for Automated and Traceable LLM Evaluation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09821:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-09821:end -->

<!-- delta:SF-2026-ARXIV-2603-09821:start -->新证据差异：exact-v1 的 `3.1 Framework Overview` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09821:end -->

边界：只支持 arXiv:2603.09821v1 §3.1 Framework Overview 的机制与 §4 Experiments 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09821:end -->
<!-- books-review:SF-2026-ARXIV-2603-09877:start -->
### InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09877:start -->已读 owner `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节。现有命题：这让 exploration 成为除模型规模和每样本计算之外的第三条训练计算轴，但没有创造更可靠的 ground truth。候选数增加 会线性或超线性放大生成与筛选成本，选择器偏差还会把某种 mode 固化成训练偏好。固定单匹配在数据近单峰、预算紧或 scorer 不可信时仍合理；多候选探索只在候选多样性、selection contract 和单位训练预算收益一起验证时成立。作者的 受限 scaling curve 不能证明它会普遍替代 AR、diffusion 或 masked generation，只说明 training-time sampling policy 本身也需要被版本化和计量。<!-- existing:SF-2026-ARXIV-2603-09877:end -->

<!-- delta:SF-2026-ARXIV-2603-09877:start -->新证据差异：exact-v1 的 `3.1.1 Overall Design Principles` 把论文方案定位到 生成顺序、proposal/correction 与终止状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09877:end -->

边界：只支持 arXiv:2603.09877v1 §3.1.1 Overall Design Principles 的机制与 §A.2.2 Evaluation Metrics 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09877:end -->
<!-- books-review:SF-2026-ARXIV-2603-09891:start -->
### Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09891:start -->已读 owner `books/part-07-agent/76-rag.md` 与相邻章节。现有命题：本章的核心判断是：**RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。**<!-- existing:SF-2026-ARXIV-2603-09891:end -->

<!-- delta:SF-2026-ARXIV-2603-09891:start -->新证据差异：exact-v1 的 `2 Task Setup` 把论文方案定位到 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09891:end -->

边界：只支持 arXiv:2603.09891v1 §2 Task Setup 的机制与 §3.3 Support Evaluation 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09891:end -->
<!-- books-review:SF-2026-ARXIV-2603-09892:start -->
### MSSR: Memory-Aware Adaptive Replay for Continual LLM Fine-Tuning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09892:start -->已读 owner `books/part-02-model/22-long-context.md` 与相邻章节。现有命题：这会让训练目标更贴近 state lifetime，却增加 delayed credit、跨 chunk replay、reset boundary 和 online update cost。 同一 sequence 不同 prefix 的 relative reward 也不等于原始 same-prompt GRPO；normalization population、state version 与使用窗口必须写入 objective identity。短状态或写入作用可立即验证时，local loss 仍是更稳定的旧方案。<!-- existing:SF-2026-ARXIV-2603-09892:end -->

<!-- delta:SF-2026-ARXIV-2603-09892:start -->新证据差异：exact-v1 的 `Framework Overview.` 把论文方案定位到 上下文选择、层次化表示和可访问记忆的语义边界；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-09892:end -->

边界：只支持 arXiv:2603.09892v1 §Framework Overview. 的机制与 §4.2 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09892:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260311-COVERAGE | fresh-context:march-lane-a-reviewer | coverage | coverage:SRC-ARXIV:20260311 | MAR26-FC-001/MAR26-FC-002/MAR26-FC-003 | pending: full-row fresh-context false-positive/false-negative replay; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260311-EVIDENCE | fresh-context:march-lane-a-reviewer | evidence | review:SF-2026-ARXIV-2603-08727; review:SF-2026-ARXIV-2603-08739; review:SF-2026-ARXIV-2603-08743; review:SF-2026-ARXIV-2603-08747; review:SF-2026-ARXIV-2603-08755; review:SF-2026-ARXIV-2603-08761; review:SF-2026-ARXIV-2603-08797; review:SF-2026-ARXIV-2603-08806; review:SF-2026-ARXIV-2603-08835; review:SF-2026-ARXIV-2603-08852; review:SF-2026-ARXIV-2603-08960; review:SF-2026-ARXIV-2603-09023; review:SF-2026-ARXIV-2603-09046; review:SF-2026-ARXIV-2603-09079; review:SF-2026-ARXIV-2603-09086; review:SF-2026-ARXIV-2603-09117; review:SF-2026-ARXIV-2603-09121; review:SF-2026-ARXIV-2603-09127; review:SF-2026-ARXIV-2603-09157; review:SF-2026-ARXIV-2603-09180; review:SF-2026-ARXIV-2603-09192; review:SF-2026-ARXIV-2603-09216; review:SF-2026-ARXIV-2603-09221; review:SF-2026-ARXIV-2603-09241; review:SF-2026-ARXIV-2603-09290; review:SF-2026-ARXIV-2603-09297; review:SF-2026-ARXIV-2603-09435; review:SF-2026-ARXIV-2603-09453; review:SF-2026-ARXIV-2603-09488; review:SF-2026-ARXIV-2603-09513; review:SF-2026-ARXIV-2603-09555; review:SF-2026-ARXIV-2603-09619; review:SF-2026-ARXIV-2603-09657; review:SF-2026-ARXIV-2603-09692; review:SF-2026-ARXIV-2603-09716; review:SF-2026-ARXIV-2603-09730; review:SF-2026-ARXIV-2603-09756; review:SF-2026-ARXIV-2603-09821; review:SF-2026-ARXIV-2603-09877; review:SF-2026-ARXIV-2603-09891; review:SF-2026-ARXIV-2603-09892 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260311-SELECTION | fresh-context:march-lane-a-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | MAR26-FC-004 | pending: recompute after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260311-BOOKS | fresh-context:march-lane-a-reviewer | books | validator:books-comparison-v1 | MAR26-FC-004 | pending: recheck disposition after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260311/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 3 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 3 项 Books Integration：
- 更新并复核 `books/part-05-inference-system/49-tensorrt-llm.md`。
- 更新并复核 `books/part-05-inference-system/56-inference-scheduling.md`。
- 更新并复核 `books/part-07-agent/75-context.md`。
- 未修改 Weekly；未 stage、commit 或 push。

## 11. Open Questions

- 未解决语义 finding=4（`MAR26-FC-001 / MAR26-FC-002 / MAR26-FC-003 / MAR26-FC-004`）；blocked / unverified / disputed 仍为 0。
- 论文自身未证明边界保留在各 Source Review 的 Claim Boundary 中；它们不是本次流程 pending。

## 12. Sources

- [arXiv](https://arxiv.org/) — exact-v1 primary manuscript and status。
- DataCite March frozen snapshot — identity/title/abstract/submission provenance only。

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


## 13. Final Status

- Completion Status: `In Progress`
- Coverage: `Open`
- Evidence: `Open`
- Books: `Open`
- unresolved findings: 4（`MAR26-FC-001 / MAR26-FC-002 / MAR26-FC-003 / MAR26-FC-004`）
