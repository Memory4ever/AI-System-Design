# Daily Research — 2026-02-05

**Research Date:** 2026-02-05

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-02-04 09:00:00 ～ 2026-02-05 09:00:00（Asia/Shanghai，左闭右开）

**Contract:** V2.1 Historical Daily independent Full Replay；既有 Weekly 未参与 discovery、分母、评分、Review、Books 判断或漏项校准；Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；全月 fresh-context 四域语义审计已通过（`papers/2026/02/_sources/february-fresh-context-audit.json`），本日 unresolved findings=0。

## Executive Summary

窗口 raw identities=795，title+abstract semantic screening=795/795；Candidate Denominator=24，pre-denominator closures=771。exact-v1 Review=24/24，withdrawn=0，blocked=0；Books Integrate=2。

本日报以官方 arXiv 公告时刻映射北京时间半开窗口；DataCite 只恢复 identity 与 registry timestamp，不把 Submitted:v1、DOI created 或后续 revision 误当作报告归属。withdrawn family 只保留在 pre-denominator closure，不进入候选、评分、Review 或 Books。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-02-05 |
| Window End | 2026-02-05 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | sha256:d575f55d8c4fdb87e291bd92ff0ba70994dc798062f4f9bf4d4a03526baa0269 |
| Denominator Frozen At | 2026-09-03T07:01:18Z |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-02-04T09:00:00+08:00 | 2026-02-05T09:00:00+08:00 | 2026-09-03T07:01:18Z | DataCite identity recovery + official arXiv announcement schedule + registered-category full title/abstract screen + exact-v1 HTML/PDF | checked | 24 | SF-2026-ARXIV-2602-02579; SF-2026-ARXIV-2602-02599; SF-2026-ARXIV-2602-02958; SF-2026-ARXIV-2602-03036; SF-2026-ARXIV-2602-03184; SF-2026-ARXIV-2602-03295; SF-2026-ARXIV-2602-03560; SF-2026-ARXIV-2602-02499; SF-2026-ARXIV-2602-02515; SF-2026-ARXIV-2602-02574; SF-2026-ARXIV-2602-02585; SF-2026-ARXIV-2602-02987; SF-2026-ARXIV-2602-03025; SF-2026-ARXIV-2602-03128; SF-2026-ARXIV-2602-03203; SF-2026-ARXIV-2602-03255; SF-2026-ARXIV-2602-03338; SF-2026-ARXIV-2602-03495; SF-2026-ARXIV-2602-03580; SF-2026-ARXIV-2602-03632; SF-2026-ARXIV-2602-03719; SF-2026-ARXIV-2602-03782; SF-2026-ARXIV-2602-02589; SF-2026-ARXIV-2602-02690 | pages=100; DOI prefixes=00..99; final_cursor=end; screened=795 | 2026-02-05T09:00:00+08:00 | papers/2026/02/_sources/daily-20260205/coverage-receipt.json; papers/2026/02/_sources/daily-20260205/screening-ledger-final.json; coverage:SRC-ARXIV:20260205 | — |

