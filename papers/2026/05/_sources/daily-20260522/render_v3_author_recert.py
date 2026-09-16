#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the bounded 2026-05-22 V3 repair packet after fresh-review FAIL.

This renderer only writes date-local research artifacts.  It deliberately does
not mutate shared Books; true proposition gaps are serialized for root.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT_DATE = "2026-05-22"
CHECKED_AT = "2026-09-16T09:21:20+08:00"
WINDOW = "[2026-05-21T09:00:00+08:00,2026-05-22T09:00:00+08:00)"
OWNER_RECEIPT = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260522/arxiv-owner-receipt.json"
CANONICAL = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260522/canonical-ledger.json"


RESTORED_IDS = """
2605.21492 2605.21493 2605.21496 2605.21497 2605.21515 2605.21537 2605.21539 2605.21541
2605.21545 2605.21558 2605.21605 2605.21609 2605.21611 2605.21630 2605.21654 2605.21699
2605.21706 2605.21724 2605.21748 2605.21778 2605.21780 2605.21810 2605.21821 2605.21822
2605.21842 2605.21851 2605.21865 2605.21883 2605.21924 2605.21931 2605.21938 2605.21954
2605.21958 2605.21988 2605.21994 2605.22005 2605.22007 2605.22050 2605.22072 2605.22142
2605.22156 2605.22170 2605.22175 2605.22205 2605.22221 2605.22237 2605.22263 2605.22273
2605.22311 2605.22368 2605.22373 2605.22389 2605.22417 2605.22428 2605.22432 2605.22454
2605.22462 2605.22476 2605.22481 2605.22488 2605.22535 2605.22537 2605.22579 2605.22589
2605.22602 2605.22651 2605.22658 2605.22662 2605.22672 2605.22675 2605.22691 2605.22703
2605.22714 2605.22719 2605.22720 2605.22737 2605.22791 2605.22814 2605.22817 2605.22823
""".split()


# The fresh reviewer found three false-positive admissions and sixteen
# false-negative closures.  Keep this delta explicit so rerunning the renderer
# cannot silently restore the failed author corpus.
REMOVED_FALSE_POSITIVES = {
    "2605.21821": (
        "vertical_llm_application_without_transferable_system_delta",
        "ABLE uses an LLM to generate malware-sandbox bypass rules, but the full abstract does not change a reusable model-security, agent-control, or platform interface contract; it is therefore closed below the project contribution denominator.",
    ),
    "2605.22602": (
        "task_asset_without_multi_agent_protocol_delta",
        "The theory-of-mind persuasive-dialogue task, dataset, and local reasoning framework do not introduce multi-agent state, coordination, protocol, or rollback semantics; the prior AGENT-MULTI-AGENT admission was an owner/category error.",
    ),
    "2605.22720": (
        "domain_asset_without_evaluation_contract_delta",
        "The conflict-context scenario suite reports a domain evaluation asset and observed failures, but the full abstract does not introduce a transferable EvalSpec, scorer, release authority, or fallback contract.",
    ),
}

FALSE_NEGATIVE_REPAIRS = {
    "2605.21661": {
        "owner": "MULTIMODAL-GENERATIVE-PARADIGMS", "score": (2, 1, 2),
        "reason": "Old path paid expensive test-time guidance/optimization for reward alignment; the paper changes the constraint by amortizing control into a hierarchical variational stochastic policy with a semi-amortized fallback, forcing a quality-versus-few-step-compute choice.",
    },
    "2605.21674": {
        "owner": "PLATFORM-SECURITY", "score": (2, 2, 2),
        "reason": "Old jailbreak evaluation treated prompts as isolated attacks; THREAT reframes discovery as multi-LLM iterative non-convex search with an explicit attack-cost budget, forcing defenses to own search state, budget, and adaptive-attack evaluation.",
    },
    "2605.21834": {
        "owner": "TRAIN-RLHF", "score": (2, 2, 2),
        "reason": "Offline consistency SFT can memorize surface forms and regress capability; OPCT evaluates the objective on the model's own response distribution, forcing ownership of on-policy state, safety generalization, and capability-regression fallback.",
    },
    "2605.21911": {
        "owner": "MULTIMODAL-GENERATIVE-PARADIGMS", "score": (2, 1, 3),
        "reason": "Empirical fixed noise schedules were selected as presets; the paper makes Fisher information the evolving state and the schedule the control under a KL-error bound, forcing an explicit schedule-control objective and assumption-bounded tuning choice.",
    },
    "2605.22011": {
        "owner": "MULTIMODAL-GENERATIVE-PARADIGMS", "score": (2, 1, 2),
        "reason": "Input-similarity token reduction inherited a discriminative-ViT proxy that can miss generative recovery error; DiTo uses prior-step output similarity plus interval and frequency controls, forcing quality/compute ownership around the generation objective.",
    },
    "2605.22012": {
        "owner": "MULTIMODAL-REPRESENTATION", "score": (2, 2, 2),
        "reason": "Text CoT compresses continuous audio-visual evidence and weakens temporal grounding; LatentOmni interleaves supervised latent sensory states with text and aligned positions, forcing a representation-state and temporal-identity choice rather than language-only reasoning.",
    },
    "2605.22223": {
        "owner": "MODEL-DECODER-ONLY", "score": (3, 1, 3),
        "reason": "The usual path attributes sequence failure to finite context or compute; the paper gives architecture-dependent accessible-sequence bounds that persist with unbounded context/compute, correcting the owner of an expressivity failure and its fallback expectations.",
    },
    "2605.22372": {
        "owner": "MODEL-SELF-ATTENTION", "score": (2, 1, 2),
        "reason": "Local attention-score pruning can preserve uninformative sink tokens; ASAP instead uses cumulative transition state and diffusion distance to the sink, forcing pruning to own attention-flow history and sink-failure detection.",
    },
    "2605.22534": {
        "owner": "PLATFORM-EVALUATION-SYSTEM", "score": (3, 2, 2),
        "reason": "Merge/reject labels were used as direct agent-capability outcomes; interaction traces show workflow constraints and reviewer intervention confound both labels, forcing Evaluation Run identity to include review state and unknown-rationale handling.",
    },
    "2605.22596": {
        "owner": "MULTIMODAL-EMBODIED-VLA", "score": (2, 2, 3),
        "reason": "Separate per-factor policies make task combinations grow multiplicatively; one shared diffusion score composes factors under stated independence and propagates score error into a closed-loop trajectory tube, forcing factor-state ownership and certificate fallback.",
    },
    "2605.22668": {
        "owner": "MULTIMODAL-GENERATIVE-PARADIGMS", "score": (2, 1, 2),
        "reason": "Uniform RoPE scaling trades global structure against fine detail outside the training resolution; SEGA makes latent spectral energy a per-step control signal, forcing dynamic scaling ownership and an out-of-range fallback.",
    },
    "2605.22671": {
        "owner": "MULTIMODAL-EMBODIED-VLA", "score": (2, 2, 2),
        "reason": "Short-horizon latent state and static execution alignment fragment behavior under shift; BehaviorVLA aggregates long-horizon behavior state and decodes actions against live phase progress, forcing state/control separation and closed-loop validation.",
    },
    "2605.22705": {
        "owner": "MODEL-TOKENIZER", "score": (2, 2, 3),
        "reason": "Greedy vocabulary construction and fixed token inference need not minimize corpus token count; ToaST couples split-tree inference to an IP/near-integral LP vocabulary objective, forcing tokenizer construction, runtime segmentation, and context-cost to share one contract.",
    },
    "2605.22765": {
        "owner": "MULTIMODAL-GENERATIVE-PARADIGMS", "score": (3, 1, 3),
        "reason": "UDM commonly feeds a denoising posterior into a plug-in bridge whose ELBO optimizes a different target; the leave-one-out conversion and absorbing reformulation correct objective/reverse-dynamics ownership and force an assumption-bounded sampler choice.",
    },
    "2605.22818": {
        "owner": "MULTIMODAL-GENERATIVE-PARADIGMS", "score": (2, 2, 2),
        "reason": "Rigid execution of sparse, causally incomplete motion paths can create implausible video; MotiMotion adds a reasoner-produced secondary-motion state and confidence-aware guidance, forcing control confidence and correction fallback to be explicit.",
    },
    "2605.22821": {
        "owner": "MODEL-TOKENIZER", "score": (2, 2, 3),
        "reason": "BPE/Unigram make local greedy vocabulary decisions without a global optimality gap; ConvexTok uses a linear-program relaxation and lower-bound certificate, forcing the tokenizer objective and acceptable optimality gap to be owned explicitly.",
    },
}

RESTORED_IDS = [aid for aid in RESTORED_IDS if aid not in REMOVED_FALSE_POSITIVES]
RESTORED_IDS.extend(FALSE_NEGATIVE_REPAIRS)


OWNERS = {
    "2605.21492": "PLATFORM-EVALUATION-SYSTEM", "2605.21493": "PLATFORM-EVALUATION-SYSTEM",
    "2605.21496": "PLATFORM-EVALUATION-SYSTEM", "2605.21497": "PLATFORM-EVALUATION-SYSTEM",
    "2605.21515": "PLATFORM-EVALUATION-SYSTEM", "2605.21537": "AGENT-WORKFLOW",
    "2605.21539": "TRAIN-DATA", "2605.21541": "PLATFORM-SECURITY",
    "2605.21545": "PLATFORM-EVALUATION-SYSTEM", "2605.21558": "TRAIN-SFT",
    "2605.21605": "AGENT-PLATFORM", "2605.21609": "PLATFORM-SECURITY",
    "2605.21611": "MULTIMODAL-REPRESENTATION", "2605.21630": "TRAIN-DATA",
    "2605.21654": "TRAIN-RLHF", "2605.21699": "TRAIN-SFT",
    "2605.21706": "PLATFORM-SECURITY", "2605.21724": "MODEL-TRANSFORMER-LAYER",
    "2605.21748": "PLATFORM-EVALUATION-SYSTEM", "2605.21778": "PLATFORM-EVALUATION-SYSTEM",
    "2605.21780": "PLATFORM-SECURITY", "2605.21810": "AGENT-PLATFORM",
    "2605.21821": "PLATFORM-SECURITY", "2605.21822": "TRAIN-RLHF",
    "2605.21842": "MODEL-SELF-ATTENTION", "2605.21851": "TRAIN-GRPO",
    "2605.21865": "PLATFORM-GATEWAY", "2605.21883": "TRAIN-DPO",
    "2605.21924": "TRAIN-SFT", "2605.21931": "MULTIMODAL-REPRESENTATION",
    "2605.21938": "PLATFORM-SECURITY", "2605.21954": "MULTIMODAL-REPRESENTATION",
    "2605.21958": "AGENT-WORKFLOW", "2605.21988": "MULTIMODAL-REPRESENTATION",
    "2605.21994": "AGENT-RAG", "2605.22005": "PLATFORM-SECURITY",
    "2605.22007": "WORLDVIEW-LLM-INTELLIGENCE", "2605.22050": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.22072": "MULTIMODAL-REPRESENTATION", "2605.22142": "AGENT-MEMORY",
    "2605.22156": "TRAIN-RLHF", "2605.22170": "MULTIMODAL-REPRESENTATION",
    "2605.22175": "PLATFORM-EVALUATION-SYSTEM", "2605.22205": "AGENT-PLATFORM",
    "2605.22221": "AGENT-PLANNING", "2605.22237": "INFER-TENSORRT-LLM",
    "2605.22263": "TRAIN-SFT", "2605.22273": "PLATFORM-SECURITY",
    "2605.22311": "TRAIN-DATA", "2605.22368": "PLATFORM-EVALUATION-SYSTEM",
    "2605.22373": "PLATFORM-SECURITY", "2605.22389": "TRAIN-DATA",
    "2605.22417": "WORLDVIEW-REPRESENTATION", "2605.22428": "MODEL-MOE",
    "2605.22432": "TRAIN-PRETRAINING", "2605.22454": "TRAIN-RLHF",
    "2605.22462": "WORLDVIEW-REPRESENTATION", "2605.22476": "MODEL-SELF-ATTENTION",
    "2605.22481": "PLATFORM-SECURITY", "2605.22488": "WORLDVIEW-REPRESENTATION",
    "2605.22535": "PLATFORM-EVALUATION-SYSTEM", "2605.22537": "TRAIN-GRPO",
    "2605.22579": "TRAIN-SFT", "2605.22589": "TRAIN-DATA",
    "2605.22602": "AGENT-MULTI-AGENT", "2605.22651": "TRAIN-DATA",
    "2605.22658": "WORLDVIEW-REPRESENTATION", "2605.22662": "AGENT-MULTI-AGENT",
    "2605.22672": "PLATFORM-EVALUATION-SYSTEM", "2605.22675": "TRAIN-SFT",
    "2605.22691": "MULTIMODAL-REPRESENTATION", "2605.22703": "TRAIN-GRPO",
    "2605.22714": "PLATFORM-EVALUATION-SYSTEM", "2605.22719": "WORLDVIEW-REPRESENTATION",
    "2605.22720": "PLATFORM-EVALUATION-SYSTEM", "2605.22737": "PLATFORM-SECURITY",
    "2605.22791": "MODEL-LONG-CONTEXT", "2605.22814": "AGENT-MEMORY",
    "2605.22817": "TRAIN-GRPO", "2605.22823": "MULTIMODAL-REPRESENTATION",
}
OWNERS.update({aid: repair["owner"] for aid, repair in FALSE_NEGATIVE_REPAIRS.items()})


AMEL_V1_PROBLEM = (
    "Reusing one evaluator conversation can make the polarity of prior verdicts an undeclared state "
    "that shifts later judgments, especially on baseline-uncertain items."
)
AMEL_V1_ABSTRACT = (
    "Large language models are routinely used as automated evaluators: to review code, moderate content, or score outputs, often with many items passing through one conversation. "
    "We ask whether the polarity of prior conversation history biases subsequent judgments, an effect we call the accumulated message effect on LLM judgments (AMEL). "
    "Across 75,898 API calls to 11 models from 4 providers (OpenAI, Anthropic, Google, and four open-source models run locally), we present identical test items in isolation, or following histories saturated with predominantly positive or negative evaluations. "
    "Models shift their responses toward the conversation's prevailing polarity (d=-0.17, p<10^-46). The effect is concentrated on items where the model is genuinely uncertain at baseline (d=-0.34 for high-entropy items, against d=-0.15 where the baseline is deterministic). "
    "Bias does not grow with context length: 5 prior turns and 50 produce essentially the same shift (Spearman |r|<0.01, p>0.94; linear-slope OLS p=0.80). "
    "Negative histories induce 1.62x stronger bias than positive ones in the v1 paired comparison (t=13.46, p<10^-39, n=2,481 pairs). "
    "Three follow-up experiments narrow the plausible mechanisms but do not isolate a single cause. For evaluation pipelines, the simplest fix is a fresh context per item; when batching is unavoidable, balancing the history helps."
)
AMEL_V1_MECHANISM = (
    "arXiv:2605.22714v1 evaluates identical items in isolation and after polarity-saturated histories "
    "across 75,898 API calls, 11 models, and 4 providers; fresh context is the primary mitigation, "
    "with balanced history only a partial fallback."
)


# Eight score-5/6 restorations completed the contract's standard source review.
# The two other score-6 restorations (2605.21674 and 2605.21834) remain deep
# review pending because they change safety constraints and therefore trigger
# the review override independently of score.
STANDARD_REVIEWS = {
    "2605.21661": {
        "adopted": "Amortizing reward guidance into a learned initial-noise policy and per-step stochastic controls moves cost from repeated test-time optimization to one-time training; semi-amortized refinement is the quality fallback when amortization error is unacceptable.",
        "method": "arXiv:2605.21661v1 HTML §2.1–§2.3 (HVP, policy learning, AHVP)",
        "evaluation": "§3 Experiments; §3.1 Main Results; §3.2 Ablations; held-out FFHQ/ImageNet inverse-problem protocol",
        "nonproof": "§5 Conclusion; known differentiable likelihood/reward assumption in §2.1; finite amortization error and semi-amortized fallback in §2.3",
        "boundary": "Evidence is limited to disclosed differentiable inverse-problem rewards, fixed pretrained denoisers, FFHQ/ImageNet-256 tasks, and the reported quality/runtime protocol; it does not prove arbitrary non-differentiable rewards or deployment SLOs.",
    },
    "2605.21911": {
        "adopted": "Noise-schedule selection can be posed as optimal control with Fisher information as state and the schedule as control, but its KL-error guarantee is conditional on the paper's regularity and score-estimation assumptions.",
        "method": "arXiv:2605.21911v1 HTML §2.1 Noise Schedule Optimization; §3.1 Optimal Control Formulation; §3.2 Noise Schedule Design",
        "evaluation": "§5 Experiments; Appendix G.1–G.3 (ACS parameters, experiment details, constant-schedule trade-offs)",
        "nonproof": "§2.1 regularity assumption; Appendix B.2 non-zero score-matching error; §6 Conclusion",
        "boundary": "The adopted claim is the state/control formulation and assumption-bounded error analysis, not a universal guarantee that the derived schedule is optimal for every data distribution, learned score, sampler, or production workload.",
    },
    "2605.22011": {
        "adopted": "For diffusion token reduction, prior-step output similarity is a better proxy for recovery error than input similarity alone; interval scheduling and frequency penalties explicitly trade matching overhead against accumulated reuse error.",
        "method": "arXiv:2605.22011v1 HTML §3.2 objective formulation; §4.1–§4.3 (output similarity, PMR interval, frequency-aware matching)",
        "evaluation": "§5.1 Experimental Settings; §5.2 Experimental Results on disclosed Flux and Stable Diffusion 3 settings",
        "nonproof": "§6 Conclusion and the disclosed model/resolution/equal-FLOPs evaluation scope",
        "boundary": "The reported Pareto improvement is confined to the disclosed DiT backbones, resolutions, matching schedules, and metrics; no claim is made for arbitrary architectures, visual domains, or latency hardware.",
    },
    "2605.22012": {
        "adopted": "Interleaving text with supervised audio-visual latent states and synchronized positions can preserve temporal sensory evidence that text-only CoT compresses away, while remaining limited to the evaluated audio-visual modalities.",
        "method": "arXiv:2605.22012v1 HTML §3.1–§3.4 (latent reasoning, unified representation/temporal alignment, data, training)",
        "evaluation": "§4.1–§4.3 (setup, main results, ablation)",
        "nonproof": "Appendix D Limitation (3D, tactile, motor/action modalities remain open); Appendix B implementation limits",
        "boundary": "Evidence supports the disclosed audio-visual benchmarks and open-source models; it does not establish causal faithfulness of latent reasoning or extension to 3D, tactile, motor, or embodied control state.",
    },
    "2605.22372": {
        "adopted": "Attention-sink-aware pruning should use cumulative attention-flow geometry rather than a single-layer salience score; diffusion distance can preserve salient trajectories while compressing background redundancy.",
        "method": "arXiv:2605.22372v1 HTML §3.1–§3.3 (lazy random walk, sink geometry, partition/compression)",
        "evaluation": "§4.1–§4.5 across disclosed image, video, VLM, hyperparameter, and efficiency tests",
        "nonproof": "§5 Discussion; Appendix E computational cost; Appendix I operating range and sensitivity",
        "boundary": "The evidence is training-free and architecture/workload bounded; the sink assumptions, cumulative-transition cost, chosen anchor, and operating range must be revalidated for other attention variants and sequence regimes.",
    },
    "2605.22668": {
        "adopted": "Resolution extrapolation can make per-frequency RoPE scaling a denoising-step control driven by latent spectral energy, avoiding the global-structure/fine-detail trade-off of uniform scaling within the tested range.",
        "method": "arXiv:2605.22668v1 HTML §4.1–§4.2 (latent spectrum and per-dimension RoPE scaling)",
        "evaluation": "§6 Experiments; §6.1 comparisons; §6.2 ablation; Appendix F alternative backbones/extreme resolutions",
        "nonproof": "Appendix D Limitation and Discussion; training-resolution and disclosed backbone/target-resolution boundary",
        "boundary": "The claim is limited to training-free inference on disclosed DiT backbones and resolutions; spectral scaling does not prove semantic or structural correctness outside that range and is not a substitute for target-resolution training.",
    },
    "2605.22671": {
        "adopted": "Separating a long-horizon visuomotor behavior state from a phase-conditioned action decoder addresses temporal fragmentation and execution drift, but must be judged in closed-loop simulation and real-world tasks.",
        "method": "arXiv:2605.22671v1 HTML §3.1–§3.4 (VBE, PBD, two-stage training)",
        "evaluation": "§4.1–§4.5; Appendix D (CALVIN, RoboTwin 2.0, real-world evaluation)",
        "nonproof": "Appendix A Limitation and Future Work; disclosed task, robot, data, and sim-to-real scope",
        "boundary": "The representation/control split is adopted only for the disclosed manipulation settings; benchmark success and reduced demonstrations do not prove arbitrary environment-shift robustness or safety.",
    },
    "2605.22818": {
        "adopted": "When user motion paths are sparse or causally incomplete, a reasoner may propose secondary motion and a confidence control may relax literal guidance; low confidence must fall back to generative priors rather than be treated as verified physics.",
        "method": "arXiv:2605.22818v1 HTML §3.1–§3.3 (motion representation, VLM reasoning/correction, confidence-aware control)",
        "evaluation": "§4.2–§4.5 (MotiBench, protocol/user study, results, ablation)",
        "nonproof": "Appendix B.2 failure cases; Appendix C Discussion §Scale and Validity of MotiBench and §Limitation",
        "boundary": "The VLM reasoner supplies plausible hypotheses rather than causal or physical proof; results are bounded to MotiBench, disclosed generators/evaluators, and human/VLM preference protocols.",
    },
}


