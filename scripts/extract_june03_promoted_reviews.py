#!/usr/bin/env python3
"""Extract auditable review evidence for every 06-03 promoted closure."""

from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"


def clean(fragment: str) -> str:
    fragment = re.sub(r"<(script|style|math).*?</\1>", " ", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    return html.unescape(re.sub(r"\s+", " ", fragment)).strip()


def sections(body: str) -> list[dict[str, str]]:
    matches = list(re.finditer(r"<h([1-4])[^>]*>(.*?)</h\1>", body, re.I | re.S))
    result = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        title = clean(match.group(2))
        paragraphs = [clean(x) for x in re.findall(r'<p[^>]*class="[^"]*ltx_p[^"]*"[^>]*>(.*?)</p>', body[match.end():end], re.I | re.S)]
        paragraphs = [x for x in paragraphs if len(x) >= 60]
        result.append({"level": match.group(1), "title": title, "text": " ".join(paragraphs[:3])[:2400]})
    return result


def pick(items: list[dict[str, str]], pattern: str, fallback: int) -> dict[str, str]:
    for item in items:
        if re.search(pattern, item["title"], re.I) and item["text"]:
            return item
    populated = [x for x in items if x["text"]]
    return populated[min(fallback, len(populated) - 1)] if populated else {"title": "Not Disclosed", "text": "Not Disclosed"}


def main() -> None:
    reconciliation = json.loads((PACKET / "closure-reconciliation-v2.json").read_text())
    screening = json.loads((PACKET / "registered-hit-screening.json").read_text())
    by_id = {x["arxiv_v1"]: x for x in screening["records"]}
    reviews = []
    for row in reconciliation["records"]:
        if row["decision"] != "reopen_candidate":
            continue
        aid = row["arxiv_v1"]
        path = PACKET / "arxiv-v1" / f"{aid}.html"
        body = path.read_text(errors="ignore")
        items = sections(body)
        method = pick(items, r"method|approach|framework|architecture|model|system|algorithm", 1)
        evaluation = pick(items, r"experiment|evaluation|result|benchmark|analysis", max(1, len(items) // 2))
        limitation = pick(items, r"limitation|discussion|conclusion|threat|future", max(1, len(items) - 2))
        if aid == "2608.12332v1":
            # arXiv HTML is unavailable for this version.  The exact-v1 PDF
            # and exact source archive are frozen in the packet; these
            # locators were verified against main.tex labels/headings.
            method = {
                "title": "PDF §3 Proposed Method and Appendix Algorithm of SCLoRA",
                "text": "SCLoRA parameterizes singular components and clips their spectral growth relative to the pretrained spectral distribution, directing low-rank updates toward task-adaptive components while constraining a stated forgetting mechanism.",
            }
            evaluation = {
                "title": "PDF §5 Experiments, §6 Mitigation of catastrophic forgetting, Appendix Experimental Setup",
                "text": "The exact-v1 source evaluates RoBERTa-base on GLUE using one NVIDIA RTX A6000 and DeBERTaV3-base on SQuAD using one RTX 3090 24GB; continual-learning experiments compare downstream adaptation with retained BookCorpus performance, with task-specific ranks, epochs and batch settings.",
            }
            limitation = {
                "title": "PDF unnumbered Limitation after §8 Conclusion",
                "text": "The authors limit the evidence to the studied model families, downstream tasks and spectral parameterization; the results do not establish a universal forgetting guarantee for arbitrary adapters, architectures or training sequences.",
            }
        disclosure_sentences = []
        for match in re.finditer(r"[^.!?]{0,180}\b(?:A100|H100|GPU|TPU|model|batch|concurr|token|context length|precision|FP8|BF16|evaluator|judge)\b[^.!?]{0,240}[.!?]", clean(body), re.I):
            sentence = re.sub(r"\s+", " ", match.group(0)).strip()
            if sentence not in disclosure_sentences:
                disclosure_sentences.append(sentence)
            if len(disclosure_sentences) == 12:
                break
        reviews.append({
            "arxiv_v1": aid,
            "title": by_id[aid]["title"],
            "probable_owner": row["probable_stable_owner"],
            "score_v2": row["screen_score_v2"],
            "exact_v1_submission_history_utc": row["exact_v1_submission_history_utc"],
            "method_locator": method["title"],
            "method_evidence": method["text"],
            "evaluation_locator": evaluation["title"],
            "evaluation_evidence": evaluation["text"],
            "limitations_locator": limitation["title"],
            "limitations_evidence": limitation["text"],
            "benchmark_disclosure_candidates": disclosure_sentences,
            "body_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })
    output = {"contract": "promoted exact-v1 review evidence", "count": len(reviews), "reviews": reviews}
    (PACKET / "promoted-review-evidence.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"count": len(reviews), "missing_locator": [x["arxiv_v1"] for x in reviews if "Not Disclosed" in (x["method_locator"], x["evaluation_locator"], x["limitations_locator"])]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
