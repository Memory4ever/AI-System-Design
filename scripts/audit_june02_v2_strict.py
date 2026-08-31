#!/usr/bin/env python3
"""Reconcile the complete 2026-06-02 arXiv identity and denominator ledgers.

This stage deliberately stops before Evidence and Books Gates.  Category Atom
snapshots are the official discovery/provenance surface; candidate exact-v1
full text is reviewed in the next stage.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260602"
OLD = PACKET / "screening-ledger.tsv"
ATOM_DIR = PACKET / "arxiv-v1"
IDENTITY = PACKET / "identity-provenance-v2-strict.json"
DENOM = PACKET / "candidate-denominator-audit-v2-strict.json"
DENOM_MD = PACKET / "CANDIDATE_DENOMINATOR_AUDIT_V2_STRICT.md"
LEDGER = PACKET / "screening-ledger-v2-strict.tsv"
RECOVERY = PACKET / "owner-recovery-ledger-v2-strict.json"

NS = {"a": "http://www.w3.org/2005/Atom"}
WINDOW_START = "2026-06-01T01:00:00Z"
WINDOW_END = "2026-06-02T01:00:00Z"

# Fresh-context decisions.  Membership is not inherited from the old 52-row
# denominator and is not selected by a target ratio or Score V2 threshold.
RETAIN = {
    "2606.01567": ("SF-SKILL-INJECTION-GUARDIAN", "PLATFORM-SECURITY", "security_release_contract"),
    "2606.01600": ("SF-ROBOTRUSTBENCH-WORLD-MODEL", "MULTIMODAL-WORLD-MODELS", "evaluation_contract"),
    "2606.01680": ("SF-OPTCC-ASYMMETRIC-ALLREDUCE", "TRAIN-DISTRIBUTED-TRAINING", "communication_control_state"),
    "2606.01725": ("SF-GAIATRACE-VIDUR-AGENT", "INFER-SCHEDULING", "agentic_serving_evaluation_contract"),
    "2606.01751": ("SF-SPARSEX-SEGMENT-KV", "INFER-KV-CACHE", "runtime_state_identity"),
    "2606.01770": ("SF-ADAPTIVE-AUTO-HARNESS", "AGENT-PLATFORM", "workflow_control_state"),
    "2606.01839": ("SF-CONSERVE-CONVERSATION-PLACEMENT", "INFER-SCHEDULING", "placement_state_ownership"),
    "2606.01850": ("SF-COMPRESSION-UNCERTAINTY", "PLATFORM-EVALUATION-SYSTEM", "evaluation_contract"),
    "2606.01927": ("SF-ASYNC-INFERENCE-OVERHEADS", "INFER-REQUEST-LIFECYCLE", "runtime_control_path"),
    "2606.02060": ("SF-DRIFT-TELBENCH", "PLATFORM-EVALUATION-SYSTEM", "failure_evidence_contract"),
    "2606.02091": ("SF-DFLARE-DIFFUSION-SPECULATION", "INFER-SPECULATIVE-DECODING", "speculative_commit_contract"),
    "2606.02218": ("SF-STRAGGLER-AWARE-RL-GROUP", "TRAIN-GRPO", "distributed_training_control_state"),
    "2606.02302": ("SF-SECLAW-SPEC-DRIVEN-SECURITY", "PLATFORM-SECURITY", "security_evaluation_contract"),
    "2606.02373": ("SF-HARNESS1-EXTERNALIZED-STATE", "AGENT-CONTEXT", "externalized_workflow_state"),
    "2606.02430": ("SF-LLMFI-ERROR-PROPAGATION", "PLATFORM-EVALUATION-SYSTEM", "failure_evidence_contract"),
    "2606.02437": ("SF-PEFT-SCALE", "PLATFORM-MODEL-REGISTRY", "artifact_identity_and_residency"),
    "2606.02483": ("SF-GHOST-TOOL-ISSUE-PRIVACY", "PLATFORM-SECURITY", "tool_effect_authorization"),
    "2606.02540": ("SF-SKILLHARM-LIFECYCLE", "PLATFORM-SECURITY", "skill_lifecycle_trust_contract"),
    "2606.02668": ("SF-CONSENT-INTEGRITY", "PLATFORM-SECURITY", "consent_effect_integrity"),
    "2606.02800": ("SF-COSMOS3-OMNIMODAL", "MULTIMODAL-WORLD-MODELS", "world_state_and_action_contract"),
    "2606.02958": ("SF-ECHELON-AGGREGATE-ONLY-ADAPTATION", "TRAIN-DISTRIBUTED-TRAINING", "privacy_boundary_training_state"),
    "2606.02959": ("SF-GATEAI-OPERATING-POINT-EVAL", "PLATFORM-EVALUATION-SYSTEM", "security_operating_point_contract"),
    "2606.02963": ("SF-KFORGE-CROSS-PLATFORM-KERNEL", "INFER-TENSORRT-LLM", "execution_plan_portability"),
    "2606.02982": ("SF-DRIFTSCHED-TOKEN-DRIFT", "INFER-SCHEDULING", "runtime_drift_control_state"),
    "2606.09864": ("SF-KV-QUANT-ALIGNMENT-COLLAPSE", "INFER-KV-CACHE", "serving_evaluation_contract"),
    "2606.28343": ("SF-CROWDED-EMBEDDING-EXTERNALITY", "AGENT-RAG", "shared_retrieval_state_externality"),
    "2607.22569": ("SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY", "PLATFORM-SECURITY", "execution_evidence_contract"),
}


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip().strip('"')


def title_key(value: str) -> str:
    return re.sub(r"[\"“”]", "", norm(value))


def base_id(identifier: str) -> str:
    return re.sub(r"v\d+$", "", identifier.removeprefix("arXiv:"))


def closure_class(title: str, abstract: str) -> str:
    text = f"{title} {abstract}".lower()
    if any(x in text for x in ("survey", "position paper", "taxonomy", "benchmark")):
        return "bounded_benchmark_survey_or_position"
    if any(x in text for x in ("medical", "clinical", "molecule", "protein", "weather", "agriculture")):
        return "domain_application_without_portable_system_contract"
    if any(x in text for x in ("attack", "jailbreak", "safety", "privacy", "secure")):
        return "scoped_security_method_without_release_contract_delta"
    if any(x in text for x in ("quantization", "pruning", "token reduction", "layer skipping", "fine-tuning")):
        return "local_model_or_optimization_delta"
    if any(x in text for x in ("agent", "tool", "memory", "rag", "retrieval")):
        return "bounded_agent_or_retrieval_method"
    if any(x in text for x in ("world model", "robot", "multimodal", "vision-language", "video")):
        return "bounded_multimodal_or_embodied_method"
    return "ai_relevant_but_no_durable_system_delta"


def family_reason(row: dict, abstract: str, cls: str) -> str:
    mechanisms = {
        "bounded_benchmark_survey_or_position": "its scope is a bounded benchmark, survey, or position and does not establish a reusable cross-workload evaluation or release contract",
        "domain_application_without_portable_system_contract": "its contribution remains domain-specific and does not transfer a durable state/data/control ownership rule",
        "scoped_security_method_without_release_contract_delta": "its threat or defense is scoped to a model/workload and does not change the durable authorization, mediation, or release contract",
        "local_model_or_optimization_delta": "its gain is a local model or optimization delta and does not change runtime/training state ownership or a platform design judgment",
        "bounded_agent_or_retrieval_method": "its method is bounded to an agent or retrieval task and does not define a reusable information/action/workflow-state contract",
        "bounded_multimodal_or_embodied_method": "its model/task delta does not redefine representation identity, mutable world state, or physical action authority",
        "ai_relevant_but_no_durable_system_delta": "the abstract does not establish a durable AI-System mechanism, ownership boundary, evaluation contract, or Books correction",
    }
    excerpt = norm(abstract)[:220]
    return f"{row['Title']}: closed before the Candidate Denominator because {mechanisms[cls]}. Abstract challenge: {excerpt}"


def load_atom() -> tuple[dict[str, dict], dict[str, list[str]]]:
    by_base: dict[str, dict] = {}
    sources: dict[str, list[str]] = defaultdict(list)
    for path in sorted(ATOM_DIR.glob("*.atom")):
        if path.name == "window.atom":
            continue
        root = ET.parse(path).getroot()
        for entry in root.findall("a:entry", NS):
            raw_id = entry.findtext("a:id", default="", namespaces=NS).split("/")[-1]
            base = base_id(raw_id)
            sources[base].append(path.name)
            record = {
                "observed_version": raw_id,
                "title": norm(entry.findtext("a:title", default="", namespaces=NS)),
                "abstract": norm(entry.findtext("a:summary", default="", namespaces=NS)),
                "published_utc": entry.findtext("a:published", default="", namespaces=NS),
                "updated_utc": entry.findtext("a:updated", default="", namespaces=NS),
            }
            prior = by_base.get(base)
            if prior is None or int(re.search(r"v(\d+)$", raw_id).group(1)) < int(re.search(r"v(\d+)$", prior["observed_version"]).group(1)):
                by_base[base] = record
    return by_base, sources


def main() -> None:
    old_rows = list(csv.DictReader(OLD.open(encoding="utf-8"), delimiter="\t"))
    assert len(old_rows) == 736
    atom, atom_sources = load_atom()
    assert {base_id(r["Primary Identifier"]) for r in old_rows} == set(atom)

    identities = []
    recovered = []
    denominator = []
    closure_counts: Counter[str] = Counter()
    output_rows = []
    old_candidate_ids = {base_id(r["Primary Identifier"]) for r in old_rows if r["Screening State"] == "routed_candidate"}
    for row in old_rows:
        base = base_id(row["Primary Identifier"])
        entry = atom[base]
        title_match = title_key(row["Title"]) == title_key(entry["title"])
        published_match = row["Published UTC"] == entry["published_utc"]
        in_window = WINDOW_START <= entry["published_utc"] < WINDOW_END
        exact = f"{base}v1"
        identity = {
            "primary_identifier": f"arXiv:{exact}",
            "title": row["Title"],
            "official_atom_published_utc": entry["published_utc"],
            "official_atom_observed_version": entry["observed_version"],
            "arxiv_doi": f"10.48550/arXiv.{base}",
            "official_abs_history_url": f"https://arxiv.org/abs/{base}",
            "official_exact_v1_url": f"https://arxiv.org/html/{exact}",
            "atom_snapshot_files": sorted(set(atom_sources[base])),
            "title_match": title_match,
            "published_match": published_match,
            "in_window": in_window,
            "identity_status": "verified_official_atom_submission_metadata" if title_match and published_match else "disputed",
            "boundary": "Atom published is the official first-submission timestamp; observed_version may be a later revision and is not candidate claim evidence.",
        }
        identities.append(identity)
        if not in_window:
            recovered.append({**identity, "recovery_action": "move_to_true_first_public_owner"})

        if in_window and base in RETAIN:
            family, owner, axis = RETAIN[base]
            decision = "retained"
            closure = "—"
            denominator.append({
                "source_family_id": family,
                "primary_identifier": f"arXiv:{exact}",
                "title": row["Title"],
                "published_utc": entry["published_utc"],
                "stable_node_id": owner,
                "retention_axis": axis,
                "origin": "old_candidate" if base in old_candidate_ids else "false_negative_recovery",
                "evidence_status": "pending_exact_v1_rebuild",
                "books_status": "pending_comparison",
            })
        else:
            cls = "out_of_window" if not in_window else closure_class(row["Title"], entry["abstract"])
            closure_counts[cls] += 1
            decision = "pre_denominator_closure" if in_window else "owner_recovery"
            closure = family_reason(row, entry["abstract"], cls) if in_window else f"Official first-submission time {entry['published_utc']} is outside the report window; move to true owner."
        output_rows.append({
            "Primary Identifier": f"arXiv:{exact}",
            "Published UTC": entry["published_utc"],
            "Title": row["Title"],
            "Abstract SHA256-16": hashlib.sha256(entry["abstract"].encode()).hexdigest()[:16],
            "Identity Status": identity["identity_status"],
            "Denominator State": decision,
            "Source Family ID": RETAIN[base][0] if in_window and base in RETAIN else "—",
            "Stable Node ID": RETAIN[base][1] if in_window and base in RETAIN else "—",
            "Closure / Retention Basis": f"Retained on axis {RETAIN[base][2]}; exact-v1 Evidence review required." if in_window and base in RETAIN else closure,
        })

    assert all(x["identity_status"] == "verified_official_atom_submission_metadata" for x in identities)
    assert not recovered
    assert len(denominator) == len(RETAIN)
    promoted = [x for x in denominator if x["origin"] == "false_negative_recovery"]
    downgraded = sorted(old_candidate_ids - set(RETAIN))

    IDENTITY.write_text(json.dumps({
        "schema_version": "identity-provenance-v2-strict",
        "window_utc": f"[{WINDOW_START}, {WINDOW_END})",
        "raw_count": len(identities),
        "verified_count": sum(x["identity_status"].startswith("verified") for x in identities),
        "disputed_count": sum(x["identity_status"] == "disputed" for x in identities),
        "out_of_window_count": len(recovered),
        "records": identities,
    }, ensure_ascii=False, indent=2) + "\n")
    RECOVERY.write_text(json.dumps({"schema_version": "owner-recovery-v2-strict", "records": recovered}, ensure_ascii=False, indent=2) + "\n")
    DENOM.write_text(json.dumps({
        "schema_version": "candidate-denominator-v2-strict",
        "raw_count": len(old_rows),
        "old_retained_count": len(old_candidate_ids),
        "new_retained_count": len(denominator),
        "new_retain_rate_percent": round(len(denominator) / len(old_rows) * 100, 2),
        "downgraded_old_candidate_count": len(downgraded),
        "promoted_false_negative_count": len(promoted),
        "closure_count": len(old_rows) - len(denominator),
        "closure_reason_counts": dict(sorted(closure_counts.items())),
        "candidates": denominator,
        "downgraded_old_candidate_base_ids": downgraded,
        "promoted_false_negatives": promoted,
        "gate_truth": "Denominator frozen provisionally; Evidence and Books remain open.",
    }, ensure_ascii=False, indent=2) + "\n")
    with LEDGER.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0]), delimiter="\t")
        writer.writeheader(); writer.writerows(output_rows)

    reason_rows = "\n".join(f"| `{k}` | {v} |" for k, v in sorted(closure_counts.items()))
    candidate_rows = "\n".join(f"| `{x['source_family_id']}` | `{x['primary_identifier']}` | `{x['stable_node_id']}` | `{x['retention_axis']}` | `{x['origin']}` |" for x in denominator)
    DENOM_MD.write_text(f"""# 2026-06-02 Candidate Denominator V2 Strict Audit

