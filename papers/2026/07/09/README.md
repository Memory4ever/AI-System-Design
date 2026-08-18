# Daily Research — 2026-07-09

**Research Date:** 2026-07-09

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-08 09:00:00 ～ 2026-07-09 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1148 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 14 个。当前路由账目为 14 个 Deep、0 个 Standard、0 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-09 |
| Window End | 2026-07-09 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-09-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T14:21:26+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-08T09:00:00+08:00 | 2026-07-09T09:00:00+08:00 | 2026-08-27T14:21:26+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 1148 | SF-2026-ARXIV-2607-06925<br>SF-2026-ARXIV-2607-06987<br>SF-2026-ARXIV-2607-07046<br>SF-2026-ARXIV-2607-07144<br>SF-2026-ARXIV-2607-07386<br>SF-2026-ARXIV-2607-09786<br>SF-2026-ARXIV-2607-07508<br>SF-2026-ARXIV-2607-07534<br>SF-2026-ARXIV-2607-07608<br>SF-2026-ARXIV-2607-07702<br>SF-2026-ARXIV-2607-07820<br>SF-2026-ARXIV-2607-07953<br>SF-2026-ARXIV-2607-07964<br>SF-2026-ARXIV-2607-08017 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-09T09:00:00+08:00 | coverage:SRC-ARXIV:20260709 | GAP-ARXIV-DIRECT-RESET-20260709 |
| SRC-GITHUB-COMMIT | 2026-07-08T09:00:00+08:00 | 2026-07-09T09:00:00+08:00 | 2026-08-27T14:21:26+08:00 | exact GitHub commit API lookups: Robbyant/lingbot-world-v2@025ba58834c689a5df765015d09f90c2f0f3ce30; moomight/STRACE@14595633a54079edb5e95287041e2cfd5bd1f1c9; tommasocerruti/linear-attention-architectures@584b8936306f84c14a335b3ab1fba9df05432bca | checked | 3 | SF-2026-ARXIV-2607-07534; SF-2026-ARXIV-2607-07702; SF-2026-ARXIV-2607-07953 | pages=3; final cursors=025ba58834c689a5df765015d09f90c2f0f3ce30,14595633a54079edb5e95287041e2cfd5bd1f1c9,584b8936306f84c14a335b3ab1fba9df05432bca; one bounded commit lookup per family | 2026-07-09T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260709 | — |

