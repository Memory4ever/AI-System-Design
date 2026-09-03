# Daily Research — 2026-03-30

**Research Date:** 2026-03-30

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-29 09:00:00 ～ 2026-03-30 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。2026-09-03 fresh-context 反证审计已重开；当前机器结构和既有 retained Review 仍可复用，但 denominator completeness 尚未按“不得抽样、逐项判断”合同重新验收。


## Executive Summary

> **2026-09-03 Semantic Reopen：** 旧 `Complete` 声明已被 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 取代。在 `MAR26-FC-001/MAR26-FC-002/MAR26-FC-003` 与 `MAR26-FC-004` 关闭前，本日报不得恢复 `Complete`；validator 通过只表示机器接口自洽。

严格窗口 raw/registered/screened=443/443/443；denominator=11、pre-denominator closures=432。exact-v1 Review complete=11、blocked=0；Integrate 建议=1。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-30 |
| Window End | 2026-03-30 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260330-AUTHOR-11 |
| Denominator Frozen At | 2026-09-02T16:07:11.473626+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-29T09:00:00+08:00 | 2026-03-30T09:00:00+08:00 | 2026-09-02T16:07:11.473626+08:00 | official-schedule recovery receipt + 443/443 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 443 | SF-2026-ARXIV-2603-25764;SF-2026-ARXIV-2603-25969;SF-2026-ARXIV-2603-25973;SF-2026-ARXIV-2603-25981;SF-2026-ARXIV-2603-26074;SF-2026-ARXIV-2603-26131;SF-2026-ARXIV-2603-26221;SF-2026-ARXIV-2603-26469;SF-2026-ARXIV-2603-26498;SF-2026-ARXIV-2603-26557;SF-2026-ARXIV-2603-26666 | pages=100; prefixes=00..99; final_cursor=end; registered=443; screened=443; retained=11; closure=432 | 2026-03-30T01:00:00+00:00 | screening-ledger-final.json#sha256=f694a68ca6f9667c7e139355b487e890df133d611b4600c746dcbb0079b35314; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260330:start -->作者侧已逐项筛选全部 443 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260330:end -->

### Fresh-context Audit