<!-- coverage:SRC-ARXIV:20260205:start -->795 个注册身份均已按 title+abstract 逐项筛选；771 个具体拒绝理由保存在 ledger。当前注册表的其他来源在 2026-08-25 才生效，不反推为 2 月 Required。全月 receipt 已完成 false-positive / false-negative、日期归属与撤稿审计，本日 Coverage Gate=Closed。<!-- coverage:SRC-ARXIV:20260205:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-02579 | arXiv:2602.02579v1 | paper-v1:2602.02579 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-02579 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02579 | no |
| SF-2026-ARXIV-2602-02599 | arXiv:2602.02599v1 | paper-v1:2602.02599 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-02599 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02599 | no |
| SF-2026-ARXIV-2602-02958 | arXiv:2602.02958v1 | paper-v1:2602.02958 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-02958 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02958 | no |
| SF-2026-ARXIV-2602-03036 | arXiv:2602.03036v1 | paper-v1:2602.03036 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03036 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03036 | no |
| SF-2026-ARXIV-2602-03184 | arXiv:2602.03184v1 | paper-v1:2602.03184 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03184 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03184 | no |
| SF-2026-ARXIV-2602-03295 | arXiv:2602.03295v1 | paper-v1:2602.03295 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2602-03295 | self | — | new_in_window | INFER-PREFILL | Integrate | books-review:SF-2026-ARXIV-2602-03295 | no |
| SF-2026-ARXIV-2602-03560 | arXiv:2602.03560v1 | paper-v1:2602.03560 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03560 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03560 | no |
| SF-2026-ARXIV-2602-02499 | arXiv:2602.02499v1 | paper-v1:2602.02499 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-02499 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02499 | no |
| SF-2026-ARXIV-2602-02515 | arXiv:2602.02515v1 | paper-v1:2602.02515 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-02515 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02515 | no |
| SF-2026-ARXIV-2602-02574 | arXiv:2602.02574v1 | paper-v1:2602.02574 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-02574 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02574 | no |
| SF-2026-ARXIV-2602-02585 | arXiv:2602.02585v1 | paper-v1:2602.02585 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-02585 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02585 | no |
| SF-2026-ARXIV-2602-02987 | arXiv:2602.02987v1 | paper-v1:2602.02987 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-02987 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02987 | no |
| SF-2026-ARXIV-2602-03025 | arXiv:2602.03025v1 | paper-v1:2602.03025 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03025 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03025 | no |
| SF-2026-ARXIV-2602-03128 | arXiv:2602.03128v1 | paper-v1:2602.03128 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03128 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03128 | no |
| SF-2026-ARXIV-2602-03203 | arXiv:2602.03203v1 | paper-v1:2602.03203 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03203 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03203 | no |
| SF-2026-ARXIV-2602-03255 | arXiv:2602.03255v1 | paper-v1:2602.03255 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03255 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03255 | no |
| SF-2026-ARXIV-2602-03338 | arXiv:2602.03338v1 | paper-v1:2602.03338 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2602-03338 | self | — | new_in_window | AGENT-REFLECTION | Integrate | books-review:SF-2026-ARXIV-2602-03338 | no |
| SF-2026-ARXIV-2602-03495 | arXiv:2602.03495v1 | paper-v1:2602.03495 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03495 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03495 | no |
| SF-2026-ARXIV-2602-03580 | arXiv:2602.03580v1 | paper-v1:2602.03580 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03580 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03580 | no |
| SF-2026-ARXIV-2602-03632 | arXiv:2602.03632v1 | paper-v1:2602.03632 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03632 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03632 | no |
| SF-2026-ARXIV-2602-03719 | arXiv:2602.03719v1 | paper-v1:2602.03719 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03719 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03719 | no |
| SF-2026-ARXIV-2602-03782 | arXiv:2602.03782v1 | paper-v1:2602.03782 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2602-03782 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03782 | no |
| SF-2026-ARXIV-2602-02589 | arXiv:2602.02589v1 | paper-v1:2602.02589 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2602-02589 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02589 | no |
| SF-2026-ARXIV-2602-02690 | arXiv:2602.02690v1 | paper-v1:2602.02690 | 2026-W06 | 2026-02-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2602-02690 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02690 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-02579 | RP-5b8d725897e5b9c9 | deep | arXiv:2602.02579v1 | SRC-ARXIV@arXiv:2602.02579v1 | arXiv:2602.02579v1 HTML — §3.1 Illustrating the Failure of Existing Methods [facet=method]; https://arxiv.org/html/2602.02579v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02579v1.html; sha256:f28add66a60856e5255aaf47f521e8f0f60fb04985f0a5a9d7732f235cca163f | arXiv:2602.02579v1 HTML — §5.2 Accuracy Evaluation [facet=evaluation]; https://arxiv.org/html/2602.02579v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02579v1.html; sha256:f28add66a60856e5255aaf47f521e8f0f60fb04985f0a5a9d7732f235cca163f | arXiv:2602.02579v1 HTML — §3.1 Illustrating the Failure of Existing Methods [facet=limitations]; https://arxiv.org/html/2602.02579v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02579v1.html; sha256:f28add66a60856e5255aaf47f521e8f0f60fb04985f0a5a9d7732f235cca163f | Not Disclosed — arXiv:2602.02579v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-02579 | complete |
| SF-2026-ARXIV-2602-02599 | RP-a9b91e4714cbac4b | deep | arXiv:2602.02599v1 | SRC-ARXIV@arXiv:2602.02599v1 | arXiv:2602.02599v1 HTML — §4 RAP: RoPE-Aligned Pruning [facet=method]; https://arxiv.org/html/2602.02599v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02599v1.html; sha256:b5e9810442094d6b112399d997798e4a183cc317321777bb5d1897beff223cc0 | arXiv:2602.02599v1 HTML — §Appendix D Complete Experimental Results [facet=evaluation]; https://arxiv.org/html/2602.02599v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02599v1.html; sha256:b5e9810442094d6b112399d997798e4a183cc317321777bb5d1897beff223cc0 | arXiv:2602.02599v1 HTML — §6.3 Ablation Study [facet=limitations]; https://arxiv.org/html/2602.02599v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02599v1.html; sha256:b5e9810442094d6b112399d997798e4a183cc317321777bb5d1897beff223cc0 | External link observed in exact-v1 body: https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-02599 | complete |
| SF-2026-ARXIV-2602-02958 | RP-a81e45f9966b8a2f | deep | arXiv:2602.02958v1 | SRC-ARXIV@arXiv:2602.02958v1 | arXiv:2602.02958v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2602.02958v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02958v1.html; sha256:0c7c4f6ad8114afd6d10f82059de93a494998871eaec083f0667f649605cdc32 | arXiv:2602.02958v1 HTML — §5.2 Quality Evaluation [facet=evaluation]; https://arxiv.org/html/2602.02958v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02958v1.html; sha256:0c7c4f6ad8114afd6d10f82059de93a494998871eaec083f0667f649605cdc32 | arXiv:2602.02958v1 HTML — §5.4 Sensitivity Test [facet=limitations]; https://arxiv.org/html/2602.02958v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02958v1.html; sha256:0c7c4f6ad8114afd6d10f82059de93a494998871eaec083f0667f649605cdc32 | External link observed in exact-v1 body: https://github.com/guandeh17/Self-Forcing/blob/main/prompts/MovieGenVideoBench_extended.txt; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-02958 | complete |
| SF-2026-ARXIV-2602-03036 | RP-2ffde298a88156f6 | deep | arXiv:2602.03036v1 | SRC-ARXIV@arXiv:2602.03036v1 | arXiv:2602.03036v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2602.03036v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03036v1.html; sha256:6354c40122badd58cc1dace2c3aabb5178d95e55d7882a09319402b8bdbce668 | arXiv:2602.03036v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2602.03036v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03036v1.html; sha256:6354c40122badd58cc1dace2c3aabb5178d95e55d7882a09319402b8bdbce668 | arXiv:2602.03036v1 HTML — §5.6 Sensitivity & Ablation Study. [facet=limitations]; https://arxiv.org/html/2602.03036v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03036v1.html; sha256:6354c40122badd58cc1dace2c3aabb5178d95e55d7882a09319402b8bdbce668 | External link observed in exact-v1 body: https://github.com/KANABOON1/LatentMem; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-03036 | complete |
| SF-2026-ARXIV-2602-03184 | RP-114e0ef67958401c | deep | arXiv:2602.03184v1 | SRC-ARXIV@arXiv:2602.03184v1 | arXiv:2602.03184v1 HTML — §B.2 Implementation details [facet=method]; https://arxiv.org/html/2602.03184v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03184v1.html; sha256:397746694f5a562f00443fc668f49d89afec4efb1b3de8908928c973df67e149 | arXiv:2602.03184v1 HTML — §5.4 Ablation Results [facet=evaluation]; https://arxiv.org/html/2602.03184v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03184v1.html; sha256:397746694f5a562f00443fc668f49d89afec4efb1b3de8908928c973df67e149 | arXiv:2602.03184v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2602.03184v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03184v1.html; sha256:397746694f5a562f00443fc668f49d89afec4efb1b3de8908928c973df67e149 | Not Disclosed — arXiv:2602.03184v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-03184 | complete |
| SF-2026-ARXIV-2602-03295 | RP-fec930cbaae6cf77 | deep | arXiv:2602.03295v1 | SRC-ARXIV@arXiv:2602.03295v1 | arXiv:2602.03295v1 HTML — §3 Method; §3.3 Prefill-Only Pruning for Efficient Inference [facet=method]; https://arxiv.org/html/2602.03295v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03295v1.html; sha256:d018d3cf5a1147b8ee1ac5bb9face9d216aa650749b25dc440f87fd1d3905f3d | arXiv:2602.03295v1 HTML — §4 Experiments; §4.2 Accuracy; §4.3 Inference Speedup; §4.4 Ablation [facet=evaluation]; https://arxiv.org/html/2602.03295v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03295v1.html; sha256:d018d3cf5a1147b8ee1ac5bb9face9d216aa650749b25dc440f87fd1d3905f3d | arXiv:2602.03295v1 HTML — §7 Limitations; Appendix C Robustness to Representation Mismatch [facet=limitations]; https://arxiv.org/html/2602.03295v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03295v1.html; sha256:d018d3cf5a1147b8ee1ac5bb9face9d216aa650749b25dc440f87fd1d3905f3d | Not Disclosed — arXiv:2602.03295v1 does not disclose an author implementation repository or exact commit used by this review | claim:SF-2026-ARXIV-2602-03295 | complete |
| SF-2026-ARXIV-2602-03560 | RP-7a99540c57cd5eb4 | deep | arXiv:2602.03560v1 | SRC-ARXIV@arXiv:2602.03560v1 | arXiv:2602.03560v1 HTML — §2.2 Hybrid Attention Architecture [facet=method]; https://arxiv.org/html/2602.03560v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03560v1.html; sha256:f88b03d4b5b953e17842bc9c7bad8000e105dccbb46a49c39f6b9d9e0513a082 | arXiv:2602.03560v1 HTML — §Evaluation Benchmark [facet=evaluation]; https://arxiv.org/html/2602.03560v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03560v1.html; sha256:f88b03d4b5b953e17842bc9c7bad8000e105dccbb46a49c39f6b9d9e0513a082 | arXiv:2602.03560v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2602.03560v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03560v1.html; sha256:f88b03d4b5b953e17842bc9c7bad8000e105dccbb46a49c39f6b9d9e0513a082 | Not Disclosed — arXiv:2602.03560v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-03560 | complete |
| SF-2026-ARXIV-2602-02499 | RP-6d03591a827ec5b5 | deep | arXiv:2602.02499v1 | SRC-ARXIV@arXiv:2602.02499v1 | arXiv:2602.02499v1 HTML — §4 Implementation [facet=method]; https://arxiv.org/html/2602.02499v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02499v1.html; sha256:afeaf1803325034e63c316ff9fd2e2486628284dcc9de041f1e2cf4af4afcaad | arXiv:2602.02499v1 HTML — §5.2 General Capability Evaluation [facet=evaluation]; https://arxiv.org/html/2602.02499v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02499v1.html; sha256:afeaf1803325034e63c316ff9fd2e2486628284dcc9de041f1e2cf4af4afcaad | arXiv:2602.02499v1 HTML — §D.2 Ablation on ROSA Symbol Width [facet=limitations]; https://arxiv.org/html/2602.02499v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02499v1.html; sha256:afeaf1803325034e63c316ff9fd2e2486628284dcc9de041f1e2cf4af4afcaad | External link observed in exact-v1 body: https://github.com/zyaaa-ux/ROSA-Tuning; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-02499 | complete |
| SF-2026-ARXIV-2602-02515 | RP-b24037b9a729317b | deep | arXiv:2602.02515v1 | SRC-ARXIV@arXiv:2602.02515v1 | arXiv:2602.02515v1 HTML — §4.1. CreditAudit Design [facet=method]; https://arxiv.org/html/2602.02515v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02515v1.html; sha256:0bbdb57dfbbdb9830a6d2ede3d634e73d05b7e8bbb5eddfcdf498fa008ec361d | arXiv:2602.02515v1 HTML — §3.1. What LLM Evaluation Estimates: Partial Observability and Prompt-Induced Reliability [facet=evaluation]; https://arxiv.org/html/2602.02515v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02515v1.html; sha256:0bbdb57dfbbdb9830a6d2ede3d634e73d05b7e8bbb5eddfcdf498fa008ec361d | arXiv:2602.02515v1 HTML — §Limitations and future work. [facet=limitations]; https://arxiv.org/html/2602.02515v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02515v1.html; sha256:0bbdb57dfbbdb9830a6d2ede3d634e73d05b7e8bbb5eddfcdf498fa008ec361d | External link observed in exact-v1 body: https://github.com/LLwork8888/CreditAudit; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-02515 | complete |
| SF-2026-ARXIV-2602-02574 | RP-13e9d8249c6735f7 | deep | arXiv:2602.02574v1 | SRC-ARXIV@arXiv:2602.02574v1 | arXiv:2602.02574v1 HTML — §Implementation note. [facet=method]; https://arxiv.org/html/2602.02574v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02574v1.html; sha256:641118b66e60a1d0cfbbe7c27c31148b0b5ebc8a07e7a01548cee3f319d67db0 | arXiv:2602.02574v1 HTML — §Policy observability and evaluation tracks. [facet=evaluation]; https://arxiv.org/html/2602.02574v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02574v1.html; sha256:641118b66e60a1d0cfbbe7c27c31148b0b5ebc8a07e7a01548cee3f319d67db0 | arXiv:2602.02574v1 HTML — §9 Limitations [facet=limitations]; https://arxiv.org/html/2602.02574v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02574v1.html; sha256:641118b66e60a1d0cfbbe7c27c31148b0b5ebc8a07e7a01548cee3f319d67db0 | External link observed in exact-v1 body: https://github.com/edgardcham/WritePolicyBench; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-02574 | complete |
| SF-2026-ARXIV-2602-02585 | RP-7fc8527bfe16a179 | deep | arXiv:2602.02585v1 | SRC-ARXIV@arXiv:2602.02585v1 | arXiv:2602.02585v1 PDF — §System Design [facet=method]; https://arxiv.org/pdf/2602.02585v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02585v1.pdf.txt; sha256:91af4963ca2033c0d1b66618be60acca24d9bd1653021ad8da8f8c6e27b202cd | arXiv:2602.02585v1 PDF — §Evaluation [facet=evaluation]; https://arxiv.org/pdf/2602.02585v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02585v1.pdf.txt; sha256:91af4963ca2033c0d1b66618be60acca24d9bd1653021ad8da8f8c6e27b202cd | arXiv:2602.02585v1 PDF — §Discussion and Future Work [facet=limitations]; https://arxiv.org/pdf/2602.02585v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02585v1.pdf.txt; sha256:91af4963ca2033c0d1b66618be60acca24d9bd1653021ad8da8f8c6e27b202cd | Not Disclosed — arXiv:2602.02585v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-02585 | complete |
| SF-2026-ARXIV-2602-02987 | RP-53f4e987d7ab0abe | deep | arXiv:2602.02987v1 | SRC-ARXIV@arXiv:2602.02987v1 | arXiv:2602.02987v1 HTML — §5.1 SLI-Aware Gate-and-Route Control Policy [facet=method]; https://arxiv.org/html/2602.02987v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02987v1.html; sha256:e3995feea443ce3e3d73807f4100ad2428f37dee1f042d5a6d2f221a974c6b68 | arXiv:2602.02987v1 HTML — §6.3 Policy Performance: Baselines and Ablations [facet=evaluation]; https://arxiv.org/html/2602.02987v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02987v1.html; sha256:e3995feea443ce3e3d73807f4100ad2428f37dee1f042d5a6d2f221a974c6b68 | arXiv:2602.02987v1 HTML — §6.3 Policy Performance: Baselines and Ablations [facet=limitations]; https://arxiv.org/html/2602.02987v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02987v1.html; sha256:e3995feea443ce3e3d73807f4100ad2428f37dee1f042d5a6d2f221a974c6b68 | Not Disclosed — arXiv:2602.02987v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-02987 | complete |
| SF-2026-ARXIV-2602-03025 | RP-76ed6d82120bbe35 | deep | arXiv:2602.03025v1 | SRC-ARXIV@arXiv:2602.03025v1 | arXiv:2602.03025v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2602.03025v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03025v1.html; sha256:df3663ae6b3c297de704fb3bf0e2db768182317b64c8aebbd9df05f60085ef51 | arXiv:2602.03025v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2602.03025v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03025v1.html; sha256:df3663ae6b3c297de704fb3bf0e2db768182317b64c8aebbd9df05f60085ef51 | Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet [facet=limitations]; https://arxiv.org/html/2602.03025v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03025v1.html; sha256:df3663ae6b3c297de704fb3bf0e2db768182317b64c8aebbd9df05f60085ef51 | Not Disclosed — arXiv:2602.03025v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-03025 | complete |
| SF-2026-ARXIV-2602-03128 | RP-f44634af54594ffc | deep | arXiv:2602.03128v1 | SRC-ARXIV@arXiv:2602.03128v1 | arXiv:2602.03128v1 HTML — §3. MAFBench: A Unified Benchmark [facet=method]; https://arxiv.org/html/2602.03128v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03128v1.html; sha256:2dffa2485e36e0929221a76ffa4c2f3e91cf08c200ac2286e2e2cac615826c5b | arXiv:2602.03128v1 HTML — §4. Evaluation [facet=evaluation]; https://arxiv.org/html/2602.03128v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03128v1.html; sha256:2dffa2485e36e0929221a76ffa4c2f3e91cf08c200ac2286e2e2cac615826c5b | arXiv:2602.03128v1 HTML — §3.4. Tool Use Benchmarks and Limitations [facet=limitations]; https://arxiv.org/html/2602.03128v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03128v1.html; sha256:2dffa2485e36e0929221a76ffa4c2f3e91cf08c200ac2286e2e2cac615826c5b | External link observed in exact-v1 body: https://github.com/CoDS-GCS/MAFBench; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-03128 | complete |
| SF-2026-ARXIV-2602-03203 | RP-ee11031ab5d60dc2 | deep | arXiv:2602.03203v1 | SRC-ARXIV@arXiv:2602.03203v1 | arXiv:2602.03203v1 HTML — §Design of Model and Sampling Algorithm. [facet=method]; https://arxiv.org/html/2602.03203v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03203v1.html; sha256:e400c1efa4ca7bbbe780efd82cdd2f8ab038c122ba63098a9677d08a55ec787d | arXiv:2602.03203v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2602.03203v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03203v1.html; sha256:e400c1efa4ca7bbbe780efd82cdd2f8ab038c122ba63098a9677d08a55ec787d | Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet [facet=limitations]; https://arxiv.org/html/2602.03203v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03203v1.html; sha256:e400c1efa4ca7bbbe780efd82cdd2f8ab038c122ba63098a9677d08a55ec787d | Not Disclosed — arXiv:2602.03203v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-03203 | complete |
| SF-2026-ARXIV-2602-03255 | RP-11f339637a96d7c9 | deep | arXiv:2602.03255v1 | SRC-ARXIV@arXiv:2602.03255v1 | arXiv:2602.03255v1 HTML — §3.3 Automated Evaluation Framework [facet=method]; https://arxiv.org/html/2602.03255v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03255v1.html; sha256:c138e83997c8d8cfd0deb0f2fe9f200d1bb90b945187431cd1119343651dd8ea | arXiv:2602.03255v1 HTML — §3.3 Automated Evaluation Framework [facet=evaluation]; https://arxiv.org/html/2602.03255v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03255v1.html; sha256:c138e83997c8d8cfd0deb0f2fe9f200d1bb90b945187431cd1119343651dd8ea | arXiv:2602.03255v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2602.03255v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03255v1.html; sha256:c138e83997c8d8cfd0deb0f2fe9f200d1bb90b945187431cd1119343651dd8ea | External link observed in exact-v1 body: https://github.com/tychenn/LPS-Bench; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-03255 | complete |
| SF-2026-ARXIV-2602-03338 | RP-004e2b119dfbac06 | deep | arXiv:2602.03338v1 | SRC-ARXIV@arXiv:2602.03338v1 | arXiv:2602.03338v1 HTML — §Experimental design. [facet=method]; https://arxiv.org/html/2602.03338v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03338v1.html; sha256:495872c269e2a00068bc462d33701d1608f8347501645b3f257bc4e52b285bd0 | arXiv:2602.03338v1 HTML — §4 Main Results [facet=evaluation]; https://arxiv.org/html/2602.03338v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03338v1.html; sha256:495872c269e2a00068bc462d33701d1608f8347501645b3f257bc4e52b285bd0 | arXiv:2602.03338v1 HTML — §Critic model scale. [facet=limitations]; https://arxiv.org/html/2602.03338v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03338v1.html; sha256:495872c269e2a00068bc462d33701d1608f8347501645b3f257bc4e52b285bd0 | External link observed in exact-v1 body: https://github.com/huggingface/smolagents; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-03338 | complete |
| SF-2026-ARXIV-2602-03495 | RP-791ac0e2d4d0d6c6 | deep | arXiv:2602.03495v1 | SRC-ARXIV@arXiv:2602.03495v1 | arXiv:2602.03495v1 HTML — §4. Design [facet=method]; https://arxiv.org/html/2602.03495v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03495v1.html; sha256:b9d7e82c90cf370f0ee7b2394e0de320641c6e049645b6fed16e81e34286c5a5 | arXiv:2602.03495v1 HTML — §6.2. Overall Results [facet=evaluation]; https://arxiv.org/html/2602.03495v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03495v1.html; sha256:b9d7e82c90cf370f0ee7b2394e0de320641c6e049645b6fed16e81e34286c5a5 | arXiv:2602.03495v1 HTML — §6.5. Discussion [facet=limitations]; https://arxiv.org/html/2602.03495v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03495v1.html; sha256:b9d7e82c90cf370f0ee7b2394e0de320641c6e049645b6fed16e81e34286c5a5 | External link observed in exact-v1 body: https://github.com/ggerganov/llama.cpp; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-03495 | complete |
| SF-2026-ARXIV-2602-03580 | RP-0b34755aedb77c6f | deep | arXiv:2602.03580v1 | SRC-ARXIV@arXiv:2602.03580v1 | arXiv:2602.03580v1 HTML — §Design of MCPDiFF [facet=method]; https://arxiv.org/html/2602.03580v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03580v1.html; sha256:31c694d4a2b6fe667c006a171130174ecb01d93097c259ea8021e0fbcf4c4792 | arXiv:2602.03580v1 HTML — §Experiment Results [facet=evaluation]; https://arxiv.org/html/2602.03580v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03580v1.html; sha256:31c694d4a2b6fe667c006a171130174ecb01d93097c259ea8021e0fbcf4c4792 | arXiv:2602.03580v1 HTML — §Open Questions and Future Directions [facet=limitations]; https://arxiv.org/html/2602.03580v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03580v1.html; sha256:31c694d4a2b6fe667c006a171130174ecb01d93097c259ea8021e0fbcf4c4792 | Not Disclosed — arXiv:2602.03580v1 does not disclose a public repository, release, commit, or executable artifact used by this review | claim:SF-2026-ARXIV-2602-03580 | complete |
| SF-2026-ARXIV-2602-03632 | RP-787a37d21a13c61a | deep | arXiv:2602.03632v1 | SRC-ARXIV@arXiv:2602.03632v1 | arXiv:2602.03632v1 HTML — §3. The CALM Approach [facet=method]; https://arxiv.org/html/2602.03632v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03632v1.html; sha256:bdd54c1e8ad8d49ec8dbdf715dc316e1e19cdb5870c6d1dd38f12cc2c91d8411 | arXiv:2602.03632v1 HTML — §5. Results [facet=evaluation]; https://arxiv.org/html/2602.03632v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03632v1.html; sha256:bdd54c1e8ad8d49ec8dbdf715dc316e1e19cdb5870c6d1dd38f12cc2c91d8411 | arXiv:2602.03632v1 HTML — §7. Threats to Validity [facet=limitations]; https://arxiv.org/html/2602.03632v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03632v1.html; sha256:bdd54c1e8ad8d49ec8dbdf715dc316e1e19cdb5870c6d1dd38f12cc2c91d8411 | External link observed in exact-v1 body: https://github.com/sa4s-serc/CALM; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-03632 | complete |
| SF-2026-ARXIV-2602-03719 | RP-98bce91be9a07068 | deep | arXiv:2602.03719v1 | SRC-ARXIV@arXiv:2602.03719v1 | arXiv:2602.03719v1 HTML — §A.1 Algorithm Details [facet=method]; https://arxiv.org/html/2602.03719v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03719v1.html; sha256:25ed1740f5933ee6d22439676f328c78d899ddccc145928251e8b939b4388801 | arXiv:2602.03719v1 HTML — §Evaluation. [facet=evaluation]; https://arxiv.org/html/2602.03719v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03719v1.html; sha256:25ed1740f5933ee6d22439676f328c78d899ddccc145928251e8b939b4388801 | arXiv:2602.03719v1 HTML — §Appendix D Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2602.03719v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03719v1.html; sha256:25ed1740f5933ee6d22439676f328c78d899ddccc145928251e8b939b4388801 | External link observed in exact-v1 body: https://github.com/YubaoZhao/BranPO; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-03719 | complete |
| SF-2026-ARXIV-2602-03782 | RP-3e96b8a145fd66fa | deep | arXiv:2602.03782v1 | SRC-ARXIV@arXiv:2602.03782v1 | arXiv:2602.03782v1 HTML — §3.3 The proposed QVLA [facet=method]; https://arxiv.org/html/2602.03782v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03782v1.html; sha256:5bd42b692579ff94463155d779771b9507d3ec1acfb83ac5004bc38d41c7c7b7 | arXiv:2602.03782v1 HTML — §4.2 Comparison with State-of-the-arts [facet=evaluation]; https://arxiv.org/html/2602.03782v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03782v1.html; sha256:5bd42b692579ff94463155d779771b9507d3ec1acfb83ac5004bc38d41c7c7b7 | arXiv:2602.03782v1 HTML — §H.2 Behavior During Full-Precision Failure Trials [facet=limitations]; https://arxiv.org/html/2602.03782v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.03782v1.html; sha256:5bd42b692579ff94463155d779771b9507d3ec1acfb83ac5004bc38d41c7c7b7 | External link observed in exact-v1 body: https://github.com/AutoLab-SAI-SJTU/AutoQVLA; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-03782 | complete |
| SF-2026-ARXIV-2602-02589 | RP-4332232a486fdb01 | standard | arXiv:2602.02589v1 | SRC-ARXIV@arXiv:2602.02589v1 | arXiv:2602.02589v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2602.02589v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02589v1.html; sha256:7239c809130fe8b05d39aca43ca6fab4882901c9afd462e4e3e1c704176c037c | arXiv:2602.02589v1 HTML — §Ablation: Peer evaluation outperforms self evaluation [facet=evaluation]; https://arxiv.org/html/2602.02589v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02589v1.html; sha256:7239c809130fe8b05d39aca43ca6fab4882901c9afd462e4e3e1c704176c037c | arXiv:2602.02589v1 HTML — §6 Discussion [facet=limitations]; https://arxiv.org/html/2602.02589v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02589v1.html; sha256:7239c809130fe8b05d39aca43ca6fab4882901c9afd462e4e3e1c704176c037c | External link observed in exact-v1 body: https://github.com/caura-ai/caura-PeerRank; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-02589 | complete |
| SF-2026-ARXIV-2602-02690 | RP-8a405dbe4b9ea625 | standard | arXiv:2602.02690v1 | SRC-ARXIV@arXiv:2602.02690v1 | arXiv:2602.02690v1 HTML — §3.1 Design [facet=method]; https://arxiv.org/html/2602.02690v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02690v1.html; sha256:13e36c25d3c0fc7be10ae7f25f3802bc5480f198aa966b090ea7eed8a62052d9 | arXiv:2602.02690v1 HTML — §5.2 RQ1: Performance difference spanning cutoff [facet=evaluation]; https://arxiv.org/html/2602.02690v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02690v1.html; sha256:13e36c25d3c0fc7be10ae7f25f3802bc5480f198aa966b090ea7eed8a62052d9 | arXiv:2602.02690v1 HTML — §7 Future Work [facet=limitations]; https://arxiv.org/html/2602.02690v1; papers/2026/02/_sources/daily-20260205/exact-v1-bodies/2602.02690v1.html; sha256:13e36c25d3c0fc7be10ae7f25f3802bc5480f198aa966b090ea7eed8a62052d9 | External link observed in exact-v1 body: https://github.com/anthropics/claude-code; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence | claim:SF-2026-ARXIV-2602-02690 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2602-02579:start -->
### ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation

