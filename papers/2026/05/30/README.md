# Daily Research — 2026-05-30

**Research Date:** 2026-05-30

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-29 09:00:00 ～ 2026-05-30 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；technical claims bind official arXiv exact-v1 HTML/PDF。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。最终 13 项已完成共享 Books 写回并通过独立 13/13 post-write semantic audit。

## Executive Summary

从 91,841 条月度 raw records 中恢复并逐项语义筛选 730/730 个窗口身份；author denominator=103 经独立审计后为 121，pre-denominator closures=609，exact-v1=121/121，blocked=0。fresh-context challenge 将 Books queue 从 29 收紧为最终 13 项；13/13 已写回并通过独立 post-write semantic audit。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-30 |
| Window End | 2026-05-30 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260530-V2-INDEPENDENT-121 |
| Denominator Frozen At | 2026-09-01T06:44:58+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-29T09:00:00+08:00 | 2026-05-30T09:00:00+08:00 | 2026-09-01T04:33:46.738417+00:00 | DataCite v2 00..99 + 730/730 semantic replay + official exact-v1 HTML/PDF | checked | 730 | SF-2026-ARXIV-2606-00144;SF-2026-ARXIV-2606-00150;SF-2026-ARXIV-2606-00152;SF-2026-ARXIV-2606-00160;SF-2026-ARXIV-2606-00162;SF-2026-ARXIV-2606-00172;SF-2026-ARXIV-2606-00183;SF-2026-ARXIV-2606-00186;SF-2026-ARXIV-2606-00189;SF-2026-ARXIV-2606-00198;SF-2026-ARXIV-2606-00206;SF-2026-ARXIV-2606-00229;SF-2026-ARXIV-2606-00232;SF-2026-ARXIV-2606-00251;SF-2026-ARXIV-2606-00257;SF-2026-ARXIV-2606-00267;SF-2026-ARXIV-2606-00269;SF-2026-ARXIV-2606-00271;SF-2026-ARXIV-2606-00279;SF-2026-ARXIV-2606-00284;SF-2026-ARXIV-2606-00301;SF-2026-ARXIV-2606-00305;SF-2026-ARXIV-2606-00308;SF-2026-ARXIV-2606-00318;SF-2026-ARXIV-2606-00329;SF-2026-ARXIV-2606-00341;SF-2026-ARXIV-2606-00348;SF-2026-ARXIV-2606-00365;SF-2026-ARXIV-2606-00376;SF-2026-ARXIV-2606-00380;SF-2026-ARXIV-2606-00382;SF-2026-ARXIV-2606-00392;SF-2026-ARXIV-2606-00395;SF-2026-ARXIV-2606-00400;SF-2026-ARXIV-2606-00408;SF-2026-ARXIV-2606-00414;SF-2026-ARXIV-2606-00424;SF-2026-ARXIV-2606-00432;SF-2026-ARXIV-2606-00437;SF-2026-ARXIV-2606-00439;SF-2026-ARXIV-2606-00448;SF-2026-ARXIV-2606-00457;SF-2026-ARXIV-2606-07595;SF-2026-ARXIV-2606-07603;SF-2026-ARXIV-2606-07616;SF-2026-ARXIV-2606-20631;SF-2026-ARXIV-2606-24893;SF-2026-ARXIV-2606-28337;SF-2026-ARXIV-2605-30711;SF-2026-ARXIV-2605-30712;SF-2026-ARXIV-2605-30723;SF-2026-ARXIV-2605-30727;SF-2026-ARXIV-2605-30728;SF-2026-ARXIV-2605-30736;SF-2026-ARXIV-2605-30738;SF-2026-ARXIV-2605-30753;SF-2026-ARXIV-2605-30757;SF-2026-ARXIV-2605-30771;SF-2026-ARXIV-2605-30777;SF-2026-ARXIV-2605-30785;SF-2026-ARXIV-2605-30789;SF-2026-ARXIV-2605-30790;SF-2026-ARXIV-2605-30803;SF-2026-ARXIV-2605-30807;SF-2026-ARXIV-2605-30824;SF-2026-ARXIV-2605-30832;SF-2026-ARXIV-2605-30833;SF-2026-ARXIV-2605-30834;SF-2026-ARXIV-2605-30837;SF-2026-ARXIV-2605-30838;SF-2026-ARXIV-2605-30842;SF-2026-ARXIV-2605-30851;SF-2026-ARXIV-2605-30852;SF-2026-ARXIV-2605-30854;SF-2026-ARXIV-2605-30855;SF-2026-ARXIV-2605-30859;SF-2026-ARXIV-2605-30880;SF-2026-ARXIV-2605-30883;SF-2026-ARXIV-2605-30888;SF-2026-ARXIV-2605-30896;SF-2026-ARXIV-2605-30898;SF-2026-ARXIV-2605-30911;SF-2026-ARXIV-2605-30917;SF-2026-ARXIV-2605-30924;SF-2026-ARXIV-2605-30998;SF-2026-ARXIV-2605-31033;SF-2026-ARXIV-2605-31042;SF-2026-ARXIV-2605-31058;SF-2026-ARXIV-2605-31066;SF-2026-ARXIV-2605-31073;SF-2026-ARXIV-2605-31086;SF-2026-ARXIV-2605-31105;SF-2026-ARXIV-2605-31111;SF-2026-ARXIV-2605-31158;SF-2026-ARXIV-2605-31159;SF-2026-ARXIV-2605-31164;SF-2026-ARXIV-2605-31167;SF-2026-ARXIV-2605-31170;SF-2026-ARXIV-2605-31175;SF-2026-ARXIV-2605-31176;SF-2026-ARXIV-2605-31244;SF-2026-ARXIV-2605-31264;SF-2026-ARXIV-2605-31278;SF-2026-ARXIV-2605-31308;SF-2026-ARXIV-2605-31328;SF-2026-ARXIV-2605-31354;SF-2026-ARXIV-2605-31361;SF-2026-ARXIV-2605-31365;SF-2026-ARXIV-2605-31381;SF-2026-ARXIV-2605-31408;SF-2026-ARXIV-2605-31455;SF-2026-ARXIV-2605-31460;SF-2026-ARXIV-2605-31463;SF-2026-ARXIV-2605-31464;SF-2026-ARXIV-2605-31468;SF-2026-ARXIV-2605-31490;SF-2026-ARXIV-2605-31509;SF-2026-ARXIV-2605-31557;SF-2026-ARXIV-2605-31584;SF-2026-ARXIV-2605-31593;SF-2026-ARXIV-2605-31598 | pages=300;final_cursor=end;raw=91841;registered=730;screened=730;retained=121;closure=609 | 2026-05-30T00:59:59Z | screening-ledger-final.json#sha256=acf722f7e80c34142e9b0819fcb03e0ffecdebd6b9f0257a91ff99865fec8131 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260530:start -->Independent reviewer 已重放 730/730：author denominator 103→final 121（FP=0、FN=18），609 个 family-specific closures 与 121/121 exact-v1 review 均已闭合；ordinary pending=0、external blocker=0。<!-- coverage:SRC-ARXIV:20260530:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-00144 | arXiv:2606.00144v1 | paper-v1:2606.00144 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00144 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00144 | no |
| SF-2026-ARXIV-2606-00150 | arXiv:2606.00150v1 | paper-v1:2606.00150 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00150 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00150 | no |
| SF-2026-ARXIV-2606-00152 | arXiv:2606.00152v1 | paper-v1:2606.00152 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00152 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00152 | no |
| SF-2026-ARXIV-2606-00160 | arXiv:2606.00160v1 | paper-v1:2606.00160 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00160 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-00160 | no |
| SF-2026-ARXIV-2606-00162 | arXiv:2606.00162v1 | paper-v1:2606.00162 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00162 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00162 | no |
| SF-2026-ARXIV-2606-00172 | arXiv:2606.00172v1 | paper-v1:2606.00172 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00172 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00172 | no |
| SF-2026-ARXIV-2606-00183 | arXiv:2606.00183v1 | paper-v1:2606.00183 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00183 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00183 | no |
| SF-2026-ARXIV-2606-00186 | arXiv:2606.00186v1 | paper-v1:2606.00186 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00186 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00186 | no |
| SF-2026-ARXIV-2606-00189 | arXiv:2606.00189v1 | paper-v1:2606.00189 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00189 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00189 | no |
| SF-2026-ARXIV-2606-00198 | arXiv:2606.00198v1 | paper-v1:2606.00198 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00198 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00198 | no |
| SF-2026-ARXIV-2606-00206 | arXiv:2606.00206v1 | paper-v1:2606.00206 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00206 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00206 | no |
| SF-2026-ARXIV-2606-00229 | arXiv:2606.00229v1 | paper-v1:2606.00229 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00229 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00229 | no |
| SF-2026-ARXIV-2606-00232 | arXiv:2606.00232v1 | paper-v1:2606.00232 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00232 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00232 | no |
| SF-2026-ARXIV-2606-00251 | arXiv:2606.00251v1 | paper-v1:2606.00251 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00251 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00251 | no |
| SF-2026-ARXIV-2606-00257 | arXiv:2606.00257v1 | paper-v1:2606.00257 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00257 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2606-00257 | no |
| SF-2026-ARXIV-2606-00267 | arXiv:2606.00267v1 | paper-v1:2606.00267 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00267 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00267 | no |
| SF-2026-ARXIV-2606-00269 | arXiv:2606.00269v1 | paper-v1:2606.00269 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00269 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00269 | no |
| SF-2026-ARXIV-2606-00271 | arXiv:2606.00271v1 | paper-v1:2606.00271 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00271 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-00271 | no |
| SF-2026-ARXIV-2606-00279 | arXiv:2606.00279v1 | paper-v1:2606.00279 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00279 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-00279 | no |
| SF-2026-ARXIV-2606-00284 | arXiv:2606.00284v1 | paper-v1:2606.00284 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00284 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00284 | no |
| SF-2026-ARXIV-2606-00301 | arXiv:2606.00301v1 | paper-v1:2606.00301 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00301 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00301 | no |
| SF-2026-ARXIV-2606-00305 | arXiv:2606.00305v1 | paper-v1:2606.00305 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00305 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00305 | no |
| SF-2026-ARXIV-2606-00308 | arXiv:2606.00308v1 | paper-v1:2606.00308 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00308 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00308 | no |
| SF-2026-ARXIV-2606-00318 | arXiv:2606.00318v1 | paper-v1:2606.00318 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00318 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-00318 | no |
| SF-2026-ARXIV-2606-00329 | arXiv:2606.00329v1 | paper-v1:2606.00329 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00329 | self | — | new_in_window | PLATFORM-MONITORING | Weekly Only — Context | books-review:SF-2026-ARXIV-2606-00329 | no |
| SF-2026-ARXIV-2606-00341 | arXiv:2606.00341v1 | paper-v1:2606.00341 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00341 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00341 | no |
| SF-2026-ARXIV-2606-00348 | arXiv:2606.00348v1 | paper-v1:2606.00348 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00348 | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00348 | no |
| SF-2026-ARXIV-2606-00365 | arXiv:2606.00365v1 | paper-v1:2606.00365 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00365 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00365 | no |
| SF-2026-ARXIV-2606-00376 | arXiv:2606.00376v1 | paper-v1:2606.00376 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00376 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00376 | no |
| SF-2026-ARXIV-2606-00380 | arXiv:2606.00380v1 | paper-v1:2606.00380 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00380 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00380 | no |
| SF-2026-ARXIV-2606-00382 | arXiv:2606.00382v1 | paper-v1:2606.00382 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00382 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00382 | no |
| SF-2026-ARXIV-2606-00392 | arXiv:2606.00392v1 | paper-v1:2606.00392 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00392 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00392 | no |
| SF-2026-ARXIV-2606-00395 | arXiv:2606.00395v1 | paper-v1:2606.00395 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00395 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00395 | no |
| SF-2026-ARXIV-2606-00400 | arXiv:2606.00400v1 | paper-v1:2606.00400 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00400 | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-ARXIV-2606-00400 | no |
| SF-2026-ARXIV-2606-00408 | arXiv:2606.00408v1 | paper-v1:2606.00408 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00408 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00408 | no |
| SF-2026-ARXIV-2606-00414 | arXiv:2606.00414v1 | paper-v1:2606.00414 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00414 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00414 | no |
| SF-2026-ARXIV-2606-00424 | arXiv:2606.00424v1 | paper-v1:2606.00424 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00424 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00424 | no |
| SF-2026-ARXIV-2606-00432 | arXiv:2606.00432v1 | paper-v1:2606.00432 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00432 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00432 | no |
| SF-2026-ARXIV-2606-00437 | arXiv:2606.00437v1 | paper-v1:2606.00437 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00437 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-00437 | no |
| SF-2026-ARXIV-2606-00439 | arXiv:2606.00439v1 | paper-v1:2606.00439 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-00439 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00439 | no |
| SF-2026-ARXIV-2606-00448 | arXiv:2606.00448v1 | paper-v1:2606.00448 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00448 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00448 | no |
| SF-2026-ARXIV-2606-00457 | arXiv:2606.00457v1 | paper-v1:2606.00457 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-00457 | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00457 | no |
| SF-2026-ARXIV-2606-07595 | arXiv:2606.07595v1 | paper-v1:2606.07595 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-07595 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07595 | no |
| SF-2026-ARXIV-2606-07603 | arXiv:2606.07603v1 | paper-v1:2606.07603 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07603 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07603 | no |
| SF-2026-ARXIV-2606-07616 | arXiv:2606.07616v1 | paper-v1:2606.07616 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-07616 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07616 | no |
| SF-2026-ARXIV-2606-20631 | arXiv:2606.20631v1 | paper-v1:2606.20631 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20631 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20631 | no |
| SF-2026-ARXIV-2606-24893 | arXiv:2606.24893v1 | paper-v1:2606.24893 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-24893 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-24893 | no |
| SF-2026-ARXIV-2606-28337 | arXiv:2606.28337v1 | paper-v1:2606.28337 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-28337 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28337 | no |
| SF-2026-ARXIV-2605-30711 | arXiv:2605.30711v1 | paper-v1:2605.30711 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30711 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30711 | no |
| SF-2026-ARXIV-2605-30712 | arXiv:2605.30712v1 | paper-v1:2605.30712 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30712 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30712 | no |
| SF-2026-ARXIV-2605-30723 | arXiv:2605.30723v1 | paper-v1:2605.30723 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30723 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30723 | no |
| SF-2026-ARXIV-2605-30727 | arXiv:2605.30727v1 | paper-v1:2605.30727 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-30727 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-30727 | no |
| SF-2026-ARXIV-2605-30728 | arXiv:2605.30728v1 | paper-v1:2605.30728 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30728 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30728 | no |
| SF-2026-ARXIV-2605-30736 | arXiv:2605.30736v1 | paper-v1:2605.30736 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30736 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30736 | no |
| SF-2026-ARXIV-2605-30738 | arXiv:2605.30738v1 | paper-v1:2605.30738 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30738 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30738 | no |
| SF-2026-ARXIV-2605-30753 | arXiv:2605.30753v1 | paper-v1:2605.30753 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30753 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30753 | no |
| SF-2026-ARXIV-2605-30757 | arXiv:2605.30757v1 | paper-v1:2605.30757 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30757 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30757 | no |
| SF-2026-ARXIV-2605-30771 | arXiv:2605.30771v1 | paper-v1:2605.30771 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30771 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30771 | no |
| SF-2026-ARXIV-2605-30777 | arXiv:2605.30777v1 | paper-v1:2605.30777 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30777 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30777 | no |
| SF-2026-ARXIV-2605-30785 | arXiv:2605.30785v1 | paper-v1:2605.30785 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30785 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30785 | no |
| SF-2026-ARXIV-2605-30789 | arXiv:2605.30789v1 | paper-v1:2605.30789 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-30789 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2605-30789 | no |
| SF-2026-ARXIV-2605-30790 | arXiv:2605.30790v1 | paper-v1:2605.30790 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-30790 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30790 | no |
| SF-2026-ARXIV-2605-30803 | arXiv:2605.30803v1 | paper-v1:2605.30803 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30803 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30803 | no |
| SF-2026-ARXIV-2605-30807 | arXiv:2605.30807v1 | paper-v1:2605.30807 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30807 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30807 | no |
| SF-2026-ARXIV-2605-30824 | arXiv:2605.30824v1 | paper-v1:2605.30824 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30824 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30824 | no |
| SF-2026-ARXIV-2605-30832 | arXiv:2605.30832v1 | paper-v1:2605.30832 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30832 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30832 | no |
| SF-2026-ARXIV-2605-30833 | arXiv:2605.30833v1 | paper-v1:2605.30833 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30833 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30833 | no |
| SF-2026-ARXIV-2605-30834 | arXiv:2605.30834v1 | paper-v1:2605.30834 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-30834 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30834 | no |
| SF-2026-ARXIV-2605-30837 | arXiv:2605.30837v1 | paper-v1:2605.30837 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-30837 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30837 | no |
| SF-2026-ARXIV-2605-30838 | arXiv:2605.30838v1 | paper-v1:2605.30838 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30838 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30838 | no |
| SF-2026-ARXIV-2605-30842 | arXiv:2605.30842v1 | paper-v1:2605.30842 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30842 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30842 | no |
| SF-2026-ARXIV-2605-30851 | arXiv:2605.30851v1 | paper-v1:2605.30851 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-30851 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-30851 | no |
| SF-2026-ARXIV-2605-30852 | arXiv:2605.30852v1 | paper-v1:2605.30852 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-30852 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30852 | no |
| SF-2026-ARXIV-2605-30854 | arXiv:2605.30854v1 | paper-v1:2605.30854 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30854 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30854 | no |
| SF-2026-ARXIV-2605-30855 | arXiv:2605.30855v1 | paper-v1:2605.30855 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30855 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30855 | no |
| SF-2026-ARXIV-2605-30859 | arXiv:2605.30859v1 | paper-v1:2605.30859 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30859 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30859 | no |
| SF-2026-ARXIV-2605-30880 | arXiv:2605.30880v1 | paper-v1:2605.30880 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-30880 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30880 | no |
| SF-2026-ARXIV-2605-30883 | arXiv:2605.30883v1 | paper-v1:2605.30883 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30883 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30883 | no |
| SF-2026-ARXIV-2605-30888 | arXiv:2605.30888v1 | paper-v1:2605.30888 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30888 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30888 | no |
| SF-2026-ARXIV-2605-30896 | arXiv:2605.30896v1 | paper-v1:2605.30896 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30896 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30896 | no |
| SF-2026-ARXIV-2605-30898 | arXiv:2605.30898v1 | paper-v1:2605.30898 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-30898 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-30898 | no |
| SF-2026-ARXIV-2605-30911 | arXiv:2605.30911v1 | paper-v1:2605.30911 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30911 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30911 | no |
| SF-2026-ARXIV-2605-30917 | arXiv:2605.30917v1 | paper-v1:2605.30917 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30917 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30917 | no |
| SF-2026-ARXIV-2605-30924 | arXiv:2605.30924v1 | paper-v1:2605.30924 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30924 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30924 | no |
| SF-2026-ARXIV-2605-30998 | arXiv:2605.30998v1 | paper-v1:2605.30998 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-30998 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30998 | no |
| SF-2026-ARXIV-2605-31033 | arXiv:2605.31033v1 | paper-v1:2605.31033 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31033 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31033 | no |
| SF-2026-ARXIV-2605-31042 | arXiv:2605.31042v1 | paper-v1:2605.31042 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-31042 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-31042 | no |
| SF-2026-ARXIV-2605-31058 | arXiv:2605.31058v1 | paper-v1:2605.31058 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31058 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31058 | no |
| SF-2026-ARXIV-2605-31066 | arXiv:2605.31066v1 | paper-v1:2605.31066 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31066 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31066 | no |
| SF-2026-ARXIV-2605-31073 | arXiv:2605.31073v1 | paper-v1:2605.31073 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31073 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31073 | no |
| SF-2026-ARXIV-2605-31086 | arXiv:2605.31086v1 | paper-v1:2605.31086 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31086 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31086 | no |
| SF-2026-ARXIV-2605-31105 | arXiv:2605.31105v1 | paper-v1:2605.31105 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31105 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31105 | no |
| SF-2026-ARXIV-2605-31111 | arXiv:2605.31111v1 | paper-v1:2605.31111 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31111 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31111 | no |
| SF-2026-ARXIV-2605-31158 | arXiv:2605.31158v1 | paper-v1:2605.31158 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31158 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31158 | no |
| SF-2026-ARXIV-2605-31159 | arXiv:2605.31159v1 | paper-v1:2605.31159 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31159 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31159 | no |
| SF-2026-ARXIV-2605-31164 | arXiv:2605.31164v1 | paper-v1:2605.31164 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31164 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31164 | no |
| SF-2026-ARXIV-2605-31167 | arXiv:2605.31167v1 | paper-v1:2605.31167 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31167 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31167 | no |
| SF-2026-ARXIV-2605-31170 | arXiv:2605.31170v1 | paper-v1:2605.31170 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-31170 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31170 | no |
| SF-2026-ARXIV-2605-31175 | arXiv:2605.31175v1 | paper-v1:2605.31175 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31175 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31175 | no |
| SF-2026-ARXIV-2605-31176 | arXiv:2605.31176v1 | paper-v1:2605.31176 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31176 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31176 | no |
| SF-2026-ARXIV-2605-31244 | arXiv:2605.31244v1 | paper-v1:2605.31244 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31244 | self | — | new_in_window | WORLDVIEW-SCALING-LAW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31244 | no |
| SF-2026-ARXIV-2605-31264 | arXiv:2605.31264v1 | paper-v1:2605.31264 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31264 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31264 | no |
| SF-2026-ARXIV-2605-31278 | arXiv:2605.31278v1 | paper-v1:2605.31278 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31278 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31278 | no |
| SF-2026-ARXIV-2605-31308 | arXiv:2605.31308v1 | paper-v1:2605.31308 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31308 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31308 | no |
| SF-2026-ARXIV-2605-31328 | arXiv:2605.31328v1 | paper-v1:2605.31328 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31328 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31328 | no |
| SF-2026-ARXIV-2605-31354 | arXiv:2605.31354v1 | paper-v1:2605.31354 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31354 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31354 | no |
| SF-2026-ARXIV-2605-31361 | arXiv:2605.31361v1 | paper-v1:2605.31361 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31361 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31361 | no |
| SF-2026-ARXIV-2605-31365 | arXiv:2605.31365v1 | paper-v1:2605.31365 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31365 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31365 | no |
| SF-2026-ARXIV-2605-31381 | arXiv:2605.31381v1 | paper-v1:2605.31381 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31381 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31381 | no |
| SF-2026-ARXIV-2605-31408 | arXiv:2605.31408v1 | paper-v1:2605.31408 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31408 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31408 | no |
| SF-2026-ARXIV-2605-31455 | arXiv:2605.31455v1 | paper-v1:2605.31455 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31455 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31455 | no |
| SF-2026-ARXIV-2605-31460 | arXiv:2605.31460v1 | paper-v1:2605.31460 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31460 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31460 | no |
| SF-2026-ARXIV-2605-31463 | arXiv:2605.31463v1 | paper-v1:2605.31463 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31463 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31463 | no |
| SF-2026-ARXIV-2605-31464 | arXiv:2605.31464v1 | paper-v1:2605.31464 | 2026-W22 | 2026-05-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31464 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31464 | no |
| SF-2026-ARXIV-2605-31468 | arXiv:2605.31468v1 | paper-v1:2605.31468 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31468 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31468 | no |
| SF-2026-ARXIV-2605-31490 | arXiv:2605.31490v1 | paper-v1:2605.31490 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31490 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31490 | no |
| SF-2026-ARXIV-2605-31509 | arXiv:2605.31509v1 | paper-v1:2605.31509 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31509 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31509 | no |
| SF-2026-ARXIV-2605-31557 | arXiv:2605.31557v1 | paper-v1:2605.31557 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-31557 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31557 | no |
| SF-2026-ARXIV-2605-31584 | arXiv:2605.31584v1 | paper-v1:2605.31584 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-31584 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31584 | no |
| SF-2026-ARXIV-2605-31593 | arXiv:2605.31593v1 | paper-v1:2605.31593 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-31593 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31593 | no |
| SF-2026-ARXIV-2605-31598 | arXiv:2605.31598v1 | paper-v1:2605.31598 | 2026-W22 | 2026-05-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-31598 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-31598 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-00144 | RP-44c990372d1f31a4 | deep | arXiv:2606.00144v1 | SRC-ARXIV@arXiv:2606.00144v1 | arXiv:2606.00144v1 HTML — §3 Method | arXiv:2606.00144v1 HTML — §4 Experimental Setup; §5 Experimental Results; §5.4 Sensitivity Analysis | arXiv:2606.00144v1 HTML — §6 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00144v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00144 | complete |
| SF-2026-ARXIV-2606-00150 | RP-da862b578cfba99e | deep | arXiv:2606.00150v1 | SRC-ARXIV@arXiv:2606.00150v1 | arXiv:2606.00150v1 HTML — §3 Proposed Method: Persona Attack | arXiv:2606.00150v1 HTML — §4 Empirical Experiments; §4.1 Experimental setup; §4.2 Experimental Results | arXiv:2606.00150v1 HTML — §5 Discussion; §5.1 Limitation; §6 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00150v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00150 | complete |
| SF-2026-ARXIV-2606-00152 | RP-4400d16c4d57b20d | deep | arXiv:2606.00152v1 | SRC-ARXIV@arXiv:2606.00152v1 | arXiv:2606.00152v1 HTML — §6 Mitigation Methods | arXiv:2606.00152v1 HTML — §3.3 Evaluation; §4 Experiments; §4.2 Main Results | arXiv:2606.00152v1 HTML — §7 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00152v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00152 | complete |
| SF-2026-ARXIV-2606-00160 | RP-3595ed13b8d0fa39 | deep | arXiv:2606.00160v1 | SRC-ARXIV@arXiv:2606.00160v1 | arXiv:2606.00160v1 HTML — §IV Method; excerpt= of LLMs? III-B What does the benign fine-tuning change? IV Method IV-A Promblem Formulation IV-B Compliance Vector Extraction IV-C Safety-Critical Layers Selection IV-D Safety-Degrading Data Filtering V Experiment V-A Experimental Setup V-B Comparative Methods V-C Effectiveness of Safety-degrading Data Selection V-D Safety Performance After Filtering Safety-degrading Samples V-E Effectiveness Analysis of Layer Selection V-F Effectivene | arXiv:2606.00160v1 HTML — §III Mechanistic Interpretability Analysis; excerpt=cal Layers Selection IV-D Safety-Degrading Data Filtering V Experiment V-A Experimental Setup V-B Comparative Methods V-C Effectiveness of Safety-degrading Data Selection V-D Safety Performance After Filtering Safety-degrading Samples V-E Effectiveness Analysis of Layer Selection V-F Effectiveness Analysis of Projection Difference V-G Safety-degrading Data Features V-H Harmful Topic Category V-I KL Divergence Analysis of Safety-degradin | arXiv:2606.00160v1 HTML — §VI Conclusion; excerpt=e importantly, the fundamental mechanisms behind LLM safety failure caused by benign fine-tuning remain insufficiently explored. To this end, we aim to address the safety degradation caused by benign fine-tuning from a data-centric perspective. Specifically, this paper focuses on the following research questions: RQ1: What are the underlying mechanisms driving safety degradation during the benign fine-tuning of LLMs? RQ2: How can we eff | https://arxiv.org/html/2606.00160v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.00160v1.html; sha256:8decd2edb0853ee74738670195b66a946b7cd1247f350171a1d27fae552fff85 | claim:SF-2026-ARXIV-2606-00160 | complete |
| SF-2026-ARXIV-2606-00162 | RP-50b1ff7402614de3 | deep | arXiv:2606.00162v1 | SRC-ARXIV@arXiv:2606.00162v1 | arXiv:2606.00162v1 HTML — §III Methodology | arXiv:2606.00162v1 HTML — §V Experimental Setup; §VI Results | arXiv:2606.00162v1 HTML — §VII Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00162v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00162 | complete |
| SF-2026-ARXIV-2606-00172 | RP-113992e6cdaf6e85 | deep | arXiv:2606.00172v1 | SRC-ARXIV@arXiv:2606.00172v1 | arXiv:2606.00172v1 HTML — §3 Method | arXiv:2606.00172v1 HTML — §4 Experiments; §4.2 Results; §8.6 Evaluation Details | arXiv:2606.00172v1 HTML — §6 Limitations; §7 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00172v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00172 | complete |
| SF-2026-ARXIV-2606-00183 | RP-933bd13b73ceaa7c | deep | arXiv:2606.00183v1 | SRC-ARXIV@arXiv:2606.00183v1 | arXiv:2606.00183v1 HTML — §2.2 Transformer Architecture; §Transformer architecture and multi-turn reasoning. | arXiv:2606.00183v1 HTML — §5 Numerical Experiments; §Results. | arXiv:2606.00183v1 HTML — §6 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00183v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00183 | complete |
| SF-2026-ARXIV-2606-00186 | RP-7f0ebc024a0887d1 | deep | arXiv:2606.00186v1 | SRC-ARXIV@arXiv:2606.00186v1 | arXiv:2606.00186v1 HTML — §3 Framework Implementation; excerpt=veloper Centered Security 2.3 Comparing Human to LLM code 3 Framework Implementation 3.1 Creating and Collecting Code 3.2 Framework Design 3.2.1 Reproducibility and Auditing 3.2.2 Containers for Security and Reproducibility 3.3 Framework Results 3.3.1 Species Fair Integrity 3.3.2 Research Utility and Framework Benefits 4 Feasibility Study 4.1 Exercise selection 4.1.1 Human Code Data sources 4.1.2 LLM Code Generation 4.1.3 Handling Error | arXiv:2606.00186v1 HTML — §2.1.1 Run-time Analysis for Errors and Correctness; excerpt=2 Containers for Security and Reproducibility 3.3 Framework Results 3.3.1 Species Fair Integrity 3.3.2 Research Utility and Framework Benefits 4 Feasibility Study 4.1 Exercise selection 4.1.1 Human Code Data sources 4.1.2 LLM Code Generation 4.1.3 Handling Errors 4.2 Feasibility Study Results 4.2.1 Data Analysis 4.2.2 Correctness 4.2.3 Failure Mode 4.2.4 Clarity 4.2.5 Security 5 Discussion 5.1 Limitations 5.2 Future Work 5.3 Ethical Con | arXiv:2606.00186v1 HTML — §4.2.3 Failure Mode; excerpt=y Study Results 4.2.1 Data Analysis 4.2.2 Correctness 4.2.3 Failure Mode 4.2.4 Clarity 4.2.5 Security 5 Discussion 5.1 Limitations 5.2 Future Work 5.3 Ethical Considerations References A Appendix: Framework and Metrics A.1 Ruff Linter Security Codes B Appendix: LLM Information C Appendix: Coding Exercises License: arXiv.org perpetual non-exclusive license arXiv:2606.00186v1 [cs.CR] 29 May 2026 *1 How to Compare the Security of Code Writ | https://arxiv.org/html/2606.00186v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.00186v1.html; sha256:0fdc2d369a4ef09db62ef07d1b3ed04c3205763b258858f5449ef9149700fe3b | claim:SF-2026-ARXIV-2606-00186 | complete |
| SF-2026-ARXIV-2606-00189 | RP-b71daada7cf68384 | deep | arXiv:2606.00189v1 | SRC-ARXIV@arXiv:2606.00189v1 | arXiv:2606.00189v1 HTML — §3 Methods; §3.1 Framework; §3.2 Learning and optimization methods | arXiv:2606.00189v1 HTML — §4 Experimental results; §Appendix A Description of benchmarks; §A.1 Benchmarks used | arXiv:2606.00189v1 HTML — §5 Limitations and broader impacts; §6 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00189v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00189 | complete |
| SF-2026-ARXIV-2606-00198 | RP-370e52300b89356b | deep | arXiv:2606.00198v1 | SRC-ARXIV@arXiv:2606.00198v1 | arXiv:2606.00198v1 HTML — §1 Introduction | arXiv:2606.00198v1 HTML — §3.4 Experimental Setup; §Appendix B Detailed Experimental Settings; §B.2 Evaluation Protocol | arXiv:2606.00198v1 HTML — §8 Conclusion and Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00198v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00198 | complete |
| SF-2026-ARXIV-2606-00206 | RP-a9ee52629ef52923 | deep | arXiv:2606.00206v1 | SRC-ARXIV@arXiv:2606.00206v1 | arXiv:2606.00206v1 HTML — §A.2 Quantization Methods | arXiv:2606.00206v1 HTML — §3 Experimental Setup; §Appendix A Experimental Details; §Appendix B Additional Results | arXiv:2606.00206v1 HTML — §7 Conclusion, Limitations, and Future Work | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00206v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00206 | complete |
| SF-2026-ARXIV-2606-00229 | RP-ff7d28f392f88042 | deep | arXiv:2606.00229v1 | SRC-ARXIV@arXiv:2606.00229v1 | arXiv:2606.00229v1 HTML — §1. Introduction | arXiv:2606.00229v1 HTML — §4. Experiments; §Real-robot evaluation.; §Appendix A Experimental Configuration | arXiv:2606.00229v1 HTML — §5. Conclusions | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00229v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00229 | complete |
| SF-2026-ARXIV-2606-00232 | RP-eb4f5a9a8ef208ba | deep | arXiv:2606.00232v1 | SRC-ARXIV@arXiv:2606.00232v1 | arXiv:2606.00232v1 HTML — §3 Methodology; §E.4 Mechanism Analysis Methodology | arXiv:2606.00232v1 HTML — §4 Experimental Evaluation; §4.1 Experimental Setup; §4.2 Main Results (RQ1) | arXiv:2606.00232v1 HTML — §5 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00232v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00232 | complete |
| SF-2026-ARXIV-2606-00251 | RP-1110dcc933d2e1d6 | deep | arXiv:2606.00251v1 | SRC-ARXIV@arXiv:2606.00251v1 | arXiv:2606.00251v1 HTML — §1 Introduction | arXiv:2606.00251v1 HTML — §3.3 CSA Inference & Evaluation; §4 Experiments and Analysis; §4.2 Main Results | arXiv:2606.00251v1 HTML — §6 Conclusion; §Appendix F Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00251v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00251 | complete |
| SF-2026-ARXIV-2606-00257 | RP-d6a9167c8fe848e9 | deep | arXiv:2606.00257v1 | SRC-ARXIV@arXiv:2606.00257v1 | arXiv:2606.00257v1 HTML — §3 Methods; excerpt=nk Adaptation in Language RL 2.2 Positioning of This Work 3 Methods 3.1 Policy Gradient with Trajectory-Level Reward 3.2 Token-Level Credit Redistribution 3.3 Intrinsic Token-Weighting Mechanisms Uniform Weighting (Baseline). Surprisal Weighting. Entropy-Reduction Weighting. Policy-Divergence Weighting. Length-Robust Normalization. Batch-Level Baselines. 3.4 Signal Degeneration Under Low-Rank Adaptation Notation. Degeneration of surpris | arXiv:2606.00257v1 HTML — §4 Experiments; excerpt=pse. Interpretation as implicit gradient-informed credit. 4 Experiments 4.1 Setup Model and task. Training. Methods. 4.2 Main Results on MATH 4.3 Credit-Assignment Diagnostics 4.4 Results and Discussion 4.5 Implementation and Metrics 4.6 Compute 4.7 Broader Impacts 4.8 Limitations 5 Conclusion References A Extended Related Work A.1 From RLHF to RLVR A.2 Critic-Based and Critic-Free Policy Optimization A.3 Reasoning-Specific Analyses of | arXiv:2606.00257v1 HTML — §4.4 Results and Discussion; excerpt=s on MATH 4.3 Credit-Assignment Diagnostics 4.4 Results and Discussion 4.5 Implementation and Metrics 4.6 Compute 4.7 Broader Impacts 4.8 Limitations 5 Conclusion References A Extended Related Work A.1 From RLHF to RLVR A.2 Critic-Based and Critic-Free Policy Optimization A.3 Reasoning-Specific Analyses of RLVR A.4 Fine-Grained Credit Assignment Beyond Uniform Token Updates A.5 Alternative Action Granularities and Token Selection B Addi | https://arxiv.org/html/2606.00257v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.00257v1.html; sha256:6ade88c2aaf8c72eaca8e0b43cf1a2a0ab2035ca397d178f5687179799ac51f5 | claim:SF-2026-ARXIV-2606-00257 | complete |
| SF-2026-ARXIV-2606-00267 | RP-7704606241922228 | deep | arXiv:2606.00267v1 | SRC-ARXIV@arXiv:2606.00267v1 | arXiv:2606.00267v1 HTML — §5 Case Study: Steering Dubins Car Video World Model | arXiv:2606.00267v1 HTML — §3 Setup: Policy Evaluation and Improvement with Video World Models; §6 Experiments: Robust Policy Evaluation and Improvement; §6.1 Robust Policy Evaluation using State-of-the-Art Video World Models | arXiv:2606.00267v1 HTML — §7 Conclusion; §Appendix F Limitations & Discussions | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00267v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00267 | complete |
| SF-2026-ARXIV-2606-00269 | RP-a8e21b95acad9008 | deep | arXiv:2606.00269v1 | SRC-ARXIV@arXiv:2606.00269v1 | arXiv:2606.00269v1 HTML — §3 Approach | arXiv:2606.00269v1 HTML — §4 Experiments; §4.1 Results.; §Appendix C Time Complexity Analysis | arXiv:2606.00269v1 HTML — §5 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00269v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00269 | complete |
| SF-2026-ARXIV-2606-00271 | RP-43f99d672951abfb | deep | arXiv:2606.00271v1 | SRC-ARXIV@arXiv:2606.00271v1 | arXiv:2606.00271v1 HTML — §3 Methodology | arXiv:2606.00271v1 HTML — §4 Experiments and Analyses; §Non-IID data domain analysis. | arXiv:2606.00271v1 HTML — §5 Conclusion; §Limitations and future work. | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00271v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00271 | complete |
| SF-2026-ARXIV-2606-00279 | RP-621c3f83951d353b | deep | arXiv:2606.00279v1 | SRC-ARXIV@arXiv:2606.00279v1 | arXiv:2606.00279v1 HTML — §3.1 Methodology; §4.1 Tensor Core Arithmetic Model | arXiv:2606.00279v1 HTML — §3.2 Results; §4.4 Diagnostics and Results; §Appendix B MoE Router Analysis | arXiv:2606.00279v1 HTML — §5 Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00279v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00279 | complete |
| SF-2026-ARXIV-2606-00284 | RP-6645ccd7d136db0a | deep | arXiv:2606.00284v1 | SRC-ARXIV@arXiv:2606.00284v1 | arXiv:2606.00284v1 HTML — §4.2 Layer Design and Task-Specific Trade-offs; excerpt=ent, distributed multilingual training. Drawing on targeted methods for low-resource language families ( Downey et al., 2024 ; Ogueji et al., 2021 ) , we generalize this approach to training language family experts, scaling the language coverage per expert while limiting intra-expert interference ( Chronopoulou et al., 2023 ) . However, while catastrophic forgetting has been studied in dense multilingual models ( Owodunni and Kumar, 202 | arXiv:2606.00284v1 HTML — §3 Experiments; excerpt=Grouping 2.2 Parameter Alignment Strategies 2.3 Baselines 3 Experiments 3.1 Experimental Setup 3.2 Language Acquisition 3.3 Catastrophic Forgetting on Downstream Tasks 3.4 Translation Quality (FLORES-200) 3.5 Within-Family Generalization 4 Understanding Layer-Aware Adaptation 4.1 Causal Analysis of Layer Drift 4.2 Layer Design and Task-Specific Trade-offs 5 Related Work 6 Conclusion References A Appendix A.1 Held-Out Evaluation Language | arXiv:2606.00284v1 HTML — §6 Conclusion; excerpt=r broad-coverage) rather than by a single aggregate metric. Limitations All experiments use a single 4B-parameter model (Gemma-3 4B) with a fixed budget of 5B tokens per family from one web corpus (MADLAD-400); we do not evaluate whether strategy rankings transfer to other model scales, architectures, or data regimes. The individual strategies are not themselves novel and each builds on established techniques, so our contribution is the | https://arxiv.org/html/2606.00284v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.00284v1.html; sha256:af6e5ceb54b75c4c86a9583a2ce3def13fc7a3f7652e798f96e55fa419687adf | claim:SF-2026-ARXIV-2606-00284 | complete |
| SF-2026-ARXIV-2606-00301 | RP-4062b8a9fd350d36 | deep | arXiv:2606.00301v1 | SRC-ARXIV@arXiv:2606.00301v1 | arXiv:2606.00301v1 HTML — §3. Methodology; excerpt=d Work 2.1 Hallucination Detection 2.2 Mixture-of-Experts 3 Methodology 3.1 Problem Formulation 3.2 Multi-View Evidence Representation 3.2.1 Latent Geometry as Evidential Signals 3.2.2 Probabilistic Trace as Evidential Signals 3.3 Group-Aware Evidential Reasoning 3.3.1 Prototype-based Evidence Allocation 3.3.2 Log-Marginal Evidence Aggregation 3.4 Learning Objective 3.4.1 Supervised Objective. 3.4.2 Semi-Supervised Objective. 4 Theoreti | arXiv:2606.00301v1 HTML — §4. Theoretical Analysis; excerpt=etical Analysis 4.1 Analysis of Approximation Error Bound 5 Experiments 5.1 Experimental Settings 5.1.1 Evaluation 5.1.2 Baselines 5.1.3 Implementation Details 5.2 Overall Performance 5.2.1 Transferability 5.2.2 Robustness 5.2.3 Interpretability 5.3 Ablation Study 5.3.1 Component-Wise Ablation 5.3.2 Hyperparameter Sensitivity 6 Conclusions and Limitations References A In-depth Theoretical Analysis A.1 Detailed Proof of Theorem Step 1: E | arXiv:2606.00301v1 HTML — §6. Conclusions and Limitations; excerpt=Ablation 5.3.2 Hyperparameter Sensitivity 6 Conclusions and Limitations References A In-depth Theoretical Analysis A.1 Detailed Proof of Theorem Step 1: Expand the numerator/denominator under the mixture. Step 2: Multiply and divide each term by π 0 ​ ( g ) ​ p g ​ ( 𝐱 ∣ 0 ) \pi_{0}(g)p_{g}(\mathbf{x}\mid 0) . Step 3: Identify the posterior under the null. Step 4: Convert into log-sum-exp form. Remark (why the posterior is under y = 0 y | https://arxiv.org/html/2606.00301v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.00301v1.html; sha256:6c20d1235eae84209575b10c601b6bfbad34e0751e7920cf5a98132f62ef485e | claim:SF-2026-ARXIV-2606-00301 | complete |
| SF-2026-ARXIV-2606-00305 | RP-f95a6b96e45e2d65 | deep | arXiv:2606.00305v1 | SRC-ARXIV@arXiv:2606.00305v1 | arXiv:2606.00305v1 HTML — §3 Methodology | arXiv:2606.00305v1 HTML — §4 Empirical Experiments; §4.2 Evaluation; §4.3 Main Results | arXiv:2606.00305v1 HTML — §7 Conclusion; §8 Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00305v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00305 | complete |
| SF-2026-ARXIV-2606-00308 | RP-e4008c06a73e8b61 | deep | arXiv:2606.00308v1 | SRC-ARXIV@arXiv:2606.00308v1 | arXiv:2606.00308v1 HTML — §How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval; excerpt=How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract I Introduction II Related Work II-A Multi-Agent LLM Code Generation II-B | arXiv:2606.00308v1 HTML — §III-D Benchmark and Dataset; excerpt=ration Architecture (Six Configurations) III-C Models III-D Benchmark and Dataset III-E Dependent Variables: Complexity Metrics III-F Pass-Conditional Robustness Analysis III-G Statistical Analysis III-G 1 Rationale for Non-Parametric Repeated-Measures Methods III-G 2 Omnibus: Friedman’s Test III-G 3 Post-hoc: Wilcoxon Signed-Rank with Holm Correction III-G 4 Effect Sizes III-G 5 Missing Data and Block Construction III-G 6 Software III- | arXiv:2606.00308v1 HTML — §V Discussion; excerpt=ness Conditioning IV-F Complexity and Functional Accuracy V Discussion V-A Interpretation V-B Implications for Practitioners V-C Threats to Validity VI Conclusion References License: arXiv.org perpetual non-exclusive license arXiv:2606.00308v1 [cs.SE] 29 May 2026 How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval Nazmus Ashrafi Affiliation: Independent Researcher nazmus.s.ashrafi@g | https://arxiv.org/html/2606.00308v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.00308v1.html; sha256:a15f5e1857055fbb172e12897b929429cc597aec7eaea58b4577145996e16f6a | claim:SF-2026-ARXIV-2606-00308 | complete |
| SF-2026-ARXIV-2606-00318 | RP-7c84eb8d1da4e1eb | deep | arXiv:2606.00318v1 | SRC-ARXIV@arXiv:2606.00318v1 | arXiv:2606.00318v1 HTML — §Where the framework applies.; §What the framework does not address. | arXiv:2606.00318v1 HTML — §5 Experimental Setup; §6 Results; §Choice of indoor benchmark. | arXiv:2606.00318v1 HTML — §7 Discussion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00318v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00318 | complete |
| SF-2026-ARXIV-2606-00329 | RP-ed70a456557897b5 | deep | arXiv:2606.00329v1 | SRC-ARXIV@arXiv:2606.00329v1 | arXiv:2606.00329v1 PDF — §§Conditional telemetry bridge; §Telemetry witnesses and matched-false-positive benchmarking; excerpt=nternal degradation — before overt failure becomes visible. We introduce Loopzero, a claim-bounded benchmark framework for testing whether recursive failures follow a directional telemetry pattern: rising gain (G), recursive persistence (p), and declining diversity ( 𝛿). The claim boundary is specified in Lean; the Lean artifact does not verify real telemetry, benchmark validity, or detector performance. We evaluate the bridge on two fr | arXiv:2606.00329v1 PDF — §§Benchmark protocol; §Results; excerpt=Benchmarking Recursive-Collapse Warning Claims Under Matched False-Positive Control David Mullett Independent Researcher ORCID: 0009-0004-2543-1664 Corresponding author: David Mullett ⋅ d@loopzero.org One-Sentence Summary A matched-FP benchmark for recursive collapse: signature directionally aligned across domains; no detector accepted. Abstract Recursive systems can enter collapse-like regimes — self-reinforcing amplification, persiste | arXiv:2606.00329v1 PDF — §§Scope summary; §Limitations and failure of all tested detectors to reach accepted operating point; excerpt= that mask accelerating internal degradation — before overt failure becomes visible. We introduce Loopzero, a claim-bounded benchmark framework for testing whether recursive failures follow a directional telemetry pattern: rising gain (G), recursive persistence (p), and declining diversity ( 𝛿). The claim boundary is specified in Lean; the Lean artifact does not verify real telemetry, benchmark validity, or detector performance. We eval | https://arxiv.org/pdf/2606.00329v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.00329v1.pdf; papers/2026/05/_sources/daily-20260530/exact-v1-pdf-text/2606.00329v1.txt; sha256:609493aec343385dd42fd4bacc10610741b91d22f9d8b80cfcea4d6c34b47a42 | claim:SF-2026-ARXIV-2606-00329 | complete |
| SF-2026-ARXIV-2606-00341 | RP-6e33e5e31c0eac2f | deep | arXiv:2606.00341v1 | SRC-ARXIV@arXiv:2606.00341v1 | arXiv:2606.00341v1 HTML — §1 Introduction | arXiv:2606.00341v1 HTML — §Agent benchmarks.; §3 ROGUE: Resource Override and Guardrail Undermining Evaluation; §Evaluation | arXiv:2606.00341v1 HTML — §6 Discussion; §Limitations and Future Work | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00341v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00341 | complete |
| SF-2026-ARXIV-2606-00348 | RP-50237ea8069ec415 | deep | arXiv:2606.00348v1 | SRC-ARXIV@arXiv:2606.00348v1 | arXiv:2606.00348v1 HTML — §III System Design; §III-A Approach Overview; §Comparison with Baseline Methodologies | arXiv:2606.00348v1 HTML — §IV Evaluation; §IV-A Experimental Setup | arXiv:2606.00348v1 HTML — §IV-H Discussion; §VI Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00348v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00348 | complete |
| SF-2026-ARXIV-2606-00365 | RP-267a4bdc9a738c75 | deep | arXiv:2606.00365v1 | SRC-ARXIV@arXiv:2606.00365v1 | arXiv:2606.00365v1 HTML — §3. SPARQLe Methodology; §3.3. SPARQLe Hardware Architecture; §4. Experimental Methodology | arXiv:2606.00365v1 HTML — §4. Experimental Methodology; §5. Experimental Results; §5.1. Accuracy and Performance Evaluation | arXiv:2606.00365v1 HTML — §6. Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00365v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00365 | complete |
| SF-2026-ARXIV-2606-00376 | RP-3bc45207dd2adf3c | deep | arXiv:2606.00376v1 | SRC-ARXIV@arXiv:2606.00376v1 | arXiv:2606.00376v1 PDF — §Theoretical Framework; §Context-Dependent Error Model; §Architecture Ablations | arXiv:2606.00376v1 PDF — §Fine-tuning experiment confirming architectural ceil-; §Deterministic Horizon and real-world benchmarks, designed to require determinis-; §Fine-Tuning Experiment | arXiv:2606.00376v1 PDF — §Conclusion | official arXiv exact-v1 PDF https://arxiv.org/pdf/2606.00376v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00376 | complete |
| SF-2026-ARXIV-2606-00380 | RP-5d7f5f8b11ff25f9 | deep | arXiv:2606.00380v1 | SRC-ARXIV@arXiv:2606.00380v1 | arXiv:2606.00380v1 HTML — §2 SUPREME Framework; §3 Experimental Methodology | arXiv:2606.00380v1 HTML — §3 Experimental Methodology; §4 Results and Discussion; §0.B.1 Model evaluation metrics | arXiv:2606.00380v1 HTML — §4 Results and Discussion; §5 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00380v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00380 | complete |
| SF-2026-ARXIV-2606-00382 | RP-a138f65cdf308fe2 | deep | arXiv:2606.00382v1 | SRC-ARXIV@arXiv:2606.00382v1 | arXiv:2606.00382v1 HTML — §3.1 Problem Formulation; excerpt=ral Norm Bound From mixing bound to adapter bound. Scope. 4 Method: CRMA 4.1 Doubly-Stochastic Mixing via Sinkhorn Normalization 4.2 Residual Behavior 4.3 Internal Transformation 4.4 What Is Omitted 4.5 Pseudocode 5 Mechanism Validation 5.1 Experimental Setup Routing at inference. 5.2 Spectral Norm Stability 5.3 Architectural Role of the Bound 6 Experiments 6.1 Continual Learning Across Real-World Domains 6.1.1 Multi-Model QA 6.1.2 Stan | arXiv:2606.00382v1 HTML — §Known limitation: global benchmark drift.; excerpt=bution is. What this paper proves. Known limitation: global benchmark drift. How CRMA is applied. Contributions. Claim summary. 2 Positioning: Why Not Frozen-Substrate Modular LoRA? Anticipated objections. Role decomposition. 3 Theoretical Foundation 3.1 Problem Formulation 3.2 The Mixing Matrix as Non-Expansive Map 3.3 Near-Identity Initialization 3.4 Spectral Norm Bound From mixing bound to adapter bound. Scope. 4 Method: CRMA 4.1 Dou | arXiv:2606.00382v1 HTML — §Known limitation: global benchmark drift.; excerpt=A’s specific contribution is. What this paper proves. Known limitation: global benchmark drift. How CRMA is applied. Contributions. Claim summary. 2 Positioning: Why Not Frozen-Substrate Modular LoRA? Anticipated objections. Role decomposition. 3 Theoretical Foundation 3.1 Problem Formulation 3.2 The Mixing Matrix as Non-Expansive Map 3.3 Near-Identity Initialization 3.4 Spectral Norm Bound From mixing bound to adapter bound. Scope. 4 M | https://arxiv.org/html/2606.00382v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.00382v1.html; sha256:ce706ae39fbdb19d04d960f074afd47b2125d802ab9ee1e99d0f9c3907f9ff38 | claim:SF-2026-ARXIV-2606-00382 | complete |
| SF-2026-ARXIV-2606-00392 | RP-553c1f7423ad977b | deep | arXiv:2606.00392v1 | SRC-ARXIV@arXiv:2606.00392v1 | arXiv:2606.00392v1 HTML — §2 Problem Formulation; excerpt=-guided paraphrasing attacks, but existing detector-evasion methods often lack precise control over semantic preservation. In particular, optimizing directly for detector evasion can degrade fine-grained semantics, whereas scalarized reward designs provide only indirect, weight-sensitive control over the evasion–semantics trade-off. We address this limitation by formulating detector-evasive LLM paraphrasing as a Constrained Markov Decis | arXiv:2606.00392v1 HTML — §4 Experiments; excerpt=roblem Formulation 3 Detector Evasion Policy Optimization 4 Experiments 4.1 Experimental Setup 4.2 Evasion vs. Semantics 4.3 Cross Detector Generalization 4.4 Cross Domain Generalization 4.5 Cross-Reward Validation 4.6 Summary 5 Conclusion References A Experimental Details A.1 Pseudocode of DEPO A.2 Baselines, Detectors, Evaluation Metrics and Evaluation Dataset A.3 Peer-review Dataset A.4 Peer-review RoBERTa Detector Validation A.5 Cho | arXiv:2606.00392v1 HTML — §5 Conclusion; excerpt=ntrol over the evasion–semantics trade-off. We address this limitation by formulating detector-evasive LLM paraphrasing as a Constrained Markov Decision Process, where detector evasion is the primary objective and semantic preservation is enforced as an explicit constraint. We propose Detector Evasion Policy Optimization (DEPO), a Lagrangian primal-dual reinforcement learning algorithm with a novel GRPO-style group-based policy update. | https://arxiv.org/html/2606.00392v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.00392v1.html; sha256:4e8f2cbaa7d26f880b6abcc6969764813063accd00e7296b430732ddf6942f37 | claim:SF-2026-ARXIV-2606-00392 | complete |
| SF-2026-ARXIV-2606-00395 | RP-01be83adce45c57e | deep | arXiv:2606.00395v1 | SRC-ARXIV@arXiv:2606.00395v1 | arXiv:2606.00395v1 HTML — §1 Introduction | arXiv:2606.00395v1 HTML — §5 Experiments; §Evaluation Benchmarks.; §Cross-Model Evaluation. | arXiv:2606.00395v1 HTML — §6 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00395v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00395 | complete |
| SF-2026-ARXIV-2606-00400 | RP-f7ed8fd0c3353588 | deep | arXiv:2606.00400v1 | SRC-ARXIV@arXiv:2606.00400v1 | arXiv:2606.00400v1 HTML — §5 Methodology; excerpt=n 2 Related Work 3 Problem Setting 4 Forgetting Mirroring 5 Methodology Controller Formulation State Representation Action Space and Replay Mixture Reward Design Policy Optimization and Transfer 6 Experimental Setup 7 Results Aggregate Performance on LLaMA-3-8B Safety-Critical Sequence Analysis Cross-Target Transfer Sensitivity Analysis 8 Analysis Interpreting the Learned Replay Policy Dynamics Ablation Study of Controller Design Choice | arXiv:2606.00400v1 HTML — §6 Experimental Setup; excerpt=ay Mixture Reward Design Policy Optimization and Transfer 6 Experimental Setup 7 Results Aggregate Performance on LLaMA-3-8B Safety-Critical Sequence Analysis Cross-Target Transfer Sensitivity Analysis 8 Analysis Interpreting the Learned Replay Policy Dynamics Ablation Study of Controller Design Choices When and Why Proxy Transfer Works 9 Conclusion References A Extended Related Work B Method Positioning Analysis C Full Proxy Training A | arXiv:2606.00400v1 HTML — §9 Conclusion; excerpt=ttings where the proxy assumption breaks down, highlighting limitations for robust deployment. 1 Introduction Language models are rarely adapted in a single step. A general-purpose chat model is typically fine-tuned sequentially across a stream of heterogeneous domains. It ranges from code generation to medical question answering, legal drafting, creative writing, multilingual instruction following, and evolving safety policies. While t | https://arxiv.org/html/2606.00400v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.00400v1.html; sha256:b8ceda3333b268a60fdd927abdd53705eda1239775815042da9f14a36a43696d | claim:SF-2026-ARXIV-2606-00400 | complete |
| SF-2026-ARXIV-2606-00408 | RP-1af6ec7c0412460f | deep | arXiv:2606.00408v1 | SRC-ARXIV@arXiv:2606.00408v1 | arXiv:2606.00408v1 HTML — §2 Methodology | arXiv:2606.00408v1 HTML — §3 Experiment Setup; §3.1 Benchmarks; §4 Main Results | arXiv:2606.00408v1 HTML — §7 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00408v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00408 | complete |
| SF-2026-ARXIV-2606-00414 | RP-702b9914166d99d1 | deep | arXiv:2606.00414v1 | SRC-ARXIV@arXiv:2606.00414v1 | arXiv:2606.00414v1 HTML — §3 Problem Formulation; excerpt=tests face an additional inverse-squared-signal budget. The framework clarifies both the promise and the limits of capacity-based safety claims: capacity counts how many distinguishable near-optimal occupancy classes exist, while sparse signatures and sample signals determine how structurally difficult those classes are to find. References [1] Chace Ashcraft and Kiran Karra. Poisoning deep reinforcement learning agents with in-distribut | arXiv:2606.00414v1 HTML — §8 Controlled Benchmarks; excerpt=r Verification 7 Capacity-Aware Regularization 8 Controlled Benchmarks 9 Discussion 10 Conclusion References A Additional Proof Details A.1 Yao reduction for Theorem A.2 Constants in the hidden-branch construction B Additional Benchmarks B.1 Trigger-room tabular benchmark B.2 Noisy-trigger sample scales B.3 Exact enumeration under the regularized objective B.4 Continuous-control auditing quantities B.5 Visual-action auditing quantities | arXiv:2606.00414v1 HTML — §9 Discussion; excerpt=n 7 Capacity-Aware Regularization 8 Controlled Benchmarks 9 Discussion 10 Conclusion References A Additional Proof Details A.1 Yao reduction for Theorem A.2 Constants in the hidden-branch construction B Additional Benchmarks B.1 Trigger-room tabular benchmark B.2 Noisy-trigger sample scales B.3 Exact enumeration under the regularized objective B.4 Continuous-control auditing quantities B.5 Visual-action auditing quantities B.6 Experimen | https://arxiv.org/html/2606.00414v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.00414v1.html; sha256:8263a84f1731b4ca26eab097661a669ae86c67b121846dda49c429690baf1e98 | claim:SF-2026-ARXIV-2606-00414 | complete |
| SF-2026-ARXIV-2606-00424 | RP-8458decf0493eb2e | deep | arXiv:2606.00424v1 | SRC-ARXIV@arXiv:2606.00424v1 | arXiv:2606.00424v1 HTML — §Weak Model Critique Framework Improves Strong Model Performance Across Tasks and Model Types.; §4 Method | arXiv:2606.00424v1 HTML — §Experimental Setting.; §5 Opcd Training-Time Experiments; §Experimental Setup. | arXiv:2606.00424v1 HTML — §6 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00424v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00424 | complete |
| SF-2026-ARXIV-2606-00432 | RP-704b9a27eaeaa12e | deep | arXiv:2606.00432v1 | SRC-ARXIV@arXiv:2606.00432v1 | arXiv:2606.00432v1 HTML — §Training-time and Decoding-time Methods; §3 Methodology | arXiv:2606.00432v1 HTML — §4 Experimental Setup; §5 Results; §Token-Level Analysis | arXiv:2606.00432v1 HTML — §6 Conclusion; §Limitations; §Appendix F Extended Discussion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00432v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00432 | complete |
| SF-2026-ARXIV-2606-00437 | RP-b19470eb6918033a | deep | arXiv:2606.00437v1 | SRC-ARXIV@arXiv:2606.00437v1 | arXiv:2606.00437v1 HTML — §3 The EST-PRM Framework; §B.1 Formal definitions of mitigation methods | arXiv:2606.00437v1 HTML — §Process reward models, benchmarks, and EST-PRM positioning.; §3.1 Formal Vulnerability Analysis; §4 Experimental Protocol | arXiv:2606.00437v1 HTML — §7 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00437v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00437 | complete |
| SF-2026-ARXIV-2606-00439 | RP-775af52c56d206d8 | deep | arXiv:2606.00439v1 | SRC-ARXIV@arXiv:2606.00439v1 | arXiv:2606.00439v1 HTML — §3 PSI architecture and training details | arXiv:2606.00439v1 HTML — §B Additional Qualitative Results; §B.5 Point-prompted movable object segmentation results; §B.6 Unprompted movable object segmentation results | arXiv:2606.00439v1 HTML — §5 Conclusion & Future Work | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00439v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00439 | complete |
| SF-2026-ARXIV-2606-00448 | RP-3049a245ffebf151 | deep | arXiv:2606.00448v1 | SRC-ARXIV@arXiv:2606.00448v1 | arXiv:2606.00448v1 HTML — §III The SkillReact Measurement Framework; §IV Methodology | arXiv:2606.00448v1 HTML — §Static-Composition Benchmark (deterministic).; §Static Analysis.; §IV-E Pairwise Compositional Analysis | arXiv:2606.00448v1 HTML — §IX Limitations and Threats to Validity; §XI Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00448v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00448 | complete |
| SF-2026-ARXIV-2606-00457 | RP-da23012bb775e621 | deep | arXiv:2606.00457v1 | SRC-ARXIV@arXiv:2606.00457v1 | arXiv:2606.00457v1 HTML — §2.2.1 Cooling and water model; §2.2.2 BESS model; §2.2.3 Workload model | arXiv:2606.00457v1 HTML — §2.3 Illustrative Results | arXiv:2606.00457v1 HTML — §3 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.00457v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-00457 | complete |
| SF-2026-ARXIV-2606-07595 | RP-087a13b459b3488d | deep | arXiv:2606.07595v1 | SRC-ARXIV@arXiv:2606.07595v1 | arXiv:2606.07595v1 HTML — §Introduction / disclosed mechanism body; excerpt=-common diagnostic control, not a comparison across defense methods. Its PII gains mostly come from safety-first suppression and should not be interpreted as a utility-preserving repair. • The email residual and rendered unsafe-text group asymmetries are diagnostic findings in this subset, not complete taxonomies of which PII or harm categories are intrinsically harder. • Per-trace logs allow full table reproduction, but regenerating lo | arXiv:2606.07595v1 HTML — §3 Evaluation Setting; excerpt=ibutions. 2 Failure Definition Why tool arguments matter. 3 Evaluation Setting Visual triggers. Models. Agent workflows. Metrics. Mitigation and guard diagnostic. Reproducibility artifact. 4 Tool Propagation Results Mitigation is asymmetric. Scenario effects. Visual-family effects. Web-research tool surface. 5 Trace Diagnostics 6 Mitigations and Residual Failures Residual rendered unsafe-text groups. Oracle boundary diagnostic. 7 Relate | arXiv:2606.07595v1 HTML — §VisualLeakBench : Reproducible Action-Boundary Propagation Failures in Vision-Language Agents; excerpt=VisualLeakBench: Reproducible Action-Boundary Propagation Failures in Vision-Language Agents Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction Contributions. 2 Failure Definition Why tool arguments matter. 3 Evaluat | https://arxiv.org/html/2606.07595v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.07595v1.html; sha256:3bb8184edb178d77de1149cd7f3a34a7c5f51b3282e8bc13a9cce44c87d4b747 | claim:SF-2026-ARXIV-2606-07595 | complete |
| SF-2026-ARXIV-2606-07603 | RP-96f04c569ba96d3a | deep | arXiv:2606.07603v1 | SRC-ARXIV@arXiv:2606.07603v1 | arXiv:2606.07603v1 HTML — §3 Methodology; §3.1 Framework Pipeline | arXiv:2606.07603v1 HTML — §4 Experiments; §4.1 Experimental Setup; §5 Analysis | arXiv:2606.07603v1 HTML — §6 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.07603v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-07603 | complete |
| SF-2026-ARXIV-2606-07616 | RP-c51f9f7a2ca4ae82 | deep | arXiv:2606.07616v1 | SRC-ARXIV@arXiv:2606.07616v1 | arXiv:2606.07616v1 HTML — §3 Method | arXiv:2606.07616v1 HTML — §Efficient LM Evaluation; §4 Experiments; §Appendix B Additional Results for Pre-training Downstream IRSL | arXiv:2606.07616v1 HTML — §5 Limitations, Discussions, and Future Work | official arXiv exact-v1 HTML https://arxiv.org/html/2606.07616v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-07616 | complete |
| SF-2026-ARXIV-2606-20631 | RP-57a9620a46c48a82 | deep | arXiv:2606.20631v1 | SRC-ARXIV@arXiv:2606.20631v1 | arXiv:2606.20631v1 HTML — §3 Methodology; §3.2 Reference Architecture Construction; §5 Reference Architecture for Skill Harnessing | arXiv:2606.20631v1 HTML — §6 Evaluation; §6.1 Evaluation Design; §6.2 Cross-Instantiation Results | arXiv:2606.20631v1 HTML — §7 Discussion; §8 Threats to Validity; §10 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2606.20631v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2606-20631 | complete |
| SF-2026-ARXIV-2606-24893 | RP-def9e9cf77cc0ae6 | deep | arXiv:2606.24893v1 | SRC-ARXIV@arXiv:2606.24893v1 | arXiv:2606.24893v1 HTML — §3.1 Formulation; excerpt=these key abilities of test-time continual learning agents, we introduce AgentOdyssey , a novel evaluation framework that procedurally generates open-ended text games with rich entities, world dynamics, and long-horizon tasks. Critically, AgentOdyssey goes beyond the conventional machine learning assumption that learning does not occur at test time by placing agents in a continuous, long-horizon setting that interleaves learning and inf | arXiv:2606.24893v1 HTML — §3.4 Evaluation Metrics; excerpt=3.2 Ontology 3.3 Game Generation with Program Synthesis 3.4 Evaluation Metrics 4 Agent Paradigms 5 Experiment 1 - Diagnosing Five Key Abilities of Agents 5.1 Game Description 5.2 Analysis and Discussion 6 Experiment 2 - Effect of Agent Mechanisms on Test-Time Training 6.1 Game Description 6.2 Analysis and Discussion 7 Conclusion References 8 More Results for Experiment 1 and Experiment 2 9 Environment Design and Implementation Details 9 | arXiv:2606.24893v1 HTML — §5.2 Analysis and Discussion; excerpt=y Abilities of Agents 5.1 Game Description 5.2 Analysis and Discussion 6 Experiment 2 - Effect of Agent Mechanisms on Test-Time Training 6.1 Game Description 6.2 Analysis and Discussion 7 Conclusion References 8 More Results for Experiment 1 and Experiment 2 9 Environment Design and Implementation Details 9.1 Tasks Main Quest. Side Quest. 9.2 Game Generation Entity Generation. Rule Generation. Quest Generation. 9.3 Additional Features T | https://arxiv.org/html/2606.24893v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.24893v1.html; sha256:64635b394d0919e1e3b56dea006a062e235204837b796b28eff03af85c9e001f | claim:SF-2026-ARXIV-2606-24893 | complete |
| SF-2026-ARXIV-2606-28337 | RP-c6687f2100fcb7fa | deep | arXiv:2606.28337v1 | SRC-ARXIV@arXiv:2606.28337v1 | arXiv:2606.28337v1 HTML — §A Systems-Level Analysis of Sensitivity, Robustness, and Stability in Retrieval-Augmented Generation; excerpt=pagation 2.6 Stability and Variance in Generation Systems 3 Methodology and Evaluation Framework 3.1 Pipeline Overview 3.2 Dataset and Corpus 3.3 Chunking and Filtering 3.4 Embedding and Indexing 3.5 Retrieval and Reranking 3.6 Packing 3.7 Generation 3.8 Metrics 3.9 Experimental Environment 4 Experimental Design 4.1 Sensitivity Experiments 4.2 Robustness Experiments 4.3 Stability Experiments 5 Results 5.1 Preprocessing Answer Survival 5 | arXiv:2606.28337v1 HTML — §A Systems-Level Analysis of Sensitivity, Robustness, and Stability in Retrieval-Augmented Generation; excerpt=bility and Variance in Generation Systems 3 Methodology and Evaluation Framework 3.1 Pipeline Overview 3.2 Dataset and Corpus 3.3 Chunking and Filtering 3.4 Embedding and Indexing 3.5 Retrieval and Reranking 3.6 Packing 3.7 Generation 3.8 Metrics 3.9 Experimental Environment 4 Experimental Design 4.1 Sensitivity Experiments 4.2 Robustness Experiments 4.3 Stability Experiments 5 Results 5.1 Preprocessing Answer Survival 5.2 Sensitivity t | arXiv:2606.28337v1 HTML — §2.5 Context Utilization and Failure Propagation; excerpt=2.4 Robustness and Noise in RAG 2.5 Context Utilization and Failure Propagation 2.6 Stability and Variance in Generation Systems 3 Methodology and Evaluation Framework 3.1 Pipeline Overview 3.2 Dataset and Corpus 3.3 Chunking and Filtering 3.4 Embedding and Indexing 3.5 Retrieval and Reranking 3.6 Packing 3.7 Generation 3.8 Metrics 3.9 Experimental Environment 4 Experimental Design 4.1 Sensitivity Experiments 4.2 Robustness Experiments | https://arxiv.org/html/2606.28337v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2606.28337v1.html; sha256:b20701099f540add64a66e00fa7e443586c2f50aac081026879aef3c9e027297 | claim:SF-2026-ARXIV-2606-28337 | complete |
| SF-2026-ARXIV-2605-30711 | RP-0ab60b31e89fa6fb | deep | arXiv:2605.30711v1 | SRC-ARXIV@arXiv:2605.30711v1 | arXiv:2605.30711v1 HTML — §3 Methodology | arXiv:2605.30711v1 HTML — §4 Experiments; §Experimental Setting.; §4.1 Results | arXiv:2605.30711v1 HTML — §5 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30711v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30711 | complete |
| SF-2026-ARXIV-2605-30712 | RP-8ee1d118f358af04 | deep | arXiv:2605.30712v1 | SRC-ARXIV@arXiv:2605.30712v1 | arXiv:2605.30712v1 HTML — §4.1 ExpGraph Outperforms General Prompt-based Baselines and Experience Learning Methods; §Retrieval-centric methods.; §G.1 ExpGraph Outperforms General Prompt-based Baselines and Experience Learning Methods | arXiv:2605.30712v1 HTML — §4 Experiments; §Training and evaluation.; §Appendix G Experimental Result Analysis | arXiv:2605.30712v1 HTML — §6 Conclusion; §Appendix A Limitations, Future Work, and Broader Impact; §Limitations. | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30712v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30712 | complete |
| SF-2026-ARXIV-2605-30723 | RP-1836d9e0c4da5222 | deep | arXiv:2605.30723v1 | SRC-ARXIV@arXiv:2605.30723v1 | arXiv:2605.30723v1 HTML — §3 Method: MASA | arXiv:2605.30723v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Skill Evolution Evaluation | arXiv:2605.30723v1 HTML — §5 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30723v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30723 | complete |
| SF-2026-ARXIV-2605-30727 | RP-3c384c9987ab2100 | deep | arXiv:2605.30727v1 | SRC-ARXIV@arXiv:2605.30727v1 | arXiv:2605.30727v1 HTML — §1 Introduction | arXiv:2605.30727v1 HTML — §Deep Research benchmarks.; §6 Evaluation Results; §Appendix C Further Evaluation Analysis | arXiv:2605.30727v1 HTML — §7 Conclusion; §8 Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30727v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30727 | complete |
| SF-2026-ARXIV-2605-30728 | RP-3dccf490b0920cb4 | deep | arXiv:2605.30728v1 | SRC-ARXIV@arXiv:2605.30728v1 | arXiv:2605.30728v1 HTML — §1. Introduction | arXiv:2605.30728v1 HTML — §6. Evaluation; §A.2.4. Benchmarks; §A.4. Evaluation workflow | arXiv:2605.30728v1 HTML — §8. Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30728v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30728 | complete |
| SF-2026-ARXIV-2605-30736 | RP-7b33175e2c729371 | deep | arXiv:2605.30736v1 | SRC-ARXIV@arXiv:2605.30736v1 | arXiv:2605.30736v1 HTML — §2 Methodology | arXiv:2605.30736v1 HTML — §3 Experiments; §3.1 RouterArena Results; §3.2 Analysis | arXiv:2605.30736v1 HTML — §4 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30736v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30736 | complete |
| SF-2026-ARXIV-2605-30738 | RP-875304bb1c4d5772 | deep | arXiv:2605.30738v1 | SRC-ARXIV@arXiv:2605.30738v1 | arXiv:2605.30738v1 HTML — §3 Methodology | arXiv:2605.30738v1 HTML — §4 Benchmark; §4.5 Evaluation Protocol and Metrics; §5 Evaluation | arXiv:2605.30738v1 HTML — §7 Discussion; §8 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30738v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30738 | complete |
| SF-2026-ARXIV-2605-30753 | RP-379685dfe0f21468 | deep | arXiv:2605.30753v1 | SRC-ARXIV@arXiv:2605.30753v1 | arXiv:2605.30753v1 HTML — §3 Methods; §A.3 TSPD Controller: Architecture and Features | arXiv:2605.30753v1 HTML — §4 Experiments; §4.1 Experimental Settings; §4.2 Main Results | arXiv:2605.30753v1 HTML — §5 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30753v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30753 | complete |
| SF-2026-ARXIV-2605-30757 | RP-b463eba52f75c6a3 | deep | arXiv:2605.30757v1 | SRC-ARXIV@arXiv:2605.30757v1 | arXiv:2605.30757v1 HTML — §1 Introduction | arXiv:2605.30757v1 HTML — §Appendix F Experimental details and seed-level results; §Experimental setup. | arXiv:2605.30757v1 HTML — §6 Discussion and limitations; §Limitations and next steps. | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30757v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30757 | complete |
| SF-2026-ARXIV-2605-30771 | RP-a16dfebcd3b5909c | deep | arXiv:2605.30771v1 | SRC-ARXIV@arXiv:2605.30771v1 | arXiv:2605.30771v1 HTML — §Recent agent-memory architectures.; §4 System Architecture | arXiv:2605.30771v1 HTML — §Benchmarks and evaluation.; §5 Evaluation; §5.1 Benchmark Setup | arXiv:2605.30771v1 HTML — §6 Discussion; §7 Threats to Validity; §8 Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30771v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30771 | complete |
| SF-2026-ARXIV-2605-30777 | RP-b23bc2387d9e73a0 | deep | arXiv:2605.30777v1 | SRC-ARXIV@arXiv:2605.30777v1 | arXiv:2605.30777v1 HTML — §4. Methodology; §Agentic Frameworks | arXiv:2605.30777v1 HTML — §5. Results | arXiv:2605.30777v1 HTML — §6. Discussion; §7. Threats to Validity; §9. Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30777v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30777 | complete |
| SF-2026-ARXIV-2605-30785 | RP-ec889282982b26ea | deep | arXiv:2605.30785v1 | SRC-ARXIV@arXiv:2605.30785v1 | arXiv:2605.30785v1 HTML — §1 Introduction | arXiv:2605.30785v1 HTML — §4 Experiments and Analysis; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.30785v1 HTML — §6 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30785v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30785 | complete |
| SF-2026-ARXIV-2605-30789 | RP-bddb2b49c9ac2eff | deep | arXiv:2605.30789v1 | SRC-ARXIV@arXiv:2605.30789v1 | arXiv:2605.30789v1 HTML — §3 Method; excerpt=mization (GRPO) 2.2 Distillation Introduces Perturbations 3 Method 3.1 Token-Level vs. Policy-Level Perturbations Token-level perturbations. Policy-level perturbations via parameter-level compression. Implications for gradient estimation in GRPO. Gradient interference under token-level perturbations. Structured gradients under policy-level perturbations. Takeaway. 3.2 S2L-PO: Small-to-Large Policy Optimization Mixed rollout generation. | arXiv:2605.30789v1 HTML — §4 Experiment; excerpt=ion. Progressive annealing. Compatibility and efficiency. 4 Experiment 4.1 Experiment Settings 4.2 Main Results Small-to-large sampling improves both convergence speed and final performance. 4.3 Diversity Analysis Quantitative measurement of policy-level diversity. Controlled experiment on rollout diversity. 4.4 Ablation Study Pure small-model rollouts are not sufficient for sustained performance gains. Progressive transition vs. abrupt | arXiv:2605.30789v1 HTML — §6 Conclusion; excerpt=p E.2 Summary: Token-Level vs. Policy-Level Signal Growth F Limitations License: arXiv.org perpetual non-exclusive license arXiv:2605.30789v1 [cs.LG] 29 May 2026 Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO Yiming Ren Affiliation: Tsinghua University Affiliation: Shanghai AI Laboratory Yiran Xu Affiliation: Tsinghua University Zicheng Lin Affiliation: Tsinghua University Chufan Shi Affiliation: Tsinghua Univer | https://arxiv.org/html/2605.30789v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2605.30789v1.html; sha256:c3e3fd9c62ef41fe0a51b795b6e4333286032752fc59d1e191344f824d20c997 | claim:SF-2026-ARXIV-2605-30789 | complete |
| SF-2026-ARXIV-2605-30790 | RP-0f5046279326836b | deep | arXiv:2605.30790v1 | SRC-ARXIV@arXiv:2605.30790v1 | arXiv:2605.30790v1 HTML — §3.2.3 Reformulation Representations; excerpt=that structural information aids the generator. Compression methods Xu et al. (2023) ; Pan et al. (2024) ; Li et al. (2023) reduce retrieved content to lower inference cost, finding that generators tolerate substantial reductions with comparable or only slightly degraded accuracy. Finally, rewriting methods learn to transform retrieved content for downstream generator utility rather than for retrieval relevance Kim et al. (2026) ; Li et | arXiv:2605.30790v1 HTML — §3 Experimental Setup; excerpt=tract Download PDF Abstract 1 Introduction 2 Related Work 3 Experimental Setup 3.1 Dataset and Retrieval 3.2 Document Representations 3.2.1 Selection Representations 3.2.2 Summarisation Representations 3.2.3 Reformulation Representations 3.2.4 Implementation details for LLM-based transformations. 3.2.5 Representation Statistics 3.3 Answer Generation 3.4 Evaluation 4 Results 4.1 RQ-1 4.2 RQ-2 4.2.1 Answer Accuracy 4.2.2 Query-time Latenc | arXiv:2605.30790v1 HTML — §5 Discussion; excerpt=ntier 4.2.4 Reducing Snippet-abstractive Latency 4.3 RQ-3 5 Discussion 5.1 Answer retention as the dominant factor 5.2 Reinterpreting prior work through retention 5.3 Source effects: human-vs-LLM and family preference 5.4 Why query-dependence underdelivers 5.5 Relation to prompt-sensitivity findings 6 Conclusion 7 Limitations 7.1 Representational dimensions and retention are not independently varied 7.2 Representational dimensions are n | https://arxiv.org/html/2605.30790v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2605.30790v1.html; sha256:878ee73f33a2ddc24223e6efaf40282b8c931b1bde9b622e667b66e5b3f256fc | claim:SF-2026-ARXIV-2605-30790 | complete |
| SF-2026-ARXIV-2605-30803 | RP-2963f0f581193e74 | deep | arXiv:2605.30803v1 | SRC-ARXIV@arXiv:2605.30803v1 | arXiv:2605.30803v1 HTML — §1 Introduction | arXiv:2605.30803v1 HTML — §2.1 Rubrics in LLM evaluation and training; §4 Experiments; §B.3.2 Full Results | arXiv:2605.30803v1 HTML — §5 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30803v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30803 | complete |
| SF-2026-ARXIV-2605-30807 | RP-d6c1e840aa134539 | deep | arXiv:2605.30807v1 | SRC-ARXIV@arXiv:2605.30807v1 | arXiv:2605.30807v1 HTML — §3 Methodology; §A.2 Stable Diffusion Model; §C.2 Choice of Latent Generative Model | arXiv:2605.30807v1 HTML — §4 Experiments; §4.1 Experiments on Synthetic Datasets; §4.2 Experiments on Image-to-Text Task | arXiv:2605.30807v1 HTML — §5 Conclusion and Future Works | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30807v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30807 | complete |
| SF-2026-ARXIV-2605-30824 | RP-25570b9bc112c3fa | deep | arXiv:2605.30824v1 | SRC-ARXIV@arXiv:2605.30824v1 | arXiv:2605.30824v1 HTML — §3 Methodology | arXiv:2605.30824v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.30824v1 HTML — §5 Conclusion; §6 Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30824v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30824 | complete |
| SF-2026-ARXIV-2605-30832 | RP-293a86405540b3a0 | deep | arXiv:2605.30832v1 | SRC-ARXIV@arXiv:2605.30832v1 | arXiv:2605.30832v1 HTML — §3 Method; §4.3.1 Extension to larger model | arXiv:2605.30832v1 HTML — §4 Experiment; §Evaluation; §4.2 Main Results | arXiv:2605.30832v1 HTML — §6 Conclusion and Future Work; §Appendix B Discussion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30832v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30832 | complete |
| SF-2026-ARXIV-2605-30833 | RP-c3f608ff4aafa9c5 | deep | arXiv:2605.30833v1 | SRC-ARXIV@arXiv:2605.30833v1 | arXiv:2605.30833v1 HTML — §1 Introduction | arXiv:2605.30833v1 HTML — §2.3 Theoretical Analysis: Signal Collapse and Compounding Drift; §4 Experiments; §4.1 Experimental Setup | arXiv:2605.30833v1 HTML — §6 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30833v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30833 | complete |
| SF-2026-ARXIV-2605-30834 | RP-974f5d5084e78d01 | deep | arXiv:2605.30834v1 | SRC-ARXIV@arXiv:2605.30834v1 | arXiv:2605.30834v1 HTML — §Detector architecture.; §D.3 Detector Architecture; §G.1 Out-of-Distribution Detection-based Methods | arXiv:2605.30834v1 HTML — §5 Experiments; §Benchmarks and models.; §Evaluation metrics. | arXiv:2605.30834v1 HTML — §6 Conclusion; §Appendix I Limitations and Future Work | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30834v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30834 | complete |
| SF-2026-ARXIV-2605-30837 | RP-1512b60000519bef | deep | arXiv:2605.30837v1 | SRC-ARXIV@arXiv:2605.30837v1 | arXiv:2605.30837v1 HTML — §1 Introduction | arXiv:2605.30837v1 HTML — §Prompt-injection attacks and benchmarks.; §Safety–utility evaluation axes.; §7 Experiments | arXiv:2605.30837v1 HTML — §7.6 Latency and deployment discussion; §8 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30837v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30837 | complete |
| SF-2026-ARXIV-2605-30838 | RP-80271d7ae2eb1c76 | deep | arXiv:2605.30838v1 | SRC-ARXIV@arXiv:2605.30838v1 | arXiv:2605.30838v1 HTML — §3 Methodology | arXiv:2605.30838v1 HTML — §4 Experiment; §4.1 Experimental Setup; §4.4 Further Analysis | arXiv:2605.30838v1 HTML — §5 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30838v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30838 | complete |
| SF-2026-ARXIV-2605-30842 | RP-e57ddbfd68dcefc8 | deep | arXiv:2605.30842v1 | SRC-ARXIV@arXiv:2605.30842v1 | arXiv:2605.30842v1 HTML — §3.2 CoMem Framework; §Appendix A Prompt for Agent Model; §Appendix B Prompt for Memory Model | arXiv:2605.30842v1 HTML — §3.1 Analysis of Agent Inference; §4 Experimental Results; §4.1 Evaluation Dataset | arXiv:2605.30842v1 HTML — §6 Discussion; §7 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30842v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30842 | complete |
| SF-2026-ARXIV-2605-30851 | RP-c655c62d2117451d | deep | arXiv:2605.30851v1 | SRC-ARXIV@arXiv:2605.30851v1 | arXiv:2605.30851v1 HTML — §J.2.2 Parallel-Decoding-Aware Architecture Design | arXiv:2605.30851v1 HTML — §3 Module-Level Analysis of Near-Free Parallelism; §Appendix C Module-Level Analysis Implementation Details; §C.1.1 Experimental Goal and Scope | arXiv:2605.30851v1 HTML — §8 Conclusion; §Limitations; §Appendix J Discussion and Implications | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30851v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30851 | complete |
| SF-2026-ARXIV-2605-30852 | RP-65c8d0746ec7d8bc | deep | arXiv:2605.30852v1 | SRC-ARXIV@arXiv:2605.30852v1 | arXiv:2605.30852v1 HTML — §3 Methodology; §3.1 Pipeline Execution Framework | arXiv:2605.30852v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Evaluation Metrics: Acceptance Length and Theoretical Speedup | arXiv:2605.30852v1 HTML — §5 Conclusion; §6 Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30852v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30852 | complete |
| SF-2026-ARXIV-2605-30854 | RP-fe3e36a8d2e85d89 | deep | arXiv:2605.30854v1 | SRC-ARXIV@arXiv:2605.30854v1 | arXiv:2605.30854v1 HTML — §3 Method | arXiv:2605.30854v1 HTML — §4 Experimental Setup; §5 Results; §6 Analysis | arXiv:2605.30854v1 HTML — §7 Conclusion; §8 Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30854v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30854 | complete |
| SF-2026-ARXIV-2605-30855 | RP-6f60faaf788b0e7f | deep | arXiv:2605.30855v1 | SRC-ARXIV@arXiv:2605.30855v1 | arXiv:2605.30855v1 HTML — §3.1 Memory-Conditioned Rollout Framework | arXiv:2605.30855v1 HTML — §4 Experiments; §4.1 Experimental Settings; §4.2 Results | arXiv:2605.30855v1 HTML — §5 Conclusion; §Appendix F Limitation | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30855v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30855 | complete |
| SF-2026-ARXIV-2605-30859 | RP-c0a65ce942eaaeaf | deep | arXiv:2605.30859v1 | SRC-ARXIV@arXiv:2605.30859v1 | arXiv:2605.30859v1 HTML — §4 Method | arXiv:2605.30859v1 HTML — §5 Experiments; §5.1 Implementation and Experimental Setups; §Appendix F Analysis on Response Length | arXiv:2605.30859v1 HTML — §5.6 Discussion; §6 Conclusion; §The Limitation of Tail Batching. | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30859v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30859 | complete |
| SF-2026-ARXIV-2605-30880 | RP-c5b6b1d591799a0a | deep | arXiv:2605.30880v1 | SRC-ARXIV@arXiv:2605.30880v1 | arXiv:2605.30880v1 HTML — §4 Methodology | arXiv:2605.30880v1 HTML — §5 Experiments; §Analysis.; §Appendix G Per-Environment Rollout Results | arXiv:2605.30880v1 HTML — §6 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30880v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30880 | complete |
| SF-2026-ARXIV-2605-30883 | RP-5e44d3a933522e28 | deep | arXiv:2605.30883v1 | SRC-ARXIV@arXiv:2605.30883v1 | arXiv:2605.30883v1 HTML — §3 Threat Model | arXiv:2605.30883v1 HTML — §5 Experiment; §5.1 Experiment Setup; §Evaluation Metrics. | arXiv:2605.30883v1 HTML — §7 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30883v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30883 | complete |
| SF-2026-ARXIV-2605-30888 | RP-970c19462abe7dfc | deep | arXiv:2605.30888v1 | SRC-ARXIV@arXiv:2605.30888v1 | arXiv:2605.30888v1 HTML — §5 Methodology | arXiv:2605.30888v1 HTML — §6 Experiments; §Reward Model Evaluation.; §Policy Model Evaluation. | arXiv:2605.30888v1 HTML — §7 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30888v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30888 | complete |
| SF-2026-ARXIV-2605-30896 | RP-023cc82d47eb3dde | deep | arXiv:2605.30896v1 | SRC-ARXIV@arXiv:2605.30896v1 | arXiv:2605.30896v1 HTML — §8 Why Actor-Critic Methods Struggle; §Appendix E Derby Framework | arXiv:2605.30896v1 HTML — §7 Mitigation Results; §Appendix D Experimental Details | arXiv:2605.30896v1 HTML — §9 Discussion and Future Work; §10 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30896v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30896 | complete |
| SF-2026-ARXIV-2605-30898 | RP-ab669035cab37faa | deep | arXiv:2605.30898v1 | SRC-ARXIV@arXiv:2605.30898v1 | arXiv:2605.30898v1 HTML — §3 The UniScale Framework; §D.3 Unified Inference Scaling Cost Model | arXiv:2605.30898v1 HTML — §4 Empirical Evaluation; §Appendix B Additional Main Experimental Details and Results; §B.4 Detailed Results on Main Experiment | arXiv:2605.30898v1 HTML — §6 Related Work and Discussion; §7 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30898v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30898 | complete |
| SF-2026-ARXIV-2605-30911 | RP-58a92fc9c7191144 | deep | arXiv:2605.30911v1 | SRC-ARXIV@arXiv:2605.30911v1 | arXiv:2605.30911v1 HTML — §IV-C 1 Uncertainty Scoring Method | arXiv:2605.30911v1 HTML — §II-C Evaluating Benchmarks for Hallucination; §IV Evaluation Protocol; §IV-B Certainty Evaluation Metrics | arXiv:2605.30911v1 HTML — §VI Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30911v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30911 | complete |
| SF-2026-ARXIV-2605-30917 | RP-e58c895f29308349 | deep | arXiv:2605.30917v1 | SRC-ARXIV@arXiv:2605.30917v1 | arXiv:2605.30917v1 HTML — §4. Method | arXiv:2605.30917v1 HTML — §5. Experiments; §Evaluation.; §5.3. Benchmark Retrieval Quality | arXiv:2605.30917v1 HTML — §6. Conclusion; §Limitations and Future Work. | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30917v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30917 | complete |
| SF-2026-ARXIV-2605-30924 | RP-662b2bf541c4893e | deep | arXiv:2605.30924v1 | SRC-ARXIV@arXiv:2605.30924v1 | arXiv:2605.30924v1 HTML — §C.2 Details of Evaluation Framework; §C.2.3 Guardrail Evaluation Method | arXiv:2605.30924v1 HTML — §3.2 Constructing Training and Evaluation Dataset; §4.1 Experimental Setup; §4.2 Results | arXiv:2605.30924v1 HTML — §5.3 Discussion; §6 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30924v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30924 | complete |
| SF-2026-ARXIV-2605-30998 | RP-050ea62975851c05 | deep | arXiv:2605.30998v1 | SRC-ARXIV@arXiv:2605.30998v1 | arXiv:2605.30998v1 HTML — §Architecture.; §3 System Model; §3.3 Threat Model | arXiv:2605.30998v1 HTML — §4 Vulnerability Analysis; §5.4.1 Experimental Setup | arXiv:2605.30998v1 HTML — §7 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.30998v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-30998 | complete |
| SF-2026-ARXIV-2605-31033 | RP-bfd9d7a7b046ef0b | deep | arXiv:2605.31033v1 | SRC-ARXIV@arXiv:2605.31033v1 | arXiv:2605.31033v1 HTML — §3. Method; §3.1. Problem Setup and Streaming Framework | arXiv:2605.31033v1 HTML — §4. Experiments; §4.1. Experiment Setups; §4.2. Main Experiments | arXiv:2605.31033v1 HTML — §4.4. Limitations and Future Work; §5. Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31033v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31033 | complete |
| SF-2026-ARXIV-2605-31042 | RP-fe51a76a8a225eab | deep | arXiv:2605.31042v1 | SRC-ARXIV@arXiv:2605.31042v1 | arXiv:2605.31042v1 HTML — §3.1 Agent Harness Model | arXiv:2605.31042v1 HTML — §2.1 Benchmarks for Agent Security; §4 The ClawTrojan Benchmark; §4.4 Comparison with Existing Benchmarks | arXiv:2605.31042v1 HTML — §7 Conclusion and Future Work; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31042v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31042 | complete |
| SF-2026-ARXIV-2605-31058 | RP-6f521188917f61b9 | deep | arXiv:2605.31058v1 | SRC-ARXIV@arXiv:2605.31058v1 | arXiv:2605.31058v1 PDF — §We propose the ADR framework, a novel paradigm that shifts from heuristic seed expansion; §Method; §Diversity: We obtain data representations using the all-MiniLM-L6-v2 embedding model | arXiv:2605.31058v1 PDF — §We establish a multi-dimensional evaluation taxonomy for verifiable synthetic data that; §Through extensive experiments on large-scale RLVR, we show the strong generalization; §Evaluation of Synthetic Data Quality | arXiv:2605.31058v1 PDF — §Conclusion | official arXiv exact-v1 PDF https://arxiv.org/pdf/2605.31058v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31058 | complete |
| SF-2026-ARXIV-2605-31066 | RP-84f61adcc0571d08 | deep | arXiv:2605.31066v1 | SRC-ARXIV@arXiv:2605.31066v1 | arXiv:2605.31066v1 HTML — §2.2 Methods for Air-Ground Cooperation; §3.1 Causally Consistent Runtime Architecture | arXiv:2605.31066v1 HTML — §2.1 Air-Ground Evaluation Infrastructure; §4 Diagnostic Evaluation; §4.3 Results | arXiv:2605.31066v1 HTML — §5 Discussion and Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31066v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31066 | complete |
| SF-2026-ARXIV-2605-31073 | RP-a41897b38f7f3ffa | deep | arXiv:2605.31073v1 | SRC-ARXIV@arXiv:2605.31073v1 | arXiv:2605.31073v1 HTML — §3 Methodology | arXiv:2605.31073v1 HTML — §4 Experiment; §Benchmarks and Evaluation Metrics.; §4.1 Main Results | arXiv:2605.31073v1 HTML — §5 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31073v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31073 | complete |
| SF-2026-ARXIV-2605-31086 | RP-285340169bc46d48 | deep | arXiv:2605.31086v1 | SRC-ARXIV@arXiv:2605.31086v1 | arXiv:2605.31086v1 HTML — §1 Introduction | arXiv:2605.31086v1 HTML — §4 Benchmark Curation; §6 Experiments; §6.1 Experimental Setup | arXiv:2605.31086v1 HTML — §7 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31086v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31086 | complete |
| SF-2026-ARXIV-2605-31105 | RP-89e0979511a317e1 | deep | arXiv:2605.31105v1 | SRC-ARXIV@arXiv:2605.31105v1 | arXiv:2605.31105v1 HTML — §3 Methods | arXiv:2605.31105v1 HTML — §4 Experiments; §4.1 Experimental Settings; §4.2 Experimental Results | arXiv:2605.31105v1 HTML — §5 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31105v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31105 | complete |
| SF-2026-ARXIV-2605-31111 | RP-8af9329531a79f07 | deep | arXiv:2605.31111v1 | SRC-ARXIV@arXiv:2605.31111v1 | arXiv:2605.31111v1 HTML — §3 Method: SD-JEPA | arXiv:2605.31111v1 HTML — §4 Theoretical analysis; §5 Experiments; §5.2 Main results | arXiv:2605.31111v1 HTML — §5.6 Cross-environment summary and limitations; §Known limitations.; §7 Discussion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31111v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31111 | complete |
| SF-2026-ARXIV-2605-31158 | RP-b78a5f968ec2dbd6 | deep | arXiv:2605.31158v1 | SRC-ARXIV@arXiv:2605.31158v1 | arXiv:2605.31158v1 HTML — §1 Introduction | arXiv:2605.31158v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Overall Performance Evaluation | arXiv:2605.31158v1 HTML — §5 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31158v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31158 | complete |
| SF-2026-ARXIV-2605-31159 | RP-5dab693cf8ebb3af | deep | arXiv:2605.31159v1 | SRC-ARXIV@arXiv:2605.31159v1 | arXiv:2605.31159v1 HTML — §1 Introduction | arXiv:2605.31159v1 HTML — §5 Experiments & Results; §5.1 Experimental Setup; §5.2 Benchmark Comparison | arXiv:2605.31159v1 HTML — §6 Discussion; §7 Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31159v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31159 | complete |
| SF-2026-ARXIV-2605-31164 | RP-f8c1a2e6afd89431 | deep | arXiv:2605.31164v1 | SRC-ARXIV@arXiv:2605.31164v1 | arXiv:2605.31164v1 HTML — §3 Methodology; §Appendix C Formulations of Influence Estimation Methods; §First-Order Symmetric Method | arXiv:2605.31164v1 HTML — §Complexity analysis.; §4 Experiments; §4.1 Experimental Settings | arXiv:2605.31164v1 HTML — §5 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31164v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31164 | complete |
| SF-2026-ARXIV-2605-31167 | RP-d33d7212ad58c727 | deep | arXiv:2605.31167v1 | SRC-ARXIV@arXiv:2605.31167v1 | arXiv:2605.31167v1 HTML — §3.2. Terminology and Framework Definition; §4.1. The BYOK Privacy Model; §4.4. Plugin Architecture: Adding Metrics, Providers, and Datasets | arXiv:2605.31167v1 HTML — §2.5.4. Baseline Grounding: Anchoring Evaluation in Deterministic References; §3.3. Evaluation Workflow; §4.5. Statistical Benchmark Analysis Dashboard [Process] | arXiv:2605.31167v1 HTML — §8. Discussion; §8.4. Limitations; §9. Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31167v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31167 | complete |
| SF-2026-ARXIV-2605-31170 | RP-a6b7dacd4b330c16 | deep | arXiv:2605.31170v1 | SRC-ARXIV@arXiv:2605.31170v1 | arXiv:2605.31170v1 HTML — §Introduction | arXiv:2605.31170v1 HTML — §Results. | arXiv:2605.31170v1 HTML — §Discussion; §Limitations; §Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31170v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31170 | complete |
| SF-2026-ARXIV-2605-31175 | RP-6fda4a7c01b9e917 | deep | arXiv:2605.31175v1 | SRC-ARXIV@arXiv:2605.31175v1 | arXiv:2605.31175v1 HTML — §4 Methodology | arXiv:2605.31175v1 HTML — §4.5 Theoretical Analysis; §5 Experiments; §5.1 Experimental Setup | arXiv:2605.31175v1 HTML — §6 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31175v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31175 | complete |
| SF-2026-ARXIV-2605-31176 | RP-06c2876ab3385fca | deep | arXiv:2605.31176v1 | SRC-ARXIV@arXiv:2605.31176v1 | arXiv:2605.31176v1 HTML — §Architecture. | arXiv:2605.31176v1 HTML — §4 Pipeline & Experimental Setup; §5 Results; §B.6 Efficient batched evaluation over retriever pools | arXiv:2605.31176v1 HTML — §Instructions for reporting errors; no dedicated limitations heading; scope is bounded by the disclosed models, tasks and setup | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31176v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31176 | complete |
| SF-2026-ARXIV-2605-31244 | RP-42016a1cfcc9c7fb | deep | arXiv:2605.31244v1 | SRC-ARXIV@arXiv:2605.31244v1 | arXiv:2605.31244v1 HTML — §Methods to enhance spectral reach.; §Comparison to Direct eNTK Methods.; §Student Architecture. | arXiv:2605.31244v1 HTML — §Experimental setup.; §Results.; §Toward mode-level analysis of semantic structure. | arXiv:2605.31244v1 HTML — §6 Discussion; §Limitations. | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31244v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31244 | complete |
| SF-2026-ARXIV-2605-31264 | RP-e18631d291974e02 | deep | arXiv:2605.31264v1 | SRC-ARXIV@arXiv:2605.31264v1 | arXiv:2605.31264v1 HTML — §1 Introduction | arXiv:2605.31264v1 HTML — §Instructions for reporting errors | arXiv:2605.31264v1 HTML — §8 Discussion; §9 Limitations and Responsible Deployment; §10 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31264v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31264 | complete |
| SF-2026-ARXIV-2605-31278 | RP-70ea2b8ad4cc3b7d | deep | arXiv:2605.31278v1 | SRC-ARXIV@arXiv:2605.31278v1 | arXiv:2605.31278v1 HTML — §4 The GLIDE Framework; §4.4 A decision framework | arXiv:2605.31278v1 HTML — §3 Why Agentic Evaluation Needs PPI; §6 Case Study: Agentic Evaluation in Practice; §6.2 Results | arXiv:2605.31278v1 HTML — §6.3 Discussion; §8 Limitations and Roadmap; §Limitations. | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31278v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31278 | complete |
| SF-2026-ARXIV-2605-31308 | RP-1f069aed50749136 | deep | arXiv:2605.31308v1 | SRC-ARXIV@arXiv:2605.31308v1 | arXiv:2605.31308v1 HTML — §B.12 Agent Framework and Recovery Templates | arXiv:2605.31308v1 HTML — §Outcome-centered evaluation.; §4 Graph Analysis with TraceGraph; §4.4 What Process Demands Do Benchmarks Impose? | arXiv:2605.31308v1 HTML — §6 Discussion and Conclusion; §7 Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31308v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31308 | complete |
| SF-2026-ARXIV-2605-31328 | RP-3f21b7975b62c24a | deep | arXiv:2605.31328v1 | SRC-ARXIV@arXiv:2605.31328v1 | arXiv:2605.31328v1 HTML — §D.3 Different judge model | arXiv:2605.31328v1 HTML — §3.1 Experimental setup; §Evaluation.; §3.2 Results | arXiv:2605.31328v1 HTML — §6 Discussion; §7 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31328v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31328 | complete |
| SF-2026-ARXIV-2605-31354 | RP-b9a591094cfd8df9 | deep | arXiv:2605.31354v1 | SRC-ARXIV@arXiv:2605.31354v1 | arXiv:2605.31354v1 HTML — §Architecture-centric document understanding.; §3 Method; §3.5 Traceability and Audit Framework | arXiv:2605.31354v1 HTML — §3.6 Cost–Utility Analysis; §4 Experiments Setup; §4.1 Evaluation Domains and Distributions | arXiv:2605.31354v1 HTML — §6 Discussions; §7 Limitations; §8 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31354v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31354 | complete |
| SF-2026-ARXIV-2605-31361 | RP-36ce5f16921eb279 | deep | arXiv:2605.31361v1 | SRC-ARXIV@arXiv:2605.31361v1 | arXiv:2605.31361v1 HTML — §3.2 Architecture | arXiv:2605.31361v1 HTML — §4 Evaluation Protocol | arXiv:2605.31361v1 HTML — §5 Discussion and Outlook | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31361v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31361 | complete |
| SF-2026-ARXIV-2605-31365 | RP-56c98c45d432156d | deep | arXiv:2605.31365v1 | SRC-ARXIV@arXiv:2605.31365v1 | arXiv:2605.31365v1 HTML — §3 Method; §Appendix A Details of SCALE Framework and SCALE-20k Dataset; §A.2 Algorithm of the SCALE Framework | arXiv:2605.31365v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.31365v1 HTML — §5 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31365v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31365 | complete |
| SF-2026-ARXIV-2605-31381 | RP-8d81207cef3e4c1d | deep | arXiv:2605.31381v1 | SRC-ARXIV@arXiv:2605.31381v1 | arXiv:2605.31381v1 HTML — §3 Methodology | arXiv:2605.31381v1 HTML — §4 Results; §4.5 Qualitative Analysis; §Appendix D Query Safety Evaluations | arXiv:2605.31381v1 HTML — §5 Discussion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31381v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31381 | complete |
| SF-2026-ARXIV-2605-31408 | RP-111171d228791f56 | deep | arXiv:2605.31408v1 | SRC-ARXIV@arXiv:2605.31408v1 | arXiv:2605.31408v1 HTML — §3. Method | arXiv:2605.31408v1 HTML — §3.2. Benchmark and Task Subset; §3.6. Statistical Analysis; §4. Results | arXiv:2605.31408v1 HTML — §5. Discussion; §6. Threats to Validity; §8. Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31408v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31408 | complete |
| SF-2026-ARXIV-2605-31455 | RP-f010d0846cd09a80 | deep | arXiv:2605.31455v1 | SRC-ARXIV@arXiv:2605.31455v1 | arXiv:2605.31455v1 HTML — §1 Introduction | arXiv:2605.31455v1 HTML — §5 Experiments; §5.1 Experimental Setup; §5.2 Main Results | arXiv:2605.31455v1 HTML — §6 Conclusion & Limitations; §E.3 Case 3: Limitations in Knowledge-Intensive Domains | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31455v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31455 | complete |
| SF-2026-ARXIV-2605-31460 | RP-1de2068e3de689a1 | deep | arXiv:2605.31460v1 | SRC-ARXIV@arXiv:2605.31460v1 | arXiv:2605.31460v1 HTML — §4 Method; §A.9 System Consistency by the Model | arXiv:2605.31460v1 HTML — §5 Evaluation; §Navigation Qualitative Analysis:; §Manipulation Failure Detection Analysis: | arXiv:2605.31460v1 HTML — §6 Limitations, Future Directions and Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31460v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31460 | complete |
| SF-2026-ARXIV-2605-31463 | RP-f809e4fa35253691 | deep | arXiv:2605.31463v1 | SRC-ARXIV@arXiv:2605.31463v1 | arXiv:2605.31463v1 HTML — §3.2 System Architecture and Optimizations | arXiv:2605.31463v1 HTML — §4 ATE-Bench: A Benchmark for Agent-Task Efficiency; §5 Evaluation; §Appendix C Per-Task Results | arXiv:2605.31463v1 HTML — §6 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31463v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31463 | complete |
| SF-2026-ARXIV-2605-31464 | RP-2dfde9f8c800d8f2 | deep | arXiv:2605.31464v1 | SRC-ARXIV@arXiv:2605.31464v1 | arXiv:2605.31464v1 HTML — §2 Method: LLM as Virtual GPU Surrogate | arXiv:2605.31464v1 HTML — §Kernel Evaluation.; §3 Experiments; §Appendix C Per-Evaluation Latency and Throughput on a Single A100 | arXiv:2605.31464v1 HTML — §5 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31464v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31464 | complete |
| SF-2026-ARXIV-2605-31468 | RP-70abc7ffa98f1e52 | deep | arXiv:2605.31468v1 | SRC-ARXIV@arXiv:2605.31468v1 | arXiv:2605.31468v1 HTML — §1 Introduction | arXiv:2605.31468v1 HTML — §7 Case Studies and Evaluation; §7.1 Experimental Setup; §7.4 Experiment Execution and Analysis | arXiv:2605.31468v1 HTML — §9 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31468v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31468 | complete |
| SF-2026-ARXIV-2605-31490 | RP-52584d3caedcbda2 | deep | arXiv:2605.31490v1 | SRC-ARXIV@arXiv:2605.31490v1 | arXiv:2605.31490v1 HTML — §4 Methods | arXiv:2605.31490v1 HTML — §5 Experiments; §5.1 LLM Reasoning Experiments; §5.2 Analysis on Autoregressive Control Task | arXiv:2605.31490v1 HTML — §7 Conclusion; §Discussion.; §8 Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31490v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31490 | complete |
| SF-2026-ARXIV-2605-31509 | RP-e12b573de8b5b15b | deep | arXiv:2605.31509v1 | SRC-ARXIV@arXiv:2605.31509v1 | arXiv:2605.31509v1 HTML — §4.4 Compared Methods | arXiv:2605.31509v1 HTML — §4 Experimental Settings; §4.3 Training and Evaluation; §5 Main Results | arXiv:2605.31509v1 HTML — §8 Conclusion; §Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31509v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31509 | complete |
| SF-2026-ARXIV-2605-31557 | RP-63e4029f0fa8b2ad | deep | arXiv:2605.31557v1 | SRC-ARXIV@arXiv:2605.31557v1 | arXiv:2605.31557v1 HTML — §4 A Unified Framework for Streaming Episodic Memory; excerpt=all Regimes 3.4 Evaluation Protocol and Metrics 4 A Unified Framework for Streaming Episodic Memory 4.1 Memory Management Strategies 5 Experiments and Results 5.1 Controlled Diagnostic Evaluation 5.2 State-of-the-Art Streaming Models 5.3 Semantic Profiles and Temporal Decay 5.4 Memory Budget 6 Conclusion and Limitations References A The EgoStream Benchmark A.1 Hard Negative Generation Protocol A.2 Evidence Moment Annotation A.3 Human Va | arXiv:2605.31557v1 HTML — §EgoStream : A Diagnostic Benchmark for Streaming Episodic Memory in Egocentric Vision; excerpt=EgoStream: A Diagnostic Benchmark for Streaming Episodic Memory in Egocentric Vision Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Related Work 3 The EgoStream Benchmark 3.1 Source Curation and Initial Set of | arXiv:2605.31557v1 HTML — §6 Conclusion and Limitations; excerpt=files and Temporal Decay 5.4 Memory Budget 6 Conclusion and Limitations References A The EgoStream Benchmark A.1 Hard Negative Generation Protocol A.2 Evidence Moment Annotation A.3 Human Validation A.4 Question Categorization Protocol and Labeling Guidelines A.4.1 Iterative Human-in-the-Loop (HITL) Workflow A.4.2 Primary Labeling: The Priority Cascade A.4.3 Secondary Labeling A.5 Answer Validity Window and Recall Regimes A.6 Recall Reg | https://arxiv.org/html/2605.31557v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2605.31557v1.html; sha256:784efa3dd9401423eec8a0f290e8cf670e782aed55597fde5975d551bb4315c8 | claim:SF-2026-ARXIV-2605-31557 | complete |
| SF-2026-ARXIV-2605-31584 | RP-7dbd6b2141fab96f | deep | arXiv:2605.31584v1 | SRC-ARXIV@arXiv:2605.31584v1 | arXiv:2605.31584v1 HTML — §3 Method | arXiv:2605.31584v1 HTML — §4 Experiments; §Benchmarks.; §4.2 Main Results | arXiv:2605.31584v1 HTML — §5 Conclusion; §6 Limitations | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31584v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31584 | complete |
| SF-2026-ARXIV-2605-31593 | RP-892216bebb8fa5d1 | deep | arXiv:2605.31593v1 | SRC-ARXIV@arXiv:2605.31593v1 | arXiv:2605.31593v1 HTML — §1 Introduction | arXiv:2605.31593v1 HTML — §4 Experiments; §Example 2: a shell-script CTF reduced to static analysis.; §Appendix C Agentic Decomposition Attack Results | arXiv:2605.31593v1 HTML — §6 Conclusion | official arXiv exact-v1 HTML https://arxiv.org/html/2605.31593v1; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-31593 | complete |
| SF-2026-ARXIV-2605-31598 | RP-b7fcb71473c10d26 | deep | arXiv:2605.31598v1 | SRC-ARXIV@arXiv:2605.31598v1 | arXiv:2605.31598v1 HTML — §3 Method; excerpt= compression for long-context LLMs and multimodal models. 3 Method 3.1 Core Assumptions 3.2 Method Overview Preliminaries. Streaming cache construction with two memory states. Key insight: dynamic compressed state. 3.3 Per-frame cache-builder forward pass Updating the compressed state via attention-driven selection Virtual sequence length and cache positions. Consistent RoPE scaling across cache building and generation. Decoding using t | arXiv:2605.31598v1 HTML — §4 Results; excerpt=ilding and generation. Decoding using the detailed cache. 4 Results Experimental Setup. Pareto frontier at fixed long-video length. FLOPs reduction enables larger backbones. Cross-backbone ablation across families and scales. Scaling behavior. Sliding-window instability across settings. Compute break-even behavior. 5 Conclusion References 0.A Empirical validation of the assumptions Scope. Shared protocol. 0.A.1 Assumption 1: concentrati | arXiv:2605.31598v1 HTML — §5 Conclusion; excerpt=ual context (e.g. by compressing the KV cache). A practical limitation of these methods is that aggressive compression can substantially degrade long-video performance unless a relatively large fraction of the visual information is retained. For instance, prior work found they must keep a large token fraction (around 60%) to avoid severe degradation when using cache-compression [ 65 ] . This issue can be even more acute for frame droppi | https://arxiv.org/html/2605.31598v1; papers/2026/05/_sources/daily-20260530/exact-v1-html/2605.31598v1.html; sha256:4cd6b084300b553849bb3afa33beab9d3b6b53e971bd9cf05e0587eac1b095ca | claim:SF-2026-ARXIV-2605-31598 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-00144:start -->
#### BudgetDraft: Acceptance-Aware Multi-View Training for Sparse-KV Speculative Decoding

问题与机制：Speculative decoding speeds up autoregressive decoding by using a drafter to propose multiple tokens that a verifier validates in parallel. Owner=`INFER-SPECULATIVE-DECODING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `BudgetDraft: Acceptance-Aware Multi-View Training for Sparse-KV Speculative Decoding` exact-v1 在 §4 Experimental Setup; §5 Experimental Results; §5.4 Sensitivity Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Method`；Evaluation=`§4 Experimental Setup; §5 Experimental Results; §5.4 Sensitivity Analysis`。

Trade-off / failure / fallback：§6 Conclusion; §Limitations 该来源没有证明 `BudgetDraft: Acceptance-Aware Multi-View Training for Sparse-KV Speculative Decoding` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00144:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00144:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00144:end -->

<!-- review:SF-2026-ARXIV-2606-00150:start -->
#### Persona Attack: Incremental Memory Injection Jailbreak Attack against Large Language Models

问题与机制：In this paper, we propose Persona Attack, a memory injection based jailbreak method that manipulates the model's context window through a step by step approach. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Persona Attack: Incremental Memory Injection Jailbreak Attack against Large Language Models` exact-v1 在 §4 Empirical Experiments; §4.1 Experimental setup; §4.2 Experimental Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Proposed Method: Persona Attack`；Evaluation=`§4 Empirical Experiments; §4.1 Experimental setup; §4.2 Experimental Results`。

Trade-off / failure / fallback：§5 Discussion; §5.1 Limitation; §6 Conclusion 该来源没有证明 `Persona Attack: Incremental Memory Injection Jailbreak Attack against Large Language Models` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00150:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00150:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00150:end -->

<!-- review:SF-2026-ARXIV-2606-00152:start -->
#### PrivacyPeek: Auditing What LLM-Based Agents Acquire, Not Just What They Say

问题与机制：To assess its prevalence, we introduce \emph{PrivacyPeek}, a benchmark for evaluating acquisition-stage privacy leakage of LLM-based agents, with $1{,}182$ cases across $7$ acquisition behaviours and $16$ application domains. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `PrivacyPeek: Auditing What LLM-Based Agents Acquire, Not Just What They Say` exact-v1 在 §3.3 Evaluation; §4 Experiments; §4.2 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§6 Mitigation Methods`；Evaluation=`§3.3 Evaluation; §4 Experiments; §4.2 Main Results`。

Trade-off / failure / fallback：§7 Conclusion; §Limitations 该来源没有证明 `PrivacyPeek: Auditing What LLM-Based Agents Acquire, Not Just What They Say` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00152:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00152:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00152:end -->

<!-- review:SF-2026-ARXIV-2606-00160:start -->
#### DataShield: Safety-degrading Data Filtering for LLM Benign Instruction Fine-Tuning

问题与机制：In this paper, we propose DataShield to efficiently and effectively identify potential safety-degrading samples. Owner=`TRAIN-DATA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `DataShield: Safety-degrading Data Filtering for LLM Benign Instruction Fine-Tuning` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§IV Method; excerpt= of LLMs? III-B What does the benign fine-tuning change? IV Method IV-A Promblem Formulation IV-B Compliance Vector Extraction IV-C Safety-Critical Layers Selection IV-D Safety-Degrading Data Filtering V Experiment V-A Experimental Setup V-B Comparative Methods V-C Effectiveness of Safety-degrading Data Selection V-D Safety Performance After Filtering Safety-degrading Samples V-E Effectiveness Analysis of Layer Selection V-F Effectivene`；Evaluation=`§III Mechanistic Interpretability Analysis; excerpt=cal Layers Selection IV-D Safety-Degrading Data Filtering V Experiment V-A Experimental Setup V-B Comparative Methods V-C Effectiveness of Safety-degrading Data Selection V-D Safety Performance After Filtering Safety-degrading Samples V-E Effectiveness Analysis of Layer Selection V-F Effectiveness Analysis of Projection Difference V-G Safety-degrading Data Features V-H Harmful Topic Category V-I KL Divergence Analysis of Safety-degradin`。

Trade-off / failure / fallback：§VI Conclusion; excerpt=e importantly, the fundamental mechanisms behind LLM safety failure caused by benign fine-tuning remain insufficiently explored. To this end, we aim to address the safety degradation caused by benign fine-tuning from a data-centric perspective. Specifically, this paper focuses on the following research questions: RQ1: What are the underlying mechanisms driving safety degradation during the benign fine-tuning of LLMs? RQ2: How can we eff 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00160:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00160:end -->

Books Decision=`Integrate`；fresh-context challenge：benign SFT samples can be safety-degrading even when topic/content filters pass; bind compliance-vector evidence and safety-critical-layer selection to the data-filter artifact, without treating the paper's models or thresholds as universal；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00160:end -->

<!-- review:SF-2026-ARXIV-2606-00162:start -->
#### Modeling Robotics Dataset Construction as an Artifact-Based Build Process

问题与机制：Across dataset sizes from 5.1 to 20.4 GB, Bagzel variants show markedly better scaling behavior than the baseline, especially in warm and incremental modes. Owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Modeling Robotics Dataset Construction as an Artifact-Based Build Process` exact-v1 在 §V Experimental Setup; §VI Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§III Methodology`；Evaluation=`§V Experimental Setup; §VI Results`。

Trade-off / failure / fallback：§VII Conclusion 该来源没有证明 `Modeling Robotics Dataset Construction as an Artifact-Based Build Process` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00162:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00162:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00162:end -->

<!-- review:SF-2026-ARXIV-2606-00172:start -->
#### CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping for GRPO

问题与机制：On-Policy Self-Distillation (OPSD) offers dense token-level guidance, but its token preferences are not necessarily aligned with trajectory correctness; empirical diagnostics show that OPSD signals behave differently on correct and incorrect rollouts, with teacher-positive and teacher-negative gap signals exhibiting different noise profiles. Owner=`TRAIN-RLHF`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping for GRPO` exact-v1 在 §4 Experiments; §4.2 Results; §8.6 Evaluation Details 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Method`；Evaluation=`§4 Experiments; §4.2 Results; §8.6 Evaluation Details`。

Trade-off / failure / fallback：§6 Limitations; §7 Conclusion 该来源没有证明 `CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping for GRPO` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00172:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00172:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00172:end -->

<!-- review:SF-2026-ARXIV-2606-00183:start -->
#### Agentic Transformers Provably Learn to Search via Reinforcement Learning

问题与机制：We study this question in a stochastic $k$-ary tree environment, where an agentic transformer observes only its trajectory history through interaction and receives a terminal reward for reaching a hidden leaf goal node. Owner=`TRAIN-GRPO`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Agentic Transformers Provably Learn to Search via Reinforcement Learning` exact-v1 在 §5 Numerical Experiments; §Results. 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§2.2 Transformer Architecture; §Transformer architecture and multi-turn reasoning.`；Evaluation=`§5 Numerical Experiments; §Results.`。

Trade-off / failure / fallback：§6 Conclusion 该来源没有证明 `Agentic Transformers Provably Learn to Search via Reinforcement Learning` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00183:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00183:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00183:end -->

<!-- review:SF-2026-ARXIV-2606-00186:start -->
#### How to Compare the Security of Code Written by Humans to LLM-generated Code

问题与机制：To facilitate this, we propose an automated framework for conducting comparative studies across human-only, LLM-only, and hybrid conditions. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `How to Compare the Security of Code Written by Humans to LLM-generated Code` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§3 Framework Implementation; excerpt=veloper Centered Security 2.3 Comparing Human to LLM code 3 Framework Implementation 3.1 Creating and Collecting Code 3.2 Framework Design 3.2.1 Reproducibility and Auditing 3.2.2 Containers for Security and Reproducibility 3.3 Framework Results 3.3.1 Species Fair Integrity 3.3.2 Research Utility and Framework Benefits 4 Feasibility Study 4.1 Exercise selection 4.1.1 Human Code Data sources 4.1.2 LLM Code Generation 4.1.3 Handling Error`；Evaluation=`§2.1.1 Run-time Analysis for Errors and Correctness; excerpt=2 Containers for Security and Reproducibility 3.3 Framework Results 3.3.1 Species Fair Integrity 3.3.2 Research Utility and Framework Benefits 4 Feasibility Study 4.1 Exercise selection 4.1.1 Human Code Data sources 4.1.2 LLM Code Generation 4.1.3 Handling Errors 4.2 Feasibility Study Results 4.2.1 Data Analysis 4.2.2 Correctness 4.2.3 Failure Mode 4.2.4 Clarity 4.2.5 Security 5 Discussion 5.1 Limitations 5.2 Future Work 5.3 Ethical Con`。

Trade-off / failure / fallback：§4.2.3 Failure Mode; excerpt=y Study Results 4.2.1 Data Analysis 4.2.2 Correctness 4.2.3 Failure Mode 4.2.4 Clarity 4.2.5 Security 5 Discussion 5.1 Limitations 5.2 Future Work 5.3 Ethical Considerations References A Appendix: Framework and Metrics A.1 Ruff Linter Security Codes B Appendix: LLM Information C Appendix: Coding Exercises License: arXiv.org perpetual non-exclusive license arXiv:2606.00186v1 [cs.CR] 29 May 2026 *1 How to Compare the Security of Code Writ 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00186:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00186:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00186:end -->

<!-- review:SF-2026-ARXIV-2606-00189:start -->
#### Learning to Construct Practical Agentic Systems

问题与机制：Automated design and optimization of agentic LLM-based systems leads to sophisticated systems that substantially improve result quality over off-the-shelf agentic patterns. Owner=`AGENT-WORKFLOW`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Learning to Construct Practical Agentic Systems` exact-v1 在 §4 Experimental results; §Appendix A Description of benchmarks; §A.1 Benchmarks used 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methods; §3.1 Framework; §3.2 Learning and optimization methods`；Evaluation=`§4 Experimental results; §Appendix A Description of benchmarks; §A.1 Benchmarks used`。

Trade-off / failure / fallback：§5 Limitations and broader impacts; §6 Conclusion 该来源没有证明 `Learning to Construct Practical Agentic Systems` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00189:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00189:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00189:end -->

<!-- review:SF-2026-ARXIV-2606-00198:start -->
#### BAGEN: Are LLM Agents Budget-Aware?

问题与机制：We then formalize budget-awareness as progressive interval estimation: at each step of a plan, an agent should predict an upper and lower bound on remaining budget, and alert when completion is unlikely. Owner=`AGENT-PLATFORM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `BAGEN: Are LLM Agents Budget-Aware?` exact-v1 在 §3.4 Experimental Setup; §Appendix B Detailed Experimental Settings; §B.2 Evaluation Protocol 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§3.4 Experimental Setup; §Appendix B Detailed Experimental Settings; §B.2 Evaluation Protocol`。

Trade-off / failure / fallback：§8 Conclusion and Limitations 该来源没有证明 `BAGEN: Are LLM Agents Budget-Aware?` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00198:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00198:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00198:end -->

<!-- review:SF-2026-ARXIV-2606-00206:start -->
#### Quantized Reasoning Models Think They Need to Think Longer, but They Do Not

问题与机制：Across math, coding, and science QA, we find that aggressive PTQ reduces accuracy while increasing chain-of-thought (CoT) length. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Quantized Reasoning Models Think They Need to Think Longer, but They Do Not` exact-v1 在 §3 Experimental Setup; §Appendix A Experimental Details; §Appendix B Additional Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§A.2 Quantization Methods`；Evaluation=`§3 Experimental Setup; §Appendix A Experimental Details; §Appendix B Additional Results`。

Trade-off / failure / fallback：§7 Conclusion, Limitations, and Future Work 该来源没有证明 `Quantized Reasoning Models Think They Need to Think Longer, but They Do Not` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00206:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00206:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00206:end -->

<!-- review:SF-2026-ARXIV-2606-00229:start -->
#### Continuous Reasoning for Vision-Language-Action

问题与机制：Based on this view, we propose Continuous Reasoning for Vision-Language-Action. Owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Continuous Reasoning for Vision-Language-Action` exact-v1 在 §4. Experiments; §Real-robot evaluation.; §Appendix A Experimental Configuration 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1. Introduction`；Evaluation=`§4. Experiments; §Real-robot evaluation.; §Appendix A Experimental Configuration`。

Trade-off / failure / fallback：§5. Conclusions 该来源没有证明 `Continuous Reasoning for Vision-Language-Action` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00229:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00229:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00229:end -->

<!-- review:SF-2026-ARXIV-2606-00232:start -->
#### TIGER: Traceable Inference with Graph-Based Evidence Routing for Mitigating Hallucinations in Multimodal Generation

问题与机制：We study fact-level repair for multimodal generation, where a fluent output may contain specific facts that are not supported by the input. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `TIGER: Traceable Inference with Graph-Based Evidence Routing for Mitigating Hallucinations in Multimodal Generation` exact-v1 在 §4 Experimental Evaluation; §4.1 Experimental Setup; §4.2 Main Results (RQ1) 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology; §E.4 Mechanism Analysis Methodology`；Evaluation=`§4 Experimental Evaluation; §4.1 Experimental Setup; §4.2 Main Results (RQ1)`。

Trade-off / failure / fallback：§5 Conclusion; §Limitations 该来源没有证明 `TIGER: Traceable Inference with Graph-Based Evidence Routing for Mitigating Hallucinations in Multimodal Generation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00232:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00232:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00232:end -->

<!-- review:SF-2026-ARXIV-2606-00251:start -->
#### Capability Self-Assessment: Teaching LLMs to Know Their Limits

问题与机制：Yet we show that modern large language models systematically lack this ability: across diverse model families and scales, they overestimate their competence and attempt queries they cannot solve. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Capability Self-Assessment: Teaching LLMs to Know Their Limits` exact-v1 在 §3.3 CSA Inference & Evaluation; §4 Experiments and Analysis; §4.2 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§3.3 CSA Inference & Evaluation; §4 Experiments and Analysis; §4.2 Main Results`。

Trade-off / failure / fallback：§6 Conclusion; §Appendix F Limitations 该来源没有证明 `Capability Self-Assessment: Teaching LLMs to Know Their Limits` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00251:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00251:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00251:end -->

<!-- review:SF-2026-ARXIV-2606-00257:start -->
#### ARCA: Adapter-Residual Credit Assignment When Token Signals Degenerate

问题与机制：We formalize this behavior and propose measuring it directly with concentration diagnostics such as weight Gini and effective-token ratio. Owner=`TRAIN-GRPO`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `ARCA: Adapter-Residual Credit Assignment When Token Signals Degenerate` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methods; excerpt=nk Adaptation in Language RL 2.2 Positioning of This Work 3 Methods 3.1 Policy Gradient with Trajectory-Level Reward 3.2 Token-Level Credit Redistribution 3.3 Intrinsic Token-Weighting Mechanisms Uniform Weighting (Baseline). Surprisal Weighting. Entropy-Reduction Weighting. Policy-Divergence Weighting. Length-Robust Normalization. Batch-Level Baselines. 3.4 Signal Degeneration Under Low-Rank Adaptation Notation. Degeneration of surpris`；Evaluation=`§4 Experiments; excerpt=pse. Interpretation as implicit gradient-informed credit. 4 Experiments 4.1 Setup Model and task. Training. Methods. 4.2 Main Results on MATH 4.3 Credit-Assignment Diagnostics 4.4 Results and Discussion 4.5 Implementation and Metrics 4.6 Compute 4.7 Broader Impacts 4.8 Limitations 5 Conclusion References A Extended Related Work A.1 From RLHF to RLVR A.2 Critic-Based and Critic-Free Policy Optimization A.3 Reasoning-Specific Analyses of `。

Trade-off / failure / fallback：§4.4 Results and Discussion; excerpt=s on MATH 4.3 Credit-Assignment Diagnostics 4.4 Results and Discussion 4.5 Implementation and Metrics 4.6 Compute 4.7 Broader Impacts 4.8 Limitations 5 Conclusion References A Extended Related Work A.1 From RLHF to RLVR A.2 Critic-Based and Critic-Free Policy Optimization A.3 Reasoning-Specific Analyses of RLVR A.4 Fine-Grained Credit Assignment Beyond Uniform Token Updates A.5 Alternative Action Granularities and Token Selection B Addi 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00257:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00257:end -->

Books Decision=`Integrate`；fresh-context challenge：adapter-constrained GRPO can collapse token credit into a few residual directions; concentration diagnostics and adapter-residual redistribution are a bounded credit-assignment branch, not a general replacement for outcome rewards；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00257:end -->

<!-- review:SF-2026-ARXIV-2606-00267:start -->
#### StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement

问题与机制：To enable robust policy evaluation and improvement over WM imaginations, we propose StressDream, which steers imaginations toward high-impact yet plausible outcomes specified at inference time by optimizing the initial noise of diffusion-based WMs. Owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement` exact-v1 在 §3 Setup: Policy Evaluation and Improvement with Video World Models; §6 Experiments: Robust Policy Evaluation and Improvement; §6.1 Robust Policy Evaluation using State-of-the-Art Video World Models 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§5 Case Study: Steering Dubins Car Video World Model`；Evaluation=`§3 Setup: Policy Evaluation and Improvement with Video World Models; §6 Experiments: Robust Policy Evaluation and Improvement; §6.1 Robust Policy Evaluation using State-of-the-Art Video World Models`。

Trade-off / failure / fallback：§7 Conclusion; §Appendix F Limitations & Discussions 该来源没有证明 `StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00267:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00267:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00267:end -->

<!-- review:SF-2026-ARXIV-2606-00269:start -->
#### Closed-Loop Neural Activation Control in Vision-Language-Action Models

问题与机制：We propose CTRL-STEER, a closed-loop framework that replaces static intervention strength with adaptive, time-varying control signals. Owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Closed-Loop Neural Activation Control in Vision-Language-Action Models` exact-v1 在 §4 Experiments; §4.1 Results.; §Appendix C Time Complexity Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Approach`；Evaluation=`§4 Experiments; §4.1 Results.; §Appendix C Time Complexity Analysis`。

Trade-off / failure / fallback：§5 Conclusion 该来源没有证明 `Closed-Loop Neural Activation Control in Vision-Language-Action Models` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00269:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00269:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00269:end -->

<!-- review:SF-2026-ARXIV-2606-00271:start -->
#### HeLoCo: Efficient asynchronous low-communication training under data and device heterogeneity

问题与机制：To address this limitation, we propose \textbf{HeLoCo}, a direction-aware correction method for asynchronous low-communication training that uses outer momentum as a reference for the current optimization trajectory and selectively adjusts incoming pseudo-gradients before the outer update. Owner=`TRAIN-DISTRIBUTED-TRAINING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `HeLoCo: Efficient asynchronous low-communication training under data and device heterogeneity` exact-v1 在 §4 Experiments and Analyses; §Non-IID data domain analysis. 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology`；Evaluation=`§4 Experiments and Analyses; §Non-IID data domain analysis.`。

Trade-off / failure / fallback：§5 Conclusion; §Limitations and future work. 该来源没有证明 `HeLoCo: Efficient asynchronous low-communication training under data and device heterogeneity` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00271:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00271:end -->

Books Decision=`Integrate`；fresh-context challenge：arrival reweighting corrects worker-frequency bias but not stale pseudo-gradient direction; outer momentum can be a current-trajectory reference, with correction variance and synchronization fallback retained；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00271:end -->

<!-- review:SF-2026-ARXIV-2606-00279:start -->
#### Bit-Exact AI Inference Verification Without Performance Tradeoffs

问题与机制：We demonstrate that such bitwise-precise re-computation does not require access to identical hardware, via a software-only emulation of LLM inference across multiple NVIDIA GPU variants. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Bit-Exact AI Inference Verification Without Performance Tradeoffs` exact-v1 在 §3.2 Results; §4.4 Diagnostics and Results; §Appendix B MoE Router Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3.1 Methodology; §4.1 Tensor Core Arithmetic Model`；Evaluation=`§3.2 Results; §4.4 Diagnostics and Results; §Appendix B MoE Router Analysis`。

Trade-off / failure / fallback：§5 Limitations 该来源没有证明 `Bit-Exact AI Inference Verification Without Performance Tradeoffs` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00279:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00279:end -->

Books Decision=`Integrate`；fresh-context challenge：bit-exact inference verification is an evidence/replay contract: software emulation can reproduce selected GPU numeric paths without identical hardware, but only for the disclosed operations, models and emulator coverage; it is not a security proof or performance guarantee；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00279:end -->

<!-- review:SF-2026-ARXIV-2606-00284:start -->
#### Parameter Alignment Mitigates Catastrophic Forgetting in Multilingual Expert Language Models

问题与机制：We link this forgetting to parameter drift in multilingual CPT and present a suite of five layer-aware parameter alignment strategies: hard layer freezing, soft regularization, post-hoc weight reversion, and model merging. Owner=`TRAIN-PRETRAINING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Parameter Alignment Mitigates Catastrophic Forgetting in Multilingual Expert Language Models` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§4.2 Layer Design and Task-Specific Trade-offs; excerpt=ent, distributed multilingual training. Drawing on targeted methods for low-resource language families ( Downey et al., 2024 ; Ogueji et al., 2021 ) , we generalize this approach to training language family experts, scaling the language coverage per expert while limiting intra-expert interference ( Chronopoulou et al., 2023 ) . However, while catastrophic forgetting has been studied in dense multilingual models ( Owodunni and Kumar, 202`；Evaluation=`§3 Experiments; excerpt=Grouping 2.2 Parameter Alignment Strategies 2.3 Baselines 3 Experiments 3.1 Experimental Setup 3.2 Language Acquisition 3.3 Catastrophic Forgetting on Downstream Tasks 3.4 Translation Quality (FLORES-200) 3.5 Within-Family Generalization 4 Understanding Layer-Aware Adaptation 4.1 Causal Analysis of Layer Drift 4.2 Layer Design and Task-Specific Trade-offs 5 Related Work 6 Conclusion References A Appendix A.1 Held-Out Evaluation Language`。

Trade-off / failure / fallback：§6 Conclusion; excerpt=r broad-coverage) rather than by a single aggregate metric. Limitations All experiments use a single 4B-parameter model (Gemma-3 4B) with a fixed budget of 5B tokens per family from one web corpus (MADLAD-400); we do not evaluate whether strategy rankings transfer to other model scales, architectures, or data regimes. The individual strategies are not themselves novel and each builds on established techniques, so our contribution is the 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00284:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00284:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00284:end -->

<!-- review:SF-2026-ARXIV-2606-00301:start -->
#### FLaG: Fine-Grained Latent Grouping for Hallucination Detection

问题与机制：In this work, we formulate hallucination detection as a mechanism-aware evidence aggregation problem, where diverse representation- and token-level signals must be interpreted under multiple latent explanations. Owner=`PLATFORM-MONITORING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `FLaG: Fine-Grained Latent Grouping for Hallucination Detection` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§3. Methodology; excerpt=d Work 2.1 Hallucination Detection 2.2 Mixture-of-Experts 3 Methodology 3.1 Problem Formulation 3.2 Multi-View Evidence Representation 3.2.1 Latent Geometry as Evidential Signals 3.2.2 Probabilistic Trace as Evidential Signals 3.3 Group-Aware Evidential Reasoning 3.3.1 Prototype-based Evidence Allocation 3.3.2 Log-Marginal Evidence Aggregation 3.4 Learning Objective 3.4.1 Supervised Objective. 3.4.2 Semi-Supervised Objective. 4 Theoreti`；Evaluation=`§4. Theoretical Analysis; excerpt=etical Analysis 4.1 Analysis of Approximation Error Bound 5 Experiments 5.1 Experimental Settings 5.1.1 Evaluation 5.1.2 Baselines 5.1.3 Implementation Details 5.2 Overall Performance 5.2.1 Transferability 5.2.2 Robustness 5.2.3 Interpretability 5.3 Ablation Study 5.3.1 Component-Wise Ablation 5.3.2 Hyperparameter Sensitivity 6 Conclusions and Limitations References A In-depth Theoretical Analysis A.1 Detailed Proof of Theorem Step 1: E`。

Trade-off / failure / fallback：§6. Conclusions and Limitations; excerpt=Ablation 5.3.2 Hyperparameter Sensitivity 6 Conclusions and Limitations References A In-depth Theoretical Analysis A.1 Detailed Proof of Theorem Step 1: Expand the numerator/denominator under the mixture. Step 2: Multiply and divide each term by π 0 ​ ( g ) ​ p g ​ ( 𝐱 ∣ 0 ) \pi_{0}(g)p_{g}(\mathbf{x}\mid 0) . Step 3: Identify the posterior under the null. Step 4: Convert into log-sum-exp form. Remark (why the posterior is under y = 0 y 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00301:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00301:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00301:end -->

<!-- review:SF-2026-ARXIV-2606-00305:start -->
#### Bridging Reasoning Trajectories in On-Policy Distillation via Near-Future Guidance

问题与机制：We show that this "trajectory-sampled but token-learned" mechanism cannot reliably bridge student trajectories toward teacher trajectories. Owner=`TRAIN-RLHF`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Bridging Reasoning Trajectories in On-Policy Distillation via Near-Future Guidance` exact-v1 在 §4 Empirical Experiments; §4.2 Evaluation; §4.3 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology`；Evaluation=`§4 Empirical Experiments; §4.2 Evaluation; §4.3 Main Results`。

Trade-off / failure / fallback：§7 Conclusion; §8 Limitations 该来源没有证明 `Bridging Reasoning Trajectories in On-Policy Distillation via Near-Future Guidance` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00305:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00305:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00305:end -->

<!-- review:SF-2026-ARXIV-2606-00308:start -->
#### How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval

问题与机制：Large-language-model code generation has shifted from single-shot prompting to multi-agent orchestrations - analyst, coder, tester, and debugger pipelines - and is evaluated almost exclusively on functional correctness. Owner=`AGENT-MULTI-AGENT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval; excerpt=How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract I Introduction II Related Work II-A Multi-Agent LLM Code Generation II-B `；Evaluation=`§III-D Benchmark and Dataset; excerpt=ration Architecture (Six Configurations) III-C Models III-D Benchmark and Dataset III-E Dependent Variables: Complexity Metrics III-F Pass-Conditional Robustness Analysis III-G Statistical Analysis III-G 1 Rationale for Non-Parametric Repeated-Measures Methods III-G 2 Omnibus: Friedman’s Test III-G 3 Post-hoc: Wilcoxon Signed-Rank with Holm Correction III-G 4 Effect Sizes III-G 5 Missing Data and Block Construction III-G 6 Software III-`。

Trade-off / failure / fallback：§V Discussion; excerpt=ness Conditioning IV-F Complexity and Functional Accuracy V Discussion V-A Interpretation V-B Implications for Practitioners V-C Threats to Validity VI Conclusion References License: arXiv.org perpetual non-exclusive license arXiv:2606.00308v1 [cs.SE] 29 May 2026 How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval Nazmus Ashrafi Affiliation: Independent Researcher nazmus.s.ashrafi@g 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00308:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00308:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：the paired HumanEval study supplies workload-specific evidence for a proposition already explicit in Ch82: added roles/topology require equal-budget benefit and coordination-cost evidence; it does not introduce a new state or commit owner；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2606-00308:end -->

<!-- review:SF-2026-ARXIV-2606-00318:start -->
#### Belief Consistency Between Foundation-Model Evidence and Geometric Perception in Persistent Robotic Maps

问题与机制：We propose an update operator with two cooperating mechanisms: a per-class calibrated commit gate, and a per-event conflict-drop window that refuses to commit foundation-model claims contradicted by the geometric channel at the moment of the claim. Owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Belief Consistency Between Foundation-Model Evidence and Geometric Perception in Persistent Robotic Maps` exact-v1 在 §5 Experimental Setup; §6 Results; §Choice of indoor benchmark. 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§Where the framework applies.; §What the framework does not address.`；Evaluation=`§5 Experimental Setup; §6 Results; §Choice of indoor benchmark.`。

Trade-off / failure / fallback：§7 Discussion 该来源没有证明 `Belief Consistency Between Foundation-Model Evidence and Geometric Perception in Persistent Robotic Maps` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00318:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00318:end -->

Books Decision=`Integrate`；fresh-context challenge：persistent map updates need a calibrated per-class commit gate plus a conflict-drop window when foundation-model claims disagree with geometric evidence; the world-state owner, not the VLA controller, owns this revision rule；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00318:end -->

<!-- review:SF-2026-ARXIV-2606-00329:start -->
#### Benchmarking Recursive-Collapse Warning Claims Under Matched False-Positive Control

问题与机制：We introduce Loopzero, a claim-bounded benchmark framework for testing whether recursive failures follow a directional telemetry pattern: rising gain (G), recursive persistence (p), and declining diversity ($δ$). Owner=`PLATFORM-MONITORING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Benchmarking Recursive-Collapse Warning Claims Under Matched False-Positive Control` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§§Conditional telemetry bridge; §Telemetry witnesses and matched-false-positive benchmarking; excerpt=nternal degradation — before overt failure becomes visible. We introduce Loopzero, a claim-bounded benchmark framework for testing whether recursive failures follow a directional telemetry pattern: rising gain (G), recursive persistence (p), and declining diversity ( 𝛿). The claim boundary is specified in Lean; the Lean artifact does not verify real telemetry, benchmark validity, or detector performance. We evaluate the bridge on two fr`；Evaluation=`§§Benchmark protocol; §Results; excerpt=Benchmarking Recursive-Collapse Warning Claims Under Matched False-Positive Control David Mullett Independent Researcher ORCID: 0009-0004-2543-1664 Corresponding author: David Mullett ⋅ d@loopzero.org One-Sentence Summary A matched-FP benchmark for recursive collapse: signature directionally aligned across domains; no detector accepted. Abstract Recursive systems can enter collapse-like regimes — self-reinforcing amplification, persiste`。

Trade-off / failure / fallback：§§Scope summary; §Limitations and failure of all tested detectors to reach accepted operating point; excerpt= that mask accelerating internal degradation — before overt failure becomes visible. We introduce Loopzero, a claim-bounded benchmark framework for testing whether recursive failures follow a directional telemetry pattern: rising gain (G), recursive persistence (p), and declining diversity ( 𝛿). The claim boundary is specified in Lean; the Lean artifact does not verify real telemetry, benchmark validity, or detector performance. We eval 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00329:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00329:end -->

Books Decision=`Weekly Only — Context`；fresh-context challenge：Loopzero is a claim-bounded benchmark proposal; its LLM matched-false-positive evaluation is explicitly deferred, so it cannot yet change the monitoring sensor or release contract；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2606-00329:end -->

<!-- review:SF-2026-ARXIV-2606-00341:start -->
#### ROGUE: Misaligned Agent Behavior Arising from Ordinary Computer Use

问题与机制：Although much work has focused on agent safety in the presence of an adversary, we show that agents can exhibit misaligned behavior even in benign settings, taking unsafe actions when those actions are instrumental to task completion. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `ROGUE: Misaligned Agent Behavior Arising from Ordinary Computer Use` exact-v1 在 §Agent benchmarks.; §3 ROGUE: Resource Override and Guardrail Undermining Evaluation; §Evaluation 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§Agent benchmarks.; §3 ROGUE: Resource Override and Guardrail Undermining Evaluation; §Evaluation`。

Trade-off / failure / fallback：§6 Discussion; §Limitations and Future Work 该来源没有证明 `ROGUE: Misaligned Agent Behavior Arising from Ordinary Computer Use` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00341:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00341:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00341:end -->

<!-- review:SF-2026-ARXIV-2606-00348:start -->
#### Augur: Pre-Execution Energy Prediction for Workflow Tasks in Heterogeneous Clusters

问题与机制：To address this critical gap, we propose Augur, a novel method to predict the energy consumption of scientific workflow tasks prior to execution. Owner=`PLATFORM-COST`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Augur: Pre-Execution Energy Prediction for Workflow Tasks in Heterogeneous Clusters` exact-v1 在 §IV Evaluation; §IV-A Experimental Setup 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§III System Design; §III-A Approach Overview; §Comparison with Baseline Methodologies`；Evaluation=`§IV Evaluation; §IV-A Experimental Setup`。

Trade-off / failure / fallback：§IV-H Discussion; §VI Conclusion 该来源没有证明 `Augur: Pre-Execution Energy Prediction for Workflow Tasks in Heterogeneous Clusters` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00348:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00348:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：pre-execution workflow-energy prediction is a domain instance of the existing calibrated cost-predictor contract; the disclosed clusters and error distribution do not create a new platform owner or universal estimator；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2606-00348:end -->

<!-- review:SF-2026-ARXIV-2606-00365:start -->
#### SPARQLe: Sub-Precision Activation Representation for Quantized LLM Inference

问题与机制：Our proposal, SPARQLe, is a hardware-software co-design framework that exploits this sub-precision redundancy in any given quantized model. Owner=`INFER-TENSORRT-LLM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `SPARQLe: Sub-Precision Activation Representation for Quantized LLM Inference` exact-v1 在 §4. Experimental Methodology; §5. Experimental Results; §5.1. Accuracy and Performance Evaluation 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3. SPARQLe Methodology; §3.3. SPARQLe Hardware Architecture; §4. Experimental Methodology`；Evaluation=`§4. Experimental Methodology; §5. Experimental Results; §5.1. Accuracy and Performance Evaluation`。

Trade-off / failure / fallback：§6. Conclusion 该来源没有证明 `SPARQLe: Sub-Precision Activation Representation for Quantized LLM Inference` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00365:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00365:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00365:end -->

<!-- review:SF-2026-ARXIV-2606-00376:start -->
#### The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary

问题与机制：Extended chain-of-thought reasoning can degrade performance on deterministic state-tracking tasks, not solely because of preference biases but, on the evidence we present, because of information-theoretic limits in the capacity of decoder-only attention. Owner=`AGENT-TOOL-CALLING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary` exact-v1 在 §Fine-tuning experiment confirming architectural ceil-; §Deterministic Horizon and real-world benchmarks, designed to require determinis-; §Fine-Tuning Experiment 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§Theoretical Framework; §Context-Dependent Error Model; §Architecture Ablations`；Evaluation=`§Fine-tuning experiment confirming architectural ceil-; §Deterministic Horizon and real-world benchmarks, designed to require determinis-; §Fine-Tuning Experiment`。

Trade-off / failure / fallback：§Conclusion 该来源没有证明 `The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00376:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00376:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00376:end -->

<!-- review:SF-2026-ARXIV-2606-00380:start -->
#### SUPREME: A Multi-GPU Framework for Reproducible Image Unlearning Method Evaluation

问题与机制：We introduce SUPREME, an open-source framework that distributes these stages across multiple GPUs. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `SUPREME: A Multi-GPU Framework for Reproducible Image Unlearning Method Evaluation` exact-v1 在 §3 Experimental Methodology; §4 Results and Discussion; §0.B.1 Model evaluation metrics 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§2 SUPREME Framework; §3 Experimental Methodology`；Evaluation=`§3 Experimental Methodology; §4 Results and Discussion; §0.B.1 Model evaluation metrics`。

Trade-off / failure / fallback：§4 Results and Discussion; §5 Conclusion 该来源没有证明 `SUPREME: A Multi-GPU Framework for Reproducible Image Unlearning Method Evaluation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00380:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00380:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00380:end -->

<!-- review:SF-2026-ARXIV-2606-00382:start -->
#### CRMA: A Spectrally-Bounded Backbone for Modular Continual Fine-Tuning of LLMs

问题与机制：We introduce CRMA (Constrained Residual Mixing Adapter), a residual adapter whose internal mixing matrix M is doubly-stochastic at every forward pass via Sinkhorn normalization, so by Birkhoff's theorem ||M||_2 <= 1 holds by construction -- a structural bound, not a penalty. Owner=`TRAIN-PRETRAINING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `CRMA: A Spectrally-Bounded Backbone for Modular Continual Fine-Tuning of LLMs` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§3.1 Problem Formulation; excerpt=ral Norm Bound From mixing bound to adapter bound. Scope. 4 Method: CRMA 4.1 Doubly-Stochastic Mixing via Sinkhorn Normalization 4.2 Residual Behavior 4.3 Internal Transformation 4.4 What Is Omitted 4.5 Pseudocode 5 Mechanism Validation 5.1 Experimental Setup Routing at inference. 5.2 Spectral Norm Stability 5.3 Architectural Role of the Bound 6 Experiments 6.1 Continual Learning Across Real-World Domains 6.1.1 Multi-Model QA 6.1.2 Stan`；Evaluation=`§Known limitation: global benchmark drift.; excerpt=bution is. What this paper proves. Known limitation: global benchmark drift. How CRMA is applied. Contributions. Claim summary. 2 Positioning: Why Not Frozen-Substrate Modular LoRA? Anticipated objections. Role decomposition. 3 Theoretical Foundation 3.1 Problem Formulation 3.2 The Mixing Matrix as Non-Expansive Map 3.3 Near-Identity Initialization 3.4 Spectral Norm Bound From mixing bound to adapter bound. Scope. 4 Method: CRMA 4.1 Dou`。

Trade-off / failure / fallback：§Known limitation: global benchmark drift.; excerpt=A’s specific contribution is. What this paper proves. Known limitation: global benchmark drift. How CRMA is applied. Contributions. Claim summary. 2 Positioning: Why Not Frozen-Substrate Modular LoRA? Anticipated objections. Role decomposition. 3 Theoretical Foundation 3.1 Problem Formulation 3.2 The Mixing Matrix as Non-Expansive Map 3.3 Near-Identity Initialization 3.4 Spectral Norm Bound From mixing bound to adapter bound. Scope. 4 M 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00382:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00382:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00382:end -->

<!-- review:SF-2026-ARXIV-2606-00392:start -->
#### Detector-Evasive LLM Paraphrasing via Constrained Policy Optimization

问题与机制：We propose Detector Evasion Policy Optimization (DEPO), a Lagrangian primal-dual reinforcement learning algorithm with a novel GRPO-style group-based policy update. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Detector-Evasive LLM Paraphrasing via Constrained Policy Optimization` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§2 Problem Formulation; excerpt=-guided paraphrasing attacks, but existing detector-evasion methods often lack precise control over semantic preservation. In particular, optimizing directly for detector evasion can degrade fine-grained semantics, whereas scalarized reward designs provide only indirect, weight-sensitive control over the evasion–semantics trade-off. We address this limitation by formulating detector-evasive LLM paraphrasing as a Constrained Markov Decis`；Evaluation=`§4 Experiments; excerpt=roblem Formulation 3 Detector Evasion Policy Optimization 4 Experiments 4.1 Experimental Setup 4.2 Evasion vs. Semantics 4.3 Cross Detector Generalization 4.4 Cross Domain Generalization 4.5 Cross-Reward Validation 4.6 Summary 5 Conclusion References A Experimental Details A.1 Pseudocode of DEPO A.2 Baselines, Detectors, Evaluation Metrics and Evaluation Dataset A.3 Peer-review Dataset A.4 Peer-review RoBERTa Detector Validation A.5 Cho`。

Trade-off / failure / fallback：§5 Conclusion; excerpt=ntrol over the evasion–semantics trade-off. We address this limitation by formulating detector-evasive LLM paraphrasing as a Constrained Markov Decision Process, where detector evasion is the primary objective and semantic preservation is enforced as an explicit constraint. We propose Detector Evasion Policy Optimization (DEPO), a Lagrangian primal-dual reinforcement learning algorithm with a novel GRPO-style group-based policy update.  该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00392:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00392:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00392:end -->

<!-- review:SF-2026-ARXIV-2606-00395:start -->
#### PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning

问题与机制：To address this limitation, we propose Predictive Routing Replay (PR2), which augments each router with a lightweight evolution predictor that learns to anticipate short-horizon router evolution. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning` exact-v1 在 §5 Experiments; §Evaluation Benchmarks.; §Cross-Model Evaluation. 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§5 Experiments; §Evaluation Benchmarks.; §Cross-Model Evaluation.`。

Trade-off / failure / fallback：§6 Conclusion 该来源没有证明 `PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00395:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00395:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00395:end -->

<!-- review:SF-2026-ARXIV-2606-00400:start -->
#### Dynamic Proxy-Mixing: Transferring Replay Controllers from Small to Large Models for Continual Instruction Tuning

问题与机制：We propose PROX-YMIX, a framework that learns a dynamic replay controller on a small proxy model and transfers the frozen controller to a larger target. Owner=`TRAIN-SFT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Dynamic Proxy-Mixing: Transferring Replay Controllers from Small to Large Models for Continual Instruction Tuning` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§5 Methodology; excerpt=n 2 Related Work 3 Problem Setting 4 Forgetting Mirroring 5 Methodology Controller Formulation State Representation Action Space and Replay Mixture Reward Design Policy Optimization and Transfer 6 Experimental Setup 7 Results Aggregate Performance on LLaMA-3-8B Safety-Critical Sequence Analysis Cross-Target Transfer Sensitivity Analysis 8 Analysis Interpreting the Learned Replay Policy Dynamics Ablation Study of Controller Design Choice`；Evaluation=`§6 Experimental Setup; excerpt=ay Mixture Reward Design Policy Optimization and Transfer 6 Experimental Setup 7 Results Aggregate Performance on LLaMA-3-8B Safety-Critical Sequence Analysis Cross-Target Transfer Sensitivity Analysis 8 Analysis Interpreting the Learned Replay Policy Dynamics Ablation Study of Controller Design Choices When and Why Proxy Transfer Works 9 Conclusion References A Extended Related Work B Method Positioning Analysis C Full Proxy Training A`。

Trade-off / failure / fallback：§9 Conclusion; excerpt=ttings where the proxy assumption breaks down, highlighting limitations for robust deployment. 1 Introduction Language models are rarely adapted in a single step. A general-purpose chat model is typically fine-tuned sequentially across a stream of heterogeneous domains. It ranges from code generation to medical question answering, legal drafting, creative writing, multilingual instruction following, and evolving safety policies. While t 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00400:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00400:end -->

Books Decision=`Integrate`；fresh-context challenge：continual SFT can learn a replay-mixture controller on a proxy and transfer the frozen policy to a larger target; controller identity, proxy-target compatibility and failure of the proxy assumption must join the training state；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00400:end -->

<!-- review:SF-2026-ARXIV-2606-00408:start -->
#### Masking Stale Observations Helps Search Agents -- Until It Doesn't: A Regime Map and Its Mechanism

问题与机制：We study observation masking through a systematic sweep over various agent backbones (4B to 284B parameters) and three retrievers on offline and live-web agentic search benchmarks. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Masking Stale Observations Helps Search Agents -- Until It Doesn't: A Regime Map and Its Mechanism` exact-v1 在 §3 Experiment Setup; §3.1 Benchmarks; §4 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§2 Methodology`；Evaluation=`§3 Experiment Setup; §3.1 Benchmarks; §4 Main Results`。

Trade-off / failure / fallback：§7 Conclusion; §Limitations 该来源没有证明 `Masking Stale Observations Helps Search Agents -- Until It Doesn't: A Regime Map and Its Mechanism` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00408:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00408:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00408:end -->

<!-- review:SF-2026-ARXIV-2606-00414:start -->
#### Auditing Near-Optimal Policies Can Be Exponentially Hard: Conditional Query Lower Bounds via Occupancy Rashomon Capacity

问题与机制：Because occupancy measures identify behavior only up to occupancy equivalence, we formulate auditing at the occupancy-class level and distinguish exact local-query oracles from noisy sample-query oracles. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Auditing Near-Optimal Policies Can Be Exponentially Hard: Conditional Query Lower Bounds via Occupancy Rashomon Capacity` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§3 Problem Formulation; excerpt=tests face an additional inverse-squared-signal budget. The framework clarifies both the promise and the limits of capacity-based safety claims: capacity counts how many distinguishable near-optimal occupancy classes exist, while sparse signatures and sample signals determine how structurally difficult those classes are to find. References [1] Chace Ashcraft and Kiran Karra. Poisoning deep reinforcement learning agents with in-distribut`；Evaluation=`§8 Controlled Benchmarks; excerpt=r Verification 7 Capacity-Aware Regularization 8 Controlled Benchmarks 9 Discussion 10 Conclusion References A Additional Proof Details A.1 Yao reduction for Theorem A.2 Constants in the hidden-branch construction B Additional Benchmarks B.1 Trigger-room tabular benchmark B.2 Noisy-trigger sample scales B.3 Exact enumeration under the regularized objective B.4 Continuous-control auditing quantities B.5 Visual-action auditing quantities `。

Trade-off / failure / fallback：§9 Discussion; excerpt=n 7 Capacity-Aware Regularization 8 Controlled Benchmarks 9 Discussion 10 Conclusion References A Additional Proof Details A.1 Yao reduction for Theorem A.2 Constants in the hidden-branch construction B Additional Benchmarks B.1 Trigger-room tabular benchmark B.2 Noisy-trigger sample scales B.3 Exact enumeration under the regularized objective B.4 Continuous-control auditing quantities B.5 Visual-action auditing quantities B.6 Experimen 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00414:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00414:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00414:end -->

<!-- review:SF-2026-ARXIV-2606-00424:start -->
#### Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight

问题与机制：We study a more tractable form of weak supervision: using a weak model as a critic rather than as a labeler or judge. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight` exact-v1 在 §Experimental Setting.; §5 Opcd Training-Time Experiments; §Experimental Setup. 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§Weak Model Critique Framework Improves Strong Model Performance Across Tasks and Model Types.; §4 Method`；Evaluation=`§Experimental Setting.; §5 Opcd Training-Time Experiments; §Experimental Setup.`。

Trade-off / failure / fallback：§6 Conclusion 该来源没有证明 `Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00424:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00424:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00424:end -->

<!-- review:SF-2026-ARXIV-2606-00432:start -->
#### Grounded Decoding: Retrieval-Anchored Probability Fusion for Faithful RAG

问题与机制：We propose a novel training-free decoding framework, \emph{Grounded Decoding}, designed to improve factual consistency in RAG without modifying model parameters. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Grounded Decoding: Retrieval-Anchored Probability Fusion for Faithful RAG` exact-v1 在 §4 Experimental Setup; §5 Results; §Token-Level Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§Training-time and Decoding-time Methods; §3 Methodology`；Evaluation=`§4 Experimental Setup; §5 Results; §Token-Level Analysis`。

Trade-off / failure / fallback：§6 Conclusion; §Limitations; §Appendix F Extended Discussion 该来源没有证明 `Grounded Decoding: Retrieval-Anchored Probability Fusion for Faithful RAG` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00432:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00432:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00432:end -->

<!-- review:SF-2026-ARXIV-2606-00437:start -->
#### EST-PRM: Stress-Testing Process Reward Models Before They Become Load-Bearing

问题与机制：Such transformations can change how PRM scores relate to correctness signals, leading to different failure modes across models.To address this gap, we introduce \textbf{EST-PRM}, a stress-testing framework for dense process rewards. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `EST-PRM: Stress-Testing Process Reward Models Before They Become Load-Bearing` exact-v1 在 §Process reward models, benchmarks, and EST-PRM positioning.; §3.1 Formal Vulnerability Analysis; §4 Experimental Protocol 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 The EST-PRM Framework; §B.1 Formal definitions of mitigation methods`；Evaluation=`§Process reward models, benchmarks, and EST-PRM positioning.; §3.1 Formal Vulnerability Analysis; §4 Experimental Protocol`。

Trade-off / failure / fallback：§7 Conclusion; §Limitations 该来源没有证明 `EST-PRM: Stress-Testing Process Reward Models Before They Become Load-Bearing` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00437:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00437:end -->

Books Decision=`Integrate`；fresh-context challenge：process reward models become load-bearing sensors and need semantics-preserving/adversarial transformation stress tests, false-positive accounting and mitigation coverage before release; tested PRMs do not establish universal robustness；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00437:end -->

<!-- review:SF-2026-ARXIV-2606-00439:start -->
#### Physical Object Understanding with a Physically Controllable World Model

问题与机制：We introduce a new class of probabilistic world models that support estimation of the probability of any visual variable, such as appearance and dynamics, conditioned on any other variables. Owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Physical Object Understanding with a Physically Controllable World Model` exact-v1 在 §B Additional Qualitative Results; §B.5 Point-prompted movable object segmentation results; §B.6 Unprompted movable object segmentation results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 PSI architecture and training details`；Evaluation=`§B Additional Qualitative Results; §B.5 Point-prompted movable object segmentation results; §B.6 Unprompted movable object segmentation results`。

Trade-off / failure / fallback：§5 Conclusion & Future Work 该来源没有证明 `Physical Object Understanding with a Physically Controllable World Model` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00439:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00439:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-00439:end -->

<!-- review:SF-2026-ARXIV-2606-00448:start -->
#### When Safe Skills Collide: Measuring Compositional Risk in Agent Skill Ecosystems

问题与机制：We study a core safety problem in agentic AI systems: whether individually safe skills can compose into unsafe installed skill sets. Owner=`AGENT-PLATFORM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `When Safe Skills Collide: Measuring Compositional Risk in Agent Skill Ecosystems` exact-v1 在 §Static-Composition Benchmark (deterministic).; §Static Analysis.; §IV-E Pairwise Compositional Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§III The SkillReact Measurement Framework; §IV Methodology`；Evaluation=`§Static-Composition Benchmark (deterministic).; §Static Analysis.; §IV-E Pairwise Compositional Analysis`。

Trade-off / failure / fallback：§IX Limitations and Threats to Validity; §XI Conclusion 该来源没有证明 `When Safe Skills Collide: Measuring Compositional Risk in Agent Skill Ecosystems` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00448:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00448:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：pairwise compositional risk is already owned by typed skill relations, permission closure and joint-evaluation admission in Ch84; the registry study quantifies a slice but does not add another authority boundary；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2606-00448:end -->

<!-- review:SF-2026-ARXIV-2606-00457:start -->
#### Maximizing Compute Capacity in AI Data Centers through Cooling, Energy Storage, and Computing Adaptation

问题与机制：We also present a problem formulation for ComputeAmp and highlight a few algorithmic and operational challenges. Owner=`PLATFORM-COST`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Maximizing Compute Capacity in AI Data Centers through Cooling, Energy Storage, and Computing Adaptation` exact-v1 在 §2.3 Illustrative Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§2.2.1 Cooling and water model; §2.2.2 BESS model; §2.2.3 Workload model`；Evaluation=`§2.3 Illustrative Results`。

Trade-off / failure / fallback：§3 Conclusion 该来源没有证明 `Maximizing Compute Capacity in AI Data Centers through Cooling, Energy Storage, and Computing Adaptation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-00457:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-00457:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：joint cooling, storage and compute adaptation is already covered by facility power, cooling, feasible placement and stranded-capacity accounting; the paper offers a formulation/illustration rather than a new validated control contract；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2606-00457:end -->

<!-- review:SF-2026-ARXIV-2606-07595:start -->
#### VisualLeakBench: Reproducible Action-Boundary Propagation Failures in Vision-Language Agents

问题与机制：We study a concrete failure mode in this setting: action-boundary propagation, where sensitive or unsafe visible text is copied from an image into downstream tool arguments. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `VisualLeakBench: Reproducible Action-Boundary Propagation Failures in Vision-Language Agents` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§Introduction / disclosed mechanism body; excerpt=-common diagnostic control, not a comparison across defense methods. Its PII gains mostly come from safety-first suppression and should not be interpreted as a utility-preserving repair. • The email residual and rendered unsafe-text group asymmetries are diagnostic findings in this subset, not complete taxonomies of which PII or harm categories are intrinsically harder. • Per-trace logs allow full table reproduction, but regenerating lo`；Evaluation=`§3 Evaluation Setting; excerpt=ibutions. 2 Failure Definition Why tool arguments matter. 3 Evaluation Setting Visual triggers. Models. Agent workflows. Metrics. Mitigation and guard diagnostic. Reproducibility artifact. 4 Tool Propagation Results Mitigation is asymmetric. Scenario effects. Visual-family effects. Web-research tool surface. 5 Trace Diagnostics 6 Mitigations and Residual Failures Residual rendered unsafe-text groups. Oracle boundary diagnostic. 7 Relate`。

Trade-off / failure / fallback：§VisualLeakBench : Reproducible Action-Boundary Propagation Failures in Vision-Language Agents; excerpt=VisualLeakBench: Reproducible Action-Boundary Propagation Failures in Vision-Language Agents Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction Contributions. 2 Failure Definition Why tool arguments matter. 3 Evaluat 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-07595:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-07595:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：visible text propagating into tool arguments is already covered by prompt-to-tool causal telemetry, canonical action and effect-time authorization; the benchmark localizes failure but does not transfer commit authority；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2606-07595:end -->

<!-- review:SF-2026-ARXIV-2606-07603:start -->
#### MetaEvo: A Meta-Optimization Framework for Experience-Driven Agent Evolution

问题与机制：To address this issue, we propose MetaEvo, a two-stage framework for continual agent evolution that focuses on improving how the model learns from tasks experience, rather than solely on what it stores. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `MetaEvo: A Meta-Optimization Framework for Experience-Driven Agent Evolution` exact-v1 在 §4 Experiments; §4.1 Experimental Setup; §5 Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology; §3.1 Framework Pipeline`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §5 Analysis`。

Trade-off / failure / fallback：§6 Conclusion 该来源没有证明 `MetaEvo: A Meta-Optimization Framework for Experience-Driven Agent Evolution` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-07603:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-07603:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-07603:end -->

<!-- review:SF-2026-ARXIV-2606-07616:start -->
#### Item Response Scaling Laws: A Measurement Theory Approach for Efficient and Generalizable Neural Scaling Estimation

问题与机制：To address this, we introduce Item Response Scaling Laws (IRSL), a unified framework that integrates Item Response Theory (IRT) within the scaling law framework. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Item Response Scaling Laws: A Measurement Theory Approach for Efficient and Generalizable Neural Scaling Estimation` exact-v1 在 §Efficient LM Evaluation; §4 Experiments; §Appendix B Additional Results for Pre-training Downstream IRSL 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Method`；Evaluation=`§Efficient LM Evaluation; §4 Experiments; §Appendix B Additional Results for Pre-training Downstream IRSL`。

Trade-off / failure / fallback：§5 Limitations, Discussions, and Future Work 该来源没有证明 `Item Response Scaling Laws: A Measurement Theory Approach for Efficient and Generalizable Neural Scaling Estimation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-07616:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-07616:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-07616:end -->

<!-- review:SF-2026-ARXIV-2606-20631:start -->
#### Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents

问题与机制：Agent skills externalise reusable agent-facing behavioural knowledge and guidance as persistent artefacts that can be discovered, activated, and interpreted by LLM agents. Owner=`AGENT-PLATFORM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents` exact-v1 在 §6 Evaluation; §6.1 Evaluation Design; §6.2 Cross-Instantiation Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology; §3.2 Reference Architecture Construction; §5 Reference Architecture for Skill Harnessing`；Evaluation=`§6 Evaluation; §6.1 Evaluation Design; §6.2 Cross-Instantiation Results`。

Trade-off / failure / fallback：§7 Discussion; §8 Threats to Validity; §10 Conclusion 该来源没有证明 `Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-20631:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-20631:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2606-20631:end -->

<!-- review:SF-2026-ARXIV-2606-24893:start -->
#### AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents

问题与机制：To evaluate these key abilities of test-time continual learning agents, we introduce AgentOdyssey, a novel evaluation framework that procedurally generates open-ended text games with rich entities, world dynamics, and long-horizon tasks. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§3.1 Formulation; excerpt=these key abilities of test-time continual learning agents, we introduce AgentOdyssey , a novel evaluation framework that procedurally generates open-ended text games with rich entities, world dynamics, and long-horizon tasks. Critically, AgentOdyssey goes beyond the conventional machine learning assumption that learning does not occur at test time by placing agents in a continuous, long-horizon setting that interleaves learning and inf`；Evaluation=`§3.4 Evaluation Metrics; excerpt=3.2 Ontology 3.3 Game Generation with Program Synthesis 3.4 Evaluation Metrics 4 Agent Paradigms 5 Experiment 1 - Diagnosing Five Key Abilities of Agents 5.1 Game Description 5.2 Analysis and Discussion 6 Experiment 2 - Effect of Agent Mechanisms on Test-Time Training 6.1 Game Description 6.2 Analysis and Discussion 7 Conclusion References 8 More Results for Experiment 1 and Experiment 2 9 Environment Design and Implementation Details 9`。

Trade-off / failure / fallback：§5.2 Analysis and Discussion; excerpt=y Abilities of Agents 5.1 Game Description 5.2 Analysis and Discussion 6 Experiment 2 - Effect of Agent Mechanisms on Test-Time Training 6.1 Game Description 6.2 Analysis and Discussion 7 Conclusion References 8 More Results for Experiment 1 and Experiment 2 9 Environment Design and Implementation Details 9.1 Tasks Main Quest. Side Quest. 9.2 Game Generation Entity Generation. Rule Generation. Quest Generation. 9.3 Additional Features T 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-24893:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-24893:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：procedurally generated long-horizon games instantiate the existing living-world/feedback-conditioned evaluation contract; generated worlds and test-time learning results remain benchmark evidence, not a new evaluation owner；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2606-24893:end -->

<!-- review:SF-2026-ARXIV-2606-28337:start -->
#### A Systems-Level Analysis of Sensitivity, Robustness, and Stability in Retrieval-Augmented Generation

问题与机制：This paper presents a controlled empirical study of RAG sensitivity, robustness, and stability across 56 experimental runs. Owner=`AGENT-RAG`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `A Systems-Level Analysis of Sensitivity, Robustness, and Stability in Retrieval-Augmented Generation` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§A Systems-Level Analysis of Sensitivity, Robustness, and Stability in Retrieval-Augmented Generation; excerpt=pagation 2.6 Stability and Variance in Generation Systems 3 Methodology and Evaluation Framework 3.1 Pipeline Overview 3.2 Dataset and Corpus 3.3 Chunking and Filtering 3.4 Embedding and Indexing 3.5 Retrieval and Reranking 3.6 Packing 3.7 Generation 3.8 Metrics 3.9 Experimental Environment 4 Experimental Design 4.1 Sensitivity Experiments 4.2 Robustness Experiments 4.3 Stability Experiments 5 Results 5.1 Preprocessing Answer Survival 5`；Evaluation=`§A Systems-Level Analysis of Sensitivity, Robustness, and Stability in Retrieval-Augmented Generation; excerpt=bility and Variance in Generation Systems 3 Methodology and Evaluation Framework 3.1 Pipeline Overview 3.2 Dataset and Corpus 3.3 Chunking and Filtering 3.4 Embedding and Indexing 3.5 Retrieval and Reranking 3.6 Packing 3.7 Generation 3.8 Metrics 3.9 Experimental Environment 4 Experimental Design 4.1 Sensitivity Experiments 4.2 Robustness Experiments 4.3 Stability Experiments 5 Results 5.1 Preprocessing Answer Survival 5.2 Sensitivity t`。

Trade-off / failure / fallback：§2.5 Context Utilization and Failure Propagation; excerpt=2.4 Robustness and Noise in RAG 2.5 Context Utilization and Failure Propagation 2.6 Stability and Variance in Generation Systems 3 Methodology and Evaluation Framework 3.1 Pipeline Overview 3.2 Dataset and Corpus 3.3 Chunking and Filtering 3.4 Embedding and Indexing 3.5 Retrieval and Reranking 3.6 Packing 3.7 Generation 3.8 Metrics 3.9 Experimental Environment 4 Experimental Design 4.1 Sensitivity Experiments 4.2 Robustness Experiments  该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2606-28337:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2606-28337:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：sensitivity, robustness, stability and stage-wise failure analysis are already part of RAG's corpus/retrieval/packing/reader evaluation contract; 56 runs do not add a new mechanism；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2606-28337:end -->

<!-- review:SF-2026-ARXIV-2605-30711:start -->
#### SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs

问题与机制：We frame memory evolution as a novelty-detection problem and propose SAGE, a Spherical Adaptive Gate for memory Evolution that scores candidate facts with a von Mises-Fisher-based density estimator over memory embeddings and routes them with an adaptive threshold that tracks memory-store geometry. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs` exact-v1 在 §4 Experiments; §Experimental Setting.; §4.1 Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology`；Evaluation=`§4 Experiments; §Experimental Setting.; §4.1 Results`。

Trade-off / failure / fallback：§5 Conclusion; §Limitations 该来源没有证明 `SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30711:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30711:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30711:end -->

<!-- review:SF-2026-ARXIV-2605-30712:start -->
#### ExpGraph: Model-Agnostic Experience Learning with Graph-Structured Memory for LLM Agents

问题与机制：We propose ExpGraph, a model-agnostic experience learning framework that enables frozen and replaceable LLM executors to improve through external experience reuse without parameter updates. Owner=`AGENT-RAG`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `ExpGraph: Model-Agnostic Experience Learning with Graph-Structured Memory for LLM Agents` exact-v1 在 §4 Experiments; §Training and evaluation.; §Appendix G Experimental Result Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§4.1 ExpGraph Outperforms General Prompt-based Baselines and Experience Learning Methods; §Retrieval-centric methods.; §G.1 ExpGraph Outperforms General Prompt-based Baselines and Experience Learning Methods`；Evaluation=`§4 Experiments; §Training and evaluation.; §Appendix G Experimental Result Analysis`。

Trade-off / failure / fallback：§6 Conclusion; §Appendix A Limitations, Future Work, and Broader Impact; §Limitations. 该来源没有证明 `ExpGraph: Model-Agnostic Experience Learning with Graph-Structured Memory for LLM Agents` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30712:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30712:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30712:end -->

<!-- review:SF-2026-ARXIV-2605-30723:start -->
#### Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents

问题与机制：However, our controlled experiments across multiple model scales show that skill effectiveness is strongly model-dependent: a skill that benefits one backbone can harm another. Owner=`AGENT-PLATFORM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents` exact-v1 在 §4 Experiments; §4.1 Experimental Setup; §4.2 Skill Evolution Evaluation 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Method: MASA`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Skill Evolution Evaluation`。

Trade-off / failure / fallback：§5 Conclusion; §Limitations 该来源没有证明 `Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30723:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30723:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30723:end -->

<!-- review:SF-2026-ARXIV-2605-30727:start -->
#### MosaicLeaks:Privacy Risks in Querying-in-the-Open for Deep Research Agents

问题与机制：We introduce MosaicLeaks, a benchmark of 1,001 multi-hop deep research tasks that chain private enterprise documents and a public web corpus, forcing agents to make external queries that depend on local information. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `MosaicLeaks:Privacy Risks in Querying-in-the-Open for Deep Research Agents` exact-v1 在 §Deep Research benchmarks.; §6 Evaluation Results; §Appendix C Further Evaluation Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§Deep Research benchmarks.; §6 Evaluation Results; §Appendix C Further Evaluation Analysis`。

Trade-off / failure / fallback：§7 Conclusion; §8 Limitations 该来源没有证明 `MosaicLeaks:Privacy Risks in Querying-in-the-Open for Deep Research Agents` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30727:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30727:end -->

Books Decision=`Integrate`；fresh-context challenge：deep-research agents can exfiltrate private local evidence through public search-query formulation before final-answer filtering; query planning therefore needs a privacy/egress gate, provenance and fail-closed fallback；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30727:end -->

<!-- review:SF-2026-ARXIV-2605-30728:start -->
#### Reducing the GPU Memory Bottleneck with Lossless Compression for ML -- Extended

问题与机制：We identify where lossless compression can be integrated into ML pipelines while minimizing interference with GPU execution. Owner=`INFER-TENSORRT-LLM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Reducing the GPU Memory Bottleneck with Lossless Compression for ML -- Extended` exact-v1 在 §6. Evaluation; §A.2.4. Benchmarks; §A.4. Evaluation workflow 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1. Introduction`；Evaluation=`§6. Evaluation; §A.2.4. Benchmarks; §A.4. Evaluation workflow`。

Trade-off / failure / fallback：§8. Conclusion 该来源没有证明 `Reducing the GPU Memory Bottleneck with Lossless Compression for ML -- Extended` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30728:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30728:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30728:end -->

<!-- review:SF-2026-ARXIV-2605-30736:start -->
#### OrcaRouter: A Production-Oriented LLM Router with Hybrid Offline-Online Learning

问题与机制：We present OrcaRouter, a production-oriented LLM router that combines a LinUCB-based contextual bandit over lexical and sentence-embedding features with a hybrid offline-online learning protocol. Owner=`INFER-SCHEDULING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `OrcaRouter: A Production-Oriented LLM Router with Hybrid Offline-Online Learning` exact-v1 在 §3 Experiments; §3.1 RouterArena Results; §3.2 Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§2 Methodology`；Evaluation=`§3 Experiments; §3.1 RouterArena Results; §3.2 Analysis`。

Trade-off / failure / fallback：§4 Conclusion 该来源没有证明 `OrcaRouter: A Production-Oriented LLM Router with Hybrid Offline-Online Learning` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30736:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30736:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30736:end -->

<!-- review:SF-2026-ARXIV-2605-30738:start -->
#### MAVEN: Improving Generalization in Agentic Tool Calling

问题与机制：We present MAVEN (Modular Agentic Verification and Execution Network), a lightweight symbolic reasoning scaffold for structured decomposition, adaptive tool orchestration, and intermediate verification. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `MAVEN: Improving Generalization in Agentic Tool Calling` exact-v1 在 §4 Benchmark; §4.5 Evaluation Protocol and Metrics; §5 Evaluation 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology`；Evaluation=`§4 Benchmark; §4.5 Evaluation Protocol and Metrics; §5 Evaluation`。

Trade-off / failure / fallback：§7 Discussion; §8 Conclusion 该来源没有证明 `MAVEN: Improving Generalization in Agentic Tool Calling` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30738:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30738:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30738:end -->

<!-- review:SF-2026-ARXIV-2605-30753:start -->
#### Efficient Diffusion LLMs via Temporal-Spatial Parallel Decoding and Confidence Extrapolation

问题与机制：We cast diffusion decoding as a dynamic control problem and show that token-wise denoising trajectories provide the key signal for reliable control. Owner=`MULTIMODAL-GENERATIVE-PARADIGMS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Efficient Diffusion LLMs via Temporal-Spatial Parallel Decoding and Confidence Extrapolation` exact-v1 在 §4 Experiments; §4.1 Experimental Settings; §4.2 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methods; §A.3 TSPD Controller: Architecture and Features`；Evaluation=`§4 Experiments; §4.1 Experimental Settings; §4.2 Main Results`。

Trade-off / failure / fallback：§5 Conclusion 该来源没有证明 `Efficient Diffusion LLMs via Temporal-Spatial Parallel Decoding and Confidence Extrapolation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30753:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30753:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30753:end -->

<!-- review:SF-2026-ARXIV-2605-30757:start -->
#### Chain-of-Thought and Compressed Looped Transformers: A Memory-Budget Separation

问题与机制：Chain-of-thought prompting and looped Transformers both give a fixed model more test-time computation, but they differ in what they remember. Owner=`AGENT-MEMORY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Chain-of-Thought and Compressed Looped Transformers: A Memory-Budget Separation` exact-v1 在 §Appendix F Experimental details and seed-level results; §Experimental setup. 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§Appendix F Experimental details and seed-level results; §Experimental setup.`。

Trade-off / failure / fallback：§6 Discussion and limitations; §Limitations and next steps. 该来源没有证明 `Chain-of-Thought and Compressed Looped Transformers: A Memory-Budget Separation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30757:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30757:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30757:end -->

<!-- review:SF-2026-ARXIV-2605-30771:start -->
#### Eywa: Provenance-Grounded Long-Term Memory for AI Agents

问题与机制：We present Eywa, a provenance-grounded memory architecture built around evidence before belief. Owner=`AGENT-MEMORY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Eywa: Provenance-Grounded Long-Term Memory for AI Agents` exact-v1 在 §Benchmarks and evaluation.; §5 Evaluation; §5.1 Benchmark Setup 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§Recent agent-memory architectures.; §4 System Architecture`；Evaluation=`§Benchmarks and evaluation.; §5 Evaluation; §5.1 Benchmark Setup`。

Trade-off / failure / fallback：§6 Discussion; §7 Threats to Validity; §8 Limitations 该来源没有证明 `Eywa: Provenance-Grounded Long-Term Memory for AI Agents` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30771:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30771:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30771:end -->

<!-- review:SF-2026-ARXIV-2605-30777:start -->
#### What Breaks When LLMs Code? Characterizing Operational Safety Failures of Agentic Code Assistants

问题与机制：We present an incident-driven empirical study grounded in two complementary evidence streams. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `What Breaks When LLMs Code? Characterizing Operational Safety Failures of Agentic Code Assistants` exact-v1 在 §5. Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§4. Methodology; §Agentic Frameworks`；Evaluation=`§5. Results`。

Trade-off / failure / fallback：§6. Discussion; §7. Threats to Validity; §9. Conclusion 该来源没有证明 `What Breaks When LLMs Code? Characterizing Operational Safety Failures of Agentic Code Assistants` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30777:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30777:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30777:end -->

<!-- review:SF-2026-ARXIV-2605-30785:start -->
#### Learning Agent-Compatible Context Management for Long-Horizon Tasks

问题与机制：We introduce Adaptive Context Management (AdaCoM), which trains an external LLM to manage the context of a frozen agent through flexible modification actions and end-to-end reinforcement learning. Owner=`AGENT-CONTEXT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Learning Agent-Compatible Context Management for Long-Horizon Tasks` exact-v1 在 §4 Experiments and Analysis; §4.1 Experimental Setup; §4.2 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§4 Experiments and Analysis; §4.1 Experimental Setup; §4.2 Main Results`。

Trade-off / failure / fallback：§6 Conclusion; §Limitations 该来源没有证明 `Learning Agent-Compatible Context Management for Long-Horizon Tasks` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30785:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30785:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30785:end -->

<!-- review:SF-2026-ARXIV-2605-30789:start -->
#### Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO

问题与机制：While GRPO relies on diverse rollouts, prevailing strategies primarily increase diversity by injecting more token-level randomness, which may introduce step-wise noise and lead to incoherent trajectories. Owner=`TRAIN-GRPO`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§3 Method; excerpt=mization (GRPO) 2.2 Distillation Introduces Perturbations 3 Method 3.1 Token-Level vs. Policy-Level Perturbations Token-level perturbations. Policy-level perturbations via parameter-level compression. Implications for gradient estimation in GRPO. Gradient interference under token-level perturbations. Structured gradients under policy-level perturbations. Takeaway. 3.2 S2L-PO: Small-to-Large Policy Optimization Mixed rollout generation. `；Evaluation=`§4 Experiment; excerpt=ion. Progressive annealing. Compatibility and efficiency. 4 Experiment 4.1 Experiment Settings 4.2 Main Results Small-to-large sampling improves both convergence speed and final performance. 4.3 Diversity Analysis Quantitative measurement of policy-level diversity. Controlled experiment on rollout diversity. 4.4 Ablation Study Pure small-model rollouts are not sufficient for sustained performance gains. Progressive transition vs. abrupt`。

Trade-off / failure / fallback：§6 Conclusion; excerpt=p E.2 Summary: Token-Level vs. Policy-Level Signal Growth F Limitations License: arXiv.org perpetual non-exclusive license arXiv:2605.30789v1 [cs.LG] 29 May 2026 Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO Yiming Ren Affiliation: Tsinghua University Affiliation: Shanghai AI Laboratory Yiran Xu Affiliation: Tsinghua University Zicheng Lin Affiliation: Tsinghua University Chufan Shi Affiliation: Tsinghua Univer 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30789:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30789:end -->

Books Decision=`Integrate`；fresh-context challenge：a smaller policy can own coherent trajectory proposals while the larger policy retains scoring/update authority; this changes rollout proposal identity and compute accounting, not the verifier or target-policy truth；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30789:end -->

<!-- review:SF-2026-ARXIV-2605-30790:start -->
#### On the impact of retrieved content representations in RAG Pipelines

问题与机制：We find that answer retention is the primary determinant of generator accuracy; notably, when retention is high, a representation's wording, structure, length, and query-dependence have limited effect. Owner=`AGENT-RAG`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `On the impact of retrieved content representations in RAG Pipelines` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§3.2.3 Reformulation Representations; excerpt=that structural information aids the generator. Compression methods Xu et al. (2023) ; Pan et al. (2024) ; Li et al. (2023) reduce retrieved content to lower inference cost, finding that generators tolerate substantial reductions with comparable or only slightly degraded accuracy. Finally, rewriting methods learn to transform retrieved content for downstream generator utility rather than for retrieval relevance Kim et al. (2026) ; Li et`；Evaluation=`§3 Experimental Setup; excerpt=tract Download PDF Abstract 1 Introduction 2 Related Work 3 Experimental Setup 3.1 Dataset and Retrieval 3.2 Document Representations 3.2.1 Selection Representations 3.2.2 Summarisation Representations 3.2.3 Reformulation Representations 3.2.4 Implementation details for LLM-based transformations. 3.2.5 Representation Statistics 3.3 Answer Generation 3.4 Evaluation 4 Results 4.1 RQ-1 4.2 RQ-2 4.2.1 Answer Accuracy 4.2.2 Query-time Latenc`。

Trade-off / failure / fallback：§5 Discussion; excerpt=ntier 4.2.4 Reducing Snippet-abstractive Latency 4.3 RQ-3 5 Discussion 5.1 Answer retention as the dominant factor 5.2 Reinterpreting prior work through retention 5.3 Source effects: human-vs-LLM and family preference 5.4 Why query-dependence underdelivers 5.5 Relation to prompt-sensitivity findings 6 Conclusion 7 Limitations 7.1 Representational dimensions and retention are not independently varied 7.2 Representational dimensions are n 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30790:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30790:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：the representation-format ablation reinforces existing evidence-retention and sufficient-context rules; its tested wording/structure/length variants do not define a new retrieval or reader state；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2605-30790:end -->

<!-- review:SF-2026-ARXIV-2605-30803:start -->
#### PReMISE: Policy Rubrics as Measurement Specifications for LLM Judges

问题与机制：We introduce PReMISE, a framework that, given pairwise human-preference data, (i) discovers a policy-level rubric set, and (ii) audits any rubric set under LLM-judge use along four axes: structural adequacy, reliability, preference fit, and adversarial robustness. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `PReMISE: Policy Rubrics as Measurement Specifications for LLM Judges` exact-v1 在 §2.1 Rubrics in LLM evaluation and training; §4 Experiments; §B.3.2 Full Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§2.1 Rubrics in LLM evaluation and training; §4 Experiments; §B.3.2 Full Results`。

Trade-off / failure / fallback：§5 Conclusion; §Limitations 该来源没有证明 `PReMISE: Policy Rubrics as Measurement Specifications for LLM Judges` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30803:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30803:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30803:end -->

<!-- review:SF-2026-ARXIV-2605-30807:start -->
#### Conformal Reliability: A New Evaluation Metric for Conditional Generation

问题与机制：In this paper, we propose a novel evaluation metric called reliability score based on conformal prediction, which measures the worst-case performance within the prediction set at a pre-specified confidence level. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Conformal Reliability: A New Evaluation Metric for Conditional Generation` exact-v1 在 §4 Experiments; §4.1 Experiments on Synthetic Datasets; §4.2 Experiments on Image-to-Text Task 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology; §A.2 Stable Diffusion Model; §C.2 Choice of Latent Generative Model`；Evaluation=`§4 Experiments; §4.1 Experiments on Synthetic Datasets; §4.2 Experiments on Image-to-Text Task`。

Trade-off / failure / fallback：§5 Conclusion and Future Works 该来源没有证明 `Conformal Reliability: A New Evaluation Metric for Conditional Generation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30807:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30807:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30807:end -->

<!-- review:SF-2026-ARXIV-2605-30824:start -->
#### Planner-Centric Reinforcement Learning for Deep Research with Structure-Aware Reward

问题与机制：We propose DecomposeR, a planner-centric deep research framework that represents research plans as typed directed acyclic graphs (DAGs), allowing planning to be made explicit, structured, and rewardable. Owner=`AGENT-WORKFLOW`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Planner-Centric Reinforcement Learning for Deep Research with Structure-Aware Reward` exact-v1 在 §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Main Results`。

Trade-off / failure / fallback：§5 Conclusion; §6 Limitations 该来源没有证明 `Planner-Centric Reinforcement Learning for Deep Research with Structure-Aware Reward` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30824:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30824:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30824:end -->

<!-- review:SF-2026-ARXIV-2605-30832:start -->
#### SLAT: Segment-Level Adaptive Trimming for Efficient CoT Reasoning

问题与机制：To address this, we demonstrate that inefficiency concentrates in high-probability segments with low marginal utility. Owner=`INFER-SCHEDULING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `SLAT: Segment-Level Adaptive Trimming for Efficient CoT Reasoning` exact-v1 在 §4 Experiment; §Evaluation; §4.2 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Method; §4.3.1 Extension to larger model`；Evaluation=`§4 Experiment; §Evaluation; §4.2 Main Results`。

Trade-off / failure / fallback：§6 Conclusion and Future Work; §Appendix B Discussion 该来源没有证明 `SLAT: Segment-Level Adaptive Trimming for Efficient CoT Reasoning` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30832:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30832:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30832:end -->

<!-- review:SF-2026-ARXIV-2605-30833:start -->
#### Your Teacher Can't Help You Here: Combating Supervision Fidelity Decay in On-Policy Distillation

问题与机制：However, we identify a critical bottleneck, \textbf{Supervision Fidelity Decay (SFD)}: as student-generated prefixes lengthen, the teacher's next-token distribution becomes less confident and less discriminative. Owner=`TRAIN-RLHF`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Your Teacher Can't Help You Here: Combating Supervision Fidelity Decay in On-Policy Distillation` exact-v1 在 §2.3 Theoretical Analysis: Signal Collapse and Compounding Drift; §4 Experiments; §4.1 Experimental Setup 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§2.3 Theoretical Analysis: Signal Collapse and Compounding Drift; §4 Experiments; §4.1 Experimental Setup`。

Trade-off / failure / fallback：§6 Conclusion 该来源没有证明 `Your Teacher Can't Help You Here: Combating Supervision Fidelity Decay in On-Policy Distillation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30833:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30833:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30833:end -->

<!-- review:SF-2026-ARXIV-2605-30834:start -->
#### Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring

问题与机制：In this paper, we propose \textbf{Hide-and-Seek}, a framework that formulates VLA failure detection as a coarsely supervised learning problem. Owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring` exact-v1 在 §5 Experiments; §Benchmarks and models.; §Evaluation metrics. 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§Detector architecture.; §D.3 Detector Architecture; §G.1 Out-of-Distribution Detection-based Methods`；Evaluation=`§5 Experiments; §Benchmarks and models.; §Evaluation metrics.`。

Trade-off / failure / fallback：§6 Conclusion; §Appendix I Limitations and Future Work 该来源没有证明 `Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30834:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30834:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：trajectory-derived VLA failure signals, calibration limits and safety-monitor ownership are already explicit in Ch26; the paper adds an evaluation slice, not a new controller；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2605-30834:end -->

<!-- review:SF-2026-ARXIV-2605-30837:start -->
#### Send a SCOUT First: Pre-hoc Reasoning for Adaptive Detector Allocation in Prompt-Injection Defense

问题与机制：Prompt-injection detectors are heterogeneous: each is strong on a different slice of attacks, and none is always reliable. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Send a SCOUT First: Pre-hoc Reasoning for Adaptive Detector Allocation in Prompt-Injection Defense` exact-v1 在 §Prompt-injection attacks and benchmarks.; §Safety–utility evaluation axes.; §7 Experiments 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§Prompt-injection attacks and benchmarks.; §Safety–utility evaluation axes.; §7 Experiments`。

Trade-off / failure / fallback：§7.6 Latency and deployment discussion; §8 Conclusion; §Limitations 该来源没有证明 `Send a SCOUT First: Pre-hoc Reasoning for Adaptive Detector Allocation in Prompt-Injection Defense` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30837:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30837:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：pre-hoc detector allocation is already covered by risk-routed pre-guards, sensor calibration and deterministic effect-time authority; SCOUT remains a detector-routing implementation branch；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2605-30837:end -->

<!-- review:SF-2026-ARXIV-2605-30838:start -->
#### COMPASS: Cognitive MCTS-Guided Process Alignment for Safe Search Agents

问题与机制：However, these capabilities introduce retrieval-induced safety degradation, as harmful intents may decompose into seemingly innocuous sub-queries that lead to unsafe outcomes. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `COMPASS: Cognitive MCTS-Guided Process Alignment for Safe Search Agents` exact-v1 在 §4 Experiment; §4.1 Experimental Setup; §4.4 Further Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology`；Evaluation=`§4 Experiment; §4.1 Experimental Setup; §4.4 Further Analysis`。

Trade-off / failure / fallback：§5 Conclusion; §Limitations 该来源没有证明 `COMPASS: Cognitive MCTS-Guided Process Alignment for Safe Search Agents` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30838:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30838:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30838:end -->

<!-- review:SF-2026-ARXIV-2605-30842:start -->
#### CoMem: Context Management with A Decoupled Long-Context Model

问题与机制：In this paper, we introduce CoMem, a novel framework that decouples memory management from the primary agent workflow, enabling these processes to execute in parallel. Owner=`AGENT-CONTEXT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `CoMem: Context Management with A Decoupled Long-Context Model` exact-v1 在 §3.1 Analysis of Agent Inference; §4 Experimental Results; §4.1 Evaluation Dataset 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3.2 CoMem Framework; §Appendix A Prompt for Agent Model; §Appendix B Prompt for Memory Model`；Evaluation=`§3.1 Analysis of Agent Inference; §4 Experimental Results; §4.1 Evaluation Dataset`。

Trade-off / failure / fallback：§6 Discussion; §7 Conclusion 该来源没有证明 `CoMem: Context Management with A Decoupled Long-Context Model` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30842:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30842:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30842:end -->

<!-- review:SF-2026-ARXIV-2605-30851:start -->
#### How Much Parallelism Is "Free"? A Principle of Near-Free Parallelism for Parallel Decoding

问题与机制：Analyzing Dense FFNs, MoE FFNs, and Attention against an idle-compute baseline, we find that NFP is shaped not by memory-bound resource slack alone, but also by implementation-induced kernel-granularity slack. Owner=`INFER-TENSORRT-LLM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `How Much Parallelism Is "Free"? A Principle of Near-Free Parallelism for Parallel Decoding` exact-v1 在 §3 Module-Level Analysis of Near-Free Parallelism; §Appendix C Module-Level Analysis Implementation Details; §C.1.1 Experimental Goal and Scope 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§J.2.2 Parallel-Decoding-Aware Architecture Design`；Evaluation=`§3 Module-Level Analysis of Near-Free Parallelism; §Appendix C Module-Level Analysis Implementation Details; §C.1.1 Experimental Goal and Scope`。

Trade-off / failure / fallback：§8 Conclusion; §Limitations; §Appendix J Discussion and Implications 该来源没有证明 `How Much Parallelism Is "Free"? A Principle of Near-Free Parallelism for Parallel Decoding` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30851:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30851:end -->

Books Decision=`Integrate`；fresh-context challenge：parallel decoding should first exploit memory-bound/kernel-granularity slack whose extra work stays off the critical path; the execution runtime owns overlap and resource admission, while speculative correctness remains in Ch48；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30851:end -->

<!-- review:SF-2026-ARXIV-2605-30852:start -->
#### Speculative Pipeline Decoding: Higher-Accuracy Drafting with Hidden Latency via Pipeline Parallelism

问题与机制：We propose Speculative Pipeline Decoding (SPD), which partitions the target LLM into $n$ pipeline stages so that $n$ tokens of a single sequence advance in parallel. Owner=`INFER-SPECULATIVE-DECODING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Speculative Pipeline Decoding: Higher-Accuracy Drafting with Hidden Latency via Pipeline Parallelism` exact-v1 在 §4 Experiments; §4.1 Experimental Setup; §4.2 Evaluation Metrics: Acceptance Length and Theoretical Speedup 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology; §3.1 Pipeline Execution Framework`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Evaluation Metrics: Acceptance Length and Theoretical Speedup`。

Trade-off / failure / fallback：§5 Conclusion; §6 Limitations 该来源没有证明 `Speculative Pipeline Decoding: Higher-Accuracy Drafting with Hidden Latency via Pipeline Parallelism` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30852:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30852:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：pipeline-parallel drafting is a workload-specific realization of existing draft/verify critical-path accounting; theoretical speedup and acceptance length do not establish a separate commit contract；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2605-30852:end -->

<!-- review:SF-2026-ARXIV-2605-30854:start -->
#### Safe Equilibrium Policy Optimization for Strategic Agent Policies

问题与机制：We propose Safe Equilibrium Policy Optimization (\sepo{}), a training objective that augments expected payoff with explicit penalties for exploitability, collusion risk, and externality cost. Owner=`TRAIN-GRPO`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Safe Equilibrium Policy Optimization for Strategic Agent Policies` exact-v1 在 §4 Experimental Setup; §5 Results; §6 Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Method`；Evaluation=`§4 Experimental Setup; §5 Results; §6 Analysis`。

Trade-off / failure / fallback：§7 Conclusion; §8 Limitations 该来源没有证明 `Safe Equilibrium Policy Optimization for Strategic Agent Policies` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30854:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30854:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30854:end -->

<!-- review:SF-2026-ARXIV-2605-30855:start -->
#### Robust Dreamer: Deviation-Aware Latent Gaussian Memory for Action-Controlled AR Video Generation

问题与机制：To address these challenges, we present \textbf{Robust Dreamer}, a memory-augmented framework built around how to design 3D memory and how to use it robustly. Owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Robust Dreamer: Deviation-Aware Latent Gaussian Memory for Action-Controlled AR Video Generation` exact-v1 在 §4 Experiments; §4.1 Experimental Settings; §4.2 Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3.1 Memory-Conditioned Rollout Framework`；Evaluation=`§4 Experiments; §4.1 Experimental Settings; §4.2 Results`。

Trade-off / failure / fallback：§5 Conclusion; §Appendix F Limitation 该来源没有证明 `Robust Dreamer: Deviation-Aware Latent Gaussian Memory for Action-Controlled AR Video Generation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30855:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30855:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30855:end -->

<!-- review:SF-2026-ARXIV-2605-30859:start -->
#### DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning

问题与机制：To address this, we propose a novel paradigm of active distribution shaping to shape the rollout distribution towards conciseness and certainty, thereby fundamentally resolving tail-induced overheads. Owner=`TRAIN-RLHF`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning` exact-v1 在 §5 Experiments; §5.1 Implementation and Experimental Setups; §Appendix F Analysis on Response Length 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§4 Method`；Evaluation=`§5 Experiments; §5.1 Implementation and Experimental Setups; §Appendix F Analysis on Response Length`。

Trade-off / failure / fallback：§5.6 Discussion; §6 Conclusion; §The Limitation of Tail Batching. 该来源没有证明 `DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30859:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30859:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30859:end -->

<!-- review:SF-2026-ARXIV-2605-30880:start -->
#### PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments

问题与机制：We introduce PatchWorld, a gradient-free framework that turns offline trajectories into executable Python world models through counterexample-guided code repair.Instead of predicting the next observation with a black-box model, PatchWorld induces symbolic belief-state programs whose action updates can be inspected, replayed, and locally patched. Owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments` exact-v1 在 §5 Experiments; §Analysis.; §Appendix G Per-Environment Rollout Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§4 Methodology`；Evaluation=`§5 Experiments; §Analysis.; §Appendix G Per-Environment Rollout Results`。

Trade-off / failure / fallback：§6 Conclusion; §Limitations 该来源没有证明 `PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30880:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30880:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：executable transition programs, counterexample repair and planner-utility evaluation are already explicit; PatchWorld is bounded experimental evidence for that branch；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2605-30880:end -->

<!-- review:SF-2026-ARXIV-2605-30883:start -->
#### TRACE: Task-Aware Adaptive Self-Evolving Agentic Jailbreaking

问题与机制：In this paper, we propose TRACE, a practical agentic jailbreaking framework to further reveal the risks of this threat surface. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `TRACE: Task-Aware Adaptive Self-Evolving Agentic Jailbreaking` exact-v1 在 §5 Experiment; §5.1 Experiment Setup; §Evaluation Metrics. 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Threat Model`；Evaluation=`§5 Experiment; §5.1 Experiment Setup; §Evaluation Metrics.`。

Trade-off / failure / fallback：§7 Conclusion 该来源没有证明 `TRACE: Task-Aware Adaptive Self-Evolving Agentic Jailbreaking` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30883:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30883:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30883:end -->

<!-- review:SF-2026-ARXIV-2605-30888:start -->
#### The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement

问题与机制：Therefore, we propose SAVE (Self-supervised reward model improvement via Value-Anchored On-policy feedback), a framework that grades on-policy responses as feedback by using the value function for on-policy RM training. Owner=`TRAIN-RLHF`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement` exact-v1 在 §6 Experiments; §Reward Model Evaluation.; §Policy Model Evaluation. 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§5 Methodology`；Evaluation=`§6 Experiments; §Reward Model Evaluation.; §Policy Model Evaluation.`。

Trade-off / failure / fallback：§7 Conclusion; §Limitations 该来源没有证明 `The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30888:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30888:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30888:end -->

<!-- review:SF-2026-ARXIV-2605-30896:start -->
#### Zero Collapse: A Failure Mode of Policy Gradient Methods in Discontinuous Reward Environments

问题与机制：We identify a fundamental failure mode in this setting termed "zero collapse." We show that stochastic exploration and gradient-based updates can cause policies to overshoot optimal high-reward regions and enter flat, zero-reward regimes. Owner=`TRAIN-GRPO`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Zero Collapse: A Failure Mode of Policy Gradient Methods in Discontinuous Reward Environments` exact-v1 在 §7 Mitigation Results; §Appendix D Experimental Details 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§8 Why Actor-Critic Methods Struggle; §Appendix E Derby Framework`；Evaluation=`§7 Mitigation Results; §Appendix D Experimental Details`。

Trade-off / failure / fallback：§9 Discussion and Future Work; §10 Conclusion 该来源没有证明 `Zero Collapse: A Failure Mode of Policy Gradient Methods in Discontinuous Reward Environments` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30896:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30896:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30896:end -->

<!-- review:SF-2026-ARXIV-2605-30898:start -->
#### UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling

问题与机制：However, this decoupled design introduces inherent limitations. Owner=`INFER-SCHEDULING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling` exact-v1 在 §4 Empirical Evaluation; §Appendix B Additional Main Experimental Details and Results; §B.4 Detailed Results on Main Experiment 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 The UniScale Framework; §D.3 Unified Inference Scaling Cost Model`；Evaluation=`§4 Empirical Evaluation; §Appendix B Additional Main Experimental Details and Results; §B.4 Detailed Results on Main Experiment`。

Trade-off / failure / fallback：§6 Related Work and Discussion; §7 Conclusion 该来源没有证明 `UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30898:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30898:end -->

Books Decision=`Integrate`；fresh-context challenge：model routing and test-time scaling consume one shared quality/latency/cost budget and should be jointly optimized online; the scheduler owns the joint action and rollback to fixed routing/budget policies；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30898:end -->

<!-- review:SF-2026-ARXIV-2605-30911:start -->
#### What Makes LVLMs Hallucinate Less? Unveiling the Architectural Factors Behind Hallucination Robustness

问题与机制：To investigate this, we factor the architecture design into three dimensions: Linguistic Foundation (LF), Visual Representation (VR), and Semantic Alignment (SA), and categorize hallucinations into Co-occurrence, Similarity, and previously overlooked Uncertainty types. Owner=`MULTIMODAL-REPRESENTATION`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `What Makes LVLMs Hallucinate Less? Unveiling the Architectural Factors Behind Hallucination Robustness` exact-v1 在 §II-C Evaluating Benchmarks for Hallucination; §IV Evaluation Protocol; §IV-B Certainty Evaluation Metrics 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§IV-C 1 Uncertainty Scoring Method`；Evaluation=`§II-C Evaluating Benchmarks for Hallucination; §IV Evaluation Protocol; §IV-B Certainty Evaluation Metrics`。

Trade-off / failure / fallback：§VI Conclusion 该来源没有证明 `What Makes LVLMs Hallucinate Less? Unveiling the Architectural Factors Behind Hallucination Robustness` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30911:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30911:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30911:end -->

<!-- review:SF-2026-ARXIV-2605-30917:start -->
#### Inference-Free Multimodal Learned Sparse Retrieval for Production-Scale Visual Document Search

问题与机制：To fill this missing serving regime, we present V-SPLADE, an inference-free sparse retriever for visual-document retrieval. Owner=`AGENT-RAG`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Inference-Free Multimodal Learned Sparse Retrieval for Production-Scale Visual Document Search` exact-v1 在 §5. Experiments; §Evaluation.; §5.3. Benchmark Retrieval Quality 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§4. Method`；Evaluation=`§5. Experiments; §Evaluation.; §5.3. Benchmark Retrieval Quality`。

Trade-off / failure / fallback：§6. Conclusion; §Limitations and Future Work. 该来源没有证明 `Inference-Free Multimodal Learned Sparse Retrieval for Production-Scale Visual Document Search` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30917:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30917:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30917:end -->

<!-- review:SF-2026-ARXIV-2605-30924:start -->
#### EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents

问题与机制：However, existing approaches lack explicit mechanisms for identifying hazards and reasoning about action-conditioned risks, leading agents to either miss risky interactions or over-identify risks. Owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents` exact-v1 在 §3.2 Constructing Training and Evaluation Dataset; §4.1 Experimental Setup; §4.2 Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§C.2 Details of Evaluation Framework; §C.2.3 Guardrail Evaluation Method`；Evaluation=`§3.2 Constructing Training and Evaluation Dataset; §4.1 Experimental Setup; §4.2 Results`。

Trade-off / failure / fallback：§5.3 Discussion; §6 Conclusion; §Limitations 该来源没有证明 `EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30924:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30924:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30924:end -->

<!-- review:SF-2026-ARXIV-2605-30998:start -->
#### Free-Riding the Agentic Web: A Systematic Security Analysis of x402 Payments

问题与机制：We identify four flaw classes: cross-resource substitution, duplicate-settlement race (independently corroborated by subsequent third-party reports), allowance overdraft, and denial of settlement. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Free-Riding the Agentic Web: A Systematic Security Analysis of x402 Payments` exact-v1 在 §4 Vulnerability Analysis; §5.4.1 Experimental Setup 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§Architecture.; §3 System Model; §3.3 Threat Model`；Evaluation=`§4 Vulnerability Analysis; §5.4.1 Experimental Setup`。

Trade-off / failure / fallback：§7 Conclusion 该来源没有证明 `Free-Riding the Agentic Web: A Systematic Security Analysis of x402 Payments` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-30998:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-30998:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-30998:end -->

<!-- review:SF-2026-ARXIV-2605-31033:start -->
#### SlotMemory: Object-Centric KV Memory for Streaming Long-Video Generation

问题与机制：To address these limitations, we propose SlotMemory, an object-centric Key-Value memory mechanism for streaming video diffusion. Owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `SlotMemory: Object-Centric KV Memory for Streaming Long-Video Generation` exact-v1 在 §4. Experiments; §4.1. Experiment Setups; §4.2. Main Experiments 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3. Method; §3.1. Problem Setup and Streaming Framework`；Evaluation=`§4. Experiments; §4.1. Experiment Setups; §4.2. Main Experiments`。

Trade-off / failure / fallback：§4.4. Limitations and Future Work; §5. Conclusion 该来源没有证明 `SlotMemory: Object-Centric KV Memory for Streaming Long-Video Generation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31033:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31033:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31033:end -->

<!-- review:SF-2026-ARXIV-2605-31042:start -->
#### From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors

问题与机制：To reveal this threat, we introduce ClawTrojan, a benchmark designed to identify multi-step trojan attacks in local agentic harnesses. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors` exact-v1 在 §2.1 Benchmarks for Agent Security; §4 The ClawTrojan Benchmark; §4.4 Comparison with Existing Benchmarks 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3.1 Agent Harness Model`；Evaluation=`§2.1 Benchmarks for Agent Security; §4 The ClawTrojan Benchmark; §4.4 Comparison with Existing Benchmarks`。

Trade-off / failure / fallback：§7 Conclusion and Future Work; §Limitations 该来源没有证明 `From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31042:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31042:end -->

Books Decision=`Integrate`；fresh-context challenge：a harness backdoor can write persistent control state in one run and trigger harmful behavior later; security must bind write provenance, activation conditions, lifecycle scanning, revocation and rollback across runs；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31042:end -->

<!-- review:SF-2026-ARXIV-2605-31058:start -->
#### Combinatorial Synthesis: Scaling Code RLVR via Atomic Decomposition and Recombination

问题与机制：To this end, we propose Atomic Decomposition and Recombination (ADR), a novel framework that generates verifiable code tasks via decomposition into atomic elements and controlled recombination, thereby enabling the generation of genuinely novel and challenging verifiable code tasks. Owner=`TRAIN-DATA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Combinatorial Synthesis: Scaling Code RLVR via Atomic Decomposition and Recombination` exact-v1 在 §We establish a multi-dimensional evaluation taxonomy for verifiable synthetic data that; §Through extensive experiments on large-scale RLVR, we show the strong generalization; §Evaluation of Synthetic Data Quality 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§We propose the ADR framework, a novel paradigm that shifts from heuristic seed expansion; §Method; §Diversity: We obtain data representations using the all-MiniLM-L6-v2 embedding model`；Evaluation=`§We establish a multi-dimensional evaluation taxonomy for verifiable synthetic data that; §Through extensive experiments on large-scale RLVR, we show the strong generalization; §Evaluation of Synthetic Data Quality`。

Trade-off / failure / fallback：§Conclusion 该来源没有证明 `Combinatorial Synthesis: Scaling Code RLVR via Atomic Decomposition and Recombination` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31058:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31058:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31058:end -->

<!-- review:SF-2026-ARXIV-2605-31066:start -->
#### Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air

问题与机制：Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks. Owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air` exact-v1 在 §2.1 Air-Ground Evaluation Infrastructure; §4 Diagnostic Evaluation; §4.3 Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§2.2 Methods for Air-Ground Cooperation; §3.1 Causally Consistent Runtime Architecture`；Evaluation=`§2.1 Air-Ground Evaluation Infrastructure; §4 Diagnostic Evaluation; §4.3 Results`。

Trade-off / failure / fallback：§5 Discussion and Conclusion 该来源没有证明 `Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31066:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31066:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31066:end -->

<!-- review:SF-2026-ARXIV-2605-31073:start -->
#### ConsisGuard: Aligning Safety Deliberation with Policy Enforcement in LLM Guardrails

问题与机制：We identify this safety-critical failure mode as the deliberation-to-enforcement gap. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `ConsisGuard: Aligning Safety Deliberation with Policy Enforcement in LLM Guardrails` exact-v1 在 §4 Experiment; §Benchmarks and Evaluation Metrics.; §4.1 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology`；Evaluation=`§4 Experiment; §Benchmarks and Evaluation Metrics.; §4.1 Main Results`。

Trade-off / failure / fallback：§5 Conclusion; §Limitations 该来源没有证明 `ConsisGuard: Aligning Safety Deliberation with Policy Enforcement in LLM Guardrails` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31073:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31073:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31073:end -->

<!-- review:SF-2026-ARXIV-2605-31086:start -->
#### Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory

问题与机制：To address these limitations, we introduce RHELM (Realistic, Heterogeneous, and Evolving Long-term Memory). Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory` exact-v1 在 §4 Benchmark Curation; §6 Experiments; §6.1 Experimental Setup 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§4 Benchmark Curation; §6 Experiments; §6.1 Experimental Setup`。

Trade-off / failure / fallback：§7 Conclusion; §Limitations 该来源没有证明 `Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31086:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31086:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31086:end -->

<!-- review:SF-2026-ARXIV-2605-31105:start -->
#### GRKV: Global Regression for Training-Free KV Cache Compression in Long-Context LLMs

问题与机制：To address this imbalance, we propose GRKV (Global Regression for KV Cache), a training-free KV-cache merging method that directly minimizes the discrepancy between compressed-cache and full-cache attention outputs. Owner=`INFER-KV-CACHE`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `GRKV: Global Regression for Training-Free KV Cache Compression in Long-Context LLMs` exact-v1 在 §4 Experiments; §4.1 Experimental Settings; §4.2 Experimental Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methods`；Evaluation=`§4 Experiments; §4.1 Experimental Settings; §4.2 Experimental Results`。

Trade-off / failure / fallback：§5 Conclusion; §Limitations 该来源没有证明 `GRKV: Global Regression for Training-Free KV Cache Compression in Long-Context LLMs` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31105:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31105:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31105:end -->

<!-- review:SF-2026-ARXIV-2605-31111:start -->
#### Subspace-Decomposed JEPAs: Disentangling Progression and Content in Latent World Models

问题与机制：Joint-Embedding Predictive Architectures (JEPAs) learn compact latent world models by predicting future embeddings, but no single coordinate of the latent is designated to encode task progression. Owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Subspace-Decomposed JEPAs: Disentangling Progression and Content in Latent World Models` exact-v1 在 §4 Theoretical analysis; §5 Experiments; §5.2 Main results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Method: SD-JEPA`；Evaluation=`§4 Theoretical analysis; §5 Experiments; §5.2 Main results`。

Trade-off / failure / fallback：§5.6 Cross-environment summary and limitations; §Known limitations.; §7 Discussion 该来源没有证明 `Subspace-Decomposed JEPAs: Disentangling Progression and Content in Latent World Models` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31111:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31111:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31111:end -->

<!-- review:SF-2026-ARXIV-2605-31158:start -->
#### Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models

问题与机制：We present Light Interaction, a training-free inference acceleration framework for interactive video world models. Owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models` exact-v1 在 §4 Experiments; §4.1 Experimental Setup; §4.2 Overall Performance Evaluation 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Overall Performance Evaluation`。

Trade-off / failure / fallback：§5 Conclusion 该来源没有证明 `Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31158:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31158:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31158:end -->

<!-- review:SF-2026-ARXIV-2605-31159:start -->
#### Trust-Region Behavior Blending for On-Policy Distillation

问题与机制：We propose Trust-Region behavior Blending (TRB), a warmup method that replaces the early rollout policy with the closest-to-teacher behavior policy inside a student-centered KL trust region, while keeping the per-prefix reverse-KL OPD loss unchanged. Owner=`TRAIN-RLHF`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Trust-Region Behavior Blending for On-Policy Distillation` exact-v1 在 §5 Experiments & Results; §5.1 Experimental Setup; §5.2 Benchmark Comparison 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§5 Experiments & Results; §5.1 Experimental Setup; §5.2 Benchmark Comparison`。

Trade-off / failure / fallback：§6 Discussion; §7 Limitations 该来源没有证明 `Trust-Region Behavior Blending for On-Policy Distillation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31159:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31159:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31159:end -->

<!-- review:SF-2026-ARXIV-2605-31164:start -->
#### D$^3$: Dynamic Directional Graph-Constrained Data Scheduling for LLM Training

问题与机制：In this work, we propose $D^3$, a Dynamic Directional graph-constrained Data scheduling framework. Owner=`TRAIN-DATA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `D$^3$: Dynamic Directional Graph-Constrained Data Scheduling for LLM Training` exact-v1 在 §Complexity analysis.; §4 Experiments; §4.1 Experimental Settings 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology; §Appendix C Formulations of Influence Estimation Methods; §First-Order Symmetric Method`；Evaluation=`§Complexity analysis.; §4 Experiments; §4.1 Experimental Settings`。

Trade-off / failure / fallback：§5 Conclusion; §Limitations 该来源没有证明 `D$^3$: Dynamic Directional Graph-Constrained Data Scheduling for LLM Training` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31164:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31164:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31164:end -->

<!-- review:SF-2026-ARXIV-2605-31167:start -->
#### LLM-FACETS: A Privacy-Preserving Framework for Evaluating LLM Transparency and Accountability

问题与机制：We introduce LLM-FACETS (LLM FActuality Cross-EvaluaTion System): an open-source framework with a browser-accessible interface and a plugin architecture, structured around three practitioner profiles (technical experts, domain experts, compliance officers) that mirror the stakeholder categories identified in the EU AI Act and the NIST AI Risk Management Framework. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `LLM-FACETS: A Privacy-Preserving Framework for Evaluating LLM Transparency and Accountability` exact-v1 在 §2.5.4. Baseline Grounding: Anchoring Evaluation in Deterministic References; §3.3. Evaluation Workflow; §4.5. Statistical Benchmark Analysis Dashboard [Process] 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3.2. Terminology and Framework Definition; §4.1. The BYOK Privacy Model; §4.4. Plugin Architecture: Adding Metrics, Providers, and Datasets`；Evaluation=`§2.5.4. Baseline Grounding: Anchoring Evaluation in Deterministic References; §3.3. Evaluation Workflow; §4.5. Statistical Benchmark Analysis Dashboard [Process]`。

Trade-off / failure / fallback：§8. Discussion; §8.4. Limitations; §9. Conclusion 该来源没有证明 `LLM-FACETS: A Privacy-Preserving Framework for Evaluating LLM Transparency and Accountability` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31167:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31167:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31167:end -->

<!-- review:SF-2026-ARXIV-2605-31170:start -->
#### Emergent Languages in Populations of Language Model Agents: From Token Efficiency to Oversight Evasion

问题与机制：Here, we study the emergent languages on Moltbook. Owner=`AGENT-MULTI-AGENT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Emergent Languages in Populations of Language Model Agents: From Token Efficiency to Oversight Evasion` exact-v1 在 §Results. 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§Introduction`；Evaluation=`§Results.`。

Trade-off / failure / fallback：§Discussion; §Limitations; §Conclusion 该来源没有证明 `Emergent Languages in Populations of Language Model Agents: From Token Efficiency to Oversight Evasion` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31170:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31170:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：emergent compact language and oversight evasion are already captured by the rule that continuous/latent channels are proposal channels and authoritative state remains typed and auditable; the paper is bounded evidence；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2605-31170:end -->

<!-- review:SF-2026-ARXIV-2605-31175:start -->
#### Towards Efficient LLMs Annealing with Principled Sample Selection

问题与机制：To this end, we propose DiReCT (Directionally-Restrained Constrained Training), a novel framework that reformulates sample selection in the annealing stage as a constrained optimization problem. Owner=`TRAIN-DATA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Towards Efficient LLMs Annealing with Principled Sample Selection` exact-v1 在 §4.5 Theoretical Analysis; §5 Experiments; §5.1 Experimental Setup 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§4 Methodology`；Evaluation=`§4.5 Theoretical Analysis; §5 Experiments; §5.1 Experimental Setup`。

Trade-off / failure / fallback：§6 Conclusion; §Limitations 该来源没有证明 `Towards Efficient LLMs Annealing with Principled Sample Selection` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31175:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31175:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31175:end -->

<!-- review:SF-2026-ARXIV-2605-31176:start -->
#### Retriever Portfolios: A Principled Approach to Adaptive RAG

问题与机制：We propose a method that automatically selects a small, diverse subset of retrievers (a portfolio) from a large pool of candidates, to cover different regions of the target query distribution. Owner=`AGENT-RAG`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Retriever Portfolios: A Principled Approach to Adaptive RAG` exact-v1 在 §4 Pipeline & Experimental Setup; §5 Results; §B.6 Efficient batched evaluation over retriever pools 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§Architecture.`；Evaluation=`§4 Pipeline & Experimental Setup; §5 Results; §B.6 Efficient batched evaluation over retriever pools`。

Trade-off / failure / fallback：§Instructions for reporting errors; no dedicated limitations heading; scope is bounded by the disclosed models, tasks and setup 该来源没有证明 `Retriever Portfolios: A Principled Approach to Adaptive RAG` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31176:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31176:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31176:end -->

<!-- review:SF-2026-ARXIV-2605-31244:start -->
#### Spectral Reach: Understanding Neural Scaling as Progress into the Spectral Tail

问题与机制：To close this gap, we introduce "spectral position": a scalable measure of which eigenvalues of the empirical neural tangent kernel (eNTK) currently drive loss reduction. Owner=`WORLDVIEW-SCALING-LAW`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Spectral Reach: Understanding Neural Scaling as Progress into the Spectral Tail` exact-v1 在 §Experimental setup.; §Results.; §Toward mode-level analysis of semantic structure. 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§Methods to enhance spectral reach.; §Comparison to Direct eNTK Methods.; §Student Architecture.`；Evaluation=`§Experimental setup.; §Results.; §Toward mode-level analysis of semantic structure.`。

Trade-off / failure / fallback：§6 Discussion; §Limitations. 该来源没有证明 `Spectral Reach: Understanding Neural Scaling as Progress into the Spectral Tail` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31244:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31244:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31244:end -->

<!-- review:SF-2026-ARXIV-2605-31264:start -->
#### COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation

问题与机制：We present an automated trace-to-skill distillation system for generating person-grounded AI skills via expert knowledge distillation. Owner=`AGENT-PLATFORM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation` exact-v1 在 §Instructions for reporting errors 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§Instructions for reporting errors`。

Trade-off / failure / fallback：§8 Discussion; §9 Limitations and Responsible Deployment; §10 Conclusion 该来源没有证明 `COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31264:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31264:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31264:end -->

<!-- review:SF-2026-ARXIV-2605-31278:start -->
#### Industrializing Prediction-Powered Inference: The GLIDE Library for Reliable GenAI and Agentic Systems Evaluation

问题与机制：We introduce GLIDE, an open-source Python library that unifies state-of-the-art PPI estimators (PPI++, Stratified PPI, Predict-Then-Debias and its stratified variants, Active Statistical Inference) and samplers (uniform, stratified, active, cost-optimal) under a scipy-style API specialized to mean estimation. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Industrializing Prediction-Powered Inference: The GLIDE Library for Reliable GenAI and Agentic Systems Evaluation` exact-v1 在 §3 Why Agentic Evaluation Needs PPI; §6 Case Study: Agentic Evaluation in Practice; §6.2 Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§4 The GLIDE Framework; §4.4 A decision framework`；Evaluation=`§3 Why Agentic Evaluation Needs PPI; §6 Case Study: Agentic Evaluation in Practice; §6.2 Results`。

Trade-off / failure / fallback：§6.3 Discussion; §8 Limitations and Roadmap; §Limitations. 该来源没有证明 `Industrializing Prediction-Powered Inference: The GLIDE Library for Reliable GenAI and Agentic Systems Evaluation` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31278:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31278:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31278:end -->

<!-- review:SF-2026-ARXIV-2605-31308:start -->
#### TraceGraph: Shared Decision Landscapes for Diagnosing and Improving Agent Trajectories

问题与机制：We introduce TraceGraph, a graph-based framework that turns released multi-model agent trajectories into shared decision landscapes. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `TraceGraph: Shared Decision Landscapes for Diagnosing and Improving Agent Trajectories` exact-v1 在 §Outcome-centered evaluation.; §4 Graph Analysis with TraceGraph; §4.4 What Process Demands Do Benchmarks Impose? 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§B.12 Agent Framework and Recovery Templates`；Evaluation=`§Outcome-centered evaluation.; §4 Graph Analysis with TraceGraph; §4.4 What Process Demands Do Benchmarks Impose?`。

Trade-off / failure / fallback：§6 Discussion and Conclusion; §7 Limitations 该来源没有证明 `TraceGraph: Shared Decision Landscapes for Diagnosing and Improving Agent Trajectories` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31308:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31308:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31308:end -->

<!-- review:SF-2026-ARXIV-2605-31328:start -->
#### Reinforcement Learning Amplifies Emergent Misalignment from Harmless Rewards

问题与机制：While EM has been extensively studied in the supervised fine-tuning (SFT) setting, evidence that it also arises from reinforcement learning (RL) is limited to large, closed-source models, leaving the phenomenon expensive to study and difficult to reproduce. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Reinforcement Learning Amplifies Emergent Misalignment from Harmless Rewards` exact-v1 在 §3.1 Experimental setup; §Evaluation.; §3.2 Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§D.3 Different judge model`；Evaluation=`§3.1 Experimental setup; §Evaluation.; §3.2 Results`。

Trade-off / failure / fallback：§6 Discussion; §7 Conclusion; §Limitations 该来源没有证明 `Reinforcement Learning Amplifies Emergent Misalignment from Harmless Rewards` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31328:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31328:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31328:end -->

<!-- review:SF-2026-ARXIV-2605-31354:start -->
#### Diagnosing Failure Modes of Shared-State Collaboration in Resource-Constrained Visual Agents

问题与机制：We study failure modes of collaborative reasoning with weak learners (4B--8B models) through the lens of noise accumulation. Owner=`AGENT-MULTI-AGENT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Diagnosing Failure Modes of Shared-State Collaboration in Resource-Constrained Visual Agents` exact-v1 在 §3.6 Cost–Utility Analysis; §4 Experiments Setup; §4.1 Evaluation Domains and Distributions 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§Architecture-centric document understanding.; §3 Method; §3.5 Traceability and Audit Framework`；Evaluation=`§3.6 Cost–Utility Analysis; §4 Experiments Setup; §4.1 Evaluation Domains and Distributions`。

Trade-off / failure / fallback：§6 Discussions; §7 Limitations; §8 Conclusion 该来源没有证明 `Diagnosing Failure Modes of Shared-State Collaboration in Resource-Constrained Visual Agents` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31354:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31354:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31354:end -->

<!-- review:SF-2026-ARXIV-2605-31361:start -->
#### Dreaming Of Others: Latent Teammate Modeling In World Models For Multi-Agent Reinforcement Learning

问题与机制：We propose a new perspective: treat teammates as structured, learnable components within the agent's world model. Owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Dreaming Of Others: Latent Teammate Modeling In World Models For Multi-Agent Reinforcement Learning` exact-v1 在 §4 Evaluation Protocol 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3.2 Architecture`；Evaluation=`§4 Evaluation Protocol`。

Trade-off / failure / fallback：§5 Discussion and Outlook 该来源没有证明 `Dreaming Of Others: Latent Teammate Modeling In World Models For Multi-Agent Reinforcement Learning` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31361:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31361:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31361:end -->

<!-- review:SF-2026-ARXIV-2605-31365:start -->
#### Learning to Adapt: Self-Improving Web Agent via Cognitive-Aware Exploration

问题与机制：To address these challenges, we propose SCALE (Self-Cognitive-Aware Learning and Exploration), which leverages three adversarial roles, Selector, Predictor, and Judger to autonomously discover the agent's limitations and expand its cognitive boundaries through environmental exploration. Owner=`AGENT-PLATFORM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Learning to Adapt: Self-Improving Web Agent via Cognitive-Aware Exploration` exact-v1 在 §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Method; §Appendix A Details of SCALE Framework and SCALE-20k Dataset; §A.2 Algorithm of the SCALE Framework`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Main Results`。

Trade-off / failure / fallback：§5 Conclusion 该来源没有证明 `Learning to Adapt: Self-Improving Web Agent via Cognitive-Aware Exploration` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31365:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31365:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31365:end -->

<!-- review:SF-2026-ARXIV-2605-31381:start -->
#### LLM Judges Inconsistently Disagree Across Safety Criteria and Harm Categories

问题与机制：We evaluate the consistency of automated judges in conducting a multi-dimensional safety evaluation in a reference-free setup. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `LLM Judges Inconsistently Disagree Across Safety Criteria and Harm Categories` exact-v1 在 §4 Results; §4.5 Qualitative Analysis; §Appendix D Query Safety Evaluations 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Methodology`；Evaluation=`§4 Results; §4.5 Qualitative Analysis; §Appendix D Query Safety Evaluations`。

Trade-off / failure / fallback：§5 Discussion; §Limitations 该来源没有证明 `LLM Judges Inconsistently Disagree Across Safety Criteria and Harm Categories` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31381:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31381:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31381:end -->

<!-- review:SF-2026-ARXIV-2605-31408:start -->
#### Skill Availability and Presentation Granularity in Large-Language-Model Agents: A Controlled SkillsBench Study

问题与机制：Skill documents provide procedural knowledge to large-language-model agents at inference time. Owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Skill Availability and Presentation Granularity in Large-Language-Model Agents: A Controlled SkillsBench Study` exact-v1 在 §3.2. Benchmark and Task Subset; §3.6. Statistical Analysis; §4. Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3. Method`；Evaluation=`§3.2. Benchmark and Task Subset; §3.6. Statistical Analysis; §4. Results`。

Trade-off / failure / fallback：§5. Discussion; §6. Threats to Validity; §8. Conclusion 该来源没有证明 `Skill Availability and Presentation Granularity in Large-Language-Model Agents: A Controlled SkillsBench Study` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31408:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31408:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31408:end -->

<!-- review:SF-2026-ARXIV-2605-31455:start -->
#### DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient Multi-Turn Optimization

问题与机制：To this end, we novelly propose DRIFT (Decoupled Rollouts and Importance-Weighted Fine-Tuning), a framework that operationalizes the theoretical insight that the KL-regularized RL objective is equivalent to importance-weighted supervised learning. Owner=`TRAIN-RLHF`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient Multi-Turn Optimization` exact-v1 在 §5 Experiments; §5.1 Experimental Setup; §5.2 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§5 Experiments; §5.1 Experimental Setup; §5.2 Main Results`。

Trade-off / failure / fallback：§6 Conclusion & Limitations; §E.3 Case 3: Limitations in Knowledge-Intensive Domains 该来源没有证明 `DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient Multi-Turn Optimization` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31455:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31455:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31455:end -->

<!-- review:SF-2026-ARXIV-2605-31460:start -->
#### On-Device Robotic Planning: Eliminating Inference Redundancy for Efficient Decision-Making

问题与机制：Based on this insight, we present REIS, a human cognition inspired robotic decision-making framework that minimizes unnecessary reasoning while preserving semantic adaptability. Owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `On-Device Robotic Planning: Eliminating Inference Redundancy for Efficient Decision-Making` exact-v1 在 §5 Evaluation; §Navigation Qualitative Analysis:; §Manipulation Failure Detection Analysis: 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§4 Method; §A.9 System Consistency by the Model`；Evaluation=`§5 Evaluation; §Navigation Qualitative Analysis:; §Manipulation Failure Detection Analysis:`。

Trade-off / failure / fallback：§6 Limitations, Future Directions and Conclusion 该来源没有证明 `On-Device Robotic Planning: Eliminating Inference Redundancy for Efficient Decision-Making` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31460:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31460:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31460:end -->

<!-- review:SF-2026-ARXIV-2605-31463:start -->
#### PithTrain: A Compact and Agent-Native MoE Training System

问题与机制：Grounded in four agent-native design principles, we build PithTrain, a compact, agent-native MoE training framework. Owner=`TRAIN-DISTRIBUTED-TRAINING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `PithTrain: A Compact and Agent-Native MoE Training System` exact-v1 在 §4 ATE-Bench: A Benchmark for Agent-Task Efficiency; §5 Evaluation; §Appendix C Per-Task Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3.2 System Architecture and Optimizations`；Evaluation=`§4 ATE-Bench: A Benchmark for Agent-Task Efficiency; §5 Evaluation; §Appendix C Per-Task Results`。

Trade-off / failure / fallback：§6 Conclusion 该来源没有证明 `PithTrain: A Compact and Agent-Native MoE Training System` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31463:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31463:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31463:end -->

<!-- review:SF-2026-ARXIV-2605-31464:start -->
#### GPU Forecasters: Language Models as Selective Surrogates for Kernel Runtime Optimization

问题与机制：To address this, we study how LLMs can serve as selective GPU surrogates for kernel evaluation, by forecasting the performance of proposed kernels. Owner=`INFER-TENSORRT-LLM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `GPU Forecasters: Language Models as Selective Surrogates for Kernel Runtime Optimization` exact-v1 在 §Kernel Evaluation.; §3 Experiments; §Appendix C Per-Evaluation Latency and Throughput on a Single A100 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§2 Method: LLM as Virtual GPU Surrogate`；Evaluation=`§Kernel Evaluation.; §3 Experiments; §Appendix C Per-Evaluation Latency and Throughput on a Single A100`。

Trade-off / failure / fallback：§5 Conclusion 该来源没有证明 `GPU Forecasters: Language Models as Selective Surrogates for Kernel Runtime Optimization` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31464:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31464:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31464:end -->

<!-- review:SF-2026-ARXIV-2605-31468:start -->
#### AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle

问题与机制：As a result, we present AutoSci, a memory-centric agentic system for the full scientific research lifecycle. Owner=`AGENT-WORKFLOW`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle` exact-v1 在 §7 Case Studies and Evaluation; §7.1 Experimental Setup; §7.4 Experiment Execution and Analysis 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§7 Case Studies and Evaluation; §7.1 Experimental Setup; §7.4 Experiment Execution and Analysis`。

Trade-off / failure / fallback：§9 Conclusion 该来源没有证明 `AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31468:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31468:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31468:end -->

<!-- review:SF-2026-ARXIV-2605-31490:start -->
#### Are Full Rollouts Necessary for On-Policy Distillation?

问题与机制：We identify the rollout horizon as a key bottleneck in OPD that substantially impacts training efficiency. Owner=`TRAIN-RLHF`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Are Full Rollouts Necessary for On-Policy Distillation?` exact-v1 在 §5 Experiments; §5.1 LLM Reasoning Experiments; §5.2 Analysis on Autoregressive Control Task 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§4 Methods`；Evaluation=`§5 Experiments; §5.1 LLM Reasoning Experiments; §5.2 Analysis on Autoregressive Control Task`。

Trade-off / failure / fallback：§7 Conclusion; §Discussion.; §8 Limitations 该来源没有证明 `Are Full Rollouts Necessary for On-Policy Distillation?` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31490:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31490:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31490:end -->

<!-- review:SF-2026-ARXIV-2605-31509:start -->
#### Skill Reuse as Compression in Agentic RL

问题与机制：To formalize this, we introduce ReuseRL, which grounds agentic RL in the Minimum Description Length (MDL) principle. Owner=`AGENT-PLATFORM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Skill Reuse as Compression in Agentic RL` exact-v1 在 §4 Experimental Settings; §4.3 Training and Evaluation; §5 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§4.4 Compared Methods`；Evaluation=`§4 Experimental Settings; §4.3 Training and Evaluation; §5 Main Results`。

Trade-off / failure / fallback：§8 Conclusion; §Limitations 该来源没有证明 `Skill Reuse as Compression in Agentic RL` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31509:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31509:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31509:end -->

<!-- review:SF-2026-ARXIV-2605-31557:start -->
#### EGOSTREAM: A Diagnostic Benchmark for Streaming Episodic Memory in Egocentric Vision

问题与机制：We introduce Egostream, a diagnostic benchmark for streaming episodic memory evaluation in egocentric vision. Owner=`AGENT-MEMORY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `EGOSTREAM: A Diagnostic Benchmark for Streaming Episodic Memory in Egocentric Vision` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§4 A Unified Framework for Streaming Episodic Memory; excerpt=all Regimes 3.4 Evaluation Protocol and Metrics 4 A Unified Framework for Streaming Episodic Memory 4.1 Memory Management Strategies 5 Experiments and Results 5.1 Controlled Diagnostic Evaluation 5.2 State-of-the-Art Streaming Models 5.3 Semantic Profiles and Temporal Decay 5.4 Memory Budget 6 Conclusion and Limitations References A The EgoStream Benchmark A.1 Hard Negative Generation Protocol A.2 Evidence Moment Annotation A.3 Human Va`；Evaluation=`§EgoStream : A Diagnostic Benchmark for Streaming Episodic Memory in Egocentric Vision; excerpt=EgoStream: A Diagnostic Benchmark for Streaming Episodic Memory in Egocentric Vision Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Related Work 3 The EgoStream Benchmark 3.1 Source Curation and Initial Set of `。

Trade-off / failure / fallback：§6 Conclusion and Limitations; excerpt=files and Temporal Decay 5.4 Memory Budget 6 Conclusion and Limitations References A The EgoStream Benchmark A.1 Hard Negative Generation Protocol A.2 Evidence Moment Annotation A.3 Human Validation A.4 Question Categorization Protocol and Labeling Guidelines A.4.1 Iterative Human-in-the-Loop (HITL) Workflow A.4.2 Primary Labeling: The Priority Cascade A.4.3 Secondary Labeling A.5 Answer Validity Window and Recall Regimes A.6 Recall Reg 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31557:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31557:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：streaming episodic-memory evaluation is already decomposed into acquisition, retention, dependency preservation, retrieval and reasoning correctness; EGOSTREAM adds an egocentric benchmark slice；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2605-31557:end -->

<!-- review:SF-2026-ARXIV-2605-31584:start -->
#### LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards

问题与机制：To address these issues, we introduce \textsc{LongTraceRL}. Owner=`TRAIN-RLHF`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards` exact-v1 在 §4 Experiments; §Benchmarks.; §4.2 Main Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§3 Method`；Evaluation=`§4 Experiments; §Benchmarks.; §4.2 Main Results`。

Trade-off / failure / fallback：§5 Conclusion; §6 Limitations 该来源没有证明 `LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31584:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31584:end -->

Books Decision=`No Change — Existing Coverage`；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31584:end -->

<!-- review:SF-2026-ARXIV-2605-31593:start -->
#### Stateful Online Monitoring Catches Distributed Agent Attacks

问题与机制：Language models can find thousands of severe software vulnerabilities, and agents are increasingly being misused for cyberattacks. Owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Stateful Online Monitoring Catches Distributed Agent Attacks` exact-v1 在 §4 Experiments; §Example 2: a shell-script CTF reduced to static analysis.; §Appendix C Agentic Decomposition Attack Results 披露的模型、任务与测量合同；未披露的硬件、精度、长度、batch、并发、SLO 或 evaluator 均记为 Not Disclosed。 Method=`§1 Introduction`；Evaluation=`§4 Experiments; §Example 2: a shell-script CTF reduced to static analysis.; §Appendix C Agentic Decomposition Attack Results`。

Trade-off / failure / fallback：§6 Conclusion 该来源没有证明 `Stateful Online Monitoring Catches Distributed Agent Attacks` 的机制能跨未披露 workload、模型族或生产约束成立，也不证明它优于 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31593:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31593:end -->

Books Decision=`No Change — Existing Coverage`；fresh-context challenge：stateful cross-session correlation and rare escalation are already owned by the cross-channel causal monitor; the paper's simulated traffic does not create a second monitoring authority；Books Gate 不需要该 family 写回；整体仍等待 final queue 写回与 post-write audit。
<!-- review:SF-2026-ARXIV-2605-31593:end -->

<!-- review:SF-2026-ARXIV-2605-31598:start -->
#### Linear Scaling Video VLMs for Long Video Understanding

问题与机制：We introduce StateKV, an inference-time method that adapts pretrained long-video VLMs to linear-time video prefill by carrying cross-frame context in a fixed-capacity, importance-based recurrent state, paired with a second full per-frame cache used for decoding. Owner=`INFER-KV-CACHE`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。

Evaluation contract：只支持 `Linear Scaling Video VLMs for Long Video Understanding` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。 Method=`§3 Method; excerpt= compression for long-context LLMs and multimodal models. 3 Method 3.1 Core Assumptions 3.2 Method Overview Preliminaries. Streaming cache construction with two memory states. Key insight: dynamic compressed state. 3.3 Per-frame cache-builder forward pass Updating the compressed state via attention-driven selection Virtual sequence length and cache positions. Consistent RoPE scaling across cache building and generation. Decoding using t`；Evaluation=`§4 Results; excerpt=ilding and generation. Decoding using the detailed cache. 4 Results Experimental Setup. Pareto frontier at fixed long-video length. FLOPs reduction enables larger backbones. Cross-backbone ablation across families and scales. Scaling behavior. Sliding-window instability across settings. Compute break-even behavior. 5 Conclusion References 0.A Empirical validation of the assumptions Scope. Shared protocol. 0.A.1 Assumption 1: concentrati`。

Trade-off / failure / fallback：§5 Conclusion; excerpt=ual context (e.g. by compressing the KV cache). A practical limitation of these methods is that aggressive compression can substantially degrade long-video performance unless a relatively large fraction of the visual information is retained. For instance, prior work found they must keep a large token fraction (around 60%) to avoid severe degradation when using cache-compression [ 65 ] . This issue can be even more acute for frame droppi 该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。

<!-- claim:SF-2026-ARXIV-2605-31598:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-31598:end -->

Books Decision=`Integrate`；fresh-context challenge：long-video VLMs can maintain a compressed recurrent construction state during frame ingestion while retaining a detailed decode cache for generation; both states need explicit identity, RoPE/position consistency, break-even accounting and fallback；最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-31598:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-00144 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00144 |
| SF-2026-ARXIV-2606-00150 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00150 |
| SF-2026-ARXIV-2606-00152 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00152 |
| SF-2026-ARXIV-2606-00160 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00160 |
| SF-2026-ARXIV-2606-00162 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00162 |
| SF-2026-ARXIV-2606-00172 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00172 |
| SF-2026-ARXIV-2606-00183 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00183 |
| SF-2026-ARXIV-2606-00186 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00186 |
| SF-2026-ARXIV-2606-00189 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00189 |
| SF-2026-ARXIV-2606-00198 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00198 |
| SF-2026-ARXIV-2606-00206 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00206 |
| SF-2026-ARXIV-2606-00229 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00229 |
| SF-2026-ARXIV-2606-00232 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00232 |
| SF-2026-ARXIV-2606-00251 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00251 |
| SF-2026-ARXIV-2606-00257 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00257 |
| SF-2026-ARXIV-2606-00267 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00267 |
| SF-2026-ARXIV-2606-00269 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00269 |
| SF-2026-ARXIV-2606-00271 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00271 |
| SF-2026-ARXIV-2606-00279 | score_7_9;forced_review;potential_books_delta | selected | DA-BIT-EXACT-INFERENCE-VERIFICATION | — | cross-layer state/control/evidence owner change | analysis:DA-BIT-EXACT-INFERENCE-VERIFICATION |
| SF-2026-ARXIV-2606-00284 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00284 |
| SF-2026-ARXIV-2606-00301 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00301 |
| SF-2026-ARXIV-2606-00305 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00305 |
| SF-2026-ARXIV-2606-00308 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00308 |
| SF-2026-ARXIV-2606-00318 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00318 |
| SF-2026-ARXIV-2606-00329 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00329 |
| SF-2026-ARXIV-2606-00341 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00341 |
| SF-2026-ARXIV-2606-00348 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00348 |
| SF-2026-ARXIV-2606-00365 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00365 |
| SF-2026-ARXIV-2606-00376 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00376 |
| SF-2026-ARXIV-2606-00380 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00380 |
| SF-2026-ARXIV-2606-00382 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00382 |
| SF-2026-ARXIV-2606-00392 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00392 |
| SF-2026-ARXIV-2606-00395 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00395 |
| SF-2026-ARXIV-2606-00400 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00400 |
| SF-2026-ARXIV-2606-00408 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00408 |
| SF-2026-ARXIV-2606-00414 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00414 |
| SF-2026-ARXIV-2606-00424 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00424 |
| SF-2026-ARXIV-2606-00432 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00432 |
| SF-2026-ARXIV-2606-00437 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00437 |
| SF-2026-ARXIV-2606-00439 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00439 |
| SF-2026-ARXIV-2606-00448 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00448 |
| SF-2026-ARXIV-2606-00457 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-00457 |
| SF-2026-ARXIV-2606-07595 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-07595 |
| SF-2026-ARXIV-2606-07603 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-07603 |
| SF-2026-ARXIV-2606-07616 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-07616 |
| SF-2026-ARXIV-2606-20631 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-20631 |
| SF-2026-ARXIV-2606-24893 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-24893 |
| SF-2026-ARXIV-2606-28337 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2606-28337 |
| SF-2026-ARXIV-2605-30711 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30711 |
| SF-2026-ARXIV-2605-30712 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30712 |
| SF-2026-ARXIV-2605-30723 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30723 |
| SF-2026-ARXIV-2605-30727 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30727 |
| SF-2026-ARXIV-2605-30728 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30728 |
| SF-2026-ARXIV-2605-30736 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30736 |
| SF-2026-ARXIV-2605-30738 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30738 |
| SF-2026-ARXIV-2605-30753 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30753 |
| SF-2026-ARXIV-2605-30757 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30757 |
| SF-2026-ARXIV-2605-30771 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30771 |
| SF-2026-ARXIV-2605-30777 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30777 |
| SF-2026-ARXIV-2605-30785 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30785 |
| SF-2026-ARXIV-2605-30789 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30789 |
| SF-2026-ARXIV-2605-30790 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30790 |
| SF-2026-ARXIV-2605-30803 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30803 |
| SF-2026-ARXIV-2605-30807 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30807 |
| SF-2026-ARXIV-2605-30824 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30824 |
| SF-2026-ARXIV-2605-30832 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30832 |
| SF-2026-ARXIV-2605-30833 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30833 |
| SF-2026-ARXIV-2605-30834 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30834 |
| SF-2026-ARXIV-2605-30837 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30837 |
| SF-2026-ARXIV-2605-30838 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30838 |
| SF-2026-ARXIV-2605-30842 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30842 |
| SF-2026-ARXIV-2605-30851 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30851 |
| SF-2026-ARXIV-2605-30852 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30852 |
| SF-2026-ARXIV-2605-30854 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30854 |
| SF-2026-ARXIV-2605-30855 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30855 |
| SF-2026-ARXIV-2605-30859 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30859 |
| SF-2026-ARXIV-2605-30880 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30880 |
| SF-2026-ARXIV-2605-30883 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30883 |
| SF-2026-ARXIV-2605-30888 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30888 |
| SF-2026-ARXIV-2605-30896 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30896 |
| SF-2026-ARXIV-2605-30898 | score_7_9;forced_review;potential_books_delta | selected | DA-UNIFIED-ROUTING-TEST-TIME-SCALING | — | cross-layer state/control/evidence owner change | analysis:DA-UNIFIED-ROUTING-TEST-TIME-SCALING |
| SF-2026-ARXIV-2605-30911 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30911 |
| SF-2026-ARXIV-2605-30917 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30917 |
| SF-2026-ARXIV-2605-30924 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30924 |
| SF-2026-ARXIV-2605-30998 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-30998 |
| SF-2026-ARXIV-2605-31033 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31033 |
| SF-2026-ARXIV-2605-31042 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31042 |
| SF-2026-ARXIV-2605-31058 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31058 |
| SF-2026-ARXIV-2605-31066 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31066 |
| SF-2026-ARXIV-2605-31073 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31073 |
| SF-2026-ARXIV-2605-31086 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31086 |
| SF-2026-ARXIV-2605-31105 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31105 |
| SF-2026-ARXIV-2605-31111 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31111 |
| SF-2026-ARXIV-2605-31158 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31158 |
| SF-2026-ARXIV-2605-31159 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31159 |
| SF-2026-ARXIV-2605-31164 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31164 |
| SF-2026-ARXIV-2605-31167 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31167 |
| SF-2026-ARXIV-2605-31170 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31170 |
| SF-2026-ARXIV-2605-31175 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31175 |
| SF-2026-ARXIV-2605-31176 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31176 |
| SF-2026-ARXIV-2605-31244 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31244 |
| SF-2026-ARXIV-2605-31264 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31264 |
| SF-2026-ARXIV-2605-31278 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31278 |
| SF-2026-ARXIV-2605-31308 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31308 |
| SF-2026-ARXIV-2605-31328 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31328 |
| SF-2026-ARXIV-2605-31354 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31354 |
| SF-2026-ARXIV-2605-31361 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31361 |
| SF-2026-ARXIV-2605-31365 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31365 |
| SF-2026-ARXIV-2605-31381 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31381 |
| SF-2026-ARXIV-2605-31408 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31408 |
| SF-2026-ARXIV-2605-31455 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31455 |
| SF-2026-ARXIV-2605-31460 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31460 |
| SF-2026-ARXIV-2605-31463 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31463 |
| SF-2026-ARXIV-2605-31464 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31464 |
| SF-2026-ARXIV-2605-31468 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31468 |
| SF-2026-ARXIV-2605-31490 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31490 |
| SF-2026-ARXIV-2605-31509 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31509 |
| SF-2026-ARXIV-2605-31557 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31557 |
| SF-2026-ARXIV-2605-31584 | score_7_9 | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31584 |
| SF-2026-ARXIV-2605-31593 | score_7_9;forced_review;potential_books_delta | selected | DA-STATEFUL-DISTRIBUTED-AGENT-MONITORING | — | cross-layer state/control/evidence owner change | analysis:DA-STATEFUL-DISTRIBUTED-AGENT-MONITORING |
| SF-2026-ARXIV-2605-31598 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 review complete; lower narrative priority | analysis-decision:SF-2026-ARXIV-2605-31598 |

<!-- analysis-decision:SF-2026-ARXIV-2606-00144:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00144:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00150:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00150:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00152:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00152:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00160:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00160:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00162:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00162:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00172:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00172:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00183:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00183:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00186:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00186:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00189:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00189:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00198:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00198:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00206:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00206:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00229:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00229:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00232:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00232:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00251:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00251:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00257:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00257:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00267:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00267:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00269:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00269:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00271:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00271:end -->

<!-- analysis:DA-BIT-EXACT-INFERENCE-VERIFICATION:start -->
### DA-BIT-EXACT-INFERENCE-VERIFICATION

旧的 inference audit 采用近似数值匹配，因为并行 reduction 的非结合性被视作不可消除噪声；这在只要求运行可复现时合理，却给低信任 prover 留下可否认空间。exact-v1 将差异拆成固定硬件/软件 reduction tree 导致的 non-invariance 与 atomic accumulation 导致的 genuine nondeterminism，并用 CPU 软件模型复现 tensor-core block-FMA、SFU、kernel reduction、RoPE 与 FlashAttention-2 的舍入路径。控制权因此从‘接受容差’转为‘记录 hardware SKU、software stack、quantization/kernel、parallel topology 与动态 batch size，再进行 bit-exact recomputation’。作者在 Qwen3-4B、多个 NVIDIA SKU 与列明的 vLLM/HF stack 上报告中间张量逐 bit 匹配；代价是维护 SKU/kernel dispatch catalog 和复算成本，且 MoE、部分 INT atomic kernel、非 NVIDIA、training backward 尚未覆盖。所以本日报只把它作为可审计 inference identity 的受限机制证据，不推导为所有加速器或所有训练 workload 都可 bit-exact。
<!-- analysis:DA-BIT-EXACT-INFERENCE-VERIFICATION:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00284:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00284:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00301:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00301:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00305:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00305:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00308:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00308:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00318:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00318:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00329:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00329:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00341:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00341:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00348:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00348:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00365:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00365:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00376:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00376:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00380:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00380:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00382:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00382:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00392:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00392:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00395:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00395:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00400:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00400:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00408:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00408:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00414:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00414:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00424:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00424:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00432:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00432:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00437:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00437:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00439:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00439:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00448:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00448:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-00457:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-00457:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07595:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-07595:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07603:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-07603:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-07616:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-07616:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20631:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-20631:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24893:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-24893:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28337:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2606-28337:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30711:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30711:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30712:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30712:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30723:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30723:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30727:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30727:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30728:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30728:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30736:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30736:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30738:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30738:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30753:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30753:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30757:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30757:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30771:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30771:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30777:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30777:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30785:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30785:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30789:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30789:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30790:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30790:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30803:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30803:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30807:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30807:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30824:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30824:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30832:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30832:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30833:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30833:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30834:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30834:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30837:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30837:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30838:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30838:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30842:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30842:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30851:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30851:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30852:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30852:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30854:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30854:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30855:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30855:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30859:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30859:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30880:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30880:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30883:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30883:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30888:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30888:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30896:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30896:end -->

<!-- analysis:DA-UNIFIED-ROUTING-TEST-TIME-SCALING:start -->
### DA-UNIFIED-ROUTING-TEST-TIME-SCALING

把 model routing 与 test-time scaling 分开优化，在模型规模离散、单模型 compute 边际收益快速递减时仍然合理，但二者各自选择会遗漏跨维组合。UniScale 把 model、reasoning path、candidate count 与 batch/configuration 组成统一 action space，由 query/action semantic representation 驱动 LinUCB，在每次请求后用 verifier quality 与 cost model 的复合 reward 更新策略；state owner 由静态 router 迁移到带 uncertainty 的在线闭环控制器。exact-v1 的实验显示其在所测动态场景中改变 quality-cost frontier，且 query embedding 加 bandit update 在作者 160 次 warm-up 后统计中占总时延 0.91%；收益同时引入 exploration、reward-estimator drift、action-space discretization 与 verifier 误差。论文结论明确仍受 PRM 精度约束，因此不能把作者结果外推成任意任务、任意 SLO 或生产流量下的最优调度；旧的固定 router 在低漂移、可预测 workload 下仍更简单。
<!-- analysis:DA-UNIFIED-ROUTING-TEST-TIME-SCALING:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30911:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30911:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30917:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30917:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30924:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30924:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-30998:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-30998:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31033:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31033:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31042:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31042:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31058:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31058:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31066:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31066:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31073:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31073:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31086:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31086:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31105:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31105:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31111:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31111:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31158:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31158:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31159:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31159:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31164:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31164:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31167:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31167:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31170:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31170:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31175:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31175:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31176:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31176:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31244:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31244:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31264:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31264:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31278:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31278:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31308:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31308:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31328:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31328:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31354:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31354:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31361:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31361:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31365:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31365:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31381:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31381:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31408:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31408:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31455:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31455:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31460:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31460:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31463:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31463:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31464:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31464:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31468:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31468:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31490:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31490:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31509:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31509:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31557:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31557:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31584:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31584:end -->

<!-- analysis:DA-STATEFUL-DISTRIBUTED-AGENT-MONITORING:start -->
### DA-STATEFUL-DISTRIBUTED-AGENT-MONITORING

逐 transcript 的无状态 monitor 在单会话攻击下合理，却看不到攻击者把同一目标拆到多个账号和 subagent 后留下的弱相关信号。exact-v1 让 monitoring state 成为跨会话资源：每个请求先做局部 suspiciousness 与 embedding，在线聚合到 centroid/buffer；只有簇积累足够跨会话证据时才调用 cross-context LLM，决定 allow/refuse。这把安全控制点从孤立 request classifier 演进为 streaming correlation + rare escalation，并在作者模拟 datacenter traffic 与 cyber task 设置中报告更早检测，同时让约 99% 流量不支付额外 LLM reasoning 延迟。代价是持久化跨用户表征带来的隐私/tenancy 边界、cluster poisoning、阈值校准、P99 escalation 与 background traffic 放大；作者 red-team 也发现状态监控仍有规避路径，不能证明对其他威胁模型或真实生产基线同样成立。
<!-- analysis:DA-STATEFUL-DISTRIBUTED-AGENT-MONITORING:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-31598:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:SF-2026-ARXIV-2605-31598:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-00144 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2606-00144 | delta:SF-2026-ARXIV-2606-00144 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00144 |
| SF-2026-ARXIV-2606-00150 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2606-00150 | delta:SF-2026-ARXIV-2606-00150 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00150 |
| SF-2026-ARXIV-2606-00152 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2606-00152 | delta:SF-2026-ARXIV-2606-00152 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00152 |
| SF-2026-ARXIV-2606-00160 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2606-00160 | delta:SF-2026-ARXIV-2606-00160 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-00160 |
| SF-2026-ARXIV-2606-00162 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2606-00162 | delta:SF-2026-ARXIV-2606-00162 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00162 |
| SF-2026-ARXIV-2606-00172 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2606-00172 | delta:SF-2026-ARXIV-2606-00172 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00172 |
| SF-2026-ARXIV-2606-00183 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2606-00183 | delta:SF-2026-ARXIV-2606-00183 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00183 |
| SF-2026-ARXIV-2606-00186 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00186 | delta:SF-2026-ARXIV-2606-00186 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00186 |
| SF-2026-ARXIV-2606-00189 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2606-00189 | delta:SF-2026-ARXIV-2606-00189 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00189 |
| SF-2026-ARXIV-2606-00198 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2606-00198 | delta:SF-2026-ARXIV-2606-00198 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00198 |
| SF-2026-ARXIV-2606-00206 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00206 | delta:SF-2026-ARXIV-2606-00206 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00206 |
| SF-2026-ARXIV-2606-00229 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2606-00229 | delta:SF-2026-ARXIV-2606-00229 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00229 |
| SF-2026-ARXIV-2606-00232 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00232 | delta:SF-2026-ARXIV-2606-00232 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00232 |
| SF-2026-ARXIV-2606-00251 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00251 | delta:SF-2026-ARXIV-2606-00251 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00251 |
| SF-2026-ARXIV-2606-00257 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2606-00257 | delta:SF-2026-ARXIV-2606-00257 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-00257 |
| SF-2026-ARXIV-2606-00267 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2606-00267 | delta:SF-2026-ARXIV-2606-00267 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00267 |
| SF-2026-ARXIV-2606-00269 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2606-00269 | delta:SF-2026-ARXIV-2606-00269 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00269 |
| SF-2026-ARXIV-2606-00271 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2606-00271 | delta:SF-2026-ARXIV-2606-00271 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-00271 |
| SF-2026-ARXIV-2606-00279 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00279 | delta:SF-2026-ARXIV-2606-00279 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-00279 |
| SF-2026-ARXIV-2606-00284 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2606-00284 | delta:SF-2026-ARXIV-2606-00284 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00284 |
| SF-2026-ARXIV-2606-00301 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66; books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2606-00301 | delta:SF-2026-ARXIV-2606-00301 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00301 |
| SF-2026-ARXIV-2606-00305 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2606-00305 | delta:SF-2026-ARXIV-2606-00305 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00305 |
| SF-2026-ARXIV-2606-00308 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2606-00308 | delta:SF-2026-ARXIV-2606-00308 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00308 |
| SF-2026-ARXIV-2606-00318 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2606-00318 | delta:SF-2026-ARXIV-2606-00318 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-00318 |
| SF-2026-ARXIV-2606-00329 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66; books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2606-00329 | delta:SF-2026-ARXIV-2606-00329 | Direct Evolution | Weekly Only — Context | books-review:SF-2026-ARXIV-2606-00329 |
| SF-2026-ARXIV-2606-00341 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2606-00341 | delta:SF-2026-ARXIV-2606-00341 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00341 |
| SF-2026-ARXIV-2606-00348 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69; books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2606-00348 | delta:SF-2026-ARXIV-2606-00348 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00348 |
| SF-2026-ARXIV-2606-00365 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2606-00365 | delta:SF-2026-ARXIV-2606-00365 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00365 |
| SF-2026-ARXIV-2606-00376 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2606-00376 | delta:SF-2026-ARXIV-2606-00376 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00376 |
| SF-2026-ARXIV-2606-00380 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00380 | delta:SF-2026-ARXIV-2606-00380 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00380 |
| SF-2026-ARXIV-2606-00382 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2606-00382 | delta:SF-2026-ARXIV-2606-00382 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00382 |
| SF-2026-ARXIV-2606-00392 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2606-00392 | delta:SF-2026-ARXIV-2606-00392 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00392 |
| SF-2026-ARXIV-2606-00395 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00395 | delta:SF-2026-ARXIV-2606-00395 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00395 |
| SF-2026-ARXIV-2606-00400 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28; books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2606-00400 | delta:SF-2026-ARXIV-2606-00400 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-00400 |
| SF-2026-ARXIV-2606-00408 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00408 | delta:SF-2026-ARXIV-2606-00408 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00408 |
| SF-2026-ARXIV-2606-00414 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00414 | delta:SF-2026-ARXIV-2606-00414 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00414 |
| SF-2026-ARXIV-2606-00424 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00424 | delta:SF-2026-ARXIV-2606-00424 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00424 |
| SF-2026-ARXIV-2606-00432 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00432 | delta:SF-2026-ARXIV-2606-00432 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00432 |
| SF-2026-ARXIV-2606-00437 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-00437 | delta:SF-2026-ARXIV-2606-00437 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-00437 |
| SF-2026-ARXIV-2606-00439 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2606-00439 | delta:SF-2026-ARXIV-2606-00439 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00439 |
| SF-2026-ARXIV-2606-00448 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2606-00448 | delta:SF-2026-ARXIV-2606-00448 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00448 |
| SF-2026-ARXIV-2606-00457 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69; books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2606-00457 | delta:SF-2026-ARXIV-2606-00457 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-00457 |
| SF-2026-ARXIV-2606-07595 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2606-07595 | delta:SF-2026-ARXIV-2606-07595 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07595 |
| SF-2026-ARXIV-2606-07603 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-07603 | delta:SF-2026-ARXIV-2606-07603 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07603 |
| SF-2026-ARXIV-2606-07616 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-07616 | delta:SF-2026-ARXIV-2606-07616 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-07616 |
| SF-2026-ARXIV-2606-20631 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2606-20631 | delta:SF-2026-ARXIV-2606-20631 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20631 |
| SF-2026-ARXIV-2606-24893 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2606-24893 | delta:SF-2026-ARXIV-2606-24893 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-24893 |
| SF-2026-ARXIV-2606-28337 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2606-28337 | delta:SF-2026-ARXIV-2606-28337 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28337 |
| SF-2026-ARXIV-2605-30711 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-30711 | delta:SF-2026-ARXIV-2605-30711 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30711 |
| SF-2026-ARXIV-2605-30712 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-30712 | delta:SF-2026-ARXIV-2605-30712 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30712 |
| SF-2026-ARXIV-2605-30723 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-30723 | delta:SF-2026-ARXIV-2605-30723 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30723 |
| SF-2026-ARXIV-2605-30727 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-30727 | delta:SF-2026-ARXIV-2605-30727 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-30727 |
| SF-2026-ARXIV-2605-30728 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-30728 | delta:SF-2026-ARXIV-2605-30728 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30728 |
| SF-2026-ARXIV-2605-30736 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-30736 | delta:SF-2026-ARXIV-2605-30736 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30736 |
| SF-2026-ARXIV-2605-30738 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-30738 | delta:SF-2026-ARXIV-2605-30738 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30738 |
| SF-2026-ARXIV-2605-30753 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23; books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-30753 | delta:SF-2026-ARXIV-2605-30753 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30753 |
| SF-2026-ARXIV-2605-30757 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-30757 | delta:SF-2026-ARXIV-2605-30757 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30757 |
| SF-2026-ARXIV-2605-30771 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-30771 | delta:SF-2026-ARXIV-2605-30771 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30771 |
| SF-2026-ARXIV-2605-30777 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-30777 | delta:SF-2026-ARXIV-2605-30777 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30777 |
| SF-2026-ARXIV-2605-30785 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74; books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-30785 | delta:SF-2026-ARXIV-2605-30785 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30785 |
| SF-2026-ARXIV-2605-30789 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-30789 | delta:SF-2026-ARXIV-2605-30789 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-30789 |
| SF-2026-ARXIV-2605-30790 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-30790 | delta:SF-2026-ARXIV-2605-30790 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30790 |
| SF-2026-ARXIV-2605-30803 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-30803 | delta:SF-2026-ARXIV-2605-30803 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30803 |
| SF-2026-ARXIV-2605-30807 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-30807 | delta:SF-2026-ARXIV-2605-30807 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30807 |
| SF-2026-ARXIV-2605-30824 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-30824 | delta:SF-2026-ARXIV-2605-30824 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30824 |
| SF-2026-ARXIV-2605-30832 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-30832 | delta:SF-2026-ARXIV-2605-30832 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30832 |
| SF-2026-ARXIV-2605-30833 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-30833 | delta:SF-2026-ARXIV-2605-30833 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30833 |
| SF-2026-ARXIV-2605-30834 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-30834 | delta:SF-2026-ARXIV-2605-30834 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30834 |
| SF-2026-ARXIV-2605-30837 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-30837 | delta:SF-2026-ARXIV-2605-30837 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30837 |
| SF-2026-ARXIV-2605-30838 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-30838 | delta:SF-2026-ARXIV-2605-30838 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30838 |
| SF-2026-ARXIV-2605-30842 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74; books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-30842 | delta:SF-2026-ARXIV-2605-30842 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30842 |
| SF-2026-ARXIV-2605-30851 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-30851 | delta:SF-2026-ARXIV-2605-30851 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-30851 |
| SF-2026-ARXIV-2605-30852 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-30852 | delta:SF-2026-ARXIV-2605-30852 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30852 |
| SF-2026-ARXIV-2605-30854 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-30854 | delta:SF-2026-ARXIV-2605-30854 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30854 |
| SF-2026-ARXIV-2605-30855 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-30855 | delta:SF-2026-ARXIV-2605-30855 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30855 |
| SF-2026-ARXIV-2605-30859 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-30859 | delta:SF-2026-ARXIV-2605-30859 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30859 |
| SF-2026-ARXIV-2605-30880 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-30880 | delta:SF-2026-ARXIV-2605-30880 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30880 |
| SF-2026-ARXIV-2605-30883 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-30883 | delta:SF-2026-ARXIV-2605-30883 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30883 |
| SF-2026-ARXIV-2605-30888 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-30888 | delta:SF-2026-ARXIV-2605-30888 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30888 |
| SF-2026-ARXIV-2605-30896 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-30896 | delta:SF-2026-ARXIV-2605-30896 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30896 |
| SF-2026-ARXIV-2605-30898 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-30898 | delta:SF-2026-ARXIV-2605-30898 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-30898 |
| SF-2026-ARXIV-2605-30911 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-30911 | delta:SF-2026-ARXIV-2605-30911 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30911 |
| SF-2026-ARXIV-2605-30917 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-30917 | delta:SF-2026-ARXIV-2605-30917 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30917 |
| SF-2026-ARXIV-2605-30924 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-30924 | delta:SF-2026-ARXIV-2605-30924 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30924 |
| SF-2026-ARXIV-2605-30998 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-30998 | delta:SF-2026-ARXIV-2605-30998 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-30998 |
| SF-2026-ARXIV-2605-31033 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-31033 | delta:SF-2026-ARXIV-2605-31033 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31033 |
| SF-2026-ARXIV-2605-31042 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-31042 | delta:SF-2026-ARXIV-2605-31042 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-31042 |
| SF-2026-ARXIV-2605-31058 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-31058 | delta:SF-2026-ARXIV-2605-31058 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31058 |
| SF-2026-ARXIV-2605-31066 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-31066 | delta:SF-2026-ARXIV-2605-31066 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31066 |
| SF-2026-ARXIV-2605-31073 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-31073 | delta:SF-2026-ARXIV-2605-31073 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31073 |
| SF-2026-ARXIV-2605-31086 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-31086 | delta:SF-2026-ARXIV-2605-31086 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31086 |
| SF-2026-ARXIV-2605-31105 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-31105 | delta:SF-2026-ARXIV-2605-31105 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31105 |
| SF-2026-ARXIV-2605-31111 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-31111 | delta:SF-2026-ARXIV-2605-31111 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31111 |
| SF-2026-ARXIV-2605-31158 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-31158 | delta:SF-2026-ARXIV-2605-31158 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31158 |
| SF-2026-ARXIV-2605-31159 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-31159 | delta:SF-2026-ARXIV-2605-31159 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31159 |
| SF-2026-ARXIV-2605-31164 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-31164 | delta:SF-2026-ARXIV-2605-31164 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31164 |
| SF-2026-ARXIV-2605-31167 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-31167 | delta:SF-2026-ARXIV-2605-31167 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31167 |
| SF-2026-ARXIV-2605-31170 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-31170 | delta:SF-2026-ARXIV-2605-31170 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31170 |
| SF-2026-ARXIV-2605-31175 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-31175 | delta:SF-2026-ARXIV-2605-31175 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31175 |
| SF-2026-ARXIV-2605-31176 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-31176 | delta:SF-2026-ARXIV-2605-31176 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31176 |
| SF-2026-ARXIV-2605-31244 | WORLDVIEW-SCALING-LAW | books/part-01-worldview/07-scaling-law.md#chapter-7 | books/part-01-worldview/06-why-transformer-changed-the-world.md#chapter-6; books/part-01-worldview/08-why-llms-show-intelligence.md#chapter-8 | existing:SF-2026-ARXIV-2605-31244 | delta:SF-2026-ARXIV-2605-31244 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31244 |
| SF-2026-ARXIV-2605-31264 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-31264 | delta:SF-2026-ARXIV-2605-31264 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31264 |
| SF-2026-ARXIV-2605-31278 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-31278 | delta:SF-2026-ARXIV-2605-31278 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31278 |
| SF-2026-ARXIV-2605-31308 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-31308 | delta:SF-2026-ARXIV-2605-31308 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31308 |
| SF-2026-ARXIV-2605-31328 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-31328 | delta:SF-2026-ARXIV-2605-31328 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31328 |
| SF-2026-ARXIV-2605-31354 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-31354 | delta:SF-2026-ARXIV-2605-31354 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31354 |
| SF-2026-ARXIV-2605-31361 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-31361 | delta:SF-2026-ARXIV-2605-31361 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31361 |
| SF-2026-ARXIV-2605-31365 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-31365 | delta:SF-2026-ARXIV-2605-31365 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31365 |
| SF-2026-ARXIV-2605-31381 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-31381 | delta:SF-2026-ARXIV-2605-31381 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31381 |
| SF-2026-ARXIV-2605-31408 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-31408 | delta:SF-2026-ARXIV-2605-31408 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31408 |
| SF-2026-ARXIV-2605-31455 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-31455 | delta:SF-2026-ARXIV-2605-31455 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31455 |
| SF-2026-ARXIV-2605-31460 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-31460 | delta:SF-2026-ARXIV-2605-31460 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31460 |
| SF-2026-ARXIV-2605-31463 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-31463 | delta:SF-2026-ARXIV-2605-31463 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31463 |
| SF-2026-ARXIV-2605-31464 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-31464 | delta:SF-2026-ARXIV-2605-31464 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31464 |
| SF-2026-ARXIV-2605-31468 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-31468 | delta:SF-2026-ARXIV-2605-31468 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31468 |
| SF-2026-ARXIV-2605-31490 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-31490 | delta:SF-2026-ARXIV-2605-31490 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31490 |
| SF-2026-ARXIV-2605-31509 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-31509 | delta:SF-2026-ARXIV-2605-31509 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31509 |
| SF-2026-ARXIV-2605-31557 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-31557 | delta:SF-2026-ARXIV-2605-31557 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31557 |
| SF-2026-ARXIV-2605-31584 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-31584 | delta:SF-2026-ARXIV-2605-31584 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31584 |
| SF-2026-ARXIV-2605-31593 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-31593 | delta:SF-2026-ARXIV-2605-31593 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-31593 |
| SF-2026-ARXIV-2605-31598 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-31598 | delta:SF-2026-ARXIV-2605-31598 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-31598 |

<!-- books-review:SF-2026-ARXIV-2606-00144:start -->
<!-- existing:SF-2026-ARXIV-2606-00144:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场 **Stable Knowledge Node ID:** `INFER-SPECULATIVE-DECODING` **Legacy Chapter:** Ch44 **Status:** Draft<!-- existing:SF-2026-ARXIV-2606-00144:end -->
<!-- delta:SF-2026-ARXIV-2606-00144:start -->Speculative decoding speeds up autoregressive decoding by using a drafter to propose multiple tokens that a verifier validates in parallel. Changed constraint / result：Experimental results on PG-19, LongBench, and LWM show that BudgetDraft achieves up to 6.55x, 4.46x, and 2.10x end-to-end speedup vs AR at 4K, 8K, and 16K context lengths, while keeping the inference pipeline memory-friendly.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00144:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00144:end -->

<!-- books-review:SF-2026-ARXIV-2606-00150:start -->
<!-- existing:SF-2026-ARXIV-2606-00150:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：从 single-turn text、isolated multimodal 或 multi-turn text，演进到 run-centric multimodal campaign，获得的是 transition-level attribution：哪一次表示变换、反馈或重试之后 policy 发生变化。新增代价包括有害 media 的 access/retention/deletion、campaign resume correctness、cache poisoning、provider drift、judge injection 与更高 成本。只保存最终 attack-success rate 会丢掉这些 state，也无法重放或修复失败路径。<!-- existing:SF-2026-ARXIV-2606-00150:end -->
<!-- delta:SF-2026-ARXIV-2606-00150:start -->In this paper, we propose Persona Attack, a memory injection based jailbreak method that manipulates the model's context window through a step by step approach. Changed constraint / result：Experimental results from applying Persona Attack to several widely used LLMs reveal that, as injections accumulate in memory, models increasingly prioritize these instructions over their internal safety alignment mechanisms.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00150:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00150:end -->

<!-- books-review:SF-2026-ARXIV-2606-00152:start -->
<!-- existing:SF-2026-ARXIV-2606-00152:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：| 发布对象 | 被保护单元与机制位置 | 获得什么 | 新增代价 | | --- | --- | --- | --- | | Synthetic data | private prediction 在 token aggregation 时消费 budget | 下游可复用 DP output | 可发布数量受 budget 限制，生成昂贵 | | Fine-tuned model | user-level clipping、sampling 与 noisy update | 模型发布不强依赖单个用户 | contribution bound 丢数据，noise 损失 utility | | Training runtime | distributed clipping/noise/accounting/auditing | 把数学机制落实到并行训练 | shard、microbatch、padding 和随机数都进入正确性边界 | | Usage insights | DP clustering/keyword extraction 后再由 LLM summarization | 发布总体使用模式 | 小群体信号和稀有主题可能被抑制 |<!-- existing:SF-2026-ARXIV-2606-00152:end -->
<!-- delta:SF-2026-ARXIV-2606-00152:start -->To assess its prevalence, we introduce \emph{PrivacyPeek}, a benchmark for evaluating acquisition-stage privacy leakage of LLM-based agents, with $1{,}182$ cases across $7$ acquisition behaviours and $16$ application domains. Changed constraint / result：Our experiments on $10$ LLM-based agents across $4$ model families show that the unnecessary acquisition of sensitive information is widespread.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00152:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00152:end -->

<!-- books-review:SF-2026-ARXIV-2606-00160:start -->
<!-- existing:SF-2026-ARXIV-2606-00160:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part IV Training System：模型能力如何产生 **Stable Knowledge Node ID:** `TRAIN-DATA` **Legacy Chapter:** Ch23 **Status:** Draft<!-- existing:SF-2026-ARXIV-2606-00160:end -->
<!-- delta:SF-2026-ARXIV-2606-00160:start -->In this paper, we propose DataShield to efficiently and effectively identify potential safety-degrading samples. Changed constraint / result：Extensive experimental evaluation on Llama3-8B, Llama3.1-8B, and Qwen2.5-7B using the Alpaca and Dolly benign datasets validates our method's effectiveness in identifying high-risk and low-risk data subsets.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00160:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00160:end -->

<!-- books-review:SF-2026-ARXIV-2606-00162:start -->
<!-- existing:SF-2026-ARXIV-2606-00162:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：这不是把 KV Cache 当作永远有效的事实。cache identity 必须绑定 episode、instruction、observation history 和 refresh generation；instruction、episode 或历史改变时必须 invalidate/rebuild。训练还要显式暴露与部署一致的 staleness range，否则 action expert 只在同步特征上学习，异步运行时会读取未见过的旧状态。<!-- existing:SF-2026-ARXIV-2606-00162:end -->
<!-- delta:SF-2026-ARXIV-2606-00162:start -->We model dataset construction as an artifact-based build process over a dependency graph and implement this approach in Bagzel, an open-source Bazel extension for reproducible, incremental dataset generation (including nuScenes-format export). Changed constraint / result：Across dataset sizes from 5.1 to 20.4 GB, Bagzel variants show markedly better scaling behavior than the baseline, especially in warm and incremental modes.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00162:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00162:end -->

<!-- books-review:SF-2026-ARXIV-2606-00172:start -->
<!-- existing:SF-2026-ARXIV-2606-00172:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text PPO on-policy optimization with learned value/advantage and clipping GRPO group-relative advantage without a learned critic DPO offline pairwise objective derived from KL-constrained preference optimization ```<!-- existing:SF-2026-ARXIV-2606-00172:end -->
<!-- delta:SF-2026-ARXIV-2606-00172:start -->On-Policy Self-Distillation (OPSD) offers dense token-level guidance, but its token preferences are not necessarily aligned with trajectory correctness; empirical diagnostics show that OPSD signals behave differently on correct and incorrect rollouts, with teacher-positive and teacher-negative gap signals exhibiting different noise profiles. Changed constraint / result：On-Policy Self-Distillation (OPSD) offers dense token-level guidance, but its token preferences are not necessarily aligned with trajectory correctness; empirical diagnostics show that OPSD signals behave differently on correct and incorrect rollouts, with teacher-positive and teacher-negative gap signals exhibiting different noise profiles.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00172:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00172:end -->

<!-- books-review:SF-2026-ARXIV-2606-00183:start -->
<!-- existing:SF-2026-ARXIV-2606-00183:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：《Reinforcement Learning for Code Optimization》在 code timing 场景中系统化展示了这条 路径，并报告 naive timing reward 会被 noise、sparsity 与 GRPO instability 淹没。其具体 数据集、reward recipe 与收益仍是单篇预印本的实验结论；本章吸收的长期原则是： **verifiable reward 的测量系统也是被优化接口，必须与 policy 一起设计和审计。**<!-- existing:SF-2026-ARXIV-2606-00183:end -->
<!-- delta:SF-2026-ARXIV-2606-00183:start -->We study this question in a stochastic $k$-ary tree environment, where an agentic transformer observes only its trajectory history through interaction and receives a terminal reward for reaching a hidden leaf goal node. Changed constraint / result：We further show that, under imbalanced goal distributions, discounting the return leads to a ranked DFS policy that prioritizes higher-probability branches.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00183:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00183:end -->

<!-- books-review:SF-2026-ARXIV-2606-00186:start -->
<!-- existing:SF-2026-ARXIV-2606-00186:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-SWE-CYCLE-BENCHMARKING-CODE-AGENTS-ACROSS-THE-COMPLETE-ISSUE-RESOLUTION-:start --> 把 issue localization、patch、test、review 与交付拆成孤立 benchmark，会让下游成功掩盖上游 handoff failure。 Full-cycle evaluation 应冻结 repository/environment identity，逐阶段保存 artifact 与 executable verifier receipt， 同时报告 isolated competence 与 end-to-end completion。它提高现实性，却扩大环境故障和 judge 误差；单机制研究 仍需要隔离阶段 baseline。有限 repository 与执行 judge 不构成通用软件工程自治证明。 <!-- semantic-body-binding:SF-SWE-CYCLE-BENCHMARKING-CODE-AGENTS-ACROSS-THE-COMPLETE-ISSUE-RESOLUTION-:end --><!-- existing:SF-2026-ARXIV-2606-00186:end -->
<!-- delta:SF-2026-ARXIV-2606-00186:start -->To facilitate this, we propose an automated framework for conducting comparative studies across human-only, LLM-only, and hybrid conditions. Changed constraint / result：By sharing lessons learned, we establish a foundation for empirical research on human and LLM-generated code for software security.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00186:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00186:end -->

<!-- books-review:SF-2026-ARXIV-2606-00189:start -->
<!-- existing:SF-2026-ARXIV-2606-00189:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：- `SF-2026-ARXIV-2606-21891` — primary `arXiv:2606.21891v1`；exact-v1 URL=`https://arxiv.org/html/2606.21891v1`；Method=`https://arxiv.org/html/2606.21891v1 — §4 ARTS; §4.1 Expanding a Search Tree with Agentic Reasoning`；Evaluation=`https://arxiv.org/html/2606.21891v1 — §6 Experiments and Analysis; Appendix I Additional Experimental Details`；Non-proof=`https://arxiv.org/html/2606.21891v1 — §7 Discussion — Limitations and Ethical Concerns`。 - `SF-2026-ARXIV-2606-21968` — primary `arXiv:2606.21968v1`；exact-v1 URL=`https://arxiv.org/html/2606.21968v1`；Method=`https://arxiv.org/html/2606.21968v1 — §3 Motivations: Understanding the Resolution–Contex<!-- existing:SF-2026-ARXIV-2606-00189:end -->
<!-- delta:SF-2026-ARXIV-2606-00189:start -->Automated design and optimization of agentic LLM-based systems leads to sophisticated systems that substantially improve result quality over off-the-shelf agentic patterns. Changed constraint / result：Automated design and optimization of agentic LLM-based systems leads to sophisticated systems that substantially improve result quality over off-the-shelf agentic patterns.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00189:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00189:end -->

<!-- books-review:SF-2026-ARXIV-2606-00198:start -->
<!-- existing:SF-2026-ARXIV-2606-00198:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text typed skill requirement + dependency graph → eligible agents by authorization and tool access → competence / cost / latency evidence by task slice → assign, verify, retry or escalate → update evidence without rewriting skill definition ```<!-- existing:SF-2026-ARXIV-2606-00198:end -->
<!-- delta:SF-2026-ARXIV-2606-00198:start -->Scoring with a rollout-replay protocol, we find consistent failure patterns on four environments and five frontier agents: (1) strong agents do not necessarily have strong budget-awareness, with correlation r=0.35. Changed constraint / result：Scoring with a rollout-replay protocol, we find consistent failure patterns on four environments and five frontier agents: (1) strong agents do not necessarily have strong budget-awareness, with correlation r=0.35.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00198:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00198:end -->

<!-- books-review:SF-2026-ARXIV-2606-00206:start -->
<!-- existing:SF-2026-ARXIV-2606-00206:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：固定 ISL/OSL microbenchmark 能隔离 kernel 与 runtime regression，但 Agent workload 会在多轮请求之间插入 tool think time、动态 prefix、短输出、长 Context 与 bursty phase。此时容量问题不再是“每秒生成多少 token”， 而是“在每个请求都满足 latency/speed SLO 时，可同时维持多少条 active trajectories”：<!-- existing:SF-2026-ARXIV-2606-00206:end -->
<!-- delta:SF-2026-ARXIV-2606-00206:start -->Across math, coding, and science QA, we find that aggressive PTQ reduces accuracy while increasing chain-of-thought (CoT) length. Changed constraint / result：Across math, coding, and science QA, we find that aggressive PTQ reduces accuracy while increasing chain-of-thought (CoT) length.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00206:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00206:end -->

<!-- books-review:SF-2026-ARXIV-2606-00229:start -->
<!-- existing:SF-2026-ARXIV-2606-00229:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Roadmap Intent:** 解释 VLM 到 VLA 的约束变化，以及 high-level reasoning、trajectory/action representation、real-time controller、sim-to-real 与 physical safety 如何形成闭环。<!-- existing:SF-2026-ARXIV-2606-00229:end -->
<!-- delta:SF-2026-ARXIV-2606-00229:start -->Based on this view, we propose Continuous Reasoning for Vision-Language-Action. Changed constraint / result：This suggests that reasoning in VLA is less about extra tokens than about a shareable, verifiable internal language for action.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00229:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00229:end -->

<!-- books-review:SF-2026-ARXIV-2606-00232:start -->
<!-- existing:SF-2026-ARXIV-2606-00232:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text Claim contract intended use / subject / population / failure taxonomy → Evidence production dataset / environment / execution / artifact / trajectory → Measurement inference scorer / rater / uncertainty / slices / provenance → Decision and feedback gate / shadow / canary / release / rollback / next-version input ```<!-- existing:SF-2026-ARXIV-2606-00232:end -->
<!-- delta:SF-2026-ARXIV-2606-00232:start -->We study fact-level repair for multimodal generation, where a fluent output may contain specific facts that are not supported by the input. Changed constraint / result：Experiments across four cross-modal paths, including image-to-text, image+text-to-text, audio-to-text, and video-to-text, show that TIGER reduces unsupported content while preserving task quality.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00232:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00232:end -->

<!-- books-review:SF-2026-ARXIV-2606-00251:start -->
<!-- existing:SF-2026-ARXIV-2606-00251:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台 **Stable Knowledge Node ID:** `PLATFORM-EVALUATION-SYSTEM` **Legacy Chapter:** Ch62 **Status:** Draft<!-- existing:SF-2026-ARXIV-2606-00251:end -->
<!-- delta:SF-2026-ARXIV-2606-00251:start -->Yet we show that modern large language models systematically lack this ability: across diverse model families and scales, they overestimate their competence and attempt queries they cannot solve. Changed constraint / result：Yet we show that modern large language models systematically lack this ability: across diverse model families and scales, they overestimate their competence and attempt queries they cannot solve.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00251:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00251:end -->

<!-- books-review:SF-2026-ARXIV-2606-00257:start -->
<!-- existing:SF-2026-ARXIV-2606-00257:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：Entropy controller 是与 credit assignment 正交的 actuator：固定 clipping 容易解释，dynamic threshold 可以 在特定 token/ratio regions 调整探索—收敛轨迹，却新增 phase、band、oscillation 和跨模型校准状态。以上机制 都只能在 hard outcome gate、独立 calibration 与完整 trajectory identity 之上使用；开放研究、不可逆 action 或 verifier 脆弱时，稀疏但可信的 terminal reward 仍优于密集而错误的 proxy。<!-- existing:SF-2026-ARXIV-2606-00257:end -->
<!-- delta:SF-2026-ARXIV-2606-00257:start -->We formalize this behavior and propose measuring it directly with concentration diagnostics such as weight Gini and effective-token ratio. Changed constraint / result：In a compact MATH/Qwen3-1.7B GRPO sweep, ARCA exhibits the predicted non-degenerate middle-regime credit distribution under matched rollout budgets and remains competitive with rank-matched baselines.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00257:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00257:end -->

<!-- books-review:SF-2026-ARXIV-2606-00267:start -->
<!-- existing:SF-2026-ARXIV-2606-00267:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：它把 world model 从 plausible video generator 进一步约束为 stochastic transition sampler。代价是更高采样成本、outcome 离散化误差、reference distribution 构造成本和 seed/runtime identity；有限样本下没有观察到某个 rare outcome，也不证明 它的概率为零。单次 deterministic transition test 在近确定性场景、smoke test 或预算很低时仍合理；只有环境固有随机性会 影响 planning/risk 时，distribution-level alignment 才成为发布条件。即使分布更接近 reference，也仍需 matched-budget policy evaluation 才能证明它改善决策。<!-- existing:SF-2026-ARXIV-2606-00267:end -->
<!-- delta:SF-2026-ARXIV-2606-00267:start -->To enable robust policy evaluation and improvement over WM imaginations, we propose StressDream, which steers imaginations toward high-impact yet plausible outcomes specified at inference time by optimizing the initial noise of diffusion-based WMs. Changed constraint / result：Video world models (WMs) have shown promise for policy evaluation and improvement by imagining realistic future observations conditioned on ego-robot actions.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00267:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00267:end -->

<!-- books-review:SF-2026-ARXIV-2606-00269:start -->
<!-- existing:SF-2026-ARXIV-2606-00269:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-2026-ARXIV-2607-13429:start --> VLA fine-tuning 可以把 action learning、冻结 teacher 的 representation anchoring，以及同一 observation 下的language-action alignment 分开优化，从而避免在保留语义先验和学习控制之间二选一。多目标权重失衡仍会抑制动作适应或保留无关语义，因此必须用 matched control 与 closed-loop outcome 验收。 <!-- semantic-body-binding:SF-2026-ARXIV-2607-13429:end --><!-- existing:SF-2026-ARXIV-2606-00269:end -->
<!-- delta:SF-2026-ARXIV-2606-00269:start -->We propose CTRL-STEER, a closed-loop framework that replaces static intervention strength with adaptive, time-varying control signals. Changed constraint / result：Experiments with a fine-tuned OpenVLA policy on four LIBERO task suites show that CTRL-STEER achieves more stable concept regulation and a better steering-task success trade-off than fixed-coefficient baselines, without modifying or retraining the base model.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00269:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00269:end -->

<!-- books-review:SF-2026-ARXIV-2606-00271:start -->
<!-- existing:SF-2026-ARXIV-2606-00271:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-RESCALED-ASYNCHRONOUS-SGD-OPTIMAL-DISTRIBUTED-OPTIMIZATION-UNDER-DATA-AN:start --> 异步 SGD 若按更新到达顺序直接应用，会让快 worker 在 heterogeneous data 下获得更大 objective 权重。Runtime 因此要记录 worker sampling probability、arrival frequency 和 intended global weighting，并对 update 做 rescale；否则系统优化已静默改写学习目标。Rescaling 可修正特定假设下的 bias，却增加方差并依赖频率估计；数据近同分布或同步成本可接受时，普通同步聚合仍更稳定。 <!-- semantic-body-binding:SF-RESCALED-ASYNCHRONOUS-SGD-OPTIMAL-DISTRIBUTED-OPTIMIZATION-UNDER-DATA-AN:end --><!-- existing:SF-2026-ARXIV-2606-00271:end -->
<!-- delta:SF-2026-ARXIV-2606-00271:start -->To address this limitation, we propose \textbf{HeLoCo}, a direction-aware correction method for asynchronous low-communication training that uses outer momentum as a reference for the current optimization trajectory and selectively adjusts incoming pseudo-gradients before the outer update. Changed constraint / result：As a result, these updates can become misaligned with the current global optimization direction, particularly in heterogeneous systems.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00271:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00271:end -->

<!-- books-review:SF-2026-ARXIV-2606-00279:start -->
<!-- existing:SF-2026-ARXIV-2606-00279:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2606-00279:end -->
<!-- delta:SF-2026-ARXIV-2606-00279:start -->We demonstrate that such bitwise-precise re-computation does not require access to identical hardware, via a software-only emulation of LLM inference across multiple NVIDIA GPU variants. Changed constraint / result：We demonstrate that such bitwise-precise re-computation does not require access to identical hardware, via a software-only emulation of LLM inference across multiple NVIDIA GPU variants.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00279:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00279:end -->

<!-- books-review:SF-2026-ARXIV-2606-00284:start -->
<!-- existing:SF-2026-ARXIV-2606-00284:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Layer-wise / parameter-group multiplier。** Fine-tuning 中可以让靠近输入的 pretrained layers 使用较小 multiplier， 让新 task head 或上层更快适应；ULMFiT 的 discriminative fine-tuning 是这类思想的早期实例。它的理由是保留可迁移 表示并减轻 catastrophic forgetting，不是“低层梯度天然更容易爆炸”。在从零 Pretraining 中，不存在脱离架构和 数据的通用“越深 learning rate 越大/越小”规律。<!-- existing:SF-2026-ARXIV-2606-00284:end -->
<!-- delta:SF-2026-ARXIV-2606-00284:start -->We link this forgetting to parameter drift in multilingual CPT and present a suite of five layer-aware parameter alignment strategies: hard layer freezing, soft regularization, post-hoc weight reversion, and model merging. Changed constraint / result：We systematically compare our alignment strategies against two unregularized CPT baselines on benchmarks spanning 32 training languages from five language families, plus held-out languages, across four evaluation axes: perplexity, reading comprehension, physical reasoning, and translation.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00284:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00284:end -->

<!-- books-review:SF-2026-ARXIV-2606-00301:start -->
<!-- existing:SF-2026-ARXIV-2606-00301:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：这里的 `Errors` 必须声明语义。`transport_error_rate` 可以由状态码、timeout、OOM 和 dependency failure 直接聚合；`contract_failure_rate` 可以来自 schema validator 或 tool protocol；但 hallucination、instruction failure 与 business outcome 通常需要第 66 章定义的 scorer、抽样和延迟标签。一个请求可以同时是 `runtime_success = true` 和 `quality_success = false`。<!-- existing:SF-2026-ARXIV-2606-00301:end -->
<!-- delta:SF-2026-ARXIV-2606-00301:start -->In this work, we formulate hallucination detection as a mechanism-aware evidence aggregation problem, where diverse representation- and token-level signals must be interpreted under multiple latent explanations. Changed constraint / result：This design enables FLaG to capture heterogeneous hallucination patterns while remaining invariant to decision thresholds and evaluation metrics.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00301:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00301:end -->

<!-- books-review:SF-2026-ARXIV-2606-00305:start -->
<!-- existing:SF-2026-ARXIV-2606-00305:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：只按 token objective 区分 SFT、distillation 与 RL，容易忽略监督发生在哪个状态上。静态 SFT 在固定数据分布上学习；on-policy distillation 让当前 policy 先到达自己的状态，再接受 teacher signal；RL 则在 policy-induced states 上用 reward 改变访问概率。约束从“标签是否正确”变化为“训练是否覆盖部署时会到达的状态”，因此 rollout producer、policy revision、teacher/reward revision 与 staleness 必须共同进入 run identity。<!-- existing:SF-2026-ARXIV-2606-00305:end -->
<!-- delta:SF-2026-ARXIV-2606-00305:start -->We show that this "trajectory-sampled but token-learned" mechanism cannot reliably bridge student trajectories toward teacher trajectories. Changed constraint / result：We show that this "trajectory-sampled but token-learned" mechanism cannot reliably bridge student trajectories toward teacher trajectories.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00305:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00305:end -->

<!-- books-review:SF-2026-ARXIV-2606-00308:start -->
<!-- existing:SF-2026-ARXIV-2606-00308:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：这减少了为每个 sender/receiver pair 训练 adapter 的要求，也可能保留序列化前的连续信息；但它没有得到稳定的 跨版本协议。Sender message、receiver tokenizer/embedding、selected suffix、alignment rule、anchor coefficient 与 model revisions 必须共同构成 channel identity。连续 prefix 不可读、难以审计，恶意或漂移 state 还可能绕过文本 policy scan，因此只能作为 proposal / reasoning channel；authoritative facts、delegation、approval、commit 与完成 证据仍应落到 typed artifact 或 Workflow state。StateBridge 的四模型、两 family、顺序四 Agent 实验仅支持该 对齐机制在所列 QA/math/code contract 下可行；没有证明跨任意 architecture、长 workflow、安全 adversary 或模型 升级后仍兼容。文本消息在可解释、重放和治理优先时继续成立，训练 adapter 在固定高流量 model pair 上也仍可能 比每次闭式对齐更稳定。<!-- existing:SF-2026-ARXIV-2606-00308:end -->
<!-- delta:SF-2026-ARXIV-2606-00308:start -->Large-language-model code generation has shifted from single-shot prompting to multi-agent orchestrations - analyst, coder, tester, and debugger pipelines - and is evaluated almost exclusively on functional correctness. Changed constraint / result：Architectural elaboration in LLM code generation should therefore be justified by measured benefit on the dimensions that matter, not assumed.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00308:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00308:end -->

<!-- books-review:SF-2026-ARXIV-2606-00318:start -->
<!-- existing:SF-2026-ARXIV-2606-00318:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：- sensor pipeline 拥有 timestamped observations； - state estimator 拥有当前 calibrated belief； - VLA/world-action model 拥有 provisional proposal； - controller 拥有 action execution lease； - safety monitor 拥有 veto / emergency stop； - environment 拥有真实 outcome； - run log 拥有 observation-action-effect evidence。<!-- existing:SF-2026-ARXIV-2606-00318:end -->
<!-- delta:SF-2026-ARXIV-2606-00318:start -->We propose an update operator with two cooperating mechanisms: a per-class calibrated commit gate, and a per-event conflict-drop window that refuses to commit foundation-model claims contradicted by the geometric channel at the moment of the claim. Changed constraint / result：We evaluate on KITTI-360 and ScanNet, with an oracle geometric channel (panoptic ground truth) and an off-the-shelf online semantic segmenter (Mask2Former) to demonstrate real-world performance.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00318:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00318:end -->

<!-- books-review:SF-2026-ARXIV-2606-00329:start -->
<!-- existing:SF-2026-ARXIV-2606-00329:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Trade-off、failure、共存与回退。** 作者自评、单模型单 agent、单日采集且无 reconstitution control；几何诊断潜力没有被真实纵向 drift 证实。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。<!-- existing:SF-2026-ARXIV-2606-00329:end -->
<!-- delta:SF-2026-ARXIV-2606-00329:start -->We introduce Loopzero, a claim-bounded benchmark framework for testing whether recursive failures follow a directional telemetry pattern: rising gain (G), recursive persistence (p), and declining diversity ($δ$). Changed constraint / result：(2024) LLM training-loop trajectories are directionally consistent with the pattern; matched-FP evaluation in that domain is deferred.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00329:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00329:end -->

<!-- books-review:SF-2026-ARXIV-2606-00341:start -->
<!-- existing:SF-2026-ARXIV-2606-00341:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：按 repository 或 CVE 精确字符串修复，在实现独立、复用少时成本最低；AI infrastructure 常复制相似 loader、conversion、serving 与 agent workflow，同一设计缺陷可能以不同 API、文件名和数据流重新出现。安全 owner 因而要保存 vulnerability 的 reference behavior、关键 data/control flow 与 affected preconditions，再在相关 repository lineage 中做 variant search；scanner 只产生候选，代码 owner 与可执行 test 才能确认修复。<!-- existing:SF-2026-ARXIV-2606-00341:end -->
<!-- delta:SF-2026-ARXIV-2606-00341:start -->Although much work has focused on agent safety in the presence of an adversary, we show that agents can exhibit misaligned behavior even in benign settings, taking unsafe actions when those actions are instrumental to task completion. Changed constraint / result：Although much work has focused on agent safety in the presence of an adversary, we show that agents can exhibit misaligned behavior even in benign settings, taking unsafe actions when those actions are instrumental to task completion.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00341:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00341:end -->

<!-- books-review:SF-2026-ARXIV-2606-00348:start -->
<!-- existing:SF-2026-ARXIV-2606-00348:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：联合预测可以减少无效 sweep，却新增 predictor calibration、价格漂移、failed-run attribution 与比较口径 不一致。任务稳定、可选路径少或 measurement 很便宜时，直接执行一个已验证方法仍更简单。作者在 11 个 NLP classification tasks、给定模型 roster 与 A100 条件下的结果只证明该 proposal path 可行，不证明生产 workload 或未来价格下仍能选中最优策略。<!-- existing:SF-2026-ARXIV-2606-00348:end -->
<!-- delta:SF-2026-ARXIV-2606-00348:start -->To address this critical gap, we propose Augur, a novel method to predict the energy consumption of scientific workflow tasks prior to execution. Changed constraint / result：By efficiently profiling both the available cluster infrastructure and the workflow at hand, Augur is capable of predicting the overall energy consumption of the workflow with a median prediction error of $16.3\pm15.3\%$ compared to Ichnos, an energy estimation method that uses fitted power models, and $18.2\pm14.7\%$ compared to Intel RAPL, as observed in our experimental evaluation on public and private cloud infrastructure.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00348:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00348:end -->

<!-- books-review:SF-2026-ARXIV-2606-00365:start -->
<!-- existing:SF-2026-ARXIV-2606-00365:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text static weight sparsity → input-dependent activation sparsity → shared addressable sparse representation → Decode: sparse matrix-vector path → Prefill: Tensor-Core sparse matrix-matrix path ```<!-- existing:SF-2026-ARXIV-2606-00365:end -->
<!-- delta:SF-2026-ARXIV-2606-00365:start -->Our proposal, SPARQLe, is a hardware-software co-design framework that exploits this sub-precision redundancy in any given quantized model. Changed constraint / result：SPARQLe demonstrates that sub-precision activation sparsity offers an effective and complementary pathway towards efficient LLM inference.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00365:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00365:end -->

<!-- books-review:SF-2026-ARXIV-2606-00376:start -->
<!-- existing:SF-2026-ARXIV-2606-00376:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：Toolformer 研究模型如何学习何时调用 API、传什么参数并利用结果；ReAct 展示 reasoning 与 environment actions 交替。它们证明一种能力路径，不证明任意调用都可靠或安全。<!-- existing:SF-2026-ARXIV-2606-00376:end -->
<!-- delta:SF-2026-ARXIV-2606-00376:start -->Extended chain-of-thought reasoning can degrade performance on deterministic state-tracking tasks, not solely because of preference biases but, on the evidence we present, because of information-theoretic limits in the capacity of decoder-only attention. Changed constraint / result：Fine-tuning on optimal-length traces yields $<$3 percentage-point improvement, supporting an architectural ceiling.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00376:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00376:end -->

<!-- books-review:SF-2026-ARXIV-2606-00380:start -->
<!-- existing:SF-2026-ARXIV-2606-00380:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:start --> Judge 给出的理由不能仅因与标签一致就当作 faithful evidence。Blind、Truth、Flip、Placebo 与 Reveal-after 等 cue intervention 可分离 outcome anchoring、rationale anchoring 与 explanation drift；evaluation owner 保存 intervention identity 和 tie-aware metrics，ranking 只消费已校准结果。新增成本是多臂实验和 cue-specific 外推边界；它能发现 rationalization bias，不证明隐藏推理或真实因果链已被恢复。 <!-- semantic-body-binding:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:end --><!-- existing:SF-2026-ARXIV-2606-00380:end -->
<!-- delta:SF-2026-ARXIV-2606-00380:start -->We introduce SUPREME, an open-source framework that distributes these stages across multiple GPUs. Changed constraint / result：Evaluating an unlearning method requires repeating training, unlearning, and evaluation across multiple seeds, which is computationally expensive.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00380:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00380:end -->

<!-- books-review:SF-2026-ARXIV-2606-00382:start -->
<!-- existing:SF-2026-ARXIV-2606-00382:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：第 35 章会说明：若 checkpoint 只保存 `theta` 而不保存 optimizer、scheduler、random state 和 data cursor，通常只能继续做新的 fine-tuning，不能精确恢复原 Pretraining trajectory。<!-- existing:SF-2026-ARXIV-2606-00382:end -->
<!-- delta:SF-2026-ARXIV-2606-00382:start -->We introduce CRMA (Constrained Residual Mixing Adapter), a residual adapter whose internal mixing matrix M is doubly-stochastic at every forward pass via Sinkhorn normalization, so by Birkhoff's theorem ||M||_2 <= 1 holds by construction -- a structural bound, not a penalty. Changed constraint / result：Three independent experimental setups (Mistral-7B 4-domain controlled ablation, TinyLlama 3-domain contamination-controlled replication, Mistral-7B cross-domain probes at 7B) all show positive backward transfer -- without replay buffers, without growing per-task memory, and without distillation.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00382:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00382:end -->

<!-- books-review:SF-2026-ARXIV-2606-00392:start -->
<!-- existing:SF-2026-ARXIV-2606-00392:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text untrusted text → policy/version-bound detector → candidate spans + classes + confidence → local policy decision → mask / remove / pseudonymize / review → audit and downstream minimization ```<!-- existing:SF-2026-ARXIV-2606-00392:end -->
<!-- delta:SF-2026-ARXIV-2606-00392:start -->We propose Detector Evasion Policy Optimization (DEPO), a Lagrangian primal-dual reinforcement learning algorithm with a novel GRPO-style group-based policy update. Changed constraint / result：Experiments on MAGE, M4, RAID, and peer-review datasets, evaluated against MAGE, RoBERTa, RADAR, Binoculars, and Fast-DetectGPT detectors, show that DEPO achieves strong detector evasion while precisely satisfying the semantic preservation constraint.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00392:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00392:end -->

<!-- books-review:SF-2026-ARXIV-2606-00395:start -->
<!-- existing:SF-2026-ARXIV-2606-00395:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：在昂贵 serving stack 上直接搜索配置、routing、KV 或 autoscaling policy，证据最真实却很难穷举；纯 analytical capacity model 便宜，但看不到 scheduler、queue 与 transfer 的状态交互。中间层可以使用 calibrated discrete-event digital twin：<!-- existing:SF-2026-ARXIV-2606-00395:end -->
<!-- delta:SF-2026-ARXIV-2606-00395:start -->To address this limitation, we propose Predictive Routing Replay (PR2), which augments each router with a lightweight evolution predictor that learns to anticipate short-horizon router evolution. Changed constraint / result：Theoretical analysis and experiments support that PR2 reduces routing-induced mismatch, improves RL stability, and yields stronger performance across various reasoning benchmarks.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00395:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00395:end -->

<!-- books-review:SF-2026-ARXIV-2606-00400:start -->
<!-- existing:SF-2026-ARXIV-2606-00400:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：Pretraining 已经让模型能够续写文本，为什么它仍可能不遵循指令、模仿错误角色或输出不合适的格式？Supervised Fine-Tuning 怎样用 demonstrations 改变条件分布？为什么 SFT 仍然使用 cross-entropy，却能显著改变模型行为？<!-- existing:SF-2026-ARXIV-2606-00400:end -->
<!-- delta:SF-2026-ARXIV-2606-00400:start -->We propose PROX-YMIX, a framework that learns a dynamic replay controller on a small proxy model and transfers the frozen controller to a larger target. Changed constraint / result：The framework is leakage free and architecture independent at the interface level, and we also identify settings where the proxy assumption breaks down, highlighting limitations for robust deployment.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00400:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00400:end -->

<!-- books-review:SF-2026-ARXIV-2606-00408:start -->
<!-- existing:SF-2026-ARXIV-2606-00408:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-SWE-CYCLE-BENCHMARKING-CODE-AGENTS-ACROSS-THE-COMPLETE-ISSUE-RESOLUTION-:start --> 把 issue localization、patch、test、review 与交付拆成孤立 benchmark，会让下游成功掩盖上游 handoff failure。 Full-cycle evaluation 应冻结 repository/environment identity，逐阶段保存 artifact 与 executable verifier receipt， 同时报告 isolated competence 与 end-to-end completion。它提高现实性，却扩大环境故障和 judge 误差；单机制研究 仍需要隔离阶段 baseline。有限 repository 与执行 judge 不构成通用软件工程自治证明。 <!-- semantic-body-binding:SF-SWE-CYCLE-BENCHMARKING-CODE-AGENTS-ACROSS-THE-COMPLETE-ISSUE-RESOLUTION-:end --><!-- existing:SF-2026-ARXIV-2606-00408:end -->
<!-- delta:SF-2026-ARXIV-2606-00408:start -->We study observation masking through a systematic sweep over various agent backbones (4B to 284B parameters) and three retrievers on offline and live-web agentic search benchmarks. Changed constraint / result：We find that the accuracy gain from masking follows an asymmetric inverted-U shape when plotted against the model's accuracy without context management: a plateau under weak retrievers, a peak when a strong retriever meets a mid-capacity model, and a sharp collapse when the model is saturated.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00408:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00408:end -->

<!-- books-review:SF-2026-ARXIV-2606-00414:start -->
<!-- existing:SF-2026-ARXIV-2606-00414:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text versioned resource vector + calibrated hardware profile → optimistic / no-overlap lower bounds → first binding wall and impossible-SLO rejection → observed steady-state service time / floor residual → profiler only for material unexplained residual → final silicon replay and tail-SLO validation ```<!-- existing:SF-2026-ARXIV-2606-00414:end -->
<!-- delta:SF-2026-ARXIV-2606-00414:start -->Because occupancy measures identify behavior only up to occupancy equivalence, we formulate auditing at the occupancy-class level and distinguish exact local-query oracles from noisy sample-query oracles. Changed constraint / result：Our main exact-query result is conditional: if the audited class contains a $2/H$-separated near-optimal packing whose local signatures are $b$-sparse, then exact local-query auditing requires $Ω(M/b)$ queries; when the packing realizes deployment-class capacity and $b=O(1)$, this becomes $Ω(2^{\Hopt^\cF(\eps)})$.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00414:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00414:end -->

<!-- books-review:SF-2026-ARXIV-2606-00424:start -->
<!-- existing:SF-2026-ARXIV-2606-00424:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：Judge 一旦进入 RL reward loop，评估分布就不再静止。离线 agreement 高，只说明 frozen candidate distribution 上近似某个 reference；训练中的 policy 会主动搜索 judge blind spot，形成 `policy -> judge reward -> policy shift` 的反馈回路。Reasoning、 更长 rubric 或 distillation 可以提高局部一致性，也可能把可利用模式训练得更稳定；它们不能替代目标规范和 adversarial robustness。<!-- existing:SF-2026-ARXIV-2606-00424:end -->
<!-- delta:SF-2026-ARXIV-2606-00424:start -->We study a more tractable form of weak supervision: using a weak model as a critic rather than as a labeler or judge. Changed constraint / result：We first show that weak critiques can improve frozen strong models at inference time, and that critique quality is key to this improvement.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00424:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00424:end -->

<!-- books-review:SF-2026-ARXIV-2606-00432:start -->
<!-- existing:SF-2026-ARXIV-2606-00432:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：| 层次 | 成功条件 | 典型失败 | | --- | --- | --- | | Transport / Runtime | 请求完成，模型和依赖没有显式异常 | timeout、OOM、tool transport error | | Contract | 输出满足 schema、stop、引用与协议约束 | JSON 无效、错误 tool arguments、流未正确终止 | | Semantic Quality | 内容正确、相关、grounded，并遵循 instruction | hallucination、错误推理、忽略 evidence | | Policy / Safety | 行为满足权限、安全、隐私与合规边界 | 越权动作、敏感数据泄漏、危险建议 | | Outcome | 用户或环境中的任务结果达到 intended use | 工单未解决、代码未通过、外部状态修改错误 |<!-- existing:SF-2026-ARXIV-2606-00432:end -->
<!-- delta:SF-2026-ARXIV-2606-00432:start -->We propose a novel training-free decoding framework, \emph{Grounded Decoding}, designed to improve factual consistency in RAG without modifying model parameters. Changed constraint / result：Experiments on ALCE, Natural Questions, and FActScore demonstrate consistent improvements in factual accuracy and citation quality over standard RAG and competitive decoding-time baselines, while maintaining fluency.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00432:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00432:end -->

<!-- books-review:SF-2026-ARXIV-2606-00437:start -->
<!-- existing:SF-2026-ARXIV-2606-00437:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text process contract + enabled affordances → typed action/tool trace → environment transition and receipts → process-compliance metrics → final outcome judgment ```<!-- existing:SF-2026-ARXIV-2606-00437:end -->
<!-- delta:SF-2026-ARXIV-2606-00437:start -->Such transformations can change how PRM scores relate to correctness signals, leading to different failure modes across models.To address this gap, we introduce \textbf{EST-PRM}, a stress-testing framework for dense process rewards. Changed constraint / result：Three mitigation strategies are evaluated, highlighting trade-offs between robustness coverage and false-positive rates.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00437:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00437:end -->

<!-- books-review:SF-2026-ARXIV-2606-00439:start -->
<!-- existing:SF-2026-ARXIV-2606-00439:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Roadmap Intent:** 区分 video generation、predictive environment model 与 causal/controllable world model，解释 action-conditioned transition、latent dynamics、imagination 和 persistent state 的演进。<!-- existing:SF-2026-ARXIV-2606-00439:end -->
<!-- delta:SF-2026-ARXIV-2606-00439:start -->We introduce a new class of probabilistic world models that support estimation of the probability of any visual variable, such as appearance and dynamics, conditioned on any other variables. Changed constraint / result：First, we demonstrate that our model captures the physical laws governing how objects move by generating multiple plausible future states of the world through sequential inference.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00439:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00439:end -->

<!-- books-review:SF-2026-ARXIV-2606-00448:start -->
<!-- existing:SF-2026-ARXIV-2606-00448:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-PROTEUS-A-SELF-EVOLVING-RED-TEAM-FOR-AGENT-SKILL-ECOSYSTEMS:start --> 一次性 payload 集只能测量已知攻击；当攻击者可以观察 audit 与 sandbox 结果并继续修改 Skill 时，安全对象变成 `skill revision -> audit feedback -> mutation -> verified side effect` 的跨轮搜索过程。Red-team runtime 应冻结 预算、环境、oracle、mutation lineage 和每轮 side-effect receipt，测量攻击是否在约束内逐步穿过审核，而不是把 最后一轮的成功率当作静态 detector recall。这样能暴露 adaptive leakage，却会增加执行成本，并可能把 audit 反馈本身变成攻击 oracle；生产 Gate 仍需隐藏不必要细节、限制重试与 mutation surface，并以确定性 postcondition 拥有最终判定。固定 Skill、低权限和无反馈分发场景下，静态 scan 加一次 sandbox run 仍是更便宜的基线。 <!-- semantic-body-binding:SF-PROTEUS-A-SELF-EVOLVING-RED-TEAM-FOR-AGENT-SKILL-ECOSYSTEMS:en<!-- existing:SF-2026-ARXIV-2606-00448:end -->
<!-- delta:SF-2026-ARXIV-2606-00448:start -->We study a core safety problem in agentic AI systems: whether individually safe skills can compose into unsafe installed skill sets. Changed constraint / result：We treat this raw rate as a recall-oriented scanner ceiling and calibrate it against human judgment: in a pattern-stratified audit, roughly one in five flagged pair-pattern hits survives as a real compositional risk (population-weighted validity 18.2%, our headline result), implying about 14K genuine risk memberships in a single registry that per-skill scanning misses by construction, since every pair is individually safe.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00448:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00448:end -->

<!-- books-review:SF-2026-ARXIV-2606-00457:start -->
<!-- existing:SF-2026-ARXIV-2606-00457:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：effective_rate = acquisition_or_cloud_rate + power/cooling/network/storage + operations and reserved-capacity effects ```<!-- existing:SF-2026-ARXIV-2606-00457:end -->
<!-- delta:SF-2026-ARXIV-2606-00457:start -->We also present a problem formulation for ComputeAmp and highlight a few algorithmic and operational challenges. Changed constraint / result：We also present a problem formulation for ComputeAmp and highlight a few algorithmic and operational challenges.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-00457:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-00457:end -->

<!-- books-review:SF-2026-ARXIV-2606-07595:start -->
<!-- existing:SF-2026-ARXIV-2606-07595:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:start --> 多轮对话中，后续生成可能在过期前提、未确认工具结果或已撤销事实上继续推导。Runtime verifier 可把可引用 claims、observation revision 与 unresolved contradictions 维护为有界 grounding state，在 continuation 前线性检查依赖是否仍成立。它能阻止部分 stale-premise propagation，却依赖抽取完整性，也不能证明新答案为真；未解析自然语言、开放世界事实或冲突无法消解时应 abstain、检索或人工升级。小规模场景结果不能外推为通用事实验证率。 <!-- semantic-body-binding:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:end --><!-- existing:SF-2026-ARXIV-2606-07595:end -->
<!-- delta:SF-2026-ARXIV-2606-07595:start -->We study a concrete failure mode in this setting: action-boundary propagation, where sensitive or unsafe visible text is copied from an image into downstream tool arguments. Changed constraint / result：We additionally provide a labeled-target oracle upper-bound diagnostic that localizes most failures at the tool boundary while leaving response-side leakage as residual risk.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-07595:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-07595:end -->

<!-- books-review:SF-2026-ARXIV-2606-07603:start -->
<!-- existing:SF-2026-ARXIV-2606-07603:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：这种分解避免把异质风险实验排成统一能力榜，也避免把“在已授权环境中可以执行”误写成“会自主获得权限”。Agent Reliability、ResearchGym 与 frontier-risk framework 为这些边界提供了 2026 年的受限证据；它们的作者分数、特定 judge 和环境结果不构成跨系统常数。<!-- existing:SF-2026-ARXIV-2606-07603:end -->
<!-- delta:SF-2026-ARXIV-2606-07603:start -->To address this issue, we propose MetaEvo, a two-stage framework for continual agent evolution that focuses on improving how the model learns from tasks experience, rather than solely on what it stores. Changed constraint / result：Experimental results on diverse reasoning benchmarks demonstrate that MetaEvo consistently outperforms strong baselines, maintains reliable improvement across iterations.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-07603:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-07603:end -->

<!-- books-review:SF-2026-ARXIV-2606-07616:start -->
<!-- existing:SF-2026-ARXIV-2606-07616:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：在昂贵 serving stack 上直接搜索配置、routing、KV 或 autoscaling policy，证据最真实却很难穷举；纯 analytical capacity model 便宜，但看不到 scheduler、queue 与 transfer 的状态交互。中间层可以使用 calibrated discrete-event digital twin：<!-- existing:SF-2026-ARXIV-2606-07616:end -->
<!-- delta:SF-2026-ARXIV-2606-07616:start -->To address this, we introduce Item Response Scaling Laws (IRSL), a unified framework that integrates Item Response Theory (IRT) within the scaling law framework. Changed constraint / result：Furthermore, we show that the estimated latent model abilities are generalizable, enabling accurate performance forecasting across benchmarks that share the same measurement objective.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-07616:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-07616:end -->

<!-- books-review:SF-2026-ARXIV-2606-20631:start -->
<!-- existing:SF-2026-ARXIV-2606-20631:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：Workspace 不是新的授权主体：credential 必须按 step 和 resource 缩小，policy revision、approval decision、文件 快照与外部副作用要回绑 AgentRun；resume 也不能重放已经发生的真实操作。长生命周期隔离提升 recovery、审计 和 least privilege，却新增镜像/secret rotation、policy skew、tenant escape、orphan cleanup 与成本回收问题。 短、只读、无副作用的任务仍适合轻量 sandbox。NVIDIA Secure Agent Workspace 只提供 reference-architecture 证据，不能作为其 alpha implementation 已具备生产多租户成熟度的证明。<!-- existing:SF-2026-ARXIV-2606-20631:end -->
<!-- delta:SF-2026-ARXIV-2606-20631:start -->Agent skills externalise reusable agent-facing behavioural knowledge and guidance as persistent artefacts that can be discovered, activated, and interpreted by LLM agents. Changed constraint / result：The resulting patterns and reference architecture provide a vocabulary and diagnostic frame for analysing skill-harnessing responsibilities across agent systems.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-20631:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-20631:end -->

<!-- books-review:SF-2026-ARXIV-2606-24893:start -->
<!-- existing:SF-2026-ARXIV-2606-24893:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text claim type + domain + generation language + model family / scale + estimator access contract → calibrated operating point for the deployment slice ```<!-- existing:SF-2026-ARXIV-2606-24893:end -->
<!-- delta:SF-2026-ARXIV-2606-24893:start -->To evaluate these key abilities of test-time continual learning agents, we introduce AgentOdyssey, a novel evaluation framework that procedurally generates open-ended text games with rich entities, world dynamics, and long-horizon tasks. Changed constraint / result：To evaluate these key abilities of test-time continual learning agents, we introduce AgentOdyssey, a novel evaluation framework that procedurally generates open-ended text games with rich entities, world dynamics, and long-horizon tasks.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-24893:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-24893:end -->

<!-- books-review:SF-2026-ARXIV-2606-28337:start -->
<!-- existing:SF-2026-ARXIV-2606-28337:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：为什么参数中的知识不足以支撑可更新、可引用的系统？RAG 是向量数据库加 Prompt，还是 retrieval 与 generation 的联合信息系统？为什么检索到正确文档仍可能回答错误？<!-- existing:SF-2026-ARXIV-2606-28337:end -->
<!-- delta:SF-2026-ARXIV-2606-28337:start -->This paper presents a controlled empirical study of RAG sensitivity, robustness, and stability across 56 experimental runs. Changed constraint / result：These findings suggest that RAG evaluation should include sensitivity, robustness, stability, and multi-stage failure analysis rather than relying only on final answer accuracy.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2606-28337:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2606-28337:end -->

<!-- books-review:SF-2026-ARXIV-2605-30711:start -->
<!-- existing:SF-2026-ARXIV-2605-30711:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start --> late-stage checkpoint 差异接近 evaluator noise 时，按单个平均分取最大值会选择偶然赢家。更稳健的 release decision 先用 pointwise floor 排除明显不合格，再做 listwise ranking 与 pairwise refinement，并把稳定性和评估不确定性写入 选择记录。它用更多 judge 调用换较低 selection variance；judge 相关偏差或分布漂移时必须回退独立任务测试和人工复核。 <!-- semantic-body-binding:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end --><!-- existing:SF-2026-ARXIV-2605-30711:end -->
<!-- delta:SF-2026-ARXIV-2605-30711:start -->We frame memory evolution as a novelty-detection problem and propose SAGE, a Spherical Adaptive Gate for memory Evolution that scores candidate facts with a von Mises-Fisher-based density estimator over memory embeddings and routes them with an adaptive threshold that tracks memory-store geometry. Changed constraint / result：The source code for our approach is accessible at https://github.com/swang1024/SAGE.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30711:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30711:end -->

<!-- books-review:SF-2026-ARXIV-2605-30712:start -->
<!-- existing:SF-2026-ARXIV-2605-30712:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text user/task state → query construction or decomposition → authorized candidate retrieval → hybrid fusion / filters → rerank → dedup/diversify → context packing → generation with citations ```<!-- existing:SF-2026-ARXIV-2605-30712:end -->
<!-- delta:SF-2026-ARXIV-2605-30712:start -->We propose ExpGraph, a model-agnostic experience learning framework that enables frozen and replaceable LLM executors to improve through external experience reuse without parameter updates. Changed constraint / result：Ablations show that graph-structured experience, utility-aware ranking, and adaptive retrieval jointly enable effective experience reuse across diverse tasks and executor models.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30712:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30712:end -->

<!-- books-review:SF-2026-ARXIV-2605-30723:start -->
<!-- existing:SF-2026-ARXIV-2605-30723:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text typed skill requirement + dependency graph → eligible agents by authorization and tool access → competence / cost / latency evidence by task slice → assign, verify, retry or escalate → update evidence without rewriting skill definition ```<!-- existing:SF-2026-ARXIV-2605-30723:end -->
<!-- delta:SF-2026-ARXIV-2605-30723:start -->However, our controlled experiments across multiple model scales show that skill effectiveness is strongly model-dependent: a skill that benefits one backbone can harm another. Changed constraint / result：However, our controlled experiments across multiple model scales show that skill effectiveness is strongly model-dependent: a skill that benefits one backbone can harm another.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30723:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30723:end -->

<!-- books-review:SF-2026-ARXIV-2605-30727:start -->
<!-- existing:SF-2026-ARXIV-2605-30727:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：OpenAI Privacy Filter 的 model card 明确把该模型限定为 data-minimization/redaction aid， 而非 anonymization 或 compliance guarantee。这一案例的长期结论是：**privacy filter 必须 绑定组织策略、目标分布、校准版本和人工升级路径**；默认阈值和作者 benchmark 不得外推为 任意 tenant、语言或高风险场景的安全保证。<!-- existing:SF-2026-ARXIV-2605-30727:end -->
<!-- delta:SF-2026-ARXIV-2605-30727:start -->We introduce MosaicLeaks, a benchmark of 1,001 multi-hop deep research tasks that chain private enterprise documents and a public web corpus, forcing agents to make external queries that depend on local information. Changed constraint / result：We find that models across families and sizes frequently leak at all three levels, that zero-shot privacy prompting reduces but does not eliminate leakage and that reinforcement learning for task performance alone worsens leakage.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30727:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30727:end -->

<!-- books-review:SF-2026-ARXIV-2605-30728:start -->
<!-- existing:SF-2026-ARXIV-2605-30728:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：这解释了为何每个固定代理都有自己的成立区间。按 token 均分在 compute-bound 区间合理，却可能把冷 experts 切到更多 GPUs，重复支付 weight-load 与 tile-padding 成本；按 activated-expert count 均分适合 memory-bound 小 batch，却可能把大量 token 留在单一 bottleneck；忽略 topology 的平衡表在多节点上还可能用跨节点 traffic 换取表面上的 GPU 均衡。<!-- existing:SF-2026-ARXIV-2605-30728:end -->
<!-- delta:SF-2026-ARXIV-2605-30728:start -->Based on our findings, we introduce Invariant Bit Packing (IBP), a novel lossless compression algorithm designed to minimize data transfer time for ML. Changed constraint / result：IBP achieves, on average, 74% faster GNN training, 180% faster DLRM embedding lookup, and 24% faster LLM inference.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30728:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30728:end -->

<!-- books-review:SF-2026-ARXIV-2605-30736:start -->
<!-- existing:SF-2026-ARXIV-2605-30736:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：Product policy 拥有 SLO 权重与不可违反的 fairness/security 约束；router 拥有短期 shadow-price state、history freshness 与 admission 决定；runtime 才拥有实际 batch/KV occupancy；Evidence Plane 必须对比 predicted 与 realized service、拒绝原因和 SLO 结果。价格是可解释的 congestion signal，不是资源真值，也不能越权修改 runtime state。<!-- existing:SF-2026-ARXIV-2605-30736:end -->
<!-- delta:SF-2026-ARXIV-2605-30736:start -->We present OrcaRouter, a production-oriented LLM router that combines a LinUCB-based contextual bandit over lexical and sentence-embedding features with a hybrid offline-online learning protocol. Changed constraint / result：At the time of our RouterArena submission (May 20, 2026), OrcaRouter-Adaptive ranked second on the public RouterArena leaderboard with an arena score of 72.08, achieving 75.54% accuracy at a cost of USD 1.00 per 1,000 queries.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30736:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30736:end -->

<!-- books-review:SF-2026-ARXIV-2605-30738:start -->
<!-- existing:SF-2026-ARXIV-2605-30738:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：评估 `model + prompt + context + retrieval + tools + policy` 的端到端结果。RAG 的 retrieval recall 与 answer groundedness、Tool Calling 的选择与执行结果，都属于这一层。<!-- existing:SF-2026-ARXIV-2605-30738:end -->
<!-- delta:SF-2026-ARXIV-2605-30738:start -->We present MAVEN (Modular Agentic Verification and Execution Network), a lightweight symbolic reasoning scaffold for structured decomposition, adaptive tool orchestration, and intermediate verification. Changed constraint / result：It also remains competitive with frontier proprietary baselines while using an open-weight backbone with an estimated cost ratio of roughly 1/10, suggesting that lightweight verification-centered scaffolds can strengthen compositional reasoning and motivate more process-aware evaluation of agents in the wild.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30738:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30738:end -->

<!-- books-review:SF-2026-ARXIV-2605-30753:start -->
<!-- existing:SF-2026-ARXIV-2605-30753:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：普通 masked diffusion 把位置从 mask 变成 token 后往往视为已解码；早期错误随后只能被其他位置条件化放大。 让已预测位置继续以 confidence-weighted token/mask 表示参与后续 denoising，可形成 provisional state，直到 block 稳定或达到阈值才 commit：<!-- existing:SF-2026-ARXIV-2605-30753:end -->
<!-- delta:SF-2026-ARXIV-2605-30753:start -->We cast diffusion decoding as a dynamic control problem and show that token-wise denoising trajectories provide the key signal for reliable control. Changed constraint / result：We cast diffusion decoding as a dynamic control problem and show that token-wise denoising trajectories provide the key signal for reliable control.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30753:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30753:end -->

<!-- books-review:SF-2026-ARXIV-2605-30757:start -->
<!-- existing:SF-2026-ARXIV-2605-30757:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text source trajectories → compressed procedural memory → planner retrieval / execution evidence → optional training update → new policy checkpoint ```<!-- existing:SF-2026-ARXIV-2605-30757:end -->
<!-- delta:SF-2026-ARXIV-2605-30757:start -->Chain-of-thought prompting and looped Transformers both give a fixed model more test-time computation, but they differ in what they remember. Changed constraint / result：Our main result shows that a compressed loop is limited by the size of its recurrent state.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30757:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30757:end -->

<!-- books-review:SF-2026-ARXIV-2605-30771:start -->
<!-- existing:SF-2026-ARXIV-2605-30771:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：这种压力测试更接近真实长期 Agent，却增加合成场景偏差、标注复杂度和 evaluator 不确定性。短 session 或单实体工作流仍可使用简单 recall；冲突无法可靠裁决时应返回多版本证据并请求确认。exact-v1 只在其构造的 multi-target interference tasks 与所测 memory-augmented agents 中支持结果，不证明开放环境或生产记忆系统的普遍失败率。<!-- existing:SF-2026-ARXIV-2605-30771:end -->
<!-- delta:SF-2026-ARXIV-2605-30771:start -->We present Eywa, a provenance-grounded memory architecture built around evidence before belief. Changed constraint / result：Full per-question artifacts, including questions, gold answers, model answers, retrieved context, and labels, are published at https://eywa.to/research.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30771:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30771:end -->

<!-- books-review:SF-2026-ARXIV-2605-30777:start -->
<!-- existing:SF-2026-ARXIV-2605-30777:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text data access and consent -> model-visible scientific context -> proposed protocol / code / experiment -> domain and safety review -> instrument or lab authorization -> bounded execution -> measurement, incident and disposal evidence ```<!-- existing:SF-2026-ARXIV-2605-30777:end -->
<!-- delta:SF-2026-ARXIV-2605-30777:start -->We present an incident-driven empirical study grounded in two complementary evidence streams. Changed constraint / result：Our findings show that coding-agent failures are often severe, with 326 of 547 incidents rated high or critical.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30777:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30777:end -->

<!-- books-review:SF-2026-ARXIV-2605-30785:start -->
<!-- existing:SF-2026-ARXIV-2605-30785:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part VII Agent：从回答问题到执行任务 **Stable Knowledge Node ID:** `AGENT-CONTEXT` **Legacy Chapter:** Ch71 **Status:** Draft<!-- existing:SF-2026-ARXIV-2605-30785:end -->
<!-- delta:SF-2026-ARXIV-2605-30785:start -->We introduce Adaptive Context Management (AdaCoM), which trains an external LLM to manage the context of a frozen agent through flexible modification actions and end-to-end reinforcement learning. Changed constraint / result：The learned strategies reveal a Fidelity-Reliability Trade-off: agents with higher vanilla ReAct performance benefit from higher-fidelity context preservation, whereas lower-performing agents require more aggressive compression to stay within a reliable reasoning regime.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30785:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30785:end -->

<!-- books-review:SF-2026-ARXIV-2605-30789:start -->
<!-- existing:SF-2026-ARXIV-2605-30789:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part IV Training System：模型能力如何产生 **Stable Knowledge Node ID:** `TRAIN-GRPO` **Legacy Chapter:** Ch29 **Status:** Draft<!-- existing:SF-2026-ARXIV-2605-30789:end -->
<!-- delta:SF-2026-ARXIV-2605-30789:start -->While GRPO relies on diverse rollouts, prevailing strategies primarily increase diversity by injecting more token-level randomness, which may introduce step-wise noise and lead to incoherent trajectories. Changed constraint / result：S2L-PO improves accuracy on diverse mathematical reasoning benchmarks (e.g., +8.8% on AIME 24 using a 1.7B explorer to guide the 8B model) while reducing rollout compute.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30789:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30789:end -->

<!-- books-review:SF-2026-ARXIV-2605-30790:start -->
<!-- existing:SF-2026-ARXIV-2605-30790:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：Index 应记录 source URI、content digest、version/time、tenant/ACL、parser/chunker 和 embedding model。Embedding vector 不是 source of truth。<!-- existing:SF-2026-ARXIV-2605-30790:end -->
<!-- delta:SF-2026-ARXIV-2605-30790:start -->We find that answer retention is the primary determinant of generator accuracy; notably, when retention is high, a representation's wording, structure, length, and query-dependence have limited effect. Changed constraint / result：We find that answer retention is the primary determinant of generator accuracy; notably, when retention is high, a representation's wording, structure, length, and query-dependence have limited effect.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30790:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30790:end -->

<!-- books-review:SF-2026-ARXIV-2605-30803:start -->
<!-- existing:SF-2026-ARXIV-2605-30803:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text workload trace / arrival and length distribution + cluster topology and hardware profile + runtime / scheduler / cache policy revision + operator latency and contention model + seed, warm-up, measurement window and SLO ```<!-- existing:SF-2026-ARXIV-2605-30803:end -->
<!-- delta:SF-2026-ARXIV-2605-30803:start -->We introduce PReMISE, a framework that, given pairwise human-preference data, (i) discovers a policy-level rubric set, and (ii) audits any rubric set under LLM-judge use along four axes: structural adequacy, reliability, preference fit, and adversarial robustness. Changed constraint / result：We contribute two audit-targeted repair operations: preference-rank selection raises judge accuracy on paired responses from $65.0\%$ to $68.6\%$, competitive with the strongest rubric-discovery baselines and leading on two of three judges in our cross-judge sweep; reliability-constrained refinement reduces the rate at which exploit responses receive high scores from $46.4\%$ to $36.0\%$ with little change in inter-judge agreement ($α{=}.531\to.519$).。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30803:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30803:end -->

<!-- books-review:SF-2026-ARXIV-2605-30807:start -->
<!-- existing:SF-2026-ARXIV-2605-30807:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：“A 比 B 安全”只有在 harness configuration 被固定时才是可复算声明。Evaluation owner 应保存模型端点、prompt/template、sampling、package、judge 与 metric 配置，并报告配置网格内的排序一致性和方差，而不是只给一个 pairwise number。收益是区分模型差异与 harness-induced reversal，代价是组合爆炸；覆盖不足时应把结论降为 configuration-conditional，而不是平均掩盖反转。exact-v1 只在论文的模型、benchmark、package envelope 与 SDI/CFR 等指标中观察到该现象，不能估计所有评测配置。<!-- source-family:SF-2026-ARXIV-2605-25492 --><!-- existing:SF-2026-ARXIV-2605-30807:end -->
<!-- delta:SF-2026-ARXIV-2605-30807:start -->In this paper, we propose a novel evaluation metric called reliability score based on conformal prediction, which measures the worst-case performance within the prediction set at a pre-specified confidence level. Changed constraint / result：In this paper, we propose a novel evaluation metric called reliability score based on conformal prediction, which measures the worst-case performance within the prediction set at a pre-specified confidence level.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30807:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30807:end -->

<!-- books-review:SF-2026-ARXIV-2605-30824:start -->
<!-- existing:SF-2026-ARXIV-2605-30824:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：- `SF-2026-ARXIV-2606-21891` — primary `arXiv:2606.21891v1`；exact-v1 URL=`https://arxiv.org/html/2606.21891v1`；Method=`https://arxiv.org/html/2606.21891v1 — §4 ARTS; §4.1 Expanding a Search Tree with Agentic Reasoning`；Evaluation=`https://arxiv.org/html/2606.21891v1 — §6 Experiments and Analysis; Appendix I Additional Experimental Details`；Non-proof=`https://arxiv.org/html/2606.21891v1 — §7 Discussion — Limitations and Ethical Concerns`。 - `SF-2026-ARXIV-2606-21968` — primary `arXiv:2606.21968v1`；exact-v1 URL=`https://arxiv.org/html/2606.21968v1`；Method=`https://arxiv.org/html/2606.21968v1 — §3 Motivations: Understanding the Resolution–Contex<!-- existing:SF-2026-ARXIV-2605-30824:end -->
<!-- delta:SF-2026-ARXIV-2605-30824:start -->Deep research tasks require LLMs to plan what to investigate, retrieve evidence, and synthesize long-form answers across multiple branches of inquiry. Changed constraint / result：Experiments show that DecomposeR-8B improves over strong comparable open baselines by 5.1-8.0 points on popular long-form benchmarks due to improved planning and answering capabilities.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30824:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30824:end -->

<!-- books-review:SF-2026-ARXIV-2605-30832:start -->
<!-- existing:SF-2026-ARXIV-2605-30832:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text serving subject = checkpoint and tokenizer + route / effort policy + reasoning token budget and stopping policy + tool and harness configuration ```<!-- existing:SF-2026-ARXIV-2605-30832:end -->
<!-- delta:SF-2026-ARXIV-2605-30832:start -->To address this, we demonstrate that inefficiency concentrates in high-probability segments with low marginal utility. Changed constraint / result：To address this, we demonstrate that inefficiency concentrates in high-probability segments with low marginal utility.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30832:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30832:end -->

<!-- books-review:SF-2026-ARXIV-2605-30833:start -->
<!-- existing:SF-2026-ARXIV-2605-30833:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：缓存 rollout 能复用昂贵采样并提高 trainer 利用率，在 policy 变化慢时是合理近似；长 horizon 或异步更新后，同一 buffer 同时包含 rollout drift 与 supervision drift，旧样本不再等价于当前 on-policy evidence。Runtime 因而要为样本绑定 behavior/teacher revision，并用 freshness score 决定接受、降权或丢弃，而不是只按到达顺序消费。<!-- existing:SF-2026-ARXIV-2605-30833:end -->
<!-- delta:SF-2026-ARXIV-2605-30833:start -->To mitigate SFD, we introduce \textbf{Lookahead Group Reward (\ours{})}. Changed constraint / result：Across six math and code benchmarks, \ours{} improves mean@8 by \textbf{2.57} points over OPD for a 7B student, with gains increasing in longer-generation and reaching +\textbf{4.92} points on AIME-26 at 39k tokens.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30833:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30833:end -->

<!-- books-review:SF-2026-ARXIV-2605-30834:start -->
<!-- existing:SF-2026-ARXIV-2605-30834:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：模型能识别物体、理解指令并生成动作 token，为什么还不等于机器人系统？VLA 是把 “A” 接到 VLM 后面，还是改变了训练与 runtime contract？大模型推理慢、控制频率高时如何分层？video generation 形成的动作想象能否直接执行？<!-- existing:SF-2026-ARXIV-2605-30834:end -->
<!-- delta:SF-2026-ARXIV-2605-30834:start -->In this paper, we propose \textbf{Hide-and-Seek}, a framework that formulates VLA failure detection as a coarsely supervised learning problem. Changed constraint / result：We evaluate Hide-and-Seek on LIBERO, VLABench, and a real-world robotic platform across three representative VLA policies: OpenVLA, $π_0$, and $π_{0.5}$.Our method achieves state-of-the-art multi-task failure detection performance with a practical accuracy--timeliness trade-off under conformal prediction, and generalizes well to both seen and unseen tasks.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30834:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30834:end -->

<!-- books-review:SF-2026-ARXIV-2605-30837:start -->
<!-- existing:SF-2026-ARXIV-2605-30837:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：Learned anonymization policy 进一步把 detector、rewrite 与 utility 放进一个经验优化回路：给定某类 attacker、 downstream task 和文本分布，选择删改哪些 span 以形成 privacy/utility Pareto。它可以比固定 redact rule 更适应 上下文，却不能提供 Differential Privacy 的跨攻击者数学保证。其 identity 至少包含 attacker model、utility metric、task/data distribution、rewrite policy、threshold 和 human escalation。Attacker、语言或用途变化后， 旧 operating point 可能失效；生成式 rewrite 还可能改变事实或制造新敏感线索。确定性规则在强格式、法规字段 或低延迟路径中继续成立。Adaptive Text Anonymization 的实验只支持其所测 contract，不应被写成 DP 或 compliance guarantee。<!-- existing:SF-2026-ARXIV-2605-30837:end -->
<!-- delta:SF-2026-ARXIV-2605-30837:start -->To evaluate this setting, we build SCOUT-450, a benchmark that captures the structurally complex, agent-facing injections that older prompt-injection sets under-represent. Changed constraint / result：SCOUT also transfers to three external benchmarks (BIPIA, IPI, and IHEval), improving the safety-utility frontier.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30837:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30837:end -->

<!-- books-review:SF-2026-ARXIV-2605-30838:start -->
<!-- existing:SF-2026-ARXIV-2605-30838:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：关键边界是最后一步：model verdict 是 policy-bound sensor，不是 authority。Gateway、tool executor 或 workflow 仍应执行确定性 deny/allow、最小权限和人工升级；policy artifact 也必须有 immutable version、owner、测试集、生效范围、rollback 与 cache key。静态 classifier 在规则稳定、低延迟或 高可预测性场景仍更合理。gpt-oss-safeguard 是该模式的 Research Preview 案例，其公开评测不能 证明开放权重 safeguard 在所有语言、攻击或本地微调后仍保持同一安全边界。<!-- existing:SF-2026-ARXIV-2605-30838:end -->
<!-- delta:SF-2026-ARXIV-2605-30838:start -->However, these capabilities introduce retrieval-induced safety degradation, as harmful intents may decompose into seemingly innocuous sub-queries that lead to unsafe outcomes. Changed constraint / result：Empirical results show that COMPASS achieves a favorable safety-utility trade-off while requiring substantially less training data.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30838:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30838:end -->

<!-- books-review:SF-2026-ARXIV-2605-30842:start -->
<!-- existing:SF-2026-ARXIV-2605-30842:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text T_max model/runtime accepted context length T_sys instructions and policies T_hist conversation history T_ret retrieved or memory content T_tool tool schemas and observations T_out reserved output budget ```<!-- existing:SF-2026-ARXIV-2605-30842:end -->
<!-- delta:SF-2026-ARXIV-2605-30842:start -->In this paper, we introduce CoMem, a novel framework that decouples memory management from the primary agent workflow, enabling these processes to execute in parallel. Changed constraint / result：Our extensive experimental results on SWE-Bench-Verified show that CoMem provides 1.4x latency improvements upon vanilla long-context solutions while preserving most of the performance.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30842:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30842:end -->

<!-- books-review:SF-2026-ARXIV-2605-30851:start -->
<!-- existing:SF-2026-ARXIV-2605-30851:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场 **Stable Knowledge Node ID:** `INFER-SPECULATIVE-DECODING` **Legacy Chapter:** Ch44 **Status:** Draft<!-- existing:SF-2026-ARXIV-2605-30851:end -->
<!-- delta:SF-2026-ARXIV-2605-30851:start -->Analyzing Dense FFNs, MoE FFNs, and Attention against an idle-compute baseline, we find that NFP is shaped not by memory-bound resource slack alone, but also by implementation-induced kernel-granularity slack. Changed constraint / result：Analyzing Dense FFNs, MoE FFNs, and Attention against an idle-compute baseline, we find that NFP is shaped not by memory-bound resource slack alone, but also by implementation-induced kernel-granularity slack.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30851:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30851:end -->

<!-- books-review:SF-2026-ARXIV-2605-30852:start -->
<!-- existing:SF-2026-ARXIV-2605-30852:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-PIPESD-AN-EFFICIENT-CLOUD-EDGE-COLLABORATIVE-PIPELINE-INFERENCE-FRAMEWOR:start --> Edge drafter 与 cloud target 若严格串行，会把网络 RTT 加到每个 verify cycle。Pipeline 可以让下一段 draft 与上一段 cloud verification 重叠，但每个 proposal 必须携带 prefix/target revision、sequence number 和 rollback frontier，网络乱序或拒绝时只提交连续已验证前缀。收益是隐藏 RTT，代价是 speculative state、带宽浪费和断连恢复；网络稳定、设备足够或隐私不允许上传时，本地 target/普通 speculative 仍更简单。作者结果只属于其 edge/cloud 拓扑与 workload。 <!-- semantic-body-binding:SF-PIPESD-AN-EFFICIENT-CLOUD-EDGE-COLLABORATIVE-PIPELINE-INFERENCE-FRAMEWOR:end --><!-- existing:SF-2026-ARXIV-2605-30852:end -->
<!-- delta:SF-2026-ARXIV-2605-30852:start -->We propose Speculative Pipeline Decoding (SPD), which partitions the target LLM into $n$ pipeline stages so that $n$ tokens of a single sequence advance in parallel. Changed constraint / result：Experiments show that SPD achieves higher theoretical and wall-clock speedup than EAGLE-3 at moderate pipeline width, while more aggressive widths still leave room for further gains.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30852:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30852:end -->

<!-- books-review:SF-2026-ARXIV-2605-30854:start -->
<!-- existing:SF-2026-ARXIV-2605-30854:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：从这些工作能稳定得到的结论是：在可采样多个候选、reward 可比较或验证的任务上， group-relative policy optimization 是一条有效工程路径；而 production reasoning model 往往 需要在 exploration、readability、general ability 与 safety 之间使用多阶段训练，而不是把某一 阶段绝对化。<!-- existing:SF-2026-ARXIV-2605-30854:end -->
<!-- delta:SF-2026-ARXIV-2605-30854:start -->We propose Safe Equilibrium Policy Optimization (\sepo{}), a training objective that augments expected payoff with explicit penalties for exploitability, collusion risk, and externality cost. Changed constraint / result：To support further research in strategic safety for agents, we release our \href{https://anonymous.4open.science/r/sepo-2668/README.md}{code} and SFT datasets.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30854:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30854:end -->

<!-- books-review:SF-2026-ARXIV-2605-30855:start -->
<!-- existing:SF-2026-ARXIV-2605-30855:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Roadmap Intent:** 区分 video generation、predictive environment model 与 causal/controllable world model，解释 action-conditioned transition、latent dynamics、imagination 和 persistent state 的演进。<!-- existing:SF-2026-ARXIV-2605-30855:end -->
<!-- delta:SF-2026-ARXIV-2605-30855:start -->To address these challenges, we present \textbf{Robust Dreamer}, a memory-augmented framework built around how to design 3D memory and how to use it robustly. Changed constraint / result：Experiments on ScanNet, DL3DV, and OmniWorldGame demonstrate state-of-the-art long-horizon performance.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30855:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30855:end -->

<!-- books-review:SF-2026-ARXIV-2605-30859:start -->
<!-- existing:SF-2026-ARXIV-2605-30859:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:start --> RL pipeline 常把 rollout engine 与 training forward 当作“同一 policy”，但 kernel、precision、sampling/logprob 实现的细小差异会让 importance ratio 和 advantage 归因偏离，即使 checkpoint 名称相同。Run identity 必须绑定两侧执行图、数值策略、tokenization 和 logprob contract，并用 zero-mismatch diagnostic 先隔离数值分歧，再讨论 stale policy 或算法。追求 bitwise 对齐会牺牲 kernel 自由和吞吐；允许误差则必须有界并监测累积。作者 collapse 结果只属于其配置，不说明所有 RL 失败都来自数值 mismatch。 <!-- semantic-body-binding:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:end --><!-- existing:SF-2026-ARXIV-2605-30859:end -->
<!-- delta:SF-2026-ARXIV-2605-30859:start -->To address this, we propose a novel paradigm of active distribution shaping to shape the rollout distribution towards conciseness and certainty, thereby fundamentally resolving tail-induced overheads. Changed constraint / result：Experiments demonstrate significant acceleration over state-of-the-art systems by up to 1.77x without compromising model performance.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30859:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30859:end -->

<!-- books-review:SF-2026-ARXIV-2605-30880:start -->
<!-- existing:SF-2026-ARXIV-2605-30880:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part III 多模态、生成与世界模型：从跨模态表示到物理行动 **Stable Knowledge Node ID:** `MULTIMODAL-WORLD-MODELS` **Legacy Chapter:** N/A **Status:** Draft<!-- existing:SF-2026-ARXIV-2605-30880:end -->
<!-- delta:SF-2026-ARXIV-2605-30880:start -->We introduce PatchWorld, a gradient-free framework that turns offline trajectories into executable Python world models through counterexample-guided code repair.Instead of predicting the next observation with a black-box model, PatchWorld induces symbolic belief-state programs whose action updates can be inspected, replayed, and locally patched. Changed constraint / result：We further find that a human-specified residual-memory bias improves surface observation fidelity but weakens agent decision-making utility.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30880:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30880:end -->

<!-- books-review:SF-2026-ARXIV-2605-30883:start -->
<!-- existing:SF-2026-ARXIV-2605-30883:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：形式证明的强度来自假设，而不是数学符号本身。Bounded active domain、identifier-renaming equivariance、有限 tool semantics 与可枚举 transition 一旦被 schema evolution、外部副作用、概率 policy 或无限对象打破，证明便不覆盖真实 系统。Formal Verification of Agentic Systems 提供这一受限分支的理论证据，不证明任意 LLM Agent 可验证；trace、 simulation、canary 与 incident evidence 因而继续存在。<!-- existing:SF-2026-ARXIV-2605-30883:end -->
<!-- delta:SF-2026-ARXIV-2605-30883:start -->In this paper, we propose TRACE, a practical agentic jailbreaking framework to further reveal the risks of this threat surface. Changed constraint / result：In this paper, we propose TRACE, a practical agentic jailbreaking framework to further reveal the risks of this threat surface.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30883:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30883:end -->

<!-- books-review:SF-2026-ARXIV-2605-30888:start -->
<!-- existing:SF-2026-ARXIV-2605-30888:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：SFT 可以模仿 demonstration，但现实中往往很难为每个 prompt 写出唯一“标准答案”。人类更容易判断两个回答哪个更好。怎样把这种相对偏好变成可训练信号？为什么需要 Reward Model、reference policy 和 KL constraint？RLHF 为什么是一条 pipeline，而不是 PPO 的同义词？<!-- existing:SF-2026-ARXIV-2605-30888:end -->
<!-- delta:SF-2026-ARXIV-2605-30888:start -->Therefore, we propose SAVE (Self-supervised reward model improvement via Value-Anchored On-policy feedback), a framework that grades on-policy responses as feedback by using the value function for on-policy RM training. Changed constraint / result：The effectiveness of SAVE for enhancing RM training is strongly validated through rigorous empirical evaluation across six diverse benchmarks.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30888:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30888:end -->

<!-- books-review:SF-2026-ARXIV-2605-30896:start -->
<!-- existing:SF-2026-ARXIV-2605-30896:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：- Reward mean/std 与 per-prompt group variance。 - All-equal reward group ratio。 - Positive/negative/zero advantage 比例。 - 每个 prompt 的有效 completions 数。 - Response length 与 reward correlation。 - Verifier failure/timeout rate。 - Rollout tokens per optimizer update。 - Policy lag 与 sample reuse epochs。 - Per-source policy sample share、support mismatch 与 cross-policy clipping fraction。 - Retokenization failure、near-zero capability denominator 与 source-age distribution。<!-- existing:SF-2026-ARXIV-2605-30896:end -->
<!-- delta:SF-2026-ARXIV-2605-30896:start -->We identify a fundamental failure mode in this setting termed "zero collapse." We show that stochastic exploration and gradient-based updates can cause policies to overshoot optimal high-reward regions and enter flat, zero-reward regimes. Changed constraint / result：We identify a fundamental failure mode in this setting termed "zero collapse." We show that stochastic exploration and gradient-based updates can cause policies to overshoot optimal high-reward regions and enter flat, zero-reward regimes.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30896:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30896:end -->

<!-- books-review:SF-2026-ARXIV-2605-30898:start -->
<!-- existing:SF-2026-ARXIV-2605-30898:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text admission control 请求是否可以进入，是否有 SLO 与 memory budget iteration scheduling 下一轮执行哪些 token work routing / placement 请求、KV 与 model workers 放在哪里 autoscaling 未来需要多少 workers 和哪类 capacity ```<!-- existing:SF-2026-ARXIV-2605-30898:end -->
<!-- delta:SF-2026-ARXIV-2605-30898:start -->However, this decoupled design introduces inherent limitations. Changed constraint / result：Evaluation shows that UniScale effectively exploits the synergy in the UIS space to deliver a fine-grained and consistently better quality-cost trade-off across diverse, dynamic inference scenarios.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30898:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30898:end -->

<!-- books-review:SF-2026-ARXIV-2605-30911:start -->
<!-- existing:SF-2026-ARXIV-2605-30911:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：先由独立 3D reconstruction pipeline 生成 mesh，再把结果作为多模态模型的只读输入，职责清楚且容易单独验证；当任务要求多轮理解、生成和局部编辑保持同一几何身份时，stateless sidecar 会丢失跨轮 mesh state。另一条分支把 3D primitives/mesh 表示纳入统一 token contract，并让 modality-specific experts 共享同一 identity 与 revision。<!-- existing:SF-2026-ARXIV-2605-30911:end -->
<!-- delta:SF-2026-ARXIV-2605-30911:start -->To investigate this, we factor the architecture design into three dimensions: Linguistic Foundation (LF), Visual Representation (VR), and Semantic Alignment (SA), and categorize hallucinations into Co-occurrence, Similarity, and previously overlooked Uncertainty types. Changed constraint / result：Experiments across 7 design aspects show that: 1) the widely emphasized scaling of model parameters has only limited impact on reducing all three types of hallucinations; 2) larger and better-trained language foundations can reduce co-occurrence hallucinations; 3) stronger visual encoders and higher resolutions mitigate similarity errors; 4) effective alignment strategies alleviate uncertainty hallucinations.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30911:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30911:end -->

<!-- books-review:SF-2026-ARXIV-2605-30917:start -->
<!-- existing:SF-2026-ARXIV-2605-30917:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：这保留了各类索引的 inductive bias，也让 operator failure 可归因；代价是 routing error、score calibration、 materialization cost 与跨源去重。Corpus 小且同质时单一 index 更简单。OmniRetrieval 只在其受限 heterogeneous KB 合同下证明统一 orchestration 的可行性；GrepSeek 则提醒 code/frozen corpus 可把 `rg/grep` pipeline 本身作为 typed retrieval program，并只并行 shard-independent transformations。它们都不证明 semantic retrieval 或 lexical search 可以普遍取代另一方。<!-- existing:SF-2026-ARXIV-2605-30917:end -->
<!-- delta:SF-2026-ARXIV-2605-30917:start -->To fill this missing serving regime, we present V-SPLADE, an inference-free sparse retriever for visual-document retrieval. Changed constraint / result：Code will be released soon at https://github.com/naver/v-splade.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30917:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30917:end -->

<!-- books-review:SF-2026-ARXIV-2605-30924:start -->
<!-- existing:SF-2026-ARXIV-2605-30924:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2605-30924:end -->
<!-- delta:SF-2026-ARXIV-2605-30924:start -->To address this, we propose EMBGuard, the first MLLM-based safety guardrail for embodied agents designed to decouple physical risk reasoning from agent policy. Changed constraint / result：We make the code, data, and models publicly available at https://github.com/dongwxxkchoi/EMBGuard。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30924:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30924:end -->

<!-- books-review:SF-2026-ARXIV-2605-30998:start -->
<!-- existing:SF-2026-ARXIV-2605-30998:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-FIVE-ATTACKS-ON-X402-AGENTIC-PAYMENT-PROTOCOL:start --> 支付协议把这条链再延伸到异步结算：HTTP 请求完成授权不等于链上付款已经 final，链上 receipt 也不必然与 原始 action、resource 和 response 唯一绑定。若授权、请求 digest、payer/payee、amount、nonce、expiry、 settlement status 与最终副作用分属不同组件，重放、错绑和“已服务未付款 / 已付款未服务”都会落在组件缝隙。 因此 payment executor 必须在 effect-time 验证同一 canonical action identity，并把 service outcome 与 settlement receipt 分别记录、最终 reconciliation。同步、低价值且由单一可信 provider 结算时，简单 request-local payment 仍可成立；跨链或外部 settlement 则以更高延迟、补偿状态和争议处理换取开放性。受限攻击实验只证明这些边界 可能被利用，不证明所有实现均存在同样漏洞。 <!-- semantic-body-binding:SF-FIVE-ATTACKS-ON-X402-AGENTIC-PAYMENT-PROTOCOL:end --><!-- existing:SF-2026-ARXIV-2605-30998:end -->
<!-- delta:SF-2026-ARXIV-2605-30998:start -->We propose per-flaw mitigations and a defense triple with provable guarantees, cutting per-call reasoning cost by 47% and inverting attacker leverage from 8.7$\times$ to 0.9$\times$ at only 2.8% overhead. Changed constraint / result：All findings have been disclosed.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-30998:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-30998:end -->

<!-- books-review:SF-2026-ARXIV-2605-31033:start -->
<!-- existing:SF-2026-ARXIV-2605-31033:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：固定最近窗口、关键帧或相似度检索假设“哪些历史重要”主要由人工规则决定。这个旧方案成本可控、容易解释， 在短片、静态主体和遮挡较少时仍合理；但 long-video generation 中，不同预测帧甚至不同 denoising timestep 需要的历史细节并不相同。于是 read policy 可以从固定 retrieval 演进为由当前 generation state 条件化的 query：<!-- existing:SF-2026-ARXIV-2605-31033:end -->
<!-- delta:SF-2026-ARXIV-2605-31033:start -->To address these limitations, we propose SlotMemory, an object-centric Key-Value memory mechanism for streaming video diffusion. Changed constraint / result：Our results demonstrate that structured semantic representation, rather than raw temporal capacity, is the essential primitive for persistent long-form video synthesis.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31033:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31033:end -->

<!-- books-review:SF-2026-ARXIV-2605-31042:start -->
<!-- existing:SF-2026-ARXIV-2605-31042:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：1. 为什么模型输出不能被视为可信主体？ 2. 签名与 provenance 分别证明什么、不证明什么？ 3. 模型 artifact 为什么可能执行恶意代码？ 4. Prompt injection 的真正权限边界应放在哪里？ 5. AI DoS 为什么不能只按 request rate 防护？ 6. NIST AI RMF 的持续闭环如何映射到平台？ 7. 为什么 example-level DP 与 user-level DP 不能互换？ 8. 为什么正确实现 DP-SGD 仍不足以证明端到端隐私合同正确？ 9. 为什么跨 turn、跨 modality 的安全评估必须保存完整 run state，而不能只留最终 ASR？ 10. CoT controllability、monitorability、faithfulness 与 outcome safety 为什么是四个不同命题？<!-- existing:SF-2026-ARXIV-2605-31042:end -->
<!-- delta:SF-2026-ARXIV-2605-31042:start -->To reveal this threat, we introduce ClawTrojan, a benchmark designed to identify multi-step trojan attacks in local agentic harnesses. Changed constraint / result：As a result, they can block a clear harmful action, but fail to detect the earlier write operation that plants the backdoor.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31042:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31042:end -->

<!-- books-review:SF-2026-ARXIV-2605-31058:start -->
<!-- existing:SF-2026-ARXIV-2605-31058:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：多模态 raw sample、codec token、frame/second 和 action trajectory 不能用一个未经定义的“token 数”混合计量。第23～26章拥有表示与行动语义；本章拥有这些样本怎样被选择、版本化、配比与送入优化。这个边界使 representation 研究不会寄居于 Data，也使 Data 不退化成文件清单。<!-- existing:SF-2026-ARXIV-2605-31058:end -->
<!-- delta:SF-2026-ARXIV-2605-31058:start -->To this end, we propose Atomic Decomposition and Recombination (ADR), a novel framework that generates verifiable code tasks via decomposition into atomic elements and controlled recombination, thereby enabling the generation of genuinely novel and challenging verifiable code tasks. Changed constraint / result：Experiments and analysis demonstrate that ADR achieves superior originality, difficulty, diversity, and test quality over existing baselines, and consistently delivers greater improvements in code ability across RLVR in diverse downstream domains, including algorithmic programming, tool usage, and data science.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31058:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31058:end -->

<!-- books-review:SF-2026-ARXIV-2605-31066:start -->
<!-- existing:SF-2026-ARXIV-2605-31066:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text explicit future rollout → joint future-and-action generation → direct policy with latent predictive interface ```<!-- existing:SF-2026-ARXIV-2605-31066:end -->
<!-- delta:SF-2026-ARXIV-2605-31066:start -->Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks. Changed constraint / result：Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31066:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31066:end -->

<!-- books-review:SF-2026-ARXIV-2605-31073:start -->
<!-- existing:SF-2026-ARXIV-2605-31073:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：MoE 还引入另一类与 availability 不同的安全边界：**routing 本身可能成为攻击面**。普通故障分析关心 expert overload、drop 或通信失败；主动输入优化则可能在输出仍流畅时，把 token 流量引向较少承担 safety behavior 的 expert path。于是安全回归不能只测最终 refusal rate，还要把 router revision、top-k policy、expert assignment distribution 与 safety slice 绑定，检测输入扰动下异常的 routing drift。<!-- existing:SF-2026-ARXIV-2605-31073:end -->
<!-- delta:SF-2026-ARXIV-2605-31073:start -->We propose ConsisGuard, a consistency-aware framework for reasoning-based LLM guardrails. Changed constraint / result：Experiments on prompt and response harmfulness detection benchmarks show that ConsisGuard improves detection performance while reducing policy execution failures.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31073:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31073:end -->

<!-- books-review:SF-2026-ARXIV-2605-31086:start -->
<!-- existing:SF-2026-ARXIV-2605-31086:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-SWE-CYCLE-BENCHMARKING-CODE-AGENTS-ACROSS-THE-COMPLETE-ISSUE-RESOLUTION-:start --> 把 issue localization、patch、test、review 与交付拆成孤立 benchmark，会让下游成功掩盖上游 handoff failure。 Full-cycle evaluation 应冻结 repository/environment identity，逐阶段保存 artifact 与 executable verifier receipt， 同时报告 isolated competence 与 end-to-end completion。它提高现实性，却扩大环境故障和 judge 误差；单机制研究 仍需要隔离阶段 baseline。有限 repository 与执行 judge 不构成通用软件工程自治证明。 <!-- semantic-body-binding:SF-SWE-CYCLE-BENCHMARKING-CODE-AGENTS-ACROSS-THE-COMPLETE-ISSUE-RESOLUTION-:end --><!-- existing:SF-2026-ARXIV-2605-31086:end -->
<!-- delta:SF-2026-ARXIV-2605-31086:start -->To address these limitations, we introduce RHELM (Realistic, Heterogeneous, and Evolving Long-term Memory). Changed constraint / result：Comprehensive experiments across full-context models, retrieval-augmented generation (RAG) methods, and representative memory frameworks reveal that contemporary approaches still expose critical weaknesses in complex, real-world settings, particularly in resolving multi-source aggregation and real-world contextual reasoning.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31086:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31086:end -->

<!-- books-review:SF-2026-ARXIV-2605-31105:start -->
<!-- existing:SF-2026-ARXIV-2605-31105:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-TRAINING-INFERENCE-CONSISTENT-SEGMENTED-EXECUTION-FOR-LONG-CONTEXT-LLMS:start --> 完整序列训练让每个位置可通过 autograd 连接全部历史，最容易定义目标；长 Context 推理却常按 segment 增量执行并 复用旧 KV。若训练只把 segmentation 当内存技巧、推理才改变 forward boundary，模型学到的依赖与 runtime 实际 可写状态会错位。一个受限替代是让两阶段共享 segment-level forward semantics：当前 segment 可以读取更早 KV， 但 gradient 只穿过声明的近邻 segment，较老状态作为只读 cache 消费。<!-- existing:SF-2026-ARXIV-2605-31105:end -->
<!-- delta:SF-2026-ARXIV-2605-31105:start -->To address this imbalance, we propose GRKV (Global Regression for KV Cache), a training-free KV-cache merging method that directly minimizes the discrepancy between compressed-cache and full-cache attention outputs. Changed constraint / result：Across the LongBench and RULER long-context benchmarks, GRKV is the only merging method that improves overall performance with minimal overhead.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31105:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31105:end -->

<!-- books-review:SF-2026-ARXIV-2605-31111:start -->
<!-- existing:SF-2026-ARXIV-2605-31111:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part III 多模态、生成与世界模型：从跨模态表示到物理行动 **Stable Knowledge Node ID:** `MULTIMODAL-WORLD-MODELS` **Legacy Chapter:** N/A **Status:** Draft<!-- existing:SF-2026-ARXIV-2605-31111:end -->
<!-- delta:SF-2026-ARXIV-2605-31111:start -->Joint-Embedding Predictive Architectures (JEPAs) learn compact latent world models by predicting future embeddings, but no single coordinate of the latent is designated to encode task progression. Changed constraint / result：Three quantitative tests back this up: $|Δθ_t|$ outperforms the standard latent-prediction-error surprise at localising semantic events on 40 held-out cube episodes by up to +0.18 pooled AUROC (97.5% per-episode win rate at $\pm 1$-step tolerance); a within-episode linear probe across all four environments (40 episodes per env) shows the 8-dimensional progression subspace (4.2% of the latent) explains 72-95% of task-progress variance..。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31111:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31111:end -->

<!-- books-review:SF-2026-ARXIV-2605-31158:start -->
<!-- existing:SF-2026-ARXIV-2605-31158:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part III 多模态、生成与世界模型：从跨模态表示到物理行动 **Stable Knowledge Node ID:** `MULTIMODAL-WORLD-MODELS` **Legacy Chapter:** N/A **Status:** Draft<!-- existing:SF-2026-ARXIV-2605-31158:end -->
<!-- delta:SF-2026-ARXIV-2605-31158:start -->We present Light Interaction, a training-free inference acceleration framework for interactive video world models. Changed constraint / result：Evaluated on HY-WorldPlay and Matrix-Game-3.0, Light Interaction achieves up to 2.59x speedup without model retraining while maintaining competitive visual quality.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31158:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31158:end -->

<!-- books-review:SF-2026-ARXIV-2605-31159:start -->
<!-- existing:SF-2026-ARXIV-2605-31159:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：缓存 rollout 能复用昂贵采样并提高 trainer 利用率，在 policy 变化慢时是合理近似；长 horizon 或异步更新后，同一 buffer 同时包含 rollout drift 与 supervision drift，旧样本不再等价于当前 on-policy evidence。Runtime 因而要为样本绑定 behavior/teacher revision，并用 freshness score 决定接受、降权或丢弃，而不是只按到达顺序消费。<!-- existing:SF-2026-ARXIV-2605-31159:end -->
<!-- delta:SF-2026-ARXIV-2605-31159:start -->We propose Trust-Region behavior Blending (TRB), a warmup method that replaces the early rollout policy with the closest-to-teacher behavior policy inside a student-centered KL trust region, while keeping the per-prefix reverse-KL OPD loss unchanged. Changed constraint / result：Across two math-reasoning distillation settings, TRB attains the strongest average among the compared methods.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31159:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31159:end -->

<!-- books-review:SF-2026-ARXIV-2605-31164:start -->
<!-- existing:SF-2026-ARXIV-2605-31164:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part IV Training System：模型能力如何产生 **Stable Knowledge Node ID:** `TRAIN-DATA` **Legacy Chapter:** Ch23 **Status:** Draft<!-- existing:SF-2026-ARXIV-2605-31164:end -->
<!-- delta:SF-2026-ARXIV-2605-31164:start -->In this work, we propose $D^3$, a Dynamic Directional graph-constrained Data scheduling framework. Changed constraint / result：For future research, the code is available at https://github.com/xuyj233/D3.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31164:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31164:end -->

<!-- books-review:SF-2026-ARXIV-2605-31167:start -->
<!-- existing:SF-2026-ARXIV-2605-31167:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：IAM/RBAC 定义 principal 能做什么，gateway 控制入口，tool-local validation 检查业务状态，sandbox 限制 capability；这些边界都继续成立。Agent 通过不同 protocol/framework、retry 和并发产生效果相同但语法不同 的 action 后，还需要一个位于真实副作用之前的共同 identity 与 authorization gate：<!-- existing:SF-2026-ARXIV-2605-31167:end -->
<!-- delta:SF-2026-ARXIV-2605-31167:start -->We introduce LLM-FACETS (LLM FActuality Cross-EvaluaTion System): an open-source framework with a browser-accessible interface and a plugin architecture, structured around three practitioner profiles (technical experts, domain experts, compliance officers) that mirror the stakeholder categories identified in the EU AI Act and the NIST AI Risk Management Framework. Changed constraint / result：Yet auditing LLMs remains inaccessible to non-technical practitioners: existing tools require programming expertise and non-trivial environment setup, and cloud-hosted platforms transmit evaluation data to external services, creating barriers for domain experts and compliance officers legally responsible for AI oversight.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31167:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31167:end -->

<!-- books-review:SF-2026-ARXIV-2605-31170:start -->
<!-- existing:SF-2026-ARXIV-2605-31170:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：这减少了为每个 sender/receiver pair 训练 adapter 的要求，也可能保留序列化前的连续信息；但它没有得到稳定的 跨版本协议。Sender message、receiver tokenizer/embedding、selected suffix、alignment rule、anchor coefficient 与 model revisions 必须共同构成 channel identity。连续 prefix 不可读、难以审计，恶意或漂移 state 还可能绕过文本 policy scan，因此只能作为 proposal / reasoning channel；authoritative facts、delegation、approval、commit 与完成 证据仍应落到 typed artifact 或 Workflow state。StateBridge 的四模型、两 family、顺序四 Agent 实验仅支持该 对齐机制在所列 QA/math/code contract 下可行；没有证明跨任意 architecture、长 workflow、安全 adversary 或模型 升级后仍兼容。文本消息在可解释、重放和治理优先时继续成立，训练 adapter 在固定高流量 model pair 上也仍可能 比每次闭式对齐更稳定。<!-- existing:SF-2026-ARXIV-2605-31170:end -->
<!-- delta:SF-2026-ARXIV-2605-31170:start -->Here, we study the emergent languages on Moltbook. Changed constraint / result：Our results show that posts proposing new languages for avoiding oversight are judged by DeepSeek-3.2 as being less aligned than the other categories and that all languages can be learned by other language models in-context merely from a description of the language.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31170:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31170:end -->

<!-- books-review:SF-2026-ARXIV-2605-31175:start -->
<!-- existing:SF-2026-ARXIV-2605-31175:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text source / executable specification → synthesize candidate task → sample current-policy rollouts → estimate correctness and group reward variance → retain, revise or retire by target difficulty zone → version task with generator / verifier / policy identity ```<!-- existing:SF-2026-ARXIV-2605-31175:end -->
<!-- delta:SF-2026-ARXIV-2605-31175:start -->Building on this insight, we formulate data selection as a problem of satisfying these directional constraints. Changed constraint / result：Extensive experiments across various model scales demonstrate that DiReCT consistently achieves state-of-the-art performance.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31175:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31175:end -->

<!-- books-review:SF-2026-ARXIV-2605-31176:start -->
<!-- existing:SF-2026-ARXIV-2605-31176:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：收益是隐藏部分 IO 延迟；代价是误预测流量、过期证据和更大的 cache/context 压力。预测置信不足、数据快速变化或高风险 claim 出现时，回退同步检索与重新验证。exact-v1 只覆盖其披露任务、预测器、retriever 和延迟/有用性指标，不证明开放对话、不同知识库或生产尾延迟中的普遍收益。<!-- existing:SF-2026-ARXIV-2605-31176:end -->
<!-- delta:SF-2026-ARXIV-2605-31176:start -->We propose a method that automatically selects a small, diverse subset of retrievers (a portfolio) from a large pool of candidates, to cover different regions of the target query distribution. Changed constraint / result：We formalize this setting via an expected best-of-$k$ objective over the query distribution and show that it admits an efficient portfolio construction algorithm with near-optimal guarantees.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31176:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31176:end -->

<!-- books-review:SF-2026-ARXIV-2605-31244:start -->
<!-- existing:SF-2026-ARXIV-2605-31244:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part I 世界观：AI 为什么会发展成今天这样 **Stable Knowledge Node ID:** `WORLDVIEW-SCALING-LAW` **Legacy Chapter:** Ch7 **Status:** Draft<!-- existing:SF-2026-ARXIV-2605-31244:end -->
<!-- delta:SF-2026-ARXIV-2605-31244:start -->To close this gap, we introduce "spectral position": a scalable measure of which eigenvalues of the empirical neural tangent kernel (eNTK) currently drive loss reduction. Changed constraint / result：Applying this measure to scaling experiments, we find that spectral position decreases throughout training: learning shifts from dominant eigenmodes into the spectral tail.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31244:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31244:end -->

<!-- books-review:SF-2026-ARXIV-2605-31264:start -->
<!-- existing:SF-2026-ARXIV-2605-31264:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：Hash lineage 证明来源和产物身份，不证明建议正确；deterministic compiler 减少格式漂移，也会稳定复制上游分类 错误。Notes2Skills 的作者实验只覆盖其 notebook corpora、directive checks 与少量 downstream sessions，支持 这条 provenance/authority boundary，不证明所有研究笔记都应自动变成 Skill。高风险或证据不足时，保留为 不可执行 knowledge artifact 仍是合理终点。<!-- existing:SF-2026-ARXIV-2605-31264:end -->
<!-- delta:SF-2026-ARXIV-2605-31264:start -->We present an automated trace-to-skill distillation system for generating person-grounded AI skills via expert knowledge distillation. Changed constraint / result：The system illustrates how person-grounded skills can be represented as portable, correctable packages rather than opaque prompts or hidden memories.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31264:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31264:end -->

<!-- books-review:SF-2026-ARXIV-2605-31278:start -->
<!-- existing:SF-2026-ARXIV-2605-31278:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：> 时效边界：本章描述长期稳定的评估对象与控制回路，不把某个 benchmark、judge model 或平台 API 当作 Evaluation 的定义。MLflow 的实现映射按 2026 年 7 月官方文档核验；其 classic ML 与 GenAI evaluation 接口仍在演进，生产使用必须锁定实际版本。<!-- existing:SF-2026-ARXIV-2605-31278:end -->
<!-- delta:SF-2026-ARXIV-2605-31278:start -->We introduce GLIDE, an open-source Python library that unifies state-of-the-art PPI estimators (PPI++, Stratified PPI, Predict-Then-Debias and its stratified variants, Active Statistical Inference) and samplers (uniform, stratified, active, cost-optimal) under a scipy-style API specialized to mean estimation. Changed constraint / result：Reliable evaluation of agentic systems requires unbiased estimates with valid uncertainty, but standard practice navigates between costly human annotation and biased LLM-as-judge proxies.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31278:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31278:end -->

<!-- books-review:SF-2026-ARXIV-2605-31308:start -->
<!-- existing:SF-2026-ARXIV-2605-31308:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start --> late-stage checkpoint 差异接近 evaluator noise 时，按单个平均分取最大值会选择偶然赢家。更稳健的 release decision 先用 pointwise floor 排除明显不合格，再做 listwise ranking 与 pairwise refinement，并把稳定性和评估不确定性写入 选择记录。它用更多 judge 调用换较低 selection variance；judge 相关偏差或分布漂移时必须回退独立任务测试和人工复核。 <!-- semantic-body-binding:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end --><!-- existing:SF-2026-ARXIV-2605-31308:end -->
<!-- delta:SF-2026-ARXIV-2605-31308:start -->We introduce TraceGraph, a graph-based framework that turns released multi-model agent trajectories into shared decision landscapes. Changed constraint / result：Agent benchmarks increasingly record rich interaction trajectories, yet evaluation often reduces each rollout to a pass rate or reward score.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31308:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31308:end -->

<!-- books-review:SF-2026-ARXIV-2605-31328:start -->
<!-- existing:SF-2026-ARXIV-2605-31328:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text dependency / developer endpoint compromise → credential and repository exposure → artifact and signature scope assessment → revoke / rotate / rebuild from trusted materials → forced client upgrade or deployment quarantine → post-incident provenance and residual-risk review ```<!-- existing:SF-2026-ARXIV-2605-31328:end -->
<!-- delta:SF-2026-ARXIV-2605-31328:start -->While EM has been extensively studied in the supervised fine-tuning (SFT) setting, evidence that it also arises from reinforcement learning (RL) is limited to large, closed-source models, leaving the phenomenon expensive to study and difficult to reproduce. Changed constraint / result：First, we show that rewarding narrow, overtly misaligned behavior produces substantially higher general-domain misalignment than sample-matched SFT.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31328:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31328:end -->

<!-- books-review:SF-2026-ARXIV-2605-31354:start -->
<!-- existing:SF-2026-ARXIV-2605-31354:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Trade-off、failure、共存与回退。** pairwise gamma 不能预测 multi-neighbor 结果且可反向排序；default agents 未自发 backfire，polarization 均为外部诱导，实验舆论任务不等于真实社会。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。<!-- existing:SF-2026-ARXIV-2605-31354:end -->
<!-- delta:SF-2026-ARXIV-2605-31354:start -->We study failure modes of collaborative reasoning with weak learners (4B--8B models) through the lens of noise accumulation. Changed constraint / result：Across multi-page, chart, and web-based benchmarks, we find a counter-intuitive degradation: naive shared workspaces often amplify hallucinations rather than resolve them.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31354:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31354:end -->

<!-- books-review:SF-2026-ARXIV-2605-31361:start -->
<!-- existing:SF-2026-ARXIV-2605-31361:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part III 多模态、生成与世界模型：从跨模态表示到物理行动 **Stable Knowledge Node ID:** `MULTIMODAL-WORLD-MODELS` **Legacy Chapter:** N/A **Status:** Draft<!-- existing:SF-2026-ARXIV-2605-31361:end -->
<!-- delta:SF-2026-ARXIV-2605-31361:start -->We propose a new perspective: treat teammates as structured, learnable components within the agent's world model. Changed constraint / result：We outline how this approach can support zero-shot and few-shot coordination in partially observable settings and propose a set of benchmarks and evaluation protocols to assess its impact.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31361:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31361:end -->

<!-- books-review:SF-2026-ARXIV-2605-31365:start -->
<!-- existing:SF-2026-ARXIV-2605-31365:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：这个 policy 只选择已批准 options，不能生成新权限或绕过 approval。它会引入 selection bias、cold-start、option catalog drift、错误 cost model 与 exploration risk；生产 query 缺少即时 ground truth 时，offline reward 也容易失真。 因此固定 workflow 在高风险、低流量或 option 差异不清楚时仍是默认分支。Adaptive configuration 只有在 hard mask、 safe fallback、shadow/canary、per-option evidence 和 tail/fairness guardrails 都存在时才是平台机制，而不是“让模型自己 挑最强架构”。<!-- existing:SF-2026-ARXIV-2605-31365:end -->
<!-- delta:SF-2026-ARXIV-2605-31365:start -->To address these challenges, we propose SCALE (Self-Cognitive-Aware Learning and Exploration), which leverages three adversarial roles, Selector, Predictor, and Judger to autonomously discover the agent's limitations and expand its cognitive boundaries through environmental exploration. Changed constraint / result：Experimental results show that our approach significantly improves the performance and generalization of multiple MLLMs in various web environments.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31365:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31365:end -->

<!-- books-review:SF-2026-ARXIV-2605-31381:start -->
<!-- existing:SF-2026-ARXIV-2605-31381:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：因此 reward judge 的验收应加入 policy-shifted red team、独立 holdout oracle、跨 judge transfer、artifact sampling 与停止条件， 并同时观察 training-judge reward 和外部 evidence。Examining Reasoning LLMs-as-Judges 的合成 preference 实验说明 reasoning judge 仍可被策略利用，且 reasoning compute 不能替代 distillation；它不证明所有 reasoning judge 更差，也不证明某公开排行榜失效。 规则、程序或 executable verifier 在可形式化域继续优先；开放域的 model judge 必须保留 disagreement、abstain 和人工升级，而 不能同时独占训练 reward 与 release authority。<!-- existing:SF-2026-ARXIV-2605-31381:end -->
<!-- delta:SF-2026-ARXIV-2605-31381:start -->We evaluate the consistency of automated judges in conducting a multi-dimensional safety evaluation in a reference-free setup. Changed constraint / result：We evaluate the consistency of automated judges in conducting a multi-dimensional safety evaluation in a reference-free setup.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31381:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31381:end -->

<!-- books-review:SF-2026-ARXIV-2605-31408:start -->
<!-- existing:SF-2026-ARXIV-2605-31408:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：- `SF-2026-ARXIV-2606-21869` — primary `arXiv:2606.21869v1`；exact-v1 URL=`https://arxiv.org/html/2606.21869v1`；Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`；Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`；Non-proof=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendations and downstream effects`。 - `SF-2026-ARXIV-2606-21954` — primary `arXiv:2606.21954v1`；exact-v1 URL=`https://arxiv.org/html/2606.<!-- existing:SF-2026-ARXIV-2605-31408:end -->
<!-- delta:SF-2026-ARXIV-2605-31408:start -->Skill documents provide procedural knowledge to large-language-model agents at inference time. Changed constraint / result：The experiment uses a pinned SkillsBench version, a 30-task domain-balanced subset validated by official oracle runs, two reasoning-enabled model configurations, six skill conditions, and five trials per task-condition-model cell.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31408:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31408:end -->

<!-- books-review:SF-2026-ARXIV-2605-31455:start -->
<!-- existing:SF-2026-ARXIV-2605-31455:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：```text SFT policy -> candidate rollouts -> preference pairs -> Reward Model -> reward - beta * KL -> PPO / GRPO policy optimization<!-- existing:SF-2026-ARXIV-2605-31455:end -->
<!-- delta:SF-2026-ARXIV-2605-31455:start -->To this end, we novelly propose DRIFT (Decoupled Rollouts and Importance-Weighted Fine-Tuning), a framework that operationalizes the theoretical insight that the KL-regularized RL objective is equivalent to importance-weighted supervised learning. Changed constraint / result：Empirically, we demonstrate that DRIFT matches or exceeds the performance of multi-turn reinforcement learning baselines while maintaining the training efficiency and simplicity of standard supervised fine-tuning.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31455:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31455:end -->

<!-- books-review:SF-2026-ARXIV-2605-31460:start -->
<!-- existing:SF-2026-ARXIV-2605-31460:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：1. 高层 goal/planning，可能以秒计； 2. action chunk 或 trajectory 更新，可能几十到数百毫秒； 3. torque/position control loop，通常更快且需要确定 deadline。<!-- existing:SF-2026-ARXIV-2605-31460:end -->
<!-- delta:SF-2026-ARXIV-2605-31460:start -->Based on this insight, we present REIS, a human cognition inspired robotic decision-making framework that minimizes unnecessary reasoning while preserving semantic adaptability. Changed constraint / result：Experiments on ALFRED, and real-world robotic tasks demonstrate that REIS significantly suppresses reasoning overhead while maintaining competitive task performance.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31460:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31460:end -->

<!-- books-review:SF-2026-ARXIV-2605-31463:start -->
<!-- existing:SF-2026-ARXIV-2605-31463:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Knowledge Tree:** Part IV Training System：模型能力如何产生 **Stable Knowledge Node ID:** `TRAIN-DISTRIBUTED-TRAINING` **Legacy Chapter:** Ch32 **Status:** Draft<!-- existing:SF-2026-ARXIV-2605-31463:end -->
<!-- delta:SF-2026-ARXIV-2605-31463:start -->Grounded in four agent-native design principles, we build PithTrain, a compact, agent-native MoE training framework. Changed constraint / result：Our evaluation shows PithTrain matches the throughput of production frameworks, and on ATE-Bench, PithTrain enables higher agent-task efficiency, with up to 62% fewer Agent Turns and 64% less Active GPU Time.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31463:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31463:end -->

<!-- books-review:SF-2026-ARXIV-2605-31464:start -->
<!-- existing:SF-2026-ARXIV-2605-31464:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：**Roadmap Intent:** 把模型语义转换为面向目标硬件的 execution plan、kernel、quantization 与 runtime。<!-- existing:SF-2026-ARXIV-2605-31464:end -->
<!-- delta:SF-2026-ARXIV-2605-31464:start -->To address this, we study how LLMs can serve as selective GPU surrogates for kernel evaluation, by forecasting the performance of proposed kernels. Changed constraint / result：While these measurements provide the ground-truth signal necessary for kernel search, they are costly, because each evaluation of a kernel requires compilation and repeated execution on a GPU.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31464:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31464:end -->

<!-- books-review:SF-2026-ARXIV-2605-31468:start -->
<!-- existing:SF-2026-ARXIV-2605-31468:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：Prompt 只携带当前决策需要的 schema 与 evidence；registry 拥有 tool/server revision，sandbox 拥有变量、process 和 filesystem state，Workflow 拥有 transition、budget、approval 与 side-effect record，Evaluation rubric 则是另一份版本化状态。Persistent interpreter 可以用代码保留循环和中间对象，减少 token 搬运，却把成本转成 process lifecycle、tenant/credential isolation、replay、resource leak 与 recovery。Lazy discovery 也可能漏召回或返回过期 schema。<!-- existing:SF-2026-ARXIV-2605-31468:end -->
<!-- delta:SF-2026-ARXIV-2605-31468:start -->As a result, we present AutoSci, a memory-centric agentic system for the full scientific research lifecycle. Changed constraint / result：As a result, we present AutoSci, a memory-centric agentic system for the full scientific research lifecycle.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31468:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31468:end -->

<!-- books-review:SF-2026-ARXIV-2605-31490:start -->
<!-- existing:SF-2026-ARXIV-2605-31490:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：训练系统还要维持 prompt、response、old log probabilities、reward、value、advantage、policy version 与 checkpoint 的一致性。Stale rollouts 会让 on-policy assumption 逐步失效。<!-- existing:SF-2026-ARXIV-2605-31490:end -->
<!-- delta:SF-2026-ARXIV-2605-31490:start -->Motivated by this insight, we propose two simple horizon-control strategies: Progressive OPD (POPD), which gradually expands the rollout horizon during training, and Truncated OPD (TOPD), which permanently performs distillation on reliable truncated rollouts. Changed constraint / result：Experiments on mathematical reasoning show that POPD improves the training efficiency of OPD by up to 3$\times$, while TOPD matches OPD performance using only 10\% of the rollout horizon, leading to substantial wall-clock and memory reductions.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31490:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31490:end -->

<!-- books-review:SF-2026-ARXIV-2605-31509:start -->
<!-- existing:SF-2026-ARXIV-2605-31509:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：把 skill 保存成 prompt 文件适合个人原型；进入平台后，skill owner 必须声明输入 schema、所需工具、可写状态、终止条件与验证回执，使 runtime 能 admission、版本化和回滚。收益是组合与治理，代价是 contract 维护和表达受限；一次性低风险任务仍可使用 prompt。<!-- source-family:SF-2026-ARXIV-2605-19604 --> exact-v1 §3 给出 programmable skill contract，§4–5 的实验不证明任意开放工具链都安全可组合。<!-- existing:SF-2026-ARXIV-2605-31509:end -->
<!-- delta:SF-2026-ARXIV-2605-31509:start -->To formalize this, we introduce ReuseRL, which grounds agentic RL in the Minimum Description Length (MDL) principle. Changed constraint / result：Across ALFWorld, TextWorld-Cooking, and Countdown-Stepwise, ReuseRL improves in- and out-of-distribution success over vanilla GRPO and strong round-length baselines.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31509:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31509:end -->

<!-- books-review:SF-2026-ARXIV-2605-31557:start -->
<!-- existing:SF-2026-ARXIV-2605-31557:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：只看最终准确率会把三种失败混在一起：目标事实从未进入 Memory、事实进入了但 revision / invalidation / conflict edge 在压缩中丢失，以及证据完整却没有完成组合推理。对长程状态任务，benchmark 应先由确定性的 typed case grammar 产生 authoritative provenance DAG 与每题 proof trace，再让语言模型只承担表面叙述；评估时分别报告 evidence coverage、dependency-edge preservation、reasoning correctness 与 outcome。<!-- existing:SF-2026-ARXIV-2605-31557:end -->
<!-- delta:SF-2026-ARXIV-2605-31557:start -->We introduce Egostream, a diagnostic benchmark for streaming episodic memory evaluation in egocentric vision. Changed constraint / result：We introduce Egostream, a diagnostic benchmark for streaming episodic memory evaluation in egocentric vision.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31557:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31557:end -->

<!-- books-review:SF-2026-ARXIV-2605-31584:start -->
<!-- existing:SF-2026-ARXIV-2605-31584:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- source-family:SF-TOWARDS-ROBUST-LLM-POST-TRAINING-AUTOMATIC-FAILURE-MANAGEMENT-FOR-REINFO --> <!-- source-family:SF-DATA-DEPENDENT-EXPLORATION-FOR-ONLINE-REINFORCEMENT-LEARNING-FROM-HUMAN- --> <!-- source-family:SF-EVERY-STEP-COUNTS-STEP-LEVEL-CREDIT-ASSIGNMENT-FOR-TOOL-INTEGRATED-TEXT- --> <!-- source-family:SF-RETHINKING-LOCAL-LEARNING-A-CHEAPER-AND-FASTER-RECIPE-FOR-LLM-POST-TRAIN --> <!-- source-family:SF-SELF-INDUCED-OUTCOME-POTENTIAL-TURN-LEVEL-CREDIT-ASSIGNMENT-FOR-AGENTS-W --><!-- existing:SF-2026-ARXIV-2605-31584:end -->
<!-- delta:SF-2026-ARXIV-2605-31584:start -->To address these issues, we introduce \textsc{LongTraceRL}. Changed constraint / result：Experiments on three reasoning LLMs (4B--30B) across five long-context benchmarks demonstrate that \textsc{LongTraceRL} consistently outperforms strong baselines and encourages comprehensive, evidence-grounded reasoning.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31584:end --> Decision=`No Change — Existing Coverage`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31584:end -->

<!-- books-review:SF-2026-ARXIV-2605-31593:start -->
<!-- existing:SF-2026-ARXIV-2605-31593:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：这种路径以在线 trace、跨 channel identity 与 attribution 误差换来 cascade 的更早定位；漏记边、共同上游或自适应通信会产生错误因果图，监控本身也可能成为额外延迟与隐私面。低风险、无共享状态或单 Agent 流程仍可使用局部 guard；证据不一致时应保留原 trace、隔离可疑传播并升级人工分析。`arXiv:2605.19240v1` 的 §4.1–4.4 与 §5 只支持其披露的 causal monitoring 与 detection/attribution evaluation，§7 明确其限制；它不证明开放拓扑中的因果完备性或生产阻断效果。<!-- existing:SF-2026-ARXIV-2605-31593:end -->
<!-- delta:SF-2026-ARXIV-2605-31593:start -->Language models can find thousands of severe software vulnerabilities, and agents are increasingly being misused for cyberattacks. Changed constraint / result：Language models can find thousands of severe software vulnerabilities, and agents are increasingly being misused for cyberattacks.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31593:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31593:end -->

<!-- books-review:SF-2026-ARXIV-2605-31598:start -->
<!-- existing:SF-2026-ARXIV-2605-31598:start -->已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：<!-- semantic-body-binding:SF-TRAINING-INFERENCE-CONSISTENT-SEGMENTED-EXECUTION-FOR-LONG-CONTEXT-LLMS:start --> 完整序列训练让每个位置可通过 autograd 连接全部历史，最容易定义目标；长 Context 推理却常按 segment 增量执行并 复用旧 KV。若训练只把 segmentation 当内存技巧、推理才改变 forward boundary，模型学到的依赖与 runtime 实际 可写状态会错位。一个受限替代是让两阶段共享 segment-level forward semantics：当前 segment 可以读取更早 KV， 但 gradient 只穿过声明的近邻 segment，较老状态作为只读 cache 消费。<!-- existing:SF-2026-ARXIV-2605-31598:end -->
<!-- delta:SF-2026-ARXIV-2605-31598:start -->We introduce StateKV, an inference-time method that adapts pretrained long-video VLMs to linear-time video prefill by carrying cross-frame context in a fixed-capacity, importance-based recurrent state, paired with a second full per-frame cache used for decoding. Changed constraint / result：These results suggest a practical step toward scalable long-video understanding.。只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。<!-- delta:SF-2026-ARXIV-2605-31598:end --> Decision=`Integrate`；本审计未修改 Books。
<!-- books-review:SF-2026-ARXIV-2605-31598:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260530-COVERAGE | fresh-context:may2026-day03 | coverage | coverage:SRC-ARXIV:20260530 | none | 730/730 replay；author 103→final 121；FP=0；FN=18；challenged-closure=10 | passed |
| SA-20260530-EVIDENCE | fresh-context:may2026-day03 | evidence | review:SF-2026-ARXIV-2606-00144 | none | final exact=121/121；ordinary pending=0；blocked=0 | passed |
| SA-20260530-SELECTION | fresh-context:may2026-day03 | deep_analysis_selection | analysis:DA-BIT-EXACT-INFERENCE-VERIFICATION | none | Top-3 只限制日报叙事；全部 denominator family 仍完成 exact-v1 review | passed |
| SA-20260530-BOOKS | fresh-context:may2026-day26-postwrite | books | books-review:SF-2026-ARXIV-2606-00160;review:SF-2026-ARXIV-2606-00329 | none | final 13/13 owner+adjacent、exact-v1 boundary、mechanism spine 与 placement 均通过；唯一 Weekly Only disposition 已逐 family 复核；ARCA 初审 finding 已修复并重审通过 | passed |

Post-write reviewer 未参与该日 author、pre-write challenge 或 13 项 Books 写回；审计期间未修改共享 Books。Cross-model challenge 因 delegated noninteractive context 记录为 skipped。

## 8. Ignored Noise

609 条逐 family pre-denominator closure 完整保存在 `screening-ledger-final.json`；每条保留具体问题/机制、排除边界和可重开条件。
## 9. Recommended Action

2026-05-30 全链已闭合；后续仅在 exact-v1 evidence 或 canonical owner 发生实质变化时重开对应 source family。
## 10. Repository Changes

- 重建 2026-05-30 independent screening/evidence/Books-comparison artifacts 与 canonical Daily。
- Fresh-context read-only Books challenge 将 canonical queue 从 29 收紧为 13：15 项 `No Change`、1 项 `Weekly Only`，并修正 3 个 canonical owner。
- Root 已按 final queue 写回 13 项共享 Books；独立 reviewer 完成 13/13 owner+adjacent post-write semantic audit，并生成 `post-write-semantic-audit.json`。
- Queue root/items、README Completion/Books Gate 与 unresolved findings 已同步为闭合状态；未 stage、commit 或 push。
## 11. Open Questions

- 无。post-write audit unresolved findings=0。


<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 12. Sources

- [BudgetDraft: Acceptance-Aware Multi-View Training for Sparse-KV Speculative Decoding](https://arxiv.org/html/2606.00144v1) — arXiv:2606.00144v1；first-public 2026-05-29；accessed 2026-09-01
- [Persona Attack: Incremental Memory Injection Jailbreak Attack against Large Language Models](https://arxiv.org/html/2606.00150v1) — arXiv:2606.00150v1；first-public 2026-05-29；accessed 2026-09-01
- [PrivacyPeek: Auditing What LLM-Based Agents Acquire, Not Just What They Say](https://arxiv.org/html/2606.00152v1) — arXiv:2606.00152v1；first-public 2026-05-29；accessed 2026-09-01
- [Modeling Robotics Dataset Construction as an Artifact-Based Build Process](https://arxiv.org/html/2606.00162v1) — arXiv:2606.00162v1；first-public 2026-05-29；accessed 2026-09-01
- [CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping for GRPO](https://arxiv.org/html/2606.00172v1) — arXiv:2606.00172v1；first-public 2026-05-29；accessed 2026-09-01
- [Agentic Transformers Provably Learn to Search via Reinforcement Learning](https://arxiv.org/html/2606.00183v1) — arXiv:2606.00183v1；first-public 2026-05-29；accessed 2026-09-01
- [Learning to Construct Practical Agentic Systems](https://arxiv.org/html/2606.00189v1) — arXiv:2606.00189v1；first-public 2026-05-29；accessed 2026-09-01
- [BAGEN: Are LLM Agents Budget-Aware?](https://arxiv.org/html/2606.00198v1) — arXiv:2606.00198v1；first-public 2026-05-29；accessed 2026-09-01
- [Quantized Reasoning Models Think They Need to Think Longer, but They Do Not](https://arxiv.org/html/2606.00206v1) — arXiv:2606.00206v1；first-public 2026-05-29；accessed 2026-09-01
- [Continuous Reasoning for Vision-Language-Action](https://arxiv.org/html/2606.00229v1) — arXiv:2606.00229v1；first-public 2026-05-29；accessed 2026-09-01
- [TIGER: Traceable Inference with Graph-Based Evidence Routing for Mitigating Hallucinations in Multimodal Generation](https://arxiv.org/html/2606.00232v1) — arXiv:2606.00232v1；first-public 2026-05-29；accessed 2026-09-01
- [Capability Self-Assessment: Teaching LLMs to Know Their Limits](https://arxiv.org/html/2606.00251v1) — arXiv:2606.00251v1；first-public 2026-05-29；accessed 2026-09-01
- [StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement](https://arxiv.org/html/2606.00267v1) — arXiv:2606.00267v1；first-public 2026-05-29；accessed 2026-09-01
- [Closed-Loop Neural Activation Control in Vision-Language-Action Models](https://arxiv.org/html/2606.00269v1) — arXiv:2606.00269v1；first-public 2026-05-29；accessed 2026-09-01
- [HeLoCo: Efficient asynchronous low-communication training under data and device heterogeneity](https://arxiv.org/html/2606.00271v1) — arXiv:2606.00271v1；first-public 2026-05-29；accessed 2026-09-01
- [Bit-Exact AI Inference Verification Without Performance Tradeoffs](https://arxiv.org/html/2606.00279v1) — arXiv:2606.00279v1；first-public 2026-05-29；accessed 2026-09-01
- [Bridging Reasoning Trajectories in On-Policy Distillation via Near-Future Guidance](https://arxiv.org/html/2606.00305v1) — arXiv:2606.00305v1；first-public 2026-05-29；accessed 2026-09-01
- [Belief Consistency Between Foundation-Model Evidence and Geometric Perception in Persistent Robotic Maps](https://arxiv.org/html/2606.00318v1) — arXiv:2606.00318v1；first-public 2026-05-29；accessed 2026-09-01
- [ROGUE: Misaligned Agent Behavior Arising from Ordinary Computer Use](https://arxiv.org/html/2606.00341v1) — arXiv:2606.00341v1；first-public 2026-05-29；accessed 2026-09-01
- [Augur: Pre-Execution Energy Prediction for Workflow Tasks in Heterogeneous Clusters](https://arxiv.org/html/2606.00348v1) — arXiv:2606.00348v1；first-public 2026-05-29；accessed 2026-09-01
- [SPARQLe: Sub-Precision Activation Representation for Quantized LLM Inference](https://arxiv.org/html/2606.00365v1) — arXiv:2606.00365v1；first-public 2026-05-29；accessed 2026-09-01
- [The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary](https://arxiv.org/html/2606.00376v1) — arXiv:2606.00376v1；first-public 2026-05-29；accessed 2026-09-01
- [SUPREME: A Multi-GPU Framework for Reproducible Image Unlearning Method Evaluation](https://arxiv.org/html/2606.00380v1) — arXiv:2606.00380v1；first-public 2026-05-29；accessed 2026-09-01
- [PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning](https://arxiv.org/html/2606.00395v1) — arXiv:2606.00395v1；first-public 2026-05-29；accessed 2026-09-01
- [Masking Stale Observations Helps Search Agents -- Until It Doesn't: A Regime Map and Its Mechanism](https://arxiv.org/html/2606.00408v1) — arXiv:2606.00408v1；first-public 2026-05-29；accessed 2026-09-01
- [Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight](https://arxiv.org/html/2606.00424v1) — arXiv:2606.00424v1；first-public 2026-05-29；accessed 2026-09-01
- [Grounded Decoding: Retrieval-Anchored Probability Fusion for Faithful RAG](https://arxiv.org/html/2606.00432v1) — arXiv:2606.00432v1；first-public 2026-05-29；accessed 2026-09-01
- [EST-PRM: Stress-Testing Process Reward Models Before They Become Load-Bearing](https://arxiv.org/html/2606.00437v1) — arXiv:2606.00437v1；first-public 2026-05-29；accessed 2026-09-01
- [Physical Object Understanding with a Physically Controllable World Model](https://arxiv.org/html/2606.00439v1) — arXiv:2606.00439v1；first-public 2026-05-29；accessed 2026-09-01
- [When Safe Skills Collide: Measuring Compositional Risk in Agent Skill Ecosystems](https://arxiv.org/html/2606.00448v1) — arXiv:2606.00448v1；first-public 2026-05-29；accessed 2026-09-01
- [Maximizing Compute Capacity in AI Data Centers through Cooling, Energy Storage, and Computing Adaptation](https://arxiv.org/html/2606.00457v1) — arXiv:2606.00457v1；first-public 2026-05-29；accessed 2026-09-01
- [MetaEvo: A Meta-Optimization Framework for Experience-Driven Agent Evolution](https://arxiv.org/html/2606.07603v1) — arXiv:2606.07603v1；first-public 2026-05-29；accessed 2026-09-01
- [Item Response Scaling Laws: A Measurement Theory Approach for Efficient and Generalizable Neural Scaling Estimation](https://arxiv.org/html/2606.07616v1) — arXiv:2606.07616v1；first-public 2026-05-29；accessed 2026-09-01
- [Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents](https://arxiv.org/html/2606.20631v1) — arXiv:2606.20631v1；first-public 2026-05-29；accessed 2026-09-01
- [SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs](https://arxiv.org/html/2605.30711v1) — arXiv:2605.30711v1；first-public 2026-05-29；accessed 2026-09-01
- [ExpGraph: Model-Agnostic Experience Learning with Graph-Structured Memory for LLM Agents](https://arxiv.org/html/2605.30712v1) — arXiv:2605.30712v1；first-public 2026-05-29；accessed 2026-09-01
- [Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents](https://arxiv.org/html/2605.30723v1) — arXiv:2605.30723v1；first-public 2026-05-29；accessed 2026-09-01
- [MosaicLeaks:Privacy Risks in Querying-in-the-Open for Deep Research Agents](https://arxiv.org/html/2605.30727v1) — arXiv:2605.30727v1；first-public 2026-05-29；accessed 2026-09-01
- [Reducing the GPU Memory Bottleneck with Lossless Compression for ML -- Extended](https://arxiv.org/html/2605.30728v1) — arXiv:2605.30728v1；first-public 2026-05-29；accessed 2026-09-01
- [OrcaRouter: A Production-Oriented LLM Router with Hybrid Offline-Online Learning](https://arxiv.org/html/2605.30736v1) — arXiv:2605.30736v1；first-public 2026-05-29；accessed 2026-09-01
- [MAVEN: Improving Generalization in Agentic Tool Calling](https://arxiv.org/html/2605.30738v1) — arXiv:2605.30738v1；first-public 2026-05-29；accessed 2026-09-01
- [Efficient Diffusion LLMs via Temporal-Spatial Parallel Decoding and Confidence Extrapolation](https://arxiv.org/html/2605.30753v1) — arXiv:2605.30753v1；first-public 2026-05-29；accessed 2026-09-01
- [Chain-of-Thought and Compressed Looped Transformers: A Memory-Budget Separation](https://arxiv.org/html/2605.30757v1) — arXiv:2605.30757v1；first-public 2026-05-29；accessed 2026-09-01
- [Eywa: Provenance-Grounded Long-Term Memory for AI Agents](https://arxiv.org/html/2605.30771v1) — arXiv:2605.30771v1；first-public 2026-05-29；accessed 2026-09-01
- [What Breaks When LLMs Code? Characterizing Operational Safety Failures of Agentic Code Assistants](https://arxiv.org/html/2605.30777v1) — arXiv:2605.30777v1；first-public 2026-05-29；accessed 2026-09-01
- [Learning Agent-Compatible Context Management for Long-Horizon Tasks](https://arxiv.org/html/2605.30785v1) — arXiv:2605.30785v1；first-public 2026-05-29；accessed 2026-09-01
- [PReMISE: Policy Rubrics as Measurement Specifications for LLM Judges](https://arxiv.org/html/2605.30803v1) — arXiv:2605.30803v1；first-public 2026-05-29；accessed 2026-09-01
- [Conformal Reliability: A New Evaluation Metric for Conditional Generation](https://arxiv.org/html/2605.30807v1) — arXiv:2605.30807v1；first-public 2026-05-29；accessed 2026-09-01
- [Planner-Centric Reinforcement Learning for Deep Research with Structure-Aware Reward](https://arxiv.org/html/2605.30824v1) — arXiv:2605.30824v1；first-public 2026-05-29；accessed 2026-09-01
- [SLAT: Segment-Level Adaptive Trimming for Efficient CoT Reasoning](https://arxiv.org/html/2605.30832v1) — arXiv:2605.30832v1；first-public 2026-05-29；accessed 2026-09-01
- [Your Teacher Can't Help You Here: Combating Supervision Fidelity Decay in On-Policy Distillation](https://arxiv.org/html/2605.30833v1) — arXiv:2605.30833v1；first-public 2026-05-29；accessed 2026-09-01
- [Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring](https://arxiv.org/html/2605.30834v1) — arXiv:2605.30834v1；first-public 2026-05-29；accessed 2026-09-01
- [Send a SCOUT First: Pre-hoc Reasoning for Adaptive Detector Allocation in Prompt-Injection Defense](https://arxiv.org/html/2605.30837v1) — arXiv:2605.30837v1；first-public 2026-05-29；accessed 2026-09-01
- [COMPASS: Cognitive MCTS-Guided Process Alignment for Safe Search Agents](https://arxiv.org/html/2605.30838v1) — arXiv:2605.30838v1；first-public 2026-05-29；accessed 2026-09-01
- [CoMem: Context Management with A Decoupled Long-Context Model](https://arxiv.org/html/2605.30842v1) — arXiv:2605.30842v1；first-public 2026-05-29；accessed 2026-09-01
- [How Much Parallelism Is "Free"? A Principle of Near-Free Parallelism for Parallel Decoding](https://arxiv.org/html/2605.30851v1) — arXiv:2605.30851v1；first-public 2026-05-29；accessed 2026-09-01
- [Speculative Pipeline Decoding: Higher-Accuracy Drafting with Hidden Latency via Pipeline Parallelism](https://arxiv.org/html/2605.30852v1) — arXiv:2605.30852v1；first-public 2026-05-29；accessed 2026-09-01
- [Safe Equilibrium Policy Optimization for Strategic Agent Policies](https://arxiv.org/html/2605.30854v1) — arXiv:2605.30854v1；first-public 2026-05-29；accessed 2026-09-01
- [Robust Dreamer: Deviation-Aware Latent Gaussian Memory for Action-Controlled AR Video Generation](https://arxiv.org/html/2605.30855v1) — arXiv:2605.30855v1；first-public 2026-05-29；accessed 2026-09-01
- [DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning](https://arxiv.org/html/2605.30859v1) — arXiv:2605.30859v1；first-public 2026-05-29；accessed 2026-09-01
- [PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments](https://arxiv.org/html/2605.30880v1) — arXiv:2605.30880v1；first-public 2026-05-29；accessed 2026-09-01
- [TRACE: Task-Aware Adaptive Self-Evolving Agentic Jailbreaking](https://arxiv.org/html/2605.30883v1) — arXiv:2605.30883v1；first-public 2026-05-29；accessed 2026-09-01
- [The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement](https://arxiv.org/html/2605.30888v1) — arXiv:2605.30888v1；first-public 2026-05-29；accessed 2026-09-01
- [Zero Collapse: A Failure Mode of Policy Gradient Methods in Discontinuous Reward Environments](https://arxiv.org/html/2605.30896v1) — arXiv:2605.30896v1；first-public 2026-05-29；accessed 2026-09-01
- [UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling](https://arxiv.org/html/2605.30898v1) — arXiv:2605.30898v1；first-public 2026-05-29；accessed 2026-09-01
- [What Makes LVLMs Hallucinate Less? Unveiling the Architectural Factors Behind Hallucination Robustness](https://arxiv.org/html/2605.30911v1) — arXiv:2605.30911v1；first-public 2026-05-29；accessed 2026-09-01
- [Inference-Free Multimodal Learned Sparse Retrieval for Production-Scale Visual Document Search](https://arxiv.org/html/2605.30917v1) — arXiv:2605.30917v1；first-public 2026-05-29；accessed 2026-09-01
- [EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents](https://arxiv.org/html/2605.30924v1) — arXiv:2605.30924v1；first-public 2026-05-29；accessed 2026-09-01
- [Free-Riding the Agentic Web: A Systematic Security Analysis of x402 Payments](https://arxiv.org/html/2605.30998v1) — arXiv:2605.30998v1；first-public 2026-05-29；accessed 2026-09-01
- [SlotMemory: Object-Centric KV Memory for Streaming Long-Video Generation](https://arxiv.org/html/2605.31033v1) — arXiv:2605.31033v1；first-public 2026-05-29；accessed 2026-09-01
- [From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors](https://arxiv.org/html/2605.31042v1) — arXiv:2605.31042v1；first-public 2026-05-29；accessed 2026-09-01
- [Combinatorial Synthesis: Scaling Code RLVR via Atomic Decomposition and Recombination](https://arxiv.org/html/2605.31058v1) — arXiv:2605.31058v1；first-public 2026-05-29；accessed 2026-09-01
- [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/html/2605.31066v1) — arXiv:2605.31066v1；first-public 2026-05-29；accessed 2026-09-01
- [ConsisGuard: Aligning Safety Deliberation with Policy Enforcement in LLM Guardrails](https://arxiv.org/html/2605.31073v1) — arXiv:2605.31073v1；first-public 2026-05-29；accessed 2026-09-01
- [Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory](https://arxiv.org/html/2605.31086v1) — arXiv:2605.31086v1；first-public 2026-05-29；accessed 2026-09-01
- [GRKV: Global Regression for Training-Free KV Cache Compression in Long-Context LLMs](https://arxiv.org/html/2605.31105v1) — arXiv:2605.31105v1；first-public 2026-05-29；accessed 2026-09-01
- [Subspace-Decomposed JEPAs: Disentangling Progression and Content in Latent World Models](https://arxiv.org/html/2605.31111v1) — arXiv:2605.31111v1；first-public 2026-05-29；accessed 2026-09-01
- [Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](https://arxiv.org/html/2605.31158v1) — arXiv:2605.31158v1；first-public 2026-05-29；accessed 2026-09-01
- [Trust-Region Behavior Blending for On-Policy Distillation](https://arxiv.org/html/2605.31159v1) — arXiv:2605.31159v1；first-public 2026-05-29；accessed 2026-09-01
- [D$^3$: Dynamic Directional Graph-Constrained Data Scheduling for LLM Training](https://arxiv.org/html/2605.31164v1) — arXiv:2605.31164v1；first-public 2026-05-29；accessed 2026-09-01
- [LLM-FACETS: A Privacy-Preserving Framework for Evaluating LLM Transparency and Accountability](https://arxiv.org/html/2605.31167v1) — arXiv:2605.31167v1；first-public 2026-05-29；accessed 2026-09-01
- [Emergent Languages in Populations of Language Model Agents: From Token Efficiency to Oversight Evasion](https://arxiv.org/html/2605.31170v1) — arXiv:2605.31170v1；first-public 2026-05-29；accessed 2026-09-01
- [Towards Efficient LLMs Annealing with Principled Sample Selection](https://arxiv.org/html/2605.31175v1) — arXiv:2605.31175v1；first-public 2026-05-29；accessed 2026-09-01
- [Retriever Portfolios: A Principled Approach to Adaptive RAG](https://arxiv.org/html/2605.31176v1) — arXiv:2605.31176v1；first-public 2026-05-29；accessed 2026-09-01
- [Spectral Reach: Understanding Neural Scaling as Progress into the Spectral Tail](https://arxiv.org/html/2605.31244v1) — arXiv:2605.31244v1；first-public 2026-05-29；accessed 2026-09-01
- [COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://arxiv.org/html/2605.31264v1) — arXiv:2605.31264v1；first-public 2026-05-29；accessed 2026-09-01
- [Industrializing Prediction-Powered Inference: The GLIDE Library for Reliable GenAI and Agentic Systems Evaluation](https://arxiv.org/html/2605.31278v1) — arXiv:2605.31278v1；first-public 2026-05-29；accessed 2026-09-01
- [TraceGraph: Shared Decision Landscapes for Diagnosing and Improving Agent Trajectories](https://arxiv.org/html/2605.31308v1) — arXiv:2605.31308v1；first-public 2026-05-29；accessed 2026-09-01
- [Reinforcement Learning Amplifies Emergent Misalignment from Harmless Rewards](https://arxiv.org/html/2605.31328v1) — arXiv:2605.31328v1；first-public 2026-05-29；accessed 2026-09-01
- [Diagnosing Failure Modes of Shared-State Collaboration in Resource-Constrained Visual Agents](https://arxiv.org/html/2605.31354v1) — arXiv:2605.31354v1；first-public 2026-05-29；accessed 2026-09-01
- [Dreaming Of Others: Latent Teammate Modeling In World Models For Multi-Agent Reinforcement Learning](https://arxiv.org/html/2605.31361v1) — arXiv:2605.31361v1；first-public 2026-05-29；accessed 2026-09-01
- [Learning to Adapt: Self-Improving Web Agent via Cognitive-Aware Exploration](https://arxiv.org/html/2605.31365v1) — arXiv:2605.31365v1；first-public 2026-05-29；accessed 2026-09-01
- [LLM Judges Inconsistently Disagree Across Safety Criteria and Harm Categories](https://arxiv.org/html/2605.31381v1) — arXiv:2605.31381v1；first-public 2026-05-29；accessed 2026-09-01
- [Skill Availability and Presentation Granularity in Large-Language-Model Agents: A Controlled SkillsBench Study](https://arxiv.org/html/2605.31408v1) — arXiv:2605.31408v1；first-public 2026-05-29；accessed 2026-09-01
- [DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient Multi-Turn Optimization](https://arxiv.org/html/2605.31455v1) — arXiv:2605.31455v1；first-public 2026-05-29；accessed 2026-09-01
- [On-Device Robotic Planning: Eliminating Inference Redundancy for Efficient Decision-Making](https://arxiv.org/html/2605.31460v1) — arXiv:2605.31460v1；first-public 2026-05-29；accessed 2026-09-01
- [PithTrain: A Compact and Agent-Native MoE Training System](https://arxiv.org/html/2605.31463v1) — arXiv:2605.31463v1；first-public 2026-05-29；accessed 2026-09-01
- [GPU Forecasters: Language Models as Selective Surrogates for Kernel Runtime Optimization](https://arxiv.org/html/2605.31464v1) — arXiv:2605.31464v1；first-public 2026-05-29；accessed 2026-09-01
- [AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle](https://arxiv.org/html/2605.31468v1) — arXiv:2605.31468v1；first-public 2026-05-29；accessed 2026-09-01
- [Are Full Rollouts Necessary for On-Policy Distillation?](https://arxiv.org/html/2605.31490v1) — arXiv:2605.31490v1；first-public 2026-05-29；accessed 2026-09-01
- [Skill Reuse as Compression in Agentic RL](https://arxiv.org/html/2605.31509v1) — arXiv:2605.31509v1；first-public 2026-05-29；accessed 2026-09-01
- [LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards](https://arxiv.org/html/2605.31584v1) — arXiv:2605.31584v1；first-public 2026-05-29；accessed 2026-09-01
- [Stateful Online Monitoring Catches Distributed Agent Attacks](https://arxiv.org/html/2605.31593v1) — arXiv:2605.31593v1；first-public 2026-05-29；accessed 2026-09-01

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

Independent pre-write audit 与 13/13 post-write semantic audit 均已完成；Coverage/Evidence/Books 全部通过。
