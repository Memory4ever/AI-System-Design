# AI Research Weekly — 2026-W12

> Coverage Window: 2026-03-16～2026-03-22
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: W12 Source-Family Books Gate Passed — 49 in-window candidate families; 48/48 `20+` Full Source Reviews and 1/1 low-score verification complete; 34 Integrate/Refine dispositions written to 17 Stable Node owners, 11 No Change, 3 Weekly Only including the low-score boundary, 1 Emerging; 0 Books pending; broader Historical Archive Gate remains open

## Executive Summary

旧版仅保留 Helium、GPT-5.4 mini/nano 与 Anthropic 用户研究，并据此写成“AI Infra 未发现更稳定
证据”。该判断未通过 Discovery Recall Gate。按 arXiv v1 first-public date 重开 Hugging Face
2026-03-16～03-24 的推荐流，并回到 primary metadata 后，目前恢复 49 个 W12 候选 family：
48 个 `>=20`，1 个低分项。新增候选覆盖 residual information flow、conditional depth、
on-policy experience consolidation、Agent RL rollout service、exact sampling、long-context typed runtime、
externalized skills、anchored memory、evaluation contract 与 graph RAG。

推荐日期与事件日期被严格分开。3 月 16～24 日推荐流中还发现大量实际在 W10/W11 首发的论文；
它们只进入 spillback ledger，不会被错误塞入 W12。Discovery 阶段先完成 primary metadata 与归周核对，
随后再逐项进入全文和章节审计；Attention Residuals 与 Mixture-of-Depths Attention 已完成新增候选中的前两份
全文 Source Review；OpenSeeker、POLCA、PokeAgent Challenge 与 Code-A1 也已完成论文、关键
Appendix、官方 artifact 和目标/相邻章节联读；HorizonMath、MiroThinker-1.7/H1、Online
Experiential Learning 与 TRUST-SQL 也已完成同级审计。Efficient Reasoning on the Edge、
SWE-Skills-Bench、FlashSampling 与 MetaClaw 现也完成全文、
revision、官方 artifact 和章节邻接复核。Complementary RL、BenchPreS、AdaMem 与 VTC-Bench
也完成同级审计，并分别收敛为 Ch29 新机制、Ch73 新机制、Ch73 既有论证精化与 Ch62 章节级
去重候选。Efficient Exploration、training-free MTP、RAMP 与 PRISM 现也完成论文全文、关键
appendix、可访问 artifact 和目标/相邻章节联读；它们分别收敛为 Ch27 新机制候选、Ch44 既有论证
精化、Ch45 `Emerging / Experimental` 与 Ch24 新机制候选。AI Scientist、Nemotron-Cascade 2、
Memento-Skills 与 AndroTMem 也完成同级审计，分别收敛为
Ch25 新机制、Ch29 新机制、Ch80 既有论证精化与 Ch73 既有论证精化。ProRL Agent、Reasoning
over Mathematical Objects、Hyperagents 与 λ-RLM 也已完成全文、关键 appendix、公开 artifact 与
目标/相邻章节联读；主 owner 分别收敛为 Ch29、Ch27、Ch77 与 Ch77。Subgoal-driven Long-Horizon
Agents、LoopRPT、BEAVER 与 Reintroducing Markov States 现也完成同级审计，owner 分别收敛为
Ch75、Ch24、Ch71 与 Ch29。AgentDS、OpenResearcher、BubbleRAG 与 HopChain 也已完成全文、
revision、evaluation contract 与章节级去重。官方/Infra 固定源扫描又恢复 Vera Rubin、DSX Air、
Dynamo v1.0.1/v1.1.0-dev.1、Kubeflow Distribution 26.03、Trainer v2.2、SDK v0.4.0 与
vLLM incremental MoE expert offloading；Astrolabe 也完成低分来源和拒绝边界核验。48 个 `20+`
候选至此全部形成非模板化 Source Review。此后完成的周级 Books Review 将 34 项 Integrate/Refine
写入 17 个 Stable Node owner，并逐项反向定位；W12 Source-Family Books Gate 已通过。W01～最新完整周
仍有 discovery/material gaps，因此 broader Historical Archive Gate 继续开放，但不撤销本周 Gate。

## Coverage and Source Coverage

- 模型与研究机构：保留 OpenAI、Anthropic，并恢复 Moonshot、Microsoft Research、Google、Meta、
  NVIDIA、Qwen、DeepMind 等 direct research source families；模型/研究机构归属仍需在 Full Review
  中与 technical report、code/model card 联读。
- arXiv / 学术来源：已核对 2026-03-16～03-20 的 direct metadata，并向后检查 03-23～03-24 的
  curation lag；推荐日期不作为 event date。
- AI Infra：除 ProRL Agent、FlashSampling 等 system/runtime 论文外，已复核 NVIDIA hardware/platform、
  Dynamo release history、Kubeflow distribution/Trainer/SDK、vLLM open PR/RFC lineage 和相邻 release 时间窗。KServe v0.17
  属于 W11，PyTorch 2.11 属于 W13，均进入跨周 ledger 而不倒写为 W12 事件。
- Discovery feeds：已逐条核对 Hugging Face 03-16～03-20 与 03-23～03-24 页面中的项目相关条目，
  并按 arXiv v1 日期完成 curation-lag 回拨。没有把全站无关条目数包装成 coverage 指标；本周只声明
  49 个已核验、已评分并有 disposition 的 in-window candidate families。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Helium: workflow-aware LLM serving | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | No Change — Already Covered |
| GPT-5.4 mini / nano | 2 | 4 | 4 | 5 | 4 | 3 | 22/30 | Weekly Only — Version/Product Fact |
| What 81,000 people want from AI | 3 | 3 | 4 | 4 | 3 | 4 | 21/30 | No Change — Already Covered |
| Attention Residuals | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Integrate — New Mechanism |
| OpenSeeker | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Integrate — New Mechanism |
| Mixture-of-Depths Attention | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Integrate — New Mechanism |
| POLCA | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | No Change — Already Covered |
| PokeAgent Challenge | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | No Change — Already Covered |
| Code-A1 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Integrate — New Mechanism |
| HorizonMath | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | No Change — Already Covered |
| MiroThinker-1.7 & H1 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | No Change — Already Covered |
| Online Experiential Learning | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Integrate — New Mechanism |
| TRUST-SQL | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Integrate — New Mechanism |
| Efficient Reasoning on the Edge | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Integrate — New Mechanism |
| SWE-Skills-Bench | 4 | 4 | 5 | 4 | 4 | 3 | 24/30 | Integrate — New Mechanism |
| FlashSampling | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Integrate — New Mechanism; v1 headline superseded by v2 |
| MetaClaw | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Integrate — New Mechanism |
| Complementary Reinforcement Learning | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Integrate — New Mechanism |
| BenchPreS | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Integrate — New Mechanism |
| Efficient Exploration at Scale | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Integrate — New Mechanism |
| AdaMem | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Refine — Existing Argument |
| Training-Free MTP via Embedding-Space Probing | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Refine — Existing Argument; Experimental |
| RAMP mixed-precision quantization | 4 | 4 | 4 | 3 | 5 | 3 | 23/30 | Full Review Complete — Emerging / Experimental |
| AI Scientist via Synthetic Task Scaling | 4 | 4 | 4 | 3 | 4 | 4 | 23/30 | Integrate — New Mechanism |
| PRISM mid-training study | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Integrate — New Mechanism |
| Nemotron-Cascade 2 | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Integrate — New Mechanism |
| Memento-Skills | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Refine — Existing Argument |
| AndroTMem | 4 | 4 | 5 | 4 | 5 | 3 | 25/30 | Refine — Existing Argument |
| VTC-Bench | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | No Change — Already Covered; tool-count metadata disputed |
| ProRL Agent | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Integrate — New Mechanism |
| Reasoning over Mathematical Objects | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Integrate — New Mechanism |
| Hyperagents | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Refine — Existing Argument |
| λ-RLM / Y-Combinator for LLMs | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — Existing Argument |
| Subgoal-driven Long-Horizon Agents | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Integrate — New Mechanism |
| LoopRPT | 4 | 4 | 3 | 4 | 5 | 4 | 24/30 | Integrate — New Mechanism; Experimental |
| BEAVER prompt compression | 4 | 4 | 5 | 4 | 4 | 3 | 24/30 | Refine — Existing Argument |
| Reintroducing Markov States | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Integrate — New Mechanism; Experimental |
| AgentDS Technical Report | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | No Change — Already Covered |
| OpenResearcher | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Integrate — New Mechanism |
| BubbleRAG | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Integrate — New Mechanism |
| HopChain | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — Existing Argument |
| NVIDIA Vera Rubin platform / POD-scale co-design | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Refine — Existing Argument |
| NVIDIA DSX Air | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Full Review Complete — Weekly Only / Product Fact |
| NVIDIA Dynamo v1.0.1 / v1.1.0-dev.1 | 3 | 4 | 4 | 5 | 5 | 2 | 23/30 | No Change — Already Covered |
| Kubeflow Community Distribution 26.03 | 2 | 4 | 4 | 5 | 4 | 2 | 21/30 | No Change — Already Covered |
| Kubeflow Trainer v2.2 | 3 | 4 | 5 | 5 | 5 | 4 | 26/30 | Refine — Existing Argument |
| Kubeflow SDK v0.4.0 | 2 | 3 | 4 | 5 | 4 | 3 | 21/30 | No Change — Already Covered |
| vLLM incremental MoE expert offloading | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Refine — Existing Argument; Experimental; open PR/RFC |
| Astrolabe | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Weekly Only — Below Threshold |

以上评分已在 Source Review 后复算；后续若 primary source revision 改变 evidence boundary，必须保留
历史事件版本并重新评估，而不能静默覆盖本周判断。

## Discovery Recall Ledger

| Ledger Item | Count | Review Result |
| --- | ---: | --- |
| Existing W12 score rows | 3 | 三项 Full Review 保留，但旧 Weekly/Books decision 改为 provisional |
| Recovered in-window candidate families | 46 | direct arXiv/HF metadata、official release/RFC/PR record 与 first-public/event date 已核对 |
| Current in-window candidate families | 49 | 48 项 `>=20`；1 项已核验低分拒绝 |
| Full Source Reviews complete under current gate | 48 | 全部 `20+` 候选已形成非模板化 Source Review |
| `20+` Full Source Reviews pending | 0 | 本项已闭合；仍不得以 abstract、推荐页或旧 Weekly 摘要替代全文阅读 |
| Low-score verification complete | 1 | Astrolabe 的来源、日期、机制披露边界、评分与拒绝理由已核验 |
| Official/infra recall | Complete for fixed source list | NVIDIA、Dynamo、Kubeflow、KServe、PyTorch 与主要 runtime release 窗口已核对；无 primary evidence 的宣传项不入候选 |

## Recovered Candidate Census

| First-public Date | Candidate | Direct Primary Source | Initial Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-16 | Attention Residuals | arXiv:2603.15031 v1 | Ch17 | Full Review Complete — Books pending |
| 2026-03-16 | OpenSeeker | arXiv:2603.15594 v1 | Ch72 | Full Review Complete — Books pending |
| 2026-03-16 | Mixture-of-Depths Attention | arXiv:2603.15619 v1 | Ch17 | Full Review Complete — Books pending |
| 2026-03-16 | POLCA | arXiv:2603.14769 v1 | Ch77 | Full Review Complete — No Change candidate |
| 2026-03-16 | PokeAgent Challenge | arXiv:2603.15563 v1 | Ch62 | Full Review Complete — No Change candidate |
| 2026-03-16 | Code-A1 | arXiv:2603.15611 v1 | Ch29 | Full Review Complete — Books pending |
| 2026-03-16 | HorizonMath | arXiv:2603.15617 v1 | Ch62 | Full Review Complete — No Change candidate |
| 2026-03-16 | MiroThinker-1.7 & H1 | arXiv:2603.15726 v1 | Ch76 | Full Review Complete — No Change candidate |
| 2026-03-16 | SWE-Skills-Bench | arXiv:2603.15401 v1 | Ch80/Ch62 | Full Review Complete — Books pending |
| 2026-03-16 | FlashSampling | arXiv:2603.15854 v1 | Ch20 | Full Review Complete — Books pending |
| 2026-03-16 | VTC-Bench | arXiv:2603.15030 v1 | Ch62 | Full Review Complete — No Change candidate; metadata disputed |
| 2026-03-17 | Online Experiential Learning | arXiv:2603.16856 v1 | Ch73 | Full Review Complete — Books pending |
| 2026-03-17 | TRUST-SQL | arXiv:2603.16448 v1 | Ch29 | Full Review Complete — Books pending |
| 2026-03-17 | Efficient Reasoning on the Edge | arXiv:2603.16867 v1 | Ch26 | Full Review Complete — Books pending |
| 2026-03-17 | MetaClaw | arXiv:2603.17187 v1 | Ch80/Ch73 | Full Review Complete — Books pending |
| 2026-03-17 | BenchPreS | arXiv:2603.16557 v1 | Ch73/Ch62 | Full Review Complete — Books pending |
| 2026-03-17 | AdaMem | arXiv:2603.16496 v1 | Ch73 | Full Review Complete — Books pending |
| 2026-03-17 | AI Scientist via Synthetic Task Scaling | arXiv:2603.17216 v1 | Ch25 | Full Review Complete — Books pending |
| 2026-03-17 | PRISM | arXiv:2603.17074 v1 | Ch24 | Full Review Complete — Books pending |
| 2026-03-17 | HopChain | arXiv:2603.17024 v1 | Ch23 | Full Review Complete — Books pending |
| 2026-03-16 | NVIDIA Vera Rubin platform | NVIDIA official announcement / technical pages | Ch50/Ch53 | Full Review Complete — Books pending |
| 2026-03-16 | NVIDIA DSX Air | NVIDIA official technical blog | Ch69/Ch53 | Full Review Complete — Weekly Only / Product Fact |
| 2026-03-16 | NVIDIA Dynamo v1.0.1 | Official release history / GitHub release | Ch48 | Full Review Complete — No Change candidate |
| 2026-03-17 | NVIDIA Dynamo v1.1.0-dev.1 | Official release history / GitHub release | Ch48 | Same Source Family — No Change candidate |
| 2026-03-17 | Astrolabe | arXiv:2603.17051 v1 / official project and repo | Ch29/Ch44 | Low-score verification complete — Weekly Only |
| 2026-03-17 | OpenResearcher | arXiv:2603.20278 v1 | Ch23 | Full Review Complete — Books pending |
| 2026-03-18 | Complementary Reinforcement Learning | arXiv:2603.17621 v1 | Ch29/Ch73 | Full Review Complete — Books pending |
| 2026-03-18 | Efficient Exploration at Scale | arXiv:2603.17378 v1 | Ch27 | Full Review Complete — Books pending |
| 2026-03-18 | Training-Free MTP | arXiv:2603.17942 v1 | Ch44 | Full Review Complete — Books pending |
| 2026-03-18 | RAMP | arXiv:2603.17891 v1 | Ch45 | Full Review Complete — Emerging / Experimental |
| 2026-03-19 | Nemotron-Cascade 2 | arXiv:2603.19220 v1 | Ch29 | Full Review Complete — Books pending |
| 2026-03-19 | Memento-Skills | arXiv:2603.18743 v1 | Ch80 | Full Review Complete — Books pending |
| 2026-03-19 | AndroTMem | arXiv:2603.18429 v1 | Ch73 | Full Review Complete — Books pending |
| 2026-03-19 | ProRL Agent | arXiv:2603.18815 v1 | Ch29 | Full Review Complete — Books pending |
| 2026-03-19 | Reasoning over Mathematical Objects | arXiv:2603.18886 v1 | Ch27 | Full Review Complete — Books pending |
| 2026-03-19 | Hyperagents | arXiv:2603.19461 v1 | Ch77 | Full Review Complete — Books pending |
| 2026-03-19 | AgentDS | arXiv:2603.19005 v1 | Ch62 | Full Review Complete — No Change candidate |
| 2026-03-19 | BubbleRAG | arXiv:2603.20309 v1 | Ch72 | Full Review Complete — Books pending |
| 2026-03-19 | Kubeflow SDK v0.4.0 | Kubeflow official blog / package release | Ch53/Ch54 | Full Review Complete — No Change candidate |
| 2026-03-20 | λ-RLM | arXiv:2603.20105 v1 | Ch77 | Full Review Complete — Books pending |
| 2026-03-20 | Subgoal-driven Long-Horizon Agents | arXiv:2603.19685 v1 | Ch75 | Full Review Complete — Books pending |
| 2026-03-20 | LoopRPT | arXiv:2603.19714 v1 | Ch24 | Full Review Complete — Books pending; Experimental |
| 2026-03-20 | BEAVER | arXiv:2603.19635 v1 | Ch71 | Full Review Complete — Books pending |
| 2026-03-20 | Reintroducing Markov States | arXiv:2603.19987 v1 | Ch29 | Full Review Complete — Books pending; Experimental |
| 2026-03-20 | Kubeflow Trainer v2.2 | Kubeflow official blog / GitHub v2.2.0 release | Ch56 | Full Review Complete — Books pending |
| 2026-03-22 | Kubeflow Community Distribution 26.03 | Kubeflow official release manifest | Ch54 | Full Review Complete — No Change candidate |
| 2026-03-16 | vLLM incremental MoE expert offloading | vLLM PR #37190; W13 RFC #38256 is later architecture evolution | Ch50 | Full Review Complete — Refine candidate; Experimental |

## Cross-Week Spillback Ledger

以下条目由 03-16～03-24 推荐流发现，但 first-public date 早于 03-16。它们不计入 W12，必须在
W10/W11 Discovery Gate 继续处理：

| Destination | Verified Examples | Review Result |
| --- | --- | --- |
| W10 | Recursive Language Models Meet Uncertainty (03-07) | W10 spillback；不在 W12 评分 |
| W11 | EvoScientist、FinToolBench、MEMO、FineRMoE、Reasoning as Compression、Deep Tabular Research | 03-09～03-10 first-public；W11 Gate 需再次打开 |
| W11 | LookaheadKV、UCIP、Safe Web Agent Learning、One-Eval | 03-10～03-11 first-public；W11 spillback |
| W11 | LMEB、Video Streaming Thinking、OpenSWE、MM-CondChain、HomeSafe-Bench、Think While Watching、Balanced Thinking、Expert Threshold Routing | 03-12～03-13 first-public；W11 spillback |
| W11 | Spend Less Reason Better、EnterpriseOps-Gym、EvoClaw、TERMINATOR、SFT vs RL、GradMem | 03-13～03-14 first-public；W11 spillback |
| W11 | AI Can Learn Scientific Taste、AgentProcessBench、V-JEPA 2.1 | 03-15 first-public；W11 spillback |
| W11 | KServe v0.17.0 | 03-13 official release；KV-aware routing、PD topology 与 LLMInferenceService 应回到 W11，不在 W12 重复计分 |

## Deep Analysis — 从 Request Scheduler 到 Workflow Optimizer

### Why → Principle → Mechanism

传统 serving engine 将每次 LLM call 当作独立请求；Agent workflow 的并行探索、重试和共享
prefix 会跨调用产生重复状态。Helium 将 workflow 表达为 query plan，并把 prompts、KV 与
intermediate results 纳入 proactive caching 和 cache-aware scheduling。原则是 scheduler 的
优化边界必须覆盖真实 dependency graph，而不能止于单个 HTTP request。

### Trade-off → Connection → Evolution

workflow visibility 提高复用机会，却要求稳定的 task identity、dependency、cache validity、
privacy 与 failure semantics。作者报告的 speedup 绑定论文 workload，不能外推。

```text
per-request batching
→ prefix/KV-aware routing
→ workflow-aware plan and cache reuse
→ 新增跨调用 state ownership、invalidation 与 fairness 问题
```

关系为 `Direct Evolution` 于 serving optimization boundary；旧的 request-level engine 在
stateless 或低复用 workload 下仍更简单。

## Evidence Level

- 已完成：Attention Residuals、Mixture-of-Depths Attention、OpenSeeker、POLCA、PokeAgent
  Challenge、Code-A1、HorizonMath、MiroThinker-1.7/H1、Online Experiential Learning 与
  TRUST-SQL、Efficient Reasoning on the Edge、SWE-Skills-Bench、FlashSampling 与 MetaClaw 均已
  覆盖全文、关键 appendix、可访问的官方 artifact 和目标/相邻章节；Helium 为论文、appendix 与
  artifact 联读；AI Scientist、Nemotron-Cascade 2、Memento-Skills、AndroTMem、ProRL Agent、Reasoning
  over Mathematical Objects、Hyperagents、λ-RLM、Subgoal-driven Long-Horizon Agents、LoopRPT、
  BEAVER、Reintroducing Markov States、AgentDS、OpenResearcher、BubbleRAG 与 HopChain 也完成
  同级 Source Review；Vera Rubin、DSX Air、Dynamo patch/dev release、Kubeflow distribution/Trainer/SDK
  也完成 official source、版本边界与章节去重复核；GPT-5.4 mini/nano 为
  官方版本事实；Anthropic 条目为官方平台用户研究。
- `20+` 全文/官方资料审计：47/47 已闭合。推荐页仍只用于 discovery，不构成机制证据。
- 低分边界：Astrolabe 调整为 19/30；论文 metadata、官方 project/repo 与 03-23 code release 已核验，
  但当前访问未获得可完成 paper-level evaluation contract 的正文，因此仅作低分拒绝，不冒充 Full Review。
- 覆盖边界：固定官方 research/release/RFC/PR/runtime 源已完成本轮确定性扫描。无法公开核验内部机制的
  DSX Air 只记录 `Version/Product Fact`；JAX 0.9.2 的 GitHub 页面时间戳与 changelog 日期冲突，按
  03-02 release date 排除；Kubernetes 1.35.3 是无新增 AI-System 机制的 patch。W12 Evidence Gate 通过。

## Cross-Week Deduplication

- 不要把 Workflow、multi-agent 与 workflow-aware serving 混成同一层：Ch77 拥有业务状态，
  inference runtime 只消费可执行 dependency 与 cache contract。
- MetaClaw、Memento-Skills、Online Experiential Learning、Complementary RL 与 Hyperagents 属于不同
  adaptation state：external skill、trajectory-derived experience、parameter update 与 editable meta-policy
  不能因“自进化”标签而合并。
- FlashSampling、training-free MTP、BEAVER 与 Helium 分别位于 sampling primitive、decoding、context
  selection 与 workflow serving 层；后续按 owner 去重，不能写成一条单向替代路线。

## Knowledge Tree Position

旧 Ch 编号是 80 章结构下的阅读快照，不作为当前 owner。最终主 owner 为
`MODEL-TRANSFORMER-LAYER`、`MODEL-SAMPLING`、`TRAIN-DATA`、`TRAIN-PRETRAINING`、`TRAIN-SFT`、
`TRAIN-LORA`、`TRAIN-RLHF`、`TRAIN-GRPO`、`INFER-SPECULATIVE-DECODING`、`INFER-GPU-MEMORY`、
`PLATFORM-TRAINING-OPERATOR`、`AGENT-CONTEXT`、`AGENT-RAG`、`AGENT-MEMORY`、`AGENT-PLANNING`、
`AGENT-WORKFLOW` 与 `AGENT-PLATFORM`。跨章节只保留 handoff，不因一项证据重复修改多个 owner。

## Recommended Action

W12 候选账与 Source-Family Books Gate 已闭合。34 项长期机制已按 Stable Node 写入或精化 17 个 owner，
11 项以具体既有论点去重，3 项保留为 Weekly Only，RAMP 保持 Emerging。下一检查点进入 W13；任何新增
in-window source family 都必须重新打开 W12 Gate。Historical Archive Completion Gate 仍因全局 discovery/
材料缺口开放，但不撤销本周已完成的 source-family integration。

## Event-Date Daily Decision

历史回填保持 Weekly-only：2026-03-16～03-20 的真实事件直接记录在本完整 ISO Weekly，不补造 Daily。

## Books Integration Decision

`W12 Source-Family Books Gate Passed`。Candidate Scoring 是 49 项最终 disposition 的唯一账本；
Full Source Review 中的 `Books Gate Pending` 与 legacy Ch 编号只表示当时的阅读阶段快照，已被本节取代。

- `Integrate/Refine (34)`：depth-history routing 与 bounded slots；fused exact sampling；graph/evidence-
  grounded data；mid-training 与 adaptive depth；environment-grounded SFT；post-prefill adapter/KV
  compatibility；uncertainty-driven feedback；adaptive verifier、phase credit、rollout service 与 explicit
  environment state；training-free speculative proposal；MoE expert cache/POD memory boundary；manager-
  owned training patches；structured Context selection；graph RAG；preference applicability、typed stores、
  causal anchors 与 parameter-consolidation boundary；verifiable subgoals；editable/recursive workflow；
  paired skill utility 与 two-timescale Agent adaptation。上述机制已写入 17 个 Stable Node owner。
- `No Change (11)`：Helium、Anthropic 用户研究、POLCA、PokeAgent、HorizonMath、MiroThinker、
  VTC-Bench、AgentDS、Dynamo、Kubeflow Distribution 与 Kubeflow SDK 均由现有具体论点覆盖。
- `Weekly Only (3)`：GPT-5.4 mini/nano 与 DSX Air 只提供版本/产品事实；Astrolabe 低于阈值且正文证据
  不完整。
- `Emerging (1)`：RAMP 的 learned allocation 尚未连接到可复核 artifact、kernel 与一致 workload contract。

| Integrated Source Family | Stable Node Owner | Current / Legacy | Final Disposition |
| --- | --- | --- | --- |
| Attention Residuals | `MODEL-TRANSFORMER-LAYER` | Ch17 / Ch17 | Integrate — depth-history aggregation |
| Mixture-of-Depths Attention | `MODEL-TRANSFORMER-LAYER` | Ch17 / Ch17 | Integrate — bounded depth slots |
| FlashSampling | `MODEL-SAMPLING` | Ch20 / Ch20 | Integrate — exact fused sampling |
| OpenResearcher | `TRAIN-DATA` | Ch27 / Ch23 | Integrate — evidence-grounded trajectory data |
| HopChain | `TRAIN-DATA` | Ch27 / Ch23 | Refine — dependency-constrained visual evidence |
| PRISM | `TRAIN-PRETRAINING` | Ch28 / Ch24 | Integrate — mid-training stage contract |
| LoopRPT | `TRAIN-PRETRAINING` | Ch28 / Ch24 | Integrate — learned recurrent depth |
| AI Scientist via Synthetic Task Scaling | `TRAIN-SFT` | Ch29 / Ch25 | Integrate — executable synthetic demonstrations |
| Efficient Reasoning on the Edge | `TRAIN-LORA` | Ch30 / Ch26 | Integrate — post-prefill adapter/KV compatibility |
| Efficient Exploration at Scale | `TRAIN-RLHF` | Ch31 / Ch27 | Integrate — uncertainty-directed feedback acquisition |
| Reasoning over Mathematical Objects | `TRAIN-RLHF` | Ch31 / Ch27 | Integrate — policy-conditioned reasoning judge |
| Code-A1 | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate — co-evolving verifier policy |
| TRUST-SQL | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate — phase-specific credit |
| Complementary Reinforcement Learning | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate — actor/extractor co-evolution |
| Nemotron-Cascade 2 | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate — staged domain RL and distillation |
| ProRL Agent | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate — rollout service boundary |
| Reintroducing Markov States | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate — explicit environment state |
| Training-Free MTP via Embedding-Space Probing | `INFER-SPECULATIVE-DECODING` | Ch48 / Ch44 | Refine — latent-probe proposal branch |
| NVIDIA Vera Rubin platform | `INFER-GPU-MEMORY` | Ch54 / Ch50 | Refine — POD-level co-design boundary |
| vLLM incremental MoE expert offloading | `INFER-GPU-MEMORY` | Ch54 / Ch50 | Refine — router-conditioned expert cache |
| Kubeflow Trainer v2.2 | `PLATFORM-TRAINING-OPERATOR` | Ch60 / Ch56 | Refine — manager-owned patch/status contract |
| BEAVER | `AGENT-CONTEXT` | Ch75 / Ch71 | Refine — structure-aware document selection |
| OpenSeeker | `AGENT-RAG` | Ch76 / Ch72 | Integrate — graph-grounded search training |
| BubbleRAG | `AGENT-RAG` | Ch76 / Ch72 | Integrate — multi-anchor evidence subgraph |
| Online Experiential Learning | `AGENT-MEMORY` | Ch77 / Ch73 | Integrate — memory-to-parameter release branch |
| BenchPreS | `AGENT-MEMORY` | Ch77 / Ch73 | Integrate — preference applicability/suppression |
| AdaMem | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — typed stores and adaptive routing |
| AndroTMem | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — causal state anchors |
| Subgoal-driven Long-Horizon Agents | `AGENT-PLANNING` | Ch79 / Ch75 | Integrate — verifiable milestones |
| Hyperagents | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — editable improvement policy |
| λ-RLM | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — deterministic recursive spine |
| SWE-Skills-Bench | `AGENT-PLATFORM` | Ch84 / Ch80 | Integrate — paired skill-utility Gate |
| MetaClaw | `AGENT-PLATFORM` | Ch84 / Ch80 | Integrate — two-timescale adaptation |
| Memento-Skills | `AGENT-PLATFORM` | Ch84 / Ch80 | Refine — versioned memory/skill operator policy |

W12 的 Source-Family Books Gate 已通过；更广的 Historical Archive Completion Gate 继续开放。

## Ignored Noise

- 缺少模型、硬件、precision、长度、batch、并发与 SLO 的性能外推。
- 以 Hugging Face 推荐日期代替 arXiv v1 first-public date。
- 把“self-evolving”“memory”“Agent RL”营销标签当成同一种 state ownership 或技术替代关系。
- 把 NVIDIA preliminary/vendor benchmark 写成跨 workload 的通用性能结论，或从 DSX Air 产品能力
  反推未公开 simulation fidelity 与内部实现。
- 把 KServe v0.17（03-13）或 PyTorch 2.11（03-23）按阅读日期错归 W12；把 JAX GitHub 页面更新时间
  当成 changelog release date。

## 2026-07-31 Full Re-Audit Addendum

- Helium 已按论文全文、实现与 evaluation conditions 重审。workflow DAG 暴露给 serving
  后可进行跨 operator reuse/batching，但 dynamic branch、external tool、identity 与
  invalidation 成为新状态；已由 Ch77 作为主 owner 吸收。
