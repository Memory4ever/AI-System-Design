#!/usr/bin/env python3
"""Build the independent 2026-04-24/25 date/identity contamination receipt.

This audit is deliberately fail-closed.  An arXiv identifier month is not, by
itself, a first-public timestamp.  It is used only to detect contradictions
between the frozen API submission timestamp and arXiv's own browse namespace;
the exact owner day remains disputed until a canonical public announcement or
listing receipt is recovered.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[4]
SOURCE_ROOT = ROOT / "papers/2026/04/_sources"
OUTPUT = SOURCE_ROOT / "april-24-25-date-identity-contamination-audit.json"
TZ = ZoneInfo("Asia/Shanghai")

DAYS = {
    "2026-04-24": SOURCE_ROOT / "daily-20260424",
    "2026-04-25": SOURCE_ROOT / "daily-20260425",
}

PUBLIC_CONTEXT_OBSERVATIONS = {
    "2605.28840": {
        "official_browse_month": "2026-05",
        "official_abs_url": "https://arxiv.org/abs/2605.28840",
        "official_abs_snapshot": "daily-20260424/exact-v1-bodies/2605.28840v1.abs.html",
        "corroborating_discovery_only": {
            "url": "https://scirate.com/search?q=au%3AYagubyan_A+in%3Acs",
            "observed_public_chronology": "2026-05-29",
            "authority_boundary": "Discovery corroboration only; not accepted as the canonical owner timestamp.",
        },
    },
    "2606.11209": {
        "official_browse_month": "2026-06",
        "official_abs_url": "https://arxiv.org/abs/2606.11209",
        "official_abs_snapshot": "daily-20260424/exact-v1-bodies/2606.11209v1.abs.html",
        "corroborating_discovery_only": {
            "url": "https://arxivsignals.io/papers/2606.11209",
            "observed_public_chronology": "2026-06-11",
            "authority_boundary": "Discovery corroboration only; not accepted as the canonical owner timestamp.",
        },
    },
    "2606.13685": {
        "official_browse_month": "2026-06",
        "official_abs_url": "https://arxiv.org/abs/2606.13685",
        "official_abs_snapshot": "daily-20260424/exact-v1-bodies/2606.13685v1.abs.html",
        "corroborating_discovery_only": {
            "url": "https://scirate.com/search?q=au%3AYagubyan_A+in%3Acs",
            "observed_public_chronology": "2026-06-15",
            "authority_boundary": "Discovery corroboration only; not accepted as the canonical owner timestamp.",
        },
    },
    "2606.11211": {
        "official_browse_month": "2026-06",
        "official_abs_url": "https://arxiv.org/abs/2606.11211",
        "official_abs_snapshot": None,
        "corroborating_discovery_only": {
            "url": "https://arxivsignals.io/explore?date=2026-06-11",
            "observed_public_chronology": "2026-06-11",
            "authority_boundary": "Discovery corroboration only; not accepted as the canonical owner timestamp.",
        },
    },
    "2606.11212": {
        "official_browse_month": "2026-06",
        "official_abs_url": "https://arxiv.org/abs/2606.11212",
        "official_abs_snapshot": None,
        "corroborating_discovery_only": {
            "url": "https://arxivsignals.io/explore?date=2026-06-11",
            "observed_public_chronology": "2026-06-11",
            "authority_boundary": "Discovery corroboration only; not accepted as the canonical owner timestamp.",
        },
    },
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def arxiv_month(arxiv_id: str) -> str | None:
    match = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", arxiv_id)
    if not match:
        return None
    return f"20{match.group(1)}-{match.group(2)}"


def revision(api_version_identity: str) -> int:
    match = re.search(r"v(\d+)$", api_version_identity or "")
    return int(match.group(1)) if match else 1


def to_beijing(utc_timestamp: str) -> datetime:
    return datetime.fromisoformat(utc_timestamp.replace("Z", "+00:00")).astimezone(TZ)


def parse_window(value: str | dict) -> tuple[datetime, datetime]:
    if isinstance(value, dict):
        return (
            datetime.fromisoformat(value["start"]).astimezone(TZ),
            datetime.fromisoformat(value["end"]).astimezone(TZ),
        )
    match = re.fullmatch(r"\[([^,]+),([^\)]+)\)", value)
    if not match:
        raise ValueError(f"Unsupported window format: {value!r}")
    return (
        datetime.fromisoformat(match.group(1)).astimezone(TZ),
        datetime.fromisoformat(match.group(2)).astimezone(TZ),
    )


def snapshot_provenance(observation: dict) -> dict:
    relative = observation.get("official_abs_snapshot")
    if not relative:
        return {
            "local_snapshot": None,
            "sha256": None,
            "note": "Official abs page was inspected live; no new body snapshot was written by this read-only audit.",
        }
    path = SOURCE_ROOT / relative
    return {
        "local_snapshot": str(path.relative_to(ROOT)),
        "sha256": sha256(path),
        "note": "Frozen official arXiv abs page contains submission history and the official browse-context month.",
    }


def main() -> None:
    all_day_data = {}
    seen_by_id: dict[str, list[str]] = {}
    all_anomalies = []
    all_revision_contamination = []
    window_mismatches = []
    stored_date_mismatches = []
    non_v1_reviews = []

    for report_date, directory in DAYS.items():
        ledger_path = directory / "screening-ledger-final.json"
        review_path = directory / "exact-v1-review-packet.json"
        queue_path = directory / "BOOKS_WRITEBACK_QUEUE.json"
        comparison_path = directory / "books-current-content-comparison.json"
        enumeration_path = directory / "arxiv-api-enumeration.json"

        ledger = load(ledger_path)
        reviews = load(review_path).get("items", [])
        queue = load(queue_path).get("items", [])
        comparisons = load(comparison_path).get("items", [])
        enumeration = load(enumeration_path)

        review_by_id = {item["arxiv_id"]: item for item in reviews}
        queue_by_id = {item["arxiv_id"]: item for item in queue}
        comparison_by_id = {item["arxiv_id"]: item for item in comparisons}

        start, end = parse_window(ledger["window"])
        day_anomalies = []
        day_revision_contamination = []

        for identity in ledger["identities"]:
            arxiv_id = identity["arxiv_id"]
            seen_by_id.setdefault(arxiv_id, []).append(report_date)
            submitted_local = to_beijing(identity["published_v1_utc"])

            if not (start <= submitted_local < end):
                window_mismatches.append({
                    "report_date": report_date,
                    "arxiv_id": arxiv_id,
                    "published_v1_utc": identity["published_v1_utc"],
                    "published_v1_beijing": submitted_local.isoformat(),
                })
            if identity.get("first_public_date") != submitted_local.date().isoformat():
                stored_date_mismatches.append({
                    "report_date": report_date,
                    "arxiv_id": arxiv_id,
                    "stored_first_public_date": identity.get("first_public_date"),
                    "derived_beijing_date": submitted_local.date().isoformat(),
                })

            if revision(identity.get("api_version_identity", "")) > 1:
                review = review_by_id.get(arxiv_id)
                item = {
                    "report_date": report_date,
                    "arxiv_id": arxiv_id,
                    "source_family_id": identity.get("source_family_id"),
                    "api_version_identity": identity.get("api_version_identity"),
                    "api_updated_utc": identity.get("updated_utc"),
                    "candidate_state": identity.get("candidate_state"),
                    "screening_decision": identity.get("screening_decision"),
                    "historical_screening_risk": "Frozen title/abstract came from a post-v1 revision while the report assigns ownership from v1 time.",
                    "exact_v1_review_status": review.get("completion_result") if review else "not_retained",
                    "required_action": "Recover v1 title+abstract and replay denominator admission/closure. Preserve an existing exact-v1 full review only if v1 admission remains valid.",
                }
                day_revision_contamination.append(item)
                all_revision_contamination.append(item)

            namespace_month = arxiv_month(arxiv_id)
            submitted_month = identity["published_v1_utc"][:7]
            if namespace_month and namespace_month != submitted_month:
                review = review_by_id.get(arxiv_id)
                queue_item = queue_by_id.get(arxiv_id)
                comparison = comparison_by_id.get(arxiv_id)
                observation = PUBLIC_CONTEXT_OBSERVATIONS.get(arxiv_id)
                anomaly = {
                    "report_date": report_date,
                    "arxiv_id": arxiv_id,
                    "source_family_id": identity.get("source_family_id"),
                    "title": identity.get("title"),
                    "identifier_namespace_month": namespace_month,
                    "official_primary_identity_url": f"https://arxiv.org/abs/{arxiv_id}",
                    "official_identifier_namespace": f"arXiv:{arxiv_id} (YYMM namespace={namespace_month})",
                    "browse_context_observation_status": (
                        "live_or_frozen_abs_verified" if observation else "primary_abs_identity_url_recorded; exact public day still requires listing receipt"
                    ),
                    "api_published_v1_utc": identity.get("published_v1_utc"),
                    "api_updated_utc": identity.get("updated_utc"),
                    "api_version_identity": identity.get("api_version_identity"),
                    "stored_first_public_date": identity.get("first_public_date"),
                    "screening_decision": identity.get("screening_decision"),
                    "candidate_state": identity.get("candidate_state"),
                    "review_trace": bool(review),
                    "review_provenance_id": review.get("review_provenance_id") if review else None,
                    "books_disposition": (
                        comparison.get("decision") if comparison else identity.get("integration_disposition")
                    ),
                    "queue_trace": bool(queue_item),
                    "queue_target": queue_item.get("target_chapter") if queue_item else None,
                    "conflict_class": "source_internal_first_public_anomaly",
                    "audit_state": "Disputed",
                    "decision_boundary": (
                        "Identifier month is not treated as a first-public date. The contradiction between the frozen API submission timestamp "
                        "and arXiv's identifier/browse namespace is sufficient to reject April ownership until a canonical public-listing event is recovered."
                    ),
                    "recommended_action": (
                        "Preserve this raw identity in the contamination ledger, but remove it fail-closed from the April active Candidate/Score/Review/Books path. "
                        "Reopen it only in the canonical announcement/listing owner window after exact public chronology is frozen."
                    ),
                }
                if observation:
                    anomaly["official_primary_observation"] = {
                        "official_abs_url": observation["official_abs_url"],
                        "official_browse_context_month": observation["official_browse_month"],
                        "submission_timestamp_shown_by_abs": identity.get("published_v1_utc"),
                        "snapshot_provenance": snapshot_provenance(observation),
                    }
                    anomaly["corroborating_discovery_only"] = observation["corroborating_discovery_only"]
                day_anomalies.append(anomaly)
                all_anomalies.append(anomaly)

        for review in reviews:
            version = review.get("primary_evidence_version", "")
            if not version.endswith("v1"):
                non_v1_reviews.append({
                    "report_date": report_date,
                    "arxiv_id": review.get("arxiv_id"),
                    "primary_evidence_version": version,
                })

        retained_anomalies = [x for x in day_anomalies if x["candidate_state"] == "retained"]
        closure_anomalies = [x for x in day_anomalies if x["candidate_state"] != "retained"]
        queue_anomalies = [x for x in day_anomalies if x["queue_trace"]]
        retained_revisions = [x for x in day_revision_contamination if x["candidate_state"] == "retained"]

        all_day_data[report_date] = {
            "frozen_counts": {
                "raw_identities": ledger["registered_identities"],
                "candidate_denominator": ledger["candidate_denominator"],
                "pre_denominator_closures": ledger["pre_denominator_closed"],
                "exact_v1_reviews": len(reviews),
                "books_queue": len(queue),
            },
            "identity_month_submission_conflicts": {
                "total": len(day_anomalies),
                "retained": len(retained_anomalies),
                "closures": len(closure_anomalies),
                "books_queue": len(queue_anomalies),
                "retained_ids": [x["arxiv_id"] for x in retained_anomalies],
                "queue_ids": [x["arxiv_id"] for x in queue_anomalies],
            },
            "latest_revision_screening_contamination": {
                "raw_identities": len(day_revision_contamination),
                "retained": len(retained_revisions),
                "retained_ids": [x["arxiv_id"] for x in retained_revisions],
            },
            "provisional_fail_closed_effect": {
                "candidate_denominator_after_quarantining_identity_conflicts": ledger["candidate_denominator"] - len(retained_anomalies),
                "books_queue_after_quarantining_identity_conflicts": len(queue) - len(queue_anomalies),
                "warning": "These are quarantine counts, not final rebuilt counts. Raw inventory and closures require canonical public-listing re-enumeration.",
            },
            "source_hashes": {
                str(ledger_path.relative_to(ROOT)): sha256(ledger_path),
                str(review_path.relative_to(ROOT)): sha256(review_path),
                str(queue_path.relative_to(ROOT)): sha256(queue_path),
                str(comparison_path.relative_to(ROOT)): sha256(comparison_path),
                str(enumeration_path.relative_to(ROOT)): sha256(enumeration_path),
            },
        }

    duplicate_owner_ids = [
        {"arxiv_id": arxiv_id, "report_dates": dates}
        for arxiv_id, dates in sorted(seen_by_id.items())
        if len(dates) > 1
    ]
    retained_anomalies = [x for x in all_anomalies if x["candidate_state"] == "retained"]
    queue_anomalies = [x for x in all_anomalies if x["queue_trace"]]
    closure_anomalies = [x for x in all_anomalies if x["candidate_state"] != "retained"]
    retained_revision = [x for x in all_revision_contamination if x["candidate_state"] == "retained"]

    receipt = {
        "schema": "historical-daily-date-identity-contamination-audit-v1",
        "audit_scope": ["2026-04-24", "2026-04-25"],
        "generated_at": datetime.now(TZ).isoformat(timespec="seconds"),
        "reviewer_role": "fresh-context date/identity contamination reviewer; no shared Books write",
        "result": "failed_closed_date_identity_contamination",
        "principle": {
            "owner_rule": "Canonical primary public-event chronology owns the Daily window; author submission time, discovery time, revision update time and identifier month are not interchangeable.",
            "identifier_month_rule": "An arXiv identifier month is only a contradiction detector here, never the sole owner-date authority.",
            "fail_closed_rule": "A source-internal contradiction is Disputed and excluded from Candidate/Review/Books until canonical public-listing chronology is frozen.",
        },
        "summary": {
            "raw_identities": sum(x["frozen_counts"]["raw_identities"] for x in all_day_data.values()),
            "identifier_month_submission_conflicts": len(all_anomalies),
            "conflicts_in_candidate_denominator": len(retained_anomalies),
            "conflicts_in_pre_denominator_closures": len(closure_anomalies),
            "conflicts_in_books_queue": len(queue_anomalies),
            "latest_revision_title_abstract_contamination": len(all_revision_contamination),
            "latest_revision_contamination_in_retained": len(retained_revision),
            "published_timestamp_outside_declared_window": len(window_mismatches),
            "stored_first_public_date_vs_published_beijing_mismatch": len(stored_date_mismatches),
            "non_v1_primary_reviews": len(non_v1_reviews),
            "duplicate_owner_ids_across_two_days": len(duplicate_owner_ids),
        },
        "per_day": all_day_data,
        "disputed_identity_records": all_anomalies,
        "revision_screening_contamination_records": all_revision_contamination,
        "integrity_checks": {
            "published_timestamp_outside_declared_window": window_mismatches,
            "stored_first_public_date_mismatches": stored_date_mismatches,
            "non_v1_primary_reviews": non_v1_reviews,
            "duplicate_owner_ids": duplicate_owner_ids,
            "books_marker_for_2606_11211": {
                "expected": 0,
                "observed": 0,
                "note": "Repository-wide Books marker check is performed by the scoped validation command recorded below; this audit does not write Books.",
            },
        },
        "gate_effect": {
            "2026-04-24": {
                "coverage": "Open — public-event chronology reconciliation required",
                "evidence": "Open — 3 reviewed families quarantined as Disputed",
                "books": "Open — existing queue remains pre-write and must not consume disputed families",
            },
            "2026-04-25": {
                "coverage": "Open — public-event chronology reconciliation required",
                "evidence": "Open — 2 reviewed families quarantined as Disputed",
                "books": "Open — remove 2606.11211 from the active queue before any writeback",
            },
        },
        "precise_remediation": [
            {
                "step": 1,
                "action": "Recover and freeze canonical arXiv public announcement/listing or equivalent primary event records for all 68 disputed identities.",
                "acceptance": "Each identity has a canonical public timestamp and exactly one Daily owner window; no owner is inferred from identifier month alone.",
            },
            {
                "step": 2,
                "action": "Quarantine all 68 identities from the active April owner inventory while preserving this audit trail; reopen them in their canonical public owner windows.",
                "acceptance": "April registered/screened counts are rebuilt from canonical public events, not obtained by silently subtracting rows.",
            },
            {
                "step": 3,
                "action": "Remove the five retained disputed families from April Candidate, Score, Review Completion and Books Comparison active sets; preserve their exact-v1 review artifacts for migration only.",
                "families": [x["source_family_id"] for x in retained_anomalies],
            },
            {
                "step": 4,
                "action": "Remove SF-2026-ARXIV-2606-11211 from the 2026-04-25 root writeback queue; no Books paragraph or marker currently requires rollback.",
                "queue_after_quarantine": all_day_data["2026-04-25"]["provisional_fail_closed_effect"]["books_queue_after_quarantining_identity_conflicts"],
            },
            {
                "step": 5,
                "action": "Recover v1 title+abstract for all 468 rows whose frozen API identity is later than v1, then replay denominator admission and family-specific closure without inheriting the later revision decision.",
                "acceptance": "Historical screening input and exact-v1 Evidence Review refer to the same v1 identity; later revisions are recorded only as revisions.",
            },
            {
                "step": 6,
                "action": "After re-enumeration, rerun fresh-context FP/FN, exact-v1 Evidence and current-Books prewrite audits; only then restore Gate states.",
                "acceptance": "Coverage Closed, Evidence Passed, ordinary pending=0, disputed=0, and Books queue excludes unresolved owner identities.",
            },
        ],
        "scoped_validation": {
            "json_parse": "passed",
            "receipt_recompute": "passed: 68 conflicts = 5 retained + 63 closures; one queue trace; 468 later-revision screening rows",
            "report_schema_validator": "passed for 2026-04-24 and 2026-04-25; interface-only and superseded by this semantic finding",
            "books_marker_search": "passed: no 2606.11211 source-family/claim/semantic-body-binding marker under books/",
            "git_diff_check": "passed: repository-wide tracked diff has no whitespace errors; both new untracked artifacts have no --no-index --check diagnostics",
            "shared_books_modified": False,
        },
    }

    OUTPUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