<!-- fresh-context-audit:lane-c:start -->
非作者审计已重放 443/443 条 title+abstract：作者 retained 7 项均保留，4 个 false-negative family 已完成 exact-v1 Source Review，6 个 recall challenge 被逐项驳回，0 个 withdrawn 只保留 identity/status；reconciled denominator 为 11；Books queue 中 6 个 `Integrate` 被降为 `No Change — Existing Coverage`，1 个 owner 已重绑。本审计已重建分母、Review 与 Books comparison，但不写 Books；Coverage/Evidence/Books Gate 继续保持 Open，等待 root final reconciliation。收据：`papers/2026/03/_sources/daily-20260330/fresh-context-audit-receipt.json`、`fresh-context-retained-evidence-audit.json`、`fresh-context-books-audit.json`。
<!-- fresh-context-audit:lane-c:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-25764 | arXiv:2603.25764v1 | paper-v1:2603.25764 | 2026-W14 | 2026-03-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25764 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25764 | no |
| SF-2026-ARXIV-2603-25969 | arXiv:2603.25969v1 | paper-v1:2603.25969 | 2026-W14 | 2026-03-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25969 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25969 | no |
| SF-2026-ARXIV-2603-25973 | arXiv:2603.25973v1 | paper-v1:2603.25973 | 2026-W14 | 2026-03-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25973 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25973 | no |
| SF-2026-ARXIV-2603-25981 | arXiv:2603.25981v1 | paper-v1:2603.25981 | 2026-W14 | 2026-03-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25981 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25981 | no |
| SF-2026-ARXIV-2603-26074 | arXiv:2603.26074v1 | paper-v1:2603.26074 | 2026-W14 | 2026-03-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-26074 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26074 | no |
| SF-2026-ARXIV-2603-26131 | arXiv:2603.26131v1 | paper-v1:2603.26131 | 2026-W14 | 2026-03-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-26131 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26131 | no |
| SF-2026-ARXIV-2603-26221 | arXiv:2603.26221v1 | paper-v1:2603.26221 | 2026-W14 | 2026-03-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-26221 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26221 | no |
| SF-2026-ARXIV-2603-26469 | arXiv:2603.26469v1 | paper-v1:2603.26469 | 2026-W14 | 2026-03-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-26469 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26469 | no |
| SF-2026-ARXIV-2603-26498 | arXiv:2603.26498v1 | paper-v1:2603.26498 | 2026-W14 | 2026-03-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-26498 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2603-26498 | no |
| SF-2026-ARXIV-2603-26557 | arXiv:2603.26557v1 | paper-v1:2603.26557 | 2026-W14 | 2026-03-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-26557 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26557 | no |
| SF-2026-ARXIV-2603-26666 | arXiv:2603.26666v1 | paper-v1:2603.26666 | 2026-W14 | 2026-03-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-26666 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26666 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-25764 | RP-5e8602a349d303d4 | standard | arXiv:2603.25764v1 | SRC-ARXIV@arXiv:2603.25764v1 | HTML — §Agent Framework. [facet=method]; https://arxiv.org/html/2603.25764v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25764v1.html; sha256:554ae39686e32e88f7877cd8b2ff4a402825aa0457da36706e76337930ccac2a | HTML — §LLM Agent Benchmarks. [facet=evaluation]; https://arxiv.org/html/2603.25764v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25764v1.html; sha256:554ae39686e32e88f7877cd8b2ff4a402825aa0457da36706e76337930ccac2a | HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.25764v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25764v1.html; sha256:554ae39686e32e88f7877cd8b2ff4a402825aa0457da36706e76337930ccac2a | arXiv exact-v1 identity https://arxiv.org/abs/2603.25764v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25764 | complete |
| SF-2026-ARXIV-2603-25969 | RP-7731dd5d3be70418 | standard | arXiv:2603.25969v1 | SRC-ARXIV@arXiv:2603.25969v1 | HTML — §II-A1 System Design [facet=method]; https://arxiv.org/html/2603.25969v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25969v1.html; sha256:2a1889cb0c59f35c713e50e03d31226e572cfe1a5d167e8044f74e43d146a380 | HTML — §V-D End-to-end Evaluation of a Firmware-Heavy Accelerator [facet=evaluation]; https://arxiv.org/html/2603.25969v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25969v1.html; sha256:2a1889cb0c59f35c713e50e03d31226e572cfe1a5d167e8044f74e43d146a380 | HTML — §VI Conclusion [facet=limitations]; https://arxiv.org/html/2603.25969v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25969v1.html; sha256:2a1889cb0c59f35c713e50e03d31226e572cfe1a5d167e8044f74e43d146a380 | arXiv exact-v1 identity https://arxiv.org/abs/2603.25969v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25969 | complete |
| SF-2026-ARXIV-2603-25973 | RP-52c9d5437417bc1c | standard | arXiv:2603.25973v1 | SRC-ARXIV@arXiv:2603.25973v1 | HTML — §2 Task Settings and Problem Formulation [facet=method]; https://arxiv.org/html/2603.25973v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25973v1.html; sha256:06e343a123fd5ab0b8d5791f8ef15ab2ba15cc3c8a46a56c789ee698ef9e978e | HTML — §4.3 Memory Methods Evaluation in Single-Domain [facet=evaluation]; https://arxiv.org/html/2603.25973v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25973v1.html; sha256:06e343a123fd5ab0b8d5791f8ef15ab2ba15cc3c8a46a56c789ee698ef9e978e | HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.25973v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25973v1.html; sha256:06e343a123fd5ab0b8d5791f8ef15ab2ba15cc3c8a46a56c789ee698ef9e978e | arXiv exact-v1 identity https://arxiv.org/abs/2603.25973v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25973 | complete |
| SF-2026-ARXIV-2603-25981 | RP-f40cc13918b0bb5e | standard | arXiv:2603.25981v1 | SRC-ARXIV@arXiv:2603.25981v1 | HTML — §3.4 Policy-Guided MPPI Planning [facet=method]; https://arxiv.org/html/2603.25981v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25981v1.html; sha256:742e69f1a2b60b7941ce39761b45e0db1521d81d080f08b05bd3a2ffa182270b | HTML — §4.2 Baselines and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.25981v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25981v1.html; sha256:742e69f1a2b60b7941ce39761b45e0db1521d81d080f08b05bd3a2ffa182270b | HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.25981v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25981v1.html; sha256:742e69f1a2b60b7941ce39761b45e0db1521d81d080f08b05bd3a2ffa182270b | arXiv exact-v1 identity https://arxiv.org/abs/2603.25981v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25981 | complete |
| SF-2026-ARXIV-2603-26074 | RP-184ecfbd174953ad | standard | arXiv:2603.26074v1 | SRC-ARXIV@arXiv:2603.26074v1 | HTML — §4.1 Design and Workflow of TRIP-RAG [facet=method]; https://arxiv.org/html/2603.26074v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26074v1.html; sha256:cbfc19e6475e3552ba74c57f5da8bd59ec49f490d02cbdec61f0935804422411 | HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.26074v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26074v1.html; sha256:cbfc19e6475e3552ba74c57f5da8bd59ec49f490d02cbdec61f0935804422411 | HTML — §7 Limitation [facet=limitations]; https://arxiv.org/html/2603.26074v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26074v1.html; sha256:cbfc19e6475e3552ba74c57f5da8bd59ec49f490d02cbdec61f0935804422411 | arXiv exact-v1 identity https://arxiv.org/abs/2603.26074v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-26074 | complete |
| SF-2026-ARXIV-2603-26131 | RP-8d2302074e76a3c2 | standard | arXiv:2603.26131v1 | SRC-ARXIV@arXiv:2603.26131v1 | HTML — §5. Evaluation Methodology [facet=method]; https://arxiv.org/html/2603.26131v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26131v1.html; sha256:c6b02d51d96b253c6ec2f9aa4dae3a63053ebc6470bb875905c6682884d4438a | HTML — §5. Evaluation Methodology [facet=evaluation]; https://arxiv.org/html/2603.26131v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26131v1.html; sha256:c6b02d51d96b253c6ec2f9aa4dae3a63053ebc6470bb875905c6682884d4438a | HTML — §4.2. Limitations of Prior Promotion-based Block-Level Compression [facet=limitations]; https://arxiv.org/html/2603.26131v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26131v1.html; sha256:c6b02d51d96b253c6ec2f9aa4dae3a63053ebc6470bb875905c6682884d4438a | arXiv exact-v1 identity https://arxiv.org/abs/2603.26131v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-26131 | complete |
| SF-2026-ARXIV-2603-26221 | RP-d07aaa2eff3d65a4 | standard | arXiv:2603.26221v1 | SRC-ARXIV@arXiv:2603.26221v1 | HTML — §3. Methodology [facet=method]; https://arxiv.org/html/2603.26221v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26221v1.html; sha256:2faf2e88a072c66ae7bbbd05cea563bae59266a9cdcc50efe92e13b33ad75130 | HTML — §5.3. Quantitative Gap Analysis [facet=evaluation]; https://arxiv.org/html/2603.26221v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26221v1.html; sha256:2faf2e88a072c66ae7bbbd05cea563bae59266a9cdcc50efe92e13b33ad75130 | HTML — §4.1. Failure Mode [facet=limitations]; https://arxiv.org/html/2603.26221v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26221v1.html; sha256:2faf2e88a072c66ae7bbbd05cea563bae59266a9cdcc50efe92e13b33ad75130 | arXiv exact-v1 identity https://arxiv.org/abs/2603.26221v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-26221 | complete |
| SF-2026-ARXIV-2603-26469 | RP-f2fc0ee52ca62c15 | standard | arXiv:2603.26469v1 | SRC-ARXIV@arXiv:2603.26469v1 | HTML — §II-B Simulation of Distributed Algorithms [facet=method]; https://arxiv.org/html/2603.26469v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26469v1.html; sha256:6d9dee5800578f9c3ab4cd9131282423a5d8f55c8031f2a5f3fae461f10a5f78 | HTML — §IV Results and Discussion [facet=evaluation]; https://arxiv.org/html/2603.26469v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26469v1.html; sha256:6d9dee5800578f9c3ab4cd9131282423a5d8f55c8031f2a5f3fae461f10a5f78 | HTML — §VI Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.26469v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26469v1.html; sha256:6d9dee5800578f9c3ab4cd9131282423a5d8f55c8031f2a5f3fae461f10a5f78 | arXiv exact-v1 identity https://arxiv.org/abs/2603.26469v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-26469 | complete |
| SF-2026-ARXIV-2603-26498 | RP-6a99294b76abf731 | deep | arXiv:2603.26498v1 | SRC-ARXIV@arXiv:2603.26498v1 | HTML — §3.1–§3.7 System Design [facet=method]; https://arxiv.org/html/2603.26498v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26498v1.html; sha256:e97a6d063de4657b5c42cc5f76b084843116406eb3042f373912a2fa18bdba3f | HTML — §4. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.26498v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26498v1.html; sha256:e97a6d063de4657b5c42cc5f76b084843116406eb3042f373912a2fa18bdba3f | HTML — §4.4. Discussion and Future Work [facet=limitations]; https://arxiv.org/html/2603.26498v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26498v1.html; sha256:e97a6d063de4657b5c42cc5f76b084843116406eb3042f373912a2fa18bdba3f | arXiv exact-v1 identity https://arxiv.org/abs/2603.26498v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-26498 | complete |
| SF-2026-ARXIV-2603-26557 | RP-a75a91364b7e3cdb | standard | arXiv:2603.26557v1 | SRC-ARXIV@arXiv:2603.26557v1 | HTML — §2.2 Overview of MemBoost [facet=method]; https://arxiv.org/html/2603.26557v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26557v1.html; sha256:e43c4875556d2053b2abbcf0095f8a02024b9ea2f8153d29294dc0d84aaa5a31 | HTML — §3.2 Results [facet=evaluation]; https://arxiv.org/html/2603.26557v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26557v1.html; sha256:e43c4875556d2053b2abbcf0095f8a02024b9ea2f8153d29294dc0d84aaa5a31 | HTML — §4 Conclusion [facet=limitations]; https://arxiv.org/html/2603.26557v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26557v1.html; sha256:e43c4875556d2053b2abbcf0095f8a02024b9ea2f8153d29294dc0d84aaa5a31 | arXiv exact-v1 identity https://arxiv.org/abs/2603.26557v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-26557 | complete |
| SF-2026-ARXIV-2603-26666 | RP-1fbbd4d378a09cfe | standard | arXiv:2603.26666v1 | SRC-ARXIV@arXiv:2603.26666v1 | HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.26666v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26666v1.html; sha256:63955025de73f8084fee550d85c99af3ef69ab523b73be40921d9ced9fad83f4 | HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.26666v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26666v1.html; sha256:63955025de73f8084fee550d85c99af3ef69ab523b73be40921d9ced9fad83f4 | HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.26666v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26666v1.html; sha256:63955025de73f8084fee550d85c99af3ef69ab523b73be40921d9ced9fad83f4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.26666v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-26666 | complete |