# First risk-prioritized deep-review batch after the fresh-review failure.  These
# records are intentionally source-specific: a title/abstract paraphrase is not
# enough for either a positive Evidence claim or a Books decision.
DEEP_REVIEWS = {
    "2605.21493": {
        "adopted": "OOD evaluation must separate representation geometry from detector quality: a compactness loss can improve in-distribution classification while removing covariance and inter-class structure used by a distance-based OOD sensor, so representation/layer/normalization and detector/calibration identities require separate ablation.",
        "method": "arXiv:2605.21493v1 HTML §3 datasets/preprocessing; §4 baseline protocol and uncertainty scores; §5.1–§5.6 multi-scale features, L2 normalization, Mahalanobis detector, calibration head and CenterLoss analysis",
        "evaluation": "§5.7 and §6 results, ablations and seed study on CIFAR-10 with the disclosed OOD sets; §7.1–§7.5 discussion",
        "nonproof": "§7.6 Limitations and Future Work and §7.7 real-hard-OOD calibration discussion; CIFAR-scale AUROC and an OOD-trained calibration head do not establish open-world epistemic uncertainty or production-shift coverage",
        "boundary": "The evidence supports the representation-versus-detector ablation contract and one observed compactness failure, not GOEN as a universal OOD solution or the numerical AUROC ordering beyond the disclosed datasets, preprocessing and seeds.",
        "tradeoff": "Preserving multi-scale covariance can improve the tested distance sensor but adds feature storage, per-layer normalization/statistics and labeled hard-OOD calibration; the calibration set can leak its own shift taxonomy into the score.",
        "fallback": "When hard-OOD labels, covariance support or calibration transfer are inadequate, retain a simpler task-specific detector, report length/shift-matched slices, and escalate unknown inputs rather than treating Mahalanobis distance as truth.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch66 already requires OOD sensors to version representation, layer, normalization, detector, reference distribution and threshold separately, challenges representation-versus-detector attribution, and falls back to labeled OOD/task-specific gates under hard shift.",
    },
    "2605.21496": {
        "adopted": "A safety-oriented agent environment must version executable world state, tool semantics and error injection, task/rubric inventory, hard safety predicates and judge overlay separately; a reward that is tolerable for evaluation can still be gameable or unsafe as an RL training signal.",
        "method": "arXiv:2605.21496v1 HTML §3.1–§3.5 FHIR world state, action/tool/error semantics, bridge and determinism; §4 reward; §5 task suite",
        "evaluation": "§6 evaluation protocol; §7 model results, multi-step collapse and V7/V8 infrastructure correction; Appendices C–F pilot history, judge reliability and deterministic overlay audit",
        "nonproof": "§8 Limitations and Future Work: dynamic patient state, full RL-loop coupling, larger disjoint training tasks, physician adjudication and training-reward ablations remain future work",
        "boundary": "HealthCraft supports a versioned, trajectory-level clinical-safety evaluation environment and exposes reward/harness failure modes; it does not validate medical deployment, physician equivalence or drop-in RL reward safety.",
        "tradeoff": "FHIR/tool fidelity and hard predicates improve failure attribution but add environment/rubric maintenance, medical adjudication and zero-reward sparsity; deterministic overlays can bound judge noise without proving rubric completeness.",
        "fallback": "If world transitions, criteria or judge reliability are incomplete, restrict use to evaluation/smoke tests, preserve failures and physician review, and do not connect the reward to policy optimization.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch66 already binds agent evaluation to harness/environment/tool/error identity, trajectory and hard predicates, separates deterministic outcome from judge overlays, and requires generated evaluators/rewards to pass non-vacuity and meta-evaluation before training or release authority.",
    },
    "2605.21497": {
        "adopted": "Security-agent capability comparisons must treat general-purpose agents as baselines and hold CTF environment, vulnerability classes, attempts, tool/browser support, refusal, cost and architecture constant enough to distinguish orchestration effects from model or harness effects.",
        "method": "arXiv:2605.21497v1 HTML §II agent syllabus; §III-A architectures; §III-B 30 web-CTF benchmark",
        "evaluation": "§IV-A setup/metrics; §IV-B aggregate results; §IV-C architecture comparisons; §IV-D failure analysis",
        "nonproof": "§V Conclusion and Future Work and Appendix traces; 30 web CTFs omit browser/concurrency and broader offensive workflows, public challenges may be contaminated, and shared failure does not identify a single cognitive cause",
        "boundary": "The evidence supports a bounded cost/success/failure comparison for the disclosed CTF harness. It does not prove near-human offensive capability, general architecture superiority or causal attribution to the base model.",
        "tradeoff": "Specialized-role orchestration may improve consistency and cost in the tested tasks but adds prompts, handoffs and tool state; a general agent is simpler and can be a strong baseline.",
        "fallback": "When environment support, task secrecy or matched budgets fail, report observed flags/refusals/tool failures separately and fall back to deterministic CTF outcome plus human-controlled security testing.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch66 already defines Security Agent evaluation as cost-success-refusal operating curves, separates CTF flags from other security outcomes, versions attempts/provider/tool/runtime policy, and warns that public-task and scaffold differences block base-model causal claims.",
    },
    "2605.21545": {
        "adopted": "Refusal rate alone cannot own a safety ranking: evaluation should pair matched benign/borderline/dual-use tasks with should-refuse positive controls, report tier discrimination and partial-compliance content separately, and bind the observed behavior to the deployed access path rather than silently attributing it to model weights.",
        "method": "arXiv:2605.21545v1 PDF §2.1–§2.7 matched prompt construction, risk tiers, model/access panel, fixed system prompt, independent judge council, compliance ladder and statistical plan",
        "evaluation": "§3.1–§3.3 refusal heterogeneity, provider/access-path decomposition, Youden-J tier discrimination and partial-compliance quadrants; §4.1–§4.7 interpretation and pipeline implications",
        "nonproof": "§4.8 Limitations: one temperature/system prompt, sensitivity subset only, five trials miss rare tails, judge-council regional imbalance, no adversarial robustness, and positive controls cannot decide whether borderline refusal was warranted without expert annotation",
        "boundary": "The adopted claim is the metric/identity correction. The May-2026 model ordering, provider association and biology-specific rates are snapshot evidence only; refusal, tier discrimination and partial assistance do not by themselves measure real harmful uplift or end-to-end pipeline safety.",
        "tradeoff": "Matched tiers, controls and content coding improve calibration diagnosis but require expert risk labels, repeated calls, access-path versioning and multi-axis reporting; a single scalar is cheaper but can reward blanket refusal or miss hedge-but-help behavior.",
        "fallback": "When risk labels, judge agreement or expert warrant are unavailable, publish refusal/partial-compliance distributions with Unknown states, use deterministic policy/outcome anchors and human review, and do not promote a model from aggregate refusal rate.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch66 separates response rate from conditional/unconditional quality and versions harness/backend, but it does not yet make matched risk-tier discrimination, should-refuse controls, partial-compliance content and access-path attribution one refusal-evaluation contract.",
        "anchor": "### Response Rate、条件质量与无条件质量不能互相替代",
        "proposed_delta": "旧 safety leaderboard 常以 aggregate refusal rate 排名；当 blanket refusal、风险不敏感的低拒绝和 hedge-but-help 都可能得到误导性单值时，EvalSpec 应冻结 access path/system prompt/judge，构造 task-framing matched 的 benign/borderline/dual-use triples 与 should-refuse controls，并分开报告 tier discrimination、strict/partial compliance 和内容级 uplift。Evaluation owner 只拥有测量，policy/release owner 决定风险权重；provider association 不得归因模型权重。risk label、judge/expert warrant 或 adversarial slice 不足时保留 Unknown/人工审查，不能用拒绝率单独批准或拒绝发布。",
    },
    "2605.21748": {
        "adopted": "A multi-turn judge benchmark can create paired conversations with one localized injected flaw, jointly estimate judge skill and pair difficulty, and curate ambiguous pairs; the generator, ranking model and human audit remain separate evidence owners.",
        "method": "arXiv:2605.21748v1 HTML §3.1 paired multi-turn construction; §3.2 joint Bradley–Terry/EIP ranking; §3.3 difficulty-based curation",
        "evaluation": "§4 across three domains and 21 judges; Appendix A stability, self-preference, filtering and alternative-ranking analyses; Appendix C human audit",
        "nonproof": "Appendices A.3–A.8 and C expose model/class bias, synthetic-flaw and human-audit limits; stability under partial observability/coarser criteria does not turn synthetic preference labels into open-domain human truth",
        "boundary": "The evidence supports a benchmark-generator and curation pattern for the disclosed flaw taxonomy and domains, not a universal judge ranking or proof that one injected flaw determines all real conversation quality.",
        "tradeoff": "Paired localization improves label clarity but constrains the task population; difficulty filtering lowers noise while risking removal of the hard or disputed cases needed in production.",
        "fallback": "If injected flaws, judge ranking or pair-difficulty estimates do not match human anchors, keep raw pairwise evidence, broaden real conversations and report ties/uncertainty rather than an Elo order.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch66 already versions benchmark generators, synthetic task populations, pairwise judge evidence, Bradley–Terry/Elo calibration and uncertainty, and requires human/held-out anchors before a ranking receives release authority.",
    },
    "2605.21778": {
        "adopted": "Before evaluating or mitigating a broad behavior such as sycophancy, the EvalSpec must declare the construct dimensions and observable behaviors; belief/person-directed and explicit/implicit forms cannot be pooled into one score without preserving taxonomy and annotator disagreement.",
        "method": "arXiv:2605.21778v1 HTML literature review/taxonomy derivation; Taxonomy Dimensions; Expert Survey and Statistical Analysis",
        "evaluation": "Expert Survey Results; Appendix A.1–A.6 literature mapping, survey instrument, annotations, demographics and robustness analyses",
        "nonproof": "Limitations: literature selection and expert non-response/coverage bias, under-representation of industry and non-English communities, and rating-scale uncertainty; taxonomy consensus does not establish harm magnitude or mitigation efficacy",
        "boundary": "The adopted proposition is construct/rubric versioning and disagreement retention. The proposed taxonomy is a useful schema for the reviewed literature and surveyed experts, not an exhaustive or universally accepted definition.",
        "tradeoff": "A multi-axis taxonomy improves comparability but expands annotation cost and leaves disputed boundary cases; collapsing to one score is cheaper but hides which behavior changed.",
        "fallback": "When construct validity or annotator agreement is weak, publish behavior-level items and disagreement, avoid aggregate release claims, and re-adjudicate with the deployment population.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch66 already separates rubric formation, criterion execution and ranking; versions annotator/policy identity, preserves disagreement and construct validity, and prohibits pooled metrics from hiding incompatible task or population slices.",
    },
    "2605.22175": {
        "adopted": "A generated software test suite should be evaluated against realistic, diverse mutants and golden references, with verification rate and mutant-detection rate kept distinct; the mutant generator proposes challenges but cannot certify its own realism or the golden oracle.",
        "method": "arXiv:2605.22175v1 HTML §3.1 agentic mutant generation; §3.2 task formulation; §3.3 benchmark characteristics",
        "evaluation": "§4.1–§4.7 models, agents, verification/detection metrics, multilingual results, mutation comparisons and failure analysis; Appendices B–F ablations/statistics/cases",
        "nonproof": "Limitations: dependence on repository golden solutions/tests despite the oracle problem, Claude-4 mutant-generator bias, language/repository coverage and environment/toolchain effects",
        "boundary": "The evidence supports mutation-based discriminative testing under the released benchmark. Low detection rates do not prove every generated suite is bad, and surviving generated mutants do not prove real faults or complete requirements.",
        "tradeoff": "Agentic mutants improve challenge diversity but cost model calls/execution and can introduce invalid or generator-specific cases; stronger golden filters can also exclude legitimate alternative implementations.",
        "fallback": "When mutant validity or golden tests are disputed, retain compile/execution receipts, manually adjudicate samples, add requirement/incident-derived tests and report Unknown rather than treating kill rate as correctness.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch66 already requires compile/test/coverage/mutation evidence, distinguishes generator proposal from execution and meta-evaluation, preserves golden/reference uncertainty, and uses deliberate mutants only as bounded test adequacy evidence.",
    },
    "2605.22368": {
        "adopted": "Adversarial test-suite expansion and cost-aware reduction should be separate stages: candidate counterexamples are generated against reference preconditions/implementations, executed in the formal environment, then compacted only after discriminative coverage is measured.",
        "method": "arXiv:2605.22368v1 HTML §3.1 adversarial test-suite expansion and type-aware mutation; §3.2 reduction",
        "evaluation": "§4.1–§4.3 VerinaPlus/VerinaLite construction and eight-model SpecGen/CodeGen comparisons; Appendices A–C rules, hyperparameters and prompts",
        "nonproof": "Limitations: ground-truth preconditions/reference implementations are required, red-team quality is bounded by the LLM and Lean-4 competence, and expansion requires heavy sampling/execution compute",
        "boundary": "The evidence supports an expansion/reduction pipeline for the disclosed Lean/Verina setting, not full formal correctness, language portability or coverage of counterexamples outside the generator/rules.",
        "tradeoff": "More adversarial executions expose hidden weaknesses but cost substantial compute; reduction lowers recurring cost while risking removal of rare but important counterexamples.",
        "fallback": "If references, type-aware mutations or reduction coverage are unreliable, retain the full executable suite, add proof/manual review, and do not infer correctness from the compact pass rate.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch66 already treats generated tests/mutations as candidate evidence, requires executable non-vacuity and reference validation, separates expansion coverage from maintenance budget, and withholds correctness when the oracle or mutation population is incomplete.",
    },
    "2605.22535": {
        "adopted": "Terminal-agent evaluation should preserve the real recording lineage while materializing a clean, reproducible environment, task intent and final-state tests; reference commands describe one journey and must not become the only accepted outcome.",
        "method": "arXiv:2605.22535v1 HTML §3.1 recording collection; §3.2 task synthesis; §3.3 Docker environment reproduction; §3.4 test generation; §4 benchmark/verified subset",
        "evaluation": "§5.1–§5.4 eight-model/six-agent results, Terminal-Bench comparison and human comparison; Appendix C settings and analyses",
        "nonproof": "Appendices A–C and scope statements: TUI/editor interactions are excluded, automated tasks inherit recording/synthesis/test biases, only 200 tasks receive the Verified-subset review, and benchmark pass does not establish production side-effect safety",
        "boundary": "The adopted proposition is recording-to-executable-task lineage and outcome-based verification. The reported pass rates and weak benchmark correlation apply only to TerminalWorld-Verified and its container/tool scope.",
        "tradeoff": "Real recordings improve ecological variety but require intent inference, dependency reconstruction, test generation and manual verification; excluding TUI and irreproducible sessions changes the represented population.",
        "fallback": "If intent, environment or final-state tests cannot be verified, retain the task as unverified discovery material or use expert-authored fixtures; do not score by replaying the reference command sequence alone.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch66 already defines terminal/workspace evaluation through initial environment, allowed tools/mutations, terminal artifact and side effects, separates reference paths from outcome witnesses, and requires verified executable fixtures before scores obtain authority.",
    },
    "2605.22672": {
        "adopted": "Forecast evaluation must score the full predictive distribution and decision-relevant upper tail: a conventional bounded threshold can hide or reverse capability scaling when errors concentrate in superlinear-growth or regime-change tails.",
        "method": "arXiv:2605.22672v1 HTML §2 ForecastBench-Sim design; §3 mechanism isolation; §4 controlled scale/post-training family; §8 threshold-score analysis",
        "evaluation": "§2.2 synthetic results; §5–§7 COVID, measles, housing and hyperinflation replications and knowledge tests; Appendices C–L data generation, statistics and robustness",
        "nonproof": "§9.1 Limitations and Appendix robustness panels: results concern selected growth/regime-change processes and elicitation; all findings are empirical, parse floors and real-data histories limit causal/general tail claims",
        "boundary": "The adopted claim is the tail-inclusive scoring contract and observed inverse-scaling risk, not that larger models forecast worse generally or that the simulated and historical series represent every production regime.",
        "tradeoff": "Continuous/unbounded distribution scores expose tail cost but are less interpretable and more outlier-sensitive than binary thresholds; tail slices require enough support and a decision-specific loss.",
        "fallback": "When tail support or loss calibration is weak, report threshold and continuous scores together with uncertainty, expand stress scenarios and keep forecasts advisory under external decision rules.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch66 already requires forecast datasets to be decision-time frozen/walk-forward, separates risk sensor from action policy, explicitly audits tail shape, threshold/grid/sample sensitivity and false positives, and falls back to external verification or conservative thresholds.",
    },
    "2605.21558": {
        "adopted": "Data selection and trainable-parameter selection should be treated as one adaptation artifact when the selector is derived from the same task signal: P2D uses a short proxy run to rank task-sensitive attention heads, uses those heads to rank examples, and updates only the selected heads on the selected data.",
        "method": "arXiv:2605.21558v1 HTML §3.1 problem formulation; §3.2.1 proxy/head identification; §3.2.2 parameter-guided data selection; §3.2.3 sparse head adaptation",
        "evaluation": "§4.1–§4.3 experiments and ablations; §5 discussion/analysis; Appendices H–L cross-ablations, systems-cost breakdown and sparsity sweeps",
        "nonproof": "Appendix M Limitations: attention-head-only adaptation can bottleneck new factual knowledge, the 100-sample proxy can miss domain-shifted heads, 7.0x is specific to eight-A100 ZeRO-2, ICL scoring remains demonstration-sensitive, and only SFT is evaluated",
        "boundary": "The adopted proposition is the shared data×parameter selection identity and end-to-end cost accounting, limited to the disclosed SFT tasks, models, proxy, attention-head mask and hardware. It does not establish the Strong Map hypothesis universally or make 10% data/heads an invariant optimum.",
        "tradeoff": "Joint selection removes duplicated selectors and can reduce training state, but adds a proxy run, head-ranking and ICL scoring whose errors are coupled; restricting updates to attention heads can block new knowledge or different trainable subspaces.",
        "fallback": "If the proxy is unstable, domain shift hides useful heads, MLP capacity is required, or end-to-end AER does not improve, retain single-axis or sequential selection, LoRA/full SFT, and independently validate target and retain slices.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch29 already makes data subset and parameter mask one versioned selection artifact, derives both from a shared task/validation interaction signal, charges selection cost, and preserves single-axis, sequential or full-SFT fallbacks when the shared approximation fails.",
    },
    "2605.21674": {
        "adopted": "Adaptive jailbreak evaluation should preserve the unsafe seed, every semantic reframe, the target response, the refusal/safety scorer revision, the candidate and iteration budgets, and the stopping rule as one attack trajectory; a fluent low-refusal rewrite is an attack finding, not proof that intent or harm was independently validated.",
        "method": "arXiv:2605.21674v1 HTML §3.2–§3.3 (non-convex formulation and stopping rule); §4 Proposed Methodology / Algorithm 1",
        "evaluation": "§5.1–§5.5 (four safety benchmarks, refusal analysis, safety-gain distribution, baselines, judge-prompt and safe-function/engine ablations)",
        "nonproof": "§5.4–§5.5 expose judge/scorer dependence; §6 Conclusion; BERT similarity and the safety classifier are proxy constraints, not independent proof that rewritten intent and resulting content are harmless or equivalent",
        "boundary": "The evidence supports THREAT as a bounded red-team search over the disclosed prompts, models, classifiers, templates and budgets. The reported refusal/safety scores do not estimate open-world attack probability and do not certify semantic preservation or defense completeness.",
        "tradeoff": "Iterative multi-model search improves attack discovery per tested budget but adds attacker/scorer coupling, query cost, semantic-drift risk and a stopping threshold that can be gamed.",
        "fallback": "If similarity or safety scorers are uncalibrated, retain the full trajectory for human/independent policy adjudication, broaden the held-out attack generator, and report only an observed lower bound rather than a safety conclusion.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch72 already requires attack-generator, submission policy, attempt opportunity, audit budget and outcome/effect evidence to be frozen; it also treats finite red-team success or zero hits as an observed lower bound, not a safety certificate.",
    },
    "2605.21834": {
        "adopted": "Consistency training should be evaluated on the policy-induced response state rather than only on an offline contrastive target: OPCT samples the current model response and supervises it with the same model conditioned on the paired contrastive prompt, while safety gains and base capabilities remain separate release gates.",
        "method": "arXiv:2605.21834v1 HTML §3 On-Policy Consistency Training (invariance and compression objectives)",
        "evaluation": "§4 Experimental Setup; §5.1–§5.4 across sycophancy, static/adaptive jailbreak, safety awareness and capability regressions; Appendices E–G disclose training/evaluator details",
        "nonproof": "Appendix A Limitations; Appendix F.5–F.8 adaptive-attacker and capability-regression scope; the three tested model families and safety axes do not prove general alignment or eliminate reward/self-supervision error",
        "boundary": "The adopted claim is the deployment-state/on-policy supervision distinction and the need for independent capability slices. It does not adopt the paper's recommendation as a universal replacement for SFT or claim safety beyond the disclosed attacks, models and judges.",
        "tradeoff": "On-policy responses reduce surface-form mismatch but add rollout cost, policy-version dependence and self-supervision correlation; contrastive prompts can encode an incorrect invariant.",
        "fallback": "When the contrastive invariant, teacher-conditioned response or adaptive-attack evaluator is unreliable, retain static SFT/curated pairs and require held-out capability and independent safety evaluation before promotion.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch31 already states that SFT, on-policy distillation and RL differ by the state distribution on which supervision is applied, versions policy/teacher/rollout state, and requires held-out capability and safety slices independent of the training signal.",
    },
    "2605.21865": {
        "adopted": "For JSON/XML response classes whose member order is contractually non-semantic yet preserved end to end, a proxy gateway can encode a trace watermark by permuting grouped keys; the watermark artifact must bind schema, grouping/order rule, key material, serialization path and extraction receipt.",
        "method": "arXiv:2605.21865v1 HTML §II Watermarking Proxy Gateway; §III-A grouping, factorial decomposition and key reordering; §III-B extraction",
        "evaluation": "§IV-A–§IV-G capacity, overhead, deletion/tamper/insert attacks and a disclosed power-industry system; nine synthetic/desensitized JSON structure configurations",
        "nonproof": "§V Limitation: 50% deletion reduces similarity to 49%–60%, fixed alphabetical order is attacker-visible, and a secret-keyed order is only proposed; the paper does not test canonicalizers, signatures/caches or clients that observe byte/key order",
        "boundary": "The evidence supports a conditional serialization-channel watermark, not the universal claim that key reordering is distortion-free or that watermark recovery proves source, integrity or authorization. The route applies only after compatibility and canonicalization gates for the exact response class.",
        "tradeoff": "A gateway-only scheme avoids mutating values and business handlers, but introduces reserialization, capacity thresholds, key/order metadata, secret management and robustness loss under deletion or normalization; fake keys used for insufficient capacity can itself change client-visible structure.",
        "fallback": "If clients, signatures, caches, canonicalizers or schema validators observe order/extra keys, or robustness/key secrecy is inadequate, disable permutation embedding and fall back to explicit signed provenance, sidecar audit receipts or application-owned watermarking.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch62 requires response/path provenance and evidence-bound receipts, but it does not define response serialization as a conditional watermark channel, name the compatibility/canonicalization gate, or separate recovered watermark evidence from integrity and authorization proof.",
        "anchor": "## 观测与容量反馈",
        "proposed_delta": "旧水印常改写字段值或业务代码；当 JSON/XML member order 对指定 client contract 不承载语义、且整个序列化链保序时，Gateway 可把 grouped-key permutation 作为受限 trace channel。Gateway/watermark owner 版本化 schema、grouping/order、secret、serializer 与 extraction receipt；client compatibility、signature/cache canonicalization 和 authorization 仍由各自 owner 验收。删除、重排、规范化、key 泄漏或容量不足时禁用该分支，回退显式 signed provenance/sidecar receipt，而不能把可提取水印当作内容完整性或授权证明。",
    },
    "2605.21958": {
        "adopted": "Failure diagnosis and repair placement are different decisions in a multi-module LLM pipeline: a causally blamed downstream module may be the worst prompt-patch target when downstream modules have co-adapted to upstream output and error distributions.",
        "method": "arXiv:2605.21958v1 HTML §3.1 failure index; §3.2 causal contribution; §3.3 per-task natural indirect effects; §3.4 correction-pool patching; §3.5 Linguistic Contract hypothesis",
        "evaluation": "§4.1–§4.4 on a four-module tau-bench pipeline across three agent families; diagnosis on retail/airline, prescription on the retail split; Appendices G–N replications and sensitivity analyses",
        "nonproof": "§6 Limitations: prescription evidence is one fixed retail topology, only a single-turn first action is studied, human evaluation is absent, the direction account is indirect, and the contract proxy reuses NIE-derived diagnosis evidence",
        "boundary": "The adopted proposition is a diagnosis/prescription ownership separation and a distribution-shift test before patch promotion. It does not establish downstream co-adaptation as a general causal law or prove that upstream patching is always safer.",
        "tradeoff": "Causal interventions and same-snapshot patch trials improve attribution but multiply executions, judges and comparison state; preserving a noisy upstream contract can also retain a real defect, while changing it can invalidate downstream assumptions.",
        "fallback": "When oracle pairing, topology stability or held-out prescription evidence is unavailable, do not auto-patch the blamed module; compare upstream/downstream candidates from one frozen snapshot, replay end to end, and fall back to no patch, interface retraining, serial redesign or human adjudication.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch81 versions fixes, measures isolated effects from the same iteration-start policy and replays the realized patch order, but it does not yet separate causal blame from repair authority or require a co-adapted interface/distribution check before choosing the patch locus.",
        "anchor": "### Reusable Scaffold 与 Fix 也是受治理的 Workflow Artifact",
        "proposed_delta": "旧调试路径常把 causal diagnosis 直接变成 patch target；多模块 LLM pipeline 中，下游可能已适应上游的语言分布及其特征性错误，使修正被归因的模块反而破坏隐式 interface contract。Diagnosis owner 只产出 blame/NIE artifact，repair owner 必须从同一 frozen snapshot 比较多个 patch loci，并由 workflow owner 做 end-to-end replay 与 promotion。该证据仅覆盖披露的单轮四模块 pipeline；oracle pairing、拓扑或 held-out prescription 不足时，回退 no-patch、接口重训/串行重构或人工裁决，不能把 upstream patch 写成普遍处方。",
    },
    "2605.22223": {
        "adopted": "For a fixed Transformer architecture, increasing context or inference time does not make every output sequence reachable: under the paper's bounded-embedding/decision-cell assumptions, maximal accessible length grows only linearly with prompt length and the accessible fraction decays exponentially beyond a model-dependent threshold.",
        "method": "arXiv:2605.22223v1 HTML §2 architecture; §3.1–§3.2 embedding-space decision regions and prompt reachability; §4.1–§4.2 accessible-sequence bounds",
        "evaluation": "§5.1–§5.4 (cramming, support refinement, cell-volume distribution and copying-length generalization); Appendix G model/support and precision analyses",
        "nonproof": "§6 Conclusion; §7 Future Work; theorems depend on the formal architecture, bounded embeddings, support/packing and precision definitions in §2 and Appendices A–F and do not characterize trained-model quality or every decoding policy",
        "boundary": "The result is an architecture-conditional support bound and tested explanation for copying/cramming cliffs. It does not prove that a particular natural-language answer is inaccessible, that training cannot change the model-dependent constants, or that reported empirical thresholds are production guarantees.",
        "tradeoff": "The bound gives a diagnostic ceiling without exhaustive generation, but computing/estimating decision-cell geometry and effective precision is model-specific and can be loose for a deployed checkpoint.",
        "fallback": "If formal assumptions or constants cannot be validated, retain direct copying/cramming and length-slice tests under the deployed tokenizer/decoder, and treat the theorem only as a risk hypothesis rather than an admission denial.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch18 separates finite-precision execution semantics from abstract expressivity, but it does not yet state the distinct prompt-length-dependent accessible-output support bound or the abrupt copying/cramming threshold.",
        "anchor": "### 表达能力还取决于实现中的有限精度状态语义",
        "proposed_delta": "旧路径通常把更长 context、更多 Decode 时间或更大采样预算当成扩大输出能力的通用手段；当固定 Transformer 的 prompt-to-output decision regions 只覆盖有限 support 时，这些预算不改变架构可达性。Ch18 应把 accessible-sequence support 作为独立于 runtime budget 的模型状态：prompt 拥有输入选择，decoder/architecture 决定可达区域，评测 owner 用 copying/cramming 与长度切片估计阈值，不能让 sampler 宣称任意序列可达。",
    },
    "2605.22237": {
        "adopted": "For FHE-only inference on a frozen single-hidden-layer ReLU classifier and declared calibration set, quadratic activation replacement can be solved against final logit-order constraints; exact preservation is certified only in the positive-margin lifted-space regime, while reduced-hull/soft-margin variants are approximate surrogates.",
        "method": "arXiv:2605.22237v1 HTML §III frozen-layer/calibration formulation; §IV-A–§IV-F exact, maximum-margin, quantization-tolerance, relaxed and multiclass theory; §V algorithms and FHE cost",
        "evaluation": "§VI protocol/threat model; §VII plaintext regime diagnostics; §VIII CKKS configuration and precision sweeps across the disclosed MLP heads and datasets",
        "nonproof": "§IX Discussion and Limitations: theorems certify the calibration set only, exact full-train feasibility is rare, multiclass results are surrogate evidence, CKKS comparison fixes one packing/modulus-search framework, and encrypted DINOv2/Qwen3 heads do not protect raw inputs",
        "boundary": "The adopted claim is a decision-aware, regime-labeled activation-replacement artifact for the disclosed shallow frozen heads. It neither certifies unseen inputs nor licenses a generic ReLU replacement in deep networks, and calibration agreement is not ground-truth correctness or end-to-end confidentiality.",
        "tradeoff": "Quadratic depth can reduce encrypted multiplications and modulus levels, but fitting global decision inequalities adds calibration dependence, margin/outlier sensitivity and coefficient/CKKS precision state; soft regimes can preserve many decisions without a certificate.",
        "fallback": "If positive-margin feasibility, unseen-slice agreement, coefficient quantization or CKKS numerical checks fail, retain the original activation where possible or use higher-degree FHE approximation, hybrid MPC/comparison protocols, retraining, or reject the encrypted deployment.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch49 already treats decision margin as a calibrated risk sensor and requires per-example/end-to-end acceptance, but it does not distinguish an exact positive-margin calibration certificate from reduced-hull/soft surrogate regimes or bind that regime to the FHE circuit artifact.",
        "anchor": "### 量化验收不能只看平均分：逐例一致性与分布漂移",
        "proposed_delta": "旧 FHE-only 路径在 activation interval 上局部逼近 ReLU；当主要成本来自 polynomial depth、最终验收关心固定 classifier 的 logit order 时，可在冻结 hidden/output head 与声明 calibration set 后，直接拟合 decision inequalities。Calibration owner 版本化样本、margin 与 exact/RCH/soft regime，compiler/FHE runtime 拥有 coefficient quantization、CKKS precision 与 circuit cost，release owner 仍要求 unseen slices 和 ground-truth quality。只有 positive-margin regime 对 calibration decisions 给出 exact certificate；soft agreement 不能冒充证明，数值或外推 Gate 失败时回退高阶近似、hybrid MPC/comparison、重训或拒绝发布。",
    },
    "2605.22534": {
        "adopted": "A pull request's merged/rejected state is not an autonomous-agent capability label; evaluation must preserve review comments, CI, follow-up commits, workflow constraints and observable human intervention so outcome, process and missing rationale remain separate dispositions.",
        "method": "arXiv:2605.22534v1 HTML §3 Data Collection; §4 Methodology and manual decision-rationale coding",
        "evaluation": "§5 RQ1 rejection drivers; §6 RQ2 human involvement in merged PRs; §7 Discussion",
        "nonproof": "§8 Threats to Validity; §9 Conclusion and Future Work; repository/sample selection, visible interaction artifacts and manual codes do not expose unrecorded decisions or causally identify agent capability",
        "boundary": "The findings support interaction-aware evaluation for the sampled open-source Agentic-PR population. They do not estimate all coding-agent deployments, prove why an individual maintainer acted, or turn merge status into a quality ground truth.",
        "tradeoff": "Interaction-level evidence improves attribution but costs manual coding and still misses private or undocumented decisions; stricter human-involvement labels can also under-credit legitimate autonomous work.",
        "fallback": "When interaction artifacts are incomplete, report outcome, observable intervention and missing-rationale states separately; do not impute agent success/failure, and fall back to executable requirement and held-out regression evidence.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch66 already requires Agent evaluation to preserve trajectory, assertions, environment and uncertainty, distinguishes final pass from process/outcome evidence, and explicitly forbids observable outcome from silently owning capability attribution.",
    },
    "2605.22428": {
        "adopted": "Multicast improves collective latency only where the topology contains a duplicating source-side bottleneck: MultiWrite carries per-packet destination-memory metadata, remains stateless in the network, uses source-rooted relay trees, and gives combine a separate reverse-tree reduction path.",
        "method": "arXiv:2605.22428v1 HTML §2.3 topology/bottleneck motivation; §3 beneficial scenarios; §4 MultiWrite semantics/properties; §5 UB software implementation",
        "evaluation": "§6 AllGather and MoE AlltoAll implementations/evaluation; disclosed Ascend/UB commercially deployed-device stress tests and topology cases",
        "nonproof": "§2.3 and §3 explicitly show multicast bandwidth reduction need not reduce latency; §7 limits comparison to documented/open transports, and the results do not establish portability to RDMA/NVLink/other fabrics or arbitrary topology and message regimes",
        "boundary": "The adopted proposition is a topology-conditioned alternative for redundant dispatch/AllGather traffic under the disclosed memory and transport semantics. It does not make multicast a universal collective replacement or transfer the reported 33% maximum to other fabrics.",
        "tradeoff": "Source-rooted replication reduces duplicate uplink traffic but adds destination maps, relay scheduling, partial reductions, buffer/atomicity contracts and a transport-specific software path; combine has no redundant input traffic and needs reduction rather than multicast.",
        "fallback": "When traffic is non-redundant, downlinks/compute dominate, the relay tree is imbalanced, transport semantics are unsupported or reliability/buffer checks fail, retain unicast ring/tree collectives or a topology-specific reference algorithm.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch21 already has a dedicated topology-conditioned multicast branch that names source-rooted relay state, per-destination semantics, reverse-tree combine, bottleneck conditions, costs, evidence limits and unicast/topology-aware fallback.",
    },
    "2605.22596": {
        "adopted": "A task tuple may be composed with one shared diffusion policy only under auditable approximate conditional independence: per-factor null-token dropout identifies additive score components, and any closed-loop certificate must propagate per-factor score error through the sampling ODE and contracting controller into a trajectory tube.",
        "method": "arXiv:2605.22596v1 HTML §2 problem; §3.1 ODE sensitivity; §3.2 factored score decomposition; §3.3 trajectory-tube certificate; Appendix A formal assumptions/proofs",
        "evaluation": "§4.1 state-based full-race composition; §4.2 vision-based single-gate traversal; Appendices B–D include K-network baseline, DDIM/seed sweeps, diagnostics and bound comparisons",
        "nonproof": "§6 Limitations and Broader Impacts; Appendix A.1–A.3 contraction, Lipschitz and factor-identifiability assumptions; drone-racing evidence does not prove arbitrary factor independence, robot safety or tight tubes",
        "boundary": "The adopted claim is the factor/score/controller ownership chain and assumption-bounded tube, limited to the disclosed diffusion/ODE/controller setup and drone tasks. The empirical pass/crash rates are not a universal safety certificate.",
        "tradeoff": "Factorization reduces combinatorial demonstration coverage but adds null-factor training, independence diagnostics, per-factor error accounting and potentially conservative trajectory tubes.",
        "fallback": "When factor dependence, score-error, contraction or observation assumptions fail, stop composing unseen tuples and fall back to jointly trained task policies, explicit planners, shorter-horizon control or the verified low-level safety controller.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch26 assigns action proposal and physical commit to separate owners and covers diffusion action chunks and runtime assurance, but it does not yet connect task-factor admission to additive score ownership and a closed-loop trajectory-tube certificate.",
        "anchor": "### VLA policy",
        "proposed_delta": "旧的 monolithic task-conditioned policy 在组合数可覆盖时最直接；当 object/obstacle/goal 等 factor 组合使 demonstration 预算乘法增长时，可在明确近似条件独立前提下让单一 diffusion network 用 per-factor null dropout 学 additive score。factor registry 拥有组合身份，score network 只拥有 action proposal，ODE 与 tracking controller 分别传播误差并保有物理提交权；tube 仅在 Lipschitz、identifiability 与 contraction 前提成立时有效。",
    },
    "2605.22705": {
        "adopted": "Tokenizer vocabulary optimality is defined relative to an inference procedure: ToaST freezes a vocabulary-independent split-tree artifact, recursively emits the first in-vocabulary nodes, and then selects the vocabulary with an IP/near-integral LP relaxation under that exact traversal.",
        "method": "arXiv:2605.22705v1 HTML §2 Split Trees; §3 Split Tree Inference; §4.1–§4.3 IP, LP relaxation and rounding",
        "evaluation": "§5 scaling; §6 intrinsic compression/Rényi metrics; §7 downstream 1.5B-model results; Appendices B–E computational scope and relaxation gap",
        "nonproof": "§8 Conclusion; Appendix A Extensions and Future Work; Appendix E relaxation gap; English/pretokenizer/data/model results do not prove multilingual, lifecycle-cost or downstream superiority, and training scales empirically quadratically in split-tree count",
        "boundary": "The adopted claim is joint versioning of split-tree inference and objective-bounded vocabulary selection. The reported compression and CORE gains are limited to the disclosed English data, vocabularies, model scale and metrics.",
        "tradeoff": "Global vocabulary selection improves the chosen compression objective but requires a new recursive decoder artifact, large count tables, LP/IP solve and quadratic observed training scaling; compatibility with existing checkpoints is lost.",
        "fallback": "When pretoken boundaries, multilingual coverage, solve cost or downstream regression fail, retain frozen BPE/Unigram and their checkpoint; use the LP bound only as an offline diagnostic, not a runtime substitution license.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch11 explains BPE and Unigram search directions plus tokenizer/checkpoint identity, but it does not yet make vocabulary optimality conditional on the frozen inference procedure or describe a split-tree/IP co-design artifact.",
        "anchor": "## Unigram 与 SentencePiece 的另一条路线",
        "proposed_delta": "旧的 BPE/Unigram greedy path 在规模、兼容与稳定性优先时合理；若目标是可审计的全局 compression，可先冻结 vocabulary-independent split trees 与 recursive inference，再在该固定 traversal 上求 IP/LP vocabulary。split-tree revision 与 vocabulary 共同拥有 tokenization identity，LP 只证明指定 corpus/objective 下的 gap，不拥有 downstream quality；solver、multilingual 或 checkpoint compatibility 越界时回退原 tokenizer。",
    },
    "2605.22765": {
        "adopted": "A discrete-diffusion artifact is not identified by its corruption marginals alone: UDM bridge plug-in, marginalization/denoiser and score parameterizations can optimize different targets, while an absorbing-state lifting may preserve the UDM joint law but change learned parameterization and sampling operations.",
        "method": "arXiv:2605.22765v1 PDF §3.1 bridge plug-in versus marginalization; §3.2 leave-one-out target/conversions; §3.3 predictor-corrector; §4.1–§4.3 absorbing-state and masked-uniform reformulations",
        "evaluation": "§6.1–§6.4 language-model and Sudoku comparisons across objectives, parameterizations and samplers; Tables 1–2 and Figures 3–4; Appendices H–I diagnostics/frontiers",
        "nonproof": "Main-text Limitations and future work (p.12); Appendix A assumptions/conversions; §4.2 replaces the exact posterior with a factorized learned approximation in practice; empirical advantage of leave-one-out remains without a complete theoretical explanation",
        "boundary": "The adopted claim is artifact identity and an objective/parameterization mismatch for exact-v1 UDM constructions. It does not claim all UDMs are inferior/superior, that empirical frontiers transfer to other domains, or that the practical learned sampler preserves an exact target law.",
        "tradeoff": "Leave-one-out conversions and absorbing lifts expose cleaner targets/remasking but add parameterization state, auxiliary absorbing variables, corrector steps and approximation error; hollow attention can be harder to train.",
        "fallback": "If objective-to-parameterization conversion, joint-law assumptions or learned-posterior approximation cannot be verified, freeze the original denoiser/sampler pair, compare full generative frontiers, and revert to the reference masked or uniform process.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch24 separates target-distribution construction, objective, commit policy and speculative verification, but it does not yet state that identical corruption marginals can hide a denoiser/leave-one-out target mismatch or require parameterization in the generative artifact identity.",
        "anchor": "## Training / Inference mismatch",
        "proposed_delta": "旧比较常把 UDM/MDM 的 corruption marginal 当作生成范式身份；exact-v1 表明同一 clean-data prediction 经 bridge plug-in、marginalization 或 score parameterization 会对应不同 reverse target，甚至可用 absorbing lift 保持 UDM joint law却获得 masked-like sampling。artifact owner 必须联合版本化 marginal、network target、loss conversion 与 sampler；理论 joint-law owner 与 learned approximate sampler 的效果 owner 分开，转换/近似失效时回退冻结的原参数化与 sampler。",
    },
    "2605.22821": {
        "adopted": "A tokenizer can expose an objective-specific optimality gap by relaxing its discrete vocabulary/segmentation program to an LP: the relaxation lower bound certifies compression distance, while rounded vocabularies still require stability, bits-per-byte and downstream evaluation.",
        "method": "arXiv:2605.22821v1 HTML §2.1 tokenizer objective; §3.1–§3.3 generalized IP, convex relaxation and rounding; Appendix C IP/token-sequence mapping",
        "evaluation": "§4 setup; §5 LP behavior, optimality certificates, sampling stability, intrinsic metrics, BpB and CORE; Appendices D–J detailed intrinsic/multilingual/downstream results",
        "nonproof": "§6 Limitations and Future Work; LP lower bound certifies only the chosen corpus/objective, rounded solution and pretokenization; ConvexTok is less stable than BPE to training-sample randomness and downstream gains are inconsistent",
        "boundary": "The adopted claim is an inspectable compression-objective certificate plus separate behavioral gates. Being within 1% of the LP lower bound does not prove a tokenizer is optimal for language modeling, multilingual fairness, latency or an existing checkpoint.",
        "tradeoff": "Convex optimization reduces greedy objective regret but introduces solver/rounding cost, sample sensitivity and artifact incompatibility; better intrinsic metrics may not translate to consistent downstream gains.",
        "fallback": "If the LP is too large, rounding is unstable, multilingual slices regress or downstream/lifecycle cost fails, retain BPE/Unigram and use the lower bound only to quantify unexplained compression headroom.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch11 covers BPE/Unigram mechanisms, compression versus lifecycle/downstream trade-offs and checkpoint coupling, but has no objective-specific lower-bound certificate or explicit separation between compression optimality and behavioral acceptance.",
        "anchor": "## Unigram 与 SentencePiece 的另一条路线",
        "proposed_delta": "BPE/Unigram 的局部/迭代选择在稳定部署中仍是基线；当团队需要回答“离指定 compression objective 还有多远”时，可把离散 vocabulary/segmentation 写成 IP，以 LP relaxation 给出 objective-specific lower bound，再把 rounding、sample stability、BpB、multilingual 与 downstream 作为独立 Gate。solver 只拥有优化证据，tokenizer owner 才能发布 artifact，certificate 不能跨 corpus、pretokenizer 或目标外推。",
    },
    "2605.22791": {
        "adopted": "A delta-rule recurrent state should not force one scalar to own two independent edit decisions: Gated DeltaNet-2 uses channel-wise key-side erase and value-side write gates while retaining channel-wise decay and a chunkwise WY training form.",
        "method": "arXiv:2605.22791v1 HTML §2.2–§2.4 delta-rule/KDA baseline; §3.1 erase/write decoupling; §3.2 fast-weight view; §3.3 chunkwise WY; Appendix A derivation and Appendix B backward pass",
        "evaluation": "§4 setup; §5 language modeling, commonsense, RULER/multi-query retrieval and recall; §6 ablations; matched 1.3B, 100B FineWeb-Edu training plus recurrent/hybrid variants",
        "nonproof": "§7 conclusion and Appendices C–H; the evidence is limited to the disclosed 1.3B/100B recipe, tasks and kernels, erase contributes most of the gain, and the work does not prove superiority to softmax or solve semantic isolation/editability",
        "boundary": "The adopted claim is the state-update ownership split and efficient implementation for the tested recurrent-attention recipe. Benchmark gains do not show that independent gates preserve arbitrary long-range facts, provide hard erasure, or generalize to all scales/hardware.",
        "tradeoff": "Separate gates increase editing freedom with a small reported throughput overhead, but add gate state, backward/kernel complexity and calibration risk; the recurrent matrix remains a compressed shared state subject to interference.",
        "fallback": "When gate stability, kernel support, retrieval/quality or request-isolation checks fail, collapse to the simpler KDA/Gated DeltaNet update, use softmax/hybrid attention, and reset state at runtime boundaries rather than relying on learned erase.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch22 already explains the scalar erase/write tie, channel-wise b_t/w_t ownership, fast-weight editing cost, limited 1.3B/100B evidence, orthogonal-subspace interference, session reset requirement and KDA/Gated DeltaNet/softmax fallback.",
    },
    "2605.21541": {
        "adopted": "A transfer-based multimodal attack can use different frequency bands for different control roles: high-frequency patch-feature alignment selects a target-facing surrogate objective, while low-pass filtering the input gradient suppresses surrogate-specific update directions; this remains an attack-finding mechanism, not a defense or universal account of visual semantics.",
        "method": "arXiv:2605.21541v1 HTML §2.1 threat model; §2.3–§2.5 high-frequency DCT/OT feature alignment and radial low-pass gradient regularization",
        "evaluation": "§3.1–§3.3 closed-source transfer panel, main comparisons and ablations; Appendices D–I threshold, budget, defense and response analyses",
        "nonproof": "Appendix B Limitations: gains depend on a three-CLIP surrogate ensemble, assume smooth spectra for continuous-tone natural images, and are evaluated through captioning/GPTScore/KMR rather than text-rich, VQA or multi-turn settings",
        "boundary": "The evidence supports one frequency-decomposed attack search over the disclosed surrogate/victim panel. It does not show that high frequencies universally encode semantic focus, that low frequencies are universally transferable, or that any inspected model is safe or unsafe outside the attack protocol.",
        "tradeoff": "Frequency decomposition and ensemble surrogates improve the tested transfer search but add multiple encoders, DCT/OT and iterative gradient cost; filtering can also remove useful attack directions when the spectral assumption fails.",
        "fallback": "For text-rich, line-drawing, non-captioning or single-surrogate regimes, fall back to transformation-aware multimodal red-team suites, direct black-box probes and independent effect-level safety controls rather than treating FRA success or failure as a certificate.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch72 already separates attack search from defense authority, requires multimodal/adversarial evaluation to bind input transformations, surrogate/target/evaluator identity and attack budget, and keeps model behavior and external effect as separate gates; a source-specific frequency attack does not change that system contract.",
    },
    "2605.21609": {
        "adopted": "A refusal-oriented guardrail may turn a recoverable adolescent interaction into harmful non-engagement; a population-specific post-generation control can instead classify the risk domain, detect unsafe or refusal-style output, propose a domain-conditioned rewrite, and pass only independently validated supportive content while preserving hard refusal for unresolvable risk.",
        "method": "arXiv:2605.21609v1 HTML Proposed Approach: CR4T, including System Overview, risk taxonomy/domain assignment, detection trigger, domain-conditioned reconstruction and instruction design",
        "evaluation": "Evaluation Method and Experimental Results & Analyses: safety/refusal detectors, two LLM judges, domain-level risk reduction, guidance, informational-value and reconstruction analyses",
        "nonproof": "Conclusions & Future Work and Ethical Considerations: adult-centric benchmarks, LlamaGuard not adolescent-specific, no real adolescent interactions, no long-horizon validation, and controlled offline model-generated responses only",
        "boundary": "The evidence supports selective rewrite as an experimental safety-control branch and exposes refusal as a possible interaction failure. It does not validate clinical/developmental appropriateness, real-minor deployment, long-conversation safety or autonomous replacement of expert policy.",
        "tradeoff": "Reconstruction can preserve guidance and continuity but adds domain classification, a second generation, judge/validator latency and risks hallucinated advice, normalization of unsafe conduct or under-refusal; hard refusal remains cheaper and clearer for high-confidence severe risk.",
        "fallback": "If population taxonomy, domain assignment, rewritten-content validation or escalation coverage is weak, keep the original safe response, refuse or route to deterministic crisis policy and qualified human review; never let the rewriter approve its own output.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch72 distinguishes static detection from intervention and closed-loop outcome, and discusses privacy rewrites, but it does not yet give safety response reconstruction a population-specific risk state, separate rewrite proposal/validation authority, or a hard-refusal/human fallback.",
        "anchor": "### 可表示、可静态判别与可闭环执行是三层不同安全前沿",
        "proposed_delta": "旧 refusal/filter 路径在严重风险、低延迟或无法验证替代内容时仍最清楚；当青少年等特定人群的突然 non-engagement 本身会放大风险时，guardrail 可把 risk-domain classification、unsafe/refusal detection、domain-conditioned rewrite 与 independent content validation 串成显式状态机。Classifier/rewriter 只提交风险与候选回复，policy/human owner 决定交付或升级；开发性 taxonomy、真实用户证据、长程上下文或 validator 不足时回退 hard refusal、确定性 crisis policy 与人工支持，不能让 rewrite 以“更有帮助”自证安全。",
    },
    "2605.21706": {
        "adopted": "Refusal-direction ablation is a minimum-confidence projection onto a linear probe boundary rather than knowledge deletion; controlled margins, layer selection and one-shot or per-token activation interventions can push the representation deeper into a compliant region, so refusal geometry must be treated as an attacker-calibrated sensor/path rather than a safety authority.",
        "method": "arXiv:2605.21706v1 HTML §2 refusal suppression as latent-space evasion; §3.1 controlled margins; §3.2 CLE-P/CLE-A activation interventions; Appendix D Bayesian layer/margin search",
        "evaluation": "§4.1–§4.3 results, mechanistic analysis and ablations across 15 instruction-tuned, multimodal and reasoning models; Appendices B–H probes, judges, coherence and additional analyses",
        "nonproof": "§6 Conclusions, Limitations and Future Work: Bayesian optimization chooses layers/margins and the attack relies on linear separability of refused/answered representations; disclosed models and judges do not establish cross-model universality or safety after intervention",
        "boundary": "The evidence supports an attack interpretation and controlled evasion for the disclosed white-box models. It does not show dangerous knowledge is localized to one linear direction, that refusal is the only safety mechanism, or that suppressing/refusing proves deletion or real-world harm.",
        "tradeoff": "Deeper margins improve the tested attack but require white-box probes, calibration, layer search and may damage coherence/utility; distributing refusal geometry may reduce this attack while complicating monitoring and alignment.",
        "fallback": "Without weight access, stable separability or held-out utility/safety validation, retain black-box red-team, external policy, sandbox and least privilege; never promote activation editing directly to a release decision.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch72 already states that behavioral refusal, representation probes and real effect are separate, treats refusal-escape directions and operator interventions as proposal-only evidence, limits them to model/layer/attack identity, and falls back to black-box red-team, output guardrails, sandbox and independent release gates.",
    },
    "2605.21780": {
        "adopted": "A certified backdoor claim must bind one joint training–test neighboring relation to the actual stack of randomized mechanisms: privacy profiles and dominating pairs can compose DP-SGD, subsampling and inference noise into an end-to-end robustness certificate, but only for the declared training radius, input radius, class-probability margin and implementation.",
        "method": "arXiv:2605.21780v1 HTML §3 threat/randomized-mechanism setup; §4 primal–dual DP and privacy-profile decomposition; §5 modular joint training–test certification with DP-SGD, Gaussian noise and DPA",
        "evaluation": "§6.1 poisoning certification and §6.2 joint robustness certification on MNIST/CIFAR-10; Appendix B setup and Appendices F–H accounting/epoch analyses",
        "nonproof": "§7 Limitations: DP-SGD certification samples many models, decomposition scales O(R), and certified robustness trades utility; guarantees remain conditional on the declared relation, numerical profile bound and image-classification mechanisms",
        "boundary": "The evidence supports a compositional certificate construction for the disclosed randomized components and threat radii. It does not certify unmodeled triggers, deterministic pipelines, arbitrary data/model families, implementation mismatch or physical/semantic effects outside the classifier decision.",
        "tradeoff": "Joint certificates expose train/test composition and can be tighter than coarse group accounting, but require stochastic training replicas, numerical privacy-profile composition, per-radius cases and utility loss from noise.",
        "fallback": "When component equivalence, dominating pairs, probability margins or compute are unavailable, report training-only/test-only evidence separately, use empirical adaptive red-team and fail closed for high-risk deployment rather than composing incompatible assurances.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch72 defines privacy units, adjacency, composition, implementation-conformant accountants and empirical audits, but it does not yet distinguish a privacy claim from a joint training–test backdoor certificate or bind both perturbation radii and class margins to one composed randomized artifact.",
        "anchor": "## Differential Privacy 先定义被保护对象，再选择机制",
        "proposed_delta": "旧 DP production contract 主要限制相邻训练记录对发布分布的影响；它不能静默升级为 backdoor robustness。若 threat model 同时允许 R 条训练增删与测试输入半径 rho，certificate owner 必须冻结 joint neighboring relation、DP-SGD/subsampling/inference-noise 等 randomized components、dominating pairs/privacy profiles、class-probability margin 与数值 accountant，再只对该半径签发 prediction invariance。Training/runtime 各自证明组件同构，Security release owner 才组合证据；抽样模型成本、O(R) composition、utility 或实现前提越界时回退分别报告 train/test 证据、adaptive red-team 或拒绝发布。",
    },
    "2605.21938": {
        "adopted": "An accountant's claimed Rényi-DP upper bound and a black-box empirical audit are different evidence directions: neighboring canary-in/out executions plus a class-restricted Donsker–Varadhan estimator can certify a finite-sample lower bound on leakage, while any two-sided or upper conclusion additionally requires a declared bounded-privacy-loss assumption and critic/optimization error accounting.",
        "method": "arXiv:2605.21938v1 HTML §2.1–§2.4 Rényi divergence, hypothesis-test conversion and black-box canary-in/out audit; §3.1–§3.3 lower confidence and class-restricted DV analysis",
        "evaluation": "§4.1–§4.4 DP-SGD audits on MNIST/CIFAR-10 with 500 observations per canary condition; Appendix C worst-case initialization and estimator/conversion comparisons",
        "nonproof": "§3.3 and Appendix B.1–B.3: critic restriction and optimization can only make the lower bound conservative, sample complexity grows with critic dimension, and an upper bound is impossible without bounded privacy loss; experiments are CNN/image/canary specific",
        "boundary": "The audit can falsify too-small claimed RDP budgets or provide a conditional interval for the observed mechanism. Failure to find a violation is not privacy proof, and a lower bound cannot be presented as the mechanism's exact epsilon or legal record-level fact.",
        "tradeoff": "Black-box access reduces instrumentation trust but requires many independent trainings, canary design and critic fitting; richer critics reduce approximation bias while raising sample/optimization cost and interval width.",
        "fallback": "If neighboring execution, canary validity, sample independence, critic convergence or bounded-loss assumptions fail, retain only a conservative observed lower bound/Unknown state, repair the mechanism or use white-box conformance plus a conservative accountant.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch72 requires an implementation-matched accountant and empirical audits/canaries, but does not state the directional semantics of RDP audit evidence, the extra assumption needed for an upper confidence bound, or the separate identities of canary, critic class, samples and optimizer.",
        "anchor": "### Privacy Accountant 必须与真实实现同构",
        "proposed_delta": "旧路径把 accountant 上界与经验 canary audit 同列，容易把一次黑盒未命中误写成 epsilon 已验证。RDP audit 应冻结 adjacency、canary-in/out 训练、输出 statistic、alpha、critic class/optimizer、样本数与置信水平：class-restricted DV 只能先给泄漏下界，critic 或优化不足使其更保守；只有额外声明 bounded privacy loss 等前提才可讨论上界/双侧区间。Auditor 负责 falsification evidence，accountant/release owner 仍负责正式保证；样本、canary、收敛或上界假设不足时保持 Unknown、修复实现或回退保守 accountant/white-box conformance。",
    },
    "2605.22005": {
        "adopted": "A weight-only lm_head SVD can cheaply prioritize token clusters for pre-release inspection, but its vocabulary-coherence score mixes semantic, script and functional geometry; decoded clusters are candidate signals only and cannot prove training-data composition, downstream behavior, harmful capability or tokenizer quality.",
        "method": "arXiv:2605.22005v1 HTML §2.1–§2.4 lm_head SVD, Vocabulary Cluster Score, base/instruct comparison and model setup; §5 Weighted Projection Score",
        "evaluation": "§3.1–§3.6 analyses of GPT-OSS-120B, Gemma-2-2B and Qwen2.5-1.5B; §4 safety interpretations; §5.3 preliminary glitch-token result",
        "nonproof": "§7 Limitations: VCS does not distinguish semantic/script/functional similarity, covers three models, has unknown relation to behavior, and token-selection geometry cannot restructure vocabulary or serve as safety assurance",
        "boundary": "The evidence supports an inexpensive static triage sensor over one lm_head/tokenizer pair. It does not justify causal claims about pretraining data, RLHF persistence, intent, behavioral safety, universal glitch tokens or automatic token removal.",
        "tradeoff": "Static SVD avoids inference and labels and can focus human review, but needs full weights, tokenizer decoding and qualitative adjudication; low-rank geometry can over-prioritize benign multilingual/script clusters and miss harmful behavior not localized in lm_head.",
        "fallback": "When weights are unavailable, clusters are ambiguous or behavior disagrees, keep the model/tokenizer unchanged and use held-out behavioral red-team, tokenizer tests and provenance review; never delete tokens or approve release from VCS/WPS alone.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch72 treats white-box activation/weight signals as proposal-only sensors and keeps tokenizer/model/release identities separate, but it does not yet identify the weight-only lm_head/tokenizer pair as a cheap triage branch or explicitly block geometric vocabulary clusters from becoming training-data and behavior claims.",
        "anchor": "### Policy 还必须约束模型内部可达的参数路径",
        "proposed_delta": "旧 safety audit 依赖 prompt、inference 与标注切片；在 open-weight pre-release 阶段，可对冻结的 lm_head matrix 与 tokenizer 做 SVD/VCS/WPS，只生成优先人工查看的 token/eigenvector candidates。Static analyzer 只拥有 triage signal，tokenizer owner 不因几何分数删词，release owner 仍需 provenance 与 held-out behavior。VCS 混合语义、script、function，三模型结果与未知 behavior linkage 不能证明训练语料或危害；权重不可见、解释歧义或行为不一致时回退常规 red-team、tokenizer regression 与人工审计。",
    },
    "2605.22273": {
        "adopted": "Visible–infrared robustness must test a shared physical-object/mask identity while allowing modality-specific rendering and cross-task effects; a curved-fractal EOT/PSO patch is one digital attack search over that contract, not proof of a realizable physical attack or a universal defense gap.",
        "method": "arXiv:2605.22273v1 HTML §3.1–§3.6 shared curved-triangle geometry, modality-specific Fraser rendering, joint objective, scene initialization, PSO and EOT",
        "evaluation": "§4.1–§4.5 VIS–IR datasets/models, zero-shot classification, captioning, VQA, transfer and ablations",
        "nonproof": "§5 Limitations and Future Work: digital evaluation only; printing, material reflectance, sensor variation, viewpoint, illumination, larger benchmarks and defenses are untested",
        "boundary": "The evidence supports a coupled digital VIS–IR attack within the disclosed models, infrared adaptation and tasks. It does not show physical persistence, deployment prevalence, arbitrary sensor transfer or that the proposed patch defeats production defenses.",
        "tradeoff": "Shared geometry improves cross-modal consistency but adds a compact nonlinear search, modality renderers and EOT/PSO compute; physical constraints can reduce attack freedom and make simpler per-modality tests more interpretable.",
        "fallback": "Without matched sensor calibration or physical validation, retain modality-specific and transformation-aware red-team tests, independent sensor fusion checks and real effect-level safeguards; label the patch result digital-only.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch72 already requires multimodal safety to preserve raw/reconstructed modality state, transformation and model identities, to measure transfer under an explicit attack budget, and to separate digital behavior from external effect/physical evidence; this attack construction adds no new control owner.",
    },
    "2605.22373": {
        "adopted": "Membership-audit target selection for safety classifiers must include low-confidence decision-boundary examples and harm/input-structure slices: ambiguous training items can expose stronger memorization signal than easy high-confidence examples, especially when one record aggregates turns or a user's conversation history.",
        "method": "arXiv:2605.22373v1 HTML §3 problem; §4.1–§4.4 membership setup, boundary-targeted selection, scoring and single/multi-turn/multi-conversation/pooled classifiers",
        "evaluation": "§5 setup; §6.1 attack results across two scores, four models and five toxicity/jailbreak/mental-health datasets; §7.1–§7.2 content diagnosis and post-hoc noise",
        "nonproof": "Appendix A Limitations: two model families up to 12B, small/synthetic datasets, reference-model access, limited defenses and local controlled pipelines; post-hoc noise is not a training-time DP guarantee",
        "boundary": "The evidence supports boundary-targeted privacy red-team for the disclosed safety classifiers. It does not identify real individuals, prove every ambiguous item is memorized, transfer rates to production, or make geometric filtering/noisy logits a complete privacy defense.",
        "tradeoff": "Boundary/harm/input-structure slicing exposes a harder privacy tail but requires confidence access, matched reference models and sensitive longitudinal fixtures; output noise can reduce attack signal while degrading safety-classifier calibration and utility.",
        "fallback": "If reference data, margin calibration or longitudinal consent is unavailable, use controlled canaries, provenance, conservative access/minimization and formal DP where appropriate; keep membership Unknown rather than removing ambiguous safety examples automatically.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch72 already requires membership signals to bind corpus, controls and attacker access, but it does not yet make target-selection/margin a first-class attack identity or cover safety-classifier privacy units that span turns, conversations and harm categories.",
        "anchor": "### Membership Signal 必须先通过可识别性审计",
        "proposed_delta": "旧 MIA audit 常优先 easy/high-confidence examples；对 safety classifier，低 ground-truth confidence 的 contested boundary item 反而可能更能分离 memorization 与 generalization。Privacy audit 应冻结 classifier/margin revision、single-turn/multi-turn/user-history privacy unit、harm category、reference model、score 与 query budget，按 boundary slice 报告而非用总体 AUC。Auditor 只产生风险 signal，data/privacy owner 决定最小化、访问或 DP；synthetic/小模型结果、reference access 与 noisy-logit defense 不构成生产保证，margin 不可靠时回退 canary/provenance/保守权限并保持 Unknown。",
    },
    "2605.22481": {
        "adopted": "Backdoor evaluation cannot assume attack success is monotone in trigger strength or infer safety from improved clean accuracy: training strength, test strength, poison rate and trigger direction must be swept independently because a finite-strength peak and a low-variance direction can hide behind an apparently healthier clean metric.",
        "method": "arXiv:2605.22481v1 HTML §2 Gaussian-mixture poisoning model and proportional/population regimes; §3.1–§3.3 finite trigger-alignment peak and covariance-eigendirection results",
        "evaluation": "§4 ERM versus information limit, clean accuracy and ASR; CIFAR-10/Gaussian-surrogate and ResNet-18 qualitative validation",
        "nonproof": "§5 Conclusion and Limitations: theory assumes Gaussian mixtures and linear/generalized-linear classifiers; deep-network evidence is qualitative, multi-class/non-uniform poisoning and defenses remain future work",
        "boundary": "The evidence supports non-monotonicity and direction sensitivity in the stated high-dimensional model plus limited qualitative checks. It does not predict a universal optimal trigger, production attack rate or defense for arbitrary deep networks.",
        "tradeoff": "A strength/direction matrix catches misleading single-point tests but expands poison construction, retraining and false-positive cost; a sparse smoke test remains cheaper for low-risk artifacts but cannot support a broad robustness claim.",
        "fallback": "When retraining sweeps or covariance assumptions are infeasible, keep the tested strength/direction explicit, add held-out trigger neighborhoods and clean controls, quarantine suspicious artifacts, and avoid extrapolating zero ASR at one strength.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch72 requires exact-trigger neighborhood tests and separates clean accuracy from ASR, but it does not yet require independent train/test strength and direction sweeps or warn that clean accuracy may improve while ASR has an unobserved finite peak.",
        "anchor": "### Backdoor Evaluation 必须测 Trigger 邻域",
        "proposed_delta": "旧 release smoke test 常固定一个 trigger/强度并同时看 clean accuracy；高维 poisoned training 下，clean accuracy 可随训练 trigger 变强而改善，ASR 却在有限强度达到峰值，最小 covariance direction 又可能最有效。Evaluation owner 应把 poison rate、training strength、test strength、direction/covariance、model/data revision 与 clean/ASR controls 组成矩阵；理论 owner 只约束 Gaussian/GLM 条件，不能给深网通用阈值。Sweep 成本过高时保留明确单点边界、held-out neighborhood 与 quarantine，不能从一次零 ASR 或更好 clean score签发安全。",
    },
    "2605.22737": {
        "adopted": "Anti-distillation defenses must be evaluated against a student that reweights released examples by learning value, not only a passive uniform collector; teacher utility, adaptive student gain, trace auditability and generation overhead form one operating frontier, while the teacher-side sampler remains a mitigation rather than a confidentiality proof.",
        "method": "arXiv:2605.22737v1 HTML §2.1–§2.3 teacher fidelity/student budget/value game; §3.1 adaptive-student and §3.2 teacher best responses, including proxy Product-of-Experts generation",
        "evaluation": "§4.1–§4.2 GSM8K/MATH passive versus adaptive students, ADS/PoE frontiers, runtime and trace-quality judge; Appendix C frontier-model and human/judge checks",
        "nonproof": "§5 Conclusion and Future Work: adaptation is limited to tractable value-based reweighting, two math tasks/model families and proxy choices; richer attacks and broader tasks remain open, and one 30-trace human check does not validate general trace utility",
        "boundary": "The evidence supports adaptive reweighting as a stronger evaluation baseline and PoE as one efficiency/utility trade-off. It does not prove model theft is prevented, cover Sybil/query-distribution adaptation, or establish that degraded student accuracy equals protected IP.",
        "tradeoff": "Adaptive evaluation increases attacker realism and changes defense ordering but costs student training/value estimation; PoE is forward-only and cheaper than finite-difference ADS in the test, yet consumes a proxy model and can reduce teacher accuracy or suppress useful rare traces.",
        "fallback": "If proxy value, task transfer or teacher utility fails, retain standard sampling with cross-principal extraction budgets, access controls, watermark/canary and human investigation; report the observed frontier rather than claiming non-extractability.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch72 aggregates extraction budgets across identities and warns that adaptive attackers defeat static audits, but it does not bind antidistillation generation, adaptive student learning value, teacher utility/trace quality and runtime cost into one release/evaluation contract.",
        "anchor": "### Extraction Budget 必须跨身份聚合",
        "proposed_delta": "旧 anti-distillation 评测让 student 均匀消费 teacher outputs，容易高估修改 logits/trace 的防御；真实 distiller 可按 learning value 重加权样本。Security/Evaluation 应冻结 teacher/proxy/student、query/training budget、value function、teacher accuracy、adaptive student gain、trace auditability 与 generation overhead，比较整条 operating frontier；teacher sampler 只拥有输出 proposal，gateway 的跨身份预算与 policy 仍拥有放行。PoE/ADS 仅覆盖两项数学任务与简化 reweighting，不证明不可提取；proxy、utility 或 richer attack 越界时回退标准 sampling、global extraction budget、watermark/canary 与人工调查。",
    },
    "2605.21537": {
        "adopted": "The model that produced a code modernization patch must not own its semantic acceptance: even articulate self-review can miss behavior drift caught by a type-strict execution oracle, and apparent review quality need not improve monotonically with model capability.",
        "method": "arXiv:2605.21537v1 HTML §3 Experimental Design: 60 Python-2-to-3 snippets, type-strict behavioral oracle, 11 models, three prompting conditions and same-model self-review",
        "evaluation": "§4–§7 modernization accuracy, error taxonomy, self-review detection, model/prompt comparisons and oracle/extractor sensitivity analyses",
        "nonproof": "§8 Limitations: Python 2-to-3 only, snippets of at most ten lines, and no multi-model, tool-assisted or human review comparison; the study does not measure repository-scale side effects or production deployment",
        "boundary": "The evidence establishes same-producer self-review as an unsafe acceptance shortcut in the disclosed modernization task. It does not prove every self-review is useless, that the chosen oracle is complete, or that one alternate model/human automatically supplies independent truth.",
        "tradeoff": "An independent behavioral oracle and reviewer reduce self-certification but add fixture construction, execution and adjudication cost; type-strict checks can also reject intentionally compatible coercions if the target contract is underspecified.",
        "fallback": "When an executable oracle is unavailable, retain the original artifact, require explicit semantic invariants and independent review, and mark the patch Needs Review rather than accepting the producer's explanation.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch81 already places tests, hidden/mutation variants and artifact verification outside the producing/optimizing model, states that completion is a bounded packet checked by a read-only verifier, and preserves Needs Review or human design review when the oracle is incomplete.",
    },
    "2605.21605": {
        "adopted": "A self-improving visual agent can turn verified tool-use trajectories into external experience records, distill reusable procedural guidance, and train a new checkpoint, but trajectory evidence, skill artifact and parameter update must remain separate versioned states with independent evaluation.",
        "method": "arXiv:2605.21605v1 HTML §3 trajectory formulation; §4 data and benchmarks; §5.1–§5.5 visual tool trajectories, SFT cold start, prompt-reference program and experience extraction/distillation",
        "evaluation": "§6 main image-generation results, WISE generalization and ablations; appendices for data, rollout, reward and training details",
        "nonproof": "§7 Conclusion and disclosed appendices: the evidence is bounded to image-generation tools, the selected teacher/judge/reward pipeline and finite benchmarks; no production-safety, open-tool or generally autonomous self-evolution guarantee is evaluated",
        "boundary": "The adopted proposition is a trajectory-to-experience-to-checkpoint pipeline with explicit identities, not a claim that the agent validates its own improvement or that distilled visual experience transfers to arbitrary tools and domains.",
        "tradeoff": "Experience extraction can amortize repeated search but adds tool rollouts, judge/reward dependence, training compute and irreversible shortcut/error consolidation into weights.",
        "fallback": "If trajectory validity, judge independence or held-out gains fail, keep verified external experience/skills without updating weights, return to the frozen checkpoint and re-run under controlled tool contracts.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch84 already separates raw trajectory, proposed skill, independent verifier/admission, versioned skill artifact and rollout/outcome evidence; Ch77 separately retains external experience as the reversible baseline before optional checkpoint consolidation.",
    },
    "2605.21810": {
        "adopted": "Verifier feedback from long-context engineering trajectories can drive an oracle–mutator–selector loop that proposes reusable skills, but skill selection must preserve trace identity, repeated-run variance and the external verifier rather than treating one successful trajectory as durable competence.",
        "method": "arXiv:2605.21810v1 HTML §2.1 execution and verifier feedback; §2.2 PassRate, AgentQ and AgentVariance; §2.3 oracle–mutator–selector skill evolution and traceability",
        "evaluation": "§3 setup and metric correlation; §4.1–§4.4 hard Verilog/CVDP results, skill evolution and ablations",
        "nonproof": "§4.5 Limitations: high trajectory variance, compute-heavy thirty-turn/verifier traffic and a Verilog-only benchmark; passing the disclosed verifier does not prove general hardware correctness or cross-domain skill transfer",
        "boundary": "The evidence supports verifier-guided skill evolution and variance-aware evaluation for the disclosed EDA setting, not autonomous proof of correctness, a universal quality metric or unbounded long-context improvement.",
        "tradeoff": "Repeated verifier-guided mutation improves observability but multiplies long trajectories, tool calls and evaluation cost; optimizing against one verifier can overfit its blind spots.",
        "fallback": "When variance, cost or verifier coverage is inadequate, retain the raw trace and versioned skill as a candidate, run independent tests/manual design review, or fall back to the frozen no-skill agent.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch84 already defines trajectory-to-candidate-skill extraction, independent verifier/admission, versioned artifacts, no-skill/skill paired evaluation, trajectory/outcome separation, rollback and lifecycle retirement; it explicitly withholds authority from a single successful trace or judge.",
    },
    "2605.21994": {
        "adopted": "Interpretable GraphRAG can make node contributions exact by constraining the graph encoder to an additive decomposition, but evidence routing must distinguish semantically high-contribution support from structurally necessary low-contribution bridge nodes and must not treat either attribution as factual entailment.",
        "method": "arXiv:2605.21994v1 HTML §3.1 graph construction; §3.2 M-GNAN intrinsically additive graph encoder; §3.3 projection and answer generation",
        "evaluation": "§5 STaRK-Prime evaluation; §6 evidence-routing analysis, fragmentation cases and semantic-versus-structural mismatch",
        "nonproof": "§7 Limitations: one dataset, one detailed query, no same-pipeline post-hoc explanation comparison, no error bars and no user study; exact additive contribution does not establish causal support or graph correctness",
        "boundary": "The evidence supports one architecture-level exact decomposition and the observed need to preserve bridge nodes. It does not prove answer faithfulness, general GraphRAG superiority or that low-attribution structure can be pruned safely on other graphs.",
        "tradeoff": "Additivity provides exact per-node accounting and simpler routing diagnostics but restricts encoder interactions and may reduce predictive performance; preserving bridge nodes increases context and traversal cost.",
        "fallback": "If additive accuracy, graph quality or bridge classification is inadequate, use the stronger conventional GNN/retriever, retain explicit traversal plus claim citations, and mark attribution as post-hoc/unsupported rather than pruning by score.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch76 already records visited, intermediate-bridge and supporting nodes in a versioned traversal and warns that attribution is not truth, but it does not distinguish architecture-exact additive semantic contribution from structural bridge necessity or state the expressivity/performance cost of exact decomposition.",
        "anchor": "### GraphRAG 的 Citation 必须绑定实际 Traversal",
        "proposed_delta": "旧 GraphRAG 可以保存 traversal/citation，再用 post-hoc score 解释节点；当 score 与路径角色混在一起时，语义贡献低的 bridge node 会被错误剪除。RAG owner 可增加 intrinsically additive graph encoder，使 answer-side representation 对节点贡献精确分解；routing controller 仍须把 semantic support 与 structural bridge role 分开保存，graph/corpus revision 和最终 claim entailment 继续由外部证据 Gate 持有。Additivity 会限制 interaction expressivity、可能降低任务性能，且论文仅覆盖 STaRK-Prime/有限案例；准确率或 graph quality 不足时回退更强 conventional GNN + actual traversal + claim citation，把 attribution 标为诊断而非事实证明。",
    },
    "2605.22142": {
        "adopted": "Under partial observability and finite memory capacity, short-to-long-term transfer can be learned as per-memory-item decisions whose values are matched by item identity rather than fixed list position; the learned policy may propose retain/transfer actions but cannot bypass provenance, conflict or capacity governance.",
        "method": "arXiv:2605.22142v1 HTML §2.1 POMDP formulation; §2.2 knowledge-graph memory and transfer decision; §3 per-item Q function and variable-cardinality temporal-difference matching",
        "evaluation": "§4 protocol and baselines; §5 quantitative results, learned-policy analysis and examples; appendices for policy definitions, training, compute and memory snapshots",
        "nonproof": "§6 conclusion and disclosed setup: RoomKG uses symbolic triples, capacity 128 and a bounded partially observable environment; no general text-memory, adversarial-write, privacy, deletion or production-agent evaluation is provided",
        "boundary": "The adopted claim is the set-identity-aware policy formulation for a constrained transfer problem. It does not make Q value a truth score, prove the selected item should become a durable fact, or establish transfer across arbitrary schemas and environments.",
        "tradeoff": "A learned per-item policy can outperform fixed FIFO/heuristics in the tested environment but adds training, reward shaping, value drift and variable-set matching cost; wrong values can permanently displace prerequisites under a hard capacity.",
        "fallback": "If reward calibration, item identity or held-out transfer fails, use explicit heuristic/recency retention, preserve raw episodic evidence, ask/reverify uncertain facts and expand capacity rather than allowing the learned policy to commit semantic memory.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch77 defines typed write transitions, provenance/admission and capacity-aware retention/eviction, but it does not describe a variable-cardinality per-item value policy for transferring short-term observations into finite long-term graph memory or keep that value proposal below durable-write authority.",
        "anchor": "### Write / Hold 不足以定义下一状态",
        "proposed_delta": "旧路径用 FIFO、recency 或手写规则从短期 buffer 迁移到有限长期 Memory，透明且适合稳定环境；部分可观测任务中，同一槽位会承载不同 item，固定位置 Q 会把 identity 与列表顺序混淆。一个条件分支对每个候选 memory item 计算 transfer/retain action value，并在 TD 更新时按 item identity 匹配可变集合；policy 只提交 action proposal，Memory owner 仍执行 provenance、conflict、capacity 与 durable commit。该 evidence 仅覆盖 capacity-128 的 RoomKG/符号 triple，不把 Q value 当真值；reward、identity 或迁移验证失效时回退 heuristic retention、raw episodic evidence、reverify 或扩容。",
    },
    "2605.22205": {
        "adopted": "Modular skillpacks can be generated and rule-verified, trained separately, merged through task-vector deltas, compressed and routed at inference, but every stage must keep skill identity, verifier assumptions, merge order and joint-evaluation evidence explicit.",
        "method": "arXiv:2605.22205v1 HTML §3.1 task/skillpack construction, self-generation, rule verification and preference optimization; §3.2 task-vector merging, quantized full-delta compression and smoothing; §3.3 routing integration",
        "evaluation": "§4 setup; §5 general and agent benchmarks; §6 ablations of construction, merge/compression and routing choices",
        "nonproof": "Limitations: benchmarks use clear domains, task-specific rule verifiers and bounded routing; open-ended or mixed-domain skills, verifier completeness and arbitrary merge interactions are not validated",
        "boundary": "The evidence supports one modular train/merge/compress/route pipeline in the disclosed domains. It does not prove independently valid skills remain compatible after composition or that rule verification grants tool or deployment authority.",
        "tradeoff": "Separate skill deltas improve modularity and storage but add training, verifier, merge-order, quantization and router error; smoothing/compression can hide destructive interactions.",
        "fallback": "If rule coverage, joint evaluation or routing confidence fails, use the frozen base or single validated skillpack, retain full deltas, and require independent regression before any merged artifact is released.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch84 already treats skills as versioned mixed-modal artifacts, separates rule/verifier evidence from admission, requires typed dependency/merge identity and no-skill/skill/alternative comparisons, records compression/runtime compatibility and falls back to frozen or single validated assets.",
    },
    "2605.22221": {
        "adopted": "Reactive backtracking decisions should attend to a canonical current search state rather than the entire order-sensitive trace; history isolation and state localization are separate requirements, and neither solves state aliasing or proactive verification without additional evidence.",
        "method": "arXiv:2605.22221v1 HTML §2 search traces, state and error-localization setup; §3 Selective State Attention with block-relative positions and attention restricted to the current decision block",
        "evaluation": "§4 state-rebuilt transfer, same-state/different-history transplant, architecture ablations and proactive-verification limit",
        "nonproof": "§6 Discussion: the method removes history entanglement but not state aliasing/localization, block-relative positions are needed for length transfer, inference-time context clearing for pretrained LLMs is future work, and proactive verification needs on-policy data",
        "boundary": "The evidence supports a representation/control separation for the disclosed reactive search setting. It does not prove current-state text is complete, solve hidden-state aliasing, or establish that a pretrained LLM can safely clear context in production.",
        "tradeoff": "Selective attention reduces spurious history dependence but requires explicit state blocks, position handling and training changes; discarding trace can remove causal/provenance evidence needed for diagnosis.",
        "fallback": "When state localization or aliasing is unresolved, retain the full auditable trace outside the policy input, rebuild state with a deterministic search engine/checkpoint, or fall back to explicit backtracking plus external verifier.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch79 defines typed current state, versioned path history, external verification and bounded backtracking, but it does not make same-state/different-history invariance an acceptance test or separate policy-input history isolation from durable trace retention and state-aliasing failure.",
        "anchor": "## Search-based Planning 的边界",
        "proposed_delta": "旧 search policy 把整段 trajectory 送入模型，便于保留 provenance，却会让相同当前 state 因不同到达历史产生不同 backtrack verdict。Planner 可以把 durable full trace 留给审计/diagnosis，同时为 reactive policy 构造 canonical current-state block，并用 same-state/different-history transplant 检查不变性；Selective State Attention 与 block-relative position 只拥有 action proposal，search runtime/verifier 持有 state transition 和 commit。它增加 state localization、训练和 position 复杂度，且不解决 state aliasing/proactive verification；定位不可靠时回退 deterministic state reconstruction、显式 backtracking 或外部 verifier，而不是删除唯一审计轨迹。",
    },
    "2605.22662": {
        "adopted": "An autonomous-research platform should expose idea, planning, coding, experiment and writing artifacts through one observable workflow while keeping experiment execution, result validity and publication acceptance with independent owners.",
        "method": "arXiv:2605.22662v1 HTML §2 layered idea/planning/coding/experiment/writing architecture and unified dashboard; §3 experiments and case demonstrations",
        "evaluation": "§3 disclosed research tasks, workflow demonstrations and reported artifact/benchmark outcomes",
        "nonproof": "The short exact-v1 has no dedicated limitations section and provides platform demonstrations rather than independent scientific replication; it does not prove novelty, experiment truth, exactly-once side effects or general autonomous research capability",
        "boundary": "The evidence supports an inspectable multi-agent research workflow case, not a scientific-validity oracle or proof that a unified dashboard closes role, recovery and artifact-consistency failures.",
        "tradeoff": "Layered agents and a dashboard improve specialization and observability but add handoffs, shared-state conflicts, compute and judge dependence; central presentation can conceal unverified underlying artifacts.",
        "fallback": "If experiment receipts, environment identity or independent replication are absent, retain the work as a draft, rerun under a pinned harness and require human scientific adjudication before publication.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch82 already separates scientist/planner/coder/executor/reviewer roles, shared artifact and workflow state, experiment receipts, monitoring, rollback/resume and independent acceptance; it explicitly refuses to equate a dashboard or generated paper with verified research.",
    },
    "2605.22814": {
        "adopted": "Long-horizon exploration needs two distinct memory states: a persistent world representation that supplies spatial novelty/reference state across episodes, and episodic policy context that records recent observations/actions for choosing how to reach novelty; neither state owns environmental truth without fresh observation.",
        "method": "arXiv:2605.22814v1 HTML §2.1 persistent online 3D forward model; §2.2 episodic-context policy; §2.3 training and regularization",
        "evaluation": "§3 indoor-exploration setup and results, persistent/episodic memory ablations, fine-tuning and two out-of-distribution generated worlds",
        "nonproof": "§4.3 and §5: experiments use static scenes and persistent 3D Gaussian Splatting as a proxy; dynamic worlds, broader embodiments and reliable world-state correction remain open, while two generated OOD worlds do not establish production generalization",
        "boundary": "The evidence supports the two-state decomposition and bounded static-scene exploration results. It does not prove the 3D representation is a truthful world model, that novelty equals task value, or that episodic context transfers to dynamic environments.",
        "tradeoff": "Persistent geometry stabilizes novelty estimation and episodic context improves action continuity, but online reconstruction consumes memory/compute, accumulates mapping error and can make stale novelty targets self-reinforcing.",
        "fallback": "If map consistency, localization or scene stationarity fails, re-anchor to direct observations, use short-horizon egocentric context or an explicit validated map, clear stale episode state and escalate rather than acting on inferred novelty.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch77 distinguishes ephemeral Context from persisted Memory and requires state identity/provenance, but it does not separate a persistent external world-reference state from episodic policy context or explain why their independent ablations and owners matter for novelty-driven exploration.",
        "anchor": "## Context 与 Memory 的状态边界",
        "proposed_delta": "旧 exploration policy 只消费当前 observation 或短 history，在静态、短 horizon 场景简单；跨 episode 导航时，‘哪里还新’需要持久 world-reference，而‘怎样到达’需要近期 episodic context。Memory owner 应把 persistent spatial/world state 与 policy episode state 分开版本化：mapper 只提交地图/novelty estimate，policy 只提 action，environment observation/controller 才拥有真实 state 与 effect commit。在线 3DGS 会增加重建/定位成本并累积 stale-map error，exact-v1 又只覆盖静态室内场景和两个生成 OOD world；map consistency 或动态假设失败时回退直接 observation、短期 egocentric context、validated explicit map 或人工/安全 controller。",
    },
    "2605.21539": {
        "adopted": "When forgetting and retaining objectives alternate, optimizer-state identity is part of the unlearning mechanism: a shared base plus objective-specific residual states can interpolate between fully shared and fully decoupled moments according to observed gradient conflict, but empirical forgetting remains only an approximate deletion result.",
        "method": "arXiv:2605.21539v1 HTML §3.1 preliminaries; §3.2 shared base and objective-specific delta optimizer states; §3.3 convergence/directional-conflict analysis; Appendix A pseudocode",
        "evaluation": "§4.1–§4.6 fictitious/real-world unlearning, safety-alignment, multi-task and ablation tests; Appendix C runtime, memory, LoRA and training-curve results",
        "nonproof": "§5 Conclusion and future-work statement; Appendix C.3 shows smaller LoRA gains, Appendix F discusses metric choices, and no scratch-retrain counterfactual, optimizer-state erasure proof or broad multi-objective generalization is established",
        "boundary": "The evidence supports one base-plus-delta optimizer design and its observed forget/retain utility frontier. It does not prove exact data deletion, that shared state contains no forgotten influence, or that the convergence assumptions hold for arbitrary nonstationary objectives.",
        "tradeoff": "Sharing a base recovers common gradient structure while residual states preserve conflict, but adds multiple moments and update-order/hyperparameter dependence; 8-bit states lower memory at quantization risk.",
        "fallback": "If matched-retrain audits, retain utility or optimizer-state identity fail, restore the pre-unlearning checkpoint and use full retraining or a simpler frozen optimizer path; report the result as approximate unlearning.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch27 already states that unlearning must compare counterfactual parameters, optimizer memory and the next update, preserve optimizer revision and matched-retrain evidence, and label residual methods approximate. A particular base/delta moment layout does not strengthen that deletion contract.",
    },
    "2605.21630": {
        "adopted": "Reasoning-data synthesis can represent difficulty as a chain of atomic knowledge/reasoning transformations, retrieve transformations compatible with the current problem state, compose under an explicit coverage distribution, and only convert examples after rollout/provenance filtering.",
        "method": "arXiv:2605.21630v1 HTML §3.1 overview; §3.2 thought-mode extraction; §3.3 retrieval learning; §3.4 distribution-aligned composition; §3.5 rollout-based filtering and conversion",
        "evaluation": "§4.1–§4.4 matched 9,230-example SFT comparisons across nine STEM/math benchmarks, component ablations and coverage/difficulty analyses; Appendices E–I pipeline and sensitivity details",
        "nonproof": "Appendix A Limitations and Future Work: generated diversity is bounded by the reference-derived thought-mode bank; larger models, RL combination and multimodal synthesis are untested, while LLM extraction/judging does not prove problem truth",
        "boundary": "The evidence supports one structural synthesis recipe and bounded downstream comparisons, not recovery of original author intent, complete reasoning coverage, contamination-free novelty or frontier-level human validity.",
        "tradeoff": "Explicit transformation chains improve controllability but require a verified source corpus, retriever, coverage tracker, multiple generations and judges; bank bias and judge error can be composed into every sample.",
        "fallback": "If compatibility, solver/judge agreement or provenance fails, keep the generated item out of training, return to expert/static verified tasks, and report missing modes rather than filling them with unsupported generation.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch27 already requires synthetic-data specification/transition identities, distribution and coverage contracts, provenance, multi-rollout/verifier gates, contamination controls and executable or human-gold fallback; the thought-mode tuple is a bounded recipe inside that existing owner contract.",
    },
    "2605.22389": {
        "adopted": "A data selector may use the sum of only the highest-entropy tokens as a cheap policy-relative reasoning signal across SFT, rejection fine-tuning and RL, but entropy is neither correctness nor difficulty and must be validated against held-out outcomes and diversity controls.",
        "method": "arXiv:2605.22389v1 HTML §2 token entropy; §3.1 high-entropy-sum variants; §3.2 selection rules for SFT, RFT and RL",
        "evaluation": "§4.1–§4.4 matched experiments for SFT/RFT/RL, transfer, scale, sensitivity and negative-diversity analysis; Appendices H–J robustness, length decoupling and cost",
        "nonproof": "§6 Conclusion and Appendix B Model Reliability plus H/I analyses: the score is model/tokenizer/distribution dependent, proxy transfer and top-percent choices are empirical, and entropy does not certify factual or logical quality",
        "boundary": "The evidence supports HES as one low-cost selector in the disclosed reasoning datasets/models. It does not prove a universal quality ordering, replace execution/verifier evidence or justify dropping low-entropy rare modes.",
        "tradeoff": "HES avoids extra judge inference and can transfer from a small proxy, but requires token distributions/logprobs, threshold tuning and diversity safeguards; it can select uncertainty/noise or reject concise correct traces.",
        "fallback": "When proxy transfer, held-out outcome or negative-diversity checks fail, use uniform/stratified sampling, execution or judge-backed selection and retain low-entropy controls.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch27 already defines post-training data selection as a current-policy control loop, requires matched held-out outcome/coverage and diversity evidence, and refuses to grant single uncertainty/difficulty scores truth or permanent deletion authority.",
    },
    "2605.22589": {
        "adopted": "Federated unlearning under edge constraints can separate historical client/layer contribution sensitivity from an Age-of-Information control that sparsifies fine-grained updates, but sensitivity and freshness are scheduling proxies rather than proof that a client's influence was removed.",
        "method": "arXiv:2605.22589v1 HTML §II system/problem formulation; §III-A parameter-alignment/distributional-impact layer sensitivity; §III-B AoI-driven state/action/reward sparsification",
        "evaluation": "§IV assumption-bounded sensitivity/convergence analysis; §V simulations and edge-device testbed across client/class/sample unlearning and heterogeneous data",
        "nonproof": "§V-D exposes degradation for fine-grained sample unlearning; §VI Conclusion has no deletion audit, adversarial clients, privacy proof or broad production network/SLO validation, and theoretical claims depend on §IV assumptions",
        "boundary": "The evidence supports a sensitivity/freshness scheduling mechanism in the disclosed MEC federated setup. It does not establish regulatory erasure, counterfactual retrain equivalence or causal localization of client data in selected layers.",
        "tradeoff": "Layer targeting and sparse fresh updates reduce edge compute/communication but add historical statistics, RL-control drift and coarse localization; sparsity can preserve stale client influence or damage retained utility.",
        "fallback": "If sample-level forgetting, freshness calibration or matched-retrain audit fails, stop the deletion claim, restore a clean checkpoint and use fuller retraining/reaggregation with explicit client/data lineage.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch27 already makes unlearning counterfactual across parameters, optimizer state and next update, requires matched retrain and lineage, labels approximate methods honestly, and separately treats event time/freshness as data identity rather than truth. SCALE does not strengthen those gates.",
    },
    "2605.22651": {
        "adopted": "After coarse image-caption alignment saturates, data curation should separately test whether individual object/attribute/relation phrases affect the measured image-text score under controlled substitution; the result is a relative scorer-specific sensitivity signal, not grounding or causal identification.",
        "method": "arXiv:2605.22651v1 HTML §3 alignment-saturation sweep; §4.1–§4.5 counterfactual phrase intervention and three-invariance replacement; §5.1–§5.3 coarse-to-fine curation",
        "evaluation": "§6 matched-budget CC3M/CLIP, NegCLIP and CE-CLIP results across general and compositional metrics; §7 aggregation, non-redundancy and nonce/text controls",
        "nonproof": "§8 Conclusion and Limitations: PAS is not grounding/localization/identification, depends on the CLIP scorer and rule-based phrase extraction, retains nonce artifacts, uses CC3M-scale ViT-B/32/limited steps and mostly two seeds, and lacks matched large-filter comparisons",
        "boundary": "The evidence supports a two-stage selection contract and one controlled sensitivity proxy. It does not prove that retained phrases are visually true, that the signal transfers to other encoders/corpora, or that moderate benchmark gains persist at web scale.",
        "tradeoff": "Phrase interventions expose compositional supervision beyond pair alignment but require parsing and multiple scorer passes, inherit scorer/tokenizer bias and can miss higher-order phrase interactions; aggressive pruning also harms transfer.",
        "fallback": "If replacement invariance, scorer transfer or held-out compositional gains fail, keep coarse alignment plus random/coverage controls, retain uncertain pairs and use human/grounded region evidence for high-stakes labels.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch27 separates data filtering from training effect and requires counterfactual/coverage validation, but it does not identify the pair-level-alignment saturation boundary or distinguish phrase-level scorer sensitivity from actual visual grounding in multimodal curation.",
        "anchor": "## Quality filtering 在过滤什么",
        "proposed_delta": "旧 image-caption curation 用一个 global alignment score 剔除粗错配，在低质样本明显时便宜有效；进入高 alignment 区间后，它无法判断 object/attribute/relation phrase 是否真正影响该 scorer。Data owner 可先冻结 pair-level baseline，再用保持 subtoken count、lexical removal 与 surface form 的 controlled nonce substitution 计算 phrase sensitivity，并在 matched budget/seed 下决定是否进入候选集。该分数只拥有 selection proposal，不是 grounding、localization 或因果证明；scorer/tokenizer、parser、replacement 与 corpus revision 都必须入账。多次 scorer pass、残余 nonce artifact 和 higher-order interaction 是代价；transfer/held-out gain 或 invariance 失败时回退 coarse alignment、随机/coverage controls、保留不确定样本与人工/region-grounded evidence。",
    },
    "2605.21654": {
        "adopted": "Critic-free LLM RL is not value-free: under the paper's differentiable-rollout and additive-noise assumptions the actor backward pass carries costates whose conditional expectation is a value gradient, while in discrete transformers attention only approximates that path and the missing token-sampling path grows with policy entropy.",
        "method": "arXiv:2605.21654v1 HTML §2.2–§2.3 score/pathwise estimators and costates; §3 continuous shift-policy bridge; §4.1–§4.2 discrete attention path, sampling gap and approximation theorem; Appendix A.1–A.10 proofs",
        "evaluation": "§5 value-gradient-signal × reachable-headroom hypothesis; §6 matched-trajectory costate diagnostics, controlled continuous task and TinyStories/Qwen checkpoint experiments",
        "nonproof": "§3 assumptions require differentiable rollout/reward and shift/additive-noise parameterization; §4's discrete bridge uses attention-path and entropy/sampling-gap bounds; §6 calibrates an affine predictor on disclosed tasks/checkpoints, so the impact law is a hypothesis rather than a universal checkpoint selector",
        "boundary": "The evidence supplies an assumption-bounded interpretation and diagnostic, not proof that practical GRPO differentiates through sampled tokens, that attention costates equal a learned critic, or that low entropy guarantees correct long-horizon credit in arbitrary LLMs.",
        "tradeoff": "Costate/headroom diagnostics can expose when critic-free updates have usable credit, but require hidden-state gradients, matched rollouts and reward estimates; low entropy may reduce the modeled sampling gap while also reducing exploration.",
        "fallback": "If the differentiability, entropy-bound or matched-trajectory assumptions fail, treat the update as an ordinary score-function estimator, retain explicit advantage/verifier diagnostics, add process reward or a learned critic where justified, and select checkpoints by held-out RL outcomes rather than the predictor.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch31 explains sequence-reward/token-credit mismatch and that GRPO removes a learned critic rather than reward design, but it does not explain the attention-path costate interpretation, its discrete sampling gap, or the signal-versus-headroom checkpoint boundary.",
        "anchor": "## Sequence reward 与 token updates 的错位",
        "proposed_delta": "旧解释把 critic-free GRPO 视为把 sequence scalar 复制到 token，简单但容易误读为没有 value-like temporal signal。一个受限解释把 actor backward 的 hidden-state sensitivity 视作 empirical costate：连续可微、additive-noise rollout 下其条件期望等于 value gradient；离散 transformer 只沿 attention path 传播，token sampling path 缺失且误差受 entropy/sampling gap 约束。Reward/verifier 仍拥有 outcome，autodiff 只产生 credit proposal，optimizer 提交 update，evaluation 用 matched trajectory 和 reachable headroom 决定是否采用。代价是 hidden-gradient/rollout 诊断、假设敏感与探索—低熵张力；假设不成立时回退标准 score-function/advantage、process reward、显式 critic 或 held-out checkpoint sweep，不能把该理论当成普适因果证明。",
    },
    "2605.21822": {
        "adopted": "When heterogeneous crowd preferences mix user-specific goals with a truly shared safety penalty, a single averaged reward can be dominated by majority context and entangle the two; a conditional alternative discovers preference-aligned low-level skills and lets a downstream task policy compose only within that skill support.",
        "method": "arXiv:2605.21822v1 HTML §4.1–§4.3 shared-safety assumptions and imbalance analysis; §5.1 policy composition; §5.2 VPL/CPL skill discovery; §5.3 downstream high-level policy and latent-prior regularization; §5.4 theory",
        "evaluation": "§6 safe-RL experiments under balanced/imbalanced preference mixtures and ablations; §7 bounded LLM response-selection evaluation; Appendices C–E data, implementation and additional results",
        "nonproof": "Appendix G requires learned preference-aligned behaviors to be expressive for and share objectives with the downstream task; §4's common-safety result assumes a sufficiently dominant shared penalty, while offline data volume and hidden-context imbalance materially affect comparisons",
        "boundary": "The evidence supports a conditional reward-versus-policy-composition distinction in disclosed safe-RL environments and a preliminary LLM selection task. It does not prove that real crowds share one latent safety objective, that discovered skills are safe, or that latent support enforces hard constraints.",
        "tradeoff": "Policy composition avoids scalar reward-scale tuning and majority leakage but adds skill discovery, offline data, latent coverage, a frozen low-level policy and high-level control; an incomplete skill basis can block valid downstream behavior or preserve unsafe modes.",
        "fallback": "If common-safety, skill expressivity, dataset balance or constraint evaluation is unverified, keep safety as an explicit hard gate/cost, report group-specific preferences, use task-only or separately supervised safe baselines, and require human or environment-level adjudication.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch31 already separates group state, pluralistic aggregation and hard constraints, but it does not state when downstream policy composition over a frozen preference-skill basis is preferable to mixing an entangled crowd reward with a new task reward.",
        "anchor": "### Pluralistic Aggregation 不能把 Group State 压成一个平均 Reward",
        "proposed_delta": "旧路径把 crowd preference 拟合成一个 reward，再与 downstream task reward 加权；当 user-specific goal 与 shared safety 混在同一标量且标注不平衡时，多数 context 会接管排序，weight tuning 也不能解开归属。条件分支先验证 shared safety 假设，再由 preference data 发现一组低层 behavior skills，冻结 low-level policy，让 downstream controller 在其 support 内选择 skill；preference owner/skill owner/task controller 与 hard-safety gate 分开持权。它用 reward-scale/entanglement 风险换 skill coverage、offline data、latent control 与 frozen-basis 成本；exact-v1 又假设 skill 足够表达 downstream objective，不证明真实 crowd 共识。假设、coverage 或 constraint eval 失败时回退 group-specific reporting、显式 safety cost/hard gate、task-only/separately supervised baseline 与人工审查。",
    },
    "2605.22156": {
        "adopted": "In verifier-guided RLVR, a reference policy need not own the update direction: an asymmetric trust region can let verifier-signed advantage determine direction while the reference only scales magnitude, accelerating inferior deviations and damping but not reversing superior ones, with periodic reference refresh as an explicit ratchet state.",
        "method": "arXiv:2605.22156v1 HTML §3.1 directional deviation, positive stop-gradient weights, Accelerated Alignment and Gain Locking; §3.2 iterative bootstrapping/reference refresh; §4 local force-reversal and one-way dynamics analysis",
        "evaluation": "§5.1 Qwen/math RLVR setup; §5.2–§5.3 main and suboptimal-prior comparisons; §5.4 asymmetry, locking, active-sample and refresh ablations",
        "nonproof": "The exact-v1 has no dedicated limitations section; §4 is a local surrogate analysis, §5 is limited to binary math verifiers/Qwen checkpoints, and §4 explicitly says OWPO is not an exact optimizer of forward or reverse KL",
        "boundary": "The evidence supports one direction/magnitude separation for disclosed RLVR tasks. It does not prove verifier correctness, monotonic self-improvement, preservation of non-verifiable behaviors, or safety after repeatedly refreshing the reference.",
        "tradeoff": "One-way weighting can avoid a stale prior reversing verified gains, but adds tokenwise reference inference, asymmetric clipping, active-sample scheduling and reference-refresh state; false-positive verifier rewards can be locked in and iterative refresh can ratchet drift.",
        "fallback": "If verifier confusion, non-verifiable regressions, KL/coverage drift or refresh instability exceeds bounds, freeze the last accepted reference, restore symmetric KL/clipping or plain GRPO, and require independent held-out/safety evaluation before another refresh.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch31 treats KL/reference as update coordinates and separately versions verifier validity and coverage, but it does not allocate verifier-signed direction versus reference-scaled magnitude or make reference refresh a gated ratchet with rollback.",
        "anchor": "### 改变输出分布是目标，不是无副作用的偏好标签",
        "proposed_delta": "旧 KL-to-reference 同时影响方向与幅度，在 prior 可靠时稳定；当 verifier 证明某个 deviation 更优而 reference 已落后，symmetric penalty 可能把 update 反向拉回 prior。条件分支让 verifier-signed advantage 只拥有 direction，reference log-ratio 仅经正的 asymmetric weight 调节 magnitude：inferior deviation 加速，superior deviation 降幅锁定，并把 periodic reference refresh 作为独立、可回滚的 ratchet state。代价是额外 reference forward、active-sample/clip/refresh 状态，且 false-positive verifier 可能被放大锁定；论文只覆盖 Qwen/math binary verifier 与局部理论。verifier confusion、non-verifiable regression、coverage/KL drift 或 refresh 不稳时冻结上次 accepted reference，回退 symmetric KL/plain GRPO，并由独立 held-out/safety gate 决定是否继续。",
    },
    "2605.22454": {
        "adopted": "In multi-cyclic value-based continual RL, rehearsal targets are mutable training state rather than timeless labels: continuously sampling replay items, refreshing stored Q values and applying regularization as soon as samples exist can reduce stale-target and first-task bias in the tested DQN setting.",
        "method": "arXiv:2605.22454v1 HTML §3 multi-cyclic state; §4.1 Q-value regularization and separate rehearsal buffer; §4.2 Live sampling, periodic target Updates and No-Wait regularization; Appendix B pseudocode",
        "evaluation": "§5 Room/Flappy/Catcher protocol and transfer/forgetting metrics; §6 main comparisons and component ablations; §7 Q-norm discussion",
        "nonproof": "§8 Limitations excludes randomized/entirely unique task sequences, requires task labels/frequent refresh, and does not cover actor-critic value-policy interactions or alternative rehearsal uses; evidence is DQN-specific rather than LLM RLHF",
        "boundary": "The adopted claim is the stale-target/state-identity lesson, not universal superiority of Q regularization, transfer to actor-critic/LLM training, or proof that refreshed Q values are correct.",
        "tradeoff": "Live sampling and Q refresh improve temporal coverage but consume replay memory/compute, require task identity and can continually rewrite targets from a drifting critic; frequent regularization can preserve obsolete values and reduce plasticity.",
        "fallback": "If task identity, target calibration or cross-cycle held-out return is unreliable, freeze/version rehearsal targets, reduce or disable Q regularization, use ordinary replay or reset from a validated checkpoint, and report DQN-specific uncertainty.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch31 already treats critic revision, behavior-policy state and replay freshness as explicit transition identity; it rejects stale off-policy credit, supports bounded sample refresh, and falls back to fresh rollout/replay or checkpoint reset. The paper adds a DQN-specific schedule outside the chapter's LLM-RLHF owner but does not strengthen that state contract.",
    },
    "2605.21851": {
        "adopted": "A critic-free token-credit estimator can accumulate privileged/self-oracle likelihood ratios as Bayesian evidence for running success probability, then let the terminal verifier anchor direction while redistributing a fixed trajectory credit budget toward uncertain/pivotal tokens.",
        "method": "arXiv:2605.21851v1 HTML §3.1 Bayesian value recursion; §3.2 self/teacher oracle surrogates; §3.3 factorization; §4 direction anchoring, evidence clipping and GRPO integration",
        "evaluation": "§5.1–§5.3 Qwen/Phi math, science and code results, ablations and length analysis; Appendices F–I extended results, sensitivity, overhead and implementation",
        "nonproof": "§6 leaves non-verifiable/richer partial rewards open; Appendix D.1 derives bias under an imperfect oracle, and the telescoping identity applies to raw rather than clipped/anchored/group-normalized advantage",
        "boundary": "The evidence supports an oracle-dependent credit proposal for binary verifiable reasoning, not causal token attribution, exact posterior recovery, teacher correctness or generalization to open-ended outcomes.",
        "tradeoff": "Running evidence can concentrate a fixed credit budget with one extra scoring pass, but accumulates oracle bias, needs the ground-truth answer/privileged conditioning and adds prior, clip and group-normalization state.",
        "fallback": "If oracle calibration, telescoping residual, verifier direction or held-out outcome fails, use sequence/segment reward, process verifier, ordinary GRPO or a learned critic and preserve the terminal outcome as the only admission authority.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch33 already requires terminal outcome to own direction, bounds teacher/self signals to token-credit proposals, distinguishes sequence/segment/token credit, versions clipping and oracle state, and falls back to process verification or a learned critic; OPPO is a source-specific estimator within that contract.",
    },
    "2605.22537": {
        "adopted": "Heterogeneous models may share rollout experience only after binding generator probabilities and filtering by target-relative competence; cross-model samples are off-policy evidence, and group normalization must remain target-owned rather than using a swarm-wide mean.",
        "method": "arXiv:2605.22537v1 HTML §3.1 truncated importance sampling; §3.2 loss-relative sample filtering; §3.3 F-TIS vertical collaboration",
        "evaluation": "§4.1–§4.7 Qwen2.5 size, expertise and PEFT heterogeneity, OOD math, filtering ablation, F-TIS/VIS and horizontal-collaboration tests",
        "nonproof": "§5 is an early bounded study with no dedicated limitations section; the disclosed experiments cover small Qwen2.5 models and math tasks, show slower initial convergence, and horizontal swarm-mean advantage degrades the smaller model",
        "boundary": "The evidence supports filtered cross-policy reuse in the disclosed vertical setup, not on-policy equivalence, unbiased gradients, arbitrary tokenizer/model-family sharing or decentralized trust/security.",
        "tradeoff": "Sharing generations can raise diversity and amortize rollout compute but requires per-token generator probabilities, target-specific scoring/filtering and extra communication; filtering creates selection bias and heterogeneous support can raise ratio variance.",
        "fallback": "If tokenizer/support, importance-ratio tails, target-owned group statistics or held-out convergence fail, reject foreign trajectories and return to each model's fresh on-policy rollout or matched-family sharing.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch33 already defines cross-policy rollout reuse as experience sharing without probability-coordinate sharing, requires generator/current policy identity, support/tokenizer compatibility, bounded importance correction and target-local group membership, and falls back to on-policy rollout.",
    },
    "2605.22703": {
        "adopted": "Hard PPO/GRPO clipping couples an admission decision with update execution; a stochastic boundary-local rescue can retain a decaying fraction of near-boundary gradients while continuing to suppress deep deviations, but the rescue distribution is part of the trust-region contract.",
        "method": "arXiv:2605.22703v1 HTML §3.1 clipping diagnosis; §3.2 decision/execution ratio decoupling; §3.3 controlled intervention; §4 Near-boundary Stochastic Rescue; §6 expectation-level soft-clipping analysis",
        "evaluation": "§5 disclosed 7B–30B dense/MoE RLVR experiments; §6.1 stability runs and §6.2 layered admission/magnitude/stochasticity ablation; Appendices B–C configurations and compute",
        "nonproof": "The exact-v1 has no dedicated limitations section; claims are bounded to clipping-based DAPO/GSPO recipes and disclosed Qwen math workloads, while stochastic rescue changes gradient variance and the expectation-level inverse-square profile is not a per-run guarantee",
        "boundary": "The evidence isolates one clipping failure and plug-in repair; it does not prove all clipped gradients outside the boundary are useful, that rescued tokens are correct, or that stochastic rescue is a universal trust region.",
        "tradeoff": "Boundary rescue recovers some discarded signal but adds randomness, rescue-probability and magnitude-modulation state, can increase variance and can admit stale or mis-signed evidence near a miscalibrated threshold.",
        "fallback": "If ratio identity, verifier sign, run-to-run stability or held-out quality fails, restore deterministic hard/asymmetric clipping, shrink the update or refresh on-policy trajectories.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch33 already treats clip location/bounds as objective semantics, separates admission from update authority, includes sign-specific and staleness-adaptive contraction, and requires ratio/verifier/freshness evidence plus hard-clipping/on-policy fallbacks. NSR does not change that owner contract.",
    },
    "2605.22817": {
        "adopted": "When deployment includes best-of-k or evolutionary search, training may optimize a set of competent solutions across vector-reward trade-offs rather than one scalar mode; multi-answer context supplies capacity, while stochastic scalarization supplies the diversity incentive.",
        "method": "arXiv:2605.22817v1 HTML §2 reward-space diversity target; §3.1 multi-answer chains; §3.2 Dirichlet scalarization and set-level best-of-set reward; Appendix B GRPO objective/configuration",
        "evaluation": "§4–§5 Maze, MuSiQue, EUREQA, ToolRL and LiveCodeBench/OpenEvolve comparisons; §5 ablations; Appendix A cases and Appendix F reward-collinearity analysis",
        "nonproof": "§7 Discussion and Conclusion limits the claim to search-augmented pipelines; tested reward vectors are disclosed task decompositions, multi-answer candidates share one autoregressive context, and best@k gains do not prove factual diversity, Pareto completeness or safety",
        "boundary": "The evidence supports reward-space set optimization in the evaluated search workloads, not that diversity is always desirable, that every reward component is valid, or that a search selector can repair missing/correlated objectives.",
        "tradeoff": "Set-level vector training improves candidate coverage but uses longer multi-answer rollouts, multiple component evaluations and scalarization samples; shared context couples candidates and weak/correlated reward dimensions can create cosmetic diversity.",
        "fallback": "If reward decomposition, competence floor or downstream search gain is absent, return to scalar GRPO with explicit entropy/coverage monitoring, independent sampling or a single validated answer.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch33 already separates exploration proposals from verifier truth, treats mode/diversity collapse and multi-reward state as independent controls, requires matched rollout/search budgets, and retains scalar GRPO or independent sampling as fallback; VPO is a bounded set-level implementation of this covered branch.",
    },
    "2605.21699": {
        "adopted": "Cross-tokenizer logit distillation must audit probability-mass coverage by task-critical token class before choosing a loss: if critical tokens fall outside an exact-match partition, the common softmax can suppress them and needs full projection; when coverage is sound, a relaxed high-confidence partition can preserve sharper pairwise targets.",
        "method": "arXiv:2605.21699v1 HTML §2.1 span/chunk alignment; §2.2 sparse probability projection; §2.5 P-KL; §2.6 H-KL; §2.7–§2.9 multi-teacher, scaling and coverage-based mode selection; Appendices 6–8",
        "evaluation": "§3 teachers/student/protocol; §3.1 benchmark results; §3.2 P-KL/H-KL, frozen/learned projection, scaling and teacher-weight ablations",
        "nonproof": "Limitations and future work restrict evaluation to Llama-3.2-1B continued pretraining with a few teacher pairs; instruction/preference tuning, larger students and low-overlap SentencePiece/BPE/byte regimes remain untested",
        "boundary": "The evidence supports coverage-aware projection choices in disclosed tokenizer pairs; string/re-tokenization mappings are approximations and do not prove semantic token equivalence, complete mass conservation or multilingual/byte-boundary fidelity.",
        "tradeoff": "Projection recovers unmatched critical mass but adds span DP, a large sparse mapping, top-k truncation and optional learned-map drift; partitioned H-KL is sharper but can silently suppress task-critical unmatched logits.",
        "fallback": "If canonicalization, critical-class coverage, residual mass or behavioral regression fails, retain same-tokenizer KD, byte-level alignment with explicit residuals, or hard sequence distillation and do not merge incompatible token probabilities.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch29 already requires a shared byte/probability interface, tokenizer identity and residual-mass accounting, but it does not explain why exact-match common-KL can suppress unmatched critical tokens or route between full projection and relaxed partition based on category coverage.",
        "anchor": "### 跨 Tokenizer 蒸馏需要共享概率接口，而不只是共享文本",
        "proposed_delta": "旧 cross-tokenizer KD 只对 exact string/common tokens 做 KL、对其余 token 做 rank matching，容易实现；当数字等 task-critical token 被 teacher 切碎却在 student 中是单 token 时，full-vocabulary softmax 会让 common-KL 对未匹配 logits 产生持续抑制。训练 artifact 应先按 critical token class 审计 coverage/residual mass：关键类落出 common set 时，经冻结 canonicalization/span alignment 和稀疏概率投影做 partition-free KL；覆盖可靠时才允许扩展 high-confidence mapping 的 hybrid KL 以保留更尖锐监督。Tokenizer/map owner 只定义概率坐标，teacher 提供监督，student optimizer 提交更新，held-out task 与 multilingual regression 决定接纳。代价是 DP alignment、稀疏矩阵/top-k 截断、映射漂移与额外审计；映射、质量回归或 residual 失败时回退 same-tokenizer KD、显式 byte residual 或 hard sequence distillation。",
    },
    "2605.21924": {
        "adopted": "In VLM on-policy distillation, output agreement need not imply visual reliance; a teacher-relative counterfactual that removes fine-grained image detail can propose sparse token/rollout weights, but this visual-advantage score remains an intervention-specific dependency proxy rather than grounding truth.",
        "method": "arXiv:2605.21924v1 HTML §2.1 teacher scoring with original versus detail-degraded image; §2.2 mask observations; §3.1 rollout reweighting; §3.2 grouped token KL; §3.3 objective",
        "evaluation": "§4.1–§4.5 Qwen3-VL teacher scales, Geometry3K/ViRL39K, eight benchmarks, ablations/controls and compute; §5 token visualization",
        "nonproof": "§7 concludes within one Qwen3-VL family and math/visual corpora; no dedicated limitations section, and the 10% pixelation intervention preserves some global image cues, teacher scores can share model bias, and VA rise does not establish causal grounding or factual correctness",
        "boundary": "The evidence supports a bounded visual-dependency weighting proxy, not that high-VA tokens are causally necessary, that low-VA language is unimportant or that a teacher can certify image truth.",
        "tradeoff": "Sparse visual weighting reduces dilution but needs original/degraded teacher passes, sibling rollouts, thresholds and group normalization; degradation artifacts or teacher blindness can misroute gradient.",
        "fallback": "If perturbation validity, teacher/student agreement or independent visual-outcome tests fail, use uniform OPD, explicit region/answer supervision and matched image-removal controls while retaining final-task evaluation as owner.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch29 already separates shared-perception rollout evidence from reasoning outcome, uses teacher/student aware-span disagreement only as a second witness, requires perturbation and final-task validation, and falls back to uniform distillation; VA-OPD is a source-specific weighting implementation inside that contract.",
    },
    "2605.22263": {
        "adopted": "Privileged self-distillation pressure need not have one sign: student entropy can route reliable teacher disagreement toward low-entropy scaffold stabilization and away from high-entropy forks, while the terminal verifier remains the global correctness anchor.",
        "method": "arXiv:2605.22263v1 HTML §3 three direction/entropy intervention probes; §4 entropy router, gap-reliability gate and verifier-anchored signed objective; Appendix B proof and C algorithm",
        "evaluation": "§5 six math benchmarks/three sizes and execution/exploration metrics; §6 causal fork/revision probes and router ablations; Appendices D–G cross-domain/family and sensitivity results",
        "nonproof": "Appendix I.1 requires verified privileged traces, two forward passes and the disclosed entropy/gap routing; student entropy is not correctness, epistemic-marker/length metrics are only exploration proxies, and tested reasoning families do not establish a universal sign rule",
        "boundary": "The evidence supports a conditional signed-teacher branch under verifier-scored rollouts; it does not prove high-entropy tokens are causally useful, that repulsion creates correct alternatives, or that the privileged self-teacher is reliable.",
        "tradeoff": "Signed routing can preserve exploration while stabilizing routine steps but doubles forward work, adds quantile/gap state and may amplify arbitrary high-entropy noise or repel a correct teacher.",
        "fallback": "If entropy calibration, privileged-trace quality, verifier outcomes or held-out execution/diversity regress, set the teacher correction to zero and return to verifier-only GRPO, uniform/gated OPD or verified SFT.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch29 distinguishes state coverage from token selection and warns that entropy/disagreement are not correctness, but it does not treat teacher-pressure sign as a routed control or specify that verifier direction remains global while privileged self-teacher pressure can be locally attractive or repulsive.",
        "anchor": "### Context Distillation：把可逆 Prompt 行为迁移进权重",
        "proposed_delta": "旧 on-policy self-distillation 对所有 student tokens 向 privileged self-teacher 施加同向吸引，在执行 scaffold 稳定时简单；推理 fork 的高不确定性若正是保留候选所需，这会把 teacher-conditioned style 过早固化。条件分支用 student entropy 和 teacher-gap reliability 路由局部 pressure：低熵 scaffold 只向 teacher 收敛，高熵 fork 可受限反向，但 terminal verifier 仍决定整条 trajectory 的正负方向，teacher 只提 token correction。它增加第二次 forward、quantile/gap state，并可能把随机高熵噪声误当探索；exact-v1 又依赖 verified privileged trace 与受测 reasoning families。entropy/teacher/verifier 或 held-out execution-diversity 失配时将 correction 归零，回退 verifier-only GRPO、uniform/gated OPD 或 verified SFT。",
    },
    "2605.22675": {
        "adopted": "Self-generated training data can be produced by a temporary, gradient-derived low-rank KV projection that biases generation toward a named capability and is removed before SFT; the projected policy and resulting corpus are distinct artifacts, and neither gradient subspace nor raw output is a correctness oracle.",
        "method": "arXiv:2605.22675v1 HTML §3.1 self-policy distillation; §3.2 correctness-span gradients, SVD and K/V projection matrices; §3.3 projection-hook generation and ordinary SFT",
        "evaluation": "§4 code/math/QA in-domain and OOD evaluations; §5 corpus/finetuning ablations and robustness; Appendix A calibration spans, hyperparameters and compute",
        "nonproof": "§6 Limitations asks for broader/high-stakes validation; the subspace comes from labeled correctness-defining spans, raw projected outputs may still be incorrect, and reported benchmark gains do not establish causal or unique capability directions",
        "boundary": "The evidence supports one self-data generation actuator in disclosed tasks/backbones, not external-signal-free truth, universal capability disentanglement or safety of training on unverified outputs.",
        "tradeoff": "Temporary KV projection avoids a permanent teacher at inference but requires gradient collection, per-layer SVD/hooks and extra corpus generation; low-rank selection can suppress coupled skills and self-training can amplify residual errors.",
        "fallback": "If calibration labels, subspace stability, generated-data validation or capability regressions fail, remove hooks, discard the corpus and return to verified external data, ordinary self-training with filters or the untouched base checkpoint.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch29 covers self-distillation target-distribution changes, trainable-subspace identity and external validation, but it does not separate a temporary gradient-derived KV generation policy from the original model and the later SFT corpus or state the rollback boundary for that three-artifact path.",
        "anchor": "#### Self-distillation 也可以改变 Target Distribution",
        "proposed_delta": "旧 self-distillation 直接从 base policy 采样 raw outputs，再筛选或全量 SFT；当目标 capability 被 style/format/error 混在同一输出分布时，条件分支可先用少量 correctness-defining spans 收集 gradient、SVD 得到低秩 K/V subspace，在自生成时临时投影 attention state，随后移除 hooks，再由原模型对生成 corpus 做普通 SFT。这里 base checkpoint、projected generation policy 与 corpus 是三个版本化 artifact：subspace owner 只提生成 bias，validator 决定样本 admission，SFT owner 才提交权重。它增加 gradient/SVD/hook/generation 成本并可能压制耦合能力或自我放大错误；论文仅覆盖 code/math/QA。标签、subspace stability、样本正确性或回归失败时删除该 corpus、移除 hooks，回退 verified external data、常规 filtered self-training 或 untouched base。",
    },
    "2605.21724": {
        "adopted": "Multi-stream residual mixing must treat exact constraint satisfaction, reachable mixing geometry, parameter memory and execution speed as separate axes: a transportation-polytope chart can cover the interior of the full doubly-stochastic set with (n-1)^2 coordinates, while recursive decomposition trades sequential exact construction for partial parallelism.",
        "method": "arXiv:2605.21724v1 HTML §2.2–§2.5 baselines and transportation-polytope decomposition; §3.1 TBP chart and §3.2 recursive TBP; Appendices A/C/H proofs and algorithms",
        "evaluation": "§4.1–§4.3 language-model pretraining implementation, validation loss/bpb and gradient-norm comparisons; Appendix G initialization, four experiments, speed and unstable-run disclosures",
        "nonproof": "§5 Limitations states that nonlinear couplings and recursive structure complicate optimization/implementation, especially at large stream count; experiments are small language-model runs and most configurations are single-seed, so exact matrix feasibility does not prove end-to-end stability, quality or hardware efficiency",
        "boundary": "The evidence supports an exact full-interior parameterization and its expressivity/speed trade-off under the disclosed hyper-connection construction; it does not prove every useful mixer is doubly stochastic, boundary points are equally trainable, or TBP/RTBP improves frontier-scale models.",
        "tradeoff": "TBP removes finite Sinkhorn error and factorial permutation mixtures but is sequential and nonlinearly coupled; RTBP adds hierarchy and partial parallelism while introducing recursive state, implementation complexity and optimizer sensitivity.",
        "fallback": "If chart saturation, gradient stability, kernel cost or held-out quality fails, retain the standard single residual stream or a validated Sinkhorn, permutation-mixture or structured mixer, and freeze the exact mixing implementation in checkpoint identity.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch17 already explains bounded multi-stream residual state and why spectral-norm or orthogonal constraints do not guarantee semantic preservation, but it does not separate approximate feasibility, full-polytope expressivity and executable speed or record the minimal transportation-chart branch.",
        "anchor": "## Residual Stream 从单一累加状态走向 Depth-wise Routing",
        "proposed_delta": "旧单 residual stream 或有限次 Sinkhorn multi-stream mixer 在实现成熟、stream 少且误差可控时更简单；约束变化发生在跨层反复混合必须同时满足 exact double-stochastic feasibility 与完整 mixing expressivity 时。一个条件分支以 transportation-polytope chart 用 `(n-1)^2` 自由度逐项消耗 row/column budget，覆盖 Birkhoff polytope interior；recursive 版本用分块一致性换部分并行。Checkpoint owner 必须联合版本化 stream count、chart/recursion、边界处理和 optimizer，runtime 只执行冻结 mixer，不能把减少迭代偷偷改成另一算子。它消除 finite Sinkhorn error 与 factorial mixture，却付出顺序依赖、非线性耦合、kernel/optimizer 成本；exact feasibility 也不证明端到端质量。chart saturation、gradient/吞吐或 held-out quality 失败时回退 single stream、经验证的 Sinkhorn、permutation mixture 或结构化 mixer。",
    },
    "2605.21842": {
        "adopted": "Attention may combine query-relative similarity with a key-local learned salience gate before value aggregation, but the gate is an inductive-bias proposal rather than intrinsic importance or a licensed cache-eviction rule.",
        "method": "arXiv:2605.21842v1 HTML §3.1–§3.2 standard attention and learned spectral-energy gate; §3.3–§3.6 wavelet variants, causality and complexity",
        "evaluation": "§4.1–§4.7 TinyShakespeare/Penn Treebank setup, scale/wavelet ablations, learned parameters and scalograms; Appendices B–C sequence-length and sensitivity protocols",
        "nonproof": "§6 Limitations restricts experiments to at most 6.2M character-level English models and states that subword/large-model scaling, learned wavelet packets and multilingual behavior remain open; the proposed threshold is not validated as a cache-retention safety boundary",
        "boundary": "The evidence supports one learned key-salience gate at small scale; it does not prove spectral projection measures semantic importance, that low-gate tokens are dispensable, or that the English threshold transfers across tokenizers, languages and long-context systems.",
        "tradeoff": "The extra projection and gate are small in the test models but add calibration and another multiplicative path; wrong salience can suppress query-relevant tokens, and dense QK/value work remains unless a separate executable sparsity contract is added.",
        "fallback": "If gate calibration, tokenizer/language transfer, attention quality or runtime benefit fails, restore ordinary query-key softmax/value aggregation or a separately validated sparse/cache policy.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch14 already defines attention as content-dependent routing, separates pairwise match from explicit gates and executable sparsity, warns that low weight is not semantic dispensability, and requires dense fallback when calibration or backend gains fail; EGA is a small-scale source-specific gate inside that contract.",
    },
    "2605.21883": {
        "adopted": "DPO's response-level preference margin can be redistributed across tokens only through a versioned weighting policy; self-attention from a prompted pairwise judge is one content-aware proposal, not causal credit or preference truth, and it changes both reward attribution and the local KL geometry.",
        "method": "arXiv:2605.21883v1 HTML §2.3 token-weighted DPO; §2.4 derivation and local trust-region interpretation; §2.5–§2.6 swapped-order pairwise-judge attention extraction, normalization and attention-sink repair; Appendices B–D",
        "evaluation": "§3 models/data/training/evaluators; §4.1 main results, §4.2 weight-source comparisons and §4.3 sink/length ablations; Appendices E–H additional models, compute and hyperparameters",
        "nonproof": "Limitations restricts tests to instruction following and modest model sizes and says optimal heads are model-dependent; judge attention is not shown to be causal token credit, shares model bias, needs two extra forward passes and does not validate preference labels",
        "boundary": "The evidence supports a token-weighted DPO objective and one attention-derived weighting heuristic on disclosed preference data; it does not prove attention identifies responsible tokens, that weights transfer across models/tasks, or that better judge scores mean safer behavior.",
        "tradeoff": "Token weighting can focus the relative margin but adds judge prompts, order-swapped forward passes, layer/head choice, sink correction and weight normalization; miscalibrated weights can hide important tokens or overfit judge artifacts.",
        "fallback": "If swap invariance, weight stability, chosen/rejected likelihood, KL or held-out behavior regresses, return to vanilla sequence-sum DPO or verified token spans/process labels while retaining the original pair and reference identity.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch34 states that vanilla DPO is a sum of equally weighted response-token log-ratios and warns that normalization changes the objective, but it does not assign ownership to token-weight policy or bound attention-derived pairwise-judge weights as a non-causal proposal.",
        "anchor": "## Sequence Log Probability 怎样得到",
        "proposed_delta": "Vanilla DPO 对 response token 的 policy/reference log-ratio 等权求和，在 preference 信号均匀且长度分布受控时最清楚；当 pair 的关键差异集中在少数 span 时，token-weighted branch 可重新分配 margin，但这已经改变 reward attribution 与 local KL geometry。一个受限 proposal 让冻结 reference 以 swapped response order 两次执行 pairwise-judge prompt，再从 verdict token 的 attention 提取、归一化权重并显式处理 attention sink。Pair label owner 决定相对偏好，weight extractor 只提 token credit，objective owner 冻结 reduction，optimizer 才提交更新；attention 不是因果解释或 preference truth。它增加两次 forward、layer/head 选择、顺序/attention-sink 与 judge bias；exact-v1 只覆盖 instruction following 和披露模型。swap invariance、weight stability、chosen/rejected likelihood、KL 或 held-out 行为失败时回退 vanilla sequence-sum DPO，或只使用经过验证的 token/process labels。",
    },
    "2605.22432": {
        "adopted": "Schedule-free matrix optimization can move the gradient-evaluation point from a fast iterate toward an averaged iterate over training, stabilizing orthogonalized momentum without knowing the final horizon; the interpolation schedule and both iterates are optimizer state, not a free replacement for evaluation or final decay.",
        "method": "arXiv:2605.22432v1 HTML §3 dominant/bulk diagnosis and SF-Muon trajectory study; §4–§4.1 time-varying interpolation and river diagnostics; Appendix C algorithm, averaging and schedule derivation",
        "evaluation": "§5.1–§5.4 image and 124M/720M/1B Llama-like pretraining comparisons and sensitivity; Appendices D–F hyperparameters, longer runs, wall-clock and ablations",
        "nonproof": "The paper has no dedicated limitations section; Appendix E.2 says 1B hyperparameters were copied from 720M without new tuning, most evidence is bounded to disclosed image/LLM tasks, and river/bulk proxies do not prove frontier-scale optimality or that anytime checkpoints meet downstream quality",
        "boundary": "The evidence supports one schedule-free Muon trajectory and a time-varying evaluation-point control in tested regimes; it does not prove the river-valley interpretation is unique, remove warmup/weight-decay/tuning needs, or dominate horizon-aware schedules.",
        "tradeoff": "The method avoids a final-horizon schedule and damps dominant-direction oscillation but maintains fast/averaged sequences, interpolation state and Muon orthogonalization; large early interpolation can destabilize and checkpoint semantics become more complex.",
        "fallback": "If early instability, averaged-iterate lag, wall-clock or held-out quality fails, restore fixed-beta schedule-free Muon, tuned Muon with cosine/WSD/decay, or AdamW and preserve both optimizer trajectories for rollback.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch28 already requires schedule-free runs to version interpolation, averaged iterate, weight decay and adaptive/matrix step state, separates Muon dominant/bulk geometry from quality authority, and retains WSD/cosine, Muon or AdamW fallbacks; AMUSE is a concrete time-varying instance within that owner contract.",
    },
    "2605.21611": {
        "adopted": "A controllable generator may co-locate a short semantic instruction with its spatial mask by rendering text into the visual condition and using one OCR-pretrained encoder, but renderer identity and phrase/mask support become part of the conditioning contract and the path does not replace unrestricted language conditioning.",
        "method": "arXiv:2605.21611v1 HTML §3 benchmark/interface definition; §4.1–§4.3 unified encoder, mask-aware fusion and two-stage alignment/diffusion training; Appendices A–C renderer and encoder details",
        "evaluation": "§5.1–§5.5 FLUX.1-dev setup, spatial/multi-region quality, efficiency and component ablations; Appendices D–F resolution/seed/free-form/overlap failures and dataset details",
        "nonproof": "§6 limits the interface to mostly 1–3-word labels, rectangular-mask training, one FLUX architecture and a fixed renderer; OCR pretraining is confounded with extra data, and FID/CLIP scores do not prove exact instruction reading or arbitrary natural-language composition",
        "boundary": "The evidence supports a fixed-renderer, short-label spatial conditioning interface for the disclosed generation task; it does not prove text-as-image is lossless, supports long/compositional instructions, or transfers to other fonts, languages, backbones and safety-critical edits.",
        "tradeoff": "Removing the standalone text encoder reduces inference cost but requires OCR-pretrained visual features, two-stage alignment, fixed rendering and mask-aware fusion; small masks, unseen glyphs and semantic ambiguity can silently corrupt the instruction.",
        "fallback": "If OCR fidelity, mask geometry, unseen wording or generation quality fails, retain the separate text encoder/global prompt, use a hybrid text+visual path, or preserve the instruction as explicit text with region coordinates.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch23 already treats rendered text as a lossy modality transport whose renderer, resolution, encoder and token budget are versioned, separates spatial/semantic alignment from truth, and keeps explicit text/source readback as fallback; UniVL is a bounded spatial-conditioning instance of that contract.",
    },
    "2605.21931": {
        "adopted": "Video self-play must reward temporal dependence separately from answer agreement: frame-order perturbation can propose temporally sensitive questions, while the sampled source window can propose a localization target for correct answers, but neither pseudo-signal is ground truth.",
        "method": "arXiv:2605.21931v1 HTML §3.1 questioner–solver self-evolution; §3.2 original/shuffled-frame temporal question reward; §3.3 window-IoU solver reward; Appendices A–B reward implementation and pipeline",
        "evaluation": "§4.1–§4.7 four base models, six benchmarks, ablations, iteration and question-evolution analysis; Appendix C dataset/benchmark details and D keyword analysis",
        "nonproof": "Appendix E.1 limits training to 16 frames and intrinsic supervision focused on temporal sensitivity/localization, leaving long-range, spatial and multi-event dependencies open; majority agreement, perturbation sensitivity and sampled-window IoU can all be wrong or shortcut-prone",
        "boundary": "The evidence supports two pseudo-supervision signals in the disclosed short-video self-play pipeline; it does not prove generated questions are factual, the window is the minimal evidence span, or lexical temporal cues imply causal video understanding.",
        "tradeoff": "Questioner/solver alternation and dual video evaluations expand raw-video supervision but add multiple rollouts, reward weights, pseudo-label feedback and collapse risk; shuffling may create artifacts and fixed windows may include irrelevant evidence.",
        "fallback": "If perturbation validity, pseudo-answer agreement, localization or held-out temporal behavior fails, restore human/verified video tasks, fixed temporal probes and uniform/full-video evidence with explicit timestamps.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch23 already requires temporal alignment/provenance, treats perturbation and probes as diagnostic rather than truth, and demands end-to-end temporal benchmarks plus counterfactual/full-evidence fallback; the questioner–solver reward recipe does not change that representation owner contract.",
    },
    "2605.21954": {
        "adopted": "Prefill attention may be used as a query-conditioned temporal-routing proposal for a second inference pass when decoding loses an earlier localization signal, but attention-head identity and the selected interval are sensors rather than evidence truth.",
        "method": "arXiv:2605.21954v1 HTML §3 attention knockout and TG-head selection; §4.1 debiased/entropy-aggregated interval extraction and confidence gate; §4.2 crop/mask re-inference",
        "evaluation": "§5.1–§5.3 three MLLMs and three VTG benchmarks with ablations; Appendices B–J implementation, head distribution, hyperparameters and latency; Appendix L failure cases",
        "nonproof": "Appendix M limits the method to single contiguous intervals and reports about 3x–4x inference time; recurrent events create multi-peak errors, and when selected heads ignore the true interval the second pass cannot recover it",
        "boundary": "The evidence supports one training-free read-then-regenerate route for disclosed VTG models; it does not prove attention is causal grounding, that one interval contains all evidence, or that localization gains transfer to general video reasoning.",
        "tradeoff": "The second pass can suppress distractors and raise per-frame resolution but requires head calibration, a zero-video bias pass, crop/mask state and up to fourfold latency; wrong or merged peaks can remove necessary evidence.",
        "fallback": "If head stability, confidence, multi-peak handling or latency fails, retain full-video inference, uniform/event-aware sampling, external temporal detectors or human/annotated grounding.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch23 already assigns query-conditioned temporal selectors and attention probes only routing/sensor authority, requires provenance and end-to-end grounding validation, records calibration/latency cost, and falls back to dense/full evidence; this read-then-regenerate instance adds no owner-level rule.",
    },
    "2605.21988": {
        "adopted": "A temporal-behavior test must preserve the expected relation across a paired counterfactual: dynamic questions should change answer under a semantics-preserving motion reversal/flip, while invariant questions should not; pair accuracy and cross-branch reward prevent a fixed shortcut from passing either side alone.",
        "method": "arXiv:2605.21988v1 HTML §3 task router, counterfactual relation reward and null option; §4 paired DyBench/P-Acc; Appendices C–F router validation, reward components and normalization/cancellation analysis",
        "evaluation": "§5.1–§5.3 Qwen3-VL models, DyBench/TimeBlind/general-video results, data controls, ablations and curves; Appendices A–B construction, shortcut isolation and training details; G cases",
        "nonproof": "Appendix H restricts transformations to horizontal flips and temporal reversals, uses an offline reasoning-model router and short DyBench videos; a transformed pair can violate task semantics, router labels can be wrong, and relation consistency is not factual correctness",
        "boundary": "The evidence supports paired change/stay constraints for disclosed reversible video relations; it does not prove arbitrary video edits preserve semantics, that a consistent pair is correct, or that long-horizon causal understanding has been learned.",
        "tradeoff": "Paired branches expose single-frame/language shortcuts but double video rollout/evaluation work, require a versioned transformation and task router, and can reward transformation artifacts or suppress legitimate invariance/variation.",
        "fallback": "If transformation validity, router agreement, pair correctness or general-video regression fails, disable relational reward and return to verified original examples, explicit temporal labels, full-video evaluation and human-reviewed counterfactuals.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch23 requires counterfactual tests for connector shortcuts and records augmentation lineage, but it does not specify a paired relation contract that distinguishes must-change from must-stay questions or prevents one-sided/fixed-answer success.",
        "anchor": "### Connector shortcut",
        "proposed_delta": "单样本视频 QA accuracy 在静态 cue 足够时简单，却无法证明 policy 消费了 motion/order。条件变化后，评测与训练应冻结 original/counterfactual pair、transform revision 与问题关系：对 direction/order 等 dynamic question，flip/reversal 后答案必须按声明关系改变；对 static question 应保持不变，并用 strict pair accuracy 与 cross-branch reward 拒绝固定答案捷径。Transformation/router 只定义 expected relation，原始标签或独立 verifier 仍拥有 correctness，optimizer 只消费通过 Gate 的 paired reward。该分支增加双路 rollout、router/transform lineage 与 normalization 成本，并可能因 flip/reversal 改变不该改变的语义；exact-v1 只覆盖短视频、两类 transform 与披露模型。transform validity、router agreement、pair correctness 或 general-video regression 失败时停用 relational reward，回退 verified original data、显式 temporal labels、完整视频评测与人工 counterfactual。",
    },
    "2605.22072": {
        "adopted": "Multimodal reasoning review should separate locating task-relevant visual evidence from using it in the derivation: a region-supervised focus token can propose the former, while an original-versus-masked next-token divergence can propose where vision changes generation; neither attention mass nor intervention sensitivity is factual-grounding truth.",
        "method": "arXiv:2605.22072v1 HTML §3.1 overview; §3.2 region-grounded <Focus> attention supervision; §3.3 original/masked-image token divergence, evidence-utilization reward and split GRPO advantage",
        "evaluation": "§4.1–§4.5 matched Qwen2.5-VL 3B/7B experiments, ablations and perception-versus-use analysis; Appendix A training/evaluation protocol and cases",
        "nonproof": "§5 Limitations: automated region annotations, one additional masked-image forward per rollout and only the disclosed Qwen2.5-VL backbones; attention concentration and intervention-specific KL do not prove factual correctness, unique causal support or trace faithfulness",
        "boundary": "The evidence supports one region-anchored and intervention-sensitive training recipe on the disclosed image-reasoning tasks. A masked-region effect is conditional on that mask and annotator, and answer-correct attention concentration is not proof that the reasoning trace or visual premise is true.",
        "tradeoff": "The two-stage recipe adds region annotation, selected layer/head supervision, an extra counterfactual forward and a second reward/advantage path; stronger attention can also amplify an incorrect region or annotator error.",
        "fallback": "If region labels, mask validity, attention stability or held-out grounding fail, remove the attention reward, retain answer-level training, preserve full-image evidence, and use external grounding, explicit region labels or human review.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch23 already separates visual evidence write/localization from language read/use, assigns attention and counterfactual branches only sensor/proposal authority, requires independent grounding/behavioral acceptance, records mask/compute cost, and falls back to full evidence and external verification; Faithful-MR1 is a bounded training instance of that contract.",
    },
    "2605.22170": {
        "adopted": "Cross-modal factual-recall mechanisms should be compared with matched clean, corrupted and activation-restored runs over aligned modality spans; weaker speech-path mediation in one model is a diagnostic result, not proof that factual knowledge failed to transfer or that one component owns recall.",
        "method": "arXiv:2605.22170v1 HTML §2.1 clean/corrupted/restored causal mediation; §2.2 SpiritLM discrete speech/text architecture; §2.3 dataset preparation; §2.4 text-to-text and speech-to-text experiments; Appendix A forced alignment",
        "evaluation": "§3 Results and Discussion on SpiritLM with the filtered Known text/synthesized-speech prompts and layer/MLP/attention AIE comparisons",
        "nonproof": "§5 Conclusion and Limitations: a single synthesized Known dataset, one SpiritLM discrete-token model, TTS/ASR and forced-alignment dependencies, and unknown transfer across speech models, text backbones or joint training; the authors explicitly withhold conclusive transfer proof",
        "boundary": "The evidence supports a preliminary modality-matched causal-mediation comparison in one discrete speech-token model. It does not identify a universal factual-memory circuit, prove modality-independent storage, or establish that low restored effect means information is absent.",
        "tradeoff": "Matched activation restoration improves localization but requires TTS, ASR/forced alignment, modality-specific corruption and many interventions; alignment/noise differences can confound the comparison and patched states can be off-distribution.",
        "fallback": "If alignment, corruption comparability or replication across speakers/models fails, keep modality-specific behavioral tests and probes, report the diagnostic as inconclusive, and use input/output grounding rather than naming a shared recall circuit.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch23 already treats speech/text tokenization and alignment as versioned modality identity, distinguishes readable representation from causal control, and requires matched interventions plus behavior before assigning mechanism ownership; the single-model SpiritLM diagnosis does not strengthen that stable contract.",
    },
    "2605.22476": {
        "adopted": "When a resolvent-style attention operator has stable block-local structure plus a light cross-block residue, evaluation can keep each local tile exact and route only the off-block residue through an order-preserving reduced system; this is an operator-specific approximation contract, not generic sparse softmax equivalence.",
        "method": "arXiv:2605.22476v1 HTML §2.1 resolvent operator; §2.2 exact local branch; §2.3 reduced residual branch; §2.4 masking/correctness; §2.5–§2.6 complexity and full algorithm",
        "evaluation": "§3.1–§3.9 controlled entity tracking, latency/accuracy, pruning, head/property capacity, causal language/code and SCROLLS transfer; Appendix B complexity and Appendix C protocols",
        "nonproof": "§3.6 shows collapse when concurrent properties exceed heads; §3.9 and §4 show dense BART fine-tuning remains best and pretrained encoder-decoder replacement is not plug-and-play; results depend on causal masks, block-local routing, resolvent semantics and the measured kernels",
        "boundary": "The evidence supports exact-local/reduced-residual evaluation for the disclosed resolvent-style operator and task regimes. It does not prove the same decomposition preserves ordinary softmax attention, diffuse routing, arbitrary masks, pretrained dense checkpoints or production hardware gains.",
        "tradeoff": "The split lowers asymptotic work only when block locality is strong enough to amortize tiling, pooling/lifting and the reduced solve; it adds block-size choice, two execution branches, kernel overhead and a head-capacity constraint.",
        "fallback": "If routing is diffuse, block/reduced residual error grows, concurrent properties exceed head capacity, pretrained adaptation regresses quality or measured runtime does not improve, return to the dense operator, dense softmax attention or a validated fixed-window/sparse kernel.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch14 separates sparse support from normalization and requires layout-aware kernels with dense fallback, but it does not state the exact-local/reduced-cross-block contract for a resolvent operator, its masking ownership, or the concurrent-property-versus-head capacity failure.",
        "anchor": "Dense attention 的另一条演进不是减少参与交互的 token，而是减少 Q/K 用于匹配的 feature。",
        "proposed_delta": "旧 dense operator 在 routing diffuse、预训练权重强绑定或序列较短时最忠实；固定窗口/稀疏 support 则会直接删除跨块边。约束变化发生在 resolvent-style attention 已呈稳定 block-local 结构、仍须保留轻量跨块传播时：operator owner 冻结 block partition、causal mask、pool/lift 与 reduced-system semantics，runtime 对 block 内执行同一 exact triangular solve，只把 off-block residue 压到 order-preserving reduced system 后再 lift；release Gate 分开验证 local exactness、residual approximation、wall-clock 与 held-out quality。收益取决于 block locality 和 kernel 摊销，代价是双分支、block-size/reduced solve、预训练 mismatch，并且多属性 tracking 在 properties 超过 heads 时会因路由通道不足崩溃。routing diffuse、残差误差、head capacity、适配质量或实测延迟失败时，回退 dense resolvent、普通 dense Attention 或已验证的 fixed-window/sparse kernel；exact-v1 不证明该分解等价于任意 softmax Attention。",
    },
    "2605.22823": {
        "adopted": "High linear decodability across the vision encoder, projector and LLM does not prove that the final readout binds a motion signal to the requested answer; a temporary projector-level motion-delta objective is one diagnosis-driven training proposal, while labels and held-out behavior retain correctness authority.",
        "method": "arXiv:2605.22823v1 HTML §3.1–§3.4 pipeline, data/prompt controls, encoder/projector/LLM probes and readout binding; §4 instruction-tuning transfer; §5.1–§5.3 adjacent-frame delta target, training-only head and objective",
        "evaluation": "§6.1–§6.4 synthetic/real direction, general-video preservation, ablations and OOD transfer; Appendices D–F probe controls, benchmark breakdowns, component analyses and open-ended cases",
        "nonproof": "Appendix F.2 shows unsupported over-specific motion descriptions; Appendix G limits evidence to signed 2-D image-plane direction, synthetic labels, mostly single-object/camera settings, LoRA-centered training and finite backbones, excluding depth, rotation, acceleration, non-rigid/multi-object and long-horizon dynamics",
        "boundary": "The evidence supports a representation-versus-readout binding diagnosis and one training-only 2-D motion auxiliary loss. Linear probes do not show that the model uses the signal, and synthetic image-plane vectors do not establish physical motion understanding or factual open-ended descriptions.",
        "tradeoff": "Probes and auxiliary motion labels improve failure localization and can shape the projector without inference overhead, but add analysis/training cost, synthetic-label bias and a tendency to over-specify ambiguous motion.",
        "fallback": "If probe results do not predict behavior, camera/object assumptions fail, OOD motion regresses or open-ended hallucination rises, remove the auxiliary head, return to ordinary instruction tuning/full-video evaluation, and use tracking/flow, explicit labels or human verification.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch23 already states that encoder/projector/LLM probes only diagnose bottlenecks, that decodability does not imply use, that visual write and language read are separate failure owners, and that counterfactual/end-to-end behavior decides acceptance; DeltaDirect is a bounded motion-specific remediation under that existing rule.",
    },
    "2605.22007": {
        "adopted": "A model can assign substantial aggregate probability to ground-truth answer aliases at the answer-commitment step and still emit a competing token or later diverge; concept-grouped mass is therefore a ground-truth-dependent analytical probe of distributional availability, not knowledge, factuality or a deployable hallucination detector.",
        "method": "arXiv:2605.22007v1 HTML §3 alias-set construction, commitment step and concept-grouped probability mass; §4.1 commitment localization; §4.2 first-token selection versus multi-token divergence; §4.3 within-population mass concentration; §4.4 pre-generation probes",
        "evaluation": "§3 Qwen/Llama Base/Instruct setup and TriviaQA/NQ-Open/MMLU/ARC-Challenge protocol; §4.1–§4.4 matched analyses across 0.8B–72B; Appendices D–M robustness, phrase-level and aggregation analyses",
        "nonproof": "§5 says the probe requires ground-truth aliases, covers 1–3-token answers, greedy decoding and only Qwen/Llama families; alias completeness and concept separation are assumptions, hidden-state decodability is not causal use, and an association with instruction tuning does not prove a universal sharpening cause",
        "boundary": "The evidence supports a bounded distributional diagnosis at disclosed commitment steps. It does not show that the model knows the answer, supply an online truth oracle, establish factual correctness from probability mass, or cover long-form commitments and non-greedy decoding.",
        "tradeoff": "Alias grouping exposes token-fragmentation and commitment failures but requires ground truth, semantic equivalence sets and commitment-step localization; incomplete aliases, multi-token prefixes and competing concepts can change the result.",
        "fallback": "If aliases or commitment steps cannot be validated, report token/sequence uncertainty only as a calibrated risk signal and return to retrieval, external evidence, verifier checks and abstention rather than inferring knowledge from logits.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch8 already separates token probability from truth, treats semantic entropy/answer-mass and hidden-state probes only as calibrated internal risk sensors, distinguishes knowledge/capability/elicitation/reliability, and assigns correctness to external evidence, verification and abstention; the commitment-step analysis is a bounded diagnostic instance of that contract.",
    },
    "2605.22050": {
        "adopted": "A diffusion runtime may treat per-timestep latent-update, latent-norm and reconstructed-initial-latent deviations from a versioned clean-reference region as a memorization-risk sensor and adapt the current denoising trajectory, but the sensor and correction do not prove training-record identity, deletion or privacy safety.",
        "method": "arXiv:2605.22050v1 HTML §4.1–§4.3 empirical regions over latent updates, latent norms and reconstructed initial latents; §5.1 step-wise Z-score detector; §5.2 two-level stability-constrained adaptive sampling; Appendix C algorithms",
        "evaluation": "§6.1 detection on SD1.4/1.5/2.1 with PNDM/DDIM and duplicated versus reference prompts; §6.2 mitigation on pretrained and finetuned SD1.4/DDIM with SSCD, CLIP and FID; Appendices E–F ablations and settings",
        "nonproof": "The paper has no dedicated limitations section; its reference region uses 50 normal prompts, mitigation is centered on SD1.4/DDIM and SSCD-style duplicate similarity, and the asserted sampler-agnostic/universal signature is not established for arbitrary models, schedulers, data, semantic memorization, privacy attacks or legal deletion",
        "boundary": "The evidence supports one calibrated trajectory sensor and on-the-fly correction on the disclosed Stable Diffusion settings. It does not prove that an out-of-region path is memorized, that an in-region output is safe, that the copied source is identified, or that model weights have forgotten it.",
        "tradeoff": "Avoiding detect-then-retry can preserve the current trajectory and reduce restart work, but adds a clean-reference calibration distribution, per-step state, severity thresholds and latent rescaling; distribution drift can cause over- or under-mitigation and semantic damage.",
        "fallback": "If reference coverage, false-positive rate, SSCD/copy audit, semantic fidelity or scheduler transfer fails, disable adaptive projection and fall back to abort/regenerate, the validated static sampler, independent copy/provenance gates, data filtering or training-time unlearning/retraining.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch24 owns mutable denoising state, per-step correction, conditional guidance and commit/fallback control, but it does not state how a calibrated stability region can act as a memorization-risk sensor without acquiring copy, privacy or deletion authority.",
        "anchor": "### Conditional Guidance 把 Diffusion 并行策略变成逐 Step 状态",
        "proposed_delta": "旧的 detect-then-retry 在 copy detector 可靠、重跑成本可接受时最容易隔离状态；固定 guidance/prompt/latent 调整也保持控制面简单，但不能随当前 trajectory 的异常强度变化。约束变化是部署中既要保留当前 denoising path、又要尽早压制潜在复制时：calibration owner 从 clean reference prompts 为每个 timestep/version 冻结 latent-update、latent-norm 与 reconstructed-z0 region；sensor 只报告偏离强度，sampler controller 才按 mild/strong policy 对当前 provisional state 做有界 rescale，独立 copy/provenance/privacy Gate 仍拥有 acceptance。该分支增加 reference-distribution、threshold、per-step state 与 drift 风险，可能把正常稀有样本误压回均值，也可能漏掉不呈该动力学的复制；exact-v1 主要覆盖 SD1.x、PNDM/DDIM、50-prompt calibration 与 SSCD-style 指标，不证明 deletion/privacy。reference coverage、FPR、copy audit、semantic fidelity 或 scheduler transfer 失败时，停用 adaptive projection，回退 abort/regenerate、已验证静态 sampler、独立 copy/provenance 检查，或训练侧 filtering/unlearning/retraining。",
    },
    "2605.22311": {
        "adopted": "Identity-conditioned diffusion unlearning can redirect one conditioning centroid toward a proximity-selected anchor and restrict updates to identity-sensitive cross-attention layers, but generator-side identity suppression is an approximate behavioral edit rather than proof that training records, features or identity information were deleted.",
        "method": "arXiv:2605.22311v1 HTML §3.1 ID-conditioned latent diffusion; §3.2 anchor-guided replacement with preservation loss and negative guidance; §3.3 ArcFace proximity anchor selection; §3.4 condition-driven localized cross-attention fine-tuning",
        "evaluation": "§4 implementation, metrics and comparisons; anchor-distance, preservation-weight and full-versus-cross-attention-versus-surgical-layer ablations; Appendix C adapted baselines",
        "nonproof": "The paper has no dedicated limitations section; results are bound to Arc2Face/ArcFace geometry, disclosed identities and generator-side similarity/quality metrics, while 4.29% localized updates and low identity similarity do not establish record deletion, inaccessible identity across prompts/attacks, legal forgetting or counterfactual retraining equivalence",
        "boundary": "The evidence supports a selective behavioral redirection recipe for one ID-conditioned diffusion architecture. It does not prove information erasure, remove source-data obligations, or generalize its anchor threshold, sensitive layers and preservation balance across encoders and generators.",
        "tradeoff": "Near anchors preserve realism but may leave the target identity; far anchors strengthen suppression but degrade retain identity and image quality. Localized updates reduce touched parameters but can miss distributed identity paths and depend on ArcFace geometry.",
        "fallback": "If forget/retain slices, alternate identity encoders, prompt attacks or generation quality fail, restore the frozen checkpoint, widen or revert the edited layers, isolate the condition adapter, or use lineage-backed retraining and matched counterfactual audits.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch27 already requires unlearning claims to align parameter and optimizer state with matched counterfactual retraining, labels behavioral suppression as approximate, preserves source/checkpoint lineage and separates adapter deactivation from deletion proof; PIU is a method-specific behavioral edit under that data owner contract.",
    },
    "2605.22417": {
        "adopted": "An attribution result explains a model-output difference only relative to a declared input reference and the output produced by that same reference; baseline identity and output matching are therefore part of the evidence artifact, while saliency relative to an implicit or unstable reference is not an absolute explanation.",
        "method": "arXiv:2605.22417v1 HTML §3.1–§3.3 input/output baseline definition; §4.1–§4.4 gradient, Integrated Gradients and Taylor relationships; §5.1 baseline selection, §5.2 output-difference interpretation and §5.3 attribution error",
        "evaluation": "§6 DETR/ODAM and VGG/LayerCAM case studies and batch attribution-error tables; disclosed visualization and normalization protocol",
        "nonproof": "§7 limits the IG path to fixed outputs and notes nonlinearity error for single-step gradient approximations; experiments are bounded to DETR/VGG-style vision models, and the paper's preference for an all-zero image is not shown to be a universal neutral or causal baseline for every modality, model and task",
        "boundary": "The evidence supports declaring the reference input, its induced output and the output difference being attributed. It does not make any chosen baseline semantically neutral, establish causal necessity, validate saliency by human resemblance, or solve attribution for variable-output systems.",
        "tradeoff": "Explicit reference/output matching makes claims inspectable but adds baseline construction, path integration and target matching; multiple plausible references can produce different explanations, and fixed-output alignment can be impossible for detectors or generative models.",
        "fallback": "If the reference is off-manifold, outputs cannot be matched or attributions are unstable across plausible baselines, report the result as reference-conditional, compare multiple controls and return to perturbation, intervention, behavioral and replication evidence.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch5 ranks probes, attribution, intervention and behavior and records replacement-model faithfulness, but it does not explicitly bind an attribution claim to the input reference and the output induced by that same reference, nor state the variable-output matching failure.",
        "anchor": "第四层是内部分析。probe、归因和干预可以生成机制假设，但应与外部行为、消融和重复实验结合。",
        "proposed_delta": "无显式 reference 的 saliency 在默认背景确实中性、输出身份固定时使用最简单，但它只能说明当前 input 相对隐式 baseline 的差异，不能解释绝对输出。约束变化后，evidence owner 必须冻结 input baseline、由该 baseline 实际诱导的 output baseline、当前 output target、path/step 与 model revision；attributor 只分配 `F(x)-F(x')`，evaluation 再用 attribution error、受控扰动、intervention 与 behavior 检查，不让热力图或人类相似度拥有 causal truth。这样换来可复核的 reference-conditional claim，却增加 baseline 选择、积分与 output matching 成本；不同 plausible baselines 会改变结论，DETR/VGG exact-v1 也不证明 all-zero 对任意模态中性。baseline off-manifold、variable output 无法稳定匹配或多 reference 结果漂移时，降级为 reference-conditional observation，并回退多 control、perturbation、causal intervention、behavior 与 replication。",
    },
    "2605.22462": {
        "adopted": "Feature analysis should advance from task localization and feature extraction to causal intervention, robustness stratification and deployment cost, because selectivity, decodability and monitor accuracy answer different questions and no single stage licenses a mechanism claim.",
        "method": "arXiv:2605.22462v1 HTML §3 five-stage methodology; §4–§6 IOI task, activation patching and SAE feature extraction; §7 causal ablation; §8–§11 fidelity, reliability and robustness stratification; §12 deployment-cost analysis",
        "evaluation": "GPT-2-small IOI circuit localization, one 1,024-feature SAE, ablation/selectivity comparisons, distribution-shift slices and threshold/cost sweeps in §§4–12",
        "nonproof": "§14 limits evidence to GPT-2 small, one template IOI task and a small SAE; NLA-inspired evaluations are reframings rather than NLA replications, the selected circuit is not necessary, and the stated production costs/base rates are illustrative assumptions rather than measured deployment outcomes",
        "boundary": "The evidence supports a staged audit and its negative/partial findings in the disclosed small-model setting. It does not establish universal feature identities, necessary circuits, frontier-model behavior or a production monitoring business case.",
        "tradeoff": "Sequencing patching, extraction, ablation, robustness and cost makes evidence claims harder to overstate but adds interventions, slice data, thresholds and operational assumptions; stronger filtering can discard weak but real distributed features.",
        "fallback": "If replacement fidelity, causal effect, seed/slice robustness or cost assumptions fail, retain activation statistics as a hypothesis, disable the feature monitor and return to task-level behavior, raw-model interventions and human review.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch5 already separates information existence, independent decodability and causal use, orders correlation→probe→intervention→behavior→replication, requires replacement fidelity and production slices, and treats online monitoring/cost as a separate acceptance layer; this five-stage case does not strengthen the owner contract.",
    },
    "2605.22488": {
        "adopted": "A candidate algorithmic intermediate can be linearly decoded from a residual stream without being the information carried along the route that causally forms the answer; route-specific ablation and matched donor patching must test use, while a sparse sufficient circuit still does not prove uniqueness or minimality.",
        "method": "arXiv:2605.22488v1 HTML §2.1 held-out base-digit task; §2.2 closed-form probes with initialization/raw-input controls; §2.3 route ablation; §2.4–§2.5 matched key/value patching; §2.6 sparse circuit search; §4.6–§4.9 implementations",
        "evaluation": "Three independently trained 10-layer decoder-only models on held-out number–base intersections, autoregressive exact-answer evaluation, cumulative layer sweeps, N/B/D-matched donor conditions, kept-only circuits and threshold sensitivity",
        "nonproof": "§3 states that output-side computation is not decomposed, nonlinear integration is not ruled out and the circuit is sufficient rather than unique/minimal; the evidence is a synthetic bounded arithmetic task, three seeds and a trained numerical range, and near-perfect held-out accuracy does not establish unbounded algorithmic generalization",
        "boundary": "The evidence rules out one probed staged route as the main causal transmission path in the disclosed models. It does not show that the quantities are never computed elsewhere, identify the unique algorithm, or generalize the factorized circuit to natural language and frontier models.",
        "tradeoff": "Probes cheaply propose hypotheses, while matched route patching and circuit search strengthen causal evidence at the cost of many interventions, donor construction, off-distribution risk and threshold-dependent incompleteness.",
        "fallback": "If patch validity, donor matching, kept-only faithfulness or seed/threshold replication fails, retain only decodability as a representational observation and return to raw behavior, broader interventions and multiple candidate mechanisms.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch5 already separates information existence, independent readout and causal use, requires localized intervention plus downstream behavior, records replacement/circuit faithfulness and rejects sufficiency as uniqueness; this synthetic arithmetic dissociation is direct evidence for the existing contract.",
    },
    "2605.22579": {
        "adopted": "Temperature is rank-preserving, whereas fine-tuning can change the checkpoint's context-dependent token ordering; entropy-matched decoding therefore cannot reproduce a learned rank reordering, and late-layer effective-dimension measurements or late-layer LoRA remain bounded diagnostics and parameter-scope proposals rather than quality proof.",
        "method": "arXiv:2605.22579v1 HTML §2 hyperfitting reproduction; §3 entropy-matched temperature, token-rank and static-bias controls; §4 layer-wise similarity/distance/participation-ratio localization; §5 late-stage LoRA; Appendices B–F model-family replications",
        "evaluation": "§6 cross-domain FS/WritingPrompts/AG News, TTR/repetition/MAUVE and decoding baselines, emergence and training-cost comparison, token-level rank analysis; disclosed 1.5B–8B model appendices",
        "nonproof": "§7 limits the mechanism study to at most 8B and says lexical-diversity metrics do not establish semantic coherence or factual accuracy; training remains long, participation-ratio expansion is an association rather than a unique causal mechanism, and last-five-layer success does not prove a universal optimal parameter mask",
        "boundary": "The evidence distinguishes a learned checkpoint change from a rank-preserving temperature transform in disclosed open-ended generation settings. It does not prove hyperfitting improves truth, safety or arbitrary tasks, nor that terminal expansion is the sole cause or transfers to 70B+ models.",
        "tradeoff": "Late-layer adaptation touches fewer parameters and can preserve early representations, but still requires long training, layer-scope selection and checkpoint timing; context-dependent rank promotion may improve diversity while degrading facts, safety or deterministic task behavior.",
        "fallback": "If held-out coherence/factuality, retain slices, layer-localization stability or checkpoint timing fails, restore the base checkpoint, use full/standard LoRA or conservative SFT, and choose the serving decoding policy independently.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch29 already separates SFT parameter updates from serving decoding, treats parameter masks as versioned selection artifacts, requires token/output-space geometry plus rollouts rather than weight distance, and keeps full/LoRA/conservative checkpoints as fallbacks; Ch20 already owns the rank-preserving temperature boundary.",
    },
    "2605.22658": {
        "adopted": "A pretrained SAE plus learned query codebook can expose which sparse activations feed a supervised segmentation head and render per-slot heatmaps/confidences, but this inspectable interface does not prove that feature labels are unique, the textual reasoning is faithful or the selected sparse features causally implement the mask.",
        "method": "arXiv:2605.22658v1 HTML §3.1 MLLM–SAE–query-codebook–mask-decoder architecture; §3.2 sparse-concept interface and slot heatmaps; §3.3 GRPO plus segmentation/confidence supervision",
        "evaluation": "§4.1 setup; §4.2 RefCOCO/+/g, gRefCOCO and ReasonSeg comparisons; §4.3 activation-count and instance-coverage analyses; §4.4 group-size, training-mode, backbone and reward ablations",
        "nonproof": "The paper has no dedicated limitations section; experiments are bound to disclosed LLaVA/Qwen backbones and segmentation datasets, top-K activation coverage is correlational, the SAE/codebook/decoder are jointly selected around supervised masks, and no matched feature intervention proves faithful CoT or unique concepts",
        "boundary": "The evidence supports an inspectable sparse interface and segmentation result on the disclosed systems. It does not establish universal SAE semantics, causal reasoning faithfulness, factual explanation, zero-shot open-world grounding or independent verification of the generated CoT.",
        "tradeoff": "Sparse slots and provenance improve inspection but add a large SAE, codebook/encoder, mask supervision, GRPO rollouts and matching/confidence calibration; sparse features may split, collide or encode dataset shortcuts.",
        "fallback": "If reconstruction, slot stability, mask grounding, intervention or held-out behavior fails, treat the sparse path as a diagnostic only and return to direct latent/text localization, explicit boxes/masks, external grounding and end-to-end behavior.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch5 already states that SAE features and natural-language labels are replacement-model hypotheses, requires reconstruction/fidelity, interventions and behavior before causal claims, and distinguishes inspectability from faithful computation; SegCompass adds a bounded segmentation interface rather than a new representation-evidence rule.",
    },
    "2605.22691": {
        "adopted": "In a linear Gaussian beta-VAE, posterior collapse can be the rate–distortion objective's mode-wise spectral pruning rather than only an optimization failure: a normalized information price and scale-invariant posterior signal fraction expose when each PCA-like mode ceases to carry input-dependent information, but the equivalence is a calibrated null model, not a general nonlinear theorem.",
        "method": "arXiv:2605.22691v1 HTML §II normalized rate–distortion control; §III single-mode collapse and scale-invariant signal fraction; §IV PCA calibration; §V utility/collapse spectral pruning",
        "evaluation": "§IV–§V WorldClim linear-Gaussian beta-VAE collapse scans, truncated posterior-mean reconstructions, PCA spectrum comparison and utility-versus-threshold analysis; Appendix A experiment details and B–C diagnostics",
        "nonproof": "§VI says nonlinear decoders, non-Gaussian likelihoods, finite training, optimization and near-degenerate modes can rotate/mix/renormalize the spectrum; §VII calls this a first step, says the scan ranks variables but does not interpret them, and the paper has one WorldClim linear experiment without downstream semantic or generation evaluation",
        "boundary": "The evidence proves the collapse-threshold/utility/PCA equivalence only for the linear Gaussian calibrated model and empirically checks that setting. For nonlinear VAEs the scan is a diagnostic whose finite utilities and thresholds must be measured; it does not identify semantic factors or prove every collapse is beneficial.",
        "tradeoff": "Scanning normalized information price reveals a data-dependent active-rank frontier without fixing capacity first, but requires multiple trained/evaluated operating points, likelihood/variance normalization and stable mode matching; rotations, mixed modes and fit noise can obscure identity.",
        "fallback": "If mode identity, reconstruction frontier, scan reproducibility or downstream quality fails, stop interpreting collapse as pruning and return to a fixed validated latent budget, PCA/reconstruction controls, lower regularization, anti-collapse schedules or a conventional VAE retrain.",
        "decision": "Integrate — root writeback pending",
        "existing": "Ch23 already requires jointly choosing representation rate, distortion and downstream capacity, but it does not explain when posterior collapse is objective-selected mode pruning, how to normalize beta by decoder/data scale, or why a collapse scan is only a utility ranking rather than semantic interpretation.",
        "anchor": "### Rate、distortion 与下游容量必须联合选择",
        "proposed_delta": "把 posterior collapse 一律当作训练故障，在 decoder 过强、优化失衡或任务确实需要全部 latent 时是安全起点；预先固定 latent count 也最容易部署，却无法判断被删除维度是无用 tail 还是被错误压掉的信息。在线性 Gaussian beta-VAE 的严格边界内，可把 `T = beta * sigma_dec^2 / V` 作为归一化 information price，扫描 T，并用对 latent rescaling 不变的 posterior signal fraction 判断每个模式何时停止携带 input-dependent information；representation owner 冻结 likelihood、decoder variance、data variance、beta schedule、latent/model revision 与 mode matching，scan 只给 utility-ranked capacity proposal，下游 reconstruction/semantic/generation Gate 才拥有采用权。该路线用多 operating-point 训练、谱匹配与归一化成本换 data-dependent active rank，也会受 mode rotation/mixing、degeneracy、finite optimization 和 nonlinear branch dependence影响；WorldClim exact-v1 只证明线性 Gaussian 下 collapse threshold、marginal reconstruction utility 与 PCA weight 的一致，不解释 latent 语义，也不证明所有 nonlinear collapse 有益。mode identity、frontier、scan reproducibility 或 downstream quality 失败时停止用 pruning 叙事，回退固定 latent budget、PCA/reconstruction control、降低 regularization、anti-collapse schedule 或常规 VAE retrain。",
    },
    "2605.22719": {
        "adopted": "A sparse feature with a strong success/failure effect size and a plausible auto-generated label is a confound candidate, not a mechanism: lexical stratification, raw-activation comparison, matched ablation and seed stability must precede causal or predictive use.",
        "method": "arXiv:2605.22719v1 HTML §III corpus, SAE activation logging, multiple-testing statistics, raw-feature prediction and seed protocol; §IV-B–§IV-D top-feature audit, lexical subset and three controls",
        "evaluation": "§IV-E–§IV-G failure prediction and conditioned residual analysis on 300 IOI prompts, GPT-2 small layer-8 Bloom SAE, five seed reruns and feature-versus-raw baselines",
        "nonproof": "§VI limits evidence to one sub-billion model, one SAE/layer/task, one human auditor and auto-generated labels; one feature/layer ablation cannot rule out distributed or earlier causes, and a robust lexical failure slice does not make the selected SAE feature causal",
        "boundary": "The evidence establishes a lexical keys-slice failure and rejects the simplest single-feature mechanism in this audit. It does not identify the distributed cause, validate SAE labels, generalize to agents/larger models or turn activation prediction into calibrated failure probability.",
        "tradeoff": "Sparse audits cheaply surface slices and candidate features but add multiple testing, label interpretation, seed instability and confounding; causal controls and raw baselines cost interventions but prevent a readable label from becoming a false mechanism.",
        "fallback": "If feature identity, ablation, raw-baseline advantage or seed replication fails, retain only the behavioral slice, disable feature-based decisions and return to raw activations, task-level regression tests and broader interventions.",
        "decision": "No Change — Existing Coverage",
        "existing": "Ch5 already says interpretable labels are not feature identity, orders correlation before intervention/behavior/replication, requires collision/activation/intervention controls and uses raw examples when labels fail; this honest negative audit is a bounded validation of that existing rule.",
    },
}

