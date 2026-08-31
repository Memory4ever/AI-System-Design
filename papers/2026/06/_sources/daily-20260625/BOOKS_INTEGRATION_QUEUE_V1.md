# 2026-06-25 Books Integration Queue V1

Denominator `daily-v2.1:2026-06-25:9dcf324622a37ab5`. Applied under the 2026-06-25 shared write lock: 63 families in 25 unique owners.

## `AGENT-MCP` → `books/part-07-agent/83-mcp.md`

- `SF-2026-ARXIV-2606-26211` — Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem
  - Delta: `Data Facts metadata schema; provenance, semantics, constraints and exchange contract` 所定义的源特定机制用于以带 provenance、语义和约束的 Data Facts 作为跨 Agent 交换契约；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Single ecosystem prototype; no proof of cross-vendor enforcement or semantic completeness` 是 `Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `NANDini multi-agent exchange examples and schema coverage` 的验证域，`AGENT-MCP` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `AGENT-MEMORY` → `books/part-07-agent/77-memory.md`

- `SF-2026-ARXIV-2606-25449` — Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One
  - Delta: `3 Brittle Memory and Reclaim Evaluation; 3.2 Reclaim Protocol` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `7 Limitations` 是 `Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental Setup; 5 Results; 5.7 Boundary of the Fix` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25658` — Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding
  - Delta: `3 Method; 3.2 Online Semantic Basis; 3.3 Dynamic Visual Memory Bank` 所定义的源特定机制用于把动态记忆写入、回收与失效变成有 owner 的持久状态迁移；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `A Limitations` 是 `Towards a Dynamic and Fixed-budget Memory Bank for Efficient Streaming Video Understanding` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiment; 4.1 Benchmarks and Metrics; 4.2 Implementation` 的验证域，`AGENT-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md`

- `SF-2026-ARXIV-2606-25514` — Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution
  - Delta: `2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication` 所定义的源特定机制用于把事件通信、角色分工与失败升级纳入多 Agent 协调状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `5 Threats to Validity` 是 `Unlocking Model Potentials Through Adaptive Multi-Agent Scaffolding for Efficient Issue Resolution` 的 source-specific 反例/局限边界；若运行条件离开 `3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures` 的验证域，`AGENT-MULTI-AGENT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `AGENT-PLANNING` → `books/part-07-agent/79-planning.md`

- `SF-2026-ARXIV-2606-25274` — UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control
  - Delta: `3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `7 Limitations` 是 `UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Implemented Evidence; 6 Analysis` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26463` — Finding the Time to Think: Learning Planning Budgets in Real-Time RL
  - Delta: `Variable-delay real-time RL; lightweight gate selects state-dependent planning budget` 所定义的源特定机制用于以候选扩展或实时 gate 分配规划预算，并在超时或低置信度时回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Game planners and timing model do not prove benefit under production tool latency or safety deadlines` 是 `Finding the Time to Think: Learning Planning Budgets in Real-Time RL` 的 source-specific 反例/局限边界；若运行条件离开 `Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation` 的验证域，`AGENT-PLANNING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `AGENT-PROMPT` → `books/part-07-agent/74-prompt.md`

- `SF-2026-ARXIV-2606-26356` — Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems
  - Delta: `Instruction Bleed formulation; prompt-composed module interference` 所定义的源特定机制用于把模块间指令干扰作为可测试的组合边界，而非默认隔离；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Prompt/module families tested do not establish universal isolation or adversarial robustness` 是 `Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-module interference experiments and mitigations` 的验证域，`AGENT-PROMPT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `AGENT-RAG` → `books/part-07-agent/76-rag.md`

- `SF-2026-ARXIV-2606-25656` — Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization
  - Delta: `3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `6 Conclusions and future work; C Retrieval-Generation Gap` 是 `Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experimental setup; 5 Experimental results` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25674` — BitNet Text Embeddings
  - Delta: `3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `4.4 Analysis; task-type sensitivity to quantization` 是 `BitNet Text Embeddings` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; 4.1 Experimental Setup; B Evaluation Details` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26439` — TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization
  - Delta: `TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved` 是 `TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization` 的 source-specific 反例/局限边界；若运行条件离开 `GPU retrieval throughput, latency and quality evaluation` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26441` — GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices
  - Delta: `GPUSparse learned sparse retrieval with parallel inverted indices` 所定义的源特定机制用于把检索索引、量化、GPU scorer 与更新一致性拆成显式数据面状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling` 是 `GPUSparse: GPU-Accelerated Learned Sparse Retrieval with Parallel Inverted Indices` 的 source-specific 反例/局限边界；若运行条件离开 `Retrieval quality, latency and GPU scaling experiments` 的验证域，`AGENT-RAG` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `AGENT-TOOL-CALLING` → `books/part-07-agent/78-tool-calling.md`

