# AI Research Weekly — 2025-W37

> Coverage Window: 2025-09-08～2025-09-14
> Research Mode: Full Historical Discovery Replay and Primary-Source Reconciliation
> Initial Archive Accessed: 2026-07-31
> Discovery Replay and Primary-source Re-audit: 2026-08-24
> Audit Status: Candidate Evidence Gate Passed — 54/54 Scored, 37/37 Retained Full Source Review, 17/17 Low-score Closure, Review Pending 0
> Discovery / Archive Gate: Conditional — fixed-source replay complete; immutable Scholar/OpenAlex export unavailable
> Historical Books Gate: Closed — Weekly evidence only

## Executive Summary

旧版只有Qwen3-Next 1项，是discovery seed。重放后建立54个canonical owners：19个25～30分、18个20～24分、17个低于20分；37/37 retained owners完成Full Source Review，17/17低分完成identity/date/score/rejection closure，ordinary `Review Pending = 0`。

主线是：异构/长时RL从同步权重扩展到带provenance的rollout；多模态与embodied从共享latent走向按任务选择state并向物理controller交接；runtime从本地计算走向checkpoint/collective/PD state-transfer contract。作者benchmark只在公开workload内成立。

## Coverage Window and Limitations

- ISO Monday 2025-09-08至Sunday 2025-09-14；论文按arXiv v1、release按first-public归周。
- 固定顺序重放模型机构→arXiv/学术→AI Infra；Hugging Face Daily Papers只作discovery，结论回到primary source。
- later revision不重复计分。9个W36 family只在下方spillback ledger记录，本周不计分；其中4项在W37窗口出现revision，但owner仍按v1回拨W36。
- Scholar/OpenAlex/DBLP/Crossref的immutable export本轮不可取得，故Candidate Evidence Gate可通过，年度Discovery/Archive Gate仍Conditional。
- 未披露hardware/model/precision/length/batch/concurrency/SLO不补猜。

## Source Coverage

### 模型与研究机构

- Qwen3-Next是本周official architecture owner。
- SafetyKit和Veo 3 GA只有case/availability事实，低分closure；不反推内部机制。

### 论文与学术

- 46个academic owners；33个达到20+并完成全文packet，13个低分closure。
- 重点覆盖RL/Agent、multimodal/VLA、evaluation/security。

### AI Infra

- PyTorch Distributed Checkpoint、native XCCL、PyTorch-vLLM disaggregated inference完成机制审计。
- SGLang 0.5.2与vLLM 0.10.2确认artifact/date/hash但缺机制contract，按Version Fact闭合。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Qwen3-Next | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Core Candidate — Full Source Review Complete |
| SAPO collective RL experience sharing | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Core Candidate — Full Source Review Complete |
| WebExplorer | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Core Candidate — Full Source Review Complete |
| Paper2Agent | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Core Candidate — Full Source Review Complete |
| SFR-DeepResearch | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Retained — Full Source Review Complete |
| AgentGym-RL | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Core Candidate — Full Source Review Complete |
| CDE curiosity-driven RL | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Core Candidate — Full Source Review Complete |
| Parallel-R1 | 4 | 4 | 3 | 5 | 4 | 3 | 23/30 | Retained — Full Source Review Complete |
| Visual Representation Alignment | 4 | 3 | 3 | 5 | 4 | 3 | 22/30 | Retained — Full Source Review Complete |
| Mini-o3 visual search | 4 | 4 | 3 | 5 | 4 | 3 | 23/30 | Retained — Full Source Review Complete |
| Reconstruction Alignment | 4 | 3 | 3 | 5 | 4 | 3 | 22/30 | Retained — Full Source Review Complete |
| F1 VLA | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Core Candidate — Full Source Review Complete |
| Language Self-Play | 4 | 3 | 4 | 5 | 4 | 3 | 23/30 | Retained — Full Source Review Complete |
| Causal Attention with Lookahead Keys | 4 | 4 | 3 | 5 | 5 | 3 | 24/30 | Retained — Full Source Review Complete |
| SimpleQA Verified | 3 | 4 | 4 | 5 | 5 | 4 | 25/30 | Core Candidate — Full Source Review Complete |
| RewardDance | 4 | 3 | 3 | 5 | 4 | 3 | 22/30 | Retained — Full Source Review Complete |
| HuMo | 4 | 3 | 4 | 5 | 4 | 3 | 23/30 | Retained — Full Source Review Complete |
| EchoX | 4 | 3 | 4 | 5 | 4 | 3 | 23/30 | Retained — Full Source Review Complete |
| Entropy-Modulated Policy Gradients | 4 | 4 | 3 | 5 | 4 | 3 | 23/30 | Retained — Full Source Review Complete |
| VLA-Adapter | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Core Candidate — Full Source Review Complete |
| SimpleVLA-RL | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Core Candidate — Full Source Review Complete |
| OmniEVA | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Core Candidate — Full Source Review Complete |
| LoCoBench | 3 | 4 | 4 | 5 | 5 | 4 | 25/30 | Core Candidate — Full Source Review Complete |
| Understanding-Generation Coexistence | 4 | 3 | 3 | 5 | 4 | 4 | 23/30 | Retained — Full Source Review Complete |
| SpatialVID | 3 | 3 | 4 | 5 | 4 | 4 | 23/30 | Retained — Full Source Review Complete |
| Reverse-Engineered Reasoning | 4 | 3 | 3 | 5 | 4 | 3 | 22/30 | Retained — Full Source Review Complete |
| dLLM RL framework | 4 | 4 | 3 | 5 | 4 | 3 | 23/30 | Retained — Full Source Review Complete |
| UniVerse-1 | 4 | 3 | 4 | 5 | 4 | 3 | 23/30 | Retained — Full Source Review Complete |
| Off-policy RL + multi-agent tree search step-provers | 4 | 4 | 3 | 5 | 4 | 3 | 23/30 | Retained — Full Source Review Complete |
| Guided Decoding for RAG | 3 | 4 | 4 | 5 | 5 | 4 | 25/30 | Core Candidate — Full Source Review Complete |
| Test-Time Scaling on Knowledge-Intensive Tasks | 3 | 4 | 4 | 5 | 5 | 4 | 25/30 | Core Candidate — Full Source Review Complete |
| MachineLearningLM | 4 | 3 | 3 | 5 | 4 | 4 | 23/30 | Retained — Full Source Review Complete |
| AU-Harness | 3 | 4 | 5 | 5 | 5 | 4 | 26/30 | Core Candidate — Full Source Review Complete |
| Reasoning poisoning attacks | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Core Candidate — Full Source Review Complete |
| PyTorch Distributed Checkpoint | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Core Candidate — Full Source Review Complete |
| PyTorch native XCCL | 3 | 5 | 5 | 5 | 5 | 4 | 27/30 | Core Candidate — Full Source Review Complete |
| PyTorch-vLLM disaggregated inference | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Core Candidate — Full Source Review Complete |
| MAS-Bench | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Low-score Closure |
| Interleaving Reasoning for Text-to-Image | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Low-score Closure |
| Kling-Avatar | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Low-score Closure |
| mmBERT | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Low-score Closure |
| FLUX-Reason-6M / PRISM-Bench | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Low-score Closure |
| EnvX | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Archive Only — Low-score Closure |
| HumanAgencyBench | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Low-score Closure |
| RL for Deep Research survey | 2 | 3 | 3 | 5 | 3 | 2 | 18/30 | Archive Only — Low-score Closure |
| RL for Large Reasoning Models survey | 2 | 3 | 3 | 5 | 3 | 2 | 18/30 | Archive Only — Low-score Closure |
| 3D and 4D World Modeling survey | 2 | 3 | 3 | 5 | 3 | 2 | 18/30 | Archive Only — Low-score Closure |
| Fuzzing Brain | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Low-score Closure |
| Capability-Adaptive Hint Scaffolding | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Low-score Closure |
| RLVR divergence choice | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Archive Only — Low-score Closure |
| vLLM 0.10.2 | 2 | 3 | 4 | 5 | 3 | 2 | 19/30 | Archive Only — Low-score Closure |
| SGLang 0.5.2 | 2 | 3 | 4 | 5 | 3 | 2 | 19/30 | Archive Only — Low-score Closure |
| SafetyKit GPT-5 case study | 1 | 3 | 3 | 4 | 3 | 2 | 16/30 | Archive Only — Low-score Closure |
| Veo 3 Vertex AI GA | 1 | 2 | 3 | 5 | 2 | 2 | 15/30 | Archive Only — Low-score Closure |