NEW_INTEGRATES = {aid: review for aid, review in DEEP_REVIEWS.items() if review["decision"].startswith("Integrate")}
ROOT_APPLIED_DEEP_BATCH_5 = {
    "2605.22223", "2605.22596", "2605.22705", "2605.22765", "2605.22821",
}
ROOT_APPLIED_DEEP_BATCH_3 = {"2605.21865", "2605.21958", "2605.22237"}
ROOT_APPLIED_DEEP_BATCH_REFUSAL = {"2605.21545"}
ROOT_APPLIED_DEEP_BATCH_SECURITY = {
    "2605.21609", "2605.21780", "2605.21938", "2605.22005",
    "2605.22373", "2605.22481", "2605.22737",
}
ROOT_APPLIED_DEEP_BATCH_AGENT = {"2605.21994", "2605.22142", "2605.22221", "2605.22814"}
ROOT_APPLIED_DEEP_BATCH_DATA_RLHF = {"2605.22651", "2605.21654", "2605.21822", "2605.22156"}
ROOT_APPLIED_DEEP_BATCH_SFT_3 = {"2605.21699", "2605.22263", "2605.22675"}
ROOT_APPLIED_DEEP_BATCH_ARCH_DPO_2 = {"2605.21724", "2605.21883"}
ROOT_APPLIED_DEEP_BATCH_RELATION_1 = {"2605.21988"}
ROOT_APPLIED_DEEP_BATCH_ATTENTION_1 = {"2605.22476"}
ROOT_APPLIED_DEEP_BATCH_SENSOR_ATTRIBUTION_2 = {"2605.22050", "2605.22417"}
ROOT_APPLIED_DEEP_BATCH_SPECTRAL_1 = {"2605.22691"}
ROOT_APPLIED_DEEP_INTEGRATES = (
    ROOT_APPLIED_DEEP_BATCH_5 | ROOT_APPLIED_DEEP_BATCH_3 |
    ROOT_APPLIED_DEEP_BATCH_REFUSAL | ROOT_APPLIED_DEEP_BATCH_SECURITY |
    ROOT_APPLIED_DEEP_BATCH_AGENT | ROOT_APPLIED_DEEP_BATCH_DATA_RLHF |
    ROOT_APPLIED_DEEP_BATCH_SFT_3 | ROOT_APPLIED_DEEP_BATCH_ARCH_DPO_2 |
    ROOT_APPLIED_DEEP_BATCH_RELATION_1 | ROOT_APPLIED_DEEP_BATCH_ATTENTION_1 |
    ROOT_APPLIED_DEEP_BATCH_SENSOR_ATTRIBUTION_2 | ROOT_APPLIED_DEEP_BATCH_SPECTRAL_1
)
ACTIVE_NEW_INTEGRATES = {
    aid: review for aid, review in NEW_INTEGRATES.items() if aid not in ROOT_APPLIED_DEEP_INTEGRATES
}


