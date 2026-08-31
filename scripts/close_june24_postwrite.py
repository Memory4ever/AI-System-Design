#!/usr/bin/env python3
"""Fresh-context post-write audit and Gate closure for 2026-06-24."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import re
from pathlib import Path

from canonicalize_june_daily_presentation import canonicalize_report
from test_june24_canonical_presentation import main as validate_canonical_presentation

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260624"
REPORT = ROOT / "papers/2026/06/24/README.md"
PRESENTATION_AUDIT = PACKET / "PRESENTATION_FRESH_AUDIT_V1.md"
SHA_MANIFEST = PACKET / "SHA256SUMS"

spec = importlib.util.spec_from_file_location("j24", ROOT / "scripts/finalize_june24_v21.py")
j24 = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(j24)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_sha_manifest() -> None:
    paths = sorted(path for path in PACKET.rglob("*") if path.is_file() and path != SHA_MANIFEST)
    paths.extend([
        REPORT,
        ROOT / "scripts/finalize_june24_v21.py",
        Path(__file__).resolve(),
        ROOT / "scripts/canonicalize_june_daily_presentation.py",
        ROOT / "scripts/test_june24_canonical_presentation.py",
    ])
    SHA_MANIFEST.write_text(
        "".join(f"{sha(path)}  {path.relative_to(ROOT).as_posix()}\n" for path in paths),
        encoding="utf-8",
    )


def main() -> None:
    reviews = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text())["items"]
    ready = (PACKET / "READY_TO_INSERT_BOOKS_V1.md").read_text()
    book_files = sorted((ROOT / "books").rglob("*.md"))
    texts = {str(p.relative_to(ROOT)): p.read_text() for p in book_files}
    rows = []
    for review in reviews:
        family = review["source_family_id"]
        target = j24.PATHS[review["stable_node_id"]]
        body = next((line for line in ready.splitlines() if line.startswith(f"- **{family}**：")), "")
        note = next((line for line in ready.splitlines() if line.startswith(f"- {family}:")), "")
        global_hits = sum(text.count(family) for text in texts.values())
        owner_hits = texts[target].count(family)
        body_hits = texts[target].count(body) if body else 0
        note_hits = texts[target].count(note) if note else 0
        other_hits = global_hits - owner_hits
        # Fallback/coexistence is source-specific: some families explicitly
        # return to a baseline, others refuse publication/write/commit, retain
        # the old path, or hand the unresolved decision to a human owner.
        mechanism = body_hits == 1 and len(body) >= 80
        exact_note = note_hits == 1 and f"arXiv:{review['primary_identifier'].split(':')[-1]}" in note and "Method=" in note and "Evaluation=" in note and "Non-proof=" in note
        ok = global_hits == 2 and owner_hits == 2 and other_hits == 0 and body_hits == 1 and note_hits == 1 and mechanism and exact_note
        rows.append({
            "source_family_id": family,
            "stable_node_id": review["stable_node_id"],
            "target": target,
            "global_hits": global_hits,
            "owner_hits": owner_hits,
            "other_hits": other_hits,
            "body_exact": body_hits,
            "review_note_exact": note_hits,
            "mechanism_control_tradeoff_fallback_boundary": "passed" if mechanism else "open",
            "exact_v1_review_note": "passed" if exact_note else "open",
            "owner_adjacent_handoff": "passed" if other_hits == 0 else "open",
            "finding": "—" if ok else "expected one exact owner body and one exact source-specific Review note, with zero adjacent/other-owner marker",
            "status": "passed" if ok else "open",
        })
    unresolved = [r for r in rows if r["status"] != "passed"]
    with (PACKET / "post-write-fresh-audit-v1.tsv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader(); w.writerows(rows)
    (PACKET / "POST_WRITE_FRESH_AUDIT_V1.md").write_text(
        "# 2026-06-24 Post-Write Fresh Audit V1\n\n"
        "- Scope: 43/43 frozen Integrate families across 19 unique owner files.\n"
        "- Checks per family: unique owner; exact mechanism/state/control/trade-off/fallback/non-proof body; exact-v1 Method/Evaluation/Non-proof Review note; zero adjacent-owner duplication.\n"
        f"- Result: {'Passed; zero unresolved findings.' if not unresolved else 'Open; ' + str(len(unresolved)) + ' unresolved finding(s).'}\n"
        "- Receipt: `post-write-fresh-audit-v1.tsv`.\n"
    )
    if unresolved:
        raise SystemExit(json.dumps(unresolved, ensure_ascii=False, indent=2))

    text = REPORT.read_text()
    text = text.replace("Coverage, exact-v1 Evidence and full-frontier Selection passed; Books Gate remains Open pending root writeback and 43/43 post-write fresh audit.", "Coverage, exact-v1 Evidence, full-frontier Selection and the 43/43 post-write Books audit passed with zero unresolved findings.")
    text = text.replace("| Completion Status | In Progress |", "| Completion Status | Complete |")
    text = text.replace("| Books Gate | Open |", "| Books Gate | Passed |")
    old = re.search(r"\| SA-20260624-BOOKS-PREWRITE-V1 \|.*?\| open \|", text)
    assert old
    replacement = "| SA-20260624-BOOKS-POSTWRITE-V1 | fresh-context:jun24-postwrite-v1 | books | " + "; ".join("books-review:" + r["source_family_id"] for r in reviews) + " | — | 43/43 passed: each family has one exact mechanism/control/trade-off/fallback/boundary body and one exact-v1 Review note in its unique owner; zero adjacent duplication; receipt `post-write-fresh-audit-v1.tsv` | passed |"
    text = text[:old.start()] + replacement + text[old.end():]
    text = text.replace("- Proposed Books disposition: 43 Integrate across 19 unique owner files; Books Gate Open until root writeback and 100% post-write audit.", "- Final Books disposition: 43 Integrate across 19 unique owner files; Books Gate Passed after the 43/43 post-write fresh audit.")
    text = text.replace("- This lane writes only the 2026-06-24 Daily, its source packet, and its date-specific finalizer; shared Books and `docs/LEARNING_STATE.md` remain unchanged.", "- This lane wrote 43 source-family deltas into 19 shared Books owners under the granted lock, updated the 2026-06-24 Daily/source packet, and left `docs/LEARNING_STATE.md` unchanged.")
    text = text.replace("- Root must serialize `READY_TO_INSERT_BOOKS_V1.md`; then this lane must independently verify every body marker, source-specific Review note, unique owner, handoff and exact-v1 boundary before Completion can become Complete.", "- None. All 43 writebacks and their owner/adjacent handoffs passed the fresh post-write audit.")
    REPORT.write_text(text)

    readme = (PACKET / "README.md").read_text()
    readme = readme.replace("- Books Gate: Open", "- Books Gate: Passed")
    readme = readme.replace("- Completion: In Progress", "- Post-write fresh audit: Passed (43/43; zero unresolved findings)\n- Completion: Complete")
    (PACKET / "README.md").write_text(readme)
    queue = (PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md").read_text()
    queue = queue.replace("Root must serialize 43 source families into 19 unique owner files; shared Books remain untouched by this lane.", "Resolved: 43 source families were serialized into 19 unique owner files and passed the 43/43 post-write fresh audit.")
    (PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md").write_text(queue)
    assert canonicalize_report(REPORT, "2026-06-24")
    validate_canonical_presentation()
    PRESENTATION_AUDIT.write_text("""# 2026-06-24 canonical presentation fresh audit v1