<!-- coverage:SRC-ARXIV:20260709:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 1148 unique identities in this strict window; 14 routed families.<!-- coverage:SRC-ARXIV:20260709:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260709:start -->repository=Robbyant/lingbot-world-v2, until=2026-07-09T01:00:00Z, full_sha=025ba58834c689a5df765015d09f90c2f0f3ce30, commit_timestamp=2026-07-08T16:40:31Z, url=https://github.com/Robbyant/lingbot-world-v2/tree/025ba58834c689a5df765015d09f90c2f0f3ce30; repository=moomight/STRACE, until=2026-07-09T01:00:00Z, full_sha=14595633a54079edb5e95287041e2cfd5bd1f1c9, commit_timestamp=2026-05-26T15:52:52Z, url=https://github.com/moomight/STRACE/tree/14595633a54079edb5e95287041e2cfd5bd1f1c9; repository=tommasocerruti/linear-attention-architectures, until=2026-07-09T01:00:00Z, full_sha=584b8936306f84c14a335b3ab1fba9df05432bca, commit_timestamp=2026-06-15T04:19:21Z, url=https://github.com/tommasocerruti/linear-attention-architectures/tree/584b8936306f84c14a335b3ab1fba9df05432bca; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260709:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 14 个 family：exact v1 为 7 个 family 披露 artifact/evidence locator，其中 7 个提供外部 repository/project/demo locator，另有 7 个未披露；本日确认 3 个 family、3 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-06925 | arXiv:2607.06925v1 | paper-v1:2607.06925 | 2026-W28 | 2026-07-08 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-06925 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2607-06925 | yes |
| SF-2026-ARXIV-2607-06987 | arXiv:2607.06987v1 | paper-v1:2607.06987 | 2026-W28 | 2026-07-08 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-06987 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2607-06987 | yes |
| SF-2026-ARXIV-2607-07046 | arXiv:2607.07046v1 | paper-v1:2607.07046 | 2026-W28 | 2026-07-08 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-07046 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607-07046 | yes |
| SF-2026-ARXIV-2607-07144 | arXiv:2607.07144v1 | paper-v1:2607.07144 | 2026-W28 | 2026-07-08 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-07144 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-07144 | yes |
| SF-2026-ARXIV-2607-07386 | arXiv:2607.07386v1 | paper-v1:2607.07386 | 2026-W28 | 2026-07-08 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-07386 | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2607-07386 | yes |
| SF-2026-ARXIV-2607-09786 | arXiv:2607.09786v1 | paper-v1:2607.09786 | 2026-W28 | 2026-07-08 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09786 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2607-07508 | arXiv:2607.07508v1 | paper-v1:2607.07508 | 2026-W28 | 2026-07-08 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-07508 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-07508 | yes |
| SF-2026-ARXIV-2607-07534 | arXiv:2607.07534v1 | paper-v1:2607.07534 | 2026-W28 | 2026-07-08 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-07534 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-07534 | yes |
| SF-2026-ARXIV-2607-07608 | arXiv:2607.07608v1 | paper-v1:2607.07608 | 2026-W28 | 2026-07-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-07608 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2607-07608 | yes |
| SF-2026-ARXIV-2607-07702 | arXiv:2607.07702v1 | paper-v1:2607.07702 | 2026-W28 | 2026-07-09 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-07702 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-07702 | yes |
| SF-2026-ARXIV-2607-07820 | arXiv:2607.07820v1 | paper-v1:2607.07820 | 2026-W28 | 2026-07-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-07820 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-07820 | yes |
| SF-2026-ARXIV-2607-07953 | arXiv:2607.07953v1 | paper-v1:2607.07953 | 2026-W28 | 2026-07-09 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-07953 | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2607-07953 | yes |
| SF-2026-ARXIV-2607-07964 | arXiv:2607.07964v1 | paper-v1:2607.07964 | 2026-W28 | 2026-07-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-07964 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607-07964 | yes |
| SF-2026-ARXIV-2607-08017 | arXiv:2607.08017v1 | paper-v1:2607.08017 | 2026-W28 | 2026-07-09 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08017 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607-08017 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-06925 | RP-6e26340a3cca5e6d | deep | arXiv:2607.06925v1 | SRC-ARXIV@arXiv:2607.06925v1 | arXiv:2607.06925v1#S3 — compact action-conditioned world-model formulation and goal-conditioned baseline; arXiv:2607.06925v1#S4 — instruction-leakage diagnosis and goal-free dynamics intervention | https://arxiv.org/html/2607.06925v1#S5.SS1 — controlled spatial-relation tasks and leakage controls; https://arxiv.org/html/2607.06925v1#S5.SS4 — goal-free comparison; https://arxiv.org/html/2607.06925v1#S6 — interpretation of grounding and planner/dynamics separation | arXiv:2607.06925v1#S7 — compact synthetic environment, narrow relation vocabulary and no large-scale physical deployment | Not Disclosed — exact v1 provides no source locator for artifact; No official event-time repository or uniquely versioned artifact is disclosed in exact v1; formulas, task construction and reported tables are manuscript evidence only. | claim:SF-2026-ARXIV-2607-06925 | complete |
| SF-2026-ARXIV-2607-06987 | RP-e05556c85ecaa249 | deep | arXiv:2607.06987v1 | SRC-ARXIV@arXiv:2607.06987v1 | arXiv:2607.06987v1 PDF §4.1-§4.2 — self-anchored positive ratio, stop-gradient denominator and asymmetric negative clipping; arXiv:2607.06987v1 PDF Appendix A — gradient derivation and relation to GRPO/DAPO/GSPO | arXiv:2607.06987v1 PDF §5.1-§5.5 — model/task contract, optimizer variants, probability-capacity analysis and ablations | arXiv:2607.06987v1 PDF §6 and experiment disclosures — author results are bounded to listed Qwen families and math/geometry regimes; no universal stability proof | Project page https://chongyu-fan.netlify.app/posts/up/ is disclosed; no uniquely identified public code repository or event-time commit is disclosed, so implementation equivalence is Not Verified. | claim:SF-2026-ARXIV-2607-06987 | complete |
| SF-2026-ARXIV-2607-07046 | RP-a45b018c8c072a7f | deep | arXiv:2607.07046v1 | SRC-ARXIV@arXiv:2607.07046v1 | https://arxiv.org/html/2607.07046v1#S3 — per-layer MP/TP planning and task-aware precision; https://arxiv.org/html/2607.07046v1#S4 — prefill/decode separation and elastic runtime controller | arXiv:2607.07046v1#S5 — six-device/three-cluster evaluation, model/task suites, trace replay and QoS thresholds; arXiv:2607.07046v1#S6 — component and adaptation ablations | arXiv:2607.07046v1#S7 — edge-cluster/network scope and workload-specific planning limitations | Not Disclosed — exact v1 provides no source locator for artifact; No official event-time source repository or uniquely versioned implementation artifact is disclosed in exact v1. | claim:SF-2026-ARXIV-2607-07046 | complete |
| SF-2026-ARXIV-2607-07144 | RP-1b9d8f16ff4498bf | deep | arXiv:2607.07144v1 | SRC-ARXIV@arXiv:2607.07144v1 | https://arxiv.org/html/2607.07144v1#S2 — contractive iterated-map encoding; https://arxiv.org/html/2607.07144v1#S3 — anchors and random access; https://arxiv.org/html/2607.07144v1#S4 — residual VQ and asymmetric K-V allocation | arXiv:2607.07144v1#S6 — reconstruction, suffix retrieval and storage experiments | arXiv:2607.07144v1#S7 — GPT-2-scale, 1024-context, one-corpus and CPU-only limitations | https://github.com/eighteight/fractal-kv is linked by the manuscript, but GitHub history contains no commit at or before the Daily window cutoff; event-time implementation provenance is therefore Not Verified. | claim:SF-2026-ARXIV-2607-07144 | complete |
| SF-2026-ARXIV-2607-07386 | RP-c1425b40e0613d64 | deep | arXiv:2607.07386v1 | SRC-ARXIV@arXiv:2607.07386v1 | https://arxiv.org/html/2607.07386v1#S3 — explicit N-slot table and product-key sparse read/write; https://arxiv.org/html/2607.07386v1#S4 — gated delta update | https://arxiv.org/html/2607.07386v1#S5 — iso-FLOP scaling and language/long-context tasks; https://arxiv.org/html/2607.07386v1#S6 — kernel and memory profiling; Appendix A-E | arXiv:2607.07386v1#S7 and Appendix F — HBM residence, large physical state, current kernel overhead and limited serving evidence | https://github.com/facebookresearch/sparse-delta-memory and https://github.com/fla-org/flash-linear-attention are disclosed, but neither provides a paper-specific event-time commit at or before the window cutoff; artifact equivalence is Not Verified. | claim:SF-2026-ARXIV-2607-07386 | complete |
| SF-2026-ARXIV-2607-09786 | RP-70b9919e6819483a | deep | arXiv:2607.09786v1 | SRC-ARXIV@arXiv:2607.09786v1 | https://arxiv.org/html/2607.09786v1#S3 — RL length-penalty intervention; https://arxiv.org/html/2607.09786v1#S4 — monitorability probes and content-blind matched shortening controls | https://arxiv.org/html/2607.09786v1#S5 — Qwen/Nemotron runs and reasoning benchmarks; https://arxiv.org/html/2607.09786v1#S7 — hint disclosure and judge analyses; Appendix A-D | arXiv:2607.09786v1#S8 and Appendix E — limited seeds/models, diagnostic subsets and evaluator dependence | Not Disclosed — exact v1 provides no source locator for artifact; No official event-time repository or uniquely versioned training artifact is disclosed in exact v1. | claim:SF-2026-ARXIV-2607-09786 | complete |
| SF-2026-ARXIV-2607-07508 | RP-2e745d3f3050f8e5 | deep | arXiv:2607.07508v1 | SRC-ARXIV@arXiv:2607.07508v1 | https://arxiv.org/html/2607.07508v1#S3.SS1 — direct two-sided importance correction; https://arxiv.org/html/2607.07508v1#S3.SS2 — trust mask and single-rollout critic; https://arxiv.org/html/2607.07508v1#S4 — asynchronous actor/learner pipeline and update protocol | https://arxiv.org/html/2607.07508v1#S5 — agentic math/SWE tasks and throughput; https://arxiv.org/html/2607.07508v1#S6 — algorithm ablations | arXiv:2607.07508v1#A2 — critic/rollout-cost assumptions, task scope and asynchronous staleness limits | Not Disclosed — exact v1 provides no source locator for artifact; No official public repository or uniquely versioned event-time artifact is disclosed in exact v1. | claim:SF-2026-ARXIV-2607-07508 | complete |
| SF-2026-ARXIV-2607-07534 | RP-ef45f2dd94f8a845 | deep | arXiv:2607.07534v1 | SRC-ARXIV@arXiv:2607.07534v1; SRC-GITHUB-COMMIT@commit:025ba58834c689a5df765015d09f90c2f0f3ce30 | https://arxiv.org/html/2607.07534v1#S2 — causal chunk generation; https://arxiv.org/html/2607.07534v1#S3 — interaction conditioning; https://arxiv.org/html/2607.07534v1#S4 — few-step distillation and runtime loop | https://arxiv.org/html/2607.07534v1#S5 — visual and interactive quality; https://arxiv.org/html/2607.07534v1#S6 — runtime demonstrations and limitations discussion | arXiv:2607.07534v1#S6 — paragraph 'Limitations and discussion': revisit regeneration, finite context, environment consistency and author-evaluation limits | https://github.com/Robbyant/lingbot-world-v2/tree/025ba58834c689a5df765015d09f90c2f0f3ce30 (event-time repository commit 2026-07-08T16:40:31Z; establishes the public implementation tree, not equivalence to every manuscript claim) | claim:SF-2026-ARXIV-2607-07534 | complete |
| SF-2026-ARXIV-2607-07608 | RP-eef3c5be1ecfaa5d | deep | arXiv:2607.07608v1 | SRC-ARXIV@arXiv:2607.07608v1 | https://arxiv.org/html/2607.07608v1#S3 — short/long latent vaults and latent curator; https://arxiv.org/html/2607.07608v1#S4 — memory-action weaving | arXiv:2607.07608v1#S5 — SimplerEnv-Bridge/LIBERO evaluation and component ablations | Not Disclosed — exact v1 provides no source locator for limitations/counterevidence; No dedicated limitations section; exact v1 leaves physical deployment, memory reset/contamination and safety-controller interaction under-evaluated | Not Disclosed — exact v1 provides no source locator for artifact; No official source repository, checkpoint or uniquely versioned event-time artifact is disclosed in exact v1. | claim:SF-2026-ARXIV-2607-07608 | complete |
| SF-2026-ARXIV-2607-07702 | RP-b4c4086ce65a17c4 | deep | arXiv:2607.07702v1 | SRC-ARXIV@arXiv:2607.07702v1; SRC-GITHUB-COMMIT@commit:14595633a54079edb5e95287041e2cfd5bd1f1c9 | https://arxiv.org/html/2607.07702v1#S3 — trajectory normalization and dependency graph; https://arxiv.org/html/2607.07702v1#S4 — backward slice and root-cause candidate extraction | https://arxiv.org/html/2607.07702v1#S4 — diagnosis comparisons; https://arxiv.org/html/2607.07702v1#S5 — agent benchmarks and component studies; appendices | arXiv:2607.07702v1#S5 — observational traces, parser/judge dependence and limited causal identification | https://github.com/moomight/STRACE/tree/14595633a54079edb5e95287041e2cfd5bd1f1c9 (event-time repository commit 2026-05-26; preserves implementation provenance) | claim:SF-2026-ARXIV-2607-07702 | complete |
| SF-2026-ARXIV-2607-07820 | RP-0af0284f505280d9 | deep | arXiv:2607.07820v1 | SRC-ARXIV@arXiv:2607.07820v1 | https://arxiv.org/html/2607.07820v1#S3 — verifiable offline search world and scaffold teacher; https://arxiv.org/html/2607.07820v1#S4 — rejection, evolving SFT and round-bounded asynchronous generation/training | arXiv:2607.07820v1#S5 and Appendix A-C — search benchmarks, training/runtime configuration and ablations | arXiv:2607.07820v1#S5 — offline-world coverage, verifier dependence and transfer to live search | Not Disclosed — exact v1 provides no source locator for artifact; No official public repository or uniquely versioned event-time environment/training artifact is disclosed in exact v1. | claim:SF-2026-ARXIV-2607-07820 | complete |
| SF-2026-ARXIV-2607-07953 | RP-91f9aefb4a32311d | deep | arXiv:2607.07953v1 | SRC-ARXIV@arXiv:2607.07953v1; SRC-GITHUB-COMMIT@commit:584b8936306f84c14a335b3ab1fba9df05432bca | https://arxiv.org/html/2607.07953v1#S2 — unified recurrent notation across linear-attention families; https://arxiv.org/html/2607.07953v1#S3 — CLER cross-layer routing; https://arxiv.org/html/2607.07953v1#S4 — CLVR representation alignment | https://arxiv.org/html/2607.07953v1#S5 — controlled architecture and optimizer comparisons; https://arxiv.org/html/2607.07953v1#S6 — routing ablations and scaling runs; Appendix A-B | arXiv:2607.07953v1#S7 and S9 — single-run routing gains, scale attenuation and absence of inference benchmarks | https://github.com/tommasocerruti/linear-attention-architectures/tree/584b8936306f84c14a335b3ab1fba9df05432bca (event-time repository commit 2026-06-15T04:19:21Z) | claim:SF-2026-ARXIV-2607-07953 | complete |
| SF-2026-ARXIV-2607-07964 | RP-71b4f11c2360490f | deep | arXiv:2607.07964v1 | SRC-ARXIV@arXiv:2607.07964v1 | https://arxiv.org/html/2607.07964v1#S3 — Kronecker-factored Hessian and bidirectional incoherence; https://arxiv.org/html/2607.07964v1#S4 — Hessian-trace mixed precision | https://arxiv.org/html/2607.07964v1#S5 — calibration, perplexity and downstream quality; https://arxiv.org/html/2607.07964v1#S6 — bit allocation, latency and ablations; Appendix A-E | arXiv:2607.07964v1#A6 — calibration overhead, temporary gradient-covariance memory and runtime comparison boundaries | https://github.com/Intelligent-Computing-Lab-Panda/KronQ is disclosed, but GitHub history contains no commit at or before the Daily window cutoff; event-time implementation provenance is Not Verified. | claim:SF-2026-ARXIV-2607-07964 | complete |
| SF-2026-ARXIV-2607-08017 | RP-7eea1056326259e5 | deep | arXiv:2607.08017v1 | SRC-ARXIV@arXiv:2607.08017v1 | https://arxiv.org/html/2607.08017v1#S3 — causal-DAG decomposition and semantic-structural graph distance; https://arxiv.org/html/2607.08017v1#S4 — medoid and GRCS uncertainty features | https://arxiv.org/html/2607.08017v1#S5.SS1 — five-benchmark and model/decomposer contract; https://arxiv.org/html/2607.08017v1#S5.SS4 — adversarial-medoid ablations; Appendix B-C | arXiv:2607.08017v1#S7 — short reasoning horizons, decomposer/judge dependence, scale attenuation and computational cost | Not Disclosed — exact v1 provides no source locator for artifact; No official public repository, graph corpus or uniquely versioned event-time artifact is disclosed in exact v1. | claim:SF-2026-ARXIV-2607-08017 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-06925:start -->
#### Grounding Spatial Relations in a Compact World Model: Instruction Leakage and a Goal-Free Dynamics Fix