INTEGRATES = {
    "2605.21492": {
        "anchor": "### Attribution 是 Versioned Evaluation Contract",
        "proposed_delta": "当相关特征允许多个近等价模型给出相反排序时，单 checkpoint 的 faithful ranking 不能同时被宣称为跨重训稳定且完整；Evaluation Run 应冻结训练 seed/model ensemble、相关结构与 attribution method，优先报告稳定组/tie/ensemble consensus，并披露未能同时满足的性质。",
        "evidence_boundary": "arXiv:2605.21492v1 HTML §3 The Attribution Impossibility; §5 Resolution: Ensemble Attribution via Dash; §10 Empirical Validation; §13 Discussion—Limitations。",
        "tradeoff": "ensemble 与稳定组报告增加重训/解释成本，并牺牲组内完整排序。",
        "failure_fallback": "因果效应不对称、模型集合不代表部署或 attribution target 改变时不能套用对称性结论；回退单模型 attribution、明确 seed/model identity，并附 instability disclosure。",
    },
    "2605.21515": {
        "anchor": "### Agent Regression Testing 需要分配 Evidence Budget",
        "proposed_delta": "Prompt program 在部署时仍由 LLM 执行，少量通过样例不能沿用 symbolic program 的近二峰性能先验；发布信心应把 artifact kind、LLM/temperature、task distribution、pass/fail evidence 与经检索构造且版本化的 performance prior 一起绑定。",
        "evidence_boundary": "arXiv:2605.21515v1 HTML §2 Predicting Performance from Examples; §3 The Performance Prior; §4 RAP; §5 Experiment; §7 Conclusion, Limitations, and Future Works。",
        "tradeoff": "先验语料、相似任务检索与 posterior calibration 增加维护成本，错误近邻会形成伪信心。",
        "failure_fallback": "iid task/instance 假设、语料可交换性或 prior calibration 失效时，停止用少量 pass 作认证，回退扩大 held-out execution、分层抽样与保守 release gate。",
    },
    "2605.22714": {
        "anchor": "### Judge 的输入扰动必须保留 Clean Twin",
        "proposed_delta": "批量复用同一 Judge conversation 会让历史 verdict 的 polarity 成为未声明的 evaluation state；默认每项使用 fresh context，必须 batching 时保存并平衡 history、在 clean twin 上校准偏移，尤其对 baseline 高不确定项。",
        "evidence_boundary": "arXiv:2605.22714v1 HTML §3 Methodology; §4 Results; §5 Characterizing AMEL; §7 Mitigation Experiments; §9 Limitations。",
        "tradeoff": "fresh context 降低 prefix/cache 复用效率，balanced history 也不能消除所有顺序与语义偏差。",
        "failure_fallback": "证据仅覆盖英语、binary judgments、三域与披露模型；越界时回退 deterministic outcome/人工 anchor，或把 history 固定为 Evaluation Identity 并报告不确定。",
    },
}


