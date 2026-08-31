# 2026-06-25 Ready-to-Insert Books Packet V1

Status: Applied. 每个 Source Family 只进入一个 owner；正文和 Review note 均绑定 exact-v1。

## `AGENT-MCP` → `books/part-07-agent/83-mcp.md`

### SF-2026-ARXIV-2606-26211

### 2606.26211 — Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem

**问题与旧路径。** NANDini (Networked Agents Natural Distillation of Interconnected Nodal Intelligence) envisions an automated ecosystem where intelligent agents independently create, process, and exchange data to drive decisions at scale.

**机制、状态与控制流。** `Data Facts metadata schema; provenance, semantics, constraints and exchange contract` 所定义的源特定机制用于以带 provenance、语义和约束的 Data Facts 作为跨 Agent 交换契约；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness` 是 `Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `NANDini multi-agent exchange examples and schema coverage` 的验证域，`AGENT-MCP` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26211:start -->
Claim boundary：仅 `arXiv:2606.26211v1`；未证明边界定位 `https://arxiv.org/html/2606.26211v1 — §Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness`。
<!-- claim:SF-2026-ARXIV-2606-26211:end -->

Review note：`SF-2026-ARXIV-2606-26211`；Method `https://arxiv.org/html/2606.26211v1 — §Data Facts metadata schema; provenance, semantics, constraints and exchange contract`；Evaluation `https://arxiv.org/html/2606.26211v1 — §NANDini multi-agent exchange examples and schema coverage`；未证明边界 `https://arxiv.org/html/2606.26211v1 — §Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness`。

## `AGENT-MEMORY` → `books/part-07-agent/77-memory.md`

### SF-2026-ARXIV-2606-25449

### 2606.25449 — Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One

**问题与旧路径。** A language model's memory can be worse than no memory at all when the model or its interface is disposed to act on it: a memory that keeps a wrong conclusion but drops the work behind it leads a model to re-emit the stale value as a confident answer, where an empty memory leads it to abstain.

**机制、状态与控制流。** `3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Limitations` 是 `Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25449:start -->
Claim boundary：仅 `arXiv:2606.25449v1`；未证明边界定位 `https://arxiv.org/html/2606.25449v1 — §7 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25449:end -->

Review note：`SF-2026-ARXIV-2606-25449`；Method `https://arxiv.org/html/2606.25449v1 — §3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol`；Evaluation `https://arxiv.org/html/2606.25449v1 — §4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix`；未证明边界 `https://arxiv.org/html/2606.25449v1 — §7 Limitations`。

### SF-2026-ARXIV-2606-25658

### 2606.25658 — Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding

**问题与旧路径。** Currently, streaming video understanding is still a daunting task for existing \emph{multimodal large language models} (MLLMs).

**机制、状态与控制流。** `3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `A Limitations` 是 `Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25658:start -->
Claim boundary：仅 `arXiv:2606.25658v1`；未证明边界定位 `https://arxiv.org/html/2606.25658v1 — §A Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25658:end -->

Review note：`SF-2026-ARXIV-2606-25658`；Method `https://arxiv.org/html/2606.25658v1 — §3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank`；Evaluation `https://arxiv.org/html/2606.25658v1 — §4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation`；未证明边界 `https://arxiv.org/html/2606.25658v1 — §A Limitations`。

## `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md`

### SF-2026-ARXIV-2606-25514

### 2606.25514 — Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution

**问题与旧路径。** Resolving issues with ambiguous and incomplete descriptions, particularly concerning complex bugs, requires a sophisticated, long-horizon workflow.

**机制、状态与控制流。** `2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication` 所定义的源特定机制用于把事件通信、角色分工与失败升级纳入多 Agent 协调状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `5 Threats to Validity` 是 `Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution` 的 source-specific 反例/局限边界；若运行条件离开 `3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures` 的验证域，`AGENT-MULTI-AGENT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25514:start -->
Claim boundary：仅 `arXiv:2606.25514v1`；未证明边界定位 `https://arxiv.org/html/2606.25514v1 — §5 Threats to Validity`。
<!-- claim:SF-2026-ARXIV-2606-25514:end -->

Review note：`SF-2026-ARXIV-2606-25514`；Method `https://arxiv.org/html/2606.25514v1 — §2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication`；Evaluation `https://arxiv.org/html/2606.25514v1 — §3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures`；未证明边界 `https://arxiv.org/html/2606.25514v1 — §5 Threats to Validity`。

## `AGENT-PLANNING` → `books/part-07-agent/79-planning.md`

### SF-2026-ARXIV-2606-25274

### 2606.25274 — UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control

**问题与旧路径。** Time-series deployments often need delayed feasible decisions, not only accurate forecasts.

**机制、状态与控制流。** `3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Limitations` 是 `UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Implemented Evidence; 6 Analysis` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25274:start -->
Claim boundary：仅 `arXiv:2606.25274v1`；未证明边界定位 `https://arxiv.org/html/2606.25274v1 — §7 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25274:end -->

Review note：`SF-2026-ARXIV-2606-25274`；Method `https://arxiv.org/html/2606.25274v1 — §3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam`；Evaluation `https://arxiv.org/html/2606.25274v1 — §5 Experiments; 5.1 Implemented Evidence; 6 Analysis`；未证明边界 `https://arxiv.org/html/2606.25274v1 — §7 Limitations`。

### SF-2026-ARXIV-2606-26463

### 2606.26463 — Finding the Time to Think: Learning Planning Budgets in Real-Time RL

**问题与旧路径。** Deliberating takes time.

**机制、状态与控制流。** `Variable-delay real-time RL; lightweight gate selects state-dependent planning budget` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Game planners and timing model do not prove benefit under production tool latency or safety deadlines` 是 `Finding the Time to Think: Learning Planning Budgets in Real-Time RL` 的 source-specific 反例/局限边界；若运行条件离开 `Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26463:start -->
Claim boundary：仅 `arXiv:2606.26463v1`；未证明边界定位 `https://arxiv.org/html/2606.26463v1 — §Game planners and timing model do not prove benefit under production tool latency or safety deadlines`。
<!-- claim:SF-2026-ARXIV-2606-26463:end -->

Review note：`SF-2026-ARXIV-2606-26463`；Method `https://arxiv.org/html/2606.26463v1 — §Variable-delay real-time RL; lightweight gate selects state-dependent planning budget`；Evaluation `https://arxiv.org/html/2606.26463v1 — §Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation`；未证明边界 `https://arxiv.org/html/2606.26463v1 — §Game planners and timing model do not prove benefit under production tool latency or safety deadlines`。

## `AGENT-PROMPT` → `books/part-07-agent/74-prompt.md`

### SF-2026-ARXIV-2606-26356

### 2606.26356 — Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems

**问题与旧路径。** Practitioners of prompt-composed agentic systems report a recurring failure mode: editing one prompt module silently shifts the behavior of others despite no shared variable or executable dependency.

**机制、状态与控制流。** `Instruction Bleed formulation; prompt-composed module interference` 所定义的源特定机制用于把模块间指令干扰作为可测试的组合边界，而非默认隔离；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Prompt/module families tested do not establish universal isolation or adversarial robustness` 是 `Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-module interference experiments and mitigations` 的验证域，`AGENT-PROMPT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26356:start -->
Claim boundary：仅 `arXiv:2606.26356v1`；未证明边界定位 `https://arxiv.org/html/2606.26356v1 — §Prompt/module families tested do not establish universal isolation or adversarial robustness`。
<!-- claim:SF-2026-ARXIV-2606-26356:end -->

Review note：`SF-2026-ARXIV-2606-26356`；Method `https://arxiv.org/html/2606.26356v1 — §Instruction Bleed formulation; prompt-composed module interference`；Evaluation `https://arxiv.org/html/2606.26356v1 — §Cross-module interference experiments and mitigations`；未证明边界 `https://arxiv.org/html/2606.26356v1 — §Prompt/module families tested do not establish universal isolation or adversarial robustness`。

## `AGENT-RAG` → `books/part-07-agent/76-rag.md`

### SF-2026-ARXIV-2606-25656

### 2606.25656 — Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization

**问题与旧路径。** As advanced RAG variants like GraphRAG and Agentic RAG emerge, one leading question is when and how to use them.

**机制、状态与控制流。** `3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Conclusions and future work; C Retrieval-Generation Gap` 是 `Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental setup; 5 Experimental results` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25656:start -->
Claim boundary：仅 `arXiv:2606.25656v1`；未证明边界定位 `https://arxiv.org/html/2606.25656v1 — §6 Conclusions and future work; C Retrieval-Generation Gap`。
<!-- claim:SF-2026-ARXIV-2606-25656:end -->

Review note：`SF-2026-ARXIV-2606-25656`；Method `https://arxiv.org/html/2606.25656v1 — §3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization`；Evaluation `https://arxiv.org/html/2606.25656v1 — §4 Experimental setup; 5 Experimental results`；未证明边界 `https://arxiv.org/html/2606.25656v1 — §6 Conclusions and future work; C Retrieval-Generation Gap`。

### SF-2026-ARXIV-2606-25674

### 2606.25674 — BitNet Text Embeddings

