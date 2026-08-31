# 2026-05-27 Independent Final Books Writeback Queue

Status: `awaiting_root_serial_writeback`

此文件是非作者 fresh-context 审计后的 canonical pre-write queue；共享 Books 尚未修改。

| Source Family | Owner | Evidence delta |
| --- | --- | --- |
| `SF-2026-ARXIV-2606-07571` | `INFER-KV-CACHE` / `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` | DLM bidirectional attention invalidates the immutable shared-prefix KV assumption and requires depth-scoped refresh. |
| `SF-2026-ARXIV-2606-07581` | `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` | training and serving kernels become explicit versioned execution identities with divergence clauses and promotion actions. |
| `SF-2026-ARXIV-2605-26433` | `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` | derived hidden-state vectors become separately governed privacy artifacts because protection of one exported representation does not protect other pooled representations |
| `SF-2026-ARXIV-2605-26461` | `PLATFORM-GPU-SCHEDULER` / `books/part-06-ai-infrastructure/63-gpu-scheduler.md` | GPU sharing needs fault-domain ownership: MMU isolation contains address faults while runtime recovery reconstitutes MPS clients after fatal SM faults |
| `SF-2026-ARXIV-2605-26497` | `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` | authorization is checked against parameter provenance by comparing clean-intent and executed information-flow graphs. |
| `SF-2026-ARXIV-2605-26508` | `AGENT-TOOL-CALLING` / `books/part-07-agent/78-tool-calling.md` | side-effecting tool calls gain a pre-action counterfactual risk budget, fixed safe default and underwriting boundary rather than relying on post-hoc liability review |
| `SF-2026-ARXIV-2605-26521` | `AGENT-WORKFLOW` / `books/part-07-agent/81-workflow.md` | workflow testing gains structural obligations for agents, allowed/restricted tools and delegation edges, separate from task success. |
| `SF-2026-ARXIV-2605-26542` | `AGENT-TOOL-CALLING` / `books/part-07-agent/78-tool-calling.md` | tool-chain authority becomes value-scoped and monotonically attenuated, closing permission laundering across locally legal calls. |
| `SF-2026-ARXIV-2605-26667` | `AGENT-MEMORY` / `books/part-07-agent/77-memory.md` | memory evaluation decomposes summary, storage and retrieval failures instead of treating memory as one black-box accuracy score. |
| `SF-2026-ARXIV-2605-26754` | `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` | RAG poisoning control removes untrusted prose from the synthesis principal and passes only audited claims across the boundary. |
| `SF-2026-ARXIV-2605-26778` | `AGENT-RAG` / `books/part-07-agent/76-rag.md` | grounded output must distinguish retrieved-context causation from coincident parametric-memory recall. |
| `SF-2026-ARXIV-2605-27220` | `AGENT-RAG` / `books/part-07-agent/76-rag.md` | production RAG routes augmentation after measuring retrieval sufficiency and traces post-retrieval cascades instead of applying augmentation globally. |
| `SF-2026-ARXIV-2605-27328` | `AGENT-PLATFORM` / `books/part-07-agent/84-agent-platform.md` | self-modifying agent harnesses require versioned executable artifacts, capability lifecycle state, governance approval and rollback instead of ungoverned prompt/code mutation |
| `SF-2026-ARXIV-2605-27480` | `PLATFORM-COST` / `books/part-06-ai-infrastructure/70-cost.md` | serving externality accounting needs a functional unit and quality-aware biodiversity impact identity, because carbon and water metrics do not proxy every lifecycle impact |
| `SF-2026-ARXIV-2605-27488` | `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` | agent trust enforcement moves below application code into eBPF-mediated, channel-attested communication. |
| `SF-2026-ARXIV-2605-27492` | `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` | production agent assessment preserves runtime state and uses resurrection artifacts to separate upstream cascade from downstream capability. |
| `SF-2026-ARXIV-2605-27494` | `AGENT-RAG` / `books/part-07-agent/76-rag.md` | answer-cache reuse is committed only against fresh evidence identity, version and support, with regeneration as fallback. |
| `SF-2026-ARXIV-2605-27566` | `PLATFORM-GPU-SCHEDULER` / `books/part-06-ai-infrastructure/63-gpu-scheduler.md` | dynamic-scheduling benchmarks must calibrate static baselines and distinguish controller quality from the observability and workload contract exposed to an LLM agent |
| `SF-2026-ARXIV-2605-27599` | `PLATFORM-MONITORING` / `books/part-06-ai-infrastructure/67-monitoring.md` | process-level energy attribution is impossible without an observable hardware counter and attribution boundary; utilization or board power are not equivalent evidence |
| `SF-2026-ARXIV-2605-27678` | `TRAIN-DISTRIBUTED-TRAINING` / `books/part-04-training-system/36-distributed-training.md` | multimodal modules receive independent parallel layouts while boundary communicators own forward activation and reverse-gradient transforms. |
| `SF-2026-ARXIV-2605-27712` | `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` | prefix-safe belief tracking separates probability calibration from candidate ranking and prevents future evidence from leaking into earlier confidence checkpoints |
| `SF-2026-ARXIV-2605-27744` | `AGENT-PLATFORM` / `books/part-07-agent/84-agent-platform.md` | a typed agent runtime tier mediates framework semantics and engine events so cross-layer serving policies have one owner. |
| `SF-2026-ARXIV-2605-27763` | `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` | batch condition and kernel path enter the safety evaluation identity through paired exact-stack tests and capability controls. |
| `SF-2026-ARXIV-2605-27784` | `AGENT-PLATFORM` / `books/part-07-agent/84-agent-platform.md` | long-lived prompt policies require executable collision witnesses and resolution profiles so rule precedence and tool-interface effects can be regression tested |
| `SF-2026-ARXIV-2605-27785` | `PLATFORM-LOGGING` / `books/part-06-ai-infrastructure/68-logging.md` | agent traces become a queryable evidence plane through a client-native engine that combines relational scans with bounded model operators. |
| `SF-2026-ARXIV-2605-27789` | `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` | LLM-judge comparisons need fixed evidence and answer budgets, cluster-aware inference, preregistered hypotheses and second-judge replication |

每项写回后必须由另一位非写作者完成 post-write semantic audit；在此之前 Books Gate 保持 Open。
