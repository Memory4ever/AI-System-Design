#!/usr/bin/env python3
"""Serialize the reviewed 2026-06-22 mechanism deltas into canonical Books owners.

This script is intentionally date-local and idempotence-strict. It may run only
while the root coordinator holds the shared Books write lock. It refuses a
partial or duplicate state instead of guessing how to merge it.
"""

from __future__ import annotations

import importlib.util
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260622"
FINALIZER = ROOT / "scripts/finalize_june22_v21.py"


def load_finalizer():
    spec = importlib.util.spec_from_file_location("june22_finalizer", FINALIZER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_finalizer()
    reviews = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text())["reviews"]
    integrations = [row for row in reviews if row["books_disposition"] == "Integrate"]
    assert len(reviews) == 39 and len(integrations) == 29

    all_books = list((ROOT / "books").rglob("*.md"))
    existing = {
        row["source_family_id"]: [
            str(path.relative_to(ROOT)) for path in all_books
            if row["source_family_id"] in path.read_text()
        ]
        for row in integrations
    }
    duplicates = {family: paths for family, paths in existing.items() if paths}
    if duplicates:
        raise RuntimeError(f"refusing partial/duplicate 06-22 writeback: {duplicates}")

    by_owner: dict[str, list[dict]] = defaultdict(list)
    for row in integrations:
        by_owner[row["stable_node_id"]].append(row)

    for owner, owner_reviews in sorted(by_owner.items()):
        path = ROOT / module.PATHS[owner]
        chapter = path.read_text()
        marker = "\n## Review notes\n"
        if chapter.count(marker) != 1:
            raise RuntimeError(f"expected exactly one Review notes marker in {path}")

        body = ["", "### 从局部结果到可执行的系统边界", ""]
        notes: list[str] = []
        for review in owner_reviews:
            aid = review["primary_identifier"].removeprefix("arXiv:").removesuffix("v1")
            evidence = module.C[aid]
            family = review["source_family_id"]
            body.extend([
                f"<!-- body-source:{family} -->",
                (
                    f"{evidence['delta']} 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；"
                    f"{evidence['boundary']} 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，"
                    "不能被新的局部结果静默覆盖。"
                ),
                "",
            ])
            notes.append(
                f"- `{family}` — primary `{review['primary_identifier']}`；"
                f"Method=`{review['method_identity_locators']}`；"
                f"Evaluation=`{review['evaluation_locators']}`；"
                f"Non-proof=`{review['limitations_counterevidence_locators']}`；"
                f"Artifact=`{review['artifact_locators']}`。"
            )

        insert = "\n".join(body).rstrip() + "\n\n## Review notes\n\n" + "\n".join(notes) + "\n"
        path.write_text(chapter.replace(marker, "\n" + insert, 1))

    print(f"applied 29 source families to {len(by_owner)} canonical owner chapters")


if __name__ == "__main__":
    main()
