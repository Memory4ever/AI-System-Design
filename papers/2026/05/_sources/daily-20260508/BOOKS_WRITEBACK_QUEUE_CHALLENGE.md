# 2026-05-08 challenge Books writeback queue

This queue contains only the four source families reopened by the 2026-09-14 denominator challenge whose exact-v1 evidence changes a durable Books proposition. It does not modify shared Books and does not claim the writeback is applied.

## SF-2026-ARXIV-2605-05365 — ZAYA1-8B / Markovian RSA

- **Canonical owner:** `INFER-SCHEDULING`, Ch56.
- **Adjacent handoff:** Ch44 decode owns per-token execution; Ch56 should own the policy that divides one reasoning job into rounds and carries state between them. Ch33 may briefly reference rollout/trainer consistency but should not duplicate the inference mechanism.
- **Old path:** one autoregressive trace keeps the full history visible. It is simple and preserves every token, but position length and active KV state grow with each reasoning round.
- **Changed constraint:** very long multi-round reasoning needs bounded active context and batched work, while maintaining enough cross-round state to continue coherently.
- **Mechanism/state ownership:** each round consumes a bounded carried tail plus new work, produces a new tail, and commits it as the next round's explicit reasoning state. The scheduler owns round boundaries and batching; the model does not prove that discarded history is irrelevant.
- **Trade-off/failure:** active context becomes bounded, but total decoded tokens can remain very large; tail truncation can lose necessary evidence, and the report lacks a matched full-chain comparison across alternatives.
- **Fallback/coexistence:** use a single full-history trace when the context fits, exact recall matters, or tail sufficiency cannot be certified.
- **Evidence boundary:** exact-v1 §VI; disclosed 8B/DP+CP system only. Do not generalize reported quality or cost beyond its setup.

## SF-2026-ARXIV-2605-06615 — SignSGD conditions

- **Canonical owner:** `TRAIN-PRETRAINING`, Ch28.
- **Adjacent handoff:** keep distributed collective details in Ch36–37; Ch28 owns optimizer geometry and noise assumptions.
- **Old path:** SGD/AdamW operates on magnitude-bearing gradients and remains the general baseline when geometry and noise structure are unknown.
- **Changed constraint:** under coordinate-separable sparse noise and ell-infinity smoothness, magnitude can be a poor signal while the sign remains stable.
- **Mechanism/state ownership:** sign-based updates discard gradient magnitude and optimize an ell-1 stationarity target; the optimizer selection contract must record norm geometry and noise assumptions rather than rank methods by name.
- **Trade-off/failure:** a dimensional advantage is conditional, not universal; correlated/dense noise or incompatible geometry can erase it. The empirical evidence is only GPT-2-small 124M for 10K steps.
- **Fallback/coexistence:** retain SGD/AdamW or another magnitude-aware optimizer when assumptions are unverified; measure optimizer-specific stability before changing a production recipe.
- **Evidence boundary:** exact-v1 §3–4 and §4.2. The paper has no explicit limitations section, so theorem assumptions and experiment scale are the non-proof boundary.

## SF-2026-ARXIV-2605-06642 — StraTA strategy state

- **Canonical owner:** `TRAIN-GRPO`, Ch33.
- **Adjacent handoff:** Ch79 owns inference-time planning; Ch33 owns how strategy and action trajectories are grouped for policy optimization.
- **Old path:** action-level or whole-trajectory returns train a reactive policy without a separately identified high-level strategy object.
- **Changed constraint:** long-horizon Agent tasks need credit assignment across high-level intent and low-level actions, but a single flat group conflates the two.
- **Mechanism/state ownership:** generate a strategy from the initial observation, bind it to the trajectory identity, sample `N` strategies and `M` action rollouts per strategy, and compute strategy-level plus action-level relative objectives.
- **Trade-off/failure:** hierarchical groups expose high-level credit but multiply rollout cost; a strategy frozen at the initial state can become stale after environment changes.
- **Fallback/coexistence:** use reactive GRPO/RLOO or a revisable/receding-horizon strategy when the environment is highly non-stationary or the `N×M` budget is unjustified.
- **Evidence boundary:** exact-v1 §4.1–4.2 and §5; ALFWorld/WebShop/SciWorld only. Do not claim general production-Agent superiority.

## SF-2026-ARXIV-2605-06650 — POPO positive-only RLVR

- **Canonical owner:** `TRAIN-GRPO`, Ch33.
- **Adjacent handoff:** keep reward construction in Ch31–32; Ch33 owns group/sample/update semantics.
- **Old path:** GRPO/PPO-style updates use both positive and negative rollouts to estimate relative advantage. This remains natural when rewards are dense enough and negative samples carry reliable information.
- **Changed constraint:** sparse binary RLVR may spend most capacity on negative rollouts whose advantage signal is noisy or unhelpful.
- **Mechanism/state ownership:** train on a positive subset with bounded/self-normalized importance, obtain implicit negative token gradients through the softmax normalizer, and constrain representation drift with an EMA siamese anchor plus bounded similarity penalty.
- **Trade-off/failure:** the branch reduces dependence on explicit negative-rollout advantage but fails when a batch has no positives, adds an EMA/reference path, and may not transfer to dense rewards or non-math domains.
- **Fallback/coexistence:** retain standard GRPO/PPO when reward density, negative-example information or domain shift makes the positive-only assumptions invalid.
- **Evidence boundary:** exact-v1 §3–5; public math benchmarks, text-only models up to 7B. No general large-scale or cross-domain result.

**Writeback state:** applied by root on 2026-09-14. The four source-family markers and their mechanism bodies are present in Ch56, Ch28 and Ch33; a never-involved reviewer must still verify each owner body and adjacent handoffs before the Daily can become Complete.