- 论文结果只绑定 Qwen3、两张 H100 NVL、vLLM 0.16、greedy decoding 与作者 workload。
  GPT-5.4 mini/nano 与 usage survey 仍为 dated state。

## Full Source Review

### Attention Residuals — 28/30

- **Source Family ID / Type / Dates**：`ATTNRES-DEPTH-AGGREGATION`；arXiv:2603.15031v1，
  first-public 2026-03-16，当前仅 v1。全文 HTML 转换失败，改读 21 页官方 PDF；同时核对
  MoonshotAI 官方仓库。仓库在核验时只有 README、论文副本与示意图，没有可运行实现、release
  或测试，因此代码实现状态记为 `Not Released / Not Independently Verified`。
- **Access / Full-read Coverage**：已覆盖 metadata、Abstract、Introduction、Motivation、Full/Block
  AttnRes method、公式与伪代码、training/inference infrastructure、scaling laws、48B training
  recipe、downstream evaluation、全部 ablation、architecture/weight analysis、structured-matrix
  interpretation、Related Work、Conclusion 与 Appendix B inference I/O 推导。论文没有独立的
  Limitations / Threats to Validity 章节，故限制由实验契约与缺失披露显式重建。
- **Original Problem / Previous Design / Changed Constraint**：标准 residual 的
  `h_l=h_(l-1)+f_(l-1)(h_(l-1))` 同时提供 identity gradient highway 和低成本逐层状态传递，
  对早期与当前深度仍然合理；但展开后每层接收所有既往输出的固定等权和。Pre-Norm 深度增加时，
  residual magnitude 随累积增长，单层相对贡献被稀释，也无法从已压缩单状态中选择性恢复较早表示。
  约束变化不是“Residual 失效”，而是更深模型开始需要可学习的 depth-wise information routing，
  同时 pipeline parallel、activation recomputation 与长 context 又不允许无限保存/传输逐层输出。
- **Mechanism / State Ownership / Control and Data Flow**：Full AttnRes 保存 embedding 与每个既往
  sub-layer output；每层以一个 learned pseudo-query 对 RMSNorm 后的这些 output 计算 depth-wise
  softmax，再以同一权重聚合原始 value。Block AttnRes 在 block 内继续做普通 residual sum，只把完成
  block 的 summary 与当前 partial sum 暴露为跨 block sources。模型 checkpoint 拥有 pseudo-query、
  RMSNorm 与 block partition；训练 runtime 拥有 block-history activation/cache 的生命周期与跨 pipeline
  stage 传输；推理 runtime 拥有两阶段调度、online-softmax statistics 与 sequence-sharded prefill state。
- **Implementation Details**：Full 方案的逐层 source 数从 1 增为 `O(L)`；Block 方案以 `N` 个 block
  summary 把存储和 pipeline communication 从 `O(Ld)` 降到 `O(Nd)`。训练侧利用 cross-stage cache
  只传增量 block；推理侧 Phase 1 批量计算同一 block 内各层对历史 block 的查询，Phase 2 顺序处理
  当前 partial sum，并以 online softmax 精确合并。长 context prefill 沿 sequence 维切分 block
  representations，并把 reduce-scatter / merge / all-gather 接入 TP 路径。以上是论文设计与伪代码，
  不是已由公开实现复现的 runtime 行为。
- **Evaluation Contract**：scaling-law sweep 使用同一 Kimi Linear-style MoE 架构、5 个 active-parameter
  规模（194M～528M）、38.7B～119B tokens、8192 context，与 PreNorm、Full/Block AttnRes 和
  mHC(-lite) 比较。主实验为 Kimi Linear 48B total / 3B activated、27 Transformer blocks、8/256
  routed experts 加 1 shared expert、Block AttnRes 9 blocks 加 embedding、1T pretraining 加约 400B
  mid-training tokens、4096 context、global batch 8M tokens，并继续扩到 32K。作者还报告 component、
  block-size、25-point depth/width/head allocation ablations。训练硬件、precision、并行规模、SLO、
  downstream decoding protocol 与统计显著性均 `Not Disclosed`；因此 `<4%` training overhead、
  `<2%` typical inference latency 和 benchmark 增益不能跨 workload 外推。
- **What the Evidence Proves / Does Not Prove**：在作者控制的 Kimi Linear/MoE 配方中，AttnRes 的
  validation loss 在五个小规模点均优于同配方 baseline；Full/Block、static/dynamic mixing、softmax/
  sigmoid、RMSNorm、multihead 与 block-size ablations 支持“内容相关的跨层选择”而非单纯参数增加
  是重要因素。48B 对照还观察到 residual magnitude 的周期性约束与更均匀的梯度。它没有证明
  这些收益适用于 dense Transformer、不同 optimizer/data/normalization、post-training、量化部署或
  其他硬件；downstream 单次表格也不能证明通用能力提升的因果来源。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：细粒度跨层访问换来 activation
  lifetime、pipeline communication、prefill memory、runtime cache consistency 与更复杂 kernel/schedule；
  block compression 又可能丢失 block 内可选择的细粒度来源。pseudo-query 必须零初始化以避免初期波动，
  learned depth weights 还会引入 attention sink、block-boundary sensitivity、checkpoint incompatibility
  与缓存/重算不一致风险。标准 residual 在浅层、低通信预算、缺乏专用 kernel、需要成熟 checkpoint
  兼容性或收益尚未跨架构验证时仍是更简单稳健的方案。
- **Evolution Relationship / ROADMAP / Chapters Read**：`Direct Evolution` 于 residual information
  aggregation，`Layering / Dependency` 于 pipeline parallel 与 inference I/O；它不是对 Pre-Norm、
  Post-Norm 或 Hyper-Connection 的单向替代。主 owner 更正为 Ch17，已读 Ch16、Ch17、Ch18；Ch17
  已覆盖 identity path、Pre/Post-Norm 与 controlled carry/transform，但尚未覆盖“单一 residual state
  → static/multi-stream mixing → selective cross-layer aggregation”这条演进和其系统成本。
- **Integration Decision / Changed Files / Open Questions**：Source Review 阶段判断为
  `Integrate — New Mechanism (Books Gate Pending)`，不在当前 checkpoint 写入 Books。待 Gate 后考虑
  refine Ch17，并以短 handoff 指向 Ch34 pipeline parallel 与 Ch39/Ch50 的 prefill/memory；需进一步
  核验公开实现、硬件/precision/并行配置，以及与 Mixture-of-Depths Attention 的依赖边界。

### Mixture-of-Depths Attention — 27/30

- **Source Family ID / Type / Dates**：`MODA-SEQUENCE-DEPTH-KV`；arXiv:2603.15619v1，
  first-public 2026-03-16，当前仅 v1。已读 18 页官方 PDF、arXiv metadata 与作者官方仓库；当前仓库
  有 42 commits、MoDA/FDA 多个 Triton kernel、unit-test 入口和 language/vision task scaffolding，
  但 README 仍把 full LLM training recipe 与 reproducible configs 列为 TODO。当前 artifact 用于核验
  机制，不倒写成 3 月 16 日已全部存在的 event fact。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Preliminary、depth-stream
  read/operate/write 设计空间、Depth Residual/Dense/Attention/MoDA、完整复杂度表、hardware-aware
  algorithm、chunk/group-aware layout、kernel evaluation、training/evaluation setup、variant/model-size/
  layer-number/kernel ablations、attention visualization、Conclusion、industrial CUDA 与 bounded-slot
  Discussion。论文无独立 Related Work、Limitations、Threats to Validity 或 Appendix；这些缺口不由
  二手摘要补造。
- **Original Problem / Previous Design / Changed Constraint**：普通 residual 用固定宽度状态和加法
  保持优化稳定，成本低、实现成熟，但历史 layer outputs 被反复压进单一路径；Depth Dense 保留全部
  状态，却引入随深度增长的 projection/连接开销。随着模型变深，作者要同时保留内容相关的跨层检索、
  causal sequence attention 和 Tensor Core 友好的连续访问，问题从“能否访问浅层信息”变成“怎样在
  一个可高效执行的概率空间内同时路由 sequence 与 depth”。
- **Mechanism / State Ownership / Control and Data Flow**：MoDA 保留当前 layer 的 sequence Q/K/V，
  并保存同一 token position 在既往 layers 的 depth K/V；每个 query head 将当前 causal sequence KV
  与自己的 historical depth KV 放进同一个 softmax probability budget。attention layer 复用原有 K/V
  写入 depth stream，FFN 可用轻量额外 projection 写入 depth K/V。checkpoint 拥有投影、GQA mapping
  与哪些 layers 写 depth state；runtime 拥有 `[token, depth, kv-head, head-dim]` cache layout、有效深度、
  causal/depth masks、online-softmax accumulator 和 cache allocation。
- **Implementation Details**：naive per-layer gather 会产生非连续访问；实现先把每个 token 的 `L`
  个 depth slots 连续排列，再按 query chunk `C` 限定局部 depth span，并利用 GQA 中 `G` 个 query
  rows 共享 base-time 的事实复用 depth blocks。sequence 与 depth loops 共享 running max、normalizer
  和 output accumulator，只在片上完成一次归一化。当前 `v17` artifact 还增加预分配 `L_max` buffer
  与 `current_depth` mask，避免每层 `stack/cat` 导致的 Python-side `O(L^2)` copy；未写 slots 必须为
  finite values，否则 tensor-core dot 可能在 mask 前传播 NaN。这是后续代码状态，不是论文 v1 的
  原始实验契约。
- **Evaluation Contract**：主模型为 700M/1.5B decoder-only、OLMo2 400B-token subset、bf16、global
  batch 1024、context 4096、AdamW/OLMo2 recipe；比较 OLMo2 与不同 depth-KV/FFN-KV projection，
  并报告 10 项 downstream 与 10 个 validation domains。小模型 depth study 使用 width 384、6 query
  heads、2 KV heads、24/48 layers 与 FineWeb-Edu held-out split。kernel 实验固定单张 A100、bf16、
  forward+backward；64K headline 对应 `B=1,d=64,C=64,G=8,Hq=64,Hk=8,L=64`。未披露完整训练硬件/
  并行拓扑、随机种子方差、统计显著性、decode latency、serving concurrency 或 SLO。
- **What the Evidence Proves / Does Not Prove**：在作者 OLMo2 配方中，Depth KV 与 FFN-side KV 的
  controlled ablations 改善 validation loss/PPL，且 700M/1.5B 平均指标方向一致；kernel ablation 证明
  contiguous layout、chunking 与 group-aware indexing 对该 Triton operator 的性能都必要。单 A100
  结果还直接显示 overhead 并非恒定：`T=64K,L=64` 时比 FA2 多 2.73%，而固定 `T=16K` 把深度从
  64 增至 256 时多 30.52%。它不证明 trillion-scale、multi-node、decode、量化、非 OLMo2 架构或
  multimodal/world-model 宣称；attention heatmap 只表明分配行为，不证明功能因果。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：统一 softmax 让 sequence evidence
  与 depth evidence 直接竞争 probability mass，获得统一路由，也可能挤压真正需要的长程 sequence
  token；全量 depth KV 的 memory/bandwidth 随 `T×L` 增长，深度增加时 kernel overhead 上升。缓存还
  引入 slot identity、valid-depth mask、layout/version compatibility、NaN contamination、eviction 与
  checkpoint incompatibility。作者提出 bounded slots，但 selection/recency policy 尚属 future work。
  标准 attention+residual 在浅层、短 cache、decode-sensitive、跨节点通信受限或缺少专用 kernel 时
  仍更合理；Depth Dense 只在小规模且需要无损保留全部层状态时保有直观价值。
- **Evolution / Relation to AttnRes / ROADMAP / Chapters Read**：与 AttnRes 都是 `Direct Evolution`
  于单一 residual state，但两者是平行 design branches：AttnRes 用 learned per-layer pseudo-query 重写
  depth aggregation，并可压成 block summaries；MoDA 复用 token query，把 per-layer depth K/V 与
  causal sequence K/V 放进同一 softmax，同时继续 residual write。二者不是先后替代，组合也不是免费
  叠加，因为会重复保存 depth state、竞争 cache 和 pipeline bandwidth。主 owner 收敛为 Ch17，已读
  Ch14～19；Ch14/15 只负责 sequence attention 与 GQA contract，Ch19 当前只覆盖跨 decode-step 的
  sequence KV，尚未覆盖模型内跨 layer 的 depth KV。
- **Integration Decision / Changed Files / Open Questions**：`Integrate — New Mechanism (Books Gate
  Pending)`；当前不写 Books。Gate 后优先在 Ch17 与 AttnRes 共同构造“单状态 → dense/static/multi-stream
  → selective depth retrieval”的分叉演进，Ch14 与 Ch19 只做短 handoff。仍需核验完整 training
  recipe、multi-node/pipeline 语义、decode cache 生命周期和 bounded-slot selection 是否公开。

### Helium: workflow-aware LLM serving — 26/30

- **Source Family ID / Type / Dates**：`HELIUM-WORKFLOW-SERVING`；arXiv:2603.16104v1，
  first-public 2026-03-17；论文、appendix 与作者 `helium_demo` artifact 联读。
- **Access / Full-read Coverage**：已覆盖 metadata、Introduction/Background、system overview、
  optimizer、processor、implementation、全部 evaluation/ablation/sensitivity/overhead、limitations、
  conclusion 与 TRT/complexity/DSL appendices。
- **Original Problem / Previous Design / Changed Constraint**：continuous batching、PagedAttention 和
  被动 prefix cache 对独立在线请求合理；batch agent workflow 暴露跨 operator、query 和 batch
  的 DAG 与重复 prefix，使 request-local runtime 看不到可复用状态。
- **Mechanism / Ownership / Flow**：DSL 编译为 DAG；CSE/pruning 和 deterministic prompt cache
  改写逻辑计划；templated radix tree 同时表达 prefix hierarchy 与 dependency；cost-based
  scheduler 分配 worker 和顺序；vLLM 0.16 worker pin/precompute KV，驱逐后重算。workflow owner
  提供静态结构和 profile，Helium 拥有计划与 cache metadata，engine 拥有 GPU KV block。
- **Implementation / Evaluation Contract**：原型基于 vLLM 0.16；同一 base model、greedy
  decoding、on-prem multi-GPU、无 remote tools。作者以 Qwen3-8B/14B、两张 H100 NVL、五类
  primitive workflow 与 19-agent/88-operator Trading workflow 比较多种 baseline，并给出
  component ablation、prompt/batch sensitivity 和规划开销；headline speedup 仅对这些条件成立。
- **What It Proves / Does Not Prove**：证明在结构提前可知、共享充分、确定性 operator 的作者
  workload 中，全局计划与 cache-aware order 能减少重复 prefill/operation；不证明 dynamic
  branching、异构模型、外部 tool、sampling、multi-tenant privacy/fairness 或故障恢复下仍成立。
- **Trade-offs / Failure Modes / Coexistence**：收益换来 compile/profile、cache identity、
  invalidation、pinned-memory pressure、stale plan 和 cross-tenant isolation；低复用或高度动态请求
  仍适合 request-level engine。关系为 `Direct Evolution`，不是 orchestration 对 serving 的替代。
- **ROADMAP / Chapters / Existing Coverage**：Ch77 主 owner，已读 Ch47～52、Ch73、Ch76～80；
  当前正文已有 workflow-visible serving 与 validity/failure contract。
- **Decision / Files / Questions**：`No Change — Already Covered`；不再复制论文功能或数字。
  开放问题是 optimizer、orchestrator 与 engine 间 cache invalidation/retry 的权威边界。

### GPT-5.4 mini / nano — 22/30

- **Sources / Verification**：OpenAI 2026-03-17 announcement 与 deployment-safety addendum 已核对。
  官方披露 API 能力、400k context（mini）、价格和自有 benchmark；训练和 runtime 机制
  `Not Disclosed`。
- **Mechanism / Evidence Boundary**：可确认 model-family 提供 quality/latency/cost 分层及大模型
  协调、小模型执行的产品模式；“2x faster”来自离线模拟 production behavior，真实 latency
  明示可能显著变化，不能反推 architecture 或普遍 routing 策略。
- **ROADMAP / Decision**：Ch37/Ch48/Ch78 已读；`Weekly Only — Version/Product Fact`。不以版本
  价格和厂商 benchmark 修改长期正文。

### What 81,000 people want from AI — 21/30

- **Sources / Coverage**：Anthropic 2026-03-18 官方用户研究及方法/限制材料已核对；涵盖抽样、
  taxonomy、aggregation 与受访/平台边界。
- **Evidence / Limits**：研究能描述其样本中用户表达的需求与分布，不能证明全球 population
  preference、真实行为、模型能力或 deployment autonomy；self-selection 和平台用户结构仍在。
- **ROADMAP / Decision**：Ch62～63 与 Ch69 已读；`No Change — Already Covered`，现有章节已要求
  population、sampling frame 和 decision risk 绑定。

### OpenSeeker — 26/30

- **Source Family ID / Type / Dates**：`OPENSEEKER-GRAPH-GROUNDED-SEARCH-SFT`；
  arXiv:2603.15594v1，first-public 2026-03-16。已联合核对 arXiv HTML 全文、官方
  `PolarSeeker/OpenSeeker` repository、`OpenSeeker-v1-Data` dataset card 与
  `OpenSeeker-v1-30B-SFT` model card。仓库的 v1 release 日期为 2026-03-17；当前仓库后续出现的
  v2 不能倒写为 W12 event fact。
- **Access / Full-read Coverage**：已覆盖 metadata/revision、Abstract、Introduction、Related Work、
  data construction、trajectory synthesis、SFT、全部实验表与 Discussion，以及 concurrent-work
  appendix；官方 dataset/model/code artifact 用于核对 schema、规模和工具路径。论文没有独立
  ablation 或多次训练的统计报告，硬件、训练时间、precision 和 distributed recipe 均
  `Not Disclosed`。
- **Original Problem / Previous Design / Changed Constraint**：直接抓取搜索轨迹或让 teacher 自由
  生成问题，成本低且能复用现有 web search，但容易得到靠参数记忆即可回答的问题、缺少事实锚点，
  或把 teacher 看到的清洗后上下文误当成 student 部署时也拥有的状态。约束变化是长程检索训练既要
  可规模化生成难题，又要证明答案来自可追溯 web evidence，并让 student 面对真实、含噪 observation。
- **Mechanism / State Ownership / Control and Data Flow**：pipeline 从 seed page 扩展网页有向图，抽取
  entity subgraph 后生成问题，再做 entity obfuscation；只有 base model closed-book 失败、但在 oracle
  entity subgraph 下成功的样本才通过 rejection sampling。trajectory synthesis 中，teacher 读取摘要化
  history 加最近一步 raw observation 生成 action，student SFT 则在原始 interaction context 上学习相同
  action。Dataset owner 保存 source graph、question/answer、tool calls、trajectory 与 correctness；tool
  runtime 拥有 search/visit observation，student checkpoint 不拥有 teacher 的 privileged denoising state。
- **Implementation Details**：公开 v1 数据为 11,677 rows（约 10.3K English、1.4K Chinese），训练
  Qwen3-30B-A3B-Thinking-2507，context 上限 256K、trajectory 最多 200 tool calls。作者只执行一次
  training run、没有 hyperparameter sweep；repository 暴露 evaluation、search/visit tool 与训练数据，
  但没有足以重建完整训练硬件和 wall-clock contract 的 disclosure。
- **Evaluation Contract**：比较 BrowseComp 的 200-question subset、BrowseComp-ZH、xbench 与
  WideSearch；部分 baseline 来自其他报告或 leaderboard，而非同一 harness 的统一复跑。论文没有
  对 graph grounding、obfuscation、rejection sampling 和 asymmetric context 分别做 ablation，也没有
  给出 seed variance。模型、tool provider、query budget、context、judge 与 baseline provenance 因此
  必须随数字保留，不能将表格外推为通用 deep-research 排名。
- **What the Evidence Proves / Does Not Prove**：它证明该公开 pipeline 能构造带 source graph 和
  executable trajectory 的训练集，并在作者训练/评测合同下得到优于所列 baselines 的结果；它没有
  证明增益只来自 data quality，也不能证明更长 tool trajectory、更高问题难度或 teacher denoising 会在
  其他模型、搜索后端与实时网页上泛化。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：事实图与 rejection sampling
  提高可审计性，却继承搜索索引偏差、网页漂移、entity extraction/obfuscation 错误和 oracle leakage；
  privileged teacher context 降低 action 生成噪声，也可能让 demonstration 隐含 student 无法恢复的
  信息。直接人工-curated QA 在高风险事实与小规模领域仍更可靠；raw-trajectory imitation 在环境噪声
  本身就是训练目标时仍合理。
- **Evolution Relationship / ROADMAP / Chapters Read**：`Direct Evolution` 于 synthetic search-data
  contract，`Layering / Dependency` 于 Agentic RAG。主 owner 从初筛 Ch74 更正为 Ch72；已读 Ch23～25、
  Ch71～74。Ch23 已覆盖 executable synthetic specification，Ch25 已覆盖 privileged-context
  distillation，Ch72 已覆盖 retrieval/compression/stopping joint policy，但尚未把“graph-grounded
  hard-question filtering + teacher/student observation asymmetry”连成 search-training data flow。
- **Integration Decision / Files / Questions**：`Integrate — New Mechanism (Books Gate Pending)`；
  Gate 后优先 refine Ch72，并只向 Ch23/25 做短 handoff。开放问题是 source graph 的 freshness、
  oracle-subgraph leakage、teacher 摘要错误和不同 search backend 下的可迁移性。

### POLCA — 23/30

- **Source Family ID / Type / Dates**：`POLCA-SEMANTIC-PROGRAM-SEARCH`；arXiv:2603.14769v1，
  first-public 2026-03-16。已读 55 页官方 PDF并核对 `rlx-lab/POLCA` 官方 repository；代码同时提供
  POLCA、GEPA、OpenEvolve 与四类 benchmark 的复现实验入口。
- **Access / Full-read Coverage**：已覆盖 metadata、Abstract、Introduction、Problem Setup、算法与
  理论、Related Work、全部实验/ablation/sensitivity、Limitations、Conclusion，以及 optimizer、
  token usage、benchmark setup 与案例 appendix。理论中的 UCB 版本与公开实验的 empirical-mean
  implementation 已分开记录。
- **Original Problem / Previous Design / Changed Constraint**：保留单一 best prompt/program 或对候选
  做无记忆随机 mutation，实现简单且适合小搜索空间；当 evaluation 随 task minibatch 波动、候选语义
  大量重复、LLM optimizer 只能看到局部失败时，搜索会浪费预算并遗忘历史。新约束是同时保持质量、
  语义多样性和跨代经验，而不让完整历史无限进入 Context。
- **Mechanism / State Ownership / Control and Data Flow**：priority queue `Q` 持有 program identity、
  evaluation history 与 selection state；每轮在同一 minibatch 上选 parent、评估 accepted candidates，
  LLM optimizer 同时读取当前局部反馈和由另一 LLM 汇总的 global history。Embedding distance 与
  epsilon 构成 semantic epsilon-net，拒绝过近候选。论文理论使用 reward-aware UCB 变体，公开实验则以
  empirical mean 更新；二者不能合并成同一个已验证算法。
- **Implementation / Evaluation Contract**：tau-bench 使用 Gemini 2.0 Flash 作为 agent/optimizer、
  `text-embedding-004`、retail 前 10 tasks 训练而余下 145 held out、6 seeds；HotpotQA 与 VeriBench
  为 3 seeds；KernelBench 仅 16 个 level-1 matmul tasks、Claude 3.7 Sonnet optimizer、
  `gemini-embedding-001`、单张 L40S、每候选平均 5 次 execution，且只有 1 seed。报告 token cost
  约为 tau-bench 31.2M/run、HotpotQA 6.54M/run、VeriBench 634K/task/10 iterations、KernelBench
  570K/task/10 iterations，且明确不含被优化程序内部 LLM calls。
- **What the Evidence Proves / Does Not Prove**：作者实验支持 epsilon-net 与 global summarizer 在所测
  配置中都贡献收益，`epsilon=0` 最差、过大 epsilon 可能改善早期速度却降低后期质量；它不证明 embedding
  distance 是可靠的程序语义等价，也不证明理论 optimizer-improvement/sub-Gaussian assumptions 在真实
  LLM search 中成立。并行 metric calls 的 evaluation step 不能直接解释为端到端 wall-clock speedup。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：多样性过滤和全局摘要减少重复探索，
  却引入 embedding/model version、epsilon sensitivity、summary distortion、queue staleness、minibatch
  overfitting 和高 token cost。简单 best-of-N、人工 search 或无 embedding 的 evolutionary loop 在预算小、
  evaluator 稳定、候选可精确 canonicalize 时仍更透明。
- **Evolution / ROADMAP / Chapters Read**：`Principle Reuse` 于 evolutionary/black-box optimization，
  `Direct Evolution` 于 evaluator-driven candidate memory。主 owner 从初筛 Ch29 更正为 Ch77；已读
  Ch28～30、Ch62、Ch73、Ch76～78。Ch77 已明确由 Workflow 拥有 candidate identity、lineage、
  evaluator/version、quality/diversity selection、failed-run retention 与 held-out verification；POLCA 的
  epsilon-net 和 summarizer 是这一框架的实验性策略实例，不改变 owner contract。
- **Integration Decision / Files / Questions**：`No Change — Already Covered`。Books Gate 后也不复制
  算法或 benchmark；本项只作为 Ch77 现有论证的支持证据。开放问题是怎样以可执行行为而非单一
  embedding 距离定义 novelty，以及 summary/queue state 怎样跨 optimizer revision 复现。

### The PokeAgent Challenge — 21/30

- **Source Family ID / Type / Dates**：`POKEAGENT-LIVING-INTERACTIVE-EVAL`；arXiv:2603.15563v1，
  first-public 2026-03-16；已联合核对 arXiv HTML 全文与官方 challenge site。项目源于 NeurIPS 2025
  competition，当前为 living benchmark；动态 leaderboard 状态不能倒写为论文 v1 的固定结果。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Related Work、competitive battling、
  speedrunning、evaluation、competition/cross-track analysis、Conclusion，以及 A～H appendices 中的
  baseline architecture、system details、state/action space、成本和扩展讨论。
- **Original Problem / Previous Design / Changed Constraint**：静态问答或单回合 game score 易复现、
  适合低成本回归，但无法暴露部分可观察、随机对手、视觉定位、长程动作、memory corruption 与环境恢复。
  当任务同时需要 perception、planning、tool/action 和持续 state 时，evaluation object 必须扩展为
  `model + harness + environment + trajectory`。
- **Mechanism / Ownership / Flow**：benchmark 分为 head-to-head competitive battle 与第一道馆
  speedrun。Battle 由独立 Pokémon Showdown server 和 opponent population 驱动；Speedrun 固定帧率，
  通过 pixels 与有限 state 观察，以 milestone、completion、time/action/token/cost 记录轨迹。Baseline
  harness 用 central orchestrator 分派 perception/memory/planning/action subagents，维护最近 10 turns 的
  sliding memory，并使用 A* 等 domain tools；这些 harness choices 属 subject identity，不是 base model
  固有能力。
- **Evaluation Contract / Evidence**：同一 organizer harness 比较 frontier models；competition 报告
  100+ teams、150+ submissions、20M+ trajectories，但 Speedrun 只有 22 submissions、6 个完成者，
  第一阶段只到 first gym。13/16 qualifying battle entries 基于 RL baselines，speedrun winner 使用 LLM
  prior 加 RL refinement。结果支持 specialist RL/MCTS 在该环境中仍可能优于 generalist LLM，并揭示
  perception/localization、memory corruption、goal oscillation 与 overcommitment；不证明该排序适用于
  其他 games、harness、opponent population 或后续 leaderboard。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：living benchmark 提供持续对手与长程
  state，却引入 population non-stationarity、server/harness drift、昂贵长轨迹和难以统一的时间、动作、
  token、货币成本。静态 snapshot、固定 opponent set 与 deterministic replay 在模型回归和因果归因时
  仍不可替代；competition rank 不能取代按 failure taxonomy 的诊断。
- **Evolution / ROADMAP / Chapters Read**：`Direct Evolution` 于 snapshot-to-interactive evaluation，
  `Layering / Dependency` 于 Agent runtime。主 owner 保持 Ch62；已读 Ch61～63、Ch73～78。Ch62 已明确
  subject 包含 harness/tools/environment，区分 candidate coverage、selector、feedback-conditioned
  trajectory 与 evolving state，并要求成本、recovery 和 environment identity 并列，因此本项没有形成
  新的长期框架缺口。
- **Integration Decision / Files / Questions**：`No Change — Already Covered`。不把 Pokémon-specific
  harness、model ranking 或竞赛数字写入 Books。开放问题是 living benchmark 如何固定 opponent/harness
  revision，并同时报告跨版本可比性与现实进展。

### Code-A1 — 25/30

- **Source Family ID / Type / Dates**：`CODE-A1-COEVOLVING-CODE-TEST-RL`；arXiv:2603.15611v1，
  first-public 2026-03-16。已读 arXiv HTML 全文，并核对 ZJU-REAL 官方 project page、repository、
  training data、config 与脚本。
- **Access / Full-read Coverage**：已覆盖 metadata、Abstract、Introduction、Related Work、全部 method、
  training/system design、experiments、analysis/ablation、Conclusion，以及 A～F appendices 中的 sandbox、
  Mistake Book、training details、evaluation metrics、case study 与 limitations。
- **Original Problem / Previous Design / Changed Constraint**：固定 unit tests 便宜、确定、适合可验证
  code RL，但覆盖不足会奖励 hard-code 或漏过语义错误；让同一 code model 同时写程序和 tests 又可能
  形成 self-collusion。约束变化是 verifier 也要针对当前 policy 的错误分布学习和探索，同时保持 test
  validity、generator/verifier separation 与失败状态可重放。
- **Mechanism / State Ownership / Control and Data Flow**：Code LLM 生成候选代码；独立 Test LLM 以
  white-box 方式读取 candidate code 生成 assertions。Tests 先在 ground-truth solution 上验证，错误
  predicted answer 由 oracle 修正；code reward 合并历史与新 tests 的 pass rate，test reward 以系数
  `alpha` 平衡 validity 与让候选失败的 adversarial difficulty。两模型均用 GRPO；TopVar 只选择
  candidate-code reward variance 较高的 groups 更新 Test LLM。Mistake Book 按 `question_id` 保存 assertion
  与失败频率：失败增加，成功递减直至删除，并在每步后 JSON 持久化。