## Deep Analysis

### RL state：weight synchronization → provenance-bearing experience flow

集中式single-policy RL在同构可信集群易维护on-policy语义；异构易失节点下，强同步扩大延迟和故障域。SAPO改为decoded rollout exchange，各节点本地过滤/重编码/更新，获得异步性，也把trust、staleness、verifier compatibility和poisoning提升为correctness state。WebExplorer、AgentGym-RL和step-prover进一步要求environment/tool/terminal verifier/replay identity共同归档。两条路线按trust与staleness边界共存。

### Multimodal state：shared latent → task-conditioned state → physical handoff

alignment/reconstruction先解决shared latent能否服务理解/生成；VLA-Adapter、F1、SimpleVLA-RL和OmniEVA把约束推进到action。task-conditioned 2D/3D gate说明“更多state”不必更好；高层plan也不等于实时control。收益伴随calibration、sim-to-real、unsafe exploration、control frequency和rollback。

### Runtime state：local compute → commit/migrate/recover protocol

Distributed Checkpoint分离logical state与physical shard；XCCL把backend纳入统一collective contract；PD把KV变成跨pool transfer state。收益是reshard、portability与独立扩缩；代价是manifest atomicity、backend skew、KV freshness、backpressure和failure recovery。

## Full Source Review

### Qwen3-Next

- **Candidate / Week / Score:** Qwen3-Next / 2025-W37 / 27/30；**Source Family / Type:** `QWEN3-NEXT-2025-09` / Official model release。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-10；later revisions同family不重复评分。Direct: official blog/model card/config；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Official artifact packet complete：通读model card、config、architecture/evaluation sections及linked repository surface；未公开独立technical report/system card，因此不存在的paper sections记为Not Disclosed，不反推。
- **Problem / Previous Design / Changed Constraint:** dense attention与dense FFN使容量、上下文和active FLOPs同时增长；成熟dense/GQA在短上下文和backend覆盖优先时仍合理。
- **Mechanism / Ownership / Flow / Implementation:** 48层按3个Gated DeltaNet+1个Gated Attention分组，高稀疏MoE与MTP共同形成model/runtime contract；模型拥有recurrent/KV/router state，engine负责TP/EP、cache与verification。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 官方公开80B total/3B active、262K native context、YaRN扩展；吞吐与1M RULER缺完整GPU/precision/batch/concurrency/SLO contract。
- **Proves / Does Not Prove:** 证明hybrid recurrent/attention、MoE与MTP可组合；不证明10x吞吐跨硬件或1M等于有效利用。
- **Trade-offs / Failure Modes / Old-design Boundary:** 降低active compute却新增recurrent state、routing、kernel coverage、MTP acceptance与rollback；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MODEL-LONG-CONTEXT / Ch22 / Legacy Ch22；handoff MODEL-MOE、INFER-DECODE。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。DeltaNet rollback、EP topology、MTP acceptance。

### SAPO collective RL experience sharing

- **Candidate / Week / Score:** SAPO collective RL experience sharing / 2025-W37 / 28/30；**Source Family / Type:** `ARXIV-2509.08721` / Research paper + artifact。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-10；later revisions同family不重复评分。Direct: arXiv v1 + GenRL/RLSwarm artifact；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Paper + artifact complete；通读metadata、Introduction/Related Work、collective experience-sharing algorithm、implementation、8-node/1000-node evaluation、ratio ablation、limitations和artifact surface。
- **Problem / Previous Design / Changed Constraint:** 同步权重的集中式RL在异构易失节点受通信拖累；可信同构集群的单policy仍更易审计。
- **Mechanism / Ownership / Flow / Implementation:** 节点广播decoded question/answer/rollout/verifier metadata，本地过滤重编码后用本地reward与GRPO/PPO更新；节点拥有policy/reward/filter，swarm只传经验。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8个Qwen2.5-0.5B、ReasoningGym、2000 rounds比较8/0至2/6；4/4累积reward高94%，千节点demo对Qwen2.5有效但Qwen3-0.6B不显著。
- **Proves / Does Not Prove:** 证明受控小模型可受益且外部占比过高会振荡；不证明恶意节点、隐私或大模型扩展。
- **Trade-offs / Failure Modes / Old-design Boundary:** 省权重同步却新增provenance、poisoning、verifier compatibility、off-policy drift；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；TRAIN-GRPO / Ch33 / Legacy Ch29；handoff TRAIN-DISTRIBUTED-TRAINING。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。attestation、staleness bound、privacy与filtering。

### WebExplorer

- **Candidate / Week / Score:** WebExplorer / 2025-W37 / 26/30；**Source Family / Type:** `ARXIV-2509.06501` / Research paper + artifact。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-08；later revisions同family不重复评分。Direct: arXiv v1 + code/data；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Paper + artifact complete；通读implicit web-space exploration、long-to-short query construction、SFT/GRPO implementation、six-benchmark evaluation、trajectory statistics、ablation、limitations与code/data surface。
- **Problem / Previous Design / Changed Constraint:** web-agent缺长链高难QA；人工或显式图构建昂贵且规则脆弱。
- **Mechanism / Ownership / Flow / Implementation:** 模型search/browse探索隐式信息空间，再以long-to-short clue removal生成难query；Qwen3-8B先SFT再GRPO到128K和100 tool turns。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** BrowseComp、GAIA、WebWalkerQA、FRAMES、XBench、HLE及trajectory/tool schema；作者报告平均约16 turns。
- **Proves / Does Not Prove:** 证明data curriculum能把检索长度变训练变量；不证明网页freshness、污染与真实任务可靠性。
- **Trade-offs / Failure Modes / Old-design Boundary:** 扩大探索却放大browsing cost、环境漂移、citation/provenance与verifier leakage；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；AGENT-WORKFLOW / Ch81 / Legacy Ch77；handoff TRAIN-DATA、AGENT-TOOL-CALLING。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。snapshot identity、failure injection、reward hacking。

### Paper2Agent

- **Candidate / Week / Score:** Paper2Agent / 2025-W37 / 26/30；**Source Family / Type:** `ARXIV-2509.06917` / Research paper + artifact。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-09；later revisions同family不重复评分。Direct: arXiv v1 + paper-to-agent code；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Paper + artifact complete；通读paper/code/data ingestion、MCP-style wrapping与schema flow、case-study evaluation、baseline/error analysis、limitations和repository surface。
- **Problem / Previous Design / Changed Constraint:** 论文方法停留在prose/PDF，手工复现易丢参数契约；自由解释又可能偏离原方法。
- **Mechanism / Ownership / Flow / Implementation:** 论文、代码、数据被转成MCP-style callable agent/tool，保留schema、execution trace和artifact version。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 多篇科学论文评估wrapper可执行性与答案质量并比较manual workflow；公开repository可审计。
- **Proves / Does Not Prove:** 证明论文可包装为可执行接口；不证明自动wrapper在未见环境或未来revision可靠。
- **Trade-offs / Failure Modes / Old-design Boundary:** 降低门槛却新增wrapper drift、dependency pinning、sandbox与result provenance；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；AGENT-TOOL-CALLING / Ch78 / Legacy Ch74；handoff AGENT-MCP、AGENT-WORKFLOW。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。wrapper-paper语义等价、rollback和副作用审计。

### SFR-DeepResearch