**问题与旧路径。** LLM-based text embedders have substantially improved retrieval and semantic representation quality, but their deployment remains costly: large backbone models slow down embedding inference, while high-dimensional full-precision embeddings impose substantial storage and bandwidth overhead on large-scale indexes.

**机制、状态与控制流。** `3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `4.4 Analysis; task-type sensitivity to quantization` 是 `BitNet Text Embeddings` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; B Evaluation Details` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25674:start -->
Claim boundary：仅 `arXiv:2606.25674v1`；未证明边界定位 `https://arxiv.org/html/2606.25674v1 — §4.4 Analysis; task-type sensitivity to quantization`。
<!-- claim:SF-2026-ARXIV-2606-25674:end -->

Review note：`SF-2026-ARXIV-2606-25674`；Method `https://arxiv.org/html/2606.25674v1 — §3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization`；Evaluation `https://arxiv.org/html/2606.25674v1 — §4 Experiments; 4.1 Experimental Setup; B Evaluation Details`；未证明边界 `https://arxiv.org/html/2606.25674v1 — §4.4 Analysis; task-type sensitivity to quantization`。

### SF-2026-ARXIV-2606-26439

### 2606.26439 — TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization

**问题与旧路径。** Multi-vector retrieval models such as ColBERT achieve state-of-the-art accuracy through fine-grained token-level MaxSim scoring, yet existing GPU implementations leave most hardware performance unused.

**机制、状态与控制流。** `TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved` 是 `TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization` 的 source-specific 反例/局限边界；若运行条件离开 `GPU retrieval throughput, latency and quality evaluation` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26439:start -->
Claim boundary：仅 `arXiv:2606.26439v1`；未证明边界定位 `https://arxiv.org/html/2606.26439v1 — §Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved`。
<!-- claim:SF-2026-ARXIV-2606-26439:end -->

Review note：`SF-2026-ARXIV-2606-26439`；Method `https://arxiv.org/html/2606.26439v1 — §TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization`；Evaluation `https://arxiv.org/html/2606.26439v1 — §GPU retrieval throughput, latency and quality evaluation`；未证明边界 `https://arxiv.org/html/2606.26439v1 — §Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved`。

### SF-2026-ARXIV-2606-26441

### 2606.26441 — GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices

**问题与旧路径。** Learned sparse retrieval models such as SPLADE achieve retrieval quality competitive with dense models while preserving the interpretability and exact-match advantages of sparse representations.

**机制、状态与控制流。** `GPUSparse learned sparse retrieval with parallel inverted indices` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling` 是 `GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices` 的 source-specific 反例/局限边界；若运行条件离开 `Retrieval quality, latency and GPU scaling experiments` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26441:start -->
Claim boundary：仅 `arXiv:2606.26441v1`；未证明边界定位 `https://arxiv.org/html/2606.26441v1 — §Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling`。
<!-- claim:SF-2026-ARXIV-2606-26441:end -->

Review note：`SF-2026-ARXIV-2606-26441`；Method `https://arxiv.org/html/2606.26441v1 — §GPUSparse learned sparse retrieval with parallel inverted indices`；Evaluation `https://arxiv.org/html/2606.26441v1 — §Retrieval quality, latency and GPU scaling experiments`；未证明边界 `https://arxiv.org/html/2606.26441v1 — §Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling`。

## `AGENT-TOOL-CALLING` → `books/part-07-agent/78-tool-calling.md`

### SF-2026-ARXIV-2606-25605

### 2606.25605 — Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints

**问题与旧路径。** Tool Calling and Structured Output are two core capabilities of modern Agent systems, yet their interaction under joint deployment conditions remains insufficiently understood.

**机制、状态与控制流。** `3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7.5 Failure Cases and Limitations; 8.4 Limitations` 是 `Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25605:start -->
Claim boundary：仅 `arXiv:2606.25605v1`；未证明边界定位 `https://arxiv.org/html/2606.25605v1 — §7.5 Failure Cases and Limitations; 8.4 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25605:end -->

Review note：`SF-2026-ARXIV-2606-25605`；Method `https://arxiv.org/html/2606.25605v1 — §3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution`；Evaluation `https://arxiv.org/html/2606.25605v1 — §5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency`；未证明边界 `https://arxiv.org/html/2606.25605v1 — §7.5 Failure Cases and Limitations; 8.4 Limitations`。

### SF-2026-ARXIV-2606-25705

### 2606.25705 — GUI agent: Guided Exploration of User-Sensitive Screens

**问题与旧路径。** LLM agents are increasingly being used to automate tasks for users within an open GUI environment.

**机制、状态与控制流。** `3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `5 Conclusion; short-paper and emulator-only boundary` 是 `GUI agent: Guided Exploration of User-Sensitive Screens` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Results` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25705:start -->
Claim boundary：仅 `arXiv:2606.25705v1`；未证明边界定位 `https://arxiv.org/html/2606.25705v1 — §5 Conclusion; short-paper and emulator-only boundary`。
<!-- claim:SF-2026-ARXIV-2606-25705:end -->

Review note：`SF-2026-ARXIV-2606-25705`；Method `https://arxiv.org/html/2606.25705v1 — §3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator`；Evaluation `https://arxiv.org/html/2606.25705v1 — §4 Experiments and Results`；未证明边界 `https://arxiv.org/html/2606.25705v1 — §5 Conclusion; short-paper and emulator-only boundary`。

### SF-2026-ARXIV-2606-25819

### 2606.25819 — Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability

**问题与旧路径。** Large language models are increasingly deployed as agents that solve tasks by interacting with external tool environments.

**机制、状态与控制流。** `ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Canonical recovery-path construction and five injected-hazard boundary` 是 `Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Experimental Setup; Further Analysis; Error Analysis` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25819:start -->
Claim boundary：仅 `arXiv:2606.25819v1`；未证明边界定位 `https://arxiv.org/html/2606.25819v1 — §Canonical recovery-path construction and five injected-hazard boundary`。
<!-- claim:SF-2026-ARXIV-2606-25819:end -->

Review note：`SF-2026-ARXIV-2606-25819`；Method `https://arxiv.org/html/2606.25819v1 — §ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection`；Evaluation `https://arxiv.org/html/2606.25819v1 — §Experiments; Experimental Setup; Further Analysis; Error Analysis`；未证明边界 `https://arxiv.org/html/2606.25819v1 — §Canonical recovery-path construction and five injected-hazard boundary`。

### SF-2026-ARXIV-2606-25987

### 2606.25987 — Weave of Formal Thought

**问题与旧路径。** Large language models (LLMs) attain remarkable surface fluency on code, yet they neither formally guarantee the syntactic validity of their output nor leverage the hierarchical structure defining the target language.

**机制、状态与控制流。** `3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Next Steps and Research Vision; technical-report preliminary-results boundary` 是 `Weave of Formal Thought` 的 source-specific 反例/局限边界；若运行条件离开 `5 WoFT Improves Surface Modeling; 5.1 Experimental setup` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25987:start -->
Claim boundary：仅 `arXiv:2606.25987v1`；未证明边界定位 `https://arxiv.org/html/2606.25987v1 — §6 Next Steps and Research Vision; technical-report preliminary-results boundary`。
<!-- claim:SF-2026-ARXIV-2606-25987:end -->

Review note：`SF-2026-ARXIV-2606-25987`；Method `https://arxiv.org/html/2606.25987v1 — §3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought`；Evaluation `https://arxiv.org/html/2606.25987v1 — §5 WoFT Improves Surface Modeling; 5.1 Experimental setup`；未证明边界 `https://arxiv.org/html/2606.25987v1 — §6 Next Steps and Research Vision; technical-report preliminary-results boundary`。

## `AGENT-WORKFLOW` → `books/part-07-agent/81-workflow.md`

### SF-2026-ARXIV-2606-25447

### 2606.25447 — The Interplay of Harness Design and Post-Training in LLM Agents

**问题与旧路径。** Tool-integrated LLM agents are often wrapped within a harness: the scaffolding that determines which tools are exposed, how they are described, and what auxiliary information accompanies each per-step observation.

**机制、状态与控制流。** `3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `B Benchmark Details; C Experimental Details; stated ALFWorld boundary` 是 `The Interplay of Harness Design and Post-Training in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25447:start -->
Claim boundary：仅 `arXiv:2606.25447v1`；未证明边界定位 `https://arxiv.org/html/2606.25447v1 — §B Benchmark Details; C Experimental Details; stated ALFWorld boundary`。
<!-- claim:SF-2026-ARXIV-2606-25447:end -->

Review note：`SF-2026-ARXIV-2606-25447`；Method `https://arxiv.org/html/2606.25447v1 — §3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type`；Evaluation `https://arxiv.org/html/2606.25447v1 — §4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness`；未证明边界 `https://arxiv.org/html/2606.25447v1 — §B Benchmark Details; C Experimental Details; stated ALFWorld boundary`。

### SF-2026-ARXIV-2606-26442

### 2606.26442 — AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities

**问题与旧路径。** We present AXLE (Axiom Lean Engine), a cloud service for Lean 4 proof manipulation, extraction, and verification.