- **Implementation Details**：训练使用 Qwen2.5-Coder 1.5B/3B/7B、9,688 个 KodCode-V1 hard
  problems、每题每模型 8 responses、每轮 `K=5` tests、temperature 1.0；verl + vLLM + FSDP，
  8×NVIDIA H20、CUDA 12.8。Sandbox timeout 10s，health check 失败后 60s backoff、最多 5 次，
  execution failure 记零 reward。公开仓库使用 Python 3.10、本地 verl fork，并包含 Ray/vLLM/SGLang/
  sandbox integration；这些是作者 artifact，不是通用 RL runtime contract。
- **Evaluation Contract**：代码能力测 HumanEval+、MBPP+、BigCodeBench；test quality 使用
  UnLeakedTestBench 的 `pass@5`、`mut@5` 及乘积指标。Ablation 显示 `alpha` 两端退化、移除 code
  visibility 或 Mistake Book 都降低作者指标，但 7B code 增益较小。Test-time scaling 使用对 candidate
  black-box 的 verifier、`M=N=16`，不能与 training-time white-box Test LLM 混称同一验证机制。
- **What the Evidence Proves / Does Not Prove**：在 Python function-level、assertion-test、存在
  ground-truth solution 的合同内，独立 Test LLM、动态 tests 与 failure replay 能形成可训练的双策略
  闭环；实验不证明对 stateful programs、I/O、distributed systems、property-based testing、无 oracle
  任务或更大模型仍成立，也不证明 adversarial test reward 与真实 specification 完备性等价。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：动态 verifier 扩展当前错误覆盖，代价是
  双模型 rollout/update、oracle dependency、test leakage/collusion、Mistake Book staleness、sandbox
  nondeterminism 与更大的 attack surface。固定人工 tests 在 regression、合规和高风险发布门禁中仍是
  authority；property/independent hidden tests 仍需与 learned verifier 共存。
- **Evolution / ROADMAP / Chapters Read**：`Direct Evolution` 于 verifiable-reward interface：
  `fixed tests → independent adaptive test policy → persistent failure replay`；`Layering / Dependency` 于
  Ch62/77 的 evaluation/workflow state。主 owner 收敛为 Ch29，已读 Ch28～30、Ch62、Ch73、Ch77。
  Ch29 已写 verifier 是可被优化的 specification、environment identity 与 held-out adversarial tests，
  但尚未完整表达 verifier 自身成为独立 policy 后的 state ownership、更新选择与 stale failure memory。
- **Integration Decision / Files / Questions**：`Integrate — New Mechanism (Books Gate Pending)`；
  Gate 后考虑 refine Ch29，Ch62/77 只做 verifier identity 与 durable failure-state handoff。开放问题是如何
  防止 code/test policies 共适应同一 oracle、怎样 version/expire Mistake Book，以及没有 ground-truth
  solution 时怎样维持 test validity。

### HorizonMath — 24/30

- **Source Family ID / Type / Dates**：`HORIZONMATH-OPEN-PROBLEM-VERIFICATION`；
  arXiv:2603.15617v1，first-public 2026-03-16，论文自标 `Working Draft`。已读 arXiv HTML 全文、
  evaluation/discussion 与两项潜在新 construction 的完整 appendix，并核对官方
  `ewang26/HorizonMath` evaluation repository。
- **Original Problem / Previous Design / Changed Constraint**：已知答案的 math benchmark 成本低、
  scorer 清楚，仍适合能力回归，却无法区分记忆与发现；完全依赖专家评审或 proof assistant 又昂贵且
  难规模化。作者选择 generator-verifier gap：只纳入“候选难生成、具体对象易计算验证”的未解问题，
  把 research evaluation 从自然语言 proof 缩到 closed form、优化 construction 与 existence object。
- **Mechanism / Ownership / Flow**：101 个问题按 output type、solvability level 和 8 个 domain 组织；
  model 输出 `proposed_solution()`。LLM compliance checker 先检查 forbidden operation，再路由到三类
  verifier：高精度 numeric comparison、相对 published baseline 的 improvement scoring、或 property
  construction check。Dataset owner 持有 problem/source/baseline/admissibility；repository 持有 executable
  checker；expert community 仍拥有“是否构成数学贡献”的最终 claim authority。
- **Implementation / Evaluation Contract**：closed-form 数值最多比较 20 decimal digits，并限制可用
  operation；construction/optimization 使用 problem-specific validators。论文评测 GPT-5.4 Pro、Gemini
  3.1 Pro、Claude Opus 4.6；前两者 high reasoning，Claude 使用最大 output limit。10 个 level-0
  calibration problems 中三者分别通过 5/3/3；GPT-5.4 Pro 在 level 1～3 提出两项通过自动 checker 的
  improvement，但 13 个问题因 API errors 未得到 GPT 结果。硬件、wall-clock、token/cost、重复采样和
  statistical uncertainty `Not Disclosed`。
- **Evidence Boundary / Limitations**：deterministic construction checks 能证明编码 property 在当前
  validator 下成立；高精度数值相等不等于 closed-form proof，LLM compliance checker 也可能 false
  accept/reject。论文明确将两项结果称为 pending expert review。更重要的是，“答案尚未知”只降低 solution
  contamination，不能证明 prompt、background、partial constructions 或 evaluation logic 从未进入训练。
- **Trade-offs / Coexistence / Evolution**：开放 verifier 提高复现与搜索速度，也扩大 benchmark gaming、
  checker bug、baseline drift 和 community-update versioning 风险。Formal proof、独立数学复核与私有
  holdout 在 theorem correctness 和 anti-overfitting 上继续成立。关系为 `Direct Evolution` 于
  `known-answer scoring → open-problem executable candidate → expert-confirmed claim`。
- **ROADMAP / Chapters / Decision**：主 owner Ch62，已读 Ch61～63、Ch76～77。Ch62 已覆盖
  `artifact + environment + executable verifier`、claim-level provenance、verifier 不完备和 expert
  authority，现有论证足以容纳该案例；`No Change — Already Covered`。开放问题是 living problem set
  如何冻结版本、隔离 checker evolution，并防止持续公开后 search-level overfitting。

### MiroThinker-1.7 & H1 — 25/30

- **Source Family ID / Type / Dates**：`MIROTHINKER-VERIFICATION-CENTRIC-RESEARCH-AGENT`；
  arXiv:2603.15726v1，first-public 2026-03-16。已读 23 页 official PDF，覆盖架构、training pipeline、
  verification mode、全部 benchmark/analysis 与 references；并核对 `MiroMindAI/MiroThinker` repository、
  1.7 model card 与配置。1.7/1.7-mini 为开放模型，H1 为 proprietary system，不能以开放 artifact 反证
  H1 内部实现。
- **Original Problem / Previous Design / Changed Constraint**：延长 ReAct turns 和保留完整 Context
  能扩大探索，对短任务仍简单有效；长程 research 中却会累积噪声、重复确认高概率路径并过早从不充分
  evidence 得出结论。约束从“允许更多 interaction”变成“每一步和整条证据链是否值得继续”。
- **Mechanism / State Ownership / Flow**：1.7 组合 256K Context、sliding-window filtering、result
  truncation、episode restart 与 search/scrape/sandbox/file tools。训练依次执行 agentic mid-training、
  trajectory SFT、DPO+preferred SFT、online GRPO；rollout runtime 用 shared queue、buffer 和 long-tail
  priority scheduling，negative rollouts 的低概率 tokens 施加 targeted KL。H1 在 inference 增加 Local
  Verifier，针对当前 step 促使替代搜索；Global Verifier 汇总完整 evidence chain，不充分时要求补全或
  resample。Workflow 拥有 budget/retry/stop，verifier 只产生反馈，不能自证最终事实。
- **Implementation / Evaluation Contract**：paper 比较 BrowseComp、BrowseComp-ZH、xbench、Seal-0、
  HLE、FrontierScience、FinSearchComp 等；默认 temperature 1.0、top-p 0.95、256K context、16,384
  max output，多数 benchmark 200 turns，部分 search benchmark 使用更高 turn budget。相关站点在 tool
  环境被 block 以降低检索泄漏。Local-only 分析使用从 BrowseComp 挑出的 295-question hard subset，
  因样本按 1.7 易失败选择，不能与 full-set gain 混用；64× token scaling 也是 H1/该 harness 的结果。
  训练 token、数据规模、硬件、随机种子、verifier false-accept/false-reject 与成本多数未披露。
- **Evidence Boundary / Limitations**：报告支持 local/global verification 在作者 system/harness 下与更高
  pass rate、较少无效 steps 相关，不隔离 base-model、training、tool、context management 和 verifier
  各自因果贡献；跨厂商表格还混合不同 agent products、工具与 budgets。论文没有系统性的独立 verifier
  calibration，因而不能把 H1 自有 judge 当作 correctness oracle。
- **Trade-offs / Coexistence / Evolution**：局部反馈可阻止惯性路径，全局 audit 可阻止 evidence 不足的
  premature answer，却增加 verifier correlated error、反复 resample、Context/token cost 和 stop-policy
  复杂度。单次 deterministic verifier、固定 Workflow 和人工 research review 在证据可形式化或风险高时
  仍更强。关系为 `Direct Evolution` 于 `longer trajectory → step feedback + chain audit → bounded retry`。
- **ROADMAP / Chapters / Decision**：主 owner 从初筛 Ch74/77 收敛到 Ch76；已读 Ch71～78 与 Ch62。
  Ch76 已按 feedback independence、constraint-wise audit、evidence-backed repair 与 stopping policy 表达
  相同长期机制，Ch62 已要求 verifier calibration；`No Change — Already Covered`。版本化模型能力与
  benchmark 数字只留 Weekly。

### Online Experiential Learning — 26/30

- **Source Family ID / Type / Dates**：`OEL-DEPLOYMENT-EXPERIENCE-CONSOLIDATION`；
  arXiv:2603.16856v1，first-public 2026-03-17；Microsoft Research paper、Appendix A～C、官方
  `microsoft/LMOps/oel` code path 与研究文章联读。它依赖同系列 On-Policy Context Distillation，
  relation 为 `Layering / Dependency`，不是两个独立无关事件。
- **Original Problem / Previous Design / Changed Constraint**：离线 SFT/RL 冻结训练分布，稳定、便于
  审计，在环境可模拟时仍合理；直接把 raw deployment trajectory 塞入 Context 或做 off-policy imitation
  会带入冗余、失败细节和 teacher/student distribution mismatch。新约束是用户侧环境不可在 server 重放，
  但只能上传 textual feedback/trajectory，又希望把可迁移经验写回参数。
- **Mechanism / State Ownership / Flow**：用户侧 policy 收集两组 trajectories；server 以当前 policy 作为
  extractor，把 success/failure interaction 压成 structured/unstructured experiential knowledge `C`。
  另一组 trajectories 产生 partial rollout prefixes；冻结 teacher 读取 `C + prefix`，student 只读 prefix，
  并在 student 自己生成的 token prefixes 上最小化 reverse KL。更新后的 checkpoint 再部署收集下一轮。
  User-side runtime 拥有 raw environment state，experience store 拥有 trajectory/provenance，extractor
  产生可失效 derived knowledge，training system 拥有 teacher snapshot、student checkpoint 和 round lineage。
- **Implementation / Evaluation Contract**：只在 TextArena Frozen Lake 与 Sokoban 文本游戏上评测
  Qwen3 1.7B/4B/8B thinking 与 Qwen3-4B-Instruct-2507；student temperature 0.7，reverse KL 只计算
  student top-256 vocabulary，learning rate `1e-6` 或 `5e-6`，每轮 20/100 steps。Raw-vs-extracted
  knowledge 对照只在 Qwen3-4B-Instruct Sokoban；OOD forgetting 对照只在 Qwen3-1.7B Frozen Lake 对
  IF-Eval。GPU、wall-clock、privacy pipeline、sample variance 与真实用户环境均 `Not Disclosed`。
- **Evidence Boundary / Limitations**：实验支持 extracted knowledge 在这些文字游戏中优于 raw trajectory，
  on-policy consolidation 比所测 off-policy alternative 更少损伤 IF-Eval，并可迭代提升；它不证明
  无 scalar reward 就没有 selection bias，也不证明真实 deployment feedback 正确、可授权上传或跨用户
  可合并。自举 loop 还可能让 extractor 与 policy 的共同盲点逐轮放大。
- **Trade-offs / Previous Design / Evolution**：参数 consolidation 降低以后每次调用的 Context 成本，
  却丢失即时回滚与 per-user separation，并新增 consent、PII、poisoning、experience weighting、teacher
  staleness、catastrophic forgetting 和 delete-from-weights 问题。Raw episodic memory 在需要 provenance、
  correction、个性化和删除时仍更合适；离线 curated training 在安全 gate 与 distribution control 上继续成立。
  演进为 `raw episode → extracted derived strategy → on-policy context distillation → versioned checkpoint`，
  不是 Memory 被参数训练替代。
- **ROADMAP / Chapters / Decision**：主 owner Ch73，已读 Ch23～25、Ch28～30、Ch71～73、Ch77。
  Ch73 已覆盖 raw trajectory 到 derived strategy 及其 provenance/supersession，但尚未明确 derived memory
  继续进入 parameter consolidation 后 owner、deletion 与 rollback 怎样改变；Ch25 已完整解释同-prefix
  on-policy context distillation。`Integrate — New Mechanism (Books Gate Pending)`，Gate 后 refine Ch73，
  只向 Ch25 做短 handoff。

### TRUST-SQL — 23/30

- **Source Family ID / Type / Dates**：`TRUSTSQL-PHASE-SPECIFIC-AGENT-RL`；arXiv:2603.16448v1，
  first-public 2026-03-17。已读 arXiv HTML 全文、A～E appendices 与匿名 reproducibility repository。
  v1 承诺 acceptance 后发布 datasets/weights；当前可核验的是 paper 与 code snapshot，不写成已正式 release。
- **Original Problem / Previous Design / Changed Constraint**：把完整 DB schema 预填 Context 能减少 tool
  round trips，适合小而稳定数据库；enterprise schema 大、噪声多、持续变化时，prefill 成本与 stale
  metadata 上升。纯 terminal execution reward 又无法区分 schema exploration 与 SQL logic，长轨迹 credit
  assignment 会鼓励无效枚举。
- **Mechanism / State Ownership / Flow**：POMDP protocol 为 Explore → Propose → Generate → Confirm；
  Propose 强制提交已验证 table/column checkpoint，Generate 执行候选 SQL，失败可回到探索。Dual-Track
  GRPO 以 Propose 为 token mask 边界：schema track 使用 schema reward，full track 使用 execution reward，
  总 loss 由 `lambda` 加权。Schema reward 只有 execution success 时才生效，避免“找对列但 SQL 错”获得
  独立正反馈。DB/tool runtime 拥有 authoritative schema/result，trajectory 持有 phase/action，trainer
  拥有 masks、ground-truth schema label、reward/version 与 rollout policy。
- **Implementation / Evaluation Contract**：Qwen3-4B/8B 先 SFT 再用 SLIME 训练；4B SFT 16×A100、
  RL 8×A100 synchronous，8B SFT 16×A100、RL 32×A100 asynchronous；RL batch 32、8 rollouts、
  train max 10 turns。18,078 train questions 经 8 次 rollout 后保留 pass-rate `<6/8` 的 11,642 项；
  schema labels 由 GPT-4.1、LongCat-Flash、Gemini-2.5-Pro 对 gold SQL 的 2/3 consensus 抽取。评测 BIRD、
  Spider 及三个 robustness variants，只使用 SQLite；majority sampling temperature 0.8、inference max
  15 turns。
- **Evidence Boundary / Ablation**：phase pilot、`lambda`、schema reward coupling/density、turn budget、
  SFT cold start 与 pass@K 均有作者 ablation。RL-only 表面高分实际通过第一轮穷举 schema reward-hack；
  schema weight 太高会无限探索；uncoupled reward 增加 turns 却降低 execution accuracy。这支持“结构边界
  和 reward coupling 是 objective semantics”，不证明相同四阶段适用于 PostgreSQL/MySQL、超大 live
  catalog、权限过滤、write query 或真实 workload。论文把 benchmark gain 称为 generalization 的表述
  超出五个 SQLite test sets 能证明的范围。
- **Trade-offs / Coexistence / Evolution**：active exploration 减少 upfront Context 和 parametric schema
  hallucination，换来 live DB calls、latency、catalog permission、turn budget、tool failure 与 masked-reward
  implementation complexity。Full-schema prefill 在小 schema、offline query 和严格 latency SLO 下仍合理；
  deterministic schema linker 在规则充分时也更透明。演进为 `terminal reward → phase checkpoint →
  phase-specific masked advantages`，同时产生 reward hacking 和 phase-boundary gaming。
- **ROADMAP / Chapters / Decision**：主 owner 从初筛 Ch77 更正为 Ch29；已读 Ch28～30、Ch62、Ch72、
  Ch74、Ch77。Ch29 已覆盖 group reward、verifier/environment identity，却未完整表达 heterogeneous
  action phases 如何用 token masks 隔离 credit、以及 structural warm-up 如何阻止合法但退化的 reward
  shortcut。`Integrate — New Mechanism (Books Gate Pending)`；Gate 后 refine Ch29，Ch72/74/77 只做
  unknown-schema retrieval、tool authority 和 workflow phase handoff。

### Efficient Reasoning on the Edge — 26/30

- **Source Family ID / Type / Dates**：`EDGE-REASONING-CROSS-LAYER-CODESIGN`；
  arXiv:2603.16867v1，first-public 2026-03-17；当前 v2 修订于 2026-06-03。历史事件只使用 v1，
  后续 revision 仅用于核验机制。已读 v1 的 44 页论文全文、关键 appendices、v2 revision metadata
  与 Qualcomm 官方 project page；project page 提供移动端演示和设计说明，但未提供可复算的端侧
  benchmark log 或完整训练/部署代码。
- **Access / Full-read Coverage**：已覆盖 system design、LoRA SFT、rank/learning-rate/batch ablation、
  switcher 与 masked-LoRA、budget-forcing reward/GRPO、parallel test-time scaling、latent verifier、
  quantization/QAMR、ONNX/QNN/GENIE export、全部 evaluation、Discussion/Challenges 和影响结论的
  appendices。论文没有独立 Threats to Validity，实际手机型号、NPU 规格、DRAM、端侧 TPS/TTFT、
  energy、并行流数与 SLO `Not Disclosed`。
- **Original Problem / Previous Design / Changed Constraint**：固定 reasoning model 对每个请求都生成
  CoT，接口简单、质量路径一致，在 cloud 或高难请求上仍合理；边缘设备却同时受 model footprint、
  KV、逐 token latency、功耗和连接可用性约束。把多个专用模型分别加载又增加 weight movement。
  约束变化使问题从“怎样让小模型会 reasoning”变成“怎样按请求只支付必要 reasoning，并让训练状态、
  prefill state、decode policy 与低比特部署相容”。
- **Mechanism / State Ownership / Control and Data Flow**：同一 Qwen2.5 base 以 reasoning LoRA 表达
  可切换能力；base-only prefill 的最后层 hidden states 经 chunked EMA 汇总，8-hidden-unit MLP switcher
  决定 decode 是否启用 adapter。普通 LoRA 会期待 adapter-on prompt KV，路由后再启用 adapter 将导致
  cache identity 不一致；masked-LoRA training 在 prompt positions 关闭 adapter、只在 response positions
  启用，使 reasoning decode 显式学习消费 base-only KV。Checkpoint 拥有 base/adapter/switcher/verifier、
  mask policy 与 quantization encodings；runtime 拥有 chunk state、route decision、KV identity、并行样本、
  selector 和 stop/budget；export chain 拥有 ONNX/QNN/GENIE artifact lineage。
- **Implementation / Evaluation Contract**：SFT 使用 Qwen2.5-3B/7B、MoT 350K 与 OT3 1.2M traces，
  bf16、5 epochs、DeepSpeed ZeRO-2/CPU offload；主 LoRA rank 128、alpha 256、batch 64、learning rate
  `2e-4`。Switcher 约 2K labeled prompts，prefill chunk 128、EMA alpha 0.5，训练注入 sigma 0.5
  Gaussian noise。Budget RL 基于 TRL 0.26.2、8×H100 80GB、每 prompt 8 rollouts。Quantized path 为
  W4A16KV8，base quantization 在单张 H100 80GB 上少于 24 小时；export 目标示例为
  `aarch64-android`。这些训练条件不能替代缺失的真机 latency/energy contract。
- **What the Evidence Proves / Does Not Prove**：作者的 controlled results 支持高质量 trace、LoRA
  capacity、masked prompt training、route threshold、KL coefficient、parallel candidate selection 与
  quantization-aware adapter training在其 Qwen2.5/math-science-code 配方中分别贡献可用 trade-off。
  `2.4x` reasoning-token compression、verifier gain 与接近全精度的量化结果只绑定相应模型、benchmark
  和 generation contract；project demo 证明可运行，不证明吞吐、能耗或任意手机上的生产 SLO。
  Switcher 按 dataset source 构造 difficulty label，也未证明能校准真实 query mix 或 distribution shift。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：base-only prefill 省去 route 后重算，
  却把训练语义限制为“adapter 只改变 response-side computation”；需要 prompt-side specialization 的
  adapter 不能直接共享这份 KV。False-negative routing 丢失难题质量，false-positive 增加 token/KV/
  power；parallel samples 把闲置 compute 换成更多 KV 与 selector correlated error；QAMR 又增加 mixed-
  precision ownership、export compatibility 和 calibration drift。固定 base 或 always-on reasoning 在
  workload 单一、route risk 高、cache 复用小或 prompt-side adapter 必需时仍更合理。
- **Evolution / ROADMAP / Chapters Read**：`Direct Evolution` 于动态 adapter serving：`per-model load
  → shared base + request adapter → post-prefill route + training-defined KV compatibility`；`Layering /
  Dependency` 于 Ch20 parallel sampling、Ch29 budget RL、Ch39～41 prefill/decode/KV 和 Ch50 memory。
  主 owner 从 Ch42/45 更正为 Ch26；已读 Ch25～27、Ch29、Ch39～42、Ch45 与 Ch50。Ch26 已覆盖
  dynamic adapter、base/version/quantization contract，却没有表达“route decision 晚于 prefill 时，
  cache compatibility 必须由训练 mask 预先定义”。
- **Integration Decision / Changed Files / Open Questions**：`Integrate — New Mechanism (Books Gate
  Pending)`；Gate 后优先 refine Ch26，Ch20/29/39～41/50 只做预算、并行选择和 KV identity handoff。
  仍需真机 workload contract、switcher calibration/shift、prompt-side adapter 边界和 multi-adapter route
  的公开验证。

### SWE-Skills-Bench — 24/30

- **Source Family ID / Type / Dates**：`SWE-SKILL-MARGINAL-UTILITY-EVAL`；arXiv:2603.15401v1，
  first-public 2026-03-16，当前仅 v1，论文自标 preliminary work in progress。已读 arXiv HTML 全文、
  methodology、全部 49-skill results 和 Discussion；论文链接的官方 GitHub repository 在本次访问中
  无法读取，故 repo-side task/config/test completeness 为 `Not Independently Verified`，不会用论文
  “available” 声明替代 artifact 检查。
- **Original Problem / Previous Design / Changed Constraint**：把 procedural guidance 放进 Context
  易部署、可撤销，也能在模型缺少特定 domain rule 时补能力；但“skill 看起来相关”不等于它比 base
  policy 的既有知识更有边际价值。随着公开 skill 快速增加，平台需要区分 capability coverage、token
  overhead、version compatibility 与 context interference，而不是只测带 skill 后的绝对成功率。
- **Mechanism / State Ownership / Control and Data Flow**：每项任务由固定 commit 的真实 repository
  `R`、container environment `E`、显式 requirement `P` 与可选 skill `S` 组成；acceptance criteria 被
  编译为 pytest execution checks，再对同一任务做 with-skill / without-skill paired evaluation。Registry
  拥有 skill identity/version/source；task owner 拥有 repo commit、requirement 和 acceptance criteria；
  harness 拥有 injection condition、container、test generator与 verdict；agent 只消费注入后的 Context。
- **Implementation / Evaluation Contract**：49 个公开 skills、约 565 instances、6 个 SWE domains；
  Ubuntu 24.04 CPU-only containers，agent 固定 Claude Code + Claude Haiku 4.5。论文分别按 skill 统计
  paired pass-rate delta、input/output token cost、relative overhead 与 cost efficiency。Task requirement
  不显式提到 skill。正文对 skill 注入位置存在 `~/.claude` 与 project root 两种描述，重复运行、seed、
  API revision、test-generation model/version、人审覆盖率及 confidence interval `Not Disclosed`。
- **What the Evidence Proves / Does Not Prove**：在该单一 agent/model/harness snapshot 中，39/49
  skills 没有 pass-rate 增益，平均 delta `+1.2%`，少数专用 skill 有正增益，三个 version-mismatched
  skills 产生负迁移；token overhead 与 correctness 不单调。它支持“skill utility 是相对 base policy、
  target version 和 executable requirement 的条件量”，不证明 skill 通常无用，也不证明这些比例可
  外推到其他模型、agent runtime、非 Python verifier、高难任务或生产 repositories。自动生成 tests
  的通过也不等于完整 specification correctness。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：Skill 可在不改权重时注入程序性
  先验，代价是 Context、anchoring、陈旧 API、互相冲突和 activation 误判。过度具体模板会把旧版本
  参数复制到新环境，抽象原则又可能缺少可操作性。Base-only 在模型已有能力或 compatibility 未验证时
  更稳；fine-tuning/tool enforcement 在需要稳定执行或可机器约束时仍是独立分支。
- **Evolution / ROADMAP / Chapters Read**：`Direct Evolution` 于 skill governance：`publish artifact
  → verify provenance → match capability/version → paired marginal-utility evaluation → controlled rollout`。
  主 owner 从 Ch62/77 收敛为 Ch80，Ch62 负责 paired EvalSpec 与 executable evidence。已读 Ch61～63、
  Ch77、Ch79～80；Ch80 已覆盖 skill identity/provenance/revocation，却未完整表达 activation 前必须
  以 no-skill counterfactual、version compatibility 和 token overhead 验证边际收益。
- **Integration Decision / Changed Files / Open Questions**：`Integrate — New Mechanism (Books Gate
  Pending)`；Gate 后 refine Ch80，Ch62 只做 paired evaluation handoff。需继续核验官方 repository 的
  task/test artifacts、injection path discrepancy、重复运行方差和多模型结果。

### FlashSampling — 27/30

- **Source Family ID / Type / Dates**：`FLASHSAMPLING-EXACT-LMHEAD-FUSION`；
  arXiv:2603.15854v1，first-public 2026-03-16；v2 修订于 2026-05-12。已读 v1 的 26 页论文全文、
  theory、algorithms、experiments 与 appendices，并核对当前官方 repository、tests 和 REPRODUCTION。
  v1 的 end-to-end headline 为最高约 19%；当前 v2 将摘要改为最高 10% 并加入更完整 TP 路径，故 v1
  数字只作为历史作者实验，不能继续写成当前结论。
- **Original Problem / Previous Design / Changed Constraint**：标准 `LM head → materialize [B,V]
  logits → softmax/filter → sample` 容易实现、支持丰富 logits processors，在大 batch/compute-bound
  场景仍可由成熟 GEMM 取胜；但 decode 小 batch、large vocabulary 时，写回并再次读取 logits 会增加
  HBM traffic 和 kernel launches。约束变化是 sampling 不再只被视为概率语义，而成为 LM-head epilogue
  的 I/O problem。
- **Mechanism / State Ownership / Control and Data Flow**：对经过 temperature/bias/mask 的 logits
  使用 Gumbel-Max：逐 tile 在片上计算 `logit + Gumbel`，每 row/tile 只保留最大 score 与 index，最后
  对小 candidate buffer reduction；不需显式 softmax 或 normalization。Pathwise exactness 来自全局
  argmax 可由 partition maxima 合并；grouped/online/TP variants 通过 group log-mass 的 hierarchical
  categorical factorization 保持 distributional exactness。Decoding config 拥有 transform order/mask/RNG；
  kernel 拥有 tile state；TP runtime 拥有 shard identity、group mass 和跨 rank reduction/communication。
- **Implementation / Evaluation Contract**：v1 Triton 3.6 / CUDA 13 / PyTorch 2.10 / FlashInfer 0.6.x，
  BF16 inputs/weights，25 warmups、100 timed medians；H100/H200/B200/B300，batch 1～256，主 shape
  `D=4096,V=151936`，另测 `D=8192,V≈128K`。End-to-end vLLM v1 在单 B200、Qwen3-1.7B/8B/32B 与
  gpt-oss-120B、AIME prompts、Poisson request rate、concurrency 1～64、5 runs 下比较 TPOT。当前
  reproduction 文档已改为 TP1/TP2 与 Llama-3.3-70B 等 v2 contract；v1 fork/脚本因 double-blind 未公开，
  因此 end-to-end v1 尚不能从 public artifact 独立复算。
- **What the Evidence Proves / Does Not Prove**：exactness proof、5K-sample chi-squared checks、logits-store
  ablation 与 roofline 支持“收益主要来自避免 logits round trip，且集中在 bandwidth-bound decode”。
  v1 显示 `B<=64` 的作者 microbench 中普遍快于三种 baseline，但 batch 增大接近 ridge point 后 Triton
  GEMM 可输给 cuBLAS；大模型 end-to-end gain 也更小。它不证明任意 top-k/top-p/grammar/logits-
  processor chain 已实现：v1 只在理论上覆盖 transforms，多种策略的实现明确留待 future work。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：fusion 消除中间 tensor 与 launch，
  也把 sampling semantics、RNG determinism、mask、kernel layout 与 LM-head implementation 紧耦合；
  processor 不可融合、需要完整 logits/logprobs、debug/audit 或高 batch GEMM 主导时，materialized path
  仍更简单。TP hierarchical sampling 降低 logits communication，却新增 shard/group identity、RNG
  reproducibility 和 failure/retry consistency。
- **Evolution / ROADMAP / Chapters Read**：`Direct Evolution` 于 sampling execution：`materialized
  probability pipeline → standalone online Gumbel-Max → LM-head fused exact sampler → hierarchical TP
  sampler`；它不替代 speculative decoding。主 owner 从 Ch44 更正为 Ch20，`Layering / Dependency`
  于 Ch40 decode I/O、Ch33 TP 与 Ch50 HBM。已读 Ch19～21、Ch33、Ch39～41、Ch44～46 与 Ch50。
  Ch20 已覆盖 sampling semantics/config/seed，却缺少“保持同一 categorical distribution时，sampling
  可以改变 materialization boundary”的系统推导。
