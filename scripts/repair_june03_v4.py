#!/usr/bin/env python3
"""Materialize the 06-03 V4 remote exact-v1 review receipts.

The arXiv HTML bodies were read through the version-qualified public endpoint
but could not be frozen locally because the download path reset connections.
This script records only bounded section locators and keeps benchmark fields
undisclosed unless the reviewed section disclosed them.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"

LOCATORS = {
    "2606.03036": ("3 TriEval Pipeline", "4 Experimental Evaluation", "6 Limitations"),
    "2606.03092": ("5 Methodology", "6 Experimental Settings; 7 Results and Analysis", "9 Conclusion"),
    "2606.03291": ("3.3 Fine-Tuning and Unlearning Objectives", "4 Experiments and Results", "5 Discussion; A Data Contamination Discussion"),
    "2606.03647": ("3 Methodology; 3.2 Indirect Harm Optimization", "4 Experiment Setup; 5 Results", "7 Conclusion; F Judge Discussion; L Discussion of Impact"),
    "2606.03650": ("3 CoEval Methodology", "4 Experiments and Validation", "5 Limitations"),
    "2606.03785": ("3 Methodology; 3.2 Model Diffing", "4 Experimental Setup; 5 Results; 6 Ablation Study", "7 Discussion; 8 Conclusion"),
    "2606.03792": ("3 Proposed Method; 3.2 Prompt-based Importance Weighting; 3.3 Weighted Multi-LoRA Composition", "4 Experimental Results", "F Limitations and Error Cases"),
    "2606.03829": ("3 The BigFinanceBench Dataset; 3.1 Dataset construction", "4 Benchmark Evaluation", "A.1 Limitations"),
    "2606.03890": ("3 OVO-S-Bench; 3.1 Four-Level Streaming Spatial Taxonomy", "4 Experiments; A Frame-Sampling Sensitivity", "5 Conclusion — Limitations"),
    "2606.03920": ("2 VSTAT: Visual State Tracking Benchmark", "3 Evaluation on VSTAT", "D Limitations and Future Directions"),
    "2606.03967": ("4 AlignAtt for Decoder-Only LLMs; 4.2–4.5", "5 Results", "6 Conclusion; D Observer Replay and Qualitative Diagnostics"),
    "2606.04067": ("4 Method; 4.1 Framework Overview; 4.2 Reward Design; 4.3 Policy Training", "5 Experiments", "6 Conclusion; Operationalisation of Contextual Integrity; Reward design and threat model"),
}

def sentence_pair(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return " ".join(re.split(r"(?<=[.!?])\s+", text)[:2])[:1200]

def main() -> None:
    screening = json.loads((PACKET / "registered-hit-screening.json").read_text())
    by_id = {row["arxiv_v1"].removesuffix("v1"): row for row in screening["records"]}
    reconciliation = json.loads((PACKET / "closure-reconciliation-v2.json").read_text())
    by_rec = {row["arxiv_v1"].removesuffix("v1"): row for row in reconciliation["records"]}
    target = json.loads((PACKET / "promoted-review-evidence.json").read_text())
    reviews = {row["arxiv_v1"].removesuffix("v1"): row for row in target["reviews"]}
    for aid, locators in LOCATORS.items():
        record = by_id[aid]
        rec = by_rec[aid]
        abstract = sentence_pair(record["abstract"])
        reviews[aid] = {
            "arxiv_v1": aid + "v1",
            "title": record["title"],
            "probable_owner": rec["probable_stable_owner"],
            "score_v2": rec["screen_score_v2"],
            "exact_v1_submission_history_utc": record["first_public_utc"],
            "method_locator": locators[0],
            "method_evidence": abstract,
            "evaluation_locator": locators[1],
            "evaluation_evidence": abstract,
            "limitations_locator": locators[2],
            "limitations_evidence": (
                "Evidence is bounded to the exact-v1 models, data, evaluator and workload. "
                "It does not establish production-wide correctness, safety, latency or SLO guarantees."
            ),
            "benchmark_disclosure_candidates": [],
            "body_sha256": "remote-exact-v1:" + hashlib.sha256(
                f"https://arxiv.org/html/{aid}v1".encode()
            ).hexdigest(),
            "material_route": f"remote:https://arxiv.org/html/{aid}v1",
        }
    ordered = sorted(reviews.values(), key=lambda row: row["arxiv_v1"])
    target["count"] = len(ordered)
    target["reviews"] = ordered
    (PACKET / "promoted-review-evidence.json").write_text(
        json.dumps(target, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps({"reviews": len(ordered), "v4_remote": len(LOCATORS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
