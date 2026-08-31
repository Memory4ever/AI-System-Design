#!/usr/bin/env python3
"""Apply the reviewed 2026-06-20 Books packet once, before Review notes.

The date owner deliberately does not touch shared Books.  This root-only
writeback keeps one body location and one evidence note per Source Family and
refuses to run if a family is already present anywhere in Books.
"""

from __future__ import annotations

import importlib.util
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260620"
FINALIZER = ROOT / "scripts/finalize_june20_v21.py"


def load_finalizer():
    spec = importlib.util.spec_from_file_location("june20_finalizer", FINALIZER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_finalizer()
    receipts = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text())["reviews"]
    retained = {
        row["arxiv_id"]: row
        for row in json.loads((PACKET / "screening-ledger.json").read_text())["identities"]
        if row["semantic_screen_status"].startswith("retained")
    }
    integrations = [r for r in receipts if r["books_disposition"] == "Integrate"]
    assert len(integrations) == 44

    all_books = list((ROOT / "books").rglob("*.md"))
    existing_counts = {
        review["source_family_id"]: sum(path.read_text().count(review["source_family_id"]) for path in all_books)
        for review in integrations
    }
    # A previous invocation may have completed the prose and stopped during
    # verification before adding the body locator.  Repair only that exact
    # state; any mixed/other state remains a hard error.
    if set(existing_counts.values()) == {1}:
        for review in integrations:
            aid = review["primary_identifier"].removeprefix("arXiv:").removesuffix("v1")
            owner = review["stable_node_id"]
            path = ROOT / module.PATHS[owner]
            text = path.read_text()
            title = retained[aid]["title"]
            marker = f"**{title} 所揭示的约束变化。**"
            if text.count(marker) != 1:
                raise RuntimeError(f"cannot locate unique body paragraph for {review['source_family_id']}")
            path.write_text(text.replace(marker, f"<!-- body-source:{review['source_family_id']} -->\n{marker}", 1))
        print("repaired 44 body-source locators after interrupted verification")
        return
    for review in integrations:
        family = review["source_family_id"]
        hits = [str(path.relative_to(ROOT)) for path in all_books if family in path.read_text()]
        if hits:
            raise RuntimeError(f"refusing duplicate write for {family}: {hits}")

    by_owner: dict[str, list[dict]] = defaultdict(list)
    for review in integrations:
        by_owner[review["stable_node_id"]].append(review)

    for owner, reviews in by_owner.items():
        path = ROOT / module.PATHS[owner]
        text = path.read_text()
        marker = "\n## Review notes\n"
        if text.count(marker) != 1:
            raise RuntimeError(f"expected one Review notes marker in {path}")

        body = ["", "### 新证据如何改变本章的设计边界", ""]
        notes = []
        for review in reviews:
            aid = review["primary_identifier"].removeprefix("arXiv:").removesuffix("v1")
            delta = module.SPECS[aid][1]
            fallback = module.FALLBACKS[owner]
            limits = review["limitations_counterevidence_locators"]
            title = retained[aid]["title"]
            body.extend(
                [
                    f"<!-- body-source:{review['source_family_id']} -->\n"
                    f"**{title} 所揭示的约束变化。** {delta}。这条路径只在 exact-v1 披露的任务与系统边界内成立；"
                    f"`{limits}` 记录了未证明范围。{fallback}；原有简单路径在其假设成立时继续共存。",
                    "",
                ]
            )
            notes.append(
                f"- `{review['source_family_id']}` — primary `{review['primary_identifier']}`；"
                f"Method=`{review['method_identity_locators']}`；"
                f"Evaluation=`{review['evaluation_locators']}`；"
                f"Non-proof=`{limits}`；Artifact=`{review['artifact_locators']}`。"
            )

        insert = "\n".join(body).rstrip() + "\n\n## Review notes\n\n" + "\n".join(notes) + "\n"
        path.write_text(text.replace(marker, "\n" + insert, 1))

    print(f"applied {len(integrations)} families to {len(by_owner)} owner files")


if __name__ == "__main__":
    main()
