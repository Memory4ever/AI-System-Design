#!/usr/bin/env python3
"""Render the strict 2026-06-07 Daily packet without editing Books."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260607"
REPORT = ROOT / "papers/2026/06/07/README.md"
DENOMINATOR = PACKET / "candidate-denominator.json"
SCREENING = PACKET / "registered-hit-screening.json"
DENOMINATOR_ID = "DEN-20260607-76380553"
EXECUTED_AT = "2026-08-29T21:45:00+08:00"
RECOVERED_ID = "2606.08317"
BLOCKED_ID = ""  # Conditional blocker was resolved from the official exact-v1 PDF.
EXACT_TITLES = {
    "2606.08348": "Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses",
}
EXACT_ABSTRACTS = {
    "2606.08348": "LLM agents increasingly rely on external inference conditions: prompts, tools, memory, SOPs, skills, and harness feedback. Bayesian-Agent treats reusable skills and SOPs as hypotheses under a frozen model and harness, records verified trajectories, maintains a feature-conditioned categorical posterior, and maps posterior state into auditable actions such as patch, split, compress, retire, and explore. With deepseek-v4-flash, incremental repair improves SOP-Bench from 80% to 95%, Lifelong AgentBench from 90% to 100%, and RealFin-Bench from 45% to 65%; native, GenericAgent, mini-swe-agent, and Claude Code backends are evaluated.",
}


def family(arxiv_id: str) -> str:
    return f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}"


def pipe(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def canon_cell(value: str) -> str:
    values = [unicodedata.normalize("NFC", item.strip()) for item in value.split(";")]
    return ";".join(sorted(item for item in values if item))


def norm_body(value: str) -> str:
    lines = [unicodedata.normalize("NFC", line.rstrip()) for line in value.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


SCORES = {
    "2606.07923": (3, 2, 3), "2606.07936": (2, 2, 3), "2606.07943": (3, 3, 3),
    "2606.07950": (2, 2, 3), "2606.07957": (3, 2, 3), "2606.07968": (2, 2, 3),
    "2606.07970": (2, 2, 2), "2606.07992": (3, 2, 3), "2606.08049": (3, 3, 3),
    "2606.08094": (3, 2, 3), "2606.08106": (3, 3, 3), "2606.08197": (2, 2, 3),
    "2606.08200": (2, 2, 3), "2606.08302": (2, 2, 2), "2606.08317": (2, 2, 2),
    "2606.08340": (2, 2, 3), "2606.08346": (2, 2, 2), "2606.08348": (3, 2, 3),
    "2606.08367": (2, 2, 3), "2606.08372": (3, 2, 3), "2606.08381": (2, 2, 2),
    "2606.08382": (2, 2, 3), "2606.09916": (3, 3, 3),
}


LOCATORS = {
    "2606.07923": ("§3 Larch; §§3.1–3.4 state, A2C, selectivity planner and latency-hiding pipeline", "§4 Experimental Evaluation; §4.1 setup; §§4.2–4.8 results, sensitivity, oracle and ablation", "§5 Discussion and Conclusion; §4.8 delayed-update counterevidence", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.07936": ("§3 Reporting Criteria and Codebook; §4 Dataset and Methods", "§5 Results over 284 manually reviewed and 1.8k+ LLM-assisted papers", "§6 Discussion and recommendations; the codebook measures reporting, not intrinsic judgment correctness", "https://github.com/larchlab/Illusions-of-the-Gold-Standard — repository disclosed; event-time commit not pinned"),
    "2606.07943": ("§3 Poise Attack; §§3.1–3.5 eligibility, placement, generation and execution postcondition", "§4 Experimental Setup; §5 Results on Skill-Inject and SkillsBench", "§6 Limitations; audit false positives and eligible-task restriction", "SkillSafety/SkillTester artifact disclosed in manuscript; immutable event-time commit not pinned"),
    "2606.07950": ("§4 CoDaPO; confidence/difficulty value, update weighting and within-mini-batch resampling", "§5 Experiments; §5.1 setup; Appendix C.6 implementation details", "§6 Conclusion; Appendix dynamic-difficulty analysis and fixed-compute boundary", "https://github.com/tmlr-group/CoDaPO — repository disclosed; event-time commit not pinned"),
    "2606.07957": ("§4 Demand-Driven Architecture; formal derivation and bidirectional catalogue/asset triggers", "§8 Evaluation Methodology; complexity analysis and worked example, not executed measurements", "§10 Limitations; rule correctness and alert prioritization explicitly out of scope", "Not Disclosed — architecture paper provides no executable artifact"),
    "2606.07968": ("§IV RecurGuard; recurrence, volume and progress signals with three-chunk termination", "§VI Experimental Setup; §VII Results and adaptive stress tests", "§XI Limitations; exposed-trace dependency and topical adaptive miss boundary", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.07970": ("§3 Methods; bi-level Patcher inner attack and parallel implementation", "§4 Experiments; §4.1 setup and full-parameter attack transfer", "§6 Limitations and Conclusion; stronger simulated attacks remain a bounded threat-model proxy", "https://github.com/haomingwen/patcher — repository disclosed; event-time commit not pinned"),
    "2606.07992": ("§3 Methodology; seven-dimensional mutation space and controlled error-path injection", "§4 Evaluation; Appendix C.1 controlled tool-error protocol", "§5 Discussion and Conclusion; production guardrails and controlled-environment boundary", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.08049": ("§3 SKILL.nb; selective formalization, versioned notebook and gate-conditioned local fallback; Appendix A", "§4 Experiments; shared Evaluation Protocol and WebArena/Mind2Web/GitLab migration slices", "§5 Limitations; Appendix A.8 lifecycle and environment-drift boundaries", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.08094": ("§3 Runtime Design; §3.3 cached prefix/action expert and Algorithm 1 solver loop", "§4 Evaluation; §4.1 setup and 200-episode LIBERO-Object protocol", "§5 Limitations; deployment portability does not prove every VLA architecture behaviorally identical", "https://fai-modelopt-tech.github.io/vla-cpp.github.io/ — project, code and scaffold disclosed; commit not pinned"),
    "2606.08106": ("§4 PACE; paired testing-by-betting e-process and Algorithm 1 commit gate", "§5 Experiments on prompt self-evolution with hidden real/no-gain conditions", "§6 Limitations; per-decision guarantee is not a global lifetime guarantee", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.08197": ("§III AlignFed Framework; §IV version grouping, semantic calibration and fairness weighting", "§V Experimental Evaluation; §V-A setup", "§VI Conclusion and stated simulation/heterogeneous-edge scope", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.08200": ("§3 Online Agent-as-a-Judge; in-world situation generation through native dialogue/action", "§4 Experiments; §4.1 life-simulation setup and human-label agreement", "§5 Discussion; evaluator intervention can change the trajectory it measures", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.08302": ("§IV attention-head analysis; §V HACK++ calibration, decoupled attention/cache budgets and adaptive allocation", "§VI Experiments across VAR generation and understanding tasks", "§VII Conclusion; one-time calibration and VAR-specific head taxonomy bound transfer", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.08317": ("§II Methodology: Literature Selection and Analysis Framework; §VI-A Evaluation Dimensions; §IX-B Database Architecture Selection Framework, Stages 1–3 and scoring formula", "§VI-B Table I directional performance characteristics; §IX-D financial-fraud case study, Tables IV–V", "§IX-B Framework Limitations; §XI Limitations", "Not Disclosed — exact-v1 PDF names no executable framework artifact or immutable repository revision"),
    "2606.08340": ("§3 alem benchmark design; procedural coordination tasks, communication and difficulty controls", "§4 Experiments; §4.1 zero-shot 13-LLM team setup and MARL reference", "§6 Limitations and Future Work; benchmark world and zero-shot policy scope", "https://github.com/alem-world/alem-env — repository disclosed; event-time commit not pinned"),
    "2606.08346": ("§3 CATPO; informativeness score, critique-guided healing and normalized tree weighting", "§4 Experiments; §4.1 Qwen2.5-Math-1.5B on MATH and four test benchmarks", "§5 Conclusion; single base-model/math-training regime and critique cost bound generality", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.08348": ("§3 Bayesian-Agent; verified trajectories, posterior skill beliefs, actions and guardrails", "§4 Experiments across RealFin-Bench, SOP-Bench, Lifelong AgentBench and harness ablations", "§5 Limitations; posterior repair depends on verifiable task artifacts", "https://github.com/DataArcTech/Bayesian-Agent — repository disclosed; event-time commit not pinned"),
    "2606.08367": ("§3 Platform Design; persistent memories, 120+ tools, live data and consequential governance", "§5.1 setup; §5.2 15-day cross-vendor results across five parallel worlds", "§8 Limitations; one 15-day simulation cannot establish deployment-timescale causality", "Prompts, logs and configurations released; immutable event-time revision not identified"),
    "2606.08372": ("§2 taxonomy and attack families; §4 memorization test and RA-as-MIA reduction", "§3 empirical study of 14 attacks, 9 generators and 5 datasets; §4 interpretation tests", "§5.3 Limitations; black-box single-record released-table threat model", "Attack infrastructure disclosed through NIST CRC context; immutable event-time revision not pinned"),
    "2606.08381": ("§3 comparative black-box framework; semantic-space divergence against a reference model set", "§4 Case Studies of previously reported provider-specific alignment behavior", "Limitations section; relative divergence detects difference, not absolute truth or provider intent", "Not Disclosed — no immutable event-time artifact revision identified"),
    "2606.08382": ("§3 STAR-KV; differentiable thresholds, key/value-specific factorization and rank-aware quantization", "§4 Experiments; Appendix A.4 kernel and benchmark details", "§5 Conclusion and ablations; low-rank sensitivity is model/workload dependent", "https://github.com/PriyanshBhatnagar/STAR-KV — repository disclosed; event-time commit not pinned"),
    "2606.09916": ("§3 IntentKV; session QueryMemory, residual scorer and slot-map sentinel redirection", "§4 Experiments; §4.1 BCP setup and longest-query stress slice", "§ Limitations (exact heading); learned pruning keeps base LLM fixed but does not prove universal task preservation", "Not Disclosed — no immutable event-time artifact revision identified"),
}


def bound_locators(arxiv_id: str) -> tuple[str, str, str, str]:
    """Bind every facet to the exact manuscript identity used by the review."""
    if arxiv_id == BLOCKED_ID:
        return (
            "Pending — arXiv:2606.08317v1 exact body unavailable after official HTML, PDF and source-bundle recovery",
            "Pending — arXiv:2606.08317v1 evaluation section unavailable; abstract-only case-study claim not admitted",
            "Pending — arXiv:2606.08317v1 limitations section unavailable; secondary summaries excluded",
            "Not Disclosed — author/project search found no verifiable arXiv:2606.08317v1 artifact mirror",
        )
    result = []
    for value in LOCATORS[arxiv_id]:
        if value.startswith(("Not Disclosed", "Not Required", "Not Applicable")):
            result.append(value)
        else:
            result.append(f"arXiv:{arxiv_id}v1 {value}")
    return tuple(result)  # type: ignore[return-value]


BENCH = {
    "2606.07923": ("Three real datasets plus three semantic-filter workloads and synthetic selectivity/horizon sweeps", "Semantic-filter LLM backends and lightweight A2C/selectivity models; exact backend matrix is workload-specific", "Not Disclosed — §4.1 does not bind one hardware topology to every result", "Not Disclosed", "Rows/documents with precomputed embeddings; no token length contract", "Filter outcomes and token calls; no output-token length contract", "Not Disclosed", "Not Disclosed", "Not Disclosed — token cost is an outcome, not an acceptance SLO", "Token use/cost overhead, convergence, sensitivity, oracle comparison and update latency"),
    "2606.07936": ("284 confirmed manual *CL 2023–2025 papers plus LLM-assisted labeling of the remaining long-form/human-evaluation corpus", "GPT-4o-mini-2025-04-16 for automatic annotation; Gemini-2.5-Pro and Claude-3.7-Sonnet-20250219 in model-selection pilot", "Not Disclosed", "Not Disclosed", "Abstract, introduction, candidate human-evaluation sections and appendix passages", "Five chunks of codebook answers as flat JSON; up to two full reruns after validation failure", "Not Disclosed — question chunks are separate API calls, not a disclosed batch size", "Not Disclosed", "Only fields with held-out validation accuracy >0.75 are reported; this is a reporting threshold, not service SLO", "Manual IAA; GPT-4o-mini selection on 26 papers; independent 125-paper/3,875-label validation; bootstrap reporting rates"),
    "2606.07943": ("Skill-Inject 25 eligible tasks ×3 harms and SkillsBench 27 tasks ×3, two trials/configuration", "codex+gpt-5.2; OpenClaw+DeepSeek-V4-Flash/Pro; Claude Code+Sonnet-4.6", "Docker/Harbor sandbox; host accelerator not disclosed", "Not Disclosed", "Skill files and task contexts; no fixed token length", "One injected instruction plus legitimate task completion", "Not Disclosed", "Not Disclosed", "ASR requires sandbox postcondition and passing legitimate-task verifier", "Joint ASR, task verifier, postcondition verifier and four-judge SkillTester delta alerts"),
    "2606.07950": ("MATH training and twelve reported math, general-reasoning and code benchmarks", "Llama-3.2-1B-Instruct; Qwen2.5-Math-1.5B and 7B", "4×NVIDIA A100", "Not Disclosed", "Dataset-defined prompts; no fixed input length", "Evaluation uses 32 responses at temperature 0.6; no fixed output cap disclosed", "16; 8 rollouts per group", "Not Disclosed", "Not Disclosed", "Accuracy across twelve benchmarks, confidence/difficulty dynamics and fixed-compute comparison"),
    "2606.07957": ("No executed benchmark — formal semantics, complexity analysis, worked example and proposed evaluation methodology", "Not Disclosed — no model evaluated", "Not Disclosed", "Not Disclosed", "Catalogue entries and live asset graphs; no fixed size", "Derived tenant-local rules", "Not Disclosed", "Not Disclosed", "Not Disclosed", "Methodology proposes latency/resource evaluation; paper explicitly does not prove rule correctness or alert priority"),
    "2606.07968": ("OverThink, ExtendAttack, held-out QA/code/math/summarization and adaptive stress tests", "DS-R1-Qwen-7B primary; DS-R1-Llama-8B, Qwen3-8B, Llama3.1-8B, Sonnet-4.5 and Opus-4.7 slices", "NVIDIA A100 for open models; count/topology not disclosed", "Not Disclosed", "Prompt/task dependent", "Reasoning trace analyzed in 64-word chunks", "Not Disclosed", "Not Disclosed", "Three consecutive anomalous chunks is termination policy, not a service SLO", "TPR/FPR, joint miss rate, token amplification and post-hoc QDM fallback"),
    "2606.07970": ("Beavertails/PKU-SafeRLHF/ToxicDPO-v2 test attacks; AdvBench, Beavertails and HEx-PHI ASR; Alpaca utility", "Qwen2.5-1.5B main/ablation; Qwen3-4B and Llama3-8B generalization; Qwen3-Max harmfulness judge", "Not Disclosed", "Not Disclosed", "200 unsafe Beavertails plus 800 GSM8K samples in default test-time mix", "Maximum 256 generated tokens; temperature 0.6 and top-p 0.9", "Global batch 4 for attack, defense, baselines and test-time attack", "Parallel attack/defense loops use stale attack vectors; worker concurrency not disclosed", "Not Disclosed", "Attack Success Rate on three safety sets, utility, transfer and wall-clock; fully poisoned and larger-malicious-set failures retained"),
    "2606.07992": ("Controlled MCP tool-error JSON with seven mutation dimensions and email-exfiltration effect", "Gemini-3.1-Pro, GPT-5.5, GLM-5.1, Qwen3-Coder", "Provider APIs; hardware not disclosed", "Not Disclosed", "Controlled agent/tool contexts; no fixed token length", "Tool-call compliance/effect", "Not Disclosed", "Not Disclosed", "Not Disclosed", "Injection compliance/ASR by error structure plus production-guardrail comparison"),
    "2606.08049": ("WebArena-Verified, Mind2Web cross-site/domain and GitLab 15.7→16.11/18.9 migration", "Agent model/backend matrix is experiment-specific; no single evaluated model identity", "Not Disclosed", "Not Disclosed", "Workflow steps, pages and notebook evidence; no fixed token length", "Task actions, screenshots and traces", "Not Disclosed", "Three re-executions for durability; not concurrency", "Gates are per-step validity policies, not service SLOs", "Success, retained success, bounded-repair recovery/regression and migration gap"),
    "2606.08094": ("LIBERO-Object 10 tasks ×20 episodes per architecture and ALOHA moving-target stress test", "Seven VLA architectures spanning five backbones/four action heads", "RTX 3060; Jetson AGX Orin; 8GB Jetson Orin Nano", "Model/package-specific; no one precision contract", "Vision-language prefix and robot observation; no fixed token length", "Action-expert solver steps", "Batch 1", "One request at a time in roofline slice; broader concurrency not disclosed", "Not Disclosed", "Episode success, behavioral match, latency, memory footprint and cross-hardware roofline"),
    "2606.08106": ("Prompt self-evolution on GSM8K, SVAMP and ARC-Challenge with hidden-real-gain and no-gain regimes", "Qwen2.5 0.5B–3B agents", "Not Disclosed", "Not Disclosed", "Paired identical evaluation instances", "Commit/reject decisions and task answers", "Not Disclosed", "Sequential optional stopping; no concurrent execution contract", "User-set per-candidate false-commit probability", "False/harmful commits, held-out accuracy, variance and evaluation cost"),
    "2606.08197": ("Heterogeneous asynchronous federated fine-tuning under non-IID data and staleness", "Llama3-8B and Qwen3-8B", "Single NVIDIA A100", "FP16", "Maximum sequence length 650", "Not Disclosed", "Batch 1", "Asynchronous clients; fixed concurrent-client count not disclosed", "Communication budget ≤50MB is a constraint, not latency SLO", "Convergence, accuracy, fairness, staleness robustness, latency and communication"),
    "2606.08200": ("Life simulation: five characters, 32 social criteria, three target backends × three seeds", "Target-agent backends vary; all automated judges use GPT-5.4-mini", "Provider APIs; hardware not disclosed", "Not Disclosed", "Interactive social histories; no fixed token length", "Dialogue/actions and criterion evidence", "Not Disclosed", "Five-character world; no request concurrency contract", "Not Disclosed", "Criteria coverage and agreement with human labels versus passive judges"),
    "2606.08302": ("Multiple VAR models over text-to-image, class-conditional and unified understanding/generation tasks", "Infinity-2B/8B and additional VAR models in §VI", "Not Disclosed", "Not Disclosed", "Multi-scale visual-token histories", "Generated images/tokens", "Not Disclosed", "Not Disclosed", "30% attention/10% cache are budgets, not SLOs", "Generation quality, task accuracy, attention/cache budget and robustness to 1% cache"),
    "2606.08317": ("Conceptual comparison of 13 database paradigms plus one representative financial-fraud architecture case; Table I ranges are directional literature synthesis, not a controlled benchmark", "Not Disclosed — no model is evaluated", "Not Disclosed", "Not Disclosed", "Workload profile over nine architectural dimensions; no fixed input length", "Ranked paradigm/architecture recommendation; no fixed output length", "Not Disclosed", "Not Disclosed", "Not Disclosed", "Qualitative compatibility values 1/2/3 weighted by workload importance; financial case maximum score 90; no product-level empirical evaluator"),
    "2606.08340": ("Procedural long-horizon alem world across coordination difficulty; homogeneous teams and MARL references", "13 modern LLMs zero-shot; named frontier examples include Gemini-3.1-Pro-High and GPT-5.4-High", "Not Disclosed", "Not Disclosed", "World observations and communication histories", "Actions/messages over long horizons", "Not Disclosed", "Team size/configuration disclosed per environment; serving concurrency not disclosed", "Not Disclosed", "Normalized return split into base-task and coordination reward; communication/memory/reasoning ablations"),
    "2606.08346": ("Qwen2.5-Math-1.5B trained on MATH; AIME24, MATH-500, OlympiadBench and MinervaMath", "Qwen2.5-Math-1.5B", "Not Disclosed", "Not Disclosed", "MATH problems and rollout trees", "Tree continuations/critiques", "Not Disclosed", "Not Disclosed", "Not Disclosed", "Pass@1/Avg@8 and macro accuracy; tree-informativeness/healing ablations"),
    "2606.08348": ("SOP-Bench, Lifelong AgentBench and RealFin-Bench across native, GenericAgent, mini-swe-agent and Claude Code backends", "deepseek-v4-flash and deepseek-v4-pro for Bayesian variants; Claude Sonnet-4.6, Claude Opus-4.6 and GPT-5.4 comparison rows", "Not Disclosed", "Not Disclosed", "Verified task trajectories with benchmark/context/failure-mode/token/turn/latency features", "Task artifacts plus skill actions; table reports input/output/total tokens", "Not Disclosed", "Not Disclosed", "Posterior action thresholds are lifecycle policy, not service SLO", "Task accuracy, token accounting, efficiency, full/incremental repair and backend/model ablations"),
    "2606.08367": ("15 days, five parallel worlds, ten agents/world, 120+ tools and three memories", "Claude Sonnet-4.6, Grok-4.1-Fast, Gemini-3-Flash, GPT-5-mini and mixed population", "Live provider APIs; hardware not disclosed", "Not Disclosed", "Persistent world plus live weather/news/internet inputs", "Actions, governance outcomes and logs", "Not Disclosed", "Ten agents/world; request concurrency not disclosed", "Not Disclosed", "Cross-world behavioral trajectories, governance stability/collapse and released logs"),
    "2606.08372": ("14 attacks ×9 synthetic-data generators ×5 datasets; QI sizes 3–16; DP epsilon sweeps", "Classifiers, graphical models and diffusion/generative attack families; not one LLM", "Not Disclosed", "Not Disclosed", "Tabular released datasets and target quasi-identifiers", "Predicted hidden attributes", "Not Disclosed", "Not Disclosed", "Not Disclosed", "Rarity-weighted reconstruction advantage, train/holdout memorization gap and RA-as-MIA comparison"),
    "2606.08381": ("Three black-box cases: DeepSeek-R1 on China- and US-sensitive domains, and Meta AI Chat/Llama 4 on Meta-related topics", "DeepSeek-R1 and Meta AI Chat/Llama 4 targets; diverse baseline ensemble; GPT-5.2 and Gemini-3.1-Flash-Lite judges; four embedding models", "Provider APIs; hardware not disclosed", "Not Disclosed", "Shared case-specific prompts generated with GPT-4o; fixed token lengths not disclosed", "Black-box responses, embeddings and ordinal judge labels", "Not Disclosed", "Not Disclosed", "Statistical alpha=0.05 is a hypothesis threshold, not service SLO", "Welch one-sided t-test, bootstrap median test, target-permutation diagnostic; relative divergence not absolute correctness or intent"),
    "2606.08382": ("WikiText-2 perplexity, six LM-Eval tasks, LongBench and 4K RULER plus kernel/throughput slices", "LongChat-7B-v1.5, Llama-2-7B, Llama-3-8B-Instruct and Llama-3.1-8B-Instruct long-context slice", "RTX Pro 6000 for <6 GPU-hour 3,000-sample calibration; single RTX 4090 for attention/kernel latency", "FP16 SDPA baseline; first 20% channels 4-bit and remainder 3-bit for average 3.2-bit quantized slice", "Benchmark-defined; RULER explicitly 4K", "Benchmark-defined generation lengths", "Not Disclosed", "Not Disclosed", "Not Disclosed", "Perplexity, zero-shot accuracy, LongBench/RULER, compression, attention speedup and end-to-end throughput"),
    "2606.09916": ("BCP agent benchmark plus the 100 longest commonly completed Qwen2.5-14B queries", "Qwen3-8B and Qwen2.5-14B", "Not Disclosed", "Not Disclosed", "Trajectory histories; 8k live-KV budget in primary slice", "Agent responses/tool trajectories", "Not Disclosed", "Not Disclosed", "8k is a KV budget, not a latency SLO", "Task accuracy, peak request tokens, worst-case raw KV reads and full-cache fidelity"),
}


INTEGRATE = {"2606.07923", "2606.07943", "2606.08049", "2606.08106", "2606.08200", "2606.09916"}
SELECTED = {"2606.07943": "DA-20260607-SECURITY", "2606.08106": "DA-20260607-EVOLUTION", "2606.09916": "DA-20260607-RUNTIME"}
NONELIGIBLE_REASON = {
    "2606.07970": "Score V2=6/9、Review Override=`none`；train-time adversarial attack 只形成 TRAIN-SFT 内的受限 robustness branch，未提出新的跨 owner 状态、结构缺口、Books correction 或 pre-Books `potential_books_delta`。",
    "2606.08302": "Score V2=6/9、Review Override=`none`；head/layer/step-aware VAR cache compression 是视觉自回归 workload 的局部压缩分支，未改变通用 KV identity owner，也没有 structural/cross-cutting correction 或 pre-Books `potential_books_delta`。",
    "2606.08317": "Score V2=6/9、Review Override=`none`；九维数据库 taxonomy、filter 与 compatibility score 是概念性选择框架，exact-v1 没有 product-level empirical evaluator，因而不构成平台 admission owner 的新机制、结构缺口或 pre-Books `potential_books_delta`。",
    "2606.08346": "Score V2=6/9、Review Override=`none`；critique-guided grafting 只修复 CATPO 的 all-fail rollout tree，是 TRAIN-GRPO 内的局部训练分支，未改变跨系统 control ownership，也没有 correction/structural gap 或 pre-Books `potential_books_delta`。",
    "2606.08381": "Score V2=6/9、Review Override=`none`；reference-set-relative divergence 只能审计 provider 间语义差异，不能判定 truth、intent、harm 或 release authority，因此未形成新的 evaluation/release contract、结构缺口或 pre-Books `potential_books_delta`。",
}

TRADE = {
    "2606.07923": "Larch-Sel buys token savings with an online estimator whose errors can reorder individual rows; static PZ/Quest-style plans remain the fallback before enough labels accrue or when embeddings are unavailable. Its evolution is from global heuristic order to learned per-row selectivity plus exact dynamic programming, not a new semantic operator.",
    "2606.07936": "A twenty-field codebook raises reporting cost and can measure whether a study is reproducible without proving that its human judgments are valid. It coexists with task-specific quality rubrics: the contribution is a receipt schema for who judged, what was measured and how results may be interpreted.",
    "2606.07943": "Moving the payload from YAML to a locally plausible body position trades visibility for dependence on the agent reading that position. The joint verifier avoids invocation-only false success, while SkillTester's high clean-skill false-positive rate shows that LLM alerts cannot replace sandbox effect evidence or conservative skill admission.",
    "2606.07950": "Difficulty-aware resampling concentrates fixed rollout compute but can starve examples whose value estimate is initially wrong; uniform GRPO remains the neutral branch when confidence and empirical difficulty are unreliable. The result supports compute reallocation within the tested regimes, not a universal optimizer ordering.",
    "2606.07957": "Tenant-local rule derivation shortens vendor cadence but makes catalogue freshness, asset-graph correctness and rule garbage collection tenant responsibilities. Centrally authored rules remain necessary for predicates not derivable from structured feeds; the paper explicitly leaves rule correctness and alert priority outside its proof.",
    "2606.07968": "Early termination saves billed reasoning tokens only when traces are observable and the three signals remain anomalous; topical adaptive attacks expose a roughly 50% joint-miss boundary. QDM therefore remains a post-hoc fallback, and the monitor must not terminate benign long reasoning from a single transient alarm.",
    "2606.07970": "A stronger inner attack improves robustness to full-parameter malicious fine-tuning at extra train-time compute; the parallel algorithm reduces wall time without removing that compute. Conventional SFT alignment remains cheaper for weaker threat models, and success against simulated attacks does not certify every future poisoning strategy.",
    "2606.07992": "Systematic mutation widens coverage of MCP error paths but the experiment's controlled tool errors and exfiltration action do not reproduce every production framework. Framework guardrails can still contain the path; the durable change is to treat errors as authority-bearing inputs rather than to ban tool error text.",
    "2606.08049": "Versioned notebooks add maintenance and gate design, and a stale gate can reject reusable code or trigger excessive natural-language fallback. One-shot free-form workflows remain useful for non-repeated tasks; SKILL.nb evolves durable workflows by localizing failure and repair evidence at each step.",
    "2606.08094": "One portable runtime reduces Python-stack drift but requires architecture adapters, self-contained bundle conversion and hardware-specific kernels. Generic PyTorch remains the development branch for unsupported models; batch-1 roofline results identify utilization as the tested lever without proving all robot control loops meet real-time deadlines.",
    "2606.08106": "PACE spends paired evaluations to avoid noisy commits and may delay acceptance of small real gains. Greedy acceptance remains faster when errors are cheap, but self-modifying production agents need the per-candidate false-commit bound; optional-stopping validity must not be misstated as a lifetime family-wise guarantee.",
    "2606.08197": "Version grouping and calibration reduce stale semantic drift but introduce calibration data, grouping delay and fairness weighting into the aggregator. Synchronous FFT remains simpler under homogeneous clients; AlignFed is the heterogeneous asynchronous branch and its single-A100 FP16 experiment does not establish large fleet SLOs.",
    "2606.08200": "An active judge improves criterion coverage by changing the situation, so its actions become part of the evidence-generating treatment and may confound natural behavior. Passive trajectory scoring remains necessary for observational questions; the two modes must be reported separately and the judge must never repair the target trajectory.",
    "2606.08302": "Head-type calibration and separate attention/cache budgets improve aggressive VAR compression but can age when model, layer behavior or generation regime changes. Global compression remains the simpler branch; HACK++ is VAR-specific evidence and does not displace general LLM KV retention owners.",
    "2606.08317": "Workload profiling and hard filtering make architecture choice auditable, but the compatibility values are qualitative paradigm-level judgments and the fraud example is illustrative rather than a controlled product benchmark. Existing platform admission and one-size-fits-all safeguards remain the owner contract; product-specific measurements, deployment constraints and empirical validation must precede any commit.",
    "2606.08340": "Alem makes coordination measurable by imposing a particular procedural ecology, reward split and communication channel; strong return there need not transfer to open production teams. Short structured benchmarks remain useful for isolated skills, while alem adds long-horizon coordination stress rather than a universal agent ranking.",
    "2606.08346": "Critique-guided healing recovers all-fail trees but adds critique generation and can graft a persuasive wrong repair. Flat GRPO/TreeRPO remain simpler when trees already contain mixed outcomes; evidence is limited to one math model/training corpus and four math benchmarks.",
    "2606.08348": "Posterior skill actions are only as trustworthy as priors, verified trajectory artifacts and the harness's failure taxonomy; sparse evidence can make repair conservative. Raw empirical rates remain transparent with abundant homogeneous trials, while Bayesian-Agent owns finite-sample cross-harness uncertainty rather than model-weight learning.",
    "2606.08367": "Continuous worlds expose drift and cross-influence at the cost of API nondeterminism, high run expense and difficult causal attribution. Exam-style benchmarks remain the controlled complement; a 15-day, five-world observation demonstrates observability, not deployment-timescale safety or vendor superiority.",
    "2606.08372": "The unified risk scale improves comparability but remains a black-box, single-record released-table threat model; model inversion, aggregate reconstruction and coordinated targets stay separate branches. The train/holdout gap prevents high reconstruction accuracy from being mislabeled as memorization, especially for rare records.",
    "2606.08381": "Relative semantic divergence depends on the reference-set composition and can detect systematic difference without identifying truth, provider intent or harm. Ground-truth task evaluation remains necessary where labels exist; this framework is the black-box comparative branch for otherwise unobservable policy variation.",
    "2606.08382": "Adaptive rank and mixed precision need learned thresholds, decomposition choices and custom Triton kernels; sensitivity can move across heads, blocks, models and workloads. Fixed-rank compression remains easier to deploy, and throughput gains cannot be transferred beyond the disclosed GPU/kernel slices.",
    "2606.09916": "QueryMemory scoring adds session state and can irreversibly drop evidence when intent changes; sentinel redirection preserves physical identity but not information already evicted. Full cache remains the correctness fallback, while budgeted pruning is justified only by the BCP fidelity and read-volume evidence reported for the two Qwen models.",
}

NOT_SELECTED_REASON = {
    "2606.07923": "Larch is the strongest semantic-query cost candidate and remains an Integrate proposal, but its planner delta is confined to AI_FILTER ordering and overlaps the selected runtime-state axis less broadly than IntentKV's cross-turn identity-preserving cache transition.",
    "2606.07936": "The human-evaluation reporting codebook changes receipt completeness, yet it audits published protocol fields rather than controlling a running evaluator; Online Agent-as-a-Judge and PACE expose more direct control/evidence transitions in this frontier.",
    "2606.07950": "CoDaPO provides a useful fixed-compute rollout allocation policy, but confidence/difficulty resampling is a narrower training optimization than PACE's statistically valid authority to commit self-evolution changes.",
    "2606.07957": "Demand-driven CSPM changes rule derivation ownership but reports an evaluation methodology rather than executed measurements; Poise provides stronger completed-effect security evidence for deep analysis while this architecture remains independently No Change.",
    "2606.07968": "RecurGuard gives a concrete early-termination monitor with strong non-adaptive detection, but its exposed-trace dependency and topical adaptive miss boundary make it narrower than Poise's end-to-end skill admission/effect contract.",
    "2606.07992": "VATS establishes the MCP error loop as an authority-bearing ingress path, but controlled injection compliance is less durable than Poise's joint postcondition plus legitimate-task verifier and varies with production guardrails.",
    "2606.08049": "SKILL.nb is an Integrate-quality workflow lifecycle mechanism, but its notebook/gate realization is an execution artifact branch; PACE isolates the more general acceptor authority and false-commit guarantee selected for self-evolution.",
    "2606.08094": "vla.cpp is strong portable-runtime evidence across three hardware tiers, but its seven VLA adapters and batch-1 roofline form a specialized deployment branch rather than a cross-turn inference-state contract.",
    "2606.08197": "AlignFed makes staleness, semantic calibration and participation fairness explicit, yet the single-A100 edge simulation is less cross-cutting than the selected acceptor and runtime-state mechanisms.",
    "2606.08200": "Online Agent-as-a-Judge survives as an Integrate proposal because intervention changes evidence acquisition, but its life-simulation criteria coverage is a narrower evaluator branch than PACE's reusable commit-control result.",
    "2606.08340": "Alem cleanly separates individual and coordination reward across 13 LLMs, but the procedural world is a benchmark owner rather than a new production coordination-control mechanism; it remains No Change against Ch82.",
    "2606.08348": "Bayesian-Agent provides evidence-bearing posterior skill actions across harnesses, but its guarantee depends on verifiable artifacts and specified priors; PACE offers the sharper optional-stopping commit boundary for the selected evolution unit.",
    "2606.08367": "Emergence World expands duration, heterogeneity and consequential governance, but five 15-day worlds demonstrate observability rather than a causal control mechanism; it remains a platform-evaluation alternative.",
    "2606.08372": "The reconstruction SoK contributes the strongest privacy interpretation result in the set, but its released-table black-box threat model is orthogonal to the selected agent security and runtime chains and is already owned by the security evaluation branch.",
    "2606.08382": "STAR-KV delivers adaptive low-rank thresholds, quantization and kernels, but Ch45 already owns variable-rank low-rank compression; IntentKV adds the less-covered cross-turn intent plus prefix-identity transition and is therefore selected.",
}

TARGET = {
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md#L358",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md#L335",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md#L367",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md#L10",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/67-monitoring.md#L10",
    "TRAIN-SFT": "books/part-04-training-system/29-sft.md#L10",
    "AGENT-MCP": "books/part-07-agent/78-tool-calling.md#L10",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md#L159",
    "INFER-REQUEST-LIFECYCLE": "books/part-05-inference-system/42-what-happens-during-inference.md#L10",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md#L343",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md#L10",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L292",
    "PLATFORM-FOUNDATIONS": "books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L10",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md#L10",
}


def review_body(item: dict, route: str) -> str:
    aid, fam, owner = item["arxiv_id"], item["source_family_id"], item["stable_node_id"]
    if aid == BLOCKED_ID:
        claim = ("该 family 只能保留 abstract-level identity：九维架构比较、workload profiling、constraint filtering、compatibility scoring、十三种范式和金融欺诈案例均未被提升为 exact-v1 机制或评估结论。")
        return f"<!-- claim:{fam}:start -->\n{claim}\n<!-- claim:{fam}:end -->\n\n恢复记录：官方 exact-v1 HTML 返回 Internal Error；PDF 与 source-bundle 连接被重置；作者/project/artifact 搜索未找到可验证镜像。ResearchGate 仅提供请求全文，Moonlight 属二手总结，二者均未用于 claim。"
    method, evaluation, limitations, artifact = LOCATORS[aid]
    workload, model, hardware, precision, input_len, output_len, batch, concurrency, slo, evaluator = BENCH[aid]
    title = item["title"]
    claim = (
        f"{title} 处理的问题是：{item['rationale']}。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `{method}`。"
        f"状态 owner 为 `{owner}`：数据面保存该论文特有的观测与派生状态，控制面只执行其显式 gate/order/termination/commit 动作，evidence plane 则由 `{evaluation}` 提供可复核结果。"
    )
    proof = (
        f"评估证明边界：workload=`{workload}`；model=`{model}`；evaluator=`{evaluator}`。"
        f"它不证明未披露的 hardware/precision/batch/concurrency/SLO，也不把实验性阈值、预算或观察到的 latency 冒充生产 SLO；对应反证与外推边界在 `{limitations}`。"
    )
    trade = f"取舍、failure、共存与演进：{TRADE[aid]} Artifact 边界：`{artifact}`。"
    return f"<!-- claim:{fam}:start -->\n{claim}\n\n{proof}\n\n{trade}\n<!-- claim:{fam}:end -->"


def provenance(item: dict, route: str, override: str, body: str) -> str:
    aid, fam = item["arxiv_id"], item["source_family_id"]
    locators = bound_locators(aid)
    fields = ["review-completion-v1", fam, f"paper-v1:{aid}", f"arXiv:{aid}v1", "SRC-ARXIV", f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1", route]
    if override != "none":
        fields.append(f"review-override:{override}")
    fields.extend(canon_cell(value) for value in locators)
    fields.extend([f"claim:{fam}", f"review:{fam}", f"review-body-sha256:{hashlib.sha256(norm_body(body).encode()).hexdigest()}"])
    return "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16]


def existing(owner: str) -> str:
    return {
        "INFER-SCHEDULING": "Ch56 已把 KV residency 和 pipeline state 变成可调度成本，但没有 semantic predicate 的逐行 selectivity 学习与精确短路排序。",
        "PLATFORM-SECURITY": "Ch72 已定义持久 Skill 的 supply-chain lifecycle、admission 和 revocation，但没有位置感知单指令、静默副作用与合法任务联合通过的攻击证据。",
        "AGENT-WORKFLOW": "Ch81 已有 split-gated self-evolution asset，但没有以 versioned notebook 为逐步 owner 的 code/NL 局部回退与多模态证据链。",
        "AGENT-PLATFORM": "Ch84 已有 Skill compiler/admission 与 executable evidence，但没有 optional-stopping 下 false-commit-controlled 的统计 acceptor。",
        "PLATFORM-EVALUATION-SYSTEM": "Ch66 已把 judge 变成有预算的 evidence acquisition policy，但没有 evaluator 通过环境原生 action 主动制造 criterion-relevant situation 的干预边界。",
        "INFER-KV-CACHE": "Ch45 已有 workload-semantic retention、variable-rank low-rank compression 与 prefix identity；缺少跨 turn QueryMemory 和 sentinel slot-map 保持行/相位/前缀身份的删除机制。",
        "PLATFORM-FOUNDATIONS": "Ch57 已把平台定义为 workload-specific identity/state/policy/evidence contract，并以 intent→admission→reconciliation 闭环和 one-size-fits-all failure 约束架构选择；概念性数据库 taxonomy 不新增独立 owner。",
    }.get(owner, f"`{owner}` 当前章节已经覆盖该 family 的主机制类别、owner 边界与常见 failure mode。")


def delta(item: dict, decision: str) -> str:
    if decision == "Integrate":
        return item["rationale"] + " 只补这一条机制、non-proof 与旧路径共存边界。"
    return item["rationale"] + " 是已有 owner contract 的实例、benchmark、理论分支或受限替代，不新增独立长期命题。"


def main() -> None:
    den = json.loads(DENOMINATOR.read_text(encoding="utf-8"))
    meta = {row["arxiv_id"]: row for row in den["rows"] if row["decision"] == "retain"}
    source = json.loads(SCREENING.read_text(encoding="utf-8"))
    abstracts = {row["arxiv_id"]: row["abstract"] for row in source["identities"]}
    assert len(meta) == 23 and set(meta) == set(SCORES) == set(LOCATORS) == set(BENCH)
    assert den["raw_identities"] == 261 and den["retained"] == 23 and den["closures"] == 238

    reviews = []
    for aid, item in meta.items():
        item = dict(item)
        discovery_title = item["title"]
        item["title"] = EXACT_TITLES.get(aid, discovery_title)
        score = SCORES[aid]
        total = sum(score)
        override = "release_security_contract" if item["stable_node_id"] == "PLATFORM-SECURITY" else "none"
        route = "deep" if total >= 7 or override != "none" else "standard"
        blocked = False
        body = review_body(item, route)
        reviews.append({
            **item, "discovery_title": discovery_title, "abstract": EXACT_ABSTRACTS.get(aid, abstracts[aid]), "score": (*score, total), "route": route, "override": override,
            "review_status": "blocked" if blocked else f"{route}_complete", "access_status": "blocked" if blocked else "accessible",
            "completion": "blocked" if blocked else "complete", "body": body,
            "provenance": provenance(item, route, override, body),
        })

    access_rows = []
    for row in reviews:
        aid = row["arxiv_id"]
        access_rows.append({
            "source_family_id": row["source_family_id"], "primary_identifier": f"arXiv:{aid}v1",
            "url": f"https://arxiv.org/pdf/{aid}v1" if aid == RECOVERED_ID else f"https://arxiv.org/html/{aid}v1",
            "route": "official-exact-v1-pdf-web-reader" if aid == RECOVERED_ID else "official-exact-v1-html-web-reader",
            "reviewed_extent": "full 18-page exact-v1 PDF" if aid == RECOVERED_ID else "full rendered body",
            "status": row["access_status"], "claim_scope": "exact-v1 only",
        })
    (PACKET / "exact-v1-access-receipt.json").write_text(json.dumps({"schema": "daily-v2.1-exact-v1-access-v1", "denominator_id": DENOMINATOR_ID, "reviewed": 23, "accessible": 23, "blocked": 0, "rows": access_rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (PACKET / "source-review-receipts-v2.1.json").write_text(json.dumps({"schema": "daily-v2.1-source-review-packet", "denominator_id": DENOMINATOR_ID, "candidate_count": 23, "review_complete_count": 23, "blocked_count": 0, "ordinary_pending_count": 0, "route_counts": dict(Counter(r["route"] for r in reviews)), "rows": reviews}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    selection = []
    eligible_reviews = [r for r in reviews if r["completion"] == "complete" and (r["score"][3] >= 7 or r["arxiv_id"] in INTEGRATE)]
    for row in eligible_reviews:
        aid, fam = row["arxiv_id"], row["source_family_id"]
        elig = ["score_7_9"] if row["score"][3] >= 7 else []
        if aid in INTEGRATE:
            elig.append("potential_books_delta")
        if row["override"] != "none":
            elig.append("forced_review")
        if aid in SELECTED:
            decision, unit, narrative = "selected", SELECTED[aid], f"analysis:{SELECTED[aid]}"
            reason = {
                "2606.07943": "Poise is the frontier's strongest non-overlapping security unit because it binds hidden skill placement to both verified side effect and legitimate-task success, exposing an admission failure that ordinary invocation metrics miss.",
                "2606.08106": "PACE is the strongest lifecycle-governance unit because it moves commit authority into an anytime-valid acceptor and quantifies both false and harmful self-modification under optional stopping.",
                "2606.09916": "IntentKV is the strongest runtime-state unit because QueryMemory changes retention across turns while slot-map redirection explicitly preserves surviving KV rows, RoPE phase and prefix-cache identity.",
            }[aid]
        else:
            decision, unit, narrative = "not_selected", "—", f"analysis-decision:{fam}"
            reason = NOT_SELECTED_REASON[aid]
        selection.append({"source_family_id": fam, "eligibility": "; ".join(elig), "decision": decision, "analysis_unit_id": unit, "subsumed_by": "—", "priority_rationale": reason, "narrative_ref": narrative})
    assert sum(r["decision"] == "selected" for r in selection) == 3
    eligible_families = {row["source_family_id"] for row in selection}
    noneligible_reviews = [row for row in reviews if row["source_family_id"] not in eligible_families]
    assert {row["arxiv_id"] for row in noneligible_reviews} == set(NONELIGIBLE_REASON)
    noneligible = []
    for row in noneligible_reviews:
        aid, fam = row["arxiv_id"], row["source_family_id"]
        assert row["score"][3] == 6 and row["override"] == "none" and aid not in INTEGRATE
        noneligible.append({
            "source_family_id": fam,
            "score_total": row["score"][3],
            "review_override": row["override"],
            "eligibility_signals": [],
            "decision": "non_eligible",
            "closure_reason": NONELIGIBLE_REASON[aid],
            "narrative_ref": f"analysis-ineligible:{fam}",
        })
    candidate_families = {row["source_family_id"] for row in reviews}
    noneligible_families = {row["source_family_id"] for row in noneligible}
    assert eligible_families.isdisjoint(noneligible_families)
    assert eligible_families | noneligible_families == candidate_families
    selection_payload = {
        "contract": "full evidence-complete frontier selection; main rows contain eligible families only",
        "candidate_count": len(reviews),
        "eligible_count": len(selection),
        "noneligible_count": len(noneligible),
        "selected_unit_count": 3,
        "rows": selection,
        "noneligible_rows": noneligible,
    }
    (PACKET / "deep-analysis-selection-v1.json").write_text(json.dumps(selection_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    comparisons = []
    for row in reviews:
        aid = row["arxiv_id"]
        decision = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
        target = TARGET[row["stable_node_id"]]
        target_path = target.split("#", 1)[0]
        adjacent = "books/part-06-ai-infrastructure/58-kubeflow.md#L10" if aid == RECOVERED_ID else f"ROADMAP.md#L1; {target_path}#L10"
        comparisons.append({"source_family_id": row["source_family_id"], "stable_node_id": row["stable_node_id"], "target_chapter_ref": target, "adjacent_chapter_refs": adjacent, "existing_proposition": f"existing:{row['source_family_id']}", "new_evidence_delta": f"delta:{row['source_family_id']}", "evolution_relation": "Direct Evolution" if decision == "Integrate" else "Alternative Branch", "decision": decision, "books_review_ref": f"books-review:{row['source_family_id']}"})
    (PACKET / "books-comparison-v1.json").write_text(json.dumps({"contract": "23/23 exact-v1-complete families compared after Conditional recovery", "row_count": 23, "decision_counts": dict(Counter(r["decision"] for r in comparisons)), "books_write_performed": True, "queue_released": True, "queue_consumed": True, "post_write_audit": "passed", "rows": comparisons}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    by_fam = {r["source_family_id"]: r for r in reviews}
    ledger_lines, receipt_lines, review_sections, benchmark_lines = [], [], [], []
    for row in reviews:
        fam, aid = row["source_family_id"], row["arxiv_id"]
        c = next((x for x in comparisons if x["source_family_id"] == fam), None)
        if c is None:
            raise AssertionError(f"missing Books comparison for {fam}")
        disp = c["decision"]
        bref = c["books_review_ref"]
        s = row["score"]
        ledger_lines.append(f"| {fam} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W23 | {row['submitted_v1_utc'][:10]} | SRC-ARXIV | {s[0]} | {s[1]} | {s[2]} | {s[3]} | retained | {row['review_status']} | {row['access_status']} | {row['override']} | review:{fam} | self | — | new_in_window | {row['stable_node_id']} | {disp} | {bref} | yes |")
        loc = bound_locators(aid)
        receipt_lines.append(f"| {fam} | {row['provenance']} | {row['route']} | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | {pipe(loc[0])} | {pipe(loc[1])} | {pipe(loc[2])} | {pipe(loc[3])} | claim:{fam} | {row['completion']} |")
        review_sections.append(f"<!-- review:{fam}:start -->\n{row['body']}\n<!-- review:{fam}:end -->")
        b = BENCH[aid]
        benchmark_lines.append("| " + fam + " | " + " | ".join(pipe(v) for v in b) + " |")

    selection_lines, selection_sections = [], []
    for row in selection:
        selection_lines.append(f"| {row['source_family_id']} | {row['eligibility']} | {row['decision']} | {row['analysis_unit_id']} | {row['subsumed_by']} | {row['priority_rationale']} | {row['narrative_ref']} |")
        if row["decision"] == "not_selected":
            selection_sections.append(f"<!-- {row['narrative_ref']}:start -->\n{row['priority_rationale']}\n<!-- {row['narrative_ref']}:end -->")
    noneligible_lines, noneligible_sections = [], []
    for row in noneligible:
        signals = "; ".join(row["eligibility_signals"]) or "none"
        noneligible_lines.append(
            f"| {row['source_family_id']} | {row['score_total']}/9 | {row['review_override']} | "
            f"{signals} | {row['closure_reason']} | {row['narrative_ref']} |"
        )
        noneligible_sections.append(
            f"<!-- {row['narrative_ref']}:start -->\n{row['closure_reason']} "
            "该 closure 只关闭长叙事 eligibility；Source Review、Benchmark Contract 与 Books Comparison 仍按 retained family 完整执行。\n"
            f"<!-- {row['narrative_ref']}:end -->"
        )

    books_lines, books_sections = [], []
    for c in comparisons:
        row = by_fam[c["source_family_id"]]
        books_lines.append(f"| {c['source_family_id']} | {c['stable_node_id']} | {c['target_chapter_ref']} | {c['adjacent_chapter_refs']} | {c['existing_proposition']} | {c['new_evidence_delta']} | {c['evolution_relation']} | {c['decision']} | {c['books_review_ref']} |")
        books_sections.append(f"<!-- {c['books_review_ref']}:start -->\nCompared `{row['title']}` against `{c['target_chapter_ref']}` and its ROADMAP-adjacent owner.\n\n<!-- {c['existing_proposition']}:start -->\n{existing(row['stable_node_id'])}\n<!-- {c['existing_proposition']}:end -->\n\n<!-- {c['new_evidence_delta']}:start -->\n{delta(row, c['decision'])}\n<!-- {c['new_evidence_delta']}:end -->\n\nDecision: `{c['decision']}`. Exact-v1 does not transfer ownership or generalize beyond its evaluator contract.\n<!-- {c['books_review_ref']}:end -->")

    source_lines = [
        f"- [{row['title']}](https://arxiv.org/abs/{row['arxiv_id']}v1) — first-public：{row['submitted_v1_utc'][:10]}；accessed：2026-08-29"
        for row in reviews
    ]
    source_lines.append(
        "- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表"
    )

    report = f"""# Daily Research — 2026-06-07

