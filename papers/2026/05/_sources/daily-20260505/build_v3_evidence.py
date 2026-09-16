#!/usr/bin/env python3
"""Build candidate-specific exact-v1 evidence and Books-decision packets."""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEDGER = HERE / "V3_CANONICAL_LEDGER.json"
HTML = HERE / "arxiv-v1-html"
OUT = HERE / "V3_EVIDENCE_REVIEWS.json"
BOOKS_MD = HERE / "V3_BOOKS_REVIEW_QUEUE.md"

DEEP = {
    "2605.00831", "2605.00842", "2605.01032", "2605.01037", "2605.01188",
    "2605.01194", "2605.01201", "2605.01342", "2605.01640", "2605.01708",
    "2605.01740", "2605.01837", "2605.01858", "2605.01930", "2605.01970",
    "2605.02187", "2605.02329", "2605.02404", "2605.02682", "2605.02881",
}

INTEGRATE_PROPOSED = {
    "2605.00935", "2605.01032", "2605.01137", "2605.01192", "2605.01220",
    "2605.01288", "2605.01449", "2605.01643", "2605.01725", "2605.01740",
    "2605.01790", "2605.01823", "2605.01837", "2605.01928", "2605.01930",
    "2605.01936", "2605.02083", "2605.02106",
}

OWNER_OVERRIDES = {
    "2605.00832": "PLATFORM-EVALUATION-SYSTEM",
    "2605.00974": "PLATFORM-SECURITY",
    "2605.00994": "PLATFORM-EVALUATION-SYSTEM",
    "2605.01032": "AGENT-PLATFORM",
    "2605.01037": "AGENT-PLATFORM",
    "2605.01060": "INFER-GPU-MEMORY",
    "2605.01069": "MULTIMODAL-EMBODIED-VLA",
    "2605.01195": "MULTIMODAL-EMBODIED-VLA",
    "2605.01255": "TRAIN-DISTRIBUTED-TRAINING",
    "2605.01298": "PLATFORM-SECURITY",
    "2605.01415": "PLATFORM-SECURITY",
    "2605.01643": "TRAIN-RLHF",
    "2605.01699": "PLATFORM-SECURITY",
    "2605.01740": "AGENT-PLATFORM",
    "2605.01761": "PLATFORM-SECURITY",
    "2605.01928": "TRAIN-PRETRAINING",
    "2605.02083": "AGENT-WORKFLOW",
    "2605.02189": "INFER-SCHEDULING",
    "2605.02241": "PLATFORM-EVALUATION-SYSTEM",
    "2605.02364": "TRAIN-DATA",
    "2605.02404": "INFER-TENSORRT-LLM",
    "2605.02739": "MULTIMODAL-EMBODIED-VLA",
    "2605.02812": "PLATFORM-SECURITY",
    "2605.02821": "PLATFORM-EVALUATION-SYSTEM",
    "2605.02853": "TRAIN-PRETRAINING",
}

CHAPTERS = {
    "WORLDVIEW-REPRESENTATION": (5, "books/part-01-worldview/05-what-neural-networks-learn.md"),
    "MULTIMODAL-REPRESENTATION": (23, "books/part-03-multimodal-world-models/23-multimodal-representation.md"),
    "MULTIMODAL-GENERATIVE-PARADIGMS": (24, "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md"),
    "MULTIMODAL-WORLD-MODELS": (25, "books/part-03-multimodal-world-models/25-multimodal-world-models.md"),
    "MULTIMODAL-EMBODIED-VLA": (26, "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md"),
    "TRAIN-DATA": (27, "books/part-04-training-system/27-data.md"),
    "TRAIN-PRETRAINING": (28, "books/part-04-training-system/28-pretraining.md"),
    "TRAIN-SFT": (29, "books/part-04-training-system/29-sft.md"),
    "TRAIN-RLHF": (31, "books/part-04-training-system/31-rlhf.md"),
    "TRAIN-GRPO": (33, "books/part-04-training-system/33-grpo.md"),
    "TRAIN-DISTRIBUTED-TRAINING": (36, "books/part-04-training-system/36-distributed-training.md"),
    "INFER-KV-CACHE": (45, "books/part-05-inference-system/45-why-kv-cache-speeds-up.md"),
    "INFER-SPECULATIVE-DECODING": (48, "books/part-05-inference-system/48-speculative-decoding.md"),
    "INFER-TENSORRT-LLM": (49, "books/part-05-inference-system/49-tensorrt-llm.md"),
    "INFER-GPU-MEMORY": (54, "books/part-05-inference-system/54-gpu-memory.md"),
    "INFER-PD-DISAGGREGATION": (55, "books/part-05-inference-system/55-pd-disaggregation.md"),
    "INFER-SCHEDULING": (56, "books/part-05-inference-system/56-inference-scheduling.md"),
    "PLATFORM-GPU-SCHEDULER": (63, "books/part-06-ai-infrastructure/63-gpu-scheduler.md"),
    "PLATFORM-EVALUATION-SYSTEM": (66, "books/part-06-ai-infrastructure/66-evaluation-system.md"),
    "PLATFORM-TRACE": (69, "books/part-06-ai-infrastructure/69-trace.md"),
    "PLATFORM-MULTI-TENANT": (71, "books/part-06-ai-infrastructure/71-multi-tenant.md"),
    "PLATFORM-SECURITY": (72, "books/part-06-ai-infrastructure/72-security.md"),
    "AGENT-CONTEXT": (75, "books/part-07-agent/75-context.md"),
    "AGENT-RAG": (76, "books/part-07-agent/76-rag.md"),
    "AGENT-MEMORY": (77, "books/part-07-agent/77-memory.md"),
    "AGENT-TOOL-CALLING": (78, "books/part-07-agent/78-tool-calling.md"),
    "AGENT-WORKFLOW": (81, "books/part-07-agent/81-workflow.md"),
    "AGENT-MULTI-AGENT": (82, "books/part-07-agent/82-multi-agent.md"),
    "AGENT-MCP": (83, "books/part-07-agent/83-mcp.md"),
    "AGENT-PLATFORM": (84, "books/part-07-agent/84-agent-platform.md"),
}


class SectionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_heading = False
        self.heading_parts: list[str] = []
        self.current = "Front matter"
        self.sections: dict[str, list[str]] = {self.current: []}
        self.in_ignored = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "nav"}:
            self.in_ignored += 1
        if re.fullmatch(r"h[1-6]", tag):
            self.in_heading = True
            self.heading_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "nav"} and self.in_ignored:
            self.in_ignored -= 1
        if re.fullmatch(r"h[1-6]", tag) and self.in_heading:
            heading = " ".join("".join(self.heading_parts).split())
            if heading and heading != "Report GitHub Issue":
                self.current = heading
                self.sections.setdefault(heading, [])
            self.in_heading = False

    def handle_data(self, data: str) -> None:
        if self.in_ignored:
            return
        if self.in_heading:
            self.heading_parts.append(data)
            return
        text = " ".join(data.split())
        if text:
            self.sections.setdefault(self.current, []).append(text)


def parse_sections(path: Path) -> dict[str, str]:
    parser = SectionParser()
    parser.feed(path.read_text(errors="replace"))
    return {heading: " ".join(parts) for heading, parts in parser.sections.items()}


def choose_headings(headings: list[str], pattern: str, fallback: list[str], limit: int = 3) -> list[str]:
    hits = [h for h in headings if re.search(pattern, h, re.I)]
    return (hits or fallback)[:limit]


def owner_for(arxiv_id: str, title: str, mechanism: str) -> str:
    if arxiv_id in OWNER_OVERRIDES:
        return OWNER_OVERRIDES[arxiv_id]
    text = f"{title} {mechanism}".lower()
    if "mcp" in text:
        return "AGENT-MCP"
    if "multi-agent" in text or "consensus" in text or "debate" in text:
        return "AGENT-MULTI-AGENT"
    if "agent memory" in text or "persistent memory" in text or "episodic-semantic" in text:
        return "AGENT-MEMORY"
    if "rag" in text or "retrieval" in text or "evidence admission" in text:
        return "AGENT-RAG"
    if "workflow" in text or "checker" in text or "recursive llm" in text:
        return "AGENT-WORKFLOW"
    if "vla" in text or "visuomotor" in text or "robot" in text or "physical" in text or "collaborative perception" in text:
        return "MULTIMODAL-EMBODIED-VLA"
    if "world-model" in text or "world model" in text or "predictive latent" in text:
        return "MULTIMODAL-WORLD-MODELS"
    if "diffusion" in text or "video generation" in text or "acoustic-token" in text or "visual implicit autoregressive" in text:
        return "MULTIMODAL-GENERATIVE-PARADIGMS"
    if "multimodal" in text or "visual" in text or "video understanding" in text:
        return "MULTIMODAL-REPRESENTATION"
    if "specul" in text:
        return "INFER-SPECULATIVE-DECODING"
    if "kv" in text and ("transfer" in text or "disaggregated" in text):
        return "INFER-PD-DISAGGREGATION"
    if "kv" in text or "cache" in text or "attention" in text:
        return "INFER-KV-CACHE"
    if "gpu" in text and ("power" in text or "tenant" in text or "sharing" in text):
        return "PLATFORM-GPU-SCHEDULER"
    if "scheduling" in text or "slo" in text or "offline inference" in text:
        return "INFER-SCHEDULING"
    if "distributed" in text or "asynchronous sgd" in text or "transport" in text:
        return "TRAIN-DISTRIBUTED-TRAINING"
    if "tokenization" in text:
        return "TRAIN-DATA"
    if "rlhf" in text or "preference" in text or "binary reward" in text or "reward model" in text:
        return "TRAIN-RLHF"
    if "grpo" in text or "rlvr" in text:
        return "TRAIN-GRPO"
    if "training" in text or "pretraining" in text or "finetun" in text or "routing" in text:
        return "TRAIN-PRETRAINING"
    if "superposition" in text or "representation" in text or "saddle" in text:
        return "WORLDVIEW-REPRESENTATION"
    if "security" in text or "attack" in text or "privacy" in text or "poison" in text or "tamper" in text or "zero-trust" in text or "jailbreak" in text or "fingerprint" in text:
        return "PLATFORM-SECURITY"
    if "trace" in text or "log" in text or "audit record" in text:
        return "PLATFORM-TRACE"
    if "evaluation" in text or "metric" in text or "confidence" in text or "reliability" in text or "credit" in text or "scoring" in text:
        return "PLATFORM-EVALUATION-SYSTEM"
    if "context" in text:
        return "AGENT-CONTEXT"
    return "PLATFORM-EVALUATION-SYSTEM"