**机制、状态与控制流。** `AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety` 是 `AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities` 的 source-specific 反例/局限边界；若运行条件离开 `Utility execution, throughput and theorem-proving workflow evaluation` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26442:start -->
Claim boundary：仅 `arXiv:2606.26442v1`；未证明边界定位 `https://arxiv.org/html/2606.26442v1 — §Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety`。
<!-- claim:SF-2026-ARXIV-2606-26442:end -->

Review note：`SF-2026-ARXIV-2606-26442`；Method `https://arxiv.org/html/2606.26442v1 — §AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling`；Evaluation `https://arxiv.org/html/2606.26442v1 — §Utility execution, throughput and theorem-proving workflow evaluation`；未证明边界 `https://arxiv.org/html/2606.26442v1 — §Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety`。

## `INFER-GPU-MEMORY` → `books/part-05-inference-system/54-gpu-memory.md`

### SF-2026-ARXIV-2606-25285

### 2606.25285 — EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression

**问题与旧路径。** Post-Training Sparsity (PTS) has emerged as a crucial paradigm for compressing Large Language Models to facilitate efficient deployment on resource-constrained devices.

**机制、状态与控制流。** `3 EPTS: Elastic Post-Training Sparsity` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Limitations and Discussion` 是 `EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; Experimental Setup; Main Results` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25285:start -->
Claim boundary：仅 `arXiv:2606.25285v1`；未证明边界定位 `https://arxiv.org/html/2606.25285v1 — §Limitations and Discussion`。
<!-- claim:SF-2026-ARXIV-2606-25285:end -->

Review note：`SF-2026-ARXIV-2606-25285`；Method `https://arxiv.org/html/2606.25285v1 — §3 EPTS: Elastic Post-Training Sparsity`；Evaluation `https://arxiv.org/html/2606.25285v1 — §4 Experiments; Experimental Setup; Main Results`；未证明边界 `https://arxiv.org/html/2606.25285v1 — §Limitations and Discussion`。

### SF-2026-ARXIV-2606-25519

### 2606.25519 — Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models

**问题与旧路径。** Quantization is widely used to reduce the inference cost of large language models, but its effect on reasoning models is not fully captured by final-answer accuracy or per-token latency.

**机制、状态与控制流。** `3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Can We Reduce Reasoning-Token Inflation; D.2 Model details` 是 `Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models` 的 source-specific 反例/局限边界；若运行条件离开 `D Additional evaluation details; D.1 Benchmarks and evaluation protocol` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25519:start -->
Claim boundary：仅 `arXiv:2606.25519v1`；未证明边界定位 `https://arxiv.org/html/2606.25519v1 — §7 Can We Reduce Reasoning-Token Inflation; D.2 Model details`。
<!-- claim:SF-2026-ARXIV-2606-25519:end -->

Review note：`SF-2026-ARXIV-2606-25519`；Method `https://arxiv.org/html/2606.25519v1 — §3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy`；Evaluation `https://arxiv.org/html/2606.25519v1 — §D Additional evaluation details; D.1 Benchmarks and evaluation protocol`；未证明边界 `https://arxiv.org/html/2606.25519v1 — §7 Can We Reduce Reasoning-Token Inflation; D.2 Model details`。

### SF-2026-ARXIV-2606-26488

### 2606.26488 — What Survives When You Compress a Recursive Reasoner for the Edge?

**问题与旧路径。** Recursive reasoning models can solve complex structured tasks with only a few million parameters by repeatedly updating a latent state.

**机制、状态与控制流。** `Compression of recursive reasoners across precision, pruning, distillation and attention variants` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Edge recursive models only; token-level preservation does not imply global-reasoning preservation` 是 `What Survives When You Compress a Recursive Reasoner for the Edge?` 的 source-specific 反例/局限边界；若运行条件离开 `Three tasks and two recursive architectures; local vs puzzle-exact accuracy` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26488:start -->
Claim boundary：仅 `arXiv:2606.26488v1`；未证明边界定位 `https://arxiv.org/html/2606.26488v1 — §Edge recursive models only; token-level preservation does not imply global-reasoning preservation`。
<!-- claim:SF-2026-ARXIV-2606-26488:end -->

Review note：`SF-2026-ARXIV-2606-26488`；Method `https://arxiv.org/html/2606.26488v1 — §Compression of recursive reasoners across precision, pruning, distillation and attention variants`；Evaluation `https://arxiv.org/html/2606.26488v1 — §Three tasks and two recursive architectures; local vs puzzle-exact accuracy`；未证明边界 `https://arxiv.org/html/2606.26488v1 — §Edge recursive models only; token-level preservation does not imply global-reasoning preservation`。

## `INFER-KV-CACHE` → `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`

### SF-2026-ARXIV-2606-26472

### 2606.26472 — Epiphany-Aware KV Cache Eviction Without the Attention Matrix

**问题与旧路径。** As reasoning models emit chains of thought tens of thousands of tokens long, KV cache increasingly becomes a deployment bottleneck.

**机制、状态与控制流。** `Epiphany score from forward-pass representation change; attention-matrix-free eviction` 所定义的源特定机制用于以表征变化分数驱动逐 token KV 驱逐，并保留完整 KV 回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback` 是 `Epiphany-Aware KV Cache Eviction Without the Attention Matrix` 的 source-specific 反例/局限边界；若运行条件离开 `Long-reasoning cache/quality evaluation and 16x feasible-context claim` 的验证域，`INFER-KV-CACHE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26472:start -->
Claim boundary：仅 `arXiv:2606.26472v1`；未证明边界定位 `https://arxiv.org/html/2606.26472v1 — §Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback`。
<!-- claim:SF-2026-ARXIV-2606-26472:end -->

Review note：`SF-2026-ARXIV-2606-26472`；Method `https://arxiv.org/html/2606.26472v1 — §Epiphany score from forward-pass representation change; attention-matrix-free eviction`；Evaluation `https://arxiv.org/html/2606.26472v1 — §Long-reasoning cache/quality evaluation and 16x feasible-context claim`；未证明边界 `https://arxiv.org/html/2606.26472v1 — §Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback`。

## `INFER-PREFILL` → `books/part-05-inference-system/43-prefill.md`

### SF-2026-ARXIV-2606-25353

### 2606.25353 — Cache-Resident LLM Inference in GB-Scale Last-Level Caches

**问题与旧路径。** Large language model (LLM) inference is increasingly dominated by data movement across the memory hierarchy.

**机制、状态与控制流。** `3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `7 Discussion; 7.2 Future Works` 是 `Cache-Resident LLM Inference in GB-Scale Last-Level Caches` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiment Setup; 6 Evaluation` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25353:start -->
Claim boundary：仅 `arXiv:2606.25353v1`；未证明边界定位 `https://arxiv.org/html/2606.25353v1 — §7 Discussion; 7.2 Future Works`。
<!-- claim:SF-2026-ARXIV-2606-25353:end -->

Review note：`SF-2026-ARXIV-2606-25353`；Method `https://arxiv.org/html/2606.25353v1 — §3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation`；Evaluation `https://arxiv.org/html/2606.25353v1 — §5 Experiment Setup; 6 Evaluation`；未证明边界 `https://arxiv.org/html/2606.25353v1 — §7 Discussion; 7.2 Future Works`。

### SF-2026-ARXIV-2606-25426

### 2606.25426 — Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX

**问题与旧路径。** On Apple Silicon the fp32 GEMMs dominating LLM prefill are dispatched by Accelerate to a matrix coprocessor (AMX) on the M1-M3.

**机制、状态与控制流。** `3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Conclusion; Limitations` 是 `Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX` 的 source-specific 反例/局限边界；若运行条件离开 `4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25426:start -->
Claim boundary：仅 `arXiv:2606.25426v1`；未证明边界定位 `https://arxiv.org/html/2606.25426v1 — §6 Conclusion; Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25426:end -->

Review note：`SF-2026-ARXIV-2606-25426`；Method `https://arxiv.org/html/2606.25426v1 — §3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing`；Evaluation `https://arxiv.org/html/2606.25426v1 — §4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement`；未证明边界 `https://arxiv.org/html/2606.25426v1 — §6 Conclusion; Limitations`。

## `INFER-REQUEST-LIFECYCLE` → `books/part-05-inference-system/42-what-happens-during-inference.md`

### SF-2026-ARXIV-2606-25838

### 2606.25838 — Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines

**问题与旧路径。** Production vision pipelines silently degrade on blurry input, wasting compute on downstream OCR, retrieval, and vision-language model (VLM) calls that cannot recover a usable output.

**机制、状态与控制流。** `III Method; IV Confidence-Aware Routing` 所定义的源特定机制用于让路由器基于请求置信度持有后端选择与回退权；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VII-C Limitations and future work` 是 `Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments; V-A Evaluation protocol; VI Deployment Patterns` 的验证域，`INFER-REQUEST-LIFECYCLE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25838:start -->
Claim boundary：仅 `arXiv:2606.25838v1`；未证明边界定位 `https://arxiv.org/html/2606.25838v1 — §VII-C Limitations and future work`。
<!-- claim:SF-2026-ARXIV-2606-25838:end -->