### Source Reviews

### Confident and Wrong: Silent Semantic Failures in Coding Agents

<!-- review:SF-2026-ARXIV-2603-25764:start -->
**问题**：coding agent 的 submit/completion rate 容易把主动提交当成功，重复给出同一错误 patch 甚至会伪装成稳定性。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：论文把 repeated-run submit、test-verified resolve、silent semantic failure 与应当 abstain 的 already-fixed probe 分离，使行动欲望不再拥有 correctness 真值。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `HTML — §Agent Framework. [facet=method]; https://arxiv.org/html/2603.25764v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25764v1.html; sha256:554ae39686e32e88f7877cd8b2ff4a402825aa0457da36706e76337930ccac2a`。

**Evaluation contract 与未证明部分**：1,750 条 SWE-bench Verified trajectory 支持所测模型存在稳定而不可见的语义失败；它不覆盖其他代码库、工具链或更强 verifier。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §LLM Agent Benchmarks. [facet=evaluation]; https://arxiv.org/html/2603.25764v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25764v1.html; sha256:554ae39686e32e88f7877cd8b2ff4a402825aa0457da36706e76337930ccac2a`。

**Trade-off / failure / coexistence**：重复验证和 abstention 指标提高可信度，却增加执行成本且仍受测试完备性限制；低风险草稿任务可保留 completion 作为运营指标，但不能作为 release gate。

<!-- claim:SF-2026-ARXIV-2603-25764:start -->**Claim Boundary**：只支持 arXiv:2603.25764v1 §Agent Framework. 的机制与 §LLM Agent Benchmarks. 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25764:end -->
<!-- review:SF-2026-ARXIV-2603-25764:end -->
### FireBridge: Cycle-Accurate Hardware + Firmware Co-Verification for Modern Accelerators

<!-- review:SF-2026-ARXIV-2603-25969:start -->
**问题**：现代 accelerator 的 hardware 与 firmware 并行演进，单侧仿真无法捕获 timing、register 和 recovery protocol 的跨层不一致。

**旧路径为何合理**：离线测试通过后人工发布最直观。

**约束变化与机制**：FireBridge 用 cycle-accurate hardware model 与真实 firmware 在同一 co-verification loop 中交换事件与状态，形成可重放接口契约。

**State / data / control owner**：`PLATFORM-PRODUCTION` 负责 evaluation evidence、release gate 与 rollback；定位证据为 `HTML — §II-A1 System Design [facet=method]; https://arxiv.org/html/2603.25969v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25969v1.html; sha256:2a1889cb0c59f35c713e50e03d31226e572cfe1a5d167e8044f74e43d146a380`。

**Evaluation contract 与未证明部分**：作者案例支持指定 accelerator block 的 bug detection 与 cycle fidelity；不能外推完整芯片、工艺或生产可靠性。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §V-D End-to-end Evaluation of a Firmware-Heavy Accelerator [facet=evaluation]; https://arxiv.org/html/2603.25969v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25969v1.html; sha256:2a1889cb0c59f35c713e50e03d31226e572cfe1a5d167e8044f74e43d146a380`。

**Trade-off / failure / coexistence**：联合验证提高覆盖却增加模型同步和仿真成本；接口稳定的小模块仍可分层测试。

