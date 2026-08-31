# 2026-05-07 Books Writeback Queue

本文件是 date-local queue；本 author lane **未修改共享 Books**。root 必须按日期串行写回并重做章节连贯性检查。

- Queue count: 35
- Writeback status: 35/35 applied and independently accepted by the existing post-write semantic audit.
- `arXiv:2605.04808v1` was recovered after that writeback and resolved `No Change — Existing Coverage`; it does not add a 36th writeback item.

## SF-DEMYSTIFYING-MANIFOLD-CONSTRAINTS-IN-LLM-PRE-TRAINING
- Primary: `arXiv:2605.04418v1`
- Owner: `TRAIN-PRETRAINING`
- Delta: explicit manifold constraints bound activation scale and update geometry rather than acting as an unexplained stabilization heuristic
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-TOWARDS-ROBUST-LLM-POST-TRAINING-AUTOMATIC-FAILURE-MANAGEMENT-FOR-REINFO
- Primary: `arXiv:2605.04431v1`
- Owner: `TRAIN-RLHF`
- Delta: RFT reliability requires observable fault fingerprints plus diagnosis and remediation as a closed training control loop
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-MISROUTER-EXPLOITING-ROUTING-MECHANISMS-FOR-INPUT-ONLY-ATTACKS-ON-MIXTUR
- Primary: `arXiv:2605.04446v1`
- Owner: `PLATFORM-SECURITY`
- Delta: MoE routing is a remotely exploitable safety surface even when attackers can only influence input tokens
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-WHEN-KV-MEETS-EMBEDDINGS-DYNAMIC-GPU-MEMORY-ALLOCATION-FOR-ACCELERATING-
- Primary: `arXiv:2605.04450v1`
- Owner: `INFER-GPU-MEMORY`
- Delta: embedding hot-cache and KV-cache allocation must be co-scheduled as one HBM control problem under tail-latency SLOs
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-STABILIZING-LLM-SUPERVISED-FINE-TUNING-VIA-EXPLICIT-DISTRIBUTIONAL-CONTR
- Primary: `arXiv:2605.04468v1`
- Owner: `TRAIN-SFT`
- Delta: SFT can constrain distribution drift through moving trust-region anchors instead of accepting catastrophic forgetting as a downstream surprise
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-DATA-DEPENDENT-EXPLORATION-FOR-ONLINE-REINFORCEMENT-LEARNING-FROM-HUMAN-
- Primary: `arXiv:2605.04477v1`
- Owner: `TRAIN-RLHF`
- Delta: online preference learning should allocate exploration from historical uncertainty rather than unreliable on-policy estimates alone
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-CCL-D-A-HIGH-PRECISION-DIAGNOSTIC-SYSTEM-FOR-SLOW-AND-HANG-ANOMALIES-IN-
- Primary: `arXiv:2605.04478v1`
- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Delta: collective slow/hang diagnosis needs rank probes, fault fingerprints and remediation ownership inside the training runtime
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-SCOUT-ACTIVE-INFORMATION-FORAGING-FOR-LONG-TEXT-UNDERSTANDING-WITH-DECOU
- Primary: `arXiv:2605.04496v1`
- Owner: `AGENT-CONTEXT`
- Delta: long-context agents need explicit epistemic state and active information acquisition rather than passive context accumulation
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-MAXIMIZING-ROLLOUT-INFORMATIVENESS-UNDER-A-FIXED-BUDGET-A-SUBMODULAR-VIE
- Primary: `arXiv:2605.05262v1`
- Owner: `AGENT-PLANNING`
- Delta: tool-use rollout selection should optimize marginal information under a budget rather than expand a search tree uniformly
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-RANGEGUARD-EFFICIENT-BOUNDED-APPROXIMATE-ERROR-CORRECTION-FOR-RELIABLE-D
- Primary: `arXiv:2605.04563v1`
- Owner: `INFER-TENSORRT-LLM`
- Delta: approximate execution needs an explicit bounded-error correction contract rather than an average-accuracy claim
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-FROM-PARAMETER-DYNAMICS-TO-RISK-SCORING-QUANTIFYING-SAMPLE-LEVEL-SAFETY-
- Primary: `arXiv:2605.04572v1`
- Owner: `PLATFORM-SECURITY`
- Delta: fine-tuning safety degradation can be localized to sample-level parameter dynamics and therefore audited during training
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-AUDITREPAIRBENCH-A-PAIRED-EXECUTION-TRACE-CORPUS-FOR-EVALUATOR-CHANNEL-R
- Primary: `arXiv:2605.04624v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: agent-repair evaluation can become unstable when paired execution traces and evaluator channels disagree
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-PARAPHRASE-INDUCED-OUTPUT-MODE-COLLAPSE-WHEN-LLMS-BREAK-CHARACTER-UNDER-
- Primary: `arXiv:2605.04665v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: semantically equivalent prompts can trigger output-mode collapse, requiring invariance tests in release evaluation
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-FROM-PIXELS-TO-TOKENS-A-SYSTEMATIC-STUDY-OF-LATENT-ACTION-SUPERVISION-FO
- Primary: `arXiv:2605.04678v1`
- Owner: `MULTIMODAL-EMBODIED-VLA`
- Delta: latent action supervision changes the representation bridge between pixels, language and controllable action
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-GRAY-BOX-POISONING-OF-CONTINUOUS-MALWARE-INGESTION-PIPELINES
- Primary: `arXiv:2605.04698v1`
- Owner: `PLATFORM-SECURITY`
- Delta: continuous ingestion turns data poisoning into a persistent supply-chain control problem with delayed effects
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-ELVIS-ENSEMBLE-CALIBRATED-LATENT-IMAGINATION-FOR-LONG-HORIZON-VISUAL-MPC
- Primary: `arXiv:2605.04709v1`
- Owner: `MULTIMODAL-WORLD-MODELS`
- Delta: visual MPC must calibrate ensembles of imagined rollouts before imagined state can safely drive long-horizon control
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-BUDGET-AWARE-AUTO-OPTIMIZER-CONFIGURATOR
- Primary: `arXiv:2605.04711v1`
- Owner: `TRAIN-PRETRAINING`
- Delta: optimizer configuration can be treated as a measured budget-aware control decision rather than a static recipe
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-EVERY-STEP-COUNTS-STEP-LEVEL-CREDIT-ASSIGNMENT-FOR-TOOL-INTEGRATED-TEXT-
- Primary: `arXiv:2605.04719v1`
- Owner: `TRAIN-RLHF`
- Delta: tool-integrated generation needs step-level credit tied to observable effects instead of terminal answer reward alone
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-TEST-TIME-TRAINING-FOR-VISUAL-FORESIGHT-VISION-LANGUAGE-ACTION-MODELS
- Primary: `arXiv:2605.08215v1`
- Owner: `MULTIMODAL-EMBODIED-VLA`
- Delta: VLA visual foresight can adapt at test time, but adaptation state becomes part of the control-loop safety identity
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-TREE-BASED-CREDIT-ASSIGNMENT-FOR-MULTI-AGENT-MEMORY-SYSTEM
- Primary: `arXiv:2605.04811v1`
- Owner: `AGENT-MEMORY`
- Delta: multi-agent memory requires tree-structured credit assignment over shared and delegated state changes
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-RETHINKING-LOCAL-LEARNING-A-CHEAPER-AND-FASTER-RECIPE-FOR-LLM-POST-TRAIN
- Primary: `arXiv:2605.04913v1`
- Owner: `TRAIN-RLHF`
- Delta: local post-training shifts update ownership from end-to-end backpropagation to cheaper layer-local objectives with new consistency costs
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-JACOBIAN-VELOCITY-BOUNDS-FOR-DEPLOYMENT-RISK-UNDER-COVARIATE-DRIFT
- Primary: `arXiv:2605.04932v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: deployment risk under covariate drift needs a Jacobian-sensitive bound rather than IID benchmark extrapolation
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-EP-GRPO-ENTROPY-PROGRESS-ALIGNED-GROUP-RELATIVE-POLICY-OPTIMIZATION-WITH
- Primary: `arXiv:2605.04960v1`
- Owner: `TRAIN-GRPO`
- Delta: GRPO updates can align entropy with verified progress instead of treating entropy as an undirected exploration proxy
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-SEALING-THE-AUDIT-RUNTIME-GAP-FOR-LLM-SKILLS
- Primary: `arXiv:2605.05274v1`
- Owner: `AGENT-PLATFORM`
- Delta: LLM skills require a sealed audit-to-runtime identity so the reviewed artifact is the artifact actually executed
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-SELF-INDUCED-OUTCOME-POTENTIAL-TURN-LEVEL-CREDIT-ASSIGNMENT-FOR-AGENTS-W
- Primary: `arXiv:2605.04984v1`
- Owner: `TRAIN-RLHF`
- Delta: turn-level agent credit can be inferred without external verifiers by using outcome-potential deltas, subject to identifiability limits
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-YOU-SNOOZE-YOU-LOSE-AUTOMATIC-SAFETY-ALIGNMENT-RESTORATION-THROUGH-NEURA
- Primary: `arXiv:2605.04992v1`
- Owner: `PLATFORM-SECURITY`
- Delta: safety alignment restoration after fine-tuning can be modeled as a weight-space repair operation with explicit regression risk
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-UNO-ORCHESTRA-PARSIMONIOUS-AGENT-ROUTING-VIA-SELECTIVE-DELEGATION
- Primary: `arXiv:2605.05007v1`
- Owner: `AGENT-MULTI-AGENT`
- Delta: multi-agent routing should selectively delegate from task and uncertainty state rather than invoke a fixed team
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-PIPER-EFFICIENT-LARGE-SCALE-MOE-TRAINING-VIA-RESOURCE-MODELING-AND-PIPEL
- Primary: `arXiv:2605.05049v1`
- Owner: `TRAIN-DISTRIBUTED-TRAINING`
- Delta: large MoE training needs resource-model-driven pipelined hybrid parallelism that co-owns expert placement and communication
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-AUTOMATICALLY-FINDING-AND-VALIDATING-UNEXPECTED-SIDE-EFFECTS-OF-INTERVEN
- Primary: `arXiv:2605.05090v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: model interventions need systematic validation of unexpected side-effects before release
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-DRIVER-WM-A-DRIVER-CENTRIC-TRAFFIC-CONDITIONED-LATENT-WORLD-MODEL-FOR-IN
- Primary: `arXiv:2605.05092v1`
- Owner: `MULTIMODAL-WORLD-MODELS`
- Delta: driver-centric world models must preserve traffic-conditioned latent state rather than optimize generic video fidelity
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-ROLLOUT-PASS-RATE-CONTROL-STEERING-BINARY-REWARD-RL-TOWARD-ITS-MOST-INFO
- Primary: `arXiv:2605.05112v1`
- Owner: `TRAIN-GRPO`
- Delta: binary-reward RL should control rollout pass rate to keep sampling in an informative regime
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-PARTIAL-EVIDENCE-BENCH-BENCHMARKING-AUTHORIZATION-LIMITED-EVIDENCE-IN-AG
- Primary: `arXiv:2605.05379v1`
- Owner: `PLATFORM-EVALUATION-SYSTEM`
- Delta: agent evaluation must model authorization-limited evidence rather than assume universal access to ground truth
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-FROM-HISTORY-TO-STATE-CONSTANT-CONTEXT-SKILL-LEARNING-FOR-LLM-AGENTS
- Primary: `arXiv:2605.05413v1`
- Owner: `AGENT-WORKFLOW`
- Delta: recurring procedures can move from growing prompts into learned modules while deterministic workflow state remains explicit
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-NITSUM-SERVING-TIERED-LLM-REQUESTS-WITH-ADAPTIVE-TENSOR-PARALLELISM
- Primary: `arXiv:2605.05467v1`
- Owner: `INFER-SCHEDULING`
- Delta: tensor parallelism can become a runtime control surface jointly optimized with PD split and request scheduling
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.

## SF-EDGESERVING-DEADLINE-AWARE-MULTI-DNN-SERVING-AT-THE-EDGE
- Primary: `arXiv:2605.05527v1`
- Owner: `INFER-SCHEDULING`
- Delta: edge multi-model scheduling should optimize system-wide deadline risk across model, early exit and batch decisions
- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.
