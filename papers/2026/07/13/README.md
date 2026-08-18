# Daily Research — 2026-07-13

**Research Date:** 2026-07-13

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-12 09:00:00 ～ 2026-07-13 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 489 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 4 个。当前路由账目为 3 个 Deep、0 个 Standard、1 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-13 |
| Window End | 2026-07-13 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-13-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T15:02:18+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-12T09:00:00+08:00 | 2026-07-13T09:00:00+08:00 | 2026-08-27T15:02:18+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 489 | SF-2026-ARXIV-2607-10532<br>SF-2026-ARXIV-2607-10582<br>SF-2026-ARXIV-2607-10599<br>SF-2026-ARXIV-2607-10709 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-13T09:00:00+08:00 | coverage:SRC-ARXIV:20260713 | GAP-ARXIV-DIRECT-RESET-20260713 |
| SRC-GITHUB-COMMIT | 2026-07-12T09:00:00+08:00 | 2026-07-13T09:00:00+08:00 | 2026-08-27T15:02:18+08:00 | exact GitHub commit API lookups: venkateshamatam/memdecay@ab8ad3f66b3445e07f19422fd046fdbabd5571e9 | checked | 1 | SF-2026-ARXIV-2607-10582 | pages=1; final cursors=ab8ad3f66b3445e07f19422fd046fdbabd5571e9; one bounded commit lookup per family | 2026-07-13T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260713 | — |

