# 2026-05-09 Books Writeback Queue

本文件是 date-local queue；本 author lane **未修改共享 Books**。root 必须按日期串行写回，并由非写作者做 post-write semantic audit。

- Queue count: 24
- Audit status: independent fresh-context review passed; root serial writeback pending

## SF-2026-ARXIV-2605-07135
- Primary: `arXiv:2605.07135v1`
- Owner: `AGENT-WORKFLOW`
- Delta: `Demystifying and Detecting Agentic Workflow Injection Vulnerabilities in GitHub Actions` 通过“In this paper, we introduce Agentic Workflow Injection (AWI), a workflow-level injection flaw where untrusted GitHub event context, such as issue bodies, pull-request descriptions, or comments, is incorporated into agent prompts or agent-consumed inputs and converted into attacker-influenced behavior through agent tools or downstream…”改变 agent workflow 的可观察机制或决策边界；exact-v1 的证明范围限于“We prioritized disclosure for 187 zero-day cases, received 26 maintainer responses, and 24 cases have been accepted or fixed at the time of writing.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-07238
- Primary: `arXiv:2605.07238v1`
- Owner: `INFER-SCHEDULING`
- Delta: `FATE: Future-State-Aware Scheduling for Heterogeneous LLM Workflows` 通过“We present FATE, a future-state-aware scheduler for heterogeneous LLM workflows.”改变 infer scheduling 的可观察机制或决策边界；exact-v1 的证明范围限于“Mechanism analysis and ablations show that these gains arise from jointly preserving multiple dimensions of future execution state rather than prefix reuse alone.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-07242
- Primary: `arXiv:2605.07242v1`
- Owner: `AGENT-MEMORY`
- Delta: `MEMOREPAIR: Barrier-First Cascade Repair in Agentic Memory` 通过“We present MemoRepair, a barrier-first cascade-repair contract for agentic memory.”改变 agent memory 的可观察机制或决策边界；exact-v1 的证明范围限于“We show that the induced publication problem reduces to maximum-weight predecessor closure and can be solved exactly by a single s-t min-cut.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-07330
- Primary: `arXiv:2605.07330v1`
- Owner: `INFER-SCHEDULING`
- Delta: `SparseRL-Sync: Lossless Weight Synchronization with ~100x Less Communication` 通过“Building on this observation, we propose and implement SparseRL-Sync, which replaces full-weight transfers with a lossless sparse update payload (indices and values) that can be exactly reconstructed on the inference side, thereby preserving 100% fidelity.”改变 infer scheduling 的可观察机制或决策边界；exact-v1 的证明范围限于“Combined with appropriate bucketing, SparseRL-Sync also reduces launch and control-plane overhead, significantly improving scalability and end-to-end efficiency in bandwidth-limited and highly asynchronous RL settings.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-07442
- Primary: `arXiv:2605.07442v1`
- Owner: `AGENT-RAG`
- Delta: `GameGen-Verifier: Parallel Keypoint-Based Verification for LLM-Generated Games via Runtime State Injection` 通过“We present GameGen-Verifier, an automated verification paradigm for LLM-generated games that decomposes a specification into verifiable keypoints and grounds them into independent verification units.”改变 agent rag 的可观察机制或决策边界；exact-v1 的证明范围限于“On VeriGame, our dataset of 100 games across seven genres, GameGen-Verifier achieves up to 92.2% accuracy against human judgments versus 58.8% for the coverage-enforced Agent-as-a-Verifier baseline, while reducing wall-clock time by up to 16.6x.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-07569
- Primary: `arXiv:2605.07569v1`
- Owner: `INFER-SCHEDULING`
- Delta: `HexiSeq: Accommodating Long Context Training of LLMs over Heterogeneous Hardware` 通过“We introduce HexiSeq, a system that supports fully asymmetric CP--HP partitioning by assigning sequence shards and attention heads according to device compute, memory, and communication capabilities.”改变 infer scheduling 的可观察机制或决策边界；exact-v1 的证明范围限于“On FLOP-comparable pairs against homogeneous clusters, HexiSeq reaches throughput close to the strongest homogeneous baseline, showing that heterogeneous clusters can be used efficiently for long-context LLM training.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-07594
- Primary: `arXiv:2605.07594v1`
- Owner: `AGENT-MEMORY`
- Delta: `MemCompiler: Compile, Don't Inject -- State-Conditioned Memory for Embodied Agents` 通过“To address this, we propose MemCompiler, which reframes memory utilization as State-Conditioned Memory Compilation.”改变 agent memory 的可观察机制或决策边界；exact-v1 的证明范围限于“Across Alf World, EmbodiedBench, and ScienceWorld, MemCompiler consistently improves over no-memory across open-source backbones (up to +129%), matches or approaches frontier closed-source systems, and reduces per-step latency by 60%, demonstrating that state-aware memory compilation…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-07689
- Primary: `arXiv:2605.07689v1`
- Owner: `TRAIN-GRPO`
- Delta: `Gradient Starvation in Binary-Reward GRPO: Why Group-Mean Centering Fails and Why the Simplest Fix Works` 通过“Group Relative Policy Optimization (GRPO) is a standard algorithm for reinforcement learning from verifiable rewards, but its group-mean-centered advantage can fail under binary rewards.”改变 train grpo 的可观察机制或决策边界；exact-v1 的证明范围限于“We then show that the fixed-reference Sign advantage, $A=2r-1$, performs pass@$G$ failure descent by increasing the probability that at least one sample in the group succeeds.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-07836
- Primary: `arXiv:2605.07836v1`
- Owner: `AGENT-MCP`
- Delta: `Unsafe by Flow: Uncovering Bidirectional Data-Flow Risks in MCP Ecosystem` 通过“Model Context Protocol (MCP) have quickly become the interface layer between LLM agents and external tools, yet they also introduce unsafe data flows that existing analyzers handle poorly.”改变 agent mcp 的可观察机制或决策边界；exact-v1 的证明范围限于“Across 15,452 real-world MCP server repositories, MCP-BiFlow surfaces 549 overlap-compressed candidate clusters; manual review confirms 118 vulnerability paths in 87 servers, establishing unsafe propagation as a recurring failure mode that resists detection without protocol-aware…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-07935
- Primary: `arXiv:2605.07935v1`
- Owner: `AGENT-MULTI-AGENT`
- Delta: `TraceFix: Repairing Agent Coordination Protocols with TLA+ Counterexamples` 通过“We present TraceFix, a verification-first pipeline for Large Language Model (LLM) multi-agent coordination.”改变 agent multi agent 的可观察机制或决策边界；exact-v1 的证明范围限于“A paired ablation under a fixed runtime shows that TLC-verified protocols cut deadlock/livelock (DL/LL) from 31.1% to 14.1%, with the largest separation under fault injection.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08317
- Primary: `arXiv:2605.08317v1`
- Owner: `INFER-KV-CACHE`
- Delta: `RDKV: Rate-Distortion Bit Allocation for Joint Eviction and Quantization of the KV Cache` 通过“Large language models (LLMs) have shown strong performance across diverse tasks, but their inference with long input contexts is bottlenecked by memory size and bandwidth.”改变 infer kv cache 的可观察机制或决策边界；exact-v1 的证明范围限于“Experiments on LongBench, RULER, and InfiniteBench show that RDKV outperforms the best evaluated baseline by 9.1% on average.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08346
- Primary: `arXiv:2605.08346v1`
- Owner: `INFER-SCHEDULING`
- Delta: `Sanity Checks for Long-Form Hallucination Detection` 通过“We introduce a controlled-invariance methodology that exposes this distinction through two oracle tests: \textsc{Force}, which replaces each response's final answer with the ground truth while preserving the reasoning trace, and \textsc{Remove}, which strips answer-announcement steps while leaving the trajectory intact.”改变 infer scheduling 的可观察机制或决策边界；exact-v1 的证明范围限于“We further show that once these artifacts are controlled for, effective detection does not necessarily require complex learned representations: TRACT, a lightweight scorer built on lexical trajectory features (hedging trends, step-length dynamics, and cross-response…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08374
- Primary: `arXiv:2605.08374v1`
- Owner: `AGENT-MEMORY`
- Delta: `MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs` 通过“We introduce MemQ, which applies TD($λ$) eligibility traces to memory Q-values, propagating credit backward through a provenance DAG that records which memories were retrieved when each new memory was created.”改变 agent memory 的可观察机制或决策边界；exact-v1 的证明范围限于“Across six benchmarks, spanning OS interaction, function calling, code generation, multimodal reasoning, embodied reasoning, and expert-level QA, MemQ achieves the highest success rate on all six in generalization evaluation and runtime learning, with gains…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08460
- Primary: `arXiv:2605.08460v1`
- Owner: `AGENT-MULTI-AGENT`
- Delta: `When Child Inherits: Modeling and Exploiting Subagent Spawn in Multi-Agent Networks` 通过“We demonstrate these risks in real agent frameworks and propose defenses based on explicit security invariants.”改变 agent multi agent 的可观察机制或决策边界；exact-v1 的证明范围限于“We demonstrate these risks in real agent frameworks and propose defenses based on explicit security invariants.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08513
- Primary: `arXiv:2605.08513v1`
- Owner: `PLATFORM-SECURITY`
- Delta: `A Single Neuron Is Sufficient to Bypass Safety Alignment in Large Language Models` 通过“Safety alignment in language models operates through two mechanistically distinct systems: refusal neurons that gate whether harmful knowledge is expressed, and concept neurons that encode the harmful knowledge itself.”改变 platform security 的可观察机制或决策边界；exact-v1 的证明范围限于“By targeting a single neuron in each system, we demonstrate both directions of failure -- bypassing safety on explicit harmful requests via suppression, and inducing harmful content from innocent prompts via amplification -- across…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08524
- Primary: `arXiv:2605.08524v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: `Unleashing Scalable Context Parallelism for Foundation Models Pre-Training via FCP` 通过“In this paper, we propose FCP, a flexible context parallelism paradigm that shards and schedules sequences at block-level granularity.”改变 platform evaluation system 的可观察机制或决策边界；exact-v1 的证明范围限于“Extensive evaluations show that FCP attains near-linear scalability on up to 256 NVIDIA GPUs, with 1.13x-2.21x improvement in the attention MFU.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08527
- Primary: `arXiv:2605.08527v1`
- Owner: `TRAIN-GRPO`
- Delta: `MARLaaS: Multi-Tenant Asynchronous Reinforcement Learning as a Service` 通过“We propose MARLaaS (Multi-tenant Asynchronous RL as a Service), a system for concurrent RL fine-tuning across multiple users and tasks.”改变 train grpo 的可观察机制或决策边界；exact-v1 的证明范围限于“In multi-task settings (we report up to 32 concurrent tasks), MARLaaS achieves single-task state-of-the-art performance while improving accelerator utilization by up to 4.3x and reducing end-to-end training time by 85%.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08541
- Primary: `arXiv:2605.08541v1`
- Owner: `AGENT-RAG`
- Delta: `Tokens-per-Parameter Coverage Is Critical for Robust LLM Scaling Law Extrapolation` 通过“We prove this for four scaling-law formalisms and derive a closed-form TPP-diversity threshold that is necessary and sufficient for well-conditioned estimation.”改变 agent rag 的可观察机制或决策边界；exact-v1 的证明范围限于“We show that this collinear design, combined with the empirically common near-equality of the exponents governing $N$ and $D$, induces an inherent ill-conditioning in the Gauss-Newton least-squares problem: the condition number of the design…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08545
- Primary: `arXiv:2605.08545v1`
- Owner: `AGENT-RAG`
- Delta: `Log analysis is necessary for credible evaluation of AI agents` 通过“In this paper, we (1) present a taxonomy of threats to credible evaluation documented through log analysis, and (2) develop a set of guiding principles for log analysis.”改变 agent rag 的可观察机制或决策边界；exact-v1 的证明范围限于“This threatens evaluation credibility in three ways.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08563
- Primary: `arXiv:2605.08563v1`
- Owner: `AGENT-WORKFLOW`
- Delta: `Why Retrying Fails: Context Contamination in LLM Agent Pipelines` 通过“We introduce the Context-Contaminated Restart Model (CCRM): a chain of T tool-call steps, each failing with base rate epsilon_0; after any failed attempt, the subsequent attempt operates in contaminated context with elevated error rate epsilon_1 &gt; epsilon_0.”改变 agent workflow 的可观察机制或决策边界；exact-v1 的证明范围限于“Monte Carlo experiments confirm all theoretical predictions.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08580
- Primary: `arXiv:2605.08580v1`
- Owner: `AGENT-MEMORY`
- Delta: `Slipstream: Trajectory-Grounded Compaction Validation for Long-Horizon Agents` 通过“To cope with the large contexts that long-horizon LLM agents produce, modern frameworks increasingly rely on compaction -- invoking an LLM to rewrite the accumulated trajectory into a shorter summary that the agent resumes from.”改变 agent memory 的可观察机制或决策边界；exact-v1 的证明范围限于“Across long-horizon coding (SWE-bench Verified) and web-browsing (BrowseComp) workloads, Slipstream improves task accuracy by up to 8.8 percentage points while reducing end-to-end latency by up to 39.7%.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-08581
- Primary: `arXiv:2605.08581v1`
- Owner: `INFER-KV-CACHE`
- Delta: `PRISM: Fast Online LLM Serving via Scheduling-Memory Co-design` 通过“Guided by this, we present PRISM (Prefix Reuse Optimization Integrated Scheduling and Memory), which co-designs a query-aware scheduler (QAS) with a demand-aware radix tree (DART) to align request admission with exact-prefix KV retention.”改变 infer kv cache 的可观察机制或决策边界；exact-v1 的证明范围限于“Our evaluation results show that, versus the strongest baseline, PRISM reduces average per-QPS P99 TTFT by 23.3\% and 37.1\% while increasing exact-prefix KV-cache hit rate by 5.9 and 12.2 percentage points on 4B and…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2605-16354
- Primary: `arXiv:2605.16354v1`
- Owner: `PLATFORM-SECURITY`
- Delta: `Augmenting Human Evaluation with LLM Judges: How Many Human Reviews Do You Need?` 通过“We propose to use a doubly robust estimator from the missing data literature, which takes advantage of the robustness property against the prediction model, since the missingness model is known by design.”改变 platform security 的可观察机制或决策边界；exact-v1 的证明范围限于“This paper (1) shifts the role of the LLM judge from substitutive to auxiliary, and (2) formulates the LLM-as-a-judge paradigm as one of augmenting human evaluation through a two-stage sampling design, where LLM evaluations…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.

## SF-2026-ARXIV-2606-20582
- Primary: `arXiv:2606.20582v1`
- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Delta: `Communication-Semantic-Aware RDMA Loss Recovery for QP-scalable Hyperscale AI Training` 通过“To address these challenges, we propose Communication-Semantic-Aware Unreliable Datagram (CSA-UD), a novel RDMA loss recovery mechanism that combines scalability and reliability.”改变 train distributed training 的可观察机制或决策边界；exact-v1 的证明范围限于“Testbed experiments and ns-3 simulations show that CSA-UD significantly reduces tail latency under large-scale collective communication.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO
- Status: `root_writeback_ready_after_independent_audit`
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, changed constraint, state/control ownership, trade-off, failure mode, evidence boundary and coexistence fallback.
