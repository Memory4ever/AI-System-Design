#!/usr/bin/env python3
"""Apply author-side false-negative corrections after closure quality review."""

import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
JP = HERE / "screening-ledger-v2.1.json"
TP = HERE / "screening-ledger-v2.1.tsv"

REOPEN = {
    "2605.01191": ("SF-SENTINEL-VLA-STATUS-CONTROL", "MULTIMODAL-EMBODIED-VLA", [3, 3, 2]),
    "2605.01201": ("SF-VISUOMOTOR-EXECUTION-GUARANTEE", "MULTIMODAL-EMBODIED-VLA", [3, 3, 3]),
    "2605.01302": ("SF-COUNTERFACTUAL-RISK-RAG", "AGENT-RAG", [3, 3, 2]),
    "2605.01386": ("SF-PROVENANCE-GRAPH-MEMORY", "AGENT-MEMORY", [2, 3, 2]),
    "2605.01429": ("SF-LORA-COMPOSITION-RELIABILITY", "TRAIN-LORA", [3, 3, 2]),
    "2605.01567": ("SF-DEVELOPER-MEMORY-OPE-GATE", "AGENT-MEMORY", [3, 3, 3]),
    "2605.01604": ("SF-PRODUCTION-AGENT-EVALUATION", "PLATFORM-EVALUATION-SYSTEM", [2, 3, 3]),
    "2605.08143": ("SF-SEQUENTIAL-MODEL-EDIT-SIDECAR", "—", [3, 3, 3]),
}

data = json.loads(JP.read_text())
for row in data["rows"]:
    if row["arxiv_id"] in REOPEN:
        family, owner, score = REOPEN[row["arxiv_id"]]
        row.update(screening_decision="retain", source_family_id=family, stable_node_id=owner, score_v2=score, closure_reason="—")
data["candidate_denominator_count"] = sum(r["screening_decision"] == "retain" for r in data["rows"])
data["pre_denominator_closure_count"] = sum(r["screening_decision"] == "pre_denominator_closure" for r in data["rows"])
data["retained_candidates"] = data["candidate_denominator_count"]
data["pre_denominator_closures"] = data["pre_denominator_closure_count"]
data["false_negative_author_audit"] = {
    "reopened": sorted(REOPEN),
    "result": "eight false negatives corrected; exact-v1 review added; independent fresh-context audit remains open",
}
JP.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
fields = list(data["rows"][0])
with TP.open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
    writer.writeheader(); writer.writerows(data["rows"])
print(data["candidate_denominator_count"], data["pre_denominator_closure_count"])