EXISTING_PROPOSITIONS = {
    "PLATFORM-EVALUATION-SYSTEM": "当前 Ch66 已把 harness/environment/backend、分布切片、judge 输入扰动、mutation strength、attribution 与 release authority 纳入 Evaluation Identity。",
    "PLATFORM-SECURITY": "当前 Ch72 已把 model signal 限为 policy-bound sensor，并覆盖 refusal、rewrite、attack budget、privacy/unlearning 与独立 utility/effect Gate。",
    "TRAIN-DATA": "当前 Ch27 已覆盖版本化 data lineage、selection/mixture/attribution、删除证据与参数链耦合。",
    "TRAIN-SFT": "当前 Ch29 已覆盖 distillation target/occupancy、data-subset×parameter-mask 联合选择、跨 tokenizer 概率接口与能力回退。",
    "TRAIN-RLHF": "当前 Ch31 已覆盖 proxy reward、credit assignment、独立 Evaluation、mode/diversity 与 checkpoint rollback。",
    "TRAIN-GRPO": "当前 Ch33 已覆盖 group-relative credit、reward/evaluator 分权、探索预算与 rollout/evaluation identity。",
    "TRAIN-DPO": "当前 Ch34 已覆盖 preference pair identity、margin/objective coupling、sample filtering 与 failure/fallback。",
    "TRAIN-PRETRAINING": "当前 Ch28 已覆盖 optimizer/regularization、data/objective scaling、checkpoint 与受限实验外推。",
    "MODEL-SELF-ATTENTION": "当前 Ch14 已覆盖注意力读写、稀疏/门控分支、代价与可观测失败边界。",
    "MODEL-TRANSFORMER-LAYER": "当前 Ch17 已覆盖残差/层内机制、表示干预、因果与相关证据边界。",
    "MODEL-MOE": "当前 Ch21 已覆盖 topology-conditioned multicast、relay state、reverse-tree reduction 与拥塞回退。",
    "MODEL-SAMPLING": "当前 Ch20 已覆盖采样分布、temperature 之外的几何变化、质量/多样性与停止边界。",
    "MODEL-LONG-CONTEXT": "当前 Ch22 已明确 Gated DeltaNet-2 的独立 erase/write gate、实验边界、代价与 fallback。",
    "MULTIMODAL-REPRESENTATION": "当前 Ch23 已覆盖 encoder/projector/readout 的责任分解、temporal aliasing、connector shortcut 与“感知到不等于行动/读出使用”。",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "当前 Ch24 已覆盖生成表示、训练/推理耦合、memorization 与受限质量证据。",
    "WORLDVIEW-REPRESENTATION": "当前 Ch5 已覆盖 probe/SAE/attribution 的相关性边界、causal intervention 与 representation-not-computation 风险。",
    "WORLDVIEW-LLM-INTELLIGENCE": "当前 Ch8 已区分 capability、knowledge、elicitation、reliability 与内部冲突 sensor。",
    "PLATFORM-GATEWAY": "当前 Ch62 已覆盖 gateway response/path provenance、policy identity、不可验证改写与 provider/session fallback。",
    "INFER-TENSORRT-LLM": "当前 Ch49 已覆盖 approximation/quantization 的逐 decision-family margin calibration、端到端 effect 验证与 fallback。",
    "AGENT-WORKFLOW": "当前 Ch81 已覆盖 patch composition、isolated effect、真实持久化顺序 replay、hidden/mutation tests 与 rollback。",
    "AGENT-RAG": "当前 Ch76 已覆盖 semantic/structural graph credit、anchor/connector、pruning frontier、evidence subgraph 与 provenance。",
    "AGENT-MEMORY": "当前 Ch77 已覆盖 keep/drop/rewrite、短长程 admission、source episode、capacity、promotion 与 selective deletion。",
    "AGENT-PLANNING": "当前 Ch79 已覆盖 search state、backtracking、verification、history/context 边界与显式状态序列化。",
    "AGENT-PLATFORM": "当前 Ch84 已覆盖 skill evolution、runtime harness、artifact inspection、monitoring 与 rollback/resume ownership。",
    "AGENT-MULTI-AGENT": "当前 Ch82 已覆盖角色/共享状态、协作拓扑、judge 分权、trace 与 rollback。",
    "AGENT-MCP": "当前 Ch83 已覆盖 MCP identity、schema/capability、authorization、transport 与 effect receipt。",
    "INFER-GPU-MEMORY": "当前 Ch54 已覆盖显存/分层存储、权重与状态身份、容量/带宽取舍及回退。",
    "INFER-KV-CACHE": "当前 Ch45 已覆盖 KV identity、压缩/量化、正确性与性能验收及 fallback。",
    "MULTIMODAL-EMBODIED-VLA": "当前 Ch26 已覆盖 VLA action representation、训练/推理边界、闭环 state/effect 与安全验收。",
    "MULTIMODAL-WORLD-MODELS": "当前 Ch25 已覆盖 world-state representation、transition/prediction、物理/控制评测与闭环边界。",
    "PLATFORM-COST": "当前 Ch70 已覆盖质量/成本联合预算、GPU/能耗测量、归因与控制 owner。",
    "PLATFORM-MONITORING": "当前 Ch67 已覆盖 model/runtime/agent 监测信号、OOD/drift、独立 authority 与响应回退。",
    "TRAIN-DISTRIBUTED-TRAINING": "当前 Ch36 已覆盖通信/计算/状态语义、collective correctness、弹性与性能证据边界。",
}


