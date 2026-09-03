#!/usr/bin/env python3
"""Remove a confirmed-withdrawn arXiv family from derived Daily artifacts.

Raw upstream snapshots are intentionally immutable. Everything derived from the
withdrawn identity (candidate, review, analysis and Books handoff) is removed.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import apply_reopen


ROOT = Path(__file__).resolve().parents[5]
REPORT = ROOT / "papers/2026/06/24/README.md"
SOURCE_DIR = ROOT / "papers/2026/06/_sources/daily-20260624"
FAMILY = "SF-2026-ARXIV-2606-24369"
ARXIV_ID = "2606.24369"
TITLE = "Accelerating Disaggregated RL for Visual Generative LLMs with Diffusion-Based Parallelism and Trainer-Assisted Generation"


def contains_target(value: object) -> bool:
    if isinstance(value, str):
        return FAMILY in value or ARXIV_ID in value
    if isinstance(value, list):
        return any(contains_target(item) for item in value)
    if isinstance(value, dict):
        return any(contains_target(item) for item in value.values())
    return False


def clean_json(value: object) -> object:
    if isinstance(value, list):
        return [clean_json(item) for item in value if not contains_target(item)]
    if isinstance(value, dict):
        return {key: clean_json(item) for key, item in value.items()}
    return value


def update_json_counts(payload: object) -> None:
    if not isinstance(payload, dict):
        return
    items = payload.get("items")
    identities = payload.get("identities")
    decisions = payload.get("decisions")
    for key in ("retained_candidate_families", "frontier_size"):
        if key in payload and isinstance(payload[key], int):
            payload[key] = max(0, payload[key] - 1)
    if isinstance(items, list):
        if "result" in payload and isinstance(payload["result"], str):
            payload["result"] = re.sub(r"\b43/43\b", "42/42", payload["result"])
        if "compared" in payload:
            payload["compared"] = f"{len(items)}/{len(items)}"
    if isinstance(identities, list):
        payload["registered_window_identities"] = len(identities)
        payload["raw_snapshot_records"] = max(
            len(identities), int(payload.get("raw_snapshot_records", len(identities)))
        )
    if isinstance(decisions, list):
        payload["frontier_size"] = len(decisions)


def clean_json_file(path: Path) -> None:
    relative = path.relative_to(ROOT).as_posix()
    payload = json.loads(subprocess.check_output(["git", "show", f":{relative}"], cwd=ROOT))
    cleaned = clean_json(payload)
    update_json_counts(cleaned)
    path.write_text(json.dumps(cleaned, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def clean_line_file(path: Path) -> None:
    relative = path.relative_to(ROOT).as_posix()
    baseline = subprocess.check_output(["git", "show", f":{relative}"], cwd=ROOT).decode("utf-8")
    lines = baseline.splitlines()
    kept = [line for line in lines if FAMILY not in line and ARXIV_ID not in line and TITLE not in line]
    path.write_text("\n".join(kept) + "\n", encoding="utf-8")


def clean_report() -> None:
    relative = REPORT.relative_to(ROOT).as_posix()
    text = subprocess.check_output(["git", "show", f":{relative}"], cwd=ROOT).decode("utf-8")
    ledger_row = next(row for row in apply_reopen.LEDGER["reports"] if row["date"] == "2026-06-24")
    ledger_row = dict(ledger_row)
    ledger_row["existing_source_ids"] = ["SRC-ARXIV"]
    text = apply_reopen.replace_metadata(text)
    text = apply_reopen.update_coverage(text, ledger_row)
    text = apply_reopen.insert_reopen_notice(text, ledger_row)
    text = apply_reopen.update_semantic_audit(text, ledger_row)
    text = apply_reopen.update_final(text, ledger_row)
    marker_names = ("review", "claim", "analysis-decision", "existing", "delta", "books-review")
    for marker in marker_names:
        text = re.sub(
            rf"\n?<!-- {marker}:{re.escape(FAMILY)}:start -->.*?<!-- {marker}:{re.escape(FAMILY)}:end -->\n?",
            "\n",
            text,
            flags=re.S,
        )
    lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if cells and cells[0] == FAMILY:
                continue
        if line.startswith("- [") and (ARXIV_ID in line or TITLE in line):
            continue
        line = re.sub(
            rf"(?:review|analysis-decision|books-review):{re.escape(FAMILY)};?\s*",
            "",
            line,
        )
        line = line.replace(f"; {FAMILY}", "").replace(f"{FAMILY}; ", "").replace(FAMILY, "")
        lines.append(line.rstrip())
    text = "\n".join(lines) + "\n"
    replacements = {
        "freezes 43 durable families and 498 family-specific closures":
            "freezes 42 durable families and 499 family-specific exclusions (including withdrawn inputs)",
        "541 = 43 retained + 498 closures": "541 = 42 retained + 499 exclusions",
        "43/43 exact-v1 identities": "42/42 exact-v1 identities",
        "Final Books disposition: 43 Integrate": "Final Books disposition: 42 Integrate",
        "the 43/43 post-write fresh audit": "the 42/42 post-write fresh audit",
        "wrote 43 source-family deltas": "wrote 42 source-family deltas",
        "All 43 writebacks": "All 42 writebacks",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    REPORT.write_text(text, encoding="utf-8")


def main() -> None:
    clean_report()
    for path in sorted(SOURCE_DIR.iterdir()):
        if not path.is_file() or path.stat().st_size == 0:
            continue
        if path.suffix == ".json":
            clean_json_file(path)
        elif path.suffix in {".tsv", ".txt", ".md"}:
            clean_line_file(path)


if __name__ == "__main__":
    main()