## Identity / Date Result

- Raw identities: 736/736.
- Official Atom submission metadata + arXiv DOI provenance verified: 736/736.
- Title/timestamp disputes: 0.
- Out-of-window owner recovery: 0.
- Important boundary: an identifier prefix or high sequence is not a date. The official `published` timestamp owns first-public routing; later `observed_version` metadata is not claim evidence.

## Denominator Result

- Old denominator: {len(old_candidate_ids)}.
- Strict denominator: {len(denominator)} ({len(denominator) / len(old_rows) * 100:.2f}%).
- Old candidates downgraded: {len(downgraded)}.
- False negatives promoted: {len(promoted)}.
- Pre-denominator closures: {len(old_rows) - len(denominator)}.

The ratio is an outcome, not a quota. All 736 rows were challenged against the durable AI-System admission rule. ROADMAP mappability, AI relevance, local model improvements, domain benchmarks, and abstract-only novelty were insufficient.

## Closure Reasons

| Reason class | Count |
| --- | ---: |
{reason_rows}

## Provisional Frozen Candidate Set

| Source Family | Primary identifier | Owner | Retention axis | Origin |
| --- | --- | --- | --- | --- |
{candidate_rows}

## Gate Truth

Identity and denominator audits are complete. Evidence, Score V2, benchmark contracts, Deep Analysis Selection, Books Comparison, serial Books writeback, and independent post-write audit remain open. This artifact does not self-pass any downstream Gate.
""", encoding="utf-8")
    print(json.dumps({"raw": 736, "verified": 736, "retained": len(denominator), "promoted": len(promoted), "downgraded": len(downgraded), "closures": 736-len(denominator)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
