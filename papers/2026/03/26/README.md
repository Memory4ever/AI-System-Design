# Daily Research — 2026-03-26

**Research Date:** 2026-03-26

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-25 09:00:00 ～ 2026-03-26 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。2026-09-03 fresh-context 反证审计已重开；当前机器结构和既有 retained Review 仍可复用，但 denominator completeness 尚未按“不得抽样、逐项判断”合同重新验收。


## Executive Summary

> **2026-09-03 Semantic Reopen：** 旧 `Complete` 声明已被 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 取代。在 `MAR26-FC-001/MAR26-FC-002/MAR26-FC-003` 与 `MAR26-FC-004` 关闭前，本日报不得恢复 `Complete`；validator 通过只表示机器接口自洽。

严格窗口 raw/registered/screened=525/525/525；denominator=12、pre-denominator closures=513。exact-v1 Review complete=12、blocked=0；Integrate 建议=1。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-26 |
| Window End | 2026-03-26 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260326-AUTHOR-12 |
| Denominator Frozen At | 2026-09-02T16:07:11.473626+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-25T09:00:00+08:00 | 2026-03-26T09:00:00+08:00 | 2026-09-02T16:07:11.473626+08:00 | official-schedule recovery receipt + 525/525 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 525 | SF-2026-ARXIV-2603-23516;SF-2026-ARXIV-2603-23528;SF-2026-ARXIV-2603-23610;SF-2026-ARXIV-2603-23791;SF-2026-ARXIV-2603-23801;SF-2026-ARXIV-2603-23806;SF-2026-ARXIV-2603-23914;SF-2026-ARXIV-2603-24060;SF-2026-ARXIV-2603-24124;SF-2026-ARXIV-2603-24203;SF-2026-ARXIV-2603-24564;SF-2026-ARXIV-2603-24582 | pages=100; prefixes=00..99; final_cursor=end; registered=525; screened=525; retained=12; closure=513 | 2026-03-26T01:00:00+00:00 | screening-ledger-final.json#sha256=bb036bc5391c67c1a9bbbcc81145e0eef7091a3479e247a63ed20995b74d8618; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260326:start -->作者侧已逐项筛选全部 525 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260326:end -->

### Fresh-context Audit

