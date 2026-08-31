# 2026-05-04 Books Writeback Queue

Author lane only. Root must serialize by event date and perform independent Books writeback review.

## SF-2026-ARXIV-2605-02960 — MoE-Prefill: Zero Redundancy Overheads in MoE Prefill Serving

- Owner: `INFER-PREFILL`
- Target: `books/part-05-inference-system/43-prefill.md`
- Adjacent comparison: `Ch21/Ch56`
- Durable delta: Prefill-only MoE workloads can exchange activation all-to-all for asynchronous expert-weight all-gather when long compute windows hide transfer; the saturation threshold and traffic drift become routing state.
- Evidence boundary: Applicability/limitations: prefill-only, batch-driven MoE; low-bandwidth links, bursty arrivals, drift and random prefixes narrow the result.
- Status: `Applied and post-write audited — books/part-05-inference-system/43-prefill.md#L240`

## SF-2026-ARXIV-2605-01708 — SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving

- Owner: `INFER-PD-DISAGGREGATION`
- Target: `books/part-05-inference-system/55-pd-disaggregation.md`
- Adjacent comparison: `Ch45/Ch56`
- Durable delta: Bit-exact KV transfer can exploit exponent redundancy with a fixed dense code plus sparse escape stream, but codec throughput and small-payload overhead must be charged against the PD handoff critical path.
- Evidence boundary: No dedicated limitations section; §4 shows short payloads can lose to fixed overhead and results bind disclosed models, links and precision.
- Status: `Applied and post-write audited — books/part-05-inference-system/55-pd-disaggregation.md#L93`

## SF-2026-ARXIV-2605-01771 — The Compliance Gap: Why AI Systems Promise to Follow Process Instructions but Don't

- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md`
- Adjacent comparison: `Ch69/Ch81`
- Durable delta: Textual agreement cannot prove process compliance; process instructions require observable tool-call traces, environment affordance controls and audit metrics owned outside the model response.
- Evidence boundary: Limitations/forecast: selected tasks, tools and frontier-model APIs do not establish universal rates; text-only observers remain outside the behavior channel.
- Status: `Applied and post-write audited — books/part-06-ai-infrastructure/66-evaluation-system.md#L144`

## SF-2026-ARXIV-2605-01831 — RMGAP: Benchmarking the Generalization of Reward Models across Diverse Preferences

- Owner: `TRAIN-RLHF`
- Target: `books/part-04-training-system/31-rlhf.md`
- Adjacent comparison: `Ch30/Ch32`
- Durable delta: Reward-model evaluation must condition the preferred response on an explicit user preference and test paraphrase consistency; a universal-quality ranking hides whether the reward function generalizes across preference contracts.
- Evidence boundary: §Limitations: intrinsic synthetic English benchmark only; no PPO/DPO downstream validation, real-user preference distribution or cross-cultural coverage.
- Status: `Applied and post-write audited — books/part-04-training-system/31-rlhf.md#L130`

## SF-2026-ARXIV-2605-01989 — DBLP: Phase-Aware Bounded-Loss Transport for Burst-Resilient Distributed ML Training

- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Target: `books/part-04-training-system/36-distributed-training.md`
- Adjacent comparison: `Ch37/Ch41`
- Durable delta: Gradient transport reliability can be phase-aware: bounded packet loss avoids microburst retransmission tails, but the model owns tolerance evidence and the transport owns per-round identity, bitmap and fallback.
- Evidence boundary: PDF p4 notes larger-scale evaluation is future work; fixed detector threshold and empirical 40% tolerance are workload-specific.
- Status: `Applied and post-write audited — books/part-04-training-system/36-distributed-training.md#L613`

## SF-2026-ARXIV-2605-02038 — What Single-Prompt Accuracy Misses: A Multi-Variant Reliability Audit of Language Models

- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Target: `books/part-06-ai-infrastructure/66-evaluation-system.md`
- Adjacent comparison: `Ch20/Ch67`
- Durable delta: A model score is inseparable from prompt variants, confidence normalization, parser and evaluator logic; multi-variant evaluation must retain raw generations and report spread instead of treating one prompt as model identity.
- Evidence boundary: §6: observational 1–8B English multiple-choice corpus, uneven families, one vLLM/bfloat16/L4 stack and two verbal-confidence phrasings; no causal training/scaling claim.
- Status: `Applied and post-write audited — books/part-06-ai-infrastructure/66-evaluation-system.md#L156`

## SF-2026-ARXIV-2605-02087 — Model Spec Midtraining: Improving How Alignment Training Generalizes

- Owner: `TRAIN-PRETRAINING`
- Target: `books/part-04-training-system/28-pretraining.md`
- Adjacent comparison: `Ch29/Ch31`
- Durable delta: Teaching a model the rationale and content of a behavior spec before demonstration alignment changes how underspecified examples generalize; the spec corpus becomes a versioned training artifact and a new mis-specification surface.
- Evidence boundary: §7: synthetic specs, selected Qwen models and narrow AFT settings do not prove broad value alignment or resistance to deceptive specifications.
- Status: `Applied and post-write audited — books/part-04-training-system/28-pretraining.md#L541`
