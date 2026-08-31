#!/usr/bin/env python3
"""Freeze the non-author denominator checkpoint for 2026-05-16.

This does not claim Evidence completion.  It separates the completed 542-row
semantic replay from the still-open exact-v1 recovery lane.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
source = json.loads((ROOT / "screening-ledger-final.json").read_text())

keep_existing = {
    "2605.15508", "2605.15514", "2605.15520", "2605.15529", "2605.15565",
    "2605.15573", "2605.15581", "2605.15609", "2605.15617", "2605.15618",
    "2605.15638", "2605.15648", "2605.15665", "2605.15694", "2605.15710",
    "2605.15734", "2605.15761", "2605.15777", "2605.15815", "2605.15846",
    "2605.15957", "2605.15960", "2605.15967", "2605.16035", "2605.16154",
    "2605.16184", "2605.16194", "2605.16198", "2605.16217", "2605.16508",
    "2605.16565", "2605.16604", "2605.16616", "2605.16626", "2605.16630",
    "2605.16637", "2605.16650", "2605.16704", "2605.16712", "2605.16725",
    "2605.21516",
}

recovered = {
    "2605.16007": ((3, 3, 3), "INFER-TENSORRT-LLM", "NPU/CPU 分阶段向量检索把量化表示、rank ownership、device placement 与 rerank correctness 变成异构执行合同"),
    "2605.16234": ((2, 2, 3), "MODEL-TRANSFORMER", "replacement 与 interchange 两种层冗余协议给出不同 pruning decision，改变压缩前必须冻结的 evaluator contract"),
    "2605.16255": ((3, 3, 3), "PLATFORM-COST", "AI rack power hierarchy 的目标从 installed MW 改为跨代际 deployable capacity，并显式联结 placement、oversubscription、workload mix 与 stranding"),
    "2605.16588": ((3, 2, 3), "MULTIMODAL-EMBODIED-VLA", "runtime safety filter 以并行有限时域 fallback-policy rollout 拥有安全 admission，改变 nominal policy 与 safety authority 的边界"),
    "2605.16622": ((2, 2, 3), "TRAIN-PRETRAINING", "weight decay 对 progressive sharpening 与 Edge-of-Stability 的 architecture-dependent 机制修正了训练稳定性的长期判断"),
    "2605.16647": ((3, 2, 3), "PLATFORM-SECURITY", "FHE sequence inference 迫使 carried encrypted state、public decay、local write path、depth 与 bootstrap pressure 共同决定模型结构"),
}

final_ids = keep_existing | set(recovered)
false_positive_ids = []
false_negative_ids = sorted(recovered)

for item in source["identities"]:
    aid = item["arxiv_id"]
    was_retained = item.get("screening_status") == "retained"
    if aid in final_ids:
        item["screening_status"] = "retained"
        if aid in recovered:
            (d, r, u), owner, reason = recovered[aid]
            item["screening_reason"] = (
                f"`{item['title']}`：恢复为 denominator candidate；{reason}。"
                "identity/abstract 已闭合，exact-v1 Method、evaluation、limitations 仍须独立恢复后才能完成 Evidence/Books Decision。"
            )
            item["score_v2"] = {"design_delta": d, "system_reach": r, "durability": u, "total": d + r + u}
            item["owner_node"] = owner
            item["source_family_id"] = f"SF-2026-ARXIV-{aid}"
            item["integration_disposition"] = "Blocked / Unverified"
        if aid == "2605.15529":
            item["review_status"] = "deep_complete"
            item["access_status"] = "accessible"
            item["integration_disposition"] = "No Change — Existing Coverage"
        else:
            item["review_status"] = "blocked"
            item["access_status"] = "blocked"
            item["integration_disposition"] = "Blocked / Unverified"
    else:
        if was_retained:
            false_positive_ids.append(aid)
            claim = item.get("abstract", "").split(". ")[0].strip()
            item["screening_reason"] = (
                f"`{item['title']}`：{claim}。该工作是单域方法、单 benchmark 或局部实现改进；"
                "没有改变跨 workload 的 state/data/control owner、evaluation/release contract 或生产 fallback，"
                "因此经非作者 challenge 降为 pre-denominator closure。"
            )
        item["screening_status"] = "pre_denominator_closure"
        item["review_status"] = "identity_date_closed"
        item["access_status"] = "accessible"
        item["integration_disposition"] = "Rejected — Below Candidate Denominator"
        for key in ("score_v2", "owner_node", "source_family_id"):
            item.pop(key, None)

retained = [x for x in source["identities"] if x["screening_status"] == "retained"]
source["schema"] = "daily-v2.1-independent-screening-ledger-v1"
source["candidate_denominator"] = len(retained)
source["pre_denominator_closures"] = len(source["identities"]) - len(retained)
source["independent_reconciliation"] = {
    "reviewer": "fresh-context:may2026-day02",
    "false_positive_downgrades": sorted(false_positive_ids),
    "false_negative_recoveries": false_negative_ids,
    "retained": len(retained),
    "closures": len(source["identities"]) - len(retained),
    "exact_v1_complete": 1,
    "exact_v1_blocked_pending_recovery": len(retained) - 1,
}

encoded = (json.dumps(source, ensure_ascii=False, indent=2) + "\n").encode()
out = ROOT / "screening-ledger-independent-checkpoint.json"
out.write_bytes(encoded)
out.with_suffix(out.suffix + ".sha256").write_text(hashlib.sha256(encoded).hexdigest() + "\n")

audit = {
    "schema": "daily-v2.1-independent-semantic-audit-v1",
    "report_date": "2026-05-16",
    "auditor": "fresh-context:may2026-day02",
    "scope": {
        "registered": 542,
        "screened": 542,
        "author_retained": 66,
        "final_retained": len(retained),
        "closures": 542 - len(retained),
    },
    "screening": {
        "status": "passed",
        "false_positive_downgrades": sorted(false_positive_ids),
        "false_negative_recoveries": false_negative_ids,
        "reason": "542/542 title+abstract replay separates recall from strict long-term AI-System denominator admission.",
    },
    "evidence": {
        "status": "open",
        "complete_source_families": ["SF-2026-ARXIV-2605.15529"],
        "blocked_source_families": [f"SF-2026-ARXIV-{x['arxiv_id']}" for x in retained if x['arxiv_id'] != "2605.15529"],
        "finding": "author packet uses generic section labels and abstract-only Review bodies; local exact-v1 body/provenance is absent. One family is recoverable from the already-audited W20 Full Source Review; remaining families require official HTML/PDF/TeX recovery.",
    },
    "books": {
        "status": "open",
        "final_queue": [],
        "reason": "No blocked family may enter current-Books comparison; the one recovered family is already covered by the existing reliability/calibration contract.",
    },
    "unresolved_findings": [
        "Recover exact-v1 body and non-generic Method/Evaluation/Limitations locators for 46 retained families before final Evidence and Books Decisions.",
        "Remove duplicate 2605.16712 Review Completion row when canonical README is re-rendered from the independent denominator.",
    ],
}
audit_bytes = (json.dumps(audit, ensure_ascii=False, indent=2) + "\n").encode()
audit_path = ROOT / "semantic-independent-audit-checkpoint.json"
audit_path.write_bytes(audit_bytes)
audit_path.with_suffix(audit_path.suffix + ".sha256").write_text(hashlib.sha256(audit_bytes).hexdigest() + "\n")

print(json.dumps({
    "retained": len(retained),
    "closures": 542 - len(retained),
    "false_positive_downgrades": len(false_positive_ids),
    "false_negative_recoveries": len(false_negative_ids),
    "exact_v1_complete": 1,
    "blocked": len(retained) - 1,
}, ensure_ascii=False))