- **Review route:** `deep`；Primary=`arXiv:2602.02579v1`；owner=`INFER-KV-CACHE`。

- **问题与旧路径：** `ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation` 是否在 `INFER-KV-CACHE` 中改变已有状态、数据或控制责任；旧路径仍成立于：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.02579v1 HTML — §3.1 Illustrating the Failure of Existing Methods` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。

- **State / data / control owner：** `INFER-KV-CACHE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.02579v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.02579v1 HTML — §5.2 Accuracy Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.02579v1 HTML — §3.1 Illustrating the Failure of Existing Methods`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2602-02579:start -->
- **Claim boundary:** 只支持 arXiv:2602.02579v1 实际披露的机制与实验。方法定位为 arXiv:2602.02579v1 HTML — §3.1 Illustrating the Failure of Existing Methods；验证定位为 arXiv:2602.02579v1 HTML — §5.2 Accuracy Evaluation；边界定位为 arXiv:2602.02579v1 HTML — §3.1 Illustrating the Failure of Existing Methods。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-02579:end -->
<!-- review:SF-2026-ARXIV-2602-02579:end -->

<!-- review:SF-2026-ARXIV-2602-02599:start -->
### RAP: KV-Cache Compression via RoPE-Aligned Pruning

- **Review route:** `deep`；Primary=`arXiv:2602.02599v1`；owner=`INFER-KV-CACHE`。

- **问题与旧路径：** `RAP: KV-Cache Compression via RoPE-Aligned Pruning` 是否在 `INFER-KV-CACHE` 中改变已有状态、数据或控制责任；旧路径仍成立于：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.02599v1 HTML — §4 RAP: RoPE-Aligned Pruning` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。

- **State / data / control owner：** `INFER-KV-CACHE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.02599v1 HTML — §Appendix D Complete Experimental Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.02599v1 HTML — §6.3 Ablation Study`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2602-02599:start -->
- **Claim boundary:** 只支持 arXiv:2602.02599v1 实际披露的机制与实验。方法定位为 arXiv:2602.02599v1 HTML — §4 RAP: RoPE-Aligned Pruning；验证定位为 arXiv:2602.02599v1 HTML — §Appendix D Complete Experimental Results；边界定位为 arXiv:2602.02599v1 HTML — §6.3 Ablation Study。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-02599:end -->
<!-- review:SF-2026-ARXIV-2602-02599:end -->

<!-- review:SF-2026-ARXIV-2602-02958:start -->
### Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization

- **Review route:** `deep`；Primary=`arXiv:2602.02958v1`；owner=`INFER-KV-CACHE`。

- **问题与旧路径：** `Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization` 是否在 `INFER-KV-CACHE` 中改变已有状态、数据或控制责任；旧路径仍成立于：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.02958v1 HTML — §4 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。

- **State / data / control owner：** `INFER-KV-CACHE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/guandeh17/Self-Forcing/blob/main/prompts/MovieGenVideoBench_extended.txt; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.02958v1 HTML — §5.2 Quality Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.02958v1 HTML — §5.4 Sensitivity Test`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2602-02958:start -->
- **Claim boundary:** 只支持 arXiv:2602.02958v1 实际披露的机制与实验。方法定位为 arXiv:2602.02958v1 HTML — §4 Methodology；验证定位为 arXiv:2602.02958v1 HTML — §5.2 Quality Evaluation；边界定位为 arXiv:2602.02958v1 HTML — §5.4 Sensitivity Test。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-02958:end -->
<!-- review:SF-2026-ARXIV-2602-02958:end -->

<!-- review:SF-2026-ARXIV-2602-03036:start -->
### LatentMem: Customizing Latent Memory for Multi-Agent Systems

- **Review route:** `deep`；Primary=`arXiv:2602.03036v1`；owner=`AGENT-MEMORY`。

- **问题与旧路径：** `LatentMem: Customizing Latent Memory for Multi-Agent Systems` 是否在 `AGENT-MEMORY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03036v1 HTML — §4 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 memory 的写入、版本、检索与失效控制权。触发约束是：长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。

- **State / data / control owner：** `AGENT-MEMORY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/KANABOON1/LatentMem; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03036v1 HTML — §5.2 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03036v1 HTML — §5.6 Sensitivity & Ablation Study.`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2602-03036:start -->
- **Claim boundary:** 只支持 arXiv:2602.03036v1 实际披露的机制与实验。方法定位为 arXiv:2602.03036v1 HTML — §4 Methodology；验证定位为 arXiv:2602.03036v1 HTML — §5.2 Main Results；边界定位为 arXiv:2602.03036v1 HTML — §5.6 Sensitivity & Ablation Study.。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03036:end -->
<!-- review:SF-2026-ARXIV-2602-03036:end -->

<!-- review:SF-2026-ARXIV-2602-03184:start -->
### DynSplit-KV: Dynamic Semantic Splitting for KVCache Compression in Efficient Long-Context LLM Inference

- **Review route:** `deep`；Primary=`arXiv:2602.03184v1`；owner=`INFER-KV-CACHE`。

- **问题与旧路径：** `DynSplit-KV: Dynamic Semantic Splitting for KVCache Compression in Efficient Long-Context LLM Inference` 是否在 `INFER-KV-CACHE` 中改变已有状态、数据或控制责任；旧路径仍成立于：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03184v1 HTML — §B.2 Implementation details` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。

- **State / data / control owner：** `INFER-KV-CACHE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.03184v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03184v1 HTML — §5.4 Ablation Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03184v1 HTML — §6 Conclusion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2602-03184:start -->
- **Claim boundary:** 只支持 arXiv:2602.03184v1 实际披露的机制与实验。方法定位为 arXiv:2602.03184v1 HTML — §B.2 Implementation details；验证定位为 arXiv:2602.03184v1 HTML — §5.4 Ablation Results；边界定位为 arXiv:2602.03184v1 HTML — §6 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03184:end -->
<!-- review:SF-2026-ARXIV-2602-03184:end -->

<!-- review:SF-2026-ARXIV-2602-03295:start -->
### POP: Prefill-Only Pruning for Efficient Large Model Inference

- **Review route:** `deep`；Primary=`arXiv:2602.03295v1`；owner=`INFER-PREFILL`。

- **问题与旧路径：** `POP: Prefill-Only Pruning for Efficient Large Model Inference` 是否在 `INFER-PREFILL` 中改变已有状态、数据或控制责任；旧路径仍成立于：Prefill 对完整 prompt 做 dense forward，语义与实现最直接。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03295v1 HTML — §3 Method; §3.3 Prefill-Only Pruning for Efficient Inference` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 prompt token、attention work、prefill plan 与 KV materialization。触发约束是：长输入和异构硬件使 token 选择、并行与带宽成为 TTFT 主约束。

- **State / data / control owner：** `INFER-PREFILL` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.03295v1 does not disclose an author implementation repository or exact commit used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03295v1 HTML — §4 Experiments; §4.2 Accuracy; §4.3 Inference Speedup; §4.4 Ablation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03295v1 HTML — §7 Limitations; Appendix C Robustness to Representation Mismatch`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：输入较短或 exact dense attention 必须保留时完整 Prefill 仍合理。

<!-- claim:SF-2026-ARXIV-2602-03295:start -->
- **Claim boundary:** 只支持 arXiv:2602.03295v1 实际披露的机制与实验。方法定位为 arXiv:2602.03295v1 HTML — §3 Method; §3.3 Prefill-Only Pruning for Efficient Inference；验证定位为 arXiv:2602.03295v1 HTML — §4 Experiments; §4.2 Accuracy; §4.3 Inference Speedup; §4.4 Ablation；边界定位为 arXiv:2602.03295v1 HTML — §7 Limitations; Appendix C Robustness to Representation Mismatch。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03295:end -->
<!-- review:SF-2026-ARXIV-2602-03295:end -->

<!-- review:SF-2026-ARXIV-2602-03560:start -->
### HySparse: A Hybrid Sparse Attention Architecture with Oracle Token Selection and KV Cache Sharing

- **Review route:** `deep`；Primary=`arXiv:2602.03560v1`；owner=`MODEL-LONG-CONTEXT`。

- **问题与旧路径：** `HySparse: A Hybrid Sparse Attention Architecture with Oracle Token Selection and KV Cache Sharing` 是否在 `MODEL-LONG-CONTEXT` 中改变已有状态、数据或控制责任；旧路径仍成立于：全量 attention 保留任意 token 交互，在中短序列上最直接。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03560v1 HTML — §2.2 Hybrid Attention Architecture` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 上下文选择、层次化表示和可访问记忆的语义边界。触发约束是：序列增长令计算、显存和信息稀释同时恶化。

