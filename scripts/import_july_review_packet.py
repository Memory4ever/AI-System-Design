#!/usr/bin/env python3
"""Persist one independently reviewed July Daily evidence packet.

The packet is copied into the July source snapshot and its exact-v1 reviews are
normalized into the renderer's central receipt ledger. Books edits remain a
separate, date-serialized root-agent responsibility.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26"
LEDGER = SOURCE_DIR / "primary-review-receipts.json"
PACKET_DIR = SOURCE_DIR / "daily-review-packets"
ARTIFACT_RECEIPT_FIELDS = {
    "repository",
    "until",
    "commit",
    "commit_timestamp",
    "url",
    "executed_at",
}


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_durable_snapshots(identifier: str, receipt: dict) -> None:
    """Replace ephemeral /private/tmp locators with verified repo snapshots.

    A completed review may be prepared in a temporary workspace, but the
    persisted packet and central ledger must remain independently reviewable
    after that workspace disappears.  The root workflow copies exact-v1 files
    into SOURCE_DIR first; import then verifies the declared hash and records a
    repository-relative path.
    """
    raw_snapshot = receipt.get("local_snapshot")
    if raw_snapshot:
        snapshot = Path(str(raw_snapshot))
        if snapshot.is_absolute() and str(snapshot).startswith("/private/tmp/"):
            if snapshot.suffix.lower() == ".html":
                durable = SOURCE_DIR / "arxiv-html" / snapshot.name
            elif snapshot.suffix.lower() == ".pdf":
                durable = SOURCE_DIR / "arxiv-pdf" / snapshot.name
            else:
                raise ValueError(f"{identifier}: unsupported exact-v1 snapshot type {snapshot}")
            if not durable.exists():
                raise ValueError(
                    f"{identifier}: durable snapshot missing; copy {snapshot} to {durable} before import"
                )
            expected = receipt.get("sha256")
            actual = file_sha256(durable)
            if expected and actual != expected:
                raise ValueError(
                    f"{identifier}: durable snapshot SHA-256 {actual} != declared {expected}"
                )
            receipt["local_snapshot"] = durable.relative_to(ROOT).as_posix()

    source_sha = receipt.get("source_archive_sha256")
    if source_sha:
        raw_archive = receipt.get("source_archive_snapshot")
        archive_name = f"{identifier}v1-src.tar"
        durable_archive = SOURCE_DIR / "arxiv-source" / archive_name
        if raw_archive and not str(raw_archive).startswith("/private/tmp/"):
            durable_archive = ROOT / str(raw_archive)
        if not durable_archive.exists():
            raise ValueError(
                f"{identifier}: durable exact-v1 source archive missing at {durable_archive}"
            )
        actual = file_sha256(durable_archive)
        if actual != source_sha:
            raise ValueError(
                f"{identifier}: source archive SHA-256 {actual} != declared {source_sha}"
            )
        receipt["source_archive_snapshot"] = durable_archive.relative_to(ROOT).as_posix()


def arxiv_id(review: dict) -> str:
    identity = review.get("identity") or review.get("primary_identifier") or ""
    match = re.search(r"arXiv:(\d{4}\.\d{4,5})v1", identity, re.I)
    if not match:
        family = review.get("source_family") or review.get("source_family_id") or ""
        match = re.search(r"ARXIV-(\d{4}-\d{4,5})", family, re.I)
        if match:
            return match.group(1).replace("-", ".", 1)
        raise ValueError(f"Cannot recover exact-v1 arXiv identity from {identity!r}")
    return match.group(1)


def score_tuple(score: dict | list) -> list[int]:
    if isinstance(score, list):
        values = score
        total = sum(values)
    else:
        values = [score["design_delta"], score["system_reach"], score["durability"]]
        total = score["total"]
    if len(values) != 3 or any(not isinstance(value, int) or not 0 <= value <= 3 for value in values):
        raise ValueError(f"Invalid Score V2 dimensions: {values!r}")
    if sum(values) != total:
        raise ValueError(f"Score V2 total mismatch: {values!r} != {total}")
    return values


def normalize_benchmark(contract: dict | str | None, evaluation: str) -> dict | None:
    if not contract:
        return None
    if isinstance(contract, str):
        # Some independently reviewed packets preserve the complete disclosed
        # benchmark boundary as prose rather than a field map. Keep that
        # evidence as the workload contract, while making every unseparated
        # field explicitly Not Disclosed. The renderer must never infer model,
        # hardware or SLO values by parsing prose heuristically.
        contract = {"workload": contract}
    if not isinstance(contract, dict):
        raise ValueError(f"Invalid benchmark contract type: {type(contract).__name__}")
    combined = contract.get("batch_or_concurrency", "Not Disclosed")
    return {
        "workload": contract.get("workload") or f"Paper-defined evaluation contract: {evaluation}",
        "model": contract.get("model") or contract.get("models", "Not Disclosed"),
        "hardware": contract.get("hardware", "Not Disclosed"),
        "precision": contract.get("precision", "Not Disclosed"),
        "input_length": contract.get("input_length") or contract.get("length", "Not Disclosed"),
        "output_length": contract.get("output_length") or contract.get("length", "Not Disclosed"),
        "batch": contract.get("batch", combined),
        "concurrency": contract.get("concurrency", combined),
        "slo": contract.get("slo", "Not Disclosed"),
        "evaluator": contract.get("evaluator") or contract.get("claim_boundary", "Not Disclosed"),
    }


def reasoned_locator(value: str, field: str) -> str:
    value = str(value).strip()
    if re.search(r"https?://|doi:|arXiv:", value, re.I):
        return value
    if re.match(r"^(Not Disclosed|Not Required|No Benchmark Claim)\b", value, re.I):
        if value.casefold() in {"not disclosed", "not required", "no benchmark claim"}:
            return f"{value} — exact v1 provides no stable {field} locator"
        return value
    return f"Not Disclosed — exact v1 provides no source locator for {field}; {value}"


def validate_exact_locators(identifier: str, values: list[str]) -> None:
    """Reject synthetic section ranges that are not real document anchors.

    A locator such as ``#S3-S4`` looks precise but points to no HTML element.
    Multi-section evidence must therefore be expressed as multiple exact URLs.
    """
    for value in values:
        for url in re.findall(r"https://arxiv\.org/html/\d{4}\.\d{4,5}v1#[^\s;]+", value):
            fragment = url.split("#", 1)[1]
            if re.search(r"-S\d", fragment):
                raise ValueError(
                    f"{identifier}: compound arXiv HTML fragment is not an exact anchor: {url}"
                )
        if re.search(r"arXiv:\d{4}\.\d{4,5}v1#[^\s;]*-S\d", value):
            raise ValueError(
                f"{identifier}: shorthand compound fragment is not an exact anchor: {value}"
            )


def validate_snapshot_anchors(
    identifier: str,
    snapshot: str | None,
    expected_sha256: str | None,
    values: list[str],
) -> None:
    """Verify exact arXiv HTML fragments against the preserved local snapshot."""
    if not snapshot:
        return
    snapshot_path = Path(snapshot)
    if not snapshot_path.is_absolute():
        snapshot_path = ROOT / snapshot_path
    if snapshot_path.suffix.lower() != ".html" or not snapshot_path.exists():
        return
    payload = snapshot_path.read_bytes()
    if expected_sha256:
        actual_sha256 = hashlib.sha256(payload).hexdigest()
        if actual_sha256 != expected_sha256:
            raise ValueError(
                f"{identifier}: snapshot SHA-256 mismatch for {snapshot_path}: "
                f"expected {expected_sha256}, got {actual_sha256}"
            )
    document = payload.decode("utf-8", errors="ignore")
    anchors = set(re.findall(r'id=["\']([^"\']+)["\']', document))
    for value in values:
        for url in re.findall(r"https://arxiv\.org/html/\d{4}\.\d{4,5}v1#([^\s;]+)", value):
            if url not in anchors:
                raise ValueError(
                    f"{identifier}: locator fragment #{url} is absent from {snapshot_path}"
                )


def validate_artifact_receipt(identifier: str, receipt: object) -> dict | None:
    """Reject prose-only artifact claims before they reach the renderer.

    Coverage receipts are machine interfaces. A sentence may preserve reviewer
    context, but it cannot prove the repository, cutoff, resolved commit and
    execution time as independently addressable fields.
    """
    if receipt is None:
        return None
    if not isinstance(receipt, dict):
        raise ValueError(f"{identifier}: artifact_receipt must be a structured object")
    missing = sorted(ARTIFACT_RECEIPT_FIELDS - set(receipt))
    if missing:
        raise ValueError(f"{identifier}: artifact_receipt missing fields: {missing}")
    return receipt


def normalize_event_time_artifact_receipts(
    identifier: str,
    raw: object,
    *,
    default_until: str,
    executed_at: str,
) -> list[dict]:
    """Convert independently audited event-time receipts to the canonical schema.

    A Source Family may legitimately pin more than one repository. Keep every
    commit as an independent receipt; the report counts unique families as
    coverage hits and commit records as pages/lookups.
    """
    if not isinstance(raw, dict) or not str(raw.get("status", "")).startswith("event_time_"):
        return []
    entries = raw.get("repositories")
    if not isinstance(entries, list):
        entries = [raw]
    normalized: list[dict] = []
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("commit"):
            continue
        cutoff_query = str(entry.get("cutoff_query") or raw.get("cutoff_query") or "")
        until_match = re.search(r"[?&]until=([^&]+)", cutoff_query)
        repository = (
            entry.get("current_redirect")
            or entry.get("repository")
            or entry.get("paper_url")
            or raw.get("repository")
        )
        receipt = {
            "repository": repository or "Not Disclosed",
            "until": until_match.group(1) if until_match else default_until,
            "commit": entry["commit"],
            "commit_timestamp": entry.get("committer_time") or raw.get("committer_time") or "Not Disclosed",
            "url": entry.get("commit_url") or raw.get("commit_url") or "Not Disclosed",
            "executed_at": executed_at,
        }
        validate_artifact_receipt(identifier, receipt)
        normalized.append(receipt)
    return normalized


def normalize_review(review: dict, accessed: str, integration_sections: dict[str, str]) -> tuple[str, dict]:
    identifier = arxiv_id(review)
    declared_route = str(review.get("route") or "").replace("_complete", "")
    locators = review.get("locators", {})
    method = locators.get("method") or review.get("method") or review.get("method_locators")
    evaluation = locators.get("evaluation") or review.get("evaluation") or review.get("evaluation_locators")
    limitations = locators.get("limitations") or review.get("limitations") or review.get("limitations_locators")
    artifact = locators.get("artifact") or review.get("artifact") or review.get("artifact_locator")

    def combine_locator_groups(*groups: object) -> str | None:
        values: list[str] = []
        seen: set[str] = set()
        for group in groups:
            if not group:
                continue
            raw_values = group if isinstance(group, list) else [group]
            for raw_value in raw_values:
                # A pre-audited packet may already serialize a locator list as
                # `; `-separated text.  Split and preserve first occurrence so
                # an ablation anchor shared with Evaluation is represented once.
                for value in str(raw_value).split("; "):
                    if value and value not in seen:
                        seen.add(value)
                        values.append(value)
        return "; ".join(values) if values else None

    # A full review may separate theoretical assumptions, implementation and
    # experimental branches from the main Method/Evaluation headings. Preserve
    # those exact anchors in the canonical receipt instead of silently dropping
    # them during packet normalization.
    method = combine_locator_groups(locators.get("theory"), method, locators.get("implementation"))
    evaluation = combine_locator_groups(
        evaluation,
        locators.get("analysis"),
        locators.get("broader_application"),
        locators.get("ablation"),
    )
    limitations = combine_locator_groups(limitations)
    if declared_route == "closure":
        closure_note = (
            review.get("closure_reason")
            or review.get("rejection_boundary")
            or "identity/date/revision and rejection disposition only"
        )
        method = method or f"Not Required — Closure route: {closure_note}"
        evaluation = evaluation or f"Not Required — Closure route: {closure_note}"
        limitations = limitations or f"Not Required — Closure route: {closure_note}"
        artifact = artifact or f"Not Required — Closure route: {closure_note}"
    exact_locator_values = [str(value) for value in (method, evaluation, limitations) if value]
    validate_exact_locators(identifier, exact_locator_values)
    validate_snapshot_anchors(
        identifier,
        review.get("local_snapshot"),
        review.get("sha256"),
        exact_locator_values,
    )
    if not all((method, evaluation, limitations, artifact)):
        raise ValueError(f"{identifier}: incomplete exact-v1 receipt locators")
    score = score_tuple(review.get("score_v2") or review.get("score"))
    mechanism = (
        review.get("mechanism")
        or review.get("delta")
        or review.get("mechanism_summary")
        or review.get("closure_reason")
    )
    if not mechanism:
        raise ValueError(f"{identifier}: missing reviewed mechanism delta")
    disposition = review.get("books_disposition") or review.get("disposition")
    if disposition == "Version Fact / Mechanism Not Fully Disclosed":
        disposition = "Version Fact / Mechanism Not Disclosed"
    reviewed_versions = review.get("reviewed_evidence_versions")
    if isinstance(reviewed_versions, list):
        reviewed_versions = "; ".join(reviewed_versions)
    review_route = declared_route
    if review_route not in {"deep", "standard", "closure"}:
        review_route = "deep" if sum(score) >= 7 or disposition == "Integrate" else "standard" if sum(score) >= 5 else "closure"
    review_override = review.get("review_override") or (
        "books_conflict" if disposition == "Integrate" and sum(score) < 7 else "none"
    )
    result = {
        "title": review.get("title"),
        "local_snapshot": review.get("local_snapshot"),
        "sha256": review.get("sha256"),
        "node": review.get("owner") or review.get("node") or review.get("stable_node_id"),
        "score": score,
        "route": review_route,
        "review_override": review_override,
        "reviewed": reviewed_versions or review.get("reviewed") or f"SRC-ARXIV@arXiv:{identifier}v1",
        "method": method,
        "evaluation": evaluation,
        "limitations": reasoned_locator(limitations, "limitations/counterevidence"),
        "artifact": reasoned_locator(artifact, "artifact"),
        "accessed": accessed,
        "delta": mechanism,
        "source_claim": review.get("source_claim") or review.get("claim_boundary") or mechanism,
        "analysis_old": (
            review.get("old_solution_and_constraint_change")
            or review.get("analysis_old")
            or review.get("books_review", {}).get("existing_proposition")
            or review.get("state_and_flow")
        ),
        "analysis_tradeoff": (
            review.get("tradeoff_and_failure_modes")
            or review.get("analysis_tradeoff")
            or review.get("benchmark_contract", {}).get("generalization_warning")
            or review.get("claim_boundary")
        ),
        "disposition": disposition,
    }
    benchmark = normalize_benchmark(review.get("benchmark_contract") or review.get("benchmark"), evaluation)
    if benchmark:
        result["benchmark"] = benchmark
    artifact_receipt = validate_artifact_receipt(identifier, review.get("artifact_receipt"))
    if artifact_receipt:
        expected_version = f"SRC-GITHUB-COMMIT@commit:{artifact_receipt['commit']}"
        if expected_version not in result["reviewed"]:
            raise ValueError(
                f"{identifier}: artifact receipt is not present in Reviewed Evidence Versions: "
                f"{expected_version}"
            )
        result["artifact_receipt"] = artifact_receipt
    if identifier in integration_sections:
        if disposition != "Integrate":
            raise ValueError(f"{identifier}: integration section supplied for {disposition!r}")
        result["integration_section"] = integration_sections[identifier]
    return identifier, result


def parse_integrations(values: list[str]) -> dict[str, str]:
    result = {}
    for value in values:
        identifier, separator, section = value.partition("=")
        if not separator or not re.fullmatch(r"\d{4}\.\d{4,5}", identifier) or not section.strip():
            raise ValueError(f"Invalid --integration value: {value!r}")
        result[identifier] = section.strip()
    return result


def normalize_books_comparison_refs(packet: dict) -> None:
    """Remove ephemeral line hints while preserving concrete chapter/section refs."""
    comparisons = packet.get("books_comparison")
    if not comparisons:
        return
    rows = comparisons.values() if isinstance(comparisons, dict) else comparisons

    def stable_ref(value: str) -> str:
        value = re.sub(r"\s*\(current line \d+\)", "", str(value))
        return value.replace("#", " — ", 1)

    for row in rows:
        if row.get("target_ref"):
            row["target_ref"] = stable_ref(row["target_ref"])
        if row.get("adjacent_refs"):
            row["adjacent_refs"] = [stable_ref(ref) for ref in row["adjacent_refs"]]


def packet_exact_ids(packet: dict) -> set[str]:
    """Return the arXiv IDs whose exact receipts belong to one persisted day."""
    if packet.get("central_receipts"):
        return set(packet["central_receipts"])
    reviews = packet.get("full_source_reviews") or packet.get("families", [])
    return {arxiv_id(review) for review in reviews}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--date", required=True, help="YYYY-MM-DD report date")
    parser.add_argument("--accessed", required=True, help="YYYY-MM-DD access date")
    parser.add_argument("--integration", action="append", default=[], metavar="ARXIV_ID=SECTION")
    parser.add_argument(
        "--replace-date",
        action="store_true",
        help="Replace only receipts owned by the already-persisted packet for this date.",
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    packet = json.loads(args.packet.read_text(encoding="utf-8"))
    packet_date = packet.get("report_date") or packet.get("date")
    if packet_date != args.date:
        raise ValueError(f"Packet date {packet_date!r} != {args.date!r}")
    unresolved = packet.get("unresolved")
    has_unresolved = (
        any(unresolved.values()) if isinstance(unresolved, dict) else bool(unresolved)
    )
    if has_unresolved:
        raise ValueError(f"Packet still has unresolved rows: {unresolved!r}")
    integrations = parse_integrations(args.integration)
    normalize_books_comparison_refs(packet)
    selection = packet.get("deep_analysis_selection")
    if isinstance(selection, dict) and isinstance(selection.get("family_decisions"), list):
        # The selection ledger is an eligibility-pool contract, not a second
        # candidate ledger. Standard/Closure families keep their full Source
        # Review and Books Comparison, but must not appear as empty or
        # ``not_eligible`` rows in the Deep-selection table.
        packet_receipts = packet.get("central_receipts", {})
        deep_ids = {
            identifier
            for identifier, receipt in packet_receipts.items()
            if str(receipt.get("route") or "").replace("_complete", "") == "deep"
        }
        selection["family_decisions"] = [
            decision
            for decision in selection["family_decisions"]
            if decision.get("decision") in {"selected", "not_selected"}
            and bool(decision.get("eligibility"))
            and (
                not deep_ids
                or re.sub(
                    r"^SF-\d{4}-ARXIV-", "", str(decision.get("source_family_id") or "")
                ).replace("-", ".", 1)
                in deep_ids
            )
        ]
    # Normalize every packet-level review as well as the canonical receipt.
    # Otherwise the persisted packet can retain an ephemeral /private/tmp path
    # even though the central ledger points to the durable repository copy.
    # Both representations are independently audited and must share one
    # provenance locator.
    packet_reviews = packet.get("full_source_reviews") or packet.get("families", [])
    packet_review_by_id = {
        arxiv_id(review): review
        for review in packet_reviews
        if arxiv_id(review)
    }
    for review in packet_reviews:
        normalize_durable_snapshots(arxiv_id(review), review)
    if packet.get("central_receipts"):
        receipts = packet["central_receipts"]
        strict_window = packet.get("strict_window")
        coverage_window = packet.get("coverage_window")
        end_text = (
            strict_window.get("end") if isinstance(strict_window, dict) else None
        ) or (
            coverage_window.get("end") if isinstance(coverage_window, dict) else None
        )
        if end_text:
            default_until = (
                datetime.fromisoformat(str(end_text))
                .astimezone(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z")
            )
        else:
            default_until = f"{args.date}T01:00:00Z"
        executed_at = str(packet.get("reviewed_at") or f"{args.accessed}T00:00:00+08:00")
        packet_artifacts = packet.get("artifact_event_time_receipts", {})
        for identifier, receipt in receipts.items():
            source_review = packet_review_by_id.get(identifier, {})
            if source_review.get("local_snapshot"):
                receipt["local_snapshot"] = source_review["local_snapshot"]
            if source_review.get("sha256"):
                receipt["sha256"] = source_review["sha256"]
            canonical_versions = [f"SRC-ARXIV@arXiv:{identifier}v1"]
            raw_artifact_receipt = (
                receipt.get("artifact_event_time_receipt")
                or packet_artifacts.get(identifier)
            )
            normalized_artifacts = normalize_event_time_artifact_receipts(
                identifier,
                raw_artifact_receipt,
                default_until=default_until,
                executed_at=executed_at,
            )
            if not normalized_artifacts:
                existing_artifacts = receipt.get("artifact_receipts")
                if isinstance(existing_artifacts, list):
                    normalized_artifacts = existing_artifacts
                elif isinstance(receipt.get("artifact_receipt"), dict):
                    normalized_artifacts = [receipt["artifact_receipt"]]
            if normalized_artifacts:
                receipt["artifact_receipts"] = normalized_artifacts
                receipt["artifact_receipt"] = normalized_artifacts[0]
                canonical_versions.extend(
                    f"SRC-GITHUB-COMMIT@commit:{item['commit']}"
                    for item in normalized_artifacts
                )
            receipt["reviewed"] = "; ".join(canonical_versions)
            artifact_locator = (
                source_review.get("artifact_locator")
                or source_review.get("locators", {}).get("artifact")
            )
            current_artifact = str(receipt.get("artifact") or "")
            artifact_receipt = receipt.get("artifact_receipt") or {}
            receipt_locator = (
                artifact_receipt.get("url")
                or artifact_receipt.get("repository")
                if isinstance(artifact_receipt, dict)
                else None
            )
            if artifact_locator and not re.search(
                r"https?://|doi:|arXiv:", current_artifact, re.IGNORECASE
            ):
                receipt["artifact"] = artifact_locator
            elif receipt_locator and not re.search(
                r"https?://|doi:|arXiv:", current_artifact, re.IGNORECASE
            ):
                boundary = re.sub(
                    r"^Not Disclosed\s*[—-]\s*exact v1 provides no source locator for artifact;\s*",
                    "",
                    current_artifact,
                    flags=re.IGNORECASE,
                ).strip()
                receipt["artifact"] = (
                    f"{receipt_locator} — disclosed artifact locator; "
                    f"{boundary or 'event-time immutable commit/hash was not audited, so no current-code claim is retained.'}"
                )
            if source_review.get("evolution_relation"):
                receipt["evolution_relation"] = source_review["evolution_relation"]
            score_tuple(receipt["score"])
            review_route = str(receipt.get("route") or "").replace("_complete", "")
            if review_route not in {"deep", "standard", "closure"}:
                raise ValueError(
                    f"Invalid central receipt route for {identifier}: {receipt.get('route')!r}"
                )
            receipt["route"] = review_route
            receipt["review_override"] = str(
                receipt.get("review_override") or "none"
            ).strip().lower()
            receipt["limitations"] = reasoned_locator(
                receipt.get("limitations") or "Not Disclosed",
                "limitations/counterevidence",
            )
            receipt["artifact"] = reasoned_locator(
                receipt.get("artifact") or "Not Disclosed",
                "artifact",
            )
            # The packet-level full review is the editable evidence contract.
            # When a semantic audit refines disclosed benchmark fields, do not
            # keep an older normalized copy from ``central_receipts`` merely
            # because that cache already exists. Re-normalize from the source
            # review and let the central ledger remain a derived interface.
            benchmark = normalize_benchmark(
                source_review.get("benchmark_contract")
                or source_review.get("benchmark")
                or receipt.get("benchmark"),
                str(receipt.get("evaluation") or "Not Disclosed"),
            )
            if benchmark:
                receipt["benchmark"] = benchmark
            else:
                receipt.pop("benchmark", None)
            normalize_durable_snapshots(identifier, receipt)
            for artifact_item in receipt.get("artifact_receipts", []):
                validate_artifact_receipt(identifier, artifact_item)
            validate_artifact_receipt(identifier, receipt.get("artifact_receipt"))
            if identifier in integrations:
                receipt["integration_section"] = integrations[identifier]
    else:
        reviews = packet.get("full_source_reviews") or packet.get("families", [])
        receipts = dict(
            normalize_review(review, args.accessed, integrations)
            for review in reviews
        )
        for identifier, receipt in receipts.items():
            normalize_durable_snapshots(identifier, receipt)
    closures = packet.get("closure_reviews", [])
    for closure in closures:
        identifier = arxiv_id(closure)
        identity_closure = closure.get("identity_date_revision_closure")
        if isinstance(identity_closure, dict):
            closure.setdefault("local_snapshot", identity_closure.get("exact_v1_snapshot"))
            closure.setdefault("sha256", identity_closure.get("sha256"))
        normalize_durable_snapshots(identifier, closure)
        closure_id, closure_receipt = normalize_review(
            closure, args.accessed, integrations
        )
        if closure_id in receipts:
            raise ValueError(
                f"{closure_id}: closure review duplicates an existing central receipt"
            )
        normalize_durable_snapshots(closure_id, closure_receipt)
        receipts[closure_id] = closure_receipt
    expected = (
        packet.get("frozen_denominator", {}).get("count")
        or packet.get("source_denominator", {}).get("count")
        or packet.get("denominator_audit", {}).get("frozen_count")
        or packet.get("denominator_count")
    )
    if expected is not None and len(receipts) != expected:
        raise ValueError(
            f"Denominator mismatch: {len(receipts)} canonical receipts != {expected}"
        )
    missing_integrations = [
        identifier
        for identifier, receipt in receipts.items()
        if receipt.get("disposition") == "Integrate" and not receipt.get("integration_section")
    ]
    if args.write and missing_integrations:
        raise ValueError(
            "Books integration sections are required before write: "
            + ", ".join(sorted(missing_integrations))
        )
    print(json.dumps({"date": args.date, "exact_receipts": len(receipts), "closures": len(closures)}, ensure_ascii=False))
    if not args.write:
        return

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    overlap = set(ledger).intersection(receipts)
    if overlap and not args.replace_date:
        raise ValueError(f"Refusing to overwrite existing receipts: {sorted(overlap)}")
    if args.replace_date:
        old_packet_path = PACKET_DIR / f"{args.date}.json"
        if not old_packet_path.exists():
            raise ValueError(f"Cannot replace missing persisted packet: {old_packet_path}")
        old_packet = json.loads(old_packet_path.read_text(encoding="utf-8"))
        old_exact = packet_exact_ids(old_packet)
        unexpected = overlap - old_exact
        if unexpected:
            raise ValueError(
                f"Refusing to overwrite receipts owned by another date: {sorted(unexpected)}"
            )
        for identifier in old_exact:
            ledger.pop(identifier, None)
    ledger.update(receipts)
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    # Persist the normalized in-memory receipts, including caller-supplied
    # Books integration sections. Copying the raw input packet here would make
    # the per-day evidence packet disagree with the central receipt ledger.
    packet["central_receipts"] = receipts
    (PACKET_DIR / f"{args.date}.json").write_text(
        json.dumps(packet, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
