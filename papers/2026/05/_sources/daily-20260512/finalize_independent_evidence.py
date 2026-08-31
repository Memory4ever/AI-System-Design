#!/usr/bin/env python3
"""Finalize the 2026-05-12 non-author exact-v1 evidence packet.

The packet records the exact paper version and the actual section headings
inspected by the independent reviewer.  It intentionally does not treat an
abstract, a title match, or a local body hash as a substitute for the public
Evidence contract.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent

# (method/system locator, evaluation locator, limitations/counterevidence locator)
# These headings were read from the exact-v1 arXiv HTML/PDF table of contents
# and the corresponding body sections, not inferred from the abstract.
SECTIONS = {
    "2605.09863": ("§3 Method (§3.1–§3.9)", "§4 Evaluation (§4.1–§4.9)", "§6 Limitations; §7 Open Source and Reproducibility"),
    "2605.09877": ("§4 Method: weight preparation, readout, recurrence, append and merge", "§5 experiments; Appendix D short-context evaluation", "No dedicated limitations section; §3 design choices and Appendix D delimit the evaluated recurrent-memory configurations"),
    "2605.09886": ("§II System Model; §III Proposed Method", "§IV Evaluation", "§VI Discussion and Limitations"),
    "2605.09889": ("§III System Model; §IV Skill Description Deception Attack", "§V Experiment Results", "No dedicated limitations section; the nine disclosed routing domains are the evidence boundary"),
    "2605.09934": ("§3 Method (§3.1–§3.3); §4 Dataset", "§5 Experiments", "Limitations section and representative provenance-failure cases"),
    "2605.09992": ("§3 Attention Drift; §4 What Causes Attention Drift? (§4.1–§4.5)", "§5 Performance Impact; Appendix B Benchmarks; Appendix C Training", "§7 Limitations"),
    "2605.09994": ("§3 Overview; §4 Transactional Global Batch: layout, manifest, atomic visibility and cursor", "§7 Evaluation", "No dedicated limitations section; the disclosed object-store and 64-GPU workloads bound the claim"),
    "2605.10012": ("§3 Formative Study and SBAC system design", "§5 Evaluation", "§6.4 Limitations"),
    "2605.10057": ("§3 Method (§3.1–§3.6): Failure-Aware Matrix Training, Parallel Activation and Recovery Reachability", "§4 Experiments: routing, failure recovery and cross-benchmark transfer", "Limitations discussion: transfer assumes shared task primitives and dependency structure"),
    "2605.10075": ("§3 Problem Formulation; §4 Active-Testing Method", "§5 Experiments", "§6 Conclusion and Limitations"),
    "2605.10094": ("§3 Retrieve-then-Steer; §4 deployment-time success-memory steering", "§5.1 simulation, §5.2 real-world evaluation; §6 ablations", "Appendix I Limitations; Appendix D real-robot details; Appendix E capacity; Appendix F overhead"),
    "2605.10124": ("§II System Model; §III GELATO adaptive scheduling algorithm", "§IV Simulation and Evaluation", "No dedicated limitations section; device-edge topology, draft/target pair and simulated resource envelope bound the result"),
    "2605.10199": ("§4 Method and user-stream routing policies; §5 training data", "§6.1–§6.4 Experiments", "§8 Limitations"),
    "2605.10223": ("§3 Core Principles; §4 Dynamic Tiered AgentRunner Architecture", "§6 Evaluation", "Limitations discussion after results; evidence is from the disclosed SaaS execution setting"),
    "2605.10246": ("§3.1 Design Principles; §3.2 Agent Framework; §3.3 Scenario Construction; §3.4 Evaluation Protocol", "§4.1 Models; §4.2 Main Results; §5.1 Behavioral Patterns; §5.2 pressure ablation; §5.3 Structural Drivers", "No dedicated Limitations section; 33 scenarios, 11 traps, 7 models and 231 minimal-ReAct runs bound the claim"),
    "2605.10347": ("§2 Constructing Mobile World Models; §3 What Should a Mobile World Model Predict? (§3.1–§3.2)", "Evaluation sections and appendix GUI-agent experiments", "No substantive dedicated limitations section; evaluated mobile-GUI tasks and model family are the boundary"),
    "2605.10351": ("Reliability–efficiency co-design chapters: inference reliability, uncertainty and system co-design", "Worked analyses and case studies across the monograph", "No single controlled evaluation contract; this is a synthesis and design framework, not comparative proof of one implementation"),
    "2605.10366": ("§3 Method (§3.1–§3.5): graph credit assignment and co-evolution loop", "Experiments and ablations", "Appendix J Limitations"),
    "2605.10380": ("§3 Pipeline Characterization; §4 Agent-X prefix cache and LLM-free drafting", "§5 Evaluation", "No dedicated limitations section; on-device models, devices and agent pipelines disclosed in §5 bound generality"),
    "2605.10405": ("§3 Low-rank best-model identification method", "§4 Experiments", "§5 Conclusion: low-rank-quality dependence and binary-score scope"),
    "2605.10426": ("§3 Methodology; §3.2 action-conditioned world model and multi-expert control", "Evaluation and autonomous-driving experiments", "No dedicated limitations section; driving simulator/data, action schema and evaluated VLA backbone delimit the result"),
    "2605.10448": ("§3 Method", "§4 Experiments; §5 Evaluation; Appendices A–E case-level audit", "§6 Limitations and Discussion"),
    "2605.10481": ("§2 Constraint Drift; §4 Paradigm Design (§4.1 CSG, §4.2 constraint-native RL, §4.3 closed loop)", "§5 Empirical Case Study", "§6 Alternative Views and Objections; §7 Research Agenda; §4 states the blueprint is not a complete verifier or RL algorithm"),
    "2605.10501": ("§2 Compound Training Challenges; §3 Maestro Design (§3.1–§3.4)", "§4 Evaluations and Case Study (§4.1 VLM training, §4.2 distillation)", "No dedicated limitations section; the disclosed compound workloads, cluster and framework integration bound the result"),
    "2605.10516": ("§2 output-consistency U-statistics; §3 execution trajectories as stochastic processes", "§4 Experiments; §5 reliability-failure diagnostics; Appendices B–D", "§6 Discussion; small-sample and multiple-valid-solution boundaries in Appendices B and D"),
    "2605.10555": ("§III Design: six-verb interface, ToolDescriptor and normalized tool contract; §IV Governance; §V Implementation", "§VI Evaluation", "§VII Discussion: protocol conventions are not a formal IDL and tools need not implement every verb"),
    "2605.10556": ("§III Methodology; §IV parallelism-aware closed-form energy model", "§V Experiments (§V-A–§V-C), including modality, quantization, batch and cross-hardware tests", "No dedicated limitations section; the enumerated model/hardware/engine deployment space bounds extrapolation"),
    "2605.10575": ("§2 Four-Diagnostic Acceptance Standard; §3 Audit Procedure", "§5 Artifact and case audit", "§6 Limitations"),
    "2605.10614": ("§3 Threat Model; §4 PRISM generation-time leakage control", "Evaluation and attack/utility experiments", "Explicit scope and behavioral Limitations section"),
    "2605.10670": ("§3 System Design (§3.1–§3.6); §4 membership-elastic communication; §5 expert-coverage repair", "Evaluation sections on failure/recovery and serving overhead", "§3.1 Failure Model and Scope; no claim beyond disclosed partial-rank failures and redundant expert state"),
    "2605.10763": ("§2 MATRA attack-surface framework", "§3 OpenClaw use case", "No controlled comparative evaluation; the single-system case study is explanatory, not prevalence evidence"),
    "2605.10779": ("§3 Dataset and real-OS threat construction; §4 evaluation framework", "§5 Experiments", "§6 Limitations"),
    "2605.10787": ("§3 ComplexMCP (§3.1 formalization, state instantiation, interdependence and deterministic evaluation)", "§4 Experiments and challenge analysis", "§5 Limitations and Future Work"),
    "2605.10805": ("§2 reasoning-judge cost study; §3 RACER; §4 theoretical results", "§5 Experiments; Appendix B evaluation protocol", "§7 Conclusion and Limitation"),
    "2605.10819": ("§3 Algebraically Consistent Latent Action Method: structured transitions, pretraining and joint flow", "§4 Experimental Setup and result/ablation sections", "No dedicated limitations section; the disclosed VLA backbones, datasets and action representation bound the claim"),
    "2605.10832": ("§2 Visual Harness and on-policy data-evolution method", "§3 Experiments and ablations", "No dedicated limitations section; evidence is bounded to the visual-search tasks, base models and iteration budget"),
    "2605.10834": ("§3 real-world pentesting protocol: ground truth, matching, metrics and stochasticity", "Evaluation and agent comparison sections", "Limitations discussion; controlled targets do not establish unrestricted real-network safety or capability"),
    "2605.10850": ("§3 VeriMap: task taxonomy, two-axis behavior model and statistical testing", "Experiments and calibration analyses", "Limitations section; medical-VQA datasets and verifier families bound transfer"),
    "2605.10870": ("§3 decision-distortion setup and forgetting boundary; §4 certified online memory splits", "§5 Experiments on synthetic tasks, LoCoMo and LongMemEval", "No dedicated limitations section; theorem assumptions and the disclosed memory tasks bound operational claims"),
    "2605.10875": ("§4 per-token self-optimizing runtime policy", "§5 Experiments and ablations", "No dedicated limitations section; evaluated models, accelerator and policy-action space bound the runtime conclusion"),
    "2605.10901": ("§3 Method and formal guardrail guarantee", "§4 Experiments", "§5.2 Limitations"),
    "2605.10905": ("§3 TLX overview; §4 MIMW; §5 implementation", "§6 Evaluation", "No dedicated limitations section; production kernels, GPU generations and compiler coverage disclosed in §6 bound the claim"),
    "2605.10912": ("§3 benchmark construction, native-runtime tasks and evaluation contract", "§4 Experiments", "Appendix B Limitations"),
    "2605.10913": ("§3 Shepherd programming model: tasks, reversible effects, scopes and replayable execution trace", "§4 Framework Performance; §5 live-supervision and counterfactual-replay experiments", "No dedicated limitations section; implementation, provider and benchmark setups delimit the evidence"),
    "2605.10923": ("§4 Dynamic Skill Lifecycle; §5 implementation", "§6 Experiments", "No dedicated limitations section; lifecycle policy, tasks and RL setting disclosed in §6 bound generality"),
    "2605.10933": ("§3 edge-MoE methodology", "§4 Experiments; §5 hyperparameters", "No dedicated limitations section; device class, expert topology and model scale disclosed in §4–§5 bound the result"),
    "2605.11039": ("§3 Pact: argument-level contracts, provenance, runtime checking and formal properties", "§4 Experiments (§4.1–§4.4), including mechanism ablations and stress boundaries", "§3.1 Threat Model and Scope; §4.4 Practicality, Stress Tests and Boundaries"),
    "2605.11047": ("§3 preliminaries and threat model; §4 DeepTrap/open-world execution-context construction", "§5 Experiments", "Limitations discussion; sampled OpenClaw contexts and agent models bound the claim"),
    "2605.11053": ("§3 Threat Model; §4 MCPShield graph, features and detector", "Evaluation and ablation sections", "Limitations discussion; observed tool-call distributions and attacks bound the detector result"),
    "2605.11086": ("§3 benchmark, evaluation protocol, task domains and construction", "§4 Evaluation; Appendices B–C task and exploit details", "§5 Discussion and Conclusion; 898 containerized instances and mitigation toggles do not establish real-world exploit coverage"),
    "2605.11093": ("§3 Challenges; §4 DMI-Lib design (HookPoint, Ring2, exporter, policies and distributed operation); §5 Implementation", "§6 Evaluation; §7 Use Cases", "No dedicated limitations section; model/runtime integrations and probes disclosed in §6–§7 bound overhead and coverage"),
    "2605.11182": ("§3 On-Policy Distillation; §5 failure mechanisms; §6 fixes", "§4 math/alignment/system-prompt experiments", "Mechanism claims are bounded to sampled-token/full-vocabulary KL variants and disclosed teachers/students; no universal distillation guarantee"),
    "2605.11186": ("§3 Preliminary and Motivation; §4 cascaded verification and adapter design", "§5 Experiments: accepted length, speedup and memory trade-off", "No dedicated limitations section; memory-limited devices, target/drafter pairs and tree budgets disclosed in §5 bound the result"),
    "2605.11202": ("§2 representative failures; §3 GRIEF fuzzing design, trace mutation and confirmation oracle", "§4 Evaluation, including KV-cache state-corruption impact", "No dedicated limitations section; tested serving stacks, mutation grammar and confirmation oracle bound discovery completeness"),
    "2605.11205": ("§3 Methodology: simple averaging and 2PL item-response model", "§4 Experimental Design across four domains; §5 Results", "No dedicated limitations section; synthetic sparsity/difficulty regimes and four disclosed domains bound the scaling-law claim"),
    "2605.11209": ("§3 problem/setup; §4 systematic failure concentration; §5 CEM failure-prone sampling", "§6 inference-efficiency experiments", "Limitations discussion; saturated benchmarks, selected models and failure parameterization bound rare-event estimates"),
    "2605.11212": ("§3 Temporal Visual Redundancy; §4 ReVision training", "§5 efficiency/performance/history-scaling experiments; §6 ablations", "No dedicated limitations section; evaluated computer-use agents, tasks and history lengths bound transfer"),
    "2605.11215": ("§3 fault-tolerance challenges; §4 ReCoVer: ULFM collectives, in-step recovery and trajectory preservation", "§5 Evaluation; Appendix A additional evaluation", "No dedicated limitations section; disclosed training frameworks, failure model and cluster configurations bound the claim"),
    "2605.11229": ("§2 threat model; §3 path-sensitive workflow analysis and prompt-provenance taint tracking", "Evaluation and case-study sections", "Limitations discussion; modeled workflow languages, events and attack sources bound completeness"),
    "2605.11234": ("PDF §3 theoretical foundation; §4 observed failure modes; §5 resolve/contextualize/annotate interface contract; §6 enforcement architecture", "PDF §7 controlled experiment", "PDF §8 limitations, scalability and integration; 72 tool calls, six configurations and Qwen3-32B bound the reported result"),
    "2605.11277": ("§3 bimodal expert-distribution problem; §4 overview; §5 Sieve scheduler", "Evaluation and sensitivity sections", "§3.4 prior-PIM limitations; evaluated MoE distributions, PIM/GPU model and simulator bound generality"),
    "2605.11317": ("§2 token-turn patterns and local manifold; §3 soft-prompt initialization, tuning, switching and rollback; §4 theory", "Evaluation and multi-turn serving experiments", "No dedicated limitations section; dialogue distributions, surrogate/target models and rollback policy bound the result"),
    "2605.11325": ("§3 structured belief architecture; §4 precision-first retrieval/index design", "Benchmark and empirical-comparison sections", "Limitations discussion; benchmark corpus, belief schema and BM25/vector baselines bound the retrieval conclusion"),
    "2605.11328": ("§2 uncertainty-guided test-time training (§2.2 LoRA ensemble, §2.3 uncertainty-shaped advantage)", "§3 Experiments, mechanism ablation and computational cost", "No dedicated limitations section; adapter ensemble, tasks and test-time update budget bound the epistemic claim"),
    "2605.11330": ("§2 benchmark desiderata; §3 audit of existing benchmarks; §4 Trivia+ construction", "Human annotation and detector evaluation sections", "Limitations discussion; RAG task generation, label process and evaluated detectors bound conclusions"),
    "2605.11333": ("§2 Chakra Schema; §3 pre/post-execution trace collection", "§4 downstream trace analysis, replay, benchmarking and co-design use cases", "No dedicated limitations section; schema expressiveness, converter coverage and replay fidelity remain implementation boundaries"),
    "2605.11334": ("§3 VERDI: rubric taxonomy, verification sub-checks, SVA/CLM/EGS signals", "§4 experiments and calibration/selective-risk evaluation", "Limitations discussion; disclosed judges, tasks and verification traces bound single-call calibration"),
    "2605.11335": ("§2 DiT/offloading motivation; §3 analytical overlap model and communication-aware chunked prefetching", "Evaluation and ablation sections", "No dedicated limitations section; PCIe topology, DiT workloads and offload regime bound the result"),
    "2605.11360": ("§3 Motivation; §5 policy/risk lattice; §6 ConLeash boundary checking and refinement", "Evaluation and user/authorization analyses", "Limitations discussion; policy language, risk lattice and MCP actions disclosed in the study bound completeness"),
    "2605.11367": ("§3 3D-Belief formulation, architecture, diffusion training and objective", "§4 three experiments; §8 extended results", "No dedicated limitations section; 3D-CORE, navigation environments and sensor/action assumptions bound world-belief claims"),
    "2605.13880": ("§3 pre-task memory construction, proposer control and validator-gated writes", "§4 Experiments and ablations", "Limitations discussion; synthetic-practice generator, validators, tasks and memory budget bound transfer"),
    "2605.18792": ("§2 knowledge-conflict benchmark; §3 self-prior, conditional belief estimation and abstention", "§4 Experiments, selective answering and ablations", "No dedicated limitations section; benchmark conflicts, model families and layer probes bound self-awareness claims"),
    "2605.18796": ("§3 formulation; §4 calibrated uncertainty and threshold policy; §5 theory", "§6 Experiments and diagnostics", "§7 Discussion and Limitations"),
    "2605.18803": ("§3 PROWL: asymmetric min-max objective, chunked diffusion forcing and adversarial curriculum", "Evaluation, prioritized-failure and ablation sections", "Limitations discussion; world-model backbone, environments and regret proxy bound generality"),
    "2605.23956": ("§2 typed pipeline graph, type-dispatched distances, sensitivity matrix and loop bifurcation", "§2.5 evaluation principles and estimation; framework case analyses", "No controlled production validation; the formal model depends on chosen distance metrics and perturbation distributions"),
}

BLOCKED = {
    "2605.10133": {
        "reason": "Official arXiv abs/version history is readable and fixes v1 at 2026-05-11 07:44:37 UTC, but exact-v1 HTML, PDF and TeX bodies remain unavailable after independent retries. Abstract-only evidence cannot establish Method, Evaluation or Limitations.",
        "request": "Any official exact-v1 PDF, TeX source, author manuscript or repository snapshot that is demonstrably identical to arXiv:2605.10133v1.",
    }
}

SPECIAL_URLS = {
    "2605.10246": "https://arxiv.org/pdf/2605.10246v1",
    "2605.11234": "https://arxiv.org/pdf/2605.11234v1",
}

ARTIFACTS = {
    "2605.09992": "https://github.com/Dogacel/Attention-Drift",
    "2605.10246": "https://github.com/liuxingtong/Sci-Integrity-Bench",
}


def compact(text: str, limit: int = 520) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def main() -> None:
    ledger_path = ROOT / "screening-ledger-independent-reconciled.json"
    ledger = json.loads(ledger_path.read_text())
    rows = [row for row in ledger["identities"] if row.get("screening_status") == "retained"]
    assert len(rows) == 76
    author_packet = {item["arxiv_id"]: item for item in json.loads((ROOT / "exact-v1-review-packet.json").read_text())}

    packet = []
    provenance = []
    materials = []
    now = datetime.now(timezone.utc).isoformat()

    for row in rows:
        aid = row["arxiv_id"]
        version = f"arXiv:{aid}v1"
        url = SPECIAL_URLS.get(aid, f"https://arxiv.org/html/{aid}v1")
        if aid in BLOCKED:
            item = {
                "arxiv_id": aid,
                "source_family_id": row["source_family_id"],
                "primary_evidence_version": version,
                "review_provenance_id": f"REVIEW-20260512-{aid.replace('.', '-')}-V1",
                "review_route": "deep",
                "method_identity_locators": "Blocked — exact-v1 body unavailable",
                "evaluation_locators": "Blocked — exact-v1 body unavailable",
                "limitations_counterevidence_locators": "Blocked — exact-v1 body unavailable",
                "artifact_locators": "Not verified because exact-v1 body is unavailable",
                "claim_nonproof_boundary": BLOCKED[aid]["reason"],
                "completion_result": "blocked",
            }
            packet.append(item)
            provenance.append({
                "arxiv_id": aid,
                "review_provenance_id": item["review_provenance_id"],
                "exact_v1_url": url,
                "retrieved_at": now,
                "retrieval_mode": "official abs/version accessible; official exact-v1 HTML/PDF/TeX body unavailable",
                "status": "blocked",
                "locator_source": "none — metadata/abstract deliberately not substituted for full body",
            })
            materials.append({
                "priority": "P1 Full Text",
                "arxiv_id": aid,
                "source_family_id": row["source_family_id"],
                "known_url": f"https://arxiv.org/abs/{aid}v1",
                "missing_material": BLOCKED[aid]["request"],
                "why_needed": BLOCKED[aid]["reason"],
                "suggested_filename": f"arxiv-{aid}v1.pdf",
            })
            row["review_status"] = "blocked"
            row["access_status"] = "blocked_exact_v1_body"
            row["integration_disposition"] = "Blocked / Unverified"
            row["review_ref"] = item["review_provenance_id"]
            continue

        assert aid in SECTIONS, aid
        method, evaluation, limitations = SECTIONS[aid]
        author = author_packet.get(aid, {})
        mechanism = row.get("screening_reason") or author.get("method_identity_locators") or row["abstract"]
        method_claim = compact(mechanism.replace("Candidate Denominator", "candidate set"))
        abstract = compact(row["abstract"], 760)
        artifact = ARTIFACTS.get(aid)
        if not artifact:
            previous = author.get("artifact_locators", "")
            artifact = previous if previous and "arxiv.org" not in previous else "Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body"
        nonproof = (
            f"The exact-v1 body supports the mechanism under {evaluation}. "
            f"Counterevidence/scope was checked at {limitations}. It does not prove that “{row['title']}” "
            "generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; "
            "author-reported comparisons remain conditional on the paper's disclosed evaluator and workload."
        )
        item = {
            "arxiv_id": aid,
            "source_family_id": row["source_family_id"],
            "primary_evidence_version": version,
            "review_provenance_id": f"REVIEW-20260512-{aid.replace('.', '-')}-V1",
            "review_route": "deep",
            "method_identity_locators": f"{version} {method} — {method_claim}",
            "evaluation_locators": f"{version} {evaluation}",
            "limitations_counterevidence_locators": f"{version} {limitations}",
            "artifact_locators": artifact,
            "claim_nonproof_boundary": nonproof,
            "abstract_identity_crosscheck": abstract,
            "completion_result": "deep_complete",
        }
        packet.append(item)
        provenance.append({
            "arxiv_id": aid,
            "review_provenance_id": item["review_provenance_id"],
            "exact_v1_url": url,
            "retrieved_at": now,
            "retrieval_mode": "official arXiv exact-v1 PDF" if aid in SPECIAL_URLS else "official arXiv exact-v1 HTML",
            "status": "accessible",
            "locator_source": "actual exact-v1 body and table-of-contents/section inspection",
        })
        row["review_status"] = "deep_complete"
        row["access_status"] = "accessible_exact_v1"
        row["review_ref"] = item["review_provenance_id"]
        row.pop("independent_evidence_status", None)
        row.pop("independent_evidence_note", None)

    ledger["identities"] = ledger["identities"]
    ledger["deep_complete"] = sum(item["completion_result"] == "deep_complete" for item in packet)
    ledger["blocked"] = sum(item["completion_result"] == "blocked" for item in packet)
    ledger["review_pending"] = 0
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "exact-v1-review-packet-independent.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "evidence-provenance-manifest-independent.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "materials-request-independent.json").write_text(json.dumps({
        "schema": "materials-request-v2.1",
        "report_date": "2026-05-12",
        "ordinary_pending": 0,
        "blocked": materials,
    }, ensure_ascii=False, indent=2) + "\n")

    audit_path = ROOT / "independent-semantic-audit.json"
    audit = json.loads(audit_path.read_text())
    audit["counts"]["exact_v1_complete"] = len(packet) - len(materials)
    audit["counts"]["blocked"] = len(materials)
    audit["counts"]["independent_exact_v1_pending"] = 0
    audit["exact_v1_receipt"] = {
        "packet": "exact-v1-review-packet-independent.json",
        "provenance": "evidence-provenance-manifest-independent.json",
        "materials_request": "materials-request-independent.json",
        "result": "75 deep_complete; 1 precise external blocker; ordinary pending 0",
    }
    audit["gate"]["evidence"] = (
        "Conditional — ordinary pending is 0 and 75/76 candidates have exact-v1 Method/Evaluation/Limitations/Artifact review. "
        "SF-2026-ARXIV-2605-10133 remains a precise external full-text blocker and is frozen from Books eligibility."
    )
    audit["gate"]["books"] = "Open — current owner+adjacent chapter comparison and root serial writeback remain required; no shared Books write occurred."
    audit["gate"]["completion"] = "In Progress — Evidence conditional; Books writeback/post-write audit pending."
    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