Review note：`SF-2026-ARXIV-2606-25838`；Method `https://arxiv.org/html/2606.25838v1 — §III Method; IV Confidence-Aware Routing`；Evaluation `https://arxiv.org/html/2606.25838v1 — §V Experiments; V-A Evaluation protocol; VI Deployment Patterns`；未证明边界 `https://arxiv.org/html/2606.25838v1 — §VII-C Limitations and future work`。

## `INFER-SCHEDULING` → `books/part-05-inference-system/56-inference-scheduling.md`

### SF-2026-ARXIV-2606-25467

### 2606.25467 — RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs

**问题与旧路径。** Intent-driven edge services allow multiple virtual network function (VNF) segments in a service function chain directed acyclic graph (SFC-DAG) to be locally reordered without changing service semantics, creating richer request-side orchestration freedom.

**机制、状态与控制流。** `III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration` 所定义的源特定机制用于让在线编排器共同持有请求资源耦合、准入和降级状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications` 是 `RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`INFER-SCHEDULING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25467:start -->
Claim boundary：仅 `arXiv:2606.25467v1`；未证明边界定位 `https://arxiv.org/html/2606.25467v1 — §D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications`。
<!-- claim:SF-2026-ARXIV-2606-25467:end -->

Review note：`SF-2026-ARXIV-2606-25467`；Method `https://arxiv.org/html/2606.25467v1 — §III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration`；Evaluation `https://arxiv.org/html/2606.25467v1 — §V Experimental Evaluation; V-A Experimental Setup`；未证明边界 `https://arxiv.org/html/2606.25467v1 — §D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications`。

## `INFER-TENSORRT-LLM` → `books/part-05-inference-system/49-tensorrt-llm.md`

### SF-2026-ARXIV-2606-25453

### 2606.25453 — EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication

**问题与旧路径。** Modern GPUs devote an increasing silicon budget to low-precision matrix-multiplication units, widening the precision-throughput gap for scientific computing workloads.

**机制、状态与控制流。** `III EmuGEMM-I; IV EmuGEMM-II` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `V-G Limitations` 是 `EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication` 的 source-specific 反例/局限边界；若运行条件离开 `V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25453:start -->
Claim boundary：仅 `arXiv:2606.25453v1`；未证明边界定位 `https://arxiv.org/html/2606.25453v1 — §V-G Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25453:end -->

Review note：`SF-2026-ARXIV-2606-25453`；Method `https://arxiv.org/html/2606.25453v1 — §III EmuGEMM-I; IV EmuGEMM-II`；Evaluation `https://arxiv.org/html/2606.25453v1 — §V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off`；未证明边界 `https://arxiv.org/html/2606.25453v1 — §V-G Limitations`。

### SF-2026-ARXIV-2606-26344

### 2606.26344 — Axon: A Synthesizing Superoptimizer for Tensor Programs

**问题与旧路径。** Writing high performance kernels for AI accelerators requires deep expertise in tiling, instruction selection, data layout, and operator fusion placing a significant burden on programmers.

**机制、状态与控制流。** `Axon synthesizing superoptimizer; tensor-program search and verification` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence` 是 `Axon: A Synthesizing Superoptimizer for Tensor Programs` 的 source-specific 反例/局限边界；若运行条件离开 `Kernel synthesis evaluation and generated-program performance` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26344:start -->
Claim boundary：仅 `arXiv:2606.26344v1`；未证明边界定位 `https://arxiv.org/html/2606.26344v1 — §Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence`。
<!-- claim:SF-2026-ARXIV-2606-26344:end -->

Review note：`SF-2026-ARXIV-2606-26344`；Method `https://arxiv.org/html/2606.26344v1 — §Axon synthesizing superoptimizer; tensor-program search and verification`；Evaluation `https://arxiv.org/html/2606.26344v1 — §Kernel synthesis evaluation and generated-program performance`；未证明边界 `https://arxiv.org/html/2606.26344v1 — §Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence`。

### SF-2026-ARXIV-2606-26453

### 2606.26453 — Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization

**问题与旧路径。** We present KernelPro, a closed-loop multi-agent system that automatically generates, profiles, and iteratively optimizes GPU kernel code by integrating large language model (LLM) code generation with hardware profiler feedback and pluggable bottleneck detection tools.

**机制、状态与控制流。** `Micro-profiling tools as expert surrogates for LLM CUDA optimization` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback` 是 `Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-kernel correctness, profiling and speed evaluation` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26453:start -->
Claim boundary：仅 `arXiv:2606.26453v1`；未证明边界定位 `https://arxiv.org/html/2606.26453v1 — §Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback`。
<!-- claim:SF-2026-ARXIV-2606-26453:end -->

Review note：`SF-2026-ARXIV-2606-26453`；Method `https://arxiv.org/html/2606.26453v1 — §Micro-profiling tools as expert surrogates for LLM CUDA optimization`；Evaluation `https://arxiv.org/html/2606.26453v1 — §Generated-kernel correctness, profiling and speed evaluation`；未证明边界 `https://arxiv.org/html/2606.26453v1 — §Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback`。

## `MODEL-LONG-CONTEXT` → `books/part-02-model/22-long-context.md`

### SF-2026-ARXIV-2606-25342

### 2606.25342 — Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention

**问题与旧路径。** Lifelong continual learning remains an obstacle on the path to human-like intelligence.

**机制、状态与控制流。** `Parametric Attention and Lifelong In-Context Learning formulation` 所定义的源特定机制用于把跨段记忆从隐式上下文提升为可更新的长期参数状态，并由模型路径决定写入与读取；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Discussion; finite-memory and task-family limitations` 是 `Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Lifelong sequence results` 的验证域，`MODEL-LONG-CONTEXT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25342:start -->
Claim boundary：仅 `arXiv:2606.25342v1`；未证明边界定位 `https://arxiv.org/html/2606.25342v1 — §Discussion; finite-memory and task-family limitations`。
<!-- claim:SF-2026-ARXIV-2606-25342:end -->

Review note：`SF-2026-ARXIV-2606-25342`；Method `https://arxiv.org/html/2606.25342v1 — §Parametric Attention and Lifelong In-Context Learning formulation`；Evaluation `https://arxiv.org/html/2606.25342v1 — §Experiments; Lifelong sequence results`；未证明边界 `https://arxiv.org/html/2606.25342v1 — §Discussion; finite-memory and task-family limitations`。

## `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`

### SF-2026-ARXIV-2606-25575

### 2606.25575 — One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand

**问题与旧路径。** Assistive robotic systems face a fundamental trade-off: fully autonomous systems lack user agency, while fully user-controlled systems demand continuous cognitive effort.

**机制、状态与控制流。** `Variable-autonomy architecture; task-phase authority transfer; always-available release gesture` 所定义的源特定机制用于把任务阶段、共享自治等级和人工接管手势纳入动作控制回路；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Single wearable-hand embodiment, known objects, five tools, and short-horizon study` 是 `One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand` 的 source-specific 反例/局限边界；若运行条件离开 `44-participant user study; five bimanual tasks; policy-variant success` 的验证域，`MULTIMODAL-EMBODIED-VLA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25575:start -->
Claim boundary：仅 `arXiv:2606.25575v1`；未证明边界定位 `https://arxiv.org/html/2606.25575v1 — §Single wearable-hand embodiment, known objects, five tools, and short-horizon study`。
<!-- claim:SF-2026-ARXIV-2606-25575:end -->

Review note：`SF-2026-ARXIV-2606-25575`；Method `https://arxiv.org/html/2606.25575v1 — §Variable-autonomy architecture; task-phase authority transfer; always-available release gesture`；Evaluation `https://arxiv.org/html/2606.25575v1 — §44-participant user study; five bimanual tasks; policy-variant success`；未证明边界 `https://arxiv.org/html/2606.25575v1 — §Single wearable-hand embodiment, known objects, five tools, and short-horizon study`。

## `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md`

### SF-2026-ARXIV-2606-25487

### 2606.25487 — How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring

**问题与旧路径。** Almost every paper on LLM jailbreaks and prompt injection reports an attack-success rate (ASR), and that number is assigned not by people but by an automated judge: either a safety classifier trained for the task, or a general chat model prompted to grade.

**机制、状态与控制流。** `3 Setup; Appendix A Prompts, wrappers, and attack configuration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Limitations` 是 `How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring` 的 source-specific 反例/局限边界；若运行条件离开 `4 Results; 4.1 Calibration against human labels; 4.3 white-box attack` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25487:start -->
Claim boundary：仅 `arXiv:2606.25487v1`；未证明边界定位 `https://arxiv.org/html/2606.25487v1 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25487:end -->

Review note：`SF-2026-ARXIV-2606-25487`；Method `https://arxiv.org/html/2606.25487v1 — §3 Setup; Appendix A Prompts, wrappers, and attack configuration`；Evaluation `https://arxiv.org/html/2606.25487v1 — §4 Results; 4.1 Calibration against human labels; 4.3 white-box attack`；未证明边界 `https://arxiv.org/html/2606.25487v1 — §6 Limitations`。

### SF-2026-ARXIV-2606-25622

### 2606.25622 — Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz

**问题与旧路径。** The NIS-2 Directive mandates robust Risk Management from thousands of small and medium enterprises.

