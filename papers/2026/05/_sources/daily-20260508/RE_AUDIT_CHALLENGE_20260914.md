# 2026-05-08 denominator challenge and repair

**Role:** challenge/re-audit author, not the final independent reviewer

**Scope:** six source families challenged from the previous 537 pre-denominator closures

**Result:** all six are retained after title + complete-abstract rebuttal and exact-v1 review. The canonical accounting is now `619 = 88 retained + 531 closure`; all 88 retained candidates have a terminal Evidence Review, with `Review Pending = 0`.

This document records a repair, not a final sign-off. Four new Books changes remain queued for the root integration owner, and the completed date must then be reviewed by an agent that has never authored or challenged 2026-05-08.

## Reopened source families

### 2605.05258 — PARNESS

- **Why retained:** the paper changes workflow ownership rather than merely presenting a research assistant. The user owns an editable YAML DAG; each node exposes a typed four-field Agent contract; verifier output, full-text/figure/table indexes and a cross-run knowledge graph become explicit durable state.
- **Exact-v1 locators:** §5.1–5.3 and §6.2/§6.3/§6.7 define the dynamic workflow, Agent contracts, verifier/index pipeline and cross-run accumulation.
- **Evaluation:** §8 validates workflow execution, recovery and system tests. It does not establish scientific-output superiority.
- **Boundary:** §9 reports no shared-task head-to-head comparison, no human evaluation of final paper quality and no ablation isolating cognitive roles.
- **Score:** `3 + 3 + 3 = 9`; deep review.
- **Books:** `No Change — Existing Coverage → AGENT-WORKFLOW`. Ch81 already owns editable/versioned DAGs, typed transitions, template-versus-realized graphs, replay and rollback. PARNESS is a concrete system instance rather than a new owner.

### 2605.05365 — ZAYA1-8B Technical Report

- **Why retained:** Markovian RSA replaces a single ever-growing reasoning trace with an explicitly carried bounded tail and batched reasoning stages. The report also makes rollout/trainer numerical identity and stale mixed-policy length bias part of the training-serving contract.
- **Exact-v1 locators:** §II describes the model architecture; §IV describes PipelineRL and BF16/selected-FP32 numerical consistency between vLLM rollout and trainer; §VI defines Markovian RSA and bounded carried state; §VII gives limitations and the stale-policy length-bias failure.
- **Evaluation:** the report evaluates the disclosed 8B system and its staged reasoning configuration. It does not provide a matched full-chain comparison against every alternative, and the disclosed multi-round setting still pays a large total decode budget.
- **Boundary:** evidence is limited to the reported scale and DP+CP setup; bounded context is not bounded total work.
- **Score:** `3 + 3 + 2 = 8`; deep review.
- **Books:** `Integrate — Queued → INFER-SCHEDULING`; precise queue in `BOOKS_WRITEBACK_QUEUE_CHALLENGE.md`.

### 2605.06599 — Weight-Decay Turns Transformer Loss Landscapes Villani

- **Why retained:** the paper turns weight decay from a heuristic into a conditional geometry statement: under bounded-input and positive-regularization assumptions, the regularized loss becomes coercive and admits functional-inequality consequences relevant to Langevin/PAC-Bayes analyses.
- **Exact-v1 locators:** Theorem 1 and the surrounding derivation establish the Villani/coercivity conditions; §VI evaluates GPT-Neo-125M on Penn Treebank and WikiText-103; §VII-A states the limits.
- **Evaluation:** one A100-80GB, BF16 with FP32 master weights, one small decoder-only model and two language-modeling corpora.
- **Boundary:** constants depend on regularization strength, dimension and sequence length; the theory assumes uniform decay and tuned temperature, has loose high-dimensional constants and is not validated above 7B.
- **Score:** `2 + 2 + 3 = 7`; deep review.
- **Books:** `No Change — Existing Coverage → TRAIN-PRETRAINING`. Ch28 already frames weight decay through geometry, curvature, regularization and stability conditions; the theorem strengthens the evidence boundary without changing the design route.

### 2605.06615 — When and Why SignSGD Outperforms SGD