- `SF-2026-ARXIV-2606-25605` — Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints
  - Delta: `3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `7.5 Failure Cases and Limitations; 8.4 Limitations` 是 `Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25705` — GUI agent: Guided Exploration of User-Sensitive Screens
  - Delta: `3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `5 Conclusion; short-paper and emulator-only boundary` 是 `GUI agent: Guided Exploration of User-Sensitive Screens` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Results` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25819` — Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability
  - Delta: `ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Canonical recovery-path construction and five injected-hazard boundary` 是 `Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Experimental Setup; Further Analysis; Error Analysis` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25987` — Weave of Formal Thought
  - Delta: `3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `6 Next Steps and Research Vision; technical-report preliminary-results boundary` 是 `Weave of Formal Thought` 的 source-specific 反例/局限边界；若运行条件离开 `5 WoFT Improves Surface Modeling; 5.1 Experimental setup` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `AGENT-WORKFLOW` → `books/part-07-agent/81-workflow.md`

- `SF-2026-ARXIV-2606-25447` — The Interplay of Harness Design and Post-Training in LLM Agents
  - Delta: `3 Experiment Setup; 3.2 Harness; 3.3 Tool Schema; 3.4 Task Type` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `B Benchmark Details; C Experimental Details; stated ALFWorld boundary` 是 `The Interplay of Harness Design and Post-Training in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `4 Analysis; 4.1 Evaluation Protocol; 4.4 OOD Robustness` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26442` — AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities
  - Delta: `AXLE cloud infrastructure for Lean 4 utilities; remote execution and artifact handling` 所定义的源特定机制用于把执行 harness、远端 utility 与 artifact handoff 变成可观测工作流状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Cloud utility success does not prove generated theorem correctness beyond Lean checking or side-effect safety` 是 `AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities` 的 source-specific 反例/局限边界；若运行条件离开 `Utility execution, throughput and theorem-proving workflow evaluation` 的验证域，`AGENT-WORKFLOW` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `INFER-GPU-MEMORY` → `books/part-05-inference-system/54-gpu-memory.md`

- `SF-2026-ARXIV-2606-25285` — EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression
  - Delta: `3 EPTS: Elastic Post-Training Sparsity` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Limitations and Discussion` 是 `EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments; Experimental Setup; Main Results` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25519` — Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models
  - Delta: `3 Experimental Setup; 5 Quantization Inflates Reasoning Tokens; 6 Anatomy` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `7 Can We Reduce Reasoning-Token Inflation; D.2 Model details` 是 `Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models` 的 source-specific 反例/局限边界；若运行条件离开 `D Additional evaluation details; D.1 Benchmarks and evaluation protocol` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26488` — What Survives When You Compress a Recursive Reasoner for the Edge?
  - Delta: `Compression of recursive reasoners across precision, pruning, distillation and attention variants` 所定义的源特定机制用于把稀疏、量化或压缩决策绑定到显存预算和质量回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Edge recursive models only; token-level preservation does not imply global-reasoning preservation` 是 `What Survives When You Compress a Recursive Reasoner for the Edge?` 的 source-specific 反例/局限边界；若运行条件离开 `Three tasks and two recursive architectures; local vs puzzle-exact accuracy` 的验证域，`INFER-GPU-MEMORY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `INFER-KV-CACHE` → `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`

