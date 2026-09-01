#!/usr/bin/env python3
"""Reconcile exact-access truth after 04-08..15 false-negative recovery."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MONTH = ROOT / "papers/2026/04"
WITHDRAWN = "2604.06798"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def clear_materials_table(text: str) -> str:
    marker = "<!-- validator:materials-request-v1 -->"
    if marker not in text:
        return text
    pos = text.index(marker) + len(marker)
    tail = text[pos:]
    lines = tail.splitlines()
    start = next((i for i, line in enumerate(lines) if line.strip().startswith("|")), None)
    if start is None:
        return text
    end = start
    while end < len(lines) and lines[end].strip().startswith("|"):
        end += 1
    lines[start + 2:end] = []
    return text[:pos] + "\n".join(lines)


def fill_materials_table(text: str, rows: list[str]) -> str:
    marker = "<!-- validator:materials-request-v1 -->"
    pos = text.index(marker) + len(marker)
    tail = text[pos:]
    lines = tail.splitlines()
    start = next(i for i, line in enumerate(lines) if line.strip().startswith("|"))
    end = start
    while end < len(lines) and lines[end].strip().startswith("|"):
        end += 1
    lines[start + 2:end] = rows
    return text[:pos] + "\n".join(lines)


for day in range(8, 16):
    packet = MONTH / f"_sources/daily-202604{day:02d}"
    audit_path = packet / "independent-recovery-prewrite-audit.json"
    audit = load(audit_path)
    challenges_path = packet / "independent-high-risk-closure-challenges.json"
    challenges = load(challenges_path)
    for row in challenges["items"]:
        row["status"] = "exact_v1_recovered_pending_source_review"
    dump(challenges_path, challenges)

    access_path = packet / "exact-v1-access-receipt.json"
    access = load(access_path)
    if day == 9 and not any(row["arxiv_id"] == WITHDRAWN for row in access["rows"]):
        abs_path = packet / f"exact-v1-bodies/{WITHDRAWN}v1.abs.html"
        access["rows"].append({
            "arxiv_id": WITHDRAWN,
            "identity_url": f"https://arxiv.org/abs/{WITHDRAWN}v1",
            "identity_path": abs_path.relative_to(ROOT).as_posix(),
            "identity_sha256": hashlib.sha256(abs_path.read_bytes()).hexdigest(),
            "withdrawn": True,
            "withdrawal_phrase": "this paper has been withdrawn",
            "body_route": "not_fetched_withdrawn",
            "body_url": "—",
            "body_path": "—",
            "body_sha256": "—",
            "error": "—",
        })
        access["rows"].sort(key=lambda row: row["arxiv_id"])
    access["withdrawn_count"] = sum(bool(row.get("withdrawn")) for row in access["rows"])
    access["accessible_count"] = sum(str(row.get("body_route", "")).startswith("official_") for row in access["rows"])
    access["blocked_count"] = sum(row.get("body_route") == "blocked" for row in access["rows"])
    access["candidate_count"] = access["accessible_count"]
    access["fetch_identity_count"] = len(access["rows"])
    access["withdrawn_screening_closure_count"] = access["withdrawn_count"]
    dump(access_path, access)

    proposed = access["accessible_count"]
    raw = audit["raw_identities_replayed"]
    audit.update({
        "proposed_refrozen_denominator": proposed,
        "proposed_refrozen_closures": raw - proposed,
        "recovered_exact_v1_accessible_for_proposed_denominator": proposed,
        "exact_v1_blocked": access["blocked_count"],
        "source_review_complete": 0,
        "source_review_pending_existing_accessible": proposed,
        "coverage_verdict": "fail_pending_denominator_refreeze",
        "evidence_verdict": "pending_source_specific_review",
        "books_prewrite_verdict": "pending_current_content_comparison",
        "gate_effect": "Coverage, Evidence, and Books remain Open; no queue is eligible for writeback.",
    })
    dump(audit_path, audit)

    materials_path = packet / "materials-request.json"
    materials = load(materials_path)
    ledger = load(packet / "screening-ledger-final.json")
    retained = [
        row for row in ledger["identities"]
        if row.get("candidate_state") == "retained" and row.get("arxiv_id") != WITHDRAWN
    ]
    materials["items"] = [
        {
            "request_id": f"MR-202604{day:02d}-{row['arxiv_id']}",
            "priority": "P1 Semantic Review",
            "source_family_id": row["source_family_id"],
            "source_id": "SRC-ARXIV",
            "gap_limitation_id": f"GAP-202604{day:02d}-SEMANTIC-{row['arxiv_id']}",
            "owner_week": "2026-W15" if day <= 12 else "2026-W16",
            "known_identifiers_urls": f"https://arxiv.org/html/{row['arxiv_id']}v1 ; https://arxiv.org/abs/{row['arxiv_id']}v1",
            "missing_material": "source-specific Method/Evaluation/Limitations semantic review receipt",
            "why_existing_evidence_is_insufficient": "exact-v1 access alone does not establish claim boundary or Books decision",
            "acceptable_substitute": "fresh-context exact-v1 semantic review with provenance digest",
            "suggested_file_name": f"{row['arxiv_id']}v1-review.json",
            "required_review_scope": "Method/Evaluation/Limitations/Artifact and current Books challenge",
        }
        for row in retained
    ]
    materials["ordinary_pending"] = len(materials["items"])
    materials["resolution"] = "Exact-v1 access recovered; semantic review receipts remain pending."
    if day == 9:
        materials["withdrawn_closed_request"] = "MR-20260409-2604-06798"
    dump(materials_path, materials)

    review_path = packet / "exact-v1-review-packet.json"
    review_packet = load(review_path)
    for item in review_packet["items"]:
        aid = item["arxiv_id"]
        body = packet / f"exact-v1-bodies/{aid}v1.html"
        item.update({
            "reviewed_evidence_versions": [f"SRC-ARXIV@arXiv:{aid}v1 exact body accessible"],
            "method_identity_locators": f"{body.relative_to(ROOT).as_posix()} — exact-v1 Method locator pending semantic read",
            "evaluation_locators": f"{body.relative_to(ROOT).as_posix()} — exact-v1 Evaluation locator pending semantic read",
            "limitations_counterevidence_locators": f"{body.relative_to(ROOT).as_posix()} — exact-v1 Limitations locator pending semantic read",
            "artifact_locators": f"https://arxiv.org/abs/{aid}v1 ; https://arxiv.org/html/{aid}v1",
            "claim_boundary": "Exact-v1 is accessible, but no mechanism/evaluation claim is admitted before source-specific semantic review.",
            "completion_result": "pending_semantic_review",
        })
    dump(review_path, review_packet)

    compare_path = packet / "books-current-content-comparison.json"
    comparisons = load(compare_path)
    for item in comparisons["items"]:
        item["new_evidence_delta"] = "Pending source-specific exact-v1 semantic review"
        item["decision"] = "Pending — Semantic Review"
    dump(compare_path, comparisons)

    readme_path = MONTH / f"{day:02d}/README.md"
    text = readme_path.read_text(encoding="utf-8")
    text = clear_materials_table(text)
    text = text.replace("| retained | pending_semantic_review | accessible |", "| retained | blocked | blocked |")
    text = text.replace("| Pending — Semantic Review | books-review:", "| Blocked / Unverified | books-review:")
    text = re.sub(r"\| claim:([^|]+) \| pending_semantic_review \|", r"| claim:\1 | blocked |", text)
    text = text.replace("Books Decision=`Pending — Semantic Review`", "Books Decision=`Blocked / Unverified`")
    text = text.replace("Decision=`Pending — Semantic Review`", "Decision=`Blocked / Unverified`")
    material_rows = [
        "| " + " | ".join([
            item["request_id"], item["priority"], item["source_family_id"], "—", "—",
            item["owner_week"], item["known_identifiers_urls"], item["missing_material"],
            item["why_existing_evidence_is_insufficient"], item["acceptable_substitute"],
            item["suggested_file_name"], item["required_review_scope"],
        ]) + " |"
        for item in materials["items"]
    ]
    text = fill_materials_table(text, material_rows)
    text = re.sub(r"exact-v1 Review complete=0，blocked=\d+", f"exact-v1 Review complete=0，pending={proposed}，blocked=0", text)
    note = (
        f"Recovery checkpoint：proposed refrozen denominator={proposed}；official exact-v1 "
        f"accessible={proposed}、blocked=0，但 source-specific Review={0}/{proposed}，"
        "current-content Books comparison 尚未重放。Materials ordinary pending=0；"
        "这不等于 Evidence 或 pre-write pass。\n\n"
    )
    marker = "## 7. Semantic Audit"
    if note not in text:
        text = text.replace(marker, note + marker)
    readme_path.write_text(text, encoding="utf-8")