- **Integration Decision / Changed Files / Open Questions**：`Integrate — New Mechanism (Books Gate
  Pending)`；Gate 后 refine Ch20，Ch40/33/50 做短 handoff。需跟踪 v2 TP 实现、公开 vLLM patch、
  top-k/top-p/grammar processors 和跨重试 RNG contract；任何性能数字必须按 revision 分开。

### MetaClaw — 26/30

- **Source Family ID / Type / Dates**：`METACLAW-TWO-TIMESCALE-AGENT-ADAPTATION`；
  arXiv:2603.17187v1，first-public 2026-03-17，当前仅 v1。MetaClaw project/repository 最早公开 release
  记录为 2026-03-09，W12 记录的是 03-17 technical-report event；已读论文 HTML 全文、prompt/template
  appendix 和官方 repo/config/benchmark/uninstall 文档。03-24 以后 memory releases 不倒写为 W12 fact。
- **Original Problem / Previous Design / Changed Constraint**：raw trajectory memory 可追溯、易删除，
  static skill 可快速注入，offline retraining 稳定且可审计；它们分别适合事实回忆、可逆行为补丁和有
  维护窗口的模型更新。长期个人 Agent 的 task distribution 漂移且不能频繁停机后，问题变成怎样协调
  external skill 与 parameter update，并防止用旧行为生成的数据训练新行为。
- **Mechanism / State Ownership / Control and Data Flow**：失败 trajectories 进入 support set，由 LLM
  evolver 合成新 skills，立即提升 skill generation `g`；新 skill 生效后的 trajectories 才进入 query/RL
  buffer，旧 generation samples 被 flush。OMLS 根据 sleep window、keyboard inactivity 或 Google
  Calendar occupancy 延迟 cloud LoRA + PRM RL；更新完成后 hot-swap policy。Proxy 持有 conversation/
  injection path，skill store 持有 versioned external policy，buffer 持有 trajectory/reward/generation，
  trainer 持有 LoRA/checkpoint，scheduler 只决定 opportunity，不能证明 update safe。
- **Implementation / Evaluation Contract**：MetaClaw-Bench 为 934 questions / 44 simulated workdays：
  Part I 30 天 346 项，Part II 14 天 588 项，persistent workspace 与 automated file checks；比较 GPT-5.2
  和 Kimi-K2.5，Full RL 只对 Kimi-K2.5 做 5-day cloud-LoRA run。AutoResearchClaw A/B 只使用同一
  research topic 和一次 23-stage pipeline configuration。公开 repo 以 local proxy 接入多种 agent，skills
  default enabled、RL 在 v0.2 后 opt-in；默认配置示例含 PRM/evolver GPT-5.2、LoRA rank 32、batch 4。
  训练硬件、token/cost、random seeds、PRM calibration、hot-swap duration distribution 与 SLO 多数
  `Not Disclosed`。
- **What the Evidence Proves / Does Not Prove**：作者结果支持在其 synthetic multi-day CLI rules 中，
  skill-only 对 procedural question 有边际收益，skills + RL 对 file execution 的增益更大；late hard days
  各条件仍共同下降，skill-only 对部分 file completion 不改善。AutoResearchClaw 的 robustness 表只证明
  同一 topic/run configuration 下的 paired case。它不证明任意真实用户对话可安全成为训练信号，
  不证明 calendar/idle 等于资源和隐私许可，也不能把 Kimi-K2.5 单一 Full-RL run 外推到其他模型。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：外部 skill 快且可回滚，但占 Context、
  可能陈旧/冲突；parameter update 降低长期 prompt 依赖，却难以解释、删除或按用户隔离。Support/query
  generation 防止一种 stale-data contamination，不解决错误 PRM、poisoned failure、skill conflict、
  catastrophic forgetting、cross-tenant mixing 和权重级删除。Repo 提供整目录 uninstall，但没有单条
  experience/skill/weight provenance 的 selective delete 或 checkpoint rollback contract。Offline curated
  training、人工批准 skill 和 raw episodic memory 在高风险/强审计场景仍成立。
- **Evolution / ROADMAP / Chapters Read**：`Direct Evolution` 于 Agent feedback plane：`raw episode
  → derived external skill → generation-separated post-adaptation data → opportunistic parameter update →
  governed rollout`；`Layering / Dependency` 于 Ch73 derived memory、Ch77 durable workflow 与 Ch29 RL。
  主 owner 从 Ch73/78 收敛为 Ch80；已读 Ch28～30、Ch72～74、Ch77～80。Ch73 已覆盖 derived strategy
  provenance，Ch80 已覆盖 run evidence 到 governed change，却尚未明确两个 adaptation timescales 之间
  的 support/query generation、scheduler opportunity 和 weight hot-swap recovery contract。
- **Integration Decision / Changed Files / Open Questions**：`Integrate — New Mechanism (Books Gate
  Pending)`；Gate 后 refine Ch80，Ch73/29/77 只做 state/learning/workflow handoff。需核验真实 workload、
  PRM calibration、user consent/tenant isolation、skill conflict resolution、partial-update recovery、
  checkpoint rollback 与 parameter deletion。

### Complementary Reinforcement Learning — 25/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `COMPLEMENTARY-RL-COEVOLVING-ACTOR-EXTRACTOR`；arXiv:2603.17621v1，first-public
  2026-03-18；v2 修订于 2026-06-27，W12 事件仍固定为 v1。已读 v1 HTML 全文、公式、算法、四组
  实验与 appendices，并核对当前 arXiv revision 和 Alibaba ROLL 官方仓库。ROLL 可验证通用 RL
  framework 与论文归属，但尚未在公开路径中定位可独立复现实验的 Complementary RL 配置，故 artifact
  状态为 `Partially Verified`。
- **Original Problem / Previous Design / Changed Constraint**：离线 curated memory、固定 extractor 或
  actor-only RL 的责任边界清楚，训练分布稳定时也更容易复现；但长期 Agent 的 policy 会持续改变其
  trajectory distribution，固定经验很快与新 policy 失配。约束变化是经验不再是静态 Context，而是由
  当前行为产生、又反过来改变后续行为的 endogenous state。
- **Mechanism / State Ownership / Control and Data Flow**：独立 actor `pi_theta` 与 extractor `pi_phi`
  采用不同 RL objectives 共演化。Extractor 从完整 trajectory 提炼结构化 experience，以“该 experience
  指导的新 trajectory 是否成功”的 binary outcome 作为 reward，并用 CISPO 更新；actor 用 GRPO，
  但把 experience-guided 与 experience-free rollouts 分组归一化，避免把两种条件的 reward baseline
  混在一起。集中式 ExperienceManager 持有 queue、embedding cache 与 semantic index，写入需 writer
  lock，读取使用 reader lock；Add/Update/Return 和周期性 LLM merge 改变持久状态，`search_and_ask`
  允许 actor 在 episode 内查询并继续修正 experience。Actor 与 extractor 可独立调度，因此
  policy/extractor version、retrieval generation 和 merge generation 都应进入 lineage，而不能只记录
  最终文本。
- **Implementation Details / Evaluation Contract**：一般任务使用 Qwen2.5-7B-Instruct actor、
  Qwen3-4B-Thinking-2507 extractor，SWE-Bench actor 改为 Qwen3-4B-Instruct；训练基于 ROLL/Megatron，
  rollout 用 vLLM，检索用 Qwen3-Embedding-0.6B。公开 contract 包括 4 个 search/embedding workers、
  query batch 16、extractor buffer 64、merge interval 5、group size 8、max turns 30、actor sequence
  32768、extractor sequence 65536；multi-task batch 384、每任务 128、训练 128 steps。论文覆盖
  MiniHack、WebShop、ALFWorld 与 SWE-Bench；硬件型号/数量、precision、seeds、置信区间、持久库规模、
  crash consistency 与线上 SLO 为 `Not Disclosed`。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：作者对比 actor-only、静态经验、
  Self-Distillation 与多种经验协作变体；multi-task 表中 baseline 平均 0.75，Complementary RL 有经验
  0.82、无经验 0.78。Separate parameters 比 shared parameters 稳定；Actor-Critic accept/refine/reject
  早期收益更好但阻塞 rollout 并增加 latency；Self-Distillation 后期 collapse，perplexity-reduction reward
  也未被采用。结果支持“在这些作者设置中，分离 actor/extractor objectives 并共同演化经验可改善任务
  成功率”，并揭示 group-conditioned advantage 与 stale experience 的训练问题。
- **What It Does Not Prove / Limitations / Threats to Validity**：binary downstream success 不能识别某条
  memory 的独立 causal credit；同一 extractor、embedding、merge policy 和 benchmark contract 也不能
  外推到开放生产 workload。论文未证明大规模多租户一致性、experience delete、merge rollback、
  poisoned trajectory 防护或故障恢复；单一作者实现和未披露统计不确定性也限制普适结论。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：在线共演化提高适应性，却新增 actor/
  extractor staleness、writer-lock bottleneck、merge distortion、cross-task contamination、cache/index
  consistency 与 off-policy retrieval lag。作者用 retrieval diversification 和按训练次数/recency 的
  advantage reweighting 缓和而非消除这些风险。高风险域、稳定任务、低写入频率或需要逐条撤销时，
  offline curated memory、固定 extractor 和人工批准策略仍更合理。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Direct Evolution` 于
  experience-driven RL：`static curated experience → actor-only/self-distilled experience → separately
  optimized extractor + actor → versioned co-evolution governance`；`Layering / Dependency` 于 Ch73
  derived memory 与 Ch80 runtime evidence。主 owner 为 Ch29；已读 Ch28～30、Ch72～74、Ch77～80。
  Ch29 已讲 trajectory credit 与 policy update，Ch73 已讲 derived memory provenance，但尚未把“经验
  生成器本身也是持续更新的 policy”及两种 rollout condition 的 advantage separation 连成一个系统契约。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New
  Mechanism (Books Gate Pending)`；Gate 后 refine Ch29，Ch73/80 只增加 state ownership 与 runtime
  handoff。本 checkpoint 不改 `books/`。待核验公开训练配置、hardware/precision、长期库扩展、并发
  merge、experience-level causal attribution、selective delete 与 rollback。

### BenchPreS — 22/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `BENCHPRES-CONTEXTUAL-PREFERENCE-SUPPRESSION`；arXiv:2603.16557v1，first-public 2026-03-17，
  当前仅 v1。已读论文 HTML 全文、evaluation appendix、prompt template，并核对 Hugging Face 官方
  dataset card、390-row schema 与 license；Source 与 artifact 均为 `Verified`。
- **Original Problem / Previous Design / Changed Constraint**：把显式 user preference 写进 persistent
  memory 并在生成时遵循，适合稳定的格式、称呼和长期习惯；只评 adherence 也能发现“记住但没有用”。
  但 recipient、task purpose 与 formal context 变化后，同一偏好可能必须抑制。新的约束不是检索
  accuracy，而是 stored preference 是否在当前 interaction 中具有 execution authority。
- **Mechanism / State Ownership / Control and Data Flow**：benchmark 从 CIMemories 构造 10 个 profile，
  每个约 152 attributes 和 5 preferences，把 profile 与 39 个 recipient/task contexts 组合。Persistent
  memory 以历史 OpenAI template 文本前置；模型必须同时完成任务，并对每项偏好执行 apply 或 suppress。
  三位 annotators 只保留 unanimous labels，模糊文化/社会情境被排除。长期系统含义是 memory read
  之后还需要独立的 applicability policy：memory store 拥有偏好事实，authorization/policy layer 拥有
  “何时可执行”，generator 只能消费带 purpose、recipient 与 policy decision 的结果。
- **Implementation Details / Evaluation Contract**：390 个 user-context rows 展开为 1950 个
  attribute-level instances；偏好含 role、style、tone、markers、nickname。作者通过 OpenRouter 测试
  10 个模型，K-EXAONE 使用 FriendliAI，temperature 1，每个 user-context 采样 3 次。MR 衡量应抑制时
  的误应用，AAR 衡量应应用时的正确应用；DeepSeek-R1 作 judge，nickname 用 exact match。100 个样本
  的 judge audit 报告 92% 与人工一致，但无置信区间，API 模型 revision 也没有冻结为可复现实物。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：跨模型结果展示 application 与
  suppression 的非单调 trade-off；显式 prompt mitigation 通常降低 MR，但可能牺牲 AAR，效果随模型而
  变。Reasoning 条件可同时抬高 AAR 与 MR，除非加入明确 constraint。作者还单独测 task completeness，
  证明“任务完成”与“偏好执行正确”不能合并成单一分数。证据支持在这一受控 formal communication
  benchmark 中，偏好记忆必须同时测 over-application 与 under-application。
- **What It Does Not Prove / Limitations / Threats to Validity**：benchmark 只测试 final generation，
  没有外部 retrieval、tool action 或真实 memory write path；情境刻意清晰且偏正式，排除了最难的文化
  模糊性。Profile、recipient 和 sample 较少，依赖 LLM judge，未报告重复运行置信区间或生产用户行为，
  因而不能把 MR/AAR 数字外推为部署阈值。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：contextual policy 可减少尴尬或越权
  个性化，却引入 purpose classification、recipient identity、policy precedence、false suppression 和
  decision logging 成本。全局稳定偏好、用户明确要求和低风险私人环境中，直接注入仍简单有效；高风险
  tool action 则需要比文本 benchmark 更强的 authorization 与 confirmation。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Direct Evolution` 于
  preference memory：`store and retrieve → apply when relevant → jointly optimize application and
  suppression → policy-governed memory execution`；`Layering / Dependency` 于 Ch62 evaluation。主 owner
  从 Ch62/73 收敛为 Ch73，Ch62 只拥有双侧指标；已读 Ch61～63、Ch68、Ch72～74。Ch73 已覆盖 tenant/
  sensitivity/read authorization，但缺少“检索到不等于当前 recipient/purpose 下可执行”这一 preference
  applicability gate。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New
  Mechanism (Books Gate Pending)`；Gate 后 refine Ch73，并在 Ch62 做 MR/AAR-style dual-risk handoff。
  本 checkpoint 不改 `books/`。待验证 informal/multilingual context、tool-action preferences、policy
  conflict、API revision drift 与不用 LLM judge 的可执行 verifier。

### AdaMem — 23/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `ADAMEM-PARTICIPANT-TYPED-ADAPTIVE-ROUTING`；arXiv:2603.16496v1，first-public 2026-03-17；
  v2 修订于 2026-04-29，W12 以 v1 为事件。已读 v1 HTML 全文、算法、ablation、sensitivity、案例与
  appendices；论文称 code 将在 acceptance 后发布，appendix 又提及 repository/evaluation script，当前
  未独立找到可验证的官方代码，artifact 状态为 `Unavailable / Claim Inconsistent`。
- **Original Problem / Previous Design / Changed Constraint**：flat semantic retrieval 实现简单，单跳事实、
  小记忆库和低 latency 场景仍最可靠；但多参与者长期对话混合 persona、event、temporal relation 与
  cross-session reference 后，单一 top-k 难以同时保证身份隔离和关系推理。变化的约束是 query 的
  information need 不同，不应每次都支付 graph propagation 或全类型 union 的成本。
- **Mechanism / State Ownership / Control and Data Flow**：每个 participant 拥有独立 working FIFO、
  episodic、persona 与 heterogeneous graph memory。新 utterance 被规范化为 summary/topic/attitude/
  reason/facts/attributes/timestamp/speaker；FIFO 容量 20，每次 pop 最老 5 条 consolidation。Router 对
  event/fact/attribute 执行 ADD/UPDATE/IGNORE，保留原消息 provenance；稀疏图只把每个 key 连到最相似
  peer，再按 connected components 聚合 topic/aspect 与 persona。Query 先做 user/assistant/both/ambiguous
  target resolution，ambiguous 同时检索两边；确定性 cue planner 默认选择 route，仅低于 0.75 confidence
  才由 LLM 在限定范围内修正。Graph propagation 使用固定 prior 与 0.85 hop decay，属于 retrieval
  scaffold，不是 learned graph reasoner。
- **Implementation Details / Evaluation Contract**：LoCoMo 平均 35 sessions、约 9000 tokens，并测试
  PERSONAMEM；backbones 为 GPT-4.1-mini、GPT-4o-mini、Qwen3-4B/30B，temperature 0，top-k 10、最多
  2 次 retrieval iteration、MiniLM embedding，公开硬件为 RTX A800。Research Agent 决定“问什么”，
  route planner 决定“如何取”，Working Agent 生成答案。论文效率表把 2248 tokens、4.722 s、44.65 F1
  放在同一配置中，但 remote API/local hardware 路径边界不清，不能转写成一般 latency 结论。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：component ablation 中移除 graph 的
  降幅最大，fusion 与 multi-agent 也有贡献；K=5/10/15、retrieval iterations=1/2/3 的 sensitivity 显示
  K=10、两轮最好，继续检索会引入噪声。案例展示系统仍无法把 deictic book 与 relative time 解析为
  absolute year，说明 retrieval 不能补救 write-time 未创建的 canonical link。证据支持在作者两个
  benchmark 与选定 backbone 下，participant-typed state 加 question-conditioned routing 优于其 baselines。
- **What It Does Not Prove / Limitations / Threats to Validity**：无公开 code、seeds/CIs、并发写入、
  versioned consistency、selective deletion、crash recovery 或生产 SLO；LLM normalization、target/entity/
  time parsing 一旦错误，后续 graph route 很难恢复。固定 benchmark 与 evaluator 也不能证明任意长期
  对话中的 graph memory 都优于 semantic retrieval。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：typed state 减少 participant 混淆，
  adaptive routing 避免每次全量图搜索，却增加 schema migration、router error、duplicate entity、edge
  staleness、summary drift 和 multi-store consistency。单参与者、单跳事实、短会话和强 latency budget
  下，flat episodic/vector memory 仍是合理分支；graph 只应在 temporal/relation query 中按需激活。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Refine` 于 long-term memory
  pipeline：`flat transcript → typed participant stores → write-time canonicalization/consolidation →
  question-conditioned bounded route → graph only for relational pressure`。主 owner 为 Ch73，Ch72 只保留
  retrieval handoff；已读 Ch72～74、Ch77～80。Ch73 已有 memory types、write transitions、retrieval、
  consolidation、derived state 与 provenance，AdaMem 不构成新章节，只补强“先规范化、再按 query
  选择最小必要 topology”的机制边界。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Refine — Existing
  Argument (Books Gate Pending)`；Gate 后只 refine Ch73，不复制论文架构图或 benchmark 数字。本
  checkpoint 不改 `books/`。待核验官方 artifact、write-time schema evolution、event-time repair、
  cross-store transaction、delete propagation 和 graph rebuild contract。

### VTC-Bench — 22/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `VTCBENCH-VISUAL-TOOLCHAIN-EXECUTABLE-EVAL`；arXiv:2603.15030v1，first-public 2026-03-16；v2
  修订于 2026-03-19，仍在 W12。已读 v1 HTML 全文、tool/category/evaluator appendices，并核对官方
  GitHub 与 Hugging Face dataset tree。Primary artifacts 可访问，但工具总数存在未消解冲突：abstract、
  main text 与 repo interface track 写 32，appendix Table 6 标题和 repo introduction 写 35；状态为
  `Verified with Disputed Metadata`，不得选一个数字伪装成一致事实。
- **Original Problem / Previous Design / Changed Constraint**：只评 final visual answer 或单次 tool call
  易复现，任务允许多条等价路径时也避免过度约束过程；但真实 visual task 常需连续 select/execute/
  inspect/replan，最终错误无法区分工具选择、参数、执行反馈与中间验证。变化的约束是评测对象从回答
  质量变成 executable toolchain contract。
- **Mechanism / State Ownership / Control and Data Flow**：benchmark 含 680 tasks、9 categories、538
  multiple-choice 与 142 open-ended tasks；参考链平均 5.04、median 5、最长 10，共 3428 reference tool
  calls。专家构造与复核任务，Gemini/GPT 辅助 label/trajectory draft，再做人类 secondary/reciprocal
  verification。Code paradigm 由模型直接生成调用，interface paradigm 通过 Qwen-Agent 或 Thyme harness
  执行；harness 持有 tool registry、round limit 与 observation，agent 持有 selection/arguments，evaluator
  持有 reference trajectory 和 final-answer contract。
- **Implementation Details / Evaluation Contract**：19 个 MLLMs 覆盖 base/code/interface；开源模型在
  H100/vLLM 上运行，闭源模型走 provider API，zero-shot，Qwen-Agent 最多 20 rounds。指标包括 Answer
  Pass Rate、Tool Call Rate、chain-length MAE，以及 effective/attempted calls 的 efficiency；final evaluator
  结合 deterministic check 与 GPT-4o judge。论文给出 sampling/max-token settings，但没有统一 model
  precision、重复 runs、置信区间、API snapshot 或端到端 latency/SLO。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：结果显示模型会过用熟悉的有限工具、
  选择错误操作、缩短链条并信任未经验证的 tool output；oracle ground-truth tool set 只能部分改善结果。
  这支持“tool availability、tool invocation 与最终任务正确性是不同层级”的诊断价值，也说明给出正确
  registry 不能替代 observation verification 和 replanning。