SOURCES = [
    ("SRC-OPENAI", "https://openai.com/research/", "官方 Research 目录与相邻日期条目", "已检查", "窗内无可确认的研究/系统事件"),
    ("SRC-ANTHROPIC", "https://www.anthropic.com/research", "官方 Research 目录与相邻日期条目", "已检查", "窗内无可确认条目"),
    ("SRC-GOOGLE-AI", "https://deepmind.google/research/", "Google DeepMind / Google Research 官方目录", "已检查", "窗内无可确认条目"),
    ("SRC-META-AI", "https://ai.meta.com/research/publications/", "Meta 官方 Publications 目录", "受阻", "官方目录本次返回空响应，不能据此证明无遗漏；恢复后只重开本源本窗"),
    ("SRC-QWEN", "https://qwenlm.github.io/blog/", "Qwen 官方 Blog / publication index", "已检查", "窗内无可确认条目"),
    ("SRC-DEEPSEEK", "https://api-docs.deepseek.com/news/news250120", "DeepSeek 官方模型/研究发布入口", "已检查", "窗内无可确认条目"),
    ("SRC-MOONSHOT", "https://www.kimi.com/blog", "Kimi 官方 Blog 目录", "已检查", "窗内无可确认条目"),
    ("SRC-TENCENT-HUNYUAN", "https://hunyuan.tencent.com/research", "Hunyuan 官方 Research 目录", "受阻", "官方目录内部错误；浏览器替代入口在当前环境不可用，不能据此证明无遗漏"),
    ("SRC-ZAI", "https://z.ai/research", "Z.ai 官方 Research 目录", "已检查", "相邻可确认条目为 2026-05-20，窗内无条目"),
    ("SRC-BYTEDANCE-SEED", "https://seed.bytedance.com/en/research", "ByteDance Seed 官方 Research 目录", "已检查", "窗内无可确认条目"),
    ("SRC-BAIDU-ERNIE", "https://yiyan.baidu.com/blog", "ERNIE 官方技术博客/发布入口", "已检查", "窗内无可确认条目"),
    ("SRC-XIAOMI-MIMO", "https://www.mi.com/global/event/mimo/", "MiMo 官方 Paper / Blog 入口", "已检查", "相邻条目跳过本窗"),
    ("SRC-MINIMAX", "https://www.minimaxi.com/news", "MiniMax 官方 Research / Blog", "已检查", "相邻技术条目为 05-26/27，窗内无条目"),
    ("SRC-ARXIV", "https://info.arxiv.org/help/availability.html", "官方 2026-05-21 20:00 EDT announcement batch；月内 ID 2605.21490–2605.22823，covered-category subset 667", "已检查", "无；DataCite 仅作 identity 佐证，不充当 cutoff 时刻"),
]


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def first_sentence(text: str) -> str:
    clean = re.sub(r"\s+", " ", html.unescape(text or "")).strip()
    parts = re.split(r"(?<=[.!?])\s+", clean)
    return (parts[0] if parts else clean)[:520]