- `SF-2026-ARXIV-2606-26472` — Epiphany-Aware KV Cache Eviction Without the Attention Matrix
  - Delta: `Epiphany score from forward-pass representation change; attention-matrix-free eviction` 所定义的源特定机制用于以表征变化分数驱动逐 token KV 驱逐，并保留完整 KV 回退；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Model/task transfer and representation-score drift are unproved; quality regression requires full-KV fallback` 是 `Epiphany-Aware KV Cache Eviction Without the Attention Matrix` 的 source-specific 反例/局限边界；若运行条件离开 `Long-reasoning cache/quality evaluation and 16x feasible-context claim` 的验证域，`INFER-KV-CACHE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `INFER-PREFILL` → `books/part-05-inference-system/43-prefill.md`

- `SF-2026-ARXIV-2606-25353` — Cache-Resident LLM Inference in GB-Scale Last-Level Caches
  - Delta: `3 Architecture; 3.1 Weight-Attention Decoupled Organization; 4 Implementation` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `7 Discussion; 7.2 Future Works` 是 `Cache-Resident LLM Inference in GB-Scale Last-Level Caches` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiment Setup; 6 Evaluation` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25426` — Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX
  - Delta: `3 Method; 3.1 Three-level cache blocking; 3.2 Weight pre-packing` 所定义的源特定机制用于把权重、attention 与 cache-blocking 路径拆成可独立放置和优化的前缀计算状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `6 Conclusion; Limitations` 是 `Above the Inner Loop: Exceeding Accelerate at LLM Prefill GEMM on the M1 AMX` 的 source-specific 反例/局限边界；若运行条件离开 `4 Evaluation; 4.1 Experimental setup; 4.7 End-to-end prefill GEMM measurement` 的验证域，`INFER-PREFILL` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `INFER-REQUEST-LIFECYCLE` → `books/part-05-inference-system/42-what-happens-during-inference.md`

- `SF-2026-ARXIV-2606-25838` — Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines
  - Delta: `III Method; IV Confidence-Aware Routing` 所定义的源特定机制用于让路由器基于请求置信度持有后端选择与回退权；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `VII-C Limitations and future work` 是 `Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments; V-A Evaluation protocol; VI Deployment Patterns` 的验证域，`INFER-REQUEST-LIFECYCLE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `INFER-SCHEDULING` → `books/part-05-inference-system/56-inference-scheduling.md`

- `SF-2026-ARXIV-2606-25467` — RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs
  - Delta: `III Request-Resource Coupling Model; IV RQ-SAFE Online Orchestration` 所定义的源特定机制用于让在线编排器共同持有请求资源耦合、准入和降级状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `D-B Runtime Boundary and Fallback; G Implementation Scope Clarifications` 是 `RQ-SAFE: Coupled Request-Resource Scheduling for Online Edge SFC-DAGs` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`INFER-SCHEDULING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `INFER-TENSORRT-LLM` → `books/part-05-inference-system/49-tensorrt-llm.md`

