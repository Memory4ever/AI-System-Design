# Daily Research — 2026-02-21

**Research Date:** 2026-02-21

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-02-20 09:00:00 ～ 2026-02-21 09:00:00（Asia/Shanghai，左闭右开）

**Contract:** V2.1 Historical Daily independent Full Replay；既有 Weekly 未参与 discovery、分母、评分、Review、Books 判断或漏项校准；Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；全月 fresh-context 四域语义审计已通过（`papers/2026/02/_sources/february-fresh-context-audit.json`），本日 unresolved findings=0。

## Executive Summary

窗口 raw identities=481，title+abstract semantic screening=481/481；Candidate Denominator=6，pre-denominator closures=475。exact-v1 Review=6/6，withdrawn=0，blocked=0；Books Integrate=1。

本日报以官方 arXiv 公告时刻映射北京时间半开窗口；DataCite 只恢复 identity 与 registry timestamp，不把 Submitted:v1、DOI created 或后续 revision 误当作报告归属。withdrawn family 只保留在 pre-denominator closure，不进入候选、评分、Review 或 Books。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-02-21 |
| Window End | 2026-02-21 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | sha256:dd05f82b78933cbb7ac054be23207bcf6c50d9527af150b1a65cfeb25dbf4491 |
| Denominator Frozen At | 2026-09-03T07:01:18Z |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-02-20T09:00:00+08:00 | 2026-02-21T09:00:00+08:00 | 2026-09-03T07:01:18Z | DataCite identity recovery + official arXiv announcement schedule + registered-category full title/abstract screen + exact-v1 HTML/PDF | checked | 6 | SF-2026-ARXIV-2602-16873; SF-2026-ARXIV-2602-17345; SF-2026-ARXIV-2602-16760; SF-2026-ARXIV-2602-16943; SF-2026-ARXIV-2602-17038; SF-2026-ARXIV-2602-17046 | pages=100; DOI prefixes=00..99; final_cursor=end; screened=481 | 2026-02-21T09:00:00+08:00 | papers/2026/02/_sources/daily-20260221/coverage-receipt.json; papers/2026/02/_sources/daily-20260221/screening-ledger-final.json; coverage:SRC-ARXIV:20260221 | — |