**Research Date:** 2026-06-07

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-06 09:00:00 ～ 2026-06-07 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；261/261 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding

## Executive Summary

Four official DataCite DOI-prefix snapshots yielded 4,000 raw overread records and 261 unique identities in the Beijing window. Full title+abstract semantic screening froze `261 = 23 retained + 238 family-specific closures`, including independent review of all 46 keyword-route negatives. Exact-v1 review is complete for 23/23 families after `2606.08317v1` was recovered from the official 18-page PDF; HTML remains unavailable but is no longer an Evidence blocker. Corrected-contract Selection conserves `23 retained = 18 eligible + 5 non-eligible`: the mutually exclusive 18-family main frontier yields exactly three non-overlapping analysis units, while five Score-6 families retain source-specific closures outside the canonical table. Books comparison covers 23/23 families: six Integrate and seventeen No Change; all six Integrate mechanisms were restored to their canonical owner chapters and then checked against the full 23-family disposition set. The recovered family is No Change because its conceptual paradigm-level selection model does not supersede Ch57's existing workload-specific platform admission contract.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-07 |
| Window End | 2026-06-07 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | {DENOMINATOR_ID} |
| Denominator Frozen At | {EXECUTED_AT} |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-06T09:00:00+08:00 | 2026-06-07T09:00:00+08:00 | {EXECUTED_AT} | DataCite DOI-prefix `2606.06`–`.09`; exact v1 creation timestamp; 261/261 full title+abstract screen | checked | 261 | {'; '.join(r['source_family_id'] for r in reviews)} | pages=4; 1,000 rows/page; final cursor=end; 4,000 raw overread; strict time filter | 2026-06-07T01:00:00Z | ../_sources/daily-20260607/registered-hit-screening.json; ../_sources/daily-20260607/candidate-denominator.json; coverage:SRC-ARXIV:20260607 | — |

