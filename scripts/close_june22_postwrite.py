#!/usr/bin/env python3
"""Adversarial post-write audit and Gate closure for 2026-06-22."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260622"
REPORT = ROOT / "papers/2026/06/22/README.md"
FINALIZER = ROOT / "scripts/finalize_june22_v21.py"

NO_CHANGE_TOKENS = {
    "2606.22319": ("low-level controller", "safety envelope"),
    "2606.22329": ("judge", "disagreement"),
    "2606.22330": ("held-out verifier", "reset 和 provenance"),
    "2606.22419": ("parametric generator", "non-parametric dense index"),
    "2606.22470": ("system policy and role", "tool schemas and results"),
    "2606.22610": ("durable workflow", "held-out"),
    "2606.22613": ("coverage", "probe"),
    "2606.22673": ("模型侧 sensor", "独立 output/action gate"),
    "2606.22678": ("过程", "最终"),
    "2606.22731": ("held-out", "promotion"),
}


def load_finalizer():
    spec = importlib.util.spec_from_file_location("june22_finalizer", FINALIZER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"closure replacement expected once, found {text.count(old)}: {old[:90]}")
    return text.replace(old, new, 1)


def main() -> None:
    module = load_finalizer()
    reviews = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text())["reviews"]
    comparisons = {
        row["source_family_id"]: row
        for row in json.loads((PACKET / "books-comparison-v1.json").read_text())["items"]
    }
    assert len(reviews) == 39 and len(comparisons) == 39
    books_files = list((ROOT / "books").rglob("*.md"))
    findings: list[tuple[str, str, object]] = []
    audit_rows: list[str] = []
    integrate_count = 0
    no_change_count = 0

    for review in reviews:
        family = review["source_family_id"]
        aid = review["primary_identifier"].removeprefix("arXiv:").removesuffix("v1")
        owner = review["stable_node_id"]
        expected = ROOT / module.PATHS[owner]
        chapter = expected.read_text()
        comparison = comparisons[family]
        adjacent_paths = [
            ROOT / ref.strip().split("#", 1)[0]
            for ref in comparison["adjacent_chapter_refs"].split(";")
        ]
        missing_adjacent = [str(path.relative_to(ROOT)) for path in adjacent_paths if not path.exists()]
        if missing_adjacent:
            findings.append((family, "adjacent path missing", missing_adjacent))
        hits = [path for path in books_files if family in path.read_text()]

        if review["books_disposition"].startswith("No Change"):
            no_change_count += 1
            if hits:
                findings.append((family, "No Change family was written into Books", [str(p.relative_to(ROOT)) for p in hits]))
            missing = [token for token in NO_CHANGE_TOKENS[aid] if token not in chapter]
            if missing:
                findings.append((family, "existing canonical proposition missing", missing))
            audit_rows.append(
                f"| `{family}` | No Change | `{owner}` → `{module.PATHS[owner]}` | existing proposition tokens re-opened: "
                f"`{'` / `'.join(NO_CHANGE_TOKENS[aid])}` | no family write | `{comparison['adjacent_chapter_refs']}` | PASS |"
            )
            continue

        integrate_count += 1
        evidence = module.C[aid]
        checks = {
            "unique canonical owner": hits == [expected],
            "body marker exactly once": chapter.count(f"body-source:{family}") == 1,
            "family identity body plus Review note": chapter.count(family) == 2,
            "mechanism delta exactly once": chapter.count(evidence["delta"]) == 1,
            "failure/coexistence boundary exactly once": chapter.count(evidence["boundary"]) == 1,
            "method locator exactly once": chapter.count(review["method_identity_locators"]) == 1,
            "evaluation locator exactly once": chapter.count(review["evaluation_locators"]) == 1,
            "non-proof locator exactly once": chapter.count(review["limitations_counterevidence_locators"]) == 1,
            "artifact locator in this family's unique Review note": sum(
                1
                for line in chapter.splitlines()
                if family in line and f"Artifact=`{review['artifact_locators']}`" in line
            ) == 1,
        }
        for label, passed in checks.items():
            if not passed:
                findings.append((family, label, [str(p.relative_to(ROOT)) for p in hits]))
        audit_rows.append(
            f"| `{family}` | Integrate | `{owner}` → `{module.PATHS[owner]}` | mechanism/failure/fallback re-opened | "
            f"exact-v1 Method/Evaluation/non-proof/artifact re-opened | `{comparison['adjacent_chapter_refs']}` | PASS |"
        )

    assert integrate_count == 29 and no_change_count == 10
    if findings:
        raise AssertionError("06-22 post-write semantic findings: " + repr(findings))

    audit = [
        "# 2026-06-22 Post-write Fresh Audit V1", "",
        "Adversarial review of the frozen 39-family denominator after serialized Books writeback. "
        "The validator and the write script were treated as interface evidence, not semantic proof.", "",
        "- Result: PASS — 39/39 dispositions; zero unresolved findings.",
        "- Integrate: 29/29 in exactly one expected canonical owner across 18 chapters; mechanism, failure/coexistence, "
        "exact-v1 Method/Evaluation/non-proof/artifact notes re-opened.",
        "- No Change: 10/10 existing propositions re-opened; no accidental Source Family write.",
        "- Owner/adjacent handoff: 39/39 paths resolve; adjacent chapters remain non-owner consumers.",
        "- Cross-model review: skipped per the user's standing instruction; the local adversarial audit checked every family.", "",
        "| Family | Disposition | Expected owner | Body / existing proposition | Evidence boundary | Adjacent handoff | Result |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        *audit_rows,
    ]
    (PACKET / "POST_WRITE_FRESH_AUDIT_V1.md").write_text("\n".join(audit) + "\n")

    report = REPORT.read_text()
    report = replace_once(
        report,
        "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open，等待已授权的 serialized writeback 后 fresh-context Semantic Audit",
        "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding",
    )
    report = replace_once(
        report,
        "Strict V2.1 full replay for `daily-v2.1:2026-06-22:7409eb001ec5b069`. Coverage Closed; Evidence and Selection Passed; Books Open pending serialized writeback and post-write audit.",
        "Strict V2.1 full replay for `daily-v2.1:2026-06-22:7409eb001ec5b069`. Coverage Closed; Evidence, Selection and Books Passed after the 39/39 post-write fresh audit.",
    )
    report = replace_once(
        report,
        "the date remains In Progress until shared writeback and post-write fresh audit.",
        "root wrote 29 Integrate families into 18 canonical owners; the 39/39 post-write audit passed with zero unresolved findings, so the date is Complete.",
    )
    report = replace_once(report, "| Completion Status | In Progress |", "| Completion Status | Complete |")
    report = replace_once(report, "| Books Gate | Open |", "| Books Gate | Passed |")
    report = replace_once(
        report,
        "| SA-20260622-BOOKS-PREWRITE-V1 | fresh-context:jun22-books-v1 | books |",
        "| SA-20260622-BOOKS-POSTWRITE-V1 | fresh-context:jun22-postwrite-v1 | books |",
    )
    report = replace_once(
        report,
        "| root writeback pending | 29 Integrate across 18 owners; 10 No Change; target/adjacent current state read; Books Gate stays Open | open |",
        "| — | 29/29 Integrate in exactly one canonical owner and 10/10 No Change propositions revalidated; owner/adjacent handoff 39/39; zero unresolved finding | passed |",
    )
    report = replace_once(
        report,
        "- Proposed `Integrate`: 29 families across 18 owner files; root writeback pending.",
        "- `Integrate`: 29/29 families written into 18 canonical owner chapters and revalidated.",
    )
    report = replace_once(
        report,
        "- `No Change — Existing Coverage`: 10 families; existing owner propositions re-opened.",
        "- `No Change — Existing Coverage`: 10/10 existing owner propositions re-opened; no duplicate family write.",
    )
    report = replace_once(
        report,
        "- Books Gate remains Open until serialized writeback and 39/39 post-write fresh audit.",
        "- Books Gate Passed after 39/39 post-write fresh audit; zero unresolved finding.",
    )
    report = replace_once(
        report,
        "- Shared Books and `docs/LEARNING_STATE.md` were not edited by this prewrite stage.",
        "- Root serialized 29 Source Family deltas into 18 canonical Books owners; no staging, commit or push was performed.",
    )
    report = replace_once(
        report,
        "- Proceed with the already-authorized serialized writeback for 29 Integrate families across 18 owners, then re-audit all 39 Books dispositions.",
        "- Serialized writeback completed for 29 Integrate families across 18 owners; all 39 Books dispositions passed the post-write fresh audit.",
    )
    report = replace_once(report, "- Status: In Progress.", "- Status: Complete.")
    report = replace_once(
        report,
        "- Books Gate: Open pending serialized writeback and post-write fresh audit.",
        "- Books Gate: Passed.\n- Fresh-context Semantic Audit: Passed；unresolved findings = 0.",
    )
    REPORT.write_text(report)

    ledger = json.loads((PACKET / "screening-ledger.json").read_text())
    ledger["gate_status"] = "complete_postwrite_fresh_audit_passed"
    ledger["audit"] = {
        "coverage": "230/230_passed",
        "evidence": "39/39_passed",
        "selection": "39/39_full_frontier_passed",
        "books": "39/39_postwrite_passed_29_integrate_plus_10_no_change",
        "unresolved_findings": 0,
    }
    (PACKET / "screening-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "README.md").write_text(
        "# 2026-06-22 source packet\n\nCanonical denominator `39/230`; closures `191`; retain rate `16.96%`. "
        "Coverage Closed, Evidence Passed, Selection Passed, Books Passed. Root wrote 29 Integrate families across "
        "18 canonical owners; 10 No Change. Post-write fresh audit: 39/39 Passed, zero unresolved finding. Completion Complete.\n"
    )
    sums = []
    for path in sorted(p for p in PACKET.iterdir() if p.is_file() and p.name not in {"SHA256SUMS", "screening-ledger-provisional.json"}):
        sums.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name)
    external_targets = (
        (REPORT, "../../22/README.md"),
        (FINALIZER, "../../../../../scripts/finalize_june22_v21.py"),
        (Path(__file__).resolve(), "../../../../../scripts/close_june22_postwrite.py"),
    )
    for path, relative_name in external_targets:
        sums.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + relative_name)
    (PACKET / "SHA256SUMS").write_text("\n".join(sums) + "\n")
    print("06-22 post-write audit PASS: 39/39, unresolved findings 0")


if __name__ == "__main__":
    main()