- `SF-2026-ARXIV-2606-25453` — EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication
  - Delta: `III EmuGEMM-I; IV EmuGEMM-II` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `V-G Limitations` 是 `EmuGEMM: Fused Tensor Core Kernels for Precision Emulation in Matrix Multiplication` 的 source-specific 反例/局限边界；若运行条件离开 `V Evaluation; V-B Experimental Setup; V-F Precision-Throughput-Memory Trade-off` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26344` — Axon: A Synthesizing Superoptimizer for Tensor Programs
  - Delta: `Axon synthesizing superoptimizer; tensor-program search and verification` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence` 是 `Axon: A Synthesizing Superoptimizer for Tensor Programs` 的 source-specific 反例/局限边界；若运行条件离开 `Kernel synthesis evaluation and generated-program performance` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26453` — Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization
  - Delta: `Micro-profiling tools as expert surrogates for LLM CUDA optimization` 所定义的源特定机制用于以可验证搜索或 profiling 反馈驱动 kernel 选择，同时保留确定性正确性路径；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback` 是 `Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-kernel correctness, profiling and speed evaluation` 的验证域，`INFER-TENSORRT-LLM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `MODEL-LONG-CONTEXT` → `books/part-02-model/22-long-context.md`

- `SF-2026-ARXIV-2606-25342` — Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention
  - Delta: `Parametric Attention and Lifelong In-Context Learning formulation` 所定义的源特定机制用于把跨段记忆从隐式上下文提升为可更新的长期参数状态，并由模型路径决定写入与读取；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Discussion; finite-memory and task-family limitations` 是 `Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Lifelong sequence results` 的验证域，`MODEL-LONG-CONTEXT` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`

- `SF-2026-ARXIV-2606-25575` — One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand
  - Delta: `Variable-autonomy architecture; task-phase authority transfer; always-available release gesture` 所定义的源特定机制用于把任务阶段、共享自治等级和人工接管手势纳入动作控制回路；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Single wearable-hand embodiment, known objects, five tools, and short-horizon study` 是 `One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand` 的 source-specific 反例/局限边界；若运行条件离开 `44-participant user study; five bimanual tasks; policy-variant success` 的验证域，`MULTIMODAL-EMBODIED-VLA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md`

- `SF-2026-ARXIV-2606-25487` — How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring
  - Delta: `3 Setup; Appendix A Prompts, wrappers, and attack configuration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `6 Limitations` 是 `How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring` 的 source-specific 反例/局限边界；若运行条件离开 `4 Results; 4.1 Calibration against human labels; 4.3 white-box attack` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25622` — Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz
  - Delta: `IV Theoretical Framework: MAS Architecture and Experimental Setup` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `VI Limitations & Future Work` 是 `Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `V Results & Discussion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25760` — Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets
  - Delta: `3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details` 是 `Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets` 的 source-specific 反例/局限边界；若运行条件离开 `4 UQ Generalizes Selectively; 5 Graded Error and Calibration` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25782` — Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation
  - Delta: `2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency` 是 `Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26071` — Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
  - Delta: `4 Protocol and Methods; 5 Environments; 7 Methodological Insights` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `10 Limitations and Future Work; negative-results and confounding boundary` 是 `Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment` 的 source-specific 反例/局限边界；若运行条件离开 `6 Case Studies; 8 Recommendations` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26185` — Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations
  - Delta: `Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Temperature control is necessary but not sufficient; prompt/model/vendor drift remains` 是 `Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-temperature, repeat-run and judge-agreement evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26300` — The Verification Horizon: No Silver Bullet for Coding Agent Rewards
  - Delta: `Verification Horizon formulation for coding-agent rewards` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `No universal reward verifier; longer horizons and hidden environment state remain` 是 `The Verification Horizon: No Silver Bullet for Coding Agent Rewards` 的 source-specific 反例/局限边界；若运行条件离开 `Reward-verification experiments across coding horizons` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26429` — DualEval: Joint Model-Item Calibration for Unified LLM Evaluation
  - Delta: `DualEval joint model-item calibration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Joint calibration assumes the evaluated item/model pool; new distributions require refitting` 是 `DualEval: Joint Model-Item Calibration for Unified LLM Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `Unified LLM evaluation experiments and calibration analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26456` — Towards Safety-Aware Mutation Testing for Autonomous Driving Systems
  - Delta: `Safety-Aware Mutation Testing proposal and interaction-aware mutant model` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional` 是 `Towards Safety-Aware Mutation Testing for Autonomous Driving Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Simulation-based ADS testing protocol and proposed adequacy criterion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26492` — Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs
  - Delta: `Within-program versus leave-program-out diagnostic design` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Fault-injected programs and studied diagnosers do not prove production root-cause validity` 是 `Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs` 的 source-specific 反例/局限边界；若运行条件离开 `DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `PLATFORM-FOUNDATIONS` → `books/part-06-ai-infrastructure/57-what-is-ai-platform.md`