<!-- claim:SF-2026-ARXIV-2603-25969:start -->**Claim Boundary**：只支持 arXiv:2603.25969v1 §II-A1 System Design 的机制与 §V-D End-to-end Evaluation of a Firmware-Heavy Accelerator 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25969:end -->
<!-- review:SF-2026-ARXIV-2603-25969:end -->
### MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization

<!-- review:SF-2026-ARXIV-2603-25973:start -->
**问题**：million-token context 并不等于 agent 会在多年、跨域历史中正确保留用户偏好，短对话合成 benchmark 难暴露 interference。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：MemoryCD 从真实长期行为构建跨域 memory source，并分开 rating、ranking、summary、generation 任务及 long-context/外部 memory 方法。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `HTML — §2 Task Settings and Problem Formulation [facet=method]; https://arxiv.org/html/2603.25973v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25973v1.html; sha256:06e343a123fd5ab0b8d5791f8ef15ab2ba15cc3c8a46a56c789ee698ef9e978e`。

**Evaluation contract 与未证明部分**：14 个模型和多种 memory method 的单域/跨域实验支持所测方法存在 transfer 与干扰差异；Amazon review 行为不是所有个性化场景的真值。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.3 Memory Methods Evaluation in Single-Domain [facet=evaluation]; https://arxiv.org/html/2603.25973v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25973v1.html; sha256:06e343a123fd5ab0b8d5791f8ef15ab2ba15cc3c8a46a56c789ee698ef9e978e`。

**Trade-off / failure / coexistence**：真实长程 benchmark 提高生态有效性，却继承选择偏差、时间泄漏和 judge 偏差；短会话 memory 仍需更窄、可控的单元测试。

<!-- claim:SF-2026-ARXIV-2603-25973:start -->**Claim Boundary**：只支持 arXiv:2603.25973v1 §2 Task Settings and Problem Formulation 的机制与 §4.3 Memory Methods Evaluation in Single-Domain 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25973:end -->
<!-- review:SF-2026-ARXIV-2603-25973:end -->
### Policy-Guided World Model Planning for Language-Conditioned Visual Navigation

<!-- review:SF-2026-ARXIV-2603-25981:start -->
**问题**：纯 reactive policy 缺少长 horizon 规划，纯 world-model search 又会在高维 action space 中从差初值开始浪费 rollout。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：PiJEPA 用训练后的 Octo policy 提供 action prior，再由 JEPA latent dynamics 与 MPPI 对候选轨迹打分；policy 负责 proposal，world model 负责可达性比较。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `HTML — §3.4 Policy-Guided MPPI Planning [facet=method]; https://arxiv.org/html/2603.25981v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25981v1.html; sha256:742e69f1a2b60b7941ce39761b45e0db1521d81d080f08b05bd3a2ffa182270b`。

**Evaluation contract 与未证明部分**：CAST navigation 上不同 encoder、baseline、位置/朝向与 latency 结果支持所测组合；不能证明 latent score 与真实环境因果完全一致。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.2 Baselines and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.25981v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.25981v1.html; sha256:742e69f1a2b60b7941ce39761b45e0db1521d81d080f08b05bd3a2ffa182270b`。

**Trade-off / failure / coexistence**：policy prior 降低搜索成本却继承 policy blind spot，world model 又可能误排 OOD action；短反应任务仍可直接 policy，强探索任务仍需更广 search。

<!-- claim:SF-2026-ARXIV-2603-25981:start -->**Claim Boundary**：只支持 arXiv:2603.25981v1 §3.4 Policy-Guided MPPI Planning 的机制与 §4.2 Baselines and Evaluation 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25981:end -->
<!-- review:SF-2026-ARXIV-2603-25981:end -->
### Not All Entities are Created Equal: A Dynamic Anonymization Framework for Privacy-Preserving RAG

<!-- review:SF-2026-ARXIV-2603-26074:start -->
**问题**：RAG 知识库若对所有敏感实体做同强度匿名化，会牺牲检索和回答 utility；只屏蔽显式 PII 又忽略上下文可重构风险。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：TRIP-RAG 先按上下文量化 entity risk，再动态选择 generalization level，并给出语义安全/不可重构分析；privacy policy 在 retrieval 前拥有变换与映射状态。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §4.1 Design and Workflow of TRIP-RAG [facet=method]; https://arxiv.org/html/2603.26074v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26074v1.html; sha256:cbfc19e6475e3552ba74c57f5da8bd59ec49f490d02cbdec61f0935804422411`。

**Evaluation contract 与未证明部分**：多数据集 utility、privacy attack 与 ablation 支持所测阈值的折中；形式证明依赖威胁模型，不能覆盖外部背景知识或所有 linkage attack。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.26074v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26074v1.html; sha256:cbfc19e6475e3552ba74c57f5da8bd59ec49f490d02cbdec61f0935804422411`。

**Trade-off / failure / coexistence**：动态匿名化保留更多 utility，却增加 risk estimator、mapping governance 与误分级；法规要求删除或极高风险字段仍应确定性移除。

<!-- claim:SF-2026-ARXIV-2603-26074:start -->**Claim Boundary**：只支持 arXiv:2603.26074v1 §4.1 Design and Workflow of TRIP-RAG 的机制与 §5.2 Main Results 的公开 workload；§7 Limitation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-26074:end -->
<!-- review:SF-2026-ARXIV-2603-26074:end -->
### IBEX: Internal Bandwidth-Efficient Compression Architecture for Scalable CXL Memory Expansion

<!-- review:SF-2026-ARXIV-2603-26131:start -->
**问题**：CXL memory expansion 增加容量却受 link bandwidth 限制，透明搬运原始 cache line 会让远端访问吞吐先耗尽。

**旧路径为何合理**：全部活跃状态驻留 GPU，访问路径最短。

**约束变化与机制**：IBEX 在扩展内存路径内压缩数据并协调 metadata、decode 与 consistency，使 bandwidth/latency 成为可控 memory-tier policy。

**State / data / control owner**：`INFER-GPU-MEMORY` 负责 HBM/DRAM 状态放置、迁移与预取；定位证据为 `HTML — §5. Evaluation Methodology [facet=method]; https://arxiv.org/html/2603.26131v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26131v1.html; sha256:c6b02d51d96b253c6ec2f9aa4dae3a63053ebc6470bb875905c6682884d4438a`。