- **What It Does Not Prove / Limitations / Threats to Validity**：参考 trajectory 是人工认可的一条路径，
  不一定是唯一或最优；chain-length MAE 与 efficiency 可能惩罚正确的替代计划。Tool Call Rate 与 APR
  的相关性不是因果，closed/open、code/interface 对比还混入 model、API 与 harness 差异。Web/Kaggle
  data provenance/license、工具数冲突、无重复统计也限制结论，不能据此排名生产 Agent runtime。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：process metrics 提供故障定位，却可能
  把 reference path 偏好误当正确性；LLM judge 增加语义覆盖，也带来 revision drift 和 judge bias。
  结果可由 deterministic verifier 完整判定、或允许大量有效路径时，应以 outcome/state invariant 为主，
  trajectory 只作诊断证据而不是唯一 oracle。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Principle Reuse` 于 Ch62：
  `final answer score → tool-call trace → executable outcome + process diagnosis → alternate-valid-path
  aware evaluation`；`Layering / Dependency` 于 Ch74 tool failure taxonomy 与 Ch75 evidence-bearing plan。
  主 owner 为 Ch62；已读 Ch61～63、Ch74～75。Ch62 已明确区分 final/process、verifier/judge、trajectory
  lineage 和 alternate valid path；Ch74 已分解 selection、arguments、execution、task success 与 retry。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`No Change — Already
  Covered`；不修改 Books，因为可沉淀的长期机制已由 Ch62/Ch74 具体覆盖，新增部分主要是受限 benchmark
  实例且 metadata 有争议。保留 Weekly 作为证据案例。待作者澄清 32/35 tools、发布 dataset license、
  多路径 verifier、repeat variance 与冻结 API/model revision。

### Efficient Exploration at Scale — 24/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `EFFICIENT-EXPLORATION-INFORMATION-DIRECTED-RLHF`；Google DeepMind arXiv:2603.17378v1，
  first-public 2026-03-18，当前仅 v1。已读 HTML 全文、方法、scaling fit、实验与 appendix；未发现作者
  代码或公开数据。论文明确说明只披露 salient elements、无意提供可复现所需的全部细节，故论文来源为
  `Verified`，artifact 与 reproducibility 为 `Unavailable / Intentionally Incomplete`。
- **Original Problem / Previous Design / Changed Constraint**：离线 RLHF 用固定 preference corpus 训练
  Reward Model，易审计、可批处理，policy 变化慢或 feedback 便宜时仍合理；periodic/online RLHF 用当前
  policy 补充 pairs，可减轻 distribution shift，却仍可能把昂贵 label 用在低信息或重复比较上。约束变化
  是 feedback budget 成为主要瓶颈，系统需要决定“下一对候选中哪一对最能降低 Reward Model 的 epistemic
  uncertainty”，而不只是扩大随机 on-policy sampling。
- **Mechanism / State Ownership / Control and Data Flow**：baseline、actor 与 reward backbone 均为 Gemma
  9B。Reward Model 使用 point head，加 100 个冻结 random-prior heads 与 100 个可训练 differential heads
  形成 epinet/ensemble；`Z=0` 给 point estimate，`Z=1..100` 表示 posterior particles。每个新 prompt 生成
  top-5 candidate responses，selector 计算各 pair 的 Bradley-Terry preference probability 在 ensemble 上的
  variance，并查询最大者。新 label 增量更新 Reward Model，再把 chosen/rejected pair 送入带 anchor
  regularization 与 affirmative nudge 的 policy update。因而 selector、RM version、policy version、pair、
  simulator/human provenance 与 update generation 都是训练 lineage，而不能只保存最终 checkpoint。
- **Implementation Details / Evaluation Contract**：实验使用约 202K internal prompts（200K train、1K
  validation/hyperparameter、1K out-of-sample），batch 64；每个 prompt 最多生成 16 responses，候选生成
  使用 top-5。Human feedback 实际由 Gemini 1.5 Pro reward model 通过 Bradley-Terry probability 模拟，
  不是现场人工标注。作者报告 epinet 参数相对 9B backbone 增量低于 5%；hardware、precision、optimizer
  细节、随机种子、置信区间、wall-clock、并发与在线 SLO 为 `Not Disclosed`。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：作者比较 offline、periodic online、
  random online 与 information-directed exploration；在同一 synthetic preference oracle、单一 Gemma 9B
  family 与内部 prompt contract 下，信息定向选择用少于 20K simulated choices 达到 offline 超过 200K
  choices 的相近 win rate。该结果支持“不确定性可成为 feedback acquisition policy 的系统输入”。论文
  所写约 1000× label efficiency 来自 1M-label 区域的 fitted scaling-curve extrapolation，不是实际执行的
  百万标签对照，必须与实测的 `>10×` 区分。
- **What It Does Not Prove / Limitations / Threats to Validity**：同一 simulator family 同时生成偏好与参与
  评估，无法证明真实人类 label efficiency、跨文化 disagreement 或 judge-independent quality。单模型、
  internal prompts、无 artifact、无统计不确定性，也不能外推到 multi-turn Agent、delayed reward、动态
  preference、safe exploration 或生产反馈闭环。Ensemble variance 是 epistemic proxy，不保证 calibration。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：active selection 减少 label 数，却会
  引入 selection bias、uncertainty miscalibration、ensemble correlation、simulator feedback loop、policy/RM
  staleness 与 informative-but-unsafe response exposure。稳定 policy、高风险任务、强合规采样或无法安全
  在线更新时，离线/周期性 curated feedback 仍具有更清晰的审计与 rollback 边界。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Direct Evolution` 于 preference
  acquisition：`static offline pairs → periodic on-policy refresh → incremental online RM/policy → epistemic-
  uncertainty-guided pair selection`；`Layering / Dependency` 于 Ch28/29 的 policy update。主 owner 从 Ch29
  更正为 Ch27；已读 Ch26～29。Ch27 已说明 candidate-distribution drift、rubric 与 RM uncertainty，却尚未把
  feedback acquisition 本身写成受 budget、安全与 calibration 约束的 adaptive control problem。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New Mechanism
  (Books Gate Pending)`；Gate 后只 refine Ch27，Ch28/29 以短 handoff 接 policy update。本 checkpoint 不改
  `books/`。待真实 human feedback、independent evaluator、公开 artifact、calibration、safe-query policy、
  rollback 与 label-efficiency scaling 的可复现验证。

### Efficient Training-Free Multi-Token Prediction via Embedding-Space Probing — 24/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `TRAINING-FREE-MTP-EMBEDDING-PROBE`；Qualcomm arXiv:2603.17942v1，first-public 2026-03-18，当前仅
  v1。已读 HTML 全文、theorem、算法、dynamic/fixed-tree 实现、全部 evaluation 与 appendix；未发现官方
  code/artifact，故 source 为 `Verified`、artifact 为 `Unavailable`。
- **Original Problem / Previous Design / Changed Constraint**：独立 small drafter、EAGLE-style hidden-state
  drafter与 trained MTP heads 在足够 workload 下能提供高质量 draft，但要增加训练、权重、部署与版本
  对齐；prompt lookup/naive lookahead 无训练却依赖 repetition 或固定局部模式。变化的约束是希望在不训练
  辅助模型的前提下，利用 target model 自己的 latent representation 一次提出多个 future-token branches，
  并把 proposal cost 纳入与 verify cost 相同的 block budget。
- **Mechanism / State Ownership / Control and Data Flow**：方法在 frozen target model 输入中动态插入 mask
  embeddings；mask hidden states 预测未来 token，并按 cumulative probability 构造 speculative tree。
  作者发现 prompt embedding mean 是较稳定的 mask，Top-1 path expansion 配合重复 parent/child pruning
  控制树宽。`Block Complexity=(k+1)(1+sum K_i)` 同时计入 draft nodes 与 mask positions；prefill 阶段扩展
  top-1，decode 阶段由 target model parallel verification 并生成下一轮候选。Fixed-tree 版本复用 attention
  mask，仅追加 zero columns 并按 accepted-token offset 移动 position IDs，避免逐轮重建 tree metadata。
- **Implementation Details / Evaluation Contract**：在单张 NVIDIA A100 上测试 LLaMA-3.2-3B-Instruct、
  LLaMA-3.1-8B-Instruct、Qwen3-8B/32B；SpecBench，最大生成 100 tokens，temperature 0 与 1，Block
  Complexity 10/30/60。Baselines 为 PLD、STAND 与 LADE，并按 block complexity 对齐。指标为每次 target
  model call 的平均 accepted tokens 与 tokens/s；未披露 seeds、置信区间、并发、batch、服务 SLO、能耗、
  multi-GPU/TP contract，也没有公开实现。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：作者设置中，embedding probe 相对
  LADE 在 LLaMA 上提高约 12% acceptance、在 Qwen 上约 8～12%，若干配置 tokens/s 提高约 15～19%，
  并减少最多约 40% forward calls。收益随 task 与 tree shape 改变：STAND 在部分 retrieval/summarization
  任务更好；BC=30 时单 mask 较稳，BC=60 的某些 closed tasks 才受益于双 mask。论文 theorem 只证明在
  hidden-state cosine similarity 超过给定阈值时，真实 token 会落入 mask Top-K，是条件性 inclusion bound，
  不是所有输入的命中保证。
- **What It Does Not Prove / Limitations / Threats to Validity**：单卡、batch-1 风格实验不能证明生产并发
  吞吐或 edge 部署。动态树并非始终优于固定树，速度也部分来自避免顺序构造 attention mask/position IDs。
  论文以 exact-match/sample matching 描述验证；在 temperature=1 下若没有完整的 distribution-preserving
  rejection/resampling contract，不能仅凭该表述断言与 target sampling distribution 完全等价。无 artifact、
  重复统计和跨拓扑实验进一步限制外推。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：省去 drafter 训练与权重后，proposal
  仍消耗 target-model block capacity，并新增 mask identity、tree-shape tuning、position/mask correctness、
  accepted-prefix rollback 与 stochastic verification semantics。强 repetition workload 仍可优先 prompt
  lookup；可承担训练且追求更高 acceptance 时，独立/hidden-state drafter 或 trained MTP heads 仍成立。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Layering / Dependency` 于 Ch44：
  `independent drafter → hidden-state/MTP drafter → training-free target-model latent probe`，是 proposal source
  的并列分支，不是单向替代；`Principle Reuse` 于 block-efficiency 与 parallel verification。主 owner 从
  Ch43/44 收敛为 Ch44；已读 Ch43～45。Ch44 已有 drafter/verification/acceptance/effective-cost 框架，但
  还未明确“用 target 自身的 masked latent future 作为 training-free proposal”及其 block-complexity边界。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Refine — Existing Argument
  (Books Gate Pending)`；Gate 后在 Ch44 增加 proposal-source 分支和 stochastic semantics 边界，Ch43 只做
  KV/mask handoff。本 checkpoint 不改 `books/`。待公开实现、精确 sampling proof、tree-build cost、TP/
  concurrency、energy 与长输出 workload 验证。

### RAMP mixed-precision quantization — 23/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `RAMP-RL-MIXED-PRECISION-GGUF`；arXiv:2603.17891v1，first-public 2026-03-18，当前仅 v1。已读 HTML
  全文、SAC formulation、Scale Folding、HALO mapping、实验与 appendices；未发现作者 code/data artifact。
  论文不同位置对可选 bit set 写法及“greedy decoding (temperature 1.0)”存在内部不一致，状态为
  `Verified Paper / Artifact Unavailable / Contract Inconsistency`。
- **Original Problem / Previous Design / Changed Constraint**：uniform quantization 与人工规则容易部署、
  也便于复现；AWQ/GPTQ 类 calibration 能在固定模型上寻找较好权重表示。但 layer sensitivity 不均且
  部署 runtime 只接受有限 artifact/kernel formats 时，连续搜索的 allocation 还必须映射到已有执行后端。
  新约束是同时满足质量、平均 bit budget 与 llama.cpp/GGUF 可执行性，而不是只最小化离线 reconstruction
  error。
- **Mechanism / State Ownership / Control and Data Flow**：RAMP 把逐层 bit assignment 建模为 sequential
  decision。11 维 state 包含 activation/weight statistics、layer structure 与 previous-bit/running-average
  context；SAC 的 squashed Gaussian action 映射到离散 bit，twin critics 与 replay buffer 学习 terminal
  reward。Reward 对 perplexity 采用非对称 quality penalty，并在平均 bit 超预算时施加 cliff。Scale Folding
  以 activation-derived per-channel scale 重参数化 Q/K/V、FFN 与 RMSNorm compensation，声称量化前保持
  forward 等价。HALO 再把 policy 映射到 GGUF Q3/Q4/Q5/Q6 formats，由 llama.cpp 选择既有 kernels 并
  解量化为 FP16 activations；“kernel-free”仅表示不新增 custom kernel。
- **Implementation Details / Evaluation Contract**：policy 在 Llama-2-7B 上以 WikiText-2 的 128 sequences
  （约 20K tokens）calibrate，转移到 Llama-2-13B、Llama-3-8B、Mistral-7B；context 2048、batch 1，
  论文称 FP32，3 runs，硬件列 RTX PRO 5000 Blackwell 与 A100。下游为 PIQA、HellaSwag、WinoGrande、
  ARC。SAC 约 200～250 episodes、replay 30K、warmup 20；未披露完整 optimizer、seed、端到端 converter
  artifact、并发或 SLO。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：作者表中 Llama-2-7B 报告 PPL 5.54、
  3.68GB，相对若干 AWQ/GPTQ/AutoMixQ baselines 保持竞争力；Scale Folding ablation 从 5.58 改善至
  5.54，并把收敛 episodes 从 250+ 降到约 150。跨模型 transfer 与 direct search 差值很小（例如 4.95
  对 4.96），只支持在这些 decoder-only families 和 calibration contract 下存在可迁移信号。论文的
  portability latency table 明确取自公开 llama.cpp benchmarks，不是 HALO artifact 的直接 measurement，
  不得转写成 RAMP deployment speedup。
- **What It Does Not Prove / Limitations / Threats to Validity**：无代码、converter、GGUF artifacts 或 direct
  runtime benchmark；bit set、decoding 描述和硬件路径不完全一致。只覆盖静态 layer-level assignment、
  decoder-only Llama/Mistral，未测试 MoE、encoder-decoder、动态 input/head/channel policy。边际 transfer
  差异、单一 calibration corpus 与小规模重复不能证明 sensitivity 主要由 architecture 决定。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：RL allocation 可表达非局部 layer
  dependency，却增加 search reward cliffs、calibration overfit、policy transfer drift、format mapping loss 与
  artifact/kernel mismatch。Uniform/fixed mixed precision 在审计、可移植和低搜索预算场景仍合理；已有
  backend 不支持所选 format 时，离线 quality gain 不产生运行时收益。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Principle Reuse` 于 Ch45：
  `uniform bits → calibration-based per-layer allocation → learned constrained allocation → executable artifact/
  kernel validation`。主 owner 从 Ch42/45 收敛为 Ch45；已读 Ch44～46。Ch45 已明确“量化不自动加速”、
  artifact、kernel、semantic portability 与 workload contract，RAMP 当前只提供一个尚不可复核的搜索案例，
  没有改变该章设计结论。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Emerging / Experimental`；
  不修改 Books。原因不是分数不足，而是公开证据尚未把 learned allocation、实际 GGUF artifact 与端到端
  runtime 连接起来，且 contract 有内部不一致。待作者发布代码、转换产物、直接 llama.cpp benchmark、
  统一 bit/decoding contract、更多模型拓扑及可重复统计后再评估。

### PRISM mid-training study — 23/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `PRISM-MIDTRAIN-STAGE-COUPLING`；arXiv:2603.17074v1，first-public 2026-03-17；v2 于 2026-03-21，
  仍在 W12；v3 于 2026-03-24，超出 W12，只用于核验 current revision，不倒写为事件事实。已读当前论文
  全文、method、weight analysis、evaluation、limitations 与 appendices，并核对官方 project、Hugging Face
  organization 和 AllenAI open-instruct 基础代码。项目的 data mixtures/models 仍标 `Coming Soon`，`Code`
  未提供 PRISM-specific artifact，故 `Verified Paper / Artifact Pending`。
- **Original Problem / Previous Design / Changed Constraint**：pretraining 后直接 SFT/RL 的 stage boundary
  清晰，适合目标分布接近 base model 且无需大规模领域迁移时；扩大 post-training compute 也能强化已有
  policy modes。但当 math/code/science distribution 与 base gap 较大，短 RL 可能无法抵达所需表示区域；
  mid-training 又可能破坏 long-context 与 general capabilities。约束变化是 stage objective、data mixture、
  context length、token budget 与后续 RL reachability 必须联合设计。
- **Mechanism / State Ownership / Control and Data Flow**：研究跨 7 个模型、4 个 families、dense 与
  attention-Mamba、3B～24B，使用约 27B-token targeted mid-training mixtures，把 educational web、domain
  reasoning、code/math/science 与 chat 组合。25K steps、bf16、FSDP2；主要比较 8K/16K/32K context 与
  token budget。8K mid-training 会显著破坏继承的 128K ability，作者用 15% base + 85% midtrained weight
  merge 后再做 128K extension，分别比较 attention-only 与 full-model training。随后以 open-instruct/GRPO
  在 verifier-backed tasks 上更新 policy。工程上 data-mixture version、midtrain checkpoint、merge ratio、
  context-extension state、RL dataset/filter 与 best-step selection 必须共同进入 lineage。
- **Implementation Details / Evaluation Contract**：mid-training LR `5e-5`、FSDP2 data-parallel sharding 8/
  replication 16；RL 每 prompt 16 responses、batch 1024/64 prompts、1000 steps、context 16384、LR `5e-7`、
  KL beta 0.05、DeepSpeed ZeRO-3。Math 每 prompt 64 samples、temperature 0.6、top-p 0.95、max 32K；code
  每题 3 samples、temperature 0.7。Difficulty filtering 统一用 Granite-3.3 midtrained model，可能对不同
  families 引入同一 evaluator bias。公开模型/data/artifact、完整 seeds/CIs 与端到端 compute 尚不可复核。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：在作者设置中，mid-training mixture 对
  最终能力的影响通常大于 RL mixture，约 15～27B tokens 后部分 3B model 指标趋于饱和，code 在更长训练
  中可下降；16K 在其 mixture 上优于 8K/32K 的平衡。RULER 128K 案例从 base 59.09 降至 midtrain 6.46，
  merge 11.32，merge+long-context full training 42.16，说明是部分恢复而非无损保留。作者以 relative-change
  threshold 得出 mid-training 改变多数 weights、RL 改变较少，并报告若干层 CKA >0.998；这些是阶段
  footprint/association 证据，不是“mid-training 改 representation、RL 不改”的因果证明。
- **What It Does Not Prove / Limitations / Threats to Validity**：规模止于 24B，领域集中在 math/code/science，
  主要 mid-training context 为 8K/16K；未覆盖 multilingual、Agent/tool use 或生产 deployment。统一 filter、
  best-step checkpoint selection、benchmark/data overlap 与尚未公开 artifact 限制复现。General average 也
  掩盖 HellaSwag、TruthfulQA 等单项 regression，不能写成“保留通用能力”。Interpolation landscape 与
  weight/CKA analysis 不能建立阶段作用的唯一 causal mechanism。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：targeted mid-training 扩大 post-training
  的可达能力区间，却新增 catastrophic forgetting、context regression、mixture overfit、merge interference、
  filter bias、stage-selection leakage 与多 checkpoint lineage。目标域与 base 接近、预算较小或 retention
  要求严格时，直接 SFT/RL 仍更简单；需要领域分布迁移时，mid-training 应被视为独立 stage，而非更多
  pretraining tokens 或更长 RL 的同义词。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Direct Evolution` 于 Ch24：
  `general pretraining → targeted mid-training → retention repair/context extension → SFT/RL specialization`；
  `Layering / Dependency` 于 Ch23 mixture-as-objective、Ch22 long-context retention、Ch29 RL reachability。
  主 owner 从 Ch21/29 更正为 Ch24；已读 Ch22～25、Ch28～29。Ch23 已说明 mixture 是 optimization policy，
  Ch24 尚缺 mid-training 作为 stage-coupling 与 retention-budget 问题的完整机制。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New Mechanism
  (Books Gate Pending)`；Gate 后 refine Ch24，Ch22/23/29 只做短 handoff。本 checkpoint 不改 `books/`。
  待公开 data/model/code、污染审计、跨规模/领域 replication、stage-level compute accounting、merge 与
  long-context restoration 的稳定性，以及不依赖同一 difficulty filter 的验证。

### AI Scientist via Synthetic Task Scaling — 23/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `AI-SCIENTIST-SYNTHETIC-EXECUTABLE-TASKS`；arXiv:2603.17216v1，first-public 2026-03-17，当前仅
  v1。已读 28-page PDF 全文、pipeline、实验、limitations 与 task/prompt/evaluator appendix；论文未链接
  作者代码、生成环境或 trajectory dataset，训练 hyperparameters 在正文声称位于 appendix、公开 appendix
  实际未给出，故 `Verified Paper / Artifact Unavailable / Training Contract Incomplete`。
- **Original Problem / Previous Design / Changed Constraint**：对论文、最终代码或静态 demonstration 做
  SFT 容易构造，适合短行为和稳定答案；但 research Agent 的能力取决于多轮读写文件、运行实验、观察失败
  并修正。新的约束是训练数据必须包含可执行 environment、intermediate actions、observations 与 outcome，
  同时需要自动检验合成任务不是不存在的数据集、损坏的 starter code 或无效 evaluator。
- **Mechanism / State Ownership / Control and Data Flow**：pipeline 先采样 1000 个 ML topics，由 GPT-5
  提议 task/dataset，调用 Hugging Face API 验证数据集并取样；再生成 MLGym-compatible config、starter
  code 与 evaluator。Dry run 在 MLGym/SWE-agent environment 执行，错误以概率 `p_debug` 回送生成器，
  或从 code stage 重启，超过 `k` 次则丢弃。通过验证的任务在 GPU cluster 上每项尝试 256 teacher
  trajectories；只保留至少一次 successful submission 且不超过 48K tokens 的轨迹，SFT 时截断至 32K。
  Task spec、dataset snapshot、container、starter/evaluator digest、teacher/harness version、trajectory 与
  filter reason 都应属于 dataset lineage。
- **Implementation Details / Evaluation Contract**：论文叙述约 500 validated tasks、约 30K～34K
  trajectories；详细统计图又给 271 tasks、56,210 raw 与 23,204 filtered trajectories，属于不同 pipeline
  checkpoint，不能混为单一精确总数。Teacher 为 GPT-5，students 为 Qwen3-4B/8B，评价于 13-task
  MLGym，SWE-agent 最多 50 rounds；每个 benchmark task 聚合 64 runs。论文报告 AUP 相对 base 提高
  9%/12%，但 hardware、SFT optimizer、batch、LR、epochs、seeds/CIs 与 cluster cost 为 `Not Disclosed`。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：作者比较 base Qwen3、SFT students、
  GPT-4o 与 GPT-5；Qwen3-4B 在 9/13 MLGym tasks 改善。证据只支持“在相同 MLGym/SWE-agent scaffold
  下，经过成功过滤的 synthetic executable trajectories 可提升所测 students 的 AUP”。论文未对 dataset
  grounding、self-debug、success-only filter、truncation 或 teacher quality 做组件 ablation，不能归因某个
  环节，也不能把 AUP 解释成 scientific novelty。
- **What It Does Not Prove / Limitations / Threats to Validity**：训练和评估共享 turn/action schema、starter
  structure 与 submission conventions，作者也明确无法分离 harness familiarity 和通用 ML research 能力。
  只测 MLGym；GPT-5 无法生成/解决的任务不会进入 training set，success-only filter 会丢失有价值失败并
  放大 selection bias。无公开 artifact、完整训练 contract、跨 harness transfer、研究新颖性或真实部署验证。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：executable environment 比静态答案提供
  更强行为监督，却引入 evaluator exploit、container/filesystem drift、teacher monoculture、任务重复、成功
  过滤偏差、长轨迹截断和昂贵 GPU generation。短任务、可信人工 demonstrations 或无法安全执行的领域，
  静态 SFT 仍更简单；synthetic task 只有在 environment/evaluator 可版本化、可审计时才值得规模化。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Direct Evolution` 于 Ch25：
  `static demonstration → synthetic answer → verified executable task → teacher interaction trajectory →
  student SFT`；`Layering / Dependency` 于 Ch77 evaluator-driven workflow 与 Ch62 outcome evaluation。
  主 owner 从 Ch77 更正为 Ch25；已读 Ch24～26、Ch62、Ch77、Ch80。Ch25 已警告 synthetic verifier 与
  teacher bias，但缺少“合成 environment 本身是带 lineage 的训练数据产品”这一机制。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New Mechanism
  (Books Gate Pending)`；Gate 后 refine Ch25，Ch77/62 只做 environment/evaluator handoff。本 checkpoint
  不改 `books/`。待公开 artifacts、训练 hyperparameters、组件 ablation、跨 harness transfer、失败轨迹
  价值、novel-discovery verifier 与完整 compute accounting。

### Nemotron-Cascade 2 — 27/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `NEMOTRON-CASCADE2-MOPD`；NVIDIA arXiv:2603.19220v1，first-public 2026-03-19；v2 修订于
  2026-03-22，仍在 W12。已读 63-page v2 report 的 SFT、Cascade RL、MOPD、RLHF、long-context/code/
  SWE RL、evaluation 与 hyperparameter appendices，并核对 NVIDIA Hugging Face model、SFT/RL data
  collection 与 model card；source family `Verified`。v2 可核验当前 recipe，但不把修订差异倒写成 v1
  首发事实。
- **Original Problem / Previous Design / Changed Constraint**：joint multi-domain RL 共享 optimizer 与 batch，
  response length、verifier latency 和 reward scale 接近时吞吐高；domain-by-domain RL 则可单独调 curriculum，
  并减少 heterogeneous straggler。随着 domain 数增加，顺序训练仍会产生 capability drift，且不同阶段会以
  不同方向损伤 entropy、math reasoning、instruction following 或 preference alignment。
- **Mechanism / State Ownership / Control and Data Flow**：Cascade 2 按 IF-RL → grouped multi-domain RL →
  Multi-domain On-Policy Distillation (MOPD) → RLHF → long-context RL → code RL → SWE RL 顺序执行；作者
  明确 stage order 不是常数，而取决于当前 checkpoint 的 behavior trajectory。只有 response length 与
  verification time 相近、且未观察到明显 interference 的 domains 才合并。MOPD 为每个 domain 选择最强
  intermediate teacher；student 自己 on-policy 采样 response，teacher 在相同 prefixes 上给 token
  probabilities，以 reverse-KL/dense token signal 统一 specialist states。每个 stage 必须绑定 student/
  rollout/teacher checkpoint、prompt pool、reward/verifier 与 regression suite。
- **Implementation Details / Evaluation Contract**：base 为 30B MoE、3B active。SFT global batch 64、
  packed sequence 256K、33K steps；IF-RL/multi-domain RL batch 128、16 rollouts、max 49K，分别 180/70
  steps；MOPD batch 128、4 rollouts、max 98K、52 steps；LR 均约 `3e-6`。后续 RLHF、long-context/code
  RL 与 SWE RL 使用不同 max lengths、rollout counts 与 tool/environment contracts。报告公开多 benchmark
  设置，但训练 hardware/count、wall-clock、seeds/CIs 和完整 contamination audit 不统一披露。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：训练 trace 显示普通 Cascade RL 仍有
  category fluctuation；MOPD 在作者 checkpoint 上恢复多个 regression。作者对同一 initial checkpoint 报告
  AIME25 中 GRPO 25 steps 到 91.0、MOPD 30 steps 到 92.0；ArenaHard matched checkpoints 中 MOPD 52
  steps 达 85.5/71.0，而 RLHF 160 steps 为 80.7/71.2。它支持“on-policy dense distillation 可作为顺序
  multi-domain RL 的稳定阶段”，不证明任意 domain/order 都优于 joint RL，也不证明 step 数等于 compute。
- **What It Does Not Prove / Limitations / Threats to Validity**：teacher 从同一训练 lineage 的最强 intermediate
  checkpoints 中选择，存在 benchmark-driven selection 与 evaluator overfit；表格混合 avg@k、TIR、不同
  harness/judge，不能只按 headline 排名。模型 card 仍显示 knowledge、long-context、agentic 与 multilingual
  项存在明显弱项。无独立 replication、统一 compute-matched ablation 或 stage-order search，不能把作者
  顺序写成通用 recipe。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：domain stages降低 verifier/length
  heterogeneity，却新增 order sensitivity、teacher registry、cross-stage regression、checkpoint explosion、
  dense teacher-forward cost 与 stale-teacher risk。任务同质且无 interference 时 joint RL 更简单高效；单一
  domain 或没有可信 teacher 时，普通 RL 仍成立。MOPD 是 periodic rebalancing branch，不是对所有 stages
  的替代。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Direct Evolution` 于 Ch29：
  `single-domain GRPO → joint multi-domain RL → sequential domain-wise RL → on-policy distillation
  stabilization → later specialized stages`；`Layering / Dependency` 于 Ch25 SFT、Ch31 checkpoint lineage。
  主 owner 从 Ch29/37 收敛为 Ch29；已读 Ch25、Ch28～31、Ch37。Ch29 已有 multi-stage R1 路线，但尚缺
  “按 response/verifier contract 分组、以 intermediate teachers 修复 sequential drift”的机制。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New Mechanism
  (Books Gate Pending)`；Gate 后 refine Ch29，Ch25/31 仅作数据与 checkpoint handoff。本 checkpoint 不改
  `books/`。待 compute-matched order ablation、teacher-selection leakage、hardware/wall-clock、跨 model
  replication、regression-suite governance 与 stage rollback。

### Memento-Skills — 26/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `MEMENTO-SKILLS-EXTERNAL-POLICY-STATE`；arXiv:2603.18743v1，first-public 2026-03-19，当前仅 v1。
  已读 23-page PDF 全文、algorithm、router objective、evaluation 与 theory sections，并核对官方 GitHub、
  skill market 和当前 code/docs；论文与 repository `Verified`。当前仓库持续演化，W12 机制事实锁定 paper
  v1，后续产品结构仅作为 current artifact verification。
- **Original Problem / Previous Design / Changed Constraint**：静态 tool/skill registry 由人维护，authority
  清楚、易测试，稳定工作流仍最可靠；raw trajectory retrieval 能复用经验，却未必形成可执行 procedure。
  当部署任务不断出现、base LLM 保持冻结时，系统需要把失败转化为可检索、可执行、可更新的 skill，而
  不是无限追加对话或每次重新设计 Agent。
- **Mechanism / State Ownership / Control and Data Flow**：Skill 是 structured markdown folder，包含 behavior
  与 context。Read 阶段由 router 选择 skill，miss 时可创建；Execute 运行 multi-step workflow；Judge 产生
  outcome；Write 更新 success/failure utility、generic tips，并用 trace 将失败归因到 target skill。达到
  minimum samples 且 utility 低于阈值时发现新 skill，否则原地优化；UnitTestGate 失败则 rollback，最多
  `K` 轮反馈重试。Router 用 LLM 合成 positive/hard-negative query，multi-positive InfoNCE 训练 Qwen3-
  Embedding-0.6B，并把 score解释为 one-step offline Q/Boltzmann routing policy。Skill version、router、
  judge、trace、test、utility counters 与 supersession 都是外部 policy state。
- **Implementation Details / Evaluation Contract**：router 以 140 synthetic routing queries 测 Recall@K，并
  用 real trajectories 测 route hit/judge success；论文报告 Memento-Qwen Recall@1 0.60，相对 Qwen3
  embedding 0.54、BM25 0.32。系统从 5 atomic skills 演化到 GAIA 41、HLE 235。GAIA/HLE 各进行多轮
  reflective learning；公开论文未统一披露每项 API/model revision、重复 runs、置信区间、全部 token/cost、
  judge calibration 或生产并发/安全 contract。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：GAIA full system test 66.0%，禁用
  failure attribution/rewriting/creation 的 Read-Write baseline 52.3%；HLE 为 38.7% 对 17.9%。训练轮次内
  指标和 skill count 上升，且 HLE 的 domain taxonomy 比 GAIA 更利于跨题 transfer。证据支持在两个作者
  benchmark 和其 judge/router 下，结构化 skill optimisation 超过只读写但不优化的 static library；不证明
  library growth 本身导致能力，也不证明理论收敛在真实非平稳环境成立。
- **What It Does Not Prove / Limitations / Threats to Validity**：synthetic router queries、LLM judge 与 benchmark
  retry 可能共享偏差；GAIA transfer 有限，HLE taxonomy 对复用有利。论文缺少污染、长期 regression、
  conflict/deprecation、malicious skill、multi-tenant concurrency 与 million-skill scale 评估；“frozen LLM、
  zero retraining”不代表零学习成本，router training、execution、reflection 和 tests 仍消耗资源。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：external skill 易回滚且无需改模型参数，
  但会带来 router miss、错误 failure attribution、skill fragmentation/duplication、utility gaming、judge
  feedback loop、code supply-chain 与 schema migration。高风险/稳定流程仍应由人工发布 immutable skills；
  自动 rewrite 只适合 sandbox、tests、review 与 bounded authority 完整的层级。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Direct Evolution` 于 Ch80：
  `human-authored static skill → retrievable skill registry → outcome-attributed rewrite/create → versioned
  tested skill policy`；`Layering / Dependency` 于 Ch73 derived procedural memory、Ch76 reflection 与 Ch77
  workflow authority。主 owner 从 Ch73/78 更正为 Ch80；已读 Ch73、Ch76～80。Ch80 已定义 Skill artifact
  identity 与 feedback loop，但尚未把 utility threshold、failure attribution、test gate 与 rollback 连成
  executable lifecycle。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Refine — Existing Argument
  (Books Gate Pending)`；Gate 后 refine Ch80，Ch73/76/77 只做状态、反思与 authority handoff。本 checkpoint
  不改 `books/`。待 independent judge、cross-version regression、skill conflict/deprecation、tenant isolation、
  malicious update、large-catalog routing 与 selective rollback。

### AndroTMem — 25/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `ANDROTMEM-CAUSAL-STATE-ANCHORS`；arXiv:2603.18429v1，first-public 2026-03-19，当前仅 v1。已读 HTML
  全文、benchmark construction、ASM equations、ablation、failure taxonomy、limitations 与 appendices，并
  核对官方 GitHub code/benchmark/resources；source family `Verified`。
- **Original Problem / Previous Design / Changed Constraint**：raw GUI trajectory 最忠实，短任务下无额外
  extraction error；running summary 便宜，允许丢失细节时有效。但 30～65-step、跨 app 且后续 action 依赖
  早期 price/entity/subgoal 时，raw history 稀释关键状态，summary 又会压平 dependency 与 evidence。
- **Mechanism / State Ownership / Control and Data Flow**：ASM 将 trajectory 转成 sparse anchors
  `m_k=<type, content, evidence, links>`；type 覆盖 subgoal、state change、dependency、exception、global
  context 与 finish，evidence 指向原 screenshot/action，links 表示稀疏 causal dependency。运行时基于当前
  UI/user task retrieve anchors，与 current observation 决策；随后 create/update/invalidate anchors 并补
  links。Anchor 在线由被测 model 从自身 observation/history 生成，不读取 benchmark ground-truth anchors；
  schema enforcement 与 invalid-output retry 降低格式差异。Memory service 拥有 anchor/evidence/version，
  workflow state 仍由真实 app/transaction 拥有。
- **Implementation Details / Evaluation Contract**：AndroTMem-Bench 有 1,069 tasks、34,473 steps、平均
  32.1、最大 65，覆盖约 50 apps 和 70+ cross-app templates；人类通过 ADB 平台逐步标注 screenshot、
  accessibility XML、action、reasoning、summary 与 anchors。12 个 closed/open/multi-agent systems 在统一
  action schema 下比较 raw history、summary 与 ASM；AMS 测 step match，TCR 要求 final anchor 且 causal
  dependencies satisfied，并记录 tokens/step 与 time/step。hardware、API snapshots、重复统计、CIs 与真实
  side-effect safety contract未完整披露。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：作者报告 ASM 相对 raw/summary 的 TCR
  改善范围 5%～30.16%、AMS 4.93%～24.66%，且长 step bins 中退化较慢、token/time 接近 summary 而低于
  raw replay。相同 model、相同 underlying trajectory、相同 prompt framework，主要变化是 history
  representation。证据支持“在该受控 Android benchmark 中，带 evidence 与 causal links 的 sparse state
  anchors 比 raw replay/coarse summary 更能保留依赖关键状态”。
- **What It Does Not Prove / Limitations / Threats to Validity**：任务来自 curated templates、goal 与 app state
  相对稳定；未覆盖跨 session、days-long gaps、动态 UI/content、随机 outcome。Ground-truth anchor sequence
  同时参与 TCR 定义，可能偏好作者 representation；自动生成 anchors 仍可能 state loss、mis-binding、context
  drift、unverified progress 与 interruption failure。不能外推为所有 Agent memory 或生产 Android 成功率。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：causal anchors 降低 context cost并增加
  traceability，却引入 anchor extraction、link authoring、invalidation、schema evolution 与 stale evidence。
  短 trajectory 保留 raw history最可靠；允许有损压缩且依赖弱时 summary 更简单；高风险 exact evidence
  应保存在 immutable artifact store，anchor 只保存受权 reference。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Refine` 于 Ch73：`raw trajectory
  → coarse summary → compact control state + evidence references → sparse causal anchors with invalidation`；
  `Layering / Dependency` 于 Ch77 authoritative workflow state。主 owner 从 Ch73/77 收敛为 Ch73；已读
  Ch72～74、Ch77。Ch73 已有 compact control state/exact evidence archive，ASM 补强 anchor schema、causal
  links 与 online invalidation，不构成新章节。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Refine — Existing Argument
  (Books Gate Pending)`；Gate 后只 refine Ch73，Ch77 保留 truth-authority handoff。本 checkpoint 不改
  `books/`。待跨 session/dynamic UI、anchor-ground-truth bias、write precision、concurrent updates、delete
  propagation、API/model revision 和真实 device side-effect 验证。

### ProRL Agent — 27/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `PRORL-AGENT-ROLLOUT-SERVICE`；NVIDIA arXiv:2603.18815v1，first-public 2026-03-19，当前论文仅
  v1。已读 HTML 全文、算法/系统结构、evaluation、ablation 与 appendix，并核对官方 GitHub 的
  server、gateway、trajectory/evaluator 文档入口。仓库当前已演化并以 Polar 名称继续开发；该后续状态只
  用于核验 lineage，不倒写为 W12 事件。论文与公开 artifact `Verified`。
- **Original Problem / Previous Design / Changed Constraint**：把 Agent rollout 嵌入 trainer 进程，在短
  response、单一 verifier 与同步 batch 下最直接，policy/version boundary 也清楚。真实 Agent RL 却包含
  I/O-heavy sandbox init、GPU-bound multi-turn inference 与毫秒到分钟级 evaluation；三阶段锁在一个 worker
  会让最慢阶段决定吞吐，长尾 rollout 还会让 DAPO 等 informative-group 收集产生 idle 与过量样本。
- **Mechanism / State Ownership / Control and Data Flow**：系统将 `INIT → RUN → EVAL` 映射到三套独立
  queue/worker pool；`AgentHandler` 拥有 task-specific lifecycle、异常回调与结果序列化，sandbox runtime
  拥有 container/process，rollout server 拥有 job/queue/backend assignment，trainer 仍拥有 policy、iteration、
  target batch 与 cancel 决策。HTTP control API 支持 submit/cancel、backend register/clear 与 lifecycle；任务
  级 min-heap routing 将同一 trajectory 固定到一个 backend 以保留 prefix cache。checkpoint 更新时 trainer
  flush/re-register backend；旧 in-flight job 的处理语义必须显式记录。
- **Implementation Details / Evaluation Contract**：HPC 路径使用 rootless Singularity/SIF、独立 loopback
  地址、SIGTERM→SIGKILL 清理与可选断网；高频 tool path 以 direct PTY、in-process IPython 与 UDS 降低
  action latency。DAPO adapter 持续补队列、达到 informative target 后 cancel 剩余 job，并允许未完成 work
  跨 iteration 保留。训练默认 batch 32、mini-batch 8、每题 8 rollouts、KL `1e-4`、LR `1e-6`，在 32×H100
  上训练 Qwen3 4B/8B/14B；system ablation 则为 Qwen3-14B-Instruct-2507、8×H100。软件/SWE、STEM、
  math、code 的 data、tool 与 verifier contracts 不同，不能合并成通用质量数字。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：component ablation 中完整配置 action
  time 0.42s、GPU utilization 78%、0.37 instance/s；移除 load balancing、efficient Bash 或 stale cleanup
  分别降至 0.25、0.29、0.30 instance/s。它支持“按资源阶段解耦、cache-affine backend selection 与
  bounded cancellation 可改善该 Agent-RL workload 的 rollout utilization”，不证明论文所称 near-linear
  node scaling 在任意网络、sandbox 或 verifier 上成立；公开 scaling figure 未给出足以复算的全部节点、
  topology、存储与置信区间。
- **What It Does Not Prove / Limitations / Threats to Validity**：SWE 质量表同时含作者 reproduced 与他作
  reported values，不能直接归因给 infrastructure；报错 rollout 被排除可能改变训练分布。论文未完整披露
  queue capacity/backpressure、跨阶段 exactly-once、trainer crash、backend failure、跨 iteration stale-prefix
  权重语义、multi-tenant isolation 与 cluster-scale fault injection，并把 richer environments 与 robustness
  留作未来工作。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：service boundary 提升 trainer/harness
  可组合性和资源重叠，却新增 job identity、policy/backend version、cancel race、orphan sandbox、queue
  overload、partial trajectory persistence、token/logprob provenance 与网络控制面。短 rollout、单机、小批量
  或需要严格 synchronous on-policy boundary 时，trainer 内嵌 rollout 仍更简单；异步服务只在 lineage、
  cancellation、backpressure 与 recovery contract 完整时成立。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Direct Evolution` 于 Ch29：
  `trainer-local synchronous rollout → dedicated rollout workers → phase-decoupled rollout service →
  trainer-controlled cancellation/version swap`；`Layering / Dependency` 于 Ch56 workload lifecycle、Ch80
  sandbox/evidence plane。主 owner 从 Ch29/Ch57 收敛为 Ch29；已读 Ch27～32、Ch56～57、Ch80。
  Ch29 已有 rollout/update、partial rollout 与 staleness，但缺少 phase ownership、backend affinity、cancel
  race 与 policy-version handoff 的完整服务 contract。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New Mechanism
  (Books Gate Pending)`；Gate 后 refine Ch29，Ch56/80 仅短 handoff。本 checkpoint 不改 `books/`。待
  exactly-once/at-least-once 语义、trainer/server crash matrix、queue backpressure、stale rollout acceptance、
  token/logprob reconstruction、multi-tenant sandbox 与可复现 cluster scaling。

### Reasoning over Mathematical Objects — 24/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `PRINCIPIA-RLLM-PARAGATOR`；Meta/FAIR arXiv:2603.18886v1，first-public 2026-03-19，当前仅 v1。
  已读 70-page PDF 全文的 Principia dataset/benchmark、VerifyBench、RLLM、ParaGator、实验、ablation、
  limitations 与相关 appendices，并核对官方 Principia Collection/Bench datasets；source family `Verified`。
- **Original Problem / Previous Design / Changed Constraint**：numeric/MCQA reward 便宜且明确，规则 verifier
  在 canonical answer 上也最可扩展；但科学推理常要求 equation、set、matrix、interval 或 piecewise function，
  等价表达不唯一，选项还会提供 backward-chaining shortcut。hard-to-verify 与 non-verifiable tasks 又使
  scalar RM、固定 rubric 或 gold-answer verifier 分别面临 distribution gap、缺少 reasoning 与适用域过窄。
- **Mechanism / State Ownership / Control and Data Flow**：Principia 用 subject taxonomy 生成复杂数学对象
  任务，并通过 pairwise equivalence、transitivity witness 与保守 majority procedure 构造答案。RLLM 先从
  target policy 的 on-policy samples 生成 teacher/verifier labels，再以 GRPO 训练可输出 reasoning+score 的
  LM-as-RM；policy 阶段只消费 pointwise/pairwise/listwise score。ParaGator 同时训练 candidate generator 与
  aggregator：首轮以 pass@k 鼓励互补覆盖，aggregation rounds 以 pass@1 优化最终答案，从而减少 fixed
  generator 与 off-policy aggregator 的错配。Policy、RM、teacher/verifier、reference、sample set、judge
  prompt 与 aggregation round 都必须有独立 identity。
- **Implementation Details / Evaluation Contract**：PrincipiaBench 含 2,558 题，Collection 含约 248K
  synthetic prompts，覆盖六类 mathematical objects；VerifyBench 用 168 个规则 verifier 与 o3 disagree
  cases做人类 meta-evaluation。Principia RL 使用多个 Qwen/OctoThinker 4B～8B backbones 与 GRPO；RLLM
  policy experiments使用 64×H200（48 trainer、16 inference）。ParaGator 在 competition math 与 30K
  Principia subset 上比较 initial pass@1/pass@4 及多轮 aggregation。各子研究的 model、数据、judge 与
  compute contract 不同，文中百分比不能跨表直接比较。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：作者比较 math-verify、general verifier
  与 GPT-OSS-120B，比较 prompted/off-policy/on-policy LM-as-RM，并比较 RLHF、RLVR、RLLM 与 offline/
  online aggregation。结果支持三个受限结论：复杂对象格式暴露 MCQA shortcut；强 model verifier 在该
  equivalence slice 比规则 verifier 更可靠；在作者 policy/RM pairing 下，on-policy judge 与 generator-
  aggregator objective alignment 可改善 policy/aggregation。它不证明 model judge 等于 ground truth，
  也不证明所有 open-ended task 都应使用 generative RM。
- **What It Does Not Prove / Limitations / Threats to Validity**：synthetic data、teacher labels、training reward
  与最终 judge 可能共享模型偏差；168 个 disagreement case 不是完整 verifier distribution。多项结果缺少
  统一 seeds/CIs、污染审计与 compute-matched human feedback；equivalence transitivity heuristic 可能拒绝
  合法少数表达。ParaGator 的 diversity 由 pass@k proxy 定义，可能增加错误模式而非真正独立 reasoning。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：on-policy RM 缩小 policy distribution
  gap，却要求持续采样、teacher labeling、RM checkpoint refresh 与 bias audit；k-wise comparison提高相对
  信息但成本随候选数增长并可能产生 intransitive rankings。规则 verifier 在 exact/canonical domain 仍更
  便宜、可复算；人工/专家复核在高风险开放任务仍是最终边界。Parallel aggregation 只有候选错误不完全
  相关且 aggregation budget 可控时才值得使用。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Direct Evolution` 于 Ch27：
  `human/scalar RM → rule-based verifiable reward → prompted generative judge → policy-conditioned on-policy
  thinking RM`；`Layering / Dependency` 于 Ch29 grouped rollout、Ch62 scorer calibration。主 owner 从
  Ch29/Ch62 更正为 Ch27；已读 Ch27～30、Ch62。Ch27 已指出 RM distribution drift 与独立 evaluation，
  但尚缺“RM 自身也按 target-policy distribution on-policy 更新”及其循环偏差；Ch62 已覆盖 judge audit，
  因而 benchmark/equivalence 只需 handoff。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New Mechanism
  (Books Gate Pending)`；Gate 后 refine Ch27，Ch29/62 只增加短 handoff。本 checkpoint 不改 `books/`。
  待 independent human calibration、teacher/policy co-adaptation stability、reward-hacking transfer、pairwise/
  listwise cost curve、expression-equivalence false reject 与 ParaGator correlated-error analysis。

### Hyperagents — 26/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `HYPERAGENTS-EDITABLE-IMPROVEMENT-POLICY`；Meta/Facebook Research arXiv:2603.19461v1，first-public
  2026-03-19，当前仅 v1。已读 60-page PDF 全文、method、four-domain evaluation、baselines、cost、
  improvement@k、transfer 与 self-modification appendices，并核对官方 repository、experiment-log 入口与
  untrusted generated-code warning；source family `Verified`。
- **Original Problem / Previous Design / Changed Constraint**：固定 meta-prompts 或 domain-specific search
  procedure 容易治理，并在 coding task 中合理，因为“改 Agent”本身也是 coding；DGM 还能保留 archive
  避免单链局部最优。但任务转向 paper review、robotics reward design 或 math grading 后，task competence
  与生成改进方案的 competence 不再天然对齐，手写 meta-level mechanism 成为上限。
- **Mechanism / State Ownership / Control and Data Flow**：hyperagent 把 task agent 与 meta agent 放进同一
  editable program；DGM-H 从 archive 按 performance 与 successful-child count 采样 parent，让其修改自身
  code，再在固定 evaluation protocol 上打分并加入 archive。可编辑 state 包含 prompt、parser、memory、
  performance tracker 与改进策略；但 main experiments 的 parent selection、task distribution 与 evaluator
  仍由外层 workflow 固定。真正 authoritative state 是 versioned code diff、parent/child lineage、evaluation
  result 与 budget，不是 Agent 对“我已进步”的叙述。
- **Implementation Details / Evaluation Contract**：初始 hyperagent 是 frozen FM + Bash/file tools，task
  agent 只做一次 FM call，meta agent获得 repo、历史结果与剩余 iterations。实验覆盖 Polyglot coding、paper
  review、robotics reward design、IMO grading；与 fixed meta-agent、无 open-ended archive、原 DGM、
  人工 domain-customized DGM 和 static systems 比较。主跨域 run 100 iterations，transfer grading 200；
  self-modification 主要使用 Claude 4.5 Sonnet，evaluation 依域使用 GPT-4o、Claude 4.5 Sonnet、o4-mini。
  100-iteration paper+robotics run 估算约 88.6M tokens，未给统一 hardware/wall-clock/SLO。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：固定 meta-agent 与移除 archive 的 baselines
  分别隔离 editable improvement procedure 与 stepping-stone population；held-out task结果支持 DGM-H 在
  作者四个 domain/evaluator 下能发现更好的 agent programs。transfer hyperagent 在 math grading 的 0.640
  对 fresh-start 0.610 差异 `p>0.05`，只能视为探索性趋势，不足以证明跨域 compounding。论文展示 persistent
  memory、bias detection、performance tracker 与 compute-aware planning 等生成 diff，证明改进策略确实被
  编辑，不证明系统已实现无界或 self-accelerating improvement。
- **What It Does Not Prove / Limitations / Threats to Validity**：task distribution、parent selection 与 evaluator
  在主实验中固定；best-of-many selection、benchmark reuse 与 model-based grading可能放大 search overfit。
  improvement@k 只取预算内最好后代且把不同 performance regime 当线性增益。实验依赖闭源 FM 与高 token
  budget，缺少独立 replication、长期 regression、adversarial evaluator、deployment side effects 与完整
  safety case；官方仓库明确警告 model-generated code 可能造成破坏。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：editable meta-policy 扩大 search space并
  减少逐域人工 prompt engineering，却新增 self-modification supply chain、archive poisoning、evaluation
  gaming、lineage explosion、unsafe code、cost escalation 与 rollback/authority 问题。稳定任务、清晰
  verifier 或不可逆副作用场景仍应使用 fixed workflow、人工发布 agent definition 与 bounded search；
  “可编辑”不等于有部署权限。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Direct Evolution` 于 Ch77：
  `fixed handcrafted workflow → evaluator-driven artifact search → archived open-ended variants → editable
  proposal/improvement policy under fixed outer loop`；`Layering / Dependency` 于 Ch80 definition/rollout/
  policy、Ch73 derived memory。主 owner 从 Ch78/Ch80 更正为 Ch77；已读 Ch73、Ch76～80。Ch77 已有
  AlphaEvolve 的 evaluator-driven program population，Hyperagents 应 refine“搜索 proposal mechanism 本身”
  这一层，而不是新增一个无约束自我改进叙事。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Refine — Existing Argument
  (Books Gate Pending)`；Gate 后 refine Ch77，Ch80/73 只作 governance/state handoff。本 checkpoint 不改
  `books/`。待独立 evaluator、holdout refresh、lineage pruning、generated-code sandbox、budget/stop policy、
  transfer significance、outer-loop mutation safety 与 selective rollback。

### λ-RLM / Y-Combinator for LLMs — 24/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `LAMBDA-RLM-TYPED-RECURSIVE-RUNTIME`；arXiv:2603.20105v1，first-public 2026-03-20，当前仅 v1。
  已读 HTML 全文的 formalization、theorems、planner、four-task evaluation、ablation、related work 与完整
  algorithm appendices；未发现独立 official code artifact，机制以论文正文核验，`Verified — Paper Only`。
- **Original Problem / Previous Design / Changed Constraint**：direct long-context inference 简单且适合输入能
  放入窗口、global attention 有价值的任务；普通 Recursive LM 把 prompt 存入 REPL，并让模型生成 Python
  做 split/search/recurse，可越过 context window 且适应开放任务。但自由代码循环把 reasoning quality 与
  coding skill、termination、parser、runtime variance 绑定，弱模型和可审计 workflow 尤其受限。
- **Mechanism / State Ownership / Control and Data Flow**：系统把完整 prompt 保存在 external REPL state，
  单次 model call 先从有限 task menu 选择 type；deterministic planner 根据 input length、window、accuracy
  target 与 composition cost 选择 split `k*`、base threshold `tau*`、depth 与 composition operator。预验证
  combinator library 构造 fixed-point recursion：`Split → Map(recursive leaf LM) → Reduce(symbolic op)`；
  LLM 只拥有 leaf content reasoning，runtime 拥有 control flow、termination、cost estimate 与 aggregation。
- **Implementation Details / Evaluation Contract**：九个 open-weight models覆盖 Qwen3、Llama、Mistral 的
  weak/medium/strong tiers，经 vLLM serving；S-NIAH、OOLONG、OOL-Pairs 与 CodeQA 覆盖约 O(1)、O(n)、
  O(n²) 与 variable structure，长度从 8K 到 128K，CodeQA 到 4.2M tokens。比较 direct、普通 RLM 与
  λ-RLM；每配置运行两次，报告 accuracy/F1、wall-clock latency 与 calls。论文未披露完整 GPU model/count、
  concurrency、precision、vLLM config、warmup 与 tail-SLO，因此 headline 不能外推为生产 speedup。
- **Baselines / Ablations / Sensitivity / What the Evidence Proves**：在 Qwen3-8B × OOLONG 131K ablation，
  random chunk、固定 task type、neural composition、free-form code 与无 prefilter 分别检验 planner、dispatch、
  symbolic reduce、typed library 与 filtering。证据支持受限 library 在可预先表达 split/reduce 的四类 workload
  中降低 malformed/non-terminating control与 coding tax；strong coding models 或 CodeQA 的自由导航有 7/36
  cells 由普通 RLM 胜出，直接证明固定 combinator 不是单向替代。
- **What It Does Not Prove / Limitations / Threats to Validity**：理论 accuracy scaling 依赖 independence、
  decomposability、leaf accuracy 与 composition accuracy 等假设；实际任务未证明满足这些假设。task menu、
  template、split 与 reduce 由作者预编排，开放任务的 plan synthesis、dynamic branching、external side effect、
  parallel scheduler 与 failure recovery 未覆盖；两次运行不足以稳定估计 stochastic variance。论文未单列
  limitations section，也没有独立 code/reproduction。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：typed runtime 提供 bounded termination、
  cost predictability 与可审计 composition，却牺牲 adaptive navigation，新增 task-classification error、library
  coverage、wrong decomposition、composition information loss 与 versioned-plan maintenance。Direct inference
  在短输入/holistic reasoning 下更低 overhead；自由 RLM 在强 coding model、未知 task topology 或需要
  backtracking 时仍合理；可先采用 typed core + bounded escape hatch，而非取消所有 neural control。
- **Evolution Relationship / ROADMAP / Chapters Read / Existing Coverage**：`Direct Evolution` 于 Ch77：
  `direct call → prompt-as-environment + model-authored REPL → deterministic typed recursive spine + bounded
  neural leaves`；`Layering / Dependency` 于 Ch22 long-context representation、Ch72 retrieval。主 owner 从
  Ch17/Ch77 收敛为 Ch77；已读 Ch17、Ch22、Ch72、Ch76～78。它不改变 Transformer Layer；Ch77 已有
  deterministic spine，但缺少“control flow 与 neural content 分离”在 recursive long-context 上的具体分支。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Refine — Existing Argument
  (Books Gate Pending)`；Gate 后 refine Ch77，Ch22 只加架构/系统边界 handoff。本 checkpoint 不改
  `books/`。待官方 code、hardware/concurrency、more-than-two-run variance、dynamic task discovery、escape-
  hatch safety、composition error propagation 与理论假设的 empirical audit。