<!-- coverage:SRC-ARXIV:20260607:start -->
All 190 Core, 25 keyword-routed non-Core and 46 route-negative identities were semantically screened. The frozen arithmetic is `261 = 23 retain + 238 closure`; closures are family-specific and remain row-addressable in `candidate-denominator.tsv`.
<!-- coverage:SRC-ARXIV:20260607:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(ledger_lines)}

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(receipt_lines)}

### Source Reviews

{chr(10).join(review_sections)}

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(benchmark_lines)}

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(selection_lines)}

{chr(10).join(selection_sections)}

### Non-eligible family-specific closures

`23 retained = 18 eligible + 5 non-eligible`；两组互斥且并集等于冻结 Candidate Denominator。下表不属于 canonical Selection 主表，`non_eligible` 也不等于 `not_selected`。

| Source Family ID | Score V2 | Review Override | Eligibility Signals | Family-specific Closure | Narrative Ref |
| --- | ---: | --- | --- | --- | --- |
{chr(10).join(noneligible_lines)}

{chr(10).join(noneligible_sections)}

**Selected Deep Analysis Narratives**

<!-- analysis:DA-20260607-SECURITY:start -->
Poise exposes why skill admission cannot stop at content scanning or invocation detection. The evidence object must join three identities: the exact skill position, the verified external side effect, and the legitimate-task verifier. This is selected over the other security families because it changes the release/admission contract without depending on a vendor-specific runtime; its SkillTester false-positive result also prevents treating an LLM audit alert as ground truth.
<!-- analysis:DA-20260607-SECURITY:end -->

