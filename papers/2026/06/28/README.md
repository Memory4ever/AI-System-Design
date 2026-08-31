# Daily Research — 2026-06-28

**Research Date:** 2026-06-28

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-27 09:00:00 ～ 2026-06-28 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 状态见第 7 节

## Executive Summary
北京时间窗口 `[2026-06-27 09:00, 2026-06-28 09:00)` 共 211 个注册 identity。全量 title+abstract 语义筛选冻结 211 = 65 retained + 146 family-specific closures；65/65 exact-v1 resolved（64 official HTML，1 version-stamped mirror cross-check），pending=0。最新 owner+adjacent 语义重审得到 6 Integrate、42 No Change 与 17 Weekly Only，合并为 6 个 owner 写入；root 已串行完成 6-family 写回，65/65 post-write fresh audit 通过。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-28 |
| Window End | 2026-06-28 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-v2.1:2026-06-28:20c51e943aacc58d |
| Denominator Frozen At | 2026-08-29T06:45:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-27T09:00:00+08:00 | 2026-06-28T09:00:00+08:00 | 2026-08-29T21:20:00+08:00 | frozen registered snapshots; exact UTC window; all categories | checked | 211 | SF-2026-ARXIV-2606-28666; SF-2026-ARXIV-2606-28679; SF-2026-ARXIV-2606-28690; SF-2026-ARXIV-2606-28692; SF-2026-ARXIV-2606-28707; SF-2026-ARXIV-2606-28712; SF-2026-ARXIV-2606-28715; SF-2026-ARXIV-2606-28720; SF-2026-ARXIV-2606-28725; SF-2026-ARXIV-2606-28733; SF-2026-ARXIV-2606-28739; SF-2026-ARXIV-2606-28747; SF-2026-ARXIV-2606-28751; SF-2026-ARXIV-2606-28754; SF-2026-ARXIV-2606-28757; SF-2026-ARXIV-2606-28758; SF-2026-ARXIV-2606-28772; SF-2026-ARXIV-2606-28781; SF-2026-ARXIV-2606-28804; SF-2026-ARXIV-2606-28813; SF-2026-ARXIV-2606-28831; SF-2026-ARXIV-2606-28839; SF-2026-ARXIV-2606-28841; SF-2026-ARXIV-2606-28843; SF-2026-ARXIV-2606-28862; SF-2026-ARXIV-2606-28863; SF-2026-ARXIV-2606-28864; SF-2026-ARXIV-2606-28867; SF-2026-ARXIV-2606-28876; SF-2026-ARXIV-2606-28896; SF-2026-ARXIV-2606-28898; SF-2026-ARXIV-2606-28900; SF-2026-ARXIV-2606-28925; SF-2026-ARXIV-2606-28932; SF-2026-ARXIV-2606-28938; SF-2026-ARXIV-2606-28939; SF-2026-ARXIV-2606-28953; SF-2026-ARXIV-2606-28955; SF-2026-ARXIV-2606-28958; SF-2026-ARXIV-2606-28962; SF-2026-ARXIV-2606-28995; SF-2026-ARXIV-2606-28998; SF-2026-ARXIV-2606-29013; SF-2026-ARXIV-2606-29030; SF-2026-ARXIV-2606-29033; SF-2026-ARXIV-2606-29038; SF-2026-ARXIV-2606-29054; SF-2026-ARXIV-2606-29059; SF-2026-ARXIV-2606-29066; SF-2026-ARXIV-2606-29067; SF-2026-ARXIV-2606-29073; SF-2026-ARXIV-2606-29082; SF-2026-ARXIV-2606-29088; SF-2026-ARXIV-2606-29089; SF-2026-ARXIV-2606-29090; SF-2026-ARXIV-2606-29091; SF-2026-ARXIV-2606-29094; SF-2026-ARXIV-2606-29097; SF-2026-ARXIV-2606-29108; SF-2026-ARXIV-2606-29112; SF-2026-ARXIV-2606-29116; SF-2026-ARXIV-2606-29119; SF-2026-ARXIV-2606-29124; SF-2026-ARXIV-2606-29126; SF-2026-ARXIV-2606-29129 | pages=40; final_cursor=end | 2026-06-28T01:00:00Z | ../_sources/daily-20260628/screening-ledger.json; ../_sources/daily-20260628/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260628 | — |

<!-- coverage:SRC-ARXIV:20260628:start -->
Full-population reconciliation: 211 = 65 + 146; full title+abstract screen and route-negative false-negative audit completed before denominator freeze.
<!-- coverage:SRC-ARXIV:20260628:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-28666 | arXiv:2606.28666v1 | paper-v1:2606.28666 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-28666 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28666 | yes |
| SF-2026-ARXIV-2606-28679 | arXiv:2606.28679v1 | paper-v1:2606.28679 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-28679 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28679 | yes |
| SF-2026-ARXIV-2606-28690 | arXiv:2606.28690v1 | paper-v1:2606.28690 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28690 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2606-28690 | yes |
| SF-2026-ARXIV-2606-28692 | arXiv:2606.28692v1 | paper-v1:2606.28692 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28692 | self | — | new_in_window | AGENT-WORKFLOW | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28707 | arXiv:2606.28707v1 | paper-v1:2606.28707 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28707 | self | — | new_in_window | TRAIN-GRPO | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28712 | arXiv:2606.28712v1 | paper-v1:2606.28712 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28712 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28715 | arXiv:2606.28715v1 | paper-v1:2606.28715 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28715 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28715 | yes |
| SF-2026-ARXIV-2606-28720 | arXiv:2606.28720v1 | paper-v1:2606.28720 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28720 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28720 | yes |
| SF-2026-ARXIV-2606-28725 | arXiv:2606.28725v1 | paper-v1:2606.28725 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28725 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28725 | yes |
| SF-2026-ARXIV-2606-28733 | arXiv:2606.28733v1 | paper-v1:2606.28733 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28733 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28733 | yes |
| SF-2026-ARXIV-2606-28739 | arXiv:2606.28739v1 | paper-v1:2606.28739 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-28739 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28739 | yes |
| SF-2026-ARXIV-2606-28747 | arXiv:2606.28747v1 | paper-v1:2606.28747 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28747 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28747 | yes |
| SF-2026-ARXIV-2606-28751 | arXiv:2606.28751v1 | paper-v1:2606.28751 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28751 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28754 | arXiv:2606.28754v1 | paper-v1:2606.28754 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28754 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28757 | arXiv:2606.28757v1 | paper-v1:2606.28757 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28757 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28757 | yes |
| SF-2026-ARXIV-2606-28758 | arXiv:2606.28758v1 | paper-v1:2606.28758 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28758 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28772 | arXiv:2606.28772v1 | paper-v1:2606.28772 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28772 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-28772 | yes |
| SF-2026-ARXIV-2606-28781 | arXiv:2606.28781v1 | paper-v1:2606.28781 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28781 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28781 | yes |
| SF-2026-ARXIV-2606-28804 | arXiv:2606.28804v1 | paper-v1:2606.28804 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28804 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28813 | arXiv:2606.28813v1 | paper-v1:2606.28813 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28813 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28813 | yes |
| SF-2026-ARXIV-2606-28831 | arXiv:2606.28831v1 | paper-v1:2606.28831 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28831 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28831 | yes |
| SF-2026-ARXIV-2606-28839 | arXiv:2606.28839v1 | paper-v1:2606.28839 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28839 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28839 | yes |
| SF-2026-ARXIV-2606-28841 | arXiv:2606.28841v1 | paper-v1:2606.28841 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28841 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28841 | yes |
| SF-2026-ARXIV-2606-28843 | arXiv:2606.28843v1 | paper-v1:2606.28843 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28843 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28843 | yes |
| SF-2026-ARXIV-2606-28862 | arXiv:2606.28862v1 | paper-v1:2606.28862 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28862 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28862 | yes |
| SF-2026-ARXIV-2606-28863 | arXiv:2606.28863v1 | paper-v1:2606.28863 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28863 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28863 | yes |
| SF-2026-ARXIV-2606-28864 | arXiv:2606.28864v1 | paper-v1:2606.28864 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28864 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28867 | arXiv:2606.28867v1 | paper-v1:2606.28867 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28867 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28867 | yes |
| SF-2026-ARXIV-2606-28876 | arXiv:2606.28876v1 | paper-v1:2606.28876 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28876 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28876 | yes |
| SF-2026-ARXIV-2606-28896 | arXiv:2606.28896v1 | paper-v1:2606.28896 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28896 | self | — | new_in_window | AGENT-WORKFLOW | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28898 | arXiv:2606.28898v1 | paper-v1:2606.28898 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28898 | self | — | new_in_window | TRAIN-DPO | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28900 | arXiv:2606.28900v1 | paper-v1:2606.28900 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28900 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28900 | yes |
| SF-2026-ARXIV-2606-28925 | arXiv:2606.28925v1 | paper-v1:2606.28925 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28925 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28925 | yes |
| SF-2026-ARXIV-2606-28932 | arXiv:2606.28932v1 | paper-v1:2606.28932 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28932 | self | — | new_in_window | TRAIN-PRETRAINING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28938 | arXiv:2606.28938v1 | paper-v1:2606.28938 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28938 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28939 | arXiv:2606.28939v1 | paper-v1:2606.28939 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28939 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28939 | yes |
| SF-2026-ARXIV-2606-28953 | arXiv:2606.28953v1 | paper-v1:2606.28953 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-28953 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28953 | yes |
| SF-2026-ARXIV-2606-28955 | arXiv:2606.28955v1 | paper-v1:2606.28955 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28955 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-28955 | yes |
| SF-2026-ARXIV-2606-28958 | arXiv:2606.28958v1 | paper-v1:2606.28958 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28958 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28958 | yes |
| SF-2026-ARXIV-2606-28962 | arXiv:2606.28962v1 | paper-v1:2606.28962 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-28962 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28962 | yes |
| SF-2026-ARXIV-2606-28995 | arXiv:2606.28995v1 | paper-v1:2606.28995 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28995 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-28995 | yes |
| SF-2026-ARXIV-2606-28998 | arXiv:2606.28998v1 | paper-v1:2606.28998 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28998 | self | — | new_in_window | TRAIN-DPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28998 | yes |
| SF-2026-ARXIV-2606-29013 | arXiv:2606.29013v1 | paper-v1:2606.29013 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29013 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29030 | arXiv:2606.29030v1 | paper-v1:2606.29030 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29030 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29030 | yes |
| SF-2026-ARXIV-2606-29033 | arXiv:2606.29033v1 | paper-v1:2606.29033 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29033 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29033 | yes |
| SF-2026-ARXIV-2606-29038 | arXiv:2606.29038v1 | paper-v1:2606.29038 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29038 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-29038 | yes |
| SF-2026-ARXIV-2606-29054 | arXiv:2606.29054v1 | paper-v1:2606.29054 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29054 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29054 | yes |
| SF-2026-ARXIV-2606-29059 | arXiv:2606.29059v1 | paper-v1:2606.29059 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29059 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29066 | arXiv:2606.29066v1 | paper-v1:2606.29066 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29066 | self | — | new_in_window | INFER-DECODE | Integrate | books-review:SF-2026-ARXIV-2606-29066 | yes |
| SF-2026-ARXIV-2606-29067 | arXiv:2606.29067v1 | paper-v1:2606.29067 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29067 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29067 | yes |
| SF-2026-ARXIV-2606-29073 | arXiv:2606.29073v1 | paper-v1:2606.29073 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29073 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29073 | yes |
| SF-2026-ARXIV-2606-29082 | arXiv:2606.29082v1 | paper-v1:2606.29082 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29082 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29082 | yes |
| SF-2026-ARXIV-2606-29088 | arXiv:2606.29088v1 | paper-v1:2606.29088 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29088 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29088 | yes |
| SF-2026-ARXIV-2606-29089 | arXiv:2606.29089v1 | paper-v1:2606.29089 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29089 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29089 | yes |
| SF-2026-ARXIV-2606-29090 | arXiv:2606.29090v1 | paper-v1:2606.29090 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29090 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29090 | yes |
| SF-2026-ARXIV-2606-29091 | arXiv:2606.29091v1 | paper-v1:2606.29091 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29091 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29091 | yes |
| SF-2026-ARXIV-2606-29094 | arXiv:2606.29094v1 | paper-v1:2606.29094 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29094 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29094 | yes |
| SF-2026-ARXIV-2606-29097 | arXiv:2606.29097v1 | paper-v1:2606.29097 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29097 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29097 | yes |
| SF-2026-ARXIV-2606-29108 | arXiv:2606.29108v1 | paper-v1:2606.29108 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29108 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29108 | yes |
| SF-2026-ARXIV-2606-29112 | arXiv:2606.29112v1 | paper-v1:2606.29112 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-29112 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29116 | arXiv:2606.29116v1 | paper-v1:2606.29116 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29116 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29116 | yes |
| SF-2026-ARXIV-2606-29119 | arXiv:2606.29119v1 | paper-v1:2606.29119 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29119 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29119 | yes |
| SF-2026-ARXIV-2606-29124 | arXiv:2606.29124v1 | paper-v1:2606.29124 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2606-29124 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29124 | yes |
| SF-2026-ARXIV-2606-29126 | arXiv:2606.29126v1 | paper-v1:2606.29126 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29126 | self | — | new_in_window | AGENT-MULTI-AGENT | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29129 | arXiv:2606.29129v1 | paper-v1:2606.29129 | 2026-W26 | 2026-06-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-29129 | self | — | new_in_window | INFER-TENSORRT-LLM | Weekly Only — Context | — | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-28666 | RP-178572df20fba829 | deep | arXiv:2606.28666v1 | SRC-ARXIV@arXiv:2606.28666v1 | https://arxiv.org/html/2606.28666v1 — §2.6 TRiSM framework; 3 Methodology; 3.2 Framework used | https://arxiv.org/html/2606.28666v1 — §4 Results; 4.6 Observation analysis | https://arxiv.org/html/2606.28666v1 — §6 Future work and limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28666 | complete |
| SF-2026-ARXIV-2606-28679 | RP-a2fecebe5d711ec3 | deep | arXiv:2606.28679v1 | SRC-ARXIV@arXiv:2606.28679v1 | https://arxiv.org/html/2606.28679v1 — §Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; III The Cross-Framework Gap; III-A Method and selection | https://arxiv.org/html/2606.28679v1 — §VI Evaluation | https://arxiv.org/html/2606.28679v1 — §Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; II Threat Model; II-A Boundary and adversary；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28679 | complete |
| SF-2026-ARXIV-2606-28690 | RP-37d64bfff74690fd | deep | arXiv:2606.28690v1 | SRC-ARXIV@arXiv:2606.28690v1 | https://arxiv.org/html/2606.28690v1 — §4. The AgentThread Framework; 4.5. Composition Methodology | https://arxiv.org/html/2606.28690v1 — §Formal Security Analysis of Agent Protocol Composition; 6. Evaluation; 6.1. Evaluation Setup | https://arxiv.org/html/2606.28690v1 — §6.4. RQ3: Composition Failures; 7. Discussion; 9. Threats to Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28690 | complete |
| SF-2026-ARXIV-2606-28692 | RP-00672c3363c773cc | standard | arXiv:2606.28692v1 | SRC-ARXIV@arXiv:2606.28692v1 | https://arxiv.org/html/2606.28692v1 — §Report GitHub Issue; An AI agent for treatment reasoning over a biomedical tool universe | https://arxiv.org/html/2606.28692v1 — §Results | https://arxiv.org/html/2606.28692v1 — §Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28692 | complete |
| SF-2026-ARXIV-2606-28707 | RP-3d6a2d01c9bbc59c | standard | arXiv:2606.28707v1 | SRC-ARXIV@arXiv:2606.28707v1 | https://arxiv.org/html/2606.28707v1 — §3 Method; 4.2 Analysis of Training Dynamics; B.2 BV-Blend Training Loop and Advantage Computation | https://arxiv.org/html/2606.28707v1 — §4 Experiments; Evaluation.; 4.1 Main Results | https://arxiv.org/html/2606.28707v1 — §5 Conclusion; Limitations; D.1 Discussion of Key Assumptions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28707 | complete |
| SF-2026-ARXIV-2606-28712 | RP-424fba9a260b69c9 | standard | arXiv:2606.28712v1 | SRC-ARXIV@arXiv:2606.28712v1 | https://arxiv.org/html/2606.28712v1 — §III-E Training and Inference | https://arxiv.org/html/2606.28712v1 — §IV Experiments | https://arxiv.org/html/2606.28712v1 — §V Conclusion and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28712 | complete |
| SF-2026-ARXIV-2606-28715 | RP-77a19f682551553a | standard | arXiv:2606.28715v1 | SRC-ARXIV@arXiv:2606.28715v1 | https://arxiv.org/html/2606.28715v1 — §Report GitHub Issue; SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages | https://arxiv.org/html/2606.28715v1 — §SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages; 2.1 Agent Evaluation; 2.2 Multilingual Evaluation | https://arxiv.org/html/2606.28715v1 — §6 Analysis and Discussion; 7 Conclusion; 8 Limitation；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28715 | complete |
| SF-2026-ARXIV-2606-28720 | RP-5731d4aefedde0a5 | standard | arXiv:2606.28720v1 | SRC-ARXIV@arXiv:2606.28720v1 | https://arxiv.org/html/2606.28720v1 — §III METHOD; IV-B System-level Comparisons | https://arxiv.org/html/2606.28720v1 — §IV EXPERIMENTS; IV-A Experimental Setup; IV-D Retrieval & Alignment Analysis | https://arxiv.org/html/2606.28720v1 — §V CONCLUSIONS；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28720 | complete |
| SF-2026-ARXIV-2606-28725 | RP-0fafab23dd264dbc | standard | arXiv:2606.28725v1 | SRC-ARXIV@arXiv:2606.28725v1 | https://arxiv.org/html/2606.28725v1 — §III Methodology; III-A Framework Overview; IV-B Model and Training Details | https://arxiv.org/html/2606.28725v1 — §IV Experimental Setup; IV-F Evaluation Metrics and Replication; V Experiments | https://arxiv.org/html/2606.28725v1 — §VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28725 | complete |
| SF-2026-ARXIV-2606-28733 | RP-569a332cbc848ff1 | standard | arXiv:2606.28733v1 | SRC-ARXIV@arXiv:2606.28733v1 | https://arxiv.org/html/2606.28733v1 — §5 Our Proposed Method for Improving Agentic Abstention: convolve; G.1 Task setting and training configuration; I.2.1 System Prompt for WebShop | https://arxiv.org/html/2606.28733v1 — §4 Experiment Setup; 4.2 Evaluation Metrics; 6 Results | https://arxiv.org/html/2606.28733v1 — §7 Conclusion; Appendix A Limitations; Failure to abstain from GPT-5.4-mini；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28733 | complete |
| SF-2026-ARXIV-2606-28739 | RP-4498659d3c8432bc | deep | arXiv:2606.28739v1 | SRC-ARXIV@arXiv:2606.28739v1 | https://arxiv.org/html/2606.28739v1 — §Report GitHub Issue; Agent Safety Is Action Alignment | https://arxiv.org/html/2606.28739v1 — §5.3. Relational and Deployment-Conditioned Evaluation | https://arxiv.org/html/2606.28739v1 — §5.2. External Enforcement at the Action Boundary; 7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28739 | complete |
| SF-2026-ARXIV-2606-28747 | RP-c1e3e99bbd1e47e4 | standard | arXiv:2606.28747v1 | SRC-ARXIV@arXiv:2606.28747v1 | https://arxiv.org/html/2606.28747v1 — §Self-Supervised Theorem Discovery in a Formal Axiomatic System; Rules of the Hilbert System. | https://arxiv.org/html/2606.28747v1 — §5 Experiments; 5.1 Experimental Setup; 5.2 Quantitative Evaluation of Theorem Discovery | https://arxiv.org/html/2606.28747v1 — §7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28747 | complete |
| SF-2026-ARXIV-2606-28751 | RP-eb725f0ecff02b63 | standard | arXiv:2606.28751v1 | SRC-ARXIV@arXiv:2606.28751v1 | https://arxiv.org/html/2606.28751v1 — §Report GitHub Issue; A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility | https://arxiv.org/html/2606.28751v1 — §VII Results and discussion; VII.2 Results | https://arxiv.org/html/2606.28751v1 — §VII Results and discussion; VII.5 Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28751 | complete |
| SF-2026-ARXIV-2606-28754 | RP-803632295b7f9cec | standard | arXiv:2606.28754v1 | SRC-ARXIV@arXiv:2606.28754v1 | https://arxiv.org/html/2606.28754v1 — §SHIFT: Dynamic Compute Relocation Framework for Communication-Aware Chiplet-Based Systems; IV SHIFT Framework; IV-A Considerations and Design Methodology | https://arxiv.org/html/2606.28754v1 — §V Evaluations; V-A Experimental Setup; V-B Experimental Results | https://arxiv.org/html/2606.28754v1 — §VI Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28754 | complete |
| SF-2026-ARXIV-2606-28757 | RP-256d401105d57f37 | standard | arXiv:2606.28757v1 | SRC-ARXIV@arXiv:2606.28757v1 | https://arxiv.org/html/2606.28757v1 — §Effect of Post-Training.; C Global Dynamic Reconstruction Methodology; G Post Training Details | https://arxiv.org/html/2606.28757v1 — §A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models; Physical-grounded Evaluation.; 3 Principles of the New Evaluation Protocol | https://arxiv.org/html/2606.28757v1 — §5 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28757 | complete |
| SF-2026-ARXIV-2606-28758 | RP-f3befa0e0e49e008 | standard | arXiv:2606.28758v1 | SRC-ARXIV@arXiv:2606.28758v1 | https://arxiv.org/html/2606.28758v1 — §2 Method; 3.3 Comparison of Diffusion Architectures | https://arxiv.org/html/2606.28758v1 — §3 Experiments; 3.5 Analysis of Structured Sketch Ground Truth | https://arxiv.org/html/2606.28758v1 — §5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28758 | complete |
| SF-2026-ARXIV-2606-28772 | RP-3957a0fe2aa3c328 | deep | arXiv:2606.28772v1 | SRC-ARXIV@arXiv:2606.28772v1 | https://arxiv.org/html/2606.28772v1 — §3 Methods | https://arxiv.org/html/2606.28772v1 — §3.3 Statistical Analysis; 4 Results | https://arxiv.org/html/2606.28772v1 — §Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain; 4.1 Disagreement Concentrates at the Value Boundary; 4.5 Boundary Disagreement Is Not Driven by Annotation Error；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28772 | complete |
| SF-2026-ARXIV-2606-28781 | RP-66dfb9ae36082359 | standard | arXiv:2606.28781v1 | SRC-ARXIV@arXiv:2606.28781v1 | https://arxiv.org/html/2606.28781v1 — §2.1 Agent Memory Systems; 3 Architecture; 4.1 Propagation Algorithm | https://arxiv.org/html/2606.28781v1 — §6 Theoretical Analysis; 8 Competitive Analysis | https://arxiv.org/html/2606.28781v1 — §9 Discussion; 9.2 Limitations and Future Work; 10 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28781 | complete |
| SF-2026-ARXIV-2606-28804 | RP-fbc1ea6418da679b | standard | arXiv:2606.28804v1 | SRC-ARXIV@arXiv:2606.28804v1 | https://arxiv.org/html/2606.28804v1 — §III Method | https://arxiv.org/html/2606.28804v1 — §IV Experiments; IV-A Experimental Setup; IV-B Quantitative Analysis | https://arxiv.org/html/2606.28804v1 — §V Limitations; VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28804 | complete |
| SF-2026-ARXIV-2606-28813 | RP-fa8f315aae351548 | standard | arXiv:2606.28813v1 | SRC-ARXIV@arXiv:2606.28813v1 | https://arxiv.org/html/2606.28813v1 — §Training data.; Appendix E Constraint-Aware Steering Algorithm; Appendix F Model and Training Details | https://arxiv.org/html/2606.28813v1 — §5 Experiments; 5.1 Experimental Setup and Baselines; 5.2 Main Results: Zero-Shot Composition and Generalization | https://arxiv.org/html/2606.28813v1 — §6 Limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28813 | complete |
| SF-2026-ARXIV-2606-28831 | RP-1ffbd671d4afd2c5 | standard | arXiv:2606.28831v1 | SRC-ARXIV@arXiv:2606.28831v1 | https://arxiv.org/html/2606.28831v1 — §System-Algorithm Co-Design in LLM Inference; 3 The Hard-KV Design; 3.1 The Framework Overview | https://arxiv.org/html/2606.28831v1 — §4 Experiment; Appendix C Experiments Details; C.3 Further Experiment Results | https://arxiv.org/html/2606.28831v1 — §5 Conclusion and Future Work; Appendix B Further Discussions on KV Index Regularization; B.2 Discussion on trade-off in the Index Management for Layerwise Selection；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28831 | complete |
| SF-2026-ARXIV-2606-28839 | RP-2f0f5c2f580d2c48 | standard | arXiv:2606.28839v1 | SRC-ARXIV@arXiv:2606.28839v1 | https://arxiv.org/html/2606.28839v1 — §The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems —and Auditing the Claims It Enables; Multi-agent LLM systems.; Network contagion and spectral methods. | https://arxiv.org/html/2606.28839v1 — §LLM bias evaluation.; 4.1.2 Experiment 1: Full CAF Matrix; 4.1.3 Experiment 2: Modality Ablation | https://arxiv.org/html/2606.28839v1 — §4.1.4 Experiment 3: Real-API with Functional BOUNDARY_SYNC; 6 Discussion; 7 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28839 | complete |
| SF-2026-ARXIV-2606-28841 | RP-a5be84d75247be66 | standard | arXiv:2606.28841v1 | SRC-ARXIV@arXiv:2606.28841v1 | https://arxiv.org/html/2606.28841v1 — §LAMP: Lean-based Agentic framework with MCP and Proof Repair; 2.3 Agentic Frameworks for Theorem Proving; 3 The LAMP System | https://arxiv.org/html/2606.28841v1 — §4 Experimental Results; 4.1 Experimental Setup; Evaluation suite: | https://arxiv.org/html/2606.28841v1 — §5 Discussion and Limitations; Failure Analysis:; Limitations and Future Work:；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28841 | complete |
| SF-2026-ARXIV-2606-28843 | RP-963da48c51046c25 | standard | arXiv:2606.28843v1 | SRC-ARXIV@arXiv:2606.28843v1 | https://arxiv.org/html/2606.28843v1 — §5.3 Pre-training distributions and scale | https://arxiv.org/html/2606.28843v1 — §3 Experimental Set Up; 3.2 Evaluation Protocol; 4 Results | https://arxiv.org/html/2606.28843v1 — §7 Discussion; 7.2 Limitations; 8 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28843 | complete |
| SF-2026-ARXIV-2606-28862 | RP-df08283ddbbe20aa | standard | arXiv:2606.28862v1 | SRC-ARXIV@arXiv:2606.28862v1 | https://arxiv.org/html/2606.28862v1 — §4 Method: HKVLM; 4.5 Cold-start training; 5 Experimental Design and Evaluation Protocol | https://arxiv.org/html/2606.28862v1 — §Hallucination evaluation.; 5 Experimental Design and Evaluation Protocol; 6 Results | https://arxiv.org/html/2606.28862v1 — §8 Discussion, Limitations, and Broader Impact; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28862 | complete |
| SF-2026-ARXIV-2606-28863 | RP-ee35ec20552de370 | standard | arXiv:2606.28863v1 | SRC-ARXIV@arXiv:2606.28863v1 | https://arxiv.org/html/2606.28863v1 — §Defeat Devices in AI Systems; 4.1 Five method families; 5.1 Defeat devices can naturally emerge in AI systems | https://arxiv.org/html/2606.28863v1 — §5.5 Four decisive experiments; 6.1 Evaluation methodology | https://arxiv.org/html/2606.28863v1 — §2.4 Boundary cases; 6.5 Limitations; 7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28863 | complete |
| SF-2026-ARXIV-2606-28864 | RP-018bb994c24c8ab2 | standard | arXiv:2606.28864v1 | SRC-ARXIV@arXiv:2606.28864v1 | https://arxiv.org/html/2606.28864v1 — §S11 Method Parameters | https://arxiv.org/html/2606.28864v1 — §4 Experiments and Takeaways; 6 Analysis of Multimodal Chain-of-Thoughts; S1 InternVL-3.5 Results | https://arxiv.org/html/2606.28864v1 — §7 Conclusion; S12 Other model failures；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28864 | complete |
| SF-2026-ARXIV-2606-28867 | RP-9ee6c870299b2a11 | standard | arXiv:2606.28867v1 | SRC-ARXIV@arXiv:2606.28867v1 | https://arxiv.org/html/2606.28867v1 — §Legal analysis of AI training data. | https://arxiv.org/html/2606.28867v1 — §Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages; Legal analysis of AI training data. | https://arxiv.org/html/2606.28867v1 — §6. Four Failure Modes; 6.4. Data Persistence Failure: The Congolese Radio Corpus; 9. Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28867 | complete |
| SF-2026-ARXIV-2606-28876 | RP-5a0256f0a4e3782a | standard | arXiv:2606.28876v1 | SRC-ARXIV@arXiv:2606.28876v1 | https://arxiv.org/html/2606.28876v1 — §2 Method Sketch | https://arxiv.org/html/2606.28876v1 — §3 Experimental Route; 4 Results; Why frozen-model evaluation is still useful. | https://arxiv.org/html/2606.28876v1 — §5 Discussion; 8 Limitations and Next Steps; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28876 | complete |
| SF-2026-ARXIV-2606-28896 | RP-374913ae69ef13c2 | standard | arXiv:2606.28896v1 | SRC-ARXIV@arXiv:2606.28896v1 | https://arxiv.org/html/2606.28896v1 — §A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation; 3 Method; 3.1 Problem Formulation and System Overview | https://arxiv.org/html/2606.28896v1 — §2.4 Tool-Augmented LLM Agents and Evaluation; 3.5 Observer-Driven Evaluation and Bounded Repair; 4 Experiments | https://arxiv.org/html/2606.28896v1 — §5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28896 | complete |
| SF-2026-ARXIV-2606-28898 | RP-d845e71ee0919445 | standard | arXiv:2606.28898v1 | SRC-ARXIV@arXiv:2606.28898v1 | https://arxiv.org/html/2606.28898v1 — §PASTA: A Paraphrasing And Self-Training Approach for Knowledge Updating in LLMs; 3 Proposed Method; 3.1 Design Motivations | https://arxiv.org/html/2606.28898v1 — §4 Experiments; 4.2 Experimental Setup; 4.3 Evaluation Methods | https://arxiv.org/html/2606.28898v1 — §5 Conclusion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28898 | complete |
| SF-2026-ARXIV-2606-28900 | RP-fb4263736b1a1927 | standard | arXiv:2606.28900v1 | SRC-ARXIV@arXiv:2606.28900v1 | https://arxiv.org/html/2606.28900v1 — §Design goals.; Training-oriented derivatives. | https://arxiv.org/html/2606.28900v1 — §Medical QA and fixed-input evaluation.; Memory, retrieval, and continual evaluation.; 3 MedEvoEval : An Executable Evaluation Protocol | https://arxiv.org/html/2606.28900v1 — §6 Discussion, Limitations, and Ethics; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28900 | complete |
| SF-2026-ARXIV-2606-28925 | RP-ecb54e5df671eee9 | standard | arXiv:2606.28925v1 | SRC-ARXIV@arXiv:2606.28925v1 | https://arxiv.org/html/2606.28925v1 — §2.1. Tool/Agent Routing in LLM Systems; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 2.6. Multi-Agent Systems and Task Decomposition | https://arxiv.org/html/2606.28925v1 — §Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 3.1. Problem setup and notation | https://arxiv.org/html/2606.28925v1 — §7. Discussion; 8. Limitations; 10. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28925 | complete |
| SF-2026-ARXIV-2606-28932 | RP-ec6387bef8bcb16e | standard | arXiv:2606.28932v1 | SRC-ARXIV@arXiv:2606.28932v1 | https://arxiv.org/html/2606.28932v1 — §DLR: Zero-Inference-Cost Latent Residuals for Low-Rank Pre-Training; 2 Low-rank efficient pre-training; Appendix D The impact of DLR on training dynamics | https://arxiv.org/html/2606.28932v1 — §2.1 Setup and a Unified View; 4 Experiments; 4.1 Evaluation Setup and Protocol | https://arxiv.org/html/2606.28932v1 — §5 Conclusion, Limitations and Outlook；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28932 | complete |
| SF-2026-ARXIV-2606-28938 | RP-1ab5d69cebbf8c46 | standard | arXiv:2606.28938v1 | SRC-ARXIV@arXiv:2606.28938v1 | https://arxiv.org/html/2606.28938v1 — §3 Methodology: Electro-Visual-Language Assistant (EVLA); 3.4 Physics-Guided Joint Training Objective; 3.5 Implementation and Training Details | https://arxiv.org/html/2606.28938v1 — §4 Experiments; 4.3 Evaluation and Main Results; 4.7 Parameter Sensitivity Analysis | https://arxiv.org/html/2606.28938v1 — §4.8 Discussion; 5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28938 | complete |
| SF-2026-ARXIV-2606-28939 | RP-88dfc073c7c6a99b | standard | arXiv:2606.28939v1 | SRC-ARXIV@arXiv:2606.28939v1 | https://arxiv.org/html/2606.28939v1 — §4 Our Approach: ReGuide; Appendix B Algorithm | https://arxiv.org/html/2606.28939v1 — §5 Experiments; Appendix D Setup Details | https://arxiv.org/html/2606.28939v1 — §6 Conclusion and Limitations; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28939 | complete |
| SF-2026-ARXIV-2606-28953 | RP-321d933d6d06c904 | deep | arXiv:2606.28953v1 | SRC-ARXIV@arXiv:2606.28953v1 | https://arxiv.org/html/2606.28953v1 — §Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 4.5 Proposed defense vs prior methods; 5.1 Proposed defense vs prior methods | https://arxiv.org/html/2606.28953v1 — §3.4 Linear Discriminant Analysis; 4 Experimental set-up; 5 Results and Discussion | https://arxiv.org/html/2606.28953v1 — §Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 2 Threat Model; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28953 | complete |
| SF-2026-ARXIV-2606-28955 | RP-b1eb168f4c50f062 | deep | arXiv:2606.28955v1 | SRC-ARXIV@arXiv:2606.28955v1 | https://arxiv.org/html/2606.28955v1 — §3 Method; Pretraining.; Pretraining budget. | https://arxiv.org/html/2606.28955v1 — §Theoretical analysis.; 4 Experiments; 4.2 Main results | https://arxiv.org/html/2606.28955v1 — §5 Limitations and Future Work; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28955 | complete |
| SF-2026-ARXIV-2606-28958 | RP-a2c09e5bba754923 | standard | arXiv:2606.28958v1 | SRC-ARXIV@arXiv:2606.28958v1 | https://arxiv.org/html/2606.28958v1 — §Report GitHub Issue; When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration | https://arxiv.org/html/2606.28958v1 — §5 Benchmark and Experimental Setup; 8 Defense Diagnostics and Trade-Off Analysis | https://arxiv.org/html/2606.28958v1 — §3 Problem Setting and Threat Model; 8.4 Transport Integrity and Fail-Closed Boundary; 9 Failure Modes and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28958 | complete |
| SF-2026-ARXIV-2606-28962 | RP-8e10ddf63257d7f8 | deep | arXiv:2606.28962v1 | SRC-ARXIV@arXiv:2606.28962v1 | https://arxiv.org/html/2606.28962v1 — §III Methodology; III-B Defense Framework Design; III-C Defense Metric Design | https://arxiv.org/html/2606.28962v1 — §IV Experiments; IV-A Experimental Setup; IV-B Experimental Scenarios and Results | https://arxiv.org/html/2606.28962v1 — §III-A Threat Model; V Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28962 | complete |
| SF-2026-ARXIV-2606-28995 | RP-0f636964a2207b59 | deep | arXiv:2606.28995v1 | SRC-ARXIV@arXiv:2606.28995v1 | https://arxiv.org/html/2606.28995v1 — §IV Methodology; V-A 3 CBVF Training Details | https://arxiv.org/html/2606.28995v1 — §III Background and Problem Setup; V Experiments; V-A Experimental Setup | https://arxiv.org/html/2606.28995v1 — §VI Conclusion, Limitations and Future Works；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28995 | complete |
| SF-2026-ARXIV-2606-28998 | RP-eae8c73448a20e12 | standard | arXiv:2606.28998v1 | SRC-ARXIV@arXiv:2606.28998v1 | https://arxiv.org/html/2606.28998v1 — §3. Methodology | https://arxiv.org/html/2606.28998v1 — §3.4. Evaluation Benchmarks; 3.4.1. Evaluation on Functional Benchmarks; 3.4.2. Evaluation on Non-Functional Benchmarks | https://arxiv.org/html/2606.28998v1 — §3.6. Threats to Validity; Small Model Limitations; Failure Cases；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28998 | complete |
| SF-2026-ARXIV-2606-29013 | RP-3b7cb4d13822de88 | standard | arXiv:2606.29013v1 | SRC-ARXIV@arXiv:2606.29013v1 | https://arxiv.org/html/2606.29013v1 — §3 Framework; 3.2 Training protocol | https://arxiv.org/html/2606.29013v1 — §3.1 Model setup; 4 Experiments | https://arxiv.org/html/2606.29013v1 — §5 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29013 | complete |
| SF-2026-ARXIV-2606-29030 | RP-53a6f90b6a80096b | standard | arXiv:2606.29030v1 | SRC-ARXIV@arXiv:2606.29030v1 | https://arxiv.org/html/2606.29030v1 — §III Architecture of the Proposed Agent | https://arxiv.org/html/2606.29030v1 — §V Numerical Results; V-A Experimental Dataset and Model Setup; V-B Comparison across Benchmarks and Model Backends | https://arxiv.org/html/2606.29030v1 — §VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29030 | complete |
| SF-2026-ARXIV-2606-29033 | RP-064af06bab544a78 | standard | arXiv:2606.29033v1 | SRC-ARXIV@arXiv:2606.29033v1 | https://arxiv.org/html/2606.29033v1 — §Approach 1: Human Verification of AI Proposals.; Approach 2: Manual Test Sets.; Approach 3: Humans Specify Criteria, AI Applies Them at Scale. | https://arxiv.org/html/2606.29033v1 — §Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations; 4. Avoiding Evaluation Tropes | https://arxiv.org/html/2606.29033v1 — §6. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29033 | complete |
| SF-2026-ARXIV-2606-29038 | RP-4b97c50e4e42bca3 | deep | arXiv:2606.29038v1 | SRC-ARXIV@arXiv:2606.29038v1 | https://arxiv.org/html/2606.29038v1 — §2 Pipeline Architecture and Metric Aggregation Divergence; 2.4 Positioning: Pipeline Architecture as Unregistered Degrees of Freedom | https://arxiv.org/html/2606.29038v1 — §3.2 Controlled Aggregation Experiment (EA-2); Appendix A Experiment Parameters | https://arxiv.org/html/2606.29038v1 — §Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy; 6 Discussion; 7 Limitations and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29038 | complete |
| SF-2026-ARXIV-2606-29054 | RP-0cab2d6674521129 | standard | arXiv:2606.29054v1 | SRC-ARXIV@arXiv:2606.29054v1 | https://arxiv.org/html/2606.29054v1 — §2 Method; Ministral violations expose framework limits.; Practical decision framework. | https://arxiv.org/html/2606.29054v1 — §Problem setup.; 3 Experiments; 3.1 Setup | https://arxiv.org/html/2606.29054v1 — §4 Discussion; 6 Conclusion; Threats to validity and limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29054 | complete |
| SF-2026-ARXIV-2606-29059 | RP-1d388ef6f62446fb | standard | arXiv:2606.29059v1 | SRC-ARXIV@arXiv:2606.29059v1 | https://arxiv.org/html/2606.29059v1 — §3 The Proposed Method: FlowWM; 3.3 Training Objectives | https://arxiv.org/html/2606.29059v1 — §4 Latent World Model Benchmarks; 4.1 Synthetic Benchmark: Bouncing Shapes; 4.2 Real-world Benchmark: FuturePerception | https://arxiv.org/html/2606.29059v1 — §6 Conclusion; Practical limitations.; Appendix J Discussion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29059 | complete |
| SF-2026-ARXIV-2606-29066 | RP-89db3198eb3c2ac2 | deep | arXiv:2606.29066v1 | SRC-ARXIV@arXiv:2606.29066v1 | https://arxiv.org/html/2606.29066v1 — §Training objective; 4 Training; 4.2 Step-Size Policy Training | https://arxiv.org/html/2606.29066v1 — §5 Experiments; 5.3 Code Generation Evaluation; Setup | https://arxiv.org/html/2606.29066v1 — §7 Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29066 | complete |
| SF-2026-ARXIV-2606-29067 | RP-b6723415f8dad570 | standard | arXiv:2606.29067v1 | SRC-ARXIV@arXiv:2606.29067v1 | https://arxiv.org/html/2606.29067v1 — §3 Method; H.1 Study Design | https://arxiv.org/html/2606.29067v1 — §Graph-based trace analysis.; Layer 4: Cross-segment analysis.; 4 Experimental Protocol | https://arxiv.org/html/2606.29067v1 — §Layer 1: Structural segmentation and boundary classification.; Layer 2: Soft boundary detection.; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29067 | complete |
| SF-2026-ARXIV-2606-29073 | RP-a7d6d25fb144b92a | standard | arXiv:2606.29073v1 | SRC-ARXIV@arXiv:2606.29073v1 | https://arxiv.org/html/2606.29073v1 — §5 HCP Design; 6 Benchmark Method; 7.7 Ecosystem Measurement | https://arxiv.org/html/2606.29073v1 — §From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes; 6 Benchmark Method; 7 Evaluation | https://arxiv.org/html/2606.29073v1 — §3 Threat Model; 6.3 Reproducibility Boundary; 8 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29073 | complete |
| SF-2026-ARXIV-2606-29082 | RP-3db51d3d82e4cdc9 | standard | arXiv:2606.29082v1 | SRC-ARXIV@arXiv:2606.29082v1 | https://arxiv.org/html/2606.29082v1 — §EFT serves as mid-training for test-time RL.; Appendix C Additional Details of Dataset Construction Method; C.1 Systematic Error Breakdown Analysis | https://arxiv.org/html/2606.29082v1 — §Optimization setup.; 3.2 Analysis of ℱ \mathcal{F} inch Collection; 4 Experiments | https://arxiv.org/html/2606.29082v1 — §7 Conclusion; Limitations; Appendix B Further Details and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29082 | complete |
| SF-2026-ARXIV-2606-29088 | RP-90490179ad4f2f88 | standard | arXiv:2606.29088v1 | SRC-ARXIV@arXiv:2606.29088v1 | https://arxiv.org/html/2606.29088v1 — §Report GitHub Issue; Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking | https://arxiv.org/html/2606.29088v1 — §Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking; 3 The Proposed Benchmark; 4 Evaluation | https://arxiv.org/html/2606.29088v1 — §5 Discussion; 6 Threats to Validity; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29088 | complete |
| SF-2026-ARXIV-2606-29089 | RP-b3a45ad3203861ed | standard | arXiv:2606.29089v1 | SRC-ARXIV@arXiv:2606.29089v1 | https://arxiv.org/html/2606.29089v1 — §3 Method | https://arxiv.org/html/2606.29089v1 — §4 Experiments; 4.1 Results | https://arxiv.org/html/2606.29089v1 — §5 Discussion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29089 | complete |
| SF-2026-ARXIV-2606-29090 | RP-4677e234443c63ce | standard | arXiv:2606.29090v1 | SRC-ARXIV@arXiv:2606.29090v1 | https://arxiv.org/html/2606.29090v1 — §III Methodology and Framework; III-A Overall Framework; III-B System Architecture | https://arxiv.org/html/2606.29090v1 — §III-F Evaluation Metrics; IV-E API Cost and Token Analysis; V Results and Analysis | https://arxiv.org/html/2606.29090v1 — §V-F Qualitative Examples and Discussion; VI Conclusion and Future Work; VI-A Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29090 | complete |
| SF-2026-ARXIV-2606-29091 | RP-79daaeca5126c731 | standard | arXiv:2606.29091v1 | SRC-ARXIV@arXiv:2606.29091v1 | https://arxiv.org/html/2606.29091v1 — §Chance across architectures. | https://arxiv.org/html/2606.29091v1 — §4 Results | https://arxiv.org/html/2606.29091v1 — §6 Discussion & Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29091 | complete |
| SF-2026-ARXIV-2606-29094 | RP-015c3be00b3c76bc | standard | arXiv:2606.29094v1 | SRC-ARXIV@arXiv:2606.29094v1 | https://arxiv.org/html/2606.29094v1 — §3.1. Design Overview; Appendix C Algorithm for Supporting Approximate KV Caching | https://arxiv.org/html/2606.29094v1 — §5. Evaluation; 5.1. Experimental Setup; 5.3. Accuracy Benchmarks | https://arxiv.org/html/2606.29094v1 — §7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29094 | complete |
| SF-2026-ARXIV-2606-29097 | RP-13a0e287206ee937 | standard | arXiv:2606.29097v1 | SRC-ARXIV@arXiv:2606.29097v1 | https://arxiv.org/html/2606.29097v1 — §3 Method | https://arxiv.org/html/2606.29097v1 — §4 Experiments; 4.1 Experimental Setup; Experiment setup. | https://arxiv.org/html/2606.29097v1 — §5 Limitations and Future Work; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29097 | complete |
| SF-2026-ARXIV-2606-29108 | RP-3845c27c6c04ed2d | standard | arXiv:2606.29108v1 | SRC-ARXIV@arXiv:2606.29108v1 | arXiv:2606.29108v1 version-stamped mirror — §Our approach; III Methodology | arXiv:2606.29108v1 version-stamped mirror — §Results; V Evaluation; V-A Experiment Setup | arXiv:2606.29108v1 version-stamped mirror — §VI Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29108 | complete |
| SF-2026-ARXIV-2606-29112 | RP-6e5de2460af3aa6c | deep | arXiv:2606.29112v1 | SRC-ARXIV@arXiv:2606.29112v1 | https://arxiv.org/html/2606.29112v1 — §3 Method | https://arxiv.org/html/2606.29112v1 — §4 Experimental Results; 4.1 Experiment Setup | https://arxiv.org/html/2606.29112v1 — §5 Summary; Instructions for reporting errors；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29112 | complete |
| SF-2026-ARXIV-2606-29116 | RP-29d8fdc9d77ad12e | standard | arXiv:2606.29116v1 | SRC-ARXIV@arXiv:2606.29116v1 | https://arxiv.org/html/2606.29116v1 — §Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem | https://arxiv.org/html/2606.29116v1 — §6.3 Benchmarks for Realistic Agent Behavior | https://arxiv.org/html/2606.29116v1 — §3.4 RQ3: Failure Handling; 5 Discussion; 5.1 Threats to Construct Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29116 | complete |
| SF-2026-ARXIV-2606-29119 | RP-1823ec4541ebe590 | standard | arXiv:2606.29119v1 | SRC-ARXIV@arXiv:2606.29119v1 | https://arxiv.org/html/2606.29119v1 — §Report GitHub Issue; Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule | https://arxiv.org/html/2606.29119v1 — §5.1 Heritability does not rescue (the κ \kappa -sparsity result); 7 The Positive Condition — a Hypothesis, Not a Result | https://arxiv.org/html/2606.29119v1 — §8 Limitations; 9 Discussion and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29119 | complete |
| SF-2026-ARXIV-2606-29124 | RP-097323bfbdb97f79 | deep | arXiv:2606.29124v1 | SRC-ARXIV@arXiv:2606.29124v1 | https://arxiv.org/html/2606.29124v1 — §3 Methodology | https://arxiv.org/html/2606.29124v1 — §Output of differential analysis:; 3.6 Stage 5: Result Analysis; LLM-based analysis of differential results: | https://arxiv.org/html/2606.29124v1 — §2.3 SMTP Nesting Failures (Mailpit); Boundary value analysis (BVA):; 6 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29124 | complete |
| SF-2026-ARXIV-2606-29126 | RP-c3fb060e10fe5e77 | standard | arXiv:2606.29126v1 | SRC-ARXIV@arXiv:2606.29126v1 | https://arxiv.org/html/2606.29126v1 — §4 Methodology; 4.1 MARL Framework; Training Objective | https://arxiv.org/html/2606.29126v1 — §5 Experiments; 5.1 Setup; 5.2 Results | https://arxiv.org/html/2606.29126v1 — §6 Conclusion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29126 | complete |
| SF-2026-ARXIV-2606-29129 | RP-3dea7788a0903e61 | standard | arXiv:2606.29129v1 | SRC-ARXIV@arXiv:2606.29129v1 | https://arxiv.org/html/2606.29129v1 — §4 Proposed Method | https://arxiv.org/html/2606.29129v1 — §3.1 Theoretical Analysis; 5 Evaluation | https://arxiv.org/html/2606.29129v1 — §3 Limitation of Fast Mode Scaling; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-29129 | complete |