<!-- claim:SF-2026-ARXIV-2607-06925:start -->Exact v1 supports the causal concern that an answer-bearing instruction can let a dynamics model bypass transition learning, and that removing the goal improves the controlled grounding test. It does not establish general physical-world causality, long-horizon planning or deployment safety. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06925:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The baseline gives the transition model both the current scene/action and an instruction that directly names the spatial relation later used as the evaluation target. The model can therefore copy goal semantics rather than infer the environment transition. Removing goal identity from dynamics and keeping it in the planner's objective forces the learned transition to explain observation changes instead of receiving the answer-bearing variable. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.06925v1#S3 — compact action-conditioned world-model formulation and goal-conditioned baseline; arXiv:2607.06925v1#S4 — instruction-leakage diagnosis and goal-free dynamics intervention`；Evaluation：`https://arxiv.org/html/2607.06925v1#S5.SS1 — controlled spatial-relation tasks and leakage controls; https://arxiv.org/html/2607.06925v1#S5.SS4 — goal-free comparison; https://arxiv.org/html/2607.06925v1#S6 — interpretation of grounding and planner/dynamics separation`；Limitations/Counterevidence：`arXiv:2607.06925v1#S7 — compact synthetic environment, narrow relation vocabulary and no large-scale physical deployment`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-06925:end -->

<!-- review:SF-2026-ARXIV-2607-06987:start -->
#### UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma

<!-- claim:SF-2026-ARXIV-2607-06987:start -->Exact v1 proves the algebraic gradient contract and reports consistent gains in its experiments. It does not provide a general convergence theorem, public implementation equivalence or evidence outside the evaluated reasoning families. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-06987:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** For positive advantages, UP replaces the stale rollout ratio with πθ divided by a stop-gradient copy of itself. Its forward value is one while its gradient is the current-policy REINFORCE gradient, so the positive branch no longer hits the usual upper clipping ceiling. The negative branch retains a conventional bounded ratio/KL safeguard, making the change asymmetric rather than removing stability controls globally. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.06987v1 PDF §4.1-§4.2 — self-anchored positive ratio, stop-gradient denominator and asymmetric negative clipping; arXiv:2607.06987v1 PDF Appendix A — gradient derivation and relation to GRPO/DAPO/GSPO`；Evaluation：`arXiv:2607.06987v1 PDF §5.1-§5.5 — model/task contract, optimizer variants, probability-capacity analysis and ablations`；Limitations/Counterevidence：`arXiv:2607.06987v1 PDF §6 and experiment disclosures — author results are bounded to listed Qwen families and math/geometry regimes; no universal stability proof`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-06987:end -->

<!-- review:SF-2026-ARXIV-2607-07046:start -->
#### Voltron: Enabling Elastic Multi-Device Execution of LLM Inference for Empowered Edge Intelligence

<!-- claim:SF-2026-ARXIV-2607-07046:start -->Exact v1 supports phase-specific, per-layer planning and boundary-safe runtime adaptation on its edge setup. It does not prove datacenter-scale behavior, arbitrary-network stability or that mixed precision preserves every task outside the measured evaluator set. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-07046:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Voltron first builds distinct per-layer execution plans for prefill and decode, choosing model/tensor parallel placement and precision according to layer/task sensitivity. At runtime it observes memory, KV growth and wireless conditions, then revises device participation, precision and pruning at token boundaries while preloading the next plan to hide reconfiguration. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.07046v1#S3 — per-layer MP/TP planning and task-aware precision; https://arxiv.org/html/2607.07046v1#S4 — prefill/decode separation and elastic runtime controller`；Evaluation：`arXiv:2607.07046v1#S5 — six-device/three-cluster evaluation, model/task suites, trace replay and QoS thresholds; arXiv:2607.07046v1#S6 — component and adaptation ablations`；Limitations/Counterevidence：`arXiv:2607.07046v1#S7 — edge-cluster/network scope and workload-specific planning limitations`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-07046:end -->

<!-- review:SF-2026-ARXIV-2607-07144:start -->
#### Fractal KV-Cache Archives: Lossless Symbolic Storage with In-Place Retrieval for Long-Context LLM Inference

<!-- claim:SF-2026-ARXIV-2607-07144:start -->Exact v1 supports lossless reconstruction of the already-quantized symbol stream, not lossless recovery of original FP16 KV; the feed quantizer incurs the paper-reported quality cost. Structural suffix similarity is not semantic relevance, and the paper does not demonstrate end-to-end production serving gains. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-07144:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A lossy feed quantizer first maps KV into symbol codes; a contractive symbolic map then serializes that quantized code stream into an archive with periodic anchors. The archive is lossless only relative to the codes, supports append and position access without decoding the whole prefix, and can serve as a structural suffix-similarity index. It does not reconstruct the original FP16 KV without quantization error. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.07144v1#S2 — contractive iterated-map encoding; https://arxiv.org/html/2607.07144v1#S3 — anchors and random access; https://arxiv.org/html/2607.07144v1#S4 — residual VQ and asymmetric K-V allocation`；Evaluation：`arXiv:2607.07144v1#S6 — reconstruction, suffix retrieval and storage experiments`；Limitations/Counterevidence：`arXiv:2607.07144v1#S7 — GPT-2-scale, 1024-context, one-corpus and CPU-only limitations`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-07144:end -->

<!-- review:SF-2026-ARXIV-2607-07386:start -->
#### Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity

<!-- claim:SF-2026-ARXIV-2607-07386:start -->Exact v1 supports scalable addressable recurrent state and reports quality gains under its iso-FLOP contract. It does not prove that current kernels beat attention/GDN in production serving or that large state can remain cheaply resident. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-07386:end -->

**旧方案与约束变化。** `本章的核心判断是：**Long Context 是位置有效性、Attention 计算、KV Cache 容量、信息利用与系统 SLO 的联合能力。**任何只移动一个瓶颈的方案，都不能自动得到可用的长上下文系统。`（`books/part-02-model/22-long-context.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Sparse Delta Memory replaces a fixed dense recurrent matrix with an explicit N-by-d memory table. Product keys choose a small write set and read set, and a gated delta rule changes only selected slots. Increasing N expands addressable state without increasing per-token arithmetic proportionally, but the physical table grows and leaves fast on-chip memory. 它改变 `MODEL-LONG-CONTEXT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.07386v1#S3 — explicit N-slot table and product-key sparse read/write; https://arxiv.org/html/2607.07386v1#S4 — gated delta update`；Evaluation：`https://arxiv.org/html/2607.07386v1#S5 — iso-FLOP scaling and language/long-context tasks; https://arxiv.org/html/2607.07386v1#S6 — kernel and memory profiling; Appendix A-E`；Limitations/Counterevidence：`arXiv:2607.07386v1#S7 and Appendix F — HBM residence, large physical state, current kernel overhead and limited serving evidence`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L637-L650`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MODEL-LONG-CONTEXT`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-07386:end -->

<!-- review:SF-2026-ARXIV-2607-09786:start -->
#### Length Penalties Make Chain-of-Thought Less Monitorable

<!-- claim:SF-2026-ARXIV-2607-09786:start -->Exact v1 supports a monitorability regression in listed training/evaluation contracts and controls for random shortening. It does not prove that visible CoT is faithful internal reasoning or that all length optimization is unsafe. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-09786:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A reward penalty for long reasoning traces does more than compress tokens: it can preferentially remove explicit intermediate hints that make a correct answer externally inspectable. Matched content-blind shortening separates mere length reduction from policy adaptation, showing monitorability is an independent objective rather than a guaranteed by-product of concise reasoning. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.09786v1#S3 — RL length-penalty intervention; https://arxiv.org/html/2607.09786v1#S4 — monitorability probes and content-blind matched shortening controls`；Evaluation：`https://arxiv.org/html/2607.09786v1#S5 — Qwen/Nemotron runs and reasoning benchmarks; https://arxiv.org/html/2607.09786v1#S7 — hint disclosure and judge analyses; Appendix A-D`；Limitations/Counterevidence：`arXiv:2607.09786v1#S8 and Appendix E — limited seeds/models, diagnostic subsets and evaluator dependence`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L445-L453`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-09786:end -->

<!-- review:SF-2026-ARXIV-2607-07508:start -->
#### Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-07508:start -->Exact v1 supports the single-rollout/critic and direct importance-correction design plus bounded task gains. It does not establish universal sample-efficiency gains or production correctness under arbitrary actor lag. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-07508:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** SAO uses one rollout per prompt, trains a value critic more frequently than the actor and corrects current-policy learning directly against the rollout policy. Tokens whose two-sided importance ratio leaves a trust interval are masked rather than allowed to dominate. This trades group-relative variance reduction for lower rollout cost and explicit staleness control. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.07508v1#S3.SS1 — direct two-sided importance correction; https://arxiv.org/html/2607.07508v1#S3.SS2 — trust mask and single-rollout critic; https://arxiv.org/html/2607.07508v1#S4 — asynchronous actor/learner pipeline and update protocol`；Evaluation：`https://arxiv.org/html/2607.07508v1#S5 — agentic math/SWE tasks and throughput; https://arxiv.org/html/2607.07508v1#S6 — algorithm ablations`；Limitations/Counterevidence：`arXiv:2607.07508v1#A2 — critic/rollout-cost assumptions, task scope and asynchronous staleness limits`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L608-L622`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-07508:end -->

