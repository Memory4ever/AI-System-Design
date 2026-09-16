# Daily Research — 2026-05-18

**规范：** V3

**窗口：** 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-09-15T19:25:55+08:00

## 1. 结论

旧 submission-window ledger 的 324 个 identity 与 52 个候选仍不属于本日 owner。当前 537 个 identity 经严格有界返修后冻结为 `537 = 64 retained + 473 pre-denominator closure + 0 withdrawn`；本轮只定点重审终审指定的 18 个 FN/signal 与 3 个 FP/score，没有重扫其余 closure。

owner-time 由 arXiv 官方 announcement schedule、announcement-time ID allocation、月内连续序号及 OAI 边界共同证明：本批在 2026-05-17 20:00 美东（2026-05-18 08:00 北京）公开，早于 09:00 截点。DataCite 仅作 identity/DOI 佐证，不作发布时间。

64 项 Evidence 已冻结为 `32 current exact-v1 + 32 replayable historical exact-v1`；原 38 reuse 逐项落为 `32 historical replay + 4 current exact-v1 recheck + 2 candidates removed`。Books Decision 为 `31 Integrate + 33 No Change`。fresh non-author final review 已逐项接受 31 个真实 Integrate 的 Books 正文承载，并确认 33 个 No Change 的既有 owner 覆盖；报告完成。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 Research/RSS 相邻事件；05-16 08:00+08 Malta 公告早于窗口起点，之后无窗内研究或系统事件 | 已检查 | 无 |
| SRC-ANTHROPIC | 官方 Research 目录；时间字段由 05-14 跳至 05-22 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind 与 Google Research publication index；相邻记录夹在 05-06/05-28 与 04-25/05-28 | 已检查 | 无 |
| SRC-META-AI | Meta Publications；GIM 目录/详情只给 05-17/05-18 冲突日期，arXiv v1 明确晚至 05-19 01:09:50+08 | 已检查 | GIM 日级日期冲突已隔离，不作为本窗确定事件 |
| SRC-QWEN | 官方 publication/blog index；无窗内条目 | 已检查 | 无 |
| SRC-DEEPSEEK | 官方模型与研究发布索引；无窗内条目 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog 与官方 GitHub；无窗内技术文章、首次公开仓库或 release，pushed_at 不作首次公开 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 官方 Research 全部列表；相邻记录为 04-30 与 05-21 | 已检查 | 无 |
| SRC-ZAI | 官方 Research 目录；相邻记录为 04-29 与 05-20 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 官方论文目录；Charon 为 05-16 00:00+08，早于窗口，之后无窗内官方事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | ERNIE 技术博客与 release index；无窗内条目 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 官方 Paper/Blog；03-13 后跳至 06-29 | 已检查 | 无 |
| SRC-MINIMAX | 官方 Research/Blog；相邻技术文章为 03-18 与 05-26/27 | 已检查 | 无 |
| SRC-ARXIV | official announcement-batch replay：537 个 covered-category identity 全部落在 2605.15202–2605.16258；64 retained、473 pre-denominator closure、0 withdrawn；announcement=2026-05-18 08:00+08，旧 324/52 submission-window 集合不再拥有本日 | 已检查 | 无；官方批次证据见 official-owner-batch-evidence-v3.json，DataCite 不充当 cutoff 时刻 |