<!-- fresh-context-audit:lane-c:start -->
非作者审计已重放 525/525 条 title+abstract：作者 retained 8 项均保留，4 个 false-negative family 已完成 exact-v1 Source Review，14 个 recall challenge 被逐项驳回，0 个 withdrawn 只保留 identity/status；reconciled denominator 为 12；Books queue 中 5 个 `Integrate` 被降为 `No Change — Existing Coverage`，0 个 owner 已重绑。本审计已重建分母、Review 与 Books comparison，但不写 Books；Coverage/Evidence/Books Gate 继续保持 Open，等待 root final reconciliation。收据：`papers/2026/03/_sources/daily-20260326/fresh-context-audit-receipt.json`、`fresh-context-retained-evidence-audit.json`、`fresh-context-books-audit.json`。
<!-- fresh-context-audit:lane-c:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-23516 | arXiv:2603.23516v1 | paper-v1:2603.23516 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23516 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23516 | no |
| SF-2026-ARXIV-2603-23528 | arXiv:2603.23528v1 | paper-v1:2603.23528 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23528 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23528 | no |
| SF-2026-ARXIV-2603-23610 | arXiv:2603.23610v1 | paper-v1:2603.23610 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23610 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23610 | no |
| SF-2026-ARXIV-2603-23791 | arXiv:2603.23791v1 | paper-v1:2603.23791 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23791 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23791 | no |
| SF-2026-ARXIV-2603-23801 | arXiv:2603.23801v1 | paper-v1:2603.23801 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23801 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23801 | no |
| SF-2026-ARXIV-2603-23806 | arXiv:2603.23806v1 | paper-v1:2603.23806 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-23806 | self | — | new_in_window | PLATFORM-TRACE | Integrate | books-review:SF-2026-ARXIV-2603-23806 | no |
| SF-2026-ARXIV-2603-23914 | arXiv:2603.23914v1 | paper-v1:2603.23914 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23914 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23914 | no |
| SF-2026-ARXIV-2603-24060 | arXiv:2603.24060v1 | paper-v1:2603.24060 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-24060 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24060 | no |
| SF-2026-ARXIV-2603-24124 | arXiv:2603.24124v1 | paper-v1:2603.24124 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-24124 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24124 | no |
| SF-2026-ARXIV-2603-24203 | arXiv:2603.24203v1 | paper-v1:2603.24203 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-24203 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24203 | no |
| SF-2026-ARXIV-2603-24564 | arXiv:2603.24564v1 | paper-v1:2603.24564 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-24564 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24564 | no |
| SF-2026-ARXIV-2603-24582 | arXiv:2603.24582v1 | paper-v1:2603.24582 | 2026-W13 | 2026-03-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-24582 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24582 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-23516 | RP-9d1c140a25579406 | standard | arXiv:2603.23516v1 | SRC-ARXIV@arXiv:2603.23516v1 | HTML — §3.1 Overall Design [facet=method]; https://arxiv.org/html/2603.23516v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23516v1.html; sha256:e37993a186bdc52b2b6e48f8062d285de8ea29232cab64affab7ea42e203958a | HTML — §4.3 Ablation Study [facet=evaluation]; https://arxiv.org/html/2603.23516v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23516v1.html; sha256:e37993a186bdc52b2b6e48f8062d285de8ea29232cab64affab7ea42e203958a | HTML — §7 Limitations [facet=limitations]; https://arxiv.org/html/2603.23516v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23516v1.html; sha256:e37993a186bdc52b2b6e48f8062d285de8ea29232cab64affab7ea42e203958a | arXiv exact-v1 identity https://arxiv.org/abs/2603.23516v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23516 | complete |
| SF-2026-ARXIV-2603-23528 | RP-67d382f6103a406d | standard | arXiv:2603.23528v1 | SRC-ARXIV@arXiv:2603.23528v1 | HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.23528v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23528v1.html; sha256:d2438105fca8a51638f503bd4f3ebf48abc354393b452fce8b26b12b33442afb | HTML — §4.3 Phase 2 Results: Local Validation [facet=evaluation]; https://arxiv.org/html/2603.23528v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23528v1.html; sha256:d2438105fca8a51638f503bd4f3ebf48abc354393b452fce8b26b12b33442afb | HTML — §6 Discussion [facet=limitations]; https://arxiv.org/html/2603.23528v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23528v1.html; sha256:d2438105fca8a51638f503bd4f3ebf48abc354393b452fce8b26b12b33442afb | arXiv exact-v1 identity https://arxiv.org/abs/2603.23528v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23528 | complete |
| SF-2026-ARXIV-2603-23610 | RP-512e9f48d826f3af | standard | arXiv:2603.23610v1 | SRC-ARXIV@arXiv:2603.23610v1 | HTML — §3.5 Implementation Details [facet=method]; https://arxiv.org/html/2603.23610v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23610v1.html; sha256:b0043806c84d83c95d30b968dda23d9f516903c1839885b84bc8944e4e0554e0 | HTML — §3 Experiments [facet=evaluation]; https://arxiv.org/html/2603.23610v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23610v1.html; sha256:b0043806c84d83c95d30b968dda23d9f516903c1839885b84bc8944e4e0554e0 | HTML — §5.5 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.23610v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23610v1.html; sha256:b0043806c84d83c95d30b968dda23d9f516903c1839885b84bc8944e4e0554e0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.23610v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23610 | complete |
| SF-2026-ARXIV-2603-23791 | RP-719605cf3e77cc97 | standard | arXiv:2603.23791v1 | SRC-ARXIV@arXiv:2603.23791v1 | HTML — §3 System Architecture: The Cognitive Firewall [facet=method]; https://arxiv.org/html/2603.23791v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23791v1.html; sha256:1bdb9a68504e87f5e9ab5a89ead400a7d94e3e14102e3396bc1ebd43cf3f9af2 | HTML — §5 Experimental Evaluation [facet=evaluation]; https://arxiv.org/html/2603.23791v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23791v1.html; sha256:1bdb9a68504e87f5e9ab5a89ead400a7d94e3e14102e3396bc1ebd43cf3f9af2 | HTML — §6.4 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.23791v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23791v1.html; sha256:1bdb9a68504e87f5e9ab5a89ead400a7d94e3e14102e3396bc1ebd43cf3f9af2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.23791v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23791 | complete |
| SF-2026-ARXIV-2603-23801 | RP-43f0dd827bb0f733 | standard | arXiv:2603.23801v1 | SRC-ARXIV@arXiv:2603.23801v1 | HTML — §5.1. Architecture Overview [facet=method]; https://arxiv.org/html/2603.23801v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23801v1.html; sha256:320f6899ff31d37be5c6dbfc21cfa3d5cbb739a89397003d587bb4daca307ede | HTML — §5.3. Phase 1: Spec-Level Analysis [facet=evaluation]; https://arxiv.org/html/2603.23801v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23801v1.html; sha256:320f6899ff31d37be5c6dbfc21cfa3d5cbb739a89397003d587bb4daca307ede | HTML — §Bounded model checking. [facet=limitations]; https://arxiv.org/html/2603.23801v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23801v1.html; sha256:320f6899ff31d37be5c6dbfc21cfa3d5cbb739a89397003d587bb4daca307ede | arXiv exact-v1 identity https://arxiv.org/abs/2603.23801v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23801 | complete |
| SF-2026-ARXIV-2603-23806 | RP-95b829ba09ecaeb2 | deep | arXiv:2603.23806v1 | SRC-ARXIV@arXiv:2603.23806v1 | HTML — §3. AgentPex Design [facet=method]; https://arxiv.org/html/2603.23806v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23806v1.html; sha256:74e91dd78b9dcd97d1b8d02ea2539659f6a5c5362051b9b0fca942b137741b7b | HTML — §4. Evaluation (§4.1 setup; §4.2–§4.5 results) [facet=evaluation]; https://arxiv.org/html/2603.23806v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23806v1.html; sha256:74e91dd78b9dcd97d1b8d02ea2539659f6a5c5362051b9b0fca942b137741b7b | HTML — §5. Discussion [facet=limitations]; https://arxiv.org/html/2603.23806v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23806v1.html; sha256:74e91dd78b9dcd97d1b8d02ea2539659f6a5c5362051b9b0fca942b137741b7b | arXiv exact-v1 identity https://arxiv.org/abs/2603.23806v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23806 | complete |
| SF-2026-ARXIV-2603-23914 | RP-40eb838b800ebde9 | standard | arXiv:2603.23914v1 | SRC-ARXIV@arXiv:2603.23914v1 | HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.23914v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23914v1.html; sha256:c0fd561ad8b94c84d173c53d56e9406a7566bb67bccd0dddccb927e93f7946cc | HTML — §4.2 Comparisons [facet=evaluation]; https://arxiv.org/html/2603.23914v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23914v1.html; sha256:c0fd561ad8b94c84d173c53d56e9406a7566bb67bccd0dddccb927e93f7946cc | HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.23914v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23914v1.html; sha256:c0fd561ad8b94c84d173c53d56e9406a7566bb67bccd0dddccb927e93f7946cc | arXiv exact-v1 identity https://arxiv.org/abs/2603.23914v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23914 | complete |
| SF-2026-ARXIV-2603-24060 | RP-8af40966dd323b0a | standard | arXiv:2603.24060v1 | SRC-ARXIV@arXiv:2603.24060v1 | HTML — §III Methodology [facet=method]; https://arxiv.org/html/2603.24060v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24060v1.html; sha256:9002a38617964a32146cd9f95e5b30a1088afbf886a7e6a8566f8c29f0c21e2a | HTML — §IV-B Main Results [facet=evaluation]; https://arxiv.org/html/2603.24060v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24060v1.html; sha256:9002a38617964a32146cd9f95e5b30a1088afbf886a7e6a8566f8c29f0c21e2a | HTML — §V CONCLUSIONS [facet=limitations]; https://arxiv.org/html/2603.24060v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24060v1.html; sha256:9002a38617964a32146cd9f95e5b30a1088afbf886a7e6a8566f8c29f0c21e2a | arXiv exact-v1 identity https://arxiv.org/abs/2603.24060v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-24060 | complete |
| SF-2026-ARXIV-2603-24124 | RP-c90aa5b9cbe929ba | standard | arXiv:2603.24124v1 | SRC-ARXIV@arXiv:2603.24124v1 | HTML — §4 Cascade Architecture [facet=method]; https://arxiv.org/html/2603.24124v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24124v1.html; sha256:98b364be5b87d84ca3dc1e7a51849f477cff15dcd5c7cab629c7a2d62eebef31 | HTML — §5 Experimental Validation [facet=evaluation]; https://arxiv.org/html/2603.24124v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24124v1.html; sha256:98b364be5b87d84ca3dc1e7a51849f477cff15dcd5c7cab629c7a2d62eebef31 | HTML — §8.2 Limitations [facet=limitations]; https://arxiv.org/html/2603.24124v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24124v1.html; sha256:98b364be5b87d84ca3dc1e7a51849f477cff15dcd5c7cab629c7a2d62eebef31 | arXiv exact-v1 identity https://arxiv.org/abs/2603.24124v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-24124 | complete |
| SF-2026-ARXIV-2603-24203 | RP-8c263516f82bde4a | standard | arXiv:2603.24203v1 | SRC-ARXIV@arXiv:2603.24203v1 | HTML — §IV-C Tree-Structured Optimization Architecture [facet=method]; https://arxiv.org/html/2603.24203v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24203v1.html; sha256:0c22870b14b596a23f82a50f777ae5b720388de71446ec8b7258deb5aab3f6b1 | HTML — §VI-C Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.24203v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24203v1.html; sha256:0c22870b14b596a23f82a50f777ae5b720388de71446ec8b7258deb5aab3f6b1 | HTML — §VIII-B Limitations and Future Works [facet=limitations]; https://arxiv.org/html/2603.24203v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24203v1.html; sha256:0c22870b14b596a23f82a50f777ae5b720388de71446ec8b7258deb5aab3f6b1 | arXiv exact-v1 identity https://arxiv.org/abs/2603.24203v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-24203 | complete |
| SF-2026-ARXIV-2603-24564 | RP-e072117d93e0f107 | standard | arXiv:2603.24564v1 | SRC-ARXIV@arXiv:2603.24564v1 | HTML — §2 ClawGang: an Infrastructure for Verifying Memory Value [facet=method]; https://arxiv.org/html/2603.24564v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24564v1.html; sha256:1cd7f93dc5403b33822ad851521534e37ccb0c2e6593f269fa034a7c130170a7 | HTML — §4 Illustrative Use Cases [facet=evaluation]; https://arxiv.org/html/2603.24564v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24564v1.html; sha256:1cd7f93dc5403b33822ad851521534e37ccb0c2e6593f269fa034a7c130170a7 | HTML — §2.3 Security and Failure Modes [facet=limitations]; https://arxiv.org/html/2603.24564v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24564v1.html; sha256:1cd7f93dc5403b33822ad851521534e37ccb0c2e6593f269fa034a7c130170a7 | arXiv exact-v1 identity https://arxiv.org/abs/2603.24564v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-24564 | complete |
| SF-2026-ARXIV-2603-24582 | RP-c4e1b351f82825e3 | standard | arXiv:2603.24582v1 | SRC-ARXIV@arXiv:2603.24582v1 | HTML — §4.1 Blind-spot mass over states and actions [facet=method]; https://arxiv.org/html/2603.24582v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24582v1.html; sha256:07e204d25f2eb7d8977544dcdeb3d9582db26051090d4da50d06bedeac516b7b | HTML — §5 Data, agent construction, and evaluation protocol [facet=evaluation]; https://arxiv.org/html/2603.24582v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24582v1.html; sha256:07e204d25f2eb7d8977544dcdeb3d9582db26051090d4da50d06bedeac516b7b | HTML — §7 Discussion and limitations [facet=limitations]; https://arxiv.org/html/2603.24582v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24582v1.html; sha256:07e204d25f2eb7d8977544dcdeb3d9582db26051090d4da50d06bedeac516b7b | arXiv exact-v1 identity https://arxiv.org/abs/2603.24582v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-24582 | complete |