- **Candidate / Week / Score:** SFR-DeepResearch / 2025-W37 / 24/30；**Source Family / Type:** `ARXIV-2509.06283` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-08；later revisions同family不重复评分。Direct: arXiv v1 + model/code；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** deep-research需要跨多轮搜索维持策略，短轨迹SFT难优化信息价值和停止。
- **Mechanism / Ownership / Flow / Implementation:** single-agent policy交替reasoning与search/browse，context持trajectory、environment持observation、evaluator持终局reward。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** BrowseComp、GAIA等research benchmark与open/proprietary baselines；tool contract和rollout length披露。
- **Proves / Does Not Prove:** 证明长轨迹RL是multi-agent之外的有效分支；不证明benchmark harness等同开放网络。
- **Trade-offs / Failure Modes / Old-design Boundary:** 减少communication tax但扩大context、credit assignment、tool error和停止失败；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；AGENT-WORKFLOW / Ch81 / Legacy Ch77；handoff TRAIN-RLHF。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。truncation、search freshness、citation verifier。

### AgentGym-RL

- **Candidate / Week / Score:** AgentGym-RL / 2025-W37 / 27/30；**Source Family / Type:** `ARXIV-2509.08755` / Research paper + environments。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-10；later revisions同family不重复评分。Direct: arXiv v1 + AgentGym environments；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** one-turn RL不覆盖长时环境转移、错误恢复和跨turn credit。
- **Mechanism / Ownership / Flow / Implementation:** 统一interactive environments与multi-turn rollout；environment拥有state transition，policy拥有action proposal，trainer拥有trajectory/reward batching。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 跨web/tool/game environments与SFT/RL baselines，含length和training ablation。
- **Proves / Does Not Prove:** 证明多环境长时训练提升一组benchmark；不证明reward scale可直接合并或真实副作用安全。
- **Trade-offs / Failure Modes / Old-design Boundary:** 多样性换更强policy，但增加simulator fidelity、reward normalization、reset/rollback风险；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；AGENT-PLATFORM / Ch84 / Legacy Ch80；handoff AGENT-WORKFLOW、TRAIN-RLHF。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。environment identity、replay、reward calibration。

### CDE curiosity-driven RL

- **Candidate / Week / Score:** CDE curiosity-driven RL / 2025-W37 / 25/30；**Source Family / Type:** `ARXIV-2509.09675` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-11；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** RLVR反复采样已掌握题目，昂贵rollout未覆盖能力边界。
- **Mechanism / Ownership / Flow / Implementation:** 用表现/不确定性驱动task sampling，把budget移向learning-progress区域；sampler拥有curriculum state。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 数学/推理模型与uniform/difficulty baselines及exploration ablation。
- **Proves / Does Not Prove:** 证明adaptive curriculum减少作者任务无效rollout；不证明proxy在开放任务校准。
- **Trade-offs / Failure Modes / Old-design Boundary:** 提高利用率却新增sampler bias、feedback loop、coverage debt；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；TRAIN-GRPO / Ch33 / Legacy Ch29；handoff TRAIN-DATA。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。coverage guardrail、OOD discovery、calibration。

### Parallel-R1

- **Candidate / Week / Score:** Parallel-R1 / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.07980` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-10；later revisions同family不重复评分。Direct: arXiv v1 + code；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 串行CoT把深度绑定latency且难回退；小预算串行仍简单。
- **Mechanism / Ownership / Flow / Implementation:** RL训练结构化并行分支与聚合；policy拥有branches，runtime拥有branch scheduling/merge。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** reasoning benchmarks与serial CoT/sampling baselines，含branch/reward sensitivity但缺真实SLO。
- **Proves / Does Not Prove:** 证明并行reasoning可学；不证明wall-clock更低或branches独立。
- **Trade-offs / Failure Modes / Old-design Boundary:** 增加覆盖也增加token/compute、branch correlation、aggregation error；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；TRAIN-GRPO / Ch33 / Legacy Ch29；handoff INFER-SCHEDULING。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。diversity、concurrency/SLO、early stop。

### Visual Representation Alignment

- **Candidate / Week / Score:** Visual Representation Alignment / 2025-W37 / 22/30；**Source Family / Type:** `ARXIV-2509.07979` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-10；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 视觉encoder token与语言latent错位，简单projector丢细节。
- **Mechanism / Ownership / Flow / Implementation:** 额外alignment objective/teacher signal约束视觉token进入LLM空间，保持encoder/projector/decoder边界。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 多MLLM backbone和视觉benchmark及alignment ablation；缺独立复现。
- **Proves / Does Not Prove:** 证明额外alignment在作者设置有效；不证明对所有modality普适。
- **Trade-offs / Failure Modes / Old-design Boundary:** 改善语义可读性但引入teacher bias、训练成本和细节压缩；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MULTIMODAL-REPRESENTATION / Ch23 / Legacy N/A。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。alignment metric与downstream utility。

### Mini-o3 visual search

- **Candidate / Week / Score:** Mini-o3 visual search / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.07969` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-10；later revisions同family不重复评分。Direct: arXiv v1 + artifact；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 视觉搜索需多次crop/observation，单次VLM不能分配sensing budget。
- **Mechanism / Ownership / Flow / Implementation:** agent交替reasoning、visual search action与observation；environment拥有image state，agent拥有query history。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** visual-search benchmark与VLM/agent baselines，含turn scaling；tool latency/error未完整披露。
- **Proves / Does Not Prove:** 证明有用交互而非仅更长文本能提高搜索；不证明无限turn单调获益。
- **Trade-offs / Failure Modes / Old-design Boundary:** 获得主动感知但新增query budget、observation drift、tool failure；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；AGENT-WORKFLOW / Ch81 / Legacy Ch77；handoff MULTIMODAL-REPRESENTATION。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。turn value、tool latency、stop policy。

### Reconstruction Alignment

- **Candidate / Week / Score:** Reconstruction Alignment / 2025-W37 / 22/30；**Source Family / Type:** `ARXIV-2509.07295` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-09；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 统一理解/生成共享latent时生成目标可能丢理解细节。
- **Mechanism / Ownership / Flow / Implementation:** 加入reconstruction-alignment信号使shared representation保持可恢复，head仅作训练约束。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 统一多模态理解/生成指标与single-task/joint ablation。
- **Proves / Does Not Prove:** 证明reconstruction是缓解objective interference的一个branch；不证明天然协同。
- **Trade-offs / Failure Modes / Old-design Boundary:** 提高保真但增加compute、decoder bias与loss-weight tuning；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MULTIMODAL-GENERATIVE-PARADIGMS / Ch24 / Legacy N/A；handoff MULTIMODAL-REPRESENTATION。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。reconstruction与semantic abstraction冲突。

### F1 VLA

- **Candidate / Week / Score:** F1 VLA / 2025-W37 / 26/30；**Source Family / Type:** `ARXIV-2509.06951` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-09；later revisions同family不重复评分。Direct: arXiv v1 + project；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** VLM理解token与action policy分离，generation知识不能直接约束控制。
- **Mechanism / Ownership / Flow / Implementation:** 统一理解/生成表示并以action head/flow policy映射动作；model拥有semantic state，controller拥有real-time execution。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** simulation/robot benchmarks与understanding/generation/action baselines；控制频率与safety仅覆盖作者平台。
- **Proves / Does Not Prove:** 证明共享表征可支持VLA；不证明视频质量等同物理可执行。
- **Trade-offs / Failure Modes / Old-design Boundary:** 共享知识但增加objective interference、latency、calibration与failure propagation；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MULTIMODAL-EMBODIED-VLA / Ch26 / Legacy N/A。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。control frequency、override、sim-to-real、rollback。

### Language Self-Play