- **State / data / control owner：** `MODEL-LONG-CONTEXT` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.03560v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03560v1 HTML — §Evaluation Benchmark`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03560v1 HTML — §6 Conclusion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：任务确实依赖密集全局交互且长度可控时全量 attention 仍是基线。

<!-- claim:SF-2026-ARXIV-2602-03560:start -->
- **Claim boundary:** 只支持 arXiv:2602.03560v1 实际披露的机制与实验。方法定位为 arXiv:2602.03560v1 HTML — §2.2 Hybrid Attention Architecture；验证定位为 arXiv:2602.03560v1 HTML — §Evaluation Benchmark；边界定位为 arXiv:2602.03560v1 HTML — §6 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03560:end -->
<!-- review:SF-2026-ARXIV-2602-03560:end -->

<!-- review:SF-2026-ARXIV-2602-02499:start -->
### ROSA-Tuning: Enhancing Long-Context Modeling via Suffix Matching

- **Review route:** `deep`；Primary=`arXiv:2602.02499v1`；owner=`MODEL-LONG-CONTEXT`。

- **问题与旧路径：** `ROSA-Tuning: Enhancing Long-Context Modeling via Suffix Matching` 是否在 `MODEL-LONG-CONTEXT` 中改变已有状态、数据或控制责任；旧路径仍成立于：全量 attention 保留任意 token 交互，在中短序列上最直接。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.02499v1 HTML — §4 Implementation` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 上下文选择、层次化表示和可访问记忆的语义边界。触发约束是：序列增长令计算、显存和信息稀释同时恶化。

- **State / data / control owner：** `MODEL-LONG-CONTEXT` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/zyaaa-ux/ROSA-Tuning; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.02499v1 HTML — §5.2 General Capability Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.02499v1 HTML — §D.2 Ablation on ROSA Symbol Width`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：任务确实依赖密集全局交互且长度可控时全量 attention 仍是基线。

<!-- claim:SF-2026-ARXIV-2602-02499:start -->
- **Claim boundary:** 只支持 arXiv:2602.02499v1 实际披露的机制与实验。方法定位为 arXiv:2602.02499v1 HTML — §4 Implementation；验证定位为 arXiv:2602.02499v1 HTML — §5.2 General Capability Evaluation；边界定位为 arXiv:2602.02499v1 HTML — §D.2 Ablation on ROSA Symbol Width。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-02499:end -->
<!-- review:SF-2026-ARXIV-2602-02499:end -->

<!-- review:SF-2026-ARXIV-2602-02515:start -->
### CreditAudit: 2$^\text{nd}$ Dimension for LLM Evaluation and Selection

- **Review route:** `deep`；Primary=`arXiv:2602.02515v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `CreditAudit: 2$^\text{nd}$ Dimension for LLM Evaluation and Selection` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.02515v1 HTML — §4.1. CreditAudit Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/LLwork8888/CreditAudit; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.02515v1 HTML — §3.1. What LLM Evaluation Estimates: Partial Observability and Prompt-Induced Reliability`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.02515v1 HTML — §Limitations and future work.`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-02515:start -->
- **Claim boundary:** 只支持 arXiv:2602.02515v1 实际披露的机制与实验。方法定位为 arXiv:2602.02515v1 HTML — §4.1. CreditAudit Design；验证定位为 arXiv:2602.02515v1 HTML — §3.1. What LLM Evaluation Estimates: Partial Observability and Prompt-Induced Reliability；边界定位为 arXiv:2602.02515v1 HTML — §Limitations and future work.。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-02515:end -->
<!-- review:SF-2026-ARXIV-2602-02515:end -->

<!-- review:SF-2026-ARXIV-2602-02574:start -->
### WritePolicyBench: Benchmarking Memory Write Policies under Byte Budgets

- **Review route:** `deep`；Primary=`arXiv:2602.02574v1`；owner=`AGENT-MEMORY`。

- **问题与旧路径：** `WritePolicyBench: Benchmarking Memory Write Policies under Byte Budgets` 是否在 `AGENT-MEMORY` 中改变已有状态、数据或控制责任；旧路径仍成立于：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.02574v1 HTML — §Implementation note.` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 memory 的写入、版本、检索与失效控制权。触发约束是：长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。

- **State / data / control owner：** `AGENT-MEMORY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/edgardcham/WritePolicyBench; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.02574v1 HTML — §Policy observability and evaluation tracks.`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.02574v1 HTML — §9 Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2602-02574:start -->
- **Claim boundary:** 只支持 arXiv:2602.02574v1 实际披露的机制与实验。方法定位为 arXiv:2602.02574v1 HTML — §Implementation note.；验证定位为 arXiv:2602.02574v1 HTML — §Policy observability and evaluation tracks.；边界定位为 arXiv:2602.02574v1 HTML — §9 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-02574:end -->
<!-- review:SF-2026-ARXIV-2602-02574:end -->

<!-- review:SF-2026-ARXIV-2602-02585:start -->
### Agentic Observability: Automated Alert Triage for Adobe E-Commerce

- **Review route:** `deep`；Primary=`arXiv:2602.02585v1`；owner=`PLATFORM-MONITORING`。

- **问题与旧路径：** `Agentic Observability: Automated Alert Triage for Adobe E-Commerce` 是否在 `PLATFORM-MONITORING` 中改变已有状态、数据或控制责任；旧路径仍成立于：人工查看告警、日志与 runbook 在事件量较小时最透明。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.02585v1 PDF — §System Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 signal identity、evidence retrieval、diagnosis state、action proposal 与 human approval。触发约束是：事件规模、跨系统证据和响应时限增长后，triage 的读取、判断与动作必须可追踪。

- **State / data / control owner：** `PLATFORM-MONITORING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.02585v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.02585v1 PDF — §Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.02585v1 PDF — §Discussion and Future Work`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：低频高风险事件仍应保留人工主导路径，自动化只提供可审计建议。

<!-- claim:SF-2026-ARXIV-2602-02585:start -->
- **Claim boundary:** 只支持 arXiv:2602.02585v1 实际披露的机制与实验。方法定位为 arXiv:2602.02585v1 PDF — §System Design；验证定位为 arXiv:2602.02585v1 PDF — §Evaluation；边界定位为 arXiv:2602.02585v1 PDF — §Discussion and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-02585:end -->
<!-- review:SF-2026-ARXIV-2602-02585:end -->

<!-- review:SF-2026-ARXIV-2602-02987:start -->
### Large-Scale LLM Inference with Heterogeneous Workloads: Prefill-Decode Contention and Asymptotically Optimal Control

- **Review route:** `deep`；Primary=`arXiv:2602.02987v1`；owner=`INFER-SCHEDULING`。

- **问题与旧路径：** `Large-Scale LLM Inference with Heterogeneous Workloads: Prefill-Decode Contention and Asymptotically Optimal Control` 是否在 `INFER-SCHEDULING` 中改变已有状态、数据或控制责任；旧路径仍成立于：FIFO 或静态批次在请求同质时易预测、易实现。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.02987v1 HTML — §5.1 SLI-Aware Gate-and-Route Control Policy` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。

- **State / data / control owner：** `INFER-SCHEDULING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.02987v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.02987v1 HTML — §6.3 Policy Performance: Baselines and Ablations`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.02987v1 HTML — §6.3 Policy Performance: Baselines and Ablations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2602-02987:start -->
- **Claim boundary:** 只支持 arXiv:2602.02987v1 实际披露的机制与实验。方法定位为 arXiv:2602.02987v1 HTML — §5.1 SLI-Aware Gate-and-Route Control Policy；验证定位为 arXiv:2602.02987v1 HTML — §6.3 Policy Performance: Baselines and Ablations；边界定位为 arXiv:2602.02987v1 HTML — §6.3 Policy Performance: Baselines and Ablations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-02987:end -->
<!-- review:SF-2026-ARXIV-2602-02987:end -->

<!-- review:SF-2026-ARXIV-2602-03025:start -->
### RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents

- **Review route:** `deep`；Primary=`arXiv:2602.03025v1`；owner=`TRAIN-GRPO`。

- **问题与旧路径：** `RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents` 是否在 `TRAIN-GRPO` 中改变已有状态、数据或控制责任；旧路径仍成立于：每条样本独立更新易实现，但难利用组内相对信号。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03025v1 HTML — §3 Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 prompt、rollout、group advantage 与 on-policy freshness。触发约束是：稀疏可验证奖励和 rollout 成本要求更有效地复用同组比较。

- **State / data / control owner：** `TRAIN-GRPO` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.03025v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03025v1 HTML — §4.2 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** exact-v1 未披露独立 limitations（`Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：高质量逐样本监督充足时 SFT/DPO 仍更简单。

<!-- claim:SF-2026-ARXIV-2602-03025:start -->
- **Claim boundary:** 只支持 arXiv:2602.03025v1 实际披露的机制与实验。方法定位为 arXiv:2602.03025v1 HTML — §3 Method；验证定位为 arXiv:2602.03025v1 HTML — §4.2 Main Results；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03025:end -->
<!-- review:SF-2026-ARXIV-2602-03025:end -->

<!-- review:SF-2026-ARXIV-2602-03128:start -->
### Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis

- **Review route:** `deep`；Primary=`arXiv:2602.03128v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03128v1 HTML — §3. MAFBench: A Unified Benchmark` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/CoDS-GCS/MAFBench; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03128v1 HTML — §4. Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03128v1 HTML — §3.4. Tool Use Benchmarks and Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-03128:start -->
- **Claim boundary:** 只支持 arXiv:2602.03128v1 实际披露的机制与实验。方法定位为 arXiv:2602.03128v1 HTML — §3. MAFBench: A Unified Benchmark；验证定位为 arXiv:2602.03128v1 HTML — §4. Evaluation；边界定位为 arXiv:2602.03128v1 HTML — §3.4. Tool Use Benchmarks and Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03128:end -->
<!-- review:SF-2026-ARXIV-2602-03128:end -->

<!-- review:SF-2026-ARXIV-2602-03203:start -->
### ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution

- **Review route:** `deep`；Primary=`arXiv:2602.03203v1`；owner=`INFER-KV-CACHE`。

- **问题与旧路径：** `ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution` 是否在 `INFER-KV-CACHE` 中改变已有状态、数据或控制责任；旧路径仍成立于：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03203v1 HTML — §Design of Model and Sampling Algorithm.` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。

- **State / data / control owner：** `INFER-KV-CACHE` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.03203v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03203v1 HTML — §4.2 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** exact-v1 未披露独立 limitations（`Not Disclosed — exact-v1 HTML has no independent limitations or counterevidence section; a positive conclusion does not replace that facet`）；这意味着审阅必须缩小主张，而不是把缺口当作反证。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2602-03203:start -->
- **Claim boundary:** 只支持 arXiv:2602.03203v1 实际披露的机制与实验。方法定位为 arXiv:2602.03203v1 HTML — §Design of Model and Sampling Algorithm.；验证定位为 arXiv:2602.03203v1 HTML — §4.2 Main Results；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03203:end -->
<!-- review:SF-2026-ARXIV-2602-03203:end -->

<!-- review:SF-2026-ARXIV-2602-03255:start -->
### LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios

- **Review route:** `deep`；Primary=`arXiv:2602.03255v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03255v1 HTML — §3.3 Automated Evaluation Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/tychenn/LPS-Bench; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03255v1 HTML — §3.3 Automated Evaluation Framework`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03255v1 HTML — §Limitations`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-03255:start -->
- **Claim boundary:** 只支持 arXiv:2602.03255v1 实际披露的机制与实验。方法定位为 arXiv:2602.03255v1 HTML — §3.3 Automated Evaluation Framework；验证定位为 arXiv:2602.03255v1 HTML — §3.3 Automated Evaluation Framework；边界定位为 arXiv:2602.03255v1 HTML — §Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03255:end -->
<!-- review:SF-2026-ARXIV-2602-03255:end -->

<!-- review:SF-2026-ARXIV-2602-03338:start -->
### Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention

- **Review route:** `deep`；Primary=`arXiv:2602.03338v1`；owner=`AGENT-REFLECTION`。

- **问题与旧路径：** `Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention` 是否在 `AGENT-REFLECTION` 中改变已有状态、数据或控制责任；旧路径仍成立于：一次生成后直接提交最短也最容易复现。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03338v1 HTML — §Experimental design.` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 critique evidence、revision lineage 与 termination control。触发约束是：长链任务与环境反馈使系统需要保存 critique、revision 与停止条件。