**Evaluation contract 与未证明部分**：架构模拟或原型支持指定压缩率、workload 与 CXL 配置；不能证明所有模型 tensor 都可压缩且无尾延迟。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5. Evaluation Methodology [facet=evaluation]; https://arxiv.org/html/2603.26131v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26131v1.html; sha256:c6b02d51d96b253c6ec2f9aa4dae3a63053ebc6470bb875905c6682884d4438a`。

**Trade-off / failure / coexistence**：压缩节省带宽却增加 compute、metadata 和不可压缩回退；HBM/DRAM 足够时本地状态仍最简单。

<!-- claim:SF-2026-ARXIV-2603-26131:start -->**Claim Boundary**：只支持 arXiv:2603.26131v1 §5. Evaluation Methodology 的机制与 §5. Evaluation Methodology 的公开 workload；§4.2. Limitations of Prior Promotion-based Block-Level Compression 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-26131:end -->
<!-- review:SF-2026-ARXIV-2603-26131:end -->
### Clawed and Dangerous: Can We Trust Open Agentic Systems?

<!-- review:SF-2026-ARXIV-2603-26221:start -->
**问题**：开放 agent runtime 的 plan、tool result、memory 与 delegated authority 都是动态且概率性的，传统固定控制流威胁模型不够。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：该 SoK 用六维 taxonomy 汇总攻击、benchmark、defense、audit 与 operational governance，并把 capability revocation、persistent-memory integrity 纳入 secure-by-construction doctrine。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §3. Methodology [facet=method]; https://arxiv.org/html/2603.26221v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26221v1.html; sha256:2faf2e88a072c66ae7bbbd05cea563bae59266a9cdcc50efe92e13b33ad75130`。

**Evaluation contract 与未证明部分**：50 篇研究的系统化归纳支持缺口与设计清单；不能证明推荐控制已经在生产验证。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.3. Quantitative Gap Analysis [facet=evaluation]; https://arxiv.org/html/2603.26221v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26221v1.html; sha256:2faf2e88a072c66ae7bbbd05cea563bae59266a9cdcc50efe92e13b33ad75130`。

**Trade-off / failure / coexistence**：更完整 doctrine 增加运行时治理成本；封闭、无持久状态 agent 可采用较窄边界。

<!-- claim:SF-2026-ARXIV-2603-26221:start -->**Claim Boundary**：只支持 arXiv:2603.26221v1 §3. Methodology 的机制与 §5.3. Quantitative Gap Analysis 的公开 workload；§4.1. Failure Mode 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-26221:end -->
<!-- review:SF-2026-ARXIV-2603-26221:end -->
### UNIFERENCE: A Discrete Event Simulation Framework for Developing Distributed AI Models

<!-- review:SF-2026-ARXIV-2603-26469:start -->
**问题**：distributed inference 研究依赖 ad-hoc testbed，难在同一代码下复现异构 device/network 与假想拓扑。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：UNIFERENCE 用按 communication primitive 同步的 discrete-event logical process 保持因果顺序，并复用 PyTorch Distributed 代码从 simulation 切到 deployment。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `HTML — §II-B Simulation of Distributed Algorithms [facet=method]; https://arxiv.org/html/2603.26469v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26469v1.html; sha256:6d9dee5800578f9c3ab4cd9131282423a5d8f55c8031f2a5f3fae461f10a5f78`。

**Evaluation contract 与未证明部分**：多 backend/hardware 对比支持论文场景的 runtime fidelity；98.6% 不能外推未建模 contention、failure 或 kernel。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §IV Results and Discussion [facet=evaluation]; https://arxiv.org/html/2603.26469v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26469v1.html; sha256:6d9dee5800578f9c3ab4cd9131282423a5d8f55c8031f2a5f3fae461f10a5f78`。

**Trade-off / failure / coexistence**：仿真提高探索速度却依赖设备模型校准；最终 release 仍需真实集群验证。

<!-- claim:SF-2026-ARXIV-2603-26469:start -->**Claim Boundary**：只支持 arXiv:2603.26469v1 §II-B Simulation of Distributed Algorithms 的机制与 §IV Results and Discussion 的公开 workload；§VI Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-26469:end -->
<!-- review:SF-2026-ARXIV-2603-26469:end -->
### TCM-Serve: Modality-aware Scheduling for Multimodal Large Language Model Inference

<!-- review:SF-2026-ARXIV-2603-26498:start -->
**问题**：text-only scheduler 把 request cost 近似为 token 数，会让 video/image preprocessing 与 encoder 阶段造成严重 head-of-line blocking。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：TCM-Serve 建立 modality-aware resource abstraction，并在 preprocessing、encoding、prefill/decode 间按异质需求排序与并发，显式拥有阶段资源状态。

**State / data / control owner**：`INFER-SCHEDULING` 负责准入、批处理、优先级、路由和资源选择；定位证据为 `HTML — §3.1–§3.7 System Design [facet=method]; https://arxiv.org/html/2603.26498v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26498v1.html; sha256:e97a6d063de4657b5c42cc5f76b084843116406eb3042f373912a2fa18bdba3f`。