<!-- coverage:SRC-ARXIV:20260713:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 489 unique identities in this strict window; 4 routed families.<!-- coverage:SRC-ARXIV:20260713:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260713:start -->repository=venkateshamatam/memdecay, until=2026-07-13T01:00:00Z, full_sha=ab8ad3f66b3445e07f19422fd046fdbabd5571e9, commit_timestamp=2026-07-11T15:54:02Z, url=https://github.com/venkateshamatam/memdecay/commit/ab8ad3f66b3445e07f19422fd046fdbabd5571e9; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260713:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 4 个 family：exact v1 为 1 个 family 披露 artifact/evidence locator，其中 1 个提供外部 repository/project/demo locator，另有 3 个未披露；本日确认 1 个 family、1 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10532 | arXiv:2607.10532v1 | paper-v1:2607.10532 | 2026-W28 | 2026-07-12 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-10532 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-10582 | arXiv:2607.10582v1 | paper-v1:2607.10582 | 2026-W28 | 2026-07-12 | SRC-ARXIV; SRC-GITHUB-COMMIT | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10582 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-10582 | yes |
| SF-2026-ARXIV-2607-10599 | arXiv:2607.10599v1 | paper-v1:2607.10599 | 2026-W28 | 2026-07-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2607-10599 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Integrate | books-review:SF-2026-ARXIV-2607-10599 | yes |
| SF-2026-ARXIV-2607-10709 | arXiv:2607.10709v1 | paper-v1:2607.10709 | 2026-W28 | 2026-07-12 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2607-10709 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607-10709 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10532 | RP-e7097e737fcf8cf8 | closure | doi:10.48550/arxiv.2607.10532@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.10532@v1 | doi:10.48550/arxiv.2607.10532#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-10532 | complete |
| SF-2026-ARXIV-2607-10582 | RP-de7e99003d9edef9 | deep | arXiv:2607.10582v1 | SRC-ARXIV@arXiv:2607.10582v1; SRC-GITHUB-COMMIT@commit:ab8ad3f66b3445e07f19422fd046fdbabd5571e9 | https://arxiv.org/html/2607.10582v1#S3.SS2 — structural priors; https://arxiv.org/html/2607.10582v1#S3.SS3 — calibrated region decay and attention refresh; https://arxiv.org/html/2607.10582v1#S3.SS4 — page-granularity eviction; https://arxiv.org/html/2607.10582v1#S3.SS5 — scope and tiered extension | https://arxiv.org/html/2607.10582v1#S4.SS1 — setup; https://arxiv.org/html/2607.10582v1#S4.SS2 — lifetime measurement; https://arxiv.org/html/2607.10582v1#S4.SS3 — budgeted recall; https://arxiv.org/html/2607.10582v1#S4.SS4 — sensitivity and overhead | https://arxiv.org/html/2607.10582v1#S5 — discussion, negative results and limitations | https://github.com/venkateshamatam/memdecay/commit/ab8ad3f66b3445e07f19422fd046fdbabd5571e9 | claim:SF-2026-ARXIV-2607-10582 | complete |
| SF-2026-ARXIV-2607-10599 | RP-623c3ccc07b51ad3 | deep | arXiv:2607.10599v1 | SRC-ARXIV@arXiv:2607.10599v1 | https://arxiv.org/html/2607.10599v1#S3.SS2 — modality-invariant alignment; https://arxiv.org/html/2607.10599v1#S3.SS3 — multi-granularity routing and leave-one-out supervision; https://arxiv.org/html/2607.10599v1#S3.SS4 — inverse-variance uncertainty-aware fusion; https://arxiv.org/html/2607.10599v1#S3.SS5 — prediction and training objective | https://arxiv.org/html/2607.10599v1#S4.SS1 — datasets; https://arxiv.org/html/2607.10599v1#S4.SS3 — implementation; https://arxiv.org/html/2607.10599v1#S4.SS4 — efficiency; https://arxiv.org/html/2607.10599v1#S4.SS6 — ablations; https://arxiv.org/html/2607.10599v1#S4.SS7 — controlled perturbations; https://arxiv.org/html/2607.10599v1#S4.SS8 — uncertainty/gate mechanism analysis | https://arxiv.org/html/2607.10599v1#S4.SS7 — severe perturbation does not always improve MAE; https://arxiv.org/html/2607.10599v1#S5 — training-cost and future-work boundary | Not Disclosed — exact v1 links no author repository, immutable implementation or checkpoint | claim:SF-2026-ARXIV-2607-10599 | complete |
| SF-2026-ARXIV-2607-10709 | RP-74184157b907c022 | deep | arXiv:2607.10709v1 | SRC-ARXIV@arXiv:2607.10709v1 | https://arxiv.org/html/2607.10709v1#S3.SS2 — threat model; https://arxiv.org/html/2607.10709v1#S4.SS2 — direct and contextual privacy scoring; https://arxiv.org/html/2607.10709v1#S4.SS3 — pairwise utility dependency; https://arxiv.org/html/2607.10709v1#S4.SS4 — constrained sanitization; https://arxiv.org/html/2607.10709v1#S4.SS5 — local restoration | https://arxiv.org/html/2607.10709v1#S5.SS1 — setup, models, datasets, baselines and metrics; https://arxiv.org/html/2607.10709v1#S5.SS2 — privacy/utility results, attacks, ablations, sensitivity and overhead | https://arxiv.org/html/2607.10709v1#S3.SS2 — honest-but-curious single-turn threat model; https://arxiv.org/html/2607.10709v1#S6 — multi-turn extension remains future work | Not Disclosed — exact v1 links no author implementation; the CodeAlpaca GitHub citation is a dataset source, not PromptGraph provenance | claim:SF-2026-ARXIV-2607-10709 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-10532:start -->
#### Implicit Fine-tuning via Context Engineering: A Curriculum Learning Framework for Multimodal Entity Alignment

<!-- claim:SF-2026-ARXIV-2607-10532:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-10532:end -->

- Identity：`arXiv:2607.10532v1`；first-public（Asia/Shanghai）：`2026-07-12`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-10532:end -->

<!-- review:SF-2026-ARXIV-2607-10582:start -->
#### MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference

<!-- claim:SF-2026-ARXIV-2607-10582:start -->The paper supports region-dependent attention lifetimes, interpretable pinned retention and its synthetic budgeted-recall/overhead results. It also reports that the unnormalized attention term was much smaller than the structural term and that accumulated-attention retention beat MemDecay on unpinned recall at larger scale. It does not prove production long-context Agent quality or tail-SLO gains. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-10582:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** An Agent orchestrator supplies typed semantic region labels and explicit pinning policy; the inference runtime combines those priors with calibrated decay and observed attention to make page-level KV eviction decisions. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.10582v1#S3.SS2 — structural priors; https://arxiv.org/html/2607.10582v1#S3.SS3 — calibrated region decay and attention refresh; https://arxiv.org/html/2607.10582v1#S3.SS4 — page-granularity eviction; https://arxiv.org/html/2607.10582v1#S3.SS5 — scope and tiered extension`；Evaluation：`https://arxiv.org/html/2607.10582v1#S4.SS1 — setup; https://arxiv.org/html/2607.10582v1#S4.SS2 — lifetime measurement; https://arxiv.org/html/2607.10582v1#S4.SS3 — budgeted recall; https://arxiv.org/html/2607.10582v1#S4.SS4 — sensitivity and overhead`；Limitations/Counterevidence：`https://arxiv.org/html/2607.10582v1#S5 — discussion, negative results and limitations`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 3 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-10582:end -->

