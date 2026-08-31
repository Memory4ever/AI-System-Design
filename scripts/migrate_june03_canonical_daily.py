#!/usr/bin/env python3
"""Idempotently migrate the accepted 2026-06-03 Daily presentation.

This is a reader-facing migration only.  It preserves every bounded Source
Review body and the entire Review Completion receipt table byte-for-byte.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/03/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"

HEADER = """**Research Date:** 2026-06-03

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-02 09:00:00 ～ 2026-06-03 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；747/747 official arXiv identities 完成 title+abstract semantic screen，技术 claim 仅来自 exact-v1 review 与 UltraEP official v1 abstract recovery boundary

**Status:** Complete — V9 semantic audits passed；Coverage `Closed`；Evidence `Passed`；Books `Passed`；UltraEP official exact-v1 abstract recovery closed the final blocker
"""

RECOMMENDED = """## 9. Recommended Action

维持 root 已接受的最终处置：`16 Integrate / 39 No Change — Existing Coverage`。UltraEP 继续由 Ch36 的 dynamic expert-placement 机制覆盖，Ch21/Ch56 保留模型路由与 serving handoff；不新增 Books 写回，也不引入 later v3/repository evidence。
"""

FINAL = """## 13. Final Status

- Denominator: `DEN-20260603-V9-STRICT-c2194043`；`747 = 55 retained + 691 pre-denominator closures + 1 same-family supporting version`。
- Evidence: `55/55` exact-v1 Reviews complete；UltraEP 只保留 official v1 abstract 所披露的 Method/Evaluation，其他字段继续 `Not Disclosed`。
- Selection / Books: eligible Selection `50/50` + non-eligible closure `5/5` = candidate coverage `55/55`；selected `3`；`16 Integrate / 39 No Change — Existing Coverage`；root writeback 与 post-write audit 已闭合。
- Gates: Coverage `Closed`；Evidence `Passed`；Books `Passed`；Completion `Complete`。
"""

EXPECTED_H2 = [
    "## Executive Summary",
    "## 1. Coverage",
    "## 2. Candidate Ledger",
    "## 3. Review Completion Receipt",
    "## 4. Benchmark Contracts",
    "## 5. Deep Analysis Selection",
    "## 6. Books Comparison",
    "## 7. Semantic Audit",
    "## 8. Ignored Noise",
    "## 9. Recommended Action",
    "## 10. Repository Changes",
    "## 11. Open Questions",
    "## 12. Sources",
    "## 13. Final Status",
]


def bounded_reviews(text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    pattern = re.compile(r"<!-- review:([^:]+):start -->.*?<!-- review:\1:end -->", re.S)
    for match in pattern.finditer(text):
        family = match.group(1)
        assert family not in found
        found[family] = match.group(0)
    return found


def receipt_table(text: str) -> str:
    start = text.index("<!-- validator:review-completion-v1 -->")
    end = text.index("\n\n### Source Reviews", start)
    return text[start:end]


def canonicalize(text: str) -> str:
    before_reviews = bounded_reviews(text)
    before_receipt = receipt_table(text)
    assert len(before_reviews) == 55

    header_start = text.index("**Research Date:**")
    executive = text.index("## Executive Summary")
    text = text[:header_start] + HEADER + "\n" + text[executive:]

    replacements = {
        "### Benchmark Contracts": "## 4. Benchmark Contracts",
        "## 4. Deep Analysis Selection": "## 5. Deep Analysis Selection",
        "## 5. Deep Analysis": "### Deep Analysis",
        "## 6. Books Comparison / Recommended Action": "## 6. Books Comparison",
        "## 8. Materials Recovery Receipt": "### Materials Recovery Receipt",
        "## 8. Materials Request": "### Materials Request",
        "## 9. Ignored Noise": "## 8. Ignored Noise",
    }
    for old, new in replacements.items():
        text = re.sub(rf"(?m)^{re.escape(old)}$", new, text)

    if "## 9. Recommended Action" not in text:
        insert_at = text.index("\n## 10. Repository Changes\n")
        text = text[:insert_at] + "\n" + RECOMMENDED + text[insert_at:]

    repository_line = "- 本轮仅迁移 reader-facing canonical 13 节；55 个 bounded Source Review body 与 Review Provenance receipt 保持逐字不变。\n"
    if repository_line not in text:
        marker = "## 10. Repository Changes\n\n"
        assert marker in text
        text = text.replace(marker, marker + repository_line, 1)

    if "## 13. Final Status" not in text:
        text = text.rstrip() + "\n\n" + FINAL
    text = text.rstrip() + "\n"

    assert bounded_reviews(text) == before_reviews
    assert receipt_table(text) == before_receipt
    headings = re.findall(r"(?m)^## .+$", text)
    assert headings == EXPECTED_H2, headings
    for marker in (
        "validator:report-metadata-v2",
        "validator:source-coverage-v2",
        "validator:candidate-ledger-v2.1",
        "validator:review-completion-v1",
        "validator:benchmark-contract-v1",
        "validator:deep-analysis-selection-v1",
        "validator:books-comparison-v1",
        "validator:semantic-audit-v1",
    ):
        assert text.count(marker) == 1, marker
    return text


def regenerate_manifest() -> None:
    """Seal every date-local packet file plus the reader-facing Daily."""
    manifest = PACKET / "SHA256SUMS"
    targets = sorted(path for path in PACKET.rglob("*") if path.is_file() and path != manifest)
    targets.append(REPORT)
    rows = [
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT)}"
        for path in sorted(targets)
    ]
    manifest.write_text("\n".join(rows) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    before = REPORT.read_text()
    after = canonicalize(before)
    if args.apply:
        REPORT.write_text(after)
        regenerate_manifest()
    print(
        f"{'changed' if before != after else 'already_canonical'} "
        f"reviews=55 receipt_bytes_preserved=yes sha256={hashlib.sha256(after.encode()).hexdigest()}"
    )


if __name__ == "__main__":
    main()