**Evaluation contract 与未证明部分**：多模态请求混合下的 latency/throughput 实验支持所测 scheduler；收益依赖视频长度、encoder、GPU 和 arrival distribution。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.26498v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26498v1.html; sha256:e97a6d063de4657b5c42cc5f76b084843116406eb3042f373912a2fa18bdba3f`。

**Trade-off / failure / coexistence**：精细分类减少大请求垄断，却增加预测误差、starvation 与跨阶段协调；同质文本 workload 仍可用现有 continuous batching。

<!-- claim:SF-2026-ARXIV-2603-26498:start -->**Claim Boundary**：只支持 arXiv:2603.26498v1 §3.1–§3.7 System Design 的机制与 §4.1–§4.4 的公开 workload；§4.4 Discussion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-26498:end -->
<!-- review:SF-2026-ARXIV-2603-26498:end -->
### MemBoost: A Memory-Boosted Framework for Cost-Aware LLM Inference

<!-- review:SF-2026-ARXIV-2603-26557:start -->
**问题**：每次重复或近重复问题都调用强模型，能保持简单语义，却在跨用户会话中重复支付同一推理成本。

**旧路径为何合理**：把一次请求视为同质前向路径，接口最简单。

**约束变化与机制**：MemBoost 把历史 answer 与supporting information 组织为可更新 memory，轻模型先判断复用/回答，困难或低置信 query 才升级强模型。

**State / data / control owner**：`INFER-REQUEST-LIFECYCLE` 负责 请求阶段、状态身份、路由与成本归属；定位证据为 `HTML — §2.2 Overview of MemBoost [facet=method]; https://arxiv.org/html/2603.26557v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26557v1.html; sha256:e43c4875556d2053b2abbcf0095f8a02024b9ea2f8153d29294dc0d84aaa5a31`。

**Evaluation contract 与未证明部分**：交互 workload 的成本与质量实验支持所测 escalation policy；历史答案正确性、隐私和 drift 依赖数据与 verifier，不能把 cache hit 当真值。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §3.2 Results [facet=evaluation]; https://arxiv.org/html/2603.26557v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26557v1.html; sha256:e43c4875556d2053b2abbcf0095f8a02024b9ea2f8153d29294dc0d84aaa5a31`。

**Trade-off / failure / coexistence**：复用降低成本，却引入 stale answer、跨租户泄漏和错误自强化；高新鲜度或高风险 query 应绕过 memory 并重新 grounding。

<!-- claim:SF-2026-ARXIV-2603-26557:start -->**Claim Boundary**：只支持 arXiv:2603.26557v1 §2.2 Overview of MemBoost 的机制与 §3.2 Results 的公开 workload；§4 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-26557:end -->
<!-- review:SF-2026-ARXIV-2603-26557:end -->
### VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation

<!-- review:SF-2026-ARXIV-2603-26666:start -->
**问题**：offline VLA SFT 样本高效但遭遇 deployment distribution shift，纯 online RL 又受 sparse reward 与 rollout 成本限制。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：VLA-OPD 在当前 policy rollout 上用 expert action 形成 dense distillation target，把 on-policy state coverage 与监督更新结合，而非等待稀疏终局奖励。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.26666v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26666v1.html; sha256:63955025de73f8084fee550d85c99af3ef69ab523b73be40921d9ced9fad83f4`。

**Evaluation contract 与未证明部分**：机器人 manipulation 实验支持所测任务的 sample efficiency 与 capability retention；expert quality、sim/real 环境和安全覆盖限制外推。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.26666v1; papers/2026/03/_sources/daily-20260330/exact-v1-bodies/2603.26666v1.html; sha256:63955025de73f8084fee550d85c99af3ef69ab523b73be40921d9ced9fad83f4`。

**Trade-off / failure / coexistence**：on-policy distillation 改善状态匹配，却需要可靠 expert 并可能复制其偏差；有密集真实 reward 时 RL、分布稳定时 offline SFT 仍更直接。

<!-- claim:SF-2026-ARXIV-2603-26666:start -->**Claim Boundary**：只支持 arXiv:2603.26666v1 §3 Methodology 的机制与 §4 Experiments 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-26666:end -->
<!-- review:SF-2026-ARXIV-2603-26666:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-26498 | score_7_9;potential_books_delta | selected | DA-20260330-09 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260330-09 |

<!-- analysis:DA-20260330-09:start -->
### TCM-Serve: Modality-aware Scheduling for Multimodal Large Language Model Inference

text-only scheduler 把 request cost 近似为 token 数，会让 video/image preprocessing 与 encoder 阶段造成严重 head-of-line blocking。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：TCM-Serve 建立 modality-aware resource abstraction，并在 preprocessing、encoding、prefill/decode 间按异质需求排序与并发，显式拥有阶段资源状态。 其公开验证边界为：多模态请求混合下的 latency/throughput 实验支持所测 scheduler；收益依赖视频长度、encoder、GPU 和 arrival distribution。 新增代价与回退条件为：精细分类减少大请求垄断，却增加预测误差、starvation 与跨阶段协调；同质文本 workload 仍可用现有 continuous batching。
<!-- analysis:DA-20260330-09:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-25764 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#http-成功只是质量判断的第一道门 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25764 | delta:SF-2026-ARXIV-2603-25764 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25764 |
| SF-2026-ARXIV-2603-25969 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/72-security.md#canonical-action-与-effect-time-authorization (section Ch-adjacent); books/part-07-agent/74-prompt.md#第74章-prompt (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25969 | delta:SF-2026-ARXIV-2603-25969 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25969 |
| SF-2026-ARXIV-2603-25973 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#retrieval-object-需要-validity-与-lifecycle (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25973 | delta:SF-2026-ARXIV-2603-25973 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25973 |
| SF-2026-ARXIV-2603-25981 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#latency-与-control-frequency (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25981 | delta:SF-2026-ARXIV-2603-25981 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25981 |
| SF-2026-ARXIV-2603-26074 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#runtime-优化统计也可能成为跨租户共享状态 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-26074 | delta:SF-2026-ARXIV-2603-26074 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26074 |
| SF-2026-ARXIV-2603-26131 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#从-memory-hierarchy-开始 (section Ch-owner) | books/part-05-inference-system/53-kserve-llm.md#第53章-llm-serving-声明式拓扑：以-kserve-为例 (section Ch-adjacent); books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-26131 | delta:SF-2026-ARXIV-2603-26131 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26131 |
| SF-2026-ARXIV-2603-26221 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#conversation-continuation-必须先验证-grounding-state (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-26221 | delta:SF-2026-ARXIV-2603-26221 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26221 |
| SF-2026-ARXIV-2603-26469 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-26469 | delta:SF-2026-ARXIV-2603-26469 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26469 |
| SF-2026-ARXIV-2603-26498 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-26498 | delta:SF-2026-ARXIV-2603-26498 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-26498 |
| SF-2026-ARXIV-2603-26557 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/41-deepspeed.md#第41章-训练状态-runtime-policy：以-deepspeed-为例 (section Ch-adjacent); books/part-05-inference-system/43-prefill.md#第43章-prefill (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-26557 | delta:SF-2026-ARXIV-2603-26557 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26557 |
| SF-2026-ARXIV-2603-26666 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#fleet-学习必须把部署、干预与再部署组成版本循环 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#open-loop-imagination-vs-closed-loop-correction (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-26666 | delta:SF-2026-ARXIV-2603-26666 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26666 |