**机制、状态与控制流。** `IV Theoretical Framework: MAS Architecture and Experimental Setup` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VI Limitations & Future Work` 是 `Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `V Results & Discussion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25622:start -->
Claim boundary：仅 `arXiv:2606.25622v1`；未证明边界定位 `https://arxiv.org/html/2606.25622v1 — §VI Limitations & Future Work`。
<!-- claim:SF-2026-ARXIV-2606-25622:end -->

Review note：`SF-2026-ARXIV-2606-25622`；Method `https://arxiv.org/html/2606.25622v1 — §IV Theoretical Framework: MAS Architecture and Experimental Setup`；Evaluation `https://arxiv.org/html/2606.25622v1 — §V Results & Discussion`；未证明边界 `https://arxiv.org/html/2606.25622v1 — §VI Limitations & Future Work`。

### SF-2026-ARXIV-2606-25760

### 2606.25760 — Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets

**问题与旧路径。** Computer-use agents turn vision-language model (VLM) predictions into executable GUI clicks, so reliable uncertainty estimates are essential for rejection, calibration, miss-severity ranking, and spatial safety regions.

**机制、状态与控制流。** `3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details` 是 `Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets` 的 source-specific 反例/局限边界；若运行条件离开 `4 UQ Generalizes Selectively; 5 Graded Error and Calibration` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25760:start -->
Claim boundary：仅 `arXiv:2606.25760v1`；未证明边界定位 `https://arxiv.org/html/2606.25760v1 — §A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details`。
<!-- claim:SF-2026-ARXIV-2606-25760:end -->

Review note：`SF-2026-ARXIV-2606-25760`；Method `https://arxiv.org/html/2606.25760v1 — §3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks`；Evaluation `https://arxiv.org/html/2606.25760v1 — §4 UQ Generalizes Selectively; 5 Graded Error and Calibration`；未证明边界 `https://arxiv.org/html/2606.25760v1 — §A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details`。

### SF-2026-ARXIV-2606-25782

### 2606.25782 — Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation

**问题与旧路径。** With the widespread adoption of large language models (LLMs) in chatbots and everyday applications, companies increasingly need guardrails that are effective while remaining low-cost and low-latency.

**机制、状态与控制流。** `2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency` 是 `Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25782:start -->
Claim boundary：仅 `arXiv:2606.25782v1`；未证明边界定位 `https://arxiv.org/html/2606.25782v1 — §OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency`。
<!-- claim:SF-2026-ARXIV-2606-25782:end -->

Review note：`SF-2026-ARXIV-2606-25782`；Method `https://arxiv.org/html/2606.25782v1 — §2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel`；Evaluation `https://arxiv.org/html/2606.25782v1 — §5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs`；未证明边界 `https://arxiv.org/html/2606.25782v1 — §OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency`。

### SF-2026-ARXIV-2606-26071

### 2606.26071 — Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment

**问题与旧路径。** A central goal of safety research is determining whether a model is misaligned.

**机制、状态与控制流。** `4 Protocol and Methods; 5 Environments; 7 Methodological Insights` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `10 Limitations and Future Work; negative-results and confounding boundary` 是 `Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment` 的 source-specific 反例/局限边界；若运行条件离开 `6 Case Studies; 8 Recommendations` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26071:start -->
Claim boundary：仅 `arXiv:2606.26071v1`；未证明边界定位 `https://arxiv.org/html/2606.26071v1 — §10 Limitations and Future Work; negative-results and confounding boundary`。
<!-- claim:SF-2026-ARXIV-2606-26071:end -->

Review note：`SF-2026-ARXIV-2606-26071`；Method `https://arxiv.org/html/2606.26071v1 — §4 Protocol and Methods; 5 Environments; 7 Methodological Insights`；Evaluation `https://arxiv.org/html/2606.26071v1 — §6 Case Studies; 8 Recommendations`；未证明边界 `https://arxiv.org/html/2606.26071v1 — §10 Limitations and Future Work; negative-results and confounding boundary`。

### SF-2026-ARXIV-2606-26185

### 2606.26185 — Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations

**问题与旧路径。** LLM-as-judge ("grader") components are now standard in evaluation harnesses, including safety evaluations where a pass/fail verdict may gate downstream deployment decisions.

**机制、状态与控制流。** `Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Temperature control is necessary but not sufficient; prompt/model/vendor drift remains` 是 `Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-temperature, repeat-run and judge-agreement evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26185:start -->
Claim boundary：仅 `arXiv:2606.26185v1`；未证明边界定位 `https://arxiv.org/html/2606.26185v1 — §Temperature control is necessary but not sufficient; prompt/model/vendor drift remains`。
<!-- claim:SF-2026-ARXIV-2606-26185:end -->

Review note：`SF-2026-ARXIV-2606-26185`；Method `https://arxiv.org/html/2606.26185v1 — §Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation`；Evaluation `https://arxiv.org/html/2606.26185v1 — §Cross-temperature, repeat-run and judge-agreement evaluation`；未证明边界 `https://arxiv.org/html/2606.26185v1 — §Temperature control is necessary but not sufficient; prompt/model/vendor drift remains`。

### SF-2026-ARXIV-2606-26300

### 2606.26300 — The Verification Horizon: No Silver Bullet for Coding Agent Rewards

**问题与旧路径。** A classical intuition holds that verifying a solution is easier than producing one.

**机制、状态与控制流。** `Verification Horizon formulation for coding-agent rewards` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `No universal reward verifier; longer horizons and hidden environment state remain` 是 `The Verification Horizon: No Silver Bullet for Coding Agent Rewards` 的 source-specific 反例/局限边界；若运行条件离开 `Reward-verification experiments across coding horizons` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26300:start -->
Claim boundary：仅 `arXiv:2606.26300v1`；未证明边界定位 `https://arxiv.org/html/2606.26300v1 — §No universal reward verifier; longer horizons and hidden environment state remain`。
<!-- claim:SF-2026-ARXIV-2606-26300:end -->

Review note：`SF-2026-ARXIV-2606-26300`；Method `https://arxiv.org/html/2606.26300v1 — §Verification Horizon formulation for coding-agent rewards`；Evaluation `https://arxiv.org/html/2606.26300v1 — §Reward-verification experiments across coding horizons`；未证明边界 `https://arxiv.org/html/2606.26300v1 — §No universal reward verifier; longer horizons and hidden environment state remain`。

### SF-2026-ARXIV-2606-26429

### 2606.26429 — DualEval: Joint Model-Item Calibration for Unified LLM Evaluation

**问题与旧路径。** Current LLM evaluation relies on two complementary but often disconnected signals: static benchmarks with objective correctness labels and arena-style preference data that better reflect open-ended user interactions.

**机制、状态与控制流。** `DualEval joint model-item calibration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Joint calibration assumes the evaluated item/model pool; new distributions require refitting` 是 `DualEval: Joint Model-Item Calibration for Unified LLM Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `Unified LLM evaluation experiments and calibration analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26429:start -->
Claim boundary：仅 `arXiv:2606.26429v1`；未证明边界定位 `https://arxiv.org/html/2606.26429v1 — §Joint calibration assumes the evaluated item/model pool; new distributions require refitting`。
<!-- claim:SF-2026-ARXIV-2606-26429:end -->

Review note：`SF-2026-ARXIV-2606-26429`；Method `https://arxiv.org/html/2606.26429v1 — §DualEval joint model-item calibration`；Evaluation `https://arxiv.org/html/2606.26429v1 — §Unified LLM evaluation experiments and calibration analysis`；未证明边界 `https://arxiv.org/html/2606.26429v1 — §Joint calibration assumes the evaluated item/model pool; new distributions require refitting`。

### SF-2026-ARXIV-2606-26456

### 2606.26456 — Towards Safety-Aware Mutation Testing for Autonomous Driving Systems

**问题与旧路径。** Simulation-based testing is essential for ensuring the safety of Autonomous Driving Systems (ADS), yet the community lacks a systematic criterion for determining when we can safely stop additional test scenario generation.

**机制、状态与控制流。** `Safety-Aware Mutation Testing proposal and interaction-aware mutant model` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional` 是 `Towards Safety-Aware Mutation Testing for Autonomous Driving Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Simulation-based ADS testing protocol and proposed adequacy criterion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26456:start -->
Claim boundary：仅 `arXiv:2606.26456v1`；未证明边界定位 `https://arxiv.org/html/2606.26456v1 — §Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional`。
<!-- claim:SF-2026-ARXIV-2606-26456:end -->

Review note：`SF-2026-ARXIV-2606-26456`；Method `https://arxiv.org/html/2606.26456v1 — §Safety-Aware Mutation Testing proposal and interaction-aware mutant model`；Evaluation `https://arxiv.org/html/2606.26456v1 — §Simulation-based ADS testing protocol and proposed adequacy criterion`；未证明边界 `https://arxiv.org/html/2606.26456v1 — §Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional`。

### SF-2026-ARXIV-2606-26492

### 2606.26492 — Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs

**问题与旧路径。** Deep Learning (DL) programs can fail during training for many reasons, and diagnosing the cause is a costly and time-consuming maintenance task.