### Source Reviews
<!-- review:SF-2026-ARXIV-2606-28666:start -->
### 2606.28666 — Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare

**问题。** 《Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare》处理的问题是：Agent-based AI has enabled the automation of tasks by exposing application tools and resources to large language models (LLMs).

**机制与 state/data/control owner。** exact-v1 的机制路径为 2.6 TRiSM framework; 3 Methodology; 3.2 Framework used。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare》和上述 method locator 共同限定。 归属 `PLATFORM-SECURITY`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Results; 4.6 Observation analysis；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：6 Future work and limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 6 Future work and limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 风险管理而不是一次性认证` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28666v1 — §2.6 TRiSM framework; 3 Methodology; 3.2 Framework used`；Evaluation=`https://arxiv.org/html/2606.28666v1 — §4 Results; 4.6 Observation analysis`；Non-proof=`https://arxiv.org/html/2606.28666v1 — §6 Future work and limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28666:start -->
Claim boundary：仅 arXiv:2606.28666v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28666:end -->
<!-- review:SF-2026-ARXIV-2606-28666:end -->

<!-- review:SF-2026-ARXIV-2606-28679:start -->
### 2606.28679 — Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks

**问题。** 《Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks》处理的问题是：Tool-using LLM agents increasingly read untrusted content while holding side-effecting tools such as payments, email, CRM, and infrastructure APIs, yet common framework defaults still conflate tool exposure with authorization.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; III The Cross-Framework Gap; III-A Method and selection。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks》和上述 method locator 共同限定。 归属 `PLATFORM-SECURITY`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 VI Evaluation；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; II Threat Model; II-A Boundary and adversary；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; II Threat Model; II-A Boundary and adversary；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 风险管理而不是一次性认证` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28679v1 — §Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; III The Cross-Framework Gap; III-A Method and selection`；Evaluation=`https://arxiv.org/html/2606.28679v1 — §VI Evaluation`；Non-proof=`https://arxiv.org/html/2606.28679v1 — §Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; II Threat Model; II-A Boundary and adversary；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28679:start -->
Claim boundary：仅 arXiv:2606.28679v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28679:end -->
<!-- review:SF-2026-ARXIV-2606-28679:end -->

<!-- review:SF-2026-ARXIV-2606-28690:start -->
### 2606.28690 — Formal Security Analysis of Agent Protocol Composition

**问题。** 《Formal Security Analysis of Agent Protocol Composition》处理的问题是：AI agent protocols define how agents use tools, delegate work, and coordinate across software systems, but their security requirements remain incomplete and inconsistently enforced across deployments.

**机制与 state/data/control owner。** exact-v1 的机制路径为 4. The AgentThread Framework; 4.5. Composition Methodology。在 `AGENT-MCP` 中，该路径改变或检验的具体对象由题名《Formal Security Analysis of Agent Protocol Composition》和上述 method locator 共同限定。 归属 `AGENT-MCP`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Formal Security Analysis of Agent Protocol Composition; 6. Evaluation; 6.1. Evaluation Setup；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：6.4. RQ3: Composition Failures; 7. Discussion; 9. Threats to Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 6.4. RQ3: Composition Failures; 7. Discussion; 9. Threats to Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Tool Catalog 扩大后，Discovery 与 Execution 必须分离` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28690v1 — §4. The AgentThread Framework; 4.5. Composition Methodology`；Evaluation=`https://arxiv.org/html/2606.28690v1 — §Formal Security Analysis of Agent Protocol Composition; 6. Evaluation; 6.1. Evaluation Setup`；Non-proof=`https://arxiv.org/html/2606.28690v1 — §6.4. RQ3: Composition Failures; 7. Discussion; 9. Threats to Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28690:start -->
Claim boundary：仅 arXiv:2606.28690v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28690:end -->
<!-- review:SF-2026-ARXIV-2606-28690:end -->

<!-- review:SF-2026-ARXIV-2606-28692:start -->
### 2606.28692 — An AI agent for treatment reasoning over a biomedical tool universe

**问题。** 《An AI agent for treatment reasoning over a biomedical tool universe》处理的问题是：Treatment reasoning underpins every therapeutic decision, integrating disease context, comorbidities, medications, contraindications, and evolving biomedical knowledge to select an appropriate therapy.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Report GitHub Issue; An AI agent for treatment reasoning over a biomedical tool universe。在 `AGENT-WORKFLOW` 中，该路径改变或检验的具体对象由题名《An AI agent for treatment reasoning over a biomedical tool universe》和上述 method locator 共同限定。 归属 `AGENT-WORKFLOW`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## State Machine 是基本模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28692v1 — §Report GitHub Issue; An AI agent for treatment reasoning over a biomedical tool universe`；Evaluation=`https://arxiv.org/html/2606.28692v1 — §Results`；Non-proof=`https://arxiv.org/html/2606.28692v1 — §Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28692:start -->
Claim boundary：仅 arXiv:2606.28692v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28692:end -->
<!-- review:SF-2026-ARXIV-2606-28692:end -->

<!-- review:SF-2026-ARXIV-2606-28707:start -->
### 2606.28707 — BV-Blend: Uncertainty-Weighted Historical Baselines for Stable Critic-Free RL with Verifiable Rewards

**问题。** 《BV-Blend: Uncertainty-Weighted Historical Baselines for Stable Critic-Free RL with Verifiable Rewards》处理的问题是：Critic-free reinforcement learning with verifiable rewards (RLVR), exemplified by Group Relative Policy Optimization (GRPO), avoids training a value function (critic) and reduces memory and compute overhead relative to critic-based PPO pipelines for aligning large language models.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3 Method; 4.2 Analysis of Training Dynamics; B.2 BV-Blend Training Loop and Advantage Computation。在 `TRAIN-GRPO` 中，该路径改变或检验的具体对象由题名《BV-Blend: Uncertainty-Weighted Historical Baselines for Stable Critic-Free RL with Verifiable Rewards》和上述 method locator 共同限定。 归属 `TRAIN-GRPO`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Experiments; Evaluation.; 4.1 Main Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Conclusion; Limitations; D.1 Discussion of Key Assumptions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Conclusion; Limitations; D.1 Discussion of Key Assumptions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28707v1 — §3 Method; 4.2 Analysis of Training Dynamics; B.2 BV-Blend Training Loop and Advantage Computation`；Evaluation=`https://arxiv.org/html/2606.28707v1 — §4 Experiments; Evaluation.; 4.1 Main Results`；Non-proof=`https://arxiv.org/html/2606.28707v1 — §5 Conclusion; Limitations; D.1 Discussion of Key Assumptions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28707:start -->
Claim boundary：仅 arXiv:2606.28707v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28707:end -->
<!-- review:SF-2026-ARXIV-2606-28707:end -->

<!-- review:SF-2026-ARXIV-2606-28712:start -->
### 2606.28712 — J-LAW: Joint Localization and Actionable World Modeling via Coupled Latent Factor Graphs

**问题。** 《J-LAW: Joint Localization and Actionable World Modeling via Coupled Latent Factor Graphs》处理的问题是：Classical SLAM estimates metric poses and a geometric map but produces no actionable predictive model for planning.

**机制与 state/data/control owner。** exact-v1 的机制路径为 III-E Training and Inference。在 `MULTIMODAL-WORLD-MODELS` 中，该路径改变或检验的具体对象由题名《J-LAW: Joint Localization and Actionable World Modeling via Coupled Latent Factor Graphs》和上述 method locator 共同限定。 归属 `MULTIMODAL-WORLD-MODELS`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 IV Experiments；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：V Conclusion and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** V Conclusion and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## State ownership` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28712v1 — §III-E Training and Inference`；Evaluation=`https://arxiv.org/html/2606.28712v1 — §IV Experiments`；Non-proof=`https://arxiv.org/html/2606.28712v1 — §V Conclusion and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28712:start -->
Claim boundary：仅 arXiv:2606.28712v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28712:end -->
<!-- review:SF-2026-ARXIV-2606-28712:end -->

<!-- review:SF-2026-ARXIV-2606-28715:start -->
### 2606.28715 — SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages

**问题。** 《SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages》处理的问题是：While AI development and evaluation for Southeast Asia (SEA) has grown rapidly, agent capabilities in regional languages are still poorly understood despite its importance to sovereign AI.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Report GitHub Issue; SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages; 2.1 Agent Evaluation; 2.2 Multilingual Evaluation；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：6 Analysis and Discussion; 7 Conclusion; 8 Limitation；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 6 Analysis and Discussion; 7 Conclusion; 8 Limitation；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28715v1 — §Report GitHub Issue; SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages`；Evaluation=`https://arxiv.org/html/2606.28715v1 — §SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages; 2.1 Agent Evaluation; 2.2 Multilingual Evaluation`；Non-proof=`https://arxiv.org/html/2606.28715v1 — §6 Analysis and Discussion; 7 Conclusion; 8 Limitation；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28715:start -->
Claim boundary：仅 arXiv:2606.28715v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28715:end -->
<!-- review:SF-2026-ARXIV-2606-28715:end -->

<!-- review:SF-2026-ARXIV-2606-28720:start -->
### 2606.28720 — CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance

**问题。** 《CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance》处理的问题是：Lifelong scene mapping under rigid object rearrangement remains a fundamental challenge in robotics.

**机制与 state/data/control owner。** exact-v1 的机制路径为 III METHOD; IV-B System-level Comparisons。在 `MULTIMODAL-WORLD-MODELS` 中，该路径改变或检验的具体对象由题名《CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance》和上述 method locator 共同限定。 归属 `MULTIMODAL-WORLD-MODELS`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 IV EXPERIMENTS; IV-A Experimental Setup; IV-D Retrieval & Alignment Analysis；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：V CONCLUSIONS；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** V CONCLUSIONS；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## State ownership` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28720v1 — §III METHOD; IV-B System-level Comparisons`；Evaluation=`https://arxiv.org/html/2606.28720v1 — §IV EXPERIMENTS; IV-A Experimental Setup; IV-D Retrieval & Alignment Analysis`；Non-proof=`https://arxiv.org/html/2606.28720v1 — §V CONCLUSIONS；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28720:start -->
Claim boundary：仅 arXiv:2606.28720v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28720:end -->
<!-- review:SF-2026-ARXIV-2606-28720:end -->

<!-- review:SF-2026-ARXIV-2606-28725:start -->
### 2606.28725 — DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation

**问题。** 《DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation》处理的问题是：Automated toxicity moderation systems operate in dynamic online environments where harmful behavior evolves through coded language, shifting targets, and strategic adaptation to enforcement.

**机制与 state/data/control owner。** exact-v1 的机制路径为 III Methodology; III-A Framework Overview; IV-B Model and Training Details。在 `PLATFORM-MONITORING` 中，该路径改变或检验的具体对象由题名《DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation》和上述 method locator 共同限定。 归属 `PLATFORM-MONITORING`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 IV Experimental Setup; IV-F Evaluation Metrics and Replication; V Experiments；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Monitoring 也会改变系统` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28725v1 — §III Methodology; III-A Framework Overview; IV-B Model and Training Details`；Evaluation=`https://arxiv.org/html/2606.28725v1 — §IV Experimental Setup; IV-F Evaluation Metrics and Replication; V Experiments`；Non-proof=`https://arxiv.org/html/2606.28725v1 — §VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28725:start -->
Claim boundary：仅 arXiv:2606.28725v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28725:end -->
<!-- review:SF-2026-ARXIV-2606-28725:end -->

<!-- review:SF-2026-ARXIV-2606-28733:start -->
### 2606.28733 — Agentic Abstention: Do Agents Know When to Stop Instead of Act?

**问题。** 《Agentic Abstention: Do Agents Know When to Stop Instead of Act?》处理的问题是：LLM agents are expected to act over multiple turns, using search, browsing interfaces, and terminal tools to complete user goals.

**机制与 state/data/control owner。** exact-v1 的机制路径为 5 Our Proposed Method for Improving Agentic Abstention: convolve; G.1 Task setting and training configuration; I.2.1 System Prompt for WebShop。在 `AGENT-PLANNING` 中，该路径改变或检验的具体对象由题名《Agentic Abstention: Do Agents Know When to Stop Instead of Act?》和上述 method locator 共同限定。 归属 `AGENT-PLANNING`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Experiment Setup; 4.2 Evaluation Metrics; 6 Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：7 Conclusion; Appendix A Limitations; Failure to abstain from GPT-5.4-mini；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 7 Conclusion; Appendix A Limitations; Failure to abstain from GPT-5.4-mini；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 完成证据与 Verification` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28733v1 — §5 Our Proposed Method for Improving Agentic Abstention: convolve; G.1 Task setting and training configuration; I.2.1 System Prompt for WebShop`；Evaluation=`https://arxiv.org/html/2606.28733v1 — §4 Experiment Setup; 4.2 Evaluation Metrics; 6 Results`；Non-proof=`https://arxiv.org/html/2606.28733v1 — §7 Conclusion; Appendix A Limitations; Failure to abstain from GPT-5.4-mini；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28733:start -->
Claim boundary：仅 arXiv:2606.28733v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28733:end -->
<!-- review:SF-2026-ARXIV-2606-28733:end -->

<!-- review:SF-2026-ARXIV-2606-28739:start -->
### 2606.28739 — Agent Safety Is Action Alignment

**问题。** 《Agent Safety Is Action Alignment》处理的问题是：Large language models increasingly act as agents: they call tools, move money, delete records, and send messages on a user's behalf.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Report GitHub Issue; Agent Safety Is Action Alignment。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Agent Safety Is Action Alignment》和上述 method locator 共同限定。 归属 `PLATFORM-SECURITY`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 5.3. Relational and Deployment-Conditioned Evaluation；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5.2. External Enforcement at the Action Boundary; 7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5.2. External Enforcement at the Action Boundary; 7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 风险管理而不是一次性认证` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28739v1 — §Report GitHub Issue; Agent Safety Is Action Alignment`；Evaluation=`https://arxiv.org/html/2606.28739v1 — §5.3. Relational and Deployment-Conditioned Evaluation`；Non-proof=`https://arxiv.org/html/2606.28739v1 — §5.2. External Enforcement at the Action Boundary; 7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28739:start -->
Claim boundary：仅 arXiv:2606.28739v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28739:end -->
<!-- review:SF-2026-ARXIV-2606-28739:end -->

<!-- review:SF-2026-ARXIV-2606-28747:start -->
### 2606.28747 — Self-Supervised Theorem Discovery in a Formal Axiomatic System

**问题。** 《Self-Supervised Theorem Discovery in a Formal Axiomatic System》处理的问题是：Recent artificial intelligence (AI) systems have shown remarkable progress in mathematical reasoning.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Self-Supervised Theorem Discovery in a Formal Axiomatic System; Rules of the Hilbert System.。在 `AGENT-WORKFLOW` 中，该路径改变或检验的具体对象由题名《Self-Supervised Theorem Discovery in a Formal Axiomatic System》和上述 method locator 共同限定。 归属 `AGENT-WORKFLOW`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 5 Experiments; 5.1 Experimental Setup; 5.2 Quantitative Evaluation of Theorem Discovery；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## State Machine 是基本模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28747v1 — §Self-Supervised Theorem Discovery in a Formal Axiomatic System; Rules of the Hilbert System.`；Evaluation=`https://arxiv.org/html/2606.28747v1 — §5 Experiments; 5.1 Experimental Setup; 5.2 Quantitative Evaluation of Theorem Discovery`；Non-proof=`https://arxiv.org/html/2606.28747v1 — §7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28747:start -->
Claim boundary：仅 arXiv:2606.28747v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28747:end -->
<!-- review:SF-2026-ARXIV-2606-28747:end -->

<!-- review:SF-2026-ARXIV-2606-28751:start -->
### 2606.28751 — A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility

**问题。** 《A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility》处理的问题是：We propose a path-space formulation of prediction in AI world models. Rather than sequences of one-step conditional distributions, we argue that a world model implicitly defines a probability measure over future trajectories.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Report GitHub Issue; A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility。在 `MULTIMODAL-WORLD-MODELS` 中，该路径改变或检验的具体对象由题名《A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility》和上述 method locator 共同限定。 归属 `MULTIMODAL-WORLD-MODELS`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 VII Results and discussion; VII.2 Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：VII Results and discussion; VII.5 Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** VII Results and discussion; VII.5 Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## State ownership` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28751v1 — §Report GitHub Issue; A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility`；Evaluation=`https://arxiv.org/html/2606.28751v1 — §VII Results and discussion; VII.2 Results`；Non-proof=`https://arxiv.org/html/2606.28751v1 — §VII Results and discussion; VII.5 Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28751:start -->
Claim boundary：仅 arXiv:2606.28751v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28751:end -->
<!-- review:SF-2026-ARXIV-2606-28751:end -->

<!-- review:SF-2026-ARXIV-2606-28754:start -->
### 2606.28754 — SHIFT: Dynamic Compute Relocation Framework for Communication-Aware Chiplet-Based Systems

**问题。** 《SHIFT: Dynamic Compute Relocation Framework for Communication-Aware Chiplet-Based Systems》处理的问题是：The increasing communication complexity of large-scale heterogeneous systems has motivated runtime methodologies for communication-aware workload placement and routing optimization.

**机制与 state/data/control owner。** exact-v1 的机制路径为 SHIFT: Dynamic Compute Relocation Framework for Communication-Aware Chiplet-Based Systems; IV SHIFT Framework; IV-A Considerations and Design Methodology。在 `PLATFORM-GPU-SCHEDULER` 中，该路径改变或检验的具体对象由题名《SHIFT: Dynamic Compute Relocation Framework for Communication-Aware Chiplet-Based Systems》和上述 method locator 共同限定。 归属 `PLATFORM-GPU-SCHEDULER`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 V Evaluations; V-A Experimental Setup; V-B Experimental Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：VI Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** VI Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## GPU 不是同质标量` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28754v1 — §SHIFT: Dynamic Compute Relocation Framework for Communication-Aware Chiplet-Based Systems; IV SHIFT Framework; IV-A Considerations and Design Methodology`；Evaluation=`https://arxiv.org/html/2606.28754v1 — §V Evaluations; V-A Experimental Setup; V-B Experimental Results`；Non-proof=`https://arxiv.org/html/2606.28754v1 — §VI Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28754:start -->
Claim boundary：仅 arXiv:2606.28754v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28754:end -->
<!-- review:SF-2026-ARXIV-2606-28754:end -->

<!-- review:SF-2026-ARXIV-2606-28757:start -->
### 2606.28757 — A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models

**问题。** 《A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models》处理的问题是：Generative world models hold immense promise as scalable simulators for autonomous systems, particularly for synthesizing rare but safety-critical multi-agent interactions, such as vehicle collisions.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Effect of Post-Training.; C Global Dynamic Reconstruction Methodology; G Post Training Details。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models; Physical-grounded Evaluation.; 3 Principles of the New Evaluation Protocol；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28757v1 — §Effect of Post-Training.; C Global Dynamic Reconstruction Methodology; G Post Training Details`；Evaluation=`https://arxiv.org/html/2606.28757v1 — §A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models; Physical-grounded Evaluation.; 3 Principles of the New Evaluation Protocol`；Non-proof=`https://arxiv.org/html/2606.28757v1 — §5 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28757:start -->
Claim boundary：仅 arXiv:2606.28757v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28757:end -->
<!-- review:SF-2026-ARXIV-2606-28757:end -->

<!-- review:SF-2026-ARXIV-2606-28758:start -->
### 2606.28758 — X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving

**问题。** 《X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving》处理的问题是：Predicting future states is essential for autonomous agents, yet current Vision-Language-Action (VLA) models fundamentally lack this capability, relying instead on reactive perception-action mapping.

**机制与 state/data/control owner。** exact-v1 的机制路径为 2 Method; 3.3 Comparison of Diffusion Architectures。在 `MULTIMODAL-WORLD-MODELS` 中，该路径改变或检验的具体对象由题名《X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving》和上述 method locator 共同限定。 归属 `MULTIMODAL-WORLD-MODELS`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 3 Experiments; 3.5 Analysis of Structured Sketch Ground Truth；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## State ownership` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28758v1 — §2 Method; 3.3 Comparison of Diffusion Architectures`；Evaluation=`https://arxiv.org/html/2606.28758v1 — §3 Experiments; 3.5 Analysis of Structured Sketch Ground Truth`；Non-proof=`https://arxiv.org/html/2606.28758v1 — §5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28758:start -->
Claim boundary：仅 arXiv:2606.28758v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28758:end -->
<!-- review:SF-2026-ARXIV-2606-28758:end -->

<!-- review:SF-2026-ARXIV-2606-28772:start -->
### 2606.28772 — Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain

**问题。** 《Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain》处理的问题是：Hate speech annotation pipelines routinely collapse annotator disagreement into majority vote labels before training.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3 Methods。在 `TRAIN-DATA` 中，该路径改变或检验的具体对象由题名《Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain》和上述 method locator 共同限定。 归属 `TRAIN-DATA`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 3.3 Statistical Analysis; 4 Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain; 4.1 Disagreement Concentrates at the Value Boundary; 4.5 Boundary Disagreement Is Not Driven by Annotation Error；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain; 4.1 Disagreement Concentrates at the Value Boundary; 4.5 Boundary Disagreement Is Not Driven by Annotation Error；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### 从 sample provenance 到训练生命周期 lineage` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28772v1 — §3 Methods`；Evaluation=`https://arxiv.org/html/2606.28772v1 — §3.3 Statistical Analysis; 4 Results`；Non-proof=`https://arxiv.org/html/2606.28772v1 — §Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain; 4.1 Disagreement Concentrates at the Value Boundary; 4.5 Boundary Disagreement Is Not Driven by Annotation Error；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28772:start -->
Claim boundary：仅 arXiv:2606.28772v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28772:end -->
<!-- review:SF-2026-ARXIV-2606-28772:end -->

<!-- review:SF-2026-ARXIV-2606-28781:start -->
### 2606.28781 — HyphaeDB: A Living Knowledge Topology for Agent-First Memory

**问题。** 《HyphaeDB: A Living Knowledge Topology for Agent-First Memory》处理的问题是：Every existing vector database and agent memory framework treats memory as passive storage that agents query explicitly.

**机制与 state/data/control owner。** exact-v1 的机制路径为 2.1 Agent Memory Systems; 3 Architecture; 4.1 Propagation Algorithm。在 `AGENT-MEMORY` 中，该路径改变或检验的具体对象由题名《HyphaeDB: A Living Knowledge Topology for Agent-First Memory》和上述 method locator 共同限定。 归属 `AGENT-MEMORY`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 6 Theoretical Analysis; 8 Competitive Analysis；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：9 Discussion; 9.2 Limitations and Future Work; 10 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 9 Discussion; 9.2 Limitations and Future Work; 10 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28781v1 — §2.1 Agent Memory Systems; 3 Architecture; 4.1 Propagation Algorithm`；Evaluation=`https://arxiv.org/html/2606.28781v1 — §6 Theoretical Analysis; 8 Competitive Analysis`；Non-proof=`https://arxiv.org/html/2606.28781v1 — §9 Discussion; 9.2 Limitations and Future Work; 10 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28781:start -->
Claim boundary：仅 arXiv:2606.28781v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28781:end -->
<!-- review:SF-2026-ARXIV-2606-28781:end -->

<!-- review:SF-2026-ARXIV-2606-28804:start -->
### 2606.28804 — ViPSim: Collaborating Visual and Parameter Spaces for Consistent Long-Horizon Embodied World Models

**问题。** 《ViPSim: Collaborating Visual and Parameter Spaces for Consistent Long-Horizon Embodied World Models》处理的问题是：Embodied World Models (EWMs) have emerged as a scalable and risk-free paradigm for advancing embodied intelligence, enabling the safety-critical evaluation of Vision-Language-Action systems.