<!-- coverage:SRC-ARXIV:20260221:start -->481 个注册身份均已按 title+abstract 逐项筛选；475 个具体拒绝理由保存在 ledger。当前注册表的其他来源在 2026-08-25 才生效，不反推为 2 月 Required。全月 receipt 已完成 false-positive / false-negative、日期归属与撤稿审计，本日 Coverage Gate=Closed。<!-- coverage:SRC-ARXIV:20260221:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-16873 | arXiv:2602.16873v1 | paper-v1:2602.16873 | 2026-W08 | 2026-02-20 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-16873 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-16873 | no |
| SF-2026-ARXIV-2602-17345 | arXiv:2602.17345v1 | paper-v1:2602.17345 | 2026-W08 | 2026-02-20 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-17345 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-17345 | no |
| SF-2026-ARXIV-2602-16760 | arXiv:2602.16760v1 | paper-v1:2602.16760 | 2026-W08 | 2026-02-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-16760 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-16760 | no |
| SF-2026-ARXIV-2602-16943 | arXiv:2602.16943v1 | paper-v1:2602.16943 | 2026-W08 | 2026-02-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-16943 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-16943 | no |
| SF-2026-ARXIV-2602-17038 | arXiv:2602.17038v1 | paper-v1:2602.17038 | 2026-W08 | 2026-02-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2602-17038 | self | — | new_in_window | MODEL-MOE | Integrate | books-review:SF-2026-ARXIV-2602-17038 | no |
| SF-2026-ARXIV-2602-17046 | arXiv:2602.17046v1 | paper-v1:2602.17046 | 2026-W08 | 2026-02-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-17046 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-17046 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-16873 | RP-8008199acde87a56 | deep | arXiv:2602.16873v1 | SRC-ARXIV@arXiv:2602.16873v1 | arXiv:2602.16873v1 HTML — §4 The AdaptOrch Framework [facet=method]; https://arxiv.org/html/2602.16873v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.16873v1.html; sha256:fb55934a5f0a42d863c6ffb8efd3b0378ed01845aaef5f852480693e2ea80721 | arXiv:2602.16873v1 HTML — §5.2 Results [facet=evaluation]; https://arxiv.org/html/2602.16873v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.16873v1.html; sha256:fb55934a5f0a42d863c6ffb8efd3b0378ed01845aaef5f852480693e2ea80721 | arXiv:2602.16873v1 HTML — §6.4 Limitations [facet=limitations]; https://arxiv.org/html/2602.16873v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.16873v1.html; sha256:fb55934a5f0a42d863c6ffb8efd3b0378ed01845aaef5f852480693e2ea80721 | External link observed in exact-v1 body: https://github.com/adaptorch/adaptorch; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-16873 | complete |
| SF-2026-ARXIV-2602-17345 | RP-fc8e4b092f9d16c6 | deep | arXiv:2602.17345v1 | SRC-ARXIV@arXiv:2602.17345v1 | arXiv:2602.17345v1 HTML — §2.2 A Minimal Architecture of Embodied AI [facet=method]; https://arxiv.org/html/2602.17345v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.17345v1.html; sha256:58c8311f79aef03eb7650bfbb5da5cafd2fbc7a39862bcbeb151c9330bd0046b | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2602.17345v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.17345v1.html; sha256:58c8311f79aef03eb7650bfbb5da5cafd2fbc7a39862bcbeb151c9330bd0046b | arXiv:2602.17345v1 HTML — §6.2.2 Three Failure Modes: Vulnerabilities at the Execution Layer [facet=limitations]; https://arxiv.org/html/2602.17345v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.17345v1.html; sha256:58c8311f79aef03eb7650bfbb5da5cafd2fbc7a39862bcbeb151c9330bd0046b | Not Disclosed — arXiv:2602.17345v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-17345 | complete |
| SF-2026-ARXIV-2602-16760 | RP-b382366c6e177994 | deep | arXiv:2602.16760v1 | SRC-ARXIV@arXiv:2602.16760v1 | arXiv:2602.16760v1 HTML — §3 System Architecture [facet=method]; https://arxiv.org/html/2602.16760v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.16760v1.html; sha256:d0892539bcdc065badd8f696d7a7b02f700fe75a2a9e02dd6afb5e3b307346db | arXiv:2602.16760v1 HTML — §6.2 Performance Results [facet=evaluation]; https://arxiv.org/html/2602.16760v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.16760v1.html; sha256:d0892539bcdc065badd8f696d7a7b02f700fe75a2a9e02dd6afb5e3b307346db | arXiv:2602.16760v1 HTML — §8.3 Limitations [facet=limitations]; https://arxiv.org/html/2602.16760v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.16760v1.html; sha256:d0892539bcdc065badd8f696d7a7b02f700fe75a2a9e02dd6afb5e3b307346db | External link observed in exact-v1 body: https://github.com/coder903/split-inference; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-16760 | complete |
| SF-2026-ARXIV-2602-16943 | RP-0e1f389a43762b84 | deep | arXiv:2602.16943v1 | SRC-ARXIV@arXiv:2602.16943v1 | arXiv:2602.16943v1 HTML — §3.1 Benchmark Design [facet=method]; https://arxiv.org/html/2602.16943v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.16943v1.html; sha256:7bc1d69991c97b23f823ec8e1f026b505ebc06d6a9bea4bca6beedf600a67a5d | arXiv:2602.16943v1 HTML — §5.2 Implications for Safety Evaluation [facet=evaluation]; https://arxiv.org/html/2602.16943v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.16943v1.html; sha256:7bc1d69991c97b23f823ec8e1f026b505ebc06d6a9bea4bca6beedf600a67a5d | arXiv:2602.16943v1 HTML — §6 Threats to Validity [facet=limitations]; https://arxiv.org/html/2602.16943v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.16943v1.html; sha256:7bc1d69991c97b23f823ec8e1f026b505ebc06d6a9bea4bca6beedf600a67a5d | External link observed in exact-v1 body: https://github.com/acartag7/edictum; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-16943 | complete |
| SF-2026-ARXIV-2602-17038 | RP-b2d686bb4612bf18 | deep | arXiv:2602.17038v1 | SRC-ARXIV@arXiv:2602.17038v1 | arXiv:2602.17038v1 HTML — §Method [facet=method]; https://arxiv.org/html/2602.17038v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.17038v1.html; sha256:1d79b414f420cc139e3f3003d1b2a347119b5ce22da2f81099ee42c61887e837 | arXiv:2602.17038v1 HTML — §Main Results [facet=evaluation]; https://arxiv.org/html/2602.17038v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.17038v1.html; sha256:1d79b414f420cc139e3f3003d1b2a347119b5ce22da2f81099ee42c61887e837 | arXiv:2602.17038v1 HTML — §Appendix G Failure Analysis [facet=limitations]; https://arxiv.org/html/2602.17038v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.17038v1.html; sha256:1d79b414f420cc139e3f3003d1b2a347119b5ce22da2f81099ee42c61887e837 | Not Disclosed — arXiv:2602.17038v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-17038 | complete |
| SF-2026-ARXIV-2602-17046 | RP-dcb815fd46cdd5c1 | deep | arXiv:2602.17046v1 | SRC-ARXIV@arXiv:2602.17046v1 | arXiv:2602.17046v1 HTML — §3.5 System Architecture [facet=method]; https://arxiv.org/html/2602.17046v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.17046v1.html; sha256:36588e3e74e34de758d3168b38e86fd5751944b46d1555a649c09d2908eb6cd8 | arXiv:2602.17046v1 HTML — §5.3 Internal Consistency Validation [facet=evaluation]; https://arxiv.org/html/2602.17046v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.17046v1.html; sha256:36588e3e74e34de758d3168b38e86fd5751944b46d1555a649c09d2908eb6cd8 | arXiv:2602.17046v1 HTML — §8 Limitations and Threats to Validity [facet=limitations]; https://arxiv.org/html/2602.17046v1; papers/2026/02/_sources/daily-20260221/exact-v1-bodies/2602.17046v1.html; sha256:36588e3e74e34de758d3168b38e86fd5751944b46d1555a649c09d2908eb6cd8 | External link observed in exact-v1 body: https://github.com/uriafranko/ITR; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-17046 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2602-16873:start -->
### AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence

- **Review route:** `deep`；Primary=`arXiv:2602.16873v1`；owner=`AGENT-MULTI-AGENT`。

- **问题与旧路径：** `AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence` 是否在 `AGENT-MULTI-AGENT` 中改变已有状态、数据或控制责任；旧路径仍成立于：单 agent 保持单一上下文与控制流，最易归因。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.16873v1 HTML — §4 The AdaptOrch Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 拓扑、消息、共享状态、路由与停止条件。触发约束是：任务分解、异构能力与并行协作引入通信、共享状态和信用分配问题。

- **State / data / control owner：** `AGENT-MULTI-AGENT` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/adaptorch/adaptorch; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.16873v1 HTML — §5.2 Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.16873v1 HTML — §6.4 Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：任务规模小或共享状态成本高时单 agent 仍更稳健。

<!-- claim:SF-2026-ARXIV-2602-16873:start -->
- **Claim boundary:** 只支持 arXiv:2602.16873v1 实际披露的机制与实验。方法定位为 arXiv:2602.16873v1 HTML — §4 The AdaptOrch Framework；验证定位为 arXiv:2602.16873v1 HTML — §5.2 Results；边界定位为 arXiv:2602.16873v1 HTML — §6.4 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-16873:end -->
<!-- review:SF-2026-ARXIV-2602-16873:end -->

<!-- review:SF-2026-ARXIV-2602-17345:start -->
### What Breaks Embodied AI Security:LLM Vulnerabilities, CPS Flaws,or Something Else?