**机制、状态与控制流。** `Within-program versus leave-program-out diagnostic design` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Fault-injected programs and studied diagnosers do not prove production root-cause validity` 是 `Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs` 的 source-specific 反例/局限边界；若运行条件离开 `DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26492:start -->
Claim boundary：仅 `arXiv:2606.26492v1`；未证明边界定位 `https://arxiv.org/html/2606.26492v1 — §Fault-injected programs and studied diagnosers do not prove production root-cause validity`。
<!-- claim:SF-2026-ARXIV-2606-26492:end -->

Review note：`SF-2026-ARXIV-2606-26492`；Method `https://arxiv.org/html/2606.26492v1 — §Within-program versus leave-program-out diagnostic design`；Evaluation `https://arxiv.org/html/2606.26492v1 — §DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis`；未证明边界 `https://arxiv.org/html/2606.26492v1 — §Fault-injected programs and studied diagnosers do not prove production root-cause validity`。

## `PLATFORM-FOUNDATIONS` → `books/part-06-ai-infrastructure/57-what-is-ai-platform.md`

### SF-2026-ARXIV-2606-25532

### 2606.25532 — Agentic evolution of physically constrained foundation models

**问题与旧路径。** Artificial intelligence increasingly drives automated scientific discovery, yet contemporary generalist agents lack physical grounding, frequently hallucinating hardware-incompatible designs.

**机制、状态与控制流。** `Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought` 所定义的源特定机制用于把硬件约束和发现链纳入平台设计候选的验收边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Exact-v1 research-prototype and evaluated hardware-design boundary` 是 `Agentic evolution of physically constrained foundation models` 的 source-specific 反例/局限边界；若运行条件离开 `Hardware-compliance evaluation and discovered-system validation` 的验证域，`PLATFORM-FOUNDATIONS` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25532:start -->
Claim boundary：仅 `arXiv:2606.25532v1`；未证明边界定位 `https://arxiv.org/html/2606.25532v1 — §Exact-v1 research-prototype and evaluated hardware-design boundary`。
<!-- claim:SF-2026-ARXIV-2606-25532:end -->

Review note：`SF-2026-ARXIV-2606-25532`；Method `https://arxiv.org/html/2606.25532v1 — §Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought`；Evaluation `https://arxiv.org/html/2606.25532v1 — §Hardware-compliance evaluation and discovered-system validation`；未证明边界 `https://arxiv.org/html/2606.25532v1 — §Exact-v1 research-prototype and evaluated hardware-design boundary`。

## `PLATFORM-GPU-SCHEDULER` → `books/part-06-ai-infrastructure/63-gpu-scheduler.md`

### SF-2026-ARXIV-2606-26341

### 2606.26341 — Scaling Nonlinear Optimization: Many Problems One GPU

**问题与旧路径。** Many robotics problems, including trajectory optimization, inverse kinematics, and contact-rich motion planning, reduce to nonlinear programs (NLPs).

**机制、状态与控制流。** `Many Problems One GPU batching and nonlinear-optimization execution design` 所定义的源特定机制用于把异构问题批处理与 GPU 执行配置作为调度状态，而非模型内部细节；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof` 是 `Scaling Nonlinear Optimization: Many Problems One GPU` 的 source-specific 反例/局限边界；若运行条件离开 `GPU scaling experiments across problem families` 的验证域，`PLATFORM-GPU-SCHEDULER` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26341:start -->
Claim boundary：仅 `arXiv:2606.26341v1`；未证明边界定位 `https://arxiv.org/html/2606.26341v1 — §Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof`。
<!-- claim:SF-2026-ARXIV-2606-26341:end -->

Review note：`SF-2026-ARXIV-2606-26341`；Method `https://arxiv.org/html/2606.26341v1 — §Many Problems One GPU batching and nonlinear-optimization execution design`；Evaluation `https://arxiv.org/html/2606.26341v1 — §GPU scaling experiments across problem families`；未证明边界 `https://arxiv.org/html/2606.26341v1 — §Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof`。

## `PLATFORM-MONITORING` → `books/part-06-ai-infrastructure/67-monitoring.md`

### SF-2026-ARXIV-2606-26383

### 2606.26383 — SOLAR: AI-Powered Speed-of-Light Performance Analysis

**问题与旧路径。** How fast could a deep-learning model run on target hardware, and how far is today's implementation from that limit?

**机制、状态与控制流。** `SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation` 所定义的源特定机制用于以校准后的硬件与 workload 参数分解性能上界和瓶颈；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects` 是 `SOLAR: AI-Powered Speed-of-Light Performance Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `Predicted-vs-observed latency and throughput analysis` 的验证域，`PLATFORM-MONITORING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26383:start -->
Claim boundary：仅 `arXiv:2606.26383v1`；未证明边界定位 `https://arxiv.org/html/2606.26383v1 — §Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects`。
<!-- claim:SF-2026-ARXIV-2606-26383:end -->

Review note：`SF-2026-ARXIV-2606-26383`；Method `https://arxiv.org/html/2606.26383v1 — §SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation`；Evaluation `https://arxiv.org/html/2606.26383v1 — §Predicted-vs-observed latency and throughput analysis`；未证明边界 `https://arxiv.org/html/2606.26383v1 — §Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects`。

## `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md`

### SF-2026-ARXIV-2606-25296

### 2606.25296 — SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety

**问题与旧路径。** With advances in autonomous driving and electric vehicle technologies, functional safety has become a critical requirement in automotive chip design.

**机制、状态与控制流。** `SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Threats to Validity; Limitations` 是 `SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety` 的 source-specific 反例/局限边界；若运行条件离开 `Experimental Evaluation; Functional-Safety Case Studies` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25296:start -->
Claim boundary：仅 `arXiv:2606.25296v1`；未证明边界定位 `https://arxiv.org/html/2606.25296v1 — §Threats to Validity; Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25296:end -->

Review note：`SF-2026-ARXIV-2606-25296`；Method `https://arxiv.org/html/2606.25296v1 — §SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation`；Evaluation `https://arxiv.org/html/2606.25296v1 — §Experimental Evaluation; Functional-Safety Case Studies`；未证明边界 `https://arxiv.org/html/2606.25296v1 — §Threats to Validity; Limitations`。

### SF-2026-ARXIV-2606-25349

### 2606.25349 — General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference

**问题与旧路径。** In secure two-party Transformer inference, linear layers are typically evaluated using Fully Homomorphic Encryption (FHE) through plaintext-ciphertext or ciphertext-ciphertext matrix multiplications, where key switching primarily occurs and dominates computational overhead in both FHE-based and hybrid FHE-MPC systems.

**机制、状态与控制流。** `IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VIII Conclusion; exact-v1 analytical-evaluation-only note` 是 `General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference` 的 source-specific 反例/局限边界；若运行条件离开 `VII Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25349:start -->
Claim boundary：仅 `arXiv:2606.25349v1`；未证明边界定位 `https://arxiv.org/html/2606.25349v1 — §VIII Conclusion; exact-v1 analytical-evaluation-only note`。
<!-- claim:SF-2026-ARXIV-2606-25349:end -->

Review note：`SF-2026-ARXIV-2606-25349`；Method `https://arxiv.org/html/2606.25349v1 — §IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation`；Evaluation `https://arxiv.org/html/2606.25349v1 — §VII Evaluation`；未证明边界 `https://arxiv.org/html/2606.25349v1 — §VIII Conclusion; exact-v1 analytical-evaluation-only note`。

### SF-2026-ARXIV-2606-25366

### 2606.25366 — Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield

**问题与旧路径。** Deep-space missions need onboard autonomy that is both capable and certifiable.

**机制、状态与控制流。** `III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `XI-D Limitations` 是 `Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield` 的 source-specific 反例/局限边界；若运行条件离开 `VIII Robustness; IX Integrated Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25366:start -->
Claim boundary：仅 `arXiv:2606.25366v1`；未证明边界定位 `https://arxiv.org/html/2606.25366v1 — §XI-D Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25366:end -->

Review note：`SF-2026-ARXIV-2606-25366`；Method `https://arxiv.org/html/2606.25366v1 — §III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance`；Evaluation `https://arxiv.org/html/2606.25366v1 — §VIII Robustness; IX Integrated Evaluation`；未证明边界 `https://arxiv.org/html/2606.25366v1 — §XI-D Limitations`。

### SF-2026-ARXIV-2606-25371

### 2606.25371 — Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers

**问题与旧路径。** Runtime assurance (RTA) protects a safety-critical system by switching from an advanced controller to a verified safe controller when a monitored condition is violated.

**机制、状态与控制流。** `III Problem Setup; IV Conformal Recovery-Deadline Certificate` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VI-D Limitations` 是 `Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25371:start -->
Claim boundary：仅 `arXiv:2606.25371v1`；未证明边界定位 `https://arxiv.org/html/2606.25371v1 — §VI-D Limitations`。
<!-- claim:SF-2026-ARXIV-2606-25371:end -->

Review note：`SF-2026-ARXIV-2606-25371`；Method `https://arxiv.org/html/2606.25371v1 — §III Problem Setup; IV Conformal Recovery-Deadline Certificate`；Evaluation `https://arxiv.org/html/2606.25371v1 — §V Experiments`；未证明边界 `https://arxiv.org/html/2606.25371v1 — §VI-D Limitations`。

### SF-2026-ARXIV-2606-25592

### 2606.25592 — VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks

**问题与旧路径。** Recent advancements in Image-to-Video (I2V) generation have transformed input images from simple appearance references into interactive control interfaces where visual cues such as arrows, sketches, and emojis orchestrate complex video dynamics with unprecedented controllability.

**机制、状态与控制流。** `2 Visual Prompt Attack and Defense; 2.2 VPA-Guard` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `E.1 Limitations; E.4 Human-in-the-loop Discussion` 是 `VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks` 的 source-specific 反例/局限边界；若运行条件离开 `3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25592:start -->
Claim boundary：仅 `arXiv:2606.25592v1`；未证明边界定位 `https://arxiv.org/html/2606.25592v1 — §E.1 Limitations; E.4 Human-in-the-loop Discussion`。
<!-- claim:SF-2026-ARXIV-2606-25592:end -->

Review note：`SF-2026-ARXIV-2606-25592`；Method `https://arxiv.org/html/2606.25592v1 — §2 Visual Prompt Attack and Defense; 2.2 VPA-Guard`；Evaluation `https://arxiv.org/html/2606.25592v1 — §3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments`；未证明边界 `https://arxiv.org/html/2606.25592v1 — §E.1 Limitations; E.4 Human-in-the-loop Discussion`。

### SF-2026-ARXIV-2606-25721

### 2606.25721 — Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution

**问题与旧路径。** Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents.

**机制、状态与控制流。** `4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Discussion; baseline and hyperparameter sensitivity` 是 `Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation; 5.1 Setup; 5.2 Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25721:start -->
Claim boundary：仅 `arXiv:2606.25721v1`；未证明边界定位 `https://arxiv.org/html/2606.25721v1 — §6 Discussion; baseline and hyperparameter sensitivity`。
<!-- claim:SF-2026-ARXIV-2606-25721:end -->

Review note：`SF-2026-ARXIV-2606-25721`；Method `https://arxiv.org/html/2606.25721v1 — §4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification`；Evaluation `https://arxiv.org/html/2606.25721v1 — §5 Evaluation; 5.1 Setup; 5.2 Results`；未证明边界 `https://arxiv.org/html/2606.25721v1 — §6 Discussion; baseline and hyperparameter sensitivity`。

### SF-2026-ARXIV-2606-25863

### 2606.25863 — Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis

**问题与旧路径。** We study how security patches in highly configurable C/C++ systems map onto the space of compile-time variants.

**机制、状态与控制流。** `PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary` 是 `Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25863:start -->
Claim boundary：仅 `arXiv:2606.25863v1`；未证明边界定位 `https://arxiv.org/pdf/2606.25863v1 — §PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary`。
<!-- claim:SF-2026-ARXIV-2606-25863:end -->

Review note：`SF-2026-ARXIV-2606-25863`；Method `https://arxiv.org/pdf/2606.25863v1 — §PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution`；Evaluation `https://arxiv.org/pdf/2606.25863v1 — §PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches`；未证明边界 `https://arxiv.org/pdf/2606.25863v1 — §PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary`。

### SF-2026-ARXIV-2606-26021

### 2606.26021 — Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries

**问题与旧路径。** Tabular foundation models are commonly assumed to present limited privacy concerns as they are often pre-trained on large collections of synthetic data.

**机制、状态与控制流。** `V Attention-based MIA; VI Inference-Time Hardening Against MIAs` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VIII-C Limitations and opportunities; I Context size` 是 `Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries` 的 source-specific 反例/局限边界；若运行条件离开 `IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26021:start -->
Claim boundary：仅 `arXiv:2606.26021v1`；未证明边界定位 `https://arxiv.org/html/2606.26021v1 — §VIII-C Limitations and opportunities; I Context size`。
<!-- claim:SF-2026-ARXIV-2606-26021:end -->

Review note：`SF-2026-ARXIV-2606-26021`；Method `https://arxiv.org/html/2606.26021v1 — §V Attention-based MIA; VI Inference-Time Hardening Against MIAs`；Evaluation `https://arxiv.org/html/2606.26021v1 — §IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results`；未证明边界 `https://arxiv.org/html/2606.26021v1 — §VIII-C Limitations and opportunities; I Context size`。

### SF-2026-ARXIV-2606-26028

### 2606.26028 — Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem

**问题与旧路径。** As autonomous AI agents increasingly transact across organizational boundaries, a fundamental trust challenge emerges: how can an agent assess whether an unknown counterpart is trustworthy?

**机制、状态与控制流。** `3 System Model: ERC-8004 Protocol; 7 Reputation Market Security` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `9 Limitations and Future Work; C x402 attribution challenges` 是 `Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26028:start -->
Claim boundary：仅 `arXiv:2606.26028v1`；未证明边界定位 `https://arxiv.org/html/2606.26028v1 — §9 Limitations and Future Work; C x402 attribution challenges`。
<!-- claim:SF-2026-ARXIV-2606-26028:end -->

Review note：`SF-2026-ARXIV-2606-26028`；Method `https://arxiv.org/html/2606.26028v1 — §3 System Model: ERC-8004 Protocol; 7 Reputation Market Security`；Evaluation `https://arxiv.org/html/2606.26028v1 — §4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market`；未证明边界 `https://arxiv.org/html/2606.26028v1 — §9 Limitations and Future Work; C x402 attribution challenges`。

### SF-2026-ARXIV-2606-26057

### 2606.26057 — The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems

**问题与旧路径。** AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems.

**机制、状态与控制流。** `2 Threat Model; 3 Requirements; 4 Design; 5 Implementation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `8.3 Limitations and Future Work; Artifact and Reproducibility` 是 `The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26057:start -->
Claim boundary：仅 `arXiv:2606.26057v1`；未证明边界定位 `https://arxiv.org/html/2606.26057v1 — §8.3 Limitations and Future Work; Artifact and Reproducibility`。
<!-- claim:SF-2026-ARXIV-2606-26057:end -->

Review note：`SF-2026-ARXIV-2606-26057`；Method `https://arxiv.org/html/2606.26057v1 — §2 Threat Model; 3 Requirements; 4 Design; 5 Implementation`；Evaluation `https://arxiv.org/html/2606.26057v1 — §6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment`；未证明边界 `https://arxiv.org/html/2606.26057v1 — §8.3 Limitations and Future Work; Artifact and Reproducibility`。

### SF-2026-ARXIV-2606-26257

### 2606.26257 — Dataset Usage Inference without Shadow Models or Held-out Data

**问题与旧路径。** How much of my data was used to train a machine learning model?

**机制、状态与控制流。** `Dataset Usage Inference formulation without shadow models or held-out data` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Requires the paper's observable score/query regime; not per-record legal attribution` 是 `Dataset Usage Inference without Shadow Models or Held-out Data` 的 source-specific 反例/局限边界；若运行条件离开 `Exact-v1 membership/dataset inference experiments and ablations` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26257:start -->
Claim boundary：仅 `arXiv:2606.26257v1`；未证明边界定位 `https://arxiv.org/html/2606.26257v1 — §Requires the paper's observable score/query regime; not per-record legal attribution`。
<!-- claim:SF-2026-ARXIV-2606-26257:end -->

Review note：`SF-2026-ARXIV-2606-26257`；Method `https://arxiv.org/html/2606.26257v1 — §Dataset Usage Inference formulation without shadow models or held-out data`；Evaluation `https://arxiv.org/html/2606.26257v1 — §Exact-v1 membership/dataset inference experiments and ablations`；未证明边界 `https://arxiv.org/html/2606.26257v1 — §Requires the paper's observable score/query regime; not per-record legal attribution`。

### SF-2026-ARXIV-2606-26298

### 2606.26298 — Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems

**问题与旧路径。** Autonomous AI agents may begin to perform consequential, irreversible actions such as clinical prescribing and production software deployment.

**机制、状态与控制流。** `Governing Actions, Not Agents; Institutional Attestation model` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Institutional model is a governance proposal, not a deployed enforcement benchmark` 是 `Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Action-level attestation scenarios and governance analysis` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26298:start -->
Claim boundary：仅 `arXiv:2606.26298v1`；未证明边界定位 `https://arxiv.org/html/2606.26298v1 — §Institutional model is a governance proposal, not a deployed enforcement benchmark`。
<!-- claim:SF-2026-ARXIV-2606-26298:end -->

Review note：`SF-2026-ARXIV-2606-26298`；Method `https://arxiv.org/html/2606.26298v1 — §Governing Actions, Not Agents; Institutional Attestation model`；Evaluation `https://arxiv.org/html/2606.26298v1 — §Action-level attestation scenarios and governance analysis`；未证明边界 `https://arxiv.org/html/2606.26298v1 — §Institutional model is a governance proposal, not a deployed enforcement benchmark`。

### SF-2026-ARXIV-2606-26377

### 2606.26377 — Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats

**问题与旧路径。** Large language models (LLMs) are increasingly deployed in interactive applications, yet they remain vulnerable to adversarial interactions that induce harmful, deceptive, or policy-violating outputs.