<!-- review:SF-2026-ARXIV-2607-10599:start -->
#### MRUF: Multi-granularity Routing with Uncertainty-Aware Fusion for Robust Multimodal Sentiment Analysis

<!-- claim:SF-2026-ARXIV-2607-10599:start -->The source supports this mechanism and its MOSI/MOSEI author experiments, ablations and perturbation tests. Predicted uncertainty is a learned reliability sensor, not a probability that a modality is true, and the results do not establish broad multimodal robustness or production behavior. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-10599:end -->

**旧方案与约束变化。** `本章的核心判断是：**多模态系统的第一问题不是把所有输入变成同一 shape，而是建立可版本化的 representation contract：每个表示必须保留它来自哪种 modality、对应什么时间与空间范围、经过哪个 encoder/codec、属于哪个 artifact version，并明确哪些信息已经不可逆地丢失。**共享 backbone 可以统一计算接口，却不会自动统一语义、采样率、误差模型和数据权利。`（`books/part-03-multimodal-world-models/23-multimodal-representation.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Separate task contribution from observation reliability: a contribution router is supervised by leave-one-out task degradation, while a distinct uncertainty head predicts modality-wise log variance and inverse-variance weights calibrate the final fusion gate. 它改变 `MULTIMODAL-REPRESENTATION` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.10599v1#S3.SS2 — modality-invariant alignment; https://arxiv.org/html/2607.10599v1#S3.SS3 — multi-granularity routing and leave-one-out supervision; https://arxiv.org/html/2607.10599v1#S3.SS4 — inverse-variance uncertainty-aware fusion; https://arxiv.org/html/2607.10599v1#S3.SS5 — prediction and training objective`；Evaluation：`https://arxiv.org/html/2607.10599v1#S4.SS1 — datasets; https://arxiv.org/html/2607.10599v1#S4.SS3 — implementation; https://arxiv.org/html/2607.10599v1#S4.SS4 — efficiency; https://arxiv.org/html/2607.10599v1#S4.SS6 — ablations; https://arxiv.org/html/2607.10599v1#S4.SS7 — controlled perturbations; https://arxiv.org/html/2607.10599v1#S4.SS8 — uncertainty/gate mechanism analysis`；Limitations/Counterevidence：`https://arxiv.org/html/2607.10599v1#S4.SS7 — severe perturbation does not always improve MAE; https://arxiv.org/html/2607.10599v1#S5 — training-cost and future-work boundary`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-REPRESENTATION`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-10599:end -->

<!-- review:SF-2026-ARXIV-2607-10709:start -->
#### PromptGraph: Graph-Guided Prompt Sanitization for Balancing Privacy and Utility in LLM Inference

<!-- claim:SF-2026-ARXIV-2607-10709:start -->The paper supports this single-turn honest-but-curious design and its MedQA/SAMSum/CodeAlpaca author experiments. It does not prove Differential Privacy, anonymity, compliance, adaptive-attacker resistance or production latency, and it does not disclose the exact local estimator, hardware or precision. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-10709:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Move prompt privacy from independent PII-span masking to a client-owned graph that estimates contextual attribute leakage and pairwise utility dependencies, selects a privacy/utility cut, sends opaque placeholders, and restores only exact consistency-checked identifiers locally. 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.10709v1#S3.SS2 — threat model; https://arxiv.org/html/2607.10709v1#S4.SS2 — direct and contextual privacy scoring; https://arxiv.org/html/2607.10709v1#S4.SS3 — pairwise utility dependency; https://arxiv.org/html/2607.10709v1#S4.SS4 — constrained sanitization; https://arxiv.org/html/2607.10709v1#S4.SS5 — local restoration`；Evaluation：`https://arxiv.org/html/2607.10709v1#S5.SS1 — setup, models, datasets, baselines and metrics; https://arxiv.org/html/2607.10709v1#S5.SS2 — privacy/utility results, attacks, ablations, sensitivity and overhead`；Limitations/Counterevidence：`https://arxiv.org/html/2607.10709v1#S3.SS2 — honest-but-curious single-turn threat model; https://arxiv.org/html/2607.10709v1#S6 — multi-turn extension remains future work`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 3 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-10709:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10582 | Controlled synthetic Agent episodes with region-labelled prompts and post-eviction recall probes | Qwen2.5-1.5B-Instruct and Qwen2.5-3B-Instruct | Apple M3 Pro for 1.5B float32; NVIDIA T4 for 3B float16 | float32 on M3 Pro; float16 on T4 | 405-507 cached tokens for short episodes; 1656-1723 for long episodes | Greedy 16-token recall probes | 24 episodes from 8 scenarios x 3 variants; 96 probes per configuration cell | No online serving concurrency | No production SLO; direct component overhead is reported for a 466-token cache | Budgeted exact recall, lifetime fits, ablation, cluster bootstrap and paired scenario comparisons; 4320 scored probes |
| SF-2026-ARXIV-2607-10599 | Multimodal sentiment analysis under aligned/unaligned inputs and controlled text masking/modality removal | MRUF on the paper's DMD-style decoupling-distillation backbone with BERT text, FACET vision and COVAREP audio features | Single NVIDIA Tesla T4 16GB | Not Disclosed | CMU-MOSI/MOSEI utterance sequences; exact token/frame lengths Not Disclosed | Sentiment classification/regression output | Batch size 16; best validation checkpoint; three random seeds | Offline evaluation; no serving concurrency | No production SLO; on aligned MOSEI the paper reports 539.3 s/training epoch and about 150.7 ms/test batch | ACC7, ACC2, F1 and MAE on standard MOSI/MOSEI splits; author baseline/ablation/perturbation contract |
| SF-2026-ARXIV-2607-10709 | Privacy-preserving cloud LLM inference for medical QA, dialogue summarization and code generation | Llama-3.1-8B, Mistral-7B and Qwen3-8B downstream models; exact local privacy estimator identity Not Disclosed | Not Disclosed | Not Disclosed | Dataset prompts plus 64-256-span scaling study; token lengths Not Disclosed | Task dependent; Not Disclosed | Offline evaluation; batch Not Disclosed | Not Disclosed | No production SLO; preprocessing time and peak incremental memory are measured, reaching about 1.1 s and 6 MB at 256 spans | PHR, recovery ASR, attribute-inference ASR, MedQA accuracy, SAMSum ROUGE-L, equal-weight CodeBLEU, ablation and sensitivity |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10582 | score_7_9;potential_books_delta | selected | DA-20260713-02 | — | V2=8/9；The paper supports region-dependent attention lifetimes, interpretable pinned retention and its synthetic budgeted-recall/overhead results. It also reports that the unnormalized attention term was much smaller than the structural term and that accumulated-attention retention beat MemDecay on unpinned recall at larger scale. It does not prove production long-context Agent quality or tail-SLO gains.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260713-02 |
| SF-2026-ARXIV-2607-10599 | forced_review;potential_books_delta | selected | DA-20260713-03 | — | V2=6/9；The source supports this mechanism and its MOSI/MOSEI author experiments, ablations and perturbation tests. Predicted uncertainty is a learned reliability sensor, not a probability that a modality is true, and the results do not establish broad multimodal robustness or production behavior.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260713-03 |
| SF-2026-ARXIV-2607-10709 | score_7_9;forced_review;potential_books_delta | selected | DA-20260713-01 | — | 命中合同第一优先级 security contract；V2=8/9；The paper supports this single-turn honest-but-curious design and its MedQA/SAMSum/CodeAlpaca author experiments. It does not prove Differential Privacy, anonymity, compliance, adaptive-attacker resistance or production latency, and it does not disclose the exact local estimator, hardware or precision.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260713-01 |

