#!/usr/bin/env python3
"""Remove a verified withdrawn arXiv identity from this day's raw screening artifacts."""

import gzip
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
WITHDRAWN = "2607.18056"


def load_gz(name: str) -> dict:
    with gzip.open(HERE / name, "rt", encoding="utf-8") as handle:
        return json.load(handle)


def save_gz(name: str, payload: dict) -> None:
    with gzip.open(HERE / name, "wt", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


raw_name = "canonical-raw-identity-inventory-v2.1.json.gz"
raw = load_gz(raw_name)
raw["identities"] = [item for item in raw["identities"] if item["arxiv_id"] != WITHDRAWN]
raw["raw_identity_count"] = len(raw["identities"])
raw["withdrawn_excluded"] = sorted(set(raw.get("withdrawn_excluded", [])) | {WITHDRAWN})
save_gz(raw_name, raw)

screen_name = "canonical-semantic-screening-checkpoint-v2.1.json.gz"
screen = load_gz(screen_name)
screen["items"] = [item for item in screen["items"] if item["arxiv_id"] != WITHDRAWN]
screen["raw_identity_count"] = len(screen["items"])
screen["closure_proposals_pending_audit"] = sum(
    item.get("semantic_screen_status") == "closure_proposed_pending_fresh_context_audit"
    for item in screen["items"]
)
save_gz(screen_name, screen)

print(json.dumps({"withdrawn": WITHDRAWN, "raw_identity_count": raw["raw_identity_count"]}))