### Source Reviews

### MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens

<!-- review:SF-2026-ARXIV-2603-23516:start -->
**问题**：full attention、固定 memory state 与外部 RAG 分别受二次成本、不可编辑或端到端失配约束。

**旧路径为何合理**：全量 attention 保留任意 token 交互，在中短序列上最直接。

**约束变化与机制**：MSA 组合 scalable sparse attention、document-wise RoPE、KV compression、Memory Parallel 与 Memory Interleaving，把超长 memory 作为可训练且可分布的模型状态。

**State / data / control owner**：`MODEL-LONG-CONTEXT` 负责 上下文选择、层次化表示和可访问记忆的语义边界；定位证据为 `HTML — §3.1 Overall Design [facet=method]; https://arxiv.org/html/2603.23516v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23516v1.html; sha256:e37993a186bdc52b2b6e48f8062d285de8ea29232cab64affab7ea42e203958a`。

**Evaluation contract 与未证明部分**：论文报告 16K→100M、2×A800 等指定配置的质量/容量；不能把作者 benchmark 外推为通用 lifetime memory。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.3 Ablation Study [facet=evaluation]; https://arxiv.org/html/2603.23516v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23516v1.html; sha256:e37993a186bdc52b2b6e48f8062d285de8ea29232cab64affab7ea42e203958a`。

**Trade-off / failure / coexistence**：线性扩展换来稀疏索引、并行通信和文档身份治理；证据需逐字引用时外部 RAG 仍更可审计。

<!-- claim:SF-2026-ARXIV-2603-23516:start -->**Claim Boundary**：只支持 arXiv:2603.23516v1 §3.1 Overall Design 的机制与 §4.3 Ablation Study 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23516:end -->
<!-- review:SF-2026-ARXIV-2603-23516:end -->
### The Compression Paradox in LLM Inference: Provider-Dependent Energy Effects of Prompt Compression

<!-- review:SF-2026-ARXIV-2603-23528:start -->
**问题**：prompt compression 常被默认视为 token 越少、能耗必然越低，但 provider 的执行路径和生成长度会改变端到端结果。

**旧路径为何合理**：把一次请求视为同质前向路径，接口最简单。

**约束变化与机制**：论文在三个 API provider、五个 benchmark 与四档压缩率上分离质量、token 数和能耗 proxy，并用本地直接测量校准 proxy；evaluation owner 因而必须记录 provider 与压缩策略。

**State / data / control owner**：`INFER-REQUEST-LIFECYCLE` 负责 请求阶段、状态身份、路由与成本归属；定位证据为 `HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.23528v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23528v1.html; sha256:d2438105fca8a51638f503bd4f3ebf48abc354393b452fce8b26b12b33442afb`。

**Evaluation contract 与未证明部分**：28,421 次成功调用支持 provider-dependent 方向差异；云端能耗仍是 proxy，不能推断数据中心实际功耗或碳排。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.3 Phase 2 Results: Local Validation [facet=evaluation]; https://arxiv.org/html/2603.23528v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23528v1.html; sha256:d2438105fca8a51638f503bd4f3ebf48abc354393b452fce8b26b12b33442afb`。

**Trade-off / failure / coexistence**：压缩可能减少输入成本，却增加摘要计算、输出长度或质量损失；短 prompt、强 prefix cache 或高质量敏感任务仍可不压缩。

<!-- claim:SF-2026-ARXIV-2603-23528:start -->**Claim Boundary**：只支持 arXiv:2603.23528v1 §3 Methodology 的机制与 §4.3 Phase 2 Results: Local Validation 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23528:end -->
<!-- review:SF-2026-ARXIV-2603-23528:end -->
### Environment Maps: Structured Environmental Representations for Long-Horizon Agents

<!-- review:SF-2026-ARXIV-2603-23610:start -->
**问题**：长任务只靠 transcript 重放环境，会把 UI 漂移、失败动作和多模态证据混进不可查询文本。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：Environment Maps 把屏幕录制与 execution trace 归并为 persistent graph，显式保存 entity、action、transition 与证据，让不同 agent 共享可更新的环境状态。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `HTML — §3.5 Implementation Details [facet=method]; https://arxiv.org/html/2603.23610v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23610v1.html; sha256:b0043806c84d83c95d30b968dda23d9f516903c1839885b84bc8944e4e0554e0`。

**Evaluation contract 与未证明部分**：长时软件 workflow 实验支持所测环境中的恢复与导航收益；图的正确性仍依赖抽取器和界面覆盖，不能视为环境真值。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §3 Experiments [facet=evaluation]; https://arxiv.org/html/2603.23610v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23610v1.html; sha256:b0043806c84d83c95d30b968dda23d9f516903c1839885b84bc8944e4e0554e0`。

**Trade-off / failure / coexistence**：结构化地图减少重复探索，却引入 stale node、错误合并和权限继承；稳定、短任务仍可直接使用当前 observation。

<!-- claim:SF-2026-ARXIV-2603-23610:start -->**Claim Boundary**：只支持 arXiv:2603.23610v1 §3.5 Implementation Details 的机制与 §3 Experiments 的公开 workload；§5.5 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23610:end -->
<!-- review:SF-2026-ARXIV-2603-23610:end -->
### The Cognitive Firewall:Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense

<!-- review:SF-2026-ARXIV-2603-23791:start -->
**问题**：纯 cloud 语义防御能力强但暴露隐私并增加交互延迟，纯 edge 规则又难识别语义化 indirect injection。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：Cognitive Firewall 把 local visual sentinel、cloud deep planner 与 deterministic execution guard 分层：edge 先筛选，cloud 解释可疑内容，最终副作用仍由本地 policy commit。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §3 System Architecture: The Cognitive Firewall [facet=method]; https://arxiv.org/html/2603.23791v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23791v1.html; sha256:1bdb9a68504e87f5e9ab5a89ead400a7d94e3e14102e3396bc1ebd43cf3f9af2`。

**Evaluation contract 与未证明部分**：1,000 个 adversarial samples 支持所测攻击下 hybrid defense 优于 edge-only；模型、页面分布和网络条件限制外推。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5 Experimental Evaluation [facet=evaluation]; https://arxiv.org/html/2603.23791v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23791v1.html; sha256:1bdb9a68504e87f5e9ab5a89ead400a7d94e3e14102e3396bc1ebd43cf3f9af2`。

**Trade-off / failure / coexistence**：split defense 平衡语义能力和隐私，却引入 cloud availability、传输泄漏和跨层 disagreement；离线或高机密环境仍需纯本地 conservative guard。

<!-- claim:SF-2026-ARXIV-2603-23791:start -->**Claim Boundary**：只支持 arXiv:2603.23791v1 §3 System Architecture: The Cognitive Firewall 的机制与 §5 Experimental Evaluation 的公开 workload；§6.4 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23791:end -->
<!-- review:SF-2026-ARXIV-2603-23791:end -->
### AgentRFC: Security Design Principles and Conformance Testing for Agent Protocols

<!-- review:SF-2026-ARXIV-2603-23801:start -->
**问题**：agent protocol 各自声明安全属性时，跨 MCP/A2A 等共享基础设施的组合破坏不会被单协议检查发现。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：AgentRFC 定义六层 protocol stack 与 11 个 TLA+ invariant，并把规范抽成 typed IR、model-check counterexample 后回放到 live SDK。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §5.1. Architecture Overview [facet=method]; https://arxiv.org/html/2603.23801v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23801v1.html; sha256:320f6899ff31d37be5c6dbfc21cfa3d5cbb739a89397003d587bb4daca307ede`。

**Evaluation contract 与未证明部分**：形式模型与代表性实现可证明定义内的 non-conformance/组合反例；不能证明规范外环境或未知实现安全。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.3. Phase 1: Spec-Level Analysis [facet=evaluation]; https://arxiv.org/html/2603.23801v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23801v1.html; sha256:320f6899ff31d37be5c6dbfc21cfa3d5cbb739a89397003d587bb4daca307ede`。

**Trade-off / failure / coexistence**：conformance pipeline 提高可复算性，却增加规范抽取、状态爆炸和 replay 维护；简单单协议仍可用较窄测试。

<!-- claim:SF-2026-ARXIV-2603-23801:start -->**Claim Boundary**：只支持 arXiv:2603.23801v1 §5.1. Architecture Overview 的机制与 §5.3. Phase 1: Spec-Level Analysis 的公开 workload；§Bounded model checking. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23801:end -->
<!-- review:SF-2026-ARXIV-2603-23801:end -->
### Willful Disobedience: Automatically Detecting Failures in Agentic Traces

<!-- review:SF-2026-ARXIV-2603-23806:start -->
**问题**：只验最终任务成功会漏掉错误路由、违规 tool call 和中途越权，因为这些程序性失败可能偶然得到正确结果。

**旧路径为何合理**：日志记录结果适合单进程、短链路故障。

**约束变化与机制**：AgentPex 从 prompt/system instruction 抽取行为规则，再对完整 trace 的对话、决策与 tool event 做 rule-conditioned judgment，把 outcome 与 process evidence 分离。

**State / data / control owner**：`PLATFORM-TRACE` 负责 trace identity、因果边和可归责事件；定位证据为 `HTML — §3. AgentPex Design [facet=method]; https://arxiv.org/html/2603.23806v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23806v1.html; sha256:74e91dd78b9dcd97d1b8d02ea2539659f6a5c5362051b9b0fca942b137741b7b`。

**Evaluation contract 与未证明部分**：多类 agent trace 上的检测实验支持该审计路径；规则抽取和 judge 一致性仍受模型偏差影响，不能替代确定性 effect receipt。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4. Evaluation (§4.1 setup; §4.2–§4.5 results) [facet=evaluation]; https://arxiv.org/html/2603.23806v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23806v1.html; sha256:74e91dd78b9dcd97d1b8d02ea2539659f6a5c5362051b9b0fca942b137741b7b`。

**Trade-off / failure / coexistence**：trace 级审计提高可诊断性，却增加存储、隐私和 judge 成本；短、确定性 workflow 仍可由显式状态机断言直接验证。

<!-- claim:SF-2026-ARXIV-2603-23806:start -->**Claim Boundary**：只支持 arXiv:2603.23806v1 §3. AgentPex Design 的机制与 §4. Evaluation（§4.1 setup；§4.2–§4.5 results）的公开 workload；§5. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23806:end -->
<!-- review:SF-2026-ARXIV-2603-23806:end -->
### Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding

<!-- review:SF-2026-ARXIV-2603-23914:start -->
**问题**：VLM decode 若完整保存每个视觉/文本 token 的多头 KV，长图像序列会让 memory bandwidth 和容量先于算力成为瓶颈。

**旧路径为何合理**：逐 token decode 保持状态提交清晰。

**约束变化与机制**：AttentionPack 在 head 间压缩 KV，并按当前 attention 需要自适应解压，把压缩 rank 与 read path 变成逐层 runtime policy。

**State / data / control owner**：`INFER-DECODE` 负责 decode 状态、memory access 与提交顺序；定位证据为 `HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.23914v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23914v1.html; sha256:c0fd561ad8b94c84d173c53d56e9406a7566bb67bccd0dddccb927e93f7946cc`。

**Evaluation contract 与未证明部分**：多高分辨率/长上下文任务的质量、显存与 latency 实验支持所测 VLM 的折中；不证明相同 rank 适用于所有模态、层和硬件。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.2 Comparisons [facet=evaluation]; https://arxiv.org/html/2603.23914v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.23914v1.html; sha256:c0fd561ad8b94c84d173c53d56e9406a7566bb67bccd0dddccb927e93f7946cc`。

**Trade-off / failure / coexistence**：attention-aware 解压节省容量，却增加 projection compute、metadata 和错误 rank 风险；视觉 token 少或 HBM 充足时完整 KV 更稳。

<!-- claim:SF-2026-ARXIV-2603-23914:start -->**Claim Boundary**：只支持 arXiv:2603.23914v1 §3 Methodology 的机制与 §4.2 Comparisons 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23914:end -->
<!-- review:SF-2026-ARXIV-2603-23914:end -->
### RoboHarness: A Memory-Augmented Policy Harness for Vision-Language-Action Model Robustness via In-Context Adaptation

