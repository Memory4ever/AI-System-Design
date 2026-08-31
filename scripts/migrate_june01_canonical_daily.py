#!/usr/bin/env python3
"""Idempotently migrate the 2026-06-01 Daily to the canonical 13-section layout.

This script only changes presentation order/headings and the top-level status
summary.  It deliberately preserves every validator marker, evidence table,
bounded review, analysis, Books comparison, audit row, and source entry.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/01/README.md"

HEADER = """**Research Date:** 2026-06-01

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-31 09:00:00 ～ 2026-06-01 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-ARXIV Atom 与 official exact-v1 history 冻结 identity/date，技术 claim 仅来自 exact arXiv v1 全文与本地冻结证据

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding
"""

FINAL_STATUS = """## 13. Final Status

- Denominator: `DEN-20260601-5c2ad97d`；`371 raw = 40 retained + 331 family-specific closures`。
- Evidence: `40/40` Source Reviews 与 Score V2、`36/36` Benchmark Claim=yes contracts、`40/40` full-frontier Selection 均已完成并通过 fresh-context audit；其余 4 个 retained family 明确为 Benchmark Claim=no。
- Books: `4 Integrate + 36 No Change`；四条写回各自唯一命中 canonical owner，excluded-family leakage 为零；完整 `40/40` Books surface 已完成 post-write fresh audit。
- Gates: Coverage `Closed`；Evidence `Passed`；Books `Passed`；Completion `Complete`。
"""

CANONICAL_HEADINGS = [
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


def normalize(text: str) -> str:
    text = text.replace("# AI Research Daily — 2026-06-01", "# Daily Research — 2026-06-01", 1)
    if "**Research Date:** 2026-06-01" not in text:
        title_end = text.index("\n", text.index("# Daily Research — 2026-06-01")) + 1
        text = text[:title_end] + "\n" + HEADER + "\n" + text[title_end:].lstrip("\n")

    replacements = {
        "## Coverage": "## 1. Coverage",
        "## Candidate Ledger": "## 2. Candidate Ledger",
        "## Review Completion Receipt": "## 3. Review Completion Receipt",
        "## Source Review": "### Source Reviews",
        "## Benchmark Contract": "## 4. Benchmark Contracts",
        "## Knowledge Tree Position": "### Knowledge Tree Position",
        "## Deep Analysis Selection": "## 5. Deep Analysis Selection",
        "## Books Comparison": "## 6. Books Comparison",
        "## Semantic Audit": "## 7. Semantic Audit",
        "## Recommended Action / Books Decision": "## 9. Recommended Action",
        "## Ignored Noise": "## 8. Ignored Noise",
        "## Repository Changes": "## 10. Repository Changes",
        "## Open Questions": "## 11. Open Questions",
        "## Sources": "## 12. Sources",
    }
    for old, new in replacements.items():
        text = re.sub(rf"(?m)^{re.escape(old)}$", new, text)

    # Knowledge-tree placement is Evidence-stage context.  Keep it inside the
    # Review/Source Reviews section rather than allowing it to become an
    # accidental subsection of Benchmark Contracts.
    knowledge_match = re.search(
        r"\n### Knowledge Tree Position\n.*?(?=\n## 5\. Deep Analysis Selection\n)",
        text,
        re.S,
    )
    benchmark_pos = text.find("\n## 4. Benchmark Contracts\n")
    if knowledge_match and knowledge_match.start() > benchmark_pos:
        block = knowledge_match.group(0)
        text = text[: knowledge_match.start()] + text[knowledge_match.end() :]
        benchmark_pos = text.index("\n## 4. Benchmark Contracts\n")
        text = text[:benchmark_pos] + block + "\n" + text[benchmark_pos:]

    # Canonical presentation puts Ignored Noise before Recommended Action.
    recommended = re.search(
        r"\n## 9\. Recommended Action\n.*?(?=\n## 8\. Ignored Noise\n)", text, re.S
    )
    ignored = re.search(
        r"\n## 8\. Ignored Noise\n.*?(?=\n## 10\. Repository Changes\n)", text, re.S
    )
    if recommended and ignored and recommended.end() <= ignored.start():
        rec_block = recommended.group(0)
        ignored_block = ignored.group(0)
        text = (
            text[: recommended.start()]
            + ignored_block
            + "\n"
            + rec_block
            + text[ignored.end() :]
        )

    if "## 13. Final Status" not in text:
        text = text.rstrip() + "\n\n" + FINAL_STATUS

    text = text.rstrip() + "\n"
    headings = re.findall(r"(?m)^## .+$", text)
    assert headings == CANONICAL_HEADINGS, headings
    assert "`40/40` benchmark contracts" not in text
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    before = REPORT.read_text()
    after = normalize(before)
    if args.apply:
        REPORT.write_text(after)
    mode = "changed" if before != after else "already_canonical"
    print(f"{mode} sha256={hashlib.sha256(after.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