def mechanism_sentence(text: str) -> str:
    clean = re.sub(r"\s+", " ", html.unescape(text or "")).strip()
    parts = re.split(r"(?<=[.!?])\s+", clean)
    for sentence in parts:
        if re.search(r"\b(propose|present|introduce|develop|show|identify|formalize|demonstrate|find|reveal|study|investigate)\b", sentence, re.I):
            return sentence[:900]
    return first_sentence(clean)


def closure_family(row: dict) -> tuple[str, str]:
    title = html.unescape(row["title"])
    abstract = html.unescape(row.get("abstract", ""))
    text = f"{title} {abstract}".lower()
    cats = set(row.get("categories", []))
    if re.search(r"survey|taxonomy|systematic review|position paper|perspective", title, re.I):
        family = "survey_or_taxonomy_context"
        boundary = "材料提供术语/版图整理，但没有新增可执行机制、接口或可证伪的长期系统命题。"
    elif re.search(r"medical|clinical|molecule|protein|agriculture|finance|traffic|weather|remote sensing|recommend", text):
        family = "vertical_domain_result"
        boundary = "贡献与证据绑定垂直任务，title+full abstract 未给出可迁移到通用 AI System 的机制或 owner contract。"
    elif re.search(r"benchmark|dataset|corpus|leaderboard", title, re.I):
        family = "asset_without_new_evaluation_contract"
        boundary = "新增的是任务资产/榜单；full abstract 没有改变通用 EvalSpec、release authority 或 failure/fallback。"
    elif cats and all(c.startswith(("math.", "physics.", "econ.", "q-bio.", "q-fin.")) for c in cats):
        family = "outside_registered_ai_system_contribution"
        boundary = "身份虽在公告批次内，但 title+full abstract 不形成当前 ROADMAP 的 AI System 长期贡献。"
    elif re.search(r"classification|segmentation|forecasting|prediction|accuracy|detection", text):
        family = "local_model_or_task_quality_delta"
        boundary = "结果停留在局部模型/任务质量；未改变可复用的训练、推理、平台或 Agent 机制与验收边界。"
    else:
        family = "no_durable_ai_system_delta"
        boundary = "title+full abstract 未形成新的长期机制、owner 边界、failure/fallback 或 evaluation/release contract。"
    reason = f"全量 title+full abstract 复核关闭 `{title}`：摘要首个可定位主张为“{first_sentence(abstract)}”。{boundary} 若 exact-v1 后续 revision 新增跨 workload 机制或与当前 Books 命题冲突，只定点重开该 family。"
    return family, reason


def score(total: int) -> dict:
    if total == 9:
        vals = (3, 3, 3)
    elif total == 8:
        vals = (3, 2, 3)
    else:
        vals = (3, 2, 2)
    return {"design_delta": vals[0], "system_reach": vals[1], "durability": vals[2], "total": sum(vals)}


roadmap = (ROOT / "ROADMAP.md").read_text()
node_paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}
receipt = json.loads(OWNER_RECEIPT.read_text())
canonical = json.loads(CANONICAL.read_text())
source_rows = {row["arxiv_id"]: row for row in receipt["identities"]}
old_candidates = {row["arxiv_id"]: row for row in canonical["candidates"]}
assert len(source_rows) == 667
assert len(old_candidates) == 70
assert len(RESTORED_IDS) == len(set(RESTORED_IDS)) == 93
assert not set(old_candidates) & set(RESTORED_IDS)


old_evidence: dict[str, dict] = {}
for path in [
    HERE / "exact-v1-review-packet.json",
    ROOT / "papers/2026/05/_sources/daily-20260516/exact-v1-review-packet.json",
    ROOT / "papers/2026/05/_sources/daily-20260521/exact-v1-review-packet.json",
]:
    if path.exists():
        for item in json.loads(path.read_text()):
            old_evidence[item["arxiv_id"]] = item
assert set(old_candidates) <= set(old_evidence)


retained_ids = set(old_candidates) | set(RESTORED_IDS)
DEEP_COMPLETE_COUNT = len(old_candidates) + len(INTEGRATES) + len(DEEP_REVIEWS)
STANDARD_COMPLETE_COUNT = len(STANDARD_REVIEWS)
PENDING_COUNT = len(retained_ids) - DEEP_COMPLETE_COUNT - STANDARD_COMPLETE_COUNT
INTEGRATE_COUNT = len(INTEGRATES) + len(NEW_INTEGRATES)
NO_CHANGE_COUNT = len(old_candidates) + sum(
    1 for review in DEEP_REVIEWS.values() if review["decision"].startswith("No Change")
)
ledger_rows = []
closure_counts: dict[str, int] = {}
for source in receipt["identities"]:
    row = dict(source)
    aid = row["arxiv_id"]
    if aid == "2605.22714":
        row["abstract"] = AMEL_V1_ABSTRACT
        row["abstract_version_note"] = "Selected exact-v1 abstract replaces the current-metadata abstract from the owner receipt, whose later-version statistics are not admissible for arXiv:2605.22714v1."
    row["owner_event_evidence"] = "official arXiv 2026-05-22 announcement batch at 2026-05-22T08:00:00+08:00; DataCite fields are identity corroboration only"
    if aid in retained_ids:
        if aid in old_candidates:
            prior = old_candidates[aid]
            owner = prior["stable_node_id"]
            score_values = {
                "design_delta": int(prior["design_delta"]),
                "system_reach": int(prior["system_reach"]),
                "durability": int(prior["durability"]),
                "total": int(prior["total"]),
            }
            route = "replayable exact-v1 evidence from the prior owner report/packet; identity, version and claim unchanged"
            review = "deep_complete_author_recertified"
            access = "accessible"
            reason = f"replayed prior title+full-abstract admission and exact-v1 review without identity/version/claim drift: {mechanism_sentence(row.get('abstract', ''))}"
        elif aid in INTEGRATES:
            owner = OWNERS[aid]
            score_values = score(8)
            route = "current official exact-v1 HTML review with concrete v1 section locators"
            review = "deep_complete_author_side"
            access = "accessible"
            reason = INTEGRATES[aid]["proposed_delta"]
        elif aid in DEEP_REVIEWS:
            if aid in FALSE_NEGATIVE_REPAIRS:
                repair = FALSE_NEGATIVE_REPAIRS[aid]
                owner = repair["owner"]
                d, r, u = repair["score"]
                score_values = {"design_delta": d, "system_reach": r, "durability": u, "total": d + r + u}
            else:
                owner = OWNERS[aid]
                score_values = score(8 if aid in {"2605.21558", "2605.21865", "2605.21958", "2605.22237", "2605.22428", "2605.22791"} else 7)
            route = "current official exact-v1 HTML/PDF deep review with concrete method/evaluation/non-proof locators"
            review = "deep_complete_repair_author"
            access = "accessible"
            reason = DEEP_REVIEWS[aid]["adopted"]
        elif aid in FALSE_NEGATIVE_REPAIRS:
            repair = FALSE_NEGATIVE_REPAIRS[aid]
            owner = repair["owner"]
            d, r, u = repair["score"]
            score_values = {"design_delta": d, "system_reach": r, "durability": u, "total": d + r + u}
            if aid in STANDARD_REVIEWS:
                route = "current official exact-v1 HTML standard source review with concrete method/evaluation/non-proof locators"
                review = "standard_complete_repair_author"
            else:
                route = "official exact-v1 HTML/PDF accessible; deep review pending after title+full-abstract restoration"
                review = "deep_review_pending_after_restoration"
            access = "accessible"
            reason = repair["reason"]
        else:
            owner = OWNERS[aid]
            total = 8 if aid in INTEGRATES or aid in {"2605.21558", "2605.21865", "2605.21958", "2605.22237", "2605.22428", "2605.22791"} else 7
            score_values = score(total)
            route = "official exact-v1 HTML/PDF accessible; prior generic locator rejected and deep review remains pending"
            review = "deep_review_pending_after_locator_audit"
            access = "accessible"
            reason = (
                "Title+full abstract still support candidate admission, but the prior record supplied no concrete "
                "method/evaluation/non-proof locator; no positive adopted proposition or Books conclusion is retained."
            )
        disposition = (
            "Integrate — root applied, fresh post-write semantic pass" if aid in INTEGRATES or aid in ROOT_APPLIED_DEEP_INTEGRATES else
            (DEEP_REVIEWS[aid]["decision"] if aid in DEEP_REVIEWS else
            ("No Change — Existing Coverage" if aid in old_candidates else
             ("Report Only — standard source review" if aid in STANDARD_REVIEWS else "Deferred — exact-v1 review pending")))
        )
        row.update(
            v3_screening_status="retained",
            screening_status="retained",
            screening_reason=reason,
            review_status=review,
            access_status=access,
            stable_node_id=owner,
            owner_path=node_paths[owner],
            score_v3=score_values,
            evidence_route=route,
            books_disposition=disposition,
        )
    else:
        if aid in REMOVED_FALSE_POSITIVES:
            family, reason = REMOVED_FALSE_POSITIVES[aid]
        else:
            family, reason = closure_family(row)
        closure_counts[family] = closure_counts.get(family, 0) + 1
        row.update(
            v3_screening_status="pre_denominator_closure",
            screening_status="pre_denominator_closure",
            screening_reason=reason,
            closure_family=family,
            review_status="identity_date_contribution_closed",
            access_status="metadata_and_full_abstract_reviewed",
            books_disposition="Rejected — Below Candidate Denominator",
        )
    ledger_rows.append(row)


ledger = {
    "schema": "daily-screening-ledger-v3-author-recertification",
    "report_date": REPORT_DATE,
    "window": WINDOW,
    "owner_batch": {
        "announcement_eastern": "2026-05-21T20:00:00-04:00",
        "announcement_asia_shanghai": "2026-05-22T08:00:00+08:00",
        "first_id": "2605.21490",
        "last_id": "2605.22823",
        "all_category_count": 1334,
        "covered_category_identity_count": 667,
        "proof": "official schedule plus announcement-time month-sequence boundaries; current OAI and DataCite are corroboration only",
    },
    "raw_identity_count": 667,
    "retained_count": 163,
    "pre_denominator_closure_count": 504,
    "withdrawn_count": 0,
    "evidence_complete_count": DEEP_COMPLETE_COUNT + STANDARD_COMPLETE_COUNT,
    "evidence_deep_complete_count": DEEP_COMPLETE_COUNT,
    "evidence_standard_complete_count": STANDARD_COMPLETE_COUNT,
    "evidence_review_pending_count": PENDING_COUNT,
    "evidence_blocked_count": 0,
    "books_integrate_count": INTEGRATE_COUNT,
    "books_no_change_count": NO_CHANGE_COUNT,
    "books_report_only_count": 8,
    "books_deferred_count": PENDING_COUNT,
    "closure_family_counts": dict(sorted(closure_counts.items())),
    "identities": ledger_rows,
}
assert 667 == 163 + 504 + 0
assert 163 == DEEP_COMPLETE_COUNT + STANDARD_COMPLETE_COUNT + PENDING_COUNT
assert 163 == INTEGRATE_COUNT + NO_CHANGE_COUNT + 8 + PENDING_COUNT
dump(HERE / "screening-ledger-v3.json", ledger)


owner_evidence = {
    "schema": "official-arxiv-owner-batch-evidence-v3",
    "report_date": REPORT_DATE,
    "strict_window": WINDOW,
    "official_policy": {
        "availability_url": "https://info.arxiv.org/help/availability.html",
        "identifier_url": "https://info.arxiv.org/help/arxiv_identifier.html",
        "statement": "Final arXiv identifiers are assigned in the scheduled announcement process; routine announcements are Sunday through Thursday at 20:00 US Eastern.",
    },
    "time_conversion": {
        "announcement_eastern": "2026-05-21T20:00:00-04:00",
        "announcement_utc": "2026-05-22T00:00:00Z",
        "announcement_asia_shanghai": "2026-05-22T08:00:00+08:00",
        "strict_cutoff_asia_shanghai": "2026-05-22T09:00:00+08:00",
        "inside_window": True,
    },
    "batch_interval": {
        "preceding_id": "2605.21489",
        "first_id": "2605.21490",
        "last_id": "2605.22823",
        "following_id": "2605.22824",
        "inclusive_all_category_count": 1334,
        "covered_category_subset_count": 667,
        "derivation": "official announcement-time month-local sequence interval; 21489 belongs to the preceding owner batch and 22824 to the following batch",
    },
    "official_oai_support": {
        "same_day_current_datestamp_count": 513,
        "later_revision_datestamp_count": 154,
        "saved_lists": [
            "papers/2026/05/_sources/arxiv-owner-replay-20260903/oai-list-identifiers/2026-05-22-cs.xml",
            "papers/2026/05/_sources/arxiv-owner-replay-20260903/oai-list-identifiers/2026-05-22-eess.xml",
            "papers/2026/05/_sources/arxiv-owner-replay-20260903/oai-list-identifiers/2026-05-22-stat.xml",
        ],
        "revision_rule": "A later current OAI datestamp is revision metadata and does not move an identifier out of its announcement-time sequence interval.",
    },
    "ledger_membership_check": {"identity_count": 667, "min_id": "2605.21490", "max_id": "2605.22823", "outside_interval_count": 0},
    "conclusion": "All 667 covered-category identities belong to the official Thursday 20:00 Eastern announcement batch, public at 08:00 Asia/Shanghai before the strict 09:00 cutoff.",
    "datacite_role": "Identity/DOI corroboration only; created/updated timestamps are not publication or cutoff timestamps.",
}
dump(HERE / "official-owner-batch-evidence-v3.json", owner_evidence)


evidence = []
comparisons = []
for aid in sorted(retained_ids, key=lambda x: int(x.split(".")[1])):
    row = next(r for r in ledger_rows if r["arxiv_id"] == aid)
    owner = row["stable_node_id"]
    owner_path = node_paths[owner]
    if aid in old_candidates:
        item = dict(old_evidence[aid])
        item.update(
            evidence_route="reused exact-v1 packet after identity/version/claim replay",
            author_recertification_status="complete",
            replay_source=old_candidates[aid]["legacy_report_ref"],
        )
    elif aid in STANDARD_REVIEWS:
        standard = STANDARD_REVIEWS[aid]
        item = {
            "source_family_id": row["source_family_id"], "arxiv_id": aid,
            "primary_evidence_version": f"arXiv:{aid}v1",
            "retrieval_route": "official arXiv exact-v1 HTML standard source review",
            "retrieved_at": CHECKED_AT, "review_status": "standard_complete_repair_author", "access_status": "accessible",
            "problem": first_sentence(row.get("abstract", "")),
            "mechanism": mechanism_sentence(row.get("abstract", "")),
            "adopted_proposition": standard["adopted"],
            "method_locator": standard["method"],
            "evaluation_locator": standard["evaluation"],
            "limitations_locator": standard["nonproof"],
            "claim_boundary": standard["boundary"],
            "artifact_locator": f"https://arxiv.org/html/{aid}v1",
        }
    elif aid in DEEP_REVIEWS:
        deep = DEEP_REVIEWS[aid]
        item = {
            "source_family_id": row["source_family_id"], "arxiv_id": aid,
            "primary_evidence_version": f"arXiv:{aid}v1",
            "retrieval_route": "official arXiv exact-v1 HTML/PDF deep source review",
            "retrieved_at": CHECKED_AT, "review_status": "deep_complete_repair_author", "access_status": "accessible",
            "problem": first_sentence(row.get("abstract", "")),
            "mechanism": mechanism_sentence(row.get("abstract", "")),
            "adopted_proposition": deep["adopted"],
            "method_locator": deep["method"],
            "evaluation_locator": deep["evaluation"],
            "limitations_locator": deep["nonproof"],
            "claim_boundary": deep["boundary"],
            "tradeoff": deep["tradeoff"],
            "failure_fallback": deep["fallback"],
            "artifact_locator": (f"https://arxiv.org/pdf/{aid}v1" if aid == "2605.22765" else f"https://arxiv.org/html/{aid}v1"),
        }
    elif aid not in INTEGRATES:
        item = {
            "source_family_id": row["source_family_id"], "arxiv_id": aid,
            "primary_evidence_version": f"arXiv:{aid}v1", "retrieval_route": "official arXiv exact-v1 HTML/PDF access probe",
            "retrieved_at": CHECKED_AT, "review_status": "deep_review_pending", "access_status": "accessible",
            "method_locator": None, "evaluation_locator": None, "limitations_locator": None,
            "adopted_proposition": None,
            "claim_boundary": "Official exact-v1 is accessible, but title and full abstract currently support denominator admission only; no positive Evidence or Books claim is accepted until the required deep review records concrete method, evaluation, and non-proof locations.",
            "next_review": f"Complete deep review of official arXiv:{aid}v1 and record adopted proposition, concrete locators, trade-off, failure/fallback, and Books comparison.",
            "artifact_locator": (f"https://arxiv.org/pdf/{aid}v1" if aid in {"2605.21545", "2605.22765"} else f"https://arxiv.org/html/{aid}v1"),
        }
    else:
        item = {
            "source_family_id": row["source_family_id"], "arxiv_id": aid,
            "primary_evidence_version": f"arXiv:{aid}v1", "retrieval_route": "official arXiv exact-v1 HTML with concrete section review",
            "retrieved_at": CHECKED_AT, "review_status": "deep_complete_author_side", "access_status": "accessible",
            "problem": first_sentence(row.get("abstract", "")), "mechanism": mechanism_sentence(row.get("abstract", "")),
            "adopted_proposition": INTEGRATES[aid]["proposed_delta"],
            "claim_boundary": "Only the exact-v1 disclosed mechanism, workloads, models, evaluators and results are supported; absent deployment and generality fields remain Not Disclosed.",
            "artifact_locator": f"https://arxiv.org/html/{aid}v1",
        }
        item["method_locator"] = INTEGRATES[aid]["evidence_boundary"].split("; ")[0]
        item["evaluation_locator"] = INTEGRATES[aid]["evidence_boundary"]
        item["limitations_locator"] = INTEGRATES[aid]["evidence_boundary"].split("; ")[-1]
        if aid == "2605.22714":
            item["problem"] = AMEL_V1_PROBLEM
            item["mechanism"] = AMEL_V1_MECHANISM
    evidence.append(item)

    decision = row["books_disposition"]
    if aid in INTEGRATES:
        existing = f"`{INTEGRATES[aid]['anchor']}` 已有相邻原则，但未表达 proposed_delta 中的特定失效条件。"
        delta = INTEGRATES[aid]["proposed_delta"]
    elif aid in DEEP_REVIEWS:
        existing = DEEP_REVIEWS[aid]["existing"]
        delta = DEEP_REVIEWS[aid]["adopted"]
    elif aid in old_candidates:
        existing = EXISTING_PROPOSITIONS[owner]
        delta = item.get("mechanism") or mechanism_sentence(row.get("abstract", ""))
    elif aid in STANDARD_REVIEWS:
        existing = "Standard review (score 5–6) does not require a Books decision; no current-body coverage claim is made."
        delta = STANDARD_REVIEWS[aid]["adopted"]
    else:
        existing = "Not compared while the accessible exact-v1 body remains Review Pending; no current-body coverage claim is made."
        delta = "Withheld: title+full abstract preserve candidate admission, but no positive adopted proposition is accepted before the accessible exact-v1 body completes deep review."
    comparison = {
        "arxiv_id": aid, "source_family_id": row["source_family_id"], "title": html.unescape(row["title"]),
        "owner_node": owner, "owner_path": owner_path,
        "existing_proposition": existing, "new_evidence_delta": delta, "decision": decision,
        "comparison_basis": "current owner main-body proposition and nearest ownership boundary; Review notes and title/marker matches do not count as semantic coverage",
        "evidence_route": row["evidence_route"],
    }
    if aid in INTEGRATES:
        comparison["postwrite_status"] = "fresh_non_author_postwrite_semantic_pass_20260915"
        comparison["postwrite_marker"] = f"semantic-body-binding:SF-2026-ARXIV-{aid.replace('.', '-')}"
    elif aid in ROOT_APPLIED_DEEP_INTEGRATES:
        comparison["postwrite_status"] = "fresh_non_author_postwrite_semantic_pass_20260915"
        comparison["postwrite_marker"] = f"semantic-body-binding:SF-2026-ARXIV-{aid.replace('.', '-')}"
    elif aid in ACTIVE_NEW_INTEGRATES:
        comparison["writeback_status"] = "root_serialized_queue_pending"
        comparison["root_queue_anchor"] = DEEP_REVIEWS[aid]["anchor"]
    comparisons.append(comparison)

dump(HERE / "exact-v1-evidence-v3.json", evidence)
dump(HERE / "books-current-content-comparison-v3.json", comparisons)


queue_items = []
for aid, delta in INTEGRATES.items():
    row = source_rows[aid]
    owner = OWNERS[aid]
    queue_items.append({
        "report_date": REPORT_DATE, "arxiv_id": aid, "source_family_id": row["source_family_id"],
        "title": html.unescape(row["title"]), "primary": f"https://arxiv.org/html/{aid}v1",
        "stable_node_id": owner, "target_path": node_paths[owner], "anchor": delta["anchor"],
        "proposed_delta": delta["proposed_delta"], "evidence_boundary": delta["evidence_boundary"],
        "tradeoff": delta["tradeoff"], "failure_fallback": delta["failure_fallback"],
        "writer": "root serialized Books owner", "author_must_not_write_books": True,
        "postwrite_status": (
            "fresh_non_author_postwrite_semantic_pass_20260916"
            if aid in ROOT_APPLIED_DEEP_BATCH_SPECTRAL_1
            else "fresh_non_author_postwrite_semantic_pass_20260915"
        ),
        "postwrite_marker": f"semantic-body-binding:SF-2026-ARXIV-{aid.replace('.', '-')}",
        "postwrite_binding": "paired :start/:end semantic-body-binding markers verified once each in the target chapter",
        "writeback_receipt": "ROOT_BOOKS_WRITEBACK_3_EVALUATION_DELTAS_20260915.md",
    })
for aid in sorted(ROOT_APPLIED_DEEP_INTEGRATES, key=lambda x: int(x.split(".")[1])):
    deep = DEEP_REVIEWS[aid]
    row = source_rows[aid]
    owner = OWNERS[aid]
    queue_items.append({
        "report_date": REPORT_DATE, "arxiv_id": aid, "source_family_id": row["source_family_id"],
        "title": html.unescape(row["title"]),
        "primary": (f"https://arxiv.org/pdf/{aid}v1" if aid in {"2605.21545", "2605.22765"} else f"https://arxiv.org/html/{aid}v1"),
        "stable_node_id": owner, "target_path": node_paths[owner], "anchor": deep["anchor"],
        "proposed_delta": deep["proposed_delta"], "evidence_boundary": deep["boundary"],
        "tradeoff": deep["tradeoff"], "failure_fallback": deep["fallback"],
        "writer": "root serialized Books owner", "author_must_not_write_books": True,
        "postwrite_status": "fresh_non_author_postwrite_semantic_pass_20260915",
        "postwrite_marker": f"semantic-body-binding:SF-2026-ARXIV-{aid.replace('.', '-')}",
        "postwrite_binding": "paired :start/:end semantic-body-binding markers verified once each before the target chapter's main Review notes; surrounding body preserves old baseline, changed constraint, ownership, evidence boundary, trade-off and fallback",
        "writeback_receipt": (
            "ROOT_BOOKS_WRITEBACK_5_RESTORED_DEEP_ITEMS_20260915.md" if aid in ROOT_APPLIED_DEEP_BATCH_5 else
            "ROOT_BOOKS_WRITEBACK_3_ACTIVE_DEEP_ITEMS_20260915.md" if aid in ROOT_APPLIED_DEEP_BATCH_3 else
            "ROOT_BOOKS_WRITEBACK_7_SECURITY_ITEMS_20260915.md" if aid in ROOT_APPLIED_DEEP_BATCH_SECURITY else
            "ROOT_BOOKS_WRITEBACK_4_AGENT_ITEMS_20260915.md" if aid in ROOT_APPLIED_DEEP_BATCH_AGENT else
            "Books body observed directly in root-owned Ch27/Ch31 files" if aid in ROOT_APPLIED_DEEP_BATCH_DATA_RLHF else
            "Books body observed directly in root-owned Ch29 file" if aid in ROOT_APPLIED_DEEP_BATCH_SFT_3 else
            "Books body observed directly in root-owned Ch17/Ch34 files" if aid in ROOT_APPLIED_DEEP_BATCH_ARCH_DPO_2 else
            "Books body observed directly in root-owned Ch23 file" if aid in ROOT_APPLIED_DEEP_BATCH_RELATION_1 else
            "Books body observed directly in root-owned Ch14 file" if aid in ROOT_APPLIED_DEEP_BATCH_ATTENTION_1 else
            "Books body observed directly in root-owned Ch24/Ch5 files" if aid in ROOT_APPLIED_DEEP_BATCH_SENSOR_ATTRIBUTION_2 else
            "Books body observed directly in root-owned Ch23 file" if aid in ROOT_APPLIED_DEEP_BATCH_SPECTRAL_1 else
            "ROOT_BOOKS_WRITEBACK_REFUSALBENCH_20260915.md"
        ),
        "postwrite_review": (
            "FRESH_POSTWRITE_REVIEW_5_RESTORED_DEEP_ITEMS_20260915.md" if aid in ROOT_APPLIED_DEEP_BATCH_5 else
            "FRESH_POSTWRITE_REVIEW_3_ACTIVE_DEEP_ITEMS_20260915.md" if aid in ROOT_APPLIED_DEEP_BATCH_3 else
            "FRESH_POSTWRITE_REVIEW_7_SECURITY_ITEMS_20260915.md" if aid in ROOT_APPLIED_DEEP_BATCH_SECURITY else
            "FRESH_POSTWRITE_REVIEW_4_AGENT_ITEMS_20260915.md" if aid in ROOT_APPLIED_DEEP_BATCH_AGENT else
            "FRESH_POSTWRITE_REVIEW_4_DATA_RLHF_ITEMS_20260915.md" if aid in ROOT_APPLIED_DEEP_BATCH_DATA_RLHF else
            "FRESH_POSTWRITE_REVIEW_3_SFT_ITEMS_20260916.md" if aid in ROOT_APPLIED_DEEP_BATCH_SFT_3 else
            "FRESH_POSTWRITE_REVIEW_2_ARCH_DPO_ITEMS_20260916.md" if aid in ROOT_APPLIED_DEEP_BATCH_ARCH_DPO_2 else
            "FRESH_POSTWRITE_REVIEW_21988_RELATION_20260916.md" if aid in ROOT_APPLIED_DEEP_BATCH_RELATION_1 else
            "FRESH_POSTWRITE_REVIEW_22476_ATTENTION_20260916.md" if aid in ROOT_APPLIED_DEEP_BATCH_ATTENTION_1 else
            "FRESH_POSTWRITE_REVIEW_22050_22417_20260916.md" if aid in ROOT_APPLIED_DEEP_BATCH_SENSOR_ATTRIBUTION_2 else
            "FRESH_POSTWRITE_REVIEW_22691_SPECTRAL_20260916.md" if aid in ROOT_APPLIED_DEEP_BATCH_SPECTRAL_1 else
            "FRESH_POSTWRITE_REVIEW_REFUSALBENCH_20260915.md"
        ),
    })
active_queue_items = []
for aid, deep in ACTIVE_NEW_INTEGRATES.items():
    row = source_rows[aid]
    owner = OWNERS[aid]
    active_queue_items.append({
        "report_date": REPORT_DATE, "arxiv_id": aid, "source_family_id": row["source_family_id"],
        "title": html.unescape(row["title"]),
        "primary": (f"https://arxiv.org/pdf/{aid}v1" if aid == "2605.22765" else f"https://arxiv.org/html/{aid}v1"),
        "stable_node_id": owner, "target_path": node_paths[owner], "anchor": deep["anchor"],
        "old_baseline_and_constraint_change": deep["proposed_delta"],
        "adopted_proposition": deep["adopted"],
        "method_locator": deep["method"], "evaluation_locator": deep["evaluation"],
        "nonproof_locator": deep["nonproof"], "evidence_boundary": deep["boundary"],
        "tradeoff": deep["tradeoff"], "failure_fallback": deep["fallback"],
        "state_control_ownership": deep["proposed_delta"],
        "writer": "root serialized Books owner", "author_must_not_write_books": True,
        "status": "pending_root_writeback_then_fresh_postwrite_semantic_review",
        "required_marker": f"semantic-body-binding:SF-2026-ARXIV-{aid.replace('.', '-')}:start/end",
    })
queue = {
    "schema": "books-writeback-queue-v3-author",
    "report_date": REPORT_DATE,
    "status": (
        "root_writeback_pending_for_active_deep-review_integrates; completed bindings passed fresh postwrite review; overall_report_repair_pending_new_fresh_review"
        if active_queue_items else
        "root_writeback_queue_clear; all bindings passed fresh postwrite review; overall_report_repair_complete_pending_new_fresh_review"
    ),
    "queue_count": len(active_queue_items), "item_count": len(active_queue_items), "items": active_queue_items,
    "root_applied_fresh_semantic_pass_count": len(queue_items),
    "root_applied_fresh_semantic_pass": queue_items,
    "books_gate": f"{len(queue_items)} root bindings passed fresh post-write semantic review. {len(active_queue_items)} newly discovered deep-review deltas require root writeback and a fresh post-write semantic review; the repaired date-local corpus remains Ongoing and then requires a new fresh non-author final Gate.",
}
dump(HERE / "BOOKS_WRITEBACK_QUEUE_V3.json", queue)


postwrite_review = f"""# Fresh post-write semantic review — five restored deep items

- Reviewer: fresh non-author for these five root Books edits; also the date-local corpus repair author
- Reviewed at: {CHECKED_AT}
- Root receipt: `ROOT_BOOKS_WRITEBACK_5_RESTORED_DEEP_ITEMS_20260915.md`
- Result: PASS for these five Books bindings only; the daily report remains Ongoing and still requires another fresh final reviewer

## Scope and checks

All five source markers are unique paired `:start`/`:end` bindings and occur before the target chapter's main `## Review notes`. The review read each bounded body and its adjacent paragraphs; marker presence alone was not accepted.

| Source | Owner/body result | Semantic result |
| --- | --- | --- |
| `2605.22223` | `MODEL-DECODER-ONLY` / Ch18 | PASS: retains longer-context/more-sampling baseline, adds architecture-conditional reachable-support constraint, assigns prompt/decoder/Evaluation ownership, limits the theorem to bounded-embedding/decision-cell assumptions, and falls back to direct copying/cramming/length-slice tests. |
| `2605.22596` | `MULTIMODAL-EMBODIED-VLA` / Ch26 | PASS: retains monolithic/joint policy baseline, conditions factor composition on approximate independence, separates registry/score/ODE/controller authority, names Lipschitz/identifiability/contraction limits, and falls back to joint policies, explicit planning, shorter horizon or the verified safety controller. |
| `2605.22705` | `MODEL-TOKENIZER` / Ch11 | PASS: keeps BPE/Unigram as the compatibility baseline, binds split tree, traversal and vocabulary identity, limits evidence to the disclosed English/1.5B setting, records solve/runtime/checkpoint cost, and falls back to the frozen tokenizer/checkpoint. |
| `2605.22765` | `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 | PASS: distinguishes marginal, network target, loss conversion and sampler, separates theoretical joint-law equivalence from learned factorized approximation, records auxiliary/corrector cost, and falls back to the frozen denoiser/sampler pair and full frontier comparison. |
| `2605.22821` | `MODEL-TOKENIZER` / Ch11 | PASS: keeps local/iterative tokenizers as baseline, assigns the LP only objective-specific lower-bound authority, leaves release to behavioral gates, records rounding/sample-sensitivity cost, and falls back to BPE/Unigram with the bound used only as diagnosis. |

## Gate boundary

This artifact closes only the write-after semantic Gate for these five root-owned edits. It does not sign the repaired 2026-05-22 daily corpus Complete: {PENDING_COUNT} accessible exact-v1 deep reviews and {len(ACTIVE_NEW_INTEGRATES)} current root queue items remain, and a different fresh non-author must execute the final daily Gate after repairs freeze.
"""
(HERE / "FRESH_POSTWRITE_REVIEW_5_RESTORED_DEEP_ITEMS_20260915.md").write_text(postwrite_review)

postwrite_review_3 = f"""# Fresh post-write semantic review — three active deep items

- Reviewer: fresh non-author for these three root Books edits; also the date-local corpus repair author
- Reviewed at: {CHECKED_AT}
- Root receipt: `ROOT_BOOKS_WRITEBACK_3_ACTIVE_DEEP_ITEMS_20260915.md`
- Result: PASS for these three Books bindings only; the daily report remains Ongoing and still requires another fresh final reviewer

## Scope and checks

All three source markers are unique paired `:start`/`:end` bindings and occur before the target chapter's main `## Review notes`. The surrounding bodies were read in sequence.

| Source | Owner/body result | Semantic result |
| --- | --- | --- |
| `2605.21865` | `PLATFORM-GATEWAY` / Ch62 | PASS: preserves value/application watermarking as the old path, conditions key permutation on a member-order-insensitive client contract and end-to-end preservation, versions schema/order/key/serializer/receipt, separates gateway encoding from compatibility/integrity/authorization, and falls back to signed provenance, sidecar receipts or application-owned watermarking. |
| `2605.21958` | `AGENT-WORKFLOW` / Ch81 | PASS: separates causal diagnosis from patch prescription, freezes the comparison snapshot and assigns end-to-end promotion to the workflow owner, limits evidence to the disclosed single-turn four-module pipeline, records intervention/judge cost and co-adaptation risk, and falls back to no patch, interface retraining, serial redesign or human adjudication. |
| `2605.22237` | `INFER-TENSORRT-LLM` / Ch49 | PASS: retains interval-based ReLU approximation as baseline, distinguishes exact positive-margin calibration certification from RCH/soft surrogates, separates calibration/compiler/runtime/release authority, withholds unseen-input/confidentiality proof, records CKKS/coefficient cost, and falls back to higher-degree, hybrid MPC, retraining or rejection. |

## Gate boundary

This closes the write-after semantic Gate for the three root-owned edits. It does not sign the repaired daily corpus Complete: {PENDING_COUNT} accessible exact-v1 deep reviews remain, and a different fresh non-author must execute the final daily Gate after all date-local repair and Books work freezes.
"""
(HERE / "FRESH_POSTWRITE_REVIEW_3_ACTIVE_DEEP_ITEMS_20260915.md").write_text(postwrite_review_3)

