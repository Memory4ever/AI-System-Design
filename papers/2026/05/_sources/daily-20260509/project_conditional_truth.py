#!/usr/bin/env python3
"""Project the independently reconciled 2026-05-09 Conditional truth.

The root writer already completed the three accessible Books deltas. This
script updates only the date-local Report and evidence packets; it never edits
shared Books.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
REPORT = ROOT.parents[1] / "09" / "README.md"
LEDGER_PATH = ROOT / "screening-ledger-independent-final.json"
LEDGER = json.loads(LEDGER_PATH.read_text())
PREWRITE = json.loads((ROOT / "books-prewrite-challenge.json").read_text())

spec = importlib.util.spec_from_file_location("research_validator", REPO / "scripts/validate_research.py")
validator = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(validator)


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def table(text: str, marker: str) -> tuple[list[str], list[list[str]], int, int]:
    start = text.index(marker)
    lines = text[start:].splitlines(keepends=True)
    header = split_row(lines[1])
    rows: list[list[str]] = []
    consumed = len(lines[0]) + len(lines[1]) + len(lines[2])
    for line in lines[3:]:
        if not line.startswith("|"):
            break
        rows.append(split_row(line))
        consumed += len(line)
    return header, rows, start, start + consumed


def render(marker: str, header: list[str], rows: list[list[str]]) -> str:
    # The validator treats every literal pipe as a column boundary.  A few
    # inherited locator/comment cells contain a pipe, so normalize it to a
    # full-width separator before rendering the canonical table.
    rows = [[str(cell).replace("|", "／") for cell in row] for row in rows]
    return (
        marker
        + "\n| "
        + " | ".join(header)
        + " |\n| "
        + " | ".join("---" for _ in header)
        + " |\n"
        + "\n".join("| " + " | ".join(row) + " |" for row in rows)
        + "\n"
    )


def replace_table(text: str, marker: str, rows: list[list[str]]) -> str:
    header, _, start, end = table(text, marker)
    return text[:start] + render(marker, header, rows) + text[end:]


def bounded_body(text: str, ref: str) -> str:
    m = re.search(
        rf"<!-- {re.escape(ref)}:start -->(.*?)<!-- {re.escape(ref)}:end -->",
        text,
        flags=re.S,
    )
    assert m, ref
    return m.group(1)


def write_json(path: Path, payload: object) -> None:
    encoded = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode()
    path.write_bytes(encoded)
    path.with_suffix(path.suffix + ".sha256").write_text(hashlib.sha256(encoded).hexdigest() + "\n")


retained = [row for row in LEDGER["identities"] if row["screening_status"] == "retained"]
blocked = [row for row in retained if row["review_status"] == "blocked"]
accessible = [row for row in retained if row["review_status"] != "blocked"]
assert (len(retained), len(accessible), len(blocked)) == (83, 66, 17)

missing_scope = {
    "2605.07111": "MoLF optimizer routing、实验/ablation、limitations 与 artifact",
    "2605.07134": "Region4Web/PageDigest method、WebArena contract 与 limitations",
    "2605.07180": "BoundaryRouter memory/routing、RouteBench、cold-start limitations",
    "2605.07514": "dynamic-consistency definition、counterfactual evaluation 与 limitations",
    "2605.07547": "deadline hierarchy、resource-sharing controller、AI-RAN contract 与 limitations",
    "2605.08267": "Execution Envelope schema、admission/commit semantics、evaluation 与 limitations",
    "2605.08268": "insider threat model、consensus propagation、evaluation 与 limitations",
    "2605.08271": "structured ultra-long-video memory、temporal identity、evaluation 与 limitations",
    "2605.08314": "FlashSVD execution path、low-rank kernel/runtime evaluation 与 limitations",
    "2605.08368": "free-energy capability elicitation/creation formalism、evidence 与 limitations",
    "2605.08399": "compositional DAG evolution、tool-state/credit flow、evaluation 与 limitations",
    "2605.08432": "semantic-sampling calibration estimator、open-ended QA protocol 与 limitations",
    "2605.08504": "massive-activation layer mechanism、intervention evidence 与 limitations",
    "2605.08505": "long-context scaling derivation、model/workload assumptions 与 limitations",
    "2605.08363": "Kettle build protocol、TEE measurement/attestation chain、verification、threat model 与 limitations",
    "2605.08565": "scale underflow、4-over-6、brute-force baseline、format/hardware scope 与 limitations",
    "2606.27379": "unlearning guarantee、reference retraining/equivalence、counterexamples 与 limitations",
}

text = REPORT.read_text()

# A prior renderer omitted the newline after the final table row, so the next
# heading or bounded Books block could be glued to that row.  Repair only these
# structural boundaries before parsing the inherited tables; no evidence text
# is discarded.
text = re.sub(
    r"(?m)^(\| (?:SF-|SA-).*?\|)\s*(?=(?:## |### |<!-- books-review:))",
    r"\1\n\n",
    text,
)

# Add bounded Review/Claim bodies for the three independent false negatives.
for row in blocked:
    sf = row["source_family_id"]
    aid = row["arxiv_id"]
    ref = f"review:{sf}"
    blocked_body = (
        f"\n### {row['title']}\n\n"
        f"Status: `Blocked / Unverified`。identity、first-public 与 abstract 已核验，但 official exact-v1 full text 未取得。\n\n"
        f"缺少材料：{missing_scope[aid]}。abstract 只能建立候选身份，不能证明 Method、evaluation、limitations 或 Books eligibility。\n\n"
        f"<!-- claim:{sf}:start -->在 exact-v1 恢复前不接受论文机制、实验或一般性结论；该 family 不进入 Books。<!-- claim:{sf}:end -->\n"
    )
    full = f"<!-- {ref}:start -->{blocked_body}<!-- {ref}:end -->"
    if f"<!-- {ref}:start -->" in text:
        text = re.sub(
            rf"<!-- {re.escape(ref)}:start -->.*?<!-- {re.escape(ref)}:end -->",
            full,
            text,
            count=1,
            flags=re.S,
        )
    else:
        text = text.replace("\n## 4. Benchmark Contracts", "\n" + full + "\n\n## 4. Benchmark Contracts", 1)

# Candidate Ledger canonicalizes the 83-family independent reconciliation.
candidate_header, author_candidates, _, _ = table(text, "<!-- validator:candidate-ledger-v2.1 -->")
candidate_rows: list[list[str]] = []
candidate_dict: dict[str, dict[str, str]] = {}
for row in retained:
    aid = row["arxiv_id"]
    sf = row["source_family_id"]
    score = row["score_v2"]
    is_blocked = row["review_status"] == "blocked"
    review_status = "blocked" if is_blocked else ("deep_complete" if score["total"] >= 7 else "standard_complete")
    disposition = "Blocked / Unverified" if is_blocked else row["integration_disposition"]
    cells = [
        sf,
        f"arXiv:{aid}v1",
        f"paper-v1:{aid}",
        "2026-W19",
        "2026-05-09",
        "SRC-ARXIV",
        str(score["design_delta"]),
        str(score["system_reach"]),
        str(score["durability"]),
        str(score["total"]),
        "retained",
        review_status,
        "blocked" if is_blocked else "accessible",
        "none",
        f"review:{sf}",
        "self",
        "—",
        "new_in_window",
        row["owner_node"],
        disposition,
        "—" if is_blocked else f"books-review:{sf}",
        "no",
    ]
    candidate_rows.append(cells)
    candidate_dict[sf] = dict(zip(candidate_header, cells))
text = replace_table(text, "<!-- validator:candidate-ledger-v2.1 -->", candidate_rows)

# Receipt rows keep actual author locators for accessible families. Blocked
# receipts state the exact missing scope and have a fresh provenance digest.
receipt_header, author_receipts, _, _ = table(text, "<!-- validator:review-completion-v1 -->")
receipt_by_sf = {row[0]: row for row in author_receipts}
receipt_rows: list[list[str]] = []
for row in retained:
    aid = row["arxiv_id"]
    sf = row["source_family_id"]
    candidate = candidate_dict[sf]
    total = row["score_v2"]["total"]
    route = "deep" if total >= 7 else "standard"
    is_blocked = row["review_status"] == "blocked"
    if is_blocked:
        method = f"Pending — exact-v1 Method required for {missing_scope[aid]}"
        evaluation = f"Pending — exact-v1 evaluation and ablations required for {missing_scope[aid]}"
        limitations = f"Pending — exact-v1 limitations and counterevidence required for {missing_scope[aid]}"
        artifact = "Pending — event-time artifact/revision and implementation scope not independently verified"
        result = "blocked"
    else:
        old = receipt_by_sf[sf]
        method, evaluation, limitations, artifact = old[5], old[6], old[7], old[8]
        result = "complete"
    primary = f"arXiv:{aid}v1"
    versions = f"SRC-ARXIV@arXiv:{aid}v1"
    claim_ref = f"claim:{sf}"
    review_ref = f"review:{sf}"
    body_hash = validator._normalized_body_sha256(bounded_body(text, review_ref))
    provenance = validator._expected_review_provenance(
        sf,
        candidate,
        route,
        primary,
        versions,
        method,
        evaluation,
        limitations,
        artifact,
        claim_ref,
        review_ref,
        body_hash,
    )
    receipt_rows.append([
        sf, provenance, route, primary, versions, method, evaluation, limitations, artifact, claim_ref, result
    ])
text = replace_table(text, "<!-- validator:review-completion-v1 -->", receipt_rows)

# Deep selection retains the three author narratives, removes false positives,
# and explicitly records blocked families as not selected.
selection_header, author_selection, _, _ = table(text, "<!-- validator:deep-analysis-selection-v1 -->")
selection_by_sf = {row[0]: row for row in author_selection}
selection_rows: list[list[str]] = []
for row in retained:
    sf = row["source_family_id"]
    total = row["score_v2"]["total"]
    # Selection Receipt is an eligibility ledger, not a second copy of the
    # Candidate Ledger.  Score < 7 without an override is not pre-Books
    # eligible and therefore must not appear here.
    if total < 7:
        continue
    if sf in selection_by_sf and row["review_status"] != "blocked":
        cells = selection_by_sf[sf]
        cells[1] = "score_7_9"
        if row["integration_disposition"] == "Integrate":
            cells[1] += ";potential_books_delta"
    else:
        cells = [
            sf,
            "score_7_9",
            "not_selected",
            "—",
            "—",
            "exact-v1 blocked；只保留候选身份与 Materials Request，不进入叙事或 Books",
            f"analysis-decision:{sf}",
        ]
        marker = f"analysis-decision:{sf}"
        if f"<!-- {marker}:start -->" not in text:
            block = f"<!-- {marker}:start -->exact-v1 blocked；不得由 abstract 推断机制、实验或 Books 结论。<!-- {marker}:end -->"
            text = text.replace("\n## 6. Books Comparison", "\n" + block + "\n\n## 6. Books Comparison", 1)
    selection_rows.append(cells)
text = replace_table(text, "<!-- validator:deep-analysis-selection-v1 -->", selection_rows)

# Books Comparison has exactly the 66 accessible final decisions. Existing
# bounded Books Reviews remain evidence; blocked families are excluded.
books_header, author_books, _, _ = table(text, "<!-- validator:books-comparison-v1 -->")
books_by_sf = {row[0]: row for row in author_books}
books_rows: list[list[str]] = []
for row in accessible:
    sf = row["source_family_id"]
    cells = books_by_sf[sf]
    cells[1] = row["owner_node"]
    cells[7] = row["integration_disposition"]
    books_rows.append(cells)
    start, end = f"<!-- books-review:{sf}:start -->", f"<!-- books-review:{sf}:end -->"
    a, b = text.find(start), text.find(end)
    assert a >= 0 and b >= 0
    block = text[a:b]
    block = re.sub(r"Decision: `[^`]+`", f"Decision: `{row['integration_disposition']}`", block)
    text = text[:a] + block + text[b:]
text = replace_table(text, "<!-- validator:books-comparison-v1 -->", books_rows)

# Materials Requests are report-visible and one-to-one with all blockers.
mr_header = [
    "Request ID", "Priority", "Source Family ID", "Source ID", "Gap / Limitation ID", "Owner Week",
    "Known Identifiers / URLs", "Missing Material", "Why Existing Evidence Is Insufficient",
    "Acceptable Substitute", "Suggested File Name", "Required Review Scope",
]
mr_rows = []
for row in blocked:
    aid, sf = row["arxiv_id"], row["source_family_id"]
    needs_books = aid in {"2605.08363", "2605.08565", "2606.27379"}
    mr_rows.append([
        f"MR-20260509-{aid}", "P1 Full Text", sf, "—", "—", "2026-W19",
        f"arXiv:{aid}v1; https://arxiv.org/html/{aid}v1; https://arxiv.org/pdf/{aid}v1",
        missing_scope[aid],
        "metadata/abstract 不能建立 exact-v1 Method、evaluation、limitations 或 artifact contract",
        "official exact-v1 HTML/PDF/LaTeX source，或带明确 v1 identity 的作者镜像",
        f"arxiv-{aid}v1.pdf",
        missing_scope[aid] + ("；完成 Score、Deep Review 与 current Books Decision" if needs_books else "；复核 owner、Score 与 No Change 结论"),
    ])
mr_table = render("<!-- validator:materials-request-v1 -->", mr_header, mr_rows)
if "<!-- validator:materials-request-v1 -->" in text:
    text = replace_table(text, "<!-- validator:materials-request-v1 -->", mr_rows)
else:
    text = text.replace("\n## 12. Sources", "\n### Materials Request\n\n" + mr_table + "\n\n## 12. Sources", 1)

# Coverage receipt, metadata and human-readable status share one truth.
families = ";".join(row["source_family_id"] for row in retained)
ledger_sha = hashlib.sha256(LEDGER_PATH.read_bytes()).hexdigest()
receipt = (
    "| SRC-ARXIV | 2026-05-08T09:00:00+08:00 | 2026-05-09T09:00:00+08:00 | 2026-09-01T17:20:00+08:00 | "
    "DataCite v2 prefixes 00..99 + independent 834/834 semantic replay + exact-v1 | checked | 834 | "
    f"{families} | pages=100; final_cursor=end; raw=91841; registered=834; screened=834; retained=83; closure=751 | "
    f"2026-05-09T00:59:59Z | screening-ledger-independent-final.json#sha256={ledger_sha} | — |"
)
text = re.sub(r"\| SRC-ARXIV \| 2026-05-08T09:00:00\+08:00 .*?\n", receipt + "\n", text, count=1)
text = re.sub(
    r"<!-- coverage:SRC-ARXIV:20260509:start -->.*?<!-- coverage:SRC-ARXIV:20260509:end -->",
    "<!-- coverage:SRC-ARXIV:20260509:start -->独立 reviewer 重放 834/834 screening：4 个 false positive 降回分母前 closure，3 个 false negative 提升进入 denominator，最终 83 retained / 751 closures。17 项 exact-v1 blocker 已逐项形成 Materials Request；ordinary coverage work 为零。<!-- coverage:SRC-ARXIV:20260509:end -->",
    text,
    count=1,
    flags=re.S,
)
for old, new in {
    "| Denominator ID | DEN-20260509-V2-FRESH-AUDIT |": "| Denominator ID | DEN-20260509-INDEPENDENT-83 |",
    "| Denominator Frozen At | 2026-09-01T03:20:00+08:00 |": "| Denominator Frozen At | 2026-09-01T17:20:00+08:00 |",
    "| Completion Status | In Progress |": "| Completion Status | Conditional |",
    "| Evidence Gate | Open |": "| Evidence Gate | Conditional Pass |",
    "| Books Gate | Open |": "| Books Gate | Conditional Pass |",
}.items():
    text = text.replace(old, new, 1)
text = re.sub(
    r"\*\*Status:\*\*.*",
    "**Status:** Conditional；Coverage=Closed、Evidence=Conditional Pass、Books=Conditional Pass。ordinary work、3 项 accessible Books 写回与 post-write audit 已闭合；只剩 17 项精确 external exact-v1 blocker。",
    text,
    count=1,
)
text = re.sub(
    r"## Executive Summary\n\n.*?\n\n## 1\. Coverage",
    "## Executive Summary\n\n相邻月份 v2 snapshot 含 91,841 条 raw records；严格窗口注册 834 条 identity 并完成 834/834 独立语义复核。最终 denominator 为 83 项，751 项 family-specific closure；66 项 exact-v1 Review 完成，17 项精确标记 `Blocked / Unverified` 并保存 Materials Request。current-content challenge 将 21 项 evidence-complete provisional Integrate 收紧为 3 项；root 已合并写入 `TRAIN-DISTRIBUTED-TRAINING`，post-write reviewer 确认 3/3 trace、owner、正文演进、trade-off/failure/fallback 与相邻章去重。\n\n## 1. Coverage",
    text,
    count=1,
    flags=re.S,
)

semantic_rows = [
    ["SA-20260509-INDEPENDENT-COVERAGE", "fresh-context:may2026-day02", "coverage", "coverage:SRC-ARXIV:20260509", "—", "834/834 replay；83 retained / 751 closures", "passed"],
    ["SA-20260509-INDEPENDENT-EVIDENCE", "fresh-context:may2026-day02", "evidence", f"review:{accessible[0]['source_family_id']}", "—", "66 complete；17 precise blocked Reviews 与 Materials Requests", "passed"],
    ["SA-20260509-INDEPENDENT-SELECTION", "fresh-context:may2026-day02", "deep_analysis_selection", "analysis:DA-FUTURE-STATE-SCHEDULING", "—", "83-family eligibility 与三项 narrative selection 已挑战", "passed"],
    ["SA-20260509-BOOKS-PREWRITE-POSTWRITE", "fresh-context:may2026-day02", "books", "books-review:SF-2026-ARXIV-2605-07330", "—", "21→3；3/3 写回语义验收通过；17 blocked 保持 conditional disposition", "passed"],
]
text = replace_table(text, "<!-- validator:semantic-audit-v1 -->", semantic_rows)
text = re.sub(
    r"## 9\. Recommended Action\n\n.*?\n\n## 10\.",
    "## 9. Recommended Action\n\n未来只在取得对应 exact-v1 材料时重开 17 项 blocker；其中 3 项 false negative 需要恢复后完成 Books Decision。其余 66 项与已写回 3 项不重复执行。\n\n## 10.",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r"## 11\. Open Questions\n\n.*?\n\n(?:### Materials Request|## 12\. Sources)",
    "## 11. Open Questions\n\n- exact-v1 材料恢复后，3 项 false negative 是否仍满足 Books Integration 门槛？\n\n### Materials Request",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r"## 13\. Final Status\n\n.*\Z",
    "## 13. Final Status\n\nCompletion Status: `Conditional`\n\nCoverage: `Closed`\n\nEvidence: `Conditional Pass`\n\nBooks: `Conditional Pass`\n\nunresolved findings: 0\n\nordinary work 已闭合；17 项精确 external exact-v1 blocker 均有一对一 Materials Request，其中 3 项标明恢复后的 Books scope。该状态是 Conditional，不是 Complete。\n",
    text,
    flags=re.S,
)
REPORT.write_text(text)

LEDGER["gate_status"] = "conditional_external_exact_v1_blockers_books_postwrite_passed"
write_json(LEDGER_PATH, LEDGER)
post = json.loads((ROOT / "post-write-semantic-audit.json").read_text())
post["gate"].update(
    books_post_write="Passed",
    books="Conditional Pass",
    completion="Conditional",
    reason="3 accessible deltas passed post-write audit; 17 exact-v1 external blockers retain Blocked / Unverified dispositions with precise Materials Requests.",
)
write_json(ROOT / "post-write-semantic-audit.json", post)
print("05-09 conditional truth projected: 83 retained, 66 complete, 17 blocked, Books post-write 3/3")