- **Candidate / Week / Score:** Language Self-Play / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.07414` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-09；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 监督数据耗尽时自生成易确认偏差。
- **Mechanism / Ownership / Flow / Implementation:** 模型以producer/solver或challenger/respondent角色生成task/response，再用verifier构造data-free loop。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 语言/推理benchmarks、外部数据与self-play baselines，含过滤/迭代。
- **Proves / Does Not Prove:** 证明受约束self-play可扩充信号；不证明truly data-free或长期不塌缩。
- **Trade-offs / Failure Modes / Old-design Boundary:** 减少标注但引入collapse、self-confirmation、novelty debt；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；TRAIN-DATA / Ch27 / Legacy Ch23；handoff TRAIN-PRETRAINING。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。provenance、novelty-quality gate。

### Causal Attention with Lookahead Keys

- **Candidate / Week / Score:** Causal Attention with Lookahead Keys / 2025-W37 / 24/30；**Source Family / Type:** `ARXIV-2509.07301` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-09；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 严格causal attention只能用历史key，局部未来结构需更多层间接传播。
- **Mechanism / Ownership / Flow / Implementation:** 在不泄漏target的约束下构造lookahead key；model定义mask/state，runtime须保持dependency。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** LM和下游任务与standard causal attention、lookahead depth ablation；缺kernel/KV contract。
- **Proves / Does Not Prove:** 证明扩展causal dependency的architecture branch；不证明KV cache无成本支持。
- **Trade-offs / Failure Modes / Old-design Boundary:** 增强规划却新增mask correctness、train/infer skew、cache identity；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MODEL-SELF-ATTENTION / Ch14 / Legacy Ch14；handoff INFER-KV-CACHE。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。incremental decode commit/rollback。

### SimpleQA Verified

- **Candidate / Week / Score:** SimpleQA Verified / 2025-W37 / 25/30；**Source Family / Type:** `ARXIV-2509.07968` / Benchmark paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-10；later revisions同family不重复评分。Direct: arXiv v1 + verified dataset；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 答案歧义/过时/grader不稳会把数据错误当hallucination。
- **Mechanism / Ownership / Flow / Implementation:** 对items多阶段验证、去歧义和answerability control；dataset owner管理item/version，harness评分。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 多模型 factuality 与原版/verified set、人类/LLM grader agreement；只测短事实recall。
- **Proves / Does Not Prove:** 证明curation改变排名与confidence interpretation；不证明开放世界置信度。
- **Trade-offs / Failure Modes / Old-design Boundary:** 提升可靠性但缩窄覆盖、增加更新成本和temporal versioning；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；PLATFORM-EVALUATION-SYSTEM / Ch66 / Legacy Ch62。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。fact expiry、claim dependency、abstention scoring。

### RewardDance

- **Candidate / Week / Score:** RewardDance / 2025-W37 / 22/30；**Source Family / Type:** `ARXIV-2509.08826` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-11；later revisions同family不重复评分。Direct: arXiv v1 + reward artifact；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 视觉生成单一reward在prompt/style/quality与scale上偏置。
- **Mechanism / Ownership / Flow / Implementation:** 扩展多维visual reward data/model并用于post-training；reward owner分rubric，generator消费信号。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** image/video baselines、人类偏好与reward scaling ablation；evaluator与训练分布耦合。
- **Proves / Does Not Prove:** 证明reward capacity/data scaling改善作者任务；不证明score等同真实偏好。
- **Trade-offs / Failure Modes / Old-design Boundary:** 可训练反馈也带来Goodhart、维度权重和domain drift；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；PLATFORM-EVALUATION-SYSTEM / Ch66 / Legacy Ch62；handoff MULTIMODAL-GENERATIVE-PARADIGMS。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。held-out human audit、uncertainty。

### HuMo

- **Candidate / Week / Score:** HuMo / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.08519` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-10；later revisions同family不重复评分。Direct: arXiv v1 + project/code；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** text、identity image、audio缺成对数据，身份与lip-sync互扰。
- **Mechanism / Ownership / Flow / Implementation:** 两阶段progressive conditioning：minimal image injection、audio cross-attention+focus-by-predicting、time-adaptive CFG。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 人像视频子任务、统一条件与专用baselines及ablation；缺完整serving SLO。
- **Proves / Does Not Prove:** 证明staged conditioning缓解目标冲突；不证明跨人物/语言/长视频同步。
- **Trade-offs / Failure Modes / Old-design Boundary:** 灵活控制但增加triplet data、condition conflict、temporal drift；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MULTIMODAL-GENERATIVE-PARADIGMS / Ch24 / Legacy N/A。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。consent、long drift、timestamp identity。

### EchoX

- **Candidate / Week / Score:** EchoX / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.09174` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-11；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** speech-to-speech的acoustic与semantic token存在鸿沟。
- **Mechanism / Ownership / Flow / Implementation:** echo training用声学回声/重建信号对齐semantic space并保留端到端生成。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** speech understanding/generation benchmarks与echo ablation；语言/噪声/real-time覆盖有限。
- **Proves / Does Not Prove:** 证明auxiliary alignment在作者数据有效；不证明统一space无损。
- **Trade-offs / Failure Modes / Old-design Boundary:** 加强语义但可能抹平speaker/prosody并增加streaming state；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MULTIMODAL-REPRESENTATION / Ch23 / Legacy N/A。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。speaker identity、chunk boundary、多语鲁棒。

### Entropy-Modulated Policy Gradients

- **Candidate / Week / Score:** Entropy-Modulated Policy Gradients / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.09265` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-11；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 长时Agent所有action同权无法区分高不确定分叉。
- **Mechanism / Ownership / Flow / Implementation:** 用policy entropy调节trajectory/token gradient；trainer拥有modulation，environment reward定义目标。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 长时agent tasks与PPO/GRPO baselines、entropy ablation；entropy不等于epistemic uncertainty。
- **Proves / Does Not Prove:** 证明entropy可作优化权重；不证明高entropy就是有价值探索。
- **Trade-offs / Failure Modes / Old-design Boundary:** 改善credit却可能强化错误高熵区并放大reward noise；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；TRAIN-PPO / Ch32 / Legacy Ch28；handoff AGENT-WORKFLOW。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。calibration、off-policy correction、critical guardrail。

### VLA-Adapter

- **Candidate / Week / Score:** VLA-Adapter / 2025-W37 / 27/30；**Source Family / Type:** `ARXIV-2509.09372` / Research paper + artifact。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-11；later revisions同family不重复评分。Direct: arXiv v1 + code/models；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** VLA依赖大VLM与robot pretraining，门槛高；复杂open-world仍可能需要大backbone。
- **Mechanism / Ownership / Flow / Implementation:** 0.5B backbone+lightweight policy/Bridge Attention，选取VL condition注入action，无robot pretraining。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** LIBERO/真实机器人与ablation；作者称单consumer GPU 8小时但具体GPU/batch/SLO不可外推。
- **Proves / Does Not Prove:** 证明小模型+bridge在给定任务可竞争；不证明复杂场景/跨embodiment等价。
- **Trade-offs / Failure Modes / Old-design Boundary:** 降低compute却受adapter bottleneck、condition selection与shift影响；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MULTIMODAL-EMBODIED-VLA / Ch26 / Legacy N/A。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。control frequency、recovery、calibration。

### SimpleVLA-RL

- **Candidate / Week / Score:** SimpleVLA-RL / 2025-W37 / 26/30；**Source Family / Type:** `ARXIV-2509.09674` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-11；later revisions同family不重复评分。Direct: arXiv v1 + project；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** VLA imitation复制演示但难按执行结果修正，naive RL受sparse reward与rollout cost限制。
- **Mechanism / Ownership / Flow / Implementation:** 环境交互reward更新action generation；simulator拥有transition，policy拥有action chunks，trainer拥有advantage/rollback。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 机器人benchmark、SFT/RL baselines及reward/rollout ablation；真实安全和fidelity有限。
- **Proves / Does Not Prove:** 证明RL可超过imitation-only；不证明sim reward现实可靠或可无保护在线训练。
- **Trade-offs / Failure Modes / Old-design Boundary:** 获得correction却新增unsafe exploration、credit horizon、sample cost；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MULTIMODAL-EMBODIED-VLA / Ch26 / Legacy N/A；handoff TRAIN-RLHF。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。offline-online gate、override、sim-to-real confidence。

### OmniEVA

