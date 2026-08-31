#!/usr/bin/env python3
"""Remove stale pre-write wording from closed May 2026 Daily reports.

This is a bounded current-truth rewrite.  It does not alter source reviews,
scores, evidence claims, Books prose, or immutable audit-stage artifacts.
"""

from __future__ import annotations

from pathlib import Path

from refresh_may_review_provenance import refresh as refresh_review_provenance


ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "2026/05/13": {
        "Books Decision=`Integrate`，等待 root 串行写回。":
            "Books Decision=`Integrate`；canonical owner 写回与独立 post-write Semantic Audit 均已通过。",
    },
    "2026/05/26": {
        "这是非作者基于 current owner+adjacent 的 pre-write decision；Integrate 项等待 root 串行写回与独立 post-write audit。":
            "这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。",
    },
    "2026/05/29": {
        "Books Gate 等待 root 写回与 post-write audit。":
            "最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。",
    },
    "2026/05/30": {
        "Books Gate 等待 root 写回与 post-write audit。":
            "最终 disposition 已由独立 post-write Semantic Audit 验收，Books Gate 已闭合。",
    },
    "2026/05/31": {
        "该项等待 root 串行写回与独立 post-write audit。":
            "该项已写入 canonical owner，并通过独立 post-write Semantic Audit。",
    },
}

STALE = (
    "Books Gate remains Open",
    "Books remains Open",
    "Books Gate 仍保持 Open",
    "Books Gate 保持 Open",
    "pending root",
    "等待 root",
    "post-write audit pending",
    "post-write audit 等待",
)


def main() -> None:
    changed = 0
    for date, replacements in REPLACEMENTS.items():
        path = ROOT / "papers" / date / "README.md"
        text = path.read_text(encoding="utf-8")
        if "**Status:** Complete" not in text or "Books=Passed" not in text:
            raise ValueError(f"refusing truth rewrite for non-closed report: {path}")
        original = text
        for old, new in replacements.items():
            count = text.count(old)
            if not count:
                # A concurrent independent closer may already have replaced
                # this stage wording with an equivalent current-state sentence.
                continue
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1

    remaining = []
    for path in sorted((ROOT / "papers/2026/05").glob("[0-3][0-9]/README.md")):
        text = path.read_text(encoding="utf-8")
        hits = {pattern: text.count(pattern) for pattern in STALE if pattern in text}
        if hits:
            remaining.append((path, hits))
    if remaining:
        raise ValueError(f"stale current-truth wording remains: {remaining}")
    refreshed = refresh_review_provenance() if changed else 0
    print(
        f"closed current-truth wording in {changed} report(s); "
        f"refreshed provenance rows={refreshed}; stale occurrences=0"
    )


if __name__ == "__main__":
    main()
