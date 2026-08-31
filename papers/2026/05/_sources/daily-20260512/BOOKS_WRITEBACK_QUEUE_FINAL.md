# 2026-05-12 Books Writeback Queue — Final Prewrite Challenge

**State:** 既有 7 项 post-write semantic audit 保持通过；恢复的第 8 项等待 root 串行写回，Report-level Books Gate=`Open`。

47 个 provisional Integrate 经 current owner + adjacent semantic-body challenge 收紧为 7；恢复 exact-v1 后，最终状态为 8 个 `Integrate`、68 个 `No Change`、0 blocker。既有 7 项 post-write audit 仍有效；第 8 项必须由 root 串行写回并接受新的独立 post-write audit。

## `TRAIN-DATA`

Target: `books/part-04-training-system/27-data.md`

- `SF-2026-ARXIV-2605-09994` / arXiv:2605.09994v1
  - Delta: 现有 Ch27 已有 immutable manifest 与消费 cursor，但尚未把对象存储中跨 producer/consumer 的全局 batch 作为原子发布、可见性与回收的共同 commit unit；应补入 batch-level atomic publication，并保留 manifest 协调、读放大与 GC 状态代价。
  - Evidence: `RP-f0ca25ae8a6b899b`；`BOOKS-REVIEW-20260512-2605-09994`
  - Non-proof: The exact-v1 body supports the mechanism under §7 Evaluation. Counterevidence/scope was checked at No dedicated limitations section; the disclosed object-store and 64-GPU workloads bound the claim. It does not prove that “BatchWeave: A Consistent Object-Store-Native Data Plane for Large Foundation Model Training” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

## `MULTIMODAL-REPRESENTATION`

Target: `books/part-03-multimodal-world-models/23-multimodal-representation.md`

- `SF-2026-ARXIV-2605-10199` / arXiv:2605.10199v1
  - Delta: 现有 Ch23 已有 modality stream、timestamp 与融合，但尚未处理 assistant 正在生成时并发 user stream 的路由：channel fusion 与 external cross-attention 改变 interruption latency、生成一致性和状态归属。
  - Evidence: `RP-bb8a7937c7e36960`；`BOOKS-REVIEW-20260512-2605-10199`
  - Non-proof: The exact-v1 body supports the mechanism under §6.1–§6.4 Experiments. Counterevidence/scope was checked at §8 Limitations. It does not prove that “How Should LLMs Listen While Speaking? A Study of User-Stream Routing in Full-Duplex Spoken Dialogue” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

## `TRAIN-DISTRIBUTED-TRAINING`

Target: `books/part-04-training-system/36-distributed-training.md`

- `SF-2026-ARXIV-2605-10501` / arXiv:2605.10501v1
  - Delta: 现有 Ch36 覆盖 collective、topology 与并行策略，但尚未把参数规模、forward-only/forward-backward、序列长度及 input-conditioned activation 不同的 compound sections 视为需要各自 execution config 的运行时计划状态。
  - Evidence: `RP-b63d7ff4cbce83b5`；`BOOKS-REVIEW-20260512-2605-10501`
  - Non-proof: The exact-v1 body supports the mechanism under §4 Evaluations and Case Study (§4.1 VLM training, §4.2 distillation). Counterevidence/scope was checked at No dedicated limitations section; the disclosed compound workloads, cluster and framework integration bound the result. It does not prove that “Accelerating Compound LLM Training Workloads with Maestro” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.
- `SF-2026-ARXIV-2605-11215` / arXiv:2605.11215v1
  - Delta: 现有 Ch36 已有 checkpoint、elastic recovery 与 failure state，但尚未保留固定 microbatch count 这一 in-step recovery invariant，用来维持每次迭代梯度与 failure-free run 的随机等价边界。
  - Evidence: `RP-82750fbea40cd4b8`；`BOOKS-REVIEW-20260512-2605-11215`
  - Non-proof: The exact-v1 body supports the mechanism under §5 Evaluation; Appendix A additional evaluation. Counterevidence/scope was checked at No dedicated limitations section; disclosed training frameworks, failure model and cluster configurations bound the claim. It does not prove that “ReCoVer: Resilient LLM Pre-Training System via Fault-Tolerant Collective and Versatile Workload” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