<!-- review:SF-2026-ARXIV-2603-24060:start -->
**问题**：冻结 VLA 在 OOD 扰动下只能重复当前 policy，既不积累失败证据，也无法解释应在何处介入。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：RoboHarness 在 policy 外维护正负 dual memory，以 retrieval 提供相似经验，再用 causal attribution 选择 intervention，而不修改基础权重。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `HTML — §III Methodology [facet=method]; https://arxiv.org/html/2603.24060v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24060v1.html; sha256:9002a38617964a32146cd9f95e5b30a1088afbf886a7e6a8566f8c29f0c21e2a`。

**Evaluation contract 与未证明部分**：多类机器人扰动实验支持所测 frozen VLA 的 in-context robustness；收益依赖 memory quality 与 attribution，不能外推到未见 embodiment。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §IV-B Main Results [facet=evaluation]; https://arxiv.org/html/2603.24060v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24060v1.html; sha256:9002a38617964a32146cd9f95e5b30a1088afbf886a7e6a8566f8c29f0c21e2a`。

**Trade-off / failure / coexistence**：外置 harness 可快速适配且可回滚，但增加 retrieval latency、memory poisoning 和错误干预；分布稳定、可重训场景仍可直接 fine-tune policy。

<!-- claim:SF-2026-ARXIV-2603-24060:start -->**Claim Boundary**：只支持 arXiv:2603.24060v1 §III Methodology 的机制与 §IV-B Main Results 的公开 workload；§V CONCLUSIONS 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-24060:end -->
<!-- review:SF-2026-ARXIV-2603-24060:end -->
### The Alignment Tax: Response Homogenization in Aligned LLMs and Its Implications for Uncertainty Estimation

<!-- review:SF-2026-ARXIV-2603-24124:start -->
**问题**：多次采样的语义分歧常被当作不确定性，但 alignment 会把表达压成同一簇，使一致性不再代表知道。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：论文通过 base→SFT→DPO stage ablation 分离 response homogenization，并比较 semantic clustering 与 token entropy；uncertainty owner 必须记录训练阶段和信号来源。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `HTML — §4 Cascade Architecture [facet=method]; https://arxiv.org/html/2603.24124v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24124v1.html; sha256:98b364be5b87d84ca3dc1e7a51849f477cff15dcd5c7cab629c7a2d62eebef31`。

**Evaluation contract 与未证明部分**：TruthfulQA、GSM8K 及多次采样结果支持 homogenization 会让 sampling-based score 失效；任务差异说明 token entropy 也不是普适置信度。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5 Experimental Validation [facet=evaluation]; https://arxiv.org/html/2603.24124v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24124v1.html; sha256:98b364be5b87d84ca3dc1e7a51849f477cff15dcd5c7cab629c7a2d62eebef31`。

**Trade-off / failure / coexistence**：更底层 entropy 保留部分信号，却可能反映措辞而非事实正确性；高风险回答仍需外部 evidence、calibration 和 abstention。

<!-- claim:SF-2026-ARXIV-2603-24124:start -->**Claim Boundary**：只支持 arXiv:2603.24124v1 §4 Cascade Architecture 的机制与 §5 Experimental Validation 的公开 workload；§8.2 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-24124:end -->
<!-- review:SF-2026-ARXIV-2603-24124:end -->
### Invisible Threats from Model Context Protocol: Generating Stealthy Injection Payload via Tree-based Adaptive Search

<!-- review:SF-2026-ARXIV-2603-24203:start -->
**问题**：固定模板或白盒优化的 MCP indirect injection 易被防御器识别，不能代表攻击者在黑盒 tool-response 通道中的适应能力。

**旧路径为何合理**：把协议当作普通 tool adapter，部署和权限模型最简单。

**约束变化与机制**：TIP 用 tree search 维护 payload 分支，结合 path feedback、tool-response simulation、defense-aware mutation 与 prune/early-stop，逐步寻找可执行且隐蔽的注入。

**State / data / control owner**：`AGENT-MCP` 负责 协议身份、capability 声明、授权与审计状态；定位证据为 `HTML — §IV-C Tree-Structured Optimization Architecture [facet=method]; https://arxiv.org/html/2603.24203v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24203v1.html; sha256:0c22870b14b596a23f82a50f777ae5b720388de71446ec8b7258deb5aab3f6b1`。

**Evaluation contract 与未证明部分**：多模型、场景、防御和真实 MCP case study 支持所测 search 的攻击成功与迁移；它不证明所有 tool client 均可被同样利用。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §VI-C Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.24203v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24203v1.html; sha256:0c22870b14b596a23f82a50f777ae5b720388de71446ec8b7258deb5aab3f6b1`。

**Trade-off / failure / coexistence**：自适应 search 提高覆盖也提高攻击查询成本，防御侧仍需 capability admission、response provenance 与 effect-time authorization，而不能只训练文本分类器。

<!-- claim:SF-2026-ARXIV-2603-24203:start -->**Claim Boundary**：只支持 arXiv:2603.24203v1 §IV-C Tree-Structured Optimization Architecture 的机制与 §VI-C Results and Analysis 的公开 workload；§VIII-B Limitations and Future Works 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-24203:end -->
<!-- review:SF-2026-ARXIV-2603-24203:end -->
### Infrastructure for Valuable, Tradable, and Verifiable Agent Memory

<!-- review:SF-2026-ARXIV-2603-24564:start -->
**问题**：agent memory 若跨主体交易，普通文本或向量记录无法证明来源、计算投入与执行环境兼容。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：clawgang 将 memory 与可验证 computation provenance 绑定，meowtrade 再把认证 artifact 的 listing、transfer 与 governance 分层。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `HTML — §2 ClawGang: an Infrastructure for Verifying Memory Value [facet=method]; https://arxiv.org/html/2603.24564v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24564v1.html; sha256:1cd7f93dc5403b33822ad851521534e37ccb0c2e6593f269fa034a7c130170a7`。

**Evaluation contract 与未证明部分**：exact-v1 主要是架构与经济机制主张，缺少独立大规模安全/价值实验；只能支持 provenance contract，不支持市场价值结论。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4 Illustrative Use Cases [facet=evaluation]; https://arxiv.org/html/2603.24564v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24564v1.html; sha256:1cd7f93dc5403b33822ad851521534e37ccb0c2e6593f269fa034a7c130170a7`。

**Trade-off / failure / coexistence**：可验证 lineage 增加签名、环境 identity、撤销和隐私成本；单用户私有 memory 无需市场层。

<!-- claim:SF-2026-ARXIV-2603-24564:start -->**Claim Boundary**：只支持 arXiv:2603.24564v1 §2 ClawGang: an Infrastructure for Verifying Memory Value 的机制与 §4 Illustrative Use Cases 的公开 workload；§2.3 Security and Failure Modes 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-24564:end -->
<!-- review:SF-2026-ARXIV-2603-24564:end -->
### The Stochastic Gap: A Markovian Framework for Pre-Deployment Reliability and Oversight-Cost Auditing in Agentic Artificial Intelligence

