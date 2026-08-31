# 2026-06-28 Candidate Denominator Fresh Audit

- Window: `[2026-06-27 09:00, 2026-06-28 09:00)` Asia/Shanghai.
- Denominator: `daily-v2.1:2026-06-28:20c51e943aacc58d`.
- Frozen arithmetic: `211 raw identities = 65 retained + 146 family-specific pre-denominator closures`.
- Retain rate: `30.81%`.
- Routes: Core `152`, keyword `17`, route-negative `42`; all route-negative identities were independently checked and `5` were recovered.
- Initial semantic screening: `211/211` title+abstract rows have an explicit decision and source-family-specific reason.
- Independent fresh-context false-positive / false-negative audit: **Passed** (`211/211` full denominator, `42/42` route-negative, zero unresolved findings).
- Coverage Gate: **Passed**; denominator frozen at `2026-08-29T06:45:00+08:00`.
- Evidence, Selection, Books Gates: **Open**. Retention is permission to inspect exact-v1 primary evidence, not proof of a durable claim.

## Resolved false positives

The provisional `58` retained families included `6` items whose contribution remains model-, task-, domain-, or theory-local after adversarial rereading:

  - `2606.28696`: composition-conditioned image generation is a local model/dataset contribution, not a durable system owner change.
  - `2606.28719`: the two-cache VLM test-time-adaptation recipe is model-local and does not establish a platform memory lifecycle.
  - `2606.28879`: the Adam analysis is generic optimizer theory for nonstationary systems rather than a pretraining-system contract.
  - `2606.28911`: the distributed kernels are specific to quantum-transport operator learning and do not generalize to the book's training topology.
  - `2606.28926`: the probabilistic account of in-context learning is model theory without a durable AI-System control or data owner.
  - `2606.29043`: the sharpness-complexity study is generalization analysis, not a system mechanism or release contract.

## Recovered false negatives

The provisional `153` closures hid `13` durable candidates:

  - `2606.28747` -> `AGENT-WORKFLOW`: alternates proof search with extraction into a reusable theorem library while retaining kernel verification.
  - `2606.28754` -> `PLATFORM-GPU-SCHEDULER`: moves both compute context and data across chiplets under communication feedback instead of moving data alone.
  - `2606.28772` -> `TRAIN-DATA`: shows that majority-vote annotation erases contested safety boundaries and therefore changes the upstream label authority contract.
  - `2606.28862` -> `PLATFORM-EVALUATION-SYSTEM`: separates proposal coverage from query-region binding error and exposes an explicit faithfulness-recall abstention trade-off.
  - `2606.28953` -> `PLATFORM-SECURITY`: filters dirty-label poisoning through unsupervised representation clusters before training without trusting corrupted labels.
  - `2606.28995` -> `MULTIMODAL-EMBODIED-VLA`: places an offline-learned barrier value function in a real-time closed-form safety-filter control path.
  - `2606.28998` -> `TRAIN-DPO`: shows that the checkpoint entering DPO/BoNBoN changes functional and non-functional alignment gains and regressions.
  - `2606.29088` -> `PLATFORM-EVALUATION-SYSTEM`: constructs a diff-based corruption pipeline and a much larger bug-fixing evaluation surface that exposes failures hidden by small benchmarks.
  - `2606.29097` -> `PLATFORM-EVALUATION-SYSTEM`: links scenario synthesis, validation, collision discovery, and retraining into an autonomous-driving evaluation loop.
  - `2606.29112` -> `PLATFORM-SECURITY`: detects a latent-class poisoning attack post-training through class-subspace orthogonalization without the training set.
  - `2606.29119` -> `PLATFORM-EVALUATION-SYSTEM`: adds a pre-implementation recovery-ratio gate that can reject an expensive evolutionary outer loop before dispatch.
  - `2606.29124` -> `PLATFORM-SECURITY`: extracts protocol validity constraints from specifications, generates boundary cases, and uses differential execution as the oracle.
  - `2606.29126` -> `AGENT-MULTI-AGENT`: turns multi-agent communication into receiver-driven selection over group, sender, and entity rather than flat-vector broadcast.

## Owner corrections

  - `2606.29066`: `MULTIMODAL-GENERATIVE-PARADIGMS` -> `INFER-DECODE`.
  - `2606.29091`: `WORLDVIEW-REPRESENTATION` -> `AGENT-RAG`.

## Route-negative handoff

All `42` route-negative identities were reread. The frozen denominator retains `5`: `2606.28720` and `2606.29108` from the provisional pass, plus newly recovered `2606.28754`, `2606.28862`, and `2606.28995`. The other `37` remain family-specific pre-denominator closures; no keyword miss is being treated as automatic exclusion.