<!-- analysis:DA-20260713-01:start -->
### PromptGraph: Graph-Guided Prompt Sanitization for Balancing Privacy and Utility in LLM Inference

**旧方案为何合理。** Regex and NER masking remain correct for explicit structured identifiers and low latency. Learned independent-span policies become insufficient when non-sensitive cues jointly reveal an attribute or when masking destroys relations required by the downstream task.（现有命题定位：`books/part-06-ai-infrastructure/72-security.md#L14-L14`）

**约束变化与机制。** Move prompt privacy from independent PII-span masking to a client-owned graph that estimates contextual attribute leakage and pairwise utility dependencies, selects a privacy/utility cut, sends opaque placeholders, and restores only exact consistency-checked identifiers locally. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `PLATFORM-SECURITY` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Relation-aware selection improves the measured privacy/utility frontier but depends on local detectors, attribute estimators, reconstruction proxies and sparse graph coverage. Greedy selection is approximate, placeholders can alter model behavior, and restoration must fail closed rather than granting the cloud model authority over private state.

<!-- analysis:DA-20260713-01:end -->

<!-- analysis:DA-20260713-02:start -->
### MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference

**旧方案为何合理。** FullKV is the correctness baseline; recency/window and accumulated-attention policies are simpler when semantic labels are unavailable or unreliable. Agent traces change the constraint because the orchestrator already knows which spans are instructions, plans, tool outputs or scratch state.（现有命题定位：`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）

**约束变化与机制。** An Agent orchestrator supplies typed semantic region labels and explicit pinning policy; the inference runtime combines those priors with calibrated decay and observed attention to make page-level KV eviction decisions. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-KV-CACHE` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Semantic labels and pinning make retention policy inspectable but convert orchestrator labeling errors into irreversible runtime deletion. Attention observation and eager-attention access add overhead; page means can dilute boundary regions; offload/recompute remain safer when future utility is uncertain.

