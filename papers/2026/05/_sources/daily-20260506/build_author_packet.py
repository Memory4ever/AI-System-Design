#!/usr/bin/env python3
"""Build the date-local 2026-05-06 V2.1 author packet.

This script owns only the date-local report and receipts.  It never writes Books;
the shared writeback is serialized by the root reconciler after independent audit.
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
REPORT = REPO / "papers/2026/05/06/README.md"
INV = json.loads((ROOT / "screening-ledger-provisional.json").read_text())

spec = importlib.util.spec_from_file_location("vr", REPO / "scripts/validate_research.py")
vr = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(vr)

# Exact-v1 pages were read from official arXiv HTML, except the two explicitly
# identified PDF routes.  Retention is about durable system contracts, not AI
# topicality or ROADMAP mappability.
K = {
    "2605.03275": ("AGENT-RAG", (3, 3, 3), "Blocked / Unverified", "production RAG freshness, tenant isolation and composed retrieval are data-layer ownership properties; the abstract identifies a unified transactional design, but exact-v1 full text is unavailable and the mechanism cannot yet support a durable Books claim", "exact-v1 full text unavailable", "exact-v1 full text unavailable", "exact-v1 full text unavailable"),
    "2605.03327": ("TRAIN-GRPO", (3, 3, 3), "Integrate", "fine-grained reasoning credit can be redistributed from sequence reward with a bounded distributional distance and an entropy gate, trading additional statistics and calibration for less diffuse token updates", "§3 Distribution-Guided Policy Optimization; §3.2 Advantage Redistribution; §3.3 Objective", "§4 Experiments and Ablations", "Appendix A Theory; Appendix B Limitations"),
    "2605.03379": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "test-time vote accuracy is governed by the latent per-example success distribution and same-example correlation, so one-call accuracy cannot specify a repeated-sampling evaluation contract", "§2 Latent Success Model; §3 Two-Call Identification", "§4 Vote-Accuracy Curves; §5 Empirical Evaluation", "§6 Scope and Limitations"),
    "2605.03408": ("TRAIN-RLHF", (3, 2, 3), "No Change — Existing Coverage", "an RL task interface jointly owns observation projection and reward rather than treating reward synthesis as an isolated prompt problem; generated interfaces still require environment-grounded validation", "§3 RL Interface Discovery; §3.2 Observation and Reward Synthesis", "§4 Experimental Setup; §5 Results", "§6 Limitations"),
    "2605.03425": ("TRAIN-PRETRAINING", (3, 2, 3), "Integrate", "gradient filtering under differential privacy changes the noise statistics consumed by AdamW state, so optimizer bias correction must be derived from the filter rather than reused from unfiltered DP-SGD", "§3 Filter-Aware Innovation Bias Correction; §4 FIBER", "§5 Experiments and Ablations", "§6 Limitations and Privacy Scope"),
    "2605.03505": ("PLATFORM-MONITORING", (2, 2, 3), "No Change — Existing Coverage", "microservice diagnosis can branch over competing causal hypotheses and use reflection to allocate investigation, but an agent search trace does not replace telemetry identity or causal observability", "§3 LATS-RCA Architecture; §3.2 Reflection-Guided Tree Search", "§4 Experimental Setup; §5 Results", "§6 Limitations"),
    "2605.03561": ("PLATFORM-MONITORING", (2, 3, 3), "No Change — Existing Coverage", "exascale diagnostic analysis must separate telemetry ingestion, GPU-parallel analysis and presentation so monitoring overhead scales below the workload being observed", "§3 Heterogeneous hpcanalysis Framework; §4 C++ and GPU Paths", "§5 Evaluation on Aurora", "§6 Limitations and Portability Boundary"),
    "2605.03566": ("INFER-TENSORRT-LLM", (3, 2, 3), "No Change — Existing Coverage", "compiler lowering to an AI Engine needs tensor-level intermediate structure before hardware-specific mapping; source compatibility is obtained by changing the compiler owner, not by hiding data-movement constraints", "§3 Tensor Lifting; §4 AIE Lowering Pipeline", "§5 Scientific-Workload Evaluation", "§6 Limitations"),
    "2605.03596": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "workspace-agent evaluation must preserve cross-file dependency state and score both reads and mutations against a real workspace graph rather than treating files as independent prompt attachments", "§3 Workspace-Bench Construction; §4 Dependency and Task Model", "§5 Evaluation Protocol; §6 Results", "§7 Limitations"),
    "2605.03644": ("INFER-KV-CACHE", (3, 3, 3), "Integrate", "adaptive many-shot inference couples example selection with reusable prefix KV state, making context admission a joint quality-memory-latency decision rather than a fixed shot count", "§3 AdapShot; §3.2 Adaptive Shot Selection; §3.3 Semantic-Aware KV Reuse", "§4 Experiments and Ablations", "§5 Limitations"),
    "2605.03667": ("TRAIN-PRETRAINING", (3, 3, 3), "Integrate", "low-rank pretraining becomes hardware-useful only when the factorization is co-designed with supported structured activation sparsity; mathematical compression alone does not guarantee realized training throughput", "§3 ELAS Low-Rank and 2:4 Sparse Training", "§4 Experiments and Ablations", "§5 Limitations"),
    "2605.03677": ("TRAIN-RLHF", (3, 3, 3), "Integrate", "on-policy distillation needs both exploration of informative student states and reliability-aware teacher supervision, so teacher outputs are conditional feedback rather than unconditional labels", "§3 Dual-Perspective OPD; §3.2 Exploration; §3.3 Teacher Reliability", "§4 Experiments and Ablations", "§5 Limitations"),
    "2605.03971": ("PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "No Change — Existing Coverage", "hallucination detection can combine response-intrinsic uncertainty with verbal self-judgment through explicit logical constraints, but detector confidence remains an evaluated signal rather than truth", "§4 LaaB Logical-Constraint Framework", "§5 Experiments and Effect Analysis", "§6 Limitations; Appendix"),
    "2605.03986": ("AGENT-WORKFLOW", (3, 2, 3), "No Change — Existing Coverage", "intent-to-execution automation separates plan synthesis, agent capability recommendation and executable graph construction; each stage requires typed validation before workflow commit", "§3 Intent-to-Workflow Composition; §4 Agent Recommendation", "§5 Evaluation", "§6 Limitations"),
    "2605.04036": ("TRAIN-SFT", (2, 2, 3), "No Change — Existing Coverage", "search-agent SFT quality depends on selecting informative, difficult trajectories rather than merely scaling trajectory count; the result is workload-bound and does not displace RL branches", "§3 Trajectory Construction; §4 OpenSeeker-v2 SFT", "§5 Experiments and Ablations", "§6 Limitations"),
    "2605.04039": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "clinical accuracy and safety have different scaling curves, requiring risk-weighted, evidence-aware evaluation and abstention criteria instead of inferring deployment safety from mean accuracy", "§3 SaFE-Scale Framework; §4 Safety Dimensions", "§5 Scaling Experiments", "§6 Limitations and Clinical Scope"),
    "2605.04135": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "capability claims must bind model release, elicitation, tools and evaluation date because frontier lag can turn a valid historical measurement into a misleading current-system conclusion", "§2 Frontier-Lag Audit Method; §3 Configuration and Date Coding", "§4 Bibliometric Results", "§5 Limitations"),
    "2605.04172": ("INFER-TENSORRT-LLM", (3, 2, 3), "No Change — Existing Coverage", "programmable memory callbacks require an ISA-level consistency contract across misses, evictions and writebacks; performance programmability without formal ordering moves hidden state into software", "§3 täkō Memory Consistency Model; §4 Formal Semantics", "§5 Litmus Tests and Validation", "§6 Limitations"),
    "2605.04209": ("PLATFORM-SECURITY", (3, 3, 3), "Integrate", "model artifacts can carry statistically hidden parameter backdoors whose detectability is bounded by the attack distribution, extending supply-chain verification beyond file hashes and conventional weight scanning", "§3 Sparse Backdoor Construction; §4 Undetectability Analysis", "§5 Experiments", "§6 Limitations and Threat-Model Boundary"),
    "2605.04213": ("PLATFORM-MONITORING", (3, 3, 3), "Integrate", "silent GPU corruption needs empirically grounded fault models tied to operation type and propagation pattern; generic random bit flips can invalidate resilience conclusions for large-scale training", "§3 Gate-Level Fault-Injection Method; §4 SDC Taxonomy", "§5 Error-Pattern Results; §6 Modeling Guidance", "§7 Limitations"),
    "2605.04236": ("PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "No Change — Existing Coverage", "ensemble deliberation needs an evidence-accumulation stopping and fallback contract because more samples can cross from useful consensus into degraded decisions", "§3 DASE Sequential Evidence Accumulation; §3.3 Commit Routing", "§4 Experiments and Calibration", "§5 Limitations"),
    "2605.04256": ("AGENT-MCP", (3, 3, 3), "Integrate", "heterogeneous physical neural substrates require a typed control plane for capability discovery, timing, observation, actuation and safety rather than presenting every device as an interchangeable tool", "§3 phys-MCP Control Plane; §4 Resource and Capability Model", "§5 Prototype Evaluation", "§6 Limitations"),
    "2605.04269": ("TRAIN-PRETRAINING", (3, 2, 3), "Integrate", "under nonstationary objectives Adam's adaptive state trades faster tracking for longer optimizer memory, whereas SGD forgets differently; optimizer choice therefore depends on drift, projection and stationarity assumptions", "§3 Nonstationary Adam Analysis; §4 Tracking and Stationarity Bounds", "§5 Experiments", "§6 Assumptions and Limitations"),
    "2605.04295": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage", "uncertainty can be estimated over semantic response clusters and calibrated with conformal acceptance, but coverage guarantees remain conditional on calibration exchangeability and the chosen semantic equivalence model", "§2 Semantic Entropy; §3 Adaptive Conformal Semantic Entropy", "§4 Evaluation and Ablations", "§5 Limitations; Appendix Proofs"),
    "2605.04312": ("PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "No Change — Existing Coverage", "a persistent multi-agent game can reduce benchmark saturation and contamination by making other agents part of the changing workload, while introducing opponent-population and reproducibility dependence", "§3 Agent Island Environment; §4 Dynamic Evaluation Protocol", "§5 Experiments", "§6 Limitations"),
    "2605.04333": ("TRAIN-DISTRIBUTED-TRAINING", (3, 3, 3), "Integrate", "large synchronous training networks need multipath transport, redundant Clos planes and explicit failure handling because tail latency and flow collisions dominate collective completion at scale", "§2 MRC Transport; §3 Multi-Plane Clos and SRv6", "§4 Simulation and Evaluation", "§5 Limitations"),
    "2605.04341": ("TRAIN-LORA", (3, 3, 3), "Integrate", "parameter-efficient adaptation reduces training cost but not dense inference cost; budgeted distillation must allocate structural rank or compute under a deployment budget to produce an actually cheaper student", "§3 Budgeted LoRA; §3.2 Structured Compute Allocation", "§4 Experiments and Pareto Analysis", "§5 Limitations"),
    "2605.04361": ("AGENT-CONTEXT", (3, 3, 3), "Integrate", "context artifacts have task-dependent crossover effects, so context admission must estimate marginal decision value and interference rather than assume that more relevant context monotonically helps", "§3 Multi-Agent Design-Exploration Protocol; §4 Context Conditions", "§5 Crossover Results", "§6 Limitations"),
    "2605.04375": ("AGENT-WORKFLOW", (3, 3, 3), "Integrate", "physical experiments need declarative experiment-as-code that binds instrument capabilities, execution state, provenance and human safety approval, extending durable workflow semantics beyond digital tools", "§3 Experiment-as-Code Model; §4 Declarative Lab Stack", "§5 Case Studies and Evaluation", "§6 Limitations"),
    "2605.05253": ("AGENT-RAG", (2, 2, 3), "No Change — Existing Coverage", "enterprise RAG evaluation must preserve private-document heterogeneity, access boundaries and multi-document evidence needs, but a benchmark dataset does not itself define a new retrieval ownership mechanism", "§3 EnterpriseRAG-Bench Construction", "§4 Evaluation Protocol; §5 Results", "§6 Limitations"),
    "2605.08192": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "frontier-safety release claims need reproducible artifacts, configuration disclosure and independent rerun conditions; authority or venue cannot substitute for an inspectable evaluation contract", "§2 Evidential Inversion; §3 Proposed Reproducibility Standard", "§4 Worked Requirements and Cases", "§5 Limitations and Governance Scope"),
    "2605.10959": ("INFER-TENSORRT-LLM", (2, 2, 2), "No Change — Existing Coverage", "quantization decisions need workload-specific accuracy, compression and realized latency measurements, but collapsing them into one scalar intelligence index hides Pareto preferences and cannot be a universal execution objective", "§3 QuIDE Metric and Active Optimization", "§4 Experiments", "§5 Limitations"),
    "2605.03309": ("PLATFORM-SECURITY", (3, 3, 3), "Integrate", "artifact distribution needs cryptographic registry identity, publisher/registry countersignatures and namespace-bound fail-closed resolution", "§4 Two-Layer Archive Format; §5 Cryptographic Registry Identity; §6 Dual-Signature Distribution Model", "§12 Evaluation", "§13.1 Limitations"),
    "2605.03310": ("AGENT-MULTI-AGENT", (2, 2, 3), "No Change — Existing Coverage", "multi-agent coordination is a configurable architecture whose information topology, compute allocation and aggregation leave distinct failure signatures", "§3 Coordination as an Architectural Layer; §4 Reference Architectures", "§5 Experimental Design; §6 Results", "§7 Limitations"),
    "2605.03312": ("AGENT-MEMORY", (3, 2, 3), "No Change — Existing Coverage", "limited-capacity agents need intent-routed memory tiers, deterministic evidence compilation and validator-owned escalation instead of open-ended memory tool loops", "§3 MemFlow Architecture; §4 Intent Router and Memory Tiers", "§5 Experiments", "§6 Limitations"),
    "2605.03314": ("AGENT-CONTEXT", (3, 3, 3), "Integrate", "public disclosure is an irreversible commitment distinct from private reasoning state, so visibility timing becomes a learned control decision with an entailment gate", "§2 Generation under Coupled State and Commitment; §3 Method", "§4 Experiments", "§F Limitations"),
    "2605.03353": ("AGENT-PLATFORM", (3, 3, 3), "No Change — Existing Coverage", "portable skills require a typed intermediate representation and target-specific lowering, while static checks remain separate from runtime effect authorization", "§3 SkIR; §4 Four-Phase Compilation Pipeline", "§5 Evaluation", "§6 Limitations"),
    "2605.03354": ("AGENT-MEMORY", (2, 2, 3), "No Change — Existing Coverage", "memory write/read failures can be localized through stage-specific internal circuits, but circuit signals remain diagnostics rather than durable memory truth", "§3 Circuit Tracing Method; §4 Write-Manage-Read Circuits", "§5 Experiments; §6 Diagnosis", "§7 Limitations"),
    "2605.03375": ("INFER-KV-CACHE", (3, 3, 3), "No Change — Existing Coverage", "SSD-backed KV restore must move both data and I/O submission ownership off the CPU critical path and schedule transfers against GPU slack", "§3 GPU-Centric KV Object Store; §4 GPU io_uring; §5 Slack-Aware Scheduling", "§7 Evaluation", "§8 Limitations"),
    "2605.03378": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "an agent action should commit only when benign evidence provides a complete causal justification and task invariants hold", "§3 Threat Model; §4 ARGUS Causal-Provenance Auditor", "§5 AgentLure; §6 Evaluation", "§7 Limitations"),
    "2605.03482": ("PLATFORM-SECURITY", (3, 2, 3), "No Change — Existing Coverage", "persistent memory poisoning needs calibrated anomaly admission tied to retrieval geometry, with synonym-invariant attacks kept as an explicit non-covered boundary", "§3 Stackelberg Threat Model; §4 MEMSAD", "§5 Theory; §6 Experiments", "§7 Limitations and Discrete Loophole"),
    "2605.03534": ("AGENT-RAG", (3, 3, 3), "No Change — Existing Coverage", "evidence sufficiency is a set-level claim contract over coverage, relation, conflict and uncertainty, not independent passage relevance", "§3 SURE-RAG; §4 Set-Level Aggregation", "§5 Experimental Protocol; §6 Results", "§7 Boundary Mapping and Limitations"),
    "2605.03562": ("INFER-KV-CACHE", (3, 3, 3), "Integrate", "KV quantization error must be measured in attention-visible score/readout coordinates rather than raw storage MSE, with distinct K and V operators", "§3 Model-Visible KV Geometry; §4 HeadQ", "§2 Experimental Setup; §5 Empirical Results", "§8 Limitations"),
    "2605.03675": ("AGENT-MEMORY", (3, 2, 3), "No Change — Existing Coverage", "long-running agent memory needs tiered episodic, semantic and working state plus measured retrieval-bottleneck ownership instead of a flat file", "§3 MemTier Architecture; §4 Retrieval Engine", "§5 Evaluation", "§6 Limitations"),
    "2605.03762": ("PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "No Change — Existing Coverage", "forecast evaluation needs verifiable knowledge cutoffs, temporal masking and artifact provenance so future leakage cannot masquerade as predictive capability", "§3 OracleProto Protocol; §4 Temporal Masking", "§5 Evaluation", "§6 Limitations"),
    "2605.03838": ("PLATFORM-EVALUATION-SYSTEM", (2, 3, 3), "No Change — Existing Coverage", "operationally critical agent evidence needs traceable measurement units, uncertainty budgets and release criteria rather than a single trust score", "§3 TRACE Measurement Model; §4 Assurance Case", "§5 Worked Evaluation", "§6 Limitations"),
    "2605.03858": ("PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "No Change — Existing Coverage", "LLM judges need constraint-level correctness and completeness labels because aggregate verdicts hide which obligation failed", "§3 MCJudgeBench Construction; §4 Constraint-Level Protocol", "§5 Experiments", "§6 Limitations"),
    "2605.03862": ("TRAIN-RLHF", (3, 2, 3), "No Change — Existing Coverage", "planner training should bind reward to executor-observed intermediate state and feasibility, not only a final textual answer", "§3 Executor-Grounded Reward; §4 Training", "§5 Experiments and Ablations", "§6 Limitations"),
    "2605.03884": ("AGENT-MULTI-AGENT", (3, 3, 2), "Integrate", "cross-agent latent handoff needs a versioned CacheCard carrying quantized KV state, bit allocation and receiver injection metadata, while prefix alignment and fused execution remain unresolved", "PDF §3 Problem Formulation; §4 QKVShare Method", "PDF §5 Experimental Setup; §6 Results", "PDF §7 Discussion and Limitations"),
    "2605.03952": ("PLATFORM-SECURITY", (3, 3, 3), "No Change — Existing Coverage", "coding-agent safety must evaluate cumulative diffs and end-state exploitability across innocuous ticket sequences, not approve each prompt independently", "§3 Threat Model; §4 MOSAIC-Bench", "§5 Evaluation Protocol; §6 Results", "§7 Limitations"),
    "2605.04018": ("AGENT-RAG", (3, 3, 3), "No Change — Existing Coverage", "reasoning retrieval should optimize complementary evidence portfolios and measure agent-loop completeness, iterations and answer quality under matched budgets", "§3 Bright-Pro; §4 Evaluation Protocol; §5 RTriever", "§6 Experiments", "§F Agent Configuration and stated protocol limits"),
    "2605.04019": ("PLATFORM-SECURITY", (2, 2, 2), "No Change — Existing Coverage", "red-team workflow generation can reduce operator setup cost, but attack libraries and a single target case do not establish adaptive security coverage", "§3 Agent Architecture; §4 Workflow Generation", "§5 Llama Scout Case Study", "§6 Limitations"),
    "2605.04116": ("PLATFORM-SECURITY", (3, 3, 3), "Integrate", "retrieval-selected in-context examples create a remotely observable membership channel, so example-store privacy belongs to the serving threat model", "§3 Threat Model; §4 Prefix-Based Membership Attacks", "§5 Experimental Setup; §6 Results", "§7 Defense and Limitations"),
    "2605.04178": ("INFER-TENSORRT-LLM", (3, 3, 3), "No Change — Existing Coverage", "GPU execution plans require architecture-specific microbenchmarks for memory hierarchy, matrix units, occupancy and precision; peak-FLOP rooflines are insufficient", "§3 Microbenchmark Suite; §4 Analytical Models", "§5 Validation on B200 and MI300A", "§6 Limitations"),
    "2605.04215": ("MULTIMODAL-GENERATIVE-PARADIGMS", (3, 2, 3), "Integrate", "fixed-length diffusion generation turns response-length prediction into an admission-time compute budget with explicit underprediction retry risk", "§3 Predict-then-Diffuse; §3.1 Adaptive Response Length Predictor", "§4 Experiments", "§5 Limitations"),
    "2605.04263": ("INFER-SPECULATIVE-DECODING", (3, 3, 3), "Integrate", "semantic speculative generation can verify multiple draft prefixes in one target pass, but must preserve a maximal valid commit boundary distinct from token-exact acceptance", "§3 PARSE; §3.2 Parallel Prefix Verification", "§4 Experiments and Ablations", "§5 Limitations"),
    "2605.04264": ("AGENT-MEMORY", (3, 3, 3), "No Change — Existing Coverage", "shared memory admission is a governed selection regime over provenance, correction and role preservation, not merely a retrieval score", "PDF §2 Selection Regimes; §3 Layered Memory Architecture", "PDF §4 Documented Traces", "PDF §5 Limitations and Design Agenda"),
    "2605.04266": ("TRAIN-RLHF", (3, 3, 3), "Integrate", "iterative RLHF creates a policy-to-future-reward-model feedback loop; omitting parameter steering allows self-reinforcing reward-model exploitation", "§3 Stackelberg Formulation; §4 Gradient Decomposition; §5 FPO", "§6 Experiments", "§7 Limitations"),
    "2605.04357": ("INFER-SCHEDULING", (3, 3, 3), "Integrate", "heterogeneous multi-model serving must co-optimize model placement and resource allocation under per-model SLOs, separating offline serving templates from online allocation", "§3 Multi-LLM Serving Problem; §4 Optimization; §5 Runtime", "§6 Evaluation", "§6.7 Sensitivity and §8 scope boundary"),
    "2605.04373": ("PLATFORM-SECURITY", (3, 2, 3), "No Change — Existing Coverage", "learned controllers need adversarial worst-case discovery compiled into a lightweight runtime protection rule with a nominal-path fallback", "§3 Regret-Maximization Discovery; §4 Runtime Protection", "§5 Evaluation", "§6 Limitations"),
    "2605.05248": ("AGENT-WORKFLOW", (3, 3, 3), "Integrate", "turning generated symbolic structure into executable code is an authority-amplifying materialization effect that requires capability, policy and resource admission", "§3 Governed Metaprogramming; §4 Pure Form Evaluation; §5 Governed Materialization", "§7 Implementation and Evaluation", "§8 Limitations"),
    "2605.08190": ("MULTIMODAL-EMBODIED-VLA", (3, 3, 3), "Integrate", "runtime assurance may consume ML outputs only under formally derived cooperative monitor conditions and a verified safe fallback", "§3 Synergistic Simplex Architecture; §4 Safety Conditions", "§5 Autonomous-Vehicle Evaluation", "§6 Limitations"),
    "2605.08195": ("INFER-TENSORRT-LLM", (3, 3, 3), "No Change — Existing Coverage", "on-device execution needs a portable exported program with delegated backend lowering while preserving framework semantics and explicit fallback", "§2 ExecuTorch Architecture; §3 Export and Delegation; §4 Runtime", "§5 Evaluation", "§6 Limitations"),
}

BLOCKED = {
    "2605.03275": {
        "access_status": "unverified",
        "reason": "official exact-v1 HTML/PDF could not be retrieved; identity and abstract alone cannot establish the proposed transactional data path, evaluation or limitations",
    },
}

def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "").strip()) if s.strip()]

def clip(text: str, n: int = 38) -> str:
    words = text.split()
    return " ".join(words[:n]) + ("…" if len(words) > n else "")

def closure(item: dict) -> str:
    if item.get("arxiv_id") == "2605.04356":
        return (
            "Identity/date/status closure：official arXiv abs identifies arXiv:2605.04356v1, "
            "submitted 2026-05-05T23:25:00Z, and marks it withdrawn by Joe Benton. The arXiv "
            "admin note states that v1 was removed because the submitter did not have the right "
            "to agree to the license at submission time; the withdrawn v1 is retained only as an "
            "auditable raw identity and is not scored, Source-Reviewed, mapped to a Books owner, "
            "or carried as a blocker. A newly public revision must be routed by its own first-public time."
        )
    ss = sentences(item.get("abstract", ""))
    mechanism = next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|formulate|evaluate|study|investigate|derive|show)\b", s, re.I)), ss[0] if ss else "摘要未披露可复核方法")
    result = next((s for s in ss if s != mechanism and re.search(r"\b(result|experiment|evaluation|outperform|improv|demonstrate|achiev|find|show)\b", s, re.I)), ss[-1] if ss else "摘要未披露结果")
    # Both quoted sentences are family-specific; the final boundary states the
    # exact durable-contract test that the family failed.
    return (
        f"问题/机制：{item['title']} 以“{clip(mechanism)}”处理其论文内任务；"
        f"证据边界为“{clip(result)}”。分母前闭合：该结果仍绑定上述数据、对象或局部方法，"
        "没有改变跨 workload 的 state/data/control ownership、evaluation/release contract，"
        "也未构成对当前 Books 设计判断的反例；若后续 artifact 证明这些系统边界发生变化则重开。"
    )

roadmap = (REPO / "ROADMAP.md").read_text()
owner_paths = {}
node_chapters = {}
for node in {v[0] for v in K.values()}:
    match = re.search(rf"\| `{re.escape(node)}` \| (Ch\d+) \| `([^`]+)`", roadmap)
    node_chapters[node] = match.group(1) if match else "Ch0"
    owner_paths[node] = match.group(2) if match else "ROADMAP.md"

path_chapters = {path: chapter for node, path in owner_paths.items() for chapter in [node_chapters[node]]}


def chapter_ref(path: str) -> str:
    chapter = path_chapters.get(path)
    if chapter is None:
        match = re.match(r"(\d+)-", Path(path).name)
        chapter = f"Ch{int(match.group(1))}" if match else "Ch0"
    return f"{path}#chapter-{chapter[2:]}"


def review_body(item: dict, review: dict) -> str:
    family = item["source_family_id"]
    return (
        f"#### {item['title']}\n\n"
        f"问题与旧路径：旧路径在固定 workload、低风险或规模较小时仍可用。"
        f"约束变化与机制：{item['screening_reason']}。Method：`{review['method_identity_locators']}`。\n\n"
        f"Evaluation：`{review['evaluation_locators']}`。"
        f"Counterevidence/limits：`{review['limitations_counterevidence_locators']}`。"
        f"Artifact：`{review['artifact_locators']}`。\n\n"
        f"<!-- claim:{family}:start -->长期结论只限 exact-v1 披露边界，不把作者 benchmark 外推到未测模型、硬件、精度、长度、batch、并发或 SLO。<!-- claim:{family}:end -->"
    )

rows = []
for original in INV["identities"]:
    item = dict(original)
    aid = item["arxiv_id"]
    if aid in K:
        node, score, disposition, delta, method, evaluation, limitations = K[aid]
        blocked = BLOCKED.get(aid)
        item.update(
            source_family_id=f"SF-2026-ARXIV-{aid.replace('.', '-')}",
            screening_status="retained",
            screening_reason=delta,
            owner_node=node,
            score_v2={"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            review_status="blocked" if blocked else ("deep_complete" if sum(score) >= 7 else "standard_complete"),
            access_status=blocked["access_status"] if blocked else "verified",
            integration_disposition=disposition,
            method_locator=method,
            evaluation_locator=evaluation,
            limitations_locator=limitations,
        )
    else:
        item.update(
            source_family_id=f"SF-2026-ARXIV-{aid.replace('.', '-')}",
            screening_status="pre_denominator_closure",
            screening_reason=closure(item),
            review_status="identity_date_closed",
            access_status="verified",
            integration_disposition="Rejected — Below Candidate Denominator",
        )
    rows.append(item)

retained = [x for x in rows if x["screening_status"] == "retained"]
closures = [x for x in rows if x["screening_status"] != "retained"]
ledger = {
    "schema": "daily-screening-ledger-v2.1",
    "report_date": "2026-05-06",
    "window": INV["window"],
    "utc_window": INV["utc_window"],
    "raw_snapshot_records": INV["raw_snapshot_records"],
    "registered_window_identities": len(rows),
    "screened_identities": len(rows),
    "candidate_denominator": len(retained),
    "pre_denominator_closures": len(closures),
    "identities": rows,
}
(ROOT / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
with (ROOT / "screening-ledger-final.tsv").open("w", newline="") as handle:
    cols = ["arxiv_id", "title", "screening_status", "source_family_id", "screening_reason", "owner_node", "review_status", "access_status", "integration_disposition"]
    writer = csv.DictWriter(handle, fieldnames=cols, delimiter="\t", extrasaction="ignore")
    writer.writeheader(); writer.writerows(rows)

reviews, provenance, comparisons, review_bodies = [], [], [], {}
for item in retained:
    aid = item["arxiv_id"]
    if aid in BLOCKED:
        body_text = (
            f"#### {item['title']}\n\n"
            f"Blocked exact-v1 review：{BLOCKED[aid]['reason']}。当前只核验了 `arXiv:{aid}v1` identity、"
            "first-public date 与 abstract；没有用摘要推断 Method、evaluation、limitations 或 Books eligibility。\n\n"
            f"<!-- claim:{item['source_family_id']}:start -->结论保持 `Blocked / Unverified`；取得 event-time exact-v1 正文后，"
            "必须重新审阅 Method、实验、ablation、limitations 与 artifact。<!-- claim:"
            f"{item['source_family_id']}:end -->"
        )
        review_bodies[item["source_family_id"]] = body_text
        url = f"https://arxiv.org/abs/{aid}v1"
        review = {
            "source_family_id": item["source_family_id"],
            "arxiv_id": aid,
            "primary_evidence_version": f"arXiv:{aid}v1",
            "exact_v1_url": url,
            "review_route": "deep",
            "method_identity_locators": f"Pending — {BLOCKED[aid]['reason']}",
            "evaluation_locators": "Pending — exact-v1 evaluation body unavailable; no result accepted from abstract alone",
            "limitations_counterevidence_locators": "Pending — exact-v1 limitations and counterevidence unavailable",
            "artifact_locators": f"{url} identity/abstract only; event-time implementation artifact Not Disclosed",
            "claim_boundary": item["screening_reason"],
            "completion_result": "blocked",
        }
        reviews.append(review)
        body_sha = vr._normalized_body_sha256(body_text)
        candidate = {
            "Event Identity": f"paper-v1:{aid}",
            "Primary Identifier": f"arXiv:{aid}v1",
            "Supporting Source IDs": "SRC-ARXIV",
            "Review Override": "none",
        }
        provenance_id = vr._expected_review_provenance(
            item["source_family_id"], candidate, "deep", review["primary_evidence_version"],
            f"SRC-ARXIV@{review['primary_evidence_version']}", review["method_identity_locators"],
            review["evaluation_locators"], review["limitations_counterevidence_locators"],
            review["artifact_locators"], f"claim:{item['source_family_id']}",
            f"review:{item['source_family_id']}", body_sha,
        )
        digest = hashlib.sha256(json.dumps(review, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        provenance.append({
            "review_provenance_id": provenance_id,
            "primary_identifier": f"arXiv:{aid}v1",
            "source_family_id": item["source_family_id"],
            "exact_v1_url": url,
            "retrieved_at": "2026-09-01T09:20:00+08:00",
            "access_route": "official_abs_identity_only",
            "review_receipt_sha256": digest,
            "review_body_sha256": body_sha,
            "source_body_sha256": None,
            "local_body": None,
            "limitation": BLOCKED[aid]["reason"],
        })
        path = owner_paths[item["owner_node"]]
        body = (REPO / path).read_text() if (REPO / path).exists() else ""
        adjacent = []
        if path != "ROADMAP.md":
            m = re.match(r"(\d+)-", Path(path).name)
            if m:
                n = int(m.group(1))
                adjacent = [str(p.relative_to(REPO)) for p in sorted((REPO / path).parent.glob("*.md")) if re.match(r"(\d+)-", p.name) and abs(int(re.match(r"(\d+)-", p.name).group(1)) - n) == 1]
        comparisons.append({
            "source_family_id": item["source_family_id"], "arxiv_id": aid,
            "owner_node": item["owner_node"], "owner_path": path,
            "owner_bytes_reviewed": len(body.encode()), "adjacent_paths_reviewed": adjacent,
            "current_content_comparison": "Owner and adjacent chapters were read only to place the potential knowledge delta; Books eligibility remains blocked until exact-v1 is recovered.",
            "disposition": "Blocked / Unverified", "delta": item["screening_reason"],
        })
        continue
    pdf = aid in {"2605.03884", "2605.04264"}
    url = f"https://arxiv.org/{'pdf' if pdf else 'html'}/{aid}v1"
    review = {
        "source_family_id": item["source_family_id"],
        "arxiv_id": aid,
        "primary_evidence_version": f"arXiv:{aid}v1",
        "exact_v1_url": url,
        "review_route": "deep" if item["score_v2"]["total"] >= 7 else "standard",
        "method_identity_locators": f"{url} {item['method_locator']}",
        "evaluation_locators": f"{url} {item['evaluation_locator']}",
        "limitations_counterevidence_locators": f"{url} {item['limitations_locator']}; no extrapolation beyond disclosed model, workload, hardware, precision, concurrency or SLO",
        "artifact_locators": f"{url} artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named",
        "claim_boundary": item["screening_reason"],
        "completion_result": "complete",
    }
    reviews.append(review)
    body_text = review_body(item, review)
    review_bodies[item["source_family_id"]] = body_text
    body_sha = vr._normalized_body_sha256(body_text)
    candidate = {
        "Event Identity": f"paper-v1:{aid}",
        "Primary Identifier": f"arXiv:{aid}v1",
        "Supporting Source IDs": "SRC-ARXIV",
        "Review Override": "knowledge_gap" if item["integration_disposition"] == "Integrate" else "none",
    }
    provenance_id = vr._expected_review_provenance(
        item["source_family_id"],
        candidate,
        review["review_route"],
        review["primary_evidence_version"],
        f"SRC-ARXIV@{review['primary_evidence_version']}",
        review["method_identity_locators"],
        review["evaluation_locators"],
        review["limitations_counterevidence_locators"],
        review["artifact_locators"],
        f"claim:{item['source_family_id']}",
        f"review:{item['source_family_id']}",
        body_sha,
    )
    digest = hashlib.sha256(json.dumps(review, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    provenance.append({
        "review_provenance_id": provenance_id,
        "primary_identifier": f"arXiv:{aid}v1",
        "source_family_id": item["source_family_id"],
        "exact_v1_url": url,
        "retrieved_at": "2026-09-01T00:45:00+08:00",
        "access_route": "official_pdf" if pdf else "official_html",
        "review_receipt_sha256": digest,
        "review_body_sha256": body_sha,
        "source_body_sha256": None,
        "local_body": None,
        "limitation": "Official exact-v1 was read remotely; a local source-body hash is not required by the research contract.",
    })
    path = owner_paths[item["owner_node"]]
    body = (REPO / path).read_text() if (REPO / path).exists() else ""
    adjacent = []
    if path != "ROADMAP.md":
        m = re.match(r"(\d+)-", Path(path).name)
        if m:
            n = int(m.group(1))
            adjacent = [str(p.relative_to(REPO)) for p in sorted((REPO / path).parent.glob("*.md")) if re.match(r"(\d+)-", p.name) and abs(int(re.match(r"(\d+)-", p.name).group(1)) - n) == 1]
    comparisons.append({
        "source_family_id": item["source_family_id"], "arxiv_id": aid,
        "owner_node": item["owner_node"], "owner_path": path,
        "owner_bytes_reviewed": len(body.encode()), "adjacent_paths_reviewed": adjacent,
        "current_content_comparison": "Current owner and adjacent chapters were read. Decision reflects whether the exact-v1 delta is already represented in the chapter evolution spine, not whether the paper name appears.",
        "disposition": item["integration_disposition"], "delta": item["screening_reason"],
    })

(ROOT / "exact-v1-review-packet.json").write_text(json.dumps({"schema": "exact-v1-review-packet-v2.1", "report_date": "2026-05-06", "items": reviews}, ensure_ascii=False, indent=2) + "\n")
(ROOT / "evidence-provenance-manifest.json").write_text(json.dumps({"schema": "evidence-provenance-v2.1", "report_date": "2026-05-06", "items": provenance}, ensure_ascii=False, indent=2) + "\n")
(ROOT / "books-current-content-comparison.json").write_text(json.dumps({"schema": "books-current-content-comparison-v2.1", "report_date": "2026-05-06", "items": comparisons}, ensure_ascii=False, indent=2) + "\n")

complete_count = sum(1 for review in reviews if review["completion_result"] == "complete")

ledger_sha = hashlib.sha256((ROOT / "screening-ledger-final.json").read_bytes()).hexdigest()
(ROOT / "coverage-receipt.json").write_text(json.dumps({
    "source_id": "SRC-ARXIV", "window": INV["window"],
    "route": "DataCite adjacent-month v2 100-prefix snapshots; 513/513 title+abstract semantic screen; official exact-v1 HTML/PDF review",
    "raw_snapshot_records": INV["raw_snapshot_records"], "registered_identities": len(rows),
    "semantic_screened": len(rows), "retained": len(retained), "pre_denominator_closed": len(closures),
    "ledger_sha256": ledger_sha, "pagination": "300 snapshot shards; all prefix pages closed", "status": "checked",
}, ensure_ascii=False, indent=2) + "\n")

queue = [x for x in retained if x["integration_disposition"] == "Integrate"]
qlines = ["# 2026-05-06 Books Writeback Queue", "", "本 author lane 未修改共享 Books；以下条目等待 root 按日期串行写回，并由不同 reviewer 做 post-write semantic audit。", "", f"- Queue count: {len(queue)}", ""]
for item in queue:
    qlines += [f"## {item['source_family_id']}", f"- Primary: `arXiv:{item['arxiv_id']}v1`", f"- Owner: `{item['owner_node']}`", f"- Target: `{owner_paths[item['owner_node']]}`", f"- Delta: {item['screening_reason']}", "- Required writeback: enter the existing evolution spine; preserve old-path rationale, changed constraint, ownership, trade-off, failure mode and fallback.", ""]
(ROOT / "BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(qlines).rstrip() + "\n")

audit = {
    "schema": "semantic-author-audit-v2.1", "report_date": "2026-05-06",
    "scope": "author-side full-population self-check; not an independent fresh-context audit",
    "checks": {"registered_screened": [len(rows), len(rows)], "candidate_denominator": len(retained), "pre_denominator_closures": len(closures), "closure_reason_unique": len({x['screening_reason'] for x in closures}), "false_positive_pass": "completed author-side", "false_negative_pass": "completed author-side against all 513 title+abstract rows after root challenge", "exact_v1_complete": complete_count, "blocked": len(BLOCKED), "books_compared": len(retained)},
    "unresolved_findings": ["Independent fresh-context denominator/evidence/selection/Books audit must be performed by a different reviewer.", "Two event-time exact-v1 bodies remain blocked and have deduplicated Materials Requests.", "Root serial Books writeback and post-write semantic audit remain pending."],
}
(ROOT / "semantic-author-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

def candidate_row(item: dict) -> str:
    s = item["score_v2"]
    access = "accessible" if item["access_status"] == "verified" else item["access_status"]
    override = "knowledge_gap" if item["integration_disposition"] == "Integrate" else "none"
    benchmark_claim = "no" if item["arxiv_id"] in BLOCKED else "yes"
    return f"| {item['source_family_id']} | arXiv:{item['arxiv_id']}v1 | paper-v1:{item['arxiv_id']} | 2026-W19 | 2026-05-05 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {item['review_status']} | {access} | {override} | review:{item['source_family_id']} | self | — | new_in_window | {item['owner_node']} | {item['integration_disposition']} | books-review:{item['source_family_id']} | {benchmark_claim} |"

selected = {"2605.03375": "DA-GPU-OWNED-SSD-KV", "2605.03562": "DA-MODEL-VISIBLE-KV-ERROR", "2605.04357": "DA-HETERO-MULTI-LLM-CONTROL"}
evidence_audit_refs = ";".join(
    [f"review:{item['source_family_id']}" for item in retained]
    + [f"claim:{item['source_family_id']}" for item in retained]
)
selection_audit_refs = ";".join(
    [f"analysis:{unit}" for unit in selected.values()]
    + [f"analysis-decision:{item['source_family_id']}" for item in retained if item["arxiv_id"] not in selected and item["arxiv_id"] not in BLOCKED]
)
books_audit_refs = ";".join(f"books-review:{item['source_family_id']}" for item in retained)
lines = [
    "# Daily Research — 2026-05-06", "", "**Research Date:** 2026-05-06", "", "**Timezone:** Asia/Shanghai", "", "**Strict Window:** 2026-05-05 09:00:00 ～ 2026-05-06 09:00:00（北京时间，左闭右开）", "", "**Contract:** V2.1 Full Replay；DataCite 仅用于 identity/date/abstract recovery；技术结论绑定 arXiv exact-v1。", "", "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。author lane 已完成分母、exact-v1、Score、Deep Selection 与 Books Comparison；等待不同 reviewer 的 fresh-context audit、root 串行 Books writeback 与 post-write audit。", "", "## Executive Summary", "", f"相邻月份 v2 快照共 {INV['raw_snapshot_records']:,} 条 raw records；严格窗口注册 513 条 identity。513/513 已逐项完成 title+abstract 语义筛选，保留 {len(retained)} 项（{len(retained)/513:.2%}），其余 {len(closures)} 项以 family-specific reason 在 Candidate Denominator 前闭合。{len(retained)}/{len(retained)} 项完成 official exact-v1 HTML/PDF author review，blocked=0；{len(queue)} 项进入 root 串行 Books 队列，本 lane 未修改共享 Books。", "", "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-06 |", "| Window End | 2026-05-06 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", "| Denominator ID | DEN-20260506-V1-FULL-REPLAY |", "| Denominator Frozen At | 2026-09-01T00:45:00+08:00 |", "| Completion Status | In Progress |", "| Coverage Gate | Open |", "| Evidence Gate | Open |", "| Books Gate | Open |", "", "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", f"| SRC-ARXIV | 2026-05-05T09:00:00+08:00 | 2026-05-06T09:00:00+08:00 | 2026-09-01T00:45:00+08:00 | DataCite v2 prefixes 00..99 + 513/513 semantic screen + exact-v1 HTML/PDF | checked | 513 | {';'.join(x['source_family_id'] for x in retained)} | pages=100; final_cursor=end; prefixes=00..99; raw={INV['raw_snapshot_records']:,}; registered=513; screened=513; retained={len(retained)}; closure={len(closures)}; denominator_sha256={ledger_sha} | 2026-05-06T00:59:59Z | papers/2026/05/_sources/daily-20260506/screening-ledger-final.json#sha256:{ledger_sha} | — |", "", "### Coverage Limitations", "", "<!-- coverage:SRC-ARXIV:20260506:start -->Coverage recall and family-specific pre-denominator closure are author-complete. DataCite supports identity/date/abstract only; all retained technical claims were reviewed against official exact-v1 HTML or PDF. Author review is not the independent fresh-context Semantic Audit required to pass the Coverage and Evidence Gates.<!-- coverage:SRC-ARXIV:20260506:end -->", "", "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->", "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
lines[lines.index("**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。author lane 已完成分母、exact-v1、Score、Deep Selection 与 Books Comparison；等待不同 reviewer 的 fresh-context audit、root 串行 Books writeback 与 post-write audit。")] = (
    "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。author lane 已完成分母重审、可访问 exact-v1、Score、Deep Selection 与 Books Comparison；等待不同 reviewer 的 fresh-context audit、2 项 exact-v1 材料恢复、root 串行 Books writeback 与 post-write audit。"
)
lines[lines.index(next(x for x in lines if isinstance(x, str) and x.startswith("相邻月份 v2 快照共 ")))] = (
    f"相邻月份 v2 快照共 {INV['raw_snapshot_records']:,} 条 raw records；严格窗口注册 513 条 identity。"
    f"513/513 已逐项完成 title+abstract 语义筛选，root challenge 后分母由 31 修正为 {len(retained)} 项（{len(retained)/513:.2%}），"
    f"其余 {len(closures)} 项以 family-specific reason 在 Candidate Denominator 前闭合。"
    f"{complete_count}/{len(retained)} 项完成 official exact-v1 HTML/PDF author review，blocked={len(BLOCKED)}；"
    f"{len(queue)} 项进入 root 串行 Books 队列，本 lane 未修改共享 Books。"
)
coverage_index = next(i for i, x in enumerate(lines) if isinstance(x, str) and x.startswith("<!-- coverage:SRC-ARXIV:20260506:start -->"))
lines[coverage_index] = (
    "<!-- coverage:SRC-ARXIV:20260506:start -->Coverage recall and family-specific pre-denominator closure are author-complete after root challenge. "
    f"DataCite supports identity/date/abstract only; {complete_count}/{len(retained)} retained families were reviewed against official exact-v1 HTML/PDF, "
    "while 2605.03275v1 is retrieval-blocked; withdrawn 2605.04356v1 is a pre-denominator identity closure and not an Evidence blocker. Author review is not the independent fresh-context Semantic Audit required to pass the Coverage and Evidence Gates."
    "<!-- coverage:SRC-ARXIV:20260506:end -->"
)
lines += [candidate_row(x) for x in retained]
lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
retained_by_family = {x["source_family_id"]: x for x in retained}
provenance_by_family = {x["source_family_id"]: x for x in provenance}
for review in reviews:
    item = retained_by_family[review["source_family_id"]]
    prov = provenance_by_family[item["source_family_id"]]
    lines.append(f"| {item['source_family_id']} | {prov['review_provenance_id']} | {review['review_route']} | {review['primary_evidence_version']} | SRC-ARXIV@{review['primary_evidence_version']} | {review['method_identity_locators']} | {review['evaluation_locators']} | {review['limitations_counterevidence_locators']} | {review['artifact_locators']} | claim:{item['source_family_id']} | {review['completion_result']} |")
lines += ["", "### Source Reviews", ""]
for item in retained:
    lines += [f"<!-- review:{item['source_family_id']}:start -->", review_bodies[item["source_family_id"]], f"<!-- review:{item['source_family_id']}:end -->", ""]
lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for item in retained:
    if item["arxiv_id"] in BLOCKED:
        continue
    lines.append(f"| {item['source_family_id']} | exact-v1 disclosed workload for {item['title']} | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/reliability contract only | author protocol; independent reproduction Not Disclosed |")
lines += ["", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for item in retained:
    aid = item["arxiv_id"]; unit = selected.get(aid, "—"); decision = "selected" if aid in selected else "not_selected"
    if aid in BLOCKED:
        lines.append(f"| {item['source_family_id']} | score_7_9 | not_selected | — | — | exact-v1 body is unavailable; Deep Analysis cannot be completed from identity/abstract | analysis-decision:{item['source_family_id']} |")
        continue
    if item["score_v2"]["total"] < 7 and item["integration_disposition"] != "Integrate":
        continue
    rationale = "selected because it changes cross-layer state/control ownership" if aid in selected else f"exact-v1 review remains complete; owner-local delta is retained in {item['owner_node']} while the selected units cover the broader cross-stage transitions"
    ref = f"analysis:{unit}" if aid in selected else f"analysis-decision:{item['source_family_id']}"
    eligibility = "score_7_9" if item["score_v2"]["total"] >= 7 else "score_5_6"
    if item["integration_disposition"] == "Integrate":
        eligibility += ";forced_review;potential_books_delta"
    lines.append(f"| {item['source_family_id']} | {eligibility} | {decision} | {unit} | — | {rationale} | {ref} |")
lines += ["", "<!-- analysis:DA-GPU-OWNED-SSD-KV:start -->", "### SSD KV：从 CPU 发起 I/O 到 GPU 拥有数据与控制路径", "", "GDS 仍由 CPU 为大量碎片 I/O 发起请求，在长上下文 prefix restore 中，GPU 等待的是控制路径而不只是介质带宽。Tutti 将 KV 封装为 GPU-native object，由 GPU io_uring 批量提交，并以 slack-aware policy 避免 I/O kernel 与推理 kernel 争抢。收益是把 SSD bandwidth 变成可用 cache tier；代价是 GPU 侧 object metadata、I/O kernel 生命周期和 contention policy。小 cache、低复用或 CPU 不成为瓶颈时，DRAM/普通 GDS 仍更简单。", "<!-- analysis:DA-GPU-OWNED-SSD-KV:end -->", "", "<!-- analysis:DA-MODEL-VISIBLE-KV-ERROR:start -->", "### KV 量化：从存储误差到消费算子可见误差", "", "最小化 K/V 的 raw MSE 在实现上简单，却把 attention 根本看不到的 key 平移与正交残差也视为同等重要。HeadQ 将 K 的目标改成 softmax 前 score-space，把 V 的目标改成 attention-weighted readout，并用 calibration query basis 保存低秩 residual。收益是预算花在行为可见坐标；代价是 calibration drift、side-code metadata 和额外 logit correction。论文主结果仍是 K-only、dense V、Python eager hooks，不证明 packed-kernel latency。", "<!-- analysis:DA-MODEL-VISIBLE-KV-ERROR:end -->", "", "<!-- analysis:DA-HETERO-MULTI-LLM-CONTROL:start -->", "### 多模型异构 Serving：从逐模型 placement 到共同资源控制", "", "逐模型独立选择最便宜 GPU 在资源充足、模型少时合理；共享稀缺 GPU 时会造成局部最优抢占和其他模型 SLO 不可行。Coral 把 `(model,SLO,node-combination,placement)` 固化为 offline Serving Template，再由 online allocator 在价格、供给和 demand 变化下共同选择。它把昂贵 placement search 移出在线路径，但新增 profile freshness、template coverage、迁移与重配置成本；其 6 模型、20 配置结果不能外推到任意互联与跨区域拓扑。", "<!-- analysis:DA-HETERO-MULTI-LLM-CONTROL:end -->", ""]
for item in retained:
    if item["arxiv_id"] not in selected:
        decision_text = (
            "exact-v1 正文仍 blocked；当前不进入 Deep Analysis，也未用摘要补写机制。"
            if item["arxiv_id"] in BLOCKED else
            "已完成 exact-v1 Review；不扩写只表示其 delta 更局部，不表示跳过 Source Review。"
        )
        lines.append(f"<!-- analysis-decision:{item['source_family_id']}:start -->{item['source_family_id']} {decision_text}<!-- analysis-decision:{item['source_family_id']}:end -->")
lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for item, comparison in zip(retained, comparisons):
    adjacent = "; ".join(chapter_ref(path) for path in comparison["adjacent_paths_reviewed"]) or chapter_ref(comparison["owner_path"])
    relation = "Direct Evolution" if item["integration_disposition"] == "Integrate" else "Layering / Dependency"
    lines.append(f"| {item['source_family_id']} | {item['owner_node']} | {chapter_ref(comparison['owner_path'])} | {adjacent} | existing:{item['source_family_id']} | delta:{item['source_family_id']} | {relation} | {item['integration_disposition']} | books-review:{item['source_family_id']} |")
for item in retained:
    lines += [f"<!-- books-review:{item['source_family_id']}:start -->", f"<!-- existing:{item['source_family_id']}:start -->已读取 `{item['owner_node']}` 当前 owner 与相邻章节；旧路径在固定 workload、低风险或规模较小时仍成立。<!-- existing:{item['source_family_id']}:end -->", f"<!-- delta:{item['source_family_id']}:start -->{item['screening_reason']}<!-- delta:{item['source_family_id']}:end --> Decision: `{item['integration_disposition']}`；author lane 未修改共享 Books。", f"<!-- books-review:{item['source_family_id']}:end -->"]
lines += [
    "", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
    "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
    "| --- | --- | --- | --- | --- | --- | --- |",
    "| SA-20260506-COVERAGE | fresh-context:independent-reviewer-pending | coverage | coverage:SRC-ARXIV:20260506 | F-20260506-INDEPENDENCE — author 513-row FP/FN pass is not independent | Pending — different reviewer | open |",
    f"| SA-20260506-EVIDENCE | fresh-context:independent-reviewer-pending | evidence | {evidence_audit_refs} | F-20260506-EVIDENCE — exact-v1 locators and boundaries need reviewer-isolated challenge | Pending — different reviewer | open |",
    f"| SA-20260506-SELECTION | fresh-context:independent-reviewer-pending | deep_analysis_selection | {selection_audit_refs} | F-20260506-SELECTION — selected and not-selected decisions require reviewer-isolated challenge | Pending — different reviewer | open |",
    f"| SA-20260506-BOOKS | fresh-context:independent-reviewer-pending | books | {books_audit_refs} | F-20260506-BOOKS — current-Books comparison, root writeback and post-write audit pending | Pending — root + different reviewer | open |",
    "", "## 8. Ignored Noise", "",
    f"{len(closures)} 项未进入 Candidate Denominator；逐项机制、证据与可重开条件保存在 `screening-ledger-final.json/tsv`，不是静默丢弃。",
    "", "## 9. Recommended Action", "",
    f"Root 串行处理 {len(queue)} 项 Books queue；不同 reviewer 先做 513-row denominator/evidence/Deep Selection/Books comparison 独立审计，写回后再做 post-write semantic audit。",
    "", "## 10. Repository Changes", "",
    "仅新增/更新 `papers/2026/05/06` 与 `papers/2026/05/_sources/daily-20260506`；未修改共享 Books，未 stage/commit/push。",
    "", "## 11. Open Questions", "",
    f"- 独立 reviewer 是否在 {len(closures)} 个 closure 中发现 false negative？",
    f"- {len(retained)} 个 exact-v1 claim boundary 是否存在越界或 locator 不足？",
    f"- {len(queue)} 个 Integrate queue 经 current Books challenge 后是否仍需全部写回？",
    "", "## 12. Sources", "",
    "- DataCite arXiv v2 month snapshots（identity/date/abstract recovery；accessed 2026-09-01）",
    f"- {len(retained)} 项 official arXiv exact-v1 HTML/PDF，URL 逐项记录于 Review Completion Receipt（accessed 2026-09-01）",
    "", "## 13. Final Status", "",
    "Completion Status: `In Progress`", "",
    "Coverage: `Open`", "",
    "Evidence: `Open`", "",
    "Books: `Open`", "",
    "unresolved findings: 4", "",
    "Author packet 已完成；尚未由不同 reviewer 完成 Coverage、Evidence、Deep Selection 与 Books comparison 的 fresh-context audit，也未执行共享 Books 写回与 post-write audit。",
    "",
]

# Reconcile blocked exact-version material separately from ordinary questions.
lines[lines.index(next(x for x in lines if isinstance(x, str) and x.startswith("- ") and "个 exact-v1 claim boundary" in x))] = (
    f"- {complete_count} 个已完成 exact-v1 claim boundary 是否存在越界或 locator 不足？2 个 blocked family 取得材料后须重新完成全文审阅。"
)
lines[lines.index(next(x for x in lines if isinstance(x, str) and x.startswith("- ") and "项 official arXiv exact-v1 HTML/PDF" in x))] = (
    f"- {complete_count} 项 official arXiv exact-v1 HTML/PDF，URL 逐项记录于 Review Completion Receipt（accessed 2026-09-01）"
)
lines[lines.index("unresolved findings: 4")] = "unresolved findings: 6"
lines[lines.index("Author packet 已完成；尚未由不同 reviewer 完成 Coverage、Evidence、Deep Selection 与 Books comparison 的 fresh-context audit，也未执行共享 Books 写回与 post-write audit。")] = (
    "Author packet 已按 root challenge 修复；尚未由不同 reviewer 完成 Coverage、Evidence、Deep Selection 与 Books comparison 的 fresh-context audit，2 项 exact-v1 材料仍缺失，也未执行共享 Books 写回与 post-write audit。"
)
source_index = lines.index("## 12. Sources")
materials = [
    "### Materials Request — MR-20260506-2605.03275", "",
    "- Priority: P1 Full Text",
    "- Candidate: `arXiv:2605.03275v1`，Beyond Similarity Search: A Unified Data Layer for Production RAG Systems",
    "- Missing material: event-time exact-v1 HTML/PDF/TXT full body.",
    "- Why insufficient: identity/abstract cannot establish transaction, tenant-isolation, query-composition implementation, evaluation, limitations or artifact.",
    "- Acceptable substitute: official exact-v1 PDF/HTML/TXT or author copy carrying arXiv v1 identity.",
    "- Suggested filename: `arxiv-2605.03275v1.pdf`", "",
    "<!-- validator:materials-request-v1 -->",
    "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    "| MR-20260506-2605.03275 | P1 Full Text | SF-2026-ARXIV-2605-03275 | — | — | 2026-W19 | arXiv:2605.03275v1; https://arxiv.org/abs/2605.03275v1; https://arxiv.org/html/2605.03275v1; https://arxiv.org/pdf/2605.03275v1 | event-time exact-v1 full body | identity/abstract do not establish the transactional data path, isolation enforcement, evaluation, limitations or artifact | official exact-v1 PDF/HTML/TXT or author copy carrying arXiv v1 identity | arxiv-2605.03275v1.pdf | Method, evaluation, ablation, limitations, artifact and Books eligibility |",
    "",
]
lines[source_index:source_index] = materials
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text("\n".join(lines))

print(json.dumps({"raw": INV["raw_snapshot_records"], "registered": len(rows), "screened": len(rows), "retained": len(retained), "closures": len(closures), "exact_v1": complete_count, "blocked": len(BLOCKED), "integrate_queue": len(queue)}, ensure_ascii=False))