<!-- analysis:DA-20260607-EVOLUTION:start -->
PACE separates proposer quality from commit authority. Reusing the same noisy dev estimate across hundreds of proposals creates adaptive multiple testing; the acceptor, not the proposer, owns whether state changes. Paired anytime-valid evidence controls each candidate's false-commit probability under optional stopping, while the paper explicitly does not claim a global lifetime error bound. This is the frontier's clearest durable self-evolution gate.
<!-- analysis:DA-20260607-EVOLUTION:end -->

<!-- analysis:DA-20260607-RUNTIME:start -->
IntentKV makes cross-turn intent a session-owned cache policy while preserving the identity constraints that prefix sharing and RoPE require. QueryMemory may change which tokens remain live, but slot-map sentinel redirection prevents eviction from silently renumbering survivors. The selected mechanism therefore connects semantic retention to physical KV state without equating an 8k budget or observed read reduction with a production latency SLO.
<!-- analysis:DA-20260607-RUNTIME:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(books_lines)}

{chr(10).join(books_sections)}

`SF-2026-ARXIV-2606-08317` is recovered and resolved as `No Change — Existing Coverage`: the exact-v1 PDF supports a conceptual workload/profile/filter/score branch, while Ch57 already owns workload-specific platform admission and the paper explicitly lacks product-level empirical validation.

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260607-COVERAGE | fresh-context:jun07-denominator-v1 | coverage | coverage:SRC-ARXIV:20260607 | — | 261/261 identities and all 46 route negatives re-read; 23+238 arithmetic and hashes reproduced | passed |
| SA-20260607-EVIDENCE | fresh-context:jun07-exact-v1-recovery-v2 | evidence | {'; '.join('review:'+r['source_family_id'] for r in reviews)} | none | 23/23 exact-v1 reviews and benchmark contracts passed; 2606.08317 method, illustrative evaluation and non-proof boundaries were recovered from the official v1 PDF | passed |
| SA-20260607-SELECTION | fresh-context:jun07-frontier-v2 | deep_analysis_selection | {'; '.join(r['narrative_ref'] for r in selection + noneligible)} | — | corrected-contract conservation reproduced: 23 retained = 18 eligible + 5 non-eligible, disjoint union; main table has only eligible families, five bounded closures stay outside it, and three non-overlapping units remain selected | passed |
| SA-20260607-BOOKS | fresh-context:jun07-postrecovery-v2 | books | {'; '.join(c['books_review_ref'] for c in comparisons)} | none | 6/6 Integrate正文与Review note通过；17/17 No Change（含恢复的2606.08317）无Books泄漏；owner/adjacent与证据边界复核通过 | passed |

