#!/usr/bin/env python3
"""Build the independent 371-row identity/date provenance receipt for 2026-06-01.

Identifier shape is used only as a review trigger.  Ownership is decided from
the official arXiv-issued DataCite DOI/Submitted-version chain, reconciled with
the frozen Atom identity, authors, current title and revision metadata.
"""

from __future__ import annotations

import csv
import gzip
import json
import re
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PACKET = Path(__file__).resolve().parent
LEDGER = PACKET / "screening-ledger.tsv"
ATOM = PACKET / "arxiv-overread-first-page.atom.gz"
DATACITE_CACHE = Path("/private/tmp/june01-datacite-v9-20260828")
RECEIPT = PACKET / "fresh-context-identity-date-provenance-independent-v9.tsv"
CHECKPOINT = PACKET / "fresh-context-identity-date-provenance-independent-v9.md"

WINDOW_START = datetime(2026, 5, 31, 1, 0, 0, tzinfo=timezone.utc)
WINDOW_END = datetime(2026, 6, 1, 1, 0, 0, tzinfo=timezone.utc)


# These 15 rows differ between the event-time ledger title and the current
# Atom/DataCite title.  Packet-local exact-v1 material preserves the event-time
# title.  Three official live v1 pages now expose the shorter current title;
# this is title metadata evolution on the same identifier/DOI/v1 timestamp.
TITLE_EVOLUTION = {
    "2606.00967": (
        "event-time-title-confirmed-current-title-evolved",
        "arxiv-v1-metadata/2606.00967v1.abs.html",
    ),
    "2606.01009": (
        "event-time-title-confirmed-current-title-evolved",
        "arxiv-v1-metadata/2606.01009v1.abs.html",
    ),
    "2606.01026": ("punctuation-only-event-title-equivalent", "arxiv-v1/2606.01026v1.html"),
    "2606.01049": (
        "event-time-title-confirmed-current-title-evolved",
        "arxiv-v1-metadata/2606.01049v1.abs.html",
    ),
    "2606.01063": (
        "event-time-title-confirmed-current-title-evolved",
        "arxiv-v1-metadata/2606.01063v1.abs.html",
    ),
    "2606.01101": (
        "live-v1-title-residual-with-local-event-artifact",
        "arxiv-v1/2606.01101v1.html",
    ),
    "2606.01173": (
        "event-time-title-confirmed-current-title-evolved",
        "arxiv-v1-metadata/2606.01173v1.abs.html",
    ),
    "2606.01185": ("punctuation-only-event-title-equivalent", "arxiv-v1/2606.01185v1.html"),
    "2606.01372": (
        "event-time-title-confirmed-current-title-evolved",
        "arxiv-v1-metadata/2606.01372v1.abs.html",
    ),
    "2606.01374": (
        "event-time-title-confirmed-current-title-evolved",
        "arxiv-v1-metadata/2606.01374v1.abs.html",
    ),
    "2606.01435": (
        "event-time-title-confirmed-current-title-evolved",
        "arxiv-v1/2606.01435v1.html",
    ),
    "2606.01495": ("punctuation-only-event-title-equivalent", "arxiv-v1/2606.01495v1.html"),
    "2606.01502": (
        "live-v1-title-residual-with-local-event-artifact",
        "arxiv-v1/2606.01502v1.html",
    ),
    "2606.01518": (
        "event-time-title-confirmed-current-title-evolved",
        "arxiv-v1-metadata/2606.01518v1.abs.html",
    ),
    "2606.07632": (
        "live-v1-title-residual-with-local-event-artifact",
        "arxiv-v1/2606.07632v1.html",
    ),
}


# Fresh official arXiv v1 pages were independently opened for seven of the
# eleven identifier-month review triggers.  The other four returned a web-cache
# miss; their official DataCite exact-v1/DOI chain and frozen Atom chain remain
# complete and are not a material/access blocker.
LIVE_V1_CONFIRMED_LATER_ID = {
    "2608.18080",
    "2607.21618",
    "2608.12327",
    "2607.24761",
    "2607.22566",
    "2607.22567",
    "2607.22568",
}
LIVE_V1_CACHE_MISS_LATER_ID = {
    "2608.18081",
    "2608.02618",
    "2608.21363",
    "2608.12328",
}


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def normalized_name(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value.casefold())
    return "".join(char for char in normalized if char.isalnum())


def parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def read_ledger() -> list[dict[str, str]]:
    with LEDGER.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_atom(ledger_ids: set[str]) -> dict[str, dict[str, object]]:
    ns = {"a": "http://www.w3.org/2005/Atom"}
    with gzip.open(ATOM, "rb") as handle:
        root = ET.parse(handle).getroot()
    records: dict[str, dict[str, object]] = {}
    for entry in root.findall("a:entry", ns):
        versioned_id = clean(entry.findtext("a:id", default="", namespaces=ns)).rsplit("/", 1)[-1]
        arxiv_id = re.sub(r"v\d+$", "", versioned_id)
        if arxiv_id not in ledger_ids:
            continue
        records[arxiv_id] = {
            "versioned_id": versioned_id,
            "version": int(re.search(r"v(\d+)$", versioned_id).group(1)),
            "title": clean(entry.findtext("a:title", default="", namespaces=ns)),
            "published": clean(entry.findtext("a:published", default="", namespaces=ns)),
            "updated": clean(entry.findtext("a:updated", default="", namespaces=ns)),
            "authors": [clean(author.findtext("a:name", default="", namespaces=ns)) for author in entry.findall("a:author", ns)],
        }
    return records


def datacite_creators(attributes: dict[str, object]) -> list[str]:
    creators: list[str] = []
    for creator in attributes["creators"]:
        full = clean(" ".join(part for part in (creator.get("givenName"), creator.get("familyName")) if part))
        creators.append(full or clean(creator.get("name", "")))
    return creators


def review_trigger(arxiv_id: str) -> str:
    prefix, suffix = arxiv_id.split(".")
    if prefix != "2606":
        return "identifier-month-review-trigger"
    if int(suffix) > 1600:
        return "high-sequence-review-trigger"
    return "normal-full-reconciliation"