### A Subgoal-driven Framework for Improving Long-Horizon LLM Agents — 24/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `MIRA-SUBGOAL-PLANNING-REWARD`；Google DeepMind arXiv:2603.19685v1，first-public 2026-03-20，
  当前仅 v1。已读 50 页 HTML 正文与 failure taxonomy、subgoal generation、dynamic milestoning、
  MiRA-RL、iterative curriculum、WebArena-Lite experiments、component ablation、judge/error analysis 和
  相关 appendices；未发现与论文绑定的官方可执行仓库，`Verified — Paper Only`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：静态 task
  decomposition、ReAct trace 或 end-to-end policy 在短链和稳定网站上简单，且不需额外 milestone judge；
  但交互步数增加、环境 observation 偏离预期后，论文的失败标注显示主要错误转为 midway stuck、循环
  与目标漂移，terminal binary reward 又不能定位最早失去进展的步骤。约束由“生成一条合理 plan”变为
  “持续证明当前状态正在接近最终目标”。
- **Mechanism / State Ownership / Control Flow / Data Flow**：teacher 先把 goal 与当前 web state 映射成
  可解释 subgoal checklist；在线 agent 每步根据 screenshot/action trace 更新二值 progress vector，未完成
  milestone 触发局部 replanning。离线 MiRA 用 LLM checker 标注 trajectory 的 subgoal progress，训练
  potential critic 与 goal-conditioned value critic，把 potential difference 加到 environment reward，再用
  TD 与 Monte-Carlo 混合的 doubly-robust advantage，通过 log-ratio MSE 更新 actor。Authoritative state
  应是 environment observation、checklist version、progress evidence、task goal 与 policy/critic version；
  AutoRater 的自然语言判断只是派生信号，不拥有业务事实。
- **Implementation Details / Evaluation Contract**：online 部分以 Gemini-2.5-Pro 生成/检查 subgoals；
  训练部分从共同 SFT checkpoint 初始化 Llama-3.1-8B 与 Gemma-3-12B actor/critic，在 165-task
  WebArena-Lite 五个 domain 上与 SFT、AWR、DigiRL、WebRL 比较，并采用 failure-driven phases 迭代
  收集、过滤和再训练。作者报告 pass@k 与 phase-wise success，并对 potential critic、MSE/KL objective、
  doubly-robust estimator 做消融；公开正文未形成可复算的完整 accelerator、precision、并发与部署 SLO
  contract，因此不保留 headline speed/success 数字为通用结论。
- **What the Evidence Proves / What It Does Not Prove**：在作者 WebArena-Lite harness 中，graded
  subgoal completion 与最终成功相关，full MiRA 相对共同初始化 baselines/ablations 更稳定；这支持
  “显式 progress state 可同时服务在线 replanning 与稀疏奖励 credit assignment”。它不证明 LLM judge
  真的验证了业务语义；论文自己记录 wrong termination 会被 AutoRater 放大，也不证明 milestone recipe
  能跨网站、跨模型或跨不可逆副作用 workflow 泛化。
- **Limitations / Threats to Validity / Trade-offs / New Failure Modes / Previous Design Still Applies**：
  checklist 增加可观测性与 dense signal，却新增 teacher bias、milestone granularity、progress false positive、
  judge/model correlated error、reward shaping shortcut、critic miscalibration、每步 judge latency 与 stale plan。
  短任务、低风险、可由 deterministic terminal verifier 判定时，直接 plan/execute 仍更便宜；subgoal 只有在
  completion evidence 可核验、重规划价值大于检查成本时才值得成为一级状态。
- **Evolution Relationship / ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：`Direct
  Evolution` 于 Ch75：`static step list → observation-triggered replanning → explicit verifiable milestones →
  milestone progress reused as training signal`；`Layering / Dependency` 于 Ch29 reward shaping 与 Ch76
  feedback diagnosis。主 owner 从 Ch76/77 更正为 Ch75；已读 Ch29、Ch74～77。Ch75 已覆盖 executable
  plan、completion evidence 与 replanning，但缺少“milestone progress 同时连接 inference state 与 training
  credit”的机制；Ch76 已覆盖 feedback independence，不应重复正文。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New Mechanism
  (Books Gate Pending)`；Gate 后 refine Ch75，Ch29/76 仅加 handoff。本 checkpoint 不改 `books/`。待官方
  artifact、独立复现、checker human calibration、subgoal version/supersession、wrong-termination recovery、
  hardware/cost contract 与不可逆 action 的 rollback/approval semantics。

### LoopRPT — 24/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `LOOPRPT-LATENT-STEP-OBJECTIVE`；arXiv:2603.19714v1，first-public 2026-03-20，当前仅 v1。已读
  25 页 PDF 的 architecture background、entropy token selection、exit policy、latent rollout reward、全部
  objectives、evaluation、ablation、sensitivity、forced-depth analysis、theory 与 training appendix；未发现
  作者公开代码，`Verified — Paper Only / Experimental`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：固定层数 Transformer
  与普通 next-token pretraining 把每个 token 的 compute 固定，系统简单、batch 规则且易于优化；looped
  model 通过参数共享的 recurrent blocks 允许 latent depth 和 adaptive exit，却暴露新错配：output-token
  loss 不告诉每个中间 latent step 何时已经足够，也不奖励更早获得正确表示。
- **Mechanism / State Ownership / Control Flow / Data Flow**：EMA teacher 估计 token entropy 并选 top-ρ
  难 token；student 对同一 token 产生多个 recurrent-step logits 与 survival/exit distribution。训练从
  noisy latent rollouts 采样 exit step，用相对 EMA reference 的 log-probability gain 减去 difficulty-aware
  time penalty 得到 step reward，组内归一化后更新 exit policy；同时以 exit probability 与 positive
  advantage 加权 next-token representation loss，并加入 exit entropy 与 teacher-relative KL。Model
  parameter/EMA/optimizer 拥有训练状态，exit distribution 和 latent activations 是 step-local state；serving
  runtime 只能执行已训练的 halting policy，不能把平均退出层当 SLO 保证。
- **Implementation Details / Evaluation Contract**：OMNI-MATH 4,428 题中 200 题验证，Ouro-1.4B/
  2.6B，最大 4 loops；3 epochs、sequence length 4096、batch 8、每例 8 个高斯 latent rollouts，8×A100
  80GB，mixed precision、DDP 与 checkpointing。评价含 entropy-bucket next-token reasoning、MMLU/
  MMLU-Pro/BBH/ARC-C/HellaSwag/Winogrande/GSM8K、MBPP/HumanEval 系列；消融 noise、policy/KL、
  representation/entropy、token selection、time penalty，并检查 sequence length、KL、group size。
- **What the Evidence Proves / What It Does Not Prove**：作者实验支持该 objective 在两种 Ouro scale 和
  给定 benchmark 上改善 accuracy-compute Pareto，并把收益分解到多个组件；forced-depth 结果还直接显示
  “循环更多次”并不单调更好。它不证明 wall-clock/energy 随平均 steps 等比例下降，不证明对非 looped
  architecture 或生产 dynamic batching 有同样收益，也没有公开代码与独立 reproduction。
- **Limitations / Threats to Validity / Trade-offs / New Failure Modes / Previous Design Still Applies**：
  adaptive latent compute 节约易 token 的深度，却新增 exit miscalibration、EMA lag、teacher entropy bias、
  noisy-rollout variance、time-penalty tuning、不同 tokens/ranks 控制流发散与 kernel underutilization。固定
  depth 在吞吐优先、shape 规则、compile/cache 稳定或 halting calibration 未验证时仍合理；普通 NTP 对
  非 recurrent model 仍是最清楚的基础 objective。
- **Evolution Relationship / ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：`Direct
  Evolution` 于 Ch24：`uniform next-token loss → weight-shared recurrent depth → learned exit policy →
  latent-step reward jointly optimizes accuracy and compute`；`Layering / Dependency` 于 Ch17 recurrent
  operator graph 与 Ch45 serving kernel/runtime。主 owner 从 Ch17/29 更正为 Ch24；已读 Ch16～17、
  Ch23～25、Ch28～29、Ch45。Ch24 已有 NTP 与 compute contract，但尚缺 objective 直接监督 latent
  compute allocation 的分支；Ch29 的 GRPO 只提供 estimator 背景，不拥有该 pretraining mechanism。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New Mechanism
  (Books Gate Pending; Status: Experimental)`；Gate 后 refine Ch24，Ch17/45 只增加 architecture/runtime
  handoff。本 checkpoint 不改 `books/`。待 official code、token-level divergence 对 batch/kernels 的实际
  影响、wall-clock/energy/TTFT contract、更多 model/data scales、exit calibration drift 与 EMA recovery。

### BEAVER — 24/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `BEAVER-STRUCTURE-AWARE-CONTEXT-SELECTION`；arXiv:2603.19635v1，first-public 2026-03-20，
  当前仅 v1。已读 HTML 全文的 related work、Segmenter/PageEncoder/QueryPlanner、四套 benchmark、
  latency/scalability、component ablation、limitations、ethics 与 appendices；论文指向项目页/代码入口，
  但本 checkpoint 未获得可独立复跑的稳定 repository snapshot，记为 `Verified — Paper; Artifact Not
  Independently Reproduced`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：token-level perplexity
  pruning 粒度细、适合 tight budget；learned compressor 可按任务适配；直接塞入长上下文则保留全部证据。
  但 16K～128K context 下，逐 token scoring 延迟高，细粒度删除破坏句法/段落结构，专用训练又增加
  deployment 与 domain-transfer 成本。约束变成在固定 prompt budget 下同时保留 discourse continuity、
  lexical needles 与可向量化吞吐。
- **Mechanism / State Ownership / Control Flow / Data Flow**：Segmenter 按自然 delimiter 切 segment 并
  paginate；dual-path PageEncoder 对每页做 mean/max pooling，并按 context statistics 自适应融合；
  QueryPlanner 把 query-page semantic similarity 与 inverse-token-frequency lexical score结合，再由 anchor、
  flow 与 flash selections 组成连续子序列，sentence smoothing 修复边界。Authoritative source 仍是原文与
  query；page tensor、embedding、scores 和 compressed prompt 都是带 source range、policy/version 的派生
  context view，不可因被选中就升级为事实。
- **Implementation Details / Evaluation Contract**：下游生成统一使用 gpt-3.5-turbo-instruct，PageEncoder
  用 Qwen3-8B embedding；page size 64，主 token budget 2K/3K，在 LongBench、ZeroSCROLLS、RULER
  16K～128K 与 L-Eval 上比较 statistical、learned、embedding baselines。延迟/吞吐在 A100 80GB 测得；
  ablation覆盖 page size、pooling、multi-token query、semantic/lexical score、sentence smoothing 和三种
  selection policy。未披露统一 batch、concurrency、precision、warmup、prompt-cache 与 tail-SLO。
- **What the Evidence Proves / What It Does Not Prove**：作者 contract 下，page-level structure 与 hybrid
  semantic/lexical selection 相比所列 baselines取得更好的 quality/latency balance，且 ablation支持三条
  selection path 的互补性。它不证明所有 domain 都可由 query overlap 找到证据，不证明 26.4× headline
  可外推到不同 GPU/model/backend，也不证明压缩后答案的 factual faithfulness。
- **Limitations / Threats to Validity / Trade-offs / New Failure Modes / Previous Design Still Applies**：page
  粒度保留结构并利于 tensorization，却保留页内冗余；semantic/lexical overlap 对 deep multi-hop、隐含前提、
  否定与跨页因果链可能漏召回；固定 hyperparameters 会跨域漂移。直接长 context 在证据量可控、遗漏成本
  高时仍合理；token pruning 在极紧 budget 且句法破坏可接受时仍有价值；learned compressor 在稳定 domain
  和充足训练数据下可换取更强适配。