- **Why retained:** the paper identifies a specific optimizer-selection regime rather than asserting a generic ranking: ell-1 stationarity, ell-infinity smoothness and separable sparse noise can yield a dimensional advantage for sign-based updates, with a matrix analogue connected to Muon.
- **Exact-v1 locators:** §3–4 give the lower/upper bounds and the SignSGD/SGD comparison; §4 also states the matrix analogue; §4.2 contains the nanoGPT experiment.
- **Evaluation:** GPT-2-small 124M, 10K steps, batch 512, sequence length 512 and a learning-rate grid. This is a limited corroborating experiment, not production-scale proof.
- **Boundary:** there is no dedicated limitations section; the theorem assumptions and the single small-model study define the non-proof boundary. The result does not say SignSGD dominates under dense/correlated noise or other geometries.
- **Score:** `3 + 2 + 3 = 8`; deep review.
- **Books:** `Integrate — Queued → TRAIN-PRETRAINING`; precise queue in `BOOKS_WRITEBACK_QUEUE_CHALLENGE.md`.

### 2605.06642 — StraTA

- **Why retained:** StraTA makes a trajectory-level strategy an explicit state object generated from the initial observation and held fixed during the rollout, then separates strategy-group and action-group credit assignment. This changes trajectory identity and the hierarchy of optimization groups.
- **Exact-v1 locators:** §4.1 defines the strategy-conditioned trajectory; §4.2 defines `N` strategies by `M` rollouts and the two levels of grouping; §5 describes ALFWorld, WebShop and SciWorld evaluation through AgentGym.
- **Evaluation:** comparisons include PPO, RLOO, GRPO and GiGPO on the disclosed interactive workloads.
- **Boundary:** the fixed initial strategy can become stale when the environment changes, the `N×M` sampling hierarchy raises rollout cost, and broader environments and production safety are untested.
- **Score:** `2 + 2 + 2 = 6`; deep review because the Books decision is `Integrate`.
- **Books:** `Integrate — Queued → TRAIN-GRPO`; precise queue in `BOOKS_WRITEBACK_QUEUE_CHALLENGE.md`.

### 2605.06650 — Beyond Negative Rollouts / POPO

- **Why retained:** POPO defines a genuine positive-only RLVR branch: a bounded/self-normalized positive-set importance objective, implicit negative logit gradients from the softmax denominator, and an EMA siamese representation anchor replace explicit negative-rollout advantages.
- **Exact-v1 locators:** §3 defines positive-set sampling, bounded importance, implicit negative gradients, the EMA policy and bounded similarity penalty; §4 reports model/task evaluation and ablations; §5 gives limitations.
- **Evaluation:** public mathematical-reasoning benchmarks and Qwen, DeepSeek and Llama families up to 7B, with component ablations.
- **Boundary:** the evidence assumes sparse binary rewards and at least some positive samples; it is text-only, math-focused and limited to 7B. It does not establish superiority under dense rewards, zero-positive batches or broader domains.
- **Score:** `3 + 2 + 2 = 7`; deep review.
- **Books:** `Integrate — Queued → TRAIN-GRPO`; precise queue in `BOOKS_WRITEBACK_QUEUE_CHALLENGE.md`.

## Selection challenge

The six families were sampled from the previous closure strata because their full abstracts contained verbs and state nouns that contradicted the generic closure reason: editable workflow definitions, bounded carried state, functional optimizer conditions, explicit trajectory strategy and positive-only update semantics. All six were false negatives and have been repaired. The repair was bounded to these named challenges; it is not presented as a new whole-corpus false-negative sign-off.

The current denominator still requires a new independent reviewer to perform a stratified closure audit that does not reuse this challenge judgment. No candidate was removed in this repair, so no new false-positive closure was introduced.

## Machine-verifiable checkpoint

- Raw identities: 619.
- Retained/evidence complete: 88/88.
- Pre-denominator closure: 531.
- Withdrawn: 0.
- Review Pending: 0.
- Review depth: 49 deep, 39 standard.
- Score distribution: Total 5 = 16, 6 = 34, 7 = 14, 8 = 16, 9 = 8.
- Books disposition: 33 already applied, 4 newly queued, 51 `No Change — Existing Coverage`.

**Status:** author/challenge repair complete; Daily remains `In Progress` pending root Books writeback and a never-involved non-author final review.