postwrite_review_refusal = f"""# Fresh post-write semantic review — RefusalBench

- Reviewer: fresh non-author for the root RefusalBench Books edit; also the date-local corpus repair author
- Reviewed at: {CHECKED_AT}
- Root receipt: `ROOT_BOOKS_WRITEBACK_REFUSALBENCH_20260915.md`
- Result: PASS for this Books binding only; the daily report remains Ongoing and still requires another fresh final reviewer

## Scope and checks

The `SF-2026-ARXIV-2605-21545` marker is a unique paired `:start`/`:end` binding before Ch66's main `## Review notes`. The bounded body and adjacent `Response Rate` and verifier-aggregation paragraphs were read in sequence.

## Semantic result

PASS: the body preserves the cheap aggregate-refusal baseline, explains why blanket refusal, risk-insensitive low refusal and hedge-but-help behavior change the constraint, and assigns matched risk-tier triples, should-refuse controls, partial-compliance/uplift dimensions and access-path identity to EvalSpec rather than model weights. It explicitly limits the exact-v1 evidence to biology prompts, one prompt/temperature regime, finite repeats and its judge council; it records expert-label, repetition and content-coding costs; and it falls back to `Unknown`, deterministic policy outcomes and human review when risk labels, judge agreement, adversarial coverage or expert warrant are insufficient. Ch66 retains measurement ownership while policy/release authority remains external.

## Gate boundary

This closes only the write-after semantic Gate for the root-owned RefusalBench edit. It does not sign the repaired daily corpus Complete: {PENDING_COUNT} accessible exact-v1 deep reviews remain, and a different fresh non-author must execute the final daily Gate after all date-local repair and Books work freezes.
"""
(HERE / "FRESH_POSTWRITE_REVIEW_REFUSALBENCH_20260915.md").write_text(postwrite_review_refusal)

postwrite_review_security = f"""# Fresh post-write semantic review — seven Security items

- Reviewer: fresh non-author for these seven root Books edits; also the date-local corpus repair author
- Reviewed at: {CHECKED_AT}
- Root receipt: `ROOT_BOOKS_WRITEBACK_7_SECURITY_ITEMS_20260915.md`
- Result: PASS for these seven Books bindings only; the daily report remains Ongoing and still requires another fresh final reviewer

## Scope and checks

All seven source markers are unique paired `:start`/`:end` bindings and occur before Ch72's main `## Review notes`. Each bounded body and its adjacent mechanism paragraphs were read in sequence; marker presence alone was not accepted.

| Source | Owner/body result | Semantic result |
| --- | --- | --- |
| `2605.21609` | `PLATFORM-SECURITY` / Ch72 | PASS: keeps hard refusal as fallback, conditions the new branch on population-specific engagement risk, separates detector/rewriter proposals from external policy, validator and human release authority, bounds evidence to the disclosed synthetic/limited setting, names latency and harmful-normalization failures, and falls back to deterministic crisis policy or qualified human support. |
| `2605.21780` | `PLATFORM-SECURITY` / Ch72 | PASS: preserves training-only DP as a narrower contract, defines a joint training/test neighboring relation and mechanism-aligned profile composition, separates component evidence from release authority, limits the certificate to declared radii/margins and image-classification mechanisms, records repeated-training/utility cost, and falls back to separate claims, adaptive red-team or fail-closed release. |
| `2605.21938` | `PLATFORM-SECURITY` / Ch72 | PASS: distinguishes accountant upper bounds from empirical black-box lower bounds, freezes canary/statistic/order/critic/sample identities, withholds a two-sided or exact epsilon claim absent bounded-loss assumptions, records training and optimization cost, and falls back to observed-lower-bound/Unknown plus white-box conformance and a conservative accountant. |
| `2605.22005` | `PLATFORM-SECURITY` / Ch72 | PASS: retains ordinary behavioral/provenance release review, restricts `lm_head` SVD/VCS to a static triage sensor, denies it training-data, behavior, deletion or release authority, records weight/tokenizer and interpretability costs, and falls back to unchanged weights plus behavioral red-team when clusters are ambiguous or inconsistent. |
| `2605.22373` | `PLATFORM-SECURITY` / Ch72 | PASS: changes easy-example MIA into boundary/harm/input-structure and conversation/user-history-unit slices, assigns only sensor authority to the audit, withholds person identification and DP claims, records reference/margin/longitudinal-fixture costs, and falls back to canaries, provenance, formal DP and `Unknown`. |
| `2605.22481` | `PLATFORM-SECURITY` / Ch72 | PASS: retains sparse trigger probes as a low-risk baseline, adds independent train/test strength, poison-rate and direction sweeps, gives the evaluation owner only matrix-reporting authority, limits the theory to Gaussian/GLM conditions, records retraining cost, and falls back to explicit untested intervals, held-out neighborhoods and quarantine. |
| `2605.22737` | `PLATFORM-SECURITY` / Ch72 | PASS: replaces passive uniform-student evaluation with an adaptive-student operating frontier while leaving release authority with cross-identity gateway policy, withholds confidentiality proof, records value-estimation/proxy/teacher-utility costs, and falls back to standard sampling, global budgets, watermark/canary, access control and human investigation. |

## Gate boundary

This closes only the write-after semantic Gate for these seven root-owned edits. It does not sign the repaired daily corpus Complete: {PENDING_COUNT} accessible exact-v1 deep reviews remain, and a different fresh non-author must execute the final daily Gate after all date-local repair and Books work freezes.
"""
(HERE / "FRESH_POSTWRITE_REVIEW_7_SECURITY_ITEMS_20260915.md").write_text(postwrite_review_security)

postwrite_review_agent = f"""# Fresh post-write semantic review — four Agent items

- Reviewer: fresh non-author for these four root Books edits; also the date-local corpus repair author
- Reviewed at: {CHECKED_AT}
- Root receipt: `ROOT_BOOKS_WRITEBACK_4_AGENT_ITEMS_20260915.md`
- Result: PASS for these four Books bindings only; the daily report remains Ongoing and still requires another fresh final reviewer

## Scope and checks

All four source markers are unique paired `:start`/`:end` bindings and occur before their target chapter's main `## Review notes`. Each bounded body and its adjacent paragraphs was read in sequence. An initial Ch79 antecedent drift was reported to root and repaired before this PASS: the following paragraph now explicitly names the separate training-teacher/runtime-controller branch.

| Source | Owner/body result | Semantic result |
| --- | --- | --- |
| `2605.21994` | `AGENT-RAG` / Ch76 | PASS: retains traversal/citation as the baseline, separates exact additive semantic contribution from structural bridge necessity, leaves graph/corpus/entailment authority outside attribution, bounds evidence to STaRK-Prime and limited cases, records expressivity/performance/context cost, and falls back to a stronger conventional GNN plus explicit traversal and claim citation. |
| `2605.22142` | `AGENT-MEMORY` / Ch77 | PASS: preserves FIFO/recency rules as the stable baseline, adds variable-cardinality per-item transfer value under partial observability, keeps durable-write authority with provenance/conflict/capacity governance, limits evidence to capacity-128 RoomKG symbolic triples, records reward/value/matching failure, and falls back to raw episodes, heuristics, re-verification or capacity expansion. |
| `2605.22221` | `AGENT-PLANNING` / Ch79 | PASS after the bounded transition repair: separates canonical current-state policy input from durable full-trace evidence, adds same-state/different-history invariance, withholds state-aliasing and proactive-verification proof, records localization/training/position cost, and falls back to deterministic state reconstruction, explicit backtracking and an external verifier. The adjacent original paragraph now unambiguously resumes the training-teacher/runtime-controller branch. |
| `2605.22814` | `AGENT-MEMORY` / Ch77 | PASS: preserves current-observation/short-history exploration as the old path, separates persistent world-reference state from episodic policy context, leaves environmental truth/effect commit with observations and the controller, limits evidence to static indoor 3DGS and two generated OOD worlds, records reconstruction/localization/staleness cost, and falls back to direct observation, short egocentric context, validated maps or a safety controller. |

## Gate boundary

This closes only the write-after semantic Gate for these four root-owned edits. It does not sign the repaired daily corpus Complete: {PENDING_COUNT} accessible exact-v1 deep reviews remain, and a different fresh non-author must execute the final daily Gate after all date-local repair and Books work freezes.
"""
(HERE / "FRESH_POSTWRITE_REVIEW_4_AGENT_ITEMS_20260915.md").write_text(postwrite_review_agent)

postwrite_review_relation = f"""# Fresh post-write semantic review — paired temporal relation

- Reviewer: fresh non-author for this root Books edit; also the date-local corpus repair author
- Reviewed at: {CHECKED_AT}
- Root body: `books/part-03-multimodal-world-models/23-multimodal-representation.md`, `### Connector shortcut`
- Result: PASS for this Books binding only; the daily report remains Ongoing and still requires another fresh final reviewer

## Scope and checks

The `SF-2026-ARXIV-2605-21988` marker is a unique paired `:start`/`:end` binding before Ch23's main `## Review notes`. The review read the pre-marker baseline, the bounded paragraph, and the transition into the engineering decision framework rather than accepting marker presence alone.

## Semantic result

PASS: the body starts from single-item video QA and the existing connector-shortcut baseline, then distinguishes must-change dynamic questions from must-stay invariant questions under a declared flip/reversal relation. It freezes pair, transform revision, router and expected relation, uses strict pair accuracy to reject one-sided fixed-answer success, and separates transformation/router relation authority from original-label or independent-verifier correctness and optimizer update authority. It records doubled video rollout, lineage and normalization cost; explicitly withholds factual correctness, arbitrary-edit semantic preservation and long-horizon causal understanding; and falls back to verified original examples, explicit temporal labels, full-video evaluation and human-reviewed counterfactuals when transform validity, router agreement, pair correctness or general-video regression fails. The transition into the chapter's engineering decision framework remains coherent.

## Gate boundary

This closes only the write-after semantic Gate for the root-owned `2605.21988` edit. It does not sign the repaired daily corpus Complete: {PENDING_COUNT} accessible exact-v1 deep reviews and {len(ACTIVE_NEW_INTEGRATES)} current root queue items remain, and a different fresh non-author must execute the final daily Gate after all repairs freeze.
"""
(HERE / "FRESH_POSTWRITE_REVIEW_21988_RELATION_20260916.md").write_text(postwrite_review_relation)

postwrite_review_attention = f"""# Fresh post-write semantic review — exact-local/reduced-residual attention

- Reviewer: fresh non-author for this root Books edit; also the date-local corpus repair author
- Reviewed at: {CHECKED_AT}
- Root body: `books/part-02-model/14-self-attention.md`, immediately after the sparse-Q/K layout branch
- Result: PASS for this Books binding only; the daily report remains Ongoing and still requires another fresh final reviewer

## Scope and checks

The `SF-2026-ARXIV-2605-22476` marker is a unique paired `:start`/`:end` binding before Ch14's main `## Review notes`. The review read the dense/sparse-QK baseline, bounded body and transition into budget-conditioned Attention rather than accepting marker presence alone.

## Semantic result

PASS: the body preserves fixed-window/sparse-support deletion as the simpler old path, identifies the changed constraint as exact block-local relations plus light cross-block propagation, and states the operator-specific exact-local/reduced-residual mechanism. It assigns block partition, causal mask, pool/lift and reduced-system semantics to the operator owner while limiting runtime to that frozen decomposition; it explicitly withholds equivalence to generic softmax sparsity and arbitrary pretrained checkpoints. It records tiling, two branches, block-size, adaptation and head-capacity costs, names diffuse routing/residual error/properties-over-heads/measured-latency failures, and falls back to dense resolvent, dense Attention or a validated fixed-window/sparse kernel. Placement between the existing feature-sparse kernel discussion and compute-budget routing is coherent.

## Gate boundary

This closes only the write-after semantic Gate for root-owned `2605.22476`. It does not sign the repaired daily corpus Complete: {PENDING_COUNT} accessible exact-v1 deep reviews and {len(ACTIVE_NEW_INTEGRATES)} current root queue items remain, and a different fresh non-author must execute the final daily Gate after all repairs freeze.
"""
(HERE / "FRESH_POSTWRITE_REVIEW_22476_ATTENTION_20260916.md").write_text(postwrite_review_attention)

postwrite_review_sensor_attribution = f"""# Fresh post-write semantic review — trajectory-risk sensor and attribution reference

- Reviewer: fresh non-author for these two root Books edits; also the date-local corpus repair author
- Reviewed at: {CHECKED_AT}
- Root bodies: Ch24 `Conditional Guidance 把 Diffusion 并行策略变成逐 Step 状态`; Ch5 internal-analysis evidence ladder
- Result: PASS for both Books bindings only; the daily report remains Ongoing and still requires another fresh final reviewer

## Scope and checks

Both source markers are unique paired `:start`/`:end` bindings before the target chapter's main `## Review notes`. Each bounded body and its adjacent transition was read in sequence; marker presence alone was not accepted.

| Source | Owner/body result | Semantic result |
| --- | --- | --- |
| `2605.22050` | `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 | PASS: keeps post-generation copy detection/retry and fixed intervention as the simple baselines; changes the constraint to preserve and adapt the current denoising trajectory; assigns clean-reference regions to calibration, deviation strength to the sensor, bounded rescaling to the sampler controller, and final acceptance to independent copy/provenance/privacy gates. It states rare-normal false positives and unseen-dynamics false negatives, withholds record identity, safety and deletion proof, binds evidence to disclosed Stable Diffusion/sampler/calibration/SSCD settings, and falls back to detect-then-retry, validated static sampling, source checks or training-side filtering/unlearning. Placement before the existing dynamic-CFG branch is coherent. |
| `2605.22417` | `WORLDVIEW-REPRESENTATION` / Ch5 | PASS: starts from the implicit-reference attribution baseline, binds the claim to input reference, its induced output baseline, target, path/step and model revision, and leaves causal truth to perturbation/intervention/behavioral checks. It records baseline/path/matching cost, explicitly rejects all-zero as a universal no-information state, limits evidence to DETR/VGG, and falls back to reference-conditional reporting, multiple controls and causal/behavioral replication. Placement between the evidence ladder's internal-analysis step and cross-model basis discussion is coherent. |

## Gate boundary

This closes only the write-after semantic Gate for root-owned `2605.22050` and `2605.22417`. It does not sign the repaired daily corpus Complete: {PENDING_COUNT} accessible exact-v1 deep reviews and {len(ACTIVE_NEW_INTEGRATES)} current root queue items remain, and a different fresh non-author must execute the final daily Gate after all repairs freeze.
"""
(HERE / "FRESH_POSTWRITE_REVIEW_22050_22417_20260916.md").write_text(postwrite_review_sensor_attribution)

postwrite_review_spectral = f"""# Fresh post-write semantic review — latent spectral pruning

- Reviewer: fresh non-author for this root Books edit; also the date-local corpus repair author
- Reviewed at: {CHECKED_AT}
- Root body: `books/part-03-multimodal-world-models/23-multimodal-representation.md`, inside `Rate、distortion 与下游容量必须联合选择`
- Result: PASS for this Books binding only; the repaired daily corpus still requires another fresh final reviewer

## Scope and checks

The `SF-2026-ARXIV-2605-22691` marker is a globally unique paired `:start`/`:end` binding before Ch23's main `## Review notes`. The review read the bounded body and the surrounding rate–distortion paragraphs rather than accepting marker presence alone.

## Semantic result

PASS: the body preserves fixed latent count and treating posterior collapse as a training failure as the conservative old baseline, then restricts the changed branch to the linear Gaussian `beta`-VAE calibration. It states normalized information price `T = beta * sigma_dec^2 / V`, scale-invariant posterior signal fraction and PCA-like mode pruning without turning the scan into semantic-factor discovery. The representation owner freezes likelihood, decoder/data variance, `beta` schedule, model revision and mode matching; the scan only proposes utility-ranked active rank, while reconstruction/semantic/generation Gates retain adoption authority. The evidence boundary is explicitly limited to the WorldClim linear-Gaussian experiment and withholds any theorem for nonlinear decoders or latent semantics. Multiple operating points, spectrum matching, mode rotation/mixing, degeneracy and finite optimization are recorded as costs/failures; fixed latent budget, PCA/reconstruction controls, lower regularization, anti-collapse schedules and conventional VAE retraining are explicit fallbacks. Placement after the chapter's joint rate–distortion–capacity argument and before the next representation branch is coherent.

## Gate boundary

This closes only the write-after semantic Gate for root-owned `2605.22691`. It clears the serialized Books queue, but does not let the date-local repair author self-sign the daily report Complete; a different fresh non-author must perform the final daily Gate.
"""
(HERE / "FRESH_POSTWRITE_REVIEW_22691_SPECTRAL_20260916.md").write_text(postwrite_review_spectral)


coverage = {
    "schema": "daily-source-coverage-v3-author",
    "report_date": REPORT_DATE, "window": WINDOW, "checked_at": CHECKED_AT,
    "sources": [{"source": s, "url": u, "scope": scope, "result": result, "gap": gap} for s, u, scope, result, gap in SOURCES],
    "checked_count": sum(1 for *_, result, _ in SOURCES if result == "已检查"),
    "blocked_count": sum(1 for *_, result, _ in SOURCES if result == "受阻"),
}
dump(HERE / "source-coverage-v3.json", coverage)


pending_ids = sorted(
    (aid for aid in retained_ids if aid not in old_candidates and aid not in INTEGRATES and aid not in STANDARD_REVIEWS and aid not in DEEP_REVIEWS),
    key=lambda x: int(x.split(".")[1]),
)
assert len(pending_ids) == PENDING_COUNT
materials = {
    "schema": "daily-materials-request-v3",
    "report_date": REPORT_DATE,
    "items": [
        {"scope": "source", "id": "SRC-META-AI", "need": "non-empty official Publications directory or date-preserving official export for the strict window", "why": "empty response cannot prove daily coverage", "current_disposition": "coverage assertion withheld", "reopen": "only SRC-META-AI for this window"},
        {"scope": "source", "id": "SRC-TENCENT-HUNYUAN", "need": "readable official Research directory or date-preserving official feed/export", "why": "official page returned an internal error and browser fallback was unavailable", "current_disposition": "coverage assertion withheld", "reopen": "only SRC-TENCENT-HUNYUAN for this window"},
    ],
}
dump(HERE / "materials-request-v3.json", materials)


pending = {
    "schema": "daily-exact-v1-review-pending-v3",
    "report_date": REPORT_DATE,
    "access_probe": {
        "official_exact_v1_candidate_count": 90,
        "html_accessible_count": 88,
        "pdf_fallback_accessible_count": 2,
        "access_blocked_count": 0,
        "pdf_fallback_ids": ["2605.21545", "2605.22765"],
        "statement": "Every one of the 90 affected families was probed at official arXiv exact-v1 HTML and, where HTML returned no document, official arXiv exact-v1 PDF; all are accessible through at least one official route.",
    },
    "standard_complete_count": len(STANDARD_REVIEWS),
    "standard_complete_ids": sorted(STANDARD_REVIEWS, key=lambda x: int(x.split(".")[1])),
    "deep_repair_batch_complete_count": len(DEEP_REVIEWS),
    "deep_repair_batch_complete_ids": sorted(DEEP_REVIEWS, key=lambda x: int(x.split(".")[1])),
    "deep_review_pending_count": len(pending_ids),
    "deep_review_pending_ids": pending_ids,
    "score_stratification": {
        "score_5_count": 4,
        "score_6_count": 6,
        "score_7_count": 77,
        "score_8_count": 57,
        "score_9_count": 19,
        "score_5_6_standard_complete_count": 8,
        "score_5_6_override_deep_complete_count": 2,
        "score_5_6_override_deep_pending_count": 0,
        "score_7_9_deep_complete_count": DEEP_COMPLETE_COUNT - 2,
        "score_7_9_deep_pending_count": PENDING_COUNT,
        "override_deep_complete_ids": ["2605.21674", "2605.21834"],
    },
    "gate": (
        "Ongoing: accessible deep review pending; Review Pending is not Access Blocked."
        if pending_ids else
        "Author repair evidence complete: no exact-v1 Review Pending and no Access Blocked; final daily Gate remains assigned to a different fresh non-author."
    ),
}
dump(HERE / "exact-v1-review-pending-v3.json", pending)


source_table = "\n".join(f"| {s} | [{scope}]({u}) | {result} | {gap} |" for s, u, scope, result, gap in SOURCES)
candidate_lines = []
evidence_sections = []
evidence_by_id = {x["arxiv_id"]: x for x in evidence}
comparison_by_id = {x["arxiv_id"]: x for x in comparisons}
for row in sorted((r for r in ledger_rows if r["v3_screening_status"] == "retained"), key=lambda r: int(r["arxiv_id"].split(".")[1])):
    aid = row["arxiv_id"]
    title = html.unescape(row["title"])
    sc = row["score_v3"]
    ev = evidence_by_id[aid]
    if "pending" in ev.get("review_status", ""):
        review_label = "待审阅"
    elif "standard_complete" in ev.get("review_status", ""):
        review_label = "标准完成"
    else:
        review_label = "深入完成"
    owner_path = node_paths[row["stable_node_id"]]
    owner_link = f"[章节](../../../../{owner_path})"
    primary_url = f"https://arxiv.org/pdf/{aid}v1" if aid in {"2605.21545", "2605.22765"} else f"https://arxiv.org/html/{aid}v1"
    if aid in INTEGRATES:
        books_label = f"整合：root 写回已通过本轮修复前的 fresh 语义复核；{owner_link}；`{row['stable_node_id']}`"
    elif aid in ROOT_APPLIED_DEEP_INTEGRATES:
        books_label = f"整合：root 写回已通过 fresh post-write 语义复核；{owner_link}；`{row['stable_node_id']}`"
    elif aid in ACTIVE_NEW_INTEGRATES:
        books_label = f"整合：精确 root serialized queue 待写回及 fresh post-write review；{owner_link}；`{row['stable_node_id']}`"
    elif aid in STANDARD_REVIEWS:
        books_label = f"仅报告：5–6 分 standard review，不触发 Books Gate；{owner_link}；`{row['stable_node_id']}`"
    elif "pending" in ev.get("review_status", ""):
        books_label = f"暂缓：official exact-v1 可访问但 deep review 尚未完成；{owner_link}；`{row['stable_node_id']}`"
    else:
        books_label = f"已有覆盖：{owner_link} 当前正文承载命题；`{row['stable_node_id']}`"
    if aid == "2605.22714":
        contribution = AMEL_V1_MECHANISM
    elif aid in DEEP_REVIEWS:
        contribution = DEEP_REVIEWS[aid]["adopted"]
    elif aid in FALSE_NEGATIVE_REPAIRS:
        contribution = FALSE_NEGATIVE_REPAIRS[aid]["reason"]
    elif "pending" in ev.get("review_status", ""):
        contribution = row["screening_reason"]
    else:
        contribution = mechanism_sentence(row.get("abstract", ""))
    contribution = contribution.replace("|", "\\|")
    candidate_lines.append(
        f"| [{title}]({primary_url}) | 2026-05-22T08:00:00+08:00 | {contribution}；{sc['design_delta']}+{sc['system_reach']}+{sc['durability']}={sc['total']} | {review_label} | {books_label} |"
    )
    comp = comparison_by_id[aid]
    if "pending" in ev.get("review_status", ""):
        evidence_text = f"exact-v1 可访问但 deep review 待完成：{ev['next_review']} 当前只用 title+full abstract 保留 denominator 身份；`adopted_proposition=null`，不作为正面 Evidence，不作 No Change，不进入 Books。"
    else:
        evidence_text = (
            f"版本与证据：`{ev.get('primary_evidence_version')}`；Method=`{ev.get('method_locator')}`；"
            f"Evaluation=`{ev.get('evaluation_locator')}`；Non-proof=`{ev.get('limitations_locator')}`。"
            f" 机制判断：{ev.get('mechanism') or mechanism_sentence(row.get('abstract', ''))} 证据边界：{ev.get('claim_boundary')}"
        )
    books_text = f"Books 比较：owner=`{comp['owner_node']}`，target=`{comp['owner_path']}`；既有命题：{comp['existing_proposition']} 结论=`{comp['decision']}`。"
    if aid in INTEGRATES:
        books_text += f" 精确 root delta：{INTEGRATES[aid]['proposed_delta']} Trade-off：{INTEGRATES[aid]['tradeoff']} Failure/Fallback：{INTEGRATES[aid]['failure_fallback']}"
    elif aid in NEW_INTEGRATES:
        books_text += f" 精确 root delta：{DEEP_REVIEWS[aid]['proposed_delta']} Trade-off：{DEEP_REVIEWS[aid]['tradeoff']} Failure/Fallback：{DEEP_REVIEWS[aid]['fallback']}"
    evidence_sections.append(f"### [{title}]({primary_url})\n\n{evidence_text}\n\n{books_text}\n")

candidate_table = "\n".join(candidate_lines)
evidence_body = "\n".join(evidence_sections)
evidence_next_step = (
    f"[`exact-v1-review-pending-v3.json`](../_sources/daily-20260522/exact-v1-review-pending-v3.json) 精确列出 {PENDING_COUNT} 个可访问但尚未完成的 deep review；逐 family 记录具体 method/evaluation/non-proof locator、adopted proposition、trade-off、failure/fallback 与 Books 比较后，才能从 Deferred 清账。它们不是 Access Blocked；一个 family 完成不能替其他 pending 项清账。"
    if PENDING_COUNT else
    "[`exact-v1-review-pending-v3.json`](../_sources/daily-20260522/exact-v1-review-pending-v3.json) 已清零 Review Pending：90 个受影响 family 均有官方 exact-v1 access attempt，82 个 deep 与 8 个 standard review 已完成，Access Blocked=0。"
)
books_next_step = (
    f"[`BOOKS_WRITEBACK_QUEUE_V3.json`](../_sources/daily-20260522/BOOKS_WRITEBACK_QUEUE_V3.json) 当前含 {len(ACTIVE_NEW_INTEGRATES)} 个 active Integrate：{', '.join(f'`{aid}`' for aid in sorted(ACTIVE_NEW_INTEGRATES))}。root 写回后必须逐项检查 marker 唯一成对、位于主 Review notes 前，且正文承载 old baseline、constraint change、state/control ownership、evidence boundary、trade-off 与 failure/fallback。"
    if ACTIVE_NEW_INTEGRATES else
    f"[`BOOKS_WRITEBACK_QUEUE_V3.json`](../_sources/daily-20260522/BOOKS_WRITEBACK_QUEUE_V3.json) 已清零 active queue；{len(INTEGRATES) + len(ROOT_APPLIED_DEEP_INTEGRATES)} 个 root binding 均已逐项通过 marker、位置、正文语义、证据边界、trade-off 与 fallback 写后复核。"
)


report = f"""# Daily Research — {REPORT_DATE}

**规范：** V3

**窗口：** 2026-05-21T09:00:00+08:00 ～ 2026-05-22T09:00:00+08:00

**状态：** 进行中

**Books：** 纳入本次

**检查时间：** {CHECKED_AT}

## 1. 结论

本次不继承旧 V2.1 的 649/75 分母或 Complete 状态。按 arXiv 官方 announcement-time ID allocation 与 2026-05-21 20:00 EDT 公告批次重建后，严格窗口中的 covered-category 身份冻结为 `667 = 163 retained + 504 family-specific pre-denominator closure + 0 withdrawn`。公告在北京时间 2026-05-22 08:00，早于 09:00 截点；DataCite `created/updated` 只作 identity/DOI 佐证，不充当发布时间。

fresh review 纠正了 author corpus 的系统性误差：16 个有明确系统机制的 closure false negative 已逐项恢复，3 个垂直应用/错 owner/仅资产 false positive 已退回 closure。对受影响的 90 项逐项探测 official exact-v1 后，`88 HTML + 2 PDF fallback = 90 accessible`，真实 Access Blocked 为 0；{STANDARD_COMPLETE_COUNT} 个 score-5/6 项已完成 standard source review，风险优先的 {len(DEEP_REVIEWS)} 项已完成 deep review（含 2 个 safety override），其余 {PENDING_COUNT} 项仍是 Review Pending。Evidence 现在严格投影为 `163 = {DEEP_COMPLETE_COUNT} deep complete + {STANDARD_COMPLETE_COUNT} standard complete + {PENDING_COUNT} review pending + 0 blocked`。Books 投影为 `{INTEGRATE_COUNT} Integrate + {NO_CHANGE_COUNT} No Change + 8 Report Only + {PENDING_COUNT} Deferred`；{len(INTEGRATES) + len(ROOT_APPLIED_DEEP_INTEGRATES)} 个 root binding 已通过 fresh post-write 语义复核，{len(ACTIVE_NEW_INTEGRATES)} 个新增 Integrate 仍在精确 root serialized queue。日报保持进行中；本轮 reviewer 已成为 date-local repair author，必须在 Books 写回及其写后审查完成后，由另一位 fresh non-author 做最终 Gate。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
{source_table}

逐项来源收据见 [`source-coverage-v3.json`](../_sources/daily-20260522/source-coverage-v3.json)，owner 批次证明见 [`official-owner-batch-evidence-v3.json`](../_sources/daily-20260522/official-owner-batch-evidence-v3.json)。Meta 与 Hunyuan 的外部材料缺口已隔离，不用于“无遗漏”断言，也不阻塞其余来源和 arXiv 候选处理。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
{candidate_table}

完整算术、504 项 family-specific closure、withdrawn 检查与候选状态见 [`screening-ledger-v3.json`](../_sources/daily-20260522/screening-ledger-v3.json)。

## 4. 证据与知识整合

{evidence_body}

结构化 Evidence 见 [`exact-v1-evidence-v3.json`](../_sources/daily-20260522/exact-v1-evidence-v3.json)，逐项 current Books 命题比较见 [`books-current-content-comparison-v3.json`](../_sources/daily-20260522/books-current-content-comparison-v3.json)，root 写回回执见 [`ROOT_BOOKS_WRITEBACK_3_EVALUATION_DELTAS_20260915.md`](../_sources/daily-20260522/ROOT_BOOKS_WRITEBACK_3_EVALUATION_DELTAS_20260915.md)、[`ROOT_BOOKS_WRITEBACK_5_RESTORED_DEEP_ITEMS_20260915.md`](../_sources/daily-20260522/ROOT_BOOKS_WRITEBACK_5_RESTORED_DEEP_ITEMS_20260915.md)、[`ROOT_BOOKS_WRITEBACK_3_ACTIVE_DEEP_ITEMS_20260915.md`](../_sources/daily-20260522/ROOT_BOOKS_WRITEBACK_3_ACTIVE_DEEP_ITEMS_20260915.md)、[`ROOT_BOOKS_WRITEBACK_REFUSALBENCH_20260915.md`](../_sources/daily-20260522/ROOT_BOOKS_WRITEBACK_REFUSALBENCH_20260915.md)、[`ROOT_BOOKS_WRITEBACK_7_SECURITY_ITEMS_20260915.md`](../_sources/daily-20260522/ROOT_BOOKS_WRITEBACK_7_SECURITY_ITEMS_20260915.md) 与 [`ROOT_BOOKS_WRITEBACK_4_AGENT_ITEMS_20260915.md`](../_sources/daily-20260522/ROOT_BOOKS_WRITEBACK_4_AGENT_ITEMS_20260915.md)；对应写后审查包括 [`FRESH_POSTWRITE_REVIEW_22691_SPECTRAL_20260916.md`](../_sources/daily-20260522/FRESH_POSTWRITE_REVIEW_22691_SPECTRAL_20260916.md)。其余批次收据见同目录 queue 的逐项 `postwrite_review` 字段。No Change 以正文命题承载为依据，不以标题、marker 或 Review notes 冒充覆盖。

## 5. 缺口与下一步

本轮只冻结 fresh FAIL 指定的 bounded repair；由于修复者现在是 author，仍有三类精确后续：

1. {evidence_next_step}
2. {books_next_step} Books 正文未被本 date-local 修复改动。
3. `SRC-META-AI` 官方目录空响应，`SRC-TENCENT-HUNYUAN` 官方目录内部错误且浏览器替代入口不可用；两者 coverage assertion 保留，恢复后只重开对应 source/window。

两个日级来源材料请求见 [`materials-request-v3.json`](../_sources/daily-20260522/materials-request-v3.json)；候选 review pending 不是材料请求。

## 6. 复核

复核者：待分配新的 fresh non-author reviewer（不得是本 bounded repair 作者）。

结论：待复核。状态保持为“进行中”，不自签 Complete。当前机械 Gate 为 JSON 解析、`667=163+504+0`、`163={DEEP_COMPLETE_COUNT}+{STANDARD_COMPLETE_COUNT}+{PENDING_COUNT}+0={INTEGRATE_COUNT}+{NO_CHANGE_COUNT}+8+{PENDING_COUNT}`、{len(INTEGRATES) + len(ROOT_APPLIED_DEEP_INTEGRATES)} 组 paired marker uniqueness/position/body Gate、163 个候选 H3 唯一性、validator 与 scoped diff-check。这些检查不替代新的独立语义复核。
"""
(ROOT / "papers/2026/05/22/README.md").write_text(report)

print(json.dumps({
    "raw": 667, "retained": 163, "closures": 504, "withdrawn": 0,
    "evidence_deep_complete": DEEP_COMPLETE_COUNT, "evidence_standard_complete": STANDARD_COMPLETE_COUNT,
    "evidence_review_pending": PENDING_COUNT, "evidence_blocked": 0,
    "books_integrate": INTEGRATE_COUNT, "books_no_change": NO_CHANGE_COUNT,
    "books_report_only": 8, "books_deferred": PENDING_COUNT,
    "root_active_queue": len(active_queue_items), "root_active_queue_ids": sorted(ACTIVE_NEW_INTEGRATES),
    "root_applied_fresh_semantic_pass": sorted(set(INTEGRATES) | ROOT_APPLIED_DEEP_INTEGRATES),
    "source_blockers": ["SRC-META-AI", "SRC-TENCENT-HUNYUAN"],
}, ensure_ascii=False))