<!-- review:SF-2026-ARXIV-2607-07534:start -->
#### Infinite Worlds with Versatile Interactions

<!-- claim:SF-2026-ARXIV-2607-07534:start -->Exact v1 and event-time code support an interactive generation pipeline and author-reported runtime. They do not establish a canonical persistent world, physical correctness or independent benchmark superiority. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-07534:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The system streams causally generated video chunks conditioned on user interactions, then uses few-step distillation and a runtime harness to sustain low-latency continuation. It can generate a long visual experience, but places that leave the active context are regenerated rather than retrieved from a canonical persistent environment state. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.07534v1#S2 — causal chunk generation; https://arxiv.org/html/2607.07534v1#S3 — interaction conditioning; https://arxiv.org/html/2607.07534v1#S4 — few-step distillation and runtime loop`；Evaluation：`https://arxiv.org/html/2607.07534v1#S5 — visual and interactive quality; https://arxiv.org/html/2607.07534v1#S6 — runtime demonstrations and limitations discussion`；Limitations/Counterevidence：`arXiv:2607.07534v1#S6 — paragraph 'Limitations and discussion': revisit regeneration, finite context, environment consistency and author-evaluation limits`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L713-L724`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-07534:end -->

<!-- review:SF-2026-ARXIV-2607-07608:start -->
#### LaMem-VLA: Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation

<!-- claim:SF-2026-ARXIV-2607-07608:start -->Exact v1 supports the dual-latent-memory mechanism and listed benchmark gains. It does not prove real-world safety, durable cross-session memory, recovery from contaminated state or general embodiment transfer. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-07608:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** LaMem-VLA keeps a short latent vault for immediate task progress and a compressed long vault for older observations, with a curator deciding what moves between them. Memory tokens are woven into action prediction rather than retrieved as text, giving the policy an internal state estimate across partially observed manipulation trajectories. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.07608v1#S3 — short/long latent vaults and latent curator; https://arxiv.org/html/2607.07608v1#S4 — memory-action weaving`；Evaluation：`arXiv:2607.07608v1#S5 — SimplerEnv-Bridge/LIBERO evaluation and component ablations`；Limitations/Counterevidence：`Not Disclosed — exact v1 provides no source locator for limitations/counterevidence; No dedicated limitations section; exact v1 leaves physical deployment, memory reset/contamination and safety-controller interaction under-evaluated`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L689-L700`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-07608:end -->

<!-- review:SF-2026-ARXIV-2607-07702:start -->
#### From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization

<!-- claim:SF-2026-ARXIV-2607-07702:start -->Exact v1 and event-time code support the structural diagnosis pipeline and bounded benchmarks. They do not prove causal identification from observational traces or eliminate evaluator dependence. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-07702:end -->

**旧方案与约束变化。** `本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。**`（`books/part-06-ai-infrastructure/69-trace.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** STRACE converts noisy agent trajectories into typed dependency graphs, then slices backward from a failed outcome to isolate the minimal relevant action/observation chain and propose root-cause candidates. Structural compression improves diagnostic focus, but a graph reconstructed from observations remains evidence for dependency, not proof of intervention-level causality. 它改变 `PLATFORM-TRACE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.07702v1#S3 — trajectory normalization and dependency graph; https://arxiv.org/html/2607.07702v1#S4 — backward slice and root-cause candidate extraction`；Evaluation：`https://arxiv.org/html/2607.07702v1#S4 — diagnosis comparisons; https://arxiv.org/html/2607.07702v1#S5 — agent benchmarks and component studies; appendices`；Limitations/Counterevidence：`arXiv:2607.07702v1#S5 — observational traces, parser/judge dependence and limited causal identification`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L813-L824`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-TRACE`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-07702:end -->

<!-- review:SF-2026-ARXIV-2607-07820:start -->
#### DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment

<!-- claim:SF-2026-ARXIV-2607-07820:start -->Exact v1 supports the offline data-factory and round-bounded self-distillation pipeline on listed search tasks. It does not validate live search safety or make the offline world a production workflow substitute. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-07820:end -->

**旧方案与约束变化。** `本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**`（`books/part-07-agent/81-workflow.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The method builds a deterministic offline search environment whose answers can be verified, uses a stronger scaffold to create and reject trajectories, then alternates self-generated data with SFT across explicit rounds. Generation and learning may overlap inside a round, but the round boundary freezes the policy/data contract before the next promotion. 它改变 `AGENT-WORKFLOW` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.07820v1#S3 — verifiable offline search world and scaffold teacher; https://arxiv.org/html/2607.07820v1#S4 — rejection, evolving SFT and round-bounded asynchronous generation/training`；Evaluation：`arXiv:2607.07820v1#S5 and Appendix A-C — search benchmarks, training/runtime configuration and ablations`；Limitations/Counterevidence：`arXiv:2607.07820v1#S5 — offline-world coverage, verifier dependence and transfer to live search`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L825-L836`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-WORKFLOW`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-07820:end -->

<!-- review:SF-2026-ARXIV-2607-07953:start -->
#### Linear Attention Architectures: Mechanisms, Trade-offs, and Cross-Layer Routing

<!-- claim:SF-2026-ARXIV-2607-07953:start -->Exact v1 supports a controlled comparison and the aligned-routing mechanism. It does not establish a universally best linear-attention architecture or production inference advantage. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-07953:end -->

**旧方案与约束变化。** `本章的核心判断是：**Long Context 是位置有效性、Attention 计算、KV Cache 容量、信息利用与系统 SLO 的联合能力。**任何只移动一个瓶颈的方案，都不能自动得到可用的长上下文系统。`（`books/part-02-model/22-long-context.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A common recurrent form exposes where DeltaNet/GDN/Kimi-like architectures differ in decay, update and gating rather than treating names as incomparable systems. Cross-layer error routing fails when a write residual is injected into a basis that does not share its representation; CLVR first projects the write value into an aligned hidden stream, making the added route semantically compatible. 它改变 `MODEL-LONG-CONTEXT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.07953v1#S2 — unified recurrent notation across linear-attention families; https://arxiv.org/html/2607.07953v1#S3 — CLER cross-layer routing; https://arxiv.org/html/2607.07953v1#S4 — CLVR representation alignment`；Evaluation：`https://arxiv.org/html/2607.07953v1#S5 — controlled architecture and optimizer comparisons; https://arxiv.org/html/2607.07953v1#S6 — routing ablations and scaling runs; Appendix A-B`；Limitations/Counterevidence：`arXiv:2607.07953v1#S7 and S9 — single-run routing gains, scale attenuation and absence of inference benchmarks`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L623-L636`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MODEL-LONG-CONTEXT`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-07953:end -->

<!-- review:SF-2026-ARXIV-2607-07964:start -->
#### KronQ: LLM Quantization via Kronecker-Factored Hessian

<!-- claim:SF-2026-ARXIV-2607-07964:start -->Exact v1 supports the Hessian factorization, transforms and reported accuracy on listed LLaMA/calibration contracts. It does not prove general runtime speedups, event-time code equivalence or universal calibration transfer. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-07964:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** KronQ approximates second-order weight sensitivity as output-gradient covariance Kronecker activation covariance, then uses two-sided incoherence transforms and Hessian-trace sensitivity for mixed-bit allocation. After preprocessing, the output-gradient factor cancels from the column update algebra, but it still influences the transformed representation and layer sensitivity decision. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.07964v1#S3 — Kronecker-factored Hessian and bidirectional incoherence; https://arxiv.org/html/2607.07964v1#S4 — Hessian-trace mixed precision`；Evaluation：`https://arxiv.org/html/2607.07964v1#S5 — calibration, perplexity and downstream quality; https://arxiv.org/html/2607.07964v1#S6 — bit allocation, latency and ablations; Appendix A-E`；Limitations/Counterevidence：`arXiv:2607.07964v1#A6 — calibration overhead, temporary gradient-covariance memory and runtime comparison boundaries`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-07964:end -->

<!-- review:SF-2026-ARXIV-2607-08017:start -->
#### Can We Trust LLM's Logic? Quantifying Uncertainty, Coherence, and Robustness via a Graph-Based Framework