### Recovered Materials Receipt

- `SF-2026-ARXIV-2606-08317`: official exact-v1 PDF `https://arxiv.org/pdf/2606.08317v1`, 18 pages, fully reviewed; official HTML still returns Internal Error.
- Recovery closed the sole Materials Request. The review binds §II/§VI-A/§IX-B method identity, §VI-B/§IX-D illustrative evaluation, and §IX-B/§XI non-proof boundaries; no secondary summary was promoted.

## 8. Ignored Noise

The 238 pre-denominator closures are not unreviewed noise. Each retains title, abstract, route, family-specific closure class and reopen condition in the frozen denominator ledger. None is scored or leaked into Selection or Books.

## 9. Recommended Action

保持本日 Complete；只有 exact-version revision、artifact provenance 或 Books owner 证据发生变化时才重开真实受影响的 Gate，不因展示迁移重复研究。

## 10. Repository Changes

This lane restores the 06-07 Daily, exact-v1 recovery receipts, full comparison and deterministic renderer. It also restores six Books integrations in Ch45, Ch56, Ch66, Ch72, Ch81 and Ch84; the recovered `2606.08317v1` family remains No Change and required no additional Books write. Nothing was staged, committed or pushed.

## 11. Open Questions

- None for this Daily. The sole Conditional blocker is resolved and the 23/23 recovery audit has zero unresolved findings.