- **Review route:** `deep`；Primary=`arXiv:2602.17345v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `What Breaks Embodied AI Security:LLM Vulnerabilities, CPS Flaws,or Something Else?` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.17345v1 HTML — §2.2 A Minimal Architecture of Embodied AI` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.17345v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** exact-v1 未披露可独立定位的 evaluation（`Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节`）；因此不声称经验收益。已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.17345v1 HTML — §6.2.2 Three Failure Modes: Vulnerabilities at the Execution Layer`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-17345:start -->
- **Claim boundary:** 只支持 arXiv:2602.17345v1 实际披露的机制与实验。方法定位为 arXiv:2602.17345v1 HTML — §2.2 A Minimal Architecture of Embodied AI；evaluation facet 未独立披露，不声称经验收益；边界定位为 arXiv:2602.17345v1 HTML — §6.2.2 Three Failure Modes: Vulnerabilities at the Execution Layer。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-17345:end -->
<!-- review:SF-2026-ARXIV-2602-17345:end -->

<!-- review:SF-2026-ARXIV-2602-16760:start -->
### Privacy-Aware Split Inference with Speculative Decoding for Large Language Models over Wide-Area Networks

- **Review route:** `deep`；Primary=`arXiv:2602.16760v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `Privacy-Aware Split Inference with Speculative Decoding for Large Language Models over Wide-Area Networks` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.16760v1 HTML — §3 System Architecture` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/coder903/split-inference; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.16760v1 HTML — §6.2 Performance Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.16760v1 HTML — §8.3 Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-16760:start -->
- **Claim boundary:** 只支持 arXiv:2602.16760v1 实际披露的机制与实验。方法定位为 arXiv:2602.16760v1 HTML — §3 System Architecture；验证定位为 arXiv:2602.16760v1 HTML — §6.2 Performance Results；边界定位为 arXiv:2602.16760v1 HTML — §8.3 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-16760:end -->
<!-- review:SF-2026-ARXIV-2602-16760:end -->

<!-- review:SF-2026-ARXIV-2602-16943:start -->
### Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents

- **Review route:** `deep`；Primary=`arXiv:2602.16943v1`；owner=`PLATFORM-SECURITY`。

- **问题与旧路径：** `Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents` 是否在 `PLATFORM-SECURITY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.16943v1 HTML — §3.1 Benchmark Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。

- **State / data / control owner：** `PLATFORM-SECURITY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/acartag7/edictum; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.16943v1 HTML — §5.2 Implications for Safety Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.16943v1 HTML — §6 Threats to Validity`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2602-16943:start -->
- **Claim boundary:** 只支持 arXiv:2602.16943v1 实际披露的机制与实验。方法定位为 arXiv:2602.16943v1 HTML — §3.1 Benchmark Design；验证定位为 arXiv:2602.16943v1 HTML — §5.2 Implications for Safety Evaluation；边界定位为 arXiv:2602.16943v1 HTML — §6 Threats to Validity。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-16943:end -->
<!-- review:SF-2026-ARXIV-2602-16943:end -->

<!-- review:SF-2026-ARXIV-2602-17038:start -->
### Phase-Aware Mixture of Experts for Agentic Reinforcement Learning

- **Review route:** `deep`；Primary=`arXiv:2602.17038v1`；owner=`MODEL-MOE`。

- **问题与旧路径：** `Phase-Aware Mixture of Experts for Agentic Reinforcement Learning` 是否在 `MODEL-MOE` 中改变已有状态、数据或控制责任；旧路径仍成立于：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.17038v1 HTML — §Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 expert 选择、capacity、placement 与通信。触发约束是：容量扩大后，激活成本和通信使全参数计算不可持续。

- **State / data / control owner：** `MODEL-MOE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.17038v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.17038v1 HTML — §Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.17038v1 HTML — §Appendix G Failure Analysis`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：规模较小、负载难预测或通信昂贵时 dense 仍可能占优。

<!-- claim:SF-2026-ARXIV-2602-17038:start -->
- **Claim boundary:** 只支持 arXiv:2602.17038v1 实际披露的机制与实验。方法定位为 arXiv:2602.17038v1 HTML — §Method；验证定位为 arXiv:2602.17038v1 HTML — §Main Results；边界定位为 arXiv:2602.17038v1 HTML — §Appendix G Failure Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-17038:end -->
<!-- review:SF-2026-ARXIV-2602-17038:end -->

<!-- review:SF-2026-ARXIV-2602-17046:start -->
### Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs

- **Review route:** `deep`；Primary=`arXiv:2602.17046v1`；owner=`AGENT-TOOL-CALLING`。