- `SF-2026-ARXIV-2606-25532` — Agentic evolution of physically constrained foundation models
  - Delta: `Physically constrained multi-agent discovery engine; Evolutionary Knowledge Graph and algorithmic chain of thought` 所定义的源特定机制用于把硬件约束和发现链纳入平台设计候选的验收边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Exact-v1 research-prototype and evaluated hardware-design boundary` 是 `Agentic evolution of physically constrained foundation models` 的 source-specific 反例/局限边界；若运行条件离开 `Hardware-compliance evaluation and discovered-system validation` 的验证域，`PLATFORM-FOUNDATIONS` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `PLATFORM-GPU-SCHEDULER` → `books/part-06-ai-infrastructure/63-gpu-scheduler.md`

- `SF-2026-ARXIV-2606-26341` — Scaling Nonlinear Optimization: Many Problems One GPU
  - Delta: `Many Problems One GPU batching and nonlinear-optimization execution design` 所定义的源特定机制用于把异构问题批处理与 GPU 执行配置作为调度状态，而非模型内部细节；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Only disclosed nonlinear solvers/problem shapes; no cluster-level scheduling or isolation proof` 是 `Scaling Nonlinear Optimization: Many Problems One GPU` 的 source-specific 反例/局限边界；若运行条件离开 `GPU scaling experiments across problem families` 的验证域，`PLATFORM-GPU-SCHEDULER` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `PLATFORM-MONITORING` → `books/part-06-ai-infrastructure/67-monitoring.md`

- `SF-2026-ARXIV-2606-26383` — SOLAR: AI-Powered Speed-of-Light Performance Analysis
  - Delta: `SOLAR speed-of-light performance model; bottleneck decomposition and bound calculation` 所定义的源特定机制用于以校准后的硬件与 workload 参数分解性能上界和瓶颈；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Analytical bounds depend on calibrated hardware/workload parameters and omit undisclosed runtime effects` 是 `SOLAR: AI-Powered Speed-of-Light Performance Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `Predicted-vs-observed latency and throughput analysis` 的验证域，`PLATFORM-MONITORING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md`

- `SF-2026-ARXIV-2606-25296` — SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety
  - Delta: `SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Threats to Validity; Limitations` 是 `SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety` 的 source-specific 反例/局限边界；若运行条件离开 `Experimental Evaluation; Functional-Safety Case Studies` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25349` — General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference
  - Delta: `IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `VIII Conclusion; exact-v1 analytical-evaluation-only note` 是 `General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference` 的 source-specific 反例/局限边界；若运行条件离开 `VII Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25366` — Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield
  - Delta: `III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `XI-D Limitations` 是 `Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield` 的 source-specific 反例/局限边界；若运行条件离开 `VIII Robustness; IX Integrated Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25371` — Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers
  - Delta: `III Problem Setup; IV Conformal Recovery-Deadline Certificate` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `VI-D Limitations` 是 `Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25592` — VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks
  - Delta: `2 Visual Prompt Attack and Defense; 2.2 VPA-Guard` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `E.1 Limitations; E.4 Human-in-the-loop Discussion` 是 `VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks` 的 source-specific 反例/局限边界；若运行条件离开 `3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25721` — Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution
  - Delta: `4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `6 Discussion; baseline and hyperparameter sensitivity` 是 `Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation; 5.1 Setup; 5.2 Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25863` — Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis
  - Delta: `PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary` 是 `Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26021` — Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries
  - Delta: `V Attention-based MIA; VI Inference-Time Hardening Against MIAs` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `VIII-C Limitations and opportunities; I Context size` 是 `Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries` 的 source-specific 反例/局限边界；若运行条件离开 `IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26028` — Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem
  - Delta: `3 System Model: ERC-8004 Protocol; 7 Reputation Market Security` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `9 Limitations and Future Work; C x402 attribution challenges` 是 `Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26057` — The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
  - Delta: `2 Threat Model; 3 Requirements; 4 Design; 5 Implementation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `8.3 Limitations and Future Work; Artifact and Reproducibility` 是 `The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26257` — Dataset Usage Inference without Shadow Models or Held-out Data
  - Delta: `Dataset Usage Inference formulation without shadow models or held-out data` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Requires the paper's observable score/query regime; not per-record legal attribution` 是 `Dataset Usage Inference without Shadow Models or Held-out Data` 的 source-specific 反例/局限边界；若运行条件离开 `Exact-v1 membership/dataset inference experiments and ablations` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26298` — Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems
  - Delta: `Governing Actions, Not Agents; Institutional Attestation model` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Institutional model is a governance proposal, not a deployed enforcement benchmark` 是 `Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Action-level attestation scenarios and governance analysis` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26377` — Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats
  - Delta: `Unified intent-and-harm verification defense` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Evaluated threat families and judges only; intent inference is not proof of harmless execution` 是 `Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats` 的 source-specific 反例/局限边界；若运行条件离开 `Threat-generation and defense evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-26479` — Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents
  - Delta: `Out-of-band prompt-injection defenses organized as reference monitors and integrity policies` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Position/evaluation paper; static AgentDojo results do not establish adaptive robustness` 是 `Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `Adaptive evaluation methodology against policy-aware attackers` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `PLATFORM-TRACE` → `books/part-06-ai-infrastructure/69-trace.md`