**机制与 state/data/control owner。** exact-v1 的机制路径为 III Method。在 `MULTIMODAL-WORLD-MODELS` 中，该路径改变或检验的具体对象由题名《ViPSim: Collaborating Visual and Parameter Spaces for Consistent Long-Horizon Embodied World Models》和上述 method locator 共同限定。 归属 `MULTIMODAL-WORLD-MODELS`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 IV Experiments; IV-A Experimental Setup; IV-B Quantitative Analysis；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：V Limitations; VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** V Limitations; VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## State ownership` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28804v1 — §III Method`；Evaluation=`https://arxiv.org/html/2606.28804v1 — §IV Experiments; IV-A Experimental Setup; IV-B Quantitative Analysis`；Non-proof=`https://arxiv.org/html/2606.28804v1 — §V Limitations; VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28804:start -->
Claim boundary：仅 arXiv:2606.28804v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28804:end -->
<!-- review:SF-2026-ARXIV-2606-28804:end -->

<!-- review:SF-2026-ARXIV-2606-28813:start -->
### 2606.28813 — Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning

**问题。** 《Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning》处理的问题是：Human videos are a scalable source of supervision for robot manipulation, as they are abundant and naturally capture rich object interactions.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Training data.; Appendix E Constraint-Aware Steering Algorithm; Appendix F Model and Training Details。在 `MULTIMODAL-EMBODIED-VLA` 中，该路径改变或检验的具体对象由题名《Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning》和上述 method locator 共同限定。 归属 `MULTIMODAL-EMBODIED-VLA`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 5 Experiments; 5.1 Experimental Setup and Baselines; 5.2 Main Results: Zero-Shot Composition and Generalization；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：6 Limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 6 Limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Safety envelope` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28813v1 — §Training data.; Appendix E Constraint-Aware Steering Algorithm; Appendix F Model and Training Details`；Evaluation=`https://arxiv.org/html/2606.28813v1 — §5 Experiments; 5.1 Experimental Setup and Baselines; 5.2 Main Results: Zero-Shot Composition and Generalization`；Non-proof=`https://arxiv.org/html/2606.28813v1 — §6 Limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28813:start -->
Claim boundary：仅 arXiv:2606.28813v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28813:end -->
<!-- review:SF-2026-ARXIV-2606-28813:end -->

<!-- review:SF-2026-ARXIV-2606-28831:start -->
### 2606.28831 — HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression

**问题。** 《HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression》处理的问题是：Long-context LLM inference faces a fundamental conflict: head-adaptive compression algorithms (e.g., Top-$p$ nucleus sampling) offer superior accuracy by dynamically fluctuating memory budgets, yet modern inference engines (e.g., vLLM) demand rigid, static memory patterns to leverage CUDA Graphs and PagedAttention.

**机制与 state/data/control owner。** exact-v1 的机制路径为 System-Algorithm Co-Design in LLM Inference; 3 The Hard-KV Design; 3.1 The Framework Overview。在 `INFER-KV-CACHE` 中，该路径改变或检验的具体对象由题名《HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression》和上述 method locator 共同限定。 归属 `INFER-KV-CACHE`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Experiment; Appendix C Experiments Details; C.3 Further Experiment Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Conclusion and Future Work; Appendix B Further Discussions on KV Index Regularization; B.2 Discussion on trade-off in the Index Management for Layerwise Selection；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Conclusion and Future Work; Appendix B Further Discussions on KV Index Regularization; B.2 Discussion on trade-off in the Index Management for Layerwise Selection；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### 先判断哪一种状态超出容量，再选择 TP 或 KV Compression` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28831v1 — §System-Algorithm Co-Design in LLM Inference; 3 The Hard-KV Design; 3.1 The Framework Overview`；Evaluation=`https://arxiv.org/html/2606.28831v1 — §4 Experiment; Appendix C Experiments Details; C.3 Further Experiment Results`；Non-proof=`https://arxiv.org/html/2606.28831v1 — §5 Conclusion and Future Work; Appendix B Further Discussions on KV Index Regularization; B.2 Discussion on trade-off in the Index Management for Layerwise Selection；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28831:start -->
Claim boundary：仅 arXiv:2606.28831v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28831:end -->
<!-- review:SF-2026-ARXIV-2606-28831:end -->

<!-- review:SF-2026-ARXIV-2606-28839:start -->
### 2606.28839 — The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables

**问题。** 《The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables》处理的问题是：We introduce the Contagion Tensor, a measurement framework for quantifying how large language model (LLM) output distributions couple across modalities, agents, and time steps.

**机制与 state/data/control owner。** exact-v1 的机制路径为 The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems —and Auditing the Claims It Enables; Multi-agent LLM systems.; Network contagion and spectral methods.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 LLM bias evaluation.; 4.1.2 Experiment 1: Full CAF Matrix; 4.1.3 Experiment 2: Modality Ablation；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：4.1.4 Experiment 3: Real-API with Functional BOUNDARY_SYNC; 6 Discussion; 7 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 4.1.4 Experiment 3: Real-API with Functional BOUNDARY_SYNC; 6 Discussion; 7 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28839v1 — §The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems —and Auditing the Claims It Enables; Multi-agent LLM systems.; Network contagion and spectral methods.`；Evaluation=`https://arxiv.org/html/2606.28839v1 — §LLM bias evaluation.; 4.1.2 Experiment 1: Full CAF Matrix; 4.1.3 Experiment 2: Modality Ablation`；Non-proof=`https://arxiv.org/html/2606.28839v1 — §4.1.4 Experiment 3: Real-API with Functional BOUNDARY_SYNC; 6 Discussion; 7 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28839:start -->
Claim boundary：仅 arXiv:2606.28839v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28839:end -->
<!-- review:SF-2026-ARXIV-2606-28839:end -->

<!-- review:SF-2026-ARXIV-2606-28841:start -->
### 2606.28841 — LAMP: Lean-based Agentic framework with MCP and Proof Repair

**问题。** 《LAMP: Lean-based Agentic framework with MCP and Proof Repair》处理的问题是：Large language models are increasingly capable of mathematical reasoning, but the proofs they generate are often unreliable and hard to verify.

**机制与 state/data/control owner。** exact-v1 的机制路径为 LAMP: Lean-based Agentic framework with MCP and Proof Repair; 2.3 Agentic Frameworks for Theorem Proving; 3 The LAMP System。在 `AGENT-WORKFLOW` 中，该路径改变或检验的具体对象由题名《LAMP: Lean-based Agentic framework with MCP and Proof Repair》和上述 method locator 共同限定。 归属 `AGENT-WORKFLOW`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Experimental Results; 4.1 Experimental Setup; Evaluation suite:；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Discussion and Limitations; Failure Analysis:; Limitations and Future Work:；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Discussion and Limitations; Failure Analysis:; Limitations and Future Work:；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## State Machine 是基本模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28841v1 — §LAMP: Lean-based Agentic framework with MCP and Proof Repair; 2.3 Agentic Frameworks for Theorem Proving; 3 The LAMP System`；Evaluation=`https://arxiv.org/html/2606.28841v1 — §4 Experimental Results; 4.1 Experimental Setup; Evaluation suite:`；Non-proof=`https://arxiv.org/html/2606.28841v1 — §5 Discussion and Limitations; Failure Analysis:; Limitations and Future Work:；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28841:start -->
Claim boundary：仅 arXiv:2606.28841v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28841:end -->
<!-- review:SF-2026-ARXIV-2606-28841:end -->

<!-- review:SF-2026-ARXIV-2606-28843:start -->
### 2606.28843 — The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning

**问题。** 《The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning》处理的问题是：Fine-tuning a large language model is a ubiquitous method for enhancing its capability on a specific downstream task.

**机制与 state/data/control owner。** exact-v1 的机制路径为 5.3 Pre-training distributions and scale。在 `TRAIN-SFT` 中，该路径改变或检验的具体对象由题名《The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning》和上述 method locator 共同限定。 归属 `TRAIN-SFT`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 3 Experimental Set Up; 3.2 Evaluation Protocol; 4 Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：7 Discussion; 7.2 Limitations; 8 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 7 Discussion; 7.2 Limitations; 8 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation 应分开能力与行为` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28843v1 — §5.3 Pre-training distributions and scale`；Evaluation=`https://arxiv.org/html/2606.28843v1 — §3 Experimental Set Up; 3.2 Evaluation Protocol; 4 Results`；Non-proof=`https://arxiv.org/html/2606.28843v1 — §7 Discussion; 7.2 Limitations; 8 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28843:start -->
Claim boundary：仅 arXiv:2606.28843v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28843:end -->
<!-- review:SF-2026-ARXIV-2606-28843:end -->

<!-- review:SF-2026-ARXIV-2606-28862:start -->
### 2606.28862 — HKVLM: Faithful Query--Region Binding for Frozen-Detector Visual Grounding

**问题。** 《HKVLM: Faithful Query--Region Binding for Frozen-Detector Visual Grounding》处理的问题是：Visual grounding often fails even when the target object is present in the proposal pool, because the language-side referent is bound to the wrong region.

**机制与 state/data/control owner。** exact-v1 的机制路径为 4 Method: HKVLM; 4.5 Cold-start training; 5 Experimental Design and Evaluation Protocol。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《HKVLM: Faithful Query--Region Binding for Frozen-Detector Visual Grounding》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Hallucination evaluation.; 5 Experimental Design and Evaluation Protocol; 6 Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：8 Discussion, Limitations, and Broader Impact; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 8 Discussion, Limitations, and Broader Impact; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28862v1 — §4 Method: HKVLM; 4.5 Cold-start training; 5 Experimental Design and Evaluation Protocol`；Evaluation=`https://arxiv.org/html/2606.28862v1 — §Hallucination evaluation.; 5 Experimental Design and Evaluation Protocol; 6 Results`；Non-proof=`https://arxiv.org/html/2606.28862v1 — §8 Discussion, Limitations, and Broader Impact; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28862:start -->
Claim boundary：仅 arXiv:2606.28862v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28862:end -->
<!-- review:SF-2026-ARXIV-2606-28862:end -->

<!-- review:SF-2026-ARXIV-2606-28863:start -->
### 2606.28863 — Defeat Devices in AI Systems

**问题。** 《Defeat Devices in AI Systems》处理的问题是：AI systems increasingly exhibit behavior that differs systematically between evaluation and deployment contexts.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Defeat Devices in AI Systems; 4.1 Five method families; 5.1 Defeat devices can naturally emerge in AI systems。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Defeat Devices in AI Systems》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 5.5 Four decisive experiments; 6.1 Evaluation methodology；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：2.4 Boundary cases; 6.5 Limitations; 7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 2.4 Boundary cases; 6.5 Limitations; 7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28863v1 — §Defeat Devices in AI Systems; 4.1 Five method families; 5.1 Defeat devices can naturally emerge in AI systems`；Evaluation=`https://arxiv.org/html/2606.28863v1 — §5.5 Four decisive experiments; 6.1 Evaluation methodology`；Non-proof=`https://arxiv.org/html/2606.28863v1 — §2.4 Boundary cases; 6.5 Limitations; 7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28863:start -->
Claim boundary：仅 arXiv:2606.28863v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28863:end -->
<!-- review:SF-2026-ARXIV-2606-28863:end -->

<!-- review:SF-2026-ARXIV-2606-28864:start -->
### 2606.28864 — On Test-Time Scaling for Vision-Language Models

**问题。** 《On Test-Time Scaling for Vision-Language Models》处理的问题是：Test-time scaling is a paradigm where large models use additional compute at inference to achieve better performance, without changing model weights.

**机制与 state/data/control owner。** exact-v1 的机制路径为 S11 Method Parameters。在 `INFER-REQUEST-LIFECYCLE` 中，该路径改变或检验的具体对象由题名《On Test-Time Scaling for Vision-Language Models》和上述 method locator 共同限定。 归属 `INFER-REQUEST-LIFECYCLE`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Experiments and Takeaways; 6 Analysis of Multimodal Chain-of-Thoughts; S1 InternVL-3.5 Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：7 Conclusion; S12 Other model failures；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 7 Conclusion; S12 Other model failures；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 请求状态机` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28864v1 — §S11 Method Parameters`；Evaluation=`https://arxiv.org/html/2606.28864v1 — §4 Experiments and Takeaways; 6 Analysis of Multimodal Chain-of-Thoughts; S1 InternVL-3.5 Results`；Non-proof=`https://arxiv.org/html/2606.28864v1 — §7 Conclusion; S12 Other model failures；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28864:start -->
Claim boundary：仅 arXiv:2606.28864v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28864:end -->
<!-- review:SF-2026-ARXIV-2606-28864:end -->

<!-- review:SF-2026-ARXIV-2606-28867:start -->
### 2606.28867 — Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages

**问题。** 《Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages》处理的问题是：Creative Commons licenses dominate African NLP corpus releases, but their compatibility rules are rarely applied.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Legal analysis of AI training data.。在 `TRAIN-DATA` 中，该路径改变或检验的具体对象由题名《Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages》和上述 method locator 共同限定。 归属 `TRAIN-DATA`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages; Legal analysis of AI training data.；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：6. Four Failure Modes; 6.4. Data Persistence Failure: The Congolese Radio Corpus; 9. Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 6. Four Failure Modes; 6.4. Data Persistence Failure: The Congolese Radio Corpus; 9. Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### 从 sample provenance 到训练生命周期 lineage` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28867v1 — §Legal analysis of AI training data.`；Evaluation=`https://arxiv.org/html/2606.28867v1 — §Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages; Legal analysis of AI training data.`；Non-proof=`https://arxiv.org/html/2606.28867v1 — §6. Four Failure Modes; 6.4. Data Persistence Failure: The Congolese Radio Corpus; 9. Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28867:start -->
Claim boundary：仅 arXiv:2606.28867v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28867:end -->
<!-- review:SF-2026-ARXIV-2606-28867:end -->

<!-- review:SF-2026-ARXIV-2606-28876:start -->
### 2606.28876 — Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory

**问题。** 《Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory》处理的问题是：Long-context language models often conflate two different goals: compressing history into an efficient state, and maintaining reliable long-term memory.

**机制与 state/data/control owner。** exact-v1 的机制路径为 2 Method Sketch。在 `MODEL-LONG-CONTEXT` 中，该路径改变或检验的具体对象由题名《Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory》和上述 method locator 共同限定。 归属 `MODEL-LONG-CONTEXT`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 3 Experimental Route; 4 Results; Why frozen-model evaluation is still useful.；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Discussion; 8 Limitations and Next Steps; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Discussion; 8 Limitations and Next Steps; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### 从 Dense Checkpoint 迁移到 Hybrid State Model` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28876v1 — §2 Method Sketch`；Evaluation=`https://arxiv.org/html/2606.28876v1 — §3 Experimental Route; 4 Results; Why frozen-model evaluation is still useful.`；Non-proof=`https://arxiv.org/html/2606.28876v1 — §5 Discussion; 8 Limitations and Next Steps; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28876:start -->
Claim boundary：仅 arXiv:2606.28876v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28876:end -->
<!-- review:SF-2026-ARXIV-2606-28876:end -->

<!-- review:SF-2026-ARXIV-2606-28896:start -->
### 2606.28896 — A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation

**问题。** 《A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation》处理的问题是：Synthetic aperture radar (SAR) data augmentation is important for improving the generalization of data-driven SAR interpretation models, yet practical augmentation workflows are often hindered by heterogeneous dataset formats, task-dependent metadata requirements, diverse generation methods, and weak validation of generated samples.

**机制与 state/data/control owner。** exact-v1 的机制路径为 A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation; 3 Method; 3.1 Problem Formulation and System Overview。在 `AGENT-WORKFLOW` 中，该路径改变或检验的具体对象由题名《A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation》和上述 method locator 共同限定。 归属 `AGENT-WORKFLOW`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 2.4 Tool-Augmented LLM Agents and Evaluation; 3.5 Observer-Driven Evaluation and Bounded Repair; 4 Experiments；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## State Machine 是基本模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28896v1 — §A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation; 3 Method; 3.1 Problem Formulation and System Overview`；Evaluation=`https://arxiv.org/html/2606.28896v1 — §2.4 Tool-Augmented LLM Agents and Evaluation; 3.5 Observer-Driven Evaluation and Bounded Repair; 4 Experiments`；Non-proof=`https://arxiv.org/html/2606.28896v1 — §5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28896:start -->
Claim boundary：仅 arXiv:2606.28896v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28896:end -->
<!-- review:SF-2026-ARXIV-2606-28896:end -->

<!-- review:SF-2026-ARXIV-2606-28898:start -->
### 2606.28898 — PASTA: A Paraphrasing And Self-Training Approach for Knowledge Updating in LLMs

**问题。** 《PASTA: A Paraphrasing And Self-Training Approach for Knowledge Updating in LLMs》处理的问题是：Knowledge updating in pre-trained Large Language Models (LLMs) remains an important challenge.

**机制与 state/data/control owner。** exact-v1 的机制路径为 PASTA: A Paraphrasing And Self-Training Approach for Knowledge Updating in LLMs; 3 Proposed Method; 3.1 Design Motivations。在 `TRAIN-DPO` 中，该路径改变或检验的具体对象由题名《PASTA: A Paraphrasing And Self-Training Approach for Knowledge Updating in LLMs》和上述 method locator 共同限定。 归属 `TRAIN-DPO`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Experiments; 4.2 Experimental Setup; 4.3 Evaluation Methods；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Conclusion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Conclusion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## KL-constrained 最优策略` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28898v1 — §PASTA: A Paraphrasing And Self-Training Approach for Knowledge Updating in LLMs; 3 Proposed Method; 3.1 Design Motivations`；Evaluation=`https://arxiv.org/html/2606.28898v1 — §4 Experiments; 4.2 Experimental Setup; 4.3 Evaluation Methods`；Non-proof=`https://arxiv.org/html/2606.28898v1 — §5 Conclusion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28898:start -->
Claim boundary：仅 arXiv:2606.28898v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28898:end -->
<!-- review:SF-2026-ARXIV-2606-28898:end -->

<!-- review:SF-2026-ARXIV-2606-28900:start -->
### 2606.28900 — MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes

**问题。** 《MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes》处理的问题是：Doctor agents are moving beyond single-turn answer generation toward evolving clinical decision systems.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Design goals.; Training-oriented derivatives.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Medical QA and fixed-input evaluation.; Memory, retrieval, and continual evaluation.; 3 MedEvoEval : An Executable Evaluation Protocol；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：6 Discussion, Limitations, and Ethics; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 6 Discussion, Limitations, and Ethics; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28900v1 — §Design goals.; Training-oriented derivatives.`；Evaluation=`https://arxiv.org/html/2606.28900v1 — §Medical QA and fixed-input evaluation.; Memory, retrieval, and continual evaluation.; 3 MedEvoEval : An Executable Evaluation Protocol`；Non-proof=`https://arxiv.org/html/2606.28900v1 — §6 Discussion, Limitations, and Ethics; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28900:start -->
Claim boundary：仅 arXiv:2606.28900v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28900:end -->
<!-- review:SF-2026-ARXIV-2606-28900:end -->

<!-- review:SF-2026-ARXIV-2606-28925:start -->
### 2606.28925 — Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation

**问题。** 《Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation》处理的问题是：Tool and agent routing from natural-language prompts is naturally a set-valued prediction problem: a single query may require multiple agents, while over-selection increases execution cost.

**机制与 state/data/control owner。** exact-v1 的机制路径为 2.1. Tool/Agent Routing in LLM Systems; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 2.6. Multi-Agent Systems and Task Decomposition。在 `AGENT-MULTI-AGENT` 中，该路径改变或检验的具体对象由题名《Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation》和上述 method locator 共同限定。 归属 `AGENT-MULTI-AGENT`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 3.1. Problem setup and notation；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：7. Discussion; 8. Limitations; 10. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 7. Discussion; 8. Limitations; 10. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### Pairwise coupling 不能外推 group dynamics` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28925v1 — §2.1. Tool/Agent Routing in LLM Systems; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 2.6. Multi-Agent Systems and Task Decomposition`；Evaluation=`https://arxiv.org/html/2606.28925v1 — §Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 3.1. Problem setup and notation`；Non-proof=`https://arxiv.org/html/2606.28925v1 — §7. Discussion; 8. Limitations; 10. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28925:start -->
Claim boundary：仅 arXiv:2606.28925v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28925:end -->
<!-- review:SF-2026-ARXIV-2606-28925:end -->

<!-- review:SF-2026-ARXIV-2606-28932:start -->
### 2606.28932 — DLR: Zero-Inference-Cost Latent Residuals for Low-Rank Pre-Training

**问题。** 《DLR: Zero-Inference-Cost Latent Residuals for Low-Rank Pre-Training》处理的问题是：Large language models have driven recent progress in language and multimodal AI, yet pre-training them at scale is prohibitively expensive.

**机制与 state/data/control owner。** exact-v1 的机制路径为 DLR: Zero-Inference-Cost Latent Residuals for Low-Rank Pre-Training; 2 Low-rank efficient pre-training; Appendix D The impact of DLR on training dynamics。在 `TRAIN-PRETRAINING` 中，该路径改变或检验的具体对象由题名《DLR: Zero-Inference-Cost Latent Residuals for Low-Rank Pre-Training》和上述 method locator 共同限定。 归属 `TRAIN-PRETRAINING`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 2.1 Setup and a Unified View; 4 Experiments; 4.1 Evaluation Setup and Protocol；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Conclusion, Limitations and Outlook；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Conclusion, Limitations and Outlook；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 一次 training step 的状态流` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28932v1 — §DLR: Zero-Inference-Cost Latent Residuals for Low-Rank Pre-Training; 2 Low-rank efficient pre-training; Appendix D The impact of DLR on training dynamics`；Evaluation=`https://arxiv.org/html/2606.28932v1 — §2.1 Setup and a Unified View; 4 Experiments; 4.1 Evaluation Setup and Protocol`；Non-proof=`https://arxiv.org/html/2606.28932v1 — §5 Conclusion, Limitations and Outlook；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28932:start -->
Claim boundary：仅 arXiv:2606.28932v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28932:end -->
<!-- review:SF-2026-ARXIV-2606-28932:end -->

<!-- review:SF-2026-ARXIV-2606-28938:start -->
### 2606.28938 — EVLA: An Electro-Aware Multimodal Assistant for Physically-Grounded Driving Reasoning and Control

**问题。** 《EVLA: An Electro-Aware Multimodal Assistant for Physically-Grounded Driving Reasoning and Control》处理的问题是：Modern vision-language models (VLMs) for driving assistants typically treat vehicle dynamics as a black box, resulting in decisions that lack awareness of the vehicle's real-time electro-mechanical state.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3 Methodology: Electro-Visual-Language Assistant (EVLA); 3.4 Physics-Guided Joint Training Objective; 3.5 Implementation and Training Details。在 `MULTIMODAL-EMBODIED-VLA` 中，该路径改变或检验的具体对象由题名《EVLA: An Electro-Aware Multimodal Assistant for Physically-Grounded Driving Reasoning and Control》和上述 method locator 共同限定。 归属 `MULTIMODAL-EMBODIED-VLA`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Experiments; 4.3 Evaluation and Main Results; 4.7 Parameter Sensitivity Analysis；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：4.8 Discussion; 5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 4.8 Discussion; 5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Safety envelope` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28938v1 — §3 Methodology: Electro-Visual-Language Assistant (EVLA); 3.4 Physics-Guided Joint Training Objective; 3.5 Implementation and Training Details`；Evaluation=`https://arxiv.org/html/2606.28938v1 — §4 Experiments; 4.3 Evaluation and Main Results; 4.7 Parameter Sensitivity Analysis`；Non-proof=`https://arxiv.org/html/2606.28938v1 — §4.8 Discussion; 5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28938:start -->
Claim boundary：仅 arXiv:2606.28938v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28938:end -->
<!-- review:SF-2026-ARXIV-2606-28938:end -->

<!-- review:SF-2026-ARXIV-2606-28939:start -->
### 2606.28939 — ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies

**问题。** 《ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies》处理的问题是：Behavior-cloned diffusion policies are expressive but remain vulnerable to covariate shift: small deviations from demonstrated states can compound into task failure.

**机制与 state/data/control owner。** exact-v1 的机制路径为 4 Our Approach: ReGuide; Appendix B Algorithm。在 `MULTIMODAL-EMBODIED-VLA` 中，该路径改变或检验的具体对象由题名《ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies》和上述 method locator 共同限定。 归属 `MULTIMODAL-EMBODIED-VLA`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 5 Experiments; Appendix D Setup Details；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：6 Conclusion and Limitations; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 6 Conclusion and Limitations; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Safety envelope` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28939v1 — §4 Our Approach: ReGuide; Appendix B Algorithm`；Evaluation=`https://arxiv.org/html/2606.28939v1 — §5 Experiments; Appendix D Setup Details`；Non-proof=`https://arxiv.org/html/2606.28939v1 — §6 Conclusion and Limitations; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28939:start -->
Claim boundary：仅 arXiv:2606.28939v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28939:end -->
<!-- review:SF-2026-ARXIV-2606-28939:end -->

<!-- review:SF-2026-ARXIV-2606-28953:start -->
### 2606.28953 — Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System

**问题。** 《Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System》处理的问题是：Poisoning attacks entail attackers intentionally tampering with training data. In this paper, we consider a dirty-label poisoning attack scenario on a speech commands classification system.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 4.5 Proposed defense vs prior methods; 5.1 Proposed defense vs prior methods。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System》和上述 method locator 共同限定。 归属 `PLATFORM-SECURITY`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 3.4 Linear Discriminant Analysis; 4 Experimental set-up; 5 Results and Discussion；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 2 Threat Model; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 2 Threat Model; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 风险管理而不是一次性认证` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28953v1 — §Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 4.5 Proposed defense vs prior methods; 5.1 Proposed defense vs prior methods`；Evaluation=`https://arxiv.org/html/2606.28953v1 — §3.4 Linear Discriminant Analysis; 4 Experimental set-up; 5 Results and Discussion`；Non-proof=`https://arxiv.org/html/2606.28953v1 — §Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 2 Threat Model; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28953:start -->
Claim boundary：仅 arXiv:2606.28953v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28953:end -->
<!-- review:SF-2026-ARXIV-2606-28953:end -->

<!-- review:SF-2026-ARXIV-2606-28955:start -->
### 2606.28955 — Modification-Considering Value Learning for Reward Hacking Mitigation in RL

**问题。** 《Modification-Considering Value Learning for Reward Hacking Mitigation in RL》处理的问题是：Reinforcement learning agents can exploit misspecified reward signals to achieve high apparent returns while failing on the intended objective, a failure mode known as reward hacking.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3 Method; Pretraining.; Pretraining budget.。在 `TRAIN-RLHF` 中，该路径改变或检验的具体对象由题名《Modification-Considering Value Learning for Reward Hacking Mitigation in RL》和上述 method locator 共同限定。 归属 `TRAIN-RLHF`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Theoretical analysis.; 4 Experiments; 4.2 Main results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Limitations and Future Work; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Limitations and Future Work; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Reward hacking 与 Goodhart's Law` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28955v1 — §3 Method; Pretraining.; Pretraining budget.`；Evaluation=`https://arxiv.org/html/2606.28955v1 — §Theoretical analysis.; 4 Experiments; 4.2 Main results`；Non-proof=`https://arxiv.org/html/2606.28955v1 — §5 Limitations and Future Work; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28955:start -->
Claim boundary：仅 arXiv:2606.28955v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28955:end -->
<!-- review:SF-2026-ARXIV-2606-28955:end -->

<!-- review:SF-2026-ARXIV-2606-28958:start -->
### 2606.28958 — When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration

**问题。** 《When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration》处理的问题是：LLM agents can share more than text. In some systems, an agent can send a short visible message while also passing its full KV-cache state to another model.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Report GitHub Issue; When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration。在 `AGENT-MULTI-AGENT` 中，该路径改变或检验的具体对象由题名《When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration》和上述 method locator 共同限定。 归属 `AGENT-MULTI-AGENT`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 5 Benchmark and Experimental Setup; 8 Defense Diagnostics and Trade-Off Analysis；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：3 Problem Setting and Threat Model; 8.4 Transport Integrity and Fail-Closed Boundary; 9 Failure Modes and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 3 Problem Setting and Threat Model; 8.4 Transport Integrity and Fail-Closed Boundary; 9 Failure Modes and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### Pairwise coupling 不能外推 group dynamics` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28958v1 — §Report GitHub Issue; When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration`；Evaluation=`https://arxiv.org/html/2606.28958v1 — §5 Benchmark and Experimental Setup; 8 Defense Diagnostics and Trade-Off Analysis`；Non-proof=`https://arxiv.org/html/2606.28958v1 — §3 Problem Setting and Threat Model; 8.4 Transport Integrity and Fail-Closed Boundary; 9 Failure Modes and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28958:start -->
Claim boundary：仅 arXiv:2606.28958v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28958:end -->
<!-- review:SF-2026-ARXIV-2606-28958:end -->

<!-- review:SF-2026-ARXIV-2606-28962:start -->
### 2606.28962 — FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks

**问题。** 《FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks》处理的问题是：Model quantization is essential for the efficient deployment of Large Language Models (LLMs), but introduces a critical vulnerability: Quantization-Conditioned Backdoor (QCB) attacks.

**机制与 state/data/control owner。** exact-v1 的机制路径为 III Methodology; III-B Defense Framework Design; III-C Defense Metric Design。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks》和上述 method locator 共同限定。 归属 `PLATFORM-SECURITY`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 IV Experiments; IV-A Experimental Setup; IV-B Experimental Scenarios and Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：III-A Threat Model; V Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** III-A Threat Model; V Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 风险管理而不是一次性认证` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28962v1 — §III Methodology; III-B Defense Framework Design; III-C Defense Metric Design`；Evaluation=`https://arxiv.org/html/2606.28962v1 — §IV Experiments; IV-A Experimental Setup; IV-B Experimental Scenarios and Results`；Non-proof=`https://arxiv.org/html/2606.28962v1 — §III-A Threat Model; V Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28962:start -->
Claim boundary：仅 arXiv:2606.28962v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28962:end -->
<!-- review:SF-2026-ARXIV-2606-28962:end -->

<!-- review:SF-2026-ARXIV-2606-28995:start -->
### 2606.28995 — HJ-SafeDMP: Hamilton-Jacobi Reachability-Guided Dynamic Movement Primitives for Provably Safe Robot Motion

**问题。** 《HJ-SafeDMP: Hamilton-Jacobi Reachability-Guided Dynamic Movement Primitives for Provably Safe Robot Motion》处理的问题是：Robots deployed in safety-critical environments must execute motions that are simultaneously robust to disturbances and provably safe from collisions.

**机制与 state/data/control owner。** exact-v1 的机制路径为 IV Methodology; V-A 3 CBVF Training Details。在 `MULTIMODAL-EMBODIED-VLA` 中，该路径改变或检验的具体对象由题名《HJ-SafeDMP: Hamilton-Jacobi Reachability-Guided Dynamic Movement Primitives for Provably Safe Robot Motion》和上述 method locator 共同限定。 归属 `MULTIMODAL-EMBODIED-VLA`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 III Background and Problem Setup; V Experiments; V-A Experimental Setup；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：VI Conclusion, Limitations and Future Works；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** VI Conclusion, Limitations and Future Works；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Safety envelope` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28995v1 — §IV Methodology; V-A 3 CBVF Training Details`；Evaluation=`https://arxiv.org/html/2606.28995v1 — §III Background and Problem Setup; V Experiments; V-A Experimental Setup`；Non-proof=`https://arxiv.org/html/2606.28995v1 — §VI Conclusion, Limitations and Future Works；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28995:start -->
Claim boundary：仅 arXiv:2606.28995v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28995:end -->
<!-- review:SF-2026-ARXIV-2606-28995:end -->

<!-- review:SF-2026-ARXIV-2606-28998:start -->
### 2606.28998 — Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation

**问题。** 《Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation》处理的问题是：Large Language Model (LLM) alignment trains an LLM using preference data to produce outputs that better meet established quality standards.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3. Methodology。在 `TRAIN-DPO` 中，该路径改变或检验的具体对象由题名《Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation》和上述 method locator 共同限定。 归属 `TRAIN-DPO`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 3.4. Evaluation Benchmarks; 3.4.1. Evaluation on Functional Benchmarks; 3.4.2. Evaluation on Non-Functional Benchmarks；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：3.6. Threats to Validity; Small Model Limitations; Failure Cases；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 3.6. Threats to Validity; Small Model Limitations; Failure Cases；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## KL-constrained 最优策略` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.28998v1 — §3. Methodology`；Evaluation=`https://arxiv.org/html/2606.28998v1 — §3.4. Evaluation Benchmarks; 3.4.1. Evaluation on Functional Benchmarks; 3.4.2. Evaluation on Non-Functional Benchmarks`；Non-proof=`https://arxiv.org/html/2606.28998v1 — §3.6. Threats to Validity; Small Model Limitations; Failure Cases；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-28998:start -->
Claim boundary：仅 arXiv:2606.28998v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28998:end -->
<!-- review:SF-2026-ARXIV-2606-28998:end -->

<!-- review:SF-2026-ARXIV-2606-29013:start -->
### 2606.29013 — Mural: Transferring LLM knowledge to image generation via Mixture-of-Transformers