<!-- books-review:SF-2026-ARXIV-2603-25764:start -->
### Confident and Wrong: Silent Semantic Failures in Coding Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25764:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：第 67 章可以持续观察 transport/runtime errors 和已产出的质量信号趋势；本章负责定义 semantic success 的口径、样本与决策边界。两者共享 request、model、prompt、retriever、tool 与 environment identity，但不能用可观测性代替规范性判断。<!-- existing:SF-2026-ARXIV-2603-25764:end -->

<!-- delta:SF-2026-ARXIV-2603-25764:start -->新证据差异：论文把 repeated-run submit、test-verified resolve、silent semantic failure 与应当 abstain 的 already-fixed probe 分离，使行动欲望不再拥有 correctness 真值。<!-- delta:SF-2026-ARXIV-2603-25764:end -->

边界：只支持 arXiv:2603.25764v1 §Agent Framework. 的机制与 §LLM Agent Benchmarks. 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25764:end -->
<!-- books-review:SF-2026-ARXIV-2603-25969:start -->
### FireBridge: Cycle-Accurate Hardware + Firmware Co-Verification for Modern Accelerators — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25969:start -->已读 owner `books/part-06-ai-infrastructure/73-production-best-practice.md` 与相邻章节。现有命题：本章的核心判断是：**生产化不是在功能完成后追加监控与安全，而是让 artifact、deployment、SLO、evidence、cost、tenancy、security 和 recovery 从设计时就共享同一身份与控制闭环。**<!-- existing:SF-2026-ARXIV-2603-25969:end -->

<!-- delta:SF-2026-ARXIV-2603-25969:start -->新证据差异：FireBridge 用 cycle-accurate hardware model 与真实 firmware 在同一 co-verification loop 中交换事件与状态，形成可重放接口契约。<!-- delta:SF-2026-ARXIV-2603-25969:end -->

边界：只支持 arXiv:2603.25969v1 §II-A1 System Design 的机制与 §V-D End-to-end Evaluation of a Firmware-Heavy Accelerator 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25969:end -->
<!-- books-review:SF-2026-ARXIV-2603-25973:start -->
### MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25973:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-25973:end -->

<!-- delta:SF-2026-ARXIV-2603-25973:start -->新证据差异：MemoryCD 从真实长期行为构建跨域 memory source，并分开 rating、ranking、summary、generation 任务及 long-context/外部 memory 方法。<!-- delta:SF-2026-ARXIV-2603-25973:end -->

边界：只支持 arXiv:2603.25973v1 §2 Task Settings and Problem Formulation 的机制与 §4.3 Memory Methods Evaluation in Single-Domain 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25973:end -->
<!-- books-review:SF-2026-ARXIV-2603-25981:start -->
### Policy-Guided World Model Planning for Language-Conditioned Visual Navigation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25981:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：一个模型能生成逼真视频，是否已经“理解世界”？能够预测下一帧，是否足以支持 planning？World Model 与 simulator、Agent Memory 有何边界？模型在内部 imagined rollout 时，谁保存事实状态，谁保存预测状态，又怎样在新 observation 到来后修正？<!-- existing:SF-2026-ARXIV-2603-25981:end -->

<!-- delta:SF-2026-ARXIV-2603-25981:start -->新证据差异：PiJEPA 用训练后的 Octo policy 提供 action prior，再由 JEPA latent dynamics 与 MPPI 对候选轨迹打分；policy 负责 proposal，world model 负责可达性比较。<!-- delta:SF-2026-ARXIV-2603-25981:end -->

边界：只支持 arXiv:2603.25981v1 §3.4 Policy-Guided MPPI Planning 的机制与 §4.2 Baselines and Evaluation 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25981:end -->
<!-- books-review:SF-2026-ARXIV-2603-26074:start -->
### Not All Entities are Created Equal: A Dynamic Anonymization Framework for Privacy-Preserving RAG — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-26074:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Per-tensor dynamic activation quantization 在单租户 batch 中根据当前输入计算共享 `min/max` 或 scale，可以比固定 scale 更贴合分布；当 batch 混合不同 tenant 时，同一统计却同时读取 victim 输入并改变 adversary 的 quantized logits，形成一条不经过显式 cache 的跨租户 side channel。于是量化 identity 不只包含 bit width 和 kernel，还必须包含 scale granularity、batch composition 与 tenant boundary。<!-- existing:SF-2026-ARXIV-2603-26074:end -->

<!-- delta:SF-2026-ARXIV-2603-26074:start -->新证据差异：TRIP-RAG 先按上下文量化 entity risk，再动态选择 generalization level，并给出语义安全/不可重构分析；privacy policy 在 retrieval 前拥有变换与映射状态。<!-- delta:SF-2026-ARXIV-2603-26074:end -->

边界：只支持 arXiv:2603.26074v1 §4.1 Design and Workflow of TRIP-RAG 的机制与 §5.2 Main Results 的公开 workload；§7 Limitation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-26074:end -->
<!-- books-review:SF-2026-ARXIV-2603-26131:start -->
### IBEX: Internal Bandwidth-Efficient Compression Architecture for Scalable CXL Memory Expansion — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-26131:start -->已读 owner `books/part-05-inference-system/54-gpu-memory.md` 与相邻章节。现有命题：这解释了为什么很多优化并不是减少数学运算，而是减少 HBM 读写，或者把数据尽可能留在片上 memory 中。FlashAttention 的核心价值就在这里。<!-- existing:SF-2026-ARXIV-2603-26131:end -->

<!-- delta:SF-2026-ARXIV-2603-26131:start -->新证据差异：IBEX 在扩展内存路径内压缩数据并协调 metadata、decode 与 consistency，使 bandwidth/latency 成为可控 memory-tier policy。<!-- delta:SF-2026-ARXIV-2603-26131:end -->

