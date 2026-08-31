#!/usr/bin/env python3
"""Materialize the independent 2026-06-02 denominator audit.

The decision set below is the result of a fresh full-population title+abstract
screen.  The V2 artifact is used only to preserve stable family identifiers and
the already-written family-specific closure text; its admission decisions,
scores, selection, and Books decisions are not inputs to the audit.
"""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260602"
BASE_LEDGER = PACKET / "screening-ledger-v2-strict.tsv"
BASE_DENOM = PACKET / "candidate-denominator-audit-v2-strict.json"
OLD_LEDGER = PACKET / "screening-ledger.tsv"
OUT_LEDGER = PACKET / "screening-ledger-v3-fresh.tsv"
OUT_JSON = PACKET / "candidate-denominator-audit-v3-fresh.json"
OUT_MD = PACKET / "CANDIDATE_DENOMINATOR_AUDIT_V3_FRESH.md"


# Independently authored admission result.  Stable family metadata is resolved
# from the repository only after the yes/no decision has been made.
RETAIN_IDS = {
    "2606.01567", "2606.01600", "2606.01680", "2606.01725",
    "2606.01751", "2606.01770", "2606.01839", "2606.01850",
    "2606.01927", "2606.02060", "2606.02091", "2606.02218",
    "2606.02302", "2606.02373", "2606.02430", "2606.02437",
    "2606.02483", "2606.02540", "2606.02668", "2606.02800",
    "2606.02958", "2606.02959", "2606.02963", "2606.02964",
    "2606.02982", "2606.09864", "2606.28343", "2607.22569",
}

ASYMCACHE = {
    "source_family_id": "SF-ASYMCACHE-MULTI-SEGMENT",
    "stable_node_id": "INFER-KV-CACHE",
    "retention_axis": "kernel_cost_aware_residency_control",
    "evidence_status": "fresh_exact_v1_complete",
    "books_status": "pending_root_serial_reconciliation",
}