**机制、状态与控制流。** `Unified intent-and-harm verification defense` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Evaluated threat families and judges only; intent inference is not proof of harmless execution` 是 `Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats` 的 source-specific 反例/局限边界；若运行条件离开 `Threat-generation and defense evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26377:start -->
Claim boundary：仅 `arXiv:2606.26377v1`；未证明边界定位 `https://arxiv.org/html/2606.26377v1 — §Evaluated threat families and judges only; intent inference is not proof of harmless execution`。
<!-- claim:SF-2026-ARXIV-2606-26377:end -->

Review note：`SF-2026-ARXIV-2606-26377`；Method `https://arxiv.org/html/2606.26377v1 — §Unified intent-and-harm verification defense`；Evaluation `https://arxiv.org/html/2606.26377v1 — §Threat-generation and defense evaluation`；未证明边界 `https://arxiv.org/html/2606.26377v1 — §Evaluated threat families and judges only; intent inference is not proof of harmless execution`。

### SF-2026-ARXIV-2606-26479

### 2606.26479 — Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents

**问题与旧路径。** Recent work (2024 to 2026) has converged on a strategy for defending tool-using LLM agents against indirect prompt injection: rather than training the model to refuse malicious instructions, enforce security outside the model with a deterministic policy that mediates the agent's actions.

**机制、状态与控制流。** `Out-of-band prompt-injection defenses organized as reference monitors and integrity policies` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Position/evaluation paper; static AgentDojo results do not establish adaptive robustness` 是 `Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `Adaptive evaluation methodology against policy-aware attackers` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26479:start -->
Claim boundary：仅 `arXiv:2606.26479v1`；未证明边界定位 `https://arxiv.org/html/2606.26479v1 — §Position/evaluation paper; static AgentDojo results do not establish adaptive robustness`。
<!-- claim:SF-2026-ARXIV-2606-26479:end -->

Review note：`SF-2026-ARXIV-2606-26479`；Method `https://arxiv.org/html/2606.26479v1 — §Out-of-band prompt-injection defenses organized as reference monitors and integrity policies`；Evaluation `https://arxiv.org/html/2606.26479v1 — §Adaptive evaluation methodology against policy-aware attackers`；未证明边界 `https://arxiv.org/html/2606.26479v1 — §Position/evaluation paper; static AgentDojo results do not establish adaptive robustness`。

## `PLATFORM-TRACE` → `books/part-06-ai-infrastructure/69-trace.md`

### SF-2026-ARXIV-2606-26449

### 2606.26449 — ProvenAI: Provenance-Native Traces of Evidence in Generated Answers

**问题与旧路径。** Retrieval-augmented systems routinely present citations alongside generated answers, yet a citation does not confirm that the corresponding source meaningfully shaped the output.

**机制、状态与控制流。** `ProvenAI provenance-native trace schema and evidence links` 所定义的源特定机制用于让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `Trace completeness depends on instrumented producers; provenance does not imply source truth` 是 `ProvenAI: Provenance-Native Traces of Evidence in Generated Answers` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-answer trace/evidence evaluation` 的验证域，`PLATFORM-TRACE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26449:start -->
Claim boundary：仅 `arXiv:2606.26449v1`；未证明边界定位 `https://arxiv.org/html/2606.26449v1 — §Trace completeness depends on instrumented producers; provenance does not imply source truth`。
<!-- claim:SF-2026-ARXIV-2606-26449:end -->

Review note：`SF-2026-ARXIV-2606-26449`；Method `https://arxiv.org/html/2606.26449v1 — §ProvenAI provenance-native trace schema and evidence links`；Evaluation `https://arxiv.org/html/2606.26449v1 — §Generated-answer trace/evidence evaluation`；未证明边界 `https://arxiv.org/html/2606.26449v1 — §Trace completeness depends on instrumented producers; provenance does not imply source truth`。

## `TRAIN-DATA` → `books/part-04-training-system/27-data.md`

### SF-2026-ARXIV-2606-25388

### 2606.25388 — TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning

**问题与旧路径。** Reliable analytics and machine-learning pipelines depend on clean tabular data, yet production tables often contain missing values, typographical errors, inconsistent formats, violated dependencies, unit mismatches, and ambiguous categorical values.

**机制、状态与控制流。** `III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `VII Discussion and Future Work` 是 `TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25388:start -->
Claim boundary：仅 `arXiv:2606.25388v1`；未证明边界定位 `https://arxiv.org/html/2606.25388v1 — §VII Discussion and Future Work`。
<!-- claim:SF-2026-ARXIV-2606-25388:end -->

Review note：`SF-2026-ARXIV-2606-25388`；Method `https://arxiv.org/html/2606.25388v1 — §III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control`；Evaluation `https://arxiv.org/html/2606.25388v1 — §V Experimental Evaluation; V-A Experimental Setup`；未证明边界 `https://arxiv.org/html/2606.25388v1 — §VII Discussion and Future Work`。

### SF-2026-ARXIV-2606-25871

### 2606.25871 — AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search

**问题与旧路径。** How can we generate high-quality relevance annotations at scale without the cost and delays of human labeling?

**机制、状态与控制流。** `3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `5 Production Deployment and Discussion; sponsored-search relevance boundary` 是 `AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25871:start -->
Claim boundary：仅 `arXiv:2606.25871v1`；未证明边界定位 `https://arxiv.org/html/2606.25871v1 — §5 Production Deployment and Discussion; sponsored-search relevance boundary`。
<!-- claim:SF-2026-ARXIV-2606-25871:end -->

Review note：`SF-2026-ARXIV-2606-25871`；Method `https://arxiv.org/html/2606.25871v1 — §3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic`；Evaluation `https://arxiv.org/html/2606.25871v1 — §4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance`；未证明边界 `https://arxiv.org/html/2606.25871v1 — §5 Production Deployment and Discussion; sponsored-search relevance boundary`。

### SF-2026-ARXIV-2606-25996

### 2606.25996 — Autodata: An agentic data scientist to create high quality synthetic data

**问题与旧路径。** We introduce Autodata, a general method that enables AI agents to act as data scientists who build high quality training and evaluation data.

**机制、状态与控制流。** `2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation` 是 `Autodata: An agentic data scientist to create high quality synthetic data` 的 source-specific 反例/局限边界；若运行条件离开 `3 Experiments; CS, legal, and scientific reasoning tasks` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25996:start -->
Claim boundary：仅 `arXiv:2606.25996v1`；未证明边界定位 `https://arxiv.org/html/2606.25996v1 — §6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation`。
<!-- claim:SF-2026-ARXIV-2606-25996:end -->

Review note：`SF-2026-ARXIV-2606-25996`；Method `https://arxiv.org/html/2606.25996v1 — §2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist`；Evaluation `https://arxiv.org/html/2606.25996v1 — §3 Experiments; CS, legal, and scientific reasoning tasks`；未证明边界 `https://arxiv.org/html/2606.25996v1 — §6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation`。

## `TRAIN-DISTRIBUTED-TRAINING` → `books/part-04-training-system/36-distributed-training.md`

### SF-2026-ARXIV-2606-25759

### 2606.25759 — NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication

**问题与旧路径。** Large-scale neural-network training repeatedly aggregates gradients across devices, making communication a central cost in distributed learning.

**机制、状态与控制流。** `3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing` 所定义的源特定机制用于把集群运行剖面映射为运行时 bucket 与并行绑定状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary` 是 `NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication` 的 source-specific 反例/局限边界；若运行条件离开 `7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope` 的验证域，`TRAIN-DISTRIBUTED-TRAINING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-25759:start -->
Claim boundary：仅 `arXiv:2606.25759v1`；未证明边界定位 `https://arxiv.org/html/2606.25759v1 — §9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary`。
<!-- claim:SF-2026-ARXIV-2606-25759:end -->

Review note：`SF-2026-ARXIV-2606-25759`；Method `https://arxiv.org/html/2606.25759v1 — §3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing`；Evaluation `https://arxiv.org/html/2606.25759v1 — §7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope`；未证明边界 `https://arxiv.org/html/2606.25759v1 — §9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary`。

## `TRAIN-GRPO` → `books/part-04-training-system/33-grpo.md`

### SF-2026-ARXIV-2606-26027

### 2606.26027 — Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It

**问题与旧路径。** Tool use enables large language models (LLMs) to perform complex tasks, and recent agentic reinforcement learning (RL) methods show promise for enhancing model capabilities.

**机制、状态与控制流。** `4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes` 所定义的源特定机制用于把崩溃信号与监督修复绑定到策略更新门控；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。

**Trade-off、failure、fallback 与共存。** `B Training Details; C Qwen3 Training; E Training Dynamic` 是 `Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation` 的验证域，`TRAIN-GRPO` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- claim:SF-2026-ARXIV-2606-26027:start -->
Claim boundary：仅 `arXiv:2606.26027v1`；未证明边界定位 `https://arxiv.org/html/2606.26027v1 — §B Training Details; C Qwen3 Training; E Training Dynamic`。
<!-- claim:SF-2026-ARXIV-2606-26027:end -->

Review note：`SF-2026-ARXIV-2606-26027`；Method `https://arxiv.org/html/2606.26027v1 — §4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes`；Evaluation `https://arxiv.org/html/2606.26027v1 — §5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation`；未证明边界 `https://arxiv.org/html/2606.26027v1 — §B Training Details; C Qwen3 Training; E Training Dynamic`。