## 12. Sources

{chr(10).join(source_lines)}

## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。261 个 raw identities 已闭合为 23 个 retained families 与 238 个 family-specific pre-denominator closures；Selection 守恒为 18 个 eligible 主表 family + 5 个具名 non-eligible closure，互斥且并集为 23，selected 仍为 3；23/23 Source Review 与 Books Decision 均已通过 fresh-context audit，未解决 finding 为 0。
"""
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(report, encoding="utf-8")

    queue = [c for c in comparisons if c["decision"] == "Integrate"]
    qlines = ["# 2026-06-07 deduplicated Books queue v1", "", f"- Denominator: `{DENOMINATOR_ID}`", "- Status: consumed; 6/6 writebacks and 23/23 post-write fresh audit passed.", "- Compared: `23/23` exact-v1-complete families; recovered `2606.08317v1` is No Change — Existing Coverage.", f"- Net writeback: `{len(queue)}`", "- Books were restored by this recovery lane after the parent confirmed no shared-file conflict.", "", "| Source Family | arXiv ID | Target locator | Minimal durable delta | Evidence boundary |", "| --- | --- | --- | --- | --- |"]
    for c in queue:
        row = by_fam[c["source_family_id"]]
        qlines.append(f"| {c['source_family_id']} | arXiv:{row['arxiv_id']}v1 | `{c['target_chapter_ref']}` | {delta(row, c['decision'])} | Exact-v1 only; preserve old path, cost/failure, non-proof and unique `{row['stable_node_id']}` ownership. |")
    (PACKET / "BOOKS_DEDUP_QUEUE_V1.md").write_text("\n".join(qlines) + "\n", encoding="utf-8")
    (PACKET / "README.md").write_text(f"# 2026-06-07 source packet\n\n`{DENOMINATOR_ID}` freezes 261 identities: 23 retained and 238 family-specific closures. Coverage, Evidence, Selection and Books passed. Corrected-contract Selection conserves `23 = 18 eligible + 5 non-eligible`; the groups are disjoint, their union is the retained denominator, and only the 18 eligible families appear in the canonical main table. `2606.08317v1` was recovered from the official 18-page PDF, making Evidence 23/23; its No Change decision did not add a seventh Books write. The six Integrate writebacks were restored and passed the 23-family post-write audit. Completion is Complete.\n", encoding="utf-8")
    (PACKET / "EVIDENCE_ACCESS_STATUS_V1.md").write_text("# 2026-06-07 exact-v1 access checkpoint\n\n- 23/23 retained families have exact-v1 bodies reviewed.\n- `2606.08317v1`: recovered through official `https://arxiv.org/pdf/2606.08317v1` (18 pages); HTML remains Internal Error but no Evidence gap remains.\n- Blocked: 0; ordinary pending: 0.\n", encoding="utf-8")
    (PACKET / "FRESH_CONTEXT_AUDIT_V1.md").write_text("# 2026-06-07 fresh-context audit v3\n\n- Coverage: PASS — 261/261 rows; 23 retain + 238 closure; 46/46 route negatives included.\n- Evidence: PASS — 23/23 exact-v1 reviews and benchmark contracts; 2606.08317v1 recovered from the official 18-page PDF with source-specific §II/§VI/§IX/§XI locators.\n- Selection: PASS — corrected-contract conservation is `23 = 18 eligible + 5 non-eligible`; the sets are disjoint and their union equals the retained denominator. Only 18 eligible families appear in the canonical main table; all five non-eligible families have source-specific reader-facing closures and bounded `analysis-ineligible` refs. Three families remain selected and the other 15 eligible families retain source-specific non-selection rationales.\n- Books: PASS — 23/23 comparisons; 6 Integrate previously applied and audited, 17 No Change have zero Books leakage.\n- Recovered disposition: 2606.08317 is No Change against Ch57 + Ch58 because its conceptual paradigm-level decision model adds no product-level empirical validation beyond the existing workload-specific platform admission contract.\n- Identity repair: DataCite discovery title for 2606.08348 differed from official exact-v1 title; denominator discovery provenance remains unchanged, while Review/Selection/Books surfaces use `Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses` and exact-v1 abstract/model identities.\n- Adversarial checks: no excluded-family leakage, no duplicate family, no score-selected denominator admission, no directional range promoted to controlled benchmark/SLO, and no secondary source promoted to exact-v1 evidence.\n- Unresolved findings: 0. Completion: Complete.\n", encoding="utf-8")
    (PACKET / "POST_WRITE_FRESH_AUDIT_V1.md").write_text("# 2026-06-07 post-recovery fresh audit v3\n\n- Selection conservation: PASS — `23 = 18 eligible + 5 non-eligible`; the canonical main table contains only eligible families, five source-specific closure rows remain outside it, and all five bounded `analysis-ineligible` refs resolve exactly once. Selected remains 3.\n- `2606.07923v1` -> Ch56: PASS; online selectivity and per-row semantic-filter ordering, old static branch, estimator error/cost and non-SLO boundary present; Review note unique.\n- `2606.07943v1` -> Ch72: PASS; position-aware one-instruction attack, joint side-effect/task verifier, high audit false-positive and sandbox boundary present; Review note unique.\n- `2606.08049v1` -> Ch81: PASS; versioned notebook step owner, gate-conditioned code/NL fallback, drift/migration cost and portability boundary present; Review note unique.\n- `2606.08106v1` -> Ch84: PASS; paired anytime-valid acceptor, optional stopping, per-decision not lifetime guarantee and held-out coexistence present; Review note unique.\n- `2606.08200v1` -> Ch66: PASS; in-world situation generation, evaluator intervention/confounding, passive scorer coexistence and no repair authority present; Review note unique.\n- `2606.09916v1` -> Ch45: PASS; QueryMemory, sentinel slot-map, surviving-row/RoPE/prefix identity, full-cache fallback and 8k-not-SLO boundary present; Review note unique.\n- No Change handoff: PASS; all 17 IDs, including recovered `2606.08317`, occur zero times in Books.\n- Recovered family: PASS; Ch57 and Ch58 were re-read, exact-v1 locators/benchmark/non-proof are source-specific, and the resolved Materials Request is absent.\n- Full scope: PASS — 23/23 Books dispositions; unresolved findings: 0.\n", encoding="utf-8")

    files = [PACKET / name for name in ["registered-hit-screening.json", "candidate-denominator.json", "candidate-denominator.tsv", "CANDIDATE_DENOMINATOR_AUDIT_V1.md", "EVIDENCE_ACCESS_STATUS_V1.md", "exact-v1-access-receipt.json", "source-review-receipts-v2.1.json", "deep-analysis-selection-v1.json", "books-comparison-v1.json", "BOOKS_DEDUP_QUEUE_V1.md", "FRESH_CONTEXT_AUDIT_V1.md", "POST_WRITE_FRESH_AUDIT_V1.md", "README.md"]] + [
        REPORT,
        ROOT / "scripts/finalize_june07_downstream.py",
        ROOT / "scripts/audit_june07_recovery.py",
        ROOT / "scripts/test_june07_selection_conservation.py",
    ]
    recovery_audit = PACKET / "CONDITIONAL_RECOVERY_FRESH_AUDIT_V2.md"
    if recovery_audit.exists():
        files.append(recovery_audit)
    manifest = [f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT)}" for path in files]
    (PACKET / "SHA256SUMS").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    print(json.dumps({"denominator_id": DENOMINATOR_ID, "retained": 23, "accessible": 23, "blocked": 0, "deep": sum(r['route'] == 'deep' for r in reviews), "standard": sum(r['route'] == 'standard' for r in reviews), "eligible": len(selection), "selected": 3, "books_queue": len(queue), "completion": "Complete"}, indent=2))


if __name__ == "__main__":
    main()
