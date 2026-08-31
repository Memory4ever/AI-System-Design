# 2026-05-06 Books Writeback Queue

本 author lane 未修改共享 Books。Root 已将 27 项写入目标章节；不同 reviewer 的 post-write semantic audit 已物化为 `post-write-semantic-audit.json`，当前结果为 `Open`。

- Presence: `27/27` 均在目标 owner 的 `Review notes` 之前找到。
- Passed: `27/27` 已进入知识树/演进总结/小结之前的章节主干；Ch72、Ch66、Ch24 与 Ch26 的 finding 均已修复并通过独立复验。
- Queue status: `27 Integrated / Audited`；post-write Books scope=`Passed`。Report-level Books Gate 仍因 Coverage/Evidence 的两项 exact-v1 blocker 与其他独立 audit scope 保持 `Open`。

- Queue count: 27

## SF-2026-ARXIV-2605-03309
- Primary: `arXiv:2605.03309v1`
- Owner: `PLATFORM-SECURITY`
- Target: `books/part-06-ai-infrastructure/72-security.md`
- Delta: artifact distribution needs cryptographic registry identity, publisher/registry countersignatures and namespace-bound fail-closed resolution
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-03314
- Primary: `arXiv:2605.03314v1`
- Owner: `AGENT-CONTEXT`
- Target: `books/part-07-agent/75-context.md`
- Delta: public disclosure is an irreversible commitment distinct from private reasoning state, so visibility timing becomes a learned control decision with an entailment gate
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-03327
- Primary: `arXiv:2605.03327v1`
- Owner: `TRAIN-GRPO`
- Target: `books/part-04-training-system/33-grpo.md`
- Delta: fine-grained reasoning credit can be redistributed from sequence reward with a bounded distributional distance and an entropy gate, trading additional statistics and calibration for less diffuse token updates
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-03425
- Primary: `arXiv:2605.03425v1`
- Owner: `TRAIN-PRETRAINING`
- Target: `books/part-04-training-system/28-pretraining.md`
- Delta: gradient filtering under differential privacy changes the noise statistics consumed by AdamW state, so optimizer bias correction must be derived from the filter rather than reused from unfiltered DP-SGD
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-03562
- Primary: `arXiv:2605.03562v1`
- Owner: `INFER-KV-CACHE`
- Target: `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`
- Delta: KV quantization error must be measured in attention-visible score/readout coordinates rather than raw storage MSE, with distinct K and V operators
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-03596
- Primary: `arXiv:2605.03596v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md`
- Delta: workspace-agent evaluation must preserve cross-file dependency state and score both reads and mutations against a real workspace graph rather than treating files as independent prompt attachments
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-03644
- Primary: `arXiv:2605.03644v1`
- Owner: `INFER-KV-CACHE`
- Target: `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`
- Delta: adaptive many-shot inference couples example selection with reusable prefix KV state, making context admission a joint quality-memory-latency decision rather than a fixed shot count
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-03667
- Primary: `arXiv:2605.03667v1`
- Owner: `TRAIN-PRETRAINING`
- Target: `books/part-04-training-system/28-pretraining.md`
- Delta: low-rank pretraining becomes hardware-useful only when the factorization is co-designed with supported structured activation sparsity; mathematical compression alone does not guarantee realized training throughput
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-03677
- Primary: `arXiv:2605.03677v1`
- Owner: `TRAIN-RLHF`
- Target: `books/part-04-training-system/31-rlhf.md`
- Delta: on-policy distillation needs both exploration of informative student states and reliability-aware teacher supervision, so teacher outputs are conditional feedback rather than unconditional labels
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-03884
- Primary: `arXiv:2605.03884v1`
- Owner: `AGENT-MULTI-AGENT`
- Target: `books/part-07-agent/82-multi-agent.md`
- Delta: cross-agent latent handoff needs a versioned CacheCard carrying quantized KV state, bit allocation and receiver injection metadata, while prefix alignment and fused execution remain unresolved
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04116
- Primary: `arXiv:2605.04116v1`
- Owner: `PLATFORM-SECURITY`
- Target: `books/part-06-ai-infrastructure/72-security.md`
- Delta: retrieval-selected in-context examples create a remotely observable membership channel, so example-store privacy belongs to the serving threat model
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04135
- Primary: `arXiv:2605.04135v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md`
- Delta: capability claims must bind model release, elicitation, tools and evaluation date because frontier lag can turn a valid historical measurement into a misleading current-system conclusion
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04209
- Primary: `arXiv:2605.04209v1`
- Owner: `PLATFORM-SECURITY`
- Target: `books/part-06-ai-infrastructure/72-security.md`
- Delta: model artifacts can carry statistically hidden parameter backdoors whose detectability is bounded by the attack distribution, extending supply-chain verification beyond file hashes and conventional weight scanning
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04213
- Primary: `arXiv:2605.04213v1`
- Owner: `PLATFORM-MONITORING`
- Target: `books/part-06-ai-infrastructure/67-monitoring.md`
- Delta: silent GPU corruption needs empirically grounded fault models tied to operation type and propagation pattern; generic random bit flips can invalidate resilience conclusions for large-scale training
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04215
- Primary: `arXiv:2605.04215v1`
- Owner: `MULTIMODAL-GENERATIVE-PARADIGMS`
- Target: `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`
- Delta: fixed-length diffusion generation turns response-length prediction into an admission-time compute budget with explicit underprediction retry risk
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04256
- Primary: `arXiv:2605.04256v1`
- Owner: `AGENT-MCP`
- Target: `books/part-07-agent/83-mcp.md`
- Delta: heterogeneous physical neural substrates require a typed control plane for capability discovery, timing, observation, actuation and safety rather than presenting every device as an interchangeable tool
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04263
- Primary: `arXiv:2605.04263v1`
- Owner: `INFER-SPECULATIVE-DECODING`
- Target: `books/part-05-inference-system/48-speculative-decoding.md`
- Delta: semantic speculative generation can verify multiple draft prefixes in one target pass, but must preserve a maximal valid commit boundary distinct from token-exact acceptance
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04266
- Primary: `arXiv:2605.04266v1`
- Owner: `TRAIN-RLHF`
- Target: `books/part-04-training-system/31-rlhf.md`
- Delta: iterative RLHF creates a policy-to-future-reward-model feedback loop; omitting parameter steering allows self-reinforcing reward-model exploitation
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04269
- Primary: `arXiv:2605.04269v1`
- Owner: `TRAIN-PRETRAINING`
- Target: `books/part-04-training-system/28-pretraining.md`
- Delta: under nonstationary objectives Adam's adaptive state trades faster tracking for longer optimizer memory, whereas SGD forgets differently; optimizer choice therefore depends on drift, projection and stationarity assumptions
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04333
- Primary: `arXiv:2605.04333v1`
- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Target: `books/part-04-training-system/36-distributed-training.md`
- Delta: large synchronous training networks need multipath transport, redundant Clos planes and explicit failure handling because tail latency and flow collisions dominate collective completion at scale
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04341
- Primary: `arXiv:2605.04341v1`
- Owner: `TRAIN-LORA`
- Target: `books/part-04-training-system/30-lora.md`
- Delta: parameter-efficient adaptation reduces training cost but not dense inference cost; budgeted distillation must allocate structural rank or compute under a deployment budget to produce an actually cheaper student
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04357
- Primary: `arXiv:2605.04357v1`
- Owner: `INFER-SCHEDULING`
- Target: `books/part-05-inference-system/56-inference-scheduling.md`
- Delta: heterogeneous multi-model serving must co-optimize model placement and resource allocation under per-model SLOs, separating offline serving templates from online allocation
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04361
- Primary: `arXiv:2605.04361v1`
- Owner: `AGENT-CONTEXT`
- Target: `books/part-07-agent/75-context.md`
- Delta: context artifacts have task-dependent crossover effects, so context admission must estimate marginal decision value and interference rather than assume that more relevant context monotonically helps
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-04375
- Primary: `arXiv:2605.04375v1`
- Owner: `AGENT-WORKFLOW`
- Target: `books/part-07-agent/81-workflow.md`
- Delta: physical experiments need declarative experiment-as-code that binds instrument capabilities, execution state, provenance and human safety approval, extending durable workflow semantics beyond digital tools
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-05248
- Primary: `arXiv:2605.05248v1`
- Owner: `AGENT-WORKFLOW`
- Target: `books/part-07-agent/81-workflow.md`
- Delta: turning generated symbolic structure into executable code is an authority-amplifying materialization effect that requires capability, policy and resource admission
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-08190
- Primary: `arXiv:2605.08190v1`
- Owner: `MULTIMODAL-EMBODIED-VLA`
- Target: `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`
- Delta: runtime assurance may consume ML outputs only under formally derived cooperative monitor conditions and a verified safe fallback
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.

## SF-2026-ARXIV-2605-08192
- Primary: `arXiv:2605.08192v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md`
- Delta: frontier-safety release claims need reproducible artifacts, configuration disclosure and independent rerun conditions; authority or venue cannot substitute for an inspectable evaluation contract
- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.