<!-- claim:SF-2026-ARXIV-2607-08017:start -->Exact v1 supports graph-structure agreement as an additional uncertainty signal and its listed ablations. It does not prove logical truth, calibrated confidence or robust decomposition for long/open-ended reasoning. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-08017:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** GraphEVAL samples multiple chains of thought, uses a separate deterministic decomposer to turn each into a claimed causal DAG, and compares semantic/structural graph distance. A graph medoid and GRCS features measure agreement and robustness; an adversarial-medoid intervention tests whether the selector merely follows a central but wrong trace. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.08017v1#S3 — causal-DAG decomposition and semantic-structural graph distance; https://arxiv.org/html/2607.08017v1#S4 — medoid and GRCS uncertainty features`；Evaluation：`https://arxiv.org/html/2607.08017v1#S5.SS1 — five-benchmark and model/decomposer contract; https://arxiv.org/html/2607.08017v1#S5.SS4 — adversarial-medoid ablations; Appendix B-C`；Limitations/Counterevidence：`arXiv:2607.08017v1#S7 — short reasoning horizons, decomposer/judge dependence, scale attenuation and computational cost`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-08017:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-06925 | compact spatial-relation prediction under instruction-conditioned and goal-free variants | paper-defined compact world-model variants; parameter count Not Disclosed in the reportable contract | Not Disclosed | Not Disclosed | short controlled trajectories; exact production horizon Not Applicable | short controlled trajectories; exact production horizon Not Applicable | Not Disclosed | Not Disclosed | No serving SLO; evaluates prediction/grounding behavior | author-defined spatial-relation tasks with leakage and withheld-goal controls |
| SF-2026-ARXIV-2607-06987 | reasoning post-training on mathematical and geometry tasks | Qwen3-8B, Qwen3-14B, Qwen3-30B-A3B and Qwen3-VL-8B variants | NVIDIA A100 GPUs where disclosed; exact GPU count varies by run and is not fully normalized | training precision Not Disclosed consistently across all runs | task-dependent reasoning trajectories; exact prompt/output distribution Not Disclosed | task-dependent reasoning trajectories; exact prompt/output distribution Not Disclosed | algorithm/run-specific and not fully normalized in the paper tables | verl/vLLM rollout pipeline; exact global rollout concurrency Not Disclosed | No serving SLO; reports training reward and benchmark accuracy | author benchmark harness for mathematics and Geometry3K-style tasks |
| SF-2026-ARXIV-2607-07046 | interactive edge LLM inference with prefill/decode and LMSYS-derived arrival traces | Qwen1.5-family and paper-listed LLM variants | six heterogeneous edge devices arranged into three measured clusters; exact device inventory is bound to paper §5 tables | mixed precision selected per layer/task; exact formats are experiment-specific | prompt/output distributions follow paper workloads; individual normalized lengths Not Disclosed for every table | prompt/output distributions follow paper workloads; individual normalized lengths Not Disclosed for every table | dynamic request workload; per-table batch Not Disclosed consistently | trace-driven multi-request execution across participating devices | TTFT 10 s and TPOT 400 ms thresholds in the reported QoS contract | MMLU, HellaSwag, GSM8K and MATH plus measured latency/QoS |
| SF-2026-ARXIV-2607-07144 | lossless archival of an already-quantized KV symbol stream and suffix retrieval on a public-domain text corpus | GPT-2 124M | single CPU; exact SKU Not Disclosed | paper-defined quantized archive; live model precision Not Disclosed | context length 1024 | context length 1024 | Not Disclosed | single-process measurements; serving concurrency Not Evaluated | No production SLO; storage, reconstruction and access metrics | author reconstruction and structural suffix-search tests |
| SF-2026-ARXIV-2607-07386 | iso-FLOP language modeling and long-context retrieval/understanding | paper scaling ladder through 8B parameters | GPU experiments reported by authors; exact SKU varies and is not normalized across every table | training/inference precision Not Disclosed uniformly | training tokens normalized by 160 tokens-per-parameter; RULER and paper long-context lengths | training tokens normalized by 160 tokens-per-parameter; RULER and paper long-context lengths | Not Disclosed consistently | single-model kernel and end-to-end measurements; online request concurrency Not Evaluated | No production SLO; loss, downstream accuracy, throughput and memory | iso-FLOP language modeling suite, RULER and author kernel profiling |
| SF-2026-ARXIV-2607-09786 | RL post-training with length penalties on mathematical/reasoning tasks | Qwen3-4B, Qwen3-14B and a Nemotron 9B check | two NVIDIA B200 GPUs per reported run | Not Disclosed | penalized chain-of-thought length; prompt/output distributions are task-specific | penalized chain-of-thought length; prompt/output distributions are task-specific | Not Disclosed | Not Disclosed | No serving SLO; evaluates accuracy and monitorability/disclosure | author probes plus judge rescoring on a limited subset |
| SF-2026-ARXIV-2607-07508 | agentic RL on tool-using math and SWE-bench-style tasks | Qwen3-30B-A3B | accelerator topology Not Disclosed sufficiently for normalized throughput comparison | Not Disclosed | maximum context 128k; up to 50 and 300 environment turns in listed regimes | maximum context 128k; up to 50 and 300 environment turns in listed regimes | Not Disclosed | asynchronous rollout generation and learner updates; exact worker count Not Disclosed | No serving SLO; sample efficiency, training throughput and task success | agentic math and SWE-bench-related evaluation, means over 16 or 4 runs as specified |
| SF-2026-ARXIV-2607-07534 | interactive streaming world/video generation | LingBot-World-v2 family as described by authors | author runtime setup; exact normalized accelerator contract Not Disclosed for all claims | Not Disclosed | author demonstrates long/hour-scale streaming; active model context remains finite | author demonstrates long/hour-scale streaming; active model context remains finite | interactive single-session demonstrations; batch Not Disclosed | Not Disclosed | author reports 720p/60fps interactive target; latency distribution and production SLO conformance Not Disclosed | author visual/interaction studies and demonstrations |
| SF-2026-ARXIV-2607-07608 | long-horizon robotic manipulation under partial observability | paper-defined VLA baselines and LaMem-VLA variants | training/inference hardware Not Disclosed sufficiently for reproducible latency comparison | Not Disclosed | task trajectories in SimplerEnv-Bridge and LIBERO; exact token/action-horizon distribution is benchmark-specific | task trajectories in SimplerEnv-Bridge and LIBERO; exact token/action-horizon distribution is benchmark-specific | Not Disclosed | single-agent policy evaluation; multi-robot concurrency Not Evaluated | No production control-frequency or safety SLO disclosed | SimplerEnv-Bridge and LIBERO success metrics plus memory ablations |
| SF-2026-ARXIV-2607-07702 | failure diagnosis and optimization over tool-using agent trajectories | paper-listed agent and evaluator models | Not Disclosed | Not Disclosed/Not Disclosed | benchmark trajectory lengths; distribution Not Disclosed consistently | benchmark trajectory lengths; distribution Not Disclosed consistently | Not Disclosed | Not Disclosed to offline diagnosis | No production SLO; diagnosis accuracy/utility and optimization outcomes | author agent benchmarks and judge/diagnosis protocol |
| SF-2026-ARXIV-2607-07820 | deep web-style search in an offline verifiable Wikipedia environment | Qwen3.5-9B learner with scaffold/teacher models as specified | one 8-GPU NVIDIA H20 node for training and a two-node H20 generation/training setup | BF16 | maximum training sequence 32,768; up to 30 agent steps | maximum training sequence 32,768; up to 30 agent steps | round-specific; exact normalized global batch is paper-defined | asynchronous generation/training across the reported H20 topology | No live-search SLO; task accuracy and training efficiency | paper deep-search benchmark suite with deterministic offline tools/verifiers |
| SF-2026-ARXIV-2607-07953 | controlled language-model pretraining and downstream evaluation of linear-attention families | 350M comparison suite plus 1.3B/3B and 15B-token scaling studies | four NVIDIA GH200 GPUs | BF16 | sequence length 4096 | sequence length 4096 | global batch 128 in the controlled setup | distributed training across four GPUs; serving concurrency Not Evaluated | No inference SLO; validation loss and downstream task quality | author controlled pretraining/downstream suite; routing experiments are primarily single runs |
| SF-2026-ARXIV-2607-07964 | post-training weight-only LLM quantization and batch-1 latency | LLaMA-2/LLaMA-3 families from 7B through 70B | NVIDIA A100; 70B BF16 uses two GPUs while W4 uses one GPU in the reported latency comparison | W2/W3/W4 quantization with BF16 baseline | calibration uses 128 WikiText2 samples of length 2048; latency sequence contract varies by table | calibration uses 128 WikiText2 samples of length 2048; latency sequence contract varies by table | batch 1 for reported latency | single-stream latency; online serving concurrency Not Evaluated | No production SLO; perplexity, downstream accuracy, calibration time and latency | WikiText2 perplexity and paper downstream suite |
| SF-2026-ARXIV-2607-08017 | multi-sample reasoning uncertainty/coherence evaluation | Llama-3.1-8B, Phi-4-14B and DeepSeek-R1-Distill-70B | Not Disclosed | Not Disclosed | 20 CoT samples per question, temperature 0.7, reasoning graphs of roughly 3-6 steps | 20 CoT samples per question, temperature 0.7, reasoning graphs of roughly 3-6 steps | Not Disclosed | offline evaluation; Not Applicable | No serving SLO; uncertainty ranking, coherence and robustness | GSM8K, BoolQ, StrategyQA, MedQA and GPQA; GPT-4o decomposer and Qwen3 embedding model |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-06925 | score_7_9;potential_books_delta | selected | DA-20260709-01 | — | V2=9/9；Exact v1 supports the causal concern that an answer-bearing instruction can let a dynamics model bypass transition learning, and that removing the goal improves the controlled grounding test. It does not establish general physical-world causality, long-horizon planning or deployment safety.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260709-01 |
| SF-2026-ARXIV-2607-06987 | score_7_9;potential_books_delta | selected | DA-20260709-02 | — | V2=8/9；Exact v1 proves the algebraic gradient contract and reports consistent gains in its experiments. It does not provide a general convergence theorem, public implementation equivalence or evidence outside the evaluated reasoning families.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260709-02 |
| SF-2026-ARXIV-2607-07046 | score_7_9;potential_books_delta | selected | DA-20260709-03 | — | V2=8/9；Exact v1 supports phase-specific, per-layer planning and boundary-safe runtime adaptation on its edge setup. It does not prove datacenter-scale behavior, arbitrary-network stability or that mixed precision preserves every task outside the measured evaluator set.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260709-03 |
| SF-2026-ARXIV-2607-07144 | score_7_9;potential_books_delta | not_selected | — | — | Complete integrable cold-tier refinement, but narrower than the three selected authority/control evolution units. | analysis-decision:SF-2026-ARXIV-2607-07144 |
| SF-2026-ARXIV-2607-07386 | score_7_9;potential_books_delta | not_selected | — | — | Despite its 9/9 score, this is a bounded model-internal capacity refinement whose current proof depends on HBM residence and immature kernels. Relative to unit 01's transition-authority correction, unit 02's optimization-control split and unit 03's boundary-safe execution-plan commit, it changes neither a cross-component correctness authority nor a deployment commit protocol; it remains fully reviewed and integrated as a focused Ch22 refinement. | analysis-decision:SF-2026-ARXIV-2607-07386 |
| SF-2026-ARXIV-2607-09786 | score_7_9;potential_books_delta | not_selected | — | — | Important monitorability trade-off, but replication and metric stability remain insufficient for a durable long-form conclusion. | analysis-decision:SF-2026-ARXIV-2607-09786 |
| SF-2026-ARXIV-2607-07508 | score_7_9;potential_books_delta | subsumed | — | DA-20260709-02 | Provides the independent rollout-freshness/single-rollout axis alongside UP's positive-update-capacity axis. | analysis:DA-20260709-02 |
| SF-2026-ARXIV-2607-07534 | score_7_9;potential_books_delta | not_selected | — | — | Full review closes an already-written generation-versus-persistent-world boundary; no new Books proposition remains. | analysis-decision:SF-2026-ARXIV-2607-07534 |
| SF-2026-ARXIV-2607-07608 | score_7_9;potential_books_delta | not_selected | — | — | Owner-correcting VLA memory delta is integrable, but it is a bounded chapter refinement rather than a broader cross-family analysis unit. | analysis-decision:SF-2026-ARXIV-2607-07608 |
| SF-2026-ARXIV-2607-07702 | score_7_9;potential_books_delta | not_selected | — | — | Exact mechanism is already covered by Ch69; this pass adds provenance, not a new narrative delta. | analysis-decision:SF-2026-ARXIV-2607-07702 |
| SF-2026-ARXIV-2607-07820 | score_7_9;potential_books_delta | not_selected | — | — | Exact mechanism is already covered by Ch81; this pass adds benchmark and evidence boundaries only. | analysis-decision:SF-2026-ARXIV-2607-07820 |
| SF-2026-ARXIV-2607-07953 | score_7_9;potential_books_delta | not_selected | — | — | Complete integrable representation-alignment correction, but kept in the candidate ledger to preserve the three-unit narrative limit. | analysis-decision:SF-2026-ARXIV-2607-07953 |
| SF-2026-ARXIV-2607-07964 | score_7_9;potential_books_delta | subsumed | — | DA-20260709-03 | Supplies the offline curvature-aware artifact branch before Voltron's runtime-revisable precision plan. | analysis:DA-20260709-03 |
| SF-2026-ARXIV-2607-08017 | score_7_9;potential_books_delta | not_selected | — | — | Complete evaluation-system delta, but graph consistency remains a bounded sensor rather than a new top-level truth contract. | analysis-decision:SF-2026-ARXIV-2607-08017 |