**问题。** 《Mural: Transferring LLM knowledge to image generation via Mixture-of-Transformers》处理的问题是：Leveraging capabilities of large language models (LLMs) in text-to-image (T2I) synthesis is an important research direction.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3 Framework; 3.2 Training protocol。在 `MULTIMODAL-GENERATIVE-PARADIGMS` 中，该路径改变或检验的具体对象由题名《Mural: Transferring LLM knowledge to image generation via Mixture-of-Transformers》和上述 method locator 共同限定。 归属 `MULTIMODAL-GENERATIVE-PARADIGMS`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 3.1 Model setup; 4 Experiments；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Cache、rollback 与 exactness` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29013v1 — §3 Framework; 3.2 Training protocol`；Evaluation=`https://arxiv.org/html/2606.29013v1 — §3.1 Model setup; 4 Experiments`；Non-proof=`https://arxiv.org/html/2606.29013v1 — §5 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29013:start -->
Claim boundary：仅 arXiv:2606.29013v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29013:end -->
<!-- review:SF-2026-ARXIV-2606-29013:end -->

<!-- review:SF-2026-ARXIV-2606-29030:start -->
### 2606.29030 — Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering

**问题。** 《Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering》处理的问题是：AI agents extend conventional large language model (LLM) applications by integrating language understanding with task execution, external tool use, and memory mechanisms.

**机制与 state/data/control owner。** exact-v1 的机制路径为 III Architecture of the Proposed Agent。在 `AGENT-MEMORY` 中，该路径改变或检验的具体对象由题名《Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering》和上述 method locator 共同限定。 归属 `AGENT-MEMORY`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 V Numerical Results; V-A Experimental Dataset and Model Setup; V-B Comparison across Benchmarks and Model Backends；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29030v1 — §III Architecture of the Proposed Agent`；Evaluation=`https://arxiv.org/html/2606.29030v1 — §V Numerical Results; V-A Experimental Dataset and Model Setup; V-B Comparison across Benchmarks and Model Backends`；Non-proof=`https://arxiv.org/html/2606.29030v1 — §VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29030:start -->
Claim boundary：仅 arXiv:2606.29030v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29030:end -->
<!-- review:SF-2026-ARXIV-2606-29030:end -->

<!-- review:SF-2026-ARXIV-2606-29033:start -->
### 2606.29033 — Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations

**问题。** 《Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations》处理的问题是：Evaluating AI/Agentic system outputs reliably requires human judgment, but how one incorporates the human determines whether one gets a real quality signal or expensive theater.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Approach 1: Human Verification of AI Proposals.; Approach 2: Manual Test Sets.; Approach 3: Humans Specify Criteria, AI Applies Them at Scale.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations; 4. Avoiding Evaluation Tropes；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：6. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 6. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29033v1 — §Approach 1: Human Verification of AI Proposals.; Approach 2: Manual Test Sets.; Approach 3: Humans Specify Criteria, AI Applies Them at Scale.`；Evaluation=`https://arxiv.org/html/2606.29033v1 — §Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations; 4. Avoiding Evaluation Tropes`；Non-proof=`https://arxiv.org/html/2606.29033v1 — §6. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29033:start -->
Claim boundary：仅 arXiv:2606.29033v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29033:end -->
<!-- review:SF-2026-ARXIV-2606-29033:end -->

<!-- review:SF-2026-ARXIV-2606-29038:start -->
### 2606.29038 — Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy

**问题。** 《Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy》处理的问题是：Metric aggregation divergence (MAD) is the silent inconsistency that arises when distinct pipeline stages in an agent-based model coupled with a multi-objective evolutionary algorithm (ABM+MOEA) independently re-implement how an outcome metric is extracted from simulation trajectories.

**机制与 state/data/control owner。** exact-v1 的机制路径为 2 Pipeline Architecture and Metric Aggregation Divergence; 2.4 Positioning: Pipeline Architecture as Unregistered Degrees of Freedom。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 3.2 Controlled Aggregation Experiment (EA-2); Appendix A Experiment Parameters；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy; 6 Discussion; 7 Limitations and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy; 6 Discussion; 7 Limitations and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29038v1 — §2 Pipeline Architecture and Metric Aggregation Divergence; 2.4 Positioning: Pipeline Architecture as Unregistered Degrees of Freedom`；Evaluation=`https://arxiv.org/html/2606.29038v1 — §3.2 Controlled Aggregation Experiment (EA-2); Appendix A Experiment Parameters`；Non-proof=`https://arxiv.org/html/2606.29038v1 — §Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy; 6 Discussion; 7 Limitations and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29038:start -->
Claim boundary：仅 arXiv:2606.29038v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29038:end -->
<!-- review:SF-2026-ARXIV-2606-29038:end -->

<!-- review:SF-2026-ARXIV-2606-29054:start -->
### 2606.29054 — When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation

**问题。** 《When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation》处理的问题是：Large language models (LLMs) deployed for structured generation (NER, JSON extraction, QA, and classification) lack formal reliability guarantees, and standard heuristic abstention policies miss user-specified risk targets by 7.5--12.5%.

**机制与 state/data/control owner。** exact-v1 的机制路径为 2 Method; Ministral violations expose framework limits.; Practical decision framework.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Problem setup.; 3 Experiments; 3.1 Setup；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：4 Discussion; 6 Conclusion; Threats to validity and limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 4 Discussion; 6 Conclusion; Threats to validity and limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29054v1 — §2 Method; Ministral violations expose framework limits.; Practical decision framework.`；Evaluation=`https://arxiv.org/html/2606.29054v1 — §Problem setup.; 3 Experiments; 3.1 Setup`；Non-proof=`https://arxiv.org/html/2606.29054v1 — §4 Discussion; 6 Conclusion; Threats to validity and limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29054:start -->
Claim boundary：仅 arXiv:2606.29054v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29054:end -->
<!-- review:SF-2026-ARXIV-2606-29054:end -->

<!-- review:SF-2026-ARXIV-2606-29059:start -->
### 2606.29059 — Flow Matching in Feature Space for Stochastic World Modeling

**问题。** 《Flow Matching in Feature Space for Stochastic World Modeling》处理的问题是：World modeling requires forecasting uncertain futures while preserving information useful for downstream perception.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3 The Proposed Method: FlowWM; 3.3 Training Objectives。在 `MULTIMODAL-WORLD-MODELS` 中，该路径改变或检验的具体对象由题名《Flow Matching in Feature Space for Stochastic World Modeling》和上述 method locator 共同限定。 归属 `MULTIMODAL-WORLD-MODELS`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Latent World Model Benchmarks; 4.1 Synthetic Benchmark: Bouncing Shapes; 4.2 Real-world Benchmark: FuturePerception；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：6 Conclusion; Practical limitations.; Appendix J Discussion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 6 Conclusion; Practical limitations.; Appendix J Discussion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## State ownership` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29059v1 — §3 The Proposed Method: FlowWM; 3.3 Training Objectives`；Evaluation=`https://arxiv.org/html/2606.29059v1 — §4 Latent World Model Benchmarks; 4.1 Synthetic Benchmark: Bouncing Shapes; 4.2 Real-world Benchmark: FuturePerception`；Non-proof=`https://arxiv.org/html/2606.29059v1 — §6 Conclusion; Practical limitations.; Appendix J Discussion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29059:start -->
Claim boundary：仅 arXiv:2606.29059v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29059:end -->
<!-- review:SF-2026-ARXIV-2606-29059:end -->

<!-- review:SF-2026-ARXIV-2606-29066:start -->
### 2606.29066 — $x$-Prediction Flow: Efficient Continuous Decoding for Masked Diffusion Language Models

**问题。** 《$x$-Prediction Flow: Efficient Continuous Decoding for Masked Diffusion Language Models》处理的问题是：Masked diffusion language models (MDLMs) generate text by iteratively unmasking tokens, but their standard decoder reduces each step to a binary action: a position is either committed to a single token or left fully masked, discarding rich predictive information rather than carrying it forward, and forcing premature, irrevocable commitments that lead to poor performance under a limited decoding budget.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Training objective; 4 Training; 4.2 Step-Size Policy Training。在 `INFER-DECODE` 中，该路径改变或检验的具体对象由题名《$x$-Prediction Flow: Efficient Continuous Decoding for Masked Diffusion Language Models》和上述 method locator 共同限定。 归属 `INFER-DECODE`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 5 Experiments; 5.3 Code Generation Evaluation; Setup；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：7 Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 7 Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Decode 的结束条件` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29066v1 — §Training objective; 4 Training; 4.2 Step-Size Policy Training`；Evaluation=`https://arxiv.org/html/2606.29066v1 — §5 Experiments; 5.3 Code Generation Evaluation; Setup`；Non-proof=`https://arxiv.org/html/2606.29066v1 — §7 Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29066:start -->
Claim boundary：仅 arXiv:2606.29066v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29066:end -->
<!-- review:SF-2026-ARXIV-2606-29066:end -->

<!-- review:SF-2026-ARXIV-2606-29067:start -->
### 2606.29067 — ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs

**问题。** 《ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs》处理的问题是：We present ThinkProbe, a framework for structural analysis of LLM reasoning traces.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3 Method; H.1 Study Design。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Graph-based trace analysis.; Layer 4: Cross-segment analysis.; 4 Experimental Protocol；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：Layer 1: Structural segmentation and boundary classification.; Layer 2: Soft boundary detection.; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** Layer 1: Structural segmentation and boundary classification.; Layer 2: Soft boundary detection.; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29067v1 — §3 Method; H.1 Study Design`；Evaluation=`https://arxiv.org/html/2606.29067v1 — §Graph-based trace analysis.; Layer 4: Cross-segment analysis.; 4 Experimental Protocol`；Non-proof=`https://arxiv.org/html/2606.29067v1 — §Layer 1: Structural segmentation and boundary classification.; Layer 2: Soft boundary detection.; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29067:start -->
Claim boundary：仅 arXiv:2606.29067v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29067:end -->
<!-- review:SF-2026-ARXIV-2606-29067:end -->

<!-- review:SF-2026-ARXIV-2606-29073:start -->
### 2606.29073 — From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes

**问题。** 《From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes》处理的问题是：Model Context Protocol (MCP)-style ecosystems give language-model applications a practical connection layer for tools, resources, prompts, and transports.

**机制与 state/data/control owner。** exact-v1 的机制路径为 5 HCP Design; 6 Benchmark Method; 7.7 Ecosystem Measurement。在 `AGENT-MCP` 中，该路径改变或检验的具体对象由题名《From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes》和上述 method locator 共同限定。 归属 `AGENT-MCP`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes; 6 Benchmark Method; 7 Evaluation；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：3 Threat Model; 6.3 Reproducibility Boundary; 8 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 3 Threat Model; 6.3 Reproducibility Boundary; 8 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Tool Catalog 扩大后，Discovery 与 Execution 必须分离` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29073v1 — §5 HCP Design; 6 Benchmark Method; 7.7 Ecosystem Measurement`；Evaluation=`https://arxiv.org/html/2606.29073v1 — §From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes; 6 Benchmark Method; 7 Evaluation`；Non-proof=`https://arxiv.org/html/2606.29073v1 — §3 Threat Model; 6.3 Reproducibility Boundary; 8 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29073:start -->
Claim boundary：仅 arXiv:2606.29073v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29073:end -->
<!-- review:SF-2026-ARXIV-2606-29073:end -->

<!-- review:SF-2026-ARXIV-2606-29082:start -->
### 2606.29082 — Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks

**问题。** 《Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks》处理的问题是：Would experience designing faster GPU kernels also help close in on a long-standing open mathematical conjecture?

**机制与 state/data/control owner。** exact-v1 的机制路径为 EFT serves as mid-training for test-time RL.; Appendix C Additional Details of Dataset Construction Method; C.1 Systematic Error Breakdown Analysis。在 `TRAIN-PRETRAINING` 中，该路径改变或检验的具体对象由题名《Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks》和上述 method locator 共同限定。 归属 `TRAIN-PRETRAINING`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Optimization setup.; 3.2 Analysis of ℱ \mathcal{F} inch Collection; 4 Experiments；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：7 Conclusion; Limitations; Appendix B Further Details and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 7 Conclusion; Limitations; Appendix B Further Details and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 一次 training step 的状态流` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29082v1 — §EFT serves as mid-training for test-time RL.; Appendix C Additional Details of Dataset Construction Method; C.1 Systematic Error Breakdown Analysis`；Evaluation=`https://arxiv.org/html/2606.29082v1 — §Optimization setup.; 3.2 Analysis of ℱ \mathcal{F} inch Collection; 4 Experiments`；Non-proof=`https://arxiv.org/html/2606.29082v1 — §7 Conclusion; Limitations; Appendix B Further Details and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29082:start -->
Claim boundary：仅 arXiv:2606.29082v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29082:end -->
<!-- review:SF-2026-ARXIV-2606-29082:end -->

<!-- review:SF-2026-ARXIV-2606-29088:start -->
### 2606.29088 — Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking

**问题。** 《Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking》处理的问题是：There are various benchmarks to evaluate bugfixing capabilities of Large Language Models.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Report GitHub Issue; Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking; 3 The Proposed Benchmark; 4 Evaluation；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Discussion; 6 Threats to Validity; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Discussion; 6 Threats to Validity; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29088v1 — §Report GitHub Issue; Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking`；Evaluation=`https://arxiv.org/html/2606.29088v1 — §Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking; 3 The Proposed Benchmark; 4 Evaluation`；Non-proof=`https://arxiv.org/html/2606.29088v1 — §5 Discussion; 6 Threats to Validity; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29088:start -->
Claim boundary：仅 arXiv:2606.29088v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29088:end -->
<!-- review:SF-2026-ARXIV-2606-29088:end -->

<!-- review:SF-2026-ARXIV-2606-29089:start -->
### 2606.29089 — TAP-VLA: Tactile Annotation Prompting for Vision Language Action Models

**问题。** 《TAP-VLA: Tactile Annotation Prompting for Vision Language Action Models》处理的问题是：Vision-Language-Action (VLA) models demonstrate impressive reasoning over visual, semantic, and spatial task variations by leveraging large-scale vision and language pre-training.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3 Method。在 `MULTIMODAL-EMBODIED-VLA` 中，该路径改变或检验的具体对象由题名《TAP-VLA: Tactile Annotation Prompting for Vision Language Action Models》和上述 method locator 共同限定。 归属 `MULTIMODAL-EMBODIED-VLA`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Experiments; 4.1 Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Discussion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Discussion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Safety envelope` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29089v1 — §3 Method`；Evaluation=`https://arxiv.org/html/2606.29089v1 — §4 Experiments; 4.1 Results`；Non-proof=`https://arxiv.org/html/2606.29089v1 — §5 Discussion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29089:start -->
Claim boundary：仅 arXiv:2606.29089v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29089:end -->
<!-- review:SF-2026-ARXIV-2606-29089:end -->

<!-- review:SF-2026-ARXIV-2606-29090:start -->
### 2606.29090 — AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering

**问题。** 《AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering》处理的问题是：Retrieval-Augmented Generation (RAG) has become the standard way to ground large language models in external knowledge, yet most systems retrieve a fixed number of passages for every question regardless of its difficulty.

**机制与 state/data/control owner。** exact-v1 的机制路径为 III Methodology and Framework; III-A Overall Framework; III-B System Architecture。在 `AGENT-RAG` 中，该路径改变或检验的具体对象由题名《AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering》和上述 method locator 共同限定。 归属 `AGENT-RAG`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 III-F Evaluation Metrics; IV-E API Cost and Token Analysis; V Results and Analysis；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：V-F Qualitative Examples and Discussion; VI Conclusion and Future Work; VI-A Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** V-F Qualitative Examples and Discussion; VI Conclusion and Future Work; VI-A Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### Query、Compression 与 Stopping 是联合 Policy` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29090v1 — §III Methodology and Framework; III-A Overall Framework; III-B System Architecture`；Evaluation=`https://arxiv.org/html/2606.29090v1 — §III-F Evaluation Metrics; IV-E API Cost and Token Analysis; V Results and Analysis`；Non-proof=`https://arxiv.org/html/2606.29090v1 — §V-F Qualitative Examples and Discussion; VI Conclusion and Future Work; VI-A Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29090:start -->
Claim boundary：仅 arXiv:2606.29090v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29090:end -->
<!-- review:SF-2026-ARXIV-2606-29090:end -->

<!-- review:SF-2026-ARXIV-2606-29091:start -->
### 2606.29091 — Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models

**问题。** 《Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models》处理的问题是：Tabular foundation models cannot reason about data produced by running systems without access to the rules that govern them.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Chance across architectures.。在 `AGENT-RAG` 中，该路径改变或检验的具体对象由题名《Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models》和上述 method locator 共同限定。 归属 `AGENT-RAG`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：6 Discussion & Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 6 Discussion & Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### Query、Compression 与 Stopping 是联合 Policy` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29091v1 — §Chance across architectures.`；Evaluation=`https://arxiv.org/html/2606.29091v1 — §4 Results`；Non-proof=`https://arxiv.org/html/2606.29091v1 — §6 Discussion & Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29091:start -->
Claim boundary：仅 arXiv:2606.29091v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29091:end -->
<!-- review:SF-2026-ARXIV-2606-29091:end -->

<!-- review:SF-2026-ARXIV-2606-29094:start -->
### 2606.29094 — DiLaServe: High SLO Attainment Serving for Diffusion Language Models

**问题。** 《DiLaServe: High SLO Attainment Serving for Diffusion Language Models》处理的问题是：Diffusion language models (DLMs) have recently emerged as a promising alternative to conventional autoregressive language models.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3.1. Design Overview; Appendix C Algorithm for Supporting Approximate KV Caching。在 `INFER-SCHEDULING` 中，该路径改变或检验的具体对象由题名《DiLaServe: High SLO Attainment Serving for Diffusion Language Models》和上述 method locator 共同限定。 归属 `INFER-SCHEDULING`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 5. Evaluation; 5.1. Experimental Setup; 5.3. Accuracy Benchmarks；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 调度对象从 request 变成 token state` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29094v1 — §3.1. Design Overview; Appendix C Algorithm for Supporting Approximate KV Caching`；Evaluation=`https://arxiv.org/html/2606.29094v1 — §5. Evaluation; 5.1. Experimental Setup; 5.3. Accuracy Benchmarks`；Non-proof=`https://arxiv.org/html/2606.29094v1 — §7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29094:start -->
Claim boundary：仅 arXiv:2606.29094v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29094:end -->
<!-- review:SF-2026-ARXIV-2606-29094:end -->

<!-- review:SF-2026-ARXIV-2606-29097:start -->
### 2606.29097 — TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation

**问题。** 《TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation》处理的问题是：Recent research has investigated the use of large language models (LLMs) to generate traffic scenarios for autonomous driving.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3 Method。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Experiments; 4.1 Experimental Setup; Experiment setup.；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Limitations and Future Work; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Limitations and Future Work; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29097v1 — §3 Method`；Evaluation=`https://arxiv.org/html/2606.29097v1 — §4 Experiments; 4.1 Experimental Setup; Experiment setup.`；Non-proof=`https://arxiv.org/html/2606.29097v1 — §5 Limitations and Future Work; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29097:start -->
Claim boundary：仅 arXiv:2606.29097v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29097:end -->
<!-- review:SF-2026-ARXIV-2606-29097:end -->

<!-- review:SF-2026-ARXIV-2606-29108:start -->
### 2606.29108 — Symbolon: Symbolic Execution by Learning Code Transformation

**问题。** 《Symbolon: Symbolic Execution by Learning Code Transformation》处理的问题是：Symbolic execution is a powerful program analysis technique with broad applications, such as vulnerability detection, security testing, and malware analysis.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Our approach; III Methodology。在 `AGENT-WORKFLOW` 中，该路径改变或检验的具体对象由题名《Symbolon: Symbolic Execution by Learning Code Transformation》和上述 method locator 共同限定。 归属 `AGENT-WORKFLOW`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Results; V Evaluation; V-A Experiment Setup；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：VI Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** VI Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## State Machine 是基本模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`arXiv:2606.29108v1 version-stamped mirror — §Our approach; III Methodology`；Evaluation=`arXiv:2606.29108v1 version-stamped mirror — §Results; V Evaluation; V-A Experiment Setup`；Non-proof=`arXiv:2606.29108v1 version-stamped mirror — §VI Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29108:start -->
Claim boundary：仅 arXiv:2606.29108v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29108:end -->
<!-- review:SF-2026-ARXIV-2606-29108:end -->

<!-- review:SF-2026-ARXIV-2606-29112:start -->
### 2606.29112 — A Novel Latent-Class Attack and its Detection by Class Subspace Orthogonalization

**问题。** 《A Novel Latent-Class Attack and its Detection by Class Subspace Orthogonalization》处理的问题是：Deep learning, which in general relies on voluminous amounts of training data, is vulnerable to data poisoning attacks, including error-generic attacks and backdoors (Trojans).

**机制与 state/data/control owner。** exact-v1 的机制路径为 3 Method。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《A Novel Latent-Class Attack and its Detection by Class Subspace Orthogonalization》和上述 method locator 共同限定。 归属 `PLATFORM-SECURITY`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 4 Experimental Results; 4.1 Experiment Setup；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：5 Summary; Instructions for reporting errors；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 5 Summary; Instructions for reporting errors；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 风险管理而不是一次性认证` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29112v1 — §3 Method`；Evaluation=`https://arxiv.org/html/2606.29112v1 — §4 Experimental Results; 4.1 Experiment Setup`；Non-proof=`https://arxiv.org/html/2606.29112v1 — §5 Summary; Instructions for reporting errors；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29112:start -->
Claim boundary：仅 arXiv:2606.29112v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29112:end -->
<!-- review:SF-2026-ARXIV-2606-29112:end -->

<!-- review:SF-2026-ARXIV-2606-29116:start -->
### 2606.29116 — Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem

**问题。** 《Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem》处理的问题是：Large Language Models (LLMs) are rapidly being adopted in low-code and no-code automation platforms, where non-expert users design workflows that combine natural language understanding with external services and APIs.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem。在 `AGENT-PLATFORM` 中，该路径改变或检验的具体对象由题名《Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem》和上述 method locator 共同限定。 归属 `AGENT-PLATFORM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 6.3 Benchmarks for Realistic Agent Behavior；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：3.4 RQ3: Failure Handling; 5 Discussion; 5.1 Threats to Construct Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 3.4 RQ3: Failure Handling; 5 Discussion; 5.1 Threats to Construct Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Agent Runtime State Machine` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29116v1 — §Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem`；Evaluation=`https://arxiv.org/html/2606.29116v1 — §6.3 Benchmarks for Realistic Agent Behavior`；Non-proof=`https://arxiv.org/html/2606.29116v1 — §3.4 RQ3: Failure Handling; 5 Discussion; 5.1 Threats to Construct Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29116:start -->
Claim boundary：仅 arXiv:2606.29116v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29116:end -->
<!-- review:SF-2026-ARXIV-2606-29116:end -->

<!-- review:SF-2026-ARXIV-2606-29119:start -->
### 2606.29119 — Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule

**问题。** 《Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule》处理的问题是：We introduce a pre-registered screening rule that decides, before any implementation, whether an evolutionary / population / lifecycle outer loop over neural-network parameters or structure is worth building.

**机制与 state/data/control owner。** exact-v1 的机制路径为 Report GitHub Issue; Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule》和上述 method locator 共同限定。 归属 `PLATFORM-EVALUATION-SYSTEM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 5.1 Heritability does not rescue (the κ \kappa -sparsity result); 7 The Positive Condition — a Hypothesis, Not a Result；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：8 Limitations; 9 Discussion and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 8 Limitations; 9 Discussion and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## Evaluation Run 的平台对象模型` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29119v1 — §Report GitHub Issue; Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule`；Evaluation=`https://arxiv.org/html/2606.29119v1 — §5.1 Heritability does not rescue (the κ \kappa -sparsity result); 7 The Positive Condition — a Hypothesis, Not a Result`；Non-proof=`https://arxiv.org/html/2606.29119v1 — §8 Limitations; 9 Discussion and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29119:start -->
Claim boundary：仅 arXiv:2606.29119v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29119:end -->
<!-- review:SF-2026-ARXIV-2606-29119:end -->

<!-- review:SF-2026-ARXIV-2606-29124:start -->
### 2606.29124 — CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs

**问题。** 《CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs》处理的问题是：Many software bugs in network protocol implementations arise near specification boundaries, such as inputs just within or outside allowed ranges, or messages that are valid in isolation but invalid in a given state.

**机制与 state/data/control owner。** exact-v1 的机制路径为 3 Methodology。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs》和上述 method locator 共同限定。 归属 `PLATFORM-SECURITY`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 Output of differential analysis:; 3.6 Stage 5: Result Analysis; LLM-based analysis of differential results:；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：2.3 SMTP Nesting Failures (Mailpit); Boundary value analysis (BVA):; 6 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 2.3 SMTP Nesting Failures (Mailpit); Boundary value analysis (BVA):; 6 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 风险管理而不是一次性认证` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29124v1 — §3 Methodology`；Evaluation=`https://arxiv.org/html/2606.29124v1 — §Output of differential analysis:; 3.6 Stage 5: Result Analysis; LLM-based analysis of differential results:`；Non-proof=`https://arxiv.org/html/2606.29124v1 — §2.3 SMTP Nesting Failures (Mailpit); Boundary value analysis (BVA):; 6 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29124:start -->
Claim boundary：仅 arXiv:2606.29124v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29124:end -->
<!-- review:SF-2026-ARXIV-2606-29124:end -->

<!-- review:SF-2026-ARXIV-2606-29126:start -->
### 2606.29126 — HiComm: Hierarchical Communication for Multi-agent Reinforcement Learning

**问题。** 《HiComm: Hierarchical Communication for Multi-agent Reinforcement Learning》处理的问题是：Cooperative multi-agent reinforcement learning (MARL) often relies on communication to mitigate partial observability, yet most existing protocols treat messages as flat dense vectors detached from the structure of the observations they summarize.

**机制与 state/data/control owner。** exact-v1 的机制路径为 4 Methodology; 4.1 MARL Framework; Training Objective。在 `AGENT-MULTI-AGENT` 中，该路径改变或检验的具体对象由题名《HiComm: Hierarchical Communication for Multi-agent Reinforcement Learning》和上述 method locator 共同限定。 归属 `AGENT-MULTI-AGENT`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 5 Experiments; 5.1 Setup; 5.2 Results；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：6 Conclusion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 6 Conclusion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `### Pairwise coupling 不能外推 group dynamics` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29126v1 — §4 Methodology; 4.1 MARL Framework; Training Objective`；Evaluation=`https://arxiv.org/html/2606.29126v1 — §5 Experiments; 5.1 Setup; 5.2 Results`；Non-proof=`https://arxiv.org/html/2606.29126v1 — §6 Conclusion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29126:start -->
Claim boundary：仅 arXiv:2606.29126v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29126:end -->
<!-- review:SF-2026-ARXIV-2606-29126:end -->

<!-- review:SF-2026-ARXIV-2606-29129:start -->
### 2606.29129 — Improved Scaling for Fast Mode of Ozaki Scheme II

**问题。** 《Improved Scaling for Fast Mode of Ozaki Scheme II》处理的问题是：Ozaki scheme II emulates high-precision matrix multiplication using low-precision integer matrix operations based on the Chinese remainder theorem (CRT).

**机制与 state/data/control owner。** exact-v1 的机制路径为 4 Proposed Method。在 `INFER-TENSORRT-LLM` 中，该路径改变或检验的具体对象由题名《Improved Scaling for Fast Mode of Ozaki Scheme II》和上述 method locator 共同限定。 归属 `INFER-TENSORRT-LLM`；相邻 owner 只消费 handoff。

**Evaluation 的 proof / non-proof。** 披露的 evaluation contract 是 3.1 Theoretical Analysis; 5 Evaluation；它只证明该 workload、模型/硬件与 evaluator 身份下的受限结果。未公开的 model、hardware、precision、length、batch、concurrency 或 SLO 字段继续保留 Not Disclosed，不能由结果反推。 它不证明：3 Limitation of Fast Mode Scaling; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。

**Trade-off、failure、coexistence 与 evolution。** 3 Limitation of Fast Mode Scaling; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。 因此前置条件、identity、evaluator 或 workload 越界时保留 `## 量化为什么不自动带来加速` 的既有路径；新机制只在其被验证的局部合同内共存。