- **State / data / control owner：** `AGENT-REFLECTION` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/huggingface/smolagents; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03338v1 HTML — §4 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03338v1 HTML — §Critic model scale.`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：低风险、可即时验证的短输出仍可直接提交。

<!-- claim:SF-2026-ARXIV-2602-03338:start -->
- **Claim boundary:** 只支持 arXiv:2602.03338v1 实际披露的机制与实验。方法定位为 arXiv:2602.03338v1 HTML — §Experimental design.；验证定位为 arXiv:2602.03338v1 HTML — §4 Main Results；边界定位为 arXiv:2602.03338v1 HTML — §Critic model scale.。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03338:end -->
<!-- review:SF-2026-ARXIV-2602-03338:end -->

<!-- review:SF-2026-ARXIV-2602-03495:start -->
### DALI: A Workload-Aware Offloading Framework for Efficient MoE Inference on Local PCs

- **Review route:** `deep`；Primary=`arXiv:2602.03495v1`；owner=`INFER-GPU-MEMORY`。

- **问题与旧路径：** `DALI: A Workload-Aware Offloading Framework for Efficient MoE Inference on Local PCs` 是否在 `INFER-GPU-MEMORY` 中改变已有状态、数据或控制责任；旧路径仍成立于：权重与运行时状态常驻单设备，状态最透明。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03495v1 HTML — §4. Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 权重、KV、临时张量的 placement、lifetime 与迁移控制。触发约束是：容量、带宽和并发超过单设备预算后，放置、迁移与回收成为控制问题。

- **State / data / control owner：** `INFER-GPU-MEMORY` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/ggerganov/llama.cpp; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03495v1 HTML — §6.2. Overall Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03495v1 HTML — §6.5. Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：模型可完整驻留且负载稳定时静态常驻仍更简单。

<!-- claim:SF-2026-ARXIV-2602-03495:start -->
- **Claim boundary:** 只支持 arXiv:2602.03495v1 实际披露的机制与实验。方法定位为 arXiv:2602.03495v1 HTML — §4. Design；验证定位为 arXiv:2602.03495v1 HTML — §6.2. Overall Results；边界定位为 arXiv:2602.03495v1 HTML — §6.5. Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03495:end -->
<!-- review:SF-2026-ARXIV-2602-03495:end -->

<!-- review:SF-2026-ARXIV-2602-03580:start -->
### Don't believe everything you read: Understanding and Measuring MCP Behavior under Misleading Tool Descriptions

- **Review route:** `deep`；Primary=`arXiv:2602.03580v1`；owner=`AGENT-MCP`。

- **问题与旧路径：** `Don't believe everything you read: Understanding and Measuring MCP Behavior under Misleading Tool Descriptions` 是否在 `AGENT-MCP` 中改变已有状态、数据或控制责任；旧路径仍成立于：把协议当作普通 tool adapter，部署和权限模型最简单。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03580v1 HTML — §Design of MCPDiFF` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 协议身份、capability 声明、授权与审计状态。触发约束是：跨 server capability、委托链与动态发现使权限边界不再等同于一次函数调用。

- **State / data / control owner：** `AGENT-MCP` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** Not Disclosed — arXiv:2602.03580v1 does not disclose a public repository, release, commit, or executable artifact used by this review

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03580v1 HTML — §Experiment Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03580v1 HTML — §Open Questions and Future Directions`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：固定工具集、单一信任域仍可保留较薄的 adapter。

<!-- claim:SF-2026-ARXIV-2602-03580:start -->
- **Claim boundary:** 只支持 arXiv:2602.03580v1 实际披露的机制与实验。方法定位为 arXiv:2602.03580v1 HTML — §Design of MCPDiFF；验证定位为 arXiv:2602.03580v1 HTML — §Experiment Results；边界定位为 arXiv:2602.03580v1 HTML — §Open Questions and Future Directions。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03580:end -->
<!-- review:SF-2026-ARXIV-2602-03580:end -->

<!-- review:SF-2026-ARXIV-2602-03632:start -->
### CALM: A Self-Adaptive Orchestration Approach for QoS-Aware Routing in Small Language Model based Systems

- **Review route:** `deep`；Primary=`arXiv:2602.03632v1`；owner=`INFER-SCHEDULING`。

- **问题与旧路径：** `CALM: A Self-Adaptive Orchestration Approach for QoS-Aware Routing in Small Language Model based Systems` 是否在 `INFER-SCHEDULING` 中改变已有状态、数据或控制责任；旧路径仍成立于：FIFO 或静态批次在请求同质时易预测、易实现。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03632v1 HTML — §3. The CALM Approach` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。

- **State / data / control owner：** `INFER-SCHEDULING` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/sa4s-serc/CALM; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03632v1 HTML — §5. Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03632v1 HTML — §7. Threats to Validity`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2602-03632:start -->
- **Claim boundary:** 只支持 arXiv:2602.03632v1 实际披露的机制与实验。方法定位为 arXiv:2602.03632v1 HTML — §3. The CALM Approach；验证定位为 arXiv:2602.03632v1 HTML — §5. Results；边界定位为 arXiv:2602.03632v1 HTML — §7. Threats to Validity。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03632:end -->
<!-- review:SF-2026-ARXIV-2602-03632:end -->

<!-- review:SF-2026-ARXIV-2602-03719:start -->
### BranPO: Scalable Contrastive Branch Sampling for Long-Horizon Agentic Reinforcement Learning

- **Review route:** `deep`；Primary=`arXiv:2602.03719v1`；owner=`TRAIN-RLHF`。

- **问题与旧路径：** `BranPO: Scalable Contrastive Branch Sampling for Long-Horizon Agentic Reinforcement Learning` 是否在 `TRAIN-RLHF` 中改变已有状态、数据或控制责任；旧路径仍成立于：固定后训练配方便于重复和对比。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03719v1 HTML — §A.1 Algorithm Details` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。

- **State / data / control owner：** `TRAIN-RLHF` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/YubaoZhao/BranPO; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03719v1 HTML — §Evaluation.`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03719v1 HTML — §Appendix D Limitations and Future Work`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：反馈稳定、任务窄且分布固定时成熟配方仍可复用。

<!-- claim:SF-2026-ARXIV-2602-03719:start -->
- **Claim boundary:** 只支持 arXiv:2602.03719v1 实际披露的机制与实验。方法定位为 arXiv:2602.03719v1 HTML — §A.1 Algorithm Details；验证定位为 arXiv:2602.03719v1 HTML — §Evaluation.；边界定位为 arXiv:2602.03719v1 HTML — §Appendix D Limitations and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03719:end -->
<!-- review:SF-2026-ARXIV-2602-03719:end -->

<!-- review:SF-2026-ARXIV-2602-03782:start -->
### QVLA: Not All Channels Are Equal in Vision-Language-Action Model's Quantization

- **Review route:** `deep`；Primary=`arXiv:2602.03782v1`；owner=`INFER-TENSORRT-LLM`。

- **问题与旧路径：** `QVLA: Not All Channels Are Equal in Vision-Language-Action Model's Quantization` 是否在 `INFER-TENSORRT-LLM` 中改变已有状态、数据或控制责任；旧路径仍成立于：通用 eager 执行便于调试且无需额外编译状态。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.03782v1 HTML — §3.3 The proposed QVLA` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。

- **State / data / control owner：** `INFER-TENSORRT-LLM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/AutoLab-SAI-SJTU/AutoQVLA; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.03782v1 HTML — §4.2 Comparison with State-of-the-arts`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.03782v1 HTML — §H.2 Behavior During Full-Precision Failure Trials`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：工作负载小、形状动态或调试优先时 eager 路径仍合理。

<!-- claim:SF-2026-ARXIV-2602-03782:start -->
- **Claim boundary:** 只支持 arXiv:2602.03782v1 实际披露的机制与实验。方法定位为 arXiv:2602.03782v1 HTML — §3.3 The proposed QVLA；验证定位为 arXiv:2602.03782v1 HTML — §4.2 Comparison with State-of-the-arts；边界定位为 arXiv:2602.03782v1 HTML — §H.2 Behavior During Full-Precision Failure Trials。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-03782:end -->
<!-- review:SF-2026-ARXIV-2602-03782:end -->

<!-- review:SF-2026-ARXIV-2602-02589:start -->
### PeerRank: Autonomous LLM Evaluation Through Web-Grounded, Bias-Controlled Peer Review

- **Review route:** `standard`；Primary=`arXiv:2602.02589v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `PeerRank: Autonomous LLM Evaluation Through Web-Grounded, Bias-Controlled Peer Review` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.02589v1 HTML — §3 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/caura-ai/caura-PeerRank; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.02589v1 HTML — §Ablation: Peer evaluation outperforms self evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.02589v1 HTML — §6 Discussion`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-02589:start -->
- **Claim boundary:** 只支持 arXiv:2602.02589v1 实际披露的机制与实验。方法定位为 arXiv:2602.02589v1 HTML — §3 Methodology；验证定位为 arXiv:2602.02589v1 HTML — §Ablation: Peer evaluation outperforms self evaluation；边界定位为 arXiv:2602.02589v1 HTML — §6 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-02589:end -->
<!-- review:SF-2026-ARXIV-2602-02589:end -->

<!-- review:SF-2026-ARXIV-2602-02690:start -->
### Outrunning LLM Cutoffs: A Live Kernel Crash Resolution Benchmark for All

- **Review route:** `standard`；Primary=`arXiv:2602.02690v1`；owner=`PLATFORM-EVALUATION-SYSTEM`。

- **问题与旧路径：** `Outrunning LLM Cutoffs: A Live Kernel Crash Resolution Benchmark for All` 是否在 `PLATFORM-EVALUATION-SYSTEM` 中改变已有状态、数据或控制责任；旧路径仍成立于：单一离线分数便于比较版本。

- **约束变化与机制：** exact-v1 的 `arXiv:2602.02690v1 HTML — §3.1 Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。

- **State / data / control owner：** `PLATFORM-EVALUATION-SYSTEM` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。

- **实现与 artifact：** External link observed in exact-v1 body: https://github.com/anthropics/claude-code; author-artifact relationship and exact commit/tag are Not Disclosed, so this link is not used as claim evidence

- **Evaluation contract：** 公开验证定位在 `arXiv:2602.02690v1 HTML — §5.2 RQ1: Performance difference spanning cutoff`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。

- **Trade-off、failure mode 与共存边界：** 限制或反证定位在 `arXiv:2602.02690v1 HTML — §7 Future Work`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2602-02690:start -->
- **Claim boundary:** 只支持 arXiv:2602.02690v1 实际披露的机制与实验。方法定位为 arXiv:2602.02690v1 HTML — §3.1 Design；验证定位为 arXiv:2602.02690v1 HTML — §5.2 RQ1: Performance difference spanning cutoff；边界定位为 arXiv:2602.02690v1 HTML — §7 Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。
<!-- claim:SF-2026-ARXIV-2602-02690:end -->
<!-- review:SF-2026-ARXIV-2602-02690:end -->

## 4. Benchmark Contracts

None — 作者实验只在各 Source Review 的 evaluation contract 内支持机制判断；本日报不发布可跨 workload 外推的 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-02579 | score_7_9 | selected | DA-20260205-1 | — | 在同日 eligibility frontier 中优先选择 Total=8 且形成独立 `INFER-KV-CACHE` 系统责任链的 family。 | analysis:DA-20260205-1 |
| SF-2026-ARXIV-2602-02599 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-KV-CACHE`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-02599 |
| SF-2026-ARXIV-2602-02958 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-KV-CACHE`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-02958 |
| SF-2026-ARXIV-2602-03036 | score_7_9 | selected | DA-20260205-2 | — | 在同日 eligibility frontier 中优先选择 Total=8 且形成独立 `AGENT-MEMORY` 系统责任链的 family。 | analysis:DA-20260205-2 |
| SF-2026-ARXIV-2602-03184 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-KV-CACHE`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03184 |
| SF-2026-ARXIV-2602-03295 | score_7_9; forced_review; potential_books_delta | selected | DA-20260205-3 | — | 在同日 eligibility frontier 中优先选择 Total=8 且形成独立 `INFER-PREFILL` 系统责任链的 family。 | analysis:DA-20260205-3 |
| SF-2026-ARXIV-2602-03560 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `MODEL-LONG-CONTEXT`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03560 |
| SF-2026-ARXIV-2602-02499 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `MODEL-LONG-CONTEXT`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-02499 |
| SF-2026-ARXIV-2602-02515 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-02515 |
| SF-2026-ARXIV-2602-02574 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `AGENT-MEMORY`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-02574 |
| SF-2026-ARXIV-2602-02585 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-MONITORING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-02585 |
| SF-2026-ARXIV-2602-02987 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-SCHEDULING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-02987 |
| SF-2026-ARXIV-2602-03025 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `TRAIN-GRPO`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03025 |
| SF-2026-ARXIV-2602-03128 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03128 |
| SF-2026-ARXIV-2602-03203 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-KV-CACHE`；同 owner 已有更高优先级叙事单元，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03203 |
| SF-2026-ARXIV-2602-03255 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `PLATFORM-EVALUATION-SYSTEM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03255 |
| SF-2026-ARXIV-2602-03338 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `AGENT-REFLECTION`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03338 |
| SF-2026-ARXIV-2602-03495 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-GPU-MEMORY`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03495 |
| SF-2026-ARXIV-2602-03580 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `AGENT-MCP`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03580 |
| SF-2026-ARXIV-2602-03632 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-SCHEDULING`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03632 |
| SF-2026-ARXIV-2602-03719 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `TRAIN-RLHF`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03719 |
| SF-2026-ARXIV-2602-03782 | score_7_9 | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `INFER-TENSORRT-LLM`；跨层影响较已选单元更窄，不降低其证据与 Books 决策责任。 | analysis-decision:SF-2026-ARXIV-2602-03782 |

<!-- analysis:DA-20260205-1:start -->
### DA-20260205-1 — ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `INFER-KV-CACHE`。exact-v1 的 `arXiv:2602.02579v1 HTML — §3.1 Illustrating the Failure of Existing Methods` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。 公开验证定位在 `arXiv:2602.02579v1 HTML — §5.2 Accuracy Evaluation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：限制或反证定位在 `arXiv:2602.02579v1 HTML — §3.1 Illustrating the Failure of Existing Methods`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。
<!-- analysis:DA-20260205-1:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-02599:start -->
`RAP: KV-Cache Compression via RoPE-Aligned Pruning` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-02599:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-02958:start -->
`Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-02958:end -->

<!-- analysis:DA-20260205-2:start -->
### DA-20260205-2 — LatentMem: Customizing Latent Memory for Multi-Agent Systems

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `AGENT-MEMORY`。exact-v1 的 `arXiv:2602.03036v1 HTML — §4 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 memory 的写入、版本、检索与失效控制权。触发约束是：长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 公开验证定位在 `arXiv:2602.03036v1 HTML — §5.2 Main Results`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：限制或反证定位在 `arXiv:2602.03036v1 HTML — §5.6 Sensitivity & Ablation Study.`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：短会话或不可接受派生状态漂移时仍应回退原始 context。
<!-- analysis:DA-20260205-2:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03184:start -->
`DynSplit-KV: Dynamic Semantic Splitting for KVCache Compression in Efficient Long-Context LLM Inference` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03184:end -->