<!-- analysis:DA-20260713-02:end -->

<!-- analysis:DA-20260713-03:start -->
### MRUF: Multi-granularity Routing with Uncertainty-Aware Fusion for Robust Multimodal Sentiment Analysis

**旧方案为何合理。** Static, symmetric or task-contribution-only fusion is reasonable when modality quality is stable. Once occlusion, noise, missing inputs or transcript error vary per utterance, contribution and current reliability become distinct control signals.（现有命题定位：`books/part-03-multimodal-world-models/23-multimodal-representation.md#L14-L14`）

**约束变化与机制。** Separate task contribution from observation reliability: a contribution router is supervised by leave-one-out task degradation, while a distinct uncertainty head predicts modality-wise log variance and inverse-variance weights calibrate the final fusion gate. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `MULTIMODAL-REPRESENTATION` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Leave-one-out supervision adds masked forwards during training; uncertainty calibration adds a learned sensor whose correlations and distribution shift can be wrong. Inference remains one forward pass in the paper, but severe perturbations did not always improve regression MAE. Static or single-modality branches remain preferable when inputs are reliable, training budget is tight or calibration evidence is weak.

<!-- analysis:DA-20260713-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10582 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L307 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-10582 | delta:SF-2026-ARXIV-2607-10582 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-10582 |
| SF-2026-ARXIV-2607-10599 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#L175 | books/part-02-model/22-long-context.md#L14-L14; books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14 | existing:SF-2026-ARXIV-2607-10599 | delta:SF-2026-ARXIV-2607-10599 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-10599 |
| SF-2026-ARXIV-2607-10709 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L83 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607-10709 | delta:SF-2026-ARXIV-2607-10709 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-10709 |

<!-- books-review:SF-2026-ARXIV-2607-10582:start --><!-- existing:SF-2026-ARXIV-2607-10582:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L307` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-10582:end --><!-- delta:SF-2026-ARXIV-2607-10582:start -->新增证据边界：An Agent orchestrator supplies typed semantic region labels and explicit pinning policy; the inference runtime combines those priors with calibrated decay and observed attention to make page-level KV eviction decisions. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L307`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-10582:end --><!-- books-review:SF-2026-ARXIV-2607-10582:end -->