- **Candidate / Week / Score:** OmniEVA / 2025-W37 / 25/30；**Source Family / Type:** `ARXIV-2509.09332` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-11；later revisions同family不重复评分。Direct: arXiv v1 + project；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 静态3D注入在无关任务制造噪声，纯2D又不满足物理约束。
- **Mechanism / Ownership / Flow / Implementation:** Task-Adaptive Gated Router按instruction/scene hard gate 2D/3D injection；TE-GRPO纳入affordance、workspace、kinematics。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8个2D/3D/video benchmarks、sim/real案例及router ablation；当前v3只作revision。
- **Proves / Does Not Prove:** 证明task-conditioned geometry可行；不证明plan等同low-level安全控制。
- **Trade-offs / Failure Modes / Old-design Boundary:** 减少无关3D cost但新增gate error、depth drift、planner-controller gap；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MULTIMODAL-EMBODIED-VLA / Ch26 / Legacy N/A。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。gate confidence、constraint verifier、controller handoff。

### LoCoBench

- **Candidate / Week / Score:** LoCoBench / 2025-W37 / 25/30；**Source Family / Type:** `ARXIV-2509.09614` / Benchmark paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-11；later revisions同family不重复评分。Direct: arXiv v1 + dataset/harness；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** needle retrieval不覆盖跨文件修改、依赖和可执行正确性。
- **Mechanism / Ownership / Flow / Implementation:** 以repository/task组织长输入与unit-test verifier；dataset拥有snapshot，harness拥有environment/scoring。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 多模型、context length与coding baselines；成本/agent opportunity需与模型能力分离。
- **Proves / Does Not Prove:** 证明有效context需executable contract；不证明总分外推生产能力。
- **Trade-offs / Failure Modes / Old-design Boundary:** 真实性增加环境复现、dependency drift和test coverage风险；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；PLATFORM-EVALUATION-SYSTEM / Ch66 / Legacy Ch62；handoff MODEL-LONG-CONTEXT。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。snapshot、hidden tests、model-vs-harness。

### Understanding-Generation Coexistence

- **Candidate / Week / Score:** Understanding-Generation Coexistence / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.09666` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-11；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 统一模型声称理解与生成互益，但共享容量也可能仅共存。
- **Mechanism / Ownership / Flow / Implementation:** controlled joint training、representation probe与transfer分解synergy/coexistence；objective owner定义mixture。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 理解/生成任务、single/joint baselines和data/objective ablations；绑定作者architecture。
- **Proves / Does Not Prove:** 证明需用transfer/ablation判定互益；不证明统一范式普遍优于专用。
- **Trade-offs / Failure Modes / Old-design Boundary:** 共享提高复用也新增negative transfer、capacity contention与loss scaling；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MULTIMODAL-GENERATIVE-PARADIGMS / Ch24 / Legacy N/A。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。何种representation与schedule产生双向transfer。

### SpatialVID

- **Candidate / Week / Score:** SpatialVID / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.09676` / Dataset paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-11；later revisions同family不重复评分。Direct: arXiv v1 + dataset；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 视频多有动作/语义标签但缺相机、深度和空间关系。
- **Mechanism / Ownership / Flow / Implementation:** 构建video+spatial annotation pipeline，将frame/time、object relation与provenance绑定。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** dataset stats、annotation quality与下游baseline；自动标注误差和license保留。
- **Proves / Does Not Prove:** 证明spatial video是独立data contract；不证明规模自动产生causal world model。
- **Trade-offs / Failure Modes / Old-design Boundary:** 增加监督但引入pseudo-label、timestamp、storage与governance；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；TRAIN-DATA / Ch27 / Legacy Ch23；handoff MULTIMODAL-WORLD-MODELS。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。confidence、temporal identity、object persistence。

### Reverse-Engineered Reasoning

- **Candidate / Week / Score:** Reverse-Engineered Reasoning / 2025-W37 / 22/30；**Source Family / Type:** `ARXIV-2509.06160` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-08；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 开放generation无唯一verifier，不能直接复用数学RLVR。
- **Mechanism / Ownership / Flow / Implementation:** 从高质量输出反向构造reasoning/constraint trajectory再训练；pipeline拥有synthetic provenance。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 创作任务与direct generation/CoT/SFT及trace ablation；主观evaluator有限。
- **Proves / Does Not Prove:** 证明反向过程监督是开放任务信号；不证明recovered reasoning是因果过程。
- **Trade-offs / Failure Modes / Old-design Boundary:** 提升controllability却有post-hoc rationalization和evaluator bias；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；TRAIN-SFT / Ch29 / Legacy Ch25；handoff PLATFORM-EVALUATION-SYSTEM。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。trace faithfulness、human calibration。

### dLLM RL framework

- **Candidate / Week / Score:** dLLM RL framework / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.06949` / Research/system paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-09；later revisions同family不重复评分。Direct: arXiv v1 + framework code；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** AR policy tooling假设左到右action，diffusion多位置去噪不能直接套用。
- **Mechanism / Ownership / Flow / Implementation:** 将denoising step/masked decisions纳入rollout、log-prob与reward assignment。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** diffusion LM reasoning、objective baselines和framework效率；wall-clock绑定作者设置。
- **Proves / Does Not Prove:** 证明RL stack须匹配generation factorization；不证明diffusion RL普遍更优。
- **Trade-offs / Failure Modes / Old-design Boundary:** 支持并行修正却新增trajectory identity、step credit、rollback；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；TRAIN-RLHF / Ch31 / Legacy Ch27；handoff MULTIMODAL-GENERATIVE-PARADIGMS。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。exact probability、step scheduling、distributed replay。

### UniVerse-1

- **Candidate / Week / Score:** UniVerse-1 / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.06155` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-08；later revisions同family不重复评分。Direct: arXiv v1 + project；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 单expert难兼顾声画质量与同步，独立模型又缺shared timeline。
- **Mechanism / Ownership / Flow / Implementation:** stitch modality experts并共享temporal/semantic condition；experts拥有modal state，stitch layer对齐。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** audio-video benchmarks、single/unified baselines与ablation；无真实streaming contract。
- **Proves / Does Not Prove:** 证明expert composition是alternative branch；不证明单模型不可行。
- **Trade-offs / Failure Modes / Old-design Boundary:** 复用专用能力但增加artifact compatibility、timestamp drift、memory；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；MULTIMODAL-GENERATIVE-PARADIGMS / Ch24 / Legacy N/A。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。expert compatibility、shared clock、long sync。

### Off-policy RL + multi-agent tree search step-provers

