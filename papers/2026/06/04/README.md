# Daily Research — 2026-06-04

**规范：** V3
**窗口：** 2026-06-03T09:00:00+08:00 ～ 2026-06-04T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T22:00:00+08:00

## 1. 结论

本窗不能继承旧完成结论。575 个去重 arXiv 题摘身份先后经过两轮作者侧收紧，随后由非作者 fresh audit 再次逐项挑战；撤稿核验又确认 2606.04101 UltraEP 的 arXiv v1/v2/v3 均因许可问题 withdrawn，不得进入 Candidate 或 Books。权威 arXiv 分母因此为 Candidate 64、Close 511；厂商源再认证另恢复 1 个 Kimi Code release Source Family，报告总分母为 65 Candidate。非作者复核相对作者侧 `73 / 502` 共关闭 9 项：2606.04101、2606.04233、2606.04460、2606.04507、2606.04536、2606.04660、2606.04847、2606.04883、2606.04970。首轮 `210 / 365` 与作者侧第二轮 `73 / 502` 都只保留为审计历史，不能再作为当前分母。完整 exception ledger 见 [JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md](../_sources/JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md)。

旧全文已保存到 [V2_1_EVIDENCE_ARCHIVE.md](../_sources/daily-20260604/V2_1_EVIDENCE_ARCHIVE.md)。存续 Candidate 的旧 exact-v1 只在身份与当前 claim 一致时复用；当前 65 项的候选级评分、Evidence 与逐项 Books Decision 已完成。EvalStop 已写入 Ch31 并通过非作者 post-write 语义复核；UltraEP 在 Books 中没有残留；2606.04071 已改判 `已有覆盖`，旧 adoption trace 也已精确删除。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [厂商源再认证](../_sources/daily-20260601/CURRENT_CONTRACT_DAILY_SOURCE_RECERT_20260914.md#来源结论)：Dreaming 只披露 06-04 日期，不能唯一落入 09:00 截点 | 受阻 | 缺原始发布时刻；隔离且不支持本窗候选或 Books |
| SRC-ANTHROPIC | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-GOOGLE-AI | 同上；合作/超智能讨论不改变当前系统设计，已关闭 | 已检查 | 无 |
| SRC-META-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-QWEN | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-DEEPSEEK | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MOONSHOT | 同上；Kimi Code 0.9.0 的精确 release 时刻落在本窗，见候选与判断 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 同上；“全部”列表本窗无条目 | 已检查 | 无 |
| SRC-ZAI | 同上；Research 列表本窗无条目 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 同上；技术博客本窗无条目 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MINIMAX | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-ARXIV | [canonical-raw-identity-inventory-v2.1.json.gz](../_sources/daily-20260604/canonical-raw-identity-inventory-v2.1.json.gz)、[canonical-semantic-screening-checkpoint-v2.1.json.gz](../_sources/daily-20260604/canonical-semantic-screening-checkpoint-v2.1.json.gz)、[V3_SCREENING_LEDGER.md](../_sources/daily-20260604/V3_SCREENING_LEDGER.md) 与独立 [fresh audit](../_sources/JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md)；575 identities，2606.04101 withdrawal closure，最终分母 64 Candidate / 511 Close | 已检查 | 无 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.9.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.9.0) | 2026-06-03T22:01:42+08:00 | ACP-over-stdio 与 side-channel conversation 分离主 turn 和外部 client control；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-MCP` — [章节](../../../../books/part-07-agent/83-mcp.md) |
| [Neither Layer Alone: Epistemic Integrity Requires Hierarchical Joint Design for Long-Running AI Agents](https://arxiv.org/abs/2606.04017v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+3+2=7；exact-v1 与当前 claim 一致，owner=`AGENT-PLATFORM` | 深入完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study](https://arxiv.org/abs/2606.04056v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+2+2=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Covert Influence Between Language Models](https://arxiv.org/abs/2606.04071v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Proof-Carrying Agent Actions: Model-Agnostic Runtime Governance for Heterogeneous Agent Systems](https://arxiv.org/abs/2606.04104v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [EvalStop: Using World Feedback to Detect and Correct Reward Overoptimization in Multi-Tenant RLHF Platforms](https://arxiv.org/abs/2606.04145v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`TRAIN-RLHF` | 深入完成 | 整合：`TRAIN-RLHF`（[books/part-04-training-system/31-rlhf.md](../../../../books/part-04-training-system/31-rlhf.md)）；正文锚点“训练停止不能只看 Training Loss 或 Reward Model Score”；下游 world-feedback/eval trajectory 驱动多租户 RLHF 作业 early stop 与 GPU 释放 |
| [Notarized Agents: Receiver-Attested Confidential Receipts for AI Agent Actions](https://arxiv.org/abs/2606.04193v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Puffin-Backed Vector Indexes: Attaching Approximate Nearest Neighbor Indexes to Apache Iceberg Snapshots for Compute-Disaggregated Query Engines](https://arxiv.org/abs/2606.04196v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-RAG` | 深入完成 | 已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)) |
| [Can Generalist Agents Automate Data Curation?](https://arxiv.org/abs/2606.04261v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+2+2=7；exact-v1 与当前 claim 一致，owner=`TRAIN-DATA` | 深入完成 | 已有覆盖：`TRAIN-DATA`（[books/part-04-training-system/27-data.md](../../../../books/part-04-training-system/27-data.md)) |
| [The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents](https://arxiv.org/abs/2606.04296v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding](https://arxiv.org/abs/2606.04302v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`INFER-KV-CACHE` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)) |
| [Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems](https://arxiv.org/abs/2606.04306v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline](https://arxiv.org/abs/2606.04315v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+2+2=7；exact-v1 与当前 claim 一致，owner=`AGENT-MEMORY` | 深入完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [The Digital Apprentice: A Framework for Human-Directed Agentic AI Development](https://arxiv.org/abs/2606.04321v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`AGENT-PLATFORM` | 深入完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents](https://arxiv.org/abs/2606.04329v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-MEMORY` | 深入完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation](https://arxiv.org/abs/2606.04402v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-SCHEDULING` | 深入完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [FlexNPU: Transparent NPU Virtualization for Dynamic LLM Prefill-Decode Co-location](https://arxiv.org/abs/2606.04415v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-PD-DISAGGREGATION` | 深入完成 | 已有覆盖：`INFER-PD-DISAGGREGATION`（[books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md)) |
| [What If Prompt Injection Never Left? Rethinking Agent Security through Cross-Session Stored Prompt Injection](https://arxiv.org/abs/2606.04425v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`AGENT-MEMORY` | 深入完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Token Rankings are Unforgeable Language Model Signatures](https://arxiv.org/abs/2606.04459v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+1=5；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [ANN Search: Recall What Matters](https://arxiv.org/abs/2606.04522v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Cartridges at Scale: Training Modular KV Caches over Large Document Collections](https://arxiv.org/abs/2606.04557v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`INFER-KV-CACHE` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)) |
| [Multi-SPIN: Multi-Access Speculative Inference for Cooperative Token Generation at the Edge](https://arxiv.org/abs/2606.04581v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`INFER-SPECULATIVE-DECODING` | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`（[books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)) |
| [Ekka: Automated Diagnosis of Silent Errors in LLM Inference](https://arxiv.org/abs/2606.04594v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-TRACE` | 深入完成 | 已有覆盖：`PLATFORM-TRACE`（[books/part-06-ai-infrastructure/69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md)) |
| [RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation](https://arxiv.org/abs/2606.04628v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`AGENT-MEMORY` | 深入完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications](https://arxiv.org/abs/2606.04769v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-MCP` | 深入完成 | 已有覆盖：`AGENT-MCP`（[books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md)) |
| [UModel: An Agent-Ready Observability Data Modeling Method at Scale](https://arxiv.org/abs/2606.04799v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-TRACE` | 深入完成 | 已有覆盖：`PLATFORM-TRACE`（[books/part-06-ai-infrastructure/69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md)) |
| [Provably Auditable and Safe LLM Agents from Human-Authored Ontologies](https://arxiv.org/abs/2606.04903v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+1=5；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [GNStor: Design of GPU-Native High-Performance Remote All-Flash Array](https://arxiv.org/abs/2606.04908v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-GPU-MEMORY` | 深入完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2606.04923v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+2+2=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Sequential Data Poisoning in LLM Post-Training](https://arxiv.org/abs/2606.04929v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [SharedRequest: Privacy-Preserving Model-Agnostic Inference for Large Language Models](https://arxiv.org/abs/2606.05004v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；2+2+2=6；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [Validity Threats for Foundation Model Research](https://arxiv.org/abs/2606.05029v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Self-Reflective APIs: Structure Beats Verbosity for AI Agent Recovery](https://arxiv.org/abs/2606.05037v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+2+2=7；exact-v1 与当前 claim 一致，owner=`AGENT-TOOL-CALLING` | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING`（[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)) |
| [Strabo: Declarative Specification and Implementation of Agentic Interaction Protocols](https://arxiv.org/abs/2606.05043v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 不重复评分：V2.1 已处理；3+3+2=8；exact-v1 与当前 claim 一致，owner=`AGENT-MULTI-AGENT` | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)) |
| [Novel Aspects of IEEE SA P3109 Arithmetic Formats for Machine Learning](https://arxiv.org/abs/2606.04028v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification](https://arxiv.org/abs/2606.04037v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Need to Know: Contextual-Integrity-Grounded Query Rewriting for Privacy-Conscious LLM Delegation](https://arxiv.org/abs/2606.04067v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-SECURITY` | 标准完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Caught in the Act(ivation): Toward Pre-Output and Multi-Turn Detection of Credential Exfiltration by LLM Agents](https://arxiv.org/abs/2606.04141v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-SECURITY` | 标准完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval](https://arxiv.org/abs/2606.04391v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Context-as-AI-Service: Surfacing Cross-File Dependency Chains for LLM-Generated Developer Documentation](https://arxiv.org/abs/2606.04397v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-RAG` | 标准完成 | 已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)) |
| [Trivium: Temporal Regret as a First-Class Objective for Causal-Memory Controllers](https://arxiv.org/abs/2606.04421v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation](https://arxiv.org/abs/2606.04435v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-RAG` | 标准完成 | 已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)) |
| [AgentJet: A Distributed Swarm Training Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.04484v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`TRAIN-DISTRIBUTED-TRAINING` | 标准完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)) |
| [Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents](https://arxiv.org/abs/2606.04555v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Selectivity Estimation for Semantic Filters on Image Data](https://arxiv.org/abs/2606.04610v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-RAG` | 标准完成 | 已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)) |
| [Bridge the Last-Mile Gap to Semantic Analytics: Compiling Natural-Language Queries into Semantic Operator Pipelines](https://arxiv.org/abs/2606.04641v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-RAG` | 标准完成 | 已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)) |
| [CYGNET: Cypher Gate for Neural Execution Triage and Cost Containment](https://arxiv.org/abs/2606.04645v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-TOOL-CALLING` | 标准完成 | 已有覆盖：`AGENT-TOOL-CALLING`（[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)) |
| [Rethinking Continual Experience Internalization for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.04703v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents](https://arxiv.org/abs/2606.04780v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [AIP: A Graph Representation for Learning and Governing Agent Skills](https://arxiv.org/abs/2606.04781v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-PLATFORM` | 标准完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents](https://arxiv.org/abs/2606.04815v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)) |
| [Channel Fracture: Three Instances of Cross-Boundary Silent Delivery Reliability Failures in Multi-Agent Systems](https://arxiv.org/abs/2606.04896v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-MULTI-AGENT` | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)) |
| [Audio Interaction Model](https://arxiv.org/abs/2606.05121v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`MULTIMODAL-REPRESENTATION` | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`（[books/part-03-multimodal-world-models/23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)) |
| [Streaming Communication in Multi-Agent Reasoning](https://arxiv.org/abs/2606.05158v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-MULTI-AGENT` | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)) |
| [Discourse-Role Labels as Presentation-Time Variables for Context Use in Language Models](https://arxiv.org/abs/2606.04109v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?](https://arxiv.org/abs/2606.04455v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [QO-Bench: Diagnosing Query-Operator-Preserving Retrieval over Typed Event Tuples](https://arxiv.org/abs/2606.04646v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`AGENT-RAG` | 标准完成 | 已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)) |
| [Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models](https://arxiv.org/abs/2606.04739v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?](https://arxiv.org/abs/2606.05080v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Failed Reasoning Traces Tell You What Is Fixable (But Not by Reading Them)](https://arxiv.org/abs/2606.05145v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`INFER-SCHEDULING` | 标准完成 | 已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)) |
| [Beyond Single-Policy: Evaluating Composed Organization-Specific Policy Alignment in LLM Chatbots](https://arxiv.org/abs/2606.04394v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [MemoryDocDataSet: A Benchmark for Joint Conversational Memory and Long Document Reasoning](https://arxiv.org/abs/2606.04442v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Benchmarking Living-Screen-Native GUI Agents on Short-Video Platforms](https://arxiv.org/abs/2606.04701v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)）；“Judge 从被动 Scorer 演进为有预算的 Evidence Acquisition Policy”与 Living-world Evaluation/Run Identity |
| [Auditing CoT Answer-Hijack Patches: Source-Control Certificates with Type-I Guarantees](https://arxiv.org/abs/2606.04717v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 仅报告：当前窗口上下文，不形成独立长期机制 |
| [Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents](https://arxiv.org/abs/2606.04874v1) | 2026-06-04T08:00:00+08:00 ～ 2026-06-04T09:00:00+08:00 | 2+2+2=6；给出可迁移的长期系统/评测合同，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |

候选分母最终冻结为 65：64 个 arXiv Candidate 加 1 个厂商 release Candidate。旧 33 项复用仍与当前 claim 一致的 exact-v1，31 个新恢复项的正文证据见下节两批审阅包；Kimi Code release 已完成官方 release Evidence。当前 disposition 为：55 项已有覆盖、9 项仅报告、1 项已整合、0 项结构候选、0 项暂缓。UltraEP 作为 withdrawal closure 不参与评分、Evidence 或 Books。

## 4. 证据与知识整合

### [Kimi Code 0.9.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.9.0)

官方 GitHub Release 的 `published_at=2026-06-03T14:01:42Z`。release notes 披露 ACP adapter 以 stdio 接入外部 client，并以 `/btw` side-channel 避免旁路问题污染主 conversation；它证明公开接口存在，不证明跨 client interoperability、durable replay、消息次序或生产 SLO。`AGENT-MCP` 已覆盖协议适配器、transport/session identity、旁路控制与失败边界，故维持 `No Change — Existing Coverage`。

旧候选的 Method/Evaluation/Limitations 与 exact-v1 保留在归档中，但旧 Books disposition 不继承；UltraEP 的归档记录仅是历史证据，不再构成当前 Source Review。独立复核确认 2606.04071 与 2606.04929 为 `已有覆盖`：前者跨 `AGENT-MEMORY` 的 Stateless API/Implicit Memory 与 `PLATFORM-SECURITY` 的 Influence Graph，后者使用 Ch72 的 `semantic-body-binding:SF-2026-ARXIV-2606-04929` Review notes 前正文 anchor。2606.04145 EvalStop 已整合至 Ch31“训练停止不能只看 Training Loss 或 Reward Model Score”：外部 Evaluation Run 产生带版本的 downstream-quality trajectory，RLHF controller 只提出 stop proposal，训练作业 owner 提交停止，GPU Scheduler 仅消费资源释放事件。正文保留了固定预算的共存边界、额外评测与反馈延迟等 trade-off，以及连续窗口、人工 gate 等 fallback。其 exact-v1 证据只限离散事件模拟、Poisson arrival、slot GPU、2-minute preemption 与 synthetic/parameterized curves；没有生产 workload、生产 SLO 或 versioned artifact。以下 31 项是本轮新恢复 Candidate 的同标题、同 URL Evidence；旧 33 项的完整 exact-v1 审阅继续由 [V2_1_EVIDENCE_ARCHIVE.md](../_sources/daily-20260604/V2_1_EVIDENCE_ARCHIVE.md) 提供。

### [Novel Aspects of IEEE SA P3109 Arithmetic Formats for Machine Learning](https://arxiv.org/abs/2606.04028v1)

`arXiv:2606.04028v1`，§III Datum Sets、§IV Operations、§V Formal Verification 与 §VIII Block Operations；贡献是数值格式语义、运算与验证边界，不是某个模型的新结构。 §X Discussion and Limitations；标准仍为 draft，不能外推为所有 accelerator 已实现或取得端到端收益。 Books 复核为`Only report`；可路由至训练数值稳定性相邻 owner，但尚不足以改变书稿的通用精度机制链。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification](https://arxiv.org/abs/2606.04037v1)

`arXiv:2606.04037v1`，§2.2 Agent Operational Envelope、§2.3 Ontology-to-Scenario Generation、§2.4 Trust Certificate 与 §2.5 Implementation Architecture；把 ontology 约束、scenario coverage、certificate 与 deployment gate 连成发布合同。 这是 proposed framework；经验有效性依赖 ontology 完整度、judge 校准与 ground-truth controls，不能视作生产认证标准。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；现有评测/发布门已覆盖预声明边界、独立 ground truth 与阻断式 gate。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Need to Know: Contextual-Integrity-Grounded Query Rewriting for Privacy-Conscious LLM Delegation](https://arxiv.org/abs/2606.04067v1)

`arXiv:2606.04067v1`，§3 DelegateCI-Bench 与 §4 Method（framework、reward、policy training）；将 disclosure decision 放在 delegation 前的 query-rewrite boundary。 独立 Limitations；medical/general-domain slice、judge 与本地 reformulator 的边界不能外推为任意隐私域或密码学保密。 Books 复核为`已有覆盖`，owner=`PLATFORM-SECURITY`；最小披露、数据边界与外部模型调用前的 policy enforcement 已有机制 owner。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Caught in the Act(ivation): Toward Pre-Output and Multi-Turn Detection of Credential Exfiltration by LLM Agents](https://arxiv.org/abs/2606.04141v1)

`arXiv:2606.04141v1`，§3 Threat Model、§4.1 System Overview、§4.2 CIFT、§4.3 DP-HONEY 与 §4.4 NIMBUS；把 pre-output activation signal、honeytoken 与跨轮泄漏预算组合成 control plane。 §6 明示小型 in-house benchmark、white-box requirement 与 preliminary prototype；不证明 API-only 黑盒或生产 FPR/SLO。 Books 复核为`已有覆盖`，owner=`PLATFORM-SECURITY`；credential least privilege、跨轮状态、独立 detector 与阻断边界已有正文机制。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval](https://arxiv.org/abs/2606.04391v1)

`arXiv:2606.04391v1`，§3 formalization 与 §4 skill extraction、state-grounded retrieval、injection/execution；skill state 由页面状态而非只由任务文本选择。 独立 Limitations；只验证 WebArena/指定模型，retrieval state 与 skill quality 不代表跨 GUI/workload 泛化。 Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；现有 memory/skill owner 已覆盖写入、检索、版本与执行反馈循环。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Context-as-AI-Service: Surfacing Cross-File Dependency Chains for LLM-Generated Developer Documentation](https://arxiv.org/abs/2606.04397v1)

`arXiv:2606.04397v1`，§3 Source Ingestion、Storage and Indexing、Retrieval Interface、Review Layer；把跨文件依赖作为可追溯 context service 返回。 独立 Limitations；两个匿名案例与文档任务不足以证明通用代码理解或自动合并安全。 Books 复核为`已有覆盖`，owner=`AGENT-RAG`；索引 owner、dependency-aware retrieval、citation/evidence trail 与人工 review handoff 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Trivium: Temporal Regret as a First-Class Objective for Causal-Memory Controllers](https://arxiv.org/abs/2606.04421v1)

`arXiv:2606.04421v1`，§3 Three-Regret Functional、drift-robust replan/dispatch coupling 与 Trivium algorithm；持久 causal log 显式记录 why/when，并影响后续 dispatch。 §5 Conclusion, Impact, and Limitations；受合成 SCM、probe assumptions 与 pilot deployment scope 限制。 Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；现有 episodic/semantic memory、provenance、失效与再规划链已覆盖该长期机制。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation](https://arxiv.org/abs/2606.04435v1)

`arXiv:2606.04435v1`，§III problem formalization、§IV CHARM 与 §V mitigation architectures；在每个 stage 维护跨阶段置信与 verifier，而非只验最终答案。 §VII Discussion；作者验证的是指定注入轨迹与 datasets，不能证明 Bayesian calibration、judge 或所有 retrieval failure 在生产中稳定。 Books 复核为`已有覆盖`，owner=`AGENT-RAG`（相邻 `PLATFORM-EVALUATION-SYSTEM`）；分阶段 citation/verification、fallback 与 end-to-end evaluation 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [AgentJet: A Distributed Swarm Training Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.04484v1)

`arXiv:2606.04484v1`，§3 Swarm Architecture、Swarm RL、episode batching 与 context tracking；client/server 解耦让异构 agent、environment 与 learner 各自拥有生命周期和故障边界。 exact-v1 未定位独立 Limitations 章节；边界由作者披露的 Werewolves/translation/AppWorld 等 workloads 推得，未建立任意环境、网络分区或生产多租户公平性结论。Books 复核为`已有覆盖`，owner=`TRAIN-DISTRIBUTED-TRAINING`；现有 actor/rollout/learner 解耦、trajectory ownership 与 backpressure/failure recovery 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents](https://arxiv.org/abs/2606.04555v1)

`arXiv:2606.04555v1`，§4.1 Conversation Segment Tree、§4.2 online construction 与 §4.3 structure-aware retrieval；显式保留 temporal order 与 hierarchical segment owner。 §6 Limitation and future work；指定 benchmark/backbone 与 online implementation 不能证明所有长期历史或事实更新模式。 Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；时间索引、层级摘要、检索传播与陈旧/冲突处理已有正文。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Selectivity Estimation for Semantic Filters on Image Data](https://arxiv.org/abs/2606.04610v1)

`arXiv:2606.04610v1`，§2 offline embeddings/online estimation、§3 specificity model、compressed KV-cache batching 与 ensemble；把 semantic filter selectivity 变成 query optimizer 的 cost signal。 §3.1 Limitations 与 §6；依赖 embedding/LLM specificity proxy，数据分布漂移和 estimator error 会破坏计划质量。 Books 复核为`已有覆盖`，owner=`AGENT-RAG`；现有检索/query-plan owner 已覆盖质量估计、缓存成本与执行期 fallback。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Bridge the Last-Mile Gap to Semantic Analytics: Compiling Natural-Language Queries into Semantic Operator Pipelines](https://arxiv.org/abs/2606.04641v1)

`arXiv:2606.04641v1`，§3 query-data linker、semantic planner、backend code generation 与 cost summary；分离 data-aware semantics 与 backend-specific execution。 §5 Conclusion；对 reference docs、backend API 稳定性和五个 datasets 的依赖不证明开放世界自然语言可无歧义编译。 Books 复核为`已有覆盖`，owner=`AGENT-RAG`；query planning、operator contract、backend adapter 与可验证执行结果已有机制链。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [CYGNET: Cypher Gate for Neural Execution Triage and Cost Containment](https://arxiv.org/abs/2606.04645v1)

`arXiv:2606.04645v1`，§2 architecture/schema sources、validator backends、mirror graph、equivalence verification、cost gate 与 corrector；在数据库执行前隔离结构错误和高成本计划。 §5 Conclusions；mirror graph/schema coverage、Neo4j planner 与 CypherBench 的结论不外推到任意 tool/database。 Books 复核为`已有覆盖`，owner=`AGENT-TOOL-CALLING`；现有 schema validation、dry-run/sandbox、cost budget 与执行前 authorization 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Rethinking Continual Experience Internalization for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.04703v1)

`arXiv:2606.04703v1`，§3 formulation 与 §5 granularity、injection pattern、internalization regime、multi-iteration stability；区分 contextual experience 与 parametric capability 的 owner。 独立 Limitations；指定任务、训练配方与多轮规模不能证明不会遗忘、污染或跨域退化。 Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；现有“外部记忆优先、参数化吸收需 release/eval gate”已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents](https://arxiv.org/abs/2606.04780v1)

`arXiv:2606.04780v1`，§3 lifecycle state、online evidence insertion、confidence update、offline consolidation 与 path retrieval；把 persona 更新与证据路径显式化。 exact-v1 未定位独立 Limitations 章节；边界由 benchmark 与 synthetic/curated persona evidence 推得，不能证明真实用户 consent、删除权、身份合并或长期漂移已解决。Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；现有 provenance、confidence、consolidation、冲突与生命周期 policy 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [AIP: A Graph Representation for Learning and Governing Agent Skills](https://arxiv.org/abs/2606.04781v1)

`arXiv:2606.04781v1`，§3 Agent Instruction Protocol；把 free-form skill 拆成 graph nodes/edges、preconditions 与 execution/governance metadata。 §4.5 Limitations；单一 benchmark、agent harness 与 graph authoring cost 不能证明所有 skill 可结构化或自动治理。 Books 复核为`已有覆盖`，owner=`AGENT-PLATFORM`；capability registry、typed precondition、version/release 与 policy ownership 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_01.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_01.md)。

### [Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents](https://arxiv.org/abs/2606.04815v1)

`arXiv:2606.04815v1`，§3.1 online lifelong formulation、§3.3 verifier-guided skill learning 与 §3.4 online skill internalization；把 action feedback、skill store 与 test-time policy 更新连成闭环。 §5 Conclusions and Further Work；指定 environments/verifier 的改善不证明开放世界长期安全，也未消除 skill poisoning、遗忘和回滚成本。 Books 复核为`已有覆盖`，owner=`AGENT-MEMORY`；skill write/read、verifier、online update 与 release/fallback 边界已有正文。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [Channel Fracture: Three Instances of Cross-Boundary Silent Delivery Reliability Failures in Multi-Agent Systems](https://arxiv.org/abs/2606.04896v1)

`arXiv:2606.04896v1`，§3 三种 injection channels/root-cause/fracture pattern 与 §4 CADVP v1.1；关键机制是 receiver-visible confirmation，而不是 writer-side success。 §5 Discussion；只有一个 Hermes/Holographic-memory 实现族和三种通道，不能推为所有多 Agent runtime 的发生率或完整协议。 Books 复核为`已有覆盖`，owner=`AGENT-MULTI-AGENT`；现有跨 Agent handoff、delivery acknowledgement、receiver verification 与 fallback 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [Audio Interaction Model](https://arxiv.org/abs/2606.05121v1)

`arXiv:2606.05121v1`，§3 always-on perceive–decide–respond、streaming construction/training 与 asynchronous FIFO inference；把 continuous audio 的 state 与 scheduling contract 显式化。 exact-v1 未定位独立 Limitations 章节；边界由作者披露的 audio models/dataset/benchmarks 推得，FIFO 稳定性不等于任意设备、噪声、延迟和 barge-in SLO 已满足。Books 复核为`已有覆盖`，owner=`MULTIMODAL-REPRESENTATION`（系统调度 handoff 至 inference owner）；流式 chunk/state、异步调度与端到端验收边界已有正文链。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [Streaming Communication in Multi-Agent Reasoning](https://arxiv.org/abs/2606.05158v1)

`arXiv:2606.05158v1`，§3 step streaming algorithm、effectiveness/efficiency characterization；下游 Agent 在上游完整结束前消费经验证的 reasoning step。 §6 Limitation；数学推理 benchmarks、commercial backbones 与固定 topology 不证明任意异步依赖或 tool workflow 保持正确。 Books 复核为`已有覆盖`，owner=`AGENT-MULTI-AGENT`；streaming handoff、partial-state provenance、backpressure 与 correction authority 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [Discourse-Role Labels as Presentation-Time Variables for Context Use in Language Models](https://arxiv.org/abs/2606.04109v1)

`arXiv:2606.04109v1`，§3 framework/methodology；content-fixed paired variants 隔离 Reference/Evidence/Instruction/Example 标签对 context adoption 的影响。 §7；模型、语言、短答案 probe 与 presentation setting 的边界不等于完整 RAG pipeline 效果。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；现有 prompt/template versioning、paired control 与 context-conflict evaluation 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?](https://arxiv.org/abs/2606.04455v1)

`arXiv:2606.04455v1`，§3 formulation、protocol、sandboxed evaluation architecture 与 integrity；将 agent-building artifact、开发预算和 unseen test 分离。 结果受 task suite、API/time budgets、Harbor sandbox 与 evaluator 实现限制，不能证明自主 agent development 的开放世界能力。 Books 复核为`Only report`，route=`PLATFORM-EVALUATION-SYSTEM`；它是有用的 benchmark contract，但未改变当前通用评测 owner。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [QO-Bench: Diagnosing Query-Operator-Preserving Retrieval over Typed Event Tuples](https://arxiv.org/abs/2606.04646v1)

`arXiv:2606.04646v1`，§3 denotational retrieval、operator preservation/execution 与 tractable subclass；把 filter/intersection/join preservation 与回答分离验收。 独立 Limitations；financial-event tuple schema、derived gold 与模板集合不代表所有开放文本 query。 Books 复核为`已有覆盖`，owner=`AGENT-RAG`；retrieval recall、operator semantics、structured execution 与 answer verification 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models](https://arxiv.org/abs/2606.04739v1)

`arXiv:2606.04739v1`，§3 Vul-RAG reconstruction 与 §4 dataset/models/metrics/implementation；贡献是对既有结果的复验边界。 垂直 vulnerability dataset/model slice 不能外推为一般 RAG，且复现失败只约束原 claim 所列设置。 Books 复核为`Only report`，route=`PLATFORM-EVALUATION-SYSTEM`；用于提醒复现与开放权重基线，不形成独立长期机制增量。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?](https://arxiv.org/abs/2606.05080v1)

`arXiv:2606.05080v1`，§2 task formulation/construction/composition 与 Appendix A scoring anchors/gates；以可执行 artifact 和长时迭代状态验收，而非单轮答案。 独立 Limitations and Broader Impact；32 个系统/CUDA/model tasks 与 harness 资源限制不代表真实科研自主性或安全部署。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；现有长程 task、artifact gate、cost/failure taxonomy 与 harness ablation 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [Failed Reasoning Traces Tell You What Is Fixable (But Not by Reading Them)](https://arxiv.org/abs/2606.05145v1)

`arXiv:2606.05145v1`，§2 operator-class setup/features/recoverability regimes，§3 routing test-time compute，§4 prospective routing policy；用可操作性而非语言解释分配重试。 §9；problem-unit、operator class、temperature 与 backbone 的边界不证明任意 reasoning failure 可被观测或修复。 Books 复核为`已有覆盖`，owner=`INFER-SCHEDULING`（相邻 Evaluation）；failure-aware compute routing、budget 与 fallback 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [Beyond Single-Policy: Evaluating Composed Organization-Specific Policy Alignment in LLM Chatbots](https://arxiv.org/abs/2606.04394v1)

`arXiv:2606.04394v1`，§3 grounding、composition、query generation 与 policy-handling evaluation；将多条组织 policy 的冲突/组合变成测试对象。 独立 Limitations；30 worlds、synthetic compositions 与 judge 不能代表全部真实制度冲突或法律正确性。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`（相邻 Security）；policy composition、冲突矩阵与多层验收已有机制。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [MemoryDocDataSet: A Benchmark for Joint Conversational Memory and Long Document Reasoning](https://arxiv.org/abs/2606.04442v1)

`arXiv:2606.04442v1`，§3 micro-world/source-dimension benchmark 与 §4 six-stage collection/verification pipeline；显式区分 conversation-only、document-only 与 hybrid evidence。 synthetic micro-worlds、50 worlds/1000 QA 和自动生成 pipeline 不能证明真实长期会话的隐私、更新与噪声边界。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`（相邻 `AGENT-MEMORY`）；source-dimension、hybrid evidence 与检索分层验收已有正文。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [Benchmarking Living-Screen-Native GUI Agents on Short-Video Platforms](https://arxiv.org/abs/2606.04701v1)

`arXiv:2606.04701v1`，§3 continuous evolving state、agent-initiated observation、task construction 与 accuracy/efficiency metrics。 独立 Limitations；short-video platform replica、语言/文化与 annotation scale 使结果不能外推至全部 GUI environments。Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；Ch66“Judge 从被动 Scorer 演进为有预算的 Evidence Acquisition Policy”与 Living-world Evaluation/Run Identity 已覆盖动态观察预算、环境推进与运行身份。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [Auditing CoT Answer-Hijack Patches: Source-Control Certificates with Type-I Guarantees](https://arxiv.org/abs/2606.04717v1)

`arXiv:2606.04717v1`，§3 K-shot layer disruption、recovery/spread metrics、pre-specified diagnostics；通过 paired source controls 区分 patch 来源与答案恢复。 §10 明示两个 model families、主要 benchmark 与 white-box operator；不构成生产 patch defense 或通用因果证明。 Books 复核为`Only report`，route=`PLATFORM-EVALUATION-SYSTEM`；作为 activation-patching 审计案例，不新增通用系统机制。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

### [Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents](https://arxiv.org/abs/2606.04874v1)

`arXiv:2606.04874v1`，§3 task/data/metrics，把 decomposition、tool selection、constraints、broken tools 与 unsolvable tasks 分轴验收。 独立 Limitations；合成 robustness scenarios、tool catalog 与 judge 不能证明真实 workflow 的全部 side effects。 Books 复核为`已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；规划分轴、失败注入、不可解判定与 executable validation 已覆盖。完整 Method/Evaluation/Limitations 记录见 [V3_EVIDENCE_BATCH_02.md](../_sources/daily-20260604/V3_EVIDENCE_BATCH_02.md)。

## 5. 缺口与下一步

1. 报告侧 Candidate、Evidence 与 Books proposal 已闭合：65/65，exact-v1 blocker 为 0；575 个 arXiv identity=64 Candidate+511 Close，另有 1 个厂商 release Candidate。
2. Books 写回：EvalStop 已写入 `TRAIN-RLHF`/Ch31，并通过非作者 post-write audit；UltraEP 在 Books 全库中无正文或 trace 残留。其余为 55 项已有覆盖、9 项仅报告。
3. 2606.04071 已改判 `已有覆盖`，Ch72 Review notes 后的旧 adoption trace 已精确删除；本日没有剩余 Books 写回或清理队列。
4. 终态保留项：OpenAI Dreaming 页面只披露 `2026-06-04`，缺原始发布时刻，无法唯一判断属于 06-04 还是 06-05 的 09:00 截点。该日期缺口已隔离，不计分、不支持正面证据、Candidate、Books 或无遗漏断言；仅在取得原始时间戳时定点重开。

## 6. 复核

复核者：JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md（非作者 denominator/Books proposal）与本次非作者 post-write fresh audit
结论：通过

非作者复核累计纠正 9 个 false positive（含 UltraEP withdrawal），冻结 575 个 arXiv identity = 64 Candidate + 511 Close；厂商源另有 1 个 release Candidate。报告侧 Evidence 65/65、Books Decision 65/65、exact-v1 blocker 0。2606.04071/04929 为 Existing，2606.04145 已真实写入 Ch31 并通过 post-write audit，UltraEP Books residue 为 0，2606.04071 的旧 adoption trace 已清除。Dreaming 的发布时刻缺口已隔离；其余分母、Evidence、Books 与 post-write Gate 均闭合。