<!-- analysis:DA-20260709-01:start -->
### Grounding Spatial Relations in a Compact World Model: Instruction Leakage and a Goal-Free Dynamics Fix

**旧方案为何合理。** Ch25 separates video continuation from action-conditioned environment dynamics and hands planning to downstream policy, but it does not make instruction leakage an explicit authority failure.（现有命题定位：`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）

**约束变化与机制。** The baseline gives the transition model both the current scene/action and an instruction that directly names the spatial relation later used as the evaluation target. The model can therefore copy goal semantics rather than infer the environment transition. Removing goal identity from dynamics and keeping it in the planner's objective forces the learned transition to explain observation changes instead of receiving the answer-bearing variable. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `MULTIMODAL-WORLD-MODELS` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** The intervention identifies one leakage channel in a compact controlled setup. It does not prove that every goal-conditioned world model is ungrounded or that goal-free dynamics alone produces causal physical understanding.

<!-- analysis:DA-20260709-01:end -->

<!-- analysis:DA-20260709-02:start -->
### UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma

**旧方案为何合理。** Ch33 explains ratio clipping, DAPO-style asymmetric pressures and the exploration/stability trade-off, but still treats both ratio sides as variants of one stale-policy ratio.（现有命题定位：`books/part-04-training-system/33-grpo.md#L14-L14`）

**约束变化与机制。** For positive advantages, UP replaces the stale rollout ratio with πθ divided by a stop-gradient copy of itself. Its forward value is one while its gradient is the current-policy REINFORCE gradient, so the positive branch no longer hits the usual upper clipping ceiling. The negative branch retains a conventional bounded ratio/KL safeguard, making the change asymmetric rather than removing stability controls globally. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `TRAIN-GRPO` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** The evidence supports one asymmetric update branch on listed Qwen/task contracts. It does not prove that removing the positive clip is safe for every reward model, policy scale or off-policy delay.

**同一演进单元的 supporting branch：Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning。** Ch32 already owns the critic-stability branch; Ch33 already states rollout-policy identity, bounded freshness and one-rollout/asynchronous alternatives with explicit off-policy correction.

SAO uses one rollout per prompt, trains a value critic more frequently than the actor and corrects current-policy learning directly against the rollout policy. Tokens whose two-sided importance ratio leaves a trust interval are masked rather than allowed to dominate. This trades group-relative variance reduction for lower rollout cost and explicit staleness control. 它与主 family 的关系是：Provides the independent rollout-freshness/single-rollout axis alongside UP's positive-update-capacity axis.

证据边界与代价：The method depends on critic quality, behavior-probability integrity and bounded staleness. It does not eliminate off-policy failure or prove one rollout is sufficient for arbitrary sparse-reward agents.

<!-- analysis:DA-20260709-02:end -->

<!-- analysis:DA-20260709-03:start -->
### Voltron: Enabling Elastic Multi-Device Execution of LLM Inference for Empowered Edge Intelligence

**旧方案为何合理。** Ch49 owns compilation and execution-plan decisions, while Ch56 owns fleet admission/routing. Current text mostly treats precision and partitioning as build-time or deployment-time choices.（现有命题定位：`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）

**约束变化与机制。** Voltron first builds distinct per-layer execution plans for prefill and decode, choosing model/tensor parallel placement and precision according to layer/task sensitivity. At runtime it observes memory, KV growth and wireless conditions, then revises device participation, precision and pruning at token boundaries while preloading the next plan to hide reconfiguration. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-TENSORRT-LLM` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Author measurements depend on the six-device wireless topology and planner cost model. They do not establish universal speedups or safe runtime repartition on unrelated devices/networks.

**同一演进单元的 supporting branch：KronQ: LLM Quantization via Kronecker-Factored Hessian。** Ch49 discusses quantization as a build artifact and covers activation-aware/error-aware methods, but not output-gradient curvature as a separate sensitivity signal.

KronQ approximates second-order weight sensitivity as output-gradient covariance Kronecker activation covariance, then uses two-sided incoherence transforms and Hessian-trace sensitivity for mixed-bit allocation. After preprocessing, the output-gradient factor cancels from the column update algebra, but it still influences the transformed representation and layer sensitivity decision. 它与主 family 的关系是：Supplies the offline curvature-aware artifact branch before Voltron's runtime-revisable precision plan.

证据边界与代价：The 70B BF16-versus-W4 hardware count is not apples-to-apples. Calibration adds roughly 8-11 seconds per layer and temporary H_G memory, and accuracy gains do not guarantee serving speed.