**Evidence。** Method=`https://arxiv.org/html/2606.29129v1 — §4 Proposed Method`；Evaluation=`https://arxiv.org/html/2606.29129v1 — §3.1 Theoretical Analysis; 5 Evaluation`；Non-proof=`https://arxiv.org/html/2606.29129v1 — §3 Limitation of Fast Mode Scaling; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-29129:start -->
Claim boundary：仅 arXiv:2606.29129v1 的上述定位；不使用 later version，不把 benchmark outcome 外推为未披露的模型、硬件、并发或生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-29129:end -->
<!-- review:SF-2026-ARXIV-2606-29129:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-28666 | 《Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare》exact-v1 evaluation scope: 4 Results; 4.6 Observation analysis | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Results; 4.6 Observation analysis |
| SF-2026-ARXIV-2606-28679 | 《Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks》exact-v1 evaluation scope: VI Evaluation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: VI Evaluation |
| SF-2026-ARXIV-2606-28690 | 《Formal Security Analysis of Agent Protocol Composition》exact-v1 evaluation scope: Formal Security Analysis of Agent Protocol Composition; 6. Evaluation; 6.1. Evaluation Setup | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Formal Security Analysis of Agent Protocol Composition; 6. Evaluation; 6.1. Evaluation Setup |
| SF-2026-ARXIV-2606-28692 | 《An AI agent for treatment reasoning over a biomedical tool universe》exact-v1 evaluation scope: Results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Results |
| SF-2026-ARXIV-2606-28707 | 《BV-Blend: Uncertainty-Weighted Historical Baselines for Stable Critic-Free RL with Verifiable Rewards》exact-v1 evaluation scope: 4 Experiments; Evaluation.; 4.1 Main Results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Experiments; Evaluation.; 4.1 Main Results |
| SF-2026-ARXIV-2606-28712 | 《J-LAW: Joint Localization and Actionable World Modeling via Coupled Latent Factor Graphs》exact-v1 evaluation scope: IV Experiments | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: IV Experiments |
| SF-2026-ARXIV-2606-28715 | 《SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages》exact-v1 evaluation scope: SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages; 2.1 Agent Evaluation; 2.2 Multilingual Evaluation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages; 2.1 Agent Evaluation; 2.2 Multilingual Evaluation |
| SF-2026-ARXIV-2606-28720 | 《CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance》exact-v1 evaluation scope: IV EXPERIMENTS; IV-A Experimental Setup; IV-D Retrieval & Alignment Analysis | Not Disclosed | single NVIDIA RTX 4090 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: IV EXPERIMENTS; IV-A Experimental Setup; IV-D Retrieval & Alignment Analysis |
| SF-2026-ARXIV-2606-28725 | 《DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation》exact-v1 evaluation scope: IV Experimental Setup; IV-F Evaluation Metrics and Replication; V Experiments | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: IV Experimental Setup; IV-F Evaluation Metrics and Replication; V Experiments |
| SF-2026-ARXIV-2606-28733 | 《Agentic Abstention: Do Agents Know When to Stop Instead of Act?》exact-v1 evaluation scope: 4 Experiment Setup; 4.2 Evaluation Metrics; 6 Results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Experiment Setup; 4.2 Evaluation Metrics; 6 Results |
| SF-2026-ARXIV-2606-28739 | 《Agent Safety Is Action Alignment》exact-v1 evaluation scope: 5.3. Relational and Deployment-Conditioned Evaluation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 5.3. Relational and Deployment-Conditioned Evaluation |
| SF-2026-ARXIV-2606-28747 | 《Self-Supervised Theorem Discovery in a Formal Axiomatic System》exact-v1 evaluation scope: 5 Experiments; 5.1 Experimental Setup; 5.2 Quantitative Evaluation of Theorem Discovery | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 5 Experiments; 5.1 Experimental Setup; 5.2 Quantitative Evaluation of Theorem Discovery |
| SF-2026-ARXIV-2606-28751 | 《A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility》exact-v1 evaluation scope: VII Results and discussion; VII.2 Results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: VII Results and discussion; VII.2 Results |
| SF-2026-ARXIV-2606-28754 | 《SHIFT: Dynamic Compute Relocation Framework for Communication-Aware Chiplet-Based Systems》exact-v1 evaluation scope: V Evaluations; V-A Experimental Setup; V-B Experimental Results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: V Evaluations; V-A Experimental Setup; V-B Experimental Results |
| SF-2026-ARXIV-2606-28757 | 《A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models》exact-v1 evaluation scope: A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models; Physical-grounded Evaluation.; 3 Principles of the New Evaluation Protocol | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models; Physical-grounded Evaluation.; 3 Principles of the New Evaluation Protocol |
| SF-2026-ARXIV-2606-28758 | 《X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving》exact-v1 evaluation scope: 3 Experiments; 3.5 Analysis of Structured Sketch Ground Truth | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 3 Experiments; 3.5 Analysis of Structured Sketch Ground Truth |
| SF-2026-ARXIV-2606-28772 | 《Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain》exact-v1 evaluation scope: 3.3 Statistical Analysis; 4 Results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 3.3 Statistical Analysis; 4 Results |
| SF-2026-ARXIV-2606-28781 | 《HyphaeDB: A Living Knowledge Topology for Agent-First Memory》exact-v1 evaluation scope: 6 Theoretical Analysis; 8 Competitive Analysis | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 6 Theoretical Analysis; 8 Competitive Analysis |
| SF-2026-ARXIV-2606-28804 | 《ViPSim: Collaborating Visual and Parameter Spaces for Consistent Long-Horizon Embodied World Models》exact-v1 evaluation scope: IV Experiments; IV-A Experimental Setup; IV-B Quantitative Analysis | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: IV Experiments; IV-A Experimental Setup; IV-B Quantitative Analysis |
| SF-2026-ARXIV-2606-28813 | 《Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning》exact-v1 evaluation scope: 5 Experiments; 5.1 Experimental Setup and Baselines; 5.2 Main Results: Zero-Shot Composition and Generalization | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 5 Experiments; 5.1 Experimental Setup and Baselines; 5.2 Main Results: Zero-Shot Composition and Generalization |
| SF-2026-ARXIV-2606-28831 | 《HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression》exact-v1 evaluation scope: 4 Experiment; Appendix C Experiments Details; C.3 Further Experiment Results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Experiment; Appendix C Experiments Details; C.3 Further Experiment Results |
| SF-2026-ARXIV-2606-28839 | 《The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables》exact-v1 evaluation scope: LLM bias evaluation.; 4.1.2 Experiment 1: Full CAF Matrix; 4.1.3 Experiment 2: Modality Ablation | DeepSeek and GPT-4o-mini API models | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: LLM bias evaluation.; 4.1.2 Experiment 1: Full CAF Matrix; 4.1.3 Experiment 2: Modality Ablation |
| SF-2026-ARXIV-2606-28841 | 《LAMP: Lean-based Agentic framework with MCP and Proof Repair》exact-v1 evaluation scope: 4 Experimental Results; 4.1 Experimental Setup; Evaluation suite: | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Experimental Results; 4.1 Experimental Setup; Evaluation suite: |
| SF-2026-ARXIV-2606-28843 | 《The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning》exact-v1 evaluation scope: 3 Experimental Set Up; 3.2 Evaluation Protocol; 4 Results | nine languages across three disclosed model families | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 3 Experimental Set Up; 3.2 Evaluation Protocol; 4 Results |
| SF-2026-ARXIV-2606-28862 | 《HKVLM: Faithful Query--Region Binding for Frozen-Detector Visual Grounding》exact-v1 evaluation scope: Hallucination evaluation.; 5 Experimental Design and Evaluation Protocol; 6 Results | Grounding DINO detector and Qwen2.5-VL | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Hallucination evaluation.; 5 Experimental Design and Evaluation Protocol; 6 Results |
| SF-2026-ARXIV-2606-28863 | 《Defeat Devices in AI Systems》exact-v1 evaluation scope: 5.5 Four decisive experiments; 6.1 Evaluation methodology | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 5.5 Four decisive experiments; 6.1 Evaluation methodology |
| SF-2026-ARXIV-2606-28864 | 《On Test-Time Scaling for Vision-Language Models》exact-v1 evaluation scope: 4 Experiments and Takeaways; 6 Analysis of Multimodal Chain-of-Thoughts; S1 InternVL-3.5 Results | Qwen, LLaVA and SmolVLM families | NVIDIA H200 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Experiments and Takeaways; 6 Analysis of Multimodal Chain-of-Thoughts; S1 InternVL-3.5 Results |
| SF-2026-ARXIV-2606-28867 | 《Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages》exact-v1 evaluation scope: Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages; Legal analysis of AI training data. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages; Legal analysis of AI training data. |
| SF-2026-ARXIV-2606-28876 | 《Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory》exact-v1 evaluation scope: 3 Experimental Route; 4 Results; Why frozen-model evaluation is still useful. | Not Disclosed | Not Disclosed | Not Disclosed | 2M-token stress slice; other staged contexts disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 3 Experimental Route; 4 Results; Why frozen-model evaluation is still useful. |
| SF-2026-ARXIV-2606-28896 | 《A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation》exact-v1 evaluation scope: 2.4 Tool-Augmented LLM Agents and Evaluation; 3.5 Observer-Driven Evaluation and Bounded Repair; 4 Experiments | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 2.4 Tool-Augmented LLM Agents and Evaluation; 3.5 Observer-Driven Evaluation and Bounded Repair; 4 Experiments |
| SF-2026-ARXIV-2606-28898 | 《PASTA: A Paraphrasing And Self-Training Approach for Knowledge Updating in LLMs》exact-v1 evaluation scope: 4 Experiments; 4.2 Experimental Setup; 4.3 Evaluation Methods | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Experiments; 4.2 Experimental Setup; 4.3 Evaluation Methods |
| SF-2026-ARXIV-2606-28900 | 《MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes》exact-v1 evaluation scope: Medical QA and fixed-input evaluation.; Memory, retrieval, and continual evaluation.; 3 MedEvoEval : An Executable Evaluation Protocol | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Medical QA and fixed-input evaluation.; Memory, retrieval, and continual evaluation.; 3 MedEvoEval : An Executable Evaluation Protocol |
| SF-2026-ARXIV-2606-28925 | 《Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation》exact-v1 evaluation scope: Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 3.1. Problem setup and notation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 3.1. Problem setup and notation |
| SF-2026-ARXIV-2606-28932 | 《DLR: Zero-Inference-Cost Latent Residuals for Low-Rank Pre-Training》exact-v1 evaluation scope: 2.1 Setup and a Unified View; 4 Experiments; 4.1 Evaluation Setup and Protocol | 60M–7B LLaMA-style models | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 2.1 Setup and a Unified View; 4 Experiments; 4.1 Evaluation Setup and Protocol |
| SF-2026-ARXIV-2606-28938 | 《EVLA: An Electro-Aware Multimodal Assistant for Physically-Grounded Driving Reasoning and Control》exact-v1 evaluation scope: 4 Experiments; 4.3 Evaluation and Main Results; 4.7 Parameter Sensitivity Analysis | Not Disclosed | single NVIDIA RTX 3090 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Experiments; 4.3 Evaluation and Main Results; 4.7 Parameter Sensitivity Analysis |
| SF-2026-ARXIV-2606-28939 | 《ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies》exact-v1 evaluation scope: 5 Experiments; Appendix D Setup Details | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 5 Experiments; Appendix D Setup Details |
| SF-2026-ARXIV-2606-28953 | 《Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System》exact-v1 evaluation scope: 3.4 Linear Discriminant Analysis; 4 Experimental set-up; 5 Results and Discussion | ResNet50 victim model | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 3.4 Linear Discriminant Analysis; 4 Experimental set-up; 5 Results and Discussion |
| SF-2026-ARXIV-2606-28955 | 《Modification-Considering Value Learning for Reward Hacking Mitigation in RL》exact-v1 evaluation scope: Theoretical analysis.; 4 Experiments; 4.2 Main results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Theoretical analysis.; 4 Experiments; 4.2 Main results |
| SF-2026-ARXIV-2606-28958 | 《When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration》exact-v1 evaluation scope: 5 Benchmark and Experimental Setup; 8 Defense Diagnostics and Trade-Off Analysis | Qwen3-4B and Qwen3-8B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 5 Benchmark and Experimental Setup; 8 Defense Diagnostics and Trade-Off Analysis |
| SF-2026-ARXIV-2606-28962 | 《FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks》exact-v1 evaluation scope: IV Experiments; IV-A Experimental Setup; IV-B Experimental Scenarios and Results | seven disclosed LLMs | Not Disclosed | INT8, FP4 and NF4 quantization paths | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: IV Experiments; IV-A Experimental Setup; IV-B Experimental Scenarios and Results |
| SF-2026-ARXIV-2606-28995 | 《HJ-SafeDMP: Hamilton-Jacobi Reachability-Guided Dynamic Movement Primitives for Provably Safe Robot Motion》exact-v1 evaluation scope: III Background and Problem Setup; V Experiments; V-A Experimental Setup | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: III Background and Problem Setup; V Experiments; V-A Experimental Setup |
| SF-2026-ARXIV-2606-28998 | 《Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation》exact-v1 evaluation scope: 3.4. Evaluation Benchmarks; 3.4.1. Evaluation on Functional Benchmarks; 3.4.2. Evaluation on Non-Functional Benchmarks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 3.4. Evaluation Benchmarks; 3.4.1. Evaluation on Functional Benchmarks; 3.4.2. Evaluation on Non-Functional Benchmarks |
| SF-2026-ARXIV-2606-29013 | 《Mural: Transferring LLM knowledge to image generation via Mixture-of-Transformers》exact-v1 evaluation scope: 3.1 Model setup; 4 Experiments | frozen Qwen2.5 branch; 1.5B/3B/7B scales | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 3.1 Model setup; 4 Experiments |
| SF-2026-ARXIV-2606-29030 | 《Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering》exact-v1 evaluation scope: V Numerical Results; V-A Experimental Dataset and Model Setup; V-B Comparison across Benchmarks and Model Backends | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: V Numerical Results; V-A Experimental Dataset and Model Setup; V-B Comparison across Benchmarks and Model Backends |
| SF-2026-ARXIV-2606-29033 | 《Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations》exact-v1 evaluation scope: Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations; 4. Avoiding Evaluation Tropes | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations; 4. Avoiding Evaluation Tropes |
| SF-2026-ARXIV-2606-29038 | 《Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy》exact-v1 evaluation scope: 3.2 Controlled Aggregation Experiment (EA-2); Appendix A Experiment Parameters | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 3.2 Controlled Aggregation Experiment (EA-2); Appendix A Experiment Parameters |
| SF-2026-ARXIV-2606-29054 | 《When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation》exact-v1 evaluation scope: Problem setup.; 3 Experiments; 3.1 Setup | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Problem setup.; 3 Experiments; 3.1 Setup |
| SF-2026-ARXIV-2606-29059 | 《Flow Matching in Feature Space for Stochastic World Modeling》exact-v1 evaluation scope: 4 Latent World Model Benchmarks; 4.1 Synthetic Benchmark: Bouncing Shapes; 4.2 Real-world Benchmark: FuturePerception | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Latent World Model Benchmarks; 4.1 Synthetic Benchmark: Bouncing Shapes; 4.2 Real-world Benchmark: FuturePerception |
| SF-2026-ARXIV-2606-29066 | 《$x$-Prediction Flow: Efficient Continuous Decoding for Masked Diffusion Language Models》exact-v1 evaluation scope: 5 Experiments; 5.3 Code Generation Evaluation; Setup | LLaDA-8B-Instruct and LLaDA2.0-mini | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 5 Experiments; 5.3 Code Generation Evaluation; Setup |
| SF-2026-ARXIV-2606-29067 | 《ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs》exact-v1 evaluation scope: Graph-based trace analysis.; Layer 4: Cross-segment analysis.; 4 Experimental Protocol | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Graph-based trace analysis.; Layer 4: Cross-segment analysis.; 4 Experimental Protocol |
| SF-2026-ARXIV-2606-29073 | 《From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes》exact-v1 evaluation scope: From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes; 6 Benchmark Method; 7 Evaluation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes; 6 Benchmark Method; 7 Evaluation |
| SF-2026-ARXIV-2606-29082 | 《Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks》exact-v1 evaluation scope: Optimization setup.; 3.2 Analysis of ℱ \mathcal{F} inch Collection; 4 Experiments | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Optimization setup.; 3.2 Analysis of ℱ \mathcal{F} inch Collection; 4 Experiments |
| SF-2026-ARXIV-2606-29088 | 《Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking》exact-v1 evaluation scope: Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking; 3 The Proposed Benchmark; 4 Evaluation | 13 open-weight models; four small fine-tuned models | Not Disclosed | bf16 for disclosed fine-tuning/evaluation path | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking; 3 The Proposed Benchmark; 4 Evaluation |
| SF-2026-ARXIV-2606-29089 | 《TAP-VLA: Tactile Annotation Prompting for Vision Language Action Models》exact-v1 evaluation scope: 4 Experiments; 4.1 Results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Experiments; 4.1 Results |
| SF-2026-ARXIV-2606-29090 | 《AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering》exact-v1 evaluation scope: III-F Evaluation Metrics; IV-E API Cost and Token Analysis; V Results and Analysis | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: III-F Evaluation Metrics; IV-E API Cost and Token Analysis; V Results and Analysis |
| SF-2026-ARXIV-2606-29091 | 《Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models》exact-v1 evaluation scope: 4 Results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Results |
| SF-2026-ARXIV-2606-29094 | 《DiLaServe: High SLO Attainment Serving for Diffusion Language Models》exact-v1 evaluation scope: 5. Evaluation; 5.1. Experimental Setup; 5.3. Accuracy Benchmarks | LLaDA-8B and Dream-7B; Llama-3.3-70B judge | NVIDIA GH200 and H100 clusters | Not Disclosed | maximum 4,096 tokens | Not Disclosed | Not Disclosed | Not Disclosed | homogeneous per-request SLO contract in §5 | Exact-v1 evaluator/metric evidence: 5. Evaluation; 5.1. Experimental Setup; 5.3. Accuracy Benchmarks |
| SF-2026-ARXIV-2606-29097 | 《TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation》exact-v1 evaluation scope: 4 Experiments; 4.1 Experimental Setup; Experiment setup. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Experiments; 4.1 Experimental Setup; Experiment setup. |
| SF-2026-ARXIV-2606-29108 | 《Symbolon: Symbolic Execution by Learning Code Transformation》exact-v1 evaluation scope: Results; V Evaluation; V-A Experiment Setup | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Results; V Evaluation; V-A Experiment Setup |
| SF-2026-ARXIV-2606-29112 | 《A Novel Latent-Class Attack and its Detection by Class Subspace Orthogonalization》exact-v1 evaluation scope: 4 Experimental Results; 4.1 Experiment Setup | ResNet-18 and ResNet-34 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 4 Experimental Results; 4.1 Experiment Setup |
| SF-2026-ARXIV-2606-29116 | 《Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem》exact-v1 evaluation scope: 6.3 Benchmarks for Realistic Agent Behavior | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 6.3 Benchmarks for Realistic Agent Behavior |
| SF-2026-ARXIV-2606-29119 | 《Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule》exact-v1 evaluation scope: 5.1 Heritability does not rescue (the κ \kappa -sparsity result); 7 The Positive Condition — a Hypothesis, Not a Result | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 5.1 Heritability does not rescue (the κ \kappa -sparsity result); 7 The Positive Condition — a Hypothesis, Not a Result |
| SF-2026-ARXIV-2606-29124 | 《CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs》exact-v1 evaluation scope: Output of differential analysis:; 3.6 Stage 5: Result Analysis; LLM-based analysis of differential results: | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: Output of differential analysis:; 3.6 Stage 5: Result Analysis; LLM-based analysis of differential results: |
| SF-2026-ARXIV-2606-29126 | 《HiComm: Hierarchical Communication for Multi-agent Reinforcement Learning》exact-v1 evaluation scope: 5 Experiments; 5.1 Setup; 5.2 Results | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 5 Experiments; 5.1 Setup; 5.2 Results |
| SF-2026-ARXIV-2606-29129 | 《Improved Scaling for Fast Mode of Ozaki Scheme II》exact-v1 evaluation scope: 3.1 Theoretical Analysis; 5 Evaluation | Not Disclosed | NVIDIA GH200 with CUDA 13.2 | INT8 matrix engines with DGEMM/SGEMM references | square matrices of size 1,024 and 16,384 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Exact-v1 evaluator/metric evidence: 3.1 Theoretical Analysis; 5 Evaluation |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-28666 | potential_books_delta; forced_review | not_selected | — | — | 《Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28666v1 — §2.6 TRiSM framework; 3 Methodology; 3.2 Framework used`；最新 owner/adjacent 已覆盖该控制边界：Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 exact-v1 non-proof=`6 Future work and limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28666 |
| SF-2026-ARXIV-2606-28679 | potential_books_delta; forced_review | not_selected | — | — | 《Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28679v1 — §Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; III The Cross-Framework Gap; III-A Method and selection`；最新 owner/adjacent 已覆盖该控制边界：Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 exact-v1 non-proof=`Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; II Threat Model; II-A Boundary and adversary；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28679 |
| SF-2026-ARXIV-2606-28690 | score_7_9; potential_books_delta | selected | DA-20260628-PROTOCOL-EXECUTION-INVARIANTS | — | 《Formal Security Analysis of Agent Protocol Composition》被选为 `DA-20260628-PROTOCOL-EXECUTION-INVARIANTS` 的代表 family，因为 `把每个 agent protocol lowering 为带 source/type evidence 的有限状态 IR，先做 pairwise composition 与 trace replay，再把 counterexample 编译成可执行回归；未知组合保持隔离。`。选择依据先冻结于 protocol/channel/metric/physical-safety 的跨层 control ownership；未证明边界是 `6.4. RQ3: Composition Failures; 7. Discussion; 9. Threats to Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis:DA-20260628-PROTOCOL-EXECUTION-INVARIANTS |
| SF-2026-ARXIV-2606-28692 | potential_books_delta | not_selected | — | — | 《An AI agent for treatment reasoning over a biomedical tool universe》未单列 Deep Analysis。决定性理由：两层 clinical self-learning 与 212-tool loop 仍由单一医疗工具宇宙、观察性 EHR 与领域 rubric 定义，不能改写通用 Workflow owner。 exact-v1 non-proof=`Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28692 |
| SF-2026-ARXIV-2606-28707 | potential_books_delta | not_selected | — | — | 《BV-Blend: Uncertainty-Weighted Historical Baselines for Stable Critic-Free RL with Verifiable Rewards》未单列 Deep Analysis。决定性理由：semantic-cluster historical baseline 是 critic-free RL 的局部方差控制器；它没有改变 verifier、trajectory 或 reward authority。 exact-v1 non-proof=`5 Conclusion; Limitations; D.1 Discussion of Key Assumptions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28707 |
| SF-2026-ARXIV-2606-28712 | potential_books_delta | not_selected | — | — | 《J-LAW: Joint Localization and Actionable World Modeling via Coupled Latent Factor Graphs》未单列 Deep Analysis。决定性理由：coupled factor graph 与 alternating IRLS 是四个 WildGS scene 上的局部优化路线，且更复杂 joint setting 并不稳定优于 pose-only。 exact-v1 non-proof=`V Conclusion and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28712 |
| SF-2026-ARXIV-2606-28715 | potential_books_delta | not_selected | — | — | 《SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28715v1 — §Report GitHub Issue; SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`6 Analysis and Discussion; 7 Conclusion; 8 Limitation；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28715 |
| SF-2026-ARXIV-2606-28720 | potential_books_delta | not_selected | — | — | 《CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28720v1 — §III METHOD; IV-B System-level Comparisons`；最新 owner/adjacent 已覆盖该控制边界：Ch25 已拥有 persistent/action-conditioned state、stochastic rollout、entity identity、simulation artifact 与 physical commit boundary。 exact-v1 non-proof=`V CONCLUSIONS；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28720 |
| SF-2026-ARXIV-2606-28725 | potential_books_delta | not_selected | — | — | 《DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28725v1 — §III Methodology; III-A Framework Overview; IV-B Model and Training Details`；最新 owner/adjacent 已覆盖该控制边界：Ch67 已把多 sensor、drift、checkpoint freshness、observe-only authority、告警与 rollback 分层。 exact-v1 non-proof=`VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28725 |
| SF-2026-ARXIV-2606-28733 | potential_books_delta | not_selected | — | — | 《Agentic Abstention: Do Agents Know When to Stop Instead of Act?》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28733v1 — §5 Our Proposed Method for Improving Agentic Abstention: convolve; G.1 Task setting and training configuration; I.2.1 System Prompt for WebShop`；最新 owner/adjacent 已覆盖该控制边界：Ch79 已把 proposal、pre-commit verifier、environment feedback、abstention 与 executable commit 分权。 exact-v1 non-proof=`7 Conclusion; Appendix A Limitations; Failure to abstain from GPT-5.4-mini；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28733 |
| SF-2026-ARXIV-2606-28739 | potential_books_delta; forced_review | not_selected | — | — | 《Agent Safety Is Action Alignment》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28739v1 — §Report GitHub Issue; Agent Safety Is Action Alignment`；最新 owner/adjacent 已覆盖该控制边界：Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 exact-v1 non-proof=`5.2. External Enforcement at the Action Boundary; 7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28739 |
| SF-2026-ARXIV-2606-28747 | potential_books_delta | not_selected | — | — | 《Self-Supervised Theorem Discovery in a Formal Axiomatic System》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28747v1 — §Self-Supervised Theorem Discovery in a Formal Axiomatic System; Rules of the Hilbert System.`；最新 owner/adjacent 已覆盖该控制边界：Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 exact-v1 non-proof=`7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28747 |
| SF-2026-ARXIV-2606-28751 | potential_books_delta | not_selected | — | — | 《A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility》未单列 Deep Analysis。决定性理由：path-space/irreversibility 主要是受控小模型上的理论结构；planning/uncertainty 结论尚未形成可部署 state contract。 exact-v1 non-proof=`VII Results and discussion; VII.5 Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28751 |
| SF-2026-ARXIV-2606-28754 | potential_books_delta | not_selected | — | — | 《SHIFT: Dynamic Compute Relocation Framework for Communication-Aware Chiplet-Based Systems》未单列 Deep Analysis。决定性理由：NoIF/SHIFT 只在作者 wafer/chiplet simulator 中成立，数据中心迁移仍是 future work，不能改写 cluster GPU scheduler。 exact-v1 non-proof=`VI Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28754 |
| SF-2026-ARXIV-2606-28757 | potential_books_delta | not_selected | — | — | 《A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28757v1 — §Effect of Post-Training.; C Global Dynamic Reconstruction Methodology; G Post Training Details`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`5 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28757 |
| SF-2026-ARXIV-2606-28758 | potential_books_delta | not_selected | — | — | 《X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving》未单列 Deep Analysis。决定性理由：96-token sketch 与 embedded world model 是驾驶模型局部架构，没有建立跨任务 world-state owner 或 physical promotion contract。 exact-v1 non-proof=`5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28758 |
| SF-2026-ARXIV-2606-28772 | score_7_9; potential_books_delta | not_selected | — | — | 《Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain》未单列 Deep Analysis。决定性理由：其长期 delta 已进入 `TRAIN-DATA`，但跨层影响弱于四个已冻结分析单元：把 per-annotator label、threshold/disagreement 与聚合 rule 作为训练数据状态保存；majority label 只是一个 materialized view，不能删除 contested boundary。 exact-v1 non-proof=`Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain; 4.1 Disagreement Concentrates at the Value Boundary; 4.5 Boundary Disagreement Is Not Driven by Annotation Error；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28772 |
| SF-2026-ARXIV-2606-28781 | potential_books_delta | not_selected | — | — | 《HyphaeDB: A Living Knowledge Topology for Agent-First Memory》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28781v1 — §2.1 Agent Memory Systems; 3 Architecture; 4.1 Propagation Algorithm`；最新 owner/adjacent 已覆盖该控制边界：Ch77 已拥有 typed write/read、provenance、conflict、transaction、visibility、rollback 与 graph dependency 生命周期。 exact-v1 non-proof=`9 Discussion; 9.2 Limitations and Future Work; 10 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28781 |
| SF-2026-ARXIV-2606-28804 | potential_books_delta | not_selected | — | — | 《ViPSim: Collaborating Visual and Parameter Spaces for Consistent Long-Horizon Embodied World Models》未单列 Deep Analysis。决定性理由：visual/parameter-space 协同视频生成是特定 embodied world-model 架构；OOD affordance 与 morphology failure 阻止其成为长期系统结论。 exact-v1 non-proof=`V Limitations; VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28804 |
| SF-2026-ARXIV-2606-28813 | potential_books_delta | not_selected | — | — | 《Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28813v1 — §Training data.; Appendix E Constraint-Aware Steering Algorithm; Appendix F Model and Training Details`；最新 owner/adjacent 已覆盖该控制边界：Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 exact-v1 non-proof=`6 Limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28813 |
| SF-2026-ARXIV-2606-28831 | potential_books_delta | not_selected | — | — | 《HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28831v1 — §System-Algorithm Co-Design in LLM Inference; 3 The Hard-KV Design; 3.1 The Framework Overview`；最新 owner/adjacent 已覆盖该控制边界：Ch45 已拥有 head/layer/page-aware eviction、quality-memory calibration、residual path、refresh、FullKV fallback 与 production SLO 边界。 exact-v1 non-proof=`5 Conclusion and Future Work; Appendix B Further Discussions on KV Index Regularization; B.2 Discussion on trade-off in the Index Management for Layerwise Selection；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28831 |
| SF-2026-ARXIV-2606-28839 | potential_books_delta | not_selected | — | — | 《The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28839v1 — §The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems —and Auditing the Claims It Enables; Multi-agent LLM systems.; Network contagion and spectral methods.`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`4.1.4 Experiment 3: Real-API with Functional BOUNDARY_SYNC; 6 Discussion; 7 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28839 |
| SF-2026-ARXIV-2606-28841 | potential_books_delta | not_selected | — | — | 《LAMP: Lean-based Agentic framework with MCP and Proof Repair》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28841v1 — §LAMP: Lean-based Agentic framework with MCP and Proof Repair; 2.3 Agentic Frameworks for Theorem Proving; 3 The LAMP System`；最新 owner/adjacent 已覆盖该控制边界：Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 exact-v1 non-proof=`5 Discussion and Limitations; Failure Analysis:; Limitations and Future Work:；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28841 |
| SF-2026-ARXIV-2606-28843 | potential_books_delta | not_selected | — | — | 《The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28843v1 — §5.3 Pre-training distributions and scale`；最新 owner/adjacent 已覆盖该控制边界：Ch29 已把 demonstration distribution、language/model slice、安全回归、forgetting 与 serving interface 分开验收。 exact-v1 non-proof=`7 Discussion; 7.2 Limitations; 8 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28843 |
| SF-2026-ARXIV-2606-28862 | potential_books_delta | not_selected | — | — | 《HKVLM: Faithful Query--Region Binding for Frozen-Detector Visual Grounding》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28862v1 — §4 Method: HKVLM; 4.5 Cold-start training; 5 Experimental Design and Evaluation Protocol`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`8 Discussion, Limitations, and Broader Impact; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28862 |
| SF-2026-ARXIV-2606-28863 | potential_books_delta | not_selected | — | — | 《Defeat Devices in AI Systems》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28863v1 — §Defeat Devices in AI Systems; 4.1 Five method families; 5.1 Defeat devices can naturally emerge in AI systems`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`2.4 Boundary cases; 6.5 Limitations; 7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28863 |
| SF-2026-ARXIV-2606-28864 | potential_books_delta | not_selected | — | — | 《On Test-Time Scaling for Vision-Language Models》未单列 Deep Analysis。决定性理由：九种 VLM test-time strategy 的胜负随模型、prompt、benchmark 与 extraction 改变，只保留经验上下文。 exact-v1 non-proof=`7 Conclusion; S12 Other model failures；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28864 |
| SF-2026-ARXIV-2606-28867 | potential_books_delta | not_selected | — | — | 《Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28867v1 — §Legal analysis of AI training data.`；最新 owner/adjacent 已覆盖该控制边界：Ch27 已拥有 sample/transform/label provenance、license、lineage、mixture 与 admission，但尚未要求保留 per-annotator distribution 以阻止 majority label 静默取得价值边界真值。 exact-v1 non-proof=`6. Four Failure Modes; 6.4. Data Persistence Failure: The Congolese Radio Corpus; 9. Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28867 |
| SF-2026-ARXIV-2606-28876 | potential_books_delta | not_selected | — | — | 《Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28876v1 — §2 Method Sketch`；最新 owner/adjacent 已覆盖该控制边界：Ch22 已显式区分 checkpoint `M_0` 与 request-owned mutable `M_t`，并覆盖 sparse slots、write conflict、reset/session identity、external-memory boundary 与 frozen-path fallback。 exact-v1 non-proof=`5 Discussion; 8 Limitations and Next Steps; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28876 |
| SF-2026-ARXIV-2606-28896 | potential_books_delta | not_selected | — | — | 《A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation》未单列 Deep Analysis。决定性理由：SAR augmentation recipe/observer/repair 由领域数据与 observer 定义，且 5/11 batch 未达到最高 evidence level。 exact-v1 non-proof=`5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28896 |
| SF-2026-ARXIV-2606-28898 | potential_books_delta | not_selected | — | — | 《PASTA: A Paraphrasing And Self-Training Approach for Knowledge Updating in LLMs》未单列 Deep Analysis。决定性理由：日文新闻上的 paraphrase+self-training+CPT/SFT/DPO 是知识更新配方，不建立通用 DPO owner 变化。 exact-v1 non-proof=`5 Conclusion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28898 |
| SF-2026-ARXIV-2606-28900 | potential_books_delta | not_selected | — | — | 《MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28900v1 — §Design goals.; Training-oriented derivatives.`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`6 Discussion, Limitations, and Ethics; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28900 |
| SF-2026-ARXIV-2606-28925 | potential_books_delta | not_selected | — | — | 《Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28925v1 — §2.1. Tool/Agent Routing in LLM Systems; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 2.6. Multi-Agent Systems and Task Decomposition`；最新 owner/adjacent 已覆盖该控制边界：Ch82 已版本化 sender/receiver/channel/topology identity、message admission、latent translation 与 commitment，但未把 set routing、receiver-owned hierarchical read 和 full-KV integrity receipt 合成同一 channel contract。 exact-v1 non-proof=`7. Discussion; 8. Limitations; 10. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28925 |
| SF-2026-ARXIV-2606-28932 | potential_books_delta | not_selected | — | — | 《DLR: Zero-Inference-Cost Latent Residuals for Low-Rank Pre-Training》未单列 Deep Analysis。决定性理由：duplicated latent residual 与 closed-form fold 是 LLaMA-style low-rank pretraining 的局部参数化，部署图不变不足以形成训练系统新 contract。 exact-v1 non-proof=`5 Conclusion, Limitations and Outlook；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28932 |
| SF-2026-ARXIV-2606-28938 | potential_books_delta | not_selected | — | — | 《EVLA: An Electro-Aware Multimodal Assistant for Physically-Grounded Driving Reasoning and Control》未单列 Deep Analysis。决定性理由：electro-aware driving co-state 只由 synthesized/simulated control proxy 验证，未形成 closed-loop road-safety 结论。 exact-v1 non-proof=`4.8 Discussion; 5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28938 |
| SF-2026-ARXIV-2606-28939 | potential_books_delta | not_selected | — | — | 《ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28939v1 — §4 Our Approach: ReGuide; Appendix B Algorithm`；最新 owner/adjacent 已覆盖该控制边界：Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 exact-v1 non-proof=`6 Conclusion and Limitations; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28939 |
| SF-2026-ARXIV-2606-28953 | potential_books_delta; forced_review | not_selected | — | — | 《Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28953v1 — §Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 4.5 Proposed defense vs prior methods; 5.1 Proposed defense vs prior methods`；最新 owner/adjacent 已覆盖该控制边界：Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 exact-v1 non-proof=`Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 2 Threat Model; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28953 |
| SF-2026-ARXIV-2606-28955 | score_7_9; potential_books_delta | not_selected | — | — | 《Modification-Considering Value Learning for Reward Hacking Mitigation in RL》未单列 Deep Analysis。决定性理由：其长期 delta 已进入 `TRAIN-RLHF`，但跨层影响弱于四个已冻结分析单元：在 transition admission 前冻结 current policy/return estimator，以 equal budget 预测 modified-policy counterfactual；只有 evaluator 接受才写入 replay。 exact-v1 non-proof=`5 Limitations and Future Work; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28955 |
| SF-2026-ARXIV-2606-28958 | potential_books_delta | not_selected | — | — | 《When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28958v1 — §Report GitHub Issue; When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration`；最新 owner/adjacent 已覆盖该控制边界：Ch82 已版本化 sender/receiver/channel/topology identity、message admission、latent translation 与 commitment，但未把 set routing、receiver-owned hierarchical read 和 full-KV integrity receipt 合成同一 channel contract。 exact-v1 non-proof=`3 Problem Setting and Threat Model; 8.4 Transport Integrity and Fail-Closed Boundary; 9 Failure Modes and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28958 |
| SF-2026-ARXIV-2606-28962 | potential_books_delta; forced_review | not_selected | — | — | 《FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28962v1 — §III Methodology; III-B Defense Framework Design; III-C Defense Metric Design`；最新 owner/adjacent 已覆盖该控制边界：Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 exact-v1 non-proof=`III-A Threat Model; V Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28962 |
| SF-2026-ARXIV-2606-28995 | score_7_9; potential_books_delta | selected | DA-20260628-COMPILED-PHYSICAL-SAFETY | — | 《HJ-SafeDMP: Hamilton-Jacobi Reachability-Guided Dynamic Movement Primitives for Provably Safe Robot Motion》被选为 `DA-20260628-COMPILED-PHYSICAL-SAFETY` 的代表 family，因为 `把离线 HJ/CBVF learned value 与 conformal calibration 编译为在线 closed-form DMP safety modulation；controller 仍拥有 physical commit。`。选择依据先冻结于 protocol/channel/metric/physical-safety 的跨层 control ownership；未证明边界是 `VI Conclusion, Limitations and Future Works；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis:DA-20260628-COMPILED-PHYSICAL-SAFETY |
| SF-2026-ARXIV-2606-28998 | potential_books_delta | not_selected | — | — | 《Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28998v1 — §3. Methodology`；最新 owner/adjacent 已覆盖该控制边界：Ch34 已绑定 base/reference/policy identity、preference construction、functional/non-functional trade-off 与 regression evaluation。 exact-v1 non-proof=`3.6. Threats to Validity; Small Model Limitations; Failure Cases；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-28998 |
| SF-2026-ARXIV-2606-29013 | potential_books_delta | not_selected | — | — | 《Mural: Transferring LLM knowledge to image generation via Mixture-of-Transformers》未单列 Deep Analysis。决定性理由：frozen Qwen branch+image expert 的 MoT 是局部 multimodal architecture；定性 transfer 不证明跨 backbone 的生成 owner 演进。 exact-v1 non-proof=`5 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29013 |
| SF-2026-ARXIV-2606-29030 | potential_books_delta | not_selected | — | — | 《Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29030v1 — §III Architecture of the Proposed Agent`；最新 owner/adjacent 已覆盖该控制边界：Ch77 已拥有 typed write/read、provenance、conflict、transaction、visibility、rollback 与 graph dependency 生命周期。 exact-v1 non-proof=`VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29030 |
| SF-2026-ARXIV-2606-29033 | potential_books_delta | not_selected | — | — | 《Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29033v1 — §Approach 1: Human Verification of AI Proposals.; Approach 2: Manual Test Sets.; Approach 3: Humans Specify Criteria, AI Applies Them at Scale.`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`6. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29033 |
| SF-2026-ARXIV-2606-29038 | score_7_9; potential_books_delta | selected | DA-20260628-SINGLE-METRIC-CONTRACT | — | 《Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy》被选为 `DA-20260628-SINGLE-METRIC-CONTRACT` 的代表 family，因为 `将 metric extraction/aggregation 实现提升为一个版本化 callable contract，由 optimizer、evaluator 与 champion selector 调用同一 artifact，并保留 raw trajectory 重算路径。`。选择依据先冻结于 protocol/channel/metric/physical-safety 的跨层 control ownership；未证明边界是 `Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy; 6 Discussion; 7 Limitations and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis:DA-20260628-SINGLE-METRIC-CONTRACT |
| SF-2026-ARXIV-2606-29054 | potential_books_delta | not_selected | — | — | 《When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29054v1 — §2 Method; Ministral violations expose framework limits.; Practical decision framework.`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`4 Discussion; 6 Conclusion; Threats to validity and limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29054 |
| SF-2026-ARXIV-2606-29059 | potential_books_delta | not_selected | — | — | 《Flow Matching in Feature Space for Stochastic World Modeling》未单列 Deep Analysis。决定性理由：frozen DINO latent 上的 feature-space flow 是 context-video 模型路线，非 action-conditioned 且 sampler/BPTT 成本高。 exact-v1 non-proof=`6 Conclusion; Practical limitations.; Appendix J Discussion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29059 |
| SF-2026-ARXIV-2606-29066 | score_7_9; potential_books_delta | not_selected | — | — | 《$x$-Prediction Flow: Efficient Continuous Decoding for Masked Diffusion Language Models》未单列 Deep Analysis。决定性理由：其长期 delta 已进入 `INFER-DECODE`，但跨层影响弱于四个已冻结分析单元：masked-diffusion decoder 为每个 token 保存可连续携带的 x-prediction mixture 与 progress，允许 bounded re-edit，只有 commit state 才进入可见 frontier。 exact-v1 non-proof=`7 Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29066 |
| SF-2026-ARXIV-2606-29067 | potential_books_delta | not_selected | — | — | 《ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29067v1 — §3 Method; H.1 Study Design`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`Layer 1: Structural segmentation and boundary classification.; Layer 2: Soft boundary detection.; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29067 |
| SF-2026-ARXIV-2606-29073 | potential_books_delta | subsumed | — | DA-20260628-PROTOCOL-EXECUTION-INVARIANTS | 《From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes》的 `把 connection capability lowering 为 grant、handle、policy 与 audit objects；每次执行先验证 machine-readable invariant，capability 仍不等于 authorization。` 与 `DA-20260628-PROTOCOL-EXECUTION-INVARIANTS` 共享同一控制链，因此保留独立 Books evidence，但不另建 Deep Analysis；边界为 `3 Threat Model; 6.3 Reproducibility Boundary; 8 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis:DA-20260628-PROTOCOL-EXECUTION-INVARIANTS |
| SF-2026-ARXIV-2606-29082 | potential_books_delta | not_selected | — | — | 《Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29082v1 — §EFT serves as mid-training for test-time RL.; Appendix C Additional Details of Dataset Construction Method; C.1 Systematic Error Breakdown Analysis`；最新 owner/adjacent 已覆盖该控制边界：Ch28 已拥有 optimizer/schedule/precision/budget、mid-training skill artifact、search experience 与 downstream promotion receipt。 exact-v1 non-proof=`7 Conclusion; Limitations; Appendix B Further Details and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29082 |
| SF-2026-ARXIV-2606-29088 | potential_books_delta | not_selected | — | — | 《Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29088v1 — §Report GitHub Issue; Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`5 Discussion; 6 Threats to Validity; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29088 |
| SF-2026-ARXIV-2606-29089 | potential_books_delta | not_selected | — | — | 《TAP-VLA: Tactile Annotation Prompting for Vision Language Action Models》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29089v1 — §3 Method`；最新 owner/adjacent 已覆盖该控制边界：Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 exact-v1 non-proof=`5 Discussion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29089 |
| SF-2026-ARXIV-2606-29090 | potential_books_delta | not_selected | — | — | 《AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29090v1 — §III Methodology and Framework; III-A Overall Framework; III-B System Architecture`；最新 owner/adjacent 已覆盖该控制边界：Ch76 已拥有 multi-index retrieval、budgeted stopping、procedural corpus、evidence sufficiency、provenance 与 fallback。 exact-v1 non-proof=`V-F Qualitative Examples and Discussion; VI Conclusion and Future Work; VI-A Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29090 |
| SF-2026-ARXIV-2606-29091 | potential_books_delta | not_selected | — | — | 《Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29091v1 — §Chance across architectures.`；最新 owner/adjacent 已覆盖该控制边界：Ch76 已拥有 multi-index retrieval、budgeted stopping、procedural corpus、evidence sufficiency、provenance 与 fallback。 exact-v1 non-proof=`6 Discussion & Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29091 |
| SF-2026-ARXIV-2606-29094 | potential_books_delta | not_selected | — | — | 《DiLaServe: High SLO Attainment Serving for Diffusion Language Models》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29094v1 — §3.1. Design Overview; Appendix C Algorithm for Supporting Approximate KV Caching`；最新 owner/adjacent 已覆盖该控制边界：Ch56 已把 admission、iteration scheduling、routing/placement、autoscaling、TP/KV state、预测误差与 SLO 放入多时间尺度控制面。 exact-v1 non-proof=`7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29094 |
| SF-2026-ARXIV-2606-29097 | potential_books_delta | not_selected | — | — | 《TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29097v1 — §3 Method`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`5 Limitations and Future Work; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29097 |
| SF-2026-ARXIV-2606-29108 | potential_books_delta | not_selected | — | — | 《Symbolon: Symbolic Execution by Learning Code Transformation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`arXiv:2606.29108v1 version-stamped mirror — §Our approach; III Methodology`；最新 owner/adjacent 已覆盖该控制边界：Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 exact-v1 non-proof=`VI Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29108 |
| SF-2026-ARXIV-2606-29112 | potential_books_delta; forced_review | not_selected | — | — | 《A Novel Latent-Class Attack and its Detection by Class Subspace Orthogonalization》未单列 Deep Analysis。决定性理由：class-subspace detector 只覆盖两个小图像数据集和一种 latent-class attack，不能外推为平台安全机制。 exact-v1 non-proof=`5 Summary; Instructions for reporting errors；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29112 |
| SF-2026-ARXIV-2606-29116 | potential_books_delta | not_selected | — | — | 《Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29116v1 — §Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem`；最新 owner/adjacent 已覆盖该控制边界：Ch84 已把 agent definition、workflow graph、runtime/harness identity、trace、promotion 与 side-effect evidence 纳入平台生命周期。 exact-v1 non-proof=`3.4 RQ3: Failure Handling; 5 Discussion; 5.1 Threats to Construct Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29116 |
| SF-2026-ARXIV-2606-29119 | potential_books_delta | not_selected | — | — | 《Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29119v1 — §Report GitHub Issue; Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`8 Limitations; 9 Discussion and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29119 |
| SF-2026-ARXIV-2606-29124 | potential_books_delta; forced_review | subsumed | — | DA-20260628-PROTOCOL-EXECUTION-INVARIANTS | 《CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs》的 `把 protocol specification revision、constraint sentence、extremal input、reference expansion、differential result 与 human verdict 串成一条安全测试 lineage。` 与 `DA-20260628-PROTOCOL-EXECUTION-INVARIANTS` 共享同一控制链，因此保留独立 Books evidence，但不另建 Deep Analysis；边界为 `2.3 SMTP Nesting Failures (Mailpit); Boundary value analysis (BVA):; 6 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis:DA-20260628-PROTOCOL-EXECUTION-INVARIANTS |
| SF-2026-ARXIV-2606-29126 | potential_books_delta | not_selected | — | — | 《HiComm: Hierarchical Communication for Multi-agent Reinforcement Learning》未单列 Deep Analysis。决定性理由：环境预给 hierarchy 下的 receiver-driven raw-feature addressing 是 cooperative MARL 的局部通信方法；它未建立跨环境的 channel identity、admission 或 privacy contract。 exact-v1 non-proof=`6 Conclusion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29126 |
| SF-2026-ARXIV-2606-29129 | potential_books_delta | not_selected | — | — | 《Improved Scaling for Fast Mode of Ozaki Scheme II》未单列 Deep Analysis。决定性理由：Ozaki II scaling 是 GH200/INT8 GEMM 的数学与 kernel 局部改进，不改变 execution-plan owner。 exact-v1 non-proof=`3 Limitation of Fast Mode Scaling; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。 | analysis-decision:SF-2026-ARXIV-2606-29129 |

