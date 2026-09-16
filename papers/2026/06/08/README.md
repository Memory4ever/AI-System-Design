# Daily Research — 2026-06-08

**规范：** V3
**窗口：** 2026-06-07T09:00:00+08:00 ～ 2026-06-08T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T22:00:00+08:00

## 1. 结论

本窗不能继承旧完成结论。498 个去重题摘身份经作者侧重审后又接受非作者 fresh audit；最终权威分母为 Candidate 48 / Close 450。独立复核从作者侧 50 项中关闭 2606.06818、2606.07017、2606.07119、2606.07190、2606.07412，并从 Close 恢复 2606.06915、2606.06991、2606.07054。逐项 exception 见 [JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md](../_sources/JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md)，作者侧 `50 / 448` 只保留为审计历史。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [厂商源再认证](../_sources/daily-20260601/CURRENT_CONTRACT_DAILY_SOURCE_RECERT_20260914.md#来源结论)：本窗无保留事件 | 已检查 | 无 |
| SRC-ANTHROPIC | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-GOOGLE-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-META-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-QWEN | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-DEEPSEEK | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MOONSHOT | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 同上；“全部”列表本窗无条目 | 已检查 | 无 |
| SRC-ZAI | 同上；Research 列表本窗无条目 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 同上；技术博客本窗无条目 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MINIMAX | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-ARXIV | [canonical-raw-identity-inventory-v2.1.json.gz](../_sources/daily-20260608/canonical-raw-identity-inventory-v2.1.json.gz)、[canonical-semantic-screening-checkpoint-v2.1.json.gz](../_sources/daily-20260608/canonical-semantic-screening-checkpoint-v2.1.json.gz)、[V3_SCREENING_LEDGER.md](../_sources/daily-20260608/V3_SCREENING_LEDGER.md) 与独立 [fresh audit](../_sources/JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md)；498 identities，最终分母 48 Candidate / 450 Close | 已检查 | 无 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [DxPTA: An Architecture Design Space Exploration with Optical Dataflow-guided Strategy for HW/SW Co-Design of Photonic Transformer Accelerators](https://arxiv.org/abs/2606.06515v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`INFER-TENSORRT-LLM` | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`（[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)) |
| [P-Cast Precision in FP8 Attention: Sink-Induced Collapse and the Optimality of S=2^8](https://arxiv.org/abs/2606.06521v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+2+2=7；exact-v1 与当前 claim 一致，owner=`INFER-TENSORRT-LLM` | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`（[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)) |
| [AgileOS: A GPU Operating System Layer for Protected CUDA Services](https://arxiv.org/abs/2606.06697v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Tensor Algebraic Property Skeletons: Amplifying Property-Based Testing for AI Compilers](https://arxiv.org/abs/2606.06747v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+3=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [StageFrontier: Synchronization-Aware Stage Accounting for Distributed ML Training](https://arxiv.org/abs/2606.06751v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-MONITORING` | 深入完成 | 已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)) |
| [SCALE: Scalable Cross-Attention Learning with Extrapolation for Agentic Workflow Scheduling](https://arxiv.org/abs/2606.06820v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+2=6；exact-v1 与当前 claim 一致，owner=`PLATFORM-GPU-SCHEDULER` | 深入完成 | 已有覆盖：`PLATFORM-GPU-SCHEDULER`（[books/part-06-ai-infrastructure/63-gpu-scheduler.md](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)) |
| [Data-Constrained Language Model Pretraining: Improved Regularization and Scaling Laws](https://arxiv.org/abs/2606.06888v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+3=7；exact-v1 与当前 claim 一致，owner=`TRAIN-PRETRAINING` | 深入完成 | 已有覆盖：`TRAIN-PRETRAINING`（[books/part-04-training-system/28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md)) |
| [GRASP: Geometry-aware Residual Alignment for Scalable Pretraining Data Attribution](https://arxiv.org/abs/2606.06892v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+2=6；exact-v1 与当前 claim 一致，owner=`TRAIN-DATA` | 深入完成 | 已有覆盖：`TRAIN-DATA`（[books/part-04-training-system/27-data.md](../../../../books/part-04-training-system/27-data.md)) |
| [From Sampled Outcomes to Capability Distributions: Rethinking Supervision for LLM Routing](https://arxiv.org/abs/2606.06924v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+3=7；exact-v1 与当前 claim 一致，owner=`INFER-SCHEDULING` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)) |
| [DataEvolver: Automatic Data Preparation for Large Language Models through Multi-Level Self-Evolving](https://arxiv.org/abs/2606.07001v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+2=6；exact-v1 与当前 claim 一致，owner=`TRAIN-DATA` | 深入完成 | 已有覆盖：`TRAIN-DATA`（[books/part-04-training-system/27-data.md](../../../../books/part-04-training-system/27-data.md)) |
| [PCCL: Process Group-Aware Scalable and Generic Collective Algorithm Synthesizer](https://arxiv.org/abs/2606.07019v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+3=7；exact-v1 与当前 claim 一致，owner=`TRAIN-DISTRIBUTED-TRAINING` | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)) |
| [Towards Tight Bounds for Streaming Attention](https://arxiv.org/abs/2606.07205v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+1+2=5；exact-v1 与当前 claim 一致，owner=`INFER-KV-CACHE` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)) |
| [Clairvoyant: Predictive Shortest-Job-First Admission for Serial LLM Inference](https://arxiv.org/abs/2606.07248v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；1+2+2=5；exact-v1 与当前 claim 一致，owner=`INFER-SCHEDULING` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)) |
| [Breaking the Ice: Analyzing Cold Start Latency in vLLM](https://arxiv.org/abs/2606.07362v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；1+2+2=5；exact-v1 与当前 claim 一致，owner=`INFER-VLLM` | 深入完成 | 已有覆盖：`INFER-VLLM`（[books/part-05-inference-system/50-vllm.md](../../../../books/part-05-inference-system/50-vllm.md)) |
| [Online Pandora's Box for Contextual LLM Cascading](https://arxiv.org/abs/2606.07392v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-SCHEDULING` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)) |
| [Lean4Agent: Formal Modeling and Verification for Agent Workflow and Trajectory](https://arxiv.org/abs/2606.06523v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`AGENT-WORKFLOW` | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)) |
| [Queen-Bee Agents: A BeeSpec-Centered Architecture for Governed Enterprise MCP Orchestration](https://arxiv.org/abs/2606.06545v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+3+2=7；exact-v1 与当前 claim 一致，owner=`AGENT-MCP` | 深入完成 | 已有覆盖：`AGENT-MCP`（[books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md)) |
| [Signal-Driven Observation for Long-Horizon Web Agents](https://arxiv.org/abs/2606.06708v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+3=7；exact-v1 与当前 claim 一致，owner=`AGENT-CONTEXT` | 深入完成 | 已有覆盖：`AGENT-CONTEXT`（[books/part-07-agent/75-context.md](../../../../books/part-07-agent/75-context.md)) |
| [Natural Language Access Control (NLAC): From Help Desk Requests to Structured Policies](https://arxiv.org/abs/2606.06726v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [OpenSkill: Open-World Self-Evolution for LLM Agents](https://arxiv.org/abs/2606.06741v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+2=6；exact-v1 与当前 claim 一致，owner=`AGENT-PLATFORM` | 深入完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [The Custody Envelope Threshold: Authority-Scaled Admission of External Artifacts in Institutional Infrastructure](https://arxiv.org/abs/2606.06767v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Towards Retrieving Interaction Spaces for Agentic Search](https://arxiv.org/abs/2606.06880v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+2=6；exact-v1 与当前 claim 一致，owner=`AGENT-RAG` | 深入完成 | 已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)) |
| [Workflow-to-Skill: Skill Creation via Routing-Workflow-Semantics-Attachments Decomposition](https://arxiv.org/abs/2606.06893v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+3=7；exact-v1 与当前 claim 一致，owner=`AGENT-WORKFLOW` | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)) |
| [From Privacy to Workflow Integrity: Communication-Graph Metadata in Autonomous Agent Interoperability](https://arxiv.org/abs/2606.07150v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+3+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety](https://arxiv.org/abs/2606.06529v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Diagnosing Evidence Utilization in Long-Context and Retrieval-Augmented Language Models under Matched Evidence Conditions](https://arxiv.org/abs/2606.06758v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills](https://arxiv.org/abs/2606.07131v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models](https://arxiv.org/abs/2606.07157v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+3=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests](https://arxiv.org/abs/2606.07379v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle](https://arxiv.org/abs/2606.07462v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+3=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning](https://arxiv.org/abs/2606.06915v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；1+2+2=5；exact-v1 与当前 claim 一致，owner=`INFER-SCHEDULING` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`；正文锚点[“Reasoning Budget 必须进入调度与评估身份”与“Model Routing 与 Test-time Scaling 必须结算同一个 Budget”](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Don't Pause: Streaming Video-Language Synchrony for Online Video Understanding](https://arxiv.org/abs/2606.06991v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+2=6；exact-v1 与当前 claim 一致，owner=`MULTIMODAL-REPRESENTATION` | 深入完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`；正文锚点[“Streaming Multimodal Identity 不止是 Token Type”与“实时多模态表示还必须拥有可中断的时间状态”](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，Ch42 只接手运行时请求生命周期 |
| [TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents](https://arxiv.org/abs/2606.07054v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+2=6；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`；正文锚点[“Trajectory Judge 必须区分叙述、动作与完成证据”](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Ch67 仅采集观测而不拥有 verdict |
| [Subtle Injection for Ground-truth Inference of LLM Training Data](https://arxiv.org/abs/2606.06502v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-SECURITY` | 标准完成 | 已有覆盖：`PLATFORM-SECURITY`；正文锚点[“memorization 与 adaptive extraction”及 membership/canary 审计边界](../../../../books/part-06-ai-infrastructure/72-security.md)，Ch27 只提供 provenance/canary 数据 handoff |
| [MacArena: Benchmarking Computer Use Agents on an Online macOS Environment](https://arxiv.org/abs/2606.06560v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [RECAP: Regression Evaluation for Continual Adaptation of Prompts](https://arxiv.org/abs/2606.06698v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Pomona: Continuous Code Quality Improvement via Small, Agentic Pull Requests at Bloomberg](https://arxiv.org/abs/2606.06752v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-WORKFLOW` | 标准完成 | 已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)) |
| [AdMem: Advanced Memory for Task-solving Agents](https://arxiv.org/abs/2606.06787v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Declarative Skills for AI Agents in Knowledge-Grounded Tool-Use Workflows](https://arxiv.org/abs/2606.06923v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-WORKFLOW` | 标准完成 | 已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)) |
| [Auditing Training Data in Domain-adapted LLMs: LoRA-MINT](https://arxiv.org/abs/2606.06946v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`TRAIN-DATA` | 标准完成 | 已有覆盖：`TRAIN-DATA`（[books/part-04-training-system/27-data.md](../../../../books/part-04-training-system/27-data.md)) |
| [FinEvolveBench: A Benchmark for Self-Evolving Agents on Low-Repetition Tasks with Implicit Rewards](https://arxiv.org/abs/2606.06960v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [MADE: Beyond Scoring via a Multilingual Agentic Diagnosing Engine for Fine-Grained Evaluation Insights](https://arxiv.org/abs/2606.07020v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [Beyond Rubrics: Exploration-Guided Evaluation Skills for Reward Modeling](https://arxiv.org/abs/2606.07040v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [SWE-Explore: Benchmarking How Coding Agents Explore Repositories](https://arxiv.org/abs/2606.07297v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning](https://arxiv.org/abs/2606.07299v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-PLATFORM` | 标准完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [Certifiable Semantic Agreement Among LLM Agents: What the Admissibility Instrument Decides](https://arxiv.org/abs/2606.07316v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MULTI-AGENT` | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)) |
| [M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions](https://arxiv.org/abs/2606.07402v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling](https://arxiv.org/abs/2606.07404v1) | 2026-06-08T08:00:00+08:00 ～ 2026-06-08T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`TRAIN-PRETRAINING` | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING`；正文锚点[“模型结构在训练中扩容时，state contract 还要包含 parameter mapping”](../../../../books/part-04-training-system/28-pretraining.md)，Ch36 仅接手并行布局和分布式 optimizer-state handoff |

候选分母最终冻结为 48；上表覆盖 33 个 prior 与 15 个 closure-recovered family。当前 disposition：45 项已有覆盖、3 项仅报告、0 项整合、0 项结构候选、0 项暂缓；3 条撤销采用链已由 root 清除。

## 4. 证据与知识整合

归档保留旧 exact-v1 证据，只在 identity/claim 不变时复用。独立 audit 将旧 13 项 disposition 重判为 10 项 `已有覆盖`、3 项撤回；new Integrate = 0，正文缺口 = 0。root 已删除 2606.06818、2606.07067、2606.07470 的 Books body/trace adoption chains。READY、QUEUE、POST_WRITE 与章末 trace 只能作为审计线索，不能授权 candidate 或 body。以下 15 项为本轮新恢复 Candidate 的同标题、同 URL Evidence；33 个 prior 的完整审阅由 [V2_1_EVIDENCE_ARCHIVE.md](../_sources/daily-20260608/V2_1_EVIDENCE_ARCHIVE.md) 提供。

### [ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning](https://arxiv.org/abs/2606.06915v1)

`arXiv:2606.06915v1`；exact-v1 披露 TTC strategies、reasoning scorers、quality-cost benchmark 与 OpenAI-compatible proxy。其长期命题是 reasoning compute 必须成为 request-level budget state，并与 model routing 在同一 controller 下结算；proxy/library 只是受限实现。Books：`已有覆盖`，canonical owner=`INFER-SCHEDULING`，锚点“Reasoning Budget 必须进入调度与评估身份”与“Model Routing 与 Test-time Scaling 必须结算同一个 Budget”。不外推到未披露硬件、并发、生产 tail SLO 或任意模型的最优预算。

### [Don't Pause: Streaming Video-Language Synchrony for Online Video Understanding](https://arxiv.org/abs/2606.06991v1)

`arXiv:2606.06991v1`；exact-v1 的 streaming assistant 以 frame-driven state 与分层控制避免生成时暂停感知。长期命题是输入 token 必须绑定 timestamp、stream revision 与 interrupt boundary；表示/fusion 拥有可消费观测，runtime 才拥有 continue/cancel/commit。Books：`已有覆盖`，canonical owner=`MULTIMODAL-REPRESENTATION`，Ch23 的 streaming identity 与可中断时间状态已承载；Ch42 只作 request-lifecycle handoff。作者 FPS/synchrony 只属于披露模型与 benchmark。

### [TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents](https://arxiv.org/abs/2606.07054v1)

`arXiv:2606.07054v1`；exact-v1 将跨 step evidence 聚合用于长程 trajectory judgment。长期命题是叙述、动作、环境变化与完成证据须按 authority 分层，judge 不能把 agent narrative 当 outcome。Books：`已有覆盖`，canonical owner=`PLATFORM-EVALUATION-SYSTEM`，锚点“Trajectory Judge 必须区分叙述、动作与完成证据”；`PLATFORM-MONITORING` 只负责采集 observation，不拥有 verdict。论文结果不外推到未披露环境和 production gate。

### [Subtle Injection for Ground-truth Inference of LLM Training Data](https://arxiv.org/abs/2606.06502v1)

`arXiv:2606.06502v1`；正文定位：3 Formal Framework；6.1 Simulation Design。用 canary 与 Neyman-Pearson FPR control 把训练数据 ownership 变成可取证、可验收的合同。 Evaluation：7 Results；7.4 Per-Strategy Analysis。 Limitations：8 Discussion；8.4 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，canonical owner=`PLATFORM-SECURITY`；Ch72 已区分 memorization、adaptive extraction、membership protocol 与 canary，Ch27 只提供 provenance/canary 数据 handoff。完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [MacArena: Benchmarking Computer Use Agents on an Online macOS Environment](https://arxiv.org/abs/2606.06560v1)

`arXiv:2606.06560v1`；正文定位：3.2 Benchmark Structure；Evaluation Framework.。原生虚拟化和跨平台任务使 GUI Agent 的环境差异可复验，并直接修正从 Linux benchmark 外推 macOS competence 的结论。 Evaluation：Evaluation Framework.；4.2 Analysis。 Limitations：5 Limitations and Future Work；6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`Only report`；保留为当前窗口上下文，不形成新的长期知识 owner。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [RECAP: Regression Evaluation for Continual Adaptation of Prompts](https://arxiv.org/abs/2606.06698v1)

`arXiv:2606.06698v1`；正文定位：Appendix A Protocol Pseudocode；Appendix H Per-Method Behavioral Profiles。用 proactive adapt-then-test、constraint-level regression/forgetting 定义生产 constraint 更新后的 release gate。 Evaluation：4 Results；Appendix E Per-Backbone Results。 Limitations：5 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [Pomona: Continuous Code Quality Improvement via Small, Agentic Pull Requests at Bloomberg](https://arxiv.org/abs/2606.06752v1)

`arXiv:2606.06752v1`；正文定位：1. Introduction；2. Pomona Overview。工业部署中用扫描 backlog、小 PR、review/merge 证据构成低风险连续 Agent 发布循环。 Evaluation：3. Early Insights and Evaluation；3.1.1. Results。 Limitations：4. Discussion；6. Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-WORKFLOW`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [AdMem: Advanced Memory for Task-solving Agents](https://arxiv.org/abs/2606.06787v1)

`arXiv:2606.06787v1`；正文定位：2.2 Framework。以 actor/memory/critic 分离 semantic/episodic/procedural、短期/长期状态，并定义 merge/prune owner。 Evaluation：正文未设独立 Evaluation 标题；只使用 exact-v1 中可识别的结果/案例。 Limitations：4 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [Declarative Skills for AI Agents in Knowledge-Grounded Tool-Use Workflows](https://arxiv.org/abs/2606.06923v1)

`arXiv:2606.06923v1`；正文定位：9.3 DeclarativeAgent system prompt。在统一 POMDP 中比较 declarative skill 与 imperative state machine，揭示 retrieval quality 对 orchestration 的控制边界。 Evaluation：6 Theoretical Analysis；7 Experimental Results。 Limitations：9 Discussion and Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-WORKFLOW`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [Auditing Training Data in Domain-adapted LLMs: LoRA-MINT](https://arxiv.org/abs/2606.06946v1)

`arXiv:2606.06946v1`；正文定位：III Proposed Method: LoRA-MINT；IV Experimental Framework。用 membership inference 审计 LoRA/domain-adapted model 的训练数据暴露，进入 data provenance contract。 Evaluation：V Experiments and Results。 Limitations：未设独立 Limitations；以 Conclusion 与披露 workload 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`TRAIN-DATA`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [FinEvolveBench: A Benchmark for Self-Evolving Agents on Low-Repetition Tasks with Implicit Rewards](https://arxiv.org/abs/2606.06960v1)

`arXiv:2606.06960v1`；正文定位：4.2 Tree-of-Experience Self-Evolution Framework。将低重复任务、延迟 noisy outcome 与 experience update 对齐，给自演化 Agent 的在线反馈/评测合同及负结果。 Evaluation：正文未设独立 Evaluation 标题；只使用 exact-v1 中可识别的结果/案例。 Limitations：6 Conclusion；7 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [MADE: Beyond Scoring via a Multilingual Agentic Diagnosing Engine for Fine-Grained Evaluation Insights](https://arxiv.org/abs/2606.07020v1)

`arXiv:2606.07020v1`；正文定位：(Meta) MADE turns benchmark landscapes into action maps.。把 8.66M evaluation records 分解为 plan、aggregate、instance、culture 与 grounded report，形成可复用诊断流水线。 Evaluation：Multilingual and multicultural evaluation.；Post-evaluation diagnosis and error analysis.。 Limitations：6 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`Only report`；保留为当前窗口上下文，不形成新的长期知识 owner。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [Beyond Rubrics: Exploration-Guided Evaluation Skills for Reward Modeling](https://arxiv.org/abs/2606.07040v1)

`arXiv:2606.07040v1`；正文定位：2.1 Task Formulation and Online Rubric-Based Reward Modeling；2.3 A Naive Skill-Based Method。将 per-query rubric 改成可演化、可复用并直接注入 judge context 的 evaluation skill state。 Evaluation：4.1 Datasets and Experiment Settings；4.2 Main Experiment Results。 Limitations：5 Analyses and Discussion；7 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [SWE-Explore: Benchmarking How Coding Agents Explore Repositories](https://arxiv.org/abs/2606.07297v1)

`arXiv:2606.07297v1`；正文定位：3 SWE-Explore Benchmark；3.1 Task Formulation。在固定 line budget 下把 repository exploration 分成 coverage、ranking、context efficiency，并与 downstream repair 对齐。 Evaluation：Validation by downstream repair.；4.2 Downstream validation.。 Limitations：5 Conclusion；Discussion.；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`Only report`；保留为当前窗口上下文，不形成新的长期知识 owner。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning](https://arxiv.org/abs/2606.07299v1)

`arXiv:2606.07299v1`；正文定位：2 DuMate-DeepResearch Framework。解耦 Agent Core/Tool Ecosystem、外层规划/内层搜索，并使中间决策和工具调用显式可审计。 Evaluation：3 Experiments and Evaluation；3.2 Detailed Analysis。 Limitations：未设独立 Limitations；以 Conclusion 与披露 workload 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-PLATFORM`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [Certifiable Semantic Agreement Among LLM Agents: What the Admissibility Instrument Decides](https://arxiv.org/abs/2606.07316v1)

`arXiv:2606.07316v1`；正文定位：Approach.；3. System Model and Problem Formulation。用 typed commit/verdict/abort certificate 明确多 Agent 语义共识，并给出 coverage 无优势与 tie-break 漏洞的负结果。 Evaluation：Evaluation.；5. Correctness Analysis。 Limitations：Scope and limitations.；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-MULTI-AGENT`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions](https://arxiv.org/abs/2606.07402v1)

`arXiv:2606.07402v1`；正文定位：2 M 3 Exam : Agent Benchmark；2.1 Task Formulation。将多模态 memory 拆成 grounding、cross-session reasoning 与 index/token cost，并按需读取 raw visual source。 Evaluation：4 Benchmarking Analysis；Evaluation Metrics.。 Limitations：7 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。 完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

### [Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling](https://arxiv.org/abs/2606.07404v1)

`arXiv:2606.07404v1`；正文定位：3 The LightningLM System。120B MoE 单节点训练以 reversible activation、state-preserving growth 与 quantized-expert/adapter optimizer state 形成端到端系统合同。 Evaluation：8.4 The difficulty curriculum, and the role of held-out evaluation。 Limitations：未设独立 Limitations；以 Conclusion 与披露 workload 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。 Books：`已有覆盖`，canonical owner=`TRAIN-PRETRAINING`；Ch28 的 shape-aware parameter mapping → activation-scale preservation → optimizer-state reset/differentiation → asymmetric rewarm → loss-shock canary/rollback 已覆盖；Ch36 只接手并行布局和分布式状态迁移。完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260608/V3_EVIDENCE_RECOVERED.md)。

## 5. 缺口与下一步

无

当前每日厂商源与 arXiv 均已按本窗回放；没有普通 Pending、材料请求或共享 Books 写回。

1. 报告侧 Candidate、Evidence 与 Books proposal 已闭合：48/48，exact-v1 blocker 为 0。
2. Books 无新增正文 proposal：45 项已有覆盖、3 项仅报告；旧 13 项 Integrate 中 10 项 Existing、3 项撤回且采用链已清理。
3. 共享 Books 当前快照的 post-write/trace reconciliation 已完成；旧 trace/post-Review note 不参与授权，所有 Existing 均绑定 Review notes 前的命题级正文。

## 6. 复核

复核者：JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md（非作者 denominator/Books proposal）与本轮 post-write fresh audit
结论：通过

非作者 fresh audit 已纠正 5 个 false positive 与 3 个 false negative，并冻结 498 = 48 Candidate + 450 Close；报告侧 Evidence 48/48、Books Decision 48/48、exact-v1 blocker 0。Books proposal 层确认 10 个旧 Integrate 为已有覆盖、3 条撤销采用链已清理、无新增正文缺口。终审另纠正 2606.06915、2606.06991、2606.07054、2606.06502、2606.07404 的 canonical owner，并逐项确认当前 Review notes 前的精确命题锚点与相邻章节 handoff；45 Existing / 3 Only report / 0 Integrate，Books Gate 通过。