<!-- analysis:DA-20260709-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-07144:start -->《Fractal KV-Cache Archives: Lossless Symbolic Storage with In-Place Retrieval for Long-Context LLM Inference》已完成 Deep Source Review。Complete integrable cold-tier refinement, but narrower than the three selected authority/control evolution units.<!-- analysis-decision:SF-2026-ARXIV-2607-07144:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-07386:start -->《Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity》已完成 Deep Source Review。Despite its 9/9 score, this is a bounded model-internal capacity refinement whose current proof depends on HBM residence and immature kernels. Relative to unit 01's transition-authority correction, unit 02's optimization-control split and unit 03's boundary-safe execution-plan commit, it changes neither a cross-component correctness authority nor a deployment commit protocol; it remains fully reviewed and integrated as a focused Ch22 refinement.<!-- analysis-decision:SF-2026-ARXIV-2607-07386:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09786:start -->《Length Penalties Make Chain-of-Thought Less Monitorable》已完成 Deep Source Review。Important monitorability trade-off, but replication and metric stability remain insufficient for a durable long-form conclusion.<!-- analysis-decision:SF-2026-ARXIV-2607-09786:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-07508:start -->《Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning》已完成 Deep Source Review。本 family 已作为 supporting evidence 纳入 `DA-20260709-02`：Provides the independent rollout-freshness/single-rollout axis alongside UP's positive-update-capacity axis.<!-- analysis-decision:SF-2026-ARXIV-2607-07508:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-07534:start -->《Infinite Worlds with Versatile Interactions》已完成 Deep Source Review。Full review closes an already-written generation-versus-persistent-world boundary; no new Books proposition remains.<!-- analysis-decision:SF-2026-ARXIV-2607-07534:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-07608:start -->《LaMem-VLA: Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation》已完成 Deep Source Review。Owner-correcting VLA memory delta is integrable, but it is a bounded chapter refinement rather than a broader cross-family analysis unit.<!-- analysis-decision:SF-2026-ARXIV-2607-07608:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-07702:start -->《From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization》已完成 Deep Source Review。Exact mechanism is already covered by Ch69; this pass adds provenance, not a new narrative delta.<!-- analysis-decision:SF-2026-ARXIV-2607-07702:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-07820:start -->《DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment》已完成 Deep Source Review。Exact mechanism is already covered by Ch81; this pass adds benchmark and evidence boundaries only.<!-- analysis-decision:SF-2026-ARXIV-2607-07820:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-07953:start -->《Linear Attention Architectures: Mechanisms, Trade-offs, and Cross-Layer Routing》已完成 Deep Source Review。Complete integrable representation-alignment correction, but kept in the candidate ledger to preserve the three-unit narrative limit.<!-- analysis-decision:SF-2026-ARXIV-2607-07953:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-07964:start -->《KronQ: LLM Quantization via Kronecker-Factored Hessian》已完成 Deep Source Review。本 family 已作为 supporting evidence 纳入 `DA-20260709-03`：Supplies the offline curvature-aware artifact branch before Voltron's runtime-revisable precision plan.<!-- analysis-decision:SF-2026-ARXIV-2607-07964:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08017:start -->《Can We Trust LLM's Logic? Quantifying Uncertainty, Coherence, and Robustness via a Graph-Based Framework》已完成 Deep Source Review。Complete evaluation-system delta, but graph consistency remains a bounded sensor rather than a new top-level truth contract.<!-- analysis-decision:SF-2026-ARXIV-2607-08017:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-06925 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L111 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-06925 | delta:SF-2026-ARXIV-2607-06925 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-06925 |
| SF-2026-ARXIV-2607-06987 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L151 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-06987 | delta:SF-2026-ARXIV-2607-06987 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-06987 |
| SF-2026-ARXIV-2607-07046 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L41 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-07046 | delta:SF-2026-ARXIV-2607-07046 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-07046 |
| SF-2026-ARXIV-2607-07144 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L508 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-07144 | delta:SF-2026-ARXIV-2607-07144 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-07144 |
| SF-2026-ARXIV-2607-07386 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L374 | books/part-02-model/21-moe.md#L14-L14; books/part-03-multimodal-world-models/23-multimodal-representation.md#L14-L14 | existing:SF-2026-ARXIV-2607-07386 | delta:SF-2026-ARXIV-2607-07386 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-07386 |
| SF-2026-ARXIV-2607-07508 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L14-L14 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-07508 | delta:SF-2026-ARXIV-2607-07508 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-07508 |
| SF-2026-ARXIV-2607-07534 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-07534 | delta:SF-2026-ARXIV-2607-07534 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-07534 |
| SF-2026-ARXIV-2607-07608 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L181 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-07608 | delta:SF-2026-ARXIV-2607-07608 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-07608 |
| SF-2026-ARXIV-2607-07702 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L14-L14 | books/part-06-ai-infrastructure/68-logging.md#L14-L14; books/part-06-ai-infrastructure/70-cost.md#L14-L14 | existing:SF-2026-ARXIV-2607-07702 | delta:SF-2026-ARXIV-2607-07702 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-07702 |
| SF-2026-ARXIV-2607-07820 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L14-L14 | books/part-07-agent/80-reflection.md#L14-L14; books/part-07-agent/82-multi-agent.md#L14-L14 | existing:SF-2026-ARXIV-2607-07820 | delta:SF-2026-ARXIV-2607-07820 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-07820 |
| SF-2026-ARXIV-2607-07953 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L180 | books/part-02-model/21-moe.md#L14-L14; books/part-03-multimodal-world-models/23-multimodal-representation.md#L14-L14 | existing:SF-2026-ARXIV-2607-07953 | delta:SF-2026-ARXIV-2607-07953 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-07953 |
| SF-2026-ARXIV-2607-07964 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L475 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-07964 | delta:SF-2026-ARXIV-2607-07964 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-07964 |
| SF-2026-ARXIV-2607-08017 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L953 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-08017 | delta:SF-2026-ARXIV-2607-08017 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-08017 |

<!-- books-review:SF-2026-ARXIV-2607-06925:start --><!-- existing:SF-2026-ARXIV-2607-06925:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L111` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-06925:end --><!-- delta:SF-2026-ARXIV-2607-06925:start -->新增证据边界：The baseline gives the transition model both the current scene/action and an instruction that directly names the spatial relation later used as the evaluation target. The model can therefore copy goal semantics rather than infer the environment transition. Removing goal identity from dynamics and keeping it in the planner's objective forces the learned transition to explain observation changes instead of receiving the answer-bearing variable. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L111`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-06925:end --><!-- books-review:SF-2026-ARXIV-2607-06925:end -->

<!-- books-review:SF-2026-ARXIV-2607-06987:start --><!-- existing:SF-2026-ARXIV-2607-06987:start -->对读 `books/part-04-training-system/33-grpo.md#L151` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-06987:end --><!-- delta:SF-2026-ARXIV-2607-06987:start -->新增证据边界：For positive advantages, UP replaces the stale rollout ratio with πθ divided by a stop-gradient copy of itself. Its forward value is one while its gradient is the current-policy REINFORCE gradient, so the positive branch no longer hits the usual upper clipping ceiling. The negative branch retains a conventional bounded ratio/KL safeguard, making the change asymmetric rather than removing stability controls globally. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L151`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-06987:end --><!-- books-review:SF-2026-ARXIV-2607-06987:end -->

<!-- books-review:SF-2026-ARXIV-2607-07046:start --><!-- existing:SF-2026-ARXIV-2607-07046:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L41` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-07046:end --><!-- delta:SF-2026-ARXIV-2607-07046:start -->新增证据边界：Voltron first builds distinct per-layer execution plans for prefill and decode, choosing model/tensor parallel placement and precision according to layer/task sensitivity. At runtime it observes memory, KV growth and wireless conditions, then revises device participation, precision and pruning at token boundaries while preloading the next plan to hide reconfiguration. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L41`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-07046:end --><!-- books-review:SF-2026-ARXIV-2607-07046:end -->

<!-- books-review:SF-2026-ARXIV-2607-07144:start --><!-- existing:SF-2026-ARXIV-2607-07144:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L508` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-07144:end --><!-- delta:SF-2026-ARXIV-2607-07144:start -->新增证据边界：A lossy feed quantizer first maps KV into symbol codes; a contractive symbolic map then serializes that quantized code stream into an archive with periodic anchors. The archive is lossless only relative to the codes, supports append and position access without decoding the whole prefix, and can serve as a structural suffix-similarity index. It does not reconstruct the original FP16 KV without quantization error. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L508`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-07144:end --><!-- books-review:SF-2026-ARXIV-2607-07144:end -->

<!-- books-review:SF-2026-ARXIV-2607-07386:start --><!-- existing:SF-2026-ARXIV-2607-07386:start -->对读 `books/part-02-model/22-long-context.md#L374` 与相邻章节后，现有命题（`books/part-02-model/22-long-context.md#L14-L14`）为：本章的核心判断是：**Long Context 是位置有效性、Attention 计算、KV Cache 容量、信息利用与系统 SLO 的联合能力。**任何只移动一个瓶颈的方案，都不能自动得到可用的长上下文系统。<!-- existing:SF-2026-ARXIV-2607-07386:end --><!-- delta:SF-2026-ARXIV-2607-07386:start -->新增证据边界：Sparse Delta Memory replaces a fixed dense recurrent matrix with an explicit N-by-d memory table. Product keys choose a small write set and read set, and a gated delta rule changes only selected slots. Increasing N expands addressable state without increasing per-token arithmetic proportionally, but the physical table grows and leaves fast on-chip memory. 该 delta 已进入 `books/part-02-model/22-long-context.md#L374`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-07386:end --><!-- books-review:SF-2026-ARXIV-2607-07386:end -->

<!-- books-review:SF-2026-ARXIV-2607-07508:start --><!-- existing:SF-2026-ARXIV-2607-07508:start -->对读 `books/part-04-training-system/33-grpo.md#L14-L14` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-07508:end --><!-- delta:SF-2026-ARXIV-2607-07508:start -->新增证据边界：SAO uses one rollout per prompt, trains a value critic more frequently than the actor and corrects current-policy learning directly against the rollout policy. Tokens whose two-sided importance ratio leaves a trust interval are masked rather than allowed to dominate. This trades group-relative variance reduction for lower rollout cost and explicit staleness control. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-07508:end --><!-- books-review:SF-2026-ARXIV-2607-07508:end -->

<!-- books-review:SF-2026-ARXIV-2607-07534:start --><!-- existing:SF-2026-ARXIV-2607-07534:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-07534:end --><!-- delta:SF-2026-ARXIV-2607-07534:start -->新增证据边界：The system streams causally generated video chunks conditioned on user interactions, then uses few-step distillation and a runtime harness to sustain low-latency continuation. It can generate a long visual experience, but places that leave the active context are regenerated rather than retrieved from a canonical persistent environment state. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-07534:end --><!-- books-review:SF-2026-ARXIV-2607-07534:end -->

<!-- books-review:SF-2026-ARXIV-2607-07608:start --><!-- existing:SF-2026-ARXIV-2607-07608:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L181` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-07608:end --><!-- delta:SF-2026-ARXIV-2607-07608:start -->新增证据边界：LaMem-VLA keeps a short latent vault for immediate task progress and a compressed long vault for older observations, with a curator deciding what moves between them. Memory tokens are woven into action prediction rather than retrieved as text, giving the policy an internal state estimate across partially observed manipulation trajectories. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L181`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-07608:end --><!-- books-review:SF-2026-ARXIV-2607-07608:end -->