- **问题与旧路径：** `Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs` 是否在 `AGENT-TOOL-CALLING` 中改变已有状态、数据或控制责任；旧路径仍成立于：固定函数表与一次调用在短任务中边界清楚。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.17046v1 HTML — §3.5 System Architecture` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 工具 capability、参数验证、调用结果与授权边界。触发约束是：动态工具、长链错误和不可信描述要求把 capability、参数与结果身份显式化。

- **State / data / control owner：** `AGENT-TOOL-CALLING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/uriafranko/ITR; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.17046v1 HTML — §5.3 Internal Consistency Validation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.17046v1 HTML — §8 Limitations and Threats to Validity`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：固定工具集、单一信任域仍适合简单函数调用。

<!-- claim:SF-2026-ARXIV-2602-17046:start -->
- **Claim boundary:** 只支持 arXiv:2602.17046v1 实际披露的机制与实验。方法定位为 arXiv:2602.17046v1 HTML — §3.5 System Architecture；验证定位为 arXiv:2602.17046v1 HTML — §5.3 Internal Consistency Validation；边界定位为 arXiv:2602.17046v1 HTML — §8 Limitations and Threats to Validity。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-17046:end -->
<!-- review:SF-2026-ARXIV-2602-17046:end -->

## 4. Benchmark Contracts

None — 作者实验只在各 Source Review 的 evaluation contract 内支持机制判断；本日报不发布可跨 workload 外推的 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-16873 | score_7_9 | selected | DA-20260221-1 | — | 在同日 eligibility frontier 中优先选择 Total=8 且形成独立 `AGENT-MULTI-AGENT` 系统责任链的 family。 | analysis:DA-20260221-1 |
| SF-2026-ARXIV-2602-17345 | score_7_9 | selected | DA-20260221-2 | — | 在同日 eligibility frontier 中优先选择 Total=8 且形成独立 `PLATFORM-SECURITY` 系统责任链的 family。 | analysis:DA-20260221-2 |
| SF-2026-ARXIV-2602-16760 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-16760 |
| SF-2026-ARXIV-2602-16943 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-SECURITY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-16943 |
| SF-2026-ARXIV-2602-17038 | score_7_9; forced_review; potential_books_delta | selected | DA-20260221-3 | — | 在同日 eligibility frontier 中优先选择 Total=7 且形成独立 `MODEL-MOE` 系统责任链的 family。 | analysis:DA-20260221-3 |
| SF-2026-ARXIV-2602-17046 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `AGENT-TOOL-CALLING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-17046 |

<!-- analysis:DA-20260221-1:start -->
### DA-20260221-1 — AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `AGENT-MULTI-AGENT`。exact-v1 的 `arXiv:2602.16873v1 HTML — §4 The AdaptOrch Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 拓扑、消息、共享状态、路由与停止条件。触发约束是：任务分解、异构能力与并行协作引入通信、共享状态和信用分配问题。 公开验证定位在 `arXiv:2602.16873v1 HTML — §5.2 Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：限制或反证定位在 `arXiv:2602.16873v1 HTML — §6.4 Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：任务规模小或共享状态成本高时单 agent 仍更稳健。
<!-- analysis:DA-20260221-1:end -->