def score_for(arxiv_id: str, title: str, mechanism: str, owner: str) -> dict[str, object]:
    """Calibrate V2 from the retained design delta, not topic keywords alone."""
    combined = f"{title} {mechanism}".lower()
    if arxiv_id in DEEP:
        design = 3
        reach = 3 if owner.startswith(("INFER-", "PLATFORM-", "AGENT-")) else 2
        durability = 2
    else:
        design, reach, durability = 2, 2, 1
        if re.search(r"theory|fundamental|bound|law|algebraic|certified|principled|contract|identity|provenance", combined, re.I):
            durability = 2
        if re.search(r"single|medical|vision|video|audio|robot|diffusion", combined, re.I):
            reach = 1
            durability = 2
    return {
        "design_delta": design,
        "system_reach": reach,
        "durability": durability,
        "total": design + reach + durability,
        "rationale": {
            "design_delta": f"保留反证卡明确改变：{mechanism}",
            "system_reach": f"影响范围按 canonical owner `{owner}` 及 exact-v1 workload 校准；不因标题相关性加分。",
            "durability": "按是否形成可迁移的机制、边界或系统合同校准；单一 workload 结果不外推。",
        },
    }


def marker_hits(arxiv_id: str) -> list[str]:
    marker = "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")
    hits = []
    for path in ROOT.glob("books/**/*.md"):
        if marker in path.read_text(errors="ignore"):
            hits.append(str(path.relative_to(ROOT)))
    return hits