<!-- books-review:SF-2026-ARXIV-2607-07702:start --><!-- existing:SF-2026-ARXIV-2607-07702:start -->对读 `books/part-06-ai-infrastructure/69-trace.md#L14-L14` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/69-trace.md#L14-L14`）为：本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。**<!-- existing:SF-2026-ARXIV-2607-07702:end --><!-- delta:SF-2026-ARXIV-2607-07702:start -->新增证据边界：STRACE converts noisy agent trajectories into typed dependency graphs, then slices backward from a failed outcome to isolate the minimal relevant action/observation chain and propose root-cause candidates. Structural compression improves diagnostic focus, but a graph reconstructed from observations remains evidence for dependency, not proof of intervention-level causality. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-07702:end --><!-- books-review:SF-2026-ARXIV-2607-07702:end -->

<!-- books-review:SF-2026-ARXIV-2607-07820:start --><!-- existing:SF-2026-ARXIV-2607-07820:start -->对读 `books/part-07-agent/81-workflow.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/81-workflow.md#L14-L14`）为：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2607-07820:end --><!-- delta:SF-2026-ARXIV-2607-07820:start -->新增证据边界：The method builds a deterministic offline search environment whose answers can be verified, uses a stronger scaffold to create and reject trajectories, then alternates self-generated data with SFT across explicit rounds. Generation and learning may overlap inside a round, but the round boundary freezes the policy/data contract before the next promotion. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-07820:end --><!-- books-review:SF-2026-ARXIV-2607-07820:end -->

<!-- books-review:SF-2026-ARXIV-2607-07953:start --><!-- existing:SF-2026-ARXIV-2607-07953:start -->对读 `books/part-02-model/22-long-context.md#L180` 与相邻章节后，现有命题（`books/part-02-model/22-long-context.md#L14-L14`）为：本章的核心判断是：**Long Context 是位置有效性、Attention 计算、KV Cache 容量、信息利用与系统 SLO 的联合能力。**任何只移动一个瓶颈的方案，都不能自动得到可用的长上下文系统。<!-- existing:SF-2026-ARXIV-2607-07953:end --><!-- delta:SF-2026-ARXIV-2607-07953:start -->新增证据边界：A common recurrent form exposes where DeltaNet/GDN/Kimi-like architectures differ in decay, update and gating rather than treating names as incomparable systems. Cross-layer error routing fails when a write residual is injected into a basis that does not share its representation; CLVR first projects the write value into an aligned hidden stream, making the added route semantically compatible. 该 delta 已进入 `books/part-02-model/22-long-context.md#L180`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-07953:end --><!-- books-review:SF-2026-ARXIV-2607-07953:end -->

<!-- books-review:SF-2026-ARXIV-2607-07964:start --><!-- existing:SF-2026-ARXIV-2607-07964:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L475` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-07964:end --><!-- delta:SF-2026-ARXIV-2607-07964:start -->新增证据边界：KronQ approximates second-order weight sensitivity as output-gradient covariance Kronecker activation covariance, then uses two-sided incoherence transforms and Hessian-trace sensitivity for mixed-bit allocation. After preprocessing, the output-gradient factor cancels from the column update algebra, but it still influences the transformed representation and layer sensitivity decision. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L475`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-07964:end --><!-- books-review:SF-2026-ARXIV-2607-07964:end -->

<!-- books-review:SF-2026-ARXIV-2607-08017:start --><!-- existing:SF-2026-ARXIV-2607-08017:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L953` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-08017:end --><!-- delta:SF-2026-ARXIV-2607-08017:start -->新增证据边界：GraphEVAL samples multiple chains of thought, uses a separate deterministic decomposer to turn each into a claimed causal DAG, and compares semantic/structural graph distance. A graph medoid and GRCS features measure agreement and robustness; an adversarial-medoid intervention tests whether the selector merely follows a central but wrong trace. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L953`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-08017:end --><!-- books-review:SF-2026-ARXIV-2607-08017:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260709-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260709; semantic-review:SA-20260709-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260709-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-06925; review:SF-2026-ARXIV-2607-06987; review:SF-2026-ARXIV-2607-07046; review:SF-2026-ARXIV-2607-07144; review:SF-2026-ARXIV-2607-07386; review:SF-2026-ARXIV-2607-09786; review:SF-2026-ARXIV-2607-07508; review:SF-2026-ARXIV-2607-07534; review:SF-2026-ARXIV-2607-07608; review:SF-2026-ARXIV-2607-07702; review:SF-2026-ARXIV-2607-07820; review:SF-2026-ARXIV-2607-07953; review:SF-2026-ARXIV-2607-07964; review:SF-2026-ARXIV-2607-08017; semantic-review:SA-20260709-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260709-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260709-01; analysis:DA-20260709-02; analysis:DA-20260709-03; semantic-review:SA-20260709-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260709-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-06925; books-review:SF-2026-ARXIV-2607-06987; books-review:SF-2026-ARXIV-2607-07046; books-review:SF-2026-ARXIV-2607-07144; books-review:SF-2026-ARXIV-2607-07386; books-review:SF-2026-ARXIV-2607-07508; books-review:SF-2026-ARXIV-2607-07534; books-review:SF-2026-ARXIV-2607-07608; books-review:SF-2026-ARXIV-2607-07702; books-review:SF-2026-ARXIV-2607-07820; books-review:SF-2026-ARXIV-2607-07953; books-review:SF-2026-ARXIV-2607-07964; books-review:SF-2026-ARXIV-2607-08017; review:SF-2026-ARXIV-2607-09786; semantic-review:SA-20260709-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260709-COVERAGE:start -->Fresh-context review reconciled the exact window, partition totals, date bucket and denominator.<!-- semantic-review:SA-20260709-COVERAGE:end -->
<!-- semantic-review:SA-20260709-EVIDENCE:start -->Fresh-context review reconciled all 14 frozen families: 14 Deep, 0 Standard and 0 Closure; 0 pending and 0 blocked rows remain explicitly outside mechanism claims.<!-- semantic-review:SA-20260709-EVIDENCE:end -->
<!-- semantic-review:SA-20260709-SELECTION:start -->Fresh-context review reconciled 14 eligible Deep families: 3 selected and 11 not selected; the narrative limit does not downgrade any completed Source Review.<!-- semantic-review:SA-20260709-SELECTION:end -->
<!-- semantic-review:SA-20260709-BOOKS:start -->Fresh-context review checked current owner and adjacent chapter handoffs; 9 个 family 已定位到实际 Books 段落，4 个 family 的 No Change 结论可定位，1 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。<!-- semantic-review:SA-20260709-BOOKS:end -->

## 8. Ignored Noise

1148 个窗口内 identity 中，1134 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：9 个 `Integrate`，4 个 `No Change — Existing Coverage`，1 个 `Weekly Only — Context`，0 个 `Rejected — Low Durability / Out of Scope`；Deep 14 / Standard 0。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/09/README.md`。
- 本日报长期 delta 已同步至：`books/part-02-model/22-long-context.md`、`books/part-03-multimodal-world-models/25-multimodal-world-models.md`、`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`、`books/part-04-training-system/33-grpo.md`、`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`、`books/part-05-inference-system/49-tensorrt-llm.md`、`books/part-06-ai-infrastructure/66-evaluation-system.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [Grounding Spatial Relations in a Compact World Model: Instruction Leakage and a Goal-Free Dynamics Fix](https://arxiv.org/abs/2607.06925v1) — first-public（Asia/Shanghai）：2026-07-08；accessed：2026-08-27
- [UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma](https://arxiv.org/abs/2607.06987v1) — first-public（Asia/Shanghai）：2026-07-08；accessed：2026-08-27
- [Voltron: Enabling Elastic Multi-Device Execution of LLM Inference for Empowered Edge Intelligence](https://arxiv.org/abs/2607.07046v1) — first-public（Asia/Shanghai）：2026-07-08；accessed：2026-08-27
- [Fractal KV-Cache Archives: Lossless Symbolic Storage with In-Place Retrieval for Long-Context LLM Inference](https://arxiv.org/abs/2607.07144v1) — first-public（Asia/Shanghai）：2026-07-08；accessed：2026-08-27
- [Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity](https://arxiv.org/abs/2607.07386v1) — first-public（Asia/Shanghai）：2026-07-08；accessed：2026-08-27
- [Length Penalties Make Chain-of-Thought Less Monitorable](https://arxiv.org/abs/2607.09786v1) — first-public（Asia/Shanghai）：2026-07-08；accessed：2026-08-27
- [Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.07508v1) — first-public（Asia/Shanghai）：2026-07-08；accessed：2026-08-27
- [Infinite Worlds with Versatile Interactions](https://arxiv.org/abs/2607.07534v1) — first-public（Asia/Shanghai）：2026-07-08；accessed：2026-08-27
- [LaMem-VLA: Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2607.07608v1) — first-public（Asia/Shanghai）：2026-07-09；accessed：2026-08-27
- [From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization](https://arxiv.org/abs/2607.07702v1) — first-public（Asia/Shanghai）：2026-07-09；accessed：2026-08-27
- [DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment](https://arxiv.org/abs/2607.07820v1) — first-public（Asia/Shanghai）：2026-07-09；accessed：2026-08-27
- [Linear Attention Architectures: Mechanisms, Trade-offs, and Cross-Layer Routing](https://arxiv.org/abs/2607.07953v1) — first-public（Asia/Shanghai）：2026-07-09；accessed：2026-08-27
- [KronQ: LLM Quantization via Kronecker-Factored Hessian](https://arxiv.org/abs/2607.07964v1) — first-public（Asia/Shanghai）：2026-07-09；accessed：2026-08-27
- [Can We Trust LLM's Logic? Quantifying Uncertainty, Coherence, and Robustness via a Graph-Based Framework](https://arxiv.org/abs/2607.08017v1) — first-public（Asia/Shanghai）：2026-07-09；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