- `SF-2026-ARXIV-2606-26449` — ProvenAI: Provenance-Native Traces of Evidence in Generated Answers
  - Delta: `ProvenAI provenance-native trace schema and evidence links` 所定义的源特定机制用于让证据生产者写入 provenance 链，消费者据此追踪而不把来源等同于真值；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `Trace completeness depends on instrumented producers; provenance does not imply source truth` 是 `ProvenAI: Provenance-Native Traces of Evidence in Generated Answers` 的 source-specific 反例/局限边界；若运行条件离开 `Generated-answer trace/evidence evaluation` 的验证域，`PLATFORM-TRACE` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `TRAIN-DATA` → `books/part-04-training-system/27-data.md`

- `SF-2026-ARXIV-2606-25388` — TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning
  - Delta: `III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `VII Discussion and Future Work` 是 `TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25871` — AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search
  - Delta: `3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `5 Production Deployment and Discussion; sponsored-search relevance boundary` 是 `AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

- `SF-2026-ARXIV-2606-25996` — Autodata: An agentic data scientist to create high quality synthetic data
  - Delta: `2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation` 是 `Autodata: An agentic data scientist to create high quality synthetic data` 的 source-specific 反例/局限边界；若运行条件离开 `3 Experiments; CS, legal, and scientific reasoning tasks` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `TRAIN-DISTRIBUTED-TRAINING` → `books/part-04-training-system/36-distributed-training.md`

- `SF-2026-ARXIV-2606-25759` — NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication
  - Delta: `3 System Overview; 4 Operating-Profile Calibration; 5 Runtime Binding and Bucket Routing` 所定义的源特定机制用于把集群运行剖面映射为运行时 bucket 与并行绑定状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `9 Limitations and Future Work; A.4 Evaluation Environment and Measurement Boundary` 是 `NEURON-Fabric: Architecture-Runtime Co-Design for Controlled Low-Bit Gradient Communication` 的 source-specific 反例/局限边界；若运行条件离开 `7 Closed-Loop Cluster Evaluation; 7.1 Evaluation Setup and Scope` 的验证域，`TRAIN-DISTRIBUTED-TRAINING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

## `TRAIN-GRPO` → `books/part-04-training-system/33-grpo.md`

- `SF-2026-ARXIV-2606-26027` — Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It
  - Delta: `4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes` 所定义的源特定机制用于把崩溃信号与监督修复绑定到策略更新门控；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。
  - Boundary: `B Training Details; C Qwen3 Training; E Training Dynamic` 是 `Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It` 的 source-specific 反例/局限边界；若运行条件离开 `5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation` 的验证域，`TRAIN-GRPO` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