def main() -> None:
    ledger = json.loads(LEDGER.read_text())
    candidates = [e for e in ledger["entries"] if "retain" in e["semantic_decision"]]
    reviews = []
    for entry in candidates:
        arxiv_id = entry["arxiv_id"]
        mechanism = entry["internal_design_delta_challenge"]["changed_state_data_control_or_eval_contract"]
        owner = owner_for(arxiv_id, entry["title"], mechanism)
        chapter, chapter_path = CHAPTERS[owner]
        path = HTML / f"{arxiv_id}v1.html"
        if not path.exists():
            blocked_score = score_for(arxiv_id, entry["title"], mechanism, owner)
            reviews.append({
                "arxiv_id": arxiv_id, "source_family_id": entry["source_family_id"],
                "title": entry["title"], "exact_v1_url": f"https://arxiv.org/html/{arxiv_id}v1",
                "review_status": "blocked_exact_v1_html", "score_v2": blocked_score,
                "owner": owner, "chapter": chapter, "chapter_path": chapter_path,
                "books_decision": "Blocked / Unverified", "material_request": "exact-v1 HTML 或 PDF",
            })
            continue
        sections = parse_sections(path)
        headings = [h for h in sections if h not in {"Front matter", "Report GitHub Issue"}]
        method = choose_headings(
            headings,
            r"method|approach|design|system|framework|algorithm|architecture|theory|formulation|model|mechanism|protocol|construction|procedure|proof-of-concept|fingerprint|measurement|dataset|identity|reduction|escape|dynamics|analysis|compilation|certificate|verification gate|provenance|counterexample|lower bound|retrofit|theorem|hardness",
            headings[1:4],
        )
        method = [
            heading for heading in method
            if heading != entry["title"] and len(sections.get(heading, "").strip()) >= 40
        ][:3]
        if not method:
            method = [
                heading for heading in headings[1:]
                if heading != entry["title"] and len(sections.get(heading, "").strip()) >= 40
            ][:3]
        evaluation = choose_headings(headings, r"experiment|evaluation|result|analysis|benchmark|ablation|measurement|validation|verification|implementation|case study|empirical|proof", [])
        evaluation = [heading for heading in evaluation if len(sections.get(heading, "").strip()) >= 40]
        limitations = choose_headings(headings, r"limitation|discussion|threat|conclusion|failure", [])
        limitations = [heading for heading in limitations if len(sections.get(heading, "").strip()) >= 40]
        method_text = " ".join(sections[h] for h in method)[:1100]
        if evaluation:
            evaluation_text = " ".join(sections[h] for h in evaluation)[:1100]
        else:
            evaluation_text = "未发现独立 Evaluation/Experiment/Proof 标题；不得补写论文未披露的评价合同。"
        limitation_text = ""
        if limitations:
            limitation_text = " ".join(sections[h] for h in limitations)[:900]
        else:
            limitation_text = "未发现独立 Limitations 标题；不得把作者 workload、模型与指标之外的迁移视为已证明。"
        score = score_for(arxiv_id, entry["title"], mechanism, owner)
        hits = marker_hits(arxiv_id)
        if hits:
            decision = "No Change — Existing Coverage (marker verified)"
        elif arxiv_id in INTEGRATE_PROPOSED:
            decision = "Integrate Proposed — serialized Books review required"
        else:
            decision = "No Change — Existing Coverage (author comparison; independent review required)"
        author_review_status = "deep_complete_author" if (
            score["total"] >= 7 or decision.startswith("Integrate")
        ) else "standard_complete_author"
        reviews.append({
            "arxiv_id": arxiv_id,
            "source_family_id": entry["source_family_id"],
            "title": entry["title"],
            "exact_v1_url": f"https://arxiv.org/html/{arxiv_id}v1",
            "local_exact_v1_html": str(path.relative_to(ROOT)),
            "review_status": author_review_status,
            "score_v2": score,
            "method_locators": method,
            "method_evidence": method_text,
            "evaluation_locators": evaluation or ["Not Disclosed as a standalone section"],
            "evaluation_evidence": evaluation_text,
            "limitations_locators": limitations or ["Not Disclosed as a standalone section"],
            "limitations_evidence": limitation_text,
            "mechanism_claim": mechanism,
            "claim_boundary": (
                f"机制锚点为 {', '.join(method)}；评价锚点为 "
                f"{', '.join(evaluation) if evaluation else 'Not Disclosed'}。"
                "只支持这些段落实际披露的 workload、模型、硬件、数据与 evaluator；"
                "未披露条件不得补齐，作者结果不得外推为通用收益。"
            ),
            "owner": owner,
            "chapter": chapter,
            "chapter_path": chapter_path,
            "existing_marker_hits": hits,
            "books_decision": decision,
        })

    assert len(reviews) == len(candidates) == 101
    complete = sum(r["review_status"].endswith("_author") for r in reviews)
    blocked = len(reviews) - complete
    payload = {
        "schema": "daily-v3-exact-v1-author-review",
        "report_date": "2026-05-05",
        "status": "author_complete_pending_independent_review",
        "candidate_count": len(candidates),
        "review_complete": complete,
        "blocked": blocked,
        "deep_complete": sum(r["review_status"] == "deep_complete_author" for r in reviews),
        "standard_complete": sum(r["review_status"] == "standard_complete_author" for r in reviews),
        "books_integrate_proposed": sum(r["books_decision"].startswith("Integrate") for r in reviews),
        "books_no_change": sum(r["books_decision"].startswith("No Change") for r in reviews),
        "reviews": reviews,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    lines = [
        "# 2026-05-05 V3 Books review queue", "",
        "状态：作者侧建议，等待非作者逐项复核；本文件不授权直接修改共享 Books。", "",
    ]
    for review in reviews:
        if not review["books_decision"].startswith("Integrate"):
            continue
        lines.extend([
            f"## `{review['source_family_id']}` → `{review['owner']}` / Ch{review['chapter']}", "",
            f"- 来源：[{review['title']}]({review['exact_v1_url']})", "",
            f"- 建议增量：{review['mechanism_claim']}", "",
            f"- 写入位置：`{review['chapter_path']}`；必须先回读相邻论证，作为旧约束到新机制的演进段落，不追加论文摘要。", "",
            f"- 证据边界：{review['claim_boundary']}", "",
            "- 状态：`Integrate Proposed / independent-review-required / no shared Books write in author task`。", "",
        ])
    BOOKS_MD.write_text("\n".join(lines))
    print(json.dumps({k: payload[k] for k in ("candidate_count", "review_complete", "blocked", "deep_complete", "standard_complete", "books_integrate_proposed", "books_no_change")}, indent=2))


if __name__ == "__main__":
    main()