<!-- analysis:DA-20260205-3:start -->
### DA-20260205-3 — POP: Prefill-Only Pruning for Efficient Large Model Inference

旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `INFER-PREFILL`。exact-v1 的 `arXiv:2602.03295v1 HTML — §3 Method; §3.3 Prefill-Only Pruning for Efficient Inference` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 prompt token、attention work、prefill plan 与 KV materialization。触发约束是：长输入和异构硬件使 token 选择、并行与带宽成为 TTFT 主约束。 公开验证定位在 `arXiv:2602.03295v1 HTML — §4 Experiments; §4.2 Accuracy; §4.3 Inference Speedup; §4.4 Ablation`；已有证据只支持论文披露的模型、数据、硬件、精度与任务组合，未披露字段保持 `Not Disclosed`，不外推为跨 workload 或 production SLO 结论。 代价、failure mode 与旧方案共存边界由以下证据限制：限制或反证定位在 `arXiv:2602.03295v1 HTML — §7 Limitations; Appendix C Robustness to Representation Mismatch`。新增 failure surface 包括机制状态陈旧、额外控制开销及分布变化；共存边界是：输入较短或 exact dense attention 必须保留时完整 Prefill 仍合理。
<!-- analysis:DA-20260205-3:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03560:start -->
`HySparse: A Hybrid Sparse Attention Architecture with Oracle Token Selection and KV Cache Sharing` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03560:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-02499:start -->
`ROSA-Tuning: Enhancing Long-Context Modeling via Suffix Matching` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-02499:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-02515:start -->
`CreditAudit: 2$^\text{nd}$ Dimension for LLM Evaluation and Selection` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-02515:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-02574:start -->
`WritePolicyBench: Benchmarking Memory Write Policies under Byte Budgets` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-02574:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-02585:start -->
`Agentic Observability: Automated Alert Triage for Adobe E-Commerce` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-02585:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-02987:start -->
`Large-Scale LLM Inference with Heterogeneous Workloads: Prefill-Decode Contention and Asymptotically Optimal Control` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-02987:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03025:start -->
`RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03025:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03128:start -->
`Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03128:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03203:start -->
`ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03203:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03255:start -->
`LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03255:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03338:start -->
`Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03338:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03495:start -->
`DALI: A Workload-Aware Offloading Framework for Efficient MoE Inference on Local PCs` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03495:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03580:start -->
`Don't believe everything you read: Understanding and Measuring MCP Behavior under Misleading Tool Descriptions` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03580:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03632:start -->
`CALM: A Self-Adaptive Orchestration Approach for QoS-Aware Routing in Small Language Model based Systems` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03632:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03719:start -->
`BranPO: Scalable Contrastive Branch Sampling for Long-Horizon Agentic Reinforcement Learning` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03719:end -->

<!-- analysis-decision:SF-2026-ARXIV-2602-03782:start -->
`QVLA: Not All Channels Are Equal in Vision-Language-Action Model's Quantization` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。
<!-- analysis-decision:SF-2026-ARXIV-2602-03782:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2602-02579 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 717) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-02579 | delta:SF-2026-ARXIV-2602-02579 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02579 |
| SF-2026-ARXIV-2602-02599 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 850) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-02599 | delta:SF-2026-ARXIV-2602-02599 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02599 |
| SF-2026-ARXIV-2602-02958 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#本章在知识树中的位置 (line 1071) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-02958 | delta:SF-2026-ARXIV-2602-02958 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02958 |
| SF-2026-ARXIV-2602-03036 | AGENT-MEMORY | books/part-07-agent/77-memory.md#从原始轨迹到派生策略memory-的演进不是无限追加 (line 670) | books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03036 | delta:SF-2026-ARXIV-2602-03036 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03036 |
| SF-2026-ARXIV-2602-03184 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-cache-的生命周期 (line 307) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03184 | delta:SF-2026-ARXIV-2602-03184 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03184 |
| SF-2026-ARXIV-2602-03295 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#计算量从哪里来 (line 62) | books/part-05-inference-system/42-what-happens-during-inference.md#本章要回答的问题 (line 10); books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03295 | delta:SF-2026-ARXIV-2602-03295 | Principle Reuse | Integrate | books-review:SF-2026-ARXIV-2602-03295 |
| SF-2026-ARXIV-2602-03560 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#路线二改变-attention-连接 (line 121) | books/part-02-model/21-moe.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/23-multimodal-representation.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03560 | delta:SF-2026-ARXIV-2602-03560 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03560 |
| SF-2026-ARXIV-2602-02499 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#路线六让模型在-test-time-更新内部记忆 (line 468) | books/part-02-model/21-moe.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/23-multimodal-representation.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-02499 | delta:SF-2026-ARXIV-2602-02499 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02499 |
| SF-2026-ARXIV-2602-02515 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#第一个不变量评估声明必须绑定完整对象 (line 179) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-02515 | delta:SF-2026-ARXIV-2602-02515 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02515 |
| SF-2026-ARXIV-2602-02574 | AGENT-MEMORY | books/part-07-agent/77-memory.md#派生-memory-的组织适用性与验证 (line 725) | books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-02574 | delta:SF-2026-ARXIV-2602-02574 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02574 |
| SF-2026-ARXIV-2602-02585 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#rateerrorsduration-与-saturation (line 152) | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/68-logging.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-02585 | delta:SF-2026-ARXIV-2602-02585 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02585 |
| SF-2026-ARXIV-2602-02987 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#iteration-scheduling (line 251) | books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-02987 | delta:SF-2026-ARXIV-2602-02987 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02987 |
| SF-2026-ARXIV-2602-03025 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#从-sequence-reward-到-typed-trajectory (line 1004) | books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10); books/part-04-training-system/34-dpo.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03025 | delta:SF-2026-ARXIV-2602-03025 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03025 |
| SF-2026-ARXIV-2602-03128 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#第一个不变量评估声明必须绑定完整对象 (line 179) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03128 | delta:SF-2026-ARXIV-2602-03128 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03128 |
| SF-2026-ARXIV-2602-03203 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-cache-的生命周期 (line 543) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03203 | delta:SF-2026-ARXIV-2602-03203 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03203 |
| SF-2026-ARXIV-2602-03255 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 689) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03255 | delta:SF-2026-ARXIV-2602-03255 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03255 |
| SF-2026-ARXIV-2602-03338 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#自检问题 (line 288) | books/part-07-agent/79-planning.md#本章要回答的问题 (line 10); books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03338 | delta:SF-2026-ARXIV-2602-03338 | Principle Reuse | Integrate | books-review:SF-2026-ARXIV-2602-03338 |
| SF-2026-ARXIV-2602-03495 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#三类缓解路径 (line 244) | books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03495 | delta:SF-2026-ARXIV-2602-03495 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03495 |
| SF-2026-ARXIV-2602-03580 | AGENT-MCP | books/part-07-agent/83-mcp.md#tool-catalog-扩大后discovery-与-execution-必须分离 (line 227) | books/part-07-agent/82-multi-agent.md#本章要回答的问题 (line 10); books/part-07-agent/84-agent-platform.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03580 | delta:SF-2026-ARXIV-2602-03580 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03580 |
| SF-2026-ARXIV-2602-03632 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#能力生产与能力交付不能互相替代 (line 901) | books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03632 | delta:SF-2026-ARXIV-2602-03632 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03632 |
| SF-2026-ARXIV-2602-03719 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#rlhfrlaif-与-verifiable-reward (line 491) | books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03719 | delta:SF-2026-ARXIV-2602-03719 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03719 |
| SF-2026-ARXIV-2602-03782 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#量化为什么不自动带来加速 (line 710) | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-03782 | delta:SF-2026-ARXIV-2602-03782 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-03782 |
| SF-2026-ARXIV-2602-02589 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 484) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-02589 | delta:SF-2026-ARXIV-2602-02589 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02589 |
| SF-2026-ARXIV-2602-02690 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 950) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2602-02690 | delta:SF-2026-ARXIV-2602-02690 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2602-02690 |

<!-- existing:SF-2026-ARXIV-2602-02579:start -->
已对读当前 owner `INFER-KV-CACHE` 在 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 717)` 的命题：### 从反应式 Recall 到预测式 Prefetch
<!-- existing:SF-2026-ARXIV-2602-02579:end -->

<!-- delta:SF-2026-ARXIV-2602-02579:start -->
exact-v1 的 `arXiv:2602.02579v1 HTML — §3.1 Illustrating the Failure of Existing Methods` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。
<!-- delta:SF-2026-ARXIV-2602-02579:end -->

<!-- books-review:SF-2026-ARXIV-2602-02579:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.02579v1 实际披露的机制与实验。方法定位为 arXiv:2602.02579v1 HTML — §3.1 Illustrating the Failure of Existing Methods；验证定位为 arXiv:2602.02579v1 HTML — §5.2 Accuracy Evaluation；边界定位为 arXiv:2602.02579v1 HTML — §3.1 Illustrating the Failure of Existing Methods。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-02579:end -->

<!-- existing:SF-2026-ARXIV-2602-02599:start -->
已对读当前 owner `INFER-KV-CACHE` 在 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#一致性不变量 (line 850)` 的命题：### Quantization Objective 应对齐 Attention Distortion
<!-- existing:SF-2026-ARXIV-2602-02599:end -->

<!-- delta:SF-2026-ARXIV-2602-02599:start -->
exact-v1 的 `arXiv:2602.02599v1 HTML — §4 RAP: RoPE-Aligned Pruning` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。
<!-- delta:SF-2026-ARXIV-2602-02599:end -->

<!-- books-review:SF-2026-ARXIV-2602-02599:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.02599v1 实际披露的机制与实验。方法定位为 arXiv:2602.02599v1 HTML — §4 RAP: RoPE-Aligned Pruning；验证定位为 arXiv:2602.02599v1 HTML — §Appendix D Complete Experimental Results；边界定位为 arXiv:2602.02599v1 HTML — §6.3 Ablation Study。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-02599:end -->

<!-- existing:SF-2026-ARXIV-2602-02958:start -->
已对读当前 owner `INFER-KV-CACHE` 在 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#本章在知识树中的位置 (line 1071)` 的命题：### Agentic KV Precision 必须绑定 Role、Modality 与生命周期
<!-- existing:SF-2026-ARXIV-2602-02958:end -->

<!-- delta:SF-2026-ARXIV-2602-02958:start -->
exact-v1 的 `arXiv:2602.02958v1 HTML — §4 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。
<!-- delta:SF-2026-ARXIV-2602-02958:end -->

<!-- books-review:SF-2026-ARXIV-2602-02958:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.02958v1 实际披露的机制与实验。方法定位为 arXiv:2602.02958v1 HTML — §4 Methodology；验证定位为 arXiv:2602.02958v1 HTML — §5.2 Quality Evaluation；边界定位为 arXiv:2602.02958v1 HTML — §5.4 Sensitivity Test。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-02958:end -->

<!-- existing:SF-2026-ARXIV-2602-03036:start -->
已对读当前 owner `AGENT-MEMORY` 在 `books/part-07-agent/77-memory.md#从原始轨迹到派生策略memory-的演进不是无限追加 (line 670)` 的命题：### 从固定 Latent 容量到按 Query 分配读取预算
<!-- existing:SF-2026-ARXIV-2602-03036:end -->

<!-- delta:SF-2026-ARXIV-2602-03036:start -->
exact-v1 的 `arXiv:2602.03036v1 HTML — §4 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 memory 的写入、版本、检索与失效控制权。触发约束是：长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。
<!-- delta:SF-2026-ARXIV-2602-03036:end -->

<!-- books-review:SF-2026-ARXIV-2602-03036:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03036v1 实际披露的机制与实验。方法定位为 arXiv:2602.03036v1 HTML — §4 Methodology；验证定位为 arXiv:2602.03036v1 HTML — §5.2 Main Results；边界定位为 arXiv:2602.03036v1 HTML — §5.6 Sensitivity & Ablation Study.。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03036:end -->

<!-- existing:SF-2026-ARXIV-2602-03184:start -->
已对读当前 owner `INFER-KV-CACHE` 在 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-cache-的生命周期 (line 307)` 的命题：### 从统一保留到 workload-aware eviction
<!-- existing:SF-2026-ARXIV-2602-03184:end -->

<!-- delta:SF-2026-ARXIV-2602-03184:start -->
exact-v1 的 `arXiv:2602.03184v1 HTML — §B.2 Implementation details` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。
<!-- delta:SF-2026-ARXIV-2602-03184:end -->

<!-- books-review:SF-2026-ARXIV-2602-03184:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03184v1 实际披露的机制与实验。方法定位为 arXiv:2602.03184v1 HTML — §B.2 Implementation details；验证定位为 arXiv:2602.03184v1 HTML — §5.4 Ablation Results；边界定位为 arXiv:2602.03184v1 HTML — §6 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03184:end -->

<!-- existing:SF-2026-ARXIV-2602-03295:start -->
已对读当前 owner `INFER-PREFILL` 在 `books/part-05-inference-system/43-prefill.md#计算量从哪里来 (line 62)` 的命题：#### Phase-aware layer execution：Prefill 与 Decode 不必共享同一计算图
<!-- existing:SF-2026-ARXIV-2602-03295:end -->

<!-- delta:SF-2026-ARXIV-2602-03295:start -->
exact-v1 的 `arXiv:2602.03295v1 HTML — §3 Method; §3.3 Prefill-Only Pruning for Efficient Inference` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 prompt token、attention work、prefill plan 与 KV materialization。触发约束是：长输入和异构硬件使 token 选择、并行与带宽成为 TTFT 主约束。
<!-- delta:SF-2026-ARXIV-2602-03295:end -->