## Scope

This presentation-only audit compares the canonical report with the frozen date-local receipts after the post-write Books audit. It does not reopen the Candidate Denominator, Source Reviews, Books Decisions or shared Books writeback.

## Results

- Canonical top fields: `5/5` present and exact.
- Canonical H2 order: `14/14` exact (`Executive Summary` plus numbered sections `1`–`13`).
- Candidate / Review / Benchmark / Selection / Books rows: `43 / 43 / 43 / 43 / 43`.
- Selection: `3 selected / 40 not selected`; Books: `43 Integrate / 0 No Change`.
- Frozen Source Review bodies: `43/43` unchanged; aggregate SHA-256 `018b822f125ea6618200f9cff9187818a8a35adf4c398f3fd31b89139e3f6b0f`.
- Review Provenance IDs: `43/43` unchanged; aggregate SHA-256 `0d5b3c5ade7d4357c10f5d061747aa04f6a7f2c32653188b769cbf88fcaa3451`.
- Sources: `43/43` exact-v1 arXiv identities plus the source registry.
- Existing semantics remain `541 raw = 43 retained + 498 closures`, with `Coverage=Closed / Evidence=Passed / Books=Passed / Completion=Complete`.
- Shared Books, `docs/LEARNING_STATE.md` and the monthly index remain outside this renderer's write set.
- Unresolved presentation findings: `0`.

## Boundary

This receipt proves that the presentation migration preserved frozen evidence identity after the independent 43/43 post-write audit. It does not replace the report's Coverage, Evidence, Selection or Books semantic audits; machine validation does not establish the underlying research claims.
""", encoding="utf-8")
    write_sha_manifest()
    print(json.dumps({"postwrite":"43/43 passed","owners":19,"unresolved":0,"books_gate":"Passed","completion":"Complete"},ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