<!-- analysis:DA-20260221-2:start -->
### DA-20260221-2 — What Breaks Embodied AI Security:LLM Vulnerabilities, CPS Flaws,or Something Else?

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `PLATFORM-SECURITY`。exact-v1 的 `arXiv:2602.17345v1 HTML — §2.2 A Minimal Architecture of Embodied AI` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 exact-v1 未披露可独立定位的 evaluation（`Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节`）；因此不声称经验收益。已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：限制或反证定位在 `arXiv:2602.17345v1 HTML — §6.2.2 Three Failure Modes: Vulnerabilities at the Execution Layer`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：无工具、无持久状态的只读场景仍可采用较薄边界。
<!-- analysis:DA-20260221-2:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-16760:start -->
`Privacy-Aware Split Inference with Speculative Decoding for Large Language Models over Wide-Area Networks` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-16760:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-16943:start -->
`Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-16943:end -->

<!-- analysis:DA-20260221-3:start -->
### DA-20260221-3 — Phase-Aware Mixture of Experts for Agentic Reinforcement Learning

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `MODEL-MOE`。exact-v1 的 `arXiv:2602.17038v1 HTML — §Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 expert 选择、capacity、placement 与通信。触发约束是：容量扩大后，激活成本和通信使全参数计算不可持续。 公开验证定位在 `arXiv:2602.17038v1 HTML — §Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：限制或反证定位在 `arXiv:2602.17038v1 HTML — §Appendix G Failure Analysis`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：规模较小、负载难预测或通信昂贵时 dense 仍可能占优。
<!-- analysis:DA-20260221-3:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-17046:start -->
`Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-17046:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-16873 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#topology-从部署前选择演进到运行时有界修复 (line 150) | books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10); books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-16873 | delta:SF-2026-ARXIV-2602-16873 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-16873 |
| SF-2026-ARXIV-2602-17345 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1106) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-17345 | delta:SF-2026-ARXIV-2602-17345 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-17345 |
| SF-2026-ARXIV-2602-16760 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1149) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-16760 | delta:SF-2026-ARXIV-2602-16760 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-16760 |
| SF-2026-ARXIV-2602-16943 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#从文本是否恶意到谁获得了行为控制权 (line 299) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-16943 | delta:SF-2026-ARXIV-2602-16943 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-16943 |
| SF-2026-ARXIV-2602-17038 | MODEL-MOE | books/part-02-model/21-moe.md#moe-与模型专家化的边界 (line 501) | books/part-02-model/20-sampling.md#本章要回答的问题 (line 10); books/part-02-model/22-long-context.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-17038 | delta:SF-2026-ARXIV-2602-17038 | Principle Reuse | Integrate | books-review:SF-2026-ARXIV-2602-17038 |
| SF-2026-ARXIV-2602-17046 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#tool-discovery-与选择 (line 82) | books/part-07-agent/77-memory.md#本章要回答的问题 (line 10); books/part-07-agent/79-planning.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-17046 | delta:SF-2026-ARXIV-2602-17046 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-17046 |

<!-- existing:SF-2026-ARXIV-2602-16873:start -->
已对读当前 owner `AGENT-MULTI-AGENT` 在 `books/part-07-agent/82-multi-agent.md#topology-从部署前选择演进到运行时有界修复 (line 150)` 的命题：## Topology 从部署前选择演进到运行时有界修复
<!-- existing:SF-2026-ARXIV-2602-16873:end -->

<!-- delta:SF-2026-ARXIV-2602-16873:start -->
exact-v1 的 `arXiv:2602.16873v1 HTML — §4 The AdaptOrch Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 拓扑、消息、共享状态、路由与停止条件。触发约束是：任务分解、异构能力与并行协作引入通信、共享状态和信用分配问题。
<!-- delta:SF-2026-ARXIV-2602-16873:end -->

<!-- books-review:SF-2026-ARXIV-2602-16873:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10); books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.16873v1 实际披露的机制与实验。方法定位为 arXiv:2602.16873v1 HTML — §4 The AdaptOrch Framework；验证定位为 arXiv:2602.16873v1 HTML — §5.2 Results；边界定位为 arXiv:2602.16873v1 HTML — §6.4 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-16873:end -->

<!-- existing:SF-2026-ARXIV-2602-17345:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1106)` 的命题：### Agent authority BOM、channel coverage 与 executable PoV
<!-- existing:SF-2026-ARXIV-2602-17345:end -->

<!-- delta:SF-2026-ARXIV-2602-17345:start -->
exact-v1 的 `arXiv:2602.17345v1 HTML — §2.2 A Minimal Architecture of Embodied AI` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-17345:end -->

<!-- books-review:SF-2026-ARXIV-2602-17345:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.17345v1 实际披露的机制与实验。方法定位为 arXiv:2602.17345v1 HTML — §2.2 A Minimal Architecture of Embodied AI；evaluation facet 未独立披露，不声称经验收益；边界定位为 arXiv:2602.17345v1 HTML — §6.2.2 Three Failure Modes: Vulnerabilities at the Execution Layer。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-17345:end -->