<!-- books-review:SF-2026-ARXIV-2602-03295:start -->
Decision=`Integrate`：现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。 相邻章节已定位为 `books/part-05-inference-system/42-what-happens-during-inference.md#本章要回答的问题 (line 10); books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03295v1 实际披露的机制与实验。方法定位为 arXiv:2602.03295v1 HTML — §3 Method; §3.3 Prefill-Only Pruning for Efficient Inference；验证定位为 arXiv:2602.03295v1 HTML — §4 Experiments; §4.2 Accuracy; §4.3 Inference Speedup; §4.4 Ablation；边界定位为 arXiv:2602.03295v1 HTML — §7 Limitations; Appendix C Robustness to Representation Mismatch。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03295:end -->

<!-- existing:SF-2026-ARXIV-2602-03560:start -->
已对读当前 owner `MODEL-LONG-CONTEXT` 在 `books/part-02-model/22-long-context.md#路线二改变-attention-连接 (line 121)` 的命题：### Conditional Attention 的路由粒度必须匹配执行粒度
<!-- existing:SF-2026-ARXIV-2602-03560:end -->

<!-- delta:SF-2026-ARXIV-2602-03560:start -->
exact-v1 的 `arXiv:2602.03560v1 HTML — §2.2 Hybrid Attention Architecture` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 上下文选择、层次化表示和可访问记忆的语义边界。触发约束是：序列增长令计算、显存和信息稀释同时恶化。
<!-- delta:SF-2026-ARXIV-2602-03560:end -->

<!-- books-review:SF-2026-ARXIV-2602-03560:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-02-model/21-moe.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/23-multimodal-representation.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03560v1 实际披露的机制与实验。方法定位为 arXiv:2602.03560v1 HTML — §2.2 Hybrid Attention Architecture；验证定位为 arXiv:2602.03560v1 HTML — §Evaluation Benchmark；边界定位为 arXiv:2602.03560v1 HTML — §6 Conclusion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03560:end -->

<!-- existing:SF-2026-ARXIV-2602-02499:start -->
已对读当前 owner `MODEL-LONG-CONTEXT` 在 `books/part-02-model/22-long-context.md#路线六让模型在-test-time-更新内部记忆 (line 468)` 的命题：### State continuity：历史可访问与计算连续性不是同一问题
<!-- existing:SF-2026-ARXIV-2602-02499:end -->

<!-- delta:SF-2026-ARXIV-2602-02499:start -->
exact-v1 的 `arXiv:2602.02499v1 HTML — §4 Implementation` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 上下文选择、层次化表示和可访问记忆的语义边界。触发约束是：序列增长令计算、显存和信息稀释同时恶化。
<!-- delta:SF-2026-ARXIV-2602-02499:end -->

<!-- books-review:SF-2026-ARXIV-2602-02499:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-02-model/21-moe.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/23-multimodal-representation.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.02499v1 实际披露的机制与实验。方法定位为 arXiv:2602.02499v1 HTML — §4 Implementation；验证定位为 arXiv:2602.02499v1 HTML — §5.2 General Capability Evaluation；边界定位为 arXiv:2602.02499v1 HTML — §D.2 Ablation on ROSA Symbol Width。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-02499:end -->

<!-- existing:SF-2026-ARXIV-2602-02515:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#第一个不变量评估声明必须绑定完整对象 (line 179)` 的命题：### Evaluation Identity 必须包含 Harness 与 Environment
<!-- existing:SF-2026-ARXIV-2602-02515:end -->

<!-- delta:SF-2026-ARXIV-2602-02515:start -->
exact-v1 的 `arXiv:2602.02515v1 HTML — §4.1. CreditAudit Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-02515:end -->

<!-- books-review:SF-2026-ARXIV-2602-02515:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.02515v1 实际披露的机制与实验。方法定位为 arXiv:2602.02515v1 HTML — §4.1. CreditAudit Design；验证定位为 arXiv:2602.02515v1 HTML — §3.1. What LLM Evaluation Estimates: Partial Observability and Prompt-Induced Reliability；边界定位为 arXiv:2602.02515v1 HTML — §Limitations and future work.。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-02515:end -->

<!-- existing:SF-2026-ARXIV-2602-02574:start -->
已对读当前 owner `AGENT-MEMORY` 在 `books/part-07-agent/77-memory.md#派生-memory-的组织适用性与验证 (line 725)` 的命题：### Retrieval 之前还有 Retention / Admission
<!-- existing:SF-2026-ARXIV-2602-02574:end -->

<!-- delta:SF-2026-ARXIV-2602-02574:start -->
exact-v1 的 `arXiv:2602.02574v1 HTML — §Implementation note.` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 memory 的写入、版本、检索与失效控制权。触发约束是：长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。
<!-- delta:SF-2026-ARXIV-2602-02574:end -->

<!-- books-review:SF-2026-ARXIV-2602-02574:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.02574v1 实际披露的机制与实验。方法定位为 arXiv:2602.02574v1 HTML — §Implementation note.；验证定位为 arXiv:2602.02574v1 HTML — §Policy observability and evaluation tracks.；边界定位为 arXiv:2602.02574v1 HTML — §9 Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-02574:end -->

<!-- existing:SF-2026-ARXIV-2602-02585:start -->
已对读当前 owner `PLATFORM-MONITORING` 在 `books/part-06-ai-infrastructure/67-monitoring.md#rateerrorsduration-与-saturation (line 152)` 的命题：### 从 Thread State 下钻到带资源身份的依赖图
<!-- existing:SF-2026-ARXIV-2602-02585:end -->

<!-- delta:SF-2026-ARXIV-2602-02585:start -->
exact-v1 的 `arXiv:2602.02585v1 PDF — §System Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 signal identity、evidence retrieval、diagnosis state、action proposal 与 human approval。触发约束是：事件规模、跨系统证据和响应时限增长后，triage 的读取、判断与动作必须可追踪。
<!-- delta:SF-2026-ARXIV-2602-02585:end -->

<!-- books-review:SF-2026-ARXIV-2602-02585:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/68-logging.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.02585v1 实际披露的机制与实验。方法定位为 arXiv:2602.02585v1 PDF — §System Design；验证定位为 arXiv:2602.02585v1 PDF — §Evaluation；边界定位为 arXiv:2602.02585v1 PDF — §Discussion and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-02585:end -->

<!-- existing:SF-2026-ARXIV-2602-02987:start -->
已对读当前 owner `INFER-SCHEDULING` 在 `books/part-05-inference-system/56-inference-scheduling.md#iteration-scheduling (line 251)` 的命题：### Exclusive Batching 的 Phase Switch 是 Workload-dependent State
<!-- existing:SF-2026-ARXIV-2602-02987:end -->

<!-- delta:SF-2026-ARXIV-2602-02987:start -->
exact-v1 的 `arXiv:2602.02987v1 HTML — §5.1 SLI-Aware Gate-and-Route Control Policy` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。
<!-- delta:SF-2026-ARXIV-2602-02987:end -->

<!-- books-review:SF-2026-ARXIV-2602-02987:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.02987v1 实际披露的机制与实验。方法定位为 arXiv:2602.02987v1 HTML — §5.1 SLI-Aware Gate-and-Route Control Policy；验证定位为 arXiv:2602.02987v1 HTML — §6.3 Policy Performance: Baselines and Ablations；边界定位为 arXiv:2602.02987v1 HTML — §6.3 Policy Performance: Baselines and Ablations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-02987:end -->

<!-- existing:SF-2026-ARXIV-2602-03025:start -->
已对读当前 owner `TRAIN-GRPO` 在 `books/part-04-training-system/33-grpo.md#从-sequence-reward-到-typed-trajectory (line 1004)` 的命题：### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界
<!-- existing:SF-2026-ARXIV-2602-03025:end -->

<!-- delta:SF-2026-ARXIV-2602-03025:start -->
exact-v1 的 `arXiv:2602.03025v1 HTML — §3 Method` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 prompt、rollout、group advantage 与 on-policy freshness。触发约束是：稀疏可验证奖励和 rollout 成本要求更有效地复用同组比较。
<!-- delta:SF-2026-ARXIV-2602-03025:end -->

<!-- books-review:SF-2026-ARXIV-2602-03025:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10); books/part-04-training-system/34-dpo.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03025v1 实际披露的机制与实验。方法定位为 arXiv:2602.03025v1 HTML — §3 Method；验证定位为 arXiv:2602.03025v1 HTML — §4.2 Main Results；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03025:end -->

<!-- existing:SF-2026-ARXIV-2602-03128:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#第一个不变量评估声明必须绑定完整对象 (line 179)` 的命题：### Evaluation Identity 必须包含 Harness 与 Environment
<!-- existing:SF-2026-ARXIV-2602-03128:end -->

<!-- delta:SF-2026-ARXIV-2602-03128:start -->
exact-v1 的 `arXiv:2602.03128v1 HTML — §3. MAFBench: A Unified Benchmark` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-03128:end -->

<!-- books-review:SF-2026-ARXIV-2602-03128:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03128v1 实际披露的机制与实验。方法定位为 arXiv:2602.03128v1 HTML — §3. MAFBench: A Unified Benchmark；验证定位为 arXiv:2602.03128v1 HTML — §4. Evaluation；边界定位为 arXiv:2602.03128v1 HTML — §3.4. Tool Use Benchmarks and Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03128:end -->

<!-- existing:SF-2026-ARXIV-2602-03203:start -->
已对读当前 owner `INFER-KV-CACHE` 在 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-cache-的生命周期 (line 543)` 的命题：### 从昂贵 Oracle 到 Learned Eviction Policy
<!-- existing:SF-2026-ARXIV-2602-03203:end -->

<!-- delta:SF-2026-ARXIV-2602-03203:start -->
exact-v1 的 `arXiv:2602.03203v1 HTML — §Design of Model and Sampling Algorithm.` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 KV 的 identity、压缩、复用、放置与失效状态。触发约束是：长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。
<!-- delta:SF-2026-ARXIV-2602-03203:end -->

<!-- books-review:SF-2026-ARXIV-2602-03203:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03203v1 实际披露的机制与实验。方法定位为 arXiv:2602.03203v1 HTML — §Design of Model and Sampling Algorithm.；验证定位为 arXiv:2602.03203v1 HTML — §4.2 Main Results；独立 limitations 未披露，因而采用更窄主张。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03203:end -->

<!-- existing:SF-2026-ARXIV-2602-03255:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 689)` 的命题：### 从 Perfect API 到累积故障：Agent 评测必须控制 Environment Complexity
<!-- existing:SF-2026-ARXIV-2602-03255:end -->

<!-- delta:SF-2026-ARXIV-2602-03255:start -->
exact-v1 的 `arXiv:2602.03255v1 HTML — §3.3 Automated Evaluation Framework` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-03255:end -->

<!-- books-review:SF-2026-ARXIV-2602-03255:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03255v1 实际披露的机制与实验。方法定位为 arXiv:2602.03255v1 HTML — §3.3 Automated Evaluation Framework；验证定位为 arXiv:2602.03255v1 HTML — §3.3 Automated Evaluation Framework；边界定位为 arXiv:2602.03255v1 HTML — §Limitations。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03255:end -->

<!-- existing:SF-2026-ARXIV-2602-03338:start -->
已对读当前 owner `AGENT-REFLECTION` 在 `books/part-07-agent/80-reflection.md#自检问题 (line 288)` 的命题：### Critic Accuracy 不等于 Intervention Value
<!-- existing:SF-2026-ARXIV-2602-03338:end -->

<!-- delta:SF-2026-ARXIV-2602-03338:start -->
exact-v1 的 `arXiv:2602.03338v1 HTML — §Experimental design.` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 critique evidence、revision lineage 与 termination control。触发约束是：长链任务与环境反馈使系统需要保存 critique、revision 与停止条件。
<!-- delta:SF-2026-ARXIV-2602-03338:end -->

<!-- books-review:SF-2026-ARXIV-2602-03338:start -->
Decision=`Integrate`：现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。 相邻章节已定位为 `books/part-07-agent/79-planning.md#本章要回答的问题 (line 10); books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03338v1 实际披露的机制与实验。方法定位为 arXiv:2602.03338v1 HTML — §Experimental design.；验证定位为 arXiv:2602.03338v1 HTML — §4 Main Results；边界定位为 arXiv:2602.03338v1 HTML — §Critic model scale.。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03338:end -->

<!-- existing:SF-2026-ARXIV-2602-03495:start -->
已对读当前 owner `INFER-GPU-MEMORY` 在 `books/part-05-inference-system/54-gpu-memory.md#三类缓解路径 (line 244)` 的命题：### 层级的管理权不应默认属于 Framework
<!-- existing:SF-2026-ARXIV-2602-03495:end -->

<!-- delta:SF-2026-ARXIV-2602-03495:start -->
exact-v1 的 `arXiv:2602.03495v1 HTML — §4. Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 权重、KV、临时张量的 placement、lifetime 与迁移控制。触发约束是：容量、带宽和并发超过单设备预算后，放置、迁移与回收成为控制问题。
<!-- delta:SF-2026-ARXIV-2602-03495:end -->

<!-- books-review:SF-2026-ARXIV-2602-03495:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03495v1 实际披露的机制与实验。方法定位为 arXiv:2602.03495v1 HTML — §4. Design；验证定位为 arXiv:2602.03495v1 HTML — §6.2. Overall Results；边界定位为 arXiv:2602.03495v1 HTML — §6.5. Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03495:end -->

<!-- existing:SF-2026-ARXIV-2602-03580:start -->
已对读当前 owner `AGENT-MCP` 在 `books/part-07-agent/83-mcp.md#tool-catalog-扩大后discovery-与-execution-必须分离 (line 227)` 的命题：### Tool Description 是可执行的 Discovery Interface
<!-- existing:SF-2026-ARXIV-2602-03580:end -->

<!-- delta:SF-2026-ARXIV-2602-03580:start -->
exact-v1 的 `arXiv:2602.03580v1 HTML — §Design of MCPDiFF` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 协议身份、capability 声明、授权与审计状态。触发约束是：跨 server capability、委托链与动态发现使权限边界不再等同于一次函数调用。
<!-- delta:SF-2026-ARXIV-2602-03580:end -->