边界：只支持 arXiv:2603.26131v1 §5. Evaluation Methodology 的机制与 §5. Evaluation Methodology 的公开 workload；§4.2. Limitations of Prior Promotion-based Block-Level Compression 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-26131:end -->
<!-- books-review:SF-2026-ARXIV-2603-26221:start -->
### Clawed and Dangerous: Can We Trust Open Agentic Systems? — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-26221:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：形式证明的强度来自假设，而不是数学符号本身。Bounded active domain、identifier-renaming equivariance、有限 tool semantics 与可枚举 transition 一旦被 schema evolution、外部副作用、概率 policy 或无限对象打破，证明便不覆盖真实 系统。Formal Verification of Agentic Systems 提供这一受限分支的理论证据，不证明任意 LLM Agent 可验证；trace、 simulation、canary 与 incident evidence 因而继续存在。<!-- existing:SF-2026-ARXIV-2603-26221:end -->

<!-- delta:SF-2026-ARXIV-2603-26221:start -->新证据差异：该 SoK 用六维 taxonomy 汇总攻击、benchmark、defense、audit 与 operational governance，并把 capability revocation、persistent-memory integrity 纳入 secure-by-construction doctrine。<!-- delta:SF-2026-ARXIV-2603-26221:end -->

边界：只支持 arXiv:2603.26221v1 §3. Methodology 的机制与 §5.3. Quantitative Gap Analysis 的公开 workload；§4.1. Failure Mode 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-26221:end -->
<!-- books-review:SF-2026-ARXIV-2603-26469:start -->
### UNIFERENCE: A Discrete Event Simulation Framework for Developing Distributed AI Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-26469:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-26469:end -->

<!-- delta:SF-2026-ARXIV-2603-26469:start -->新证据差异：UNIFERENCE 用按 communication primitive 同步的 discrete-event logical process 保持因果顺序，并复用 PyTorch Distributed 代码从 simulation 切到 deployment。<!-- delta:SF-2026-ARXIV-2603-26469:end -->

边界：只支持 arXiv:2603.26469v1 §II-B Simulation of Distributed Algorithms 的机制与 §IV Results and Discussion 的公开 workload；§VI Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-26469:end -->
<!-- books-review:SF-2026-ARXIV-2603-26498:start -->
### TCM-Serve: Modality-aware Scheduling for Multimodal Large Language Model Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-26498:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2603-26498:end -->

<!-- delta:SF-2026-ARXIV-2603-26498:start -->新证据差异：TCM-Serve 建立 modality-aware resource abstraction，并在 preprocessing、encoding、prefill/decode 间按异质需求排序与并发，显式拥有阶段资源状态。<!-- delta:SF-2026-ARXIV-2603-26498:end -->

边界：只支持 arXiv:2603.26498v1 §3.1–§3.7 System Design 的机制与 §4.1–§4.4 的公开 workload；§4.4 Discussion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **Integrate**；正文已写回，当前等待非作者 post-write semantic audit。
<!-- books-review:SF-2026-ARXIV-2603-26498:end -->
<!-- books-review:SF-2026-ARXIV-2603-26557:start -->
### MemBoost: A Memory-Boosted Framework for Cost-Aware LLM Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-26557:start -->已读 owner `books/part-05-inference-system/42-what-happens-during-inference.md` 与相邻章节。现有命题：本章的核心判断是：**LLM inference 是一个持续演化的 token-generation process，而不是一次无状态函数调用。**请求会依次经历输入处理、admission、Prefill、Decode、streaming 和完成清理；每一步都在改变 token progress、KV ownership、GPU memory 与调度资格。<!-- existing:SF-2026-ARXIV-2603-26557:end -->

<!-- delta:SF-2026-ARXIV-2603-26557:start -->新证据差异：MemBoost 把历史 answer 与supporting information 组织为可更新 memory，轻模型先判断复用/回答，困难或低置信 query 才升级强模型。<!-- delta:SF-2026-ARXIV-2603-26557:end -->

边界：只支持 arXiv:2603.26557v1 §2.2 Overview of MemBoost 的机制与 §3.2 Results 的公开 workload；§4 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-26557:end -->
<!-- books-review:SF-2026-ARXIV-2603-26666:start -->
### VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-26666:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：deployment owner 持有生效 revision，teleoperation/intervention service 持有接管事实，training run 只产生 candidate policy，controller 与 safety monitor 仍拥有动作提交和 veto。该循环获得更贴近失败前沿的数据，却引入 on-policy exploration risk、选择偏差、版本碎片和旧能力退化；干预稀疏、奖励不可信或物理 blast radius 无法隔离时，应停在离线更新、simulation/shadow evaluation 和人工审批，不把“来自真实 fleet”误写成安全证明。<!-- existing:SF-2026-ARXIV-2603-26666:end -->

<!-- delta:SF-2026-ARXIV-2603-26666:start -->新证据差异：VLA-OPD 在当前 policy rollout 上用 expert action 形成 dense distillation target，把 on-policy state coverage 与监督更新结合，而非等待稀疏终局奖励。<!-- delta:SF-2026-ARXIV-2603-26666:end -->

边界：只支持 arXiv:2603.26666v1 §3 Methodology 的机制与 §4 Experiments 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-26666:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260330-COVERAGE | fresh-context:march-lane-c-reviewer | coverage | fresh-context-audit:lane-c | MAR26-FC-001/MAR26-FC-002/MAR26-FC-003 | pending: full-row fresh-context false-positive/false-negative replay; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260330-EVIDENCE | fresh-context:march-lane-c-reviewer | evidence | fresh-context-audit:lane-c;validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260330-SELECTION | fresh-context:march-lane-c-reviewer | deep_analysis_selection | fresh-context-audit:lane-c;validator:deep-analysis-selection-v1 | MAR26-FC-004 | pending: recompute after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260330-BOOKS | fresh-context:march-lane-c-reviewer | books | fresh-context-audit:lane-c;validator:books-comparison-v1 | MAR26-FC-004 | pending: recheck disposition after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260330/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 1 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 1 项 Books Integration：
- 更新并复核 `books/part-05-inference-system/56-inference-scheduling.md`。
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