合并叙事：compound section 的 execution-plan state 先扩展正常执行配置空间；partial failure 随后要求 recovery 在该计划内保持 fixed-microbatch gradient invariant。两项必须写成同一条 execution→failure→recovery 演进链。

## `INFER-DYNAMO`

Target: `books/part-05-inference-system/52-dynamo.md`

- `SF-2026-ARXIV-2605-10670` / arXiv:2605.10670v1
  - Delta: 现有 Ch52 已有 distributed request/state/control path 与部分故障边界，但未把 live membership 收缩、expert coverage 修复和 CUDA-graph execution identity 作为宽 EP MoE partial-rank recovery 的联合 runtime contract。
  - Evidence: `RP-2c6f98138c9d3d63`；`BOOKS-REVIEW-20260512-2605-10670`
  - Non-proof: The exact-v1 body supports the mechanism under Evaluation sections on failure/recovery and serving overhead. Counterevidence/scope was checked at §3.1 Failure Model and Scope; no claim beyond disclosed partial-rank failures and redundant expert state. It does not prove that “Surviving Partial Rank Failures in Wide Expert-Parallel MoE Inference” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

## `INFER-TENSORRT-LLM`

Target: `books/part-05-inference-system/49-tensorrt-llm.md`

- `SF-2026-ARXIV-2605-10875` / arXiv:2605.10875v1
  - Delta: 现有 Ch49 分别讨论 activation sparsity 与 mixed precision，但尚未形成按 token 联合控制 attention sparsity、structured pruning 与 precision 的质量/算力预算控制器。
  - Evidence: `RP-d0dacfe66096e3b3`；`BOOKS-REVIEW-20260512-2605-10875`
  - Non-proof: The exact-v1 body supports the mechanism under §5 Experiments and ablations. Counterevidence/scope was checked at No dedicated limitations section; evaluated models, accelerator and policy-action space bound the runtime conclusion. It does not prove that “Compute Where it Counts: Self Optimizing Language Models” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

## `PLATFORM-MONITORING`

Target: `books/part-06-ai-infrastructure/67-monitoring.md`

- `SF-2026-ARXIV-2605-11093` / arXiv:2605.11093v1
  - Delta: 现有 Ch67 已有 metrics、probes 与 activation-monitor validation，但尚未把模型内部 tensor capture 通过异步 GPU→CPU staged sensor substrate 从 inference hot path 解耦，并作为 policy-controlled observability contract。
  - Evidence: `RP-00677d6b789019a8`；`BOOKS-REVIEW-20260512-2605-11093`
  - Non-proof: The exact-v1 body supports the mechanism under §6 Evaluation; §7 Use Cases. Counterevidence/scope was checked at No dedicated limitations section; model/runtime integrations and probes disclosed in §6–§7 bound overhead and coverage. It does not prove that “Enabling Performant and Flexible Model-Internal Observability for LLM Inference” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

## `PLATFORM-SECURITY` — waiting for root serial writeback

Target: `books/part-06-ai-infrastructure/72-security.md`

- `SF-2026-ARXIV-2605-10133` / arXiv:2605.10133v1
  - Delta: Current Ch72 treats prompt, code, package and tool outputs as untrusted inputs, and already requires independent effect-time verification, but it does not yet make the developer requirement itself a versioned supply-chain input. The durable addition is to carry explicit security invariants from requirement admission through code proposal and dual functional/security verification; the coding model owns only the proposal, while policy/CI and the repository owner retain merge authority.
  - Evidence: `RP-0c0df531268b04c2`；`BOOKS-REVIEW-20260512-2605-10133`
  - Non-proof: Requirement intake is a security boundary: a coding model may preserve secure behavior under the original task yet drop implicit security constraints when explicit functionality, implementation or trade-off wording becomes the higher-salience objective. The exact-v1 evidence supports this failure mode only for the disclosed benchmark, models, attack generator/judge and verification protocol; it does not prove all issue-tracker requests are adversarial, all coding models fail, the internal cause is identified, or the proposed defenses are effective.
  - Required flow: trusted/internal requirement intake → mixed-trust requirement artifact → explicit security invariants → model code proposal → functional/security effect checks → repository-owner commit；failure 时回退 human review、SAST 或 approved templates。