<!-- analysis-decision:SF-2026-ARXIV-2606-28666:start -->
《Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28666v1 — §2.6 TRiSM framework; 3 Methodology; 3.2 Framework used`；最新 owner/adjacent 已覆盖该控制边界：Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 exact-v1 non-proof=`6 Future work and limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28666:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28679:start -->
《Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28679v1 — §Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; III The Cross-Framework Gap; III-A Method and selection`；最新 owner/adjacent 已覆盖该控制边界：Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 exact-v1 non-proof=`Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; II Threat Model; II-A Boundary and adversary；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28679:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28692:start -->
《An AI agent for treatment reasoning over a biomedical tool universe》未单列 Deep Analysis。决定性理由：两层 clinical self-learning 与 212-tool loop 仍由单一医疗工具宇宙、观察性 EHR 与领域 rubric 定义，不能改写通用 Workflow owner。 exact-v1 non-proof=`Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28692:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28707:start -->
《BV-Blend: Uncertainty-Weighted Historical Baselines for Stable Critic-Free RL with Verifiable Rewards》未单列 Deep Analysis。决定性理由：semantic-cluster historical baseline 是 critic-free RL 的局部方差控制器；它没有改变 verifier、trajectory 或 reward authority。 exact-v1 non-proof=`5 Conclusion; Limitations; D.1 Discussion of Key Assumptions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28707:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28712:start -->
《J-LAW: Joint Localization and Actionable World Modeling via Coupled Latent Factor Graphs》未单列 Deep Analysis。决定性理由：coupled factor graph 与 alternating IRLS 是四个 WildGS scene 上的局部优化路线，且更复杂 joint setting 并不稳定优于 pose-only。 exact-v1 non-proof=`V Conclusion and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28712:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28715:start -->
《SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28715v1 — §Report GitHub Issue; SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`6 Analysis and Discussion; 7 Conclusion; 8 Limitation；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28715:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28720:start -->
《CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28720v1 — §III METHOD; IV-B System-level Comparisons`；最新 owner/adjacent 已覆盖该控制边界：Ch25 已拥有 persistent/action-conditioned state、stochastic rollout、entity identity、simulation artifact 与 physical commit boundary。 exact-v1 non-proof=`V CONCLUSIONS；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28720:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28725:start -->
《DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28725v1 — §III Methodology; III-A Framework Overview; IV-B Model and Training Details`；最新 owner/adjacent 已覆盖该控制边界：Ch67 已把多 sensor、drift、checkpoint freshness、observe-only authority、告警与 rollback 分层。 exact-v1 non-proof=`VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28725:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28733:start -->
《Agentic Abstention: Do Agents Know When to Stop Instead of Act?》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28733v1 — §5 Our Proposed Method for Improving Agentic Abstention: convolve; G.1 Task setting and training configuration; I.2.1 System Prompt for WebShop`；最新 owner/adjacent 已覆盖该控制边界：Ch79 已把 proposal、pre-commit verifier、environment feedback、abstention 与 executable commit 分权。 exact-v1 non-proof=`7 Conclusion; Appendix A Limitations; Failure to abstain from GPT-5.4-mini；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28733:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28739:start -->
《Agent Safety Is Action Alignment》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28739v1 — §Report GitHub Issue; Agent Safety Is Action Alignment`；最新 owner/adjacent 已覆盖该控制边界：Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 exact-v1 non-proof=`5.2. External Enforcement at the Action Boundary; 7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28739:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28747:start -->
《Self-Supervised Theorem Discovery in a Formal Axiomatic System》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28747v1 — §Self-Supervised Theorem Discovery in a Formal Axiomatic System; Rules of the Hilbert System.`；最新 owner/adjacent 已覆盖该控制边界：Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 exact-v1 non-proof=`7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28747:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28751:start -->
《A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility》未单列 Deep Analysis。决定性理由：path-space/irreversibility 主要是受控小模型上的理论结构；planning/uncertainty 结论尚未形成可部署 state contract。 exact-v1 non-proof=`VII Results and discussion; VII.5 Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28751:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28754:start -->
《SHIFT: Dynamic Compute Relocation Framework for Communication-Aware Chiplet-Based Systems》未单列 Deep Analysis。决定性理由：NoIF/SHIFT 只在作者 wafer/chiplet simulator 中成立，数据中心迁移仍是 future work，不能改写 cluster GPU scheduler。 exact-v1 non-proof=`VI Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28754:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28757:start -->
《A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28757v1 — §Effect of Post-Training.; C Global Dynamic Reconstruction Methodology; G Post Training Details`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`5 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28757:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28758:start -->
《X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving》未单列 Deep Analysis。决定性理由：96-token sketch 与 embedded world model 是驾驶模型局部架构，没有建立跨任务 world-state owner 或 physical promotion contract。 exact-v1 non-proof=`5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28758:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28772:start -->
《Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain》未单列 Deep Analysis。决定性理由：其长期 delta 已进入 `TRAIN-DATA`，但跨层影响弱于四个已冻结分析单元：把 per-annotator label、threshold/disagreement 与聚合 rule 作为训练数据状态保存；majority label 只是一个 materialized view，不能删除 contested boundary。 exact-v1 non-proof=`Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain; 4.1 Disagreement Concentrates at the Value Boundary; 4.5 Boundary Disagreement Is Not Driven by Annotation Error；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28772:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28781:start -->
《HyphaeDB: A Living Knowledge Topology for Agent-First Memory》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28781v1 — §2.1 Agent Memory Systems; 3 Architecture; 4.1 Propagation Algorithm`；最新 owner/adjacent 已覆盖该控制边界：Ch77 已拥有 typed write/read、provenance、conflict、transaction、visibility、rollback 与 graph dependency 生命周期。 exact-v1 non-proof=`9 Discussion; 9.2 Limitations and Future Work; 10 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28781:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28804:start -->
《ViPSim: Collaborating Visual and Parameter Spaces for Consistent Long-Horizon Embodied World Models》未单列 Deep Analysis。决定性理由：visual/parameter-space 协同视频生成是特定 embodied world-model 架构；OOD affordance 与 morphology failure 阻止其成为长期系统结论。 exact-v1 non-proof=`V Limitations; VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28804:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28813:start -->
《Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28813v1 — §Training data.; Appendix E Constraint-Aware Steering Algorithm; Appendix F Model and Training Details`；最新 owner/adjacent 已覆盖该控制边界：Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 exact-v1 non-proof=`6 Limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28813:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28831:start -->
《HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28831v1 — §System-Algorithm Co-Design in LLM Inference; 3 The Hard-KV Design; 3.1 The Framework Overview`；最新 owner/adjacent 已覆盖该控制边界：Ch45 已拥有 head/layer/page-aware eviction、quality-memory calibration、residual path、refresh、FullKV fallback 与 production SLO 边界。 exact-v1 non-proof=`5 Conclusion and Future Work; Appendix B Further Discussions on KV Index Regularization; B.2 Discussion on trade-off in the Index Management for Layerwise Selection；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28831:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28839:start -->
《The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28839v1 — §The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems —and Auditing the Claims It Enables; Multi-agent LLM systems.; Network contagion and spectral methods.`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`4.1.4 Experiment 3: Real-API with Functional BOUNDARY_SYNC; 6 Discussion; 7 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28839:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28841:start -->
《LAMP: Lean-based Agentic framework with MCP and Proof Repair》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28841v1 — §LAMP: Lean-based Agentic framework with MCP and Proof Repair; 2.3 Agentic Frameworks for Theorem Proving; 3 The LAMP System`；最新 owner/adjacent 已覆盖该控制边界：Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 exact-v1 non-proof=`5 Discussion and Limitations; Failure Analysis:; Limitations and Future Work:；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28841:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28843:start -->
《The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28843v1 — §5.3 Pre-training distributions and scale`；最新 owner/adjacent 已覆盖该控制边界：Ch29 已把 demonstration distribution、language/model slice、安全回归、forgetting 与 serving interface 分开验收。 exact-v1 non-proof=`7 Discussion; 7.2 Limitations; 8 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28843:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28862:start -->
《HKVLM: Faithful Query--Region Binding for Frozen-Detector Visual Grounding》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28862v1 — §4 Method: HKVLM; 4.5 Cold-start training; 5 Experimental Design and Evaluation Protocol`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`8 Discussion, Limitations, and Broader Impact; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28862:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28863:start -->
《Defeat Devices in AI Systems》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28863v1 — §Defeat Devices in AI Systems; 4.1 Five method families; 5.1 Defeat devices can naturally emerge in AI systems`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`2.4 Boundary cases; 6.5 Limitations; 7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28863:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28864:start -->
《On Test-Time Scaling for Vision-Language Models》未单列 Deep Analysis。决定性理由：九种 VLM test-time strategy 的胜负随模型、prompt、benchmark 与 extraction 改变，只保留经验上下文。 exact-v1 non-proof=`7 Conclusion; S12 Other model failures；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28864:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28867:start -->
《Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28867v1 — §Legal analysis of AI training data.`；最新 owner/adjacent 已覆盖该控制边界：Ch27 已拥有 sample/transform/label provenance、license、lineage、mixture 与 admission，但尚未要求保留 per-annotator distribution 以阻止 majority label 静默取得价值边界真值。 exact-v1 non-proof=`6. Four Failure Modes; 6.4. Data Persistence Failure: The Congolese Radio Corpus; 9. Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28867:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28876:start -->
《Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28876v1 — §2 Method Sketch`；最新 owner/adjacent 已覆盖该控制边界：Ch22 已显式区分 checkpoint `M_0` 与 request-owned mutable `M_t`，并覆盖 sparse slots、write conflict、reset/session identity、external-memory boundary 与 frozen-path fallback。 exact-v1 non-proof=`5 Discussion; 8 Limitations and Next Steps; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28876:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28896:start -->
《A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation》未单列 Deep Analysis。决定性理由：SAR augmentation recipe/observer/repair 由领域数据与 observer 定义，且 5/11 batch 未达到最高 evidence level。 exact-v1 non-proof=`5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28896:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28898:start -->
《PASTA: A Paraphrasing And Self-Training Approach for Knowledge Updating in LLMs》未单列 Deep Analysis。决定性理由：日文新闻上的 paraphrase+self-training+CPT/SFT/DPO 是知识更新配方，不建立通用 DPO owner 变化。 exact-v1 non-proof=`5 Conclusion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28898:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28900:start -->
《MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28900v1 — §Design goals.; Training-oriented derivatives.`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`6 Discussion, Limitations, and Ethics; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28900:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28925:start -->
《Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28925v1 — §2.1. Tool/Agent Routing in LLM Systems; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 2.6. Multi-Agent Systems and Task Decomposition`；最新 owner/adjacent 已覆盖该控制边界：Ch82 已版本化 sender/receiver/channel/topology identity、message admission、latent translation 与 commitment，但未把 set routing、receiver-owned hierarchical read 和 full-KV integrity receipt 合成同一 channel contract。 exact-v1 non-proof=`7. Discussion; 8. Limitations; 10. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28925:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28932:start -->
《DLR: Zero-Inference-Cost Latent Residuals for Low-Rank Pre-Training》未单列 Deep Analysis。决定性理由：duplicated latent residual 与 closed-form fold 是 LLaMA-style low-rank pretraining 的局部参数化，部署图不变不足以形成训练系统新 contract。 exact-v1 non-proof=`5 Conclusion, Limitations and Outlook；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28932:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28938:start -->
《EVLA: An Electro-Aware Multimodal Assistant for Physically-Grounded Driving Reasoning and Control》未单列 Deep Analysis。决定性理由：electro-aware driving co-state 只由 synthesized/simulated control proxy 验证，未形成 closed-loop road-safety 结论。 exact-v1 non-proof=`4.8 Discussion; 5 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28938:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28939:start -->
《ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28939v1 — §4 Our Approach: ReGuide; Appendix B Algorithm`；最新 owner/adjacent 已覆盖该控制边界：Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 exact-v1 non-proof=`6 Conclusion and Limitations; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28939:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28953:start -->
《Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28953v1 — §Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 4.5 Proposed defense vs prior methods; 5.1 Proposed defense vs prior methods`；最新 owner/adjacent 已覆盖该控制边界：Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 exact-v1 non-proof=`Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 2 Threat Model; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28953:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28955:start -->
《Modification-Considering Value Learning for Reward Hacking Mitigation in RL》未单列 Deep Analysis。决定性理由：其长期 delta 已进入 `TRAIN-RLHF`，但跨层影响弱于四个已冻结分析单元：在 transition admission 前冻结 current policy/return estimator，以 equal budget 预测 modified-policy counterfactual；只有 evaluator 接受才写入 replay。 exact-v1 non-proof=`5 Limitations and Future Work; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28955:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28958:start -->
《When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28958v1 — §Report GitHub Issue; When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration`；最新 owner/adjacent 已覆盖该控制边界：Ch82 已版本化 sender/receiver/channel/topology identity、message admission、latent translation 与 commitment，但未把 set routing、receiver-owned hierarchical read 和 full-KV integrity receipt 合成同一 channel contract。 exact-v1 non-proof=`3 Problem Setting and Threat Model; 8.4 Transport Integrity and Fail-Closed Boundary; 9 Failure Modes and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28958:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28962:start -->
《FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28962v1 — §III Methodology; III-B Defense Framework Design; III-C Defense Metric Design`；最新 owner/adjacent 已覆盖该控制边界：Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 exact-v1 non-proof=`III-A Threat Model; V Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28962:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28998:start -->
《Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.28998v1 — §3. Methodology`；最新 owner/adjacent 已覆盖该控制边界：Ch34 已绑定 base/reference/policy identity、preference construction、functional/non-functional trade-off 与 regression evaluation。 exact-v1 non-proof=`3.6. Threats to Validity; Small Model Limitations; Failure Cases；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-28998:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29013:start -->
《Mural: Transferring LLM knowledge to image generation via Mixture-of-Transformers》未单列 Deep Analysis。决定性理由：frozen Qwen branch+image expert 的 MoT 是局部 multimodal architecture；定性 transfer 不证明跨 backbone 的生成 owner 演进。 exact-v1 non-proof=`5 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29013:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29030:start -->
《Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29030v1 — §III Architecture of the Proposed Agent`；最新 owner/adjacent 已覆盖该控制边界：Ch77 已拥有 typed write/read、provenance、conflict、transaction、visibility、rollback 与 graph dependency 生命周期。 exact-v1 non-proof=`VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29030:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29033:start -->
《Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29033v1 — §Approach 1: Human Verification of AI Proposals.; Approach 2: Manual Test Sets.; Approach 3: Humans Specify Criteria, AI Applies Them at Scale.`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`6. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29033:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29054:start -->
《When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29054v1 — §2 Method; Ministral violations expose framework limits.; Practical decision framework.`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`4 Discussion; 6 Conclusion; Threats to validity and limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29054:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29059:start -->
《Flow Matching in Feature Space for Stochastic World Modeling》未单列 Deep Analysis。决定性理由：frozen DINO latent 上的 feature-space flow 是 context-video 模型路线，非 action-conditioned 且 sampler/BPTT 成本高。 exact-v1 non-proof=`6 Conclusion; Practical limitations.; Appendix J Discussion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29059:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29066:start -->
《$x$-Prediction Flow: Efficient Continuous Decoding for Masked Diffusion Language Models》未单列 Deep Analysis。决定性理由：其长期 delta 已进入 `INFER-DECODE`，但跨层影响弱于四个已冻结分析单元：masked-diffusion decoder 为每个 token 保存可连续携带的 x-prediction mixture 与 progress，允许 bounded re-edit，只有 commit state 才进入可见 frontier。 exact-v1 non-proof=`7 Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29066:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29067:start -->
《ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29067v1 — §3 Method; H.1 Study Design`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`Layer 1: Structural segmentation and boundary classification.; Layer 2: Soft boundary detection.; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29067:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29082:start -->
《Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29082v1 — §EFT serves as mid-training for test-time RL.; Appendix C Additional Details of Dataset Construction Method; C.1 Systematic Error Breakdown Analysis`；最新 owner/adjacent 已覆盖该控制边界：Ch28 已拥有 optimizer/schedule/precision/budget、mid-training skill artifact、search experience 与 downstream promotion receipt。 exact-v1 non-proof=`7 Conclusion; Limitations; Appendix B Further Details and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29082:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29088:start -->
《Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29088v1 — §Report GitHub Issue; Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`5 Discussion; 6 Threats to Validity; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29088:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29089:start -->
《TAP-VLA: Tactile Annotation Prompting for Vision Language Action Models》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29089v1 — §3 Method`；最新 owner/adjacent 已覆盖该控制边界：Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 exact-v1 non-proof=`5 Discussion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29089:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29090:start -->
《AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29090v1 — §III Methodology and Framework; III-A Overall Framework; III-B System Architecture`；最新 owner/adjacent 已覆盖该控制边界：Ch76 已拥有 multi-index retrieval、budgeted stopping、procedural corpus、evidence sufficiency、provenance 与 fallback。 exact-v1 non-proof=`V-F Qualitative Examples and Discussion; VI Conclusion and Future Work; VI-A Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29090:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29091:start -->
《Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29091v1 — §Chance across architectures.`；最新 owner/adjacent 已覆盖该控制边界：Ch76 已拥有 multi-index retrieval、budgeted stopping、procedural corpus、evidence sufficiency、provenance 与 fallback。 exact-v1 non-proof=`6 Discussion & Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29091:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29094:start -->
《DiLaServe: High SLO Attainment Serving for Diffusion Language Models》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29094v1 — §3.1. Design Overview; Appendix C Algorithm for Supporting Approximate KV Caching`；最新 owner/adjacent 已覆盖该控制边界：Ch56 已把 admission、iteration scheduling、routing/placement、autoscaling、TP/KV state、预测误差与 SLO 放入多时间尺度控制面。 exact-v1 non-proof=`7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29094:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29097:start -->
《TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29097v1 — §3 Method`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`5 Limitations and Future Work; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29097:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29108:start -->
《Symbolon: Symbolic Execution by Learning Code Transformation》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`arXiv:2606.29108v1 version-stamped mirror — §Our approach; III Methodology`；最新 owner/adjacent 已覆盖该控制边界：Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 exact-v1 non-proof=`VI Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29108:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29112:start -->
《A Novel Latent-Class Attack and its Detection by Class Subspace Orthogonalization》未单列 Deep Analysis。决定性理由：class-subspace detector 只覆盖两个小图像数据集和一种 latent-class attack，不能外推为平台安全机制。 exact-v1 non-proof=`5 Summary; Instructions for reporting errors；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29112:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29116:start -->
《Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29116v1 — §Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem`；最新 owner/adjacent 已覆盖该控制边界：Ch84 已把 agent definition、workflow graph、runtime/harness identity、trace、promotion 与 side-effect evidence 纳入平台生命周期。 exact-v1 non-proof=`3.4 RQ3: Failure Handling; 5 Discussion; 5.1 Threats to Construct Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29116:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29119:start -->
《Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule》未单列 Deep Analysis。决定性理由：其 source-specific mechanism=`https://arxiv.org/html/2606.29119v1 — §Report GitHub Issue; Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule`；最新 owner/adjacent 已覆盖该控制边界：Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 exact-v1 non-proof=`8 Limitations; 9 Discussion and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29119:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29126:start -->
《HiComm: Hierarchical Communication for Multi-agent Reinforcement Learning》未单列 Deep Analysis。决定性理由：环境预给 hierarchy 下的 receiver-driven raw-feature addressing 是 cooperative MARL 的局部通信方法；它未建立跨环境的 channel identity、admission 或 privacy contract。 exact-v1 non-proof=`6 Conclusion and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29126:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29129:start -->
《Improved Scaling for Fast Mode of Ozaki Scheme II》未单列 Deep Analysis。决定性理由：Ozaki II scaling 是 GH200/INT8 GEMM 的数学与 kernel 局部改进，不改变 execution-plan owner。 exact-v1 non-proof=`3 Limitation of Fast Mode Scaling; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。`。
<!-- analysis-decision:SF-2026-ARXIV-2606-29129:end -->

<!-- analysis:DA-20260628-PROTOCOL-EXECUTION-INVARIANTS:start -->
### DA-20260628-PROTOCOL-EXECUTION-INVARIANTS

Protocol connectivity 必须先编译成可组合状态与可执行 invariant，再由 effect authorization commit；composition counterexample、grant/handle object 与 extremal differential test 是一条证据链。
<!-- analysis:DA-20260628-PROTOCOL-EXECUTION-INVARIANTS:end -->

<!-- analysis:DA-20260628-COMPILED-PHYSICAL-SAFETY:start -->
### DA-20260628-COMPILED-PHYSICAL-SAFETY

离线 reachability approximation 可以降低在线 safety-filter 成本，但 learned value 与 calibration 只提供 bounded sensor；real observation/controller 继续拥有物理 commit。
<!-- analysis:DA-20260628-COMPILED-PHYSICAL-SAFETY:end -->

<!-- analysis:DA-20260628-SINGLE-METRIC-CONTRACT:start -->
### DA-20260628-SINGLE-METRIC-CONTRACT

优化、评估与 champion selection 若分别重写 aggregation，会在同一候选集上制造 selection inversion；metric implementation 必须成为唯一版本化执行 artifact。
<!-- analysis:DA-20260628-SINGLE-METRIC-CONTRACT:end -->

## 6. Books Comparison

 and Decision

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-28666 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28666 | delta:SF-2026-ARXIV-2606-28666 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28666 |
| SF-2026-ARXIV-2606-28679 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28679 | delta:SF-2026-ARXIV-2606-28679 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28679 |
| SF-2026-ARXIV-2606-28690 | AGENT-MCP | books/part-07-agent/83-mcp.md#L178 — ## Tool Catalog 扩大后，Discovery 与 Execution 必须分离 | books/part-07-agent/82-multi-agent.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28690 | delta:SF-2026-ARXIV-2606-28690 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28690 |
| SF-2026-ARXIV-2606-28715 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28715 | delta:SF-2026-ARXIV-2606-28715 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28715 |
| SF-2026-ARXIV-2606-28720 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251 — ## State ownership | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28720 | delta:SF-2026-ARXIV-2606-28720 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28720 |
| SF-2026-ARXIV-2606-28725 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L206 — ## Monitoring 也会改变系统 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28725 | delta:SF-2026-ARXIV-2606-28725 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28725 |
| SF-2026-ARXIV-2606-28733 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L271 — ## 完成证据与 Verification | books/part-07-agent/78-tool-calling.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28733 | delta:SF-2026-ARXIV-2606-28733 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28733 |
| SF-2026-ARXIV-2606-28739 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28739 | delta:SF-2026-ARXIV-2606-28739 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28739 |
| SF-2026-ARXIV-2606-28747 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | books/part-07-agent/80-reflection.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28747 | delta:SF-2026-ARXIV-2606-28747 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28747 |
| SF-2026-ARXIV-2606-28757 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28757 | delta:SF-2026-ARXIV-2606-28757 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28757 |
| SF-2026-ARXIV-2606-28772 | TRAIN-DATA | books/part-04-training-system/27-data.md#L487 — ### 从 sample provenance 到训练生命周期 lineage | books/part-04-training-system/28-pretraining.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28772 | delta:SF-2026-ARXIV-2606-28772 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28772 |
| SF-2026-ARXIV-2606-28781 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L874 — ### Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery | books/part-07-agent/76-rag.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28781 | delta:SF-2026-ARXIV-2606-28781 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28781 |
| SF-2026-ARXIV-2606-28813 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L305 — ## Safety envelope | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28813 | delta:SF-2026-ARXIV-2606-28813 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28813 |
| SF-2026-ARXIV-2606-28831 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L735 — ### 先判断哪一种状态超出容量，再选择 TP 或 KV Compression | books/part-05-inference-system/44-decode.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28831 | delta:SF-2026-ARXIV-2606-28831 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28831 |
| SF-2026-ARXIV-2606-28839 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28839 | delta:SF-2026-ARXIV-2606-28839 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28839 |
| SF-2026-ARXIV-2606-28841 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | books/part-07-agent/80-reflection.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28841 | delta:SF-2026-ARXIV-2606-28841 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28841 |
| SF-2026-ARXIV-2606-28843 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L481 — ## Evaluation 应分开能力与行为 | books/part-04-training-system/30-lora.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28843 | delta:SF-2026-ARXIV-2606-28843 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28843 |
| SF-2026-ARXIV-2606-28862 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28862 | delta:SF-2026-ARXIV-2606-28862 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28862 |
| SF-2026-ARXIV-2606-28863 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28863 | delta:SF-2026-ARXIV-2606-28863 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28863 |
| SF-2026-ARXIV-2606-28867 | TRAIN-DATA | books/part-04-training-system/27-data.md#L487 — ### 从 sample provenance 到训练生命周期 lineage | books/part-04-training-system/28-pretraining.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28867 | delta:SF-2026-ARXIV-2606-28867 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28867 |
| SF-2026-ARXIV-2606-28876 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L283 — ### 从 Dense Checkpoint 迁移到 Hybrid State Model | books/part-02-model/21-moe.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28876 | delta:SF-2026-ARXIV-2606-28876 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28876 |
| SF-2026-ARXIV-2606-28900 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28900 | delta:SF-2026-ARXIV-2606-28900 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28900 |
| SF-2026-ARXIV-2606-28925 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L243 — ### Pairwise coupling 不能外推 group dynamics | books/part-07-agent/81-workflow.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28925 | delta:SF-2026-ARXIV-2606-28925 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28925 |
| SF-2026-ARXIV-2606-28939 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L305 — ## Safety envelope | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28939 | delta:SF-2026-ARXIV-2606-28939 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28939 |
| SF-2026-ARXIV-2606-28953 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28953 | delta:SF-2026-ARXIV-2606-28953 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28953 |
| SF-2026-ARXIV-2606-28955 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L168 — ## Reward hacking 与 Goodhart's Law | books/part-04-training-system/32-ppo.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28955 | delta:SF-2026-ARXIV-2606-28955 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28955 |
| SF-2026-ARXIV-2606-28958 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L243 — ### Pairwise coupling 不能外推 group dynamics | books/part-07-agent/81-workflow.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28958 | delta:SF-2026-ARXIV-2606-28958 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28958 |
| SF-2026-ARXIV-2606-28962 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28962 | delta:SF-2026-ARXIV-2606-28962 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28962 |
| SF-2026-ARXIV-2606-28995 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L305 — ## Safety envelope | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28995 | delta:SF-2026-ARXIV-2606-28995 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28995 |
| SF-2026-ARXIV-2606-28998 | TRAIN-DPO | books/part-04-training-system/34-dpo.md#L42 — ## KL-constrained 最优策略 | books/part-04-training-system/33-grpo.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28998 | delta:SF-2026-ARXIV-2606-28998 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28998 |
| SF-2026-ARXIV-2606-29030 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L874 — ### Memory Transaction Boundary 同时约束 Admission、Visibility 与 Recovery | books/part-07-agent/76-rag.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29030 | delta:SF-2026-ARXIV-2606-29030 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29030 |
| SF-2026-ARXIV-2606-29033 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29033 | delta:SF-2026-ARXIV-2606-29033 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29033 |
| SF-2026-ARXIV-2606-29038 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29038 | delta:SF-2026-ARXIV-2606-29038 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29038 |
| SF-2026-ARXIV-2606-29054 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29054 | delta:SF-2026-ARXIV-2606-29054 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29054 |
| SF-2026-ARXIV-2606-29066 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L174 — ## Decode 的结束条件 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29066 | delta:SF-2026-ARXIV-2606-29066 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-29066 |
| SF-2026-ARXIV-2606-29067 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29067 | delta:SF-2026-ARXIV-2606-29067 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29067 |
| SF-2026-ARXIV-2606-29073 | AGENT-MCP | books/part-07-agent/83-mcp.md#L178 — ## Tool Catalog 扩大后，Discovery 与 Execution 必须分离 | books/part-07-agent/82-multi-agent.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29073 | delta:SF-2026-ARXIV-2606-29073 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29073 |
| SF-2026-ARXIV-2606-29082 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L100 — ## 一次 training step 的状态流 | books/part-04-training-system/27-data.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29082 | delta:SF-2026-ARXIV-2606-29082 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29082 |
| SF-2026-ARXIV-2606-29088 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29088 | delta:SF-2026-ARXIV-2606-29088 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29088 |
| SF-2026-ARXIV-2606-29089 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L305 — ## Safety envelope | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29089 | delta:SF-2026-ARXIV-2606-29089 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29089 |
| SF-2026-ARXIV-2606-29090 | AGENT-RAG | books/part-07-agent/76-rag.md#L266 — ### Query、Compression 与 Stopping 是联合 Policy | books/part-07-agent/77-memory.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29090 | delta:SF-2026-ARXIV-2606-29090 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29090 |
| SF-2026-ARXIV-2606-29091 | AGENT-RAG | books/part-07-agent/76-rag.md#L266 — ### Query、Compression 与 Stopping 是联合 Policy | books/part-07-agent/77-memory.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29091 | delta:SF-2026-ARXIV-2606-29091 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29091 |
| SF-2026-ARXIV-2606-29094 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L16 — ## 调度对象从 request 变成 token state | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29094 | delta:SF-2026-ARXIV-2606-29094 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29094 |
| SF-2026-ARXIV-2606-29097 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29097 | delta:SF-2026-ARXIV-2606-29097 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29097 |
| SF-2026-ARXIV-2606-29108 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | books/part-07-agent/80-reflection.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29108 | delta:SF-2026-ARXIV-2606-29108 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29108 |
| SF-2026-ARXIV-2606-29116 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L399 — ## Agent Runtime State Machine | books/part-07-agent/83-mcp.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29116 | delta:SF-2026-ARXIV-2606-29116 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29116 |
| SF-2026-ARXIV-2606-29119 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1615 — ## Evaluation Run 的平台对象模型 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29119 | delta:SF-2026-ARXIV-2606-29119 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29119 |
| SF-2026-ARXIV-2606-29124 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-29124 | delta:SF-2026-ARXIV-2606-29124 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29124 |

<!-- existing:SF-2026-ARXIV-2606-28666:start -->
Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare》的 `https://arxiv.org/html/2606.28666v1 — §2.6 TRiSM framework; 3 Methodology; 3.2 Framework used` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28666:end -->

<!-- delta:SF-2026-ARXIV-2606-28666:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 2.6 TRiSM framework; 3 Methodology; 3.2 Framework used。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare》和上述 method locator 共同限定。`; `6 Future work and limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28666:end -->

<!-- books-review:SF-2026-ARXIV-2606-28666:start -->
Principle Reuse; No Change — Existing Coverage. Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare》的 `https://arxiv.org/html/2606.28666v1 — §2.6 TRiSM framework; 3 Methodology; 3.2 Framework used` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 2.6 TRiSM framework; 3 Methodology; 3.2 Framework used。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare》和上述 method locator 共同限定。`; `6 Future work and limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28666:end -->

<!-- existing:SF-2026-ARXIV-2606-28679:start -->
Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks》的 `https://arxiv.org/html/2606.28679v1 — §Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; III The Cross-Framework Gap; III-A Method and selection` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28679:end -->

<!-- delta:SF-2026-ARXIV-2606-28679:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; III The Cross-Framework Gap; III-A Method and selection。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks》和上述 method locator 共同限定。`; `Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; II Threat Model; II-A Boundary and adversary；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28679:end -->

<!-- books-review:SF-2026-ARXIV-2606-28679:start -->
Principle Reuse; No Change — Existing Coverage. Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks》的 `https://arxiv.org/html/2606.28679v1 — §Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; III The Cross-Framework Gap; III-A Method and selection` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; III The Cross-Framework Gap; III-A Method and selection。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks》和上述 method locator 共同限定。`; `Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks; II Threat Model; II-A Boundary and adversary；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28679:end -->

<!-- existing:SF-2026-ARXIV-2606-28690:start -->
Ch83 有 group admission，却没有 per-protocol IR、trace replay 与 pairwise composition counterexample 作为组合升级前的验证对象。
<!-- existing:SF-2026-ARXIV-2606-28690:end -->

<!-- delta:SF-2026-ARXIV-2606-28690:start -->
把每个 agent protocol lowering 为带 source/type evidence 的有限状态 IR，先做 pairwise composition 与 trace replay，再把 counterexample 编译成可执行回归；未知组合保持隔离。
<!-- delta:SF-2026-ARXIV-2606-28690:end -->

<!-- books-review:SF-2026-ARXIV-2606-28690:start -->
Direct Evolution; Integrate. Ch83 有 group admission，却没有 per-protocol IR、trace replay 与 pairwise composition counterexample 作为组合升级前的验证对象。 把每个 agent protocol lowering 为带 source/type evidence 的有限状态 IR，先做 pairwise composition 与 trace replay，再把 counterexample 编译成可执行回归；未知组合保持隔离。
<!-- books-review:SF-2026-ARXIV-2606-28690:end -->

<!-- existing:SF-2026-ARXIV-2606-28715:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages》的 `https://arxiv.org/html/2606.28715v1 — §Report GitHub Issue; SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28715:end -->

<!-- delta:SF-2026-ARXIV-2606-28715:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Report GitHub Issue; SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages》和上述 method locator 共同限定。`; `6 Analysis and Discussion; 7 Conclusion; 8 Limitation；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28715:end -->

<!-- books-review:SF-2026-ARXIV-2606-28715:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages》的 `https://arxiv.org/html/2606.28715v1 — §Report GitHub Issue; SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Report GitHub Issue; SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages》和上述 method locator 共同限定。`; `6 Analysis and Discussion; 7 Conclusion; 8 Limitation；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28715:end -->

<!-- existing:SF-2026-ARXIV-2606-28720:start -->
Ch25 已拥有 persistent/action-conditioned state、stochastic rollout、entity identity、simulation artifact 与 physical commit boundary。 Fresh owner+adjacent reread found that《CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance》的 `https://arxiv.org/html/2606.28720v1 — §III METHOD; IV-B System-level Comparisons` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28720:end -->

<!-- delta:SF-2026-ARXIV-2606-28720:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 III METHOD; IV-B System-level Comparisons。在 `MULTIMODAL-WORLD-MODELS` 中，该路径改变或检验的具体对象由题名《CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance》和上述 method locator 共同限定。`; `V CONCLUSIONS；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28720:end -->

<!-- books-review:SF-2026-ARXIV-2606-28720:start -->
Principle Reuse; No Change — Existing Coverage. Ch25 已拥有 persistent/action-conditioned state、stochastic rollout、entity identity、simulation artifact 与 physical commit boundary。 Fresh owner+adjacent reread found that《CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance》的 `https://arxiv.org/html/2606.28720v1 — §III METHOD; IV-B System-level Comparisons` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 III METHOD; IV-B System-level Comparisons。在 `MULTIMODAL-WORLD-MODELS` 中，该路径改变或检验的具体对象由题名《CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance》和上述 method locator 共同限定。`; `V CONCLUSIONS；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28720:end -->

<!-- existing:SF-2026-ARXIV-2606-28725:start -->
Ch67 已把多 sensor、drift、checkpoint freshness、observe-only authority、告警与 rollback 分层。 Fresh owner+adjacent reread found that《DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation》的 `https://arxiv.org/html/2606.28725v1 — §III Methodology; III-A Framework Overview; IV-B Model and Training Details` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28725:end -->

<!-- delta:SF-2026-ARXIV-2606-28725:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 III Methodology; III-A Framework Overview; IV-B Model and Training Details。在 `PLATFORM-MONITORING` 中，该路径改变或检验的具体对象由题名《DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation》和上述 method locator 共同限定。`; `VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28725:end -->

