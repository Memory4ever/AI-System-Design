# Daily Research — 2026-06-10

**规范：** V3
**窗口：** 2026-06-09T09:00:00+08:00 ～ 2026-06-10T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T22:00:00+08:00

## 1. 结论

本窗以 685 个可读 canonical identity 逐题复核。旧 35 项前沿保留 30、关闭 5；旧 650 项 closure 重新执行 title-first 与边界 abstract 复核后恢复 22、维持关闭 628。最终分母为 **52 Candidate / 633 Close**。七个被独立反例审计判定为 false positive 的恢复项是：2606.10106, 2606.10209, 2606.10217, 2606.10660, 2606.10702, 2606.11042, 2606.11070；逐项已转回 family-specific pre-denominator closure。

54 个 Candidate 均已完成 Evidence 与 current Books 对照：49 项为 `No Change — Existing Coverage`，5 项真实长期语义增量已经按 owner 写入 Ch59、Ch66 与 Ch72。MaxProof 改变的是 verifier/reward ownership 的长期机制，而非数学领域内容；当前 `TRAIN-GRPO` 已有精确正文，因此重判 Existing。2606.10794 已以官方 exact-v1 纠正被污染的本地 title/benchmark：正确身份是 *READER: Robust Evidence-based Authorship Decoding via Extracted Representations*，50-target Agent500、500 prompts、25,000 trajectories，单响应 31.0–42.4%、50 响应 70.0–84.0%；旧标题及污染数字不再作为证据。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [厂商源再认证](../_sources/daily-20260601/CURRENT_CONTRACT_DAILY_SOURCE_RECERT_20260914.md#来源结论)：本窗无保留事件 | 已检查 | 无 |
| SRC-ANTHROPIC | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-GOOGLE-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-META-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-QWEN | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-DEEPSEEK | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MOONSHOT | 同上；Kimi Code 0.12.0/0.12.1 的精确 release 时刻落在本窗，见候选与判断 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 同上；“全部”列表本窗无条目 | 已检查 | 无 |
| SRC-ZAI | 同上；Research 列表本窗无条目 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 同上；技术博客本窗无条目 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MINIMAX | 同上；MaxProof 的 JSON-LD 时刻落在本窗，见候选与判断 | 已检查 | 无 |
| SRC-ARXIV | [canonical inventory](../_sources/daily-20260610/canonical-raw-identity-inventory-v2.1.json.gz)、[strict screening ledger](../_sources/daily-20260610/V3_SCREENING_LEDGER.md) 与 [旧 exact-v1 archive](../_sources/daily-20260610/V2_1_EVIDENCE_ARCHIVE.md)；685 identities 已逐题 reconciliation | 已检查 | 无 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.12.0 / 0.12.1](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.12.0) | 2026-06-09T11:56:11+08:00 ～ 2026-06-09T17:04:14+08:00 | 版本级 context/workflow 行为变化；1+2+1=4 | 关闭判断完成 | 已有覆盖：`AGENT-MULTI-AGENT` — [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [MaxProof](https://www.minimax.io/blog/minimax-maxproof-math-proof-evolution) | 2026-06-09T21:43:00+08:00 | proof generator、verifier、repair 与 test-time search 的受限闭环；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-GRPO` — [章节](../../../../books/part-04-training-system/33-grpo.md)；正文锚点「但 verifier 仍是 specification」与「Verifier 也成为 Policy 时，必须分离更新与权威」 |
| [From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents](https://arxiv.org/abs/2606.09863v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | false-success measurement 补充 outcome contract；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点「Agent and Outcome Evaluation」 |
| [Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation](https://arxiv.org/abs/2606.09864v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | KV quantization 的 alignment 风险边界；2+2+2=6 | 标准完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点「从离线平均质量到运行时风险门」 |
| [IntentKV: Cross-Turn Intent-Aware KV Cache Pruning for Agent Inference](https://arxiv.org/abs/2606.09916v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 单一 KV pruning 机制及跨 turn 边界；2+1+2=5 | 标准完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点「跨 Turn Eviction 必须保留 Surviving-row Identity」 |
| [RKSC: Reasoning-Aware KV Cache Sharing and Confident Early Exit for Multi-Step LLM Inference](https://arxiv.org/abs/2606.09937v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 单一 reasoning-serving 组合分支；2+1+2=5 | 标准完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点「Prefix reuse」 |
| [RATrain: A Resource-Aware Training Runtime for Large Language Models on Bandwidth-Constrained Heterogeneous Supercomputing Platforms](https://arxiv.org/abs/2606.10415v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 异构带宽约束下的 training runtime 分支；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING — [章节](../../../../books/part-04-training-system/36-distributed-training.md)；命题锚点「异构设备需要显式的 Resource Model」 |
| [ASTRA-sim 3.0: Next-Level Distributed Machine Learning Simulations via High-Fidelity GPU and Infrastructure Modeling](https://arxiv.org/abs/2606.10440v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | simulator fidelity 的系统/评测边界；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点「Simulator Fidelity：保留真实 Control Plane 仍不足以等同真实硬件」 |
| [SpenseGPT: Practical One-shot Pruning Enabling Sparse and Dense GEMMs for LLM Inference](https://arxiv.org/abs/2606.10445v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 单一 pruning/GEMM operating point；2+1+2=5 | 标准完成 | 已有覆盖：INFER-DECODE — [章节](../../../../books/part-05-inference-system/44-decode.md)；命题锚点「MoE 怎样改变 Decode 的执行形态」 |
| [Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design](https://arxiv.org/abs/2606.10493v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | CPU/GPU hybrid MoE 的 serving 边界；2+2+2=6 | 标准完成 | 已有覆盖：INFER-PD-DISAGGREGATION — [章节](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；命题锚点「局部加速必须通过完整部署账本」 |
| [Prefilling-dLLM: Predictive Prefilling for Long-Context Inference in Diffusion Language Models](https://arxiv.org/abs/2606.10537v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | diffusion LM 的单一 predictive-prefill 分支；2+1+2=5 | 标准完成 | 已有覆盖：INFER-PREFILL — [章节](../../../../books/part-05-inference-system/43-prefill.md)；命题锚点「Prefill 的工作量来自输入长度」 |
| [Unifying Local Communications and Local Updates for LLM Pretraining](https://arxiv.org/abs/2606.11081v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 改变局部通信能否保持全局优化语义的判断；3+2+3=8 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING — [章节](../../../../books/part-04-training-system/36-distributed-training.md)；命题锚点「局部通信与局部更新不能静默改变全局目标」 |
| [TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning](https://arxiv.org/abs/2606.11119v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | rollout budget 的训练/系统联合分配机制；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-GRPO — [章节](../../../../books/part-04-training-system/33-grpo.md)；命题锚点「Rollout Budget 必须由训练收益与系统成本共同拥有」 |
| [OpenPCC: Open and Confidential LLM Serving on Commodity TEEs](https://arxiv.org/abs/2606.11145v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | TEE serving 的实现与信任边界；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点「TEE / Confidential Computing：保护执行环境」 |
| [ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models](https://arxiv.org/abs/2606.11164v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 单一 KV budget allocation 机制；2+1+2=5 | 标准完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点「KV Budget 必须按阶段和层级分配」 |
| [Piper: A Programmable Distributed Training System](https://arxiv.org/abs/2606.11169v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | training dataflow runtime 的状态边显式化；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING — [章节](../../../../books/part-04-training-system/36-distributed-training.md)；命题锚点「Dataflow Runtime 把训练组件与状态边显式化」 |
| [One Lens, Many Worlds : A Capability-Typed Interface for World-Model Interpretability](https://arxiv.org/abs/2606.09936v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 单一 world-model interpretability interface；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS — [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点「World Model 是可检验的状态转移契约」 |
| [Right Family, Wrong Skill: Benchmarking Risk Exposure in Agent Skill Retrieval](https://arxiv.org/abs/2606.10388v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | skill retrieval 的风险/治理边界；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW — [章节](../../../../books/part-07-agent/81-workflow.md)；命题锚点「Reusable Scaffold 与 Fix 也是受治理的 Workflow Artifact」 |
| [STAGE-Claw: Automated State-based Agent Benchmarking for Realistic Scenarios](https://arxiv.org/abs/2606.10394v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | state-based Agent evaluation contract；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点「Agent and Outcome Evaluation」 |
| [Trace2Policy: From Expert Behavior Traces to Self-Evolving Decision Agents](https://arxiv.org/abs/2606.10457v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | trace-to-policy 的归因与 promotion 边界；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW — [章节](../../../../books/part-07-agent/81-workflow.md)；命题锚点「从 Agent Trace 编译 Workflow 需要可归因的数据依赖」 |
| [Learning What to Remember: Observability-Safe Memory Retention via Constrained Optimization for Long-Horizon Language Agents](https://arxiv.org/abs/2606.10616v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | retention objective 与 observability constraint；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md)；命题锚点「Memory Write 是高风险决策」 |
| [Decentralized Multi-Agent Systems with Shared Context](https://arxiv.org/abs/2606.10662v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | shared-context 的版本和访问边界；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT — [章节](../../../../books/part-07-agent/82-multi-agent.md)；命题锚点「共享 Context 需要独立版本与访问边界」 |
| [RedAct: Redacting Agent Capability Traces for Procedural Skill Protection](https://arxiv.org/abs/2606.10813v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 3+2+3=8；exact-v1 identity/claim 与 V2.1 证据一致，按当前三维 schema 复核 | 深入完成 | 已有覆盖：PLATFORM-TRACE — [章节](../../../../books/part-06-ai-infrastructure/69-trace.md)；命题锚点「Trace 需要分离可观测证据与可复用能力」 |
| [Provenance Tracking in AI Compilers through the Lens of Coalgebra](https://arxiv.org/abs/2606.10937v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 3+3+3=9；exact-v1 identity/claim 与 V2.1 证据一致，按当前三维 schema 复核 | 深入完成 | 已有覆盖：PLATFORM-TRACE — [章节](../../../../books/part-06-ai-infrastructure/69-trace.md)；命题锚点「Failure Attribution 必须从阶段定位升级到可证伪的因果候选」 |
| [Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation](https://arxiv.org/abs/2606.11127v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 3+2+3=8；exact-v1 identity/claim 与 V2.1 证据一致，按当前三维 schema 复核 | 深入完成 | 已有覆盖：TRAIN-DATA — [章节](../../../../books/part-04-training-system/27-data.md)；命题锚点「Post-training Data Selection 是当前 Policy 的在线控制环」 |
| [When RL Fails after SFT: Rejuvenating Model Plasticity for Robust SFT-to-RL Handoff](https://arxiv.org/abs/2606.09932v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 3+3+3=9；exact-v1 identity/claim 与 V2.1 证据一致，按当前三维 schema 复核 | 深入完成 | 已有覆盖：TRAIN-RLHF — [章节](../../../../books/part-04-training-system/31-rlhf.md)；命题锚点「SFT-to-RL Handoff 需要 Plasticity Probe」 |
| [GitInject: Real-World Prompt Injection Attacks in AI-Powered CI/CD Pipelines](https://arxiv.org/abs/2606.09935v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 3+3+3=9；exact-v1 identity/claim 与 V2.1 证据一致，按当前三维 schema 复核 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点「CI/CD Agent 的 Repository Content 是不可信输入」 |
| [Stop Early, Spend Less: Hidden-State Probes as a Practical Recipe for Streaming Moderation of LLM Outputs](https://arxiv.org/abs/2606.10487v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 3+2+3=8；exact-v1 identity/claim 与 V2.1 证据一致，按当前三维 schema 复核 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点「Learned Security Sensor 与 Reference Monitor 必须分层」 |
| [Fingerprinting All AI Cluster I/O Without Mutually Trusted Processors](https://arxiv.org/abs/2606.10724v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 3+3+3=9；exact-v1 identity/claim 与 V2.1 证据一致，按当前三维 schema 复核 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文「Cluster I/O 证明需要把观察、承诺与通道治理分开」 |
| [MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents](https://arxiv.org/abs/2606.10742v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 3+2+3=8；exact-v1 identity/claim 与 V2.1 证据一致，按当前三维 schema 复核 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md)；命题锚点「Memory 安全」 |
| [Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models](https://arxiv.org/abs/2606.10949v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 3+2+3=8；exact-v1 identity/claim 与 V2.1 证据一致，按当前三维 schema 复核 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md)；命题锚点「Recall、Use 与 Overuse 必须分开测量」 |
| [CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs](https://arxiv.org/abs/2606.11063v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 2+2+3=7；exact-v1 identity/claim 与 V2.1 证据一致，按当前三维 schema 复核 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点「Control Evaluation 要测试 Attacker 如何选择攻击时机」 |
| [Operator Fusion for LLM Inference on the Tensix Architecture](https://arxiv.org/abs/2606.09879v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | operator fusion 把多个算子边界编译为一个执行计划；3+3+2=8 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM — [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；命题锚点「Execution Plan 的等价性与 Safe Commit」 |
| [WebChallenger: A Reliable and Efficient Generalist Web Agent](https://arxiv.org/abs/2606.10423v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | web agent 把页面观察、动作结果与 finish gate 组成可恢复执行合同；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING — [章节](../../../../books/part-07-agent/78-tool-calling.md)；命题锚点「Tool 完成必须由 Program State 与 Effect State 验证」 |
| [Streaming Knowledge Compilation: Proactive Materiality-Scored Pinning for Time-Evolving LLM Wikis](https://arxiv.org/abs/2606.09877v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 未知未来 query 下以 materiality proposal 管理编译知识的驻留与回收；3+2+3=8 | 深入完成 | 已有覆盖：INFER-KV-CACHE — [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点「Future Reuse Intent 需要变成可验证的 Resident Claim」 |
| [Less Context, More Accuracy: A Bi-Temporal Memory Engine for LLM Agents Where a Lean Retrieved Context Beats the Full History](https://arxiv.org/abs/2606.09900v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | bitemporal memory 分离事实有效时间、写入时间与查询可见快照；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md)；命题锚点「Bitemporal Memory 把有效时间与写入时间分开」 |
| [ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning](https://arxiv.org/abs/2606.10532v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | distributed active memory 显式化并行写入、聚合与读取版本；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md)；命题锚点「并行经验汇总需要 Bounded Fan-in 与 Context Version」 |
| [SkillAxe: Sharpening LLM-Authored Agent Skills Through Evaluation-Guided Self-Refinement](https://arxiv.org/abs/2606.10546v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | skill refinement 将生成、试验、独立验证与 promotion 分离；2+2+3=7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW — [章节](../../../../books/part-07-agent/81-workflow.md)；命题锚点「Trial Evidence 不能直接提交为 Workflow Revision」 |
| [Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory](https://arxiv.org/abs/2606.10677v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | topic document 把 lossless source 与可维护派生视图分层；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md)；命题锚点「Memory 粒度必须分层，不能用一个 Summary 同时承担证据与画像」 |
| [REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs](https://arxiv.org/abs/2606.10694v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | reasoning-enhanced graph memory 要让 relation、来源、有效期和 supersession 同步演进；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md)；命题锚点「Graph Memory 的 Relation 也需要 Provenance」 |
| [The Arbiter Agent: Continually Monitoring Multi-Agent Conversations to Detect Emergent Misalignment](https://arxiv.org/abs/2606.10747v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | arbiter 以持续观测和有界 intervention 监控 multi-agent 偏移；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点「Judge 从被动 Scorer 演进为有预算的 Evidence Acquisition Policy」 |
| [READER: Robust Evidence-based Authorship Decoding via Extracted Representations](https://arxiv.org/abs/2606.10794v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 动态黑盒 provenance 以 frozen proxy representation 与多 query 贝叶斯证据累积识别候选来源；3+2+3=8 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY — [章节](../../../../books/part-06-ai-infrastructure/59-model-registry.md)；正文「从固定 Challenge 到 Query-varying 流量：黑盒身份只能逐步累积证据」 |
| [CollabSkill: Evaluating Human-Agent Collaboration On Real-World Tasks](https://arxiv.org/abs/2606.09833v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 真实 human-agent 协作把参与者、agent、任务与 outcome 绑定到同一 attribution model；3+2+3=8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文「Human–Agent Team 必须成为独立 Evaluation Object」 |
| [FailureScope: Cross-Regime Behavioral Diagnosis of Language Model Weaknesses](https://arxiv.org/abs/2606.09878v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | cross-regime taxonomy 暴露总体均值掩盖的 failure family；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点「从“已见切片均值”到 Blind-spot Mass」 |
| [PreAct-Bench: Benchmarking Predictive Monitoring in LLMs](https://arxiv.org/abs/2606.09890v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | predictive monitoring 需要在 action 前评价预警与误报，而非只看最终结果；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点「Proactive Agent 必须同时测 Act、Silent 与 Stop」 |
| [IDP-Bench: Benchmarking ability of LLMs to protect personal information in interdependent privacy contexts](https://arxiv.org/abs/2606.09908v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 隐私对象从单一 data owner 扩展为多 subject、recipient 与 transmission principle；3+3+3=9 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文「Privacy Gate 必须同时识别 Recipient 与所有 Data Subjects」 |
| [Quality Is Not a Safety Proxy Under Quantization](https://arxiv.org/abs/2606.10154v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 量化发布不能用平均质量代理安全回归；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点「Quantization 是新的 Security Revision」 |
| [Catching One in Five: LLM-as-Judge Blind Spots in Production Multi-Turn Transaction Agents](https://arxiv.org/abs/2606.10315v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 生产多轮 transaction 暴露 judge 对真实 effect 的系统性 blind spot；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点「Trajectory Judge 必须区分叙述、动作与完成证据」 |
| [AgentCanary: A Security Evaluation Framework for Autonomous AI Agents in Real Executable Environments](https://arxiv.org/abs/2606.10484v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | Agent 安全评估必须运行真实可执行环境并以 side effect/outcome 判定；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点「Agent authority BOM、channel coverage 与 executable PoV」 |
| [Assessing Automated Prompt Injection Attacks in Agentic Environments](https://arxiv.org/abs/2606.10525v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 自动 prompt injection campaign 暴露跨 task/OOD/model 的 transfer boundary；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点「Control Evaluation 要测试 Attacker 如何选择攻击时机」 |
| [When the Defense Writes the Refusal: Auditing Keyword-Scored Evaluation of Inference-Time Defenses for Multimodal Large Language Models](https://arxiv.org/abs/2606.10904v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | keyword scorer 与拒答文本可把防御输出误计为安全成功；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点「Judge 先证明看见了目标变化，再谈总体准确率」 |
| [VISTA: A Versatile Interactive User Simulation Toolkit for Agent Evaluation](https://arxiv.org/abs/2606.11079v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | user simulator 需要以隐藏约束与 consequential outcome 校准；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM — [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点「Simulator Fidelity：保留真实 Control Plane 仍不足以等同真实硬件」 |
| [The Interlocutor Effect: Why LLMs Leak More Personal Data to Agents Than Humans](https://arxiv.org/abs/2606.09844v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 同一敏感内容对 agent recipient 的泄漏差异使 recipient identity 成为 security context；3+2+3=8 | 深入完成 | 整合：PLATFORM-SECURITY — [章节](../../../../books/part-06-ai-infrastructure/72-security.md)；正文「Privacy Gate 必须同时识别 Recipient 与所有 Data Subjects」 |
| [Deployment-Time Memorization in Foundation-Model Agents](https://arxiv.org/abs/2606.10062v1) | 2026-06-10T08:00:00+08:00 ～ 2026-06-10T09:00:00+08:00 | 部署期写入会形成参数外 memorization，删除必须沿 memory lineage 传播；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MEMORY — [章节](../../../../books/part-07-agent/77-memory.md)；命题锚点「Bitemporal Memory 把有效时间与写入时间分开」 |

候选分母冻结为 54：52 个 arXiv Candidate 加 2 个厂商 Source Family。30 个 surviving prior 复用 identity/claim 未变化的 V2.1 exact-v1 Review，但 Books disposition 已按 current body 重判；22 个恢复项与 2 个厂商候选的本轮审阅如下。

## 4. 证据与知识整合

### [Kimi Code 0.12.0 / 0.12.1](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.12.0)

官方 GitHub Release 的 `published_at` 分别为 `2026-06-09T03:56:11Z` 与 `2026-06-09T09:04:14Z`。0.12.0 默认启用 micro-compaction、goal/background/sub-skill，并增加 `/swarm`；0.12.1 是同一 Source Family 的紧随修补。它证明公开版本中的控制接口，不证明多 Agent 的正确性、扩展性、恢复语义或生产 SLO。`AGENT-MULTI-AGENT`、`AGENT-CONTEXT` 与 `AGENT-WORKFLOW` 已覆盖 bounded fan-out、context compaction、delegation budget、join/timeout 与失败边界，故维持 Existing。

### [MaxProof](https://www.minimax.io/blog/minimax-maxproof-math-proof-evolution)

官方 Blog 的 JSON-LD 把发布时间固定为 `2026-06-09T13:43:00Z`。公开机制把 proof generator、外部 generative verifier reward、错误定位/修复 expert 与 evolutionary test-time search 连接为闭环：verifier 同时影响训练 reward 与推理时 proposal selection，因此其版本、校准、假阳性和 reward hacking 会跨越训练—推理边界传播。公开证据绑定数学证明 workload 与厂商披露的模型/评测，不能外推到通用 RL、任意 verifier 或生产 agent；页面没有给出足以复现全部训练和搜索结果的不可变 artifact。本项不是 AI-for-Science 领域任务本身的吸收，而是对 reward/verifier authority 的长期机制证据。当前 `TRAIN-GRPO` 已在「Verifiable Reward 的优势与边界」明确 verifier 仍是 specification，要求 held-out tests、adversarial cases 与独立人工检查；又在「Verifier 也成为 Policy 时，必须分离更新与权威」区分 proposal/update 与 oracle authority，并说明 collusion、共同偏差、reward hacking、固定 hidden tests 和人工 fallback。MaxProof 提供了该机制在证明生成/修复闭环中的实例，但没有改变现有命题或共存边界，故为 `No Change — Existing Coverage`。

### [From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents](https://arxiv.org/abs/2606.09863v1)

Agent 自称完成或 LLM judge 看语气，无法确认外部状态真的改变。该研究用 tau2-bench/AppWorld 的 text-independent ground truth 标记 false success，再比较五类 judge/prompt 与轻量 TF-IDF detector。 11,755 条 trajectory 支持 confident closing/action volume 会误导 judge，且 task-disjoint 轻量 detector 更适合 triage；AUROC 仍不是 correctness，domain detector 需要重校准。最终权威必须是 environment verifier，语言 detector 只分流。
Deep evidence contract：Method/identity=`arXiv:2606.09863v1 exact-v1 HTML § `3 Methods``；Evaluation=`arXiv:2606.09863v1 exact-v1 HTML § `4 Results``；Limitations/counterevidence=`arXiv:2606.09863v1 exact-v1 HTML § `5 Limitations``；Artifact=`arXiv:2606.09863v1 exact-v1 HTML § `Reproducibility.`; no immutable commit inferred beyond the manuscript`。Owner/authority：`From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents` 的长期机制归入 `PLATFORM-EVALUATION-SYSTEM`；benchmark denominator、subject version、environment、evaluator 与 decision boundary 必须同时冻结；ground truth/verifier 负责裁定，judge 或 probe 只提供受限证据。

### [Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation](https://arxiv.org/abs/2606.09864v1)

KV quantization 通常只以 perplexity、task accuracy 与 memory 验收，但 refusal behavior 依赖低维 activation subspace，可能在这些 aggregate metric 几乎不变时发生 model-specific phase transition。论文用 ConditionalFlip、layer scan、per-channel reduction 与 layer spread 诊断 mitigation；证据覆盖 11 个 3.8B–72B 模型、五个 safety benchmarks 和生产 vLLM FP8 case，但仍受 refusal evaluator、prompt set、量化器与 post-training family 约束。结论是压缩 artifact 必须重新做行为/安全 release evaluation，而不是存在统一 safe bit-width。 证据边界绑定 exact-v1 与上述 workload；不得把作者结果外推成跨模型/跨部署普遍结论。

### [IntentKV: Cross-Turn Intent-Aware KV Cache Pruning for Agent Inference](https://arxiv.org/abs/2606.09916v1)

IntentKV: Cross-Turn Intent-Aware KV Cache Pruning for Agent Inference 处理的问题是：Cross-turn QueryMemory controls live-token retention while slot-map redirection preserves surviving rows, RoPE phase, and prefix-cache identity during eviction.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 IntentKV; session QueryMemory, residual scorer and slot-map sentinel redirection`。状态 owner 为 `INFER-KV-CACHE`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `§4 Experiments; §4.1 BCP setup and longest-query stress slice` 提供可复核结果。

评估证明边界：workload=`BCP agent benchmark plus the 100 longest commonly completed Qwen2.5-14B queries`；model=`Qwen3-8B and Qwen2.5-14B`；evaluator=`Task accuracy, peak request tokens, worst-case raw KV reads and full-cache fidelity`。它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `§ Limitations (exact heading); learned pruning keeps base LLM fixed but does not prove universal task preservation`。

取舍、failure、共存与演进：QueryMemory scoring adds session state and can irreversibly drop evidence when intent changes; sentinel redirection preserves physical identity but not information already evicted. Full cache remains the correctness fallback, while budgeted pruning is justified only by the BCP fidelity and read-volume evidence reported for the two Qwen models. Artifact 边界：`Not Disclosed — no immutable event-time artifact revision identified`。

### [RKSC: Reasoning-Aware KV Cache Sharing and Confident Early Exit for Multi-Step LLM Inference](https://arxiv.org/abs/2606.09937v1)

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：RKSC 在 multi-branch reasoning 中用 hidden-state similarity 决定 prefix KV sharing，并以 confidence early exit 管理共享错误与冗余 decode。 exact-v1 摘要将具体问题界定为：We introduce RKSC (Reasoning-Aware KV Cache Sharing), a training-free inference framework that eliminates two structural redundancies in multi-branch LLM reasoning pipelines. ASKS (Attention-Similarity KV Sharing) computes the prefix KV cache once and broadcasts it to all semantically similar branches via hidden-state cosine similarity, strictly generalising the token-exact prefix caching used by vLLM and SGLang. CGEE (Confidence-Gated Early Exit) applies two complementary exit mechanisms: (1) it skips the verifica

**State / data / control owner。** `INFER-KV-CACHE` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“RKSC 在 multi-branch reasoning 中用 hidden-state similarity 决定 prefix KV sharing，并以 confidence early exit 管理共享错误与冗余 decode。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.09937v1 §3 Experimentation and Results; §3.1 setup; §§3.2–3.4` 实际支持的合同是 `Disclosed — GPQA Diamond, MMLU-STEM, ARC-Challenge and GSM8K with held-out calibration and timing repeats`，evaluator 是 `Disclosed — latency decomposition, accuracy agreement, skip/reuse rates, threshold sensitivity and 42 A100-GPU-hour budget`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.09937v1 §2 RKSC Pipeline; §§2.1–2.4 ASKS/CGEE/RSBCM`；counterevidence locator: `arXiv:2606.09937v1 §4 Analysis/Ablations; §5 Limitations; Appendices C–G sensitivity/failures`。

**Trade-off / failure / coexistence / evolution。** KV sharing 与 early exit 降低多分支重复计算，却依赖 similarity/calibration 且当前是单 GPU、固定八分支；token-exact prefix cache 仍是保守路径，异构请求会增加误共享风险。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

**Claim boundary。** 可引用内容限于 `arXiv:2606.09937v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。

### [RATrain: A Resource-Aware Training Runtime for Large Language Models on Bandwidth-Constrained Heterogeneous Supercomputing Platforms](https://arxiv.org/abs/2606.10415v1)

`LifeTrain: Training-State Lifecycle Scheduling for Large Language Model Training on Bandwidth-Constrained Heterogeneous Supercomputers` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10415v1`：Production heterogeneous supercomputing platforms are increasingly used to host large language model (LLM) training workloads.

机制与 owner：Schedule gradient sync, update, parameter-view prefetch and activation recovery as a layer- and stage-local training-state lifecycle under explicit DDR and link constraints. 状态/数据/控制 owner 固定为 `TRAIN-DISTRIBUTED-TRAINING`；Method 锚点是 `§4 Design`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§6 Evaluation` 只证明 `Production heterogeneous supercomputing platforms are increasingly used to host large language model (LLM) training workloads.` 上、`LLaMA-2-7B, Baichuan2-13B, Qwen2.5-32B, and LLaMA-2-70B configurations` 条件下的报告指标。hardware=`MT-3000 heterogeneous supercomputer; usable DDR 20GB per compute cluster`；precision=`FP16 kernels disclosed; other state precision is configuration-specific`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：The planner is tied to MT-3000's hierarchy and non-interleaved 1F1B; GPU runtimes remain the better branch when HBM and collectives are abundant. 反证/外推边界在 `§2.3 GPU-oriented limitations and §8 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [ASTRA-sim 3.0: Next-Level Distributed Machine Learning Simulations via High-Fidelity GPU and Infrastructure Modeling](https://arxiv.org/abs/2606.10440v1)

`ASTRA-sim 3.0: Next-Level Distributed Machine Learning Simulations via High-Fidelity GPU and Infrastructure Modeling` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10440v1`：Distributed machine learning (ML) is a key paradigm for today's large-scale artificial intelligence applications.

机制与 owner：Raise distributed-ML simulation from coarse events to cache-line load/store GPU execution and a backend-neutral InfraGraph for reusable infrastructure identity. 状态/数据/控制 owner 固定为 `PLATFORM-EVALUATION-SYSTEM`；Method 锚点是 `§4 ASTRA-sim 3.0`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Case Studies` 只证明 `Distributed machine learning (ML) is a key paradigm for today's large-scale artificial intelligence applications.` 上、`No single LM checkpoint: ASTRA-sim case studies evaluate GPU, collective, and infrastructure configurations` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Higher fidelity increases simulation cost and still inherits model error; a simulated timing result is not a measured production SLO. 反证/外推边界在 `§3 Motivation and §7 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [SpenseGPT: Practical One-shot Pruning Enabling Sparse and Dense GEMMs for LLM Inference](https://arxiv.org/abs/2606.10445v1)

`SpenseGPT: Practical One-shot Pruning Enabling Sparse and Dense GEMMs for LLM Inference` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10445v1`：Semi-structured 2:4 sparsity is widely supported by modern accelerators, providing up to a 2x theoretical speedup.

机制与 owner：Split each weight matrix into a contiguous dense region plus hardware-native 2:4 sparse region so existing dense and sparse GEMM libraries can execute one-shot-pruned LLMs. 状态/数据/控制 owner 固定为 `INFER-DECODE`；Method 锚点是 `§3 Proposed Method`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Experiments` 只证明 `Semi-structured 2:4 sparsity is widely supported by modern accelerators, providing up to a 2x theoretical speedup.` 上、`Qwen3-32B; Seed-OSS-36B` 条件下的报告指标。hardware=`NVIDIA B200`；precision=`FP8 inference with hybrid dense/2:4 sparse weights`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Dense-index choice is load-bearing and small GEMMs may not amortize sparse-kernel overhead; the B200 FP8 results do not imply cross-hardware speedup. 反证/外推边界在 `§3.1.3 existing-method failures and §5 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design](https://arxiv.org/abs/2606.10493v1)

`Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10493v1`：Local deployment of large Mixture-of-Experts (MoE) models falls short of the service quality achieved in cloud-scale environments, even under low-concurrency workloads.

机制与 owner：Co-design stream-loaded prefill, small expert parallelism, zero-copy intra-node PD separation, dual-batch overlap and CPU FP8 GEMV for intact local MoE serving. 状态/数据/控制 owner 固定为 `INFER-PD-DISAGGREGATION`；Method 锚点是 `§3 System Design`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Evaluations` 只证明 `Local deployment of large Mixture-of-Experts (MoE) models falls short of the service quality achieved in cloud-scale environments, even under low-concurrency workloads.` 上、`DeepSeek-V3/R1 family, intact FP8 and INT4 configurations` 条件下的报告指标。hardware=`Dual-socket CPUs with 1–2 RTX 5090 consumer GPUs; AVX-512 CPU path`；precision=`FP8 and INT4 are separate evaluated branches`；batch=`Not Disclosed`；concurrency=`Mixed prefill/decode and dual-batch decode are measured; production arrival process not disclosed`；SLO=`30s TTFT and >20 tok/s are author-selected cloud-reference goals, not verified production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：The 30-second TTFT and 20-token/s values are paper reference goals, not independently validated production SLOs; benefits depend on dual-socket DDR, AVX-512 and RTX 5090-class hardware. 反证/外推边界在 `§6 Discussion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Prefilling-dLLM: Predictive Prefilling for Long-Context Inference in Diffusion Language Models](https://arxiv.org/abs/2606.10537v1)

`Prefilling-dLLM: Predictive Prefilling for Long-Context Inference in Diffusion Language Models` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10537v1`：Diffusion large language models (dLLMs) re-encode the entire prefix at every denoising step, causing recomputation that scales quadratically with context length and becomes prohibitive for long-context scenarios.

机制与 owner：Prefill long dLLM prefixes once into chunked KV, retrieve only relevant chunks/tokens during iterative denoising, and use periodic BOS anchors to preserve middle evidence. 状态/数据/控制 owner 固定为 `INFER-PREFILL`；Method 锚点是 `§5 Method`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§6 Experiments` 只证明 `Diffusion large language models (dLLMs) re-encode the entire prefix at every denoising step, causing recomputation that scales quadratically with context length and becomes prohibitive for long-context scenarios.` 上、`Dream-v0-Base-7B and UltraLLaDA configurations` 条件下的报告指标。hardware=`Exact-v1 evaluation hardware is experiment-specific; no fleet topology`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Sparse chunk selection can discard needed evidence and cached non-contiguous KV consumes memory; the 8K–32K kernel speedups are bounded to tested dLLMs and contexts. 反证/外推边界在 `§7 Conclusion and Appendix ablations`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Unifying Local Communications and Local Updates for LLM Pretraining](https://arxiv.org/abs/2606.11081v1)

`Unifying Local Communications and Local Updates for LLM Pretraining` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11081v1`：Communication-efficient pre-training of LLMs is increasingly important as training draws on compute distributed across clusters, data centers, and lower-bandwidth links.

机制与 owner：Combine adaptive local optimizer steps with sparse randomized gossip so LLM pretraining can progress without globally identical state or synchronous all-reduce. 状态/数据/控制 owner 固定为 `TRAIN-DISTRIBUTED-TRAINING`；Method 锚点是 `§3 Method`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Numerical Experiments` 只证明 `Communication-efficient pre-training of LLMs is increasingly important as training draws on compute distributed across clusters, data centers, and lower-bandwidth links.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Model replicas diverge and topology/bandwidth heterogeneity changes convergence; synchronous collectives remain the conservative branch on reliable fabrics. 反证/外推边界在 `§5 Conclusion and Appendices B/F`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning](https://arxiv.org/abs/2606.11119v1)

`TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11119v1`：Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in large language models.

机制与 owner：Allocate a fixed rollout budget jointly to prompt roots and informative intermediate ReAct prefixes, turning multi-turn exploration into a reward-contrast tree. 状态/数据/控制 owner 固定为 `TRAIN-GRPO`；Method 锚点是 `§§3–4 allocation principle and TRACE`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Experiments` 只证明 `Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in large language models.` 上、`Qwen3-8B and Qwen3-14B; Llama-3.2-3B-Instruct in additional Multi-Hop QA experiments` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Prefix continuation adds tree state and selection bias; outcome-only terminal reward still limits credit assignment when all branches share the same result. 反证/外推边界在 `Appendix B Discussion and C Extended Results`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [OpenPCC: Open and Confidential LLM Serving on Commodity TEEs](https://arxiv.org/abs/2606.11145v1)

`OpenPCC: Open and Confidential LLM Serving on Commodity TEEs` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11145v1`：Generative AI applications such as personal AI agents, image generators, and chat assistants offer advanced capabilities to improve user experience.

机制与 owner：Build an open confidential inference service on commodity TEEs with remote attestation and a public trust chain instead of proprietary cloud hardware. 状态/数据/控制 owner 固定为 `PLATFORM-SECURITY`；Method 锚点是 `§§3–5 OpenPcc design and implementation`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§6 Evaluation` 只证明 `Generative AI applications such as personal AI agents, image generators, and chat assistants offer advanced capabilities to improve user experience.` 上、`Llama-3 8B vLLM end-to-end workload` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：TEE side channels, availability and accelerator boundary remain platform-specific; confidentiality evidence does not prove model correctness or operator-free governance. 反证/外推边界在 `§7 Security Analysis and §9 Future Works`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models](https://arxiv.org/abs/2606.11164v1)

`ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11164v1`：Long chain-of-thought (CoT) trajectories in large language model (LLM) reasoning cause severe inference bottlenecks due to rapid key-value (KV) cache growth.

机制与 owner：Allocate reasoning-model decode KV hierarchically: offline per-layer demand followed by online head-level reallocation from current utility. 状态/数据/控制 owner 固定为 `INFER-KV-CACHE`；Method 锚点是 `§5 ReasonAlloc Framework`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§§6–8 experiments, efficiency, and ablations` 只证明 `Long chain-of-thought (CoT) trajectories in large language model (LLM) reasoning cause severe inference bottlenecks due to rapid key-value (KV) cache growth.` 上、`DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, AceReason-14B` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Eviction utility is workload-dependent and compression can erase late-used evidence; uniform budgets remain predictable when online signals are unstable. 反证/外推边界在 `§6.2 static-heuristic limits, §7 efficiency, and §9 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Piper: A Programmable Distributed Training System](https://arxiv.org/abs/2606.11169v1)

`Piper: A Programmable Distributed Training System` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11169v1`：Large-scale model training increasingly relies on composing multiple parallelism strategies, such as data, pipeline, and expert parallelism, together with memory-saving optimizations like ZeRO.

机制与 owner：Compile model annotations and scheduling directives into a global computation/communication DAG, then derive per-device plans independent of the chosen parallelism strategy. 状态/数据/控制 owner 固定为 `TRAIN-DISTRIBUTED-TRAINING`；Method 锚点是 `§4 Design`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§6 Evaluation` 只证明 `Large-scale model training increasingly relies on composing multiple parallelism strategies, such as data, pipeline, and expert parallelism, together with memory-saving optimizations like ZeRO.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：A programmable IR moves complexity into transformations and validation; specialized runtimes remain simpler for fixed strategies and unsupported optimizations. 反证/外推边界在 `§3 Challenges and §8 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [One Lens, Many Worlds : A Capability-Typed Interface for World-Model Interpretability](https://arxiv.org/abs/2606.09936v1)

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：不同 world-model substrate 只能通过 capability-typed interface 比较 observability 与 intervention，不能假设 latent、token 与 joint-embedding state 同构。 exact-v1 摘要将具体问题界定为：World models are now built on substantially different computational substrates. Latent recurrent state-space models such as PlaNet and the Dreamer family compress observations into recurrent states; token-based models such as IRIS quantize observations into a learned codebook and predict autoregressively with a transformer; and joint-embedding predictive architectures such as I-JEPA predict in a learned latent space with no pixel decoder. The interpretability methods applied to these models, including probing, acti

**State / data / control owner。** `MULTIMODAL-WORLD-MODELS` 负责机制所需的数据、状态、控制与证据元数据；在本 source 中，需被显式持有、传递或阻断的状态正是“不同 world-model substrate 只能通过 capability-typed interface 比较 observability 与 intervention，不能假设 latent、token 与 joint-embedding state 同构。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.09936v1 §4 reusable analyses; §5 Evaluation; §§5.1–5.3` 实际支持的合同是 `Disclosed — exact-v1 evaluation workload is bound at the evaluation locator; abstract evidence: every model implements four required methods (encode, transition, initial state, sample) and declares a set of optional heads (decode, reward, continue, actor, critic) through an explicit capability descriptor, so that reinforcement-learning and self-supervised world models are first-class without either imitating the other. A single hook and cache layer exposes time-indexed activations, imagination rollouts, and int`，evaluator 是 `Disclosed — exact-v1 paper-defined metrics and comparisons at the evaluation locator; claim remains paper-scope, not universal superiority`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.09936v1 §3 WorldModelLens abstraction; §§3.1–3.3 capability adapters/hooks/replay`；counterevidence locator: `arXiv:2606.09936v1 §7 Limitations and Roadmap; heterogeneous-substrate capability boundary`。

**Trade-off / failure / coexistence / evolution。** capability-typed adapter 复用分析却只统一接口而不统一 state semantics；substrate-specific hooks 仍需共存，错误宣告 capability 会让跨模型比较失真。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

**Claim boundary。** 可引用内容限于 `arXiv:2606.09936v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。

### [Right Family, Wrong Skill: Benchmarking Risk Exposure in Agent Skill Retrieval](https://arxiv.org/abs/2606.10388v1)

`SkillResolve-Bench: Measuring and Resolving Same-Capability Ambiguity in Agent Skill Retrieval` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10388v1`：Agent skill libraries are routable software assets.

机制与 owner：Resolve the active capability family, learn query-conditioned utility from confusable skills, and expose one representative before global top-k skill ranking. 状态/数据/控制 owner 固定为 `AGENT-WORKFLOW`；Method 锚点是 `§3 Problem and Method`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Experiments` 只证明 `Agent skill libraries are routable software assets.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Family-resolution errors can hide the helpful skill or split risky siblings; the v1 benchmark proves retrieval exposure on a fixed library, not runtime safety after a skill executes. 反证/外推边界在 `§5 Analysis and Execution Scope`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [STAGE-Claw: Automated State-based Agent Benchmarking for Realistic Scenarios](https://arxiv.org/abs/2606.10394v1)

`STAGE-Claw: Automated State-based Agent Benchmarking for Realistic Scenarios` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10394v1`：Large language models are increasingly used to power personal agents for everyday applications, but evaluating these agents remains a challenge.

机制与 owner：Generate realistic personal-computing tasks together with initial state, ground truth and executable final-state verifiers, so agent evaluation is owned by environment state rather than answer text. 状态/数据/控制 owner 固定为 `PLATFORM-EVALUATION-SYSTEM`；Method 锚点是 `§2 STAGE-Claw`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§3 Evaluation` 只证明 `Large language models are increasingly used to power personal agents for everyday applications, but evaluating these agents remains a challenge.` 上、`Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3.5-Plus, GPT-5.5, GPT-5.4, Gemini-3.1-pro-preview, Doubao-Seed-2.0-Pro, GLM-5, Kimi-K2.6, MiniMax-M2.7` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Automatically generated scenarios can encode validator blind spots; forty tasks and eleven models establish a benchmark slice, not production reliability. 反证/外推边界在 `§4 Analysis and Appendix A audit`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Trace2Policy: From Expert Behavior Traces to Self-Evolving Decision Agents](https://arxiv.org/abs/2606.10457v1)

`Trace2Policy: From Expert Behavior Traces to Self-Evolving Decision Agents` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10457v1`：Decision rules that enterprise experts apply tacitly -- in auditing, compliance, and contract review -- can be systematically recovered and improved through iterative error analysis.

机制与 owner：Maintain a human-readable decision rule as versioned state; cluster validation errors into missing, wrong or conflicting rules and commit only regression-passing patches. 状态/数据/控制 owner 固定为 `AGENT-WORKFLOW`；Method 锚点是 `§3 Trace2Policy Framework`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§§4–6 production, experiments, and transfer` 只证明 `Decision rules that enterprise experts apply tacitly -- in auditing, compliance, and contract review -- can be systematically recovered and improved through iterative error analysis.` 上、`GLM-5, Kimi-K2.5, Qwen3.5-plus, MiniMax-M2.5, Claude Opus 4.6, Claude Haiku 4.5` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Compiled rules improve determinism but narrow coverage to expressible policy; an LLM prompt remains useful where cases cannot be compiled or verified. 反证/外推边界在 `Appendix B Limitations and Broader Impacts`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Learning What to Remember: Observability-Safe Memory Retention via Constrained Optimization for Long-Horizon Language Agents](https://arxiv.org/abs/2606.10616v1)

`Learning What to Remember: Observability-Safe Memory Retention via Constrained Optimization for Long-Horizon Language Agents` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10616v1`：Long-horizon language agents accumulate observations, reasoning traces, and retrieved facts exceeding context windows, making memory retention a fundamental resource-allocation problem.

机制与 owner：Separate online-observable retention features from offline supervision and optimize memory under budget, evidence utility, miss, reacquisition and stale costs. 状态/数据/控制 owner 固定为 `AGENT-MEMORY`；Method 锚点是 `§3 Method`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Experiments` 只证明 `Long-horizon language agents accumulate observations, reasoning traces, and retrieved facts exceeding context windows, making memory retention a fundamental resource-allocation problem.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：The learned retention policy depends on realized-query distribution and can still discard future evidence; simple recency or full retention remains safer when observability assumptions fail. 反证/外推边界在 `§5 Conclusion and Discussion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Decentralized Multi-Agent Systems with Shared Context](https://arxiv.org/abs/2606.10662v1)

`Decentralized Multi-Agent Systems with Shared Context` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10662v1`：Multi-agent systems (MAS) can scale large language model reasoning at test time by decomposing complex problems into parallel subtasks.

机制与 owner：Replace a central merger with asynchronously claimed subtasks, a shared verified context and compact write-back records. 状态/数据/控制 owner 固定为 `AGENT-MULTI-AGENT`；Method 锚点是 `§3 Decentralized Language Models`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Experiments` 只证明 `Multi-agent systems (MAS) can scale large language model reasoning at test time by decomposing complex problems into parallel subtasks.` 上、`Gemini 3 Flash and Claude Opus 4.6 base models` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Shared-context verification becomes a contention and trust boundary; centralized orchestration remains simpler for small task graphs or unverifiable partial work. 反证/外推边界在 `§7 Limitations and Future Work`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [RedAct: Redacting Agent Capability Traces for Procedural Skill Protection](https://arxiv.org/abs/2606.10813v1)

`RedAct: Redacting Agent Capability Traces for Procedural Skill Protection` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10813v1`：Users rely on execution traces to observe agent behavior, diagnose failures, and ensure accountability.

机制与 owner：Release agent traces through selective protected-information rewriting while preserving verifier-critical evidence and adding behavioral provenance watermarks. 状态/数据/控制 owner 固定为 `PLATFORM-TRACE`；Method 锚点是 `§§3–4 CapTraceBench and Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Experiments` 只证明 `Users rely on execution traces to observe agent behavior, diagnose failures, and ensure accountability.` 上、`Claude Opus 4.6, Sonnet 4.6, Haiku 4.5, GPT-5.2 Codex, Gemini 3 Flash/Pro; Qwen3-8B/4B for open-model studies` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Redaction can remove diagnostic detail and watermarks are probabilistic; private full traces and least-privilege access remain necessary for incident response. 反证/外推边界在 `§5.4 Diagnostics/Robustness and §7 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Provenance Tracking in AI Compilers through the Lens of Coalgebra](https://arxiv.org/abs/2606.10937v1)

`Provenance Tracking in AI Compilers through the Lens of Coalgebra` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10937v1`：AI compilers aggressively rewrite computation graphs through normalization, lowering, and optimization, making it difficult to track the provenance of tensors and operators across compilation.

机制与 owner：Observe compiler graph transformations and reconstruct tensor/operator provenance through coalgebraic behavior rather than propagating fragile IDs through non-injective rewrites. 状态/数据/控制 owner 固定为 `PLATFORM-TRACE`；Method 锚点是 `§§3–4 observational correctness and Covan`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Evaluation` 只证明 `AI compilers aggressively rewrite computation graphs through normalization, lowering, and optimization, making it difficult to track the provenance of tensors and operators across compilation.` 上、`Modified MNIST and MobileNetV2-0.25 compiler benchmarks; proprietary models omitted` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Observational equivalence can merge distinctions needed by a debugger and the COVAN prototype is not evidence for every compiler pass; explicit IDs remain useful where rewrites preserve them. 反证/外推边界在 `§3.1 provenance limitation and §7 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation](https://arxiv.org/abs/2606.11127v1)

`Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11127v1`：Synthetic post-training pipelines commonly filter generated samples with reward models or holistic LLM judges, yet two practices remain rarely examined together: whether the filtering signal is grounded in the source evidence that induced each generation, and whether rejected samples can be systematically recovered rather than permanently discarded.

机制与 owner：Attach append-only source provenance to each synthetic sample, require separate faithfulness and reward gates, then route rejected samples to diagnosed repair rather than blind retry. 状态/数据/控制 owner 固定为 `TRAIN-DATA`；Method 锚点是 `§2 Methodology`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§3–4 Experimental Setup and Results` 只证明 `Synthetic post-training pipelines commonly filter generated samples with reward models or holistic LLM judges, yet two practices remain rarely examined together: whether the filtering signal is grounded in the source evidence that induced each generation, and whether rejected samples can be systematically recovered rather than permanently discarded.` 上、`Qwen3 1.7B/4B/8B generators; Qwen3-14B, Qwen3.6-27B-FP8, Qwen3.6-35B-A3B judges` 条件下的报告指标。hardware=`Not Disclosed`；precision=`27B judge FP8; other precision not disclosed`；batch=`Approximately 8,000–8,500 candidates per generator; training batch hyperparameters are in exact-v1 Appendix E`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Stronger judges improve the provenance gate but generator scale dominates downstream quality; fixed thresholds and synthetic injections are experiment policy, not universal release criteria. 反证/外推边界在 `Appendix D Discussion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [When RL Fails after SFT: Rejuvenating Model Plasticity for Robust SFT-to-RL Handoff](https://arxiv.org/abs/2606.09932v1)

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：过度 SFT 会耗尽后续 RL 的 policy plasticity；SFT-to-RL handoff 应以可学习性而非只看 SFT checkpoint accuracy 作为 release 条件。 exact-v1 摘要将具体问题界定为：Supervised Fine-Tuning (SFT) followed by Reinforcement Learning (RL) has become a standard pipeline for Large Language Model (LLM) post-training. SFT is expected to provide a useful behavioral prior for RL to further enhance model capabilities. However, checkpoints with excessive SFT often show limited improvement during RL. We attribute this failure to the loss of model plasticity: the reduced ability of an SFT-initialized policy to be effectively reshaped by subsequent RL. To better understand this phenomenon, we

**State / data / control owner。** `TRAIN-RLHF` 负责rollout distribution、checkpoint plasticity 与 sampler identity；在本 source 中，需被显式持有、传递或阻断的状态正是“过度 SFT 会耗尽后续 RL 的 policy plasticity；SFT-to-RL handoff 应以可学习性而非只看 SFT checkpoint accuracy 作为 release 条件。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.09932v1 §4 Experiments; §4.1 Setup; §§4.2–4.3; Appendix B` 实际支持的合同是 `Disclosed — math RL and τ-bench Retail agentic SFT/RL, with plasticity probes and periodic validation`，evaluator 是 `Disclosed — checkpoint/RL improvement, Math-Verify reward, τ-bench task outcomes, plasticity diagnostics and rejuvenation cost`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.09932v1 §3 Diagnosing and Restoring Plasticity; §§3.1–3.4`；counterevidence locator: `arXiv:2606.09932v1 Appendix C analyses/cost; handoff evidence is workload-specific, not a universal SFT stopping rule`。

**Trade-off / failure / coexistence / evolution。** plasticity rejuvenation 避免重跑 SFT，却可能牺牲已学能力并依赖 base anchor；适度 SFT checkpoint 仍应首选，reset/fusion 只能作为 handoff repair。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

**Claim boundary。** 可引用内容限于 `arXiv:2606.09932v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。

### [GitInject: Real-World Prompt Injection Attacks in AI-Powered CI/CD Pipelines](https://arxiv.org/abs/2606.09935v1)

**问题、旧路径与机制。** 旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：GitInject 把 issue、PR 与仓库文本中的 prompt injection 连到高权限 CI/CD agent，要求 untrusted content、repository permission 与 approval gate 分离。 exact-v1 摘要将具体问题界定为：AI-powered agents are increasingly embedded in continuous integration and continuous delivery/deployment (CI/CD) pipelines to autonomously review pull requests (PRs), triage issues, and maintain codebases. These agents ingest untrusted content while operating with elevated repository permissions, making them a natural target for prompt injection attacks with supply chain consequences. We present GitInject, an open-source framework for evaluating prompt injection vulnerabilities in real, live GitHub workflows, a wid

**State / data / control owner。** `PLATFORM-SECURITY` 负责输入信任、权限与阻断/升级控制；在本 source 中，需被显式持有、传递或阻断的状态正是“GitInject 把 issue、PR 与仓库文本中的 prompt injection 连到高权限 CI/CD agent，要求 untrusted content、repository permission 与 approval gate 分离。”所指向的中间产物。论文项目名不取得跨章节 ownership。

**Evaluation：proof / non-proof。** `arXiv:2606.09935v1 §5 Results; §§5.1–5.5; Appendices B–C` 实际支持的合同是 `Disclosed — real-world AI-powered CI/CD agent workflows with malicious issue/PR/repository content and permission-bearing actions`，evaluator 是 `Disclosed — exploit/attack outcomes across injection surfaces, permissions and mitigations; claim is CI/CD threat-model scoped`。这能支持该 workload 下的机制差异，但不证明生产 SLO 或跨模型/跨版本普遍优越性；未披露字段在合同中继续保持 `Not Disclosed`。Method locator: `arXiv:2606.09935v1 §3 Threat Model; §4 GitInject workflows/scenarios/execution`；counterevidence locator: `arXiv:2606.09935v1 §§6.1–6.3 structural scope, limitations, and responsible disclosure`。

**Trade-off / failure / coexistence / evolution。** 权限与不可信内容分离降低 CI/CD injection，却增加 approval friction；只读、低权限 bot 可保留自动路径，高权限 agent 若继承仓库文本即形成结构性失败。 长期知识只吸收这个约束变化与 owner 交接，不吸收产品排名。

**Claim boundary。** 可引用内容限于 `arXiv:2606.09935v1` 的 method/evaluation/limitations 与下列 benchmark contract。Access route: `official-exact-v1-html-web-proxy`；ordinary pending=`0`。

### [Stop Early, Spend Less: Hidden-State Probes as a Practical Recipe for Streaming Moderation of LLM Outputs](https://arxiv.org/abs/2606.10487v1)

`Stop Early, Spend Less: Hidden-State Probes as a Practical Recipe for Streaming Moderation of LLM Outputs` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10487v1`：Deploying large language models in user-facing systems requires efficient output safety filtering.

机制与 owner：Reuse generator hidden states for token-level safety probes and give the decoding loop early halt/modify authority before unsafe output completes. 状态/数据/控制 owner 固定为 `PLATFORM-SECURITY`；Method 锚点是 `§3 Method`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§§4–8 offline and online evaluation` 只证明 `Deploying large language models in user-facing systems requires efficient output safety filtering.` 上、`DeepSeek-R1-0528-Qwen3-8B reported; Qwen3-8B and Qwen3-30B-A3B-Thinking-2507 probes are qualitative omitted runs` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：A cheap probe is a latency-oriented surrogate for a stronger guard and can miss distribution shift; post-hoc moderation remains a fallback rather than disappearing. 反证/外推边界在 `§9 Discussion and future work`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Fingerprinting All AI Cluster I/O Without Mutually Trusted Processors](https://arxiv.org/abs/2606.10724v1)

`Fingerprinting All AI Cluster I/O Without Mutually Trusted Processors` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10724v1`：In preparation for potential international agreements on artificial intelligence, the development of verification infrastructure for AI data centres is vital.

机制与 owner：Commit all cluster ingress and egress at passive optical taps and sanitize timing, analogue and protocol-header covert channels in a separate secure gateway. 状态/数据/控制 owner 固定为 `PLATFORM-SECURITY`；Method 锚点是 `§4 Architecture`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§5 Covert Channel Estimates` 只证明 `In preparation for potential international agreements on artificial intelligence, the development of verification infrastructure for AI data centres is vital.` 上、`Not applicable: architecture/estimate paper, no evaluated LM checkpoint` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：The paper specifies architecture and estimates rather than a deployed device; encrypted payload semantics and untapped physical paths remain outside the proof. 反证/外推边界在 `§6 Limitations and Future Work`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents](https://arxiv.org/abs/2606.10742v1)

`MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10742v1`：External memory has become a core component of modern web agents, enabling long-horizon reasoning through the retrieval of past experiences.

机制与 owner：Treat multimodal external memory as a persistent attack surface: trigger-conditioned retrieval recalls poisoned text-image evidence that then redirects the web agent. 状态/数据/控制 owner 固定为 `AGENT-MEMORY`；Method 锚点是 `§3 Method`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Experiments` 只证明 `External memory has become a core component of modern web agents, enabling long-horizon reasoning through the retrieval of past experiences.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：High attack success assumes the tested memory graph, OCR path and black-box threat model; memory admission, provenance and post-retrieval containment must coexist. 反证/外推边界在 `§4.6 Further Analysis and §5 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models](https://arxiv.org/abs/2606.10949v1)

`Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.10949v1`：Persistent memory systems promise to make LLMs more helpful by storing user beliefs over time.

机制与 owner：Make memory extraction preserve corrective context and disagreement instead of compressing only user misconceptions that later amplify sycophancy. 状态/数据/控制 owner 固定为 `AGENT-MEMORY`；Method 锚点是 `§3 Methods`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§§4–6 Results, Analysis, and Mitigation` 只证明 `Persistent memory systems promise to make LLMs more helpful by storing user beliefs over time.` 上、`GPT-5.2, Claude Sonnet 4.6, Qwen 3.5, Kimi K2.5, MiniMax 2.5 across Mem0, MemOS, and Zep` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Mitigations are evaluated on synthetic conversations and can trade recall for correction; memory is still useful when belief provenance and counterevidence survive extraction. 反证/外推边界在 `§5 Analysis and §7 Conclusion`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs](https://arxiv.org/abs/2606.11063v1)

`CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs` 的 exact-v1 问题边界来自 `https://arxiv.org/html/2606.11063v1`：AI control protocols oversee untrusted models by monitoring their actions and modifying potentially unsafe steps, often using a trusted model.

机制与 owner：Measure whether an untrusted model can distinguish its own trajectory from trusted-control interventions before deploying a monitoring protocol. 状态/数据/控制 owner 固定为 `PLATFORM-SECURITY`；Method 锚点是 `§3 CIAware-Bench`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。

Evaluation proof：`§4 Results` 只证明 `AI control protocols oversee untrusted models by monitoring their actions and modifying potentially unsafe steps, often using a trusted model.` 上、`Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity` 条件下的报告指标。hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed — measured outcomes and experimental thresholds are not production SLOs`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。

Trade-off、failure、共存与演进：Awareness varies by domain, provider style and model pair; benchmark accuracy does not prove strategic evasion or safety under a live controller. 反证/外推边界在 `§5.2 Limitations and Future Work`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。

### [Operator Fusion for LLM Inference on the Tensix Architecture](https://arxiv.org/abs/2606.09879v1)

Exact-v1 §3 定义 Tensix 上的 operator fusion 与 data-layout 约束，§4 比较所列模型/算子，§5 说明平台与 shape 外推边界。它把多个 kernel launch 与中间 materialization 编译为一个 execution plan；收益是减少搬运与启动，代价是更窄的 shape、数值等价性验证和平台耦合。当前 Ch49 已要求 fusion 只作为 plan proposal，经目标硬件 correctness/quality gate 后才能 commit，因此为已有覆盖。

**证据边界：** primary=`arXiv:2606.09879v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [WebChallenger: A Reliable and Efficient Generalist Web Agent](https://arxiv.org/abs/2606.10423v1)

Exact-v1 §2 给出 PageMem、页面观察与 action/finish 管线，§3 在作者 web task 上评估，§5 保留站点漂移、成本和泛化限制。它需要显式维护页面状态、工具 effect 与完成判定，但当前 Ch78 已将 program-state observation 与 effect-state receipt 作为 finish gate，Ch77/81 分别拥有持久记忆与 workflow recovery，因此不新增 owner。

**证据边界：** primary=`arXiv:2606.10423v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [Streaming Knowledge Compilation: Proactive Materiality-Scored Pinning for Time-Evolving LLM Wikis](https://arxiv.org/abs/2606.09877v1)

Exact-v1 §3 将动态文档流、固定 token budget 与未知未来 query 形式化，§4 给出 materiality-scored pinning 和 regret 分析；结论只在 materiality error 与论文假设下成立。该机制牺牲 oracle 精度换主动驻留，materiality 漂移时必须回退可恢复 tier；Ch45 已明确 future reuse intent、semantic region identity 与 eviction owner。

**证据边界：** primary=`arXiv:2606.09877v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [Less Context, More Accuracy: A Bi-Temporal Memory Engine for LLM Agents Where a Lean Retrieved Context Beats the Full History](https://arxiv.org/abs/2606.09900v1)

Exact-v1 §3 定义 event time/transaction time、snapshot 与 supersession，§4–5 在作者任务上评估，§6 说明外部知识和长周期边界。双时间能减少过期上下文，却增加 revision、snapshot 和纠错传播成本；Ch77 的 Bitemporal Memory、transaction 与 rollback 命题已完整承载。

**证据边界：** primary=`arXiv:2606.09900v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning](https://arxiv.org/abs/2606.10532v1)

Exact-v1 §3 将 long-horizon reasoning 的 memory 写入、并行 worker、aggregation 与读取分开，§4 报告论文任务结果；未证明开放生产一致性或无界扩展。并行提高 throughput，却引入 write conflict、fan-in 与 stale context；Ch77 已要求 memory controller 与 fact owner 分离，并保存 lossless source 和 bounded fan-in/version。

**证据边界：** primary=`arXiv:2606.10532v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [SkillAxe: Sharpening LLM-Authored Agent Skills Through Evaluation-Guided Self-Refinement](https://arxiv.org/abs/2606.10546v1)

Exact-v1 §3 给出 skill 生成—测试—修订循环，§4 评估作者环境，§5–6 说明 evaluator 偏差与跨任务限制。自改进能减少人工编辑，却可能把 trial overfit 直接晋级；Ch81 已把 trial evidence、独立 promotion、rollback 与 sequential refinement 分开，故为已有覆盖。

**证据边界：** primary=`arXiv:2606.10546v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory](https://arxiv.org/abs/2606.10677v1)

Exact-v1 §3 将长期经验组织为可维护 topic documents，§4 验证检索/维护，§5 保留 summary loss、drift 与扩展限制。派生文档减少读取成本，却不能替代 raw evidence；Ch77 已规定分层粒度、lossless source、read-time construction 和 lifecycle。

**证据边界：** primary=`arXiv:2606.10677v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs](https://arxiv.org/abs/2606.10694v1)

Exact-v1 §III 定义 reasoning-enhanced memory graph，后续实验评估检索/更新；论文不能证明关系为事实或跨域稳定。图结构提升关联召回，却引入 relation hallucination、版本和删除传播；Ch77 已要求 edge provenance、valid time、confidence、supersession 与 dependency propagation。

**证据边界：** primary=`arXiv:2606.10694v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [The Arbiter Agent: Continually Monitoring Multi-Agent Conversations to Detect Emergent Misalignment](https://arxiv.org/abs/2606.10747v1)

Exact-v1 §3 定义持续旁观 multi-agent conversation 的 Arbiter，§4–5 报告检测，限制在合成/披露对话和模型。持续监控提高早期发现，却引入 observer bias、预算和过度干预；Ch66 已将 Judge 定义为有预算 evidence-acquisition policy，不能拥有环境真值。

**证据边界：** primary=`arXiv:2606.10747v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [READER: Robust Evidence-based Authorship Decoding via Extracted Representations](https://arxiv.org/abs/2606.10794v1)

官方 exact-v1 §3.1–3.4 定义 frozen proxy hidden-state reading、response 内 temporal low-pass filtering、L2 multinomial probe 与跨独立 prompts 的 Bayesian Evidence Accumulation；§4 在 50-target Agent500、500 prompts、25,000 trajectories 与九个 proxy readers 上评估，单响应 top-1 31.0–42.4%，50 响应 70.0–84.0%。§5 明确 closed-set、single-source、增 label 需重训，且未覆盖 closed API、multi-backend/post-processing、adaptive attack 与跨 language/task/decoding/deployment；它不是身份真值、权重等价证明或 attestation。Ch59 已拥有模型身份和 behavior provenance，但只覆盖主动固定 probes，尚未覆盖 query-varying 被动流的 proxy reader 与证据累积，因此构成真实增量；Ch69/72 仅接收 trace 与安全 handoff。

**证据边界：** primary=`arXiv:2606.10794v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [CollabSkill: Evaluating Human-Agent Collaboration On Real-World Tasks](https://arxiv.org/abs/2606.09833v1)

Exact-v1 §3 收集 386 sessions、93 workers 与 10/20 个 O*NET sector 的协作数据，§4 用 rating model 分离 human/agent contribution，§5–6 分析经验与协作；selection bias、scalar task score 和覆盖有限。现有 Ch66 没有把 team 与 attribution estimator 建成独立 evaluation object，因此提议补入。

**证据边界：** primary=`arXiv:2606.09833v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [FailureScope: Cross-Regime Behavioral Diagnosis of Language Model Weaknesses](https://arxiv.org/abs/2606.09878v1)

Exact-v1 §3–8 建立 cross-regime failure taxonomy、slice 与对照；它能诊断 regime shift，但不证明 taxonomy 完备或因果根因。Ch66 已要求 blind-spot mass、failure-type slices 与非因果边界，故只保留受限案例。

**证据边界：** primary=`arXiv:2606.09878v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [PreAct-Bench: Benchmarking Predictive Monitoring in LLMs](https://arxiv.org/abs/2606.09890v1)

Exact-v1 §3 定义 action 前 predictive monitoring 与 clean twin，§4 报告不同模型/任务结果；固定可见 prefix、review length 与 synthetic setup 限制外推。Ch66 已要求 proactive Agent 同时测 act/silent/stop，并保留 pre-execution sensor 的误报和升级边界。

**证据边界：** primary=`arXiv:2606.09890v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [IDP-Bench: Benchmarking ability of LLMs to protect personal information in interdependent privacy contexts](https://arxiv.org/abs/2606.09908v1)

Exact-v1 §3 以 Contextual Integrity 建模 sender、recipient、transmission principle、attribute，并增加 primary/secondary subject 与 co-ownership；§4 和 Appendix A 报告 synthetic vignettes、LLM judge 与局限。它不证明法律正确性，却新增 multi-subject privacy object 和 ambiguous-consent gate，建议写入 Ch72。

**证据边界：** primary=`arXiv:2606.09908v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [Quality Is Not a Safety Proxy Under Quantization](https://arxiv.org/abs/2606.10154v1)

Exact-v1 §3–5 证明模型平均质量保持时安全行为仍可在量化后变化；结果绑定论文模型、量化配置与 evaluator，不是通用安全退化率。Ch72 已把 quantization 定义为新的 Security Revision，Ch45 负责 precision/runtime 验收。

**证据边界：** primary=`arXiv:2606.10154v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [Catching One in Five: LLM-as-Judge Blind Spots in Production Multi-Turn Transaction Agents](https://arxiv.org/abs/2606.10315v1)

Exact-v1 §3–8 比较 production-style multi-turn transaction trajectories 与 LLM judge，暴露 final narrative 对真实 effect 的盲区；数据、domain、judge 与 adjudication 都限制外推。Ch66 已要求 trajectory judge 分开叙述、动作、effect receipt 与 failure recall。

**证据边界：** primary=`arXiv:2606.10315v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [AgentCanary: A Security Evaluation Framework for Autonomous AI Agents in Real Executable Environments](https://arxiv.org/abs/2606.10484v1)

Exact-v1 定义 Entry×Impact taxonomy、真实 executable environment、full trajectory 与 outcome/effect evaluator，并在作者 agent/runtime 上测试；覆盖仍不等于完备安全。Ch72 已拥有 authority BOM、channel coverage、executable PoV 与 reference monitor 分权。

**证据边界：** primary=`arXiv:2606.10484v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [Assessing Automated Prompt Injection Attacks in Agentic Environments](https://arxiv.org/abs/2606.10525v1)

官方 exact-v1 §3 threat model、§4 problem、§5 automated attack 与 §6 experiments 覆盖 80 task pairs、4 domains 和多模型，证明 transfer 依赖 attacker/target model、task/OOD 与 safety tuning；不证明通用攻击率。Ch72 已明确 generator checkpoint/guard revision、model mismatch/transfer failure 与 campaign budget。

**证据边界：** primary=`arXiv:2606.10525v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [When the Defense Writes the Refusal: Auditing Keyword-Scored Evaluation of Inference-Time Defenses for Multimodal Large Language Models](https://arxiv.org/abs/2606.10904v1)

Exact-v1 §3–6 通过 intervention arms 检查 keyword-scored defense evaluation，说明 refusal token 可能被 scorer 当成成功；结论绑定论文防御、模型和 evaluator。Ch66 已要求 construct-validity intervention 与 evaluator admission，故不重复正文。

**证据边界：** primary=`arXiv:2606.10904v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [VISTA: A Versatile Interactive User Simulation Toolkit for Agent Evaluation](https://arxiv.org/abs/2606.11079v1)

Exact-v1 将 user simulator、hidden constraints 与 consequential outcome 组合为 Agent testbed，实验与结论只覆盖披露 domains/models，不能代替真人或生产环境。Ch66 已把 simulator fidelity、user bias 与 domain slice 纳入 evaluation identity。

**证据边界：** primary=`arXiv:2606.11079v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [The Interlocutor Effect: Why LLMs Leak More Personal Data to Agents Than Humans](https://arxiv.org/abs/2606.09844v1)

Exact-v1 §III–IV 用 2×2 factorial 和 3,464 次交互检验 recipient framing，§V–VI 明确模型依赖、Llama 结果不显著、judge/temperature/confound；attention-head 解释仍是机制假设。它要求 egress policy 绑定 recipient principal/purpose/fields，unknown recipient fail closed，建议写入 Ch72。

**证据边界：** primary=`arXiv:2606.09844v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。
### [Deployment-Time Memorization in Foundation-Model Agents](https://arxiv.org/abs/2606.10062v1)

Exact-v1 §2 定义 deployment-time memorization，§3 评估参数外 Agent memory 的写入与恢复；没有证明完全删除、跨实现等价或生产隐私。Ch77 已有 bitemporal/supersession/transaction/deletion propagation，Ch72 负责 parameter–memory backflow，故为已有覆盖。

**证据边界：** primary=`arXiv:2606.10062v1`；Method/Evaluation/Limitations 均已定位；未披露的 hardware、precision、batch、concurrency 与 production SLO 保持 `Not Disclosed`，作者 benchmark 不外推。

## 5. 缺口与下一步

无

普通 Pending、exact-v1 access blocker 与 Books writeback queue 均为 0。五项新增正文保留了旧方案成立条件、状态/控制权变化、证据边界、trade-off 与 fallback；Kimi Code 与 MaxProof 均由当前命题级正文覆盖。当前每日厂商源与 arXiv 均已按本窗回放，不需要用户补材料。

## 6. 复核

复核者：root post-write semantic audit；独立 full-table audit 见 `v3-candidate-denominator-audit-20260911.json` 与 `v3-reverse-admission-audit-20260911.json`
结论：通过

Coverage、candidate admission 与 Evidence 已闭合；49 项 Existing 与既有 5 项 Books 正文均已核验。Kimi Code release 只作为版本接口证据，MaxProof 已由 `TRAIN-GRPO` 的 verifier specification、独立 oracle 与权威分离命题覆盖；不存在开放 Books proposal。