<!-- existing:SF-2026-ARXIV-2602-16760:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1149)` 的命题：### 从输入窗口到中间激活与权重：Observer State 决定隐私边界
<!-- existing:SF-2026-ARXIV-2602-16760:end -->

<!-- delta:SF-2026-ARXIV-2602-16760:start -->
exact-v1 的 `arXiv:2602.16760v1 HTML — §3 System Architecture` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-16760:end -->

<!-- books-review:SF-2026-ARXIV-2602-16760:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.16760v1 实际披露的机制与实验。方法定位为 arXiv:2602.16760v1 HTML — §3 System Architecture；验证定位为 arXiv:2602.16760v1 HTML — §6.2 Performance Results；边界定位为 arXiv:2602.16760v1 HTML — §8.3 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-16760:end -->

<!-- existing:SF-2026-ARXIV-2602-16943:start -->
已对读当前 owner `PLATFORM-SECURITY` 在 `books/part-06-ai-infrastructure/72-security.md#从文本是否恶意到谁获得了行为控制权 (line 299)` 的命题：## 从“文本是否恶意”到“谁获得了行为控制权”
<!-- existing:SF-2026-ARXIV-2602-16943:end -->

<!-- delta:SF-2026-ARXIV-2602-16943:start -->
exact-v1 的 `arXiv:2602.16943v1 HTML — §3.1 Benchmark Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 身份、授权、数据流、策略执行点与审计证据。触发约束是：工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。
<!-- delta:SF-2026-ARXIV-2602-16943:end -->

<!-- books-review:SF-2026-ARXIV-2602-16943:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.16943v1 实际披露的机制与实验。方法定位为 arXiv:2602.16943v1 HTML — §3.1 Benchmark Design；验证定位为 arXiv:2602.16943v1 HTML — §5.2 Implications for Safety Evaluation；边界定位为 arXiv:2602.16943v1 HTML — §6 Threats to Validity。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-16943:end -->

<!-- existing:SF-2026-ARXIV-2602-17038:start -->
已对读当前 owner `MODEL-MOE` 在 `books/part-02-model/21-moe.md#moe-与模型专家化的边界 (line 501)` 的命题：## MoE 与模型“专家化”的边界
<!-- existing:SF-2026-ARXIV-2602-17038:end -->

<!-- delta:SF-2026-ARXIV-2602-17038:start -->
exact-v1 的 `arXiv:2602.17038v1 HTML — §Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 expert 选择、capacity、placement 与通信。触发约束是：容量扩大后，激活成本和通信使全参数计算不可持续。
<!-- delta:SF-2026-ARXIV-2602-17038:end -->

<!-- books-review:SF-2026-ARXIV-2602-17038:start -->
Decision=`Integrate`：现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。 相邻章节已定位为 `books/part-02-model/20-sampling.md#本章要回答的问题 (line 10); books/part-02-model/22-long-context.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.17038v1 实际披露的机制与实验。方法定位为 arXiv:2602.17038v1 HTML — §Method；验证定位为 arXiv:2602.17038v1 HTML — §Main Results；边界定位为 arXiv:2602.17038v1 HTML — §Appendix G Failure Analysis。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-17038:end -->

<!-- existing:SF-2026-ARXIV-2602-17046:start -->
已对读当前 owner `AGENT-TOOL-CALLING` 在 `books/part-07-agent/78-tool-calling.md#tool-discovery-与选择 (line 82)` 的命题：## Tool Discovery 与选择
<!-- existing:SF-2026-ARXIV-2602-17046:end -->

<!-- delta:SF-2026-ARXIV-2602-17046:start -->
exact-v1 的 `arXiv:2602.17046v1 HTML — §3.5 System Architecture` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 工具 capability、参数验证、调用结果与授权边界。触发约束是：动态工具、长链错误和不可信描述要求把 capability、参数与结果身份显式化。
<!-- delta:SF-2026-ARXIV-2602-17046:end -->

<!-- books-review:SF-2026-ARXIV-2602-17046:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-07-agent/77-memory.md#本章要回答的问题 (line 10); books/part-07-agent/79-planning.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.17046v1 实际披露的机制与实验。方法定位为 arXiv:2602.17046v1 HTML — §3.5 System Architecture；验证定位为 arXiv:2602.17046v1 HTML — §5.3 Internal Consistency Validation；边界定位为 arXiv:2602.17046v1 HTML — §8 Limitations and Threats to Validity。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-17046:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
<!-- audit-receipt:FCSA-2026-02-FINAL:20260221:start -->
全月验收：`papers/2026/02/_sources/february-fresh-context-audit.json`；本日受审收据：`papers/2026/02/_sources/daily-20260221/screening-ledger-author.json`、`papers/2026/02/_sources/daily-20260221/screening-ledger-final.json`、`papers/2026/02/_sources/daily-20260221/exact-v1-review-packet.json`、`papers/2026/02/_sources/daily-20260221/books-current-content-comparison.json`、`papers/2026/02/_sources/daily-20260221/BOOKS_WRITEBACK_QUEUE.json`。
<!-- audit-receipt:FCSA-2026-02-FINAL:20260221:end -->

| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260221-COVERAGE-FINAL | fresh-context:february-independent-reviewer | coverage | coverage:SRC-ARXIV:20260221; audit-receipt:FCSA-2026-02-FINAL:20260221 | — | 本日 raw=481、retained=6、closures=475；全月 FP/FN、日期与撤稿 finding 均已解决 | passed |
| SA-20260221-EVIDENCE-FINAL | fresh-context:february-independent-reviewer | evidence | review:SF-2026-ARXIV-2602-16873; review:SF-2026-ARXIV-2602-17345; review:SF-2026-ARXIV-2602-16760; review:SF-2026-ARXIV-2602-16943; review:SF-2026-ARXIV-2602-17038; review:SF-2026-ARXIV-2602-17046; audit-receipt:FCSA-2026-02-FINAL:20260221 | — | exact-v1 complete=6、blocked=0；locator、excerpt、RP 与 claim boundary 已验收 | passed |
| SA-20260221-SELECTION-FINAL | fresh-context:february-independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1; audit-receipt:FCSA-2026-02-FINAL:20260221 | — | 本日完整 eligibility frontier 与最多三个叙事单元已验收，未选择项均保留显式理由 | passed |
| SA-20260221-BOOKS-POSTWRITE-FINAL | fresh-context:february-independent-reviewer | books | books-review:SF-2026-ARXIV-2602-16873; books-review:SF-2026-ARXIV-2602-17345; books-review:SF-2026-ARXIV-2602-16760; books-review:SF-2026-ARXIV-2602-16943; books-review:SF-2026-ARXIV-2602-17038; books-review:SF-2026-ARXIV-2602-17046; audit-receipt:FCSA-2026-02-FINAL:20260221 | — | 本日 Integrate=1；canonical owner、相邻命题、disposition 与 post-write/no-writeback 状态已验收 | passed |

## 8. Ignored Noise

475 个 pre-denominator closure 保存在 `papers/2026/02/_sources/daily-20260221/screening-ledger-final.json`；每项含 identity、title、abstract 与 family-specific reason。withdrawn=0，撤稿不留 selected 痕迹。

## 9. Recommended Action

本日四域 Gate 已关闭；保留 `papers/2026/02/_sources/february-fresh-context-audit.json` 与本地冻结收据。仅在 primary evidence、撤稿状态或公共合同变化时重新打开对应 scope。

## 10. Repository Changes

- promotion 更新 `papers/2026/02/21/README.md` 与本日 `_sources` 最终状态收据。
- 本步骤不修改 Books 或 Weekly，也不 stage、commit 或 push；此前已验收的 Books 写回由本日 queue 记录 post-write 状态。

## 11. Open Questions

- 无 Gate 阻塞项；论文自身未证明的边界继续保留在 Claim Boundary 中，不构成未解决流程 finding。

## 12. Sources

- [arXiv:2602.16873v1](https://arxiv.org/abs/2602.16873v1) — official exact-v1；first-public `2026-02-20T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.17345v1](https://arxiv.org/abs/2602.17345v1) — official exact-v1；first-public `2026-02-20T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.16760v1](https://arxiv.org/abs/2602.16760v1) — official exact-v1；first-public `2026-02-20T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.16943v1](https://arxiv.org/abs/2602.16943v1) — official exact-v1；first-public `2026-02-20T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.17038v1](https://arxiv.org/abs/2602.17038v1) — official exact-v1；first-public `2026-02-20T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.17046v1](https://arxiv.org/abs/2602.17046v1) — official exact-v1；first-public `2026-02-20T09:00:00+08:00`；访问日期 2026-09-02。

## 13. Final Status

Completion Status=`Complete`；Coverage=`Closed`；Evidence=`Passed`；Books=`Passed`；Unresolved Findings=0。最终 raw=481、retained=6、closures=475、exact-v1 reviews=6、blocked=0。