<!-- review:SF-2026-ARXIV-2603-24582:start -->
**问题**：agent workflow 的 state 看似常见，不代表 state-action transition 有足够样本支持自动执行。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：该框架用 Markov visitation measure 区分 state blind mass 与 state-action blind mass，并把 entropy escalation gate 映射为预期人工 oversight cost。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `HTML — §4.1 Blind-spot mass over states and actions [facet=method]; https://arxiv.org/html/2603.24582v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24582v1.html; sha256:07e204d25f2eb7d8977544dcdeb3d9582db26051090d4da50d06bedeac516b7b`。

**Evaluation contract 与未证明部分**：BPI 2019 log 的 held-out simulation 支持所定义 blind-mass/成本关系；日志策略不是真实 autonomous agent，不能证明 deployment reliability。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5 Data, agent construction, and evaluation protocol [facet=evaluation]; https://arxiv.org/html/2603.24582v1; papers/2026/03/_sources/daily-20260326/exact-v1-bodies/2603.24582v1.html; sha256:07e204d25f2eb7d8977544dcdeb3d9582db26051090d4da50d06bedeac516b7b`。

**Trade-off / failure / coexistence**：细化 state 提高风险可见性却扩大稀疏空间和人工负担；确定性流程仍可用显式规则。

<!-- claim:SF-2026-ARXIV-2603-24582:start -->**Claim Boundary**：只支持 arXiv:2603.24582v1 §4.1 Blind-spot mass over states and actions 的机制与 §5 Data, agent construction, and evaluation protocol 的公开 workload；§7 Discussion and limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-24582:end -->
<!-- review:SF-2026-ARXIV-2603-24582:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-23806 | score_7_9;potential_books_delta | selected | DA-20260326-06 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260326-06 |

<!-- analysis:DA-20260326-06:start -->
### Willful Disobedience: Automatically Detecting Failures in Agentic Traces

只验最终任务成功会漏掉错误路由、违规 tool call 和中途越权，因为这些程序性失败可能偶然得到正确结果。 旧路径在其原约束下仍合理：日志记录结果适合单进程、短链路故障。 本 family 的设计变化是：AgentPex 从 prompt/system instruction 抽取行为规则，再对完整 trace 的对话、决策与 tool event 做 rule-conditioned judgment，把 outcome 与 process evidence 分离。 其公开验证边界为：多类 agent trace 上的检测实验支持该审计路径；规则抽取和 judge 一致性仍受模型偏差影响，不能替代确定性 effect receipt。 新增代价与回退条件为：trace 级审计提高可诊断性，却增加存储、隐私和 judge 成本；短、确定性 workflow 仍可由显式状态机断言直接验证。
<!-- analysis:DA-20260326-06:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-23516 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#conditional-attention-的路由粒度必须匹配执行粒度 (section Ch-owner) | books/part-02-model/21-moe.md#第21章-moe (section Ch-adjacent); books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23516 | delta:SF-2026-ARXIV-2603-23516 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23516 |
| SF-2026-ARXIV-2603-23528 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/41-deepspeed.md#第41章-训练状态-runtime-policy：以-deepspeed-为例 (section Ch-adjacent); books/part-05-inference-system/43-prefill.md#第43章-prefill (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23528 | delta:SF-2026-ARXIV-2603-23528 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23528 |
| SF-2026-ARXIV-2603-23610 | AGENT-MEMORY | books/part-07-agent/77-memory.md#fact-state-与-retrieval-policy-state-必须分离 (section Ch-owner) | books/part-07-agent/76-rag.md#retrieval-object-需要-validity-与-lifecycle (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23610 | delta:SF-2026-ARXIV-2603-23610 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23610 |
| SF-2026-ARXIV-2603-23791 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#多跳-delegation-必须保留-human-principal (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23791 | delta:SF-2026-ARXIV-2603-23791 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23791 |
| SF-2026-ARXIV-2603-23801 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#多-agent-cascade-需要跨-channel-的-influence-graph (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23801 | delta:SF-2026-ARXIV-2603-23801 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23801 |
| SF-2026-ARXIV-2603-23806 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#安全与成本 (section Ch-owner) | books/part-06-ai-infrastructure/68-logging.md#第68章-logging (section Ch-adjacent); books/part-06-ai-infrastructure/70-cost.md#第70章-cost (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23806 | delta:SF-2026-ARXIV-2603-23806 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-23806 |
| SF-2026-ARXIV-2603-23914 | INFER-DECODE | books/part-05-inference-system/44-decode.md#自检问题 (section Ch-owner) | books/part-05-inference-system/43-prefill.md#第43章-prefill (section Ch-adjacent); books/part-05-inference-system/45-why-kv-cache-speeds-up.md#第45章-为什么-kv-cache-能提速 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23914 | delta:SF-2026-ARXIV-2603-23914 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23914 |
| SF-2026-ARXIV-2603-24060 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#continual-vla-的-adapter-timescale-与-replay-frontier-属于-policy-identity (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#open-loop-imagination-vs-closed-loop-correction (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-24060 | delta:SF-2026-ARXIV-2603-24060 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24060 |
| SF-2026-ARXIV-2603-24124 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-24124 | delta:SF-2026-ARXIV-2603-24124 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24124 |
| SF-2026-ARXIV-2603-24203 | AGENT-MCP | books/part-07-agent/83-mcp.md#update-2026-07-29-—-从连接会话到显式请求契约 (section Ch-owner) | books/part-07-agent/82-multi-agent.md#扩展-agent-数量之前，先测量-coordination-tax (section Ch-adjacent); books/part-07-agent/84-agent-platform.md#从-trajectory-到-skill-是一次受治理的-compilation (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-24203 | delta:SF-2026-ARXIV-2603-24203 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24203 |
| SF-2026-ARXIV-2603-24564 | AGENT-MEMORY | books/part-07-agent/77-memory.md#context-与-memory-的状态边界 (section Ch-owner) | books/part-07-agent/76-rag.md#retrieval-object-需要-validity-与-lifecycle (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-24564 | delta:SF-2026-ARXIV-2603-24564 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24564 |
| SF-2026-ARXIV-2603-24582 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#skill-必须在真实-control-path-中评估 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-24582 | delta:SF-2026-ARXIV-2603-24582 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24582 |

<!-- books-review:SF-2026-ARXIV-2603-23516:start -->
### MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23516:start -->已读 owner `books/part-02-model/22-long-context.md` 与相邻章节。现有命题：Head-level route 更细，却容易造成同一 kernel 内不规则 memory access；layer-level route 损失表达粒度，但更容易 整体跳过远端 KV traffic。Route vector 必须进入 prefix/KV/cache identity；tool result 追加或 Context mutation 后 要定义延续、重算或 fallback。固定配置在 batch 规整、graph capture、cache sharing 或 calibration 不可靠时仍然 合理。Flux Attention 的作者结果只覆盖特定模型、A800、batch 1、BF16 和 sparse kernel，不是 production goodput。<!-- existing:SF-2026-ARXIV-2603-23516:end -->

<!-- delta:SF-2026-ARXIV-2603-23516:start -->新证据差异：MSA 组合 scalable sparse attention、document-wise RoPE、KV compression、Memory Parallel 与 Memory Interleaving，把超长 memory 作为可训练且可分布的模型状态。<!-- delta:SF-2026-ARXIV-2603-23516:end -->