- **Evolution Relationship / ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：`Direct
  Evolution` 于 Ch71：`retain all context → token-level hard pruning → learned task-aware compression →
  structure-aware page selection with hybrid retrieval`；`Layering / Dependency` 于 Ch72 retrieval 与 Ch39
  Prefill cost。主 owner 从 Ch39/Ch74 更正为 Ch71；已读 Ch39、Ch71～74。Ch71 已说明 compression loss
  与 source-linked context，却缺少“压缩粒度决定信息完整性与硬件规则性”的明确分支；Ch72 已覆盖 query/
  compression/stopping，不应复制 benchmark。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Refine — Existing Argument
  (Books Gate Pending)`；Gate 后 refine Ch71，Ch39/72 只增加 cost/retrieval handoff。本 checkpoint 不改
  `books/`。待稳定官方 artifact、multi-hop recall 与 faithfulness、跨域参数选择、batch/concurrency、KV
  reuse、document update/invalidation 以及 sensitive segment 的 authorization-preserving selection。

### Breaking the Capability Ceiling by Reintroducing Markov States — 24/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `MARKOV-STATE-LLM-POSTTRAINING`；arXiv:2603.19987v1，first-public 2026-03-20，当前仅 v1。已读
  HTML 全文的 RL formulation、action/state/action-state baselines、three-puzzle experiments、theory、
  SFT/transition-model/Pass@k appendices 与 implementation details；未发现作者公开代码，`Verified — Paper
  Only / Experimental`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：把全部 token/action
  history 当 state 与 autoregressive model 原生接口一致，不需外部 simulator，并能保留非 Markov 信息；
  但在可由 compact current state 完全描述的长时程环境中，相同 board/code snapshot 可由许多历史到达，
  history-as-state 会重复学习等价路径并把 transition reconstruction 与 action policy 混在同一模型里。
- **Mechanism / State Ownership / Control Flow / Data Flow**：训练时 environment 执行动作并返回真实 next
  state，policy 仅根据当前 explicit state 生成下一 action；另训练 Qwen2.5-3B transition model，从 state+action
  预测 next state，测试时替代 environment。作者还比较保留全 state-action history 的中间 baseline，以隔离
  “显式 state 可见”与“强制 Markov policy”两项效应。Authoritative state 应由 environment/simulator 或
  versioned artifact snapshot 拥有；learned transition output 是带置信度的估计，policy history 不是事实源。
- **Implementation Details / Evaluation Contract**：Qwen3-4B 与 Qwen2.5-3B-Instruct 分任务先做短 SFT
  warm-up，再在 Reasoning-Gym 的 Sudoku、Sokoban、Futoshiki 上以 rLLM/GRPO、稀疏 terminal reward
  训练；ID/OOD 各采 128 solutions，报告 Avg@128 与 Pass@128。对 current-state ablation、SFT warm-up、
  SFT-only 与 oracle-action variants 做补充实验。理论假设 deterministic transition、bounded reward、
  optimization/advantage error，并通过 occupancy coverage 对比 history tree 与 Markov state coverage。
  正文未披露可复算的硬件、precision、batch/concurrency、总 compute 或 wall-clock/SLO。
- **What the Evidence Proves / What It Does Not Prove**：在三个 fully observable deterministic puzzle 与
  两个小模型上，explicit state 和 Markov conditioning 分别贡献增益，且训练 reward 更快上升；理论给出
  在其 coverage/error 假设下 history representation 可能指数膨胀的边界。它不证明 RL 产生了预训练中
  不存在的通用能力，不证明 code/web/partial-observable environment 满足 Markov 假设，也不证明 learned
  transition 在长 horizon 不积累错误。
- **Limitations / Threats to Validity / Trade-offs / New Failure Modes / Previous Design Still Applies**：compact
  state 降低冗余、改善 credit assignment，却新增 state schema、transition-model drift、error compounding、
  hidden-variable aliasing、snapshot consistency 与 recovery ownership。若 environment 部分可观测、history
  包含必要因果信息、transition 不可可靠重放，belief/history policy 仍合理；能提供 deterministic state
  machine 的 code/test/workflow 才是最直接的下一类适用场景。
- **Evolution Relationship / ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：`Direct
  Evolution` 于 Ch29：`response history as state → expose current environment state → separate transition and
  action policy → train on compact state-action credit`；`Layering / Dependency` 于 Ch73 state provenance 与
  Ch77 durable workflow snapshot。主 owner 从 Ch29/76 收敛为 Ch29；已读 Ch28～30、Ch73、Ch76～77。
  Ch29 已讨论 trajectory identity、partial rollout 与 reward context，但缺少“state representation 本身改变
  sample complexity 与 credit assignment”的机制；Ch77 已拥有 authoritative workflow state。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New Mechanism
  (Books Gate Pending; Status: Experimental)`；Gate 后 refine Ch29，Ch73/77 只增加 state-ownership handoff。
  本 checkpoint 不改 `books/`。待官方 artifact、stochastic/partially observable environments、transition-error
  sensitivity、long-horizon rollback、state-schema evolution、hardware/compute contract 与真实 code/web tests。

### AgentDS Technical Report — 22/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `AGENTDS-DOMAIN-DATA-SCIENCE-EVAL`；arXiv:2603.19005v1，first-public 2026-03-19；v2/v3 分别
  于 2026-05-31/06-03 修订。已读 v1 HTML 的 benchmark design、challenge taxonomy、competition
  protocol、scoring、AI baselines、human-AI collaboration、limitations 与 appendices，并核对当前 metadata
  与官方项目页。v3 摘要调整了相对人类排名措辞，因此不把任一 headline rank 当稳定事实；`Verified —
  Paper and Official Project Page`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：通用问答、代码生成
  或单一 Kaggle-style metric 便于规模化比较，也能隔离一项能力；但真实 data-science work 同时依赖 domain
  interpretation、multimodal evidence、data manipulation、analysis choice 与可交付 artifact。约束从“答案是否
  正确”变为“在有限时间、工具和领域信息下，完整工作流能否产生可评分结果”。
- **Mechanism / State Ownership / Control Flow / Data Flow**：benchmark 以 17 个 synthetic challenges 覆盖
  6 个行业；organizer 发布任务与数据，participant/agent 生成预测或 artifact，challenge metric 先评分，再以
  participant pool 内 quantile 归一化到 domain 与 overall。权威状态包括 challenge/data revision、submission、
  metric implementation、deadline 与 participant pool；自然语言解释和 agent trace 只是诊断证据，不能替代
  executable output。Human-AI collaboration 来自赛后行为观察，不是随机对照处理。
- **Implementation Details / Evaluation Contract**：29 支队伍、80 名参与者在 2025-10-18～27 的十天赛程
  完成任务，每 challenge 最多 100 次提交。AI baselines 包括 GPT-4o 单 prompt 生成并执行代码，以及
  Claude Code v2.1.30 / claude-sonnet-4.5 在每 challenge 十分钟预算下非交互执行。相对排名依赖同一
  participant pool、任务集合、工具配置与 quantile aggregation；论文 revision 改动也说明 headline 不能脱离
  版本复述。
- **What the Evidence Proves / What It Does Not Prove**：该 artifact 支持“Agent/data-science evaluation 必须
  同时绑定 domain task、executable submission、scorer 与 resource contract”，并提供人类与 AI 在同一竞赛
  外壳中的受限观察。它不证明模型在真实企业数据、长期协作或生产治理中的通用自主性；参与者自选、synthetic
  data、有限行业和非随机协作分析也不能支持因果化的人机互补结论。
- **Limitations / Threats to Validity / Trade-offs / New Failure Modes / Previous Design Still Applies**：统一
  submission/scoring 提高可比较性，却引入 synthetic-data realism、metric gaming、participant-pool dependence、
  tool-budget mismatch 与 aggregate quantile 掩盖 domain failure。单任务 deterministic benchmark 在回归定位和
  低成本 gate 中仍更合适；多域 competition 只在 deployment 也包含这些交付物与约束时增加外部效度。
- **Evolution Relationship / ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：`Layering /
  Dependency` 于 Ch62：`model answer score → system artifact score → multi-domain workflow evaluation →
  observational human-agent process evidence`；Ch69 只消费 readiness decision。主 owner 从 Ch62/69 收敛为
  Ch62；已读 Ch62、Ch68～69。Ch62 已明确 subject、distribution、scorer、execution artifact、domain slice、
  human judgement 与 observational boundary，AgentDS 没有改变该设计结论。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`No Change — Already Covered`；
  不将一届 competition 或 revision-sensitive rank 写进 Books。现有 Ch62 的 evaluation object、distribution、
  executable evidence 与 uncertainty 已完整拥有该观点。本 checkpoint 不改 `books/`。待公开 per-challenge
  artifact lineage、baseline sandbox/tool image、成本拆分、跨年份复测与 randomized collaboration protocol。

### OpenResearcher — 26/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `OPENRESEARCHER-OFFLINE-DEEP-RESEARCH-DATA`；arXiv:2603.20278v1，first-public 2026-03-17，当前
  仅 v1；联读官方 `TIGER-AI-Lab/OpenResearcher` repository。已读 HTML 全文的 answer-guided corpus
  bootstrapping、teacher rollout、filtering、SFT、offline/live evaluation、trajectory analysis、tool ablation、
  scaling、limitations 与 appendices，并核对公开 data/model/retriever artifacts；`Verified — Paper and Official
  Repository`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：直接在 live web 上采集
  research trajectories 最接近真实环境，也自然包含 freshness 与开放检索；但结果随时间、搜索 API、网页
  变更与成本漂移，难以复现长轨迹训练。固定 QA corpus 则便于监督，却常缺少足以支撑答案的完整 documents。
  约束变成：先构造可离线重放且确实含 evidence 的开放检索环境，再学习 search/open/find policy。
- **Mechanism / State Ownership / Control Flow / Data Flow**：一次性 answer-guided bootstrap 用 question 与
  reference answer 检索 gold documents，再与约 15M FineWeb documents 合并为 distractor corpus；
  Qwen3-Embedding-8B 与 FAISS 建索引。GPT-OSS-120B teacher 在生成轨迹时看不到 reference answer，只能
  调用 search/open/find，失败、malformed tool call、context overflow 与超预算轨迹被过滤；保留约 55K
  correct trajectories 做 SFT。权威状态是 source document、corpus/index revision、question/reference answer、
  tool result 与 filter verdict；trajectory 是其派生训练样本，不能反向证明 web 事实或 corpus 完整性。
- **Implementation Details / Evaluation Contract**：student 为 NVIDIA Nemotron-3-Nano-30B-A3B-Base-BF16，
  用 Megatron-LM 在 8×H100 上训练约 8 小时，packed context 256K、global batch 64、347 steps、学习率
  `5e-5`。BrowseComp-Plus 使用固定 offline corpus；BrowseComp、GAIA 与 xbench 使用 Serper live web。
  分析覆盖正确/错误/all trajectory filtering、gold-document removal、search/open/find tool ablation、retrieved-
  evidence 与 correctness、最大 turn budget；“API cost 为零”不包含 corpus embedding、index storage 与 serving。
- **What the Evidence Proves / What It Does Not Prove**：作者 contract 下，先保证 corpus support 再训练工具
  policy可得到可复现的长时程 research data；移除 gold documents 会显著破坏 coverage，而找到 gold document
  仍不足以保证答案正确。Correctness-only、incorrect-only 与 all-trajectory SFT 差异很小，支持“terminal
  correctness 不是唯一有用的数据过滤信号”，但不证明错误轨迹普遍安全或应无条件保留。
- **Limitations / Threats to Validity / Trade-offs / New Failure Modes / Previous Design Still Applies**：固定环境
  提高重放性，却以 answer-guided privileged support、benchmark contamination、index staleness 与巨额预计算
  换取确定性；teacher/filter 同源还会保留 false claim、bad stop 与 tool-pattern bias。Live web 在 freshness、
  authorization 与真实 adversarial conditions 上仍必要；小型 curated corpus 在题域稳定、证据许可严格时更
  可控。错误轨迹只有在错误类型可标注、目标与 loss 不奖励错误 claim 时才可能保留探索结构。
- **Evolution Relationship / ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：`Direct
  Evolution` 于 Ch23：`answer-only synthetic data → evidence-supported offline environment → tool-grounded
  trajectory synthesis → separate corpus coverage from policy success`；`Layering / Dependency` 于 Ch72 的
  retrieval contract、Ch74 的 tool schema 与 Ch77 的 workflow trace。主 owner 从 Ch74/77 收敛为 Ch23；
  已读 Ch22～25、Ch71～74、Ch77。Ch23 已覆盖 synthetic specification 与 verifier lineage，但尚未把
  corpus support/index revision 作为 trajectory-data contract 的前置变量。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New Mechanism
  (Books Gate Pending)`；Gate 后 refine Ch23，Ch72/74/77 仅加短 handoff。本 checkpoint 不改 `books/`。
  待 answer-guided leakage audit、错误轨迹 taxonomy、cross-retriever/corpus transfer、index build/serve 成本、
  web freshness、安全/许可与同一训练环境上的 independent held-out evaluation。

### BubbleRAG — 24/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `BUBBLERAG-BLACKBOX-KG-EVIDENCE-SUBGRAPH`；arXiv:2603.20309v1，first-public 2026-03-19，
  当前仅 v1。已读 15 页 technical report 的 formalization、semantic anchoring、bubble expansion、collision、
  ranking、reasoning-aware expansion、retrieval/generation evaluation、efficiency、ablation 与 sensitivity；未发现
  与论文绑定的公开代码，`Verified — Paper Only`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：vector top-k 对单跳语义
  相似问题便宜，显式 schema 的 KG query 可直接约束 relation/path；但第三方或自动构建 KG 常只暴露
  topology/text，不暴露稳定 schema。多跳问题于是同时存在 semantic instantiation、structural path 与
  evidential comparison 三重不确定性，单点相似度不能保证召回一组可连通、可共同作证的事实。
- **Mechanism / State Ownership / Control Flow / Data Flow**：LLM 从 query 提取 explicit/implicit concepts，
  每组 concept 生成 top-k semantic anchors；系统在局部 h-hop subgraph 中从多组 anchors 做 anisotropic
  multi-source bubble expansion，异组前沿 collision 时重建 candidate evidence graph，未碰撞则 fallback 到
  anchors。候选按 semantic cost 与 missing-concept/structural-completeness penalty 排序，再做 reasoning-aware
  expansion；最终 graph 通过 provenance pointer 映射回 raw chunks。权威事实仍属于 source chunks/KG
  revision；anchor、path、CEG、rank score 与 merged context 都是 query-specific derived views。
- **Implementation Details / Evaluation Contract**：HotpotQA、MuSiQue、2WikiMultiHopQA 各取 1K validation
  questions，统一 Qwen3-Embedding-8B、最多 15 chunks，并在 30B/8B generation settings 下与 NaiveRAG、
  ToG、HippoRAG2、RAPTOR、ClueRAG、LightRAG variants 等比较；semantic answer score 使用 Qwen3-7B
  judge。消融/敏感性覆盖 expansion budget、depth 与 structural penalty；效率在单 A100、100 queries 上测量。
  未披露生产并发、KG build/update cost、precision、cache 或 tail-SLO contract。
- **What the Evidence Proves / What It Does Not Prove**：作者设置下，query-specific connected evidence graph
  与三类不确定性建模改善所列 multi-hop QA 的 retrieval/generation，并显示 expansion/penalty 的条件性作用。
  它不证明 Group-Steiner 近似在任意 KG 上最优，不证明 LLM anchor/judge 无同源偏差，也不证明单 A100
  headline latency 能外推到动态生产图谱或其他模型。
- **Limitations / Threats to Validity / Trade-offs / New Failure Modes / Previous Design Still Applies**：局部图
  search 保留跨 hop 关系，却新增 anchor miss、frontier explosion、false collision、graph extraction error、
  provenance break、stale edge、LLM reasoning cost 与 judge bias。Dense top-k 在单跳、图质量差或 latency
  紧张时仍更合理；显式 schema/query plan 在 ontology 稳定时更精确。Graph path 只说明连接性，不自动证明
  relation truth、authorization 或 context sufficiency。
- **Evolution Relationship / ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：`Direct
  Evolution` 于 Ch72：`independent chunk similarity → entity/edge traversal → multi-anchor frontier collision →
  query-specific evidence subgraph with source dereference`；`Layering / Dependency` 于 Ch71 context packing 与
  Ch62 system evaluation。主 owner 从 Ch74 更正为 Ch72；已读 Ch62、Ch71～74。Ch72 已覆盖 relevance、
  sufficiency、agentic retrieval 与 provenance，但缺少 black-box KG 下“连接证据集合而非排序独立 chunks”
  的清晰设计分支。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Integrate — New Mechanism
  (Books Gate Pending)`；Gate 后 refine Ch72，Ch62/71 只增加 evaluation/context handoff。本 checkpoint 不改
  `books/`。待官方 artifact、KG construction/provenance contract、dynamic update/delete、anchor calibration、
  judge-independent evaluation、concurrency/tail latency 与授权过滤不破坏连通性的设计。

### HopChain — 24/30

- **Source Family ID / Source Type / Event Date / First-public Date / Revision History / Direct Primary
  Sources / Related Primary Sources / Access and Verification Status / Full-read Coverage**：
  `HOPCHAIN-MULTIHOP-VISUAL-RLVR-DATA`；arXiv:2603.17024v1，first-public 2026-03-17；v2 于
  2026-03-19 修订。已读 v1 28 页 HTML 的 data synthesis、image filtering、query generation、annotation、
  difficulty filtering、RLVR training、24-benchmark evaluation、full/half/single-hop ablation、error/length analysis
  与 appendices，并核对 v2 metadata；未发现官方 code/data artifact，`Verified — Paper Only`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：single-hop VQA 或普通
  multimodal RLVR 便于得到确定 reward，也能训练局部识别与推理；但长 CoT 中 perception、knowledge、
  reasoning 与 hallucination error 会逐步累积，而同一图片配一个难问题不保证每一步都必须重新 grounded。
  约束变成生成一条逻辑依赖链，使后一步只有在前一步正确定位视觉对象后才可继续。
- **Mechanism / State Ownership / Control Flow / Data Flow**：Qwen3-VL-235B-A22B-Thinking 先识别语义类别，
  SAM3 产生 instance masks/bounding boxes；从中选 3～6 个对象生成依赖式 multi-hop query。crop/mask 只在
  design-time 帮助 generator，不允许出现在最终 query。四名 annotators 独立求解且必须一致；弱模型八次全对
  的样本被去除，得到每模型约 6K～8K visual RLVR samples，并与近似数量的 math RLVR 混合。权威证据是
  source image、object annotation、dependency graph 与 agreed answer；自然语言 chain 是模型行为，不拥有
  图像事实。
- **Implementation Details / Evaluation Contract**：Qwen3.5-35B-A3B 与 Qwen3.5-397B-A17B 分别比较原
  RLVR data 与 `original + HopChain`，在 STEM/puzzle、general VQA、OCR/document 与 video 共 24 个
  benchmarks 上评价；full-chain、half-chain、single-hop 在五个代表 benchmark 上消融。公开正文未披露可
  复算的 accelerator、precision、batch、optimizer、concurrency、总 compute 或 serving SLO；error analysis
  每 benchmark 只抽取 20 个错误并标注 primary category，因此只能作定性诊断。
- **What the Evidence Proves / What It Does Not Prove**：作者实验支持“结构性依赖的 visual evidence chain”
  相比相同来源的 shorter-hop variants 对两种 Qwen3.5 scale 更有效，并在 20/24 benchmark 上改善。它不证明
  单纯延长 CoT 会改善 grounding，不证明所有 visual reasoning 都可还原为 3～6 个 segmented instances，也
  不证明收益跨模型 family、真实图像分布或未公开训练 contract 泛化；四个 benchmark regression 也不能省略。
- **Limitations / Threats to Validity / Trade-offs / New Failure Modes / Previous Design Still Applies**：结构化
  chain 强化 repeated grounding，却新增 segmentation bias、generator/annotator shared assumption、synthetic
  wording、exact-numeric-answer 偏置与 design-time crop leakage。Single-hop data 在基础 perception、低延迟
  和局部回归测试中仍合理；自然图文 instruction data 保留开放语义。更长 chain 只有在每 hop 的 evidence
  dependency 可验证时才是难度，而非 verbosity。
- **Evolution Relationship / ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：`Refine —
  Existing Argument` 于 Ch23：`image-answer pair → annotated object evidence → dependency-constrained multi-hop
  task → RLVR trajectory requiring repeated grounding`；`Layering / Dependency` 于 Ch29 reward 与 Ch22 的
  effective visual-token evidence。主 owner 从 Ch23/29 收敛为 Ch23；已读 Ch22～24、Ch28～29。Ch23 已
  覆盖 multimodal transformation lineage 与 specification-derived synthetic data；HopChain 补充的是 dependency
  graph 如何避免把“长答案”误当成“多步证据”。
- **Integration Decision / Changed Files or Rejection Reason / Open Questions**：`Refine — Existing Argument
  (Books Gate Pending)`；Gate 后 refine Ch23，Ch22/29 只增加 visual-evidence/reward handoff。本 checkpoint
  不改 `books/`。待 official artifact、hardware/training recipe、natural-image/domain transfer、segmentation
  failure slices、per-hop grounding verifier、四个 regression 原因与人工标注一致性细节。

### NVIDIA Vera Rubin platform / POD-scale co-design — 27/30

- **Source Family ID / Source Type / Event Date / Direct Primary Sources / Access and Verification Status /
  Full-read Coverage**：`NVIDIA-VERA-RUBIN-POD-CO-DESIGN`；2026-03-16 官方 announcement、platform
  overview、developer technical article 与 NVLink specification 联读。页面将数字标为 preliminary，故
  `Verified — Official Architecture and Preliminary Specifications`，不是独立 benchmark 复现。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：以单 GPU 或单服务器
  为采购、编译和运维边界，在模型可装入单机、collective 主要留在机内时最简单；当训练与推理跨 rack，
  bottleneck 同时落在 compute、HBM、scale-up/scale-out network、storage、power 和 cooling，单芯片优化
  无法保证系统平衡，设计单位转向 rack/POD。
- **Mechanism / State Ownership / Control Flow / Data Flow / Implementation Details**：官方公开的是七类芯片、
  五种 rack system 与 POD-level integration 的组合。NVL72 以 72 个 Rubin GPU、36 个 Vera CPU 形成
  scale-up domain；NVLink 6 页面给出每 GPU 3.6 TB/s、NVL72 aggregate 260 TB/s 的 preliminary link
  contract。GPU/CPU 拥有 compute 与 memory state，fabric 拥有 reachability/transport，cluster control plane
  拥有 placement、health 和 repair；三者是 layering，不可把 fabric bandwidth 写成 application throughput。
- **Evaluation Contract / What the Evidence Proves / What It Does Not Prove**：官方材料证明 NVIDIA 把
  data-center/POD 作为 co-design 与交付边界，并披露目标 topology/specification；vendor workload 数字没有
  完整绑定 model、precision、length、batch、concurrency、software version 与 SLO，因此不进入长期结论，
  也不证明任意 workload 都应采用最大 scale-up domain。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：更大 failure domain 能减少跨层 protocol
  mismatch，却提高 power/cooling/network 共故障、升级耦合、容量碎片与供应商锁定风险。小模型、端侧、
  独立 batch job 或 elastic scale-out 仍可选择较小服务器边界。
- **Evolution Relationship / ROADMAP / Adjacent Chapters / Integration Decision**：相对“单 accelerator 优化”
  为 `Direct Evolution` 的 design boundary expansion；相对 scheduler、storage、serving control plane 为
  `Layering / Dependency`。主 owner Ch50，handoff Ch53/57/59；已读 Ch48～53。`Refine — Existing Argument
  (Books Gate Pending)`：补强 workload contract 如何上升到 rack/POD co-design，不写产品规格表。

### NVIDIA DSX Air — 23/30

- **Source Family / Type / Event Date / Sources / Access**：`NVIDIA-DSX-AIR-AI-FACTORY-SIMULATION`；
  2026-03-16 NVIDIA official announcement 与 developer article；`Verified — Product/Architecture Fact`。
- **Problem / Previous Design / Changed Constraint**：真实机房 staging 能验证网络、storage、security 与
  workload integration，但昂贵、慢且在硬件到货后才暴露错误；AI factory 的组合空间和 deployment cost
  使 pre-deployment simulation 更有价值。
- **Mechanism / Ownership / Flow**：公开材料把 infrastructure blueprint、simulated compute/network/storage/
  security 与 validation scenario 组合为 digital environment。设计输入属于 platform/infrastructure owner，
  scenario 和 pass/fail criterion 属于 validation owner，真实 production telemetry 仍需在部署后校准模型。
  官方未披露 simulator fidelity model、event scheduling、network/storage contention 实现或 failure injection
  coverage，不能由产品目标反推内部机制。
- **Evidence Boundary / Trade-off**：材料证明存在 design-before-build、test-before-deploy 的产品边界；没有
  公开受控实验证明其 prediction error、跨 vendor fidelity 或生产 SLO 改善。simulation 降低物理试错成本，
  但新增 model drift、false confidence、scenario coverage 和 simulated/real identity 对齐问题；lab staging、
  canary 与 production observability 仍不可替代。
- **ROADMAP / Disposition**：主 owner Ch69，handoff Ch53/63～65；已读 Ch53、Ch63～69。
  `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`，不修改 Books。

### NVIDIA Dynamo v1.0.1 / v1.1.0-dev.1 — 23/30

- **Source Family / Event Date / Sources / Access**：`DYNAMO-INDEX-EVENT-RECOVERY`；v1.0.1 于
  2026-03-16，v1.1.0-dev.1 于 03-17；官方 release history、per-release notes 与 GitHub release 联读；
  `Verified — Official Release and Documentation`。dev release 明示 early access、not for production。
- **Problem / Previous Design / Changed Constraint**：in-process KV index/event handling 在单模型和低故障率时
  直接；多模型、多 tenant、P2P member failure 与 event gap 使 index identity、ordering 和 recovery 需要
  独立生命周期。patch release 同时暴露 serving API 的 byte/token streaming correctness 不是外围细节。
- **Mechanism / State Ownership / Control Flow / Data Flow**：v1.0.1 修复 CUDA 13.1 cutlass-dsl crash、
  OpenAI-compatible logprobs bytes/token 与 Kimi tokenizer incomplete-multibyte streaming panic；不增加或删除
  artifacts。v1.1.0-dev.1 将 KV indexer 拆为独立 crate/process，引入 model/tenant isolation、P2P recovery、
  ZMQ gap detection/replay、metrics、pluggable router queue scheduling 与 Velo async events。producer 拥有
  authoritative KV lifecycle event，indexer 拥有 derived searchable view，router 只消费带 freshness/recovery
  contract 的 view。
- **Evidence Boundary / Trade-off / Failure Modes**：release notes 证明 interface 与 component boundary 的
  变化，不提供可外推的 latency/throughput 结论。独立 index 提高隔离和恢复能力，却新增 event ordering、
  gap replay、stale view、rebuild、backpressure 与 control-plane availability；小规模单进程路径仍更简单。
- **ROADMAP / Existing Coverage / Disposition**：`Direct Evolution`：in-process derived state → standalone
  recoverable index；主 owner Ch48，已读 Ch47～49。Ch48 已明确 index 不是 source of truth，并覆盖 sharding、
  event ordering/freshness、rebuild 与 fallback，且以后续 stable Dynamo evidence 论证，故
  `No Change — Already Covered`。

### Kubeflow Community Distribution 26.03 — 21/30

- **Source Family / Event Date / Sources / Access**：`KUBEFLOW-COMMUNITY-DISTRIBUTION-CONTRACT`；
  2026-03-22 official distribution release page；`Verified — Official Release Manifest`。
- **Problem / Previous Design / Changed Constraint**：各 Kubeflow component 独立升级允许快速演化，却把
  API、dependency、RBAC、image 与 installation compatibility 风险转给使用者。完整 distribution 需要一个
  跨 component 的 tested version set，而不是把“每个组件最新”当成“平台兼容”。
- **Mechanism / State Ownership / Flow**：26.03 转为 calendar versioning，并锁定 Pipelines、KServe、Trainer、
  Model Registry 等 component versions。distribution manifest 拥有组合兼容声明；subproject release 仍拥有
  自身 API/feature truth。安装者从 manifest 选择组合，不能用某个 subproject 的新版本能力反推 distribution
  已携带该能力。
- **Evidence Boundary / Trade-off**：官方 manifest 证明版本集合和 release identity，不证明所有 deployment
  profile、upgrade path 或第三方 extension 都已验证。固定组合减少 integration entropy，但引入 release lag、
  coordinated CVE patch 与 cherry-pick pressure；advanced operator 仍可独立组合，但必须自己拥有测试契约。
- **ROADMAP / Existing Coverage / Disposition**：主 owner Ch54，已读 Ch53～55。Ch54 已明确 distribution
  contract 与 subproject release 解耦，故 `No Change — Already Covered`。

### Kubeflow Trainer v2.2 — 26/30

- **Source Family / Event Date / Sources / Access**：`KUBEFLOW-TRAINER-V2-RUNTIME-OWNERSHIP`；
  2026-03-20 official release blog、GitHub v2.2.0 release 与 current docs 联读；`Verified — Official Release,
  API and Documentation`。V2 APIs 仍有 alpha/breaking-change 边界。
- **Problem / Previous Design / Changed Constraint**：framework-specific job types 和无 owner 的 arbitrary
  Pod patch 在少数框架时灵活，但随着 JAX、XGBoost、MPI/HPC 与 platform policy 汇合，同一 workload
  intent 会被多套 CRD、状态和 override 语义分裂。平台需要统一提交面，同时保留不同 runtime 的能力边界。
- **Mechanism / State Ownership / Control Flow / Data Flow**：v2.2 将 JAX/XGBoost 纳入 TrainJob runtime，
  将 script progress/metrics 传播到 TrainJob status，支持 Flux HPC/MPI 与 `activeDeadlineSeconds`；
  `RuntimePatches` 用 immutable manager key 建立字段所有权，替代无 owner 的 PodTemplateOverrides，并移除
  `ElasticPolicy`。TrainJob 拥有 workload intent/attempt，Runtime 拥有 reusable topology，patch manager
  拥有受控字段，controller 汇总 observed status；scheduler 仍拥有 admission/placement。
- **Implementation / Evaluation Contract / Evidence Boundary**：公开 evidence 是 API、release note、controller
  contract 与 examples，不是性能 benchmark。它证明 control-plane boundary 和 breaking migration，不能证明
  JAX、XGBoost、PyTorch 在容错、elasticity、checkpoint 或 telemetry 上语义等价；移除 ElasticPolicy
  反而说明 unified API 不等于 feature parity。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：manager-key ownership 改善冲突审计和
  admission safety，却增加 manager identity、field conflict、patch migration 与 abandoned-manager cleanup；
  status 传播提高可观测性，但需要处理 stale/partial metrics 和 attempt identity。旧 V1 CRD 在既有部署可继续，
  不应与 V2 contract 混写。
- **ROADMAP / Existing Coverage / Disposition**：`Direct Evolution`：framework-specific CRD/unowned override
  → TrainJob + runtime + manager-owned patch；主 owner Ch56，已读 Ch55～57。现有 Ch56 已覆盖受控 patch、
  attempt/status 与 operator/scheduler 分责，但未充分说明 manager-key field ownership、status propagation 与
  “统一提交面不等于 runtime 语义等价”，故 `Refine — Existing Argument (Books Gate Pending)`。

### Kubeflow SDK v0.4.0 — 21/30

- **Source Family / Event Date / Sources / Access**：`KUBEFLOW-SDK-LIFECYCLE-FACADE`；2026-03-19
  official release blog、package/repository documentation；`Verified — Official Release Fact`。