- **Candidate / Week / Score:** Off-policy RL + multi-agent tree search step-provers / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.06493` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-08；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 形式证明长链稀疏，on-policy单Agent采样昂贵且卡branch。
- **Mechanism / Ownership / Flow / Implementation:** 多Agent tree search产生proof trajectories，off-policy RL回收；tree拥有branch state，learner处理replay/staleness。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** step-prover benchmark与on-policy/single-agent baselines；communication/compute限制普适性。
- **Proves / Does Not Prove:** 证明搜索+replay提升形式环境探索；不证明更多agents单调获益。
- **Trade-offs / Failure Modes / Old-design Boundary:** 扩大覆盖但新增stale policy、shared-state conflict和communication tax；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；AGENT-MULTI-AGENT / Ch82 / Legacy Ch78；handoff TRAIN-PPO。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。replay freshness、branch dedup、agent headroom。

### Guided Decoding for RAG

- **Candidate / Week / Score:** Guided Decoding for RAG / 2025-W37 / 25/30；**Source Family / Type:** `ARXIV-2509.06631` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-08；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** RAG检索到证据后free decoding仍可忽略或生成证据外claim。
- **Mechanism / Ownership / Flow / Implementation:** decoding用evidence/constraint引导token；retriever拥有evidence set，decoder拥有constrained generation。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** QA/RAG benchmarks与unguided variants；检索错误、cost和开放生成覆盖有限。
- **Proves / Does Not Prove:** 证明retrieval与evidence-use是独立contract；不证明guided output即factual。
- **Trade-offs / Failure Modes / Old-design Boundary:** 提高遵循却可能压制泛化、放大错误证据、增加latency；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；AGENT-RAG / Ch76 / Legacy Ch72；handoff MODEL-SAMPLING。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。conflict、claim coverage、abstention/confidence。

### Test-Time Scaling on Knowledge-Intensive Tasks

- **Candidate / Week / Score:** Test-Time Scaling on Knowledge-Intensive Tasks / 2025-W37 / 25/30；**Source Family / Type:** `ARXIV-2509.06861` / Evaluation paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-09；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 更多reasoning在知识缺失时可能只放大猜测。
- **Mechanism / Ownership / Flow / Implementation:** 控制inference budget和sampling/selection，按knowledge dependency分层；harness分离sampling与retrieval opportunity。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** reasoning models、knowledge QA与math-like tasks的budget curves；retrieval/cost未统一。
- **Proves / Does Not Prove:** 证明收益依赖information availability；不证明reasoning无用或retrieval总能补足。
- **Trade-offs / Failure Modes / Old-design Boundary:** 更多compute可提高覆盖也增加correlated hallucination和成本；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；PLATFORM-EVALUATION-SYSTEM / Ch66 / Legacy Ch62；handoff MODEL-SAMPLING。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。retrieval/abstain trigger、marginal value。

### MachineLearningLM

- **Candidate / Week / Score:** MachineLearningLM / 2025-W37 / 23/30；**Source Family / Type:** `ARXIV-2509.06806` / Research paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-09；later revisions同family不重复评分。Direct: arXiv v1 + task generator；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** 通用LM对tabular prediction需task fitting，文本预训缺ML episodes。
- **Mechanism / Ownership / Flow / Implementation:** 持续预训于数百万synthetic tabular tasks，使LM in-context推断task；generator拥有task distribution。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 多tabular datasets、classical/TabPFN/LLM baselines与scale curves；真实shift有限。
- **Proves / Does Not Prove:** 证明data distribution可教LM执行in-context ML；不证明替代专用模型。
- **Trade-offs / Failure Modes / Old-design Boundary:** 获得few-shot适应但增加synthetic bias、context cost和calibration；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；TRAIN-PRETRAINING / Ch28 / Legacy Ch24；handoff WORLDVIEW-REPRESENTATION。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。generator coverage、uncertainty、privacy。

### AU-Harness

- **Candidate / Week / Score:** AU-Harness / 2025-W37 / 26/30；**Source Family / Type:** `ARXIV-2509.08031` / Evaluation system paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-10；later revisions同family不重复评分。Direct: arXiv v1 + toolkit；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** Audio LLM benchmark preprocessing、prompt、I/O、grader各异，分数不可比。
- **Mechanism / Ownership / Flow / Implementation:** 统一task registry、audio preprocessing、model adapter、runner/evaluator；artifact pin config与trace。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 多Audio LLM和任务与原论文数字复核；hardware/API drift需持续记录。
- **Proves / Does Not Prove:** 证明harness contract是evidence一部分；不证明部署声学可靠。
- **Trade-offs / Failure Modes / Old-design Boundary:** 提高复现但新增adapter correctness、normalization、version drift；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；PLATFORM-EVALUATION-SYSTEM / Ch66 / Legacy Ch62。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。streaming latency、noise distribution、pinning。

### Reasoning poisoning attacks

- **Candidate / Week / Score:** Reasoning poisoning attacks / 2025-W37 / 26/30；**Source Family / Type:** `ARXIV-2509.05739` / Security paper。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-08；later revisions同family不重复评分。Direct: arXiv v1；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Source complete；覆盖metadata、Introduction/Related Work、Method/architecture、state/control/data flow、Implementation、Evaluation、baseline/ablation/sensitivity、关键Appendix、limitations与artifact surface；Not Disclosed不反推。
- **Problem / Previous Design / Changed Constraint:** reasoning traces扩展训练/提示攻击面，final-only评测漏过程攻击。
- **Mechanism / Ownership / Flow / Implementation:** 构造reasoning poisoning/backdoor并比较trigger、trace、detection；attacker拥有poison，monitor观测rationale。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 多reasoning/non-reasoning models、ASR/utility/detection与trigger sensitivity；真实供应链有限。
- **Proves / Does Not Prove:** 证明reasoning改变而非消除attack surface；不证明CoT完整反映因果。
- **Trade-offs / Failure Modes / Old-design Boundary:** 提供监控信号也增加攻击载体、persistence和false reassurance；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；PLATFORM-SECURITY / Ch72 / Legacy Ch68；handoff AGENT-REFLECTION。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。hidden-state monitorability、provenance、red-team。

### PyTorch Distributed Checkpoint

- **Candidate / Week / Score:** PyTorch Distributed Checkpoint / 2025-W37 / 29/30；**Source Family / Type:** `PYTORCH-DCP-2025-09-11` / Official engineering design。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-11；later revisions同family不重复评分。Direct: official PyTorch blog + docs/code；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Official engineering packet complete：通读blog的design、planner/storage/data-flow、implementation/evaluation/limitations并交叉核对docs/code surface；非论文材料没有Related Work/Appendix，不虚构覆盖。
- **Problem / Previous Design / Changed Constraint:** 大规模训练单rank汇聚造成内存/IO bottleneck，拓扑变化使恢复脆弱。
- **Mechanism / Ownership / Flow / Implementation:** 各rank并行保存sharded state，planner/storage分离logical与physical layout，load按新topology reshard。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 官方案例覆盖large jobs、async/staged和storage；收益绑定FS/model/shard/failure timing。
- **Proves / Does Not Prove:** 证明checkpoint是versioned distributed protocol；不证明任意custom state自动迁移。
- **Trade-offs / Failure Modes / Old-design Boundary:** 降低pause但新增schema、partial write、atomic commit、GC与compatibility；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；TRAIN-CHECKPOINT / Ch35 / Legacy Ch31；handoff TRAIN-DISTRIBUTED-TRAINING。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。manifest/commit、cleanup、migration。

### PyTorch native XCCL

- **Candidate / Week / Score:** PyTorch native XCCL / 2025-W37 / 27/30；**Source Family / Type:** `PYTORCH-XCCL-2.8` / Official backend integration。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-12；later revisions同family不重复评分。Direct: official PyTorch blog + RFC/tests；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Official backend packet complete：通读announcement、backend integration、TorchTitan case、tests/RFC surface与已披露限制；未公开的网络拓扑和precision配置记为Not Disclosed。
- **Problem / Previous Design / Changed Constraint:** Intel XPU缺native distributed backend，应用特殊集成且FSDP2/TP parity不稳。
- **Mechanism / Ownership / Flow / Implementation:** XCCL注册process-group backend，XPU可自动选择；backend-agnostic tests复用collective contract。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** TorchTitan Llama3、FSDP2+TP到2K ranks；厂商matching claim缺同构网络/precision。
- **Proves / Does Not Prove:** 证明公共API可把backend portability变contract；不证明性能等价。
- **Trade-offs / Failure Modes / Old-design Boundary:** 减少应用分叉但新增backend failure、semantics和version matrix；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；TRAIN-DISTRIBUTED-TRAINING / Ch36 / Legacy Ch32；handoff TRAIN-TENSOR-PARALLEL。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。collective parity、diagnostics、topology tuning。

### PyTorch-vLLM disaggregated inference

- **Candidate / Week / Score:** PyTorch-vLLM disaggregated inference / 2025-W37 / 28/30；**Source Family / Type:** `PYTORCH-VLLM-DISAGG-2025-09-12` / Official engineering case。
- **Event / Revision / Sources:** first-public 或 arXiv v1 2025-09-12；later revisions同family不重复评分。Direct: official PyTorch/vLLM blog；2026-08-24复核arXiv HTML/PDF、official docs/repository（存在时）。
- **Access / Full-read Coverage:** Official engineering case packet complete：通读P/D design、KV-transfer flow、implementation/evaluation contract与failure discussion；无独立论文Appendix，未披露配置不反推。
- **Problem / Previous Design / Changed Constraint:** prefill/decode形态不同，共置副本难同时满足TTFT、TPOT与利用率。
- **Mechanism / Ownership / Flow / Implementation:** P/D worker分池并KV transfer；runtime执行，router/control plane负责阶段路由与容量。
- **Evaluation Contract / Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 官方scale case绑定model/GPU/network/KV connector/batch/concurrency，不能外推。
- **Proves / Does Not Prove:** 证明PD是state-transfer control flow而非拆服务；不证明所有长度获益。
- **Trade-offs / Failure Modes / Old-design Boundary:** 独立扩缩却新增KV identity、transfer failure、backpressure和rollback；作者实验不视为跨硬件、跨数据、跨SLO通用事实。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage:** `Layering / Dependency` 或受限 alternative branch；INFER-PD-DISAGGREGATION / Ch55 / Legacy Ch51；handoff INFER-SCHEDULING。已同读owner与相邻章；保留旧方案成立条件。
- **Integration / Changed Files / Open Questions:** `Books Pending — Integration Deferred`；Historical Books Gate关闭，未修改Books。KV ownership、connector recovery、admission。

## Low-score Identity / Date / Rejection Closure

| Candidate | Source Family ID | First-public / v1 | Score | Verified Rejection Reason |
| --- | --- | --- | ---: | --- |
| MAS-Bench | `ARXIV-2509.06477` | 2025-09-08 | 19/30 | mobile GUI shortcut benchmark过窄，opportunity与模型能力难分离 |
| Interleaving Reasoning for Text-to-Image | `ARXIV-2509.06945` | 2025-09-09 | 19/30 | 机制与既有interleaved planning分支重叠，system contract不足 |
| Kling-Avatar | `ARXIV-2509.09595` | 2025-09-11 | 19/30 | 长时avatar事实保留，公开evidence不足以形成通用runtime结论 |
| mmBERT | `ARXIV-2509.06888` | 2025-09-09 | 19/30 | multilingual encoder专项，不改变当前AI System结论 |
| FLUX-Reason-6M / PRISM-Bench | `ARXIV-2509.09680` | 2025-09-11 | 19/30 | 规模与作者harness不能单独支持长期机制 |
| EnvX | `ARXIV-2509.08088` | 2025-09-10 | 18/30 | scope宽，artifact/evaluation不足以建立新owner |
| HumanAgencyBench | `ARXIV-2509.08494` | 2025-09-10 | 19/30 | 主要是rubric/benchmark proposal，先归档 |
| RL for Deep Research survey | `ARXIV-2509.06733` | 2025-09-09 | 18/30 | survey只用于discovery，不作新机制primary evidence |
| RL for Large Reasoning Models survey | `ARXIV-2509.08827` | 2025-09-11 | 18/30 | survey用于路线校准，不重复机制owner |
| 3D and 4D World Modeling survey | `ARXIV-2509.07996` | 2025-09-10 | 18/30 | taxonomy有用但不是新primary mechanism |
| Fuzzing Brain | `ARXIV-2509.07225` | 2025-09-09 | 19/30 | 真实exploit correctness与安全边界不足 |
| Capability-Adaptive Hint Scaffolding | `ARXIV-2509.06923` | 2025-09-09 | 19/30 | 未越过核心门槛，避免与CDE重复owner |
| RLVR divergence choice | `ARXIV-2509.07430` | 2025-09-09 | 19/30 | objective细节作related evidence，不重构主线 |
| vLLM 0.10.2 | `VLLM-0.10.2` | 2025-09-13 | 19/30 | PyPI artifact/date/hash已核验；Version Fact / Mechanism Not Disclosed |
| SGLang 0.5.2 | `SGLANG-0.5.2` | 2025-09-11 | 19/30 | PyPI artifact/date/hash已核验；版本本身缺机制contract |
| SafetyKit GPT-5 case study | `OPENAI-SAFETYKIT-2025-09-09` | 2025-09-09 | 16/30 | 客户案例指标来自vendor/customer eval，机制与workload未公开 |
| Veo 3 Vertex AI GA | `VERTEX-VEO3-GA-2025-09-08` | 2025-09-08 | 15/30 | availability fact；内部模型/serving机制未披露 |

## Evidence Level

- Level A：official artifact/API/release fact，只证明公开contract。
- Level B：33个20+ arXiv owners完成primary full-read packet，仍是作者实验。
- Level C：survey/version/case只用于discovery与去重。
- evolution与owner mapping是本项目推断，已与source claims分开。

## Cross-Week Deduplication and Spillback

- W36 spillback identity ledger（均不计入W37的54个owners）：

| Source Family | Canonical title | v1 / owner week | W37-window revision | W36 ledger state at review |
| --- | --- | --- | --- | --- |
| `ARXIV-2509.04013` | On Robustness and Reliability of Benchmark-Based Evaluation of LLMs | 2025-09-04 / W36 | None | Already present in rebuilt W36 ledger |
| `ARXIV-2509.04185` | Set Block Decoding is a Language Model Inference Accelerator | 2025-09-04 / W36 | None | Already present in rebuilt W36 ledger |
| `ARXIV-2509.04504` | Behavioral Fingerprinting of Large Language Models | 2025-09-02 / W36 | None | Already present in rebuilt W36 ledger |
| `ARXIV-2509.04575` | Bootstrapping Task Spaces for Self-Improvement | 2025-09-04 / W36 | v2 2025-09-09 | Already present in rebuilt W36 ledger |
| `ARXIV-2509.04664` | Why Language Models Hallucinate | 2025-09-04 / W36 | None | Already present in W36 |
| `ARXIV-2509.05263` | LatticeWorld | 2025-09-05 / W36 | v2 2025-09-08 | Already present in rebuilt W36 ledger |
| `ARXIV-2509.05296` | WinT3R | 2025-09-05 / W36 | None | Already present in rebuilt W36 ledger |
| `ARXIV-2509.03646` | Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning | 2025-09-03 / W36 | v2 2025-09-08 | Spillback required |
| `ARXIV-2509.05209` | Hunyuan-MT Technical Report | 2025-09-05 / W36 | v2 2025-09-09 | Spillback required |

- W36 串行对账确认：`2509.04013`、`2509.04185`、`2509.04504`、`2509.04575`、`2509.04664`、`2509.05263`、`2509.05296` 已在 rebuilt ledger；真正缺失并触发 W36 reclosure 的只有 `2509.03646` 与 `2509.05209`。九项均不改变 W37 denominator。
- W38 boundary：2025-09-15及之后的v1/release不提前吸收。
- Qwen release/model card/config共享一个family；later revision/current HTML不改变v1 owner date。

## Independent Review and Gate

- ISO/date：54/54在W37；9项前置spillback W36；无W38倒灌。
- Score：54 = 19 high + 18 medium + 17 low；六维和机械复算。
- Evidence：37/37 retained packets、17/17 low closures；ordinary Pending 0、Blocked 0、family Disputed 0。
- Books：Historical Books Gate关闭；未修改Books。
- Gate：Candidate Evidence Gate **Passed**；Discovery/Archive **Conditional**（缺immutable Scholar/OpenAlex export）。

## Recommended Action

保留三条未来Books route：`TRAIN-GRPO → AGENT-WORKFLOW`、`MULTIMODAL-REPRESENTATION → MULTIMODAL-EMBODIED-VLA`、`TRAIN-CHECKPOINT → INFER-PD-DISAGGREGATION`。本阶段不做Books Integration。

## Event-Date Daily Decision

Historical Backfill不创建Daily；真实日期、spillback和证据边界保留在Weekly。

## Books Integration Decision

`Deferred — Historical Books Gate Closed`。legacy Books wording不是本轮完成证据。

## Ignored Noise

转载、榜单、无primary identity demo、API alias/价格变化、客户指标和跨周revision均不作新机制owner。

## Repository Changes

- 幂等重建本README：1个legacy seed→54个canonical owners。
- 增加37个Full Source Review、17个低分closure、9个W36 spillback。
- 未改年度索引/Books/Learning State；未stage/commit/push。

## Open Questions

- immutable Scholar/OpenAlex/DBLP/Crossref export仍待年度reconciliation。
- rollout provenance/privacy/off-policy bound、embodied controller safety、PD/checkpoint/collective跨版本恢复仍待验证。

## Sources

- Qwen3-Next — https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct（First Public: 2025-09-10；Accessed: 2026-08-24）
- SAPO collective RL experience sharing — https://arxiv.org/html/2509.08721（First Public: 2025-09-10；Accessed: 2026-08-24）
- WebExplorer — https://arxiv.org/html/2509.06501（First Public: 2025-09-08；Accessed: 2026-08-24）
- Paper2Agent — https://arxiv.org/html/2509.06917（First Public: 2025-09-09；Accessed: 2026-08-24）
- SFR-DeepResearch — https://arxiv.org/html/2509.06283（First Public: 2025-09-08；Accessed: 2026-08-24）
- AgentGym-RL — https://arxiv.org/html/2509.08755（First Public: 2025-09-10；Accessed: 2026-08-24）
- CDE curiosity-driven RL — https://arxiv.org/html/2509.09675（First Public: 2025-09-11；Accessed: 2026-08-24）
- Parallel-R1 — https://arxiv.org/html/2509.07980（First Public: 2025-09-10；Accessed: 2026-08-24）
- Visual Representation Alignment — https://arxiv.org/html/2509.07979（First Public: 2025-09-10；Accessed: 2026-08-24）
- Mini-o3 visual search — https://arxiv.org/html/2509.07969（First Public: 2025-09-10；Accessed: 2026-08-24）
- Reconstruction Alignment — https://arxiv.org/html/2509.07295（First Public: 2025-09-09；Accessed: 2026-08-24）
- F1 VLA — https://arxiv.org/html/2509.06951（First Public: 2025-09-09；Accessed: 2026-08-24）
- Language Self-Play — https://arxiv.org/html/2509.07414（First Public: 2025-09-09；Accessed: 2026-08-24）
- Causal Attention with Lookahead Keys — https://arxiv.org/html/2509.07301（First Public: 2025-09-09；Accessed: 2026-08-24）
- SimpleQA Verified — https://arxiv.org/html/2509.07968（First Public: 2025-09-10；Accessed: 2026-08-24）
- RewardDance — https://arxiv.org/html/2509.08826（First Public: 2025-09-11；Accessed: 2026-08-24）
- HuMo — https://arxiv.org/html/2509.08519（First Public: 2025-09-10；Accessed: 2026-08-24）
- EchoX — https://arxiv.org/html/2509.09174（First Public: 2025-09-11；Accessed: 2026-08-24）
- Entropy-Modulated Policy Gradients — https://arxiv.org/html/2509.09265（First Public: 2025-09-11；Accessed: 2026-08-24）
- VLA-Adapter — https://arxiv.org/html/2509.09372（First Public: 2025-09-11；Accessed: 2026-08-24）
- SimpleVLA-RL — https://arxiv.org/html/2509.09674（First Public: 2025-09-11；Accessed: 2026-08-24）
- OmniEVA — https://arxiv.org/html/2509.09332（First Public: 2025-09-11；Accessed: 2026-08-24）
- LoCoBench — https://arxiv.org/html/2509.09614（First Public: 2025-09-11；Accessed: 2026-08-24）
- Understanding-Generation Coexistence — https://arxiv.org/html/2509.09666（First Public: 2025-09-11；Accessed: 2026-08-24）
- SpatialVID — https://arxiv.org/html/2509.09676（First Public: 2025-09-11；Accessed: 2026-08-24）
- Reverse-Engineered Reasoning — https://arxiv.org/html/2509.06160（First Public: 2025-09-08；Accessed: 2026-08-24）
- dLLM RL framework — https://arxiv.org/html/2509.06949（First Public: 2025-09-09；Accessed: 2026-08-24）
- UniVerse-1 — https://arxiv.org/html/2509.06155（First Public: 2025-09-08；Accessed: 2026-08-24）
- Off-policy RL + multi-agent tree search step-provers — https://arxiv.org/html/2509.06493（First Public: 2025-09-08；Accessed: 2026-08-24）
- Guided Decoding for RAG — https://arxiv.org/html/2509.06631（First Public: 2025-09-08；Accessed: 2026-08-24）
- Test-Time Scaling on Knowledge-Intensive Tasks — https://arxiv.org/html/2509.06861（First Public: 2025-09-09；Accessed: 2026-08-24）
- MachineLearningLM — https://arxiv.org/html/2509.06806（First Public: 2025-09-09；Accessed: 2026-08-24）
- AU-Harness — https://arxiv.org/html/2509.08031（First Public: 2025-09-10；Accessed: 2026-08-24）
- Reasoning poisoning attacks — https://arxiv.org/html/2509.05739（First Public: 2025-09-08；Accessed: 2026-08-24）
- PyTorch Distributed Checkpoint — https://pytorch.org/blog/distributed-checkpoint-efficient-checkpointing-in-large-scale-jobs/（First Public: 2025-09-11；Accessed: 2026-08-24）
- PyTorch native XCCL — https://pytorch.org/blog/pytorch-2-8-brings-native-xccl-support-to-intel-gpus-case-studies-from-argonne-national-laboratory/（First Public: 2025-09-12；Accessed: 2026-08-24）
- PyTorch-vLLM disaggregated inference — https://pytorch.org/blog/disaggregated-inference-at-scale-with-pytorch-vllm/（First Public: 2025-09-12；Accessed: 2026-08-24）
- MAS-Bench — https://arxiv.org/html/2509.06477（First Public: 2025-09-08；Accessed: 2026-08-24）
- Interleaving Reasoning for Text-to-Image — https://arxiv.org/html/2509.06945（First Public: 2025-09-09；Accessed: 2026-08-24）
- Kling-Avatar — https://arxiv.org/html/2509.09595（First Public: 2025-09-11；Accessed: 2026-08-24）
- mmBERT — https://arxiv.org/html/2509.06888（First Public: 2025-09-09；Accessed: 2026-08-24）
- FLUX-Reason-6M / PRISM-Bench — https://arxiv.org/html/2509.09680（First Public: 2025-09-11；Accessed: 2026-08-24）
- EnvX — https://arxiv.org/html/2509.08088（First Public: 2025-09-10；Accessed: 2026-08-24）
- HumanAgencyBench — https://arxiv.org/html/2509.08494（First Public: 2025-09-10；Accessed: 2026-08-24）
- RL for Deep Research survey — https://arxiv.org/html/2509.06733（First Public: 2025-09-09；Accessed: 2026-08-24）
- RL for Large Reasoning Models survey — https://arxiv.org/html/2509.08827（First Public: 2025-09-11；Accessed: 2026-08-24）
- 3D and 4D World Modeling survey — https://arxiv.org/html/2509.07996（First Public: 2025-09-10；Accessed: 2026-08-24）
- Fuzzing Brain — https://arxiv.org/html/2509.07225（First Public: 2025-09-09；Accessed: 2026-08-24）
- Capability-Adaptive Hint Scaffolding — https://arxiv.org/html/2509.06923（First Public: 2025-09-09；Accessed: 2026-08-24）
- RLVR divergence choice — https://arxiv.org/html/2509.07430（First Public: 2025-09-09；Accessed: 2026-08-24）
- vLLM 0.10.2 — https://pypi.org/project/vllm/0.10.2/（First Public: 2025-09-13；Accessed: 2026-08-24）
- SGLang 0.5.2 — https://pypi.org/project/sglang/0.5.2/（First Public: 2025-09-11；Accessed: 2026-08-24）
- SafetyKit GPT-5 case study — https://openai.com/index/safetykit/（First Public: 2025-09-09；Accessed: 2026-08-24）
- Veo 3 Vertex AI GA — https://docs.cloud.google.com/vertex-ai/generative-ai/docs/release-notes（First Public: 2025-09-08；Accessed: 2026-08-24）
