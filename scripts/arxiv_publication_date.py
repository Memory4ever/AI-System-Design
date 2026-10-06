"""Local arXiv v1 announcement envelope; not a first-publication certificate.

Implements docs/RESEARCH_CONTRACT.md section 2, using the announcement schedule
at https://info.arxiv.org/help/availability.html and DataCite's distinction
between created and registered. Raw provenance and known earlier-text,
withdrawal or revision events still require human review.
"""

import argparse
from datetime import datetime, time, timedelta, timezone
import json
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo


UTC = timezone.utc
NEW_YORK = ZoneInfo("America/New_York")
BJT = ZoneInfo("Asia/Shanghai")
IDENTITY = re.compile(r"(?P<id>\d{4}\.\d{4,5}|[a-z][a-z.-]+/\d{7})(?P<version>v\d+)?")
TIMESTAMP = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})")
LIMITATIONS = (
    "Conditional arXiv v1 announcement day only; not global first publication.",
    "Raw-source authenticity and earlier text, withdrawal or revision signals require human review.",
    "The schedule is a lower bound, not evidence of completed announcement; delays may occur.",
)


def _record(raw):
    # Support a single JSON:API resource and common saved payload/data wrappers.
    for _ in range(4):
        if not isinstance(raw, dict):
            return None
        if "attributes" in raw:
            return raw if isinstance(raw["attributes"], dict) else None
        wrappers = [key for key in ("payload", "data") if key in raw]
        if len(wrappers) != 1:
            return None
        raw = raw[wrappers[0]]
    return None


def _timestamp(value):
    if not isinstance(value, str) or not TIMESTAMP.fullmatch(value):
        raise ValueError("Expected a timezone-aware RFC3339 timestamp")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _earliest_announcement(submitted):
    local = submitted.astimezone(NEW_YORK)
    weekday = local.weekday()
    boundary = weekday < 5 and local.time() == time(14)
    # At the exact cutoff retain the earlier allowed bound, never the next one.
    before_or_at = local.time() <= time(14)
    if weekday < 4:
        days = 0 if before_or_at else (3 if weekday == 3 else 1)
    elif weekday == 4:
        days = 2 if before_or_at else 3
    else:
        days = 7 - weekday
    day = local.date() + timedelta(days=days)
    return datetime.combine(day, time(20), NEW_YORK).astimezone(UTC), boundary


def _iso(value):
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z")


def publication_date_envelope(raw, arxiv_id):
    """Return JSON-safe bounds without I/O, mutation or created-date fallback.

    arxiv_id is the expected bare ID (optionally v1), not an inferred identity.
    A bounded result only applies under the contract's announcement/ID rules.
    JSON duplicate keys must be rejected before parsing (as the CLI does).
    """
    result = {
        "status": "unresolved", "arxiv_id": arxiv_id,
        "scope": "arxiv_v1_announcement_only", "bounded_bjt_date": None,
        "earliest_announcement_utc": None, "registered_upper_utc": None,
        "source_fields": {}, "reasons": [], "limitations": list(LIMITATIONS),
    }
    reasons = result["reasons"]
    match = IDENTITY.fullmatch(arxiv_id) if isinstance(arxiv_id, str) else None
    if not match:
        reasons.append("invalid_arxiv_id")
        return result
    identity = match.group("id")
    result["arxiv_id"] = identity
    if match.group("version") not in (None, "v1"):
        reasons.append("version_conflict")
    resource = _record(raw)
    if resource is None:
        reasons.append("invalid_record")
        return result
    attributes = resource["attributes"]
    client = resource.get("relationships", {})
    for key in ("client", "data", "id"):
        client = client.get(key) if isinstance(client, dict) else None
    doi = attributes.get("doi")
    result["source_fields"] = {
        "record_id": resource.get("id"), "doi": doi, "client_id": client,
        "publisher": attributes.get("publisher"), "state": attributes.get("state"),
        "registered": attributes.get("registered"), "created": attributes.get("created"),
    }
    expected_doi = "10.48550/arxiv." + identity
    if any(not isinstance(value, str) or value.lower() != expected_doi
           for value in (doi, resource.get("id"))):
        reasons.append("doi_mismatch")
    if client != "arxiv.content" or attributes.get("clientId", client) != client:
        reasons.append("client_mismatch")
    if attributes.get("publisher") != "arXiv":
        reasons.append("publisher_mismatch")
    if attributes.get("state") != "findable":
        reasons.append("not_findable")
    dates = attributes.get("dates")
    if not isinstance(dates, list):
        reasons.append("invalid_dates")
        dates = []
    submitted_dates = [item.get("date") for item in dates if isinstance(item, dict)
                       and item.get("dateType") == "Submitted"
                       and item.get("dateInformation") == "v1"]
    earliest = None
    if len(submitted_dates) != 1:
        reasons.append("missing_v1_submitted" if not submitted_dates else "multiple_v1_submitted")
    else:
        result["source_fields"]["submitted_v1"] = submitted_dates[0]
        try:
            earliest, boundary = _earliest_announcement(_timestamp(submitted_dates[0]))
            result["earliest_announcement_utc"] = _iso(earliest)
            if boundary:
                reasons.append("cutoff_boundary")
        except (ValueError, OverflowError):
            reasons.append("invalid_v1_submitted")
    registered = None
    if attributes.get("registered") in (None, ""):
        reasons.append("missing_registered")
    else:
        try:
            parsed = _timestamp(attributes["registered"])
            if parsed.utcoffset() != timedelta(0):
                reasons.append("registered_not_utc")
            else:
                registered = parsed
                result["registered_upper_utc"] = _iso(registered)
        except (ValueError, OverflowError):
            reasons.append("invalid_registered")
    # Optional draft creation is only a consistency check, never either bound.
    if attributes.get("created") not in (None, ""):
        try:
            created = _timestamp(attributes["created"])
            if registered is not None and created > registered:
                reasons.append("created_after_registered")
        except (ValueError, OverflowError):
            reasons.append("invalid_created")
    if earliest is not None and registered is not None:
        if registered < earliest:
            reasons.append("reversed_bounds")
        elif earliest.astimezone(BJT).date() != registered.astimezone(BJT).date():
            reasons.append("cross_bjt_dates")
        elif not reasons:
            # An incompatibility veto only: ID months never supply/tighten a bound.
            compatible_months = {bound.astimezone(zone).strftime("%y%m")
                                 for bound in (earliest, registered)
                                 for zone in (UTC, NEW_YORK, BJT)}
            if "/" in identity:
                reasons.append("legacy_id_month_unverified")
            elif identity[:4] not in compatible_months:
                reasons.append("id_month_conflict")
            else:
                result["status"] = "bounded"
                result["bounded_bjt_date"] = earliest.astimezone(BJT).date().isoformat()
    return result


def _unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key: " + key)
        result[key] = value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("raw_json", help="Single local DataCite JSON file, or - for stdin")
    parser.add_argument("--arxiv-id", required=True, help="Expected exact arXiv ID (bare or v1)")
    args = parser.parse_args(argv)
    try:
        text = sys.stdin.read() if args.raw_json == "-" else Path(args.raw_json).read_text(encoding="utf-8")
        raw = json.loads(text, object_pairs_hook=_unique_keys)
    except (OSError, UnicodeError, ValueError) as error:
        print("Input error: " + str(error), file=sys.stderr)
        return 2
    result = publication_date_envelope(raw, args.arxiv_id)
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0 if result["status"] == "bounded" else 1


if __name__ == "__main__":
    sys.exit(main())