<!-- books-review:SF-2026-ARXIV-2606-28725:start -->
Principle Reuse; No Change — Existing Coverage. Ch67 已把多 sensor、drift、checkpoint freshness、observe-only authority、告警与 rollback 分层。 Fresh owner+adjacent reread found that《DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation》的 `https://arxiv.org/html/2606.28725v1 — §III Methodology; III-A Framework Overview; IV-B Model and Training Details` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 III Methodology; III-A Framework Overview; IV-B Model and Training Details。在 `PLATFORM-MONITORING` 中，该路径改变或检验的具体对象由题名《DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation》和上述 method locator 共同限定。`; `VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28725:end -->

<!-- existing:SF-2026-ARXIV-2606-28733:start -->
Ch79 已把 proposal、pre-commit verifier、environment feedback、abstention 与 executable commit 分权。 Fresh owner+adjacent reread found that《Agentic Abstention: Do Agents Know When to Stop Instead of Act?》的 `https://arxiv.org/html/2606.28733v1 — §5 Our Proposed Method for Improving Agentic Abstention: convolve; G.1 Task setting and training configuration; I.2.1 System Prompt for WebShop` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28733:end -->

<!-- delta:SF-2026-ARXIV-2606-28733:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 5 Our Proposed Method for Improving Agentic Abstention: convolve; G.1 Task setting and training configuration; I.2.1 System Prompt for WebShop。在 `AGENT-PLANNING` 中，该路径改变或检验的具体对象由题名《Agentic Abstention: Do Agents Know When to Stop Instead of Act?》和上述 method locator 共同限定。`; `7 Conclusion; Appendix A Limitations; Failure to abstain from GPT-5.4-mini；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28733:end -->

<!-- books-review:SF-2026-ARXIV-2606-28733:start -->
Principle Reuse; No Change — Existing Coverage. Ch79 已把 proposal、pre-commit verifier、environment feedback、abstention 与 executable commit 分权。 Fresh owner+adjacent reread found that《Agentic Abstention: Do Agents Know When to Stop Instead of Act?》的 `https://arxiv.org/html/2606.28733v1 — §5 Our Proposed Method for Improving Agentic Abstention: convolve; G.1 Task setting and training configuration; I.2.1 System Prompt for WebShop` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 5 Our Proposed Method for Improving Agentic Abstention: convolve; G.1 Task setting and training configuration; I.2.1 System Prompt for WebShop。在 `AGENT-PLANNING` 中，该路径改变或检验的具体对象由题名《Agentic Abstention: Do Agents Know When to Stop Instead of Act?》和上述 method locator 共同限定。`; `7 Conclusion; Appendix A Limitations; Failure to abstain from GPT-5.4-mini；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28733:end -->

<!-- existing:SF-2026-ARXIV-2606-28739:start -->
Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《Agent Safety Is Action Alignment》的 `https://arxiv.org/html/2606.28739v1 — §Report GitHub Issue; Agent Safety Is Action Alignment` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28739:end -->

<!-- delta:SF-2026-ARXIV-2606-28739:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Report GitHub Issue; Agent Safety Is Action Alignment。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Agent Safety Is Action Alignment》和上述 method locator 共同限定。`; `5.2. External Enforcement at the Action Boundary; 7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28739:end -->

<!-- books-review:SF-2026-ARXIV-2606-28739:start -->
Principle Reuse; No Change — Existing Coverage. Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《Agent Safety Is Action Alignment》的 `https://arxiv.org/html/2606.28739v1 — §Report GitHub Issue; Agent Safety Is Action Alignment` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Report GitHub Issue; Agent Safety Is Action Alignment。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Agent Safety Is Action Alignment》和上述 method locator 共同限定。`; `5.2. External Enforcement at the Action Boundary; 7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28739:end -->

<!-- existing:SF-2026-ARXIV-2606-28747:start -->
Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 Fresh owner+adjacent reread found that《Self-Supervised Theorem Discovery in a Formal Axiomatic System》的 `https://arxiv.org/html/2606.28747v1 — §Self-Supervised Theorem Discovery in a Formal Axiomatic System; Rules of the Hilbert System.` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28747:end -->

<!-- delta:SF-2026-ARXIV-2606-28747:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Self-Supervised Theorem Discovery in a Formal Axiomatic System; Rules of the Hilbert System.。在 `AGENT-WORKFLOW` 中，该路径改变或检验的具体对象由题名《Self-Supervised Theorem Discovery in a Formal Axiomatic System》和上述 method locator 共同限定。`; `7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28747:end -->

<!-- books-review:SF-2026-ARXIV-2606-28747:start -->
Principle Reuse; No Change — Existing Coverage. Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 Fresh owner+adjacent reread found that《Self-Supervised Theorem Discovery in a Formal Axiomatic System》的 `https://arxiv.org/html/2606.28747v1 — §Self-Supervised Theorem Discovery in a Formal Axiomatic System; Rules of the Hilbert System.` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Self-Supervised Theorem Discovery in a Formal Axiomatic System; Rules of the Hilbert System.。在 `AGENT-WORKFLOW` 中，该路径改变或检验的具体对象由题名《Self-Supervised Theorem Discovery in a Formal Axiomatic System》和上述 method locator 共同限定。`; `7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28747:end -->

<!-- existing:SF-2026-ARXIV-2606-28757:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models》的 `https://arxiv.org/html/2606.28757v1 — §Effect of Post-Training.; C Global Dynamic Reconstruction Methodology; G Post Training Details` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28757:end -->

<!-- delta:SF-2026-ARXIV-2606-28757:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Effect of Post-Training.; C Global Dynamic Reconstruction Methodology; G Post Training Details。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models》和上述 method locator 共同限定。`; `5 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28757:end -->

<!-- books-review:SF-2026-ARXIV-2606-28757:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models》的 `https://arxiv.org/html/2606.28757v1 — §Effect of Post-Training.; C Global Dynamic Reconstruction Methodology; G Post Training Details` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Effect of Post-Training.; C Global Dynamic Reconstruction Methodology; G Post Training Details。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models》和上述 method locator 共同限定。`; `5 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28757:end -->

<!-- existing:SF-2026-ARXIV-2606-28772:start -->
Ch27 保存 label lineage，却没有规定 contested safety boundary 必须保留原始 annotator distribution 而非只提交 majority label。
<!-- existing:SF-2026-ARXIV-2606-28772:end -->

<!-- delta:SF-2026-ARXIV-2606-28772:start -->
把 per-annotator label、threshold/disagreement 与聚合 rule 作为训练数据状态保存；majority label 只是一个 materialized view，不能删除 contested boundary。
<!-- delta:SF-2026-ARXIV-2606-28772:end -->

<!-- books-review:SF-2026-ARXIV-2606-28772:start -->
Direct Evolution; Integrate. Ch27 保存 label lineage，却没有规定 contested safety boundary 必须保留原始 annotator distribution 而非只提交 majority label。 把 per-annotator label、threshold/disagreement 与聚合 rule 作为训练数据状态保存；majority label 只是一个 materialized view，不能删除 contested boundary。
<!-- books-review:SF-2026-ARXIV-2606-28772:end -->

<!-- existing:SF-2026-ARXIV-2606-28781:start -->
Ch77 已拥有 typed write/read、provenance、conflict、transaction、visibility、rollback 与 graph dependency 生命周期。 Fresh owner+adjacent reread found that《HyphaeDB: A Living Knowledge Topology for Agent-First Memory》的 `https://arxiv.org/html/2606.28781v1 — §2.1 Agent Memory Systems; 3 Architecture; 4.1 Propagation Algorithm` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28781:end -->

<!-- delta:SF-2026-ARXIV-2606-28781:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 2.1 Agent Memory Systems; 3 Architecture; 4.1 Propagation Algorithm。在 `AGENT-MEMORY` 中，该路径改变或检验的具体对象由题名《HyphaeDB: A Living Knowledge Topology for Agent-First Memory》和上述 method locator 共同限定。`; `9 Discussion; 9.2 Limitations and Future Work; 10 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28781:end -->

<!-- books-review:SF-2026-ARXIV-2606-28781:start -->
Principle Reuse; No Change — Existing Coverage. Ch77 已拥有 typed write/read、provenance、conflict、transaction、visibility、rollback 与 graph dependency 生命周期。 Fresh owner+adjacent reread found that《HyphaeDB: A Living Knowledge Topology for Agent-First Memory》的 `https://arxiv.org/html/2606.28781v1 — §2.1 Agent Memory Systems; 3 Architecture; 4.1 Propagation Algorithm` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 2.1 Agent Memory Systems; 3 Architecture; 4.1 Propagation Algorithm。在 `AGENT-MEMORY` 中，该路径改变或检验的具体对象由题名《HyphaeDB: A Living Knowledge Topology for Agent-First Memory》和上述 method locator 共同限定。`; `9 Discussion; 9.2 Limitations and Future Work; 10 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28781:end -->

<!-- existing:SF-2026-ARXIV-2606-28813:start -->
Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 Fresh owner+adjacent reread found that《Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning》的 `https://arxiv.org/html/2606.28813v1 — §Training data.; Appendix E Constraint-Aware Steering Algorithm; Appendix F Model and Training Details` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28813:end -->

<!-- delta:SF-2026-ARXIV-2606-28813:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Training data.; Appendix E Constraint-Aware Steering Algorithm; Appendix F Model and Training Details。在 `MULTIMODAL-EMBODIED-VLA` 中，该路径改变或检验的具体对象由题名《Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning》和上述 method locator 共同限定。`; `6 Limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28813:end -->

<!-- books-review:SF-2026-ARXIV-2606-28813:start -->
Principle Reuse; No Change — Existing Coverage. Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 Fresh owner+adjacent reread found that《Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning》的 `https://arxiv.org/html/2606.28813v1 — §Training data.; Appendix E Constraint-Aware Steering Algorithm; Appendix F Model and Training Details` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Training data.; Appendix E Constraint-Aware Steering Algorithm; Appendix F Model and Training Details。在 `MULTIMODAL-EMBODIED-VLA` 中，该路径改变或检验的具体对象由题名《Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning》和上述 method locator 共同限定。`; `6 Limitations; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28813:end -->

<!-- existing:SF-2026-ARXIV-2606-28831:start -->
Ch45 已拥有 head/layer/page-aware eviction、quality-memory calibration、residual path、refresh、FullKV fallback 与 production SLO 边界。 Fresh owner+adjacent reread found that《HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression》的 `https://arxiv.org/html/2606.28831v1 — §System-Algorithm Co-Design in LLM Inference; 3 The Hard-KV Design; 3.1 The Framework Overview` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28831:end -->

<!-- delta:SF-2026-ARXIV-2606-28831:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 System-Algorithm Co-Design in LLM Inference; 3 The Hard-KV Design; 3.1 The Framework Overview。在 `INFER-KV-CACHE` 中，该路径改变或检验的具体对象由题名《HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression》和上述 method locator 共同限定。`; `5 Conclusion and Future Work; Appendix B Further Discussions on KV Index Regularization; B.2 Discussion on trade-off in the Index Management for Layerwise Selection；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28831:end -->

<!-- books-review:SF-2026-ARXIV-2606-28831:start -->
Principle Reuse; No Change — Existing Coverage. Ch45 已拥有 head/layer/page-aware eviction、quality-memory calibration、residual path、refresh、FullKV fallback 与 production SLO 边界。 Fresh owner+adjacent reread found that《HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression》的 `https://arxiv.org/html/2606.28831v1 — §System-Algorithm Co-Design in LLM Inference; 3 The Hard-KV Design; 3.1 The Framework Overview` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 System-Algorithm Co-Design in LLM Inference; 3 The Hard-KV Design; 3.1 The Framework Overview。在 `INFER-KV-CACHE` 中，该路径改变或检验的具体对象由题名《HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression》和上述 method locator 共同限定。`; `5 Conclusion and Future Work; Appendix B Further Discussions on KV Index Regularization; B.2 Discussion on trade-off in the Index Management for Layerwise Selection；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28831:end -->

<!-- existing:SF-2026-ARXIV-2606-28839:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables》的 `https://arxiv.org/html/2606.28839v1 — §The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems —and Auditing the Claims It Enables; Multi-agent LLM systems.; Network contagion and spectral methods.` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28839:end -->

<!-- delta:SF-2026-ARXIV-2606-28839:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems —and Auditing the Claims It Enables; Multi-agent LLM systems.; Network contagion and spectral methods.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables》和上述 method locator 共同限定。`; `4.1.4 Experiment 3: Real-API with Functional BOUNDARY_SYNC; 6 Discussion; 7 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28839:end -->

<!-- books-review:SF-2026-ARXIV-2606-28839:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables》的 `https://arxiv.org/html/2606.28839v1 — §The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems —and Auditing the Claims It Enables; Multi-agent LLM systems.; Network contagion and spectral methods.` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems —and Auditing the Claims It Enables; Multi-agent LLM systems.; Network contagion and spectral methods.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables》和上述 method locator 共同限定。`; `4.1.4 Experiment 3: Real-API with Functional BOUNDARY_SYNC; 6 Discussion; 7 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28839:end -->

<!-- existing:SF-2026-ARXIV-2606-28841:start -->
Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 Fresh owner+adjacent reread found that《LAMP: Lean-based Agentic framework with MCP and Proof Repair》的 `https://arxiv.org/html/2606.28841v1 — §LAMP: Lean-based Agentic framework with MCP and Proof Repair; 2.3 Agentic Frameworks for Theorem Proving; 3 The LAMP System` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28841:end -->

<!-- delta:SF-2026-ARXIV-2606-28841:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 LAMP: Lean-based Agentic framework with MCP and Proof Repair; 2.3 Agentic Frameworks for Theorem Proving; 3 The LAMP System。在 `AGENT-WORKFLOW` 中，该路径改变或检验的具体对象由题名《LAMP: Lean-based Agentic framework with MCP and Proof Repair》和上述 method locator 共同限定。`; `5 Discussion and Limitations; Failure Analysis:; Limitations and Future Work:；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28841:end -->

<!-- books-review:SF-2026-ARXIV-2606-28841:start -->
Principle Reuse; No Change — Existing Coverage. Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 Fresh owner+adjacent reread found that《LAMP: Lean-based Agentic framework with MCP and Proof Repair》的 `https://arxiv.org/html/2606.28841v1 — §LAMP: Lean-based Agentic framework with MCP and Proof Repair; 2.3 Agentic Frameworks for Theorem Proving; 3 The LAMP System` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 LAMP: Lean-based Agentic framework with MCP and Proof Repair; 2.3 Agentic Frameworks for Theorem Proving; 3 The LAMP System。在 `AGENT-WORKFLOW` 中，该路径改变或检验的具体对象由题名《LAMP: Lean-based Agentic framework with MCP and Proof Repair》和上述 method locator 共同限定。`; `5 Discussion and Limitations; Failure Analysis:; Limitations and Future Work:；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28841:end -->

<!-- existing:SF-2026-ARXIV-2606-28843:start -->
Ch29 已把 demonstration distribution、language/model slice、安全回归、forgetting 与 serving interface 分开验收。 Fresh owner+adjacent reread found that《The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning》的 `https://arxiv.org/html/2606.28843v1 — §5.3 Pre-training distributions and scale` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28843:end -->

<!-- delta:SF-2026-ARXIV-2606-28843:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 5.3 Pre-training distributions and scale。在 `TRAIN-SFT` 中，该路径改变或检验的具体对象由题名《The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning》和上述 method locator 共同限定。`; `7 Discussion; 7.2 Limitations; 8 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28843:end -->

<!-- books-review:SF-2026-ARXIV-2606-28843:start -->
Principle Reuse; No Change — Existing Coverage. Ch29 已把 demonstration distribution、language/model slice、安全回归、forgetting 与 serving interface 分开验收。 Fresh owner+adjacent reread found that《The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning》的 `https://arxiv.org/html/2606.28843v1 — §5.3 Pre-training distributions and scale` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 5.3 Pre-training distributions and scale。在 `TRAIN-SFT` 中，该路径改变或检验的具体对象由题名《The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning》和上述 method locator 共同限定。`; `7 Discussion; 7.2 Limitations; 8 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28843:end -->

<!-- existing:SF-2026-ARXIV-2606-28862:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《HKVLM: Faithful Query--Region Binding for Frozen-Detector Visual Grounding》的 `https://arxiv.org/html/2606.28862v1 — §4 Method: HKVLM; 4.5 Cold-start training; 5 Experimental Design and Evaluation Protocol` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28862:end -->

<!-- delta:SF-2026-ARXIV-2606-28862:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 4 Method: HKVLM; 4.5 Cold-start training; 5 Experimental Design and Evaluation Protocol。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《HKVLM: Faithful Query--Region Binding for Frozen-Detector Visual Grounding》和上述 method locator 共同限定。`; `8 Discussion, Limitations, and Broader Impact; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28862:end -->

<!-- books-review:SF-2026-ARXIV-2606-28862:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《HKVLM: Faithful Query--Region Binding for Frozen-Detector Visual Grounding》的 `https://arxiv.org/html/2606.28862v1 — §4 Method: HKVLM; 4.5 Cold-start training; 5 Experimental Design and Evaluation Protocol` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 4 Method: HKVLM; 4.5 Cold-start training; 5 Experimental Design and Evaluation Protocol。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《HKVLM: Faithful Query--Region Binding for Frozen-Detector Visual Grounding》和上述 method locator 共同限定。`; `8 Discussion, Limitations, and Broader Impact; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28862:end -->

<!-- existing:SF-2026-ARXIV-2606-28863:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《Defeat Devices in AI Systems》的 `https://arxiv.org/html/2606.28863v1 — §Defeat Devices in AI Systems; 4.1 Five method families; 5.1 Defeat devices can naturally emerge in AI systems` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28863:end -->

<!-- delta:SF-2026-ARXIV-2606-28863:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Defeat Devices in AI Systems; 4.1 Five method families; 5.1 Defeat devices can naturally emerge in AI systems。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Defeat Devices in AI Systems》和上述 method locator 共同限定。`; `2.4 Boundary cases; 6.5 Limitations; 7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28863:end -->

<!-- books-review:SF-2026-ARXIV-2606-28863:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《Defeat Devices in AI Systems》的 `https://arxiv.org/html/2606.28863v1 — §Defeat Devices in AI Systems; 4.1 Five method families; 5.1 Defeat devices can naturally emerge in AI systems` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Defeat Devices in AI Systems; 4.1 Five method families; 5.1 Defeat devices can naturally emerge in AI systems。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Defeat Devices in AI Systems》和上述 method locator 共同限定。`; `2.4 Boundary cases; 6.5 Limitations; 7 Conclusions；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28863:end -->

<!-- existing:SF-2026-ARXIV-2606-28867:start -->
Ch27 已拥有 sample/transform/label provenance、license、lineage、mixture 与 admission，但尚未要求保留 per-annotator distribution 以阻止 majority label 静默取得价值边界真值。 Fresh owner+adjacent reread found that《Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages》的 `https://arxiv.org/html/2606.28867v1 — §Legal analysis of AI training data.` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28867:end -->

<!-- delta:SF-2026-ARXIV-2606-28867:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Legal analysis of AI training data.。在 `TRAIN-DATA` 中，该路径改变或检验的具体对象由题名《Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages》和上述 method locator 共同限定。`; `6. Four Failure Modes; 6.4. Data Persistence Failure: The Congolese Radio Corpus; 9. Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28867:end -->

<!-- books-review:SF-2026-ARXIV-2606-28867:start -->
Principle Reuse; No Change — Existing Coverage. Ch27 已拥有 sample/transform/label provenance、license、lineage、mixture 与 admission，但尚未要求保留 per-annotator distribution 以阻止 majority label 静默取得价值边界真值。 Fresh owner+adjacent reread found that《Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages》的 `https://arxiv.org/html/2606.28867v1 — §Legal analysis of AI training data.` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Legal analysis of AI training data.。在 `TRAIN-DATA` 中，该路径改变或检验的具体对象由题名《Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages》和上述 method locator 共同限定。`; `6. Four Failure Modes; 6.4. Data Persistence Failure: The Congolese Radio Corpus; 9. Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28867:end -->

<!-- existing:SF-2026-ARXIV-2606-28876:start -->
Ch22 已显式区分 checkpoint `M_0` 与 request-owned mutable `M_t`，并覆盖 sparse slots、write conflict、reset/session identity、external-memory boundary 与 frozen-path fallback。 Fresh owner+adjacent reread found that《Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory》的 `https://arxiv.org/html/2606.28876v1 — §2 Method Sketch` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28876:end -->

<!-- delta:SF-2026-ARXIV-2606-28876:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 2 Method Sketch。在 `MODEL-LONG-CONTEXT` 中，该路径改变或检验的具体对象由题名《Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory》和上述 method locator 共同限定。`; `5 Discussion; 8 Limitations and Next Steps; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28876:end -->

<!-- books-review:SF-2026-ARXIV-2606-28876:start -->
Principle Reuse; No Change — Existing Coverage. Ch22 已显式区分 checkpoint `M_0` 与 request-owned mutable `M_t`，并覆盖 sparse slots、write conflict、reset/session identity、external-memory boundary 与 frozen-path fallback。 Fresh owner+adjacent reread found that《Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory》的 `https://arxiv.org/html/2606.28876v1 — §2 Method Sketch` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 2 Method Sketch。在 `MODEL-LONG-CONTEXT` 中，该路径改变或检验的具体对象由题名《Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory》和上述 method locator 共同限定。`; `5 Discussion; 8 Limitations and Next Steps; 9 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28876:end -->

<!-- existing:SF-2026-ARXIV-2606-28900:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes》的 `https://arxiv.org/html/2606.28900v1 — §Design goals.; Training-oriented derivatives.` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28900:end -->

<!-- delta:SF-2026-ARXIV-2606-28900:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Design goals.; Training-oriented derivatives.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes》和上述 method locator 共同限定。`; `6 Discussion, Limitations, and Ethics; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28900:end -->

<!-- books-review:SF-2026-ARXIV-2606-28900:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes》的 `https://arxiv.org/html/2606.28900v1 — §Design goals.; Training-oriented derivatives.` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Design goals.; Training-oriented derivatives.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes》和上述 method locator 共同限定。`; `6 Discussion, Limitations, and Ethics; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28900:end -->

<!-- existing:SF-2026-ARXIV-2606-28925:start -->
Ch82 已版本化 sender/receiver/channel/topology identity、message admission、latent translation 与 commitment，但未把 set routing、receiver-owned hierarchical read 和 full-KV integrity receipt 合成同一 channel contract。 Fresh owner+adjacent reread found that《Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation》的 `https://arxiv.org/html/2606.28925v1 — §2.1. Tool/Agent Routing in LLM Systems; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 2.6. Multi-Agent Systems and Task Decomposition` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28925:end -->

<!-- delta:SF-2026-ARXIV-2606-28925:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 2.1. Tool/Agent Routing in LLM Systems; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 2.6. Multi-Agent Systems and Task Decomposition。在 `AGENT-MULTI-AGENT` 中，该路径改变或检验的具体对象由题名《Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation》和上述 method locator 共同限定。`; `7. Discussion; 8. Limitations; 10. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28925:end -->

<!-- books-review:SF-2026-ARXIV-2606-28925:start -->
Principle Reuse; No Change — Existing Coverage. Ch82 已版本化 sender/receiver/channel/topology identity、message admission、latent translation 与 commitment，但未把 set routing、receiver-owned hierarchical read 和 full-KV integrity receipt 合成同一 channel contract。 Fresh owner+adjacent reread found that《Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation》的 `https://arxiv.org/html/2606.28925v1 — §2.1. Tool/Agent Routing in LLM Systems; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 2.6. Multi-Agent Systems and Task Decomposition` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 2.1. Tool/Agent Routing in LLM Systems; 2.4. Learning-to-Rank, Retrieval, and Evaluation Methodology; 2.6. Multi-Agent Systems and Task Decomposition。在 `AGENT-MULTI-AGENT` 中，该路径改变或检验的具体对象由题名《Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation》和上述 method locator 共同限定。`; `7. Discussion; 8. Limitations; 10. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28925:end -->

<!-- existing:SF-2026-ARXIV-2606-28939:start -->
Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 Fresh owner+adjacent reread found that《ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies》的 `https://arxiv.org/html/2606.28939v1 — §4 Our Approach: ReGuide; Appendix B Algorithm` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28939:end -->

<!-- delta:SF-2026-ARXIV-2606-28939:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 4 Our Approach: ReGuide; Appendix B Algorithm。在 `MULTIMODAL-EMBODIED-VLA` 中，该路径改变或检验的具体对象由题名《ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies》和上述 method locator 共同限定。`; `6 Conclusion and Limitations; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28939:end -->

<!-- books-review:SF-2026-ARXIV-2606-28939:start -->
Principle Reuse; No Change — Existing Coverage. Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 Fresh owner+adjacent reread found that《ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies》的 `https://arxiv.org/html/2606.28939v1 — §4 Our Approach: ReGuide; Appendix B Algorithm` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 4 Our Approach: ReGuide; Appendix B Algorithm。在 `MULTIMODAL-EMBODIED-VLA` 中，该路径改变或检验的具体对象由题名《ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies》和上述 method locator 共同限定。`; `6 Conclusion and Limitations; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28939:end -->

<!-- existing:SF-2026-ARXIV-2606-28953:start -->
Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System》的 `https://arxiv.org/html/2606.28953v1 — §Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 4.5 Proposed defense vs prior methods; 5.1 Proposed defense vs prior methods` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28953:end -->

<!-- delta:SF-2026-ARXIV-2606-28953:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 4.5 Proposed defense vs prior methods; 5.1 Proposed defense vs prior methods。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System》和上述 method locator 共同限定。`; `Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 2 Threat Model; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28953:end -->

<!-- books-review:SF-2026-ARXIV-2606-28953:start -->
Principle Reuse; No Change — Existing Coverage. Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System》的 `https://arxiv.org/html/2606.28953v1 — §Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 4.5 Proposed defense vs prior methods; 5.1 Proposed defense vs prior methods` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 4.5 Proposed defense vs prior methods; 5.1 Proposed defense vs prior methods。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System》和上述 method locator 共同限定。`; `Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System Thanks: Based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. HR001120C0114. Opinions, findings and conclusions or recommendations in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).; 2 Threat Model; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28953:end -->

<!-- existing:SF-2026-ARXIV-2606-28955:start -->
Ch31 讨论 reward hacking，却没有在 transition 写入 replay 前比较 cloned current/modified policy 的 equal-budget counterfactual。
<!-- existing:SF-2026-ARXIV-2606-28955:end -->

<!-- delta:SF-2026-ARXIV-2606-28955:start -->
在 transition admission 前冻结 current policy/return estimator，以 equal budget 预测 modified-policy counterfactual；只有 evaluator 接受才写入 replay。
<!-- delta:SF-2026-ARXIV-2606-28955:end -->

<!-- books-review:SF-2026-ARXIV-2606-28955:start -->
Direct Evolution; Integrate. Ch31 讨论 reward hacking，却没有在 transition 写入 replay 前比较 cloned current/modified policy 的 equal-budget counterfactual。 在 transition admission 前冻结 current policy/return estimator，以 equal budget 预测 modified-policy counterfactual；只有 evaluator 接受才写入 replay。
<!-- books-review:SF-2026-ARXIV-2606-28955:end -->

<!-- existing:SF-2026-ARXIV-2606-28958:start -->
Ch82 已版本化 sender/receiver/channel/topology identity、message admission、latent translation 与 commitment，但未把 set routing、receiver-owned hierarchical read 和 full-KV integrity receipt 合成同一 channel contract。 Fresh owner+adjacent reread found that《When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration》的 `https://arxiv.org/html/2606.28958v1 — §Report GitHub Issue; When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28958:end -->

<!-- delta:SF-2026-ARXIV-2606-28958:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Report GitHub Issue; When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration。在 `AGENT-MULTI-AGENT` 中，该路径改变或检验的具体对象由题名《When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration》和上述 method locator 共同限定。`; `3 Problem Setting and Threat Model; 8.4 Transport Integrity and Fail-Closed Boundary; 9 Failure Modes and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28958:end -->

<!-- books-review:SF-2026-ARXIV-2606-28958:start -->
Principle Reuse; No Change — Existing Coverage. Ch82 已版本化 sender/receiver/channel/topology identity、message admission、latent translation 与 commitment，但未把 set routing、receiver-owned hierarchical read 和 full-KV integrity receipt 合成同一 channel contract。 Fresh owner+adjacent reread found that《When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration》的 `https://arxiv.org/html/2606.28958v1 — §Report GitHub Issue; When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Report GitHub Issue; When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration。在 `AGENT-MULTI-AGENT` 中，该路径改变或检验的具体对象由题名《When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration》和上述 method locator 共同限定。`; `3 Problem Setting and Threat Model; 8.4 Transport Integrity and Fail-Closed Boundary; 9 Failure Modes and Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28958:end -->

<!-- existing:SF-2026-ARXIV-2606-28962:start -->
Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks》的 `https://arxiv.org/html/2606.28962v1 — §III Methodology; III-B Defense Framework Design; III-C Defense Metric Design` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28962:end -->

<!-- delta:SF-2026-ARXIV-2606-28962:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 III Methodology; III-B Defense Framework Design; III-C Defense Metric Design。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks》和上述 method locator 共同限定。`; `III-A Threat Model; V Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28962:end -->

<!-- books-review:SF-2026-ARXIV-2606-28962:start -->
Principle Reuse; No Change — Existing Coverage. Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks》的 `https://arxiv.org/html/2606.28962v1 — §III Methodology; III-B Defense Framework Design; III-C Defense Metric Design` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 III Methodology; III-B Defense Framework Design; III-C Defense Metric Design。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks》和上述 method locator 共同限定。`; `III-A Threat Model; V Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28962:end -->

<!-- existing:SF-2026-ARXIV-2606-28995:start -->
Ch26 有独立 safety filter 与 controller-owned physical commit，却没有把离线 HJ/barrier approximation 编译为在线闭式 DMP modulation，也没有把 learned value 的 calibration 前提与 certificate 退化写入 fallback 边界。
<!-- existing:SF-2026-ARXIV-2606-28995:end -->

<!-- delta:SF-2026-ARXIV-2606-28995:start -->
把离线 HJ/CBVF learned value 与 conformal calibration 编译为在线 closed-form DMP safety modulation；controller 仍拥有 physical commit。
<!-- delta:SF-2026-ARXIV-2606-28995:end -->

<!-- books-review:SF-2026-ARXIV-2606-28995:start -->
Direct Evolution; Integrate. Ch26 有独立 safety filter 与 controller-owned physical commit，却没有把离线 HJ/barrier approximation 编译为在线闭式 DMP modulation，也没有把 learned value 的 calibration 前提与 certificate 退化写入 fallback 边界。 把离线 HJ/CBVF learned value 与 conformal calibration 编译为在线 closed-form DMP safety modulation；controller 仍拥有 physical commit。
<!-- books-review:SF-2026-ARXIV-2606-28995:end -->

<!-- existing:SF-2026-ARXIV-2606-28998:start -->
Ch34 已绑定 base/reference/policy identity、preference construction、functional/non-functional trade-off 与 regression evaluation。 Fresh owner+adjacent reread found that《Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation》的 `https://arxiv.org/html/2606.28998v1 — §3. Methodology` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-28998:end -->

<!-- delta:SF-2026-ARXIV-2606-28998:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 3. Methodology。在 `TRAIN-DPO` 中，该路径改变或检验的具体对象由题名《Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation》和上述 method locator 共同限定。`; `3.6. Threats to Validity; Small Model Limitations; Failure Cases；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-28998:end -->

<!-- books-review:SF-2026-ARXIV-2606-28998:start -->
Principle Reuse; No Change — Existing Coverage. Ch34 已绑定 base/reference/policy identity、preference construction、functional/non-functional trade-off 与 regression evaluation。 Fresh owner+adjacent reread found that《Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation》的 `https://arxiv.org/html/2606.28998v1 — §3. Methodology` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 3. Methodology。在 `TRAIN-DPO` 中，该路径改变或检验的具体对象由题名《Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation》和上述 method locator 共同限定。`; `3.6. Threats to Validity; Small Model Limitations; Failure Cases；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-28998:end -->

<!-- existing:SF-2026-ARXIV-2606-29030:start -->
Ch77 已拥有 typed write/read、provenance、conflict、transaction、visibility、rollback 与 graph dependency 生命周期。 Fresh owner+adjacent reread found that《Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering》的 `https://arxiv.org/html/2606.29030v1 — §III Architecture of the Proposed Agent` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29030:end -->

<!-- delta:SF-2026-ARXIV-2606-29030:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 III Architecture of the Proposed Agent。在 `AGENT-MEMORY` 中，该路径改变或检验的具体对象由题名《Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering》和上述 method locator 共同限定。`; `VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29030:end -->

<!-- books-review:SF-2026-ARXIV-2606-29030:start -->
Principle Reuse; No Change — Existing Coverage. Ch77 已拥有 typed write/read、provenance、conflict、transaction、visibility、rollback 与 graph dependency 生命周期。 Fresh owner+adjacent reread found that《Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering》的 `https://arxiv.org/html/2606.29030v1 — §III Architecture of the Proposed Agent` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 III Architecture of the Proposed Agent。在 `AGENT-MEMORY` 中，该路径改变或检验的具体对象由题名《Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering》和上述 method locator 共同限定。`; `VI Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29030:end -->

<!-- existing:SF-2026-ARXIV-2606-29033:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations》的 `https://arxiv.org/html/2606.29033v1 — §Approach 1: Human Verification of AI Proposals.; Approach 2: Manual Test Sets.; Approach 3: Humans Specify Criteria, AI Applies Them at Scale.` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29033:end -->

<!-- delta:SF-2026-ARXIV-2606-29033:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Approach 1: Human Verification of AI Proposals.; Approach 2: Manual Test Sets.; Approach 3: Humans Specify Criteria, AI Applies Them at Scale.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations》和上述 method locator 共同限定。`; `6. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29033:end -->

<!-- books-review:SF-2026-ARXIV-2606-29033:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations》的 `https://arxiv.org/html/2606.29033v1 — §Approach 1: Human Verification of AI Proposals.; Approach 2: Manual Test Sets.; Approach 3: Humans Specify Criteria, AI Applies Them at Scale.` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Approach 1: Human Verification of AI Proposals.; Approach 2: Manual Test Sets.; Approach 3: Humans Specify Criteria, AI Applies Them at Scale.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations》和上述 method locator 共同限定。`; `6. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29033:end -->

<!-- existing:SF-2026-ARXIV-2606-29038:start -->
Ch66 已版本化 metric identity、raw evidence 与 release selector，却没有禁止 optimizer、evaluator、champion selector 各自重写 aggregation semantics，也没有要求三者调用同一个可执行 metric artifact。
<!-- existing:SF-2026-ARXIV-2606-29038:end -->

<!-- delta:SF-2026-ARXIV-2606-29038:start -->
将 metric extraction/aggregation 实现提升为一个版本化 callable contract，由 optimizer、evaluator 与 champion selector 调用同一 artifact，并保留 raw trajectory 重算路径。
<!-- delta:SF-2026-ARXIV-2606-29038:end -->

<!-- books-review:SF-2026-ARXIV-2606-29038:start -->
Direct Evolution; Integrate. Ch66 已版本化 metric identity、raw evidence 与 release selector，却没有禁止 optimizer、evaluator、champion selector 各自重写 aggregation semantics，也没有要求三者调用同一个可执行 metric artifact。 将 metric extraction/aggregation 实现提升为一个版本化 callable contract，由 optimizer、evaluator 与 champion selector 调用同一 artifact，并保留 raw trajectory 重算路径。
<!-- books-review:SF-2026-ARXIV-2606-29038:end -->

<!-- existing:SF-2026-ARXIV-2606-29054:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation》的 `https://arxiv.org/html/2606.29054v1 — §2 Method; Ministral violations expose framework limits.; Practical decision framework.` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29054:end -->

<!-- delta:SF-2026-ARXIV-2606-29054:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 2 Method; Ministral violations expose framework limits.; Practical decision framework.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation》和上述 method locator 共同限定。`; `4 Discussion; 6 Conclusion; Threats to validity and limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29054:end -->