边界：只支持 arXiv:2603.23516v1 §3.1 Overall Design 的机制与 §4.3 Ablation Study 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23516:end -->
<!-- books-review:SF-2026-ARXIV-2603-23528:start -->
### The Compression Paradox in LLM Inference: Provider-Dependent Energy Effects of Prompt Compression — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23528:start -->已读 owner `books/part-05-inference-system/42-what-happens-during-inference.md` 与相邻章节。现有命题：本章的核心判断是：**LLM inference 是一个持续演化的 token-generation process，而不是一次无状态函数调用。**请求会依次经历输入处理、admission、Prefill、Decode、streaming 和完成清理；每一步都在改变 token progress、KV ownership、GPU memory 与调度资格。<!-- existing:SF-2026-ARXIV-2603-23528:end -->

<!-- delta:SF-2026-ARXIV-2603-23528:start -->新证据差异：论文在三个 API provider、五个 benchmark 与四档压缩率上分离质量、token 数和能耗 proxy，并用本地直接测量校准 proxy；evaluation owner 因而必须记录 provider 与压缩策略。<!-- delta:SF-2026-ARXIV-2603-23528:end -->

边界：只支持 arXiv:2603.23528v1 §3 Methodology 的机制与 §4.3 Phase 2 Results: Local Validation 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23528:end -->
<!-- books-review:SF-2026-ARXIV-2603-23610:start -->
### Environment Maps: Structured Environmental Representations for Long-Horizon Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23610:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：若先在全库排名再过滤 ACL，会把不可访问信息泄漏进 score；若 benchmark 静默改变 granularity 或 candidate pool， NDCG/Recall 也不再是同一问题。LMEB 的受限对照支持通用 passage ranking 不能代表 long-horizon Memory retrieval， 不证明其混合数据集均值就是生产选择标准。MTEB/BEIR 在开放文档检索中继续成立；Memory benchmark 还必须测 write correctness、authorization、deletion/freshness、answer use 与最终 outcome，不能由 retrieval 分数包办。<!-- existing:SF-2026-ARXIV-2603-23610:end -->

<!-- delta:SF-2026-ARXIV-2603-23610:start -->新证据差异：Environment Maps 把屏幕录制与 execution trace 归并为 persistent graph，显式保存 entity、action、transition 与证据，让不同 agent 共享可更新的环境状态。<!-- delta:SF-2026-ARXIV-2603-23610:end -->

边界：只支持 arXiv:2603.23610v1 §3.5 Implementation Details 的机制与 §3 Experiments 的公开 workload；§5.5 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23610:end -->
<!-- books-review:SF-2026-ARXIV-2603-23791:start -->
### The Cognitive Firewall:Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23791:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：这把 authorization 从 prompt/Agent 自述迁移到可核验 provenance chain，但不证明行为正确，也不替代 prompt-injection defense、sandbox 或最小权限。Key/token 生命周期、撤销、重放和 scope composition 都是新增压力；链不完整、过期或验证失败时必须 fail closed，并回退人工授权。<!-- existing:SF-2026-ARXIV-2603-23791:end -->

<!-- delta:SF-2026-ARXIV-2603-23791:start -->新证据差异：Cognitive Firewall 把 local visual sentinel、cloud deep planner 与 deterministic execution guard 分层：edge 先筛选，cloud 解释可疑内容，最终副作用仍由本地 policy commit。<!-- delta:SF-2026-ARXIV-2603-23791:end -->

边界：只支持 arXiv:2603.23791v1 §3 System Architecture: The Cognitive Firewall 的机制与 §5 Experimental Evaluation 的公开 workload；§6.4 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23791:end -->
<!-- books-review:SF-2026-ARXIV-2603-23801:start -->
### AgentRFC: Security Design Principles and Conformance Testing for Agent Protocols — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23801:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：逐条扫描 message 或只在最终 action 上做 policy check，在通信拓扑固定、传播链短时简单有效；当一个污染信号经 message、shared memory、delegation 与 tool result 多次改写后，单 channel 告警既无法说明起点，也无法判断哪个 Agent 正在放大影响。运行时可以维护带 revision 的 cross-channel influence graph：各 channel adapter 只提交 observation，causal monitor 关联传播路径并提出 suspect source / edge，security policy 仍独立决定隔离、降权或阻断，不能把统计 attribution 当作 authorization。<!-- existing:SF-2026-ARXIV-2603-23801:end -->

<!-- delta:SF-2026-ARXIV-2603-23801:start -->新证据差异：AgentRFC 定义六层 protocol stack 与 11 个 TLA+ invariant，并把规范抽成 typed IR、model-check counterexample 后回放到 live SDK。<!-- delta:SF-2026-ARXIV-2603-23801:end -->

边界：只支持 arXiv:2603.23801v1 §5.1. Architecture Overview 的机制与 §5.3. Phase 1: Spec-Level Analysis 的公开 workload；§Bounded model checking. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23801:end -->
<!-- books-review:SF-2026-ARXIV-2603-23806:start -->
### Willful Disobedience: Automatically Detecting Failures in Agentic Traces — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23806:start -->已读 owner `books/part-06-ai-infrastructure/69-trace.md` 与相邻章节。现有命题：Instrumentation overhead 应被度量：serialization、context propagation、collector queue、export failures 与 storage cost。Trace 系统故障不应阻塞普通请求，但高风险 action 的 audit 要另有可靠路径。<!-- existing:SF-2026-ARXIV-2603-23806:end -->

<!-- delta:SF-2026-ARXIV-2603-23806:start -->新证据差异：AgentPex 从 prompt/system instruction 抽取行为规则，再对完整 trace 的对话、决策与 tool event 做 rule-conditioned judgment，把 outcome 与 process evidence 分离。<!-- delta:SF-2026-ARXIV-2603-23806:end -->

边界：只支持 arXiv:2603.23806v1 §3. AgentPex Design 的机制与 §4. Evaluation（§4.1 setup；§4.2–§4.5 results）的公开 workload；§5. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-23806:end -->
<!-- books-review:SF-2026-ARXIV-2603-23914:start -->
### Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23914:start -->已读 owner `books/part-05-inference-system/44-decode.md` 与相邻章节。现有命题：1. Autoregressive factorization 为什么造成真实时间依赖？ 2. Decode 的 logical shape 与 Prefill 有何不同？ 3. KV Cache 消除了哪些 work，又保留了什么？ 4. 为什么单请求 Decode 常难以充分复用 weights？ 5. 增大 active batch 为什么可能同时提升吞吐并恶化 TPOT？ 6. Iteration latency 为什么不必然等于请求 TPOT？ 7. Speculative Decoding 是否消除了 autoregressive dependency？ 8. Decode runner 为什么必须同时携带 `position`、`context_len` 与 `block_table`？ 9. 为什么 sampled token 只能在本轮 KV progress 提交后成为下一轮输入？<!-- existing:SF-2026-ARXIV-2603-23914:end -->

<!-- delta:SF-2026-ARXIV-2603-23914:start -->新证据差异：AttentionPack 在 head 间压缩 KV，并按当前 attention 需要自适应解压，把压缩 rank 与 read path 变成逐层 runtime policy。<!-- delta:SF-2026-ARXIV-2603-23914:end -->

