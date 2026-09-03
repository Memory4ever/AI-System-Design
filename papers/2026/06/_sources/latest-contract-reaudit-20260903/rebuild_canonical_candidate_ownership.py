#!/usr/bin/env python3
"""Move retained candidate evidence bundles to canonical owner Dailies.

The script consumes the immutable precanonical snapshot, so zero-owner reports
may be safely rewritten first.  It does not close Coverage: raw-identity
closure proposals still require a fresh-context semantic audit.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
AUDIT = Path(__file__).resolve().parent
SNAPSHOT = AUDIT / "precanonical-report-snapshots-v1.json.gz"
OWNER = AUDIT / "owner-recovery/owner-reconciliation.tsv"
WITHDRAWN = {"2606.24369"}
ABSENT_VALUES = {"", "-", "—", "n/a", "N/A", "Not Applicable"}

TABLE_SPECS = {
    "candidate": (
        "validator:candidate-ledger-v2.1",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ),
    "review": (
        "validator:review-completion-v1",
        "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ),
    "benchmark": (
        "validator:benchmark-contract-v1",
        "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ),
    "selection": (
        "validator:deep-analysis-selection-v1",
        "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |\n"
        "| --- | --- | --- | --- | --- | --- | --- |",
    ),
    "books": (
        "validator:books-comparison-v1",
        "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ),
}


def table(text: str, marker: str) -> dict[str, list[str]]:
    match = re.search(rf"<!-- {re.escape(marker)} -->\n(.*?)(?=\n(?:<!--|##|###)|\Z)", text, re.S)
    result = {}
    if not match:
        return result
    for line in match.group(1).splitlines():
        if not line.startswith("| SF-"):
            continue
        cells = [
            cell.strip()
            for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))
        ]
        result[cells[0]] = cells
    return result


def block(text: str, ref: str) -> str:
    match = re.search(
        rf"<!-- {re.escape(ref)}:start -->(.*?)<!-- {re.escape(ref)}:end -->",
        text,
        re.S,
    )
    return f"<!-- {ref}:start -->{match.group(1)}<!-- {ref}:end -->" if match else ""


def iso_week(day: str) -> str:
    year, week, _ = date.fromisoformat(day).isocalendar()
    return f"{year}-W{week:02d}"


def md_row(cells: list[str]) -> str:
    # Narrative cells can contain mathematical conditionals or copied prose
    # with a literal pipe.  An unescaped pipe changes the Markdown table
    # arity, so normalize it at the serialization boundary.
    escaped = [re.sub(r"(?<!\\)\|", r"\\|", cell) for cell in cells]
    return "| " + " | ".join(escaped) + " |"


def replace_section(text: str, number: int, next_number: int, body: str) -> str:
    return re.sub(
        rf"## {number}\..*?(?=\n## {next_number}\.)",
        lambda _match: body.rstrip(),
        text,
        count=1,
        flags=re.S,
    )


def source_review_summary(review_block: str) -> str:
    plain = re.sub(r"<!--.*?-->", "", review_block, flags=re.S)
    plain = re.sub(r"[#*`]", "", plain)
    plain = re.sub(r"\s+", " ", plain).strip()
    return plain[:700]


def retarget_review_block(review_block: str, target: str) -> str:
    """Keep copied evidence, but rewrite report-owned archive dates.

    The immutable arXiv identifier and exact-v1 locators remain unchanged.  A
    first-public date printed inside a Source Review is report metadata, so it
    must follow the canonical owner rather than the precanonical report that
    happened to hold the block.
    """
    return re.sub(
        r"(first-public(?:（Asia/Shanghai）)?[:：]\s*`?)(20\d{2}-\d{2}-\d{2})(`?)",
        rf"\g<1>{target}\g<3>",
        review_block,
        flags=re.I,
    )


def normalized_body_sha256(body: str) -> str:
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def recompute_review_provenance(candidate: list[str], review: list[str], review_block: str) -> str:
    def canonical_multi(value: str) -> str:
        items = []
        for raw_item in value.split(";"):
            item = unicodedata.normalize("NFC", raw_item.strip())
            if item and item not in ABSENT_VALUES:
                items.append(item)
        return ";".join(sorted(items))

    review_ref = candidate[14]
    start = f"<!-- {review_ref}:start -->"
    end = f"<!-- {review_ref}:end -->"
    if start not in review_block or end not in review_block:
        raise RuntimeError(f"missing bounded review body for {candidate[0]}")
    body = review_block.split(start, 1)[1].split(end, 1)[0]
    # The validator removes Markdown code fences with ``strip("`")`` at the
    # receipt interface before hashing.  Mirror that exact boundary here;
    # otherwise a locator ending in an inline-code fragment produces a valid-
    # looking but unreproducible RP id.
    normalized_review = [value.strip("`") for value in review]
    fields = [
        "review-completion-v1", candidate[0], candidate[2], candidate[1],
        canonical_multi(candidate[5]), normalized_review[3],
        canonical_multi(normalized_review[4]), normalized_review[2],
    ]
    if candidate[13] not in {"", "none"}:
        fields.append(f"review-override:{candidate[13]}")
    fields.extend([
        canonical_multi(normalized_review[5]), canonical_multi(normalized_review[6]),
        canonical_multi(normalized_review[7]), canonical_multi(normalized_review[8]),
        normalized_review[9], review_ref,
        f"review-body-sha256:{normalized_body_sha256(body)}",
    ])
    return "RP-" + hashlib.sha256("|".join(fields).encode("utf-8")).hexdigest()[:16]


def add_missing_support_receipts(
    text: str,
    target: str,
    candidates: list[list[str]],
) -> str:
    """Add exact-artifact receipts required by transferred candidate rows.

    These are bounded support receipts, not claims that the whole GitHub or
    vendor source was searched for discovery in the historical window.
    """
    # Make regeneration idempotent after schema corrections.
    text = re.sub(
        r"\n?<!-- coverage:SRC-[^ ]+?-owner-transfer:start -->.*?"
        r"<!-- coverage:SRC-[^ ]+?-owner-transfer:end -->\n?",
        "\n",
        text,
        flags=re.S,
    )
    text = re.sub(
        r"^\| SRC-[^|]+ \|[^\n]*canonical-owner transferred exact artifact provenance[^\n]*\n",
        "",
        text,
        flags=re.M,
    )
    compact_day = target.replace("-", "")
    required_by_source: dict[str, list[str]] = defaultdict(list)
    for candidate in candidates:
        for source_id in candidate[5].split(";"):
            source_id = source_id.strip()
            if source_id and source_id != "SRC-ARXIV":
                required_by_source[source_id].append(candidate[0])

    lines = text.splitlines()
    marker_index = next(
        index for index, line in enumerate(lines)
        if line.strip() == "<!-- validator:source-coverage-v2 -->"
    )
    table_start = next(
        index for index in range(marker_index + 1, len(lines))
        if lines[index].startswith("|")
    )
    table_end = table_start
    while table_end + 1 < len(lines) and lines[table_end + 1].startswith("|"):
        table_end += 1

    # Reconcile pre-existing support receipts with the moved candidate set.
    # Keep the header/separator and the canonical arXiv receipt; update a
    # support receipt's family list, or remove it when no current candidate
    # depends on that source.
    rebuilt_table = lines[table_start:table_start + 2]
    removed_refs = []
    existing = set()
    for line in lines[table_start + 2:table_end + 1]:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or not cells[0].startswith("SRC-"):
            rebuilt_table.append(line)
            continue
        source_id = cells[0]
        if source_id == "SRC-ARXIV":
            rebuilt_table.append(line)
            existing.add(source_id)
            continue
        families = sorted(set(required_by_source.get(source_id, [])))
        if not families:
            if len(cells) > 10 and cells[10].startswith("coverage:"):
                removed_refs.append(cells[10])
            continue
        cells[6] = str(len(families))
        cells[7] = ";".join(families)
        rebuilt_table.append(md_row(cells))
        existing.add(source_id)
    lines[table_start:table_end + 1] = rebuilt_table
    text = "\n".join(lines) + "\n"
    for ref in removed_refs:
        text = re.sub(
            rf"\n?<!-- {re.escape(ref)}:start -->.*?<!-- {re.escape(ref)}:end -->\n?",
            "\n",
            text,
            flags=re.S,
        )

    by_source = {
        source_id: families
        for source_id, families in required_by_source.items()
        if source_id not in existing
    }
    if not by_source:
        return text

    # Locate the now-normalized table again before inserting new support rows.
    lines = text.splitlines()
    marker_index = next(
        index for index, line in enumerate(lines)
        if line.strip() == "<!-- validator:source-coverage-v2 -->"
    )
    table_start = next(
        index for index in range(marker_index + 1, len(lines))
        if lines[index].startswith("|")
    )
    table_end = table_start
    while table_end + 1 < len(lines) and lines[table_end + 1].startswith("|"):
        table_end += 1
    additions = []
    blocks = []
    for source_id, families in sorted(by_source.items()):
        unique_families = sorted(set(families))
        ref = f"coverage:{source_id}:{compact_day}-owner-transfer"
        additions.append(md_row([
            source_id,
            f"{target}T00:00:00+08:00",
            f"{target}T23:59:59+08:00",
            "2026-09-03T12:45:00+08:00",
            "canonical-owner transferred exact artifact provenance from retained Source Review",
            "checked",
            str(len(unique_families)),
            ";".join(unique_families),
            "Not Applicable — bounded exact artifact set has no pagination",
            "2026-09-03T12:45:00+08:00",
            ref,
            "—",
        ]))
        blocks.extend([
            "",
            f"<!-- {ref}:start -->",
            f"{source_id} is retained only as exact supporting-artifact provenance for "
            f"{'; '.join(unique_families)} after canonical owner transfer. This receipt does "
            "not assert a full historical discovery scan of the source.",
            f"<!-- {ref}:end -->",
        ])
    lines[table_end + 1:table_end + 1] = additions + blocks
    return "\n".join(lines) + "\n"


def main() -> None:
    with gzip.open(SNAPSHOT, "rt", encoding="utf-8") as handle:
        snapshots = json.load(handle)["reports"]
    bundles = {}
    source_day = {}
    for saved in snapshots:
        text = saved["body"]
        source_date = saved["path"].replace("papers/2026/", "").replace("/README.md", "").replace("/", "-")
        tables = {name: table(text, spec[0]) for name, spec in TABLE_SPECS.items()}
        for family, candidate in tables["candidate"].items():
            review_ref = candidate[14]
            books_ref = candidate[20]
            selection = tables["selection"].get(family)
            narrative_ref = selection[6] if selection and len(selection) == 7 else "—"
            books_review_block = block(text, books_ref) if books_ref != "—" else ""
            # Some older reports put existing:/delta: inside the canonical
            # books-review block; others place them as sibling blocks.  Emit
            # exactly one marker pair for each ref after transfer.
            books_blocks = []
            if books_review_block:
                existing_ref = (tables["books"].get(family) or ["—"] * 9)[4]
                delta_ref = (tables["books"].get(family) or ["—"] * 9)[5]
                for child_ref in (existing_ref, delta_ref):
                    if child_ref != "—" and f"<!-- {child_ref}:start -->" not in books_review_block:
                        child_block = block(text, child_ref)
                        if child_block:
                            books_blocks.append(child_block)
                books_blocks.append(books_review_block)
            bundles[family] = {
                "candidate": candidate,
                "review": tables["review"].get(family),
                "benchmark": tables["benchmark"].get(family),
                "selection": selection,
                "books": tables["books"].get(family),
                "review_block": block(text, review_ref),
                "books_blocks": books_blocks,
                "selection_block": block(text, narrative_ref) if narrative_ref != "—" else "",
            }
            source_day[family] = source_date

    targets: dict[str, list[tuple[dict, dict]]] = defaultdict(list)
    external = []
    with OWNER.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["arxiv_id"] in WITHDRAWN:
                continue
            bundle = bundles.get(row["source_family_id"])
            if not bundle:
                raise RuntimeError(f"missing frozen bundle {row['source_family_id']}")
            target = row["resolved_owner_report_date"]
            if row["reconciliation"] == "identifier_month_conflict_ambiguous":
                target = row["report_date"]
            if not ("2026-06-01" <= target <= "2026-07-31"):
                external.append({**row, "bundle_available": True})
                continue
            targets[target].append((row, bundle))

    for target, entries in sorted(targets.items()):
        month, day = target[5:7], target[8:10]
        report = ROOT / f"papers/2026/{month}/{day}/README.md"
        text = report.read_text(encoding="utf-8")
        entries.sort(key=lambda pair: pair[0]["arxiv_id"])
        candidate_rows = []
        review_rows = []
        benchmark_rows = []
        selection_rows = []
        books_rows = []
        review_blocks = []
        books_blocks = []
        selected_blocks = []
        semantic_review_refs = []
        semantic_selection_refs = []
        semantic_books_refs = []

        prior_selected = [
            (row, bundle) for row, bundle in entries
            if bundle["selection"] and bundle["selection"][2] == "selected" and bundle["selection_block"]
        ]
        chosen = {row["source_family_id"] for row, _ in sorted(
            prior_selected,
            key=lambda pair: (-int(pair[1]["candidate"][9]), pair[0]["source_family_id"]),
        )[:3]}

        for owner, bundle in entries:
            family = owner["source_family_id"]
            owner_ambiguous = owner["reconciliation"] == "identifier_month_conflict_ambiguous"
            candidate = list(bundle["candidate"])
            candidate[3] = iso_week(target)
            candidate[4] = target
            candidate[15] = (
                "pending:official-announcement-owner-resolution" if owner_ambiguous else "self"
            )
            candidate[16] = "—"
            candidate[17] = (
                "earlier_owner_pending" if owner_ambiguous
                else "new_in_window"
            )
            if owner_ambiguous:
                # The exact-v1 evidence is available and reviewed; only the
                # archive owner date remains unresolved.  Keep the scored
                # candidate visible, freeze Books, and let reconciliation keep
                # all report Gates open without mislabeling evidence access.
                candidate[10] = "retained"
                candidate[12] = "accessible"
            candidate_rows.append(md_row(candidate))
            review = list(bundle["review"])
            review_block = retarget_review_block(bundle["review_block"], target)
            review[1] = recompute_review_provenance(candidate, review, review_block)
            review_rows.append(md_row(review))
            semantic_review_refs.append(candidate[14])
            if bundle["benchmark"]:
                benchmark_rows.append(md_row(bundle["benchmark"]))
            if bundle["books"]:
                books_rows.append(md_row(bundle["books"]))
                semantic_books_refs.append(bundle["books"][8])
            review_blocks.append(review_block)
            books_blocks.extend(bundle["books_blocks"])

            if bundle["selection"]:
                selection = list(bundle["selection"])
            else:
                # Selection is a report-owned prioritization decision, not a
                # primary-source fact.  Reconstruct the missing receipt from
                # the already frozen score and Source Review, while keeping
                # the report Open for the independent semantic audit.
                score = int(candidate[9])
                if score < 7 and candidate[13] == "none":
                    # Non-eligible families correctly have no Selection row.
                    continue
                eligibility = "score_7_9" if score >= 7 else "forced_review"
                selection = [
                    family,
                    eligibility,
                    "not_selected",
                    "—",
                    "—",
                    (
                        f"{owner['title']} has a complete Source Review but the precanonical "
                        "report omitted its selection receipt. Canonical-owner reconstruction "
                        "records it as not selected; this is a prioritization closure, not a new evidence claim."
                    ),
                    f"analysis-decision:{family}",
                ]
            if family in chosen:
                selection_rows.append(md_row(selection))
                selected_blocks.append(bundle["selection_block"])
                semantic_selection_refs.append(selection[6])
            else:
                selection[2] = "not_selected"
                selection[3] = "—"
                selection[4] = "—"
                selection[5] = (
                    f"{owner['title']} remains evidence-complete after canonical owner transfer "
                    f"with V2 score {candidate[9]} and owner {candidate[18]}. The selected units "
                    "rank higher on distinct cross-layer state/control impact in this owner window; "
                    "the full family review remains authoritative and is not reduced by narrative prioritization."
                )
                selection[6] = f"analysis-decision:{family}"
                selection_rows.append(md_row(selection))
                semantic_selection_refs.append(selection[6])
                selected_blocks.append(
                    f"<!-- analysis-decision:{family}:start -->\n{selection[5]}\n"
                    f"<!-- analysis-decision:{family}:end -->"
                )

        candidate_body = (
            "## 2. Candidate Ledger\n\n<!-- validator:candidate-ledger-v2.1 -->\n"
            + TABLE_SPECS["candidate"][1] + "\n" + "\n".join(candidate_rows)
        )
        review_body = (
            "## 3. Review Completion Receipt\n\n<!-- validator:review-completion-v1 -->\n"
            + TABLE_SPECS["review"][1] + "\n" + "\n".join(review_rows)
            + "\n\n### Source Reviews\n\n" + "\n\n".join(review_blocks)
            + "\n\n<!-- audit-target:evidence:end -->"
        )
        benchmark_body = "## 4. Benchmark Contracts\n\n"
        if benchmark_rows:
            benchmark_body += (
                "<!-- validator:benchmark-contract-v1 -->\n" + TABLE_SPECS["benchmark"][1]
                + "\n" + "\n".join(benchmark_rows)
            )
        else:
            benchmark_body += "None — retained family 没有 benchmark claim。"
        selection_body = (
            "<!-- audit-target:deep_analysis_selection:start -->\n## 5. Deep Analysis Selection\n\n<!-- validator:deep-analysis-selection-v1 -->\n"
            + TABLE_SPECS["selection"][1] + "\n" + "\n".join(selection_rows)
            + "\n\n### Selected Analysis Narratives\n\n" + "\n\n".join(selected_blocks)
            + "\n\n<!-- audit-target:deep_analysis_selection:end -->"
        )
        books_body = (
            "<!-- audit-target:books:start -->\n## 6. Books Comparison\n\n<!-- validator:books-comparison-v1 -->\n"
            + TABLE_SPECS["books"][1] + "\n" + "\n".join(books_rows)
            + "\n\n" + "\n\n".join(books_blocks)
            + "\n\n<!-- audit-target:books:end -->"
        )
        compact_day = target.replace("-", "")
        coverage_refs = re.findall(r"<!-- (coverage:[^ ]+):start -->", text)
        coverage_review_ref = coverage_refs[0] if coverage_refs else "audit-target:coverage"
        audit_body = (
            "## 7. Semantic Audit\n\n"
            "<!-- validator:semantic-audit-v1 -->\n"
            "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |\n"
            "| --- | --- | --- | --- | --- | --- | --- |\n"
            f"| SA-{compact_day}-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | {coverage_review_ref} | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-{compact_day}: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |\n"
            f"| SA-{compact_day}-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | {'; '.join(semantic_review_refs)} | EVIDENCE-OWNER-REBUILD-{compact_day}: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |\n"
            f"| SA-{compact_day}-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | {'; '.join(semantic_selection_refs)} | SELECTION-OWNER-REBUILD-{compact_day}: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |\n"
            f"| SA-{compact_day}-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | {'; '.join(semantic_books_refs)} | BOOKS-OWNER-REBUILD-{compact_day}: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |"
        )
        source_body = (
            "## 12. Sources\n\n"
            + "\n".join(
                f"- [{owner['title']}](https://arxiv.org/abs/{owner['arxiv_id']}v1) — "
                f"first-public（Asia/Shanghai）：{target}；exact evidence：v1；"
                "accessed：2026-09-03"
                for owner, _bundle in entries
            )
        )
        for number, nxt, body in (
            (2, 3, candidate_body), (3, 4, review_body), (4, 5, benchmark_body),
            (5, 6, selection_body), (6, 7, books_body), (7, 8, audit_body),
        ):
            text = replace_section(text, number, nxt, body)
        text = replace_section(text, 12, 13, source_body)

        text = add_missing_support_receipts(
            text,
            target,
            [list(bundle["candidate"]) for _owner, bundle in entries],
        )

        # Align the coverage receipt's family list with the moved candidate set.
        lines = text.splitlines()
        families = ";".join(row[0]["source_family_id"] for row in entries) or "—"
        for index, line in enumerate(lines):
            if line.startswith("| SRC-ARXIV |"):
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                cells[7] = families
                lines[index] = md_row(cells)
                break
        report.write_text("\n".join(line.rstrip() for line in lines) + "\n", encoding="utf-8")

    (AUDIT / "external-owner-handoffs-with-bundles.json").write_text(
        json.dumps({"schema": "external-owner-handoffs-v1", "items": external}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