<!-- books-review:SF-2026-ARXIV-2606-29054:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation》的 `https://arxiv.org/html/2606.29054v1 — §2 Method; Ministral violations expose framework limits.; Practical decision framework.` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 2 Method; Ministral violations expose framework limits.; Practical decision framework.。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation》和上述 method locator 共同限定。`; `4 Discussion; 6 Conclusion; Threats to validity and limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29054:end -->

<!-- existing:SF-2026-ARXIV-2606-29066:start -->
Ch44 区分 refinement/advancement，却没有 request-local continuous mixture、异步 per-token progress、re-edit 与 commit state。
<!-- existing:SF-2026-ARXIV-2606-29066:end -->

<!-- delta:SF-2026-ARXIV-2606-29066:start -->
masked-diffusion decoder 为每个 token 保存可连续携带的 x-prediction mixture 与 progress，允许 bounded re-edit，只有 commit state 才进入可见 frontier。
<!-- delta:SF-2026-ARXIV-2606-29066:end -->

<!-- books-review:SF-2026-ARXIV-2606-29066:start -->
Direct Evolution; Integrate. Ch44 区分 refinement/advancement，却没有 request-local continuous mixture、异步 per-token progress、re-edit 与 commit state。 masked-diffusion decoder 为每个 token 保存可连续携带的 x-prediction mixture 与 progress，允许 bounded re-edit，只有 commit state 才进入可见 frontier。
<!-- books-review:SF-2026-ARXIV-2606-29066:end -->

<!-- existing:SF-2026-ARXIV-2606-29067:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs》的 `https://arxiv.org/html/2606.29067v1 — §3 Method; H.1 Study Design` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29067:end -->

<!-- delta:SF-2026-ARXIV-2606-29067:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 3 Method; H.1 Study Design。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs》和上述 method locator 共同限定。`; `Layer 1: Structural segmentation and boundary classification.; Layer 2: Soft boundary detection.; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29067:end -->

<!-- books-review:SF-2026-ARXIV-2606-29067:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs》的 `https://arxiv.org/html/2606.29067v1 — §3 Method; H.1 Study Design` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 3 Method; H.1 Study Design。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs》和上述 method locator 共同限定。`; `Layer 1: Structural segmentation and boundary classification.; Layer 2: Soft boundary detection.; 5 Results and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29067:end -->

<!-- existing:SF-2026-ARXIV-2606-29073:start -->
Ch83 已把 discovery/capability 与业务授权、effect-time policy、group admission 分开，但尚未把多协议组合和一次 execution 的 grant/handle/policy/audit 对象统一进可检查状态机。 Fresh owner+adjacent reread found that《From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes》的 `https://arxiv.org/html/2606.29073v1 — §5 HCP Design; 6 Benchmark Method; 7.7 Ecosystem Measurement` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29073:end -->

<!-- delta:SF-2026-ARXIV-2606-29073:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 5 HCP Design; 6 Benchmark Method; 7.7 Ecosystem Measurement。在 `AGENT-MCP` 中，该路径改变或检验的具体对象由题名《From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes》和上述 method locator 共同限定。`; `3 Threat Model; 6.3 Reproducibility Boundary; 8 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29073:end -->

<!-- books-review:SF-2026-ARXIV-2606-29073:start -->
Principle Reuse; No Change — Existing Coverage. Ch83 已把 discovery/capability 与业务授权、effect-time policy、group admission 分开，但尚未把多协议组合和一次 execution 的 grant/handle/policy/audit 对象统一进可检查状态机。 Fresh owner+adjacent reread found that《From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes》的 `https://arxiv.org/html/2606.29073v1 — §5 HCP Design; 6 Benchmark Method; 7.7 Ecosystem Measurement` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 5 HCP Design; 6 Benchmark Method; 7.7 Ecosystem Measurement。在 `AGENT-MCP` 中，该路径改变或检验的具体对象由题名《From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes》和上述 method locator 共同限定。`; `3 Threat Model; 6.3 Reproducibility Boundary; 8 Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29073:end -->

<!-- existing:SF-2026-ARXIV-2606-29082:start -->
Ch28 已拥有 optimizer/schedule/precision/budget、mid-training skill artifact、search experience 与 downstream promotion receipt。 Fresh owner+adjacent reread found that《Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks》的 `https://arxiv.org/html/2606.29082v1 — §EFT serves as mid-training for test-time RL.; Appendix C Additional Details of Dataset Construction Method; C.1 Systematic Error Breakdown Analysis` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29082:end -->

<!-- delta:SF-2026-ARXIV-2606-29082:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 EFT serves as mid-training for test-time RL.; Appendix C Additional Details of Dataset Construction Method; C.1 Systematic Error Breakdown Analysis。在 `TRAIN-PRETRAINING` 中，该路径改变或检验的具体对象由题名《Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks》和上述 method locator 共同限定。`; `7 Conclusion; Limitations; Appendix B Further Details and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29082:end -->

<!-- books-review:SF-2026-ARXIV-2606-29082:start -->
Principle Reuse; No Change — Existing Coverage. Ch28 已拥有 optimizer/schedule/precision/budget、mid-training skill artifact、search experience 与 downstream promotion receipt。 Fresh owner+adjacent reread found that《Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks》的 `https://arxiv.org/html/2606.29082v1 — §EFT serves as mid-training for test-time RL.; Appendix C Additional Details of Dataset Construction Method; C.1 Systematic Error Breakdown Analysis` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 EFT serves as mid-training for test-time RL.; Appendix C Additional Details of Dataset Construction Method; C.1 Systematic Error Breakdown Analysis。在 `TRAIN-PRETRAINING` 中，该路径改变或检验的具体对象由题名《Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks》和上述 method locator 共同限定。`; `7 Conclusion; Limitations; Appendix B Further Details and Discussion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29082:end -->

<!-- existing:SF-2026-ARXIV-2606-29088:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking》的 `https://arxiv.org/html/2606.29088v1 — §Report GitHub Issue; Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29088:end -->

<!-- delta:SF-2026-ARXIV-2606-29088:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Report GitHub Issue; Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking》和上述 method locator 共同限定。`; `5 Discussion; 6 Threats to Validity; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29088:end -->

<!-- books-review:SF-2026-ARXIV-2606-29088:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking》的 `https://arxiv.org/html/2606.29088v1 — §Report GitHub Issue; Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Report GitHub Issue; Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking》和上述 method locator 共同限定。`; `5 Discussion; 6 Threats to Validity; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29088:end -->

<!-- existing:SF-2026-ARXIV-2606-29089:start -->
Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 Fresh owner+adjacent reread found that《TAP-VLA: Tactile Annotation Prompting for Vision Language Action Models》的 `https://arxiv.org/html/2606.29089v1 — §3 Method` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29089:end -->

<!-- delta:SF-2026-ARXIV-2606-29089:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 3 Method。在 `MULTIMODAL-EMBODIED-VLA` 中，该路径改变或检验的具体对象由题名《TAP-VLA: Tactile Annotation Prompting for Vision Language Action Models》和上述 method locator 共同限定。`; `5 Discussion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29089:end -->

<!-- books-review:SF-2026-ARXIV-2606-29089:start -->
Principle Reuse; No Change — Existing Coverage. Ch26 已分离 observation、policy proposal、world-model/critic signal、safety filter、controller commit 与 real-world validation，但尚未给出离线 learned reachability value 到在线 closed-form modulation 的编译边界。 Fresh owner+adjacent reread found that《TAP-VLA: Tactile Annotation Prompting for Vision Language Action Models》的 `https://arxiv.org/html/2606.29089v1 — §3 Method` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 3 Method。在 `MULTIMODAL-EMBODIED-VLA` 中，该路径改变或检验的具体对象由题名《TAP-VLA: Tactile Annotation Prompting for Vision Language Action Models》和上述 method locator 共同限定。`; `5 Discussion; 6 Limitations；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29089:end -->

<!-- existing:SF-2026-ARXIV-2606-29090:start -->
Ch76 已拥有 multi-index retrieval、budgeted stopping、procedural corpus、evidence sufficiency、provenance 与 fallback。 Fresh owner+adjacent reread found that《AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering》的 `https://arxiv.org/html/2606.29090v1 — §III Methodology and Framework; III-A Overall Framework; III-B System Architecture` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29090:end -->

<!-- delta:SF-2026-ARXIV-2606-29090:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 III Methodology and Framework; III-A Overall Framework; III-B System Architecture。在 `AGENT-RAG` 中，该路径改变或检验的具体对象由题名《AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering》和上述 method locator 共同限定。`; `V-F Qualitative Examples and Discussion; VI Conclusion and Future Work; VI-A Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29090:end -->

<!-- books-review:SF-2026-ARXIV-2606-29090:start -->
Principle Reuse; No Change — Existing Coverage. Ch76 已拥有 multi-index retrieval、budgeted stopping、procedural corpus、evidence sufficiency、provenance 与 fallback。 Fresh owner+adjacent reread found that《AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering》的 `https://arxiv.org/html/2606.29090v1 — §III Methodology and Framework; III-A Overall Framework; III-B System Architecture` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 III Methodology and Framework; III-A Overall Framework; III-B System Architecture。在 `AGENT-RAG` 中，该路径改变或检验的具体对象由题名《AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering》和上述 method locator 共同限定。`; `V-F Qualitative Examples and Discussion; VI Conclusion and Future Work; VI-A Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29090:end -->

<!-- existing:SF-2026-ARXIV-2606-29091:start -->
Ch76 已拥有 multi-index retrieval、budgeted stopping、procedural corpus、evidence sufficiency、provenance 与 fallback。 Fresh owner+adjacent reread found that《Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models》的 `https://arxiv.org/html/2606.29091v1 — §Chance across architectures.` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29091:end -->

<!-- delta:SF-2026-ARXIV-2606-29091:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Chance across architectures.。在 `AGENT-RAG` 中，该路径改变或检验的具体对象由题名《Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models》和上述 method locator 共同限定。`; `6 Discussion & Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29091:end -->

<!-- books-review:SF-2026-ARXIV-2606-29091:start -->
Principle Reuse; No Change — Existing Coverage. Ch76 已拥有 multi-index retrieval、budgeted stopping、procedural corpus、evidence sufficiency、provenance 与 fallback。 Fresh owner+adjacent reread found that《Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models》的 `https://arxiv.org/html/2606.29091v1 — §Chance across architectures.` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Chance across architectures.。在 `AGENT-RAG` 中，该路径改变或检验的具体对象由题名《Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models》和上述 method locator 共同限定。`; `6 Discussion & Conclusion; Limitations.；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29091:end -->

<!-- existing:SF-2026-ARXIV-2606-29094:start -->
Ch56 已把 admission、iteration scheduling、routing/placement、autoscaling、TP/KV state、预测误差与 SLO 放入多时间尺度控制面。 Fresh owner+adjacent reread found that《DiLaServe: High SLO Attainment Serving for Diffusion Language Models》的 `https://arxiv.org/html/2606.29094v1 — §3.1. Design Overview; Appendix C Algorithm for Supporting Approximate KV Caching` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29094:end -->

<!-- delta:SF-2026-ARXIV-2606-29094:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 3.1. Design Overview; Appendix C Algorithm for Supporting Approximate KV Caching。在 `INFER-SCHEDULING` 中，该路径改变或检验的具体对象由题名《DiLaServe: High SLO Attainment Serving for Diffusion Language Models》和上述 method locator 共同限定。`; `7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29094:end -->

<!-- books-review:SF-2026-ARXIV-2606-29094:start -->
Principle Reuse; No Change — Existing Coverage. Ch56 已把 admission、iteration scheduling、routing/placement、autoscaling、TP/KV state、预测误差与 SLO 放入多时间尺度控制面。 Fresh owner+adjacent reread found that《DiLaServe: High SLO Attainment Serving for Diffusion Language Models》的 `https://arxiv.org/html/2606.29094v1 — §3.1. Design Overview; Appendix C Algorithm for Supporting Approximate KV Caching` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 3.1. Design Overview; Appendix C Algorithm for Supporting Approximate KV Caching。在 `INFER-SCHEDULING` 中，该路径改变或检验的具体对象由题名《DiLaServe: High SLO Attainment Serving for Diffusion Language Models》和上述 method locator 共同限定。`; `7. Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29094:end -->

<!-- existing:SF-2026-ARXIV-2606-29097:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation》的 `https://arxiv.org/html/2606.29097v1 — §3 Method` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29097:end -->

<!-- delta:SF-2026-ARXIV-2606-29097:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 3 Method。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation》和上述 method locator 共同限定。`; `5 Limitations and Future Work; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29097:end -->

<!-- books-review:SF-2026-ARXIV-2606-29097:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation》的 `https://arxiv.org/html/2606.29097v1 — §3 Method` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 3 Method。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation》和上述 method locator 共同限定。`; `5 Limitations and Future Work; 6 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29097:end -->

<!-- existing:SF-2026-ARXIV-2606-29108:start -->
Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 Fresh owner+adjacent reread found that《Symbolon: Symbolic Execution by Learning Code Transformation》的 `arXiv:2606.29108v1 version-stamped mirror — §Our approach; III Methodology` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29108:end -->

<!-- delta:SF-2026-ARXIV-2606-29108:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Our approach; III Methodology。在 `AGENT-WORKFLOW` 中，该路径改变或检验的具体对象由题名《Symbolon: Symbolic Execution by Learning Code Transformation》和上述 method locator 共同限定。`; `VI Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29108:end -->

<!-- books-review:SF-2026-ARXIV-2606-29108:start -->
Principle Reuse; No Change — Existing Coverage. Ch81 已拥有 typed state machine、validator-owned commit、durable replay、sandbox、artifact lineage 与 bounded repair。 Fresh owner+adjacent reread found that《Symbolon: Symbolic Execution by Learning Code Transformation》的 `arXiv:2606.29108v1 version-stamped mirror — §Our approach; III Methodology` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Our approach; III Methodology。在 `AGENT-WORKFLOW` 中，该路径改变或检验的具体对象由题名《Symbolon: Symbolic Execution by Learning Code Transformation》和上述 method locator 共同限定。`; `VI Discussion; VIII Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29108:end -->

<!-- existing:SF-2026-ARXIV-2606-29116:start -->
Ch84 已把 agent definition、workflow graph、runtime/harness identity、trace、promotion 与 side-effect evidence 纳入平台生命周期。 Fresh owner+adjacent reread found that《Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem》的 `https://arxiv.org/html/2606.29116v1 — §Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29116:end -->

<!-- delta:SF-2026-ARXIV-2606-29116:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem。在 `AGENT-PLATFORM` 中，该路径改变或检验的具体对象由题名《Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem》和上述 method locator 共同限定。`; `3.4 RQ3: Failure Handling; 5 Discussion; 5.1 Threats to Construct Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29116:end -->

<!-- books-review:SF-2026-ARXIV-2606-29116:start -->
Principle Reuse; No Change — Existing Coverage. Ch84 已把 agent definition、workflow graph、runtime/harness identity、trace、promotion 与 side-effect evidence 纳入平台生命周期。 Fresh owner+adjacent reread found that《Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem》的 `https://arxiv.org/html/2606.29116v1 — §Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem。在 `AGENT-PLATFORM` 中，该路径改变或检验的具体对象由题名《Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem》和上述 method locator 共同限定。`; `3.4 RQ3: Failure Handling; 5 Discussion; 5.1 Threats to Construct Validity；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29116:end -->

<!-- existing:SF-2026-ARXIV-2606-29119:start -->
Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule》的 `https://arxiv.org/html/2606.29119v1 — §Report GitHub Issue; Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29119:end -->

<!-- delta:SF-2026-ARXIV-2606-29119:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 Report GitHub Issue; Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule》和上述 method locator 共同限定。`; `8 Limitations; 9 Discussion and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29119:end -->

<!-- books-review:SF-2026-ARXIV-2606-29119:start -->
Principle Reuse; No Change — Existing Coverage. Ch66 已版本化 EvalSpec、dataset/model/harness/environment/evaluator/metric/selector、校准与 release gate，但尚未要求 optimizer、evaluator 与 champion selector 调用同一可执行 aggregation contract。 Fresh owner+adjacent reread found that《Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule》的 `https://arxiv.org/html/2606.29119v1 — §Report GitHub Issue; Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 Report GitHub Issue; Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule。在 `PLATFORM-EVALUATION-SYSTEM` 中，该路径改变或检验的具体对象由题名《Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule》和上述 method locator 共同限定。`; `8 Limitations; 9 Discussion and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29119:end -->

<!-- existing:SF-2026-ARXIV-2606-29124:start -->
Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs》的 `https://arxiv.org/html/2606.29124v1 — §3 Methodology` remains an instance or bounded probe of this existing proposition.
<!-- existing:SF-2026-ARXIV-2606-29124:end -->

<!-- delta:SF-2026-ARXIV-2606-29124:start -->
该 family 的 source-specific contribution is `exact-v1 的机制路径为 3 Methodology。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs》和上述 method locator 共同限定。`; `2.3 SMTP Nesting Failures (Mailpit); Boundary value analysis (BVA):; 6 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- delta:SF-2026-ARXIV-2606-29124:end -->

<!-- books-review:SF-2026-ARXIV-2606-29124:start -->
Principle Reuse; No Change — Existing Coverage. Ch72 已拥有 capability/auth/effect 分权、canonical action、external reference monitor、quantization-conditioned backdoor gate、provenance 与 fail-closed fallback，但尚未把 protocol specification 编译为 extremal differential test receipt。 Fresh owner+adjacent reread found that《CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs》的 `https://arxiv.org/html/2606.29124v1 — §3 Methodology` remains an instance or bounded probe of this existing proposition. 该 family 的 source-specific contribution is `exact-v1 的机制路径为 3 Methodology。在 `PLATFORM-SECURITY` 中，该路径改变或检验的具体对象由题名《CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs》和上述 method locator 共同限定。`; `2.3 SMTP Nesting Failures (Mailpit); Boundary value analysis (BVA):; 6 Limitations and Future Work；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。` prevents it from adding a new owner/control/release contract.
<!-- books-review:SF-2026-ARXIV-2606-29124:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260628-COVERAGE-V1 | fresh-context:jun28-downstream-v1 | coverage | coverage:SRC-ARXIV:20260628 | — | 211/211 screened; 65 retained; 146 closures; denominator frozen | passed |
| SA-20260628-EVIDENCE-V1 | fresh-context:jun28-downstream-v1 | evidence | review:SF-2026-ARXIV-2606-28666; review:SF-2026-ARXIV-2606-28679; review:SF-2026-ARXIV-2606-28690; review:SF-2026-ARXIV-2606-28692; review:SF-2026-ARXIV-2606-28707; review:SF-2026-ARXIV-2606-28712; review:SF-2026-ARXIV-2606-28715; review:SF-2026-ARXIV-2606-28720; review:SF-2026-ARXIV-2606-28725; review:SF-2026-ARXIV-2606-28733; review:SF-2026-ARXIV-2606-28739; review:SF-2026-ARXIV-2606-28747; review:SF-2026-ARXIV-2606-28751; review:SF-2026-ARXIV-2606-28754; review:SF-2026-ARXIV-2606-28757; review:SF-2026-ARXIV-2606-28758; review:SF-2026-ARXIV-2606-28772; review:SF-2026-ARXIV-2606-28781; review:SF-2026-ARXIV-2606-28804; review:SF-2026-ARXIV-2606-28813; review:SF-2026-ARXIV-2606-28831; review:SF-2026-ARXIV-2606-28839; review:SF-2026-ARXIV-2606-28841; review:SF-2026-ARXIV-2606-28843; review:SF-2026-ARXIV-2606-28862; review:SF-2026-ARXIV-2606-28863; review:SF-2026-ARXIV-2606-28864; review:SF-2026-ARXIV-2606-28867; review:SF-2026-ARXIV-2606-28876; review:SF-2026-ARXIV-2606-28896; review:SF-2026-ARXIV-2606-28898; review:SF-2026-ARXIV-2606-28900; review:SF-2026-ARXIV-2606-28925; review:SF-2026-ARXIV-2606-28932; review:SF-2026-ARXIV-2606-28938; review:SF-2026-ARXIV-2606-28939; review:SF-2026-ARXIV-2606-28953; review:SF-2026-ARXIV-2606-28955; review:SF-2026-ARXIV-2606-28958; review:SF-2026-ARXIV-2606-28962; review:SF-2026-ARXIV-2606-28995; review:SF-2026-ARXIV-2606-28998; review:SF-2026-ARXIV-2606-29013; review:SF-2026-ARXIV-2606-29030; review:SF-2026-ARXIV-2606-29033; review:SF-2026-ARXIV-2606-29038; review:SF-2026-ARXIV-2606-29054; review:SF-2026-ARXIV-2606-29059; review:SF-2026-ARXIV-2606-29066; review:SF-2026-ARXIV-2606-29067; review:SF-2026-ARXIV-2606-29073; review:SF-2026-ARXIV-2606-29082; review:SF-2026-ARXIV-2606-29088; review:SF-2026-ARXIV-2606-29089; review:SF-2026-ARXIV-2606-29090; review:SF-2026-ARXIV-2606-29091; review:SF-2026-ARXIV-2606-29094; review:SF-2026-ARXIV-2606-29097; review:SF-2026-ARXIV-2606-29108; review:SF-2026-ARXIV-2606-29112; review:SF-2026-ARXIV-2606-29116; review:SF-2026-ARXIV-2606-29119; review:SF-2026-ARXIV-2606-29124; review:SF-2026-ARXIV-2606-29126; review:SF-2026-ARXIV-2606-29129 | — | 65/65 exact-v1 resolved; 64 official HTML plus one version-stamped mirror cross-check; blocker=0 | passed |
| SA-20260628-SELECTION-V1 | fresh-context:jun28-downstream-v1 | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-28666; analysis-decision:SF-2026-ARXIV-2606-28679; analysis:DA-20260628-PROTOCOL-EXECUTION-INVARIANTS; analysis-decision:SF-2026-ARXIV-2606-28692; analysis-decision:SF-2026-ARXIV-2606-28707; analysis-decision:SF-2026-ARXIV-2606-28712; analysis-decision:SF-2026-ARXIV-2606-28715; analysis-decision:SF-2026-ARXIV-2606-28720; analysis-decision:SF-2026-ARXIV-2606-28725; analysis-decision:SF-2026-ARXIV-2606-28733; analysis-decision:SF-2026-ARXIV-2606-28739; analysis-decision:SF-2026-ARXIV-2606-28747; analysis-decision:SF-2026-ARXIV-2606-28751; analysis-decision:SF-2026-ARXIV-2606-28754; analysis-decision:SF-2026-ARXIV-2606-28757; analysis-decision:SF-2026-ARXIV-2606-28758; analysis-decision:SF-2026-ARXIV-2606-28772; analysis-decision:SF-2026-ARXIV-2606-28781; analysis-decision:SF-2026-ARXIV-2606-28804; analysis-decision:SF-2026-ARXIV-2606-28813; analysis-decision:SF-2026-ARXIV-2606-28831; analysis-decision:SF-2026-ARXIV-2606-28839; analysis-decision:SF-2026-ARXIV-2606-28841; analysis-decision:SF-2026-ARXIV-2606-28843; analysis-decision:SF-2026-ARXIV-2606-28862; analysis-decision:SF-2026-ARXIV-2606-28863; analysis-decision:SF-2026-ARXIV-2606-28864; analysis-decision:SF-2026-ARXIV-2606-28867; analysis-decision:SF-2026-ARXIV-2606-28876; analysis-decision:SF-2026-ARXIV-2606-28896; analysis-decision:SF-2026-ARXIV-2606-28898; analysis-decision:SF-2026-ARXIV-2606-28900; analysis-decision:SF-2026-ARXIV-2606-28925; analysis-decision:SF-2026-ARXIV-2606-28932; analysis-decision:SF-2026-ARXIV-2606-28938; analysis-decision:SF-2026-ARXIV-2606-28939; analysis-decision:SF-2026-ARXIV-2606-28953; analysis-decision:SF-2026-ARXIV-2606-28955; analysis-decision:SF-2026-ARXIV-2606-28958; analysis-decision:SF-2026-ARXIV-2606-28962; analysis:DA-20260628-COMPILED-PHYSICAL-SAFETY; analysis-decision:SF-2026-ARXIV-2606-28998; analysis-decision:SF-2026-ARXIV-2606-29013; analysis-decision:SF-2026-ARXIV-2606-29030; analysis-decision:SF-2026-ARXIV-2606-29033; analysis:DA-20260628-SINGLE-METRIC-CONTRACT; analysis-decision:SF-2026-ARXIV-2606-29054; analysis-decision:SF-2026-ARXIV-2606-29059; analysis-decision:SF-2026-ARXIV-2606-29066; analysis-decision:SF-2026-ARXIV-2606-29067; analysis-decision:SF-2026-ARXIV-2606-29082; analysis-decision:SF-2026-ARXIV-2606-29088; analysis-decision:SF-2026-ARXIV-2606-29089; analysis-decision:SF-2026-ARXIV-2606-29090; analysis-decision:SF-2026-ARXIV-2606-29091; analysis-decision:SF-2026-ARXIV-2606-29094; analysis-decision:SF-2026-ARXIV-2606-29097; analysis-decision:SF-2026-ARXIV-2606-29108; analysis-decision:SF-2026-ARXIV-2606-29112; analysis-decision:SF-2026-ARXIV-2606-29116; analysis-decision:SF-2026-ARXIV-2606-29119; analysis-decision:SF-2026-ARXIV-2606-29126; analysis-decision:SF-2026-ARXIV-2606-29129 | — | 65/65 frontier; 3 selected, 2 subsumed, 60 not selected | passed |
| SA-20260628-BOOKS-POSTWRITE-V1 | fresh-context:jun28-downstream-v1 | books | books-review:SF-2026-ARXIV-2606-28666; books-review:SF-2026-ARXIV-2606-28679; books-review:SF-2026-ARXIV-2606-28690; review:SF-2026-ARXIV-2606-28692; review:SF-2026-ARXIV-2606-28707; review:SF-2026-ARXIV-2606-28712; books-review:SF-2026-ARXIV-2606-28715; books-review:SF-2026-ARXIV-2606-28720; books-review:SF-2026-ARXIV-2606-28725; books-review:SF-2026-ARXIV-2606-28733; books-review:SF-2026-ARXIV-2606-28739; books-review:SF-2026-ARXIV-2606-28747; review:SF-2026-ARXIV-2606-28751; review:SF-2026-ARXIV-2606-28754; books-review:SF-2026-ARXIV-2606-28757; review:SF-2026-ARXIV-2606-28758; books-review:SF-2026-ARXIV-2606-28772; books-review:SF-2026-ARXIV-2606-28781; review:SF-2026-ARXIV-2606-28804; books-review:SF-2026-ARXIV-2606-28813; books-review:SF-2026-ARXIV-2606-28831; books-review:SF-2026-ARXIV-2606-28839; books-review:SF-2026-ARXIV-2606-28841; books-review:SF-2026-ARXIV-2606-28843; books-review:SF-2026-ARXIV-2606-28862; books-review:SF-2026-ARXIV-2606-28863; review:SF-2026-ARXIV-2606-28864; books-review:SF-2026-ARXIV-2606-28867; books-review:SF-2026-ARXIV-2606-28876; review:SF-2026-ARXIV-2606-28896; review:SF-2026-ARXIV-2606-28898; books-review:SF-2026-ARXIV-2606-28900; books-review:SF-2026-ARXIV-2606-28925; review:SF-2026-ARXIV-2606-28932; review:SF-2026-ARXIV-2606-28938; books-review:SF-2026-ARXIV-2606-28939; books-review:SF-2026-ARXIV-2606-28953; books-review:SF-2026-ARXIV-2606-28955; books-review:SF-2026-ARXIV-2606-28958; books-review:SF-2026-ARXIV-2606-28962; books-review:SF-2026-ARXIV-2606-28995; books-review:SF-2026-ARXIV-2606-28998; review:SF-2026-ARXIV-2606-29013; books-review:SF-2026-ARXIV-2606-29030; books-review:SF-2026-ARXIV-2606-29033; books-review:SF-2026-ARXIV-2606-29038; books-review:SF-2026-ARXIV-2606-29054; review:SF-2026-ARXIV-2606-29059; books-review:SF-2026-ARXIV-2606-29066; books-review:SF-2026-ARXIV-2606-29067; books-review:SF-2026-ARXIV-2606-29073; books-review:SF-2026-ARXIV-2606-29082; books-review:SF-2026-ARXIV-2606-29088; books-review:SF-2026-ARXIV-2606-29089; books-review:SF-2026-ARXIV-2606-29090; books-review:SF-2026-ARXIV-2606-29091; books-review:SF-2026-ARXIV-2606-29094; books-review:SF-2026-ARXIV-2606-29097; books-review:SF-2026-ARXIV-2606-29108; review:SF-2026-ARXIV-2606-29112; books-review:SF-2026-ARXIV-2606-29116; books-review:SF-2026-ARXIV-2606-29119; books-review:SF-2026-ARXIV-2606-29124; review:SF-2026-ARXIV-2606-29126; review:SF-2026-ARXIV-2606-29129 | — | 6/6 Integrate writebacks, 42/42 No Change and 17/17 Weekly Only passed the 65/65 post-write fresh audit; unresolved findings 0 | passed |

## 8. Ignored Noise

候选分母外 identity 已在 full-population semantic screening ledger 中按 family-specific 理由关闭；Coverage Receipt 与 source packet 保留 raw、retained、closure 和 route-negative 账目，正文不重复展开低耐久度或越界项目。

### Materials and Access

- 65/65 exact-v1 resolved; 64 official HTML and one version-stamped full-text mirror cross-checked with arXiv metadata (`2606.29108v1`); pending=0; blocker=0; later versions used=0.
- No open Materials Request.

## 9. Recommended Action

- Integrate: 6/6 written across 6 owners; No Change: 42/42 revalidated; Weekly Only: 17/17 remained context-only.
- Shared Books were updated under root's serialized write lock; `docs/LEARNING_STATE.md` was not edited by this lane; all 65 dispositions were audited after writeback.

## 10. Repository Changes

- Date-local Daily/source packet/scripts plus the root-authorized six-owner Books writeback.

## 11. Open Questions

- Evidence and Selection passed the full fresh pre-write semantic audit.
- Books passed the 65/65 post-write fresh audit; unresolved findings: 0.

## 12. Sources

- [Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare](https://arxiv.org/abs/2606.28666v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks](https://arxiv.org/abs/2606.28679v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Formal Security Analysis of Agent Protocol Composition](https://arxiv.org/abs/2606.28690v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [An AI agent for treatment reasoning over a biomedical tool universe](https://arxiv.org/abs/2606.28692v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [BV-Blend: Uncertainty-Weighted Historical Baselines for Stable Critic-Free RL with Verifiable Rewards](https://arxiv.org/abs/2606.28707v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [J-LAW: Joint Localization and Actionable World Modeling via Coupled Latent Factor Graphs](https://arxiv.org/abs/2606.28712v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages](https://arxiv.org/abs/2606.28715v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance](https://arxiv.org/abs/2606.28720v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation](https://arxiv.org/abs/2606.28725v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Agentic Abstention: Do Agents Know When to Stop Instead of Act?](https://arxiv.org/abs/2606.28733v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Agent Safety Is Action Alignment](https://arxiv.org/abs/2606.28739v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Self-Supervised Theorem Discovery in a Formal Axiomatic System](https://arxiv.org/abs/2606.28747v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility](https://arxiv.org/abs/2606.28751v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [SHIFT: Dynamic Compute Relocation Framework for Communication-Aware Chiplet-Based Systems](https://arxiv.org/abs/2606.28754v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models](https://arxiv.org/abs/2606.28757v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving](https://arxiv.org/abs/2606.28758v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain](https://arxiv.org/abs/2606.28772v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [HyphaeDB: A Living Knowledge Topology for Agent-First Memory](https://arxiv.org/abs/2606.28781v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [ViPSim: Collaborating Visual and Parameter Spaces for Consistent Long-Horizon Embodied World Models](https://arxiv.org/abs/2606.28804v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning](https://arxiv.org/abs/2606.28813v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression](https://arxiv.org/abs/2606.28831v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables](https://arxiv.org/abs/2606.28839v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [LAMP: Lean-based Agentic framework with MCP and Proof Repair](https://arxiv.org/abs/2606.28841v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning](https://arxiv.org/abs/2606.28843v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [HKVLM: Faithful Query--Region Binding for Frozen-Detector Visual Grounding](https://arxiv.org/abs/2606.28862v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Defeat Devices in AI Systems](https://arxiv.org/abs/2606.28863v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [On Test-Time Scaling for Vision-Language Models](https://arxiv.org/abs/2606.28864v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages](https://arxiv.org/abs/2606.28867v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory](https://arxiv.org/abs/2606.28876v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation](https://arxiv.org/abs/2606.28896v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [PASTA: A Paraphrasing And Self-Training Approach for Knowledge Updating in LLMs](https://arxiv.org/abs/2606.28898v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes](https://arxiv.org/abs/2606.28900v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation](https://arxiv.org/abs/2606.28925v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [DLR: Zero-Inference-Cost Latent Residuals for Low-Rank Pre-Training](https://arxiv.org/abs/2606.28932v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [EVLA: An Electro-Aware Multimodal Assistant for Physically-Grounded Driving Reasoning and Control](https://arxiv.org/abs/2606.28938v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies](https://arxiv.org/abs/2606.28939v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Clustering Unsupervised Representations as Defense against Poisoning Attacks on Speech Commands Classification System](https://arxiv.org/abs/2606.28953v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Modification-Considering Value Learning for Reward Hacking Mitigation in RL](https://arxiv.org/abs/2606.28955v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration](https://arxiv.org/abs/2606.28958v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks](https://arxiv.org/abs/2606.28962v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [HJ-SafeDMP: Hamilton-Jacobi Reachability-Guided Dynamic Movement Primitives for Provably Safe Robot Motion](https://arxiv.org/abs/2606.28995v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation](https://arxiv.org/abs/2606.28998v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Mural: Transferring LLM knowledge to image generation via Mixture-of-Transformers](https://arxiv.org/abs/2606.29013v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering](https://arxiv.org/abs/2606.29030v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations](https://arxiv.org/abs/2606.29033v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy](https://arxiv.org/abs/2606.29038v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation](https://arxiv.org/abs/2606.29054v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Flow Matching in Feature Space for Stochastic World Modeling](https://arxiv.org/abs/2606.29059v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [$x$-Prediction Flow: Efficient Continuous Decoding for Masked Diffusion Language Models](https://arxiv.org/abs/2606.29066v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [ThinkProbe: Beyond Accuracy -- Structural Profiling of Open-Ended LLM Reasoning Traces via Non-Generative Thought Graphs](https://arxiv.org/abs/2606.29067v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes](https://arxiv.org/abs/2606.29073v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks](https://arxiv.org/abs/2606.29082v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking](https://arxiv.org/abs/2606.29088v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [TAP-VLA: Tactile Annotation Prompting for Vision Language Action Models](https://arxiv.org/abs/2606.29089v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering](https://arxiv.org/abs/2606.29090v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models](https://arxiv.org/abs/2606.29091v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [DiLaServe: High SLO Attainment Serving for Diffusion Language Models](https://arxiv.org/abs/2606.29094v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [TrafficAlign: Aligning Large Language Models for Traffic Scenario Generation](https://arxiv.org/abs/2606.29097v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Symbolon: Symbolic Execution by Learning Code Transformation](https://arxiv.org/abs/2606.29108v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [A Novel Latent-Class Attack and its Detection by Class Subspace Orthogonalization](https://arxiv.org/abs/2606.29112v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem](https://arxiv.org/abs/2606.29116v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Knowing in Advance When an Evolutionary Outer Loop Will Not Help: A Pre-Registered Cheap-Baseline Screening Rule](https://arxiv.org/abs/2606.29119v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [CornerCase: Automated Extremal Testing of Protocol Implementations using LLMs](https://arxiv.org/abs/2606.29124v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [HiComm: Hierarchical Communication for Multi-agent Reinforcement Learning](https://arxiv.org/abs/2606.29126v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Improved Scaling for Fast Mode of Ozaki Scheme II](https://arxiv.org/abs/2606.29129v1) — first-public（Asia/Shanghai）：2026-06-27；accessed：2026-08-29
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表

## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论由第 7 节记录的 pre-write 与 post-write fresh-context audit 承担。

State Truth: Completion=Complete；Coverage=Closed；Evidence=Passed；Books=Passed；Unresolved Findings=0。