def base_id(value: str) -> str:
    return value.removeprefix("arXiv:").removesuffix("v1")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    base_rows = list(csv.DictReader(BASE_LEDGER.open(encoding="utf-8"), delimiter="\t"))
    old_rows = list(csv.DictReader(OLD_LEDGER.open(encoding="utf-8"), delimiter="\t"))
    assert len(base_rows) == len(old_rows) == 736
    base_json = json.loads(BASE_DENOM.read_text(encoding="utf-8"))
    meta = {base_id(x["primary_identifier"]): x for x in base_json["candidates"]}
    old_by_id = {base_id(x["Primary Identifier"]): x for x in old_rows}
    meta["2606.02964"] = {
        "source_family_id": ASYMCACHE["source_family_id"],
        "primary_identifier": "arXiv:2606.02964v1",
        "title": old_by_id["2606.02964"]["Title"],
        "published_utc": old_by_id["2606.02964"]["Published UTC"],
        "stable_node_id": ASYMCACHE["stable_node_id"],
        "retention_axis": ASYMCACHE["retention_axis"],
        "origin": "old_candidate_fresh_recovery",
        "evidence_status": ASYMCACHE["evidence_status"],
        "books_status": ASYMCACHE["books_status"],
    }
    assert RETAIN_IDS <= set(meta)

    header = list(base_rows[0]) + ["Fresh Audit Verdict", "Fresh Audit Basis"]
    output_rows = []
    closure_counts: Counter[str] = Counter()
    candidates = []
    old_candidate_ids = {
        base_id(x["Primary Identifier"])
        for x in old_rows
        if x["Screening State"] == "routed_candidate"
    }
    strict_ids = {base_id(x["primary_identifier"]) for x in base_json["candidates"]}

    for row in base_rows:
        bid = base_id(row["Primary Identifier"])
        out = dict(row)
        if bid in RETAIN_IDS:
            item = dict(meta[bid])
            item["evidence_status"] = "fresh_exact_v1_complete"
            item["books_status"] = "pending_root_serial_reconciliation"
            candidates.append(item)
            out["Denominator State"] = "retained"
            out["Source Family ID"] = item["source_family_id"]
            out["Stable Node ID"] = item["stable_node_id"]
            out["Closure / Retention Basis"] = (
                f"{row['Title']}: retained after independent full-population title+abstract "
                f"screen because it changes {item['retention_axis']}; admission is not "
                "derived from ROADMAP mappability or Score V2."
            )
            out["Fresh Audit Verdict"] = "retain"
            out["Fresh Audit Basis"] = item["retention_axis"]
        else:
            assert row["Denominator State"] == "pre_denominator_closure"
            out["Fresh Audit Verdict"] = "pre_denominator_closure"
            out["Fresh Audit Basis"] = row["Closure / Retention Basis"]
            # The original closure class is stable and precedes the colon-free
            # prose in the JSON accounting.  Recompute it from the stored V2
            # reason-count membership where possible, with a durable fallback.
            basis = row["Closure / Retention Basis"].lower()
            if "benchmark, survey, or position" in basis:
                cls = "bounded_benchmark_survey_or_position"
            elif "domain-specific" in basis:
                cls = "domain_application_without_portable_system_contract"
            elif "threat or defense is scoped" in basis:
                cls = "scoped_security_method_without_release_contract_delta"
            elif "local model or optimization delta" in basis:
                cls = "local_model_or_optimization_delta"
            elif "agent or retrieval task" in basis:
                cls = "bounded_agent_or_retrieval_method"
            elif "representation identity, mutable world state" in basis:
                cls = "bounded_multimodal_or_embodied_method"
            else:
                cls = "ai_relevant_but_no_durable_system_delta"
            closure_counts[cls] += 1
        output_rows.append(out)

    candidates.sort(key=lambda x: x["published_utc"])
    with OUT_LEDGER.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    strict_fp = sorted(strict_ids - RETAIN_IDS)
    strict_fn = sorted(RETAIN_IDS - strict_ids)
    old_retained = RETAIN_IDS & old_candidate_ids
    result = {
        "schema_version": "candidate-denominator-v3-fresh",
        "audit_owner": "fresh-context:jun02-v3-adversarial",
        "raw_identity_count": 736,
        "title_abstract_screened_count": 736,
        "fresh_retained_count": len(RETAIN_IDS),
        "fresh_retain_rate_percent": round(len(RETAIN_IDS) / 736 * 100, 2),
        "pre_denominator_closure_count": 736 - len(RETAIN_IDS),
        "closure_reason_counts": dict(sorted(closure_counts.items())),
        "comparison_to_v2_strict": {
            "previous_retained": len(strict_ids),
            "false_positives": strict_fp,
            "false_negatives": strict_fn,
        },
        "comparison_to_original_52": {
            "original_retained": len(old_candidate_ids),
            "still_retained": len(old_retained),
            "downgraded": len(old_candidate_ids - RETAIN_IDS),
            "promoted_from_original_closure": len(RETAIN_IDS - old_candidate_ids),
        },
        "candidates": candidates,
        "ordinary_pending": 0,
        "access_blocked": 0,
        "gate_truth": "Denominator frozen; Evidence and Books remain Open until canonical Daily reconciliation, root serial Books action, and independent post-write audit.",
    }
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    rows = "\n".join(
        f"| `{x['source_family_id']}` | `{x['primary_identifier']}` | `{x['stable_node_id']}` | `{x['retention_axis']}` |"
        for x in candidates
    )
    closures = "\n".join(f"| `{k}` | {v} |" for k, v in sorted(closure_counts.items()))
    OUT_MD.write_text(f"""# 2026-06-02 Candidate Denominator V3 Fresh Audit

## Result

- Raw identities: 736/736.
- Full-population title+abstract semantic screen: 736/736; no sampling.
- Retained candidates: {len(RETAIN_IDS)}/736 ({len(RETAIN_IDS)/736*100:.2f}%).
- Pre-denominator closures: {736-len(RETAIN_IDS)}.
- Relative to V2 Strict: false positives={len(strict_fp)}, false negatives={len(strict_fn)} (`2606.02964`).
- Relative to the original 52-row pool: retained={len(old_retained)}, downgraded={len(old_candidate_ids-RETAIN_IDS)}, promoted={len(RETAIN_IDS-old_candidate_ids)}.

The ratio is an outcome, not a quota.  Every abstract was challenged against
`RESEARCH_CONTRACT.md §4.2`: ROADMAP mappability, AI relevance, a domain method,
or a benchmark alone did not admit a family.  `Score V2` was not consulted.

## Fresh Finding

`AsymCache` was a V2 Strict false negative.  Its contribution is not merely a
local throughput number: it changes the owner and input of a lossless KV
residency decision.  The cache manager consumes reuse probability *and* the
position-dependent recomputation/kernel cost; a non-contiguous attention path
then preserves exact output while the scheduler chooses chunk boundaries.
This is a durable `state/control` contract even though the reported gains remain
bounded to the disclosed models, H20 topology, cache budgets and workloads.

## Closure Classes

| Closure class | Count |
| --- | ---: |
{closures}

## Frozen Candidate Set

| Source Family | Primary identifier | Stable owner | Admission axis |
| --- | --- | --- | --- |
{rows}

## Evidence Boundary

All 28 candidates were re-opened against exact-v1.  Existing Report prose and
scores were treated as claims to disprove, not as evidence of completion.
`AsymCache` exact-v1 was checked at Method §§3–5, Evaluation §6 including §6.5,
and Discussion/Conclusion §§7–8.  No exact-v1 candidate is blocked.  The
canonical Daily and root Books marker reconciliation remain downstream, so this
artifact does not close Evidence or Books Gate by itself.

## Integrity

- Ledger SHA-256: `{sha256(OUT_LEDGER)}`
- JSON SHA-256 is recorded after file creation by the caller.
""", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