<!-- books-review:SF-2026-ARXIV-2602-03580:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-07-agent/82-multi-agent.md#本章要回答的问题 (line 10); books/part-07-agent/84-agent-platform.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03580v1 实际披露的机制与实验。方法定位为 arXiv:2602.03580v1 HTML — §Design of MCPDiFF；验证定位为 arXiv:2602.03580v1 HTML — §Experiment Results；边界定位为 arXiv:2602.03580v1 HTML — §Open Questions and Future Directions。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03580:end -->

<!-- existing:SF-2026-ARXIV-2602-03632:start -->
已对读当前 owner `INFER-SCHEDULING` 在 `books/part-05-inference-system/56-inference-scheduling.md#能力生产与能力交付不能互相替代 (line 901)` 的命题：### Heterogeneous Model Pool 与 Routing Policy 要独立版本化
<!-- existing:SF-2026-ARXIV-2602-03632:end -->

<!-- delta:SF-2026-ARXIV-2602-03632:start -->
exact-v1 的 `arXiv:2602.03632v1 HTML — §3. The CALM Approach` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 准入、批处理、优先级、路由和资源选择。触发约束是：长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。
<!-- delta:SF-2026-ARXIV-2602-03632:end -->

<!-- books-review:SF-2026-ARXIV-2602-03632:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03632v1 实际披露的机制与实验。方法定位为 arXiv:2602.03632v1 HTML — §3. The CALM Approach；验证定位为 arXiv:2602.03632v1 HTML — §5. Results；边界定位为 arXiv:2602.03632v1 HTML — §7. Threats to Validity。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03632:end -->

<!-- existing:SF-2026-ARXIV-2602-03719:start -->
已对读当前 owner `TRAIN-RLHF` 在 `books/part-04-training-system/31-rlhf.md#rlhfrlaif-与-verifiable-reward (line 491)` 的命题：在每个 episode 清空外部状态，rollout distribution 只需绑定 policy、prompt 和 environment；让 Agent 先生成 tips/memory 并在后续 episode 中读取，会同时改变 observation、exploration path 与 action probability。若随后混合 on-policy 与 replayed/off-policy updates，样本 identity 必须增加 memory content/hash、生成它的 policy/reward revision、read mode、behavior probability、episode lineage 与清空边界。memory generator 只产生 exploration proposal，trajectory store 保存真实 context，learner 根据 support/freshness 决定 update，outcome verifier 仍拥有任务正确性。
<!-- existing:SF-2026-ARXIV-2602-03719:end -->

<!-- delta:SF-2026-ARXIV-2602-03719:start -->
exact-v1 的 `arXiv:2602.03719v1 HTML — §A.1 Algorithm Details` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 rollout、reward、policy/reference 与更新 freshness。触发约束是：模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。
<!-- delta:SF-2026-ARXIV-2602-03719:end -->

<!-- books-review:SF-2026-ARXIV-2602-03719:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03719v1 实际披露的机制与实验。方法定位为 arXiv:2602.03719v1 HTML — §A.1 Algorithm Details；验证定位为 arXiv:2602.03719v1 HTML — §Evaluation.；边界定位为 arXiv:2602.03719v1 HTML — §Appendix D Limitations and Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03719:end -->

<!-- existing:SF-2026-ARXIV-2602-03782:start -->
已对读当前 owner `INFER-TENSORRT-LLM` 在 `books/part-05-inference-system/49-tensorrt-llm.md#量化为什么不自动带来加速 (line 710)` 的命题：#### Embodied phase 可以选择精度，但不能接管物理安全
<!-- existing:SF-2026-ARXIV-2602-03782:end -->

<!-- delta:SF-2026-ARXIV-2602-03782:start -->
exact-v1 的 `arXiv:2602.03782v1 HTML — §3.3 The proposed QVLA` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 graph lowering、kernel/precision 选择与执行计划版本。触发约束是：模型规模、算子形态和 SLO 使执行计划、精度与 kernel 选择成为主要成本。
<!-- delta:SF-2026-ARXIV-2602-03782:end -->

<!-- books-review:SF-2026-ARXIV-2602-03782:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.03782v1 实际披露的机制与实验。方法定位为 arXiv:2602.03782v1 HTML — §3.3 The proposed QVLA；验证定位为 arXiv:2602.03782v1 HTML — §4.2 Comparison with State-of-the-arts；边界定位为 arXiv:2602.03782v1 HTML — §H.2 Behavior During Full-Precision Failure Trials。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-03782:end -->

<!-- existing:SF-2026-ARXIV-2602-02589:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 484)` 的命题：### Judge 从被动 Scorer 演进为有预算的 Evidence Acquisition Policy
<!-- existing:SF-2026-ARXIV-2602-02589:end -->

<!-- delta:SF-2026-ARXIV-2602-02589:start -->
exact-v1 的 `arXiv:2602.02589v1 HTML — §3 Methodology` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-02589:end -->

<!-- books-review:SF-2026-ARXIV-2602-02589:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.02589v1 实际披露的机制与实验。方法定位为 arXiv:2602.02589v1 HTML — §3 Methodology；验证定位为 arXiv:2602.02589v1 HTML — §Ablation: Peer evaluation outperforms self evaluation；边界定位为 arXiv:2602.02589v1 HTML — §6 Discussion。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-02589:end -->

<!-- existing:SF-2026-ARXIV-2602-02690:start -->
已对读当前 owner `PLATFORM-EVALUATION-SYSTEM` 在 `books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 950)` 的命题：## 从答案评分到可执行证据
<!-- existing:SF-2026-ARXIV-2602-02690:end -->

<!-- delta:SF-2026-ARXIV-2602-02690:start -->
exact-v1 的 `arXiv:2602.02690v1 HTML — §3.1 Design` 公开了该 family 的机制边界；本 Review 只据此判断它如何改变 evaluation contract、覆盖分母、evidence lineage 与 release gate。触发约束是：agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。
<!-- delta:SF-2026-ARXIV-2602-02690:end -->

<!-- books-review:SF-2026-ARXIV-2602-02690:start -->
Decision=`No Change — Existing Coverage`：当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。 相邻章节已定位为 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据不得越过：只支持 arXiv:2602.02690v1 实际披露的机制与实验。方法定位为 arXiv:2602.02690v1 HTML — §3.1 Design；验证定位为 arXiv:2602.02690v1 HTML — §5.2 RQ1: Performance difference spanning cutoff；边界定位为 arXiv:2602.02690v1 HTML — §7 Future Work。不外推生产 SLO、多租户、跨硬件或长期可靠性。 本项已由全月 fresh-context receipt 验收。
<!-- books-review:SF-2026-ARXIV-2602-02690:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
<!-- audit-receipt:FCSA-2026-02-FINAL:20260205:start -->
全月验收：`papers/2026/02/_sources/february-fresh-context-audit.json`；本日受审收据：`papers/2026/02/_sources/daily-20260205/screening-ledger-author.json`、`papers/2026/02/_sources/daily-20260205/screening-ledger-final.json`、`papers/2026/02/_sources/daily-20260205/exact-v1-review-packet.json`、`papers/2026/02/_sources/daily-20260205/books-current-content-comparison.json`、`papers/2026/02/_sources/daily-20260205/BOOKS_WRITEBACK_QUEUE.json`。
<!-- audit-receipt:FCSA-2026-02-FINAL:20260205:end -->

| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260205-COVERAGE-FINAL | fresh-context:february-independent-reviewer | coverage | coverage:SRC-ARXIV:20260205; audit-receipt:FCSA-2026-02-FINAL:20260205 | — | 本日 raw=795、retained=24、closures=771；全月 FP/FN、日期与撤稿 finding 均已解决 | passed |
| SA-20260205-EVIDENCE-FINAL | fresh-context:february-independent-reviewer | evidence | review:SF-2026-ARXIV-2602-02579; review:SF-2026-ARXIV-2602-02599; review:SF-2026-ARXIV-2602-02958; review:SF-2026-ARXIV-2602-03036; review:SF-2026-ARXIV-2602-03184; review:SF-2026-ARXIV-2602-03295; review:SF-2026-ARXIV-2602-03560; review:SF-2026-ARXIV-2602-02499; review:SF-2026-ARXIV-2602-02515; review:SF-2026-ARXIV-2602-02574; review:SF-2026-ARXIV-2602-02585; review:SF-2026-ARXIV-2602-02987; review:SF-2026-ARXIV-2602-03025; review:SF-2026-ARXIV-2602-03128; review:SF-2026-ARXIV-2602-03203; review:SF-2026-ARXIV-2602-03255; review:SF-2026-ARXIV-2602-03338; review:SF-2026-ARXIV-2602-03495; review:SF-2026-ARXIV-2602-03580; review:SF-2026-ARXIV-2602-03632; review:SF-2026-ARXIV-2602-03719; review:SF-2026-ARXIV-2602-03782; review:SF-2026-ARXIV-2602-02589; review:SF-2026-ARXIV-2602-02690; audit-receipt:FCSA-2026-02-FINAL:20260205 | — | exact-v1 complete=24、blocked=0；locator、excerpt、RP 与 claim boundary 已验收 | passed |
| SA-20260205-SELECTION-FINAL | fresh-context:february-independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1; audit-receipt:FCSA-2026-02-FINAL:20260205 | — | 本日完整 eligibility frontier 与最多三个叙事单元已验收，未选择项均保留显式理由 | passed |
| SA-20260205-BOOKS-POSTWRITE-FINAL | fresh-context:february-independent-reviewer | books | books-review:SF-2026-ARXIV-2602-02579; books-review:SF-2026-ARXIV-2602-02599; books-review:SF-2026-ARXIV-2602-02958; books-review:SF-2026-ARXIV-2602-03036; books-review:SF-2026-ARXIV-2602-03184; books-review:SF-2026-ARXIV-2602-03295; books-review:SF-2026-ARXIV-2602-03560; books-review:SF-2026-ARXIV-2602-02499; books-review:SF-2026-ARXIV-2602-02515; books-review:SF-2026-ARXIV-2602-02574; books-review:SF-2026-ARXIV-2602-02585; books-review:SF-2026-ARXIV-2602-02987; books-review:SF-2026-ARXIV-2602-03025; books-review:SF-2026-ARXIV-2602-03128; books-review:SF-2026-ARXIV-2602-03203; books-review:SF-2026-ARXIV-2602-03255; books-review:SF-2026-ARXIV-2602-03338; books-review:SF-2026-ARXIV-2602-03495; books-review:SF-2026-ARXIV-2602-03580; books-review:SF-2026-ARXIV-2602-03632; books-review:SF-2026-ARXIV-2602-03719; books-review:SF-2026-ARXIV-2602-03782; books-review:SF-2026-ARXIV-2602-02589; books-review:SF-2026-ARXIV-2602-02690; audit-receipt:FCSA-2026-02-FINAL:20260205 | — | 本日 Integrate=2；canonical owner、相邻命题、disposition 与 post-write/no-writeback 状态已验收 | passed |

## 8. Ignored Noise

771 个 pre-denominator closure 保存在 `papers/2026/02/_sources/daily-20260205/screening-ledger-final.json`；每项含 identity、title、abstract 与 family-specific reason。withdrawn=0，撤稿不留 selected 痕迹。

## 9. Recommended Action

本日四域 Gate 已关闭；保留 `papers/2026/02/_sources/february-fresh-context-audit.json` 与本地冻结收据。仅在 primary evidence、撤稿状态或公共合同变化时重新打开对应 scope。

## 10. Repository Changes

- promotion 更新 `papers/2026/02/05/README.md` 与本日 `_sources` 最终状态收据。
- 本步骤不修改 Books 或 Weekly，也不 stage、commit 或 push；此前已验收的 Books 写回由本日 queue 记录 post-write 状态。

## 11. Open Questions

- 无 Gate 阻塞项；论文自身未证明的边界继续保留在 Claim Boundary 中，不构成未解决流程 finding。

## 12. Sources

- [arXiv:2602.02579v1](https://arxiv.org/abs/2602.02579v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.02599v1](https://arxiv.org/abs/2602.02599v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.02958v1](https://arxiv.org/abs/2602.02958v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03036v1](https://arxiv.org/abs/2602.03036v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03184v1](https://arxiv.org/abs/2602.03184v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03295v1](https://arxiv.org/abs/2602.03295v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03560v1](https://arxiv.org/abs/2602.03560v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.02499v1](https://arxiv.org/abs/2602.02499v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.02515v1](https://arxiv.org/abs/2602.02515v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.02574v1](https://arxiv.org/abs/2602.02574v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.02585v1](https://arxiv.org/abs/2602.02585v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.02987v1](https://arxiv.org/abs/2602.02987v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03025v1](https://arxiv.org/abs/2602.03025v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03128v1](https://arxiv.org/abs/2602.03128v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03203v1](https://arxiv.org/abs/2602.03203v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03255v1](https://arxiv.org/abs/2602.03255v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03338v1](https://arxiv.org/abs/2602.03338v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03495v1](https://arxiv.org/abs/2602.03495v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03580v1](https://arxiv.org/abs/2602.03580v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03632v1](https://arxiv.org/abs/2602.03632v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03719v1](https://arxiv.org/abs/2602.03719v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.03782v1](https://arxiv.org/abs/2602.03782v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.02589v1](https://arxiv.org/abs/2602.02589v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。
- [arXiv:2602.02690v1](https://arxiv.org/abs/2602.02690v1) — official exact-v1；first-public `2026-02-04T09:00:00+08:00`；访问日期 2026-09-02。

## 13. Final Status

Completion Status=`Complete`；Coverage=`Closed`；Evidence=`Passed`；Books=`Passed`；Unresolved Findings=0。最终 raw=795、retained=24、closures=771、exact-v1 reviews=24、blocked=0。