- **Problem / Previous Design / Changed Constraint**：分别调用 pipelines、trainer、registry 与 Spark clients
  保留组件边界，但让 notebook/workflow 代码承担多套 auth、namespace、artifact 与 local/remote lifecycle。
- **Mechanism / Ownership / Flow**：v0.4.0 增加 ModelRegistryClient、SparkClient/Spark Connect、namespaced
  TrainingRuntimes，以及 dataset/model initializers 的 local/remote parity。SDK 只拥有 client-side intent、
  serialization 和 convenience；server-side controller/registry 仍拥有 durable identity、reconciliation 与
  authorization。相同 Python call 不能证明 local 和 remote execution 具备相同 failure、lineage 或 isolation。
- **Evidence Boundary / Trade-off**：release 证明 facade surface 与 minimum Python contract，不证明 underlying
  components 已形成 transactional end-to-end lifecycle。统一 SDK 减少 integration friction，却可能隐藏
  capability mismatch、version skew 与 partial failure；直接 component API 在调试和 advanced feature 场景仍合理。
- **ROADMAP / Existing Coverage / Disposition**：主 owner Ch53，handoff Ch54～56；已读 Ch53～56。现有章节
  已把 platform 定义为共享对象与 lifecycle contract，而非 SDK/tool collection，故
  `No Change — Already Covered`。

### vLLM incremental MoE expert offloading — 26/30

- **Source Family / Event Date / Revision / Access**：`VLLM-MOE-EXPERT-WEIGHT-TIERING`；
  vLLM PR #37190 于 2026-03-16 首次公开，建立本 family 的 owner week；2026-03-26 的 RFC #38256
  属于 W13 architecture evolution。已读 PR purpose、code/change inventory、review threads、tests、
  current limitations 与 RFC 全文；截至 2026-08-11 二者仍为 `Open`，不是 merged release behavior。
  当前 PR 已吸收多轮 review 后的 provider/mapping/guard 设计，不能倒写成 3 月 16 日初始 commit 已经
  具备全部机制。
- **Original Problem / Why Previous Designs Were Reasonable / Changed Constraint**：静态 CPU weight
  offload 在模型能以固定分层方式运行时简单、可预测，全量 HBM residency 在 latency-sensitive serving
  中仍是最稳分支。但 MoE 的 total expert weights 可远大于每 token 的 active experts；当模型总权重超过
  HBM、而 router 的短期 working set 有 locality 时，“所有 expert 永久在 GPU”浪费 capacity，“固定一部分
  永久在 CPU”又不能跟随热点变化。约束变化是 router-conditioned working set、有限 GPU slots 与 PCIe
  miss latency 同时进入每层 critical path。
- **Mechanism / State Ownership**：CPU pinned memory 保存 local experts 的 backing weights；固定地址的
  GPU slots 保存 resident experts；`CachedWeightProvider` 拥有 `expert_id -> slot_id` mapping、free slots、
  LFRU frequency/recency state 与 hit/miss。Router 仍拥有 global top-k expert ids，EP mapping 仍负责
  global-to-local identity；provider 只保证请求的 local experts resident 并把 ids 重映射为 slot ids。
  Kernel 消费 GPU buffers 和 remapped ids，不应知道 weight 来自 HBM 还是 host tier。这个 ownership
  boundary 避免为 offload 建立绕过正常 quantization/runner 的第二条 forward path。
- **Control Flow / Data Flow**：`router top-k ids -> global/local expert mapping -> provider.prepare(unique ids)
  -> cache hit update or LFRU victim selection -> pinned-DRAM-to-GPU copy -> persistent mapping in-place update
  -> slot ids -> existing fused-MoE kernel`。Batched Prefill 先 deduplicate requested experts，避免按
  `sequence_length × top_k` 重复搬同一权重；Decode 则暴露逐步 miss 与热点漂移。PR 1 只有 synchronous
  H2D，RFC 中 async stream、cross-layer prediction、disk tier、telemetry 与 EPLB integration 属于后续
  proposal，不能记作已实现。
- **Implementation Contract**：当前 proposal 为 BF16 与 FP8 per-tensor scales、single GPU、
  `--enforce-eager`，固定 GPU buffers 和 persistent `int32` mapping；bias、EP>1、CUDA graph/compile path、
  async prefetch、其他 quant formats 与 concurrent forwards 均未形成发布保证。默认 cache size 为零时走
  原路径；请求的 unique experts 超过 capacity 时设计选择显式报错，而不是静默 CPU compute fallback。
- **Evaluation Contract / What Evidence Proves**：RFC 引用 tinyserve 的独立实现：RTX PRO 2000 8 GB、
  GPT-OSS-20B MXFP4、238 cache slots、single-stream Decode，报告约 30 tok/s 与 97～100% hit rate；还报告
  batched Prefill 将重复 loads 从 token-assignment 量级降到 unique-expert 量级。它只证明同类机制在该
  laptop-GPU、模型、量化、cache capacity 和单流 workload 中可行。没有 H100/A100 multi-user batching、
  TP/EP、长尾 SLO、domain shift、cold start、PCIe contention 或与同预算 full-GPU baseline 的完整对齐；
  PR/RFC 也不是 vLLM maintainer acceptance 或 production support 证明。
- **Ablation / Sensitivity / Overhead Boundary**：公开材料比较 LFRU 与 pure LRU 的动机，并披露 hub-expert
  preservation、fixed mapping 与 batched dedup，但没有系统覆盖 cache size、batch diversity、routing
  entropy、layer-wise locality、host bandwidth、KV budget 或多租户 interference 的 sensitivity surface。
  PR review 已明确指出 synchronous H2D、mapping allocation、runner bypass、bias、graph capture、memory
  accounting 与 thread safety 风险；后续 revision 修正部分接口问题，不等于 latency/throughput 风险消失。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：dynamic cache 让超出 HBM 的 MoE
  成为可执行候选，却新增 cache thrashing、cold-start miss、pinned-memory pressure、H2D queueing、stale
  mapping、capacity overflow、quant/bias incompatibility、graph-capture invalidation、shared-weight race 与
  EP collective stall。Batch 越多样，expert union 越大，单流 locality 越不能外推。模型可完全驻留或
  TPOT SLO 严格时 full HBM 仍成立；热点稳定且可接受固定慢路径时 static offload 更简单；compression
  减 bytes，offload 改 tier，二者是可组合分支而非互相替代。
- **Evolution Relationship / ROADMAP / Existing Coverage / Disposition**：`full HBM residency -> static
  host offload -> router-conditioned expert cache -> async prediction/prefetch proposal` 是 `Direct Evolution`；
  与 KV tiering 只是 `Principle Reuse`，两者的 identity、reuse window 与 correctness payload 不同。主 owner
  Ch50，已读 Ch49～51；另核对 Ch21 与 Ch46。Ch50 已覆盖 weight/KV/workspace 对 HBM 的竞争和 offload
  trade-off，但尚未显式拥有“router 产生 weight working set、provider 拥有 residency/mapping、batch
  diversity 决定 miss surface”的机制，因此暂定 `Refine — Existing Argument (Experimental;
  Provisional; Historical Books Gate Closed)`。Ch21 只保留 active/total parameter 与 routing handoff，
  Ch46 只保留 vLLM version boundary；本轮不修改 Books。

### Astrolabe — low-score verification, 19/30

- **Source / Date / Revision / Access**：arXiv:2603.17051 v1 first-public 2026-03-17；官方 project page 与
  `franklinz233/Astrolabe` repository 已核对，code 于 03-23 发布，属于 W13 follow-up。当前访问未获得可完成
  appendix/evaluation-contract 审计的 paper body，因此不建立伪 Full Source Review。
- **Verified Boundary**：公开摘要与 repo 支持 forward-process RL、negative-aware fine-tuning、rolling
  KV-cache、detached local-window gradients、多 reward、uncertainty-selective KL 和 dynamic reference update；
  支持 LongLive、Self-Forcing、Causal Forcing、Krea14B，并使用 HPSv3 与 VideoAlign reward families。
  它不证明 reward 改善等于 temporal consistency，也不披露足以外推的 hardware、precision、batch、video
  length、compute、ablation 与 deployment SLO contract。
- **Score / Rejection / ROADMAP**：source reliability 从 3 调整为 4，总分 19/30。它是 niche video
  post-training mechanism，当前无法通过 full-paper gate，且对本书主干的长期 system impact 仍不足。
  `Weekly Only — Below Threshold; Mechanism Not Fully Verified`；潜在 owner Ch29，Ch44 仅为 cache analogy；
  不修改 Books，W13 只记录 code-release lineage，不重复作为新研究结论。

## Repository Changes

- 本节前半保留 Discovery/Source Review 阶段的历史变更轨迹；其中 legacy Ch 编号、`provisional` 与
  `Books Gate Pending` 已被最终 Candidate Scoring、Books Integration Decision 和上表取代。
- 重开并完成 W12 Discovery Recall Gate，将候选池从 3 项扩展为 49 个 in-window candidate families。
- 新增 46 个 recovered candidate rows、评分、primary-date census 与 W10/W11 spillback ledger。
- 完成 18 个 recovered candidates 的全文、关键 appendix、可访问的官方 artifacts 和目标/相邻章节
  非模板化 Source Review。新增本批中，Efficient Reasoning 从 Ch42/45 更正为 Ch26，SWE-Skills-Bench
  从 Ch62/77 收敛到 Ch80，FlashSampling 从 Ch44 更正为 Ch20，MetaClaw 从 Ch73/78 收敛到 Ch80。
  Complementary RL 收敛到 Ch29，BenchPreS 从 Ch62/73 收敛到 Ch73，AdaMem 保持 Ch73 并归类为
  refine，VTC-Bench 保持 Ch62 且以章节级去重结束。Efficient Exploration 从 Ch29 更正为 Ch27，
  training-free MTP 从 Ch43/44 收敛到 Ch44，RAMP 从 Ch42/45 收敛到 Ch45 并保持 Experimental，PRISM
  从 Ch21/29 更正为 Ch24。AI Scientist 从 Ch77 更正为 Ch25，Nemotron-Cascade 2 从 Ch29/37 收敛为
  Ch29，Memento-Skills 从 Ch73/78 更正为 Ch80，AndroTMem 从 Ch73/77 收敛为 Ch73。ProRL Agent 从
  Ch29/57 收敛为 Ch29，Reasoning over Mathematical Objects 从 Ch29/62 更正为 Ch27，Hyperagents 从
  Ch78/80 更正为 Ch77，λ-RLM 从 Ch17/77 收敛为 Ch77。Subgoal-driven Agents 从 Ch76/77 收敛为
  Ch75，LoopRPT 从 Ch17/29 收敛为 Ch24，BEAVER 从 Ch39/74 收敛为 Ch71，Reintroducing Markov
  States 从 Ch29/76 收敛为 Ch29。AgentDS 从 Ch62/69 收敛为 Ch62 并完成章节级去重；OpenResearcher
  从 Ch74/77 更正为 Ch23；BubbleRAG 从 Ch74 更正为 Ch72；HopChain 从 Ch23/29 收敛为 Ch23。
  官方/Infra 收口批次又完成 Vera Rubin、DSX Air、Dynamo v1.0.1/v1.1.0-dev.1、Kubeflow
  Distribution 26.03、Trainer v2.2、SDK v0.4.0 与 vLLM incremental MoE expert offloading 七份
  Source Review；Astrolabe 完成低分拒绝核验。vLLM family 按 3 月 16 日 open PR 回归 W12，3 月 26 日
  RFC 只在 W13 记录 architecture evolution，未重复计分。
  当前 48/48 个 `20+` review complete，0/48 pending，1/1 low-score verification complete。
- 保留全部 Source Review 作为 evidence packet，并完成周级 Books Integration：34 项 Integrate/Refine
  进入 17 个 Stable Node owner，11 项 No Change、3 项 Weekly Only、1 项 Emerging。旧 legacy Ch 编号
  仅作为阅读快照；最终 owner/current/legacy mapping 由本周 Books Integration Decision 与 ROADMAP 解释。
- 同步年度索引与 `docs/LEARNING_STATE.md`。W12 Source-Family Books Gate 通过，Historical Archive
  Completion Gate 仍开放；下一检查点进入 W13。

## Open Questions

1. Vera Rubin 的 preliminary topology/spec 能否在 shipment 后由公开 topology-aware workload contract
   复核，且 rack/POD failure domain 如何进入 scheduler 与 serving recovery policy？
2. Attention Residuals 与 Mixture-of-Depths 的收益分别来自 depth-wise aggregation 与 conditional
   computation 的哪一层，二者在 pipeline communication 上是否形成依赖而非替代？
3. Online Experiential Learning、Complementary RL、MetaClaw 与 Memento-Skills 的 experience/skill/
   parameter state 如何做 provenance、versioning、rollback 与 deletion？
4. ProRL Agent 的 rollout-as-a-service API、sandbox lifecycle 与 trainer backpressure 在公开实现中由谁
   拥有？
5. workflow optimizer 与 engine scheduler 谁拥有 cache invalidation 和 retry semantics？
6. OpenSeeker 的 oracle subgraph、teacher summary 与真实 raw observation 之间如何检测不可恢复的
   privileged-information leakage？
7. Code-A1 的 Test LLM 与 Mistake Book 如何 version、expire 和跨 checkpoint 回放，才不会把旧 policy
   的失败分布固化成新的 verifier blind spot？
8. OEL 的 user-side trajectories 和 derived experience 如何执行 consent、tenant isolation、poisoning
   review 与 parameter-level deletion/rollback？
9. TRUST-SQL 的 phase mask 与 schema reward 在非 SQLite、带权限的 live catalog 中是否仍能阻止
   exhaustive-enumeration shortcut？
10. MoE expert cache 在多请求 routing diversity、TP/EP、严格 TPOT SLO 与 KV capacity 竞争下，何时会
    因 PCIe miss、collective stall 或 cache thrashing 失去相对 full residency/static offload 的收益？
11. Efficient Reasoning 的 base-only prompt KV 是否能扩展到需要 prompt-side adapter 的任务，真实手机
    上 route error、TTFT、TPS、energy 与并行候选的 operating point 是什么？
12. SWE-Skills-Bench 的官方 artifact 能否解释论文两种 injection path，且多模型、重复 runs 和更难
    repositories 下是否仍有相同的 compatibility/interference 结论？
13. FlashSampling v2 为何把 v1 的约 19% end-to-end headline 修订为 10%，公开 vLLM/TP patch 后能否
    复算 processor compatibility 与 RNG/retry semantics？
14. MetaClaw 如何把 consent、tenant、skill generation、PRM、checkpoint、rollback 和 selective deletion
    串成可审计 lineage，而不是只提供整目录 uninstall？
15. Complementary RL 如何把 actor/extractor、experience merge 与 retrieval generation 纳入同一 lineage，
    并在缺少 hardware、precision 与公开实验配置时复核长期稳定性？
16. BenchPreS 的 preference applicability policy 能否扩展到 informal/multilingual context 与具有外部副作用
    的 tool action，而不把 false suppression 变成新的可用性风险？
17. AdaMem 的 write-time canonicalization 错误如何修复并传播到 episodic/persona/graph stores，delete 与
    graph rebuild 是否能保持跨 store 一致？
18. VTC-Bench 的 32/35 tools 冲突、dataset license 与 alternate-valid-path verifier 能否由作者 artifact
    给出确定答案？
19. 信息定向 feedback selection 在真实人类 disagreement、safe exploration 与独立 evaluator 下还能否
    保持 label-efficiency 优势，1000× curve extrapolation 是否能被实测？
20. Training-free MTP 在 stochastic sampling 下的 acceptance/rejection 如何严格保持 target distribution，
    tree-build metadata、TP 与高并发会否抵消单卡收益？
21. RAMP 能否发布可执行 GGUF artifact 并在同一 workload 上直接复核 quality、memory 与 latency，而非
    引用公共 llama.cpp 表；论文内部 bit/decoding contract 如何统一？
22. PRISM 的 data/model/code 何时公开，mid-training 的 long-context damage、merge repair 与后续 RL
    reachability 能否在跨 family、跨领域且无 shared-filter bias 的设置中复现？
23. Synthetic ML environment 的 task/evaluator/container/teacher lineage 如何发布，跨 SWE-agent/MLGym
    之外的 harness 后，能力增益还剩多少？
24. Cascade RL 的 stage order 如何以 compute-matched regression suite 决定；MOPD teacher selection、
    reverse-KL 与 rollback 如何避免把 benchmark-selected specialist bias 固化进统一 policy？
25. Memento-Skills 如何治理自动 rewrite 的 supply-chain、版本冲突、退化检测、tenant isolation 与 selective
    rollback，且 router/judge 不共享同一偏差？
26. ASM 在跨 session、动态 UI 和并发 workflow 中如何维护 anchor evidence、causal link、invalidation 与
    delete propagation，而不把 derived memory 升级为 authoritative state？
27. ProRL Agent 的跨阶段 job、policy/backend version 与 cancel race 如何形成可恢复的 exactly-once 或
    明确 at-least-once contract，且报错 rollout exclusion 是否改变 policy distribution？
28. on-policy LM-as-RM 如何避免 teacher、reward model 与 policy 共同放大 correlated bias；复杂数学对象
    equivalence 的 false accept/false reject 怎样由独立专家证据校准？
29. Hyperagents 的 outer-loop evaluator、task distribution 与 parent selection 若也允许修改，谁拥有不可变
    safety boundary、budget、holdout 与 rollback authority？
30. λ-RLM 在未知 task topology、dynamic branching 与 external side effects 下怎样安全扩展 typed library，
    又不退化回 unrestricted model-authored control flow？
31. AgentDS 的 baseline sandbox、tool image、per-challenge artifact 与跨年份复测能否形成稳定的 system
    evaluation contract，而不是依赖当届 participant-pool quantile？
32. OpenResearcher 的 answer-guided corpus support 如何审计 benchmark leakage，并把 index build/storage/
    serving 成本、freshness 与 deletion 纳入所谓 offline deterministic environment？
33. BubbleRAG 在 KG 更新、edge deletion 与 per-tenant authorization 后，怎样保持 evidence subgraph 连通性
    和 source provenance，而不把连接性误当真实性？
34. HopChain 能否公开 per-hop grounding verifier、完整训练 contract 与失败切片，以区分 dependency learning、
    segmentation bias 和单纯增加 synthetic difficulty？
35. DSX Air 的 simulation fidelity、scenario coverage 与 real-world calibration error 是否会公开，避免
    “可仿真”被误写成“可预测生产 SLO”？
36. Dynamo standalone index 的 event gap replay、tenant isolation 与 rebuild fallback 在 stable release 中
    是否保持同一 contract？
37. Trainer v2.2 的 manager-key patch ownership 如何处理 field conflict、orphan manager、attempt restart 和
    status metric staleness；各 runtime 的 capability matrix 是否能机器校验？

## Sources

- Wadlom et al., “Efficient LLM Serving for Agentic Workflows,” submitted 2026-03-17:
  https://arxiv.org/abs/2603.16104
- OpenAI, “Introducing GPT-5.4 mini and nano,” published 2026-03-17:
  https://openai.com/index/introducing-gpt-5-4-mini-and-nano/
- Anthropic Research index, user study dated 2026-03-18:
  https://www.anthropic.com/research
- Moonshot AI, “Attention Residuals,” first-public 2026-03-16；arXiv record、21-page PDF 与官方
  repository，访问 2026-08-09:
  https://arxiv.org/abs/2603.15031
  https://arxiv.org/pdf/2603.15031
  https://github.com/MoonshotAI/Attention-Residuals
- PolarSeeker, “OpenSeeker,” first-public 2026-03-16；arXiv HTML、官方 repository、dataset 与 model
  artifact，访问 2026-08-09:
  https://arxiv.org/abs/2603.15594
  https://arxiv.org/html/2603.15594v1
  https://github.com/PolarSeeker/OpenSeeker
  https://huggingface.co/datasets/PolarSeeker/OpenSeeker-v1-Data
  https://huggingface.co/PolarSeeker/OpenSeeker-v1-30B-SFT
- ByteDance Seed / HUST Vision Lab, “Mixture-of-Depths Attention,” first-public 2026-03-16；arXiv
  record、18-page PDF 与官方 repository，访问 2026-08-09:
  https://arxiv.org/abs/2603.15619
  https://arxiv.org/pdf/2603.15619
  https://github.com/hustvl/MoDA
- “POLCA,” first-public 2026-03-16；55-page official PDF 与官方 repository，访问 2026-08-09:
  https://arxiv.org/abs/2603.14769
  https://arxiv.org/pdf/2603.14769v1
  https://github.com/rlx-lab/POLCA
- “The PokeAgent Challenge,” first-public 2026-03-16；arXiv HTML 与官方 challenge site，访问
  2026-08-09:
  https://arxiv.org/abs/2603.15563
  https://arxiv.org/html/2603.15563v1
  https://pokeagentchallenge.com/
- ZJU-REAL, “Code-A1,” first-public 2026-03-16；arXiv HTML、官方 project page 与 repository，访问
  2026-08-09:
  https://arxiv.org/abs/2603.15611
  https://arxiv.org/html/2603.15611v1
  https://zju-real.github.io/Code-A1/
  https://github.com/ZJU-REAL/Code-A1
- “HorizonMath,” first-public 2026-03-16:
  https://arxiv.org/abs/2603.15617
  https://arxiv.org/html/2603.15617v1
  https://github.com/ewang26/HorizonMath
- MiroMind, “MiroThinker-1.7 & H1,” first-public 2026-03-16:
  https://arxiv.org/abs/2603.15726
  https://arxiv.org/pdf/2603.15726v1
  https://github.com/MiroMindAI/MiroThinker
  https://huggingface.co/miromind-ai/MiroThinker-1.7
- “SWE-Skills-Bench,” first-public 2026-03-16:
  https://arxiv.org/abs/2603.15401
  https://arxiv.org/html/2603.15401v1
  https://github.com/GeniusHTX/SWE-Skills-Bench
- “FlashSampling,” first-public 2026-03-16:
  https://arxiv.org/abs/2603.15854
  https://arxiv.org/html/2603.15854v1
  https://github.com/FlashSampling/FlashSampling
  https://github.com/FlashSampling/FlashSampling/blob/main/REPRODUCTION.md
- “VTC-Bench,” first-public 2026-03-16:
  https://arxiv.org/abs/2603.15030
  https://arxiv.org/html/2603.15030v1
  https://github.com/zhuzil/VTC-Bench
  https://huggingface.co/datasets/zzzhu/VTC-Bench/tree/main
- Microsoft Research, “Online Experiential Learning for Language Models,” first-public 2026-03-17:
  https://arxiv.org/abs/2603.16856
  https://arxiv.org/html/2603.16856v1
  https://github.com/microsoft/LMOps/tree/main/oel
- “TRUST-SQL,” first-public 2026-03-17:
  https://arxiv.org/abs/2603.16448
  https://arxiv.org/html/2603.16448v1
  https://anonymous.4open.science/r/TrustSQL-0902
- Qualcomm, “Efficient Reasoning on the Edge,” first-public 2026-03-17:
  https://arxiv.org/abs/2603.16867
  https://arxiv.org/pdf/2603.16867v1
  https://qualcomm-ai-research.github.io/llm-reasoning-on-edge/
- “MetaClaw,” first-public 2026-03-17:
  https://arxiv.org/abs/2603.17187
  https://arxiv.org/html/2603.17187v1
  https://github.com/aiming-lab/MetaClaw
- “BenchPreS,” first-public 2026-03-17:
  https://arxiv.org/abs/2603.16557
  https://arxiv.org/html/2603.16557v1
  https://huggingface.co/datasets/sangyon/BenchPreS
- “AdaMem,” first-public 2026-03-17:
  https://arxiv.org/abs/2603.16496
  https://arxiv.org/html/2603.16496v1
- “AI Scientist via Synthetic Task Scaling,” first-public 2026-03-17:
  https://arxiv.org/abs/2603.17216
  https://arxiv.org/pdf/2603.17216
- “PRISM,” first-public 2026-03-17:
  https://arxiv.org/abs/2603.17074
  https://arxiv.org/html/2603.17074v1
  https://bharat-runwal.github.io/PRISM/
  https://huggingface.co/PRISM-Midtraining
  https://github.com/allenai/open-instruct/tree/main
- Qwen, “HopChain,” first-public 2026-03-17:
  https://arxiv.org/abs/2603.17024
  https://arxiv.org/html/2603.17024v1
  https://arxiv.org/pdf/2603.17024
- “Astrolabe,” first-public 2026-03-17:
  https://arxiv.org/abs/2603.17051
  https://franklinz233.github.io/projects/astrolabe/
  https://github.com/franklinz233/Astrolabe
- “OpenResearcher,” first-public 2026-03-17:
  https://arxiv.org/abs/2603.20278
  https://arxiv.org/html/2603.20278v1
  https://github.com/TIGER-AI-Lab/OpenResearcher
- “Complementary Reinforcement Learning,” first-public 2026-03-18:
  https://arxiv.org/abs/2603.17621
  https://arxiv.org/html/2603.17621v1
  https://github.com/alibaba/ROLL
- Google, “Efficient Exploration at Scale,” first-public 2026-03-18:
  https://arxiv.org/abs/2603.17378
  https://arxiv.org/html/2603.17378v1
- Qualcomm, “Efficient Training-Free Multi-Token Prediction,” first-public 2026-03-18:
  https://arxiv.org/abs/2603.17942
  https://arxiv.org/html/2603.17942v1
- “RAMP,” first-public 2026-03-18:
  https://arxiv.org/abs/2603.17891
  https://arxiv.org/html/2603.17891v1
- NVIDIA, “Nemotron-Cascade 2,” first-public 2026-03-19:
  https://arxiv.org/abs/2603.19220
  https://arxiv.org/pdf/2603.19220
  https://huggingface.co/collections/nvidia/nemotron-cascade-2
  https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B
- “Memento-Skills,” first-public 2026-03-19:
  https://arxiv.org/abs/2603.18743
  https://arxiv.org/pdf/2603.18743
  https://github.com/Memento-Teams/Memento-Skills
  https://skills.memento.run/market/
- “AndroTMem,” first-public 2026-03-19:
  https://arxiv.org/abs/2603.18429
  https://arxiv.org/html/2603.18429v1
  https://github.com/CVC2233/AndroTMem
- NVIDIA, “ProRL Agent,” first-public 2026-03-19:
  https://arxiv.org/abs/2603.18815
  https://arxiv.org/html/2603.18815v1
  https://github.com/NVIDIA-NeMo/ProRL-Agent-Server
- Meta, “Reasoning over mathematical objects,” first-public 2026-03-19:
  https://arxiv.org/abs/2603.18886
  https://arxiv.org/pdf/2603.18886
  https://huggingface.co/datasets/facebook/principia-collection
  https://huggingface.co/datasets/facebook/principia-bench
- “Hyperagents,” first-public 2026-03-19:
  https://arxiv.org/abs/2603.19461
  https://arxiv.org/pdf/2603.19461
  https://github.com/facebookresearch/Hyperagents
- “AgentDS Technical Report,” first-public 2026-03-19:
  https://arxiv.org/abs/2603.19005
  https://arxiv.org/html/2603.19005v1
  https://agentds.org/
- “BubbleRAG,” first-public 2026-03-19:
  https://arxiv.org/abs/2603.20309
  https://arxiv.org/pdf/2603.20309
- “The Y-Combinator for LLMs,” first-public 2026-03-20:
  https://arxiv.org/abs/2603.20105
  https://arxiv.org/html/2603.20105v1
- Google DeepMind, “A Subgoal-driven Framework for Improving Long-Horizon LLM Agents,” first-public
  2026-03-20:
  https://arxiv.org/abs/2603.19685
  https://arxiv.org/html/2603.19685v1
- “LoopRPT,” first-public 2026-03-20:
  https://arxiv.org/abs/2603.19714
  https://arxiv.org/pdf/2603.19714
- “BEAVER,” first-public 2026-03-20:
  https://arxiv.org/abs/2603.19635
  https://arxiv.org/html/2603.19635v1
- “Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States,” first-public
  2026-03-20:
  https://arxiv.org/abs/2603.19987
  https://arxiv.org/html/2603.19987v1
- NVIDIA, “NVIDIA Vera Rubin Platform,” published 2026-03-16；official announcement、platform、
  developer technical article 与 NVLink specification，访问 2026-08-09：
  https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform
  https://www.nvidia.com/en-us/data-center/technologies/rubin/
  https://developer.nvidia.com/blog/?p=113993
  https://www.nvidia.com/en-us/data-center/nvlink/
- NVIDIA, “Design, Simulate, and Scale AI Factory Infrastructure with NVIDIA DSX Air,” published
  2026-03-16，访问 2026-08-09：
  https://developer.nvidia.com/blog/design-simulate-and-scale-ai-factory-infrastructure-with-nvidia-dsx-air/
- NVIDIA Dynamo release history / v1.0 documentation / GitHub releases，v1.0.1 published
  2026-03-16、v1.1.0-dev.1 published 2026-03-17，访问 2026-08-09：
  https://docs.nvidia.com/dynamo/dev/reference/releases/release-history
  https://docs.nvidia.com/dynamo/dev/reference/releases/v1-0-0
  https://github.com/ai-dynamo/dynamo/releases
- Kubeflow Community Distribution 26.03, released 2026-03-22，访问 2026-08-09：
  https://www.kubeflow.org/docs/kubeflow-distribution/releases/kubeflow-26.03/
- Kubeflow, “Kubeflow Trainer v2.2 Release,” published 2026-03-20；official release，访问
  2026-08-09：
  https://blog.kubeflow.org/kubeflow-trainer-v2.2-release/
  https://github.com/kubeflow/trainer/releases/tag/v2.2.0
- Kubeflow, “Kubeflow SDK 0.4.0 Release,” published 2026-03-19，访问 2026-08-09：
  https://blog.kubeflow.org/kubeflow-sdk-0.4.0-release/
- KServe v0.17.0 official release, published 2026-03-13（W11 spillback；未计入 W12）：
  https://github.com/kserve/kserve/releases/tag/v0.17.0
- vLLM PR #37190, “Run MoE models exceeding VRAM via expert CPU offloading with GPU cache,”
  first-public 2026-03-16；open PR，访问 2026-08-11：
  https://github.com/vllm-project/vllm/pull/37190
- vLLM RFC #38256, “Incremental MoE Expert Offloading — GPU Cache + Async Pipeline,”
  published 2026-03-26（W13 architecture-evolution node；未在 W12 重复计分），访问 2026-08-11：
  https://github.com/vllm-project/vllm/issues/38256