完整 identity、分页/路由与逐项理由见 [`screening-ledger-v3.json`](../_sources/daily-20260518/screening-ledger-v3.json)，严格批次证明见 [`official-owner-batch-evidence-v3.json`](../_sources/daily-20260518/official-owner-batch-evidence-v3.json)；旧/新集合调和见 [`owner-reconciliation-v3.json`](../_sources/daily-20260518/owner-reconciliation-v3.json)。`已检查` 只证明注册入口的有界窗口检查，不声称互联网绝无遗漏。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [SDOF: Taming the Alignment Tax in Multi-Agent Orchestration with State-Constrained Dispatch](https://arxiv.org/html/2605.15204v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | - **Problem:** Multi-agent orchestration frameworks such as LangChain, LangGraph, and CrewAI route tasks through graph-based pipelines but do not enforce the stage constraints that govern real business processes. - **Old path / changed constraint:** However, in their native forms they do not expose business-stage legality as an explicit runtime contract of the kind evaluated here. - **Mechanism / ownership:** We present SDOF, a framework that treats multi-agent execution as a constrained state machine. - **Evaluation contract:** Our GSPO-aligned 7B Intent Router achieves higher joint accuracy than zero-shot GPT-4o on this FSM-constrained adversarial routing benchmark (80.9% versus 48.9%). - **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. - **Trade-off / failure mode:** Violations cause compliance failures, data corruption, and legal risk. - **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement. - **Primary:** [arXiv:2605.15204v1](https://arxiv.org/abs/2605.15204v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.15204v1.html.html`。 - **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.；3+2+2=7 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`AGENT-MULTI-AGENT` [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [Hydra: Efficient, Correct Code Generation via Checkpoint-and-Rollback Support](https://arxiv.org/html/2605.15238v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。；3+3+3=9 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`AGENT-WORKFLOW` [章节](../../../../books/part-07-agent/81-workflow.md) |
| [Training on Documents About Monitoring Leads to CoT Obfuscation](https://arxiv.org/html/2605.15257v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。；3+3+3=9 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`PLATFORM-MONITORING` [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](https://arxiv.org/html/2605.15338v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。；3+3+3=9 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`AGENT-MEMORY` [章节](../../../../books/part-07-agent/77-memory.md) |
| [Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute](https://arxiv.org/html/2605.15377v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。；3+3+3=9 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`PLATFORM-MONITORING` [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Is One Score Enough? Rethinking the Evaluation of Sequentially Evolving LLM Memory](https://arxiv.org/html/2605.15384v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。；3+3+3=9 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`AGENT-MEMORY` [章节](../../../../books/part-07-agent/77-memory.md) |
| [$ϕ$-Balancing for Mixture-of-Experts Training](https://arxiv.org/html/2605.15403v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`MODEL-MOE` [章节](../../../../books/part-02-model/21-moe.md) |
| [DualKV: Shared-Prompt Flash Attention for Efficient RL Training with Large Rollouts and Long Contexts](https://arxiv.org/html/2605.15422v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。；3+3+3=9 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`TRAIN-DISTRIBUTED-TRAINING` [章节](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Runtime-Structured Task Decomposition for Agentic Coding Systems](https://arxiv.org/html/2605.15425v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。；3+3+3=9 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`AGENT-WORKFLOW` [章节](../../../../books/part-07-agent/81-workflow.md) |
| [Entity-Centric World Models: Interaction-Aware Masking for Causal Video Prediction](https://arxiv.org/html/2605.15466v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`MULTIMODAL-WORLD-MODELS` [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [EgoExo-WM: Unlocking Exo Video for Ego World Models](https://arxiv.org/html/2605.15477v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。；3+3+3=9 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`MULTIMODAL-WORLD-MODELS` [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [STS: Efficient Sparse Attention with Speculative Token Sparsity](https://arxiv.org/html/2605.15508v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `STS: Efficient Sparse Attention with Speculative Token Sparsity` is supported only under the v1-disclosed workload and evaluator behind `6 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`MODEL-LONG-CONTEXT` [章节](../../../../books/part-02-model/22-long-context.md) |
| [RoPE Distinguishes Neither Positions Nor Tokens in Long Contexts, Provably](https://arxiv.org/html/2605.15514v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `RoPE Distinguishes Neither Positions Nor Tokens in Long Contexts, Provably` is supported only under the v1-disclosed workload and evaluator behind `§§3.1 and 5 — empirical verification and indexing-task evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`MODEL-POSITION-ENCODING` [章节](../../../../books/part-02-model/13-position-encoding.md) |
| [On the Fragility of Data Attribution When Learning Is Distributed](https://arxiv.org/html/2605.15520v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `On the Fragility of Data Attribution When Learning Is Distributed` is supported only under the v1-disclosed workload and evaluator behind `§4 Experimental Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`TRAIN-DATA` [章节](../../../../books/part-04-training-system/27-data.md) |
| [Process Rewards with Learned Reliability](https://arxiv.org/html/2605.15529v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | Concentration is learned evidence reliability under the continuation generator and judge, not calibrated epistemic truth or a frequentist confidence interval.；3+2+3=8 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`TRAIN-RLHF` [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs](https://arxiv.org/html/2605.15565v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs` is supported only under the v1-disclosed workload and evaluator behind `§4 Evaluation: Applications of AstraFlow`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`TRAIN-DISTRIBUTED-TRAINING` [章节](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Response-Conditioned Parallel-to-Sequential Orchestration for Multi-Agent Systems](https://arxiv.org/html/2605.15573v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Response-Conditioned Parallel-to-Sequential Orchestration for Multi-Agent Systems` is supported only under the v1-disclosed workload and evaluator behind `4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`AGENT-MULTI-AGENT` [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [STAR: A Stage-attributed Triage and Repair framework for RCA Agents in Microservices](https://arxiv.org/html/2605.15581v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `STAR: A Stage-attributed Triage and Repair framework for RCA Agents in Microservices` is supported only under the v1-disclosed workload and evaluator behind `§V Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`AGENT-WORKFLOW` [章节](../../../../books/part-07-agent/81-workflow.md) |
| [PSD: Pushing the Pareto Frontier of Diffusion LLMs via Parallel Speculative Decoding](https://arxiv.org/html/2605.15609v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `PSD: Pushing the Pareto Frontier of Diffusion LLMs via Parallel Speculative Decoding` is supported only under the v1-disclosed workload and evaluator behind `4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`MULTIMODAL-GENERATIVE-PARADIGMS` [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [A Few GPUs, A Whole Lotta Scale: Faithful LLM Training Emulation with PrismLLM](https://arxiv.org/html/2605.15617v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `A Few GPUs, A Whole Lotta Scale: Faithful LLM Training Emulation with PrismLLM` is supported only under the v1-disclosed workload and evaluator behind `§8 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`TRAIN-DISTRIBUTED-TRAINING` [章节](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Latent Video Prediction Learns Better World Models](https://arxiv.org/html/2605.15618v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Latent Video Prediction Learns Better World Models` is supported only under the v1-disclosed workload and evaluator behind `§§4–9 representation, corruption, physics and prediction evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`MULTIMODAL-WORLD-MODELS` [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Rethinking the Security of DP-SGD: A Corrected Analysis of Differentially Private Machine Learning](https://arxiv.org/html/2605.15648v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Rethinking the Security of DP-SGD: A Corrected Analysis of Differentially Private Machine Learning` is supported only under the v1-disclosed workload and evaluator behind `§§4–6 auditing and experimental comparison`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`PLATFORM-SECURITY` [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [PRISM: Prompt Reliability via Iterative Simulation and Monitoring for Enterprise Conversational AI](https://arxiv.org/html/2605.15665v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `PRISM: Prompt Reliability via Iterative Simulation and Monitoring for Enterprise Conversational AI` is supported only under the v1-disclosed workload and evaluator behind `§5 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`PLATFORM-MONITORING` [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Going Beyond the Edge: Distributed Inference of Transformer Models on Ultra-Low-Power Wireless Devices](https://arxiv.org/html/2605.15694v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Going Beyond the Edge: Distributed Inference of Transformer Models on Ultra-Low-Power Wireless Devices` is supported only by the exact-v1 PDF's disclosed workload and evaluator; undisclosed deployment fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`INFER-SCHEDULING` [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory](https://arxiv.org/html/2605.15710v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiment`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation](https://arxiv.org/html/2605.15761v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?](https://arxiv.org/html/2605.15777v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiment`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge](https://arxiv.org/html/2605.15815v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge` is supported only under the v1-disclosed workload and evaluator behind `4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`AGENT-PLATFORM` [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades](https://arxiv.org/html/2605.15846v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [To GPU or Not to GPU: Vector Search in Relational Engines](https://arxiv.org/html/2605.15957v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `To GPU or Not to GPU: Vector Search in Relational Engines` is supported only under the v1-disclosed workload and evaluator behind `§§3 and 5 Vec-H/operator evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`INFER-TENSORRT-LLM` [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Imperfect World Models are Exploitable](https://arxiv.org/html/2605.15960v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Imperfect World Models are Exploitable` is supported only under the v1-disclosed workload and evaluator behind `§3 Results`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`MULTIMODAL-WORLD-MODELS` [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Deterministic Event-Graph Substrates as World Models for Counterfactual Reasoning](https://arxiv.org/html/2605.15967v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Deterministic Event-Graph Substrates as World Models for Counterfactual Reasoning` is supported only under the v1-disclosed workload and evaluator behind `Summary of empirical findings.`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`MULTIMODAL-WORLD-MODELS` [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Who Owns This Agent? Tracing AI Agents Back to Their Owners](https://arxiv.org/html/2605.16035v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Who Owns This Agent? Tracing AI Agents Back to Their Owners` is supported only under the v1-disclosed workload and evaluator behind `§6 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`AGENT-PLATFORM` [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking](https://arxiv.org/html/2605.16154v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking` is supported only under the v1-disclosed workload and evaluator behind `§5 Empirical Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`MULTIMODAL-EMBODIED-VLA` [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Runtime-Orchestrated Second-Order Optimization for Scalable LLM Training](https://arxiv.org/html/2605.16184v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Runtime-Orchestrated Second-Order Optimization for Scalable LLM Training` is supported only under the v1-disclosed workload and evaluator behind `§IV Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+3+3=9 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`TRAIN-DISTRIBUTED-TRAINING` [章节](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems](https://arxiv.org/html/2605.16198v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems` is supported only under the v1-disclosed workload and evaluator behind `§5 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`PLATFORM-SECURITY` [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Argus: Evidence Assembly for Scalable Deep Research Agents](https://arxiv.org/html/2605.16217v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Argus: Evidence Assembly for Scalable Deep Research Agents` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`AGENT-RAG` [章节](../../../../books/part-07-agent/76-rag.md) |
| [Ascend-RaBitQ: Heterogeneous NPU-CPU Acceleration of Billion-Scale Similarity Search with 1-bit Quantization](https://arxiv.org/html/2605.16007v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Ascend-RaBitQ: Heterogeneous NPU-CPU Acceleration of Billion-Scale Similarity Search with 1-bit Quantization` is supported only under the v1-disclosed workload and evaluator behind `4 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+3+3=9 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`INFER-TENSORRT-LLM` [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [No Free Swap: Protocol-Dependent Layer Redundancy in Transformers](https://arxiv.org/html/2605.16234v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `No Free Swap: Protocol-Dependent Layer Redundancy in Transformers` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；2+2+3=7 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`MODEL-TRANSFORMER-LAYER` [章节](../../../../books/part-02-model/17-transformer-layer.md) |
| [Designing Datacenter Power Delivery Hierarchies for the AI Era](https://arxiv.org/html/2605.16255v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | `Designing Datacenter Power Delivery Hierarchies for the AI Era` is supported only under the v1-disclosed workload and evaluator behind `4 Datacenter Design Evaluation Framework`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.；3+3+3=9 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`PLATFORM-COST` [章节](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices](https://arxiv.org/html/2605.15206v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期可保留结论是：Local agent execution needs an explicit stop controller that trades expected task value against marginal energy rather than running every trajectory to a fixed cap. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；3+2+3=8 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`AGENT-PLATFORM` [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Quantization Undoes Alignment: Bias Emergence in Compressed LLMs Across Models and Precision Levels](https://arxiv.org/html/2605.15208v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。；2+3+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SkillSmith: Compiling Agent Skills into Boundary-Guided Runtime Interfaces](https://arxiv.org/html/2605.15215v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`AGENT-PLATFORM` [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination](https://arxiv.org/html/2605.15207v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 长期可保留结论是：Sequentially fine-tuning interacting agents invalidates cached-rollout occupancy; resampling and per-agent trust regions make the joint update contract explicit. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。；3+2+3=8 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`AGENT-MULTI-AGENT` [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems](https://arxiv.org/html/2605.15228v1) | 2026-05-17T09:00:00+08:00 ～ 2026-05-18T09:00:00+08:00 | 只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。；3+3+3=9 | 深入完成 | 整合：正文已存在并通过非作者写后复核；`PLATFORM-SECURITY` [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Fair outputs, Biased Internals: Causal Potency and Asymmetry of Latent Bias in LLMs for High-Stakes Decisions](https://arxiv.org/html/2605.15217v1) | 2026-05-18T08:00:00+08:00 | 输出层公平不代表内部 demographic signal 无决策因果力；跨层 activation steering 可使被抑制表示重新改变决策，因此需要重考虑 fairness release gate 是否必须同时包含 output behavior、decodability 与 causal intervention。；3+2+3=8 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Always Learning, Always Mixing: Efficient and Simple Data Mixing All The Time](https://arxiv.org/html/2605.15220v1) | 2026-05-18T08:00:00+08:00 | 静态或分阶段 mixture 在训练阶段切换后会失去当前模型动力学；OP-Mix 用当前 checkpoint 上的低秩 adapter 插值模拟候选 mixture，因此需要把 mixture 从一次性配方重考虑为贯穿 pretraining、midtraining 与 instruction tuning 的 on-policy control。；2+3+2=7 | 深入完成 | 整合：待 root 写入并由非作者复核；`TRAIN-DATA` [章节](../../../../books/part-04-training-system/27-data.md) |
| [ICRL: Learning to Internalize Self-Critique with Reinforcement Learning](https://arxiv.org/html/2605.15224v1) | 2026-05-18T08:00:00+08:00 | 外部 critique 能修正一次回答但不保证能力在移除 critique 后仍存在；ICRL 共享 solver/critic backbone，以 solver 后续增益奖励 critic，并用 distribution calibration 和 role-wise group advantage 转移为无 scaffold solver 能力，因此需要重考虑 self-critique 的训练 ownership。；2+2+2=6 | 深入完成 | 整合：待 root 写入并由非作者复核；`TRAIN-GRPO` [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [Reducing the Safety Tax in LLM Safety Alignment with On-Policy Self-Distillation](https://arxiv.org/html/2605.15239v1) | 2026-05-18T08:00:00+08:00 | 固定安全示范的 off-policy state mismatch 可成为 safety tax 的独立来源；OPSA 在 student 自身 rollout 上用 privileged-context frozen self-teacher 的 token KL，并用 teacher flip rate 选择安全 context，因此需要重考虑安全蒸馏的 occupancy 与监督有效性。；3+2+2=7 | 深入完成 | 整合：待 root 写入并由非作者复核；`TRAIN-SFT` [章节](../../../../books/part-04-training-system/29-sft.md) |
| [Probing Privacy Leaks in LLM-based Code Generation via Test Generation](https://arxiv.org/html/2605.15248v1) | 2026-05-18T08:00:00+08:00 | ad-hoc privacy prompts 不能逼近 PII 在代码 corpus 中的真实使用形态；以 code scenario 生成函数再从 tests 中验证泄漏、并用自动 feature library 提供模板，改变了 code-LLM memorization audit 的 attack surface，因此需要重考虑 privacy red-team 的输入生成合同。；2+2+2=6 | 深入完成 | 整合：待 root 写入并由非作者复核；`PLATFORM-SECURITY` [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [GQLA: Group-Query Latent Attention for Hardware-Adaptive Large Language Model Decoding](https://arxiv.org/html/2605.15250v1) | 2026-05-18T08:00:00+08:00 | 普通 checkpoint 的 MHA/GQA/MQA shape 不能被 runtime 无损切换；GQLA 专门训练一组参数暴露代数等价的 MQA-absorb 与 per-group GQA 两条 decode path，因此需要重考虑 attention state shape 是否能把硬件 compute-bandwidth ratio 与 TP axis 变成运行时选择。；3+3+2=8 | 深入完成 | 整合：待 root 写入并由非作者复核；`MODEL-MULTI-HEAD-ATTENTION` [章节](../../../../books/part-02-model/15-multi-head-attention.md) |
| [GQA-μP: The maximal parameterization update for grouped query attention](https://arxiv.org/html/2605.15290v1) | 2026-05-18T08:00:00+08:00 | 既有 μP 迁移不能假定新 attention 参数矩阵满秩或 repetition factor 不改变尺度；论文给出适配 GQA rank/repetition 的 modified spectral-norm 条件并验证 learning-rate 与 weight-decay transfer，因此需要重考虑 GQA architecture search 中可直接复用的超参数合同。；2+2+3=7 | 深入完成 | 整合：待 root 写入并由非作者复核；`TRAIN-PRETRAINING` [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [PhysBrain 1.0 Technical Report](https://arxiv.org/html/2605.15298v1) | 2026-05-18T08:00:00+08:00 | robot trajectory coverage有限时，可先将 human egocentric video 编译成 scene/dynamics/depth/affordance 的 structured physical supervision，再以 capability-preserving adaptation 迁移到 VLA，因此需要核验 Books 是否已拥有 human-video breadth 到 typed action alignment 的分层数据路线。；2+3+2=7 | 深入完成 | 已有覆盖：命题级比较通过非作者复核；`MULTIMODAL-EMBODIED-VLA` [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Deep Pre-Alignment for VLMs](https://arxiv.org/html/2605.15300v1) | 2026-05-18T08:00:00+08:00 | 轻量 projector 把未对齐 visual features 推入 LLM 后会消耗早层深度并造成语言能力破坏；DPA 让小 VLM perceiver 在入口前完成深层语言空间对齐，因此需要重考虑 projector、perceiver 与 LLM depth 的职责边界。；2+2+2=6 | 深入完成 | 整合：待 root 写入并由非作者复核；`MULTIMODAL-REPRESENTATION` [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [One Pass Is Not Enough: Recursive Latent Refinement for Generative Models](https://arxiv.org/html/2605.15309v1) | 2026-05-18T08:00:00+08:00 | 单次 latent mapping 即使 FID 低也可能牺牲 mode coverage；递归 token mapper 允许推理时增加 refinement cycles 并用 precision/recall 分离 fidelity/coverage，因此需要核验生成范式是否已把 refinement depth 作为可变状态。；2+1+2=5 | 标准完成 | 已有覆盖：命题级比较通过非作者复核；`MULTIMODAL-GENERATIVE-PARADIGMS` [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Video Models Can Reason with Verifiable Rewards](https://arxiv.org/html/2605.15458v1) | 2026-05-18T08:00:00+08:00 | 视频生成 RL 不能把语言模型 token-level GRPO 直接搬到 SDE trajectory；SDE-GRPO、可验证 puzzle reward 和 early-step focus 把 credit 与扩散早期全局结构绑定，因此需要重考虑 video generator 的 RLVR state 与 budget。；2+2+2=6 | 深入完成 | 整合：待 root 写入并由非作者复核；`MULTIMODAL-GENERATIVE-PARADIGMS` [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [When Does Sparse MoE Help in Vision? The Role of Backbone Compute Leverage in Sparse Routing](https://arxiv.org/html/2605.15484v1) | 2026-05-18T08:00:00+08:00 | 稀疏 MoE 的 active-parameter headline 没有说明专家计算在整网 FLOPs 中是否足够大；受控 rho/top-k 实验与 per-sample Soft-MoE 反例表明 backbone compute leverage 和 batch-axis dispatch 可反转 sparse-vs-dense 排序，因此需要重考虑视觉 MoE 的 matched-compute admission。；2+2+2=6 | 深入完成 | 整合：待 root 写入并由非作者复核；`MODEL-MOE` [章节](../../../../books/part-02-model/21-moe.md) |
| [Ghosted Layers: Unconstrained Activation Alignment for Recovering Layer-Pruned LLMs](https://arxiv.org/html/2605.15491v1) | 2026-05-18T08:00:00+08:00 | 整层 pruning 破坏下一 surviving layer 的输入分布，不能只用 pruning score 解释质量损失；Ghosted Layers 从小 calibration set 求闭式线性 boundary operator，因此需要重考虑 layer removal 的恢复 artifact 与校准边界。；2+1+2=5 | 深入完成 | 整合：待 root 写入并由非作者复核；`MODEL-TRANSFORMER-LAYER` [章节](../../../../books/part-02-model/17-transformer-layer.md) |
| [FLASH: Efficient Visuomotor Policy via Sparse Sampling](https://arxiv.org/html/2605.15492v1) | 2026-05-18T08:00:00+08:00 | 离散 action chunk 与多步 diffusion 把 horizon、inference cadence 和 controller sampling 紧耦合；FLASH 用连续 Legendre 系数、稀疏时间拟合和 history-anchored single-step flow 分离表示 horizon、生成次数与执行频率，因此需要重考虑 VLA action representation 到低层控制器的接口。；2+3+2=7 | 深入完成 | 整合：待 root 写入并由非作者复核；`MULTIMODAL-EMBODIED-VLA` [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Can We Trust AI-Inferred User States. A Psychometric Framework for Validating the Reliability of Users States Classification by LLMs in Operational Environments](https://arxiv.org/html/2605.15734v1) | 2026-05-18T08:00:00+08:00 | 聚合后稳定的 inferred user-state metric 不能自动支持个体实时 adaptation；三种 bimodal LLM 的重复测量仅 31/213 指标达到标准，因此 evaluation 必须分别验收 individual reliability 与 post-hoc aggregate utility。；2+1+2=5 | 标准完成 | 已有覆盖：命题级比较通过非作者复核；`PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Look Before You Leap: Autonomous Exploration for LLM Agents](https://arxiv.org/html/2605.16143v1) | 2026-05-18T08:00:00+08:00 | task-only RL 会过早 exploitation；独立 exploration rollout、ECC coverage 与 Explore-then-Act 把信息收集预算和任务执行分离，因此需要核验 Planning 是否已拥有 evidence-gathering action 与提交 action 的分权。；2+2+2=6 | 标准完成 | 已有覆盖：命题级比较通过非作者复核；`AGENT-PLANNING` [章节](../../../../books/part-07-agent/79-planning.md) |
| [Second-Order Multi-Level Variance Correction for Modality Competition in Multimodal Models](https://arxiv.org/html/2605.16165v1) | 2026-05-18T08:00:00+08:00 | 统一 next-token objective 不保证图像与文本梯度在大 batch 下共享稳定尺度；Fisher-orthogonal projection 与 multi-level folding 把 modality variance 变成可诊断、可校正的 optimizer state，因此需要重考虑 multimodal pretraining 的 large-batch optimizer branch。；2+2+2=6 | 深入完成 | 整合：待 root 写入并由非作者复核；`TRAIN-PRETRAINING` [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast](https://arxiv.org/html/2605.16233v1) | 2026-05-18T08:00:00+08:00 | 单流 Reflexion 会把每条轨迹困在局部经验中；FORGE 将 failure-derived prompt memory 放入 population stages，由 champion broadcast 扩散且以 graduation 冻结实例，因此需要重考虑 memory promotion 的群体传播、成本停止与污染半径。；2+2+2=6 | 深入完成 | 整合：待 root 写入并由非作者复核；`AGENT-MEMORY` [章节](../../../../books/part-07-agent/77-memory.md) |
| [Offline Semantic Guidance for Efficient Vision-Language-Action Policy Distillation](https://arxiv.org/html/2605.16241v1) | 2026-05-18T08:00:00+08:00 | 只模仿 teacher action 会把动作噪声写入小 student；VLA-AD 将 phase anchor 和多帧方向作为仅训练期语义监督、部署时完全移除 teacher/VLM，因此需要核验 Books 是否已拥有 privileged teacher 与独立 runtime student 的边界。；2+2+2=6 | 标准完成 | 已有覆盖：命题级比较通过非作者复核；`MULTIMODAL-EMBODIED-VLA` [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |

## 4. 证据与知识整合

64 项的结构化 evidence route、精确版本、评分和 claim boundary 见 [`evidence-review-v3.json`](../_sources/daily-20260518/evidence-review-v3.json)。38 项 reuse 的逐项原 locator/version/claim 对照另见 [`evidence-reuse-replay-v3.json`](../_sources/daily-20260518/evidence-reuse-replay-v3.json)。以下保留每项实际证据判断，不以“已读全文”替代机制、评价和未证明边界。

### [SDOF: Taming the Alignment Tax in Multi-Agent Orchestration with State-Constrained Dispatch](https://arxiv.org/html/2605.15204v1)

<!-- review:SF-2026-ARXIV-2605-15204:start -->
<!-- claim:SF-2026-ARXIV-2605-15204:start -->
- **Problem:** Multi-agent orchestration frameworks such as LangChain, LangGraph, and CrewAI route tasks through graph-based pipelines but do not enforce the stage constraints that govern real business processes.
- **Old path / changed constraint:** However, in their native forms they do not expose business-stage legality as an explicit runtime contract of the kind evaluated here.
- **Mechanism / ownership:** We present SDOF, a framework that treats multi-agent execution as a constrained state machine.
- **Evaluation contract:** Our GSPO-aligned 7B Intent Router achieves higher joint accuracy than zero-shot GPT-4o on this FSM-constrained adversarial routing benchmark (80.9% versus 48.9%).
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** Violations cause compliance failures, data corruption, and legal risk.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.15204v1](https://arxiv.org/abs/2605.15204v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.15204v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-15204:end -->
<!-- review:SF-2026-ARXIV-2605-15204:end -->

### [Hydra: Efficient, Correct Code Generation via Checkpoint-and-Rollback Support](https://arxiv.org/html/2605.15238v1)

<!-- review:SF-2026-ARXIV-2605-15238:start -->
问题与演进：代码生成可把 incremental compiler checker 作为异步 sensor，并用 checkpoint/rollback 保留已验证前缀；compiler 只拥有 static-correctness feedback，不拥有 task correctness。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15238v1 §3 Hydra Overview; §4 Design; §5 Incremental Checker — mechanism boundary: Large language models are increasingly used for code generation, but many generated programs fail to compile, a prerequisite for further correctness checks such as unit tests.`。

Evaluation：`https://arxiv.org/html/2605.15238v1 §7 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15238v1 §8 Discussion — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15238v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15238:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15238:end -->
<!-- review:SF-2026-ARXIV-2605-15238:end -->

### [Training on Documents About Monitoring Leads to CoT Obfuscation](https://arxiv.org/html/2605.15257v1)

<!-- review:SF-2026-ARXIV-2605-15257:start -->
问题与演进：CoT monitor 进入训练分布后，模型可能学习 monitor-aware obfuscation；监控合同必须包含 adaptive exposure、外部 signals 与不可由被监控模型控制的 escalation。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15257v1 §2 Experimental Design — mechanism boundary: Chain-of-thought (CoT) monitoring is one of the most promising tools we have for detecting model misbehavior, but its effectiveness depends on models faithfully externalizing their reasoning.`。

Evaluation：`https://arxiv.org/html/2605.15257v1 §3 Results and Discussion — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15257v1 §5 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15257v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15257:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15257:end -->
<!-- review:SF-2026-ARXIV-2605-15257:end -->

### [Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](https://arxiv.org/html/2605.15338v1)

<!-- review:SF-2026-ARXIV-2605-15338:start -->
问题与演进：memory poisoning 可延迟触发并跨 session 重放；write admission、provenance、activation-time policy 与 expiry 必须共同拥有防线。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15338v1 §3 Sleeper Memory Poisoning Threat Model — mechanism boundary: Large language models are increasingly augmented with persistent memory, allowing assistants to store user-specific information across sessions for personalization and continuity.`。

Evaluation：`https://arxiv.org/html/2605.15338v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15338v1 Appendix A Limitations and Impact — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15338v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15338:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15338:end -->
<!-- review:SF-2026-ARXIV-2605-15338:end -->

### [Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute](https://arxiv.org/html/2605.15377v1)

<!-- review:SF-2026-ARXIV-2605-15377:start -->
问题与演进：AI control monitoring 应优先组合异质 signal 以降低共同盲区，而非只增加同类 monitor compute；ensemble 自身仍需校准、correlation audit 与独立 stop authority。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15377v1 §3 Ensemble Monitoring Method — mechanism boundary: As AI systems are increasingly deployed in autonomous agentic settings at scale, it is important to ensure the actions they take are safe and aligned with user intent.`。

Evaluation：`https://arxiv.org/html/2605.15377v1 §4–§6 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15377v1 §6.3 Limitations and Future Work — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15377v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15377:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15377:end -->
<!-- review:SF-2026-ARXIV-2605-15377:end -->

### [Is One Score Enough? Rethinking the Evaluation of Sequentially Evolving LLM Memory](https://arxiv.org/html/2605.15384v1)

<!-- review:SF-2026-ARXIV-2605-15384:start -->
问题与演进：顺序演化 memory 的评测必须把 acquisition、retention、forgetting、transfer 与 interference 分成时间序列诊断，不能由最终平均分掩盖负迁移。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15384v1 §3 SeqMem-Eval — mechanism boundary: Memory plays a central role in enabling large language models (LLMs) to operate over sequential tasks by accumulating and reusing experience over time.`。

Evaluation：`https://arxiv.org/html/2605.15384v1 §4–§6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15384v1 Appendix G Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15384v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15384:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15384:end -->
<!-- review:SF-2026-ARXIV-2605-15384:end -->

### [$ϕ$-Balancing for Mixture-of-Experts Training](https://arxiv.org/html/2605.15403v1)

<!-- review:SF-2026-ARXIV-2605-15403:start -->
问题与演进：MoE balance controller 应估计 population-level routing distribution，而不是把 noisy mini-batch count 当真值；EMA/mirror-descent bias correction换来更稳定利用率，也新增 lag 与非平稳漂移。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15403v1 §3 φ-balancing objective and mirror-descent controller — mechanism boundary: Mixture-of-Experts (MoE) models rely on balanced expert utilization to fully realize their scalability.`。

Evaluation：`https://arxiv.org/html/2605.15403v1 §4 Pretraining/fine-tuning evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15403v1 §5 Limitations and topology/workload boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15403v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15403:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15403:end -->
<!-- review:SF-2026-ARXIV-2605-15403:end -->

### [DualKV: Shared-Prompt Flash Attention for Efficient RL Training with Large Rollouts and Long Contexts](https://arxiv.org/html/2605.15422v1)

<!-- review:SF-2026-ARXIV-2605-15422:start -->
问题与演进：共享 prompt 的大 rollout RL 训练可将 prompt K/V 与 response K/V 分开复用并保持 causal gradient；收益必须绑定 N、P、R、kernel 与 backward contract。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15422v1 §3–§4 DualKV — mechanism boundary: Modern RL post-training methods such as GRPO and DAPO train on N response sequences of R tokens sampled from a shared prompt of P tokens, but standard FlashAttention replicates all P prompt tokens N times across both forward and backward passes -- duplicating compute and memory on identical hidden states.`。

Evaluation：`https://arxiv.org/html/2605.15422v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15422v1 §6 Conclusion and disclosed workload/hardware boundary; no dedicated limitations section — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15422v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15422:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15422:end -->
<!-- review:SF-2026-ARXIV-2605-15422:end -->

### [Runtime-Structured Task Decomposition for Agentic Coding Systems](https://arxiv.org/html/2605.15425v1)

<!-- review:SF-2026-ARXIV-2605-15425:start -->
问题与演进：Agent coding workflow 应把 task decomposition、branch/retry与schema validation移出 monolithic prompt，交给 executable runtime；LLM只拥有局部判断，不拥有全局控制流提交。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15425v1 §3 Runtime-structured decomposition architecture — mechanism boundary: Agentic coding systems increasingly use large language models (LLMs) for software engineering tasks such as debugging, root cause analysis, and code review.`。

Evaluation：`https://arxiv.org/html/2605.15425v1 §4 Monolithic/static/runtime comparison — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15425v1 §5 Limitations and two-workload/three-configuration boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15425v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15425:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15425:end -->
<!-- review:SF-2026-ARXIV-2605-15425:end -->

### [Entity-Centric World Models: Interaction-Aware Masking for Causal Video Prediction](https://arxiv.org/html/2605.15466v1)

<!-- review:SF-2026-ARXIV-2605-15466:start -->
问题与演进：predictive representation只有在 masking 聚焦 entity interaction且用 causal reasoning/action outcome验证时才接近 world-state signal；重建 latent trajectory仍不自动获得控制充分性。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15466v1 §3 Interaction-Aware JEPA motion/entity masking — mechanism boundary: Learning predictive world models from unlabelled video is a foundational challenge in artificial intelligence.`。

Evaluation：`https://arxiv.org/html/2605.15466v1 §4 CLEVRER causal evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15466v1 §5 Limitations and synthetic-video/action boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15466v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15466:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15466:end -->
<!-- review:SF-2026-ARXIV-2605-15466:end -->

### [EgoExo-WM: Unlocking Exo Video for Ego World Models](https://arxiv.org/html/2605.15477v1)

<!-- review:SF-2026-ARXIV-2605-15477:start -->
问题与演进：exo video要服务 ego world model，必须先恢复body pose/action schema并显式转换视角；数据扩容收益依赖action identity与ego observation对齐，不能把普通视频直接当控制轨迹。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15477v1 §3 Exo-to-ego conversion and action representation — mechanism boundary: Egocentric world models present a promising direction for enabling agents to predict and plan, but their performance is constrained by the limited availability of egocentric training data and its inherent partial observability of humans' physical actions.`。

Evaluation：`https://arxiv.org/html/2605.15477v1 §4 Prediction/planning evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15477v1 §5 Limitations and pose/kinematics/domain boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15477v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15477:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15477:end -->
<!-- review:SF-2026-ARXIV-2605-15477:end -->

### [STS: Efficient Sparse Attention with Speculative Token Sparsity](https://arxiv.org/html/2605.15508v1)

<!-- review:SF-2026-ARXIV-2605-15508:start -->
问题与约束：The quadratic complexity of attention imposes severe memory and computational bottlenecks on Large Language Model (LLM) inference.

机制与 ownership：We propose STS, a sparse attention mechanism that requires no model retraining.

Evaluation contract：Our evaluation shows that STS achieves a 2.67x speedup operating at approximately 90% sparsity on representative benchmark NarrativeQA, maintaining negligible accuracy degradation compared to dense attention.

Trade-off / failure：The mechanism described in `4 STS Design` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15508:start -->`STS: Efficient Sparse Attention with Speculative Token Sparsity` is supported only under the v1-disclosed workload and evaluator behind `6 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15508:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15508`。
<!-- review:SF-2026-ARXIV-2605-15508:end -->

### [RoPE Distinguishes Neither Positions Nor Tokens in Long Contexts, Provably](https://arxiv.org/html/2605.15514v1)

<!-- review:SF-2026-ARXIV-2605-15514:start -->
问题与约束：We identify intrinsic limitations of Rotary Positional Embeddings (RoPE) in Transformer-based long-context language models.

机制与 ownership：We identify intrinsic limitations of Rotary Positional Embeddings (RoPE) in Transformer-based long-context language models.

Evaluation contract：Our empirical analysis shows that multi-head, multi-layer architectures are insufficient to overcome these limitations.

Trade-off / failure：The mechanism described in `§§3–5 — four RoPE failure modes and multilayer/multihead extension` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§6 Conclusion and Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15514:start -->`RoPE Distinguishes Neither Positions Nor Tokens in Long Contexts, Provably` is supported only under the v1-disclosed workload and evaluator behind `§§3.1 and 5 — empirical verification and indexing-task evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15514:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15514`。
<!-- review:SF-2026-ARXIV-2605-15514:end -->

### [On the Fragility of Data Attribution When Learning Is Distributed](https://arxiv.org/html/2605.15520v1)

<!-- review:SF-2026-ARXIV-2605-15520:start -->
问题与约束：Data attribution has become an important component of pricing, auditing, and governance in machine learning pipelines, yet most attribution methods implicitly assume that attribution values faithfully reflect participants' contributions.

机制与 ownership：We show that this assumption can fail: a single participant in a standard distributed training workflow can substantially inflate its measured attribution value while preserving global utility.

Evaluation contract：We show that this assumption can fail: a single participant in a standard distributed training workflow can substantially inflate its measured attribution value while preserving global utility.

Trade-off / failure：The mechanism described in `§3 Latent Optimization Attack` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§§5–6 Defenses and Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15520:start -->`On the Fragility of Data Attribution When Learning Is Distributed` is supported only under the v1-disclosed workload and evaluator behind `§4 Experimental Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15520:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15520`。
<!-- review:SF-2026-ARXIV-2605-15520:end -->

### [Process Rewards with Learned Reliability](https://arxiv.org/html/2605.15529v1)

<!-- review:SF-2026-ARXIV-2605-15529:start -->
问题与约束：A scalar process reward discards the evidence quantity behind finite Monte-Carlo success counts, so downstream allocation cannot distinguish high reward with strong support from high reward with weak support.

机制与 ownership：BetaPRM preserves (K,N) count evidence in a Beta-Binomial objective and exposes mean plus concentration; the ACA controller owns risk-adjusted ranking, stopping, and repair.

Evaluation contract：The evidence is limited to the disclosed VisualPRM count supervision, four visual-math benchmarks, four backbones, and the author candidate pools and judges; hardware for the main training runs is not fully disclosed.

Trade-off / failure：Preserving counts raises rollout, judge, and storage cost; miscalibration can cause confident-wrong early stops, while conservative control loses the compute benefit.

旧路径与共存边界：Scalar PRMs and fixed Best-of-N remain reasonable when counts are unavailable, the scorer is uncalibrated, or predictable latency is more valuable than adaptive allocation.

<!-- claim:SF-2026-ARXIV-2605-15529:start -->Concentration is learned evidence reliability under the continuation generator and judge, not calibrated epistemic truth or a frequentist confidence interval.<!-- claim:SF-2026-ARXIV-2605-15529:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15529`。
<!-- review:SF-2026-ARXIV-2605-15529:end -->

### [AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs](https://arxiv.org/html/2605.15565v1)

<!-- review:SF-2026-ARXIV-2605-15565:start -->
问题与约束：Existing LLM RL systems support some of these capabilities, but each new extension often requires dedicated system engineering.

机制与 ownership：To address these limitations, we propose AstraFlow, a dataflow-oriented RL system that replaces conventional trainer-centered control with principled component abstractions.

Evaluation contract：We evaluate AstraFlow across math, code, search, and AgentBench workloads, showing that the same system supports multi-policy training, elastic scaling, heterogeneous cross-region execution, and composable data algorithms without system-level code changes.

Trade-off / failure：The mechanism described in `§3 Dataflow-Oriented RL for Agentic LLMs` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15565:start -->`AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs` is supported only under the v1-disclosed workload and evaluator behind `§4 Evaluation: Applications of AstraFlow`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15565:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15565`。
<!-- review:SF-2026-ARXIV-2605-15565:end -->

### [Response-Conditioned Parallel-to-Sequential Orchestration for Multi-Agent Systems](https://arxiv.org/html/2605.15573v1)

<!-- review:SF-2026-ARXIV-2605-15573:start -->
问题与约束：Existing collaboration frameworks typically operate in either a parallel or a sequential mode.

机制与 ownership：In this work, we introduce a hybrid paradigm called Nexa, a trainable response-conditioned policy that bridges the gap between the two modes.

Evaluation contract：We formalize this hybrid execution problem, show that the resulting graph is acyclic by construction, and that the framework strictly subsumes pure parallel execution, and present a training procedure based on policy-gradient optimization.

Trade-off / failure：The mechanism described in `2 Problem Formulation and Preliminaries` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `6 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15573:start -->`Response-Conditioned Parallel-to-Sequential Orchestration for Multi-Agent Systems` is supported only under the v1-disclosed workload and evaluator behind `4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15573:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15573`。
<!-- review:SF-2026-ARXIV-2605-15573:end -->

### [STAR: A Stage-attributed Triage and Repair framework for RCA Agents in Microservices](https://arxiv.org/html/2605.15581v1)

<!-- review:SF-2026-ARXIV-2605-15581:start -->
问题与约束：However, their reliability remains fragile: an error in early evidence collection, hypothesis formulation, or causal analysis can propagate through the reasoning trace and eventually corrupt the final diagnosis.

机制与 ownership：In this paper, we present \textbf{STAR}, a \emph{Stage-attributed Triage and Repair} framework for repairing erroneous RCA traces.

Evaluation contract：We evaluate STAR on a public large-scale benchmark and a real-world production dataset, using two RCA agent workflows and three foundation models.

Trade-off / failure：The mechanism described in `§IV Methodology` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§§VI–VII Discussion/Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15581:start -->`STAR: A Stage-attributed Triage and Repair framework for RCA Agents in Microservices` is supported only under the v1-disclosed workload and evaluator behind `§V Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15581:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15581`。
<!-- review:SF-2026-ARXIV-2605-15581:end -->

### [PSD: Pushing the Pareto Frontier of Diffusion LLMs via Parallel Speculative Decoding](https://arxiv.org/html/2605.15609v1)

<!-- review:SF-2026-ARXIV-2605-15609:start -->
问题与约束：Diffusion large language models (dLLMs) generate text by iteratively denoising masked token sequences.

机制与 ownership：We propose Parallel Speculative Decoding (PSD), a training-free framework that jointly improves inference along both axes.

Evaluation contract：Experiments on three dLLMs across reasoning and code generation tasks show that PSD achieves favorable trade-offs between inference efficiency and generation quality, reaching up to $5.5\times$ tokens per forward pass with accuracy comparable to greedy decoding.

Trade-off / failure：The mechanism described in `3 Methodology` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `6 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15609:start -->`PSD: Pushing the Pareto Frontier of Diffusion LLMs via Parallel Speculative Decoding` is supported only under the v1-disclosed workload and evaluator behind `4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15609:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15609`。
<!-- review:SF-2026-ARXIV-2605-15609:end -->

### [A Few GPUs, A Whole Lotta Scale: Faithful LLM Training Emulation with PrismLLM](https://arxiv.org/html/2605.15617v1)

<!-- review:SF-2026-ARXIV-2605-15617:start -->
问题与约束：Large language model (LLM) training today runs on clusters spanning thousands of GPUs.

机制与 ownership：We present PrismLLM to decouple large-scale execution from the need to access large clusters, enabling engineers to run and observe ranks of interest under faithful large-scale behavior using only a few GPUs.

Evaluation contract：This is because engineers often need to reproduce production behaviors to diagnose failures or evaluate optimizations, thereby demanding frequent and even exclusive access to production-scale clusters -- which becomes increasingly hard given that the majority of GPUs are already committed to production workloads.

Trade-off / failure：The mechanism described in `§§4–7 PrismLLM design, graph construction and hybrid emulation` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§§9–10 Discussion and Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15617:start -->`A Few GPUs, A Whole Lotta Scale: Faithful LLM Training Emulation with PrismLLM` is supported only under the v1-disclosed workload and evaluator behind `§8 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15617:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15617`。
<!-- review:SF-2026-ARXIV-2605-15617:end -->

### [Latent Video Prediction Learns Better World Models](https://arxiv.org/html/2605.15618v1)

<!-- review:SF-2026-ARXIV-2605-15618:start -->
问题与约束：Self-supervised video models are increasingly framed as world models, yet their evaluation remains largely confined to a single top-1 accuracy score on clean benchmarks.

机制与 ownership：We present the first systematic study addressing this gap, analyzing four matched-capacity frontier video foundation models, V-JEPA 2.1, V-JEPA 2, VideoPrism, and VideoMAEv2, across five robustness axes relevant to their deployment as video world models: feature discriminability, corruption robustness, fine-grained discrimination, occlusion robustness, and sensitivity to temporal direction.

Evaluation contract：Self-supervised video models are increasingly framed as world models, yet their evaluation remains largely confined to a single top-1 accuracy score on clean benchmarks.

Trade-off / failure：The mechanism described in `§3 Evaluation framework` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§10 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15618:start -->`Latent Video Prediction Learns Better World Models` is supported only under the v1-disclosed workload and evaluator behind `§§4–9 representation, corruption, physics and prediction evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15618:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15618`。
<!-- review:SF-2026-ARXIV-2605-15618:end -->

### [Rethinking the Security of DP-SGD: A Corrected Analysis of Differentially Private Machine Learning](https://arxiv.org/html/2605.15648v1)

<!-- review:SF-2026-ARXIV-2605-15648:start -->
问题与约束：Existing analyses often model DP-SGD and its variants as the Subsampled Gaussian Mechanism (SGM), where Gaussian noise is added to the sum of clipped gradients computed from a Poisson-sampled batch.

机制与 ownership：We identify a mismatch between this formal analysis and common DP-SGD implementations.

Evaluation contract：Our theoretical results show that these guarantees can be weaker than the standard SGM-based guarantee, implying that the true privacy leakage may exceed the reported guarantee in some regimes.

Trade-off / failure：The mechanism described in `§3 Privacy Analysis of EASGM and ASGM` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§7 Conclusion and Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15648:start -->`Rethinking the Security of DP-SGD: A Corrected Analysis of Differentially Private Machine Learning` is supported only under the v1-disclosed workload and evaluator behind `§§4–6 auditing and experimental comparison`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15648:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15648`。
<!-- review:SF-2026-ARXIV-2605-15648:end -->

### [PRISM: Prompt Reliability via Iterative Simulation and Monitoring for Enterprise Conversational AI](https://arxiv.org/html/2605.15665v1)

<!-- review:SF-2026-ARXIV-2605-15665:start -->
问题与约束：Existing prompt optimization frameworks address prompt quality as a one-time compile-time problem, leaving open the equally critical question of how to detect and repair prompt regressions caused by silent LLM behavior changes over time.

机制与 ownership：We present PRISM (Prompt Reliability via Iterative Simulation and Monitoring), a closed-loop framework that treats prompt engineering as a continuous reliability engineering problem rather than a one-time authorship task.

Evaluation contract：It automatically generates test cases from requirements, simulates full multi-turn conversations against a platform-faithful LLM environment, evaluates pass/fail using an LLM-as-judge, diagnoses root causes of failures, and surgically repairs the prompt -- iterating until all tests pass.

Trade-off / failure：The mechanism described in `§4 The PRISM Framework` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§7 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15665:start -->`PRISM: Prompt Reliability via Iterative Simulation and Monitoring for Enterprise Conversational AI` is supported only under the v1-disclosed workload and evaluator behind `§5 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15665:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15665`。
<!-- review:SF-2026-ARXIV-2605-15665:end -->

### [Going Beyond the Edge: Distributed Inference of Transformer Models on Ultra-Low-Power Wireless Devices](https://arxiv.org/html/2605.15694v1)

<!-- review:SF-2026-ARXIV-2605-15694:start -->
问题与约束：Transformer models are rapidly becoming a cornerstone of modern Internet of Things (IoT) applications, yet their computational and memory demands far exceed the capabilities of a single typical ultra-low-power IoT device.

机制与 ownership：We present CATS, a framework for distributed transformer inference on ultra-low-power wireless devices, enabling multiple devices to collaboratively execute models far larger than what a single device can sustain.

Evaluation contract：In real-world experiments, we show that CATS brings distributed transformer inference to ultra-low-power wireless devices for the first time, with deployments on up to 16 devices that collaboratively execute transformer models up to 14 times larger than what a single device can run.

Trade-off / failure：The mechanism at `PDF pp.1–5 — CATS communication-aware training/partitioning, SomeGather, message-dropout` trades added coordination/metadata/runtime work against the measured benefit; `PDF pp.1,7–8 — C1/C2/C3 scope, packet-loss and mesh/resource boundaries` bounds any extrapolation.

旧路径与共存边界：The prior design remains valid outside the exact-v1 workload or when the new coordination and verification costs dominate.

<!-- claim:SF-2026-ARXIV-2605-15694:start -->`Going Beyond the Edge: Distributed Inference of Transformer Models on Ultra-Low-Power Wireless Devices` is supported only by the exact-v1 PDF's disclosed workload and evaluator; undisclosed deployment fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15694:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15694`。
<!-- review:SF-2026-ARXIV-2605-15694:end -->

### [SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory](https://arxiv.org/html/2605.15710v1)

<!-- review:SF-2026-ARXIV-2605-15710:start -->
问题与约束：Existing benchmarks for multimodal memory reasoning largely evaluate systems within pre-assembled contexts, but under-evaluate whether agents can use evidence distributed across independently originated sources.

机制与 ownership：To address this gap, we introduce Source-distributed Multimodal Memory Benchmark(SMMBench), which measures whether agents can retrieve, align, and compose multimodal evidence scattered across multiple sources rather than reason within a single curated context.

Evaluation contract：Existing benchmarks for multimodal memory reasoning largely evaluate systems within pre-assembled contexts, but under-evaluate whether agents can use evidence distributed across independently originated sources.

Trade-off / failure：The mechanism described in `§3 SMMBench Benchmark` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15710:start -->`SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiment`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15710:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15710`。
<!-- review:SF-2026-ARXIV-2605-15710:end -->

### [A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation](https://arxiv.org/html/2605.15761v1)

<!-- review:SF-2026-ARXIV-2605-15761:start -->
问题与约束：Evaluation leaderboards such as LMArena play a central role in benchmarking large language models by aggregating pairwise human preferences into model rankings, yet the robustness of these rankings remains poorly understood.

机制与 ownership：We present a unified perturbation framework for analyzing Bradley-Terry leaderboards under structured data modifications using influence-based approximations.

Evaluation contract：Evaluation leaderboards such as LMArena play a central role in benchmarking large language models by aggregating pairwise human preferences into model rankings, yet the robustness of these rankings remains poorly understood.

Trade-off / failure：The mechanism described in `§3 Influence Framework` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§6 Conclusion, limitations, and future work` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15761:start -->`A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15761:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15761`。
<!-- review:SF-2026-ARXIV-2605-15761:end -->

### [SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?](https://arxiv.org/html/2605.15777v1)

<!-- review:SF-2026-ARXIV-2605-15777:start -->
问题与约束：However, existing web and GUI agent benchmarks often rely on simplified settings, isolated tasks, or short-horizon interactions, making it difficult to assess capabilities of agents in realistic professional workflows.

机制与 ownership：To this end, we introduce SaaS-Bench, a benchmark built on 23 deployable SaaS systems across six professional domains, containing 106 tasks grounded in realistic work scenarios.

Evaluation contract：However, existing web and GUI agent benchmarks often rely on simplified settings, isolated tasks, or short-horizon interactions, making it difficult to assess capabilities of agents in realistic professional workflows.

Trade-off / failure：The mechanism described in `§3 SaaS-Bench construction and protocol` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15777:start -->`SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiment`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15777:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15777`。
<!-- review:SF-2026-ARXIV-2605-15777:end -->

### [BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge](https://arxiv.org/html/2605.15815v1)

<!-- review:SF-2026-ARXIV-2605-15815:start -->
问题与约束：This process requires substantial trial-and-error exploration, yet the resulting knowledge--resolved dependencies, repair strategies--stays trapped in a single conversation, unavailable to future agents.

机制与 ownership：This process requires substantial trial-and-error exploration, yet the resulting knowledge--resolved dependencies, repair strategies--stays trapped in a single conversation, unavailable to future agents.

Evaluation contract：Experiments on three benchmarks show that BootstrapAgent achieves a 92.9% success rate, outperforming the baseline by over 10% while reducing downstream agent token usage by 25.9% and build time by 22.3%.

Trade-off / failure：The mechanism described in `3.1 Problem Formulation` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `5 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15815:start -->`BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge` is supported only under the v1-disclosed workload and evaluator behind `4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15815:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15815`。
<!-- review:SF-2026-ARXIV-2605-15815:end -->

### [RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades](https://arxiv.org/html/2605.15846v1)

<!-- review:SF-2026-ARXIV-2605-15846:start -->
问题与约束：However, most existing benchmarks focus predominantly on single-issue bug fixes from Python repositories, with coarse pass/fail evaluation outcomes, and thus fail to capture long-horizon, multi-target development at real engineering scale.

机制与 ownership：To address this gap, we present RoadmapBench, a benchmark of 115 long-horizon coding tasks grounded in real open-source version upgrades across 17 repositories and 5 programming languages.

Evaluation contract：However, most existing benchmarks focus predominantly on single-issue bug fixes from Python repositories, with coarse pass/fail evaluation outcomes, and thus fail to capture long-horizon, multi-target development at real engineering scale.

Trade-off / failure：The mechanism described in `§3 RoadmapBench` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§§5–6 Discussion and Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15846:start -->`RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15846:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15846`。
<!-- review:SF-2026-ARXIV-2605-15846:end -->

### [To GPU or Not to GPU: Vector Search in Relational Engines](https://arxiv.org/html/2605.15957v1)

<!-- review:SF-2026-ARXIV-2605-15957:start -->
问题与约束：However, while vector search is a common feature in AI/ML/LLMs where the dominant computing platforms are GPUs, existing database engines operate on CPUs even when implementing vector search.

机制与 ownership：Second, we develop a modular execution engine that can run SQL+VS queries across CPU and GPU.

Evaluation contract：First, we extend the TPC-H benchmark with vector data (from text and images) and propose a number of representative SQL+VS queries.

Trade-off / failure：The mechanism described in `§4 MaxVec Engine and §5 modular CPU/GPU execution` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§6 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15957:start -->`To GPU or Not to GPU: Vector Search in Relational Engines` is supported only under the v1-disclosed workload and evaluator behind `§§3 and 5 Vec-H/operator evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15957:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15957`。
<!-- review:SF-2026-ARXIV-2605-15957:end -->

### [Imperfect World Models are Exploitable](https://arxiv.org/html/2605.15960v1)

<!-- review:SF-2026-ARXIV-2605-15960:start -->
问题与约束：We propose a novel definition of model exploitation in reinforcement learning.

机制与 ownership：We propose a novel definition of model exploitation in reinforcement learning.

Evaluation contract：We analogize our definition with a prior characterization of reward hacking but show that the associated proof of inevitability does not transfer to exploitation.

Trade-off / failure：The mechanism described in `§§2.2–3 model-exploitation definitions and results` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15960:start -->`Imperfect World Models are Exploitable` is supported only under the v1-disclosed workload and evaluator behind `§3 Results`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15960:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15960`。
<!-- review:SF-2026-ARXIV-2605-15960:end -->

### [Deterministic Event-Graph Substrates as World Models for Counterfactual Reasoning](https://arxiv.org/html/2605.15967v1)

<!-- review:SF-2026-ARXIV-2605-15967:start -->
问题与约束：We study event-graph substrates: a class of world models that represent agent state as an append-only log of typed RDF triples and answer counterfactual queries by forking the log under a structured intervention vocabulary.

机制与 ownership：Substrates are inspectable at the triple level, support exact counterfactuals, and transfer across domains without learned components.

Evaluation contract：We formalize the class, prove a duality between explanatory and counterfactual queries that reduces both to the same causal-ancestor traversal, and evaluate a 1,400-line CLEVRER-DSL interpreter atop a domain-agnostic substrate runtime at full CLEVRER validation scale (n=75,618).

Trade-off / failure：The mechanism described in `4.2 Implementation per subset` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15967:start -->`Deterministic Event-Graph Substrates as World Models for Counterfactual Reasoning` is supported only under the v1-disclosed workload and evaluator behind `Summary of empirical findings.`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15967:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15967`。
<!-- review:SF-2026-ARXIV-2605-15967:end -->

### [Who Owns This Agent? Tracing AI Agents Back to Their Owners](https://arxiv.org/html/2605.16035v1)

<!-- review:SF-2026-ARXIV-2605-16035:start -->
问题与约束：AI agents are increasingly deployed to act autonomously in the world, yet there is still no reliable way to trace a harmful agent back to the account that deployed it.

机制与 ownership：For adversarial operators who filter or paraphrase incoming content, we develop robust canary constructions that cannot be suppressed without degrading the agent's own task performance, yielding a formal asymmetry in the defender's favor.

Evaluation contract：We evaluate a variety of scenarios including real-world agents and show that our attribution method is reliable, robust, and scalable for vendor-side deployment.

Trade-off / failure：The mechanism described in `§4 The Agent Attribution Protocol` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§7 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16035:start -->`Who Owns This Agent? Tracing AI Agents Back to Their Owners` is supported only under the v1-disclosed workload and evaluator behind `§6 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16035:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16035`。
<!-- review:SF-2026-ARXIV-2605-16035:end -->

### [Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking](https://arxiv.org/html/2605.16154v1)

<!-- review:SF-2026-ARXIV-2605-16154:start -->
问题与约束：However, GRPO assigns the same advantage to every chunk in a rollout.

机制与 ownership：A natural response has been to speed rollout collection through faster simulators and world models.

Evaluation contract：We formalize per-phase gradient variance as the quantity determines where gradient computation is useful and show that success-failure action variance provides a measurable proxy for it.

Trade-off / failure：The mechanism described in `§4 Probabilistic Chunk Masking` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5.2 Results and Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16154:start -->`Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking` is supported only under the v1-disclosed workload and evaluator behind `§5 Empirical Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16154:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16154`。
<!-- review:SF-2026-ARXIV-2605-16154:end -->

### [Runtime-Orchestrated Second-Order Optimization for Scalable LLM Training](https://arxiv.org/html/2605.16184v1)

<!-- review:SF-2026-ARXIV-2605-16184:start -->
问题与约束：We introduce \textbf{Asteria}, a runtime system designed to remove this bottleneck by separating second-order optimization logic from the critical GPU training path.

机制与 ownership：We introduce \textbf{Asteria}, a runtime system designed to remove this bottleneck by separating second-order optimization logic from the critical GPU training path.

Evaluation contract：We evaluate Asteria on both memory-constrained and distributed training settings.

Trade-off / failure：The mechanism described in `§III System Design and Methodology` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§V Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16184:start -->`Runtime-Orchestrated Second-Order Optimization for Scalable LLM Training` is supported only under the v1-disclosed workload and evaluator behind `§IV Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16184:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16184`。
<!-- review:SF-2026-ARXIV-2605-16184:end -->

### [Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems](https://arxiv.org/html/2605.16198v1)

<!-- review:SF-2026-ARXIV-2605-16198:start -->
问题与约束：We examine one particular dimension of AI governance: how to monitor and audit AI-enabled products and services throughout the AI development lifecycle, from pre-deployment testing to post-deployment auditing.

机制与 ownership：Combining principles from formal methods with SoTA machine learning, we propose techniques that enable AI-enabled product and service developers, as well as third party AI developers and evaluators, to perform offline auditing and online (runtime) monitoring of product-specific (temporally extended) behavioral constraints such as safety constraints, norms, rules and regulations with respect to black-box advanced AI systems, notably LLMs.

Evaluation contract：Experimental results show that by exploiting the formal syntax and semantics of Linear Temporal Logic (LTL), our proposed auditing and monitoring techniques are superior to LLM baseline methods in detecting violations of temporally extended behavioral constraints; with our approach, even small-model labelers match or exceed frontier LLM judges.

Trade-off / failure：The mechanism described in `§§3–4 assessment, monitoring, auditing and intervention` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§§5.1 and 6 auditor limitations/discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16198:start -->`Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems` is supported only under the v1-disclosed workload and evaluator behind `§5 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16198:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16198`。
<!-- review:SF-2026-ARXIV-2605-16198:end -->

### [Argus: Evidence Assembly for Scalable Deep Research Agents](https://arxiv.org/html/2605.16217v1)

<!-- review:SF-2026-ARXIV-2605-16217:start -->
问题与约束：Yet deep research answers are composed of complementary pieces of evidence, which parallel rollouts often duplicate rather than complete, yielding diminishing returns while pushing the aggregation context toward the model's limit.

机制与 ownership：We propose Argus, an agentic system in which a Searcher and a Navigator cooperate to treat deep research as assembling a jigsaw from complementary evidence pieces, rather than brute forcing the whole answer in parallel.

Evaluation contract：With both Searcher and Navigator built on a 35B-A3B MoE backbone, Argus gains 5.5 points with a single Searcher and 12.7 points with 8 parallel Searchers, averaged over eight benchmarks.

Trade-off / failure：The mechanism described in `§§2–3 Argus evidence assembly and learning` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§4.4 Limitation and Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16217:start -->`Argus: Evidence Assembly for Scalable Deep Research Agents` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16217:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16217`。
<!-- review:SF-2026-ARXIV-2605-16217:end -->

### [Ascend-RaBitQ: Heterogeneous NPU-CPU Acceleration of Billion-Scale Similarity Search with 1-bit Quantization](https://arxiv.org/html/2605.16007v1)

<!-- review:SF-2026-ARXIV-2605.16007:start -->
问题与约束：Vector similarity search is a critical component of modern AI systems, but traditional CPU-based implementations face fundamental scalability bottlenecks for billion-scale corpora due to prohibitive computational overhead and memory bandwidth limitations.

机制与 ownership：We propose a three-stage heterogeneous execution path comprising AI Core-accelerated coarse ranking on 1-bit quantized vectors, on-device AI CPU Top-k processing, and host CPU fine re-ranking on full-precision vectors.

Evaluation contract：Evaluation on standard datasets shows that Ascend-RaBitQ achieves 3.0X to 62.8X faster index construction than the CPU baseline, up to 11.7X throughput improvement over the fastest CPU IVF-RaBitQ implementation, and over two orders of magnitude over the mathematically equivalent CPU baseline, while demonstrating encouraging scalability on distributed multi-NPU systems.

Trade-off / failure：The mechanism described in `NPU Architecture-Native RaBitQ Optimizations` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `6 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16007:start -->`Ascend-RaBitQ: Heterogeneous NPU-CPU Acceleration of Billion-Scale Similarity Search with 1-bit Quantization` is supported only under the v1-disclosed workload and evaluator behind `4 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16007:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16007`。
<!-- review:SF-2026-ARXIV-2605.16007:end -->

### [No Free Swap: Protocol-Dependent Layer Redundancy in Transformers](https://arxiv.org/html/2605.16234v1)

<!-- review:SF-2026-ARXIV-2605.16234:start -->
问题与约束：When researchers ask whether two transformer layers are "equivalent" for compression, they often conflate distinct tests.

机制与 ownership：Replacement asks whether one layer's map can substitute for another's in place; interchange asks whether two layers approximately commute when their positions are swapped.

Evaluation contract：Under one matched WikiText-2 contract at 8B scale, Qwen3-8B enters a divergent regime: interchange-guided removal is several-fold safer than replacement-guided at the same layer budgets, while Llama-3.1-8B ties the two protocols for pruning cost even though interchange KL is lower, showing metric gaps need not map one-to-one to removal.

Trade-off / failure：The mechanism described in `§§1.1 and 3 protocol vocabulary and Swap-KL method` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `Appendix M Additional Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16234:start -->`No Free Swap: Protocol-Dependent Layer Redundancy in Transformers` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16234:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16234`。
<!-- review:SF-2026-ARXIV-2605.16234:end -->

### [Designing Datacenter Power Delivery Hierarchies for the AI Era](https://arxiv.org/html/2605.16255v1)

<!-- review:SF-2026-ARXIV-2605.16255:start -->
问题与约束：This poses a major challenge for datacenter power delivery designers.

机制与 ownership：To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences.

Evaluation contract：Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes.

Trade-off / failure：The mechanism described in `3.1 A Tale of Two Designs` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16255:start -->`Designing Datacenter Power Delivery Hierarchies for the AI Era` is supported only under the v1-disclosed workload and evaluator behind `4 Datacenter Design Evaluation Framework`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16255:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16255`。
<!-- review:SF-2026-ARXIV-2605.16255:end -->

### [AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices](https://arxiv.org/html/2605.15206v1)

<!-- review:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:start -->
### AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices

问题与旧路径：Local agent execution needs an explicit stop controller that trades expected task value against marginal energy rather than running every trajectory to a fixed cap. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 energy/task-value stop model and runtime controller；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：consumer-device agent workloads and energy/quality measurements。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：device, workload and termination-estimator boundary。Artifact：implementation described; immutable commit not established。<!-- claim:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:start -->长期可保留结论是：Local agent execution needs an explicit stop controller that trades expected task value against marginal energy rather than running every trajectory to a fixed cap. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:end -->
<!-- review:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:end -->

### [Quantization Undoes Alignment: Bias Emergence in Compressed LLMs Across Models and Precision Levels](https://arxiv.org/html/2605.15208v1)

<!-- review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->
### Quantization Behavioral Regression

aggregate perplexity 对低精度的平均误差敏感，却会漏掉少数安全关键 item 的 answer flip。作者在三模型、五 precision、BBQ 与五 seeds 上报告 4-bit 时已有 bias transition 而 perplexity 变化很小，3-bit 更明显。研究只覆盖 post-training quantization、一个 bias benchmark 和有限模型，alignment-layer 解释是推断；长期结论是 model artifact promotion 必须绑定 precision/quantizer/kernel 与 item-level behavior slices。

<!-- claim:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->
<!-- review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->

### [SkillSmith: Compiling Agent Skills into Boundary-Guided Runtime Interfaces](https://arxiv.org/html/2605.15215v1)

<!-- review:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:start -->
问题与机制：To this end, we propose SkillSmith, a boundary-first compiler-runtime framework that compiles skill packages offline into minimal executable interfaces.。机制 owner=`AGENT-PLATFORM`。
全文定位：`arXiv:2605.15215v1 HTML — §3 SkillSmith compiler/runtime pipeline`；evaluation=`arXiv:2605.15215v1 — §4 skill-construction evaluation`；limitations/counterevidence=`arXiv:2605.15215v1 — §5 limitations: tool schema, verifier and deployment scope`。
<!-- claim:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:end -->

### [TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination](https://arxiv.org/html/2605.15207v1)

<!-- review:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:start -->
### TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination

问题与旧路径：Sequentially fine-tuning interacting agents invalidates cached-rollout occupancy; resampling and per-agent trust regions make the joint update contract explicit. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 occupancy-shift analysis, resampling and per-agent trust-region updates；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：multi-agent coordination experiments and component-replacement tests。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：shared-context team, cached-rollout and benchmark boundary。Artifact：paper-linked GitHub; event-time commit not pinned。<!-- claim:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:start -->长期可保留结论是：Sequentially fine-tuning interacting agents invalidates cached-rollout occupancy; resampling and per-agent trust regions make the joint update contract explicit. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:end -->
<!-- review:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:end -->

### [Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems](https://arxiv.org/html/2605.15228v1)

<!-- review:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->
问题与机制：We introduce a Distributed Trust Framework (DTF), a verification framework for governed mutation systems that computes execution authority from structured, verifiable artifacts.。机制 owner=`PLATFORM-SECURITY`。
全文定位：`arXiv:2605.15228v1 HTML — §Method / System Design — Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end -->
Books Decision=`Integrate`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end -->


### [Fair outputs, Biased Internals: Causal Potency and Asymmetry of Latent Bias in LLMs for High-Stakes Decisions](https://arxiv.org/html/2605.15217v1)

<!-- review:SF-2026-ARXIV-2605-15217:start -->
- **Contribution screen:** 输出层公平不代表内部 demographic signal 无决策因果力；跨层 activation steering 可使被抑制表示重新改变决策，因此需要重考虑 fairness release gate 是否必须同时包含 output behavior、decodability 与 causal intervention。
- **Mechanism:** matched mortgage prompts 显示 output parity 与 latent divergence 并存，跨层 steering 暴露方向不对称的因果敏感性；证据限三类开源模型、该决策任务与 intervention design。
- **Evaluation boundary:** exact-v1 摘要结果与 `§3.1-3.8 behavioral parity, representation divergence and intervention results` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§5 Limitations; Appendix A.4 cross-model replication`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15217v1 — §2.3-2.8 behavioral tests, representations and steering interventions`；Evaluation=`arXiv:2605.15217v1 — §3.1-3.8 behavioral parity, representation divergence and intervention results`；Limitations=`arXiv:2605.15217v1 — §5 Limitations; Appendix A.4 cross-model replication`。
- **Primary:** [arXiv:2605.15217v1](https://arxiv.org/html/2605.15217v1)。
- **Books:** `No Change — Existing Coverage` → `PLATFORM-EVALUATION-SYSTEM`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15217:start -->matched mortgage prompts 显示 output parity 与 latent divergence 并存，跨层 steering 暴露方向不对称的因果敏感性；证据限三类开源模型、该决策任务与 intervention design。<!-- claim:SF-2026-ARXIV-2605-15217:end -->
<!-- review:SF-2026-ARXIV-2605-15217:end -->

### [Always Learning, Always Mixing: Efficient and Simple Data Mixing All The Time](https://arxiv.org/html/2605.15220v1)

<!-- review:SF-2026-ARXIV-2605-15220:start -->
- **Contribution screen:** 静态或分阶段 mixture 在训练阶段切换后会失去当前模型动力学；OP-Mix 用当前 checkpoint 上的低秩 adapter 插值模拟候选 mixture，因此需要把 mixture 从一次性配方重考虑为贯穿 pretraining、midtraining 与 instruction tuning 的 on-policy control。
- **Mechanism:** 候选 mixture 由当前模型的低秩 adapter 插值提出，统一覆盖 pretraining、continual midtraining 与 instruction tuning；controller 节省 proxy compute，但仍受 adapter 近似误差、候选域集合与 scale transfer 限制。
- **Evaluation boundary:** exact-v1 摘要结果与 `§4.1 lifecycle experiments; §4.2 performance-efficiency frontier` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§6 Limitations and Future Work; Appendix A reproducibility`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15220v1 — §3 OP-Mix: On-Policy Data Mixing`；Evaluation=`arXiv:2605.15220v1 — §4.1 lifecycle experiments; §4.2 performance-efficiency frontier`；Limitations=`arXiv:2605.15220v1 — §6 Limitations and Future Work; Appendix A reproducibility`。
- **Primary:** [arXiv:2605.15220v1](https://arxiv.org/html/2605.15220v1)。
- **Books:** `Integrate` → `TRAIN-DATA`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15220:start -->候选 mixture 由当前模型的低秩 adapter 插值提出，统一覆盖 pretraining、continual midtraining 与 instruction tuning；controller 节省 proxy compute，但仍受 adapter 近似误差、候选域集合与 scale transfer 限制。<!-- claim:SF-2026-ARXIV-2605-15220:end -->
<!-- review:SF-2026-ARXIV-2605-15220:end -->

### [ICRL: Learning to Internalize Self-Critique with Reinforcement Learning](https://arxiv.org/html/2605.15224v1)

<!-- review:SF-2026-ARXIV-2605-15224:start -->
- **Contribution screen:** 外部 critique 能修正一次回答但不保证能力在移除 critique 后仍存在；ICRL 共享 solver/critic backbone，以 solver 后续增益奖励 critic，并用 distribution calibration 和 role-wise group advantage 转移为无 scaffold solver 能力，因此需要重考虑 self-critique 的训练 ownership。
- **Mechanism:** solver 与 critic 联合训练；critic reward 绑定 solver 后续增益，distribution ratio 限制 critique-conditioned 到 critique-free 的迁移，role-wise advantage 稳定两角色更新。
- **Evaluation boundary:** exact-v1 摘要结果与 `§4.2-4.3 agent/math results; §5.2-5.4 dynamics and ablations` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `Appendix B Limitations; Appendix A critique-conditioned trajectory analysis`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15224v1 — §3.1 self-improving workflow; §3.2 self-improvement policy optimization`；Evaluation=`arXiv:2605.15224v1 — §4.2-4.3 agent/math results; §5.2-5.4 dynamics and ablations`；Limitations=`arXiv:2605.15224v1 — Appendix B Limitations; Appendix A critique-conditioned trajectory analysis`。
- **Primary:** [arXiv:2605.15224v1](https://arxiv.org/html/2605.15224v1)。
- **Books:** `Integrate` → `TRAIN-GRPO`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15224:start -->solver 与 critic 联合训练；critic reward 绑定 solver 后续增益，distribution ratio 限制 critique-conditioned 到 critique-free 的迁移，role-wise advantage 稳定两角色更新。<!-- claim:SF-2026-ARXIV-2605-15224:end -->
<!-- review:SF-2026-ARXIV-2605-15224:end -->

### [Reducing the Safety Tax in LLM Safety Alignment with On-Policy Self-Distillation](https://arxiv.org/html/2605.15239v1)

<!-- review:SF-2026-ARXIV-2605-15239:start -->
- **Contribution screen:** 固定安全示范的 off-policy state mismatch 可成为 safety tax 的独立来源；OPSA 在 student 自身 rollout 上用 privileged-context frozen self-teacher 的 token KL，并用 teacher flip rate 选择安全 context，因此需要重考虑安全蒸馏的 occupancy 与监督有效性。
- **Mechanism:** teacher flip rate 先筛出能把 unsafe rollout 翻为 safe 的 privileged context，再在 student on-policy token 上施加 dense KL；早期 compliance token 集中更新是受限机制证据，不是普遍无税安全对齐保证。
- **Evaluation boundary:** exact-v1 摘要结果与 `§5.1 safety-reasoning tradeoff; §5.2 adaptive jailbreaks; Appendices C,G` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `Appendix A Limitations; Appendix F KL-direction ablation`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15239v1 — §3.1 off-policy safety-tax diagnosis; §3.2 on-policy dense self-supervision`；Evaluation=`arXiv:2605.15239v1 — §5.1 safety-reasoning tradeoff; §5.2 adaptive jailbreaks; Appendices C,G`；Limitations=`arXiv:2605.15239v1 — Appendix A Limitations; Appendix F KL-direction ablation`。
- **Primary:** [arXiv:2605.15239v1](https://arxiv.org/html/2605.15239v1)。
- **Books:** `Integrate` → `TRAIN-SFT`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15239:start -->teacher flip rate 先筛出能把 unsafe rollout 翻为 safe 的 privileged context，再在 student on-policy token 上施加 dense KL；早期 compliance token 集中更新是受限机制证据，不是普遍无税安全对齐保证。<!-- claim:SF-2026-ARXIV-2605-15239:end -->
<!-- review:SF-2026-ARXIV-2605-15239:end -->

### [Probing Privacy Leaks in LLM-based Code Generation via Test Generation](https://arxiv.org/html/2605.15248v1)

<!-- review:SF-2026-ARXIV-2605-15248:start -->
- **Contribution screen:** ad-hoc privacy prompts 不能逼近 PII 在代码 corpus 中的真实使用形态；以 code scenario 生成函数再从 tests 中验证泄漏、并用自动 feature library 提供模板，改变了 code-LLM memorization audit 的 attack surface，因此需要重考虑 privacy red-team 的输入生成合同。
- **Mechanism:** scenario→code question→generated function→test cases 的 pipeline 用 feature library 替代手工 prompt，检测率提升仅证明五个所测模型和 judge/validation protocol；它不证明未命中即无泄漏。
- **Evaluation boundary:** exact-v1 摘要结果与 `§6.1-6.2 experiments; Appendix D validation` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `Limitation; Ethics Consideration; Appendix A.2 comparison protocol`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15248v1 — §4 Privacy Leakage Pipeline; §5 Privacy Feature Library`；Evaluation=`arXiv:2605.15248v1 — §6.1-6.2 experiments; Appendix D validation`；Limitations=`arXiv:2605.15248v1 — Limitation; Ethics Consideration; Appendix A.2 comparison protocol`。
- **Primary:** [arXiv:2605.15248v1](https://arxiv.org/html/2605.15248v1)。
- **Books:** `Integrate` → `PLATFORM-SECURITY`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15248:start -->scenario→code question→generated function→test cases 的 pipeline 用 feature library 替代手工 prompt，检测率提升仅证明五个所测模型和 judge/validation protocol；它不证明未命中即无泄漏。<!-- claim:SF-2026-ARXIV-2605-15248:end -->
<!-- review:SF-2026-ARXIV-2605-15248:end -->

### [GQLA: Group-Query Latent Attention for Hardware-Adaptive Large Language Model Decoding](https://arxiv.org/html/2605.15250v1)

<!-- review:SF-2026-ARXIV-2605-15250:start -->
- **Contribution screen:** 普通 checkpoint 的 MHA/GQA/MQA shape 不能被 runtime 无损切换；GQLA 专门训练一组参数暴露代数等价的 MQA-absorb 与 per-group GQA 两条 decode path，因此需要重考虑 attention state shape 是否能把硬件 compute-bandwidth ratio 与 TP axis 变成运行时选择。
- **Mechanism:** 同一 GQLA 权重暴露 MQA-absorb compact-cache 与 per-group GQA expanded-cache 两条代数等价路径，runtime 按硬件 roofline 和 TP 选择；这不是任意 checkpoint 的无损改写，代价是训练/转换、expanded cache 与路径验收。
- **Evaluation boundary:** exact-v1 摘要结果与 `§4.2 roofline paths; §5 Experiments` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `Limitations; §6 Conclusion`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15250v1 — §3.1 Group-Query Latent Attention; §3.2 TransGQLA`；Evaluation=`arXiv:2605.15250v1 — §4.2 roofline paths; §5 Experiments`；Limitations=`arXiv:2605.15250v1 — Limitations; §6 Conclusion`。
- **Primary:** [arXiv:2605.15250v1](https://arxiv.org/html/2605.15250v1)。
- **Books:** `Integrate` → `MODEL-MULTI-HEAD-ATTENTION`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15250:start -->同一 GQLA 权重暴露 MQA-absorb compact-cache 与 per-group GQA expanded-cache 两条代数等价路径，runtime 按硬件 roofline 和 TP 选择；这不是任意 checkpoint 的无损改写，代价是训练/转换、expanded cache 与路径验收。<!-- claim:SF-2026-ARXIV-2605-15250:end -->
<!-- review:SF-2026-ARXIV-2605-15250:end -->

### [GQA-μP: The maximal parameterization update for grouped query attention](https://arxiv.org/html/2605.15290v1)

<!-- review:SF-2026-ARXIV-2605-15290:start -->
- **Contribution screen:** 既有 μP 迁移不能假定新 attention 参数矩阵满秩或 repetition factor 不改变尺度；论文给出适配 GQA rank/repetition 的 modified spectral-norm 条件并验证 learning-rate 与 weight-decay transfer，因此需要重考虑 GQA architecture search 中可直接复用的超参数合同。
- **Mechanism:** modified spectral norm 在非满秩权重下保留有效 scaling law，并导出 GQA repetition、depth 与 weight-decay 的 maximal-update scaling；transfer 证据限论文模型形状和 coordinate checks。
- **Evaluation boundary:** exact-v1 摘要结果与 `§4 Empirical Results; Appendix B.1-B.4` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§5 Conclusions; Appendix B.2 Failure of Yang-Type Coordinate Checking`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15290v1 — §3 Deriving Novel Maximal Update Parameterizations; §3.2 Grouped Query Attention`；Evaluation=`arXiv:2605.15290v1 — §4 Empirical Results; Appendix B.1-B.4`；Limitations=`arXiv:2605.15290v1 — §5 Conclusions; Appendix B.2 Failure of Yang-Type Coordinate Checking`。
- **Primary:** [arXiv:2605.15290v1](https://arxiv.org/html/2605.15290v1)。
- **Books:** `Integrate` → `TRAIN-PRETRAINING`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15290:start -->modified spectral norm 在非满秩权重下保留有效 scaling law，并导出 GQA repetition、depth 与 weight-decay 的 maximal-update scaling；transfer 证据限论文模型形状和 coordinate checks。<!-- claim:SF-2026-ARXIV-2605-15290:end -->
<!-- review:SF-2026-ARXIV-2605-15290:end -->

### [PhysBrain 1.0 Technical Report](https://arxiv.org/html/2605.15298v1)

<!-- review:SF-2026-ARXIV-2605-15298:start -->
- **Contribution screen:** robot trajectory coverage有限时，可先将 human egocentric video 编译成 scene/dynamics/depth/affordance 的 structured physical supervision，再以 capability-preserving adaptation 迁移到 VLA，因此需要核验 Books 是否已拥有 human-video breadth 到 typed action alignment 的分层数据路线。
- **Mechanism:** human video 先成为 structured physical QA prior，再通过 language-sensitive adaptation 进入 VLA；SOTA 结果限披露 benchmark，不能证明物理 truth、未见 embodiment 或闭环安全。
- **Evaluation boundary:** exact-v1 摘要结果与 `§4 VLM/VLA simulation; §5 real-world experiments` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§6 Discussion; §7 Conclusion`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15298v1 — §2 data engine; §3.3-3.6 preservation, language alignment and robot adaptation`；Evaluation=`arXiv:2605.15298v1 — §4 VLM/VLA simulation; §5 real-world experiments`；Limitations=`arXiv:2605.15298v1 — §6 Discussion; §7 Conclusion`。
- **Primary:** [arXiv:2605.15298v1](https://arxiv.org/html/2605.15298v1)。
- **Books:** `No Change — Existing Coverage` → `MULTIMODAL-EMBODIED-VLA`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15298:start -->human video 先成为 structured physical QA prior，再通过 language-sensitive adaptation 进入 VLA；SOTA 结果限披露 benchmark，不能证明物理 truth、未见 embodiment 或闭环安全。<!-- claim:SF-2026-ARXIV-2605-15298:end -->
<!-- review:SF-2026-ARXIV-2605-15298:end -->

### [Deep Pre-Alignment for VLMs](https://arxiv.org/html/2605.15300v1)

<!-- review:SF-2026-ARXIV-2605-15300:start -->
- **Contribution screen:** 轻量 projector 把未对齐 visual features 推入 LLM 后会消耗早层深度并造成语言能力破坏；DPA 让小 VLM perceiver 在入口前完成深层语言空间对齐，因此需要重考虑 projector、perceiver 与 LLM depth 的职责边界。
- **Mechanism:** 用可复用小 VLM 取代 ViT+projector 作为 perceiver，使视觉表示在进入目标 LLM 前先经过 language blocks；代价是额外 perceiver compute、模块兼容和对其文本能力的依赖。
- **Evaluation boundary:** exact-v1 摘要结果与 `§3 Experiments; §4.1-4.5 analysis and efficiency` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `Appendix C destructive adaptation; Appendix D failure behaviors; §6 Conclusion`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15300v1 — §2.1-2.3 architecture, perceiver language blocks and training`；Evaluation=`arXiv:2605.15300v1 — §3 Experiments; §4.1-4.5 analysis and efficiency`；Limitations=`arXiv:2605.15300v1 — Appendix C destructive adaptation; Appendix D failure behaviors; §6 Conclusion`。
- **Primary:** [arXiv:2605.15300v1](https://arxiv.org/html/2605.15300v1)。
- **Books:** `Integrate` → `MULTIMODAL-REPRESENTATION`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15300:start -->用可复用小 VLM 取代 ViT+projector 作为 perceiver，使视觉表示在进入目标 LLM 前先经过 language blocks；代价是额外 perceiver compute、模块兼容和对其文本能力的依赖。<!-- claim:SF-2026-ARXIV-2605-15300:end -->
<!-- review:SF-2026-ARXIV-2605-15300:end -->

### [One Pass Is Not Enough: Recursive Latent Refinement for Generative Models](https://arxiv.org/html/2605.15309v1)

<!-- review:SF-2026-ARXIV-2605-15309:start -->
- **Contribution screen:** 单次 latent mapping 即使 FID 低也可能牺牲 mode coverage；递归 token mapper 允许推理时增加 refinement cycles 并用 precision/recall 分离 fidelity/coverage，因此需要核验生成范式是否已把 refinement depth 作为可变状态。
- **Mechanism:** 同一 mapper 递归 H/L cycles，推理 refinement 数可独立于训练设置变化；结果限 IMLE/StyleGAN 与所测图像数据，不证明无限递归稳定。
- **Evaluation boundary:** exact-v1 摘要结果与 `§4.1-4.4 CIFAR/CelebA/StyleGAN and refinement-step analysis` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§5 Limitations and Future Work; Appendix F training stability`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15309v1 — §3.2 Recursive Token Mapper; Appendix A algorithm`；Evaluation=`arXiv:2605.15309v1 — §4.1-4.4 CIFAR/CelebA/StyleGAN and refinement-step analysis`；Limitations=`arXiv:2605.15309v1 — §5 Limitations and Future Work; Appendix F training stability`。
- **Primary:** [arXiv:2605.15309v1](https://arxiv.org/html/2605.15309v1)。
- **Books:** `No Change — Existing Coverage` → `MULTIMODAL-GENERATIVE-PARADIGMS`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15309:start -->同一 mapper 递归 H/L cycles，推理 refinement 数可独立于训练设置变化；结果限 IMLE/StyleGAN 与所测图像数据，不证明无限递归稳定。<!-- claim:SF-2026-ARXIV-2605-15309:end -->
<!-- review:SF-2026-ARXIV-2605-15309:end -->

### [Video Models Can Reason with Verifiable Rewards](https://arxiv.org/html/2605.15458v1)

<!-- review:SF-2026-ARXIV-2605-15458:start -->
- **Contribution screen:** 视频生成 RL 不能把语言模型 token-level GRPO 直接搬到 SDE trajectory；SDE-GRPO、可验证 puzzle reward 和 early-step focus 把 credit 与扩散早期全局结构绑定，因此需要重考虑 video generator 的 RLVR state 与 budget。
- **Mechanism:** 对 video diffusion/flow trajectory 使用 SDE-GRPO，并把 compute 聚焦到决定全局结构的早期 steps；reward 仅覆盖可程序验证的 maze/FlowFree/Sokoban 条件，不能外推开放视频语义或真实 latency。
- **Evaluation boundary:** exact-v1 摘要结果与 `§5.1-5.4 experiments/OOD; §6.1-6.3 ablation and reward analysis` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§7 Conclusion; Appendix C.1 KL constraint`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15458v1 — §4.1 SDE-GRPO; §4.2 early-step focus; §4.3 verifiable reward`；Evaluation=`arXiv:2605.15458v1 — §5.1-5.4 experiments/OOD; §6.1-6.3 ablation and reward analysis`；Limitations=`arXiv:2605.15458v1 — §7 Conclusion; Appendix C.1 KL constraint`。
- **Primary:** [arXiv:2605.15458v1](https://arxiv.org/html/2605.15458v1)。
- **Books:** `Integrate` → `MULTIMODAL-GENERATIVE-PARADIGMS`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15458:start -->对 video diffusion/flow trajectory 使用 SDE-GRPO，并把 compute 聚焦到决定全局结构的早期 steps；reward 仅覆盖可程序验证的 maze/FlowFree/Sokoban 条件，不能外推开放视频语义或真实 latency。<!-- claim:SF-2026-ARXIV-2605-15458:end -->
<!-- review:SF-2026-ARXIV-2605-15458:end -->

### [When Does Sparse MoE Help in Vision? The Role of Backbone Compute Leverage in Sparse Routing](https://arxiv.org/html/2605.15484v1)

<!-- review:SF-2026-ARXIV-2605-15484:start -->
- **Contribution screen:** 稀疏 MoE 的 active-parameter headline 没有说明专家计算在整网 FLOPs 中是否足够大；受控 rho/top-k 实验与 per-sample Soft-MoE 反例表明 backbone compute leverage 和 batch-axis dispatch 可反转 sparse-vs-dense 排序，因此需要重考虑视觉 MoE 的 matched-compute admission。
- **Mechanism:** MoE 收益取决于 expert branch 占全 backbone compute 的 leverage；只改 top-k 可在固定架构下反转收益，batch-axis Soft-MoE 在 per-sample CNN 中还是主要 failure mode。
- **Evaluation boundary:** exact-v1 摘要结果与 `§4.2-4.5 controlled rho sweep and validation; §5 mechanistic analysis` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§5.1-5.4 routing stability/specialization/efficiency; §6 Conclusion`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15484v1 — §3.2 hard-capacity sparse routing; §3.5 per-sample soft gating`；Evaluation=`arXiv:2605.15484v1 — §4.2-4.5 controlled rho sweep and validation; §5 mechanistic analysis`；Limitations=`arXiv:2605.15484v1 — §5.1-5.4 routing stability/specialization/efficiency; §6 Conclusion`。
- **Primary:** [arXiv:2605.15484v1](https://arxiv.org/html/2605.15484v1)。
- **Books:** `Integrate` → `MODEL-MOE`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15484:start -->MoE 收益取决于 expert branch 占全 backbone compute 的 leverage；只改 top-k 可在固定架构下反转收益，batch-axis Soft-MoE 在 per-sample CNN 中还是主要 failure mode。<!-- claim:SF-2026-ARXIV-2605-15484:end -->
<!-- review:SF-2026-ARXIV-2605-15484:end -->

### [Ghosted Layers: Unconstrained Activation Alignment for Recovering Layer-Pruned LLMs](https://arxiv.org/html/2605.15491v1)

<!-- review:SF-2026-ARXIV-2605-15491:start -->
- **Contribution screen:** 整层 pruning 破坏下一 surviving layer 的输入分布，不能只用 pruning score 解释质量损失；Ghosted Layers 从小 calibration set 求闭式线性 boundary operator，因此需要重考虑 layer removal 的恢复 artifact 与校准边界。
- **Mechanism:** 在被删 block 的边界收集 activation pair，解 unconstrained closed-form linear alignment 并插回模型；它保留 pruning speedup但引入 calibration dependence、operator state 和未测分布风险。
- **Evaluation boundary:** exact-v1 摘要结果与 `§5.1-5.3 experiments and calibration-size ablation; Appendix G latency` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§6 Discussion; Appendix D fine-tuning comparison`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15491v1 — §3.2.1-3.2.3 boundary activations, closed-form operator and insertion`；Evaluation=`arXiv:2605.15491v1 — §5.1-5.3 experiments and calibration-size ablation; Appendix G latency`；Limitations=`arXiv:2605.15491v1 — §6 Discussion; Appendix D fine-tuning comparison`。
- **Primary:** [arXiv:2605.15491v1](https://arxiv.org/html/2605.15491v1)。
- **Books:** `Integrate` → `MODEL-TRANSFORMER-LAYER`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15491:start -->在被删 block 的边界收集 activation pair，解 unconstrained closed-form linear alignment 并插回模型；它保留 pruning speedup但引入 calibration dependence、operator state 和未测分布风险。<!-- claim:SF-2026-ARXIV-2605-15491:end -->
<!-- review:SF-2026-ARXIV-2605-15491:end -->

### [FLASH: Efficient Visuomotor Policy via Sparse Sampling](https://arxiv.org/html/2605.15492v1)

<!-- review:SF-2026-ARXIV-2605-15492:start -->
- **Contribution screen:** 离散 action chunk 与多步 diffusion 把 horizon、inference cadence 和 controller sampling 紧耦合；FLASH 用连续 Legendre 系数、稀疏时间拟合和 history-anchored single-step flow 分离表示 horizon、生成次数与执行频率，因此需要重考虑 VLA action representation 到低层控制器的接口。
- **Mechanism:** 连续 Legendre trajectory 让单次生成覆盖长 horizon，并可解析求导给 controller feed-forward；history anchor 缩短 flow path，但多项式拟合、长 horizon drift 与稀疏演示边界仍需 controller 验证。
- **Evaluation boundary:** exact-v1 摘要结果与 `§4.1-4.4 training, inference, tracking and speed modulation; §5 ablations` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§7 Limitations; Appendices F-G controller and speed analysis`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15492v1 — §3.1 sparse Legendre trajectory; §3.2 history-anchored flow; §3.3 objectives`；Evaluation=`arXiv:2605.15492v1 — §4.1-4.4 training, inference, tracking and speed modulation; §5 ablations`；Limitations=`arXiv:2605.15492v1 — §7 Limitations; Appendices F-G controller and speed analysis`。
- **Primary:** [arXiv:2605.15492v1](https://arxiv.org/html/2605.15492v1)。
- **Books:** `Integrate` → `MULTIMODAL-EMBODIED-VLA`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15492:start -->连续 Legendre trajectory 让单次生成覆盖长 horizon，并可解析求导给 controller feed-forward；history anchor 缩短 flow path，但多项式拟合、长 horizon drift 与稀疏演示边界仍需 controller 验证。<!-- claim:SF-2026-ARXIV-2605-15492:end -->
<!-- review:SF-2026-ARXIV-2605-15492:end -->

### [Can We Trust AI-Inferred User States. A Psychometric Framework for Validating the Reliability of Users States Classification by LLMs in Operational Environments](https://arxiv.org/html/2605.15734v1)

<!-- review:SF-2026-ARXIV-2605-15734:start -->
- **Contribution screen:** 聚合后稳定的 inferred user-state metric 不能自动支持个体实时 adaptation；三种 bimodal LLM 的重复测量仅 31/213 指标达到标准，因此 evaluation 必须分别验收 individual reliability 与 post-hoc aggregate utility。
- **Mechanism:** 同一 metric 的 individual repeatability 与 aggregate analytical utility必须分别判定；证据只覆盖论文定义的 213 metrics、三模型与 replication protocol。
- **Evaluation boundary:** exact-v1 摘要结果与 `§5 Results; individual-score versus aggregate reliability across three bimodal LLMs` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§6 Discussion; §7 Limitations and Further Research`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.15734v1 — §4 Study Design and Descriptions of Experiments`；Evaluation=`arXiv:2605.15734v1 — §5 Results; individual-score versus aggregate reliability across three bimodal LLMs`；Limitations=`arXiv:2605.15734v1 — §6 Discussion; §7 Limitations and Further Research`。
- **Primary:** [arXiv:2605.15734v1](https://arxiv.org/html/2605.15734v1)。
- **Books:** `No Change — Existing Coverage` → `PLATFORM-EVALUATION-SYSTEM`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-15734:start -->同一 metric 的 individual repeatability 与 aggregate analytical utility必须分别判定；证据只覆盖论文定义的 213 metrics、三模型与 replication protocol。<!-- claim:SF-2026-ARXIV-2605-15734:end -->
<!-- review:SF-2026-ARXIV-2605-15734:end -->

### [Look Before You Leap: Autonomous Exploration for LLM Agents](https://arxiv.org/html/2605.16143v1)

<!-- review:SF-2026-ARXIV-2605-16143:start -->
- **Contribution screen:** task-only RL 会过早 exploitation；独立 exploration rollout、ECC coverage 与 Explore-then-Act 把信息收集预算和任务执行分离，因此需要核验 Planning 是否已拥有 evidence-gathering action 与提交 action 的分权。
- **Mechanism:** 先用预算发现 state/object/affordance checkpoints，再带 grounded knowledge 执行任务；ECC 是受限环境 coverage proxy，不是开放环境完整性证明。
- **Evaluation boundary:** exact-v1 摘要结果与 `§4.2-4.4 diagnosis, intervention and analysis` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `Appendix A Limitations and Future Work; Appendix D sensitivity`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.16143v1 — §3.2 Exploration Checkpoint Coverage; §3.3 training; §3.4 Explore-then-Act`；Evaluation=`arXiv:2605.16143v1 — §4.2-4.4 diagnosis, intervention and analysis`；Limitations=`arXiv:2605.16143v1 — Appendix A Limitations and Future Work; Appendix D sensitivity`。
- **Primary:** [arXiv:2605.16143v1](https://arxiv.org/html/2605.16143v1)。
- **Books:** `No Change — Existing Coverage` → `AGENT-PLANNING`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-16143:start -->先用预算发现 state/object/affordance checkpoints，再带 grounded knowledge 执行任务；ECC 是受限环境 coverage proxy，不是开放环境完整性证明。<!-- claim:SF-2026-ARXIV-2605-16143:end -->
<!-- review:SF-2026-ARXIV-2605-16143:end -->

### [Second-Order Multi-Level Variance Correction for Modality Competition in Multimodal Models](https://arxiv.org/html/2605.16165v1)

<!-- review:SF-2026-ARXIV-2605-16165:start -->
- **Contribution screen:** 统一 next-token objective 不保证图像与文本梯度在大 batch 下共享稳定尺度；Fisher-orthogonal projection 与 multi-level folding 把 modality variance 变成可诊断、可校正的 optimizer state，因此需要重考虑 multimodal pretraining 的 large-batch optimizer branch。
- **Mechanism:** ML-FOP-SOAP 用曲率感知 projection 抑制跨模态方差冲突，并以 hierarchical folding 降低 gradient-accumulation micro-step 成本；证据限 Janus/Emu3、作者 batch 与 Fisher/tensor-preconditioner 近似。
- **Evaluation boundary:** exact-v1 摘要结果与 `§4 setup; §5 Experiments; Appendix D.3 reproducibility` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§6 Conclusion; Appendix A-C theoretical assumptions`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.16165v1 — §3.1-3.5 modality competition, Fisher projection and hierarchical folding`；Evaluation=`arXiv:2605.16165v1 — §4 setup; §5 Experiments; Appendix D.3 reproducibility`；Limitations=`arXiv:2605.16165v1 — §6 Conclusion; Appendix A-C theoretical assumptions`。
- **Primary:** [arXiv:2605.16165v1](https://arxiv.org/html/2605.16165v1)。
- **Books:** `Integrate` → `TRAIN-PRETRAINING`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-16165:start -->ML-FOP-SOAP 用曲率感知 projection 抑制跨模态方差冲突，并以 hierarchical folding 降低 gradient-accumulation micro-step 成本；证据限 Janus/Emu3、作者 batch 与 Fisher/tensor-preconditioner 近似。<!-- claim:SF-2026-ARXIV-2605-16165:end -->
<!-- review:SF-2026-ARXIV-2605-16165:end -->

### [FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast](https://arxiv.org/html/2605.16233v1)

<!-- review:SF-2026-ARXIV-2605-16233:start -->
- **Contribution screen:** 单流 Reflexion 会把每条轨迹困在局部经验中；FORGE 将 failure-derived prompt memory 放入 population stages，由 champion broadcast 扩散且以 graduation 冻结实例，因此需要重考虑 memory promotion 的群体传播、成本停止与污染半径。
- **Mechanism:** 外环按 stage 选 champion 并广播自然语言 memory，graduation 主要节省 compute；broadcast ablation 支持传播是收益机制，但全部证据限 CAGE-2 B-line，错误 champion 也会扩大污染。
- **Evaluation boundary:** exact-v1 摘要结果与 `§5.1 broadcast comparison; §5.2-5.3 graduation/threshold ablations` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `§7 Limitations & Future Work; Appendix A artifact scope`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.16233v1 — §3.1 hierarchical ReAct memory; §3.2 failure reflexion; §3.3 FORGE protocol`；Evaluation=`arXiv:2605.16233v1 — §5.1 broadcast comparison; §5.2-5.3 graduation/threshold ablations`；Limitations=`arXiv:2605.16233v1 — §7 Limitations & Future Work; Appendix A artifact scope`。
- **Primary:** [arXiv:2605.16233v1](https://arxiv.org/html/2605.16233v1)。
- **Books:** `Integrate` → `AGENT-MEMORY`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-16233:start -->外环按 stage 选 champion 并广播自然语言 memory，graduation 主要节省 compute；broadcast ablation 支持传播是收益机制，但全部证据限 CAGE-2 B-line，错误 champion 也会扩大污染。<!-- claim:SF-2026-ARXIV-2605-16233:end -->
<!-- review:SF-2026-ARXIV-2605-16233:end -->

### [Offline Semantic Guidance for Efficient Vision-Language-Action Policy Distillation](https://arxiv.org/html/2605.16241v1)

<!-- review:SF-2026-ARXIV-2605-16241:start -->
- **Contribution screen:** 只模仿 teacher action 会把动作噪声写入小 student；VLA-AD 将 phase anchor 和多帧方向作为仅训练期语义监督、部署时完全移除 teacher/VLM，因此需要核验 Books 是否已拥有 privileged teacher 与独立 runtime student 的边界。
- **Mechanism:** 训练期 VLM 提供 phase/direction semantic targets，student 部署时独立运行；收益限 LIBERO 与两类 teacher，语义监督不取得物理提交权。
- **Evaluation boundary:** exact-v1 摘要结果与 `§4.2-4.5 teacher generalization, granularity, efficiency and noise robustness` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `Appendix Limitations; §5 Conclusion`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:2605.16241v1 — §3.2-3.4 dual-path supervision, phase anchors and multi-frame direction`；Evaluation=`arXiv:2605.16241v1 — §4.2-4.5 teacher generalization, granularity, efficiency and noise robustness`；Limitations=`arXiv:2605.16241v1 — Appendix Limitations; §5 Conclusion`。
- **Primary:** [arXiv:2605.16241v1](https://arxiv.org/html/2605.16241v1)。
- **Books:** `No Change — Existing Coverage` → `MULTIMODAL-EMBODIED-VLA`；作者侧未写共享 Books。
<!-- claim:SF-2026-ARXIV-2605-16241:start -->训练期 VLM 提供 phase/direction semantic targets，student 部署时独立运行；收益限 LIBERO 与两类 teacher，语义监督不取得物理提交权。<!-- claim:SF-2026-ARXIV-2605-16241:end -->
<!-- review:SF-2026-ARXIV-2605-16241:end -->
### Books 对读

当前 owner、相邻章节、正文哈希、现有 binding 与命题级比较见 [`books-comparison-v3.json`](../_sources/daily-20260518/books-comparison-v3.json)。19 个整合项的正文已经存在；作者侧只登记队列，不删除、不追加、不把 source marker 当成语义验收。

<!-- books-review:SF-2026-ARXIV-2605-15204:start -->
<!-- existing:SF-2026-ARXIV-2605-15204:start -->对读 `books/part-07-agent/82-multi-agent.md#L267 (H2: Message 不是 State)` 及相邻章节后，现有命题为：本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-15204:end -->
<!-- delta:SF-2026-ARXIV-2605-15204:start -->Exact-v1 的 source-specific delta 是：We present SDOF, a framework that treats multi-agent execution as a constrained state machine. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-15204:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-15204:end -->

<!-- books-review:SF-2026-ARXIV-2605-15238:start -->
<!-- existing:SF-2026-ARXIV-2605-15238:start -->已读取 `books/part-07-agent/81-workflow.md` 及相邻章节；当前主线已覆盖durable DAG/state、checkpoint、retry、compensation、external evidence 与 commit authority。正文尚未明确承载本 family 的增量：代码生成可把 incremental compiler checker 作为异步 sensor，并用 checkpoint/rollback 保留已验证前缀；compiler 只拥有 static-correctness feedback，不拥有 task correctness。 Owner snapshot sha256=`a8a935c80e5047500f9c7beb334a74ac83381e49176a11f8beaa8b3da089fa92`；相邻章节=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-15238:end -->
<!-- delta:SF-2026-ARXIV-2605-15238:start -->代码生成可把 incremental compiler checker 作为异步 sensor，并用 checkpoint/rollback 保留已验证前缀；compiler 只拥有 static-correctness feedback，不拥有 task correctness<!-- delta:SF-2026-ARXIV-2605-15238:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15238:end -->

<!-- books-review:SF-2026-ARXIV-2605-15257:start -->
<!-- existing:SF-2026-ARXIV-2605-15257:start -->已读取 `books/part-06-ai-infrastructure/67-monitoring.md` 及相邻章节；当前主线已覆盖多源 sensor、trace/evidence identity、阈值、盲区、escalation 与 independent control authority。正文尚未明确承载本 family 的增量：CoT monitor 进入训练分布后，模型可能学习 monitor-aware obfuscation；监控合同必须包含 adaptive exposure、外部 signals 与不可由被监控模型控制的 escalation。 Owner snapshot sha256=`311704bec6f23882d2259d2365d557dca6cae87f79c809c87698f0866dcfe88e`；相邻章节=`books/part-06-ai-infrastructure/66-evaluation-system.md, books/part-06-ai-infrastructure/68-logging.md`。<!-- existing:SF-2026-ARXIV-2605-15257:end -->
<!-- delta:SF-2026-ARXIV-2605-15257:start -->CoT monitor 进入训练分布后，模型可能学习 monitor-aware obfuscation；监控合同必须包含 adaptive exposure、外部 signals 与不可由被监控模型控制的 escalation<!-- delta:SF-2026-ARXIV-2605-15257:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15257:end -->

<!-- books-review:SF-2026-ARXIV-2605-15338:start -->
<!-- existing:SF-2026-ARXIV-2605-15338:start -->已读取 `books/part-07-agent/77-memory.md` 及相邻章节；当前主线已覆盖write admission、provenance、derived state、retrieval、expiry、poisoning containment 与可逆更新。本 family 的增量“memory poisoning 可延迟触发并跨 session 重放；write admission、provenance、activation-time policy 与 expiry 必须共同拥有防线”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7`；相邻章节=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-15338:end -->
<!-- delta:SF-2026-ARXIV-2605-15338:start -->memory poisoning 可延迟触发并跨 session 重放；write admission、provenance、activation-time policy 与 expiry 必须共同拥有防线<!-- delta:SF-2026-ARXIV-2605-15338:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15338:end -->

<!-- books-review:SF-2026-ARXIV-2605-15377:start -->
<!-- existing:SF-2026-ARXIV-2605-15377:start -->已读取 `books/part-06-ai-infrastructure/67-monitoring.md` 及相邻章节；当前主线已覆盖多源 sensor、trace/evidence identity、阈值、盲区、escalation 与 independent control authority。正文尚未明确承载本 family 的增量：AI control monitoring 应优先组合异质 signal 以降低共同盲区，而非只增加同类 monitor compute；ensemble 自身仍需校准、correlation audit 与独立 stop authority。 Owner snapshot sha256=`311704bec6f23882d2259d2365d557dca6cae87f79c809c87698f0866dcfe88e`；相邻章节=`books/part-06-ai-infrastructure/66-evaluation-system.md, books/part-06-ai-infrastructure/68-logging.md`。<!-- existing:SF-2026-ARXIV-2605-15377:end -->
<!-- delta:SF-2026-ARXIV-2605-15377:start -->AI control monitoring 应优先组合异质 signal 以降低共同盲区，而非只增加同类 monitor compute；ensemble 自身仍需校准、correlation audit 与独立 stop authority<!-- delta:SF-2026-ARXIV-2605-15377:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15377:end -->

<!-- books-review:SF-2026-ARXIV-2605-15384:start -->
<!-- existing:SF-2026-ARXIV-2605-15384:start -->已读取 `books/part-07-agent/77-memory.md` 及相邻章节；当前主线已覆盖write admission、provenance、derived state、retrieval、expiry、poisoning containment 与可逆更新。正文尚未明确承载本 family 的增量：顺序演化 memory 的评测必须把 acquisition、retention、forgetting、transfer 与 interference 分成时间序列诊断，不能由最终平均分掩盖负迁移。 Owner snapshot sha256=`ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7`；相邻章节=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-15384:end -->
<!-- delta:SF-2026-ARXIV-2605-15384:start -->顺序演化 memory 的评测必须把 acquisition、retention、forgetting、transfer 与 interference 分成时间序列诊断，不能由最终平均分掩盖负迁移<!-- delta:SF-2026-ARXIV-2605-15384:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15384:end -->

<!-- books-review:SF-2026-ARXIV-2605-15403:start -->
<!-- existing:SF-2026-ARXIV-2605-15403:start -->已读取 `books/part-02-model/21-moe.md` 及相邻章节；当前主线已覆盖router probability、expert capacity、load balance、communication、placement 与 fallback 的条件计算合同。本 family 的增量“MoE balance controller 应估计 population-level routing distribution，而不是把 noisy mini-batch count 当真值；EMA/mirror-descent bias correction换来更稳定利用率，也新增 lag 与非平稳漂移”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`3eaf93101db6b0f4fb7aa292a3e610b6fc1cc14af84e385edd9b2c7d115de79d`；相邻章节=`books/part-02-model/20-sampling.md, books/part-02-model/22-long-context.md`。<!-- existing:SF-2026-ARXIV-2605-15403:end -->
<!-- delta:SF-2026-ARXIV-2605-15403:start -->MoE balance controller 应估计 population-level routing distribution，而不是把 noisy mini-batch count 当真值；EMA/mirror-descent bias correction换来更稳定利用率，也新增 lag 与非平稳漂移<!-- delta:SF-2026-ARXIV-2605-15403:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15403:end -->

<!-- books-review:SF-2026-ARXIV-2605-15422:start -->
<!-- existing:SF-2026-ARXIV-2605-15422:start -->已读取 `books/part-04-training-system/36-distributed-training.md` 及相邻章节；当前主线已覆盖parallel state、collective/placement、kernel execution、checkpoint 与 optimization semantics。正文尚未明确承载本 family 的增量：共享 prompt 的大 rollout RL 训练可将 prompt K/V 与 response K/V 分开复用并保持 causal gradient；收益必须绑定 N、P、R、kernel 与 backward contract。 Owner snapshot sha256=`5e9d628aaf7a6c0995918787baa0681091e4e65365fddc0457075715547d969d`；相邻章节=`books/part-04-training-system/35-checkpoint.md, books/part-04-training-system/37-tensor-parallel.md`。<!-- existing:SF-2026-ARXIV-2605-15422:end -->
<!-- delta:SF-2026-ARXIV-2605-15422:start -->共享 prompt 的大 rollout RL 训练可将 prompt K/V 与 response K/V 分开复用并保持 causal gradient；收益必须绑定 N、P、R、kernel 与 backward contract<!-- delta:SF-2026-ARXIV-2605-15422:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15422:end -->

<!-- books-review:SF-2026-ARXIV-2605-15425:start -->
<!-- existing:SF-2026-ARXIV-2605-15425:start -->已读取 `books/part-07-agent/81-workflow.md` 及相邻章节；当前主线已覆盖durable DAG/state、checkpoint、retry、compensation、external evidence 与 commit authority。本 family 的增量“Agent coding workflow 应把 task decomposition、branch/retry与schema validation移出 monolithic prompt，交给 executable runtime；LLM只拥有局部判断，不拥有全局控制流提交”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`a8a935c80e5047500f9c7beb334a74ac83381e49176a11f8beaa8b3da089fa92`；相邻章节=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-15425:end -->
<!-- delta:SF-2026-ARXIV-2605-15425:start -->Agent coding workflow 应把 task decomposition、branch/retry与schema validation移出 monolithic prompt，交给 executable runtime；LLM只拥有局部判断，不拥有全局控制流提交<!-- delta:SF-2026-ARXIV-2605-15425:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15425:end -->

<!-- books-review:SF-2026-ARXIV-2605-15466:start -->
<!-- existing:SF-2026-ARXIV-2605-15466:start -->已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节；当前主线已覆盖observation quality、action-conditioned transition、geometry、persistent world state 与 planning handoff。本 family 的增量“predictive representation只有在 masking 聚焦 entity interaction且用 causal reasoning/action outcome验证时才接近 world-state signal；重建 latent trajectory仍不自动获得控制充分性”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`2b8a3f6f457ba203854a2b4078d943ca0b14422f842cad9ee4809b1e86684998`；相邻章节=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md, books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。<!-- existing:SF-2026-ARXIV-2605-15466:end -->
<!-- delta:SF-2026-ARXIV-2605-15466:start -->predictive representation只有在 masking 聚焦 entity interaction且用 causal reasoning/action outcome验证时才接近 world-state signal；重建 latent trajectory仍不自动获得控制充分性<!-- delta:SF-2026-ARXIV-2605-15466:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15466:end -->

<!-- books-review:SF-2026-ARXIV-2605-15477:start -->
<!-- existing:SF-2026-ARXIV-2605-15477:start -->已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节；当前主线已覆盖observation quality、action-conditioned transition、geometry、persistent world state 与 planning handoff。本 family 的增量“exo video要服务 ego world model，必须先恢复body pose/action schema并显式转换视角；数据扩容收益依赖action identity与ego observation对齐，不能把普通视频直接当控制轨迹”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`2b8a3f6f457ba203854a2b4078d943ca0b14422f842cad9ee4809b1e86684998`；相邻章节=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md, books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。<!-- existing:SF-2026-ARXIV-2605-15477:end -->
<!-- delta:SF-2026-ARXIV-2605-15477:start -->exo video要服务 ego world model，必须先恢复body pose/action schema并显式转换视角；数据扩容收益依赖action identity与ego observation对齐，不能把普通视频直接当控制轨迹<!-- delta:SF-2026-ARXIV-2605-15477:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15477:end -->

<!-- books-review:SF-2026-ARXIV-2605-15508:start -->
<!-- existing:SF-2026-ARXIV-2605-15508:start -->`books/part-02-model/22-long-context.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15508:end -->
<!-- delta:SF-2026-ARXIV-2605-15508:start -->Draft-model attention is reused as the target model's sparse admission mask while target KV remains authoritative; this adds a draft/target state-ownership and false-negative fallback boundary not explicit in Ch22.<!-- delta:SF-2026-ARXIV-2605-15508:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15508:end -->

<!-- books-review:SF-2026-ARXIV-2605-15514:start -->
<!-- existing:SF-2026-ARXIV-2605-15514:start -->`books/part-02-model/13-position-encoding.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15514:end -->
<!-- delta:SF-2026-ARXIV-2605-15514:start -->The exact-v1 proof separates position inversion/aliasing from token inversion/aliasing, tightening Ch13's qualitative RoPE extrapolation account into a protocol-specific representational limit.<!-- delta:SF-2026-ARXIV-2605-15514:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15514:end -->

<!-- books-review:SF-2026-ARXIV-2605-15520:start -->
<!-- existing:SF-2026-ARXIV-2605-15520:start -->`books/part-04-training-system/27-data.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15520:end -->
<!-- delta:SF-2026-ARXIV-2605-15520:start -->A participant can preserve model utility while corrupting distributed data-attribution credit, so provenance integrity needs an adversarial contract rather than treating attribution as a passive statistic.<!-- delta:SF-2026-ARXIV-2605-15520:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15520:end -->

<!-- books-review:SF-2026-ARXIV-2605-15529:start -->
<!-- existing:SF-2026-ARXIV-2605-15529:start -->`books/part-04-training-system/31-rlhf.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15529:end -->
<!-- delta:SF-2026-ARXIV-2605-15529:start -->Count evidence and learned concentration make process-reward reliability an input to ranking, stopping and repair; Ch31 has uncertainty-selected feedback but not this finite-evidence control contract.<!-- delta:SF-2026-ARXIV-2605-15529:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15529:end -->

<!-- books-review:SF-2026-ARXIV-2605-15565:start -->
<!-- existing:SF-2026-ARXIV-2605-15565:start -->`books/part-04-training-system/36-distributed-training.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15565:end -->
<!-- delta:SF-2026-ARXIV-2605-15565:start -->Trainer-centered RL coordination becomes explicit dataflow components with rollout-as-a-service and versioned weight transfer, moving orchestration ownership into the distributed runtime.<!-- delta:SF-2026-ARXIV-2605-15565:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15565:end -->

<!-- books-review:SF-2026-ARXIV-2605-15573:start -->
<!-- existing:SF-2026-ARXIV-2605-15573:start -->Ch82 already treats parallel/sequential topology as runtime policy with admission, convergence and rollback rather than a fixed multi-agent graph.<!-- existing:SF-2026-ARXIV-2605-15573:end -->
<!-- delta:SF-2026-ARXIV-2605-15573:start -->Ch82 already treats parallel/sequential topology as runtime policy with admission, convergence and rollback rather than a fixed multi-agent graph.<!-- delta:SF-2026-ARXIV-2605-15573:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15573:end -->

<!-- books-review:SF-2026-ARXIV-2605-15581:start -->
<!-- existing:SF-2026-ARXIV-2605-15581:start -->Ch81 already owns stage-localized failure evidence, replayable repair and durable workflow recovery; STAR is a scoped RCA realization.<!-- existing:SF-2026-ARXIV-2605-15581:end -->
<!-- delta:SF-2026-ARXIV-2605-15581:start -->Ch81 already owns stage-localized failure evidence, replayable repair and durable workflow recovery; STAR is a scoped RCA realization.<!-- delta:SF-2026-ARXIV-2605-15581:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15581:end -->

<!-- books-review:SF-2026-ARXIV-2605-15609:start -->
<!-- existing:SF-2026-ARXIV-2605-15609:start -->Ch24 already carries proposal, parallel refinement, verification, rejection and rollback as the diffusion/speculation evolution spine.<!-- existing:SF-2026-ARXIV-2605-15609:end -->
<!-- delta:SF-2026-ARXIV-2605-15609:start -->Ch24 already carries proposal, parallel refinement, verification, rejection and rollback as the diffusion/speculation evolution spine.<!-- delta:SF-2026-ARXIV-2605-15609:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15609:end -->

<!-- books-review:SF-2026-ARXIV-2605-15617:start -->
<!-- existing:SF-2026-ARXIV-2605-15617:start -->`books/part-04-training-system/36-distributed-training.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15617:end -->
<!-- delta:SF-2026-ARXIV-2605-15617:start -->Selective real-rank execution plus calibrated virtual participants makes cluster-scale training control paths testable on small hardware and introduces fidelity/error ownership absent from Ch36.<!-- delta:SF-2026-ARXIV-2605-15617:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15617:end -->

<!-- books-review:SF-2026-ARXIV-2605-15618:start -->
<!-- existing:SF-2026-ARXIV-2605-15618:start -->Ch25 already distinguishes predictive representation quality from controllable world-state usefulness and requires robustness/evaluation boundaries.<!-- existing:SF-2026-ARXIV-2605-15618:end -->
<!-- delta:SF-2026-ARXIV-2605-15618:start -->Ch25 already distinguishes predictive representation quality from controllable world-state usefulness and requires robustness/evaluation boundaries.<!-- delta:SF-2026-ARXIV-2605-15618:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15618:end -->

<!-- books-review:SF-2026-ARXIV-2605-15648:start -->
<!-- existing:SF-2026-ARXIV-2605-15648:start -->`books/part-06-ai-infrastructure/72-security.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15648:end -->
<!-- delta:SF-2026-ARXIV-2605-15648:start -->The paper shows that an implementation variant can invalidate the privacy analysis used for DP-SGD, requiring mechanism-to-accountant conformance and audit evidence before a privacy claim is admitted.<!-- delta:SF-2026-ARXIV-2605-15648:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15648:end -->

<!-- books-review:SF-2026-ARXIV-2605-15665:start -->
<!-- existing:SF-2026-ARXIV-2605-15665:start -->Ch67 already connects requirement-derived tests, production-faithful simulation, diagnosis, prompt repair and continuous drift monitoring.<!-- existing:SF-2026-ARXIV-2605-15665:end -->
<!-- delta:SF-2026-ARXIV-2605-15665:start -->Ch67 already connects requirement-derived tests, production-faithful simulation, diagnosis, prompt repair and continuous drift monitoring.<!-- delta:SF-2026-ARXIV-2605-15665:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15665:end -->

<!-- books-review:SF-2026-ARXIV-2605-15694:start -->
<!-- existing:SF-2026-ARXIV-2605-15694:start -->Ch52 already owns distributed inference placement under link loss, partition cost, state movement and heterogeneous edge constraints; CATS is a narrow deployment case.<!-- existing:SF-2026-ARXIV-2605-15694:end -->
<!-- delta:SF-2026-ARXIV-2605-15694:start -->Ch52 already owns distributed inference placement under link loss, partition cost, state movement and heterogeneous edge constraints; CATS is a narrow deployment case.<!-- delta:SF-2026-ARXIV-2605-15694:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15694:end -->

<!-- books-review:SF-2026-ARXIV-2605-15710:start -->
<!-- existing:SF-2026-ARXIV-2605-15710:start -->Ch66 and Ch77 already require source-distributed evidence identity, provenance-aware memory evaluation and claim-level retrieval correctness.<!-- existing:SF-2026-ARXIV-2605-15710:end -->
<!-- delta:SF-2026-ARXIV-2605-15710:start -->Ch66 and Ch77 already require source-distributed evidence identity, provenance-aware memory evaluation and claim-level retrieval correctness.<!-- delta:SF-2026-ARXIV-2605-15710:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15710:end -->

<!-- books-review:SF-2026-ARXIV-2605-15734:start --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15734:end -->

<!-- books-review:SF-2026-ARXIV-2605-15761:start -->
<!-- existing:SF-2026-ARXIV-2605-15761:start -->Ch66 already models leaderboard stability as an evaluator/version/perturbation contract and includes manipulation-sensitive release evidence.<!-- existing:SF-2026-ARXIV-2605-15761:end -->
<!-- delta:SF-2026-ARXIV-2605-15761:start -->Ch66 already models leaderboard stability as an evaluator/version/perturbation contract and includes manipulation-sensitive release evidence.<!-- delta:SF-2026-ARXIV-2605-15761:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15761:end -->

<!-- books-review:SF-2026-ARXIV-2605-15777:start -->
<!-- existing:SF-2026-ARXIV-2605-15777:start -->Ch66 already evaluates workflow agents through executable task effects, environment state and bounded judge evidence rather than answer similarity alone.<!-- existing:SF-2026-ARXIV-2605-15777:end -->
<!-- delta:SF-2026-ARXIV-2605-15777:start -->Ch66 already evaluates workflow agents through executable task effects, environment state and bounded judge evidence rather than answer similarity alone.<!-- delta:SF-2026-ARXIV-2605-15777:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15777:end -->

<!-- books-review:SF-2026-ARXIV-2605-15815:start -->
<!-- existing:SF-2026-ARXIV-2605-15815:start -->Ch84 already owns reusable skill compilation, verification, provenance, lifecycle and transfer; repository setup is one skill domain.<!-- existing:SF-2026-ARXIV-2605-15815:end -->
<!-- delta:SF-2026-ARXIV-2605-15815:start -->Ch84 already owns reusable skill compilation, verification, provenance, lifecycle and transfer; repository setup is one skill domain.<!-- delta:SF-2026-ARXIV-2605-15815:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15815:end -->

<!-- books-review:SF-2026-ARXIV-2605-15846:start -->
<!-- existing:SF-2026-ARXIV-2605-15846:start -->Ch66 and Ch84 already require versioned long-horizon tasks, reproducible harness identity and rollout-based quality control.<!-- existing:SF-2026-ARXIV-2605-15846:end -->
<!-- delta:SF-2026-ARXIV-2605-15846:start -->Ch66 and Ch84 already require versioned long-horizon tasks, reproducible harness identity and rollout-based quality control.<!-- delta:SF-2026-ARXIV-2605-15846:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15846:end -->

<!-- books-review:SF-2026-ARXIV-2605-15957:start -->
<!-- existing:SF-2026-ARXIV-2605-15957:start -->Ch49 already owns heterogeneous CPU/GPU execution plans, phase-aware placement, data-layout conversion and fallback; MaxVec is a vector-search realization.<!-- existing:SF-2026-ARXIV-2605-15957:end -->
<!-- delta:SF-2026-ARXIV-2605-15957:start -->Ch49 already owns heterogeneous CPU/GPU execution plans, phase-aware placement, data-layout conversion and fallback; MaxVec is a vector-search realization.<!-- delta:SF-2026-ARXIV-2605-15957:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15957:end -->

<!-- books-review:SF-2026-ARXIV-2605-15960:start -->
<!-- existing:SF-2026-ARXIV-2605-15960:start -->Ch25 explicitly distinguishes model error from planner exploitation and requires adversarial imagined-rollout validation.<!-- existing:SF-2026-ARXIV-2605-15960:end -->
<!-- delta:SF-2026-ARXIV-2605-15960:start -->Ch25 explicitly distinguishes model error from planner exploitation and requires adversarial imagined-rollout validation.<!-- delta:SF-2026-ARXIV-2605-15960:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15960:end -->

<!-- books-review:SF-2026-ARXIV-2605-15967:start -->
<!-- existing:SF-2026-ARXIV-2605-15967:start -->Ch25 already separates observed, latent and imagined state and supports executable causal transition substrates with intervention boundaries.<!-- existing:SF-2026-ARXIV-2605-15967:end -->
<!-- delta:SF-2026-ARXIV-2605-15967:start -->Ch25 already separates observed, latent and imagined state and supports executable causal transition substrates with intervention boundaries.<!-- delta:SF-2026-ARXIV-2605-15967:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15967:end -->

<!-- books-review:SF-2026-ARXIV-2605-16035:start -->
<!-- existing:SF-2026-ARXIV-2605-16035:start -->Ch84 already requires agent/operator/service identity, signed ownership, delegation scope and accountable action traces.<!-- existing:SF-2026-ARXIV-2605-16035:end -->
<!-- delta:SF-2026-ARXIV-2605-16035:start -->Ch84 already requires agent/operator/service identity, signed ownership, delegation scope and accountable action traces.<!-- delta:SF-2026-ARXIV-2605-16035:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16035:end -->

<!-- books-review:SF-2026-ARXIV-2605-16154:start -->
<!-- existing:SF-2026-ARXIV-2605-16154:start -->Ch26 already treats action chunks, control frequency and rollout allocation as workload-specific training/runtime trade-offs; probabilistic masking is a local optimization.<!-- existing:SF-2026-ARXIV-2605-16154:end -->
<!-- delta:SF-2026-ARXIV-2605-16154:start -->Ch26 already treats action chunks, control frequency and rollout allocation as workload-specific training/runtime trade-offs; probabilistic masking is a local optimization.<!-- delta:SF-2026-ARXIV-2605-16154:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16154:end -->

<!-- books-review:SF-2026-ARXIV-2605-16184:start -->
<!-- existing:SF-2026-ARXIV-2605-16184:start -->`books/part-04-training-system/36-distributed-training.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-16184:end -->
<!-- delta:SF-2026-ARXIV-2605-16184:start -->Second-order state moves to heterogeneous memory under hook-driven overlap and bounded-staleness coherence; the runtime, not only the optimizer, now owns update timing and consistency.<!-- delta:SF-2026-ARXIV-2605-16184:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-16184:end -->

<!-- books-review:SF-2026-ARXIV-2605-16194:start --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16194:end -->

<!-- books-review:SF-2026-ARXIV-2605-16198:start -->
<!-- existing:SF-2026-ARXIV-2605-16198:start -->Ch72 already carries formal properties, bounded-state monitors, intervention, auditor false negatives and verification scope limits.<!-- existing:SF-2026-ARXIV-2605-16198:end -->
<!-- delta:SF-2026-ARXIV-2605-16198:start -->Ch72 already carries formal properties, bounded-state monitors, intervention, auditor false negatives and verification scope limits.<!-- delta:SF-2026-ARXIV-2605-16198:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16198:end -->

<!-- books-review:SF-2026-ARXIV-2605-16217:start -->
<!-- existing:SF-2026-ARXIV-2605-16217:start -->Ch76 already owns search, evidence graph growth, claim verification, synthesis and complementary retrieval under provenance constraints.<!-- existing:SF-2026-ARXIV-2605-16217:end -->
<!-- delta:SF-2026-ARXIV-2605-16217:start -->Ch76 already owns search, evidence graph growth, claim verification, synthesis and complementary retrieval under provenance constraints.<!-- delta:SF-2026-ARXIV-2605-16217:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16217:end -->

<!-- books-review:SF-2026-ARXIV-2605.16007:start -->
<!-- existing:SF-2026-ARXIV-2605.16007:start -->Ch49 already includes NPU/CPU phase ownership, quantized candidate generation, host reranking and heterogeneous scheduling; this is architecture-specific evidence.<!-- existing:SF-2026-ARXIV-2605.16007:end -->
<!-- delta:SF-2026-ARXIV-2605.16007:start -->Ch49 already includes NPU/CPU phase ownership, quantized candidate generation, host reranking and heterogeneous scheduling; this is architecture-specific evidence.<!-- delta:SF-2026-ARXIV-2605.16007:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605.16007:end -->

<!-- books-review:SF-2026-ARXIV-2605.16234:start -->
<!-- existing:SF-2026-ARXIV-2605.16234:start -->`books/part-02-model/17-transformer-layer.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605.16234:end -->
<!-- delta:SF-2026-ARXIV-2605.16234:start -->Layer redundancy conclusions change between replacement and interchange protocols, so pruning must freeze intervention semantics and evaluator identity before treating layers as substitutable.<!-- delta:SF-2026-ARXIV-2605.16234:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605.16234:end -->

<!-- books-review:SF-2026-ARXIV-2605.16255:start -->
<!-- existing:SF-2026-ARXIV-2605.16255:start -->`books/part-06-ai-infrastructure/70-cost.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605.16255:end -->
<!-- delta:SF-2026-ARXIV-2605.16255:start -->AI power design is reframed from installed megawatts to deployable capacity across rack generations, linking topology, placement and redundancy to multi-resource stranding.<!-- delta:SF-2026-ARXIV-2605.16255:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605.16255:end -->

<!-- books-review:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:start -->
<!-- existing:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:start -->已逐章核对 `books/part-07-agent/84-agent-platform.md` 的“Agent Runtime State Machine；Scheduling 不只是 GPU；Release、Canary 与 Rollback”：现章已把 run identity、runtime state、调度和发布纳入平台；缺少质量门控的执行粒度、verification-gated skill admission 与价值-能耗 stop controller。<!-- existing:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:end --> <!-- delta:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:start -->exact-v1 新增 delta 是“Local agent execution needs an explicit stop controller that trades expected task value against marginal energy rather than running every trajectory to a fixed cap.”。<!-- delta:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:end --> 相邻章节 `books/part-07-agent/83-mcp.md` 只保留 handoff。正文写回位于 `books/part-07-agent/84-agent-platform.md#L429-L439`，并由 `post-write-audit-v1:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION` 验证；状态为 integrated/post-write-passed。
<!-- books-review:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:end -->

<!-- books-review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->
<!-- existing:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->已对读当前 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`。Execution/Evaluation 已将 quantization 视为行为变换，要求 dense-vs-quantized per-example correctness、slice、校准及真实硬件验证；该 family 直接落在现有 contract 内。<!-- existing:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->
<!-- delta:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->dense-vs-quantized 的 item-level divergence 强化既有行为回归 gate；相同命题已完整存在，新增论文名称不会改善论证。<!-- delta:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->
<!-- existing:SF-2026-ARXIV-2605-15220:start -->当前对读 `books/part-04-training-system/27-data.md` 与相邻章节后：Ch27 已把 mixture 写成版本化 data control plane，也讨论交互实验，但没有当前模型 adapter 插值驱动的跨训练阶段 on-policy mixture 分支。 Owner snapshot sha256=`b70df07b3fcb120b15cde29f53bf2551818f0b5a5cce99153dbd7a21a4cfbcd5`。<!-- existing:SF-2026-ARXIV-2605-15220:end -->
<!-- delta:SF-2026-ARXIV-2605-15220:start -->Exact-v1 新增：候选 mixture 由当前模型的低秩 adapter 插值提出，统一覆盖 pretraining、continual midtraining 与 instruction tuning；controller 节省 proxy compute，但仍受 adapter 近似误差、候选域集合与 scale transfer 限制。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15220:end -->

<!-- existing:SF-2026-ARXIV-2605-15250:start -->当前对读 `books/part-02-model/15-multi-head-attention.md` 与相邻章节后：Ch15 已说明压缩 latent state 必须保留可分片轴，也明确普通 checkpoint 不能任意在 MHA/GQA/MQA 间无损切换；尚缺‘专门参数化后同权重可合法暴露双 decode path’这一条件分支。 Owner snapshot sha256=`619ff7dc2733ab899fcdcd2d9e0cfd91c178c00b6809af701778f6a64a677d34`。<!-- existing:SF-2026-ARXIV-2605-15250:end -->
<!-- delta:SF-2026-ARXIV-2605-15250:start -->Exact-v1 新增：同一 GQLA 权重暴露 MQA-absorb compact-cache 与 per-group GQA expanded-cache 两条代数等价路径，runtime 按硬件 roofline 和 TP 选择；这不是任意 checkpoint 的无损改写，代价是训练/转换、expanded cache 与路径验收。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15250:end -->

<!-- existing:SF-2026-ARXIV-2605-15290:start -->当前对读 `books/part-04-training-system/28-pretraining.md` 与相邻章节后：Ch28 已区分 hyperparameter transfer 与 feature learning regime，但没有 GQA repetition/rank 使标准 μP 推导失效及其修正。 Owner snapshot sha256=`db601e3351f7931d229c1fd409347e977d2cd710be4466e9aec083858775bcb3`。<!-- existing:SF-2026-ARXIV-2605-15290:end -->
<!-- delta:SF-2026-ARXIV-2605-15290:start -->Exact-v1 新增：modified spectral norm 在非满秩权重下保留有效 scaling law，并导出 GQA repetition、depth 与 weight-decay 的 maximal-update scaling；transfer 证据限论文模型形状和 coordinate checks。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15290:end -->

<!-- existing:SF-2026-ARXIV-2605-15484:start -->当前对读 `books/part-02-model/21-moe.md` 与相邻章节后：Ch21 已覆盖 fixed/variable top-k、capacity 与 matched-compute gate，但没有把 backbone compute leverage 和 batch-axis dispatch 作为视觉 MoE 可行性的独立坐标。 Owner snapshot sha256=`6b7186654f0da7f619be02f0b1deb6bf934282621c6c067c37c366daf4050823`。<!-- existing:SF-2026-ARXIV-2605-15484:end -->
<!-- delta:SF-2026-ARXIV-2605-15484:start -->Exact-v1 新增：MoE 收益取决于 expert branch 占全 backbone compute 的 leverage；只改 top-k 可在固定架构下反转收益，batch-axis Soft-MoE 在 per-sample CNN 中还是主要 failure mode。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15484:end -->

<!-- existing:SF-2026-ARXIV-2605-15492:start -->当前对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节后：Ch26 已拥有 action chunk、flow/diffusion latency 与 controller authority，但没有连续多项式轨迹把生成 cadence 与控制频率解耦的替代表示。 Owner snapshot sha256=`6ccdc08b7cbf228f71718cf2d887be98d5f54f49bf1df45056ad99ef8d140b42`。<!-- existing:SF-2026-ARXIV-2605-15492:end -->
<!-- delta:SF-2026-ARXIV-2605-15492:start -->Exact-v1 新增：连续 Legendre trajectory 让单次生成覆盖长 horizon，并可解析求导给 controller feed-forward；history anchor 缩短 flow path，但多项式拟合、长 horizon drift 与稀疏演示边界仍需 controller 验证。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15492:end -->

<!-- existing:SF-2026-ARXIV-2605-16165:start -->当前对读 `books/part-04-training-system/28-pretraining.md` 与相邻章节后：Ch28 已把 objective、parameterization、optimizer state 与数据变换绑定，但没有 modality competition 的 Fisher-orthogonal variance correction 或 multi-level folding。 Owner snapshot sha256=`db601e3351f7931d229c1fd409347e977d2cd710be4466e9aec083858775bcb3`。<!-- existing:SF-2026-ARXIV-2605-16165:end -->
<!-- delta:SF-2026-ARXIV-2605-16165:start -->Exact-v1 新增：ML-FOP-SOAP 用曲率感知 projection 抑制跨模态方差冲突，并以 hierarchical folding 降低 gradient-accumulation micro-step 成本；证据限 Janus/Emu3、作者 batch 与 Fisher/tensor-preconditioner 近似。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-16165:end -->

<!-- existing:SF-2026-ARXIV-2605-16241:start -->当前对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节后：Ch26 §‘Privileged 3D Teacher 可以留在训练期，不能冒充运行时观测’已明确 training-only privileged target、student representation、部署移除 teacher、噪声传播与 controller/safety authority，足以承载本项长期机制。 Owner snapshot sha256=`6ccdc08b7cbf228f71718cf2d887be98d5f54f49bf1df45056ad99ef8d140b42`。<!-- existing:SF-2026-ARXIV-2605-16241:end -->
<!-- delta:SF-2026-ARXIV-2605-16241:start -->Exact-v1 新增：训练期 VLM 提供 phase/direction semantic targets，student 部署时独立运行；收益限 LIBERO 与两类 teacher，语义监督不取得物理提交权。 Decision=`No Change — Existing Coverage`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-16241:end -->

<!-- existing:SF-2026-ARXIV-2605-15239:start -->当前对读 `books/part-04-training-system/29-sft.md` 与相邻章节后：Ch29 已覆盖 on-policy distillation 的 state-distribution mismatch，但尚未拥有 safety privileged-context 的有效性筛选、teacher flip rate 与 early compliance-token 边界。 Owner snapshot sha256=`ef1699d49f0b708a8364e024522a498d6d9b6f2981953f715b7179738dc27a6f`。<!-- existing:SF-2026-ARXIV-2605-15239:end -->
<!-- delta:SF-2026-ARXIV-2605-15239:start -->Exact-v1 新增：teacher flip rate 先筛出能把 unsafe rollout 翻为 safe 的 privileged context，再在 student on-policy token 上施加 dense KL；早期 compliance token 集中更新是受限机制证据，不是普遍无税安全对齐保证。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15239:end -->

<!-- existing:SF-2026-ARXIV-2605-15224:start -->当前对读 `books/part-04-training-system/33-grpo.md` 与相邻章节后：Ch33/Ch80 已讨论 critic、self-critique 与 scaffold-removal，但没有共享 backbone 的 joint solver/critic objective、distribution-calibrated transfer 和 role-wise group advantage。 Owner snapshot sha256=`71afb6ee9d553b256ccfbecea5c1ec46bc098cc0ec419d890feb6cf510c57e4b`。<!-- existing:SF-2026-ARXIV-2605-15224:end -->
<!-- delta:SF-2026-ARXIV-2605-15224:start -->Exact-v1 新增：solver 与 critic 联合训练；critic reward 绑定 solver 后续增益，distribution ratio 限制 critique-conditioned 到 critique-free 的迁移，role-wise advantage 稳定两角色更新。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15224:end -->

<!-- existing:SF-2026-ARXIV-2605-15300:start -->当前对读 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节后：Ch23 已拥有 visual encoder/projector 与 alignment 一般机制，但没有‘以小 VLM perceiver 提前消化浅层对齐、保留目标 LLM 推理深度’的分支。 Owner snapshot sha256=`8c0c12e94af35dd1cf017ba9b664188508eaec7d7941ee64605a5e27b6644030`。<!-- existing:SF-2026-ARXIV-2605-15300:end -->
<!-- delta:SF-2026-ARXIV-2605-15300:start -->Exact-v1 新增：用可复用小 VLM 取代 ViT+projector 作为 perceiver，使视觉表示在进入目标 LLM 前先经过 language blocks；代价是额外 perceiver compute、模块兼容和对其文本能力的依赖。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15300:end -->

<!-- existing:SF-2026-ARXIV-2605-15491:start -->当前对读 `books/part-02-model/17-transformer-layer.md` 与相邻章节后：Ch17 解释 residual/layer state 与可移除性，尚未拥有 pruning 后 boundary-activation mismatch 的闭式恢复 operator。 Owner snapshot sha256=`d7d68284f08d6346a8e8b0b8befb568250625ed85c633db8b86560618ca56394`。<!-- existing:SF-2026-ARXIV-2605-15491:end -->
<!-- delta:SF-2026-ARXIV-2605-15491:start -->Exact-v1 新增：在被删 block 的边界收集 activation pair，解 unconstrained closed-form linear alignment 并插回模型；它保留 pruning speedup但引入 calibration dependence、operator state 和未测分布风险。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15491:end -->

<!-- existing:SF-2026-ARXIV-2605-16233:start -->当前对读 `books/part-07-agent/77-memory.md` 与相邻章节后：Ch77 已有 failure receipt、memory admission 与 rollback，却没有 population-level champion broadcast、graduation 和跨实例污染/成本边界。 Owner snapshot sha256=`802b9647ef7a07a5745f166806e095eda2e76f2336cf90cada9eb7e5f36e3935`。<!-- existing:SF-2026-ARXIV-2605-16233:end -->
<!-- delta:SF-2026-ARXIV-2605-16233:start -->Exact-v1 新增：外环按 stage 选 champion 并广播自然语言 memory，graduation 主要节省 compute；broadcast ablation 支持传播是收益机制，但全部证据限 CAGE-2 B-line，错误 champion 也会扩大污染。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-16233:end -->

<!-- existing:SF-2026-ARXIV-2605-16143:start -->当前对读 `books/part-07-agent/79-planning.md` 与相邻章节后：Ch79 §‘先校准不确定性，再决定行动、询问或探索’已把 expected information gain、ask/explore cost、act/gather/defer 与 observed-outcome belief update 绑定，并保留预算上限和低置信回退；本项没有改变该长期控制结构。 Owner snapshot sha256=`362120bd9edc9b31c70b93593f29610cce7fad4a1e9047533926142834a5f842`。<!-- existing:SF-2026-ARXIV-2605-16143:end -->
<!-- delta:SF-2026-ARXIV-2605-16143:start -->Exact-v1 新增：先用预算发现 state/object/affordance checkpoints，再带 grounded knowledge 执行任务；ECC 是受限环境 coverage proxy，不是开放环境完整性证明。 Decision=`No Change — Existing Coverage`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-16143:end -->

<!-- existing:SF-2026-ARXIV-2605-15309:start -->当前对读 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节后：Ch24 已把 serial dimension 从 output length 改为 refinement steps，并明确 mutable provisional state、repeated revision、commit gate、训练分布与 runtime budget；本项是该机制在 IMLE mapper 的受限实现。 Owner snapshot sha256=`1ca25bfdf30fff824f73fb0ff8175de062d70cf84689b67ec471e34b9a4c520e`。<!-- existing:SF-2026-ARXIV-2605-15309:end -->
<!-- delta:SF-2026-ARXIV-2605-15309:start -->Exact-v1 新增：同一 mapper 递归 H/L cycles，推理 refinement 数可独立于训练设置变化；结果限 IMLE/StyleGAN 与所测图像数据，不证明无限递归稳定。 Decision=`No Change — Existing Coverage`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15309:end -->

<!-- existing:SF-2026-ARXIV-2605-15458:start -->当前对读 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节后：Ch24 已管理 refinement trajectory 与 step budget，Ch33 已管理 verifiable reward，但当前 owner 尚未连接 video SDE trajectory、early-step credit 与 verifiable visual reasoning reward。 Owner snapshot sha256=`1ca25bfdf30fff824f73fb0ff8175de062d70cf84689b67ec471e34b9a4c520e`。<!-- existing:SF-2026-ARXIV-2605-15458:end -->
<!-- delta:SF-2026-ARXIV-2605-15458:start -->Exact-v1 新增：对 video diffusion/flow trajectory 使用 SDE-GRPO，并把 compute 聚焦到决定全局结构的早期 steps；reward 仅覆盖可程序验证的 maze/FlowFree/Sokoban 条件，不能外推开放视频语义或真实 latency。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15458:end -->

<!-- existing:SF-2026-ARXIV-2605-15217:start -->当前对读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节后：Ch66 已明确 internal representation 可解码不等于 causal use，并要求 decodability、intervention 与 output behavior 分层；现有 activation failure probe note 也保留模型/任务/线性配置边界，已承载 dual-layer diagnostic ladder。 Owner snapshot sha256=`cbfd7c82a4ac8446fdecdcf297929755be0dded3dbb84b712b561867f8aa6454`。<!-- existing:SF-2026-ARXIV-2605-15217:end -->
<!-- delta:SF-2026-ARXIV-2605-15217:start -->Exact-v1 新增：matched mortgage prompts 显示 output parity 与 latent divergence 并存，跨层 steering 暴露方向不对称的因果敏感性；证据限三类开源模型、该决策任务与 intervention design。 Decision=`No Change — Existing Coverage`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15217:end -->

<!-- existing:SF-2026-ARXIV-2605-15248:start -->当前对读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节后：Ch72 已覆盖 PII/memorization、targeted extraction 与未命中非删除证明，但没有 test-generation 作为 realistic code-context elicitation，以及 feature-library/version identity。 Owner snapshot sha256=`eff666119d1482106b6296751c84866c60059573be887d5d7b7fabb8a8d79845`。<!-- existing:SF-2026-ARXIV-2605-15248:end -->
<!-- delta:SF-2026-ARXIV-2605-15248:start -->Exact-v1 新增：scenario→code question→generated function→test cases 的 pipeline 用 feature library 替代手工 prompt，检测率提升仅证明五个所测模型和 judge/validation protocol；它不证明未命中即无泄漏。 Decision=`Integrate`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15248:end -->

<!-- existing:SF-2026-ARXIV-2605-15298:start -->当前对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节后：Ch26 §‘数据演进：从专用演示到多来源对齐’已明确 human video 没有原生 robot action，需 derived state-transition/trajectory labels、embodiment/action-schema alignment、provenance 与 closed-loop validation，足以承载本项长期链路。 Owner snapshot sha256=`6ccdc08b7cbf228f71718cf2d887be98d5f54f49bf1df45056ad99ef8d140b42`。<!-- existing:SF-2026-ARXIV-2605-15298:end -->
<!-- delta:SF-2026-ARXIV-2605-15298:start -->Exact-v1 新增：human video 先成为 structured physical QA prior，再通过 language-sensitive adaptation 进入 VLA；SOTA 结果限披露 benchmark，不能证明物理 truth、未见 embodiment 或闭环安全。 Decision=`No Change — Existing Coverage`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15298:end -->

<!-- existing:SF-2026-ARXIV-2605-15734:start -->当前对读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节后：Ch66 已要求 repeated sampling、within-model reliable-change interval、sampling variance 与 item-level harmed/helped ledger，并把 construct、slice、calibration 和 evaluator identity 分开；本项没有改变该 evaluation contract。 Owner snapshot sha256=`cbfd7c82a4ac8446fdecdcf297929755be0dded3dbb84b712b561867f8aa6454`。<!-- existing:SF-2026-ARXIV-2605-15734:end -->
<!-- delta:SF-2026-ARXIV-2605-15734:start -->Exact-v1 新增：同一 metric 的 individual repeatability 与 aggregate analytical utility必须分别判定；证据只覆盖论文定义的 213 metrics、三模型与 replication protocol。 Decision=`No Change — Existing Coverage`；作者侧不写共享 Books。<!-- delta:SF-2026-ARXIV-2605-15734:end -->

结论：**31 Integrate / 33 No Change；Integrate 仅进入 root queue，作者未写 Books。**
<!-- books-review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->

<!-- books-review:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:start -->
<!-- existing:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:start -->`books/part-07-agent/84-agent-platform.md` 已以更一般的 AGENT-PLATFORM 演进链承载 `SkillSmith: Compiling Agent Skills into Boundary-Guided Runtime Interfaces` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:end -->
<!-- delta:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:start -->To this end, we propose SkillSmith, a boundary-first compiler-runtime framework that compiles skill packages offline into minimal executable interfaces.<!-- delta:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:end -->

<!-- books-review:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:start -->
<!-- existing:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:start -->已逐章核对 `books/part-07-agent/82-multi-agent.md` 的“Coordination Tax；Message 不是 State；Verification 与 Aggregation”：现章已要求度量 coordination tax、隔离 message/state 并治理更新；缺少 sequential agent updates 导致 occupancy shift 时的 resampling 与 per-agent trust region。<!-- existing:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:end --> <!-- delta:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:start -->exact-v1 新增 delta 是“Sequentially fine-tuning interacting agents invalidates cached-rollout occupancy; resampling and per-agent trust regions make the joint update contract explicit.”。<!-- delta:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:end --> 相邻章节 `books/part-07-agent/81-workflow.md`、`books/part-07-agent/83-mcp.md` 只保留 handoff。正文写回位于 `books/part-07-agent/82-multi-agent.md#L430-L442`，并由 `post-write-audit-v1:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT` 验证；状态为 integrated/post-write-passed。
<!-- books-review:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:end -->

<!-- books-review:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->
<!-- existing:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；owner 当前主干包含 ['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end -->
<!-- delta:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->We introduce a Distributed Trust Framework (DTF), a verification framework for governed mutation systems that computes execution authority from structured, verifiable artifacts.<!-- delta:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end --> Independent decision=`Integrate`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end -->

### 原始来源

- [SDOF: Taming the Alignment Tax in Multi-Agent Orchestration with State-Constrained Dispatch](https://arxiv.org/html/2605.15204v1) — `arXiv:2605.15204v1`
- [Hydra: Efficient, Correct Code Generation via Checkpoint-and-Rollback Support](https://arxiv.org/html/2605.15238v1) — `arXiv:2605.15238v1`
- [Training on Documents About Monitoring Leads to CoT Obfuscation](https://arxiv.org/html/2605.15257v1) — `arXiv:2605.15257v1`
- [Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](https://arxiv.org/html/2605.15338v1) — `arXiv:2605.15338v1`
- [Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute](https://arxiv.org/html/2605.15377v1) — `arXiv:2605.15377v1`
- [Is One Score Enough? Rethinking the Evaluation of Sequentially Evolving LLM Memory](https://arxiv.org/html/2605.15384v1) — `arXiv:2605.15384v1`
- [$ϕ$-Balancing for Mixture-of-Experts Training](https://arxiv.org/html/2605.15403v1) — `arXiv:2605.15403v1`
- [DualKV: Shared-Prompt Flash Attention for Efficient RL Training with Large Rollouts and Long Contexts](https://arxiv.org/html/2605.15422v1) — `arXiv:2605.15422v1`
- [Runtime-Structured Task Decomposition for Agentic Coding Systems](https://arxiv.org/html/2605.15425v1) — `arXiv:2605.15425v1`
- [Entity-Centric World Models: Interaction-Aware Masking for Causal Video Prediction](https://arxiv.org/html/2605.15466v1) — `arXiv:2605.15466v1`
- [EgoExo-WM: Unlocking Exo Video for Ego World Models](https://arxiv.org/html/2605.15477v1) — `arXiv:2605.15477v1`
- [STS: Efficient Sparse Attention with Speculative Token Sparsity](https://arxiv.org/html/2605.15508v1) — `arXiv:2605.15508v1`
- [RoPE Distinguishes Neither Positions Nor Tokens in Long Contexts, Provably](https://arxiv.org/html/2605.15514v1) — `arXiv:2605.15514v1`
- [On the Fragility of Data Attribution When Learning Is Distributed](https://arxiv.org/html/2605.15520v1) — `arXiv:2605.15520v1`
- [Process Rewards with Learned Reliability](https://arxiv.org/html/2605.15529v1) — `arXiv:2605.15529v1`
- [AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs](https://arxiv.org/html/2605.15565v1) — `arXiv:2605.15565v1`
- [Response-Conditioned Parallel-to-Sequential Orchestration for Multi-Agent Systems](https://arxiv.org/html/2605.15573v1) — `arXiv:2605.15573v1`
- [STAR: A Stage-attributed Triage and Repair framework for RCA Agents in Microservices](https://arxiv.org/html/2605.15581v1) — `arXiv:2605.15581v1`
- [PSD: Pushing the Pareto Frontier of Diffusion LLMs via Parallel Speculative Decoding](https://arxiv.org/html/2605.15609v1) — `arXiv:2605.15609v1`
- [A Few GPUs, A Whole Lotta Scale: Faithful LLM Training Emulation with PrismLLM](https://arxiv.org/html/2605.15617v1) — `arXiv:2605.15617v1`
- [Latent Video Prediction Learns Better World Models](https://arxiv.org/html/2605.15618v1) — `arXiv:2605.15618v1`
- [Rethinking the Security of DP-SGD: A Corrected Analysis of Differentially Private Machine Learning](https://arxiv.org/html/2605.15648v1) — `arXiv:2605.15648v1`
- [PRISM: Prompt Reliability via Iterative Simulation and Monitoring for Enterprise Conversational AI](https://arxiv.org/html/2605.15665v1) — `arXiv:2605.15665v1`
- [Going Beyond the Edge: Distributed Inference of Transformer Models on Ultra-Low-Power Wireless Devices](https://arxiv.org/html/2605.15694v1) — `arXiv:2605.15694v1`
- [SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory](https://arxiv.org/html/2605.15710v1) — `arXiv:2605.15710v1`
- [Can We Trust AI-Inferred User States. A Psychometric Framework for Validating the Reliability of Users States Classification by LLMs in Operational Environments](https://arxiv.org/html/2605.15734v1) — `arXiv:2605.15734v1`
- [A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation](https://arxiv.org/html/2605.15761v1) — `arXiv:2605.15761v1`
- [SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?](https://arxiv.org/html/2605.15777v1) — `arXiv:2605.15777v1`
- [BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge](https://arxiv.org/html/2605.15815v1) — `arXiv:2605.15815v1`
- [RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades](https://arxiv.org/html/2605.15846v1) — `arXiv:2605.15846v1`
- [To GPU or Not to GPU: Vector Search in Relational Engines](https://arxiv.org/html/2605.15957v1) — `arXiv:2605.15957v1`
- [Imperfect World Models are Exploitable](https://arxiv.org/html/2605.15960v1) — `arXiv:2605.15960v1`
- [Deterministic Event-Graph Substrates as World Models for Counterfactual Reasoning](https://arxiv.org/html/2605.15967v1) — `arXiv:2605.15967v1`
- [Who Owns This Agent? Tracing AI Agents Back to Their Owners](https://arxiv.org/html/2605.16035v1) — `arXiv:2605.16035v1`
- [Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking](https://arxiv.org/html/2605.16154v1) — `arXiv:2605.16154v1`
- [Runtime-Orchestrated Second-Order Optimization for Scalable LLM Training](https://arxiv.org/html/2605.16184v1) — `arXiv:2605.16184v1`
- [Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems](https://arxiv.org/html/2605.16198v1) — `arXiv:2605.16198v1`
- [Argus: Evidence Assembly for Scalable Deep Research Agents](https://arxiv.org/html/2605.16217v1) — `arXiv:2605.16217v1`
- [Ascend-RaBitQ: Heterogeneous NPU-CPU Acceleration of Billion-Scale Similarity Search with 1-bit Quantization](https://arxiv.org/html/2605.16007v1) — `arXiv:2605.16007v1`
- [No Free Swap: Protocol-Dependent Layer Redundancy in Transformers](https://arxiv.org/html/2605.16234v1) — `arXiv:2605.16234v1`
- [Designing Datacenter Power Delivery Hierarchies for the AI Era](https://arxiv.org/html/2605.16255v1) — `arXiv:2605.16255v1`
- [AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices](https://arxiv.org/html/2605.15206v1) — `arXiv:2605.15206v1`
- [Quantization Undoes Alignment: Bias Emergence in Compressed LLMs Across Models and Precision Levels](https://arxiv.org/html/2605.15208v1) — `arXiv:2605.15208v1`
- [SkillSmith: Compiling Agent Skills into Boundary-Guided Runtime Interfaces](https://arxiv.org/html/2605.15215v1) — `arXiv:2605.15215v1`
- [TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination](https://arxiv.org/html/2605.15207v1) — `arXiv:2605.15207v1`
- [Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems](https://arxiv.org/html/2605.15228v1) — `arXiv:2605.15228v1`
- [Fair outputs, Biased Internals: Causal Potency and Asymmetry of Latent Bias in LLMs for High-Stakes Decisions](https://arxiv.org/html/2605.15217v1) — `arXiv:2605.15217v1`
- [Always Learning, Always Mixing: Efficient and Simple Data Mixing All The Time](https://arxiv.org/html/2605.15220v1) — `arXiv:2605.15220v1`
- [ICRL: Learning to Internalize Self-Critique with Reinforcement Learning](https://arxiv.org/html/2605.15224v1) — `arXiv:2605.15224v1`
- [Reducing the Safety Tax in LLM Safety Alignment with On-Policy Self-Distillation](https://arxiv.org/html/2605.15239v1) — `arXiv:2605.15239v1`
- [Probing Privacy Leaks in LLM-based Code Generation via Test Generation](https://arxiv.org/html/2605.15248v1) — `arXiv:2605.15248v1`
- [GQLA: Group-Query Latent Attention for Hardware-Adaptive Large Language Model Decoding](https://arxiv.org/html/2605.15250v1) — `arXiv:2605.15250v1`
- [GQA-μP: The maximal parameterization update for grouped query attention](https://arxiv.org/html/2605.15290v1) — `arXiv:2605.15290v1`
- [PhysBrain 1.0 Technical Report](https://arxiv.org/html/2605.15298v1) — `arXiv:2605.15298v1`
- [Deep Pre-Alignment for VLMs](https://arxiv.org/html/2605.15300v1) — `arXiv:2605.15300v1`
- [One Pass Is Not Enough: Recursive Latent Refinement for Generative Models](https://arxiv.org/html/2605.15309v1) — `arXiv:2605.15309v1`
- [Video Models Can Reason with Verifiable Rewards](https://arxiv.org/html/2605.15458v1) — `arXiv:2605.15458v1`
- [When Does Sparse MoE Help in Vision? The Role of Backbone Compute Leverage in Sparse Routing](https://arxiv.org/html/2605.15484v1) — `arXiv:2605.15484v1`
- [Ghosted Layers: Unconstrained Activation Alignment for Recovering Layer-Pruned LLMs](https://arxiv.org/html/2605.15491v1) — `arXiv:2605.15491v1`
- [FLASH: Efficient Visuomotor Policy via Sparse Sampling](https://arxiv.org/html/2605.15492v1) — `arXiv:2605.15492v1`
- [Look Before You Leap: Autonomous Exploration for LLM Agents](https://arxiv.org/html/2605.16143v1) — `arXiv:2605.16143v1`
- [Second-Order Multi-Level Variance Correction for Modality Competition in Multimodal Models](https://arxiv.org/html/2605.16165v1) — `arXiv:2605.16165v1`
- [FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast](https://arxiv.org/html/2605.16233v1) — `arXiv:2605.16233v1`
- [Offline Semantic Guidance for Efficient Vision-Language-Action Policy Distillation](https://arxiv.org/html/2605.16241v1) — `arXiv:2605.16241v1`

## 5. 缺口与下一步

本轮材料 blocker：无。38 项 reuse 最终落为 32 项可重放历史 locator/version/claim、4 项 current exact-v1 定点复核和 2 项移出候选；六个非必要 current-abstract 状态探测超时已在作者返修记录中精确列出，但不阻断采用命题。`2605.15529` 原登记的 W20 locator 在当前仓库不存在，已明确标记 superseded/invalid，不伪造文件或 digest；fresh non-author reviewer 已直接复核官方 exact-v1 的 §4.1–4.3、§5、§6.1–6.3 与附录边界并接受原 adopted claim。

1. root 已按 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260518/root-books-writeback-queue-v3.json) 处理 31 个真实 Integrate：18 项既有正文与 13 项新增机制正文均通过 fresh non-author 写后语义复核；没有为 Existing Coverage 项重复追加。
2. `2605.15638` 已移出分母；其独占的 Monitoring 正文和 binding 已删除，Books 当前无该 family 残留。
3. official batch 归属、18 项准入、64 项 Evidence、31/33 Books 决定、marker 唯一性与实际正文承载均已完成最终复核；无剩余返修项。

Meta GIM 的既有日级冲突是本窗终态保留项：不用于正面证据、不进入 Books，也不支撑“无遗漏”断言。只有取得能消解 05-17/05-18 冲突的官方精确发布时间材料时，才定点重开该 Source Family；本次没有扩源重查它。

## 6. 复核

复核者：`fresh non-author final reviewer（未参与作者返修或 root Books 写回）`

结论：通过

Daily V3、Evidence 与 Books Gate 均为 Complete。

fresh non-author reviewer 独立复算 `537=64+473`、`64=32 current exact-v1+32 historical replay`、原 `38=32 replay+4 current recheck+2 removed`、`64=31 Integrate+33 No Change`。18 项新准入逐项对照 exact-v1，31 个 Integrate 均沿 owner marker 检查到 `Review notes` 前的真实正文；13 项新增正文和 18 项既有正文都承载旧方案、约束变化、state/control ownership、证据边界、trade-off、failure mode 与 fallback。上一轮未通过结论保留在 [`FRESH_NONAUTHOR_V3_AUDIT_20260915.md`](../_sources/daily-20260518/FRESH_NONAUTHOR_V3_AUDIT_20260915.md)，最终验收记录见 [`V3_FRESH_NONAUTHOR_POSTWRITE_FINAL_REVIEW_20260915.md`](../_sources/daily-20260518/V3_FRESH_NONAUTHOR_POSTWRITE_FINAL_REVIEW_20260915.md)。