<!-- books-review:SF-2026-ARXIV-2607-10599:start --><!-- existing:SF-2026-ARXIV-2607-10599:start -->对读 `books/part-03-multimodal-world-models/23-multimodal-representation.md#L175` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/23-multimodal-representation.md#L14-L14`）为：本章的核心判断是：**多模态系统的第一问题不是把所有输入变成同一 shape，而是建立可版本化的 representation contract：每个表示必须保留它来自哪种 modality、对应什么时间与空间范围、经过哪个 encoder/codec、属于哪个 artifact version，并明确哪些信息已经不可逆地丢失。**共享 backbone 可以统一计算接口，却不会自动统一语义、采样率、误差模型和数据权利。<!-- existing:SF-2026-ARXIV-2607-10599:end --><!-- delta:SF-2026-ARXIV-2607-10599:start -->新增证据边界：Separate task contribution from observation reliability: a contribution router is supervised by leave-one-out task degradation, while a distinct uncertainty head predicts modality-wise log variance and inverse-variance weights calibrate the final fusion gate. 该 delta 已进入 `books/part-03-multimodal-world-models/23-multimodal-representation.md#L175`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-10599:end --><!-- books-review:SF-2026-ARXIV-2607-10599:end -->

<!-- books-review:SF-2026-ARXIV-2607-10709:start --><!-- existing:SF-2026-ARXIV-2607-10709:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L83` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2607-10709:end --><!-- delta:SF-2026-ARXIV-2607-10709:start -->新增证据边界：Move prompt privacy from independent PII-span masking to a client-owned graph that estimates contextual attribute leakage and pairwise utility dependencies, selects a privacy/utility cut, sends opaque placeholders, and restores only exact consistency-checked identifiers locally. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L83`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-10709:end --><!-- books-review:SF-2026-ARXIV-2607-10709:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260713-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260713; semantic-review:SA-20260713-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260713-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-10532; review:SF-2026-ARXIV-2607-10582; review:SF-2026-ARXIV-2607-10599; review:SF-2026-ARXIV-2607-10709; semantic-review:SA-20260713-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260713-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260713-01; analysis:DA-20260713-02; analysis:DA-20260713-03; semantic-review:SA-20260713-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260713-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-10582; books-review:SF-2026-ARXIV-2607-10599; books-review:SF-2026-ARXIV-2607-10709; semantic-review:SA-20260713-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260713-COVERAGE:start -->Fresh-context review reconciled the exact window, partition totals, date bucket and denominator.<!-- semantic-review:SA-20260713-COVERAGE:end -->
<!-- semantic-review:SA-20260713-EVIDENCE:start -->Fresh-context review reconciled all 4 frozen families: 3 Deep, 0 Standard and 1 Closure; 0 pending and 0 blocked rows remain explicitly outside mechanism claims.<!-- semantic-review:SA-20260713-EVIDENCE:end -->
<!-- semantic-review:SA-20260713-SELECTION:start -->Fresh-context review reconciled 3 eligible Deep families: 3 selected and 0 not selected; the narrative limit does not downgrade any completed Source Review.<!-- semantic-review:SA-20260713-SELECTION:end -->
<!-- semantic-review:SA-20260713-BOOKS:start -->Fresh-context review checked current owner and adjacent chapter handoffs; 3 个 family 已定位到实际 Books 段落，0 个 family 的 No Change 结论可定位，0 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。<!-- semantic-review:SA-20260713-BOOKS:end -->

## 8. Ignored Noise

489 个窗口内 identity 中，485 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：3 个 `Integrate`，0 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，1 个 `Rejected — Low Durability / Out of Scope`；Deep 3 / Standard 0。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/13/README.md`。
- 本日报长期 delta 已同步至：`books/part-03-multimodal-world-models/23-multimodal-representation.md`、`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`、`books/part-06-ai-infrastructure/72-security.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [Implicit Fine-tuning via Context Engineering: A Curriculum Learning Framework for Multimodal Entity Alignment](https://arxiv.org/abs/2607.10532v1) — first-public（Asia/Shanghai）：2026-07-12；accessed：2026-08-26
- [MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference](https://arxiv.org/abs/2607.10582v1) — first-public（Asia/Shanghai）：2026-07-12；accessed：2026-08-27
- [MRUF: Multi-granularity Routing with Uncertainty-Aware Fusion for Robust Multimodal Sentiment Analysis](https://arxiv.org/abs/2607.10599v1) — first-public（Asia/Shanghai）：2026-07-12；accessed：2026-08-27
- [PromptGraph: Graph-Guided Prompt Sanitization for Balancing Privacy and Utility in LLM Inference](https://arxiv.org/abs/2607.10709v1) — first-public（Asia/Shanghai）：2026-07-12；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