def write_tsv(rows: list[dict[str, str]]) -> None:
    with RECEIPT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    ledger = read_ledger()
    ledger_ids = {row["arxiv_id"] for row in ledger}
    atom = read_atom(ledger_ids)
    assert len(ledger) == 371
    assert len(ledger_ids) == 371
    assert len(atom) == 371
    assert len(TITLE_EVOLUTION) == 15
    assert LIVE_V1_CONFIRMED_LATER_ID.isdisjoint(LIVE_V1_CACHE_MISS_LATER_ID)
    assert LIVE_V1_CONFIRMED_LATER_ID | LIVE_V1_CACHE_MISS_LATER_ID == {
        arxiv_id for arxiv_id in ledger_ids if not arxiv_id.startswith("2606.")
    }

    rows: list[dict[str, str]] = []
    for ledger_row in ledger:
        arxiv_id = ledger_row["arxiv_id"]
        atom_row = atom[arxiv_id]
        datacite_path = DATACITE_CACHE / f"{arxiv_id}.json"
        assert datacite_path.exists(), datacite_path
        attributes = json.loads(datacite_path.read_text(encoding="utf-8"))["data"]["attributes"]

        alternate_ids = attributes.get("alternateIdentifiers", [])
        alternate_id = next(
            item["alternateIdentifier"]
            for item in alternate_ids
            if item.get("alternateIdentifierType") == "arXiv"
        )
        official_doi = clean(attributes["doi"])
        official_title = clean(attributes["titles"][0]["title"])
        creators = datacite_creators(attributes)
        submitted = [item for item in attributes["dates"] if item.get("dateType") == "Submitted"]
        submitted_by_version = {
            int(re.fullmatch(r"v(\d+)", item["dateInformation"]).group(1)): item["date"]
            for item in submitted
        }
        official_v1 = submitted_by_version[1]
        official_version = int(attributes["version"])
        latest_submitted = submitted_by_version[max(submitted_by_version)]
        withdrawn = [item for item in attributes["dates"] if item.get("dateType") == "Withdrawn"]

        assert alternate_id == arxiv_id
        assert official_doi.casefold() == f"10.48550/arxiv.{arxiv_id}".casefold()
        assert ledger_row["first_public_utc"] == official_v1
        assert atom_row["published"] == official_v1
        assert atom_row["title"] == official_title
        assert atom_row["version"] == official_version
        assert [normalized_name(name) for name in atom_row["authors"]] == [
            normalized_name(name) for name in creators
        ]

        title_differs = clean(ledger_row["title"]) != official_title
        assert title_differs == (arxiv_id in TITLE_EVOLUTION), arxiv_id
        if title_differs:
            title_class, title_locator = TITLE_EVOLUTION[arxiv_id]
            assert (PACKET / title_locator).exists(), title_locator
        else:
            title_class, title_locator = "stable-event-current-title-match", "—"

        if official_version in submitted_by_version and atom_row["updated"] == submitted_by_version[official_version]:
            revision_status = "submitted-version-chain-match"
            current_version_event_utc = submitted_by_version[official_version]
            withdrawal_notice = "—"
        else:
            current_withdrawal = [
                item
                for item in withdrawn
                if item.get("dateInformation", "").startswith(f"v{official_version};")
            ]
            assert len(current_withdrawal) == 1, (arxiv_id, submitted_by_version, withdrawn)
            assert atom_row["updated"] == current_withdrawal[0]["date"]
            revision_status = "withdrawn-current-version-exact-history-match"
            current_version_event_utc = current_withdrawal[0]["date"]
            withdrawal_notice = clean(current_withdrawal[0]["dateInformation"])

        if arxiv_id in LIVE_V1_CONFIRMED_LATER_ID:
            live_v1_status = "fresh-official-v1-page-confirmed"
        elif arxiv_id in LIVE_V1_CACHE_MISS_LATER_ID:
            live_v1_status = "official-datacite-v1-chain-confirmed-web-cache-miss"
        else:
            live_v1_status = "official-datacite-v1-chain-confirmed"

        in_window = WINDOW_START <= parse_utc(official_v1) < WINDOW_END
        rows.append(
            {
                "arxiv_id": arxiv_id,
                "review_trigger": review_trigger(arxiv_id),
                "ledger_first_public_utc": ledger_row["first_public_utc"],
                "official_v1_submitted_utc": official_v1,
                "in_beijing_daily_window": "yes" if in_window else "no",
                "ledger_event_title": clean(ledger_row["title"]),
                "official_datacite_current_title": official_title,
                "atom_current_title": atom_row["title"],
                "title_chain_class": title_class,
                "event_time_exact_v1_title_locator": title_locator,
                "atom_identity_version": atom_row["versioned_id"],
                "official_datacite_version": str(official_version),
                "atom_updated_utc": atom_row["updated"],
                "official_latest_submitted_utc": latest_submitted,
                "official_current_version_event_utc": current_version_event_utc,
                "revision_chain_status": revision_status,
                "withdrawal_notice": withdrawal_notice,
                "atom_authors": "; ".join(atom_row["authors"]),
                "official_datacite_creators": "; ".join(creators),
                "author_chain_status": "normalized-order-match",
                "official_doi": official_doi,
                "official_alternate_identifier": alternate_id,
                "official_datacite_locator": f"https://api.datacite.org/dois/10.48550/arXiv.{arxiv_id}",
                "official_exact_v1_locator": f"https://arxiv.org/abs/{arxiv_id}v1",
                "live_exact_v1_status": live_v1_status,
                "identity_date_resolution": "same-identity-official-v1-in-window",
                "audit_status": "fresh-context-independent-provenance-reconciled",
            }
        )

    rows.sort(key=lambda row: (row["official_v1_submitted_utc"], row["arxiv_id"]))
    write_tsv(rows)

    trigger_counts = Counter(row["review_trigger"] for row in rows)
    title_counts = Counter(row["title_chain_class"] for row in rows)
    revision_counts = Counter(row["revision_chain_status"] for row in rows)
    live_counts = Counter(row["live_exact_v1_status"] for row in rows)
    assert Counter(row["in_beijing_daily_window"] for row in rows) == {"yes": 371}
    assert Counter(row["identity_date_resolution"] for row in rows) == {
        "same-identity-official-v1-in-window": 371
    }
    assert trigger_counts == {
        "normal-full-reconciliation": 326,
        "high-sequence-review-trigger": 34,
        "identifier-month-review-trigger": 11,
    }
    assert title_counts == {
        "stable-event-current-title-match": 356,
        "event-time-title-confirmed-current-title-evolved": 9,
        "punctuation-only-event-title-equivalent": 3,
        "live-v1-title-residual-with-local-event-artifact": 3,
    }
    assert revision_counts == {
        "submitted-version-chain-match": 366,
        "withdrawn-current-version-exact-history-match": 5,
    }
    assert live_counts == {
        "official-datacite-v1-chain-confirmed": 360,
        "fresh-official-v1-page-confirmed": 7,
        "official-datacite-v1-chain-confirmed-web-cache-miss": 4,
    }

    title_rows = [row for row in rows if row["title_chain_class"] != "stable-event-current-title-match"]
    revision_rows = [row for row in rows if row["revision_chain_status"] != "submitted-version-chain-match"]

    def md(value: str) -> str:
        return clean(value).replace("|", "\\|")

    def table(selected: list[dict[str, str]], fields: list[tuple[str, str]]) -> str:
        result = ["| " + " | ".join(label for label, _ in fields) + " |"]
        result.append("| " + " | ".join("---" for _ in fields) + " |")
        for row in selected:
            result.append("| " + " | ".join(md(row[key]) for _, key in fields) + " |")
        return "\n".join(result)

    checkpoint = f"""# 2026-06-01 Identity/Date Provenance Audit — Fresh-Context Independent V9

## Outcome

- Scope: **371/371** raw ledger identities; no sampling.
- Official chain: arXiv-issued DataCite DOI, exact `Submitted v1`, all submitted versions, current title/creators and alternate arXiv identifier, reconciled with the frozen Atom identity/title/authors/published/updated chain.
- Correct in-window raw identities: **371/371**. Identity mismatch=0; DOI mismatch=0; exact-v1 timestamp mismatch=0; author mismatch=0; out-of-window=0.
- Identifier shape was only a review trigger: normal full reconciliation={trigger_counts['normal-full-reconciliation']}; high-sequence trigger={trigger_counts['high-sequence-review-trigger']}; identifier-month trigger={trigger_counts['identifier-month-review-trigger']}. No row was reassigned from prefix/sequence inference.
- Title chain: 356 stable matches; 15 event-time ledger/current metadata differences = 9 confirmed title evolutions, 3 punctuation-only equivalents and 3 live-v1 current-title residuals with packet-local event-time exact-v1 artifacts.
- Revision chain: 366 submitted-version chains align exactly; 5 current `v2` withdrawals are preserved below. DataCite exposes a `Withdrawn v2` event rather than a `Submitted v2` event, and Atom's current `v2` timestamp matches the withdrawal event exactly.
- Later-identifier direct v1 trigger review: 7 fresh official v1 pages opened successfully; 4 page-cache misses are covered by the official DataCite exact-v1/DOI chain plus frozen Atom identity/author/title chain. There is no material/access blocker.

The authoritative row-level receipt is `{RECEIPT.name}`. Every row preserves both official locators and the compared identity/date/title/author/revision values.

## Title evolution / residual rows (15)

{table(title_rows, [('arXiv', 'arxiv_id'), ('Event-time title', 'ledger_event_title'), ('Current official title', 'official_datacite_current_title'), ('Class', 'title_chain_class'), ('Event artifact', 'event_time_exact_v1_title_locator')])}

The three `live-v1-title-residual-with-local-event-artifact` rows are `2606.01101`, `2606.01502` and `2606.07632`: the current official v1 page and DataCite/Atom expose the shorter current title, while the packet-local exact-v1 artifact preserves the event-time ledger title. Exact identifier, authors, DOI and Submitted-v1 timestamp remain the same, so these are title metadata evolution rather than corrupt or misassigned identities.

## Current-version withdrawal rows (5)

{table(revision_rows, [('arXiv', 'arxiv_id'), ('Atom identity', 'atom_identity_version'), ('Atom/current-version event', 'official_current_version_event_utc'), ('Latest official Submitted', 'official_latest_submitted_utc'), ('Withdrawal notice', 'withdrawal_notice'), ('Resolution', 'revision_chain_status')])}

These rows remain identity/date-reconciled because the official `Submitted v1` event still exactly matches the Daily event. The later withdrawal materially weakens or removes the paper as evidence, however: three notices cite author-authenticity concerns, one cites unresolved authorship and scientific-validation issues, and one redirects the work to another arXiv identity. All five are semantic closures in the strict denominator receipt; none is retained.

## Denominator implication and Gate truth

- The provenance audit finds no corrupt/misassigned raw identity and no out-of-window owner transfer. The correct raw in-window accounting remains **371**.
- This receipt only resolves identity/date provenance. It does not by itself approve the Candidate Denominator semantic proposal, Source Reviews, Daily body, Selection, Books Comparison or Books.
- Coverage, Evidence, Selection, Books Comparison and Books Gates remain **Open** pending root reconciliation/refreeze and the required downstream fresh-context audits.
"""
    CHECKPOINT.write_text(checkpoint, encoding="utf-8")
    print(
        "rows=371 in_window=371 identity_mismatch=0 doi_mismatch=0 "
        "v1_timestamp_mismatch=0 author_mismatch=0 title_evolution=15 "
        "current_version_withdrawal=5 material_blocker=0"
    )


if __name__ == "__main__":
    main()