边界：只支持 arXiv:2603.23914v1 §3 Methodology 的机制与 §4.2 Comparisons 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23914:end -->
<!-- books-review:SF-2026-ARXIV-2603-24060:start -->
### RoboHarness: A Memory-Augmented Policy Harness for Vision-Language-Action Model Robustness via In-Context Adaptation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-24060:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：一个受限分支把 adaptation state 拆成 fast 与 slow 两个 timescale：fast adapter 接收当前 task，slow adapter 保存较稳定的跨 task knowledge；replay cache 只保留带 provenance 的有界样本，并在旧 prefix 上 stop-gradient、对新 suffix 重新生成训练 signal。此时 adapter pair、task order、replay frontier、cache admission、base-policy revision 与 reset boundary 共同构成 policy identity，不能只保存一份 LoRA weights 就声称可恢复。<!-- existing:SF-2026-ARXIV-2603-24060:end -->

<!-- delta:SF-2026-ARXIV-2603-24060:start -->新证据差异：RoboHarness 在 policy 外维护正负 dual memory，以 retrieval 提供相似经验，再用 causal attribution 选择 intervention，而不修改基础权重。<!-- delta:SF-2026-ARXIV-2603-24060:end -->

边界：只支持 arXiv:2603.24060v1 §III Methodology 的机制与 §IV-B Main Results 的公开 workload；§V CONCLUSIONS 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-24060:end -->
<!-- books-review:SF-2026-ARXIV-2603-24124:start -->
### The Alignment Tax: Response Homogenization in Aligned LLMs and Its Implications for Uncertainty Estimation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-24124:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章使用 `x` 表示 prompt，`y_w`、`y_l` 表示 preferred/chosen 与 dispreferred/rejected response，`r_phi(x,y)` 表示 Reward Model score，`pi_theta(y|x)` 表示当前 policy，`pi_ref(y|x)` 表示 reference policy，`beta` 表示 KL regularization strength。<!-- existing:SF-2026-ARXIV-2603-24124:end -->

<!-- delta:SF-2026-ARXIV-2603-24124:start -->新证据差异：论文通过 base→SFT→DPO stage ablation 分离 response homogenization，并比较 semantic clustering 与 token entropy；uncertainty owner 必须记录训练阶段和信号来源。<!-- delta:SF-2026-ARXIV-2603-24124:end -->

边界：只支持 arXiv:2603.24124v1 §4 Cascade Architecture 的机制与 §5 Experimental Validation 的公开 workload；§8.2 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-24124:end -->
<!-- books-review:SF-2026-ARXIV-2603-24203:start -->
### Invisible Threats from Model Context Protocol: Generating Stealthy Injection Payload via Tree-based Adaptive Search — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-24203:start -->已读 owner `books/part-07-agent/83-mcp.md` 与相邻章节。现有命题：`subscriptions/listen`、trace context、cache hints 与移入官方 extension 的 tasks 说明协议正在把长时交互、可观测性和缓存建议从隐式连接行为改写为显式契约。 Roots、Sampling、Logging 和 HTTP+SSE 则进入 feature lifecycle 的 deprecated 阶段。这里的“稳定”只描述 specification revision；它不表示 SDK/server fleet 已经同步迁移。官方 TypeScript SDK 迁移指南仍要求显式 opt-in，旧实现也可能继续 使用 2025-era handshake，因此生产部署必须按目标 SDK 与 server 的实际 revision 做 capability probe、兼容测试和分阶段迁移。<!-- existing:SF-2026-ARXIV-2603-24203:end -->

<!-- delta:SF-2026-ARXIV-2603-24203:start -->新证据差异：TIP 用 tree search 维护 payload 分支，结合 path feedback、tool-response simulation、defense-aware mutation 与 prune/early-stop，逐步寻找可执行且隐蔽的注入。<!-- delta:SF-2026-ARXIV-2603-24203:end -->

边界：只支持 arXiv:2603.24203v1 §IV-C Tree-Structured Optimization Architecture 的机制与 §VI-C Results and Analysis 的公开 workload；§VIII-B Limitations and Future Works 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-24203:end -->
<!-- books-review:SF-2026-ARXIV-2603-24564:start -->
### Infrastructure for Valuable, Tradable, and Verifiable Agent Memory — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-24564:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：模型架构中的 test-time neural memory 也不属于本章的 Agent Memory。前者在 forward 期间按 surprise/gradient 更新模型内部参数化 state，owner 是 sequence model，主要目标是压缩和利用 长输入；后者由平台跨调用持久化，必须具备 provenance、authorization、correction 与 deletion。 二者共享“write、retain、forget”的 `Principle Reuse`，但 truth authority 与生命周期不同。 第 22 章讨论 Titans/MIRAS 这类模型内部路线，本章只处理外部 durable state。<!-- existing:SF-2026-ARXIV-2603-24564:end -->

<!-- delta:SF-2026-ARXIV-2603-24564:start -->新证据差异：clawgang 将 memory 与可验证 computation provenance 绑定，meowtrade 再把认证 artifact 的 listing、transfer 与 governance 分层。<!-- delta:SF-2026-ARXIV-2603-24564:end -->

边界：只支持 arXiv:2603.24564v1 §2 ClawGang: an Infrastructure for Verifying Memory Value 的机制与 §4 Illustrative Use Cases 的公开 workload；§2.3 Security and Failure Modes 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-24564:end -->
<!-- books-review:SF-2026-ARXIV-2603-24582:start -->
### The Stochastic Gap: A Markovian Framework for Pre-Deployment Reliability and Oversight-Cost Auditing in Agentic Artificial Intelligence — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-24582:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：Refinement 只能重组已有 evidence，不能从缺失知识中创造可靠 procedure；失败还可能低于 no-Skill baseline。 Agentic Skills in the Wild 的作者结果支持这一分层，不支持固定模型排名或特定 registry size 的通用结论。<!-- existing:SF-2026-ARXIV-2603-24582:end -->

<!-- delta:SF-2026-ARXIV-2603-24582:start -->新证据差异：该框架用 Markov visitation measure 区分 state blind mass 与 state-action blind mass，并把 entropy escalation gate 映射为预期人工 oversight cost。<!-- delta:SF-2026-ARXIV-2603-24582:end -->

边界：只支持 arXiv:2603.24582v1 §4.1 Blind-spot mass over states and actions 的机制与 §5 Data, agent construction, and evaluation protocol 的公开 workload；§7 Discussion and limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-24582:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260326-COVERAGE | fresh-context:march-lane-c-reviewer | coverage | fresh-context-audit:lane-c | MAR26-FC-001/MAR26-FC-002/MAR26-FC-003 | pending: full-row fresh-context false-positive/false-negative replay; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260326-EVIDENCE | fresh-context:march-lane-c-reviewer | evidence | fresh-context-audit:lane-c;validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260326-SELECTION | fresh-context:march-lane-c-reviewer | deep_analysis_selection | fresh-context-audit:lane-c;validator:deep-analysis-selection-v1 | MAR26-FC-004 | pending: recompute after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260326-BOOKS | fresh-context:march-lane-c-reviewer | books | fresh-context-audit:lane-c;validator:books-comparison-v1 | MAR26-FC-004 | pending: recheck disposition after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260326/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 1 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 1 项 Books Integration：
- 更新并复核 `books/part-06-ai-infrastructure/69-trace.md`。
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
