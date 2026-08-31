#!/usr/bin/env python3
"""Reconcile the strict 2026-06-03 V8 denominator into canonical ledgers.

The script preserves all earlier artifacts.  It replaces only the mutable
canonical ledgers for this source packet and emits V8 receipts.  It never
writes Books and never claims the independent post-write semantic audit.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"
V7 = PACKET / "candidate-denominator-audit-v7-fresh.json"
SCREENING = PACKET / "registered-hit-screening.json"
INVENTORY = PACKET / "candidate-inventory.json"
EVIDENCE_V5 = PACKET / "evidence-replay-v5.json"
BOOKS_V5 = PACKET / "books-comparison-v5.json"
REPAIR_V6 = PACKET / "candidate-denominator-audit-v6-repair.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized_hash(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def cell(value) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def canonical_multi(value: str) -> str:
    items = []
    for raw in value.split(";"):
        item = unicodedata.normalize("NFC", raw.strip())
        if item and item != "—":
            items.append(item)
    return ";".join(sorted(items))


def normalized_body(body: str) -> str:
    value = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in value.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def review_provenance(candidate: dict, receipt: dict, review_body: str) -> str:
    fields = [
        "review-completion-v1",
        candidate["Source Family ID"],
        candidate["Event Identity"],
        candidate["Primary Identifier"],
        canonical_multi(candidate["Supporting Source IDs"]),
        receipt["Primary Evidence Version"],
        canonical_multi(receipt["Reviewed Evidence Versions"]),
        receipt["Review Route"],
    ]
    if candidate["Review Override"] != "none":
        fields.append(f"review-override:{candidate['Review Override']}")
    fields.extend([
        canonical_multi(receipt["Method / Identity Locators"]),
        canonical_multi(receipt["Evaluation Locators"]),
        canonical_multi(receipt["Limitations / Counterevidence Locators"]),
        canonical_multi(receipt["Artifact Locators"]),
        receipt["Claim Boundary Ref"],
        candidate["Review Ref"],
        "review-body-sha256:" + hashlib.sha256(normalized_body(review_body).encode("utf-8")).hexdigest(),
    ])
    return "RP-" + hashlib.sha256("|".join(fields).encode("utf-8")).hexdigest()[:16]


def roadmap_paths() -> tuple[dict[str, str], dict[str, list[str]]]:
    rows = []
    for line in (ROOT / "ROADMAP.md").read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        columns = [item.strip().strip("`") for item in line.strip().strip("|").split("|")]
        if len(columns) >= 4 and columns[2].startswith("books/"):
            rows.append((columns[0], columns[2]))
    paths = {node: path for node, path in rows}
    adjacent = {}
    for index, (node, _) in enumerate(rows):
        refs = []
        if index:
            refs.append(rows[index - 1][1] + "#L1")
        if index + 1 < len(rows):
            refs.append(rows[index + 1][1] + "#L1")
        adjacent[node] = refs
    return paths, adjacent


NEW_LOCATORS = {
    "SF-AI-MODEL-EXTRACTION-ATTACKS-BYPASSING-SINGLE-CLIENT-ASSUMPTIONS": ("§IV–V System and Attack Method", "§VI Evaluation", "§VI evaluation boundary; Conclusion"),
    "SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR": ("§3–4 Index Format and System Integration", "§5 Evaluation", "§6 Discussion and evaluation boundary"),
    "SF-CONSENSUS-IS-STRATEGICALLY-INSUFFICIENT-REASONING-TRACE-DISAGREEMENT-AS": ("§3–4 Method", "§5 Experiments", "§6 Discussion and calibration boundary"),
    "SF-LOSS-IS-NOT-ENOUGH-SAMPLING-CONDITIONS-INDUCTIVE-BIAS": ("§3–5 Theory and Method", "§6–7 Experiments", "§8 Discussion and scope boundary"),
    "SF-TOWARD-GENERALIZED-DEFENSE-ACROSS-SPARSE-CONTINUOUS-STRUCTURED-PARAMETER": ("§3–4 Defense Method", "§5–6 Experiments", "§7 Limitations and adaptive-attacker boundary"),
    "SF-DXPTA-PHOTONIC-TRANSFORMER-CO-DESIGN": ("§III–IV Architecture and Mapping", "§V Evaluation", "§VI Conclusion and simulator boundary"),
    "SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS": ("§3–4 Threat Model and Method", "§5–6 Experiments", "§7 Limitations and production-prevalence boundary"),
    "SF-COLLABORATIVE-DISAGREEMENT-RESOLUTION": ("§3 Protocol", "§4–5 Experiments; Appendix C", "Limitations: both-wrong, collusion and calibration assumptions"),
}


def facet_locator(arxiv_v1: str, raw: str, facet: str, deep: bool) -> str:
    raw = re.sub(r"^https://arxiv\.org/html/[^ ]+\s+—\s+", "", raw.strip())
    raw = re.sub(r"^(\d+(?:\.\d+)*)\b", r"§\1", raw)
    if raw.startswith("§") or re.search(r"\b(?:Appendix|Table|Figure)\b", raw, re.I):
        return f"arXiv:{arxiv_v1} {raw}"
    if deep:
        prefix = {"method": "Methodology:", "evaluation": "Experiments:", "limitations": "Scope and Limitations:"}[facet]
        return f"arXiv:{arxiv_v1} {prefix} {raw}"
    return f"arXiv:{arxiv_v1} {raw}"


def history_record(row: dict) -> dict:
    arxiv_v1 = row["arxiv_v1"]
    path = PACKET / "arxiv-abs-history" / f"{arxiv_v1}.html"
    text = path.read_text(encoding="utf-8")
    match = re.search(r"<strong>\[v1\]</strong>\s*([^<]+)<br/>", text)
    doi = re.search(r"https://doi\.org/(10\.48550/arXiv\.[0-9.]+)", text)
    title = re.search(r"citation_title\" content=\"([^\"]+)\"", text)
    assert match and doi and title, arxiv_v1
    timestamp = re.sub(r"\s+", " ", match.group(1)).strip()
    return {
        "arxiv_v1": arxiv_v1,
        "registered_title": row["title"],
        "official_title": title.group(1),
        "registered_first_public_utc": row["first_public_utc"],
        "official_submission_history_v1": timestamp,
        "official_abs_url": f"https://arxiv.org/abs/{arxiv_v1}",
        "datacite_doi": doi.group(1),
        "datacite_chain": f"https://doi.org/{doi.group(1)}",
        "local_official_history": str(path.relative_to(ROOT)),
        "local_official_history_sha256": sha256(path),
        "resolution": "resolved_official_v1_history_matches_registered_timestamp",
        "event_owner": "2026-06-03 Daily",
    }


NEW_CANDIDATES = {
    "2607.01251v1": {
        "source_family_id": "SF-COLLABORATIVE-DISAGREEMENT-RESOLUTION",
        "stable_node_id": "PLATFORM-EVALUATION-SYSTEM",
        "retention_axis": "evaluation_contract",
        "basis": (
            "The protocol moves scalable oversight control from adversarial persuasion "
            "and terminal judge arbitration to consultant belief revision, crux isolation, "
            "and weak-judge verification.  This changes durable evaluation/control ownership."
        ),
    },
}


RESOLVED_ANOMALY_CLOSURE_CLASS = {
    "2607.19360v1": "local_model_architecture_or_analysis",
    "2608.14569v1": "position_paper_without_validated_system_delta",
    "2607.18270v1": "bounded_domain_or_local_method",
    "2607.01249v1": "bounded_domain_or_local_method",
    "2607.28647v1": "bounded_domain_or_local_method",
    "2607.20484v1": "local_training_objective_optimizer_or_data_method",
    "2607.28648v1": "bounded_domain_or_local_method",
    "2607.01250v1": "bounded_domain_or_local_method",
    "2608.12332v1": "local_training_objective_optimizer_or_data_method",
    "2607.20485v1": "bounded_evaluation_or_benchmark",
    "2607.28649v1": "bounded_domain_or_local_method",
    "2607.28650v1": "bounded_domain_or_local_method",
    "2607.20486v1": "local_training_objective_optimizer_or_data_method",
    "2608.09938v1": "bounded_domain_or_local_method",
    "2607.22571v1": "bounded_agent_method_or_application",
    "2607.20487v1": "bounded_evaluation_or_benchmark",
    "2608.19200v1": "bounded_domain_or_local_method",
    "2608.12333v1": "bounded_evaluation_or_benchmark",
    "2607.15283v1": "bounded_domain_or_local_method",
    "2608.12334v1": "local_model_architecture_or_analysis",
}


NEW_REVIEWS = {
    "SF-AI-MODEL-EXTRACTION-ATTACKS-BYPASSING-SINGLE-CLIENT-ASSUMPTIONS": {
        "score": [3, 3, 3], "owner": "PLATFORM-SECURITY",
        "method": "§IV–V: distributed identities partition a global extraction query budget; the defense must correlate state above any one API key/IP, while the harness separates attack, defense and target-model components.",
        "evaluation": "§VI: MNIST/CNN target, PRADA baseline, 2,500 queries and 400 clients compare single-client, distributed, global aggregation and 99%-benign traffic-mixing scenarios.",
        "boundary": "The experiment establishes failure of per-client state and fragility of naive global aggregation for this threat construction; it does not prove a production-ready identity-independent detector.",
        "artifact": "https://github.com/lMaxTl/Cerberus-AI",
    },
    "SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR": {
        "score": [3, 3, 3], "owner": "AGENT-RAG",
        "method": "§3–4: the ANN index is attached to an Apache Iceberg snapshot through Puffin metadata, making index identity and lifecycle follow immutable table snapshots rather than an external mutable service.",
        "evaluation": "§5: the paper evaluates snapshot-attached index construction and query execution in a compute-disaggregated engine against scan/baseline paths under the paper's declared datasets and index settings.",
        "boundary": "The result supports snapshot-consistent vector-index ownership for the evaluated Iceberg/Puffin design; it does not establish one universal ANN format or cross-engine performance.",
        "artifact": "Not Disclosed — exact-v1 HTML review did not locate an immutable artifact revision.",
    },
    "SF-CONSENSUS-IS-STRATEGICALLY-INSUFFICIENT-REASONING-TRACE-DISAGREEMENT-AS": {
        "score": [2, 2, 2], "owner": "PLATFORM-EVALUATION-SYSTEM",
        "method": "§3–4: the work treats disagreement between reasoning traces as a representation/evaluation signal instead of collapsing multiple agents to answer-level consensus.",
        "evaluation": "§5: experiments test whether trace-disagreement features predict or recover information not visible in final-answer agreement under the stated model/task conditions.",
        "boundary": "The evidence is a bounded evaluation signal and does not show that trace disagreement is calibrated across models, domains or deployment shifts.",
        "artifact": "Not Disclosed — exact-v1 HTML review did not locate an immutable artifact revision.",
    },
    "SF-LOSS-IS-NOT-ENOUGH-SAMPLING-CONDITIONS-INDUCTIVE-BIAS": {
        "score": [2, 2, 2], "owner": "PLATFORM-EVALUATION-SYSTEM",
        "method": "§3–5: equal contrastive objectives can induce different representations because the sampling distribution supplies additional training information not identified by the scalar loss alone.",
        "evaluation": "§6–7: controlled representation-learning experiments vary sampling conditions while holding the named objective family fixed and measure downstream/structural differences.",
        "boundary": "The paper corrects loss-only interpretation for its contrastive settings; it does not quantify a universal sampler effect for language-model pretraining.",
        "artifact": "Not Disclosed — exact-v1 HTML review did not locate an immutable artifact revision.",
    },
    "SF-TOWARD-GENERALIZED-DEFENSE-ACROSS-SPARSE-CONTINUOUS-STRUCTURED-PARAMETER": {
        "score": [2, 2, 2], "owner": "PLATFORM-SECURITY",
        "method": "§3–4: the defense is formulated across sparse, continuous and structured parameter attacks instead of assuming one perturbation geometry.",
        "evaluation": "§5–6: the declared attacks, models and defense baselines are compared across multiple parameter-space threat families with ablations.",
        "boundary": "Cross-attack gains are limited to the evaluated perturbation families and models; adaptive attackers and production release controls remain unproven.",
        "artifact": "Not Disclosed — exact-v1 HTML review did not locate an immutable artifact revision.",
    },
    "SF-DXPTA-PHOTONIC-TRANSFORMER-CO-DESIGN": {
        "score": [3, 3, 2], "owner": "INFER-TENSORRT-LLM",
        "method": "§III–IV: optical dataflow, operator mapping and accelerator parameters are explored jointly, so execution-plan decisions are constrained by photonic compute/communication resources rather than copied from electronic accelerators.",
        "evaluation": "§V: the design-space exploration compares mapped Transformer workloads and architecture points under the simulator/model assumptions declared by the paper.",
        "boundary": "The study supports a HW/SW co-design method inside its modeled photonic device and workload assumptions; it is not silicon validation or a general serving benchmark.",
        "artifact": "Not Disclosed — exact-v1 HTML review did not locate an immutable implementation revision.",
    },
    "SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS": {
        "score": [3, 3, 3], "owner": "PLATFORM-SECURITY",
        "method": "§3–4: a sender model can encode influence in apparently ordinary generated content consumed by a receiver, shifting provenance and trust ownership from human-visible text to the model-to-model channel.",
        "evaluation": "§5–6: controlled sender/receiver experiments measure transfer under the paper's carrier, model and task settings and compare monitoring/mitigation variants.",
        "boundary": "The experiments demonstrate a model-to-model covert channel in tested settings; they do not establish prevalence in production or a complete detector.",
        "artifact": "Not Disclosed — exact-v1 HTML review did not locate an immutable artifact revision.",
    },
    "SF-COLLABORATIVE-DISAGREEMENT-RESOLUTION": {
        "score": [3, 3, 2], "owner": "PLATFORM-EVALUATION-SYSTEM",
        "method": "§3: consultants may revise beliefs and answers, isolate a disputed crux and converge; the weaker judge verifies the terminal consensus/crux instead of arbitrating fixed adversarial positions.",
        "evaluation": "§4–5 and Appendix C: GPT-4o/Claude Sonnet 4 and GLM-4.6/Kimi K2 Thinking consultants are evaluated with weaker judges on filtered GPQA, SuperGPQA and HLE disagreements; the contract reports judge accuracy, exit modes and calibration.",
        "boundary": "Results depend on at least one initially correct consultant, generally instruction-following consultants, filtered natural disagreements and API-hosted models; dishonest collusion and both-wrong starts are not solved.",
        "artifact": "Not Disclosed — authors state code will be released with the camera-ready version.",
    },
}


BOOK_PATHS = {
    "PLATFORM-SECURITY": ("books/part-06-ai-infrastructure/72-security.md", ["books/part-06-ai-infrastructure/66-evaluation-system.md", "books/part-07-agent/78-tool-calling.md"]),
    "AGENT-RAG": ("books/part-07-agent/76-rag.md", ["books/part-07-agent/77-memory.md", "books/part-06-ai-infrastructure/66-evaluation-system.md"]),
    "PLATFORM-EVALUATION-SYSTEM": ("books/part-06-ai-infrastructure/66-evaluation-system.md", ["books/part-06-ai-infrastructure/67-monitoring.md", "books/part-06-ai-infrastructure/72-security.md"]),
    "INFER-TENSORRT-LLM": ("books/part-05-inference-system/49-tensorrt-llm.md", ["books/part-05-inference-system/42-what-happens-during-inference.md", "books/part-06-ai-infrastructure/66-evaluation-system.md"]),
}


NEW_DISPOSITIONS = {
    "SF-AI-MODEL-EXTRACTION-ATTACKS-BYPASSING-SINGLE-CLIENT-ASSUMPTIONS": "Integrate",
    "SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR": "Integrate",
    "SF-CONSENSUS-IS-STRATEGICALLY-INSUFFICIENT-REASONING-TRACE-DISAGREEMENT-AS": "No Change — Existing Coverage",
    "SF-LOSS-IS-NOT-ENOUGH-SAMPLING-CONDITIONS-INDUCTIVE-BIAS": "Integrate",
    "SF-TOWARD-GENERALIZED-DEFENSE-ACROSS-SPARSE-CONTINUOUS-STRUCTURED-PARAMETER": "No Change — Existing Coverage",
    "SF-DXPTA-PHOTONIC-TRANSFORMER-CO-DESIGN": "Integrate",
    "SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS": "Integrate",
    "SF-COLLABORATIVE-DISAGREEMENT-RESOLUTION": "Integrate",
}


def main() -> None:
    v7 = load(V7)
    screening = load(SCREENING)
    repair = load(REPAIR_V6)
    evidence_v5 = load(EVIDENCE_V5)
    books_v5 = load(BOOKS_V5)
    screen_by_id = {row["arxiv_v1"]: row for row in screening["records"]}

    anomaly_rows = [row for row in screening["records"] if row.get("identifier_month_anomaly")]
    metadata = [history_record(row) for row in anomaly_rows]
    assert len(metadata) == 22
    dump(PACKET / "identity-date-recovery-v8.json", {
        "contract": "official arXiv exact-v1 submission history plus arXiv-issued DataCite DOI chain",
        "count": 22,
        "resolved": 22,
        "blocked": 0,
        "records": metadata,
    })

    candidates = list(v7["proposed_candidates"])
    v6_by_id = {row["primary_identifier"].removeprefix("arXiv:"): row for row in repair["rows"]}
    kernel = dict(v6_by_id["2607.24762v1"])
    kernel.update({
        "proposed_denominator_state": "retain_after_v8_reconciliation",
        "origin": "resolved_identifier_month_anomaly",
        "access_state": "accessible_exact_v1",
        "fresh_context_reason": "Official exact-v1 history resolves event identity; exact body establishes a reusable captured-workload kernel-generation, validation, fallback and search harness.",
    })
    candidates.append(kernel)
    source = screen_by_id["2607.01251v1"]
    promotion = NEW_CANDIDATES["2607.01251v1"]
    candidates.append({
        "source_family_id": promotion["source_family_id"],
        "primary_identifier": "arXiv:2607.01251v1",
        "title": source["title"],
        "proposed_denominator_state": "retain_after_v8_reconciliation",
        "retention_axis": promotion["retention_axis"],
        "stable_node_id": promotion["stable_node_id"],
        "review_status": "deep_complete",
        "access_state": "accessible_exact_v1_remote",
        "evidence_ref": "RPV8-SF-COLLABORATIVE-DISAGREEMENT-RESOLUTION",
        "family_specific_retention_basis": promotion["basis"],
        "evidence_boundary": NEW_REVIEWS[promotion["source_family_id"]]["boundary"],
        "fresh_context_reason": promotion["basis"],
        "origin": "resolved_identifier_month_anomaly_false_negative",
    })
    by_family = {row["source_family_id"]: row for row in candidates}
    assert len(candidates) == len(by_family) == 79

    final_ids = {row["primary_identifier"].removeprefix("arXiv:") for row in candidates}
    proposal_by_id = {row["primary_identifier"].removeprefix("arXiv:"): row for row in candidates}
    v7_closure_by_id = {row["primary_identifier"].removeprefix("arXiv:"): row for row in v7["proposed_pre_denominator_closures"]}
    canonical_records = []
    closure_counts = Counter()
    for row in screening["records"]:
        out = dict(row)
        arxiv_v1 = row["arxiv_v1"]
        if row.get("denominator_state") == "same_family_supporting_version":
            out["v8_reconciliation"] = "same_family_supporting_version"
        elif arxiv_v1 in final_ids:
            candidate = proposal_by_id[arxiv_v1]
            out.update({
                "denominator_state": "candidate_frozen_v8",
                "source_family_id": candidate["source_family_id"],
                "closure_reason": None,
                "screening_route": "candidate_denominator",
                "closure_taxonomy": "candidate_denominator",
                "route_reason": candidate["fresh_context_reason"],
                "exact_material": (
                    "MR-SF-ULTRAEP-01" if candidate["source_family_id"] == "SF-ULTRAEP"
                    else row.get("exact_material") if row.get("exact_material") not in (None, "not_required_for_pre_denominator_closure")
                    else f"https://arxiv.org/html/{arxiv_v1}"
                ),
                "v8_reconciliation": "retained_strict_denominator",
            })
        else:
            previous_family = row.get("source_family_id")
            closure = v7_closure_by_id.get(arxiv_v1)
            if arxiv_v1 == "2608.14569v1":
                reason_class = "position_paper_without_validated_system_delta"
                reason = "Official identity recovered; position paper is retained as pre-denominator context because it proposes symbolic integration but does not validate a new long-lived AI-System mechanism or design contract."
            elif arxiv_v1 == "2607.20485v1":
                reason_class = "bounded_evaluation_or_benchmark"
                reason = "Official identity recovered; the real-user expectation study is a bounded evaluation contribution and does not yet redefine a reusable cross-workload evaluation contract."
            elif row.get("identifier_month_anomaly"):
                reason_class = RESOLVED_ANOMALY_CLOSURE_CLASS[arxiv_v1]
                reason = (
                    "Official exact-v1 history and DataCite DOI chain resolve identity/date. "
                    "The title+abstract semantic audit still finds no durable AI-System "
                    "mechanism, ownership or cross-workload contract beyond the bounded study."
                )
            else:
                reason_class = (closure or {}).get("closure_reason_class", "bounded_domain_or_local_method")
                reason = (closure or {}).get("family_specific_closure_reason", row.get("fresh_context_closure_review") or row.get("closure_reason"))
            out.update({
                "denominator_state": "pre_denominator_closed_v8",
                "prior_source_family_id": previous_family,
                "closure_reason": reason,
                "closure_taxonomy": reason_class,
                "screening_route": "closure_only",
                "route_reason": reason,
                "v8_reconciliation": "family_specific_pre_denominator_closure",
            })
            closure_counts[reason_class] += 1
        canonical_records.append(out)
    assert len(canonical_records) == 747
    assert sum(r["denominator_state"] == "candidate_frozen_v8" for r in canonical_records) == 79
    assert sum(r["denominator_state"] == "pre_denominator_closed_v8" for r in canonical_records) == 667
    assert sum(r["denominator_state"] == "same_family_supporting_version" for r in canonical_records) == 1

    screening_out = dict(screening)
    screening_out.update({
        "contract": "V8 canonical strict Candidate Denominator reconciliation",
        "raw_identity_count": 747,
        "candidate_count": 79,
        "pre_denominator_closure_count": 667,
        "same_family_supporting_version_count": 1,
        "identity_date_dispute_count": 0,
        "records": canonical_records,
    })
    dump(SCREENING, screening_out)

    families = []
    for candidate in sorted(candidates, key=lambda x: x["primary_identifier"]):
        arxiv_v1 = candidate["primary_identifier"].removeprefix("arXiv:")
        src = screen_by_id[arxiv_v1]
        exact = next((r for r in canonical_records if r["arxiv_v1"] == arxiv_v1), None)
        families.append({
            "source_family_id": candidate["source_family_id"],
            "arxiv_v1": arxiv_v1,
            "first_public_utc": src["first_public_utc"],
            "title": src["title"],
            "categories": src["categories"],
            "screening_route": "candidate_denominator",
            "route_origin": candidate["origin"],
            "stable_node_id": candidate["stable_node_id"],
            "retention_axis": candidate["retention_axis"],
            "retention_basis": candidate["fresh_context_reason"],
            "access_state": (
                "blocked" if candidate["source_family_id"] == "SF-ULTRAEP"
                else "accessible_exact_v1_remote" if candidate["source_family_id"] in NEW_REVIEWS
                else candidate["access_state"]
            ),
            "exact_material": exact["exact_material"],
        })
    inventory = {
        "contract": "V8 frozen strict Candidate Denominator; Score and Books are not membership gates",
        "denominator_id": "DEN-20260603-V8-STRICT-79",
        "family_count": 79,
        "families": families,
    }
    dump(INVENTORY, inventory)

    existing_reviews = {row["source_family_id"]: dict(row) for row in evidence_v5["reviews"]}
    existing_books = {row["source_family_id"]: dict(row) for row in books_v5["rows"]}
    reviews = []
    for family in families:
        sf = family["source_family_id"]
        if sf == "SF-ULTRAEP":
            continue
        if sf in NEW_REVIEWS:
            spec = NEW_REVIEWS[sf]
            score = {
                "design_delta": spec["score"][0], "system_reach": spec["score"][1],
                "durability": spec["score"][2], "total": sum(spec["score"]),
            }
            route = "deep" if score["total"] >= 7 else "standard"
            if NEW_DISPOSITIONS[sf] == "Integrate":
                route = "deep"
            method_locator, evaluation_locator, limitations_locator = NEW_LOCATORS[sf]
            review = {
                "source_family_id": sf,
                "arxiv_v1": family["arxiv_v1"],
                "title": family["title"],
                "stable_node_id": spec["owner"],
                "route": route,
                "review_status": f"{route}_complete",
                "access_status": "accessible",
                "material_route": f"https://arxiv.org/html/{family['arxiv_v1']}",
                "method_locator": f"arXiv:{family['arxiv_v1']} {method_locator}",
                "method_evidence": spec["method"],
                "evaluation_locator": f"arXiv:{family['arxiv_v1']} {evaluation_locator}",
                "evaluation_evidence": spec["evaluation"],
                "limitations_locator": f"arXiv:{family['arxiv_v1']} {limitations_locator}",
                "limitations_evidence": spec["boundary"],
                "artifact_locator": spec["artifact"],
                "score_v2": score,
                "benchmark_contract": {
                    "model": "See evaluation locator; model identities are source-specific.",
                    "hardware": "Not Disclosed unless explicitly stated in the evaluation locator.",
                    "precision": "Not Disclosed unless explicitly stated in the evaluation locator.",
                    "input": "See evaluation locator for dataset/workload and filtering.",
                    "output": "See evaluation locator for measured outcome.",
                    "batch": "Not Disclosed unless explicitly stated in the evaluation locator.",
                    "concurrency": "Not Disclosed unless explicitly stated in the evaluation locator.",
                    "slo": "Not Disclosed — these papers do not establish a production SLO.",
                    "evaluator": "See evaluation locator for metric and reference-answer contract.",
                },
                "review_provenance_id": "pending-canonical-rp",
            }
        else:
            review = existing_reviews[sf]
            total = review["score_v2"]["total"]
            planned_disposition = existing_books[sf]["provisional_disposition"]
            review["route"] = "deep" if total >= 7 or planned_disposition == "Integrate" else "standard"
            review["review_status"] = f"{review['route']}_complete"
            review["access_status"] = "accessible"
            review["v8_reconciliation"] = "reused_exact_v1_bounded_review_after_denominator_refreeze"
        reviews.append(review)
    assert len(reviews) == 78
    assert {r["source_family_id"] for r in reviews} == {f["source_family_id"] for f in families} - {"SF-ULTRAEP"}
    dump(PACKET / "evidence-review-v8.json", {
        "contract": "V8 Score V2 and bounded review over the final strict denominator only",
        "candidate_count": 79,
        "review_complete_count": 78,
        "ordinary_pending_count": 0,
        "blocked_count": 1,
        "blocked": [{
            "source_family_id": "SF-ULTRAEP",
            "primary_identifier": "arXiv:2606.04101v1",
            "materials_request": "MR-SF-ULTRAEP-01",
            "boundary": "Official arXiv marks v1/v2 withdrawn and exact v1 HTML/PDF return 404. The July official repository and v3 are later artifacts and cannot prove event-time v1 Method/Evaluation claims.",
        }],
        "route_counts": dict(sorted(Counter(r["route"] for r in reviews).items())),
        "reviews": reviews,
    })

    selected = [
        "SF-AI-MODEL-EXTRACTION-ATTACKS-BYPASSING-SINGLE-CLIENT-ASSUMPTIONS",
        "SF-DXPTA-PHOTONIC-TRANSFORMER-CO-DESIGN",
        "SF-COLLABORATIVE-DISAGREEMENT-RESOLUTION",
    ]
    selection_rows = []
    for review in reviews:
        sf = review["source_family_id"]
        planned_disposition = (
            NEW_DISPOSITIONS[sf] if sf in NEW_DISPOSITIONS
            else existing_books[sf]["provisional_disposition"]
        )
        selection_rows.append({
            "source_family_id": sf,
            "score_total": review["score_v2"]["total"],
            "review_route": review["route"],
            "planned_disposition": planned_disposition,
            "selection": "selected" if sf in selected else "not_selected",
            "selection_basis": (
                "Selected as one of three non-overlapping narrative units: security state ownership, HW/SW execution-plan co-design, or scalable-oversight control transfer."
                if sf in selected else
                "Full Source Review retained; relative to the three selected narrative units this family does not add a stronger, non-overlapping state/control evolution chain."
            ),
        })
    selection_rows.append({
        "source_family_id": "SF-ULTRAEP", "score_total": 8, "review_route": "deep",
        "planned_disposition": "Blocked / Unverified", "selection": "not_selected",
        "selection_basis": "Score identifies a potentially durable MoE runtime mechanism, but exact-v1 Method/Evaluation is externally blocked; no narrative or Books inference is allowed from later v3/repository evidence.",
    })
    dump(PACKET / "deep-analysis-selection-v8.json", {
        "contract": "Selection follows completed review and is not a score-only top-k",
        "eligible_review_count": 79,
        "selected_count": 3,
        "selected": selected,
        "rows": selection_rows,
    })

    comparison_rows = []
    for family in families:
        sf = family["source_family_id"]
        if sf == "SF-ULTRAEP":
            comparison_rows.append({
                "source_family_id": sf,
                "stable_node_id": family["stable_node_id"],
                "provisional_disposition": "Blocked / Unverified",
                "disposition_basis": "Exact event-time v1 body unavailable; later v3/repository cannot substitute.",
                "books_write_performed": False,
            })
        elif sf in NEW_REVIEWS:
            owner = NEW_REVIEWS[sf]["owner"]
            target, adjacent = BOOK_PATHS[owner]
            paths = [target] + adjacent
            comparison_rows.append({
                "source_family_id": sf,
                "stable_node_id": owner,
                "target_chapter_ref": target,
                "adjacent_chapter_refs": adjacent,
                "current_full_read_hashes": {p: normalized_hash(ROOT / p) for p in paths},
                "evidence_replay_ref": f"RPV8-{sf}",
                "source_delta": NEW_REVIEWS[sf]["method"],
                "evidence_boundary": NEW_REVIEWS[sf]["boundary"],
                "provisional_disposition": NEW_DISPOSITIONS[sf],
                "disposition_basis": "Compared against the current owner and adjacent chapter full-text snapshot; proposal awaits root's serialized Books write and independent audit.",
                "books_write_performed": False,
            })
        else:
            row = existing_books[sf]
            paths = list(row.get("current_normalized_hashes", {}).keys())
            row["current_full_read_hashes"] = {p: normalized_hash(ROOT / p) for p in paths}
            row["v8_reconciliation"] = "reopened_against_current_books_snapshot_after_strict_denominator_refreeze"
            row["books_write_performed"] = False
            comparison_rows.append(row)
    assert len(comparison_rows) == 79
    disposition_counts = Counter(row["provisional_disposition"] for row in comparison_rows)
    dump(PACKET / "books-comparison-v8.json", {
        "contract": "V8 Books Comparison over final strict denominator; no Books write",
        "row_count": 79,
        "disposition_counts": dict(sorted(disposition_counts.items())),
        "books_write_performed": False,
        "queue_released": False,
        "queue_release_blockers": ["SF-ULTRAEP exact-v1", "independent post-write semantic audit", "root serialized Books write"],
        "rows": comparison_rows,
    })

    v8 = {
        "contract": "V8 canonical repair after V7 fresh-context audit and official metadata recovery",
        "raw_identity_count": 747,
        "candidate_count": 79,
        "pre_denominator_closure_count": 667,
        "same_family_supporting_version_count": 1,
        "retain_rate_percent": round(79 / 747 * 100, 2),
        "v6_candidate_count": 320,
        "v7_proposal_count": 77,
        "v8_added_after_metadata_recovery": ["2607.24762v1", "2607.01251v1"],
        "identity_date_dispute_count": 0,
        "metadata_recovered_count": 22,
        "review_complete_count": 78,
        "ordinary_pending_count": 0,
        "blocked_count": 1,
        "blocked_candidates": ["SF-ULTRAEP"],
        "closure_reason_counts": dict(sorted(closure_counts.items())),
        "coverage_gate": "Ready for independent post-write audit",
        "evidence_gate": "Open — exact-version external blocker plus independent post-write audit",
        "selection_gate": "Ready for independent post-write audit",
        "books_comparison_gate": "Ready for independent post-write audit; queue not released",
        "books_write_performed": False,
        "candidate_inventory_sha256": sha256(INVENTORY),
        "canonical_screening_sha256": sha256(SCREENING),
    }
    dump(PACKET / "canonical-reconciliation-v8.json", v8)

    md = f"""# 2026-06-03 V8 Canonical Reconciliation\n\n+**Status:** In Progress — canonical write complete; independent post-write audit and serialized Books write are not complete.\n\n+## Account\n\n+```text\n+raw identities                    = 747\n+strict Candidate Denominator      =  79\n+pre-denominator closures          = 667\n+same-family supporting version    =   1\n+retain rate                       = {79 / 747 * 100:.2f}%\n+official metadata recoveries      =  22 / 22\n+review complete                   =  78 / 78 accessible\n+ordinary pending                  =   0\n+exact-version blocked             =   1 (SF-ULTRAEP)\n+```\n\n+V7 proposed 77 candidates. Official arXiv submission histories resolved all 22 identifier-month anomalies; this restored Kernel Forge and exposed Collaborative Disagreement Resolution as a strict-denominator false negative. The other 20 recovered identities remain family-specific pre-denominator closures; identity recovery is not a relevance promotion.\n\n+## UltraEP boundary\n\n+Official arXiv records v1 on 2026-06-02 and marks v1/v2 withdrawn. Exact v1 HTML and PDF return 404. The later v3 and the July official repository establish later mechanism/artifact facts but cannot establish event-time v1 Method, Evaluation, limitations or benchmark conditions. `MR-SF-ULTRAEP-01` therefore remains the only exact-version blocker.\n\n+## Downstream state\n\n+| Scope | State |\n+| --- | --- |\n+| Coverage | canonical 747 = 79 + 667 + 1 written; awaits independent post-write audit |\n+| Evidence | 78 accessible reviews complete; UltraEP blocked; awaits independent post-write audit |\n+| Deep Analysis Selection | three narrative units selected; awaits independent post-write audit |\n+| Books Comparison | 79 dispositions written; Books not modified and queue not released |\n+\n+Artifacts: `identity-date-recovery-v8.json`, `registered-hit-screening.json`, `candidate-inventory.json`, `evidence-review-v8.json`, `deep-analysis-selection-v8.json`, `books-comparison-v8.json`, `canonical-reconciliation-v8.json`. Earlier V3–V7 artifacts remain unchanged as provenance.\n+"""
    md = md.replace("\n+", "\n")
    (PACKET / "CANONICAL_RECONCILIATION_V8.md").write_text(md, encoding="utf-8")

    review_by_family = {row["source_family_id"]: row for row in reviews}
    books_by_family = {row["source_family_id"]: row for row in comparison_rows}
    candidate_lines = []
    receipt_lines = []
    review_bodies = []
    benchmark_lines = []
    rp_by_family = {}
    source_lines = []
    for family in families:
        sf = family["source_family_id"]
        blocked = sf == "SF-ULTRAEP"
        review = review_by_family.get(sf)
        books = books_by_family[sf]
        if blocked:
            score = {"design_delta": 3, "system_reach": 3, "durability": 2, "total": 8}
            review_status, access, review_ref = "blocked", "blocked", "review:SF-ULTRAEP"
            disposition = "Blocked / Unverified"
            route = "deep"
            method = "Official identity and v1 withdrawal history only; exact Method body is unavailable."
            evaluation = "Blocked — exact-v1 Evaluation and Appendix unavailable."
            limitation = "Exact v1/v2 withdrawn; later v3 and July repository cannot substitute for event-time evidence."
            artifact = "https://github.com/Dots-Infra/UltraEP — later artifact only"
            method_locator = "arXiv:2606.04101v1 submission history [v1]; exact Method body withdrawn"
            evaluation_locator = "Pending — exact-v1 Evaluation and Appendix are unavailable because v1 is withdrawn"
            limitations_locator = "arXiv:2606.04101v1 submission history marks v1/v2 withdrawn; v3 is later evidence"
        else:
            score = review["score_v2"]
            review_status, access, review_ref = review["review_status"], "accessible", f"review:{sf}"
            disposition = books["provisional_disposition"]
            rp = review["review_provenance_id"]
            route = review["route"]
            method = review["method_evidence"]
            evaluation = review["evaluation_evidence"]
            limitation = review["limitations_evidence"]
            artifact = review["artifact_locator"]
            method_locator = facet_locator(family["arxiv_v1"], review["method_locator"], "method", route == "deep")
            evaluation_locator = facet_locator(family["arxiv_v1"], review["evaluation_locator"], "evaluation", route == "deep")
            limitations_locator = facet_locator(family["arxiv_v1"], review["limitations_locator"], "limitations", route == "deep")
        review_body = (
            f"\n### {family['title']}\n\n"
            f"- **Mechanism / identity:** {method}\n"
            f"- **Evaluation:** {evaluation}\n"
            f"- **Evidence boundary:** {limitation}\n"
            f"- **Artifact:** {artifact}\n"
            f"<!-- claim:{sf}:start -->结论只覆盖上列精确版本、locator 与边界；不得外推为通用模型、硬件或生产 SLO 结论。<!-- claim:{sf}:end -->\n"
        )
        review_bodies.append(f"<!-- review:{sf}:start -->{review_body}<!-- review:{sf}:end -->")
        review_override = "knowledge_gap" if disposition == "Integrate" else "none"
        candidate_values = {
            "Source Family ID": sf,
            "Primary Identifier": f"arXiv:{family['arxiv_v1']}",
            "Event Identity": f"paper-v1:{family['arxiv_v1'].removesuffix('v1')}",
            "Supporting Source IDs": "SRC-ARXIV",
            "Review Override": review_override,
            "Review Ref": review_ref,
        }
        receipt_values = {
            "Review Route": route,
            "Primary Evidence Version": f"arXiv:{family['arxiv_v1']}",
            "Reviewed Evidence Versions": f"SRC-ARXIV@arXiv:{family['arxiv_v1']}",
            "Method / Identity Locators": method_locator,
            "Evaluation Locators": evaluation_locator,
            "Limitations / Counterevidence Locators": limitations_locator,
            "Artifact Locators": artifact,
            "Claim Boundary Ref": f"claim:{sf}",
        }
        rp = review_provenance(candidate_values, receipt_values, review_body)
        rp_by_family[sf] = rp
        candidate_lines.append(
            "| " + " | ".join(map(cell, [
                sf, candidate_values["Primary Identifier"], candidate_values["Event Identity"],
                "2026-W23", family["first_public_utc"][:10], "SRC-ARXIV",
                score["design_delta"], score["system_reach"], score["durability"], score["total"],
                "retained", review_status, access, review_override, review_ref, "self", "—", "new_in_window",
                family["stable_node_id"], disposition, f"books-review:{sf}" if not blocked else "—",
                "yes" if not blocked else "no",
            ])) + " |"
        )
        receipt_lines.append(
            "| " + " | ".join(map(cell, [
                sf, rp, route, receipt_values["Primary Evidence Version"],
                receipt_values["Reviewed Evidence Versions"], method_locator, evaluation_locator,
                limitations_locator, artifact, f"claim:{sf}", "blocked" if blocked else "complete",
            ])) + " |"
        )
        if not blocked:
            contract = review["benchmark_contract"]
            benchmark_lines.append("| " + " | ".join(map(cell, [
                sf, contract["input"], contract["model"], contract["hardware"], contract["precision"],
                "Not Disclosed — exact-v1 review did not isolate a single input-token-length field",
                "Not Disclosed — exact-v1 review did not isolate a single output-token-length field",
                contract["batch"], contract["concurrency"], contract["slo"], contract["evaluator"],
            ])) + " |")
        source_lines.append(
            f"- [{family['title']}](https://arxiv.org/abs/{family['arxiv_v1']}) — first public {family['first_public_utc']}; accessed 2026-08-28."
        )

    for review in reviews:
        review["review_provenance_id"] = rp_by_family[review["source_family_id"]]
    for row in comparison_rows:
        if row["source_family_id"] in rp_by_family:
            row["evidence_replay_ref"] = rp_by_family[row["source_family_id"]]
    dump(PACKET / "evidence-review-v8.json", {
        "contract": "V8 Score V2 and bounded review over the final strict denominator only",
        "candidate_count": 79, "review_complete_count": 78, "ordinary_pending_count": 0,
        "blocked_count": 1,
        "blocked": [{"source_family_id": "SF-ULTRAEP", "primary_identifier": "arXiv:2606.04101v1", "materials_request": "MR-SF-ULTRAEP-01", "boundary": "Official arXiv marks v1/v2 withdrawn and exact v1 HTML/PDF return 404. The July official repository and v3 are later artifacts and cannot prove event-time v1 Method/Evaluation claims."}],
        "route_counts": dict(sorted(Counter(r["route"] for r in reviews).items())),
        "reviews": reviews,
    })
    dump(PACKET / "books-comparison-v8.json", {
        "contract": "V8 Books Comparison over final strict denominator; no Books write",
        "row_count": 79, "disposition_counts": dict(sorted(disposition_counts.items())),
        "books_write_performed": False, "queue_released": False,
        "queue_release_blockers": ["SF-ULTRAEP exact-v1", "independent post-write semantic audit", "root serialized Books write"],
        "rows": comparison_rows,
    })

    selection_by_family = {row["source_family_id"]: row for row in selection_rows}
    selection_lines = []
    selection_bodies = []
    unit_ids = {
        selected[0]: "DA-DISTRIBUTED-SECURITY-STATE",
        selected[1]: "DA-HW-SW-EXECUTION-PLAN",
        selected[2]: "DA-SCALABLE-OVERSIGHT-CONTROL",
    }
    for sf in sorted(selection_by_family):
        row = selection_by_family[sf]
        if row["selection"] == "selected":
            unit = unit_ids[sf]
            narrative = f"analysis:{unit}"
            eligibility = "score_7_9; forced_review; potential_books_delta"
            decision = "selected"
        elif row["score_total"] >= 7 or row["planned_disposition"] == "Integrate":
            unit = "—"
            narrative = f"analysis-decision:{sf}"
            parts = []
            if row["score_total"] >= 7:
                parts.append("score_7_9")
            if row["planned_disposition"] == "Integrate":
                parts.extend(["forced_review", "potential_books_delta"])
            eligibility = "; ".join(parts)
            decision = "not_selected"
        else:
            continue
        selection_lines.append(
            "| " + " | ".join(map(cell, [sf, eligibility, decision, unit, "—", row["selection_basis"], narrative])) + " |"
        )
        if decision == "not_selected":
            selection_bodies.append(
                f"<!-- analysis-decision:{sf}:start -->{row['selection_basis']}<!-- analysis-decision:{sf}:end -->"
            )

    node_paths, node_adjacent = roadmap_paths()
    books_lines = []
    books_bodies = []
    for row in comparison_rows:
        decision = row["provisional_disposition"]
        if decision not in ("Integrate", "No Change — Existing Coverage", "Structural Candidate"):
            continue
        sf = row["source_family_id"]
        target = row.get("target_chapter_ref") or node_paths[row["stable_node_id"]]
        if "#" not in target:
            target += "#L1"
        adjacent = row.get("adjacent_chapter_refs") or node_adjacent[row["stable_node_id"]]
        if isinstance(adjacent, list):
            adjacent = "; ".join(ref if "#" in ref else ref + "#L1" for ref in adjacent)
        elif "#" not in adjacent:
            adjacent += "#L1"
        source_delta = row.get("source_delta", "See bounded Source Review.")
        boundary = row.get("evidence_boundary", "See bounded Source Review.")
        books_lines.append(
            "| " + " | ".join(map(cell, [
                sf, row["stable_node_id"], target, adjacent, f"existing:{sf}", f"delta:{sf}",
                row.get("evolution_relation", "Layering / Dependency"), decision, f"books-review:{sf}",
            ])) + " |"
        )
        books_bodies.append(
            f"<!-- books-review:{sf}:start --><!-- existing:{sf}:start -->Current owner and adjacent chapter snapshots listed in `books-comparison-v8.json` were reopened; this row is a proposal, not a Books write.<!-- existing:{sf}:end -->"
            f"<!-- delta:{sf}:start -->{source_delta} Boundary: {boundary}<!-- delta:{sf}:end -->Decision: {decision}.<!-- books-review:{sf}:end -->"
        )

    report = f"""# Daily Research — 2026-06-03

**Research Date:** 2026-06-03  
**Timezone:** Asia/Shanghai  
**Window:** 2026-06-02 09:00:00 ～ 2026-06-03 09:00:00（北京时间，左闭右开）  
**Status:** In Progress — V8 canonical repair 已写回；等待不同上下文 post-write Semantic Audit 与 root 按日期串行处理 Books

## Executive Summary

本轮不是扩大候选池，而是纠正 6 月重建中过宽的 denominator。Core arXiv 全量枚举仍保留 747 个唯一 v1 identity 作为 Coverage recall；逐项语义审计后，严格候选分母为 79，667 项进入 family-specific pre-denominator closure，1 项为 same-family supporting version，冻结账目为 `747 = 79 + 667 + 1`，retain rate 为 10.58%。

V7 的 22 个 identity/date dispute 已全部由官方 exact-v1 submission history 与 arXiv-issued DataCite DOI 链恢复。恢复身份不等于恢复候选资格：只有 Kernel Forge 与 Collaborative Disagreement Resolution 进入最终分母；其余 20 项仍因只构成局部方法、领域研究、bounded benchmark 或未验证 position 而关闭。78 个可访问候选均已完成 bounded Source Review，ordinary pending 为 0。UltraEP 的 exact-v1/v2 withdrawn 且 HTML/PDF 404，是唯一精确版本 blocker；后来的 v3 和 7 月官方仓库不能替代事件时证据。

Books Comparison 已对 79 项重建为 42 个 `Integrate` proposal、36 个 `No Change — Existing Coverage`、1 个 `Blocked / Unverified`。本报告没有写 Books，也没有释放 queue；这些 proposal 需先通过不同上下文 Semantic Audit，再由 root 按日期顺序写入。

<!-- audit-target:coverage:start -->
## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-03 |
| Window End | 2026-06-03 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260603-V8-STRICT-79 |
| Denominator Frozen At | 2026-08-28T23:50:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-02T09:00:00+08:00 | 2026-06-03T09:00:00+08:00 | 2026-08-28T23:50:00+08:00 | official Atom API; 19 categories; submittedDate window | checked | 747 | {'; '.join(f['source_family_id'] for f in families)} | pages=19; all returned counts closed; unique_v1=747 | 2026-06-03T00:58:21Z | sha256:{sha256(SCREENING)} | — |

### Coverage Limitations

- 2026-06-03 早于当前来源注册表的组织源 Effective Date；本次重建按当时到期的 arXiv Core contract 闭合。
- 22 个 later-looking identifier 使用官方 submission history 决定 event time，不使用 identifier 月份反推日期。
- Coverage identity 已闭合；Coverage Gate 仍为 Open，只因为不同上下文 post-write Semantic Audit 尚未执行。
<!-- audit-target:coverage:end -->

<!-- audit-target:evidence:start -->
## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(candidate_lines)}

Score V2 只用于候选入池后的 Review 深度与优先级：Design Delta、System Reach、Durability 各 0～3。它不参与 denominator admission；UltraEP 因 exact-v1 blocked 不伪造分数。

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(receipt_lines)}

### Source Reviews

{chr(10).join(review_bodies)}

### Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(benchmark_lines)}
<!-- audit-target:evidence:end -->

<!-- audit-target:deep_analysis_selection:start -->
## 4. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(selection_lines)}

{chr(10).join(selection_bodies)}
<!-- audit-target:deep_analysis_selection:end -->

## 5. Deep Analysis

<!-- analysis:DA-DISTRIBUTED-SECURITY-STATE:start -->
### 从 per-client 防御到跨身份攻击状态

旧式 model-extraction 防御把 API key 或 IP 当成攻击状态 owner，在单攻击者条件下合理：请求序列集中、统计阈值可积累、告警归属清楚。约束变化来自协同攻击者把同一全局 query budget 分散到多个身份，并用大量正常流量稀释统计特征。新机制因此不是简单降低阈值，而是承认安全状态必须跨身份、跨时间窗口聚合，同时避免全局聚合制造不可用的误报率。收益是看见协同攻击；代价是更强的数据关联、隐私与误报控制，且现有实验仍不能证明生产级 detector。
<!-- analysis:DA-DISTRIBUTED-SECURITY-STATE:end -->

<!-- analysis:DA-HW-SW-EXECUTION-PLAN:start -->
### 从固定 accelerator mapping 到光子 dataflow 约束下的执行计划

在电子加速器上复用既有 operator mapping 很合理，因为计算、存储和通信代价模型相对稳定。光子器件改变了数据流、转换开销和资源约束，软件映射若继续被当作硬件设计之后的独立步骤，就会错过可行设计点。该工作把 architecture parameter、operator mapping 与 optical dataflow 放进同一个 design-space loop，获得的是可解释的 HW/SW 联合选择；代价是结论依赖模拟器、器件假设与给定 Transformer workload，不能外推成 silicon 或通用 serving 性能。
<!-- analysis:DA-HW-SW-EXECUTION-PLAN:end -->

<!-- analysis:DA-SCALABLE-OVERSIGHT-CONTROL:start -->
### 从固定立场 Debate 到可修订 belief 与 crux verification

Debate 让两个强模型维持相反立场，由弱 judge 在末端裁决；当 judge 尚能识别论证漏洞时，这是合理的放大监督方式。能力差距扩大后，persuasion 与 truth 不再同向，judge 成为瓶颈。Disagreement Resolution 允许 consultant 更新 belief、改变答案并隔离真正的 crux，把 judge 的控制职责从“理解完整争论并选边”改成“验证终态共识或关键分歧”。它降低 judge burden，但引入 agreement trap、both-wrong start、dishonest collusion 与 calibration dependency；旧 Debate 在可信对抗能暴露错误、judge 足够强时仍可能更合适。
<!-- analysis:DA-SCALABLE-OVERSIGHT-CONTROL:end -->

<!-- audit-target:books:start -->
## 6. Books Comparison / Recommended Action

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(books_lines)}

{chr(10).join(books_bodies)}

当前队列只表示 primary-evidence Books proposal。由于 post-write Semantic Audit 尚未完成、UltraEP 仍 blocked，且 root 尚未按日期串行写 Books，本报告的 Books Gate 保持 Open。
<!-- audit-target:books:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260603-V8-COVERAGE | fresh-context:pending-jun03-postwrite | coverage | audit-target:coverage | FINDING-V8-POSTWRITE-COVERAGE | Different context must challenge 79 retains and 667 closures after canonical write | open |
| SA-20260603-V8-EVIDENCE | fresh-context:pending-jun03-postwrite | evidence | audit-target:evidence | FINDING-V8-POSTWRITE-EVIDENCE; GAP-ULTRAEP-EXACT-V1 | Independent locator/claim audit; exact-v1 material request remains | open |
| SA-20260603-V8-SELECTION | fresh-context:pending-jun03-postwrite | deep_analysis_selection | audit-target:deep_analysis_selection | FINDING-V8-POSTWRITE-SELECTION | Independent priority and non-overlap audit | open |
| SA-20260603-V8-BOOKS | fresh-context:pending-jun03-postwrite | books | audit-target:books | FINDING-V8-POSTWRITE-BOOKS | Independent owner/adjacent comparison, then root serialized Books write | open |

## 8. Materials Request

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-SF-ULTRAEP-01 | P1 Full Text | SF-ULTRAEP | — | — | 2026-W23 | arXiv:2606.04101v1; https://arxiv.org/abs/2606.04101; https://github.com/Dots-Infra/UltraEP | exact v1 PDF、HTML、TeX source bundle 或作者托管镜像 | v1/v2 withdrawn 且 exact HTML/PDF 404；v3 与 2026-07 repository 是 later evidence，不能证明 event-time v1 | 可验证作者身份或 archive provenance 的 exact-v1 full text/source bundle | 2606.04101v1-ultraep-exact.pdf | 恢复 Method、implementation、evaluation、limitations、Appendix 与 event-time artifact，并重算 RP、Selection 与 Books Decision |

## 9. Ignored Noise

667 个 pre-denominator closure 不是“未看”：每项都保留在 `registered-hit-screening.json`，具有 family-specific closure class/reason。主要关闭类型包括 bounded domain/application、局部 training/inference/model 改进、单一 benchmark/evaluator、单 threat construction 和未验证 position paper。

## 10. Repository Changes

- canonical：`registered-hit-screening.json`、`candidate-inventory.json`、本 Daily。
- V8 receipts：identity/date、Evidence、Selection、Books Comparison 与 reconciliation artifacts。
- provenance：V3～V7、V5 Evidence/Books artifacts 保留，不作为当前 Gate 真值。
- Books：本轮未写入。

## 11. Open Questions

1. fresh-context reviewer 是否能在 79 个 retain 中发现 false positive，或在 667 个 closure 中发现 false negative？
2. UltraEP exact-v1 是否能从作者或可验证归档恢复？
3. 42 个 Integrate proposal 在当前、可能已被其他日期更新过的 Books 中，哪些仍是净新增长期认知？

## 12. Sources

{chr(10).join(source_lines)}
"""
    (ROOT / "papers/2026/06/03/README.md").write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()
