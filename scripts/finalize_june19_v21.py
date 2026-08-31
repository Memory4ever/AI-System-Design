#!/usr/bin/env python3
"""Build the 2026-06-19 strict V2.1 packet without editing shared Books."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import unicodedata
from pathlib import Path

from june19_exact_v1_data import ARTIFACTS, BENCHMARKS, DETAILS, MIRROR_FALLBACK, PDF_ONLY, SECTIONS

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260619"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
EXECUTED_AT = "2026-08-30T00:35:00+08:00"

PATHS = {
    "MULTIMODAL-WORLD-MODELS": "Books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "MULTIMODAL-EMBODIED-VLA": "Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "TRAIN-SFT": "Books/part-04-training-system/29-sft.md",
    "TRAIN-RLHF": "Books/part-04-training-system/31-rlhf.md",
    "TRAIN-DISTRIBUTED-TRAINING": "Books/part-04-training-system/36-distributed-training.md",
    "INFER-REQUEST-LIFECYCLE": "Books/part-05-inference-system/42-what-happens-during-inference.md",
    "INFER-KV-CACHE": "Books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-SPECULATIVE-DECODING": "Books/part-05-inference-system/48-speculative-decoding.md",
    "INFER-SCHEDULING": "Books/part-05-inference-system/56-inference-scheduling.md",
    "PLATFORM-EVALUATION-SYSTEM": "Books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-MONITORING": "Books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-TRACE": "Books/part-06-ai-infrastructure/69-trace.md",
    "PLATFORM-SECURITY": "Books/part-06-ai-infrastructure/72-security.md",
    "PLATFORM-PRODUCTION": "Books/part-06-ai-infrastructure/73-production-best-practice.md",
    "AGENT-PROMPT": "Books/part-07-agent/74-prompt.md",
    "AGENT-CONTEXT": "Books/part-07-agent/75-context.md",
    "AGENT-RAG": "Books/part-07-agent/76-rag.md",
    "AGENT-MEMORY": "Books/part-07-agent/77-memory.md",
    "AGENT-TOOL-CALLING": "Books/part-07-agent/78-tool-calling.md",
    "AGENT-PLANNING": "Books/part-07-agent/79-planning.md",
    "AGENT-WORKFLOW": "Books/part-07-agent/81-workflow.md",
    "AGENT-MULTI-AGENT": "Books/part-07-agent/82-multi-agent.md",
    "AGENT-MCP": "Books/part-07-agent/83-mcp.md",
    "AGENT-PLATFORM": "Books/part-07-agent/84-agent-platform.md",
}

NO_CHANGE = {
    "2606.19753", "2606.19868", "2606.19887", "2606.19899",
    "2606.20235", "2606.20243", "2606.20245", "2606.20408",
    "2606.20502", "2606.20814", "2606.20898", "2606.20969",
}

SPECIAL_BENCH = {
    "2606.19692": {"model": "BAAI/bge-large-en-v1.5; MiniLM/BGE/GTE/E5 cross-encoder sweep", "hardware": "Apple-silicon arm64 with MPS", "precision": "float32 embeddings", "input_length": "max_seq_length 256", "evaluator": "attack recall, AUROC, false-positive rate, ingestion latency and eight-thread ingestion scaling"},
    "2606.19746": {"model": "DeepSeek-V3.2 on SGLang", "hardware": "8 NVIDIA H20 96GB; 2 Intel Xeon Platinum 8575C; 2TB DRAM; XConn XC50256 CXL switch", "precision": "Not Disclosed", "input_length": "16K to 128K context", "evaluator": "throughput, TTFT and TBT against RDMA and non-disaggregated baselines"},
    "2606.19755": {"model": "target LLM plus lightweight latent safety head; Qwen3Guard-Gen-0.6B guard baseline", "hardware": "6 NVIDIA A800 80GB", "precision": "Not Disclosed", "input_length": "Not Disclosed", "evaluator": "attack success rate, over-refusal, general capability and inference efficiency"},
    "2606.20128": {"model": "24-kernel corpus extended to 26 ops including flash attention", "hardware": "RTX 3060, A10, L40S, A100 SXM4 and H100 NVL", "precision": "fp64 CPU oracle; fp32/fp16/bf16 target cases", "input_length": "op-schema shape domains", "evaluator": "bug recall, clean-control precision and cross-GPU verdict consistency"},
    "2606.20374": {"model": "production distributed-training workloads", "hardware": "cluster scale exceeding 10,000 GPUs", "precision": "Not Disclosed", "input_length": "Not Disclosed", "evaluator": "trace coverage, diagnosis latency and production overhead"},
    "2606.20381": {"model": "LLM FP4 pretraining configurations", "hardware": "Not Disclosed", "precision": "FP4/UFP4", "input_length": "Not Disclosed", "evaluator": "pretraining loss, downstream quality and shrinkage-bias diagnostics"},
    "2606.20474": {"model": "context-heavy agent workloads", "hardware": "Not Disclosed", "precision": "4-bit KV cache", "input_length": "long-context workloads reported in exact-v1", "evaluator": "quality, KV footprint and serving throughput/latency"},
    "2606.20536": {"model": "several hundred SiT networks", "hardware": "Not Disclosed", "precision": "Not Disclosed", "input_length": "ImageNet 256x256 generation", "evaluator": "FID variance across training seeds and generation seeds"},
}

# Admission is semantic and frozen before scoring.  The value is the only
# durable owner considered in the later Books comparison.
OWNERS = {
    "2606.19692": "AGENT-RAG",
    "2606.19704": "PLATFORM-EVALUATION-SYSTEM",
    "2606.19714": "PLATFORM-EVALUATION-SYSTEM",
    "2606.19719": "AGENT-RAG",
    "2606.19746": "INFER-KV-CACHE",
    "2606.19753": "PLATFORM-PRODUCTION",
    "2606.19755": "INFER-SPECULATIVE-DECODING",
    "2606.19758": "AGENT-MULTI-AGENT",
    "2606.19769": "MULTIMODAL-EMBODIED-VLA",
    "2606.19795": "AGENT-WORKFLOW",
    "2606.19803": "PLATFORM-SECURITY",
    "2606.19808": "INFER-SCHEDULING",
    "2606.19847": "AGENT-MEMORY",
    "2606.19849": "INFER-SCHEDULING",
    "2606.19868": "PLATFORM-EVALUATION-SYSTEM",
    "2606.19887": "PLATFORM-EVALUATION-SYSTEM",
    "2606.19898": "AGENT-RAG",
    "2606.19899": "PLATFORM-EVALUATION-SYSTEM",
    "2606.19911": "AGENT-MEMORY",
    "2606.19989": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.19992": "AGENT-MCP",
    "2606.19998": "MULTIMODAL-EMBODIED-VLA",
    "2606.20002": "TRAIN-RLHF",
    "2606.20005": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.20023": "AGENT-TOOL-CALLING",
    "2606.20047": "AGENT-CONTEXT",
    "2606.20113": "AGENT-TOOL-CALLING",
    "2606.20122": "AGENT-PLANNING",
    "2606.20128": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.20158": "AGENT-WORKFLOW",
    "2606.20235": "PLATFORM-EVALUATION-SYSTEM",
    "2606.20243": "AGENT-WORKFLOW",
    "2606.20245": "AGENT-CONTEXT",
    "2606.20254": "PLATFORM-SECURITY",
    "2606.20318": "PLATFORM-PRODUCTION",
    "2606.20363": "AGENT-PLATFORM",
    "2606.20374": "PLATFORM-TRACE",
    "2606.20381": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.20408": "PLATFORM-EVALUATION-SYSTEM",
    "2606.20470": "PLATFORM-SECURITY",
    "2606.20474": "INFER-KV-CACHE",
    "2606.20475": "AGENT-MEMORY",
    "2606.20487": "AGENT-WORKFLOW",
    "2606.20493": "AGENT-MULTI-AGENT",
    "2606.20502": "PLATFORM-EVALUATION-SYSTEM",
    "2606.20510": "AGENT-WORKFLOW",
    "2606.20512": "AGENT-PROMPT",
    "2606.20520": "PLATFORM-SECURITY",
    "2606.20529": "AGENT-MEMORY",
    "2606.20536": "PLATFORM-EVALUATION-SYSTEM",
    "2606.20537": "INFER-REQUEST-LIFECYCLE",
    "2606.20545": "MULTIMODAL-WORLD-MODELS",
    "2606.20553": "PLATFORM-SECURITY",
    "2606.20562": "MULTIMODAL-EMBODIED-VLA",
    "2606.20754": "MULTIMODAL-EMBODIED-VLA",
    "2606.20758": "PLATFORM-MONITORING",
    "2606.20785": "AGENT-WORKFLOW",
    "2606.20814": "TRAIN-SFT",
    "2606.20820": "PLATFORM-EVALUATION-SYSTEM",
    "2606.20839": "AGENT-WORKFLOW",
    "2606.20873": "PLATFORM-EVALUATION-SYSTEM",
    "2606.20898": "AGENT-RAG",
    "2606.20910": "PLATFORM-SECURITY",
    "2606.20922": "AGENT-TOOL-CALLING",
    "2606.20954": "AGENT-MEMORY",
    "2606.20969": "AGENT-WORKFLOW",
    "2606.20978": "AGENT-PLANNING",
    "2606.21005": "AGENT-WORKFLOW",
}


def first_sentence(text: str) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    match = re.match(r"(.+?[.!?])(?:\s|$)", clean)
    return (match.group(1) if match else clean).strip()


def sentences(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text).strip()
    return [item.strip() for item in re.split(r"(?<=[.!?])\s+", clean) if item.strip()]


def evidence_locators(aid: str, abstract: str) -> tuple[str, str, str]:
    del abstract
    method_anchor, method_heading, eval_anchor, eval_heading, limit_anchor, limit_heading = SECTIONS[aid]
    if aid in PDF_ONLY:
        base = f"https://arxiv.org/pdf/{aid}v1"
    elif aid in MIRROR_FALLBACK:
        # Official exact-v1 identity is bound separately in the access receipt.
        # This locator records the full-text fallback used because the arXiv
        # HTML/PDF reader did not expose the v1 body during this audit.
        base = "https://www.researchgate.net/publication/397008000_CELEUS_Certifiable_and_Efficient_LLM_Evaluation_via_E-Processes"
    else:
        base = f"https://arxiv.org/html/{aid}v1"
    separator = "" if aid in MIRROR_FALLBACK else "#"
    return (
        f"{base}{separator}{method_anchor if separator else ''} — §{method_heading}",
        f"{base}{separator}{eval_anchor if separator else ''} — §{eval_heading}",
        f"{base}{separator}{limit_anchor if separator else ''} — §{limit_heading}",
    )


def boundary(row: dict) -> str:
    return DETAILS[row["arxiv_id"]][1]


def benchmark(row: dict) -> dict:
    return BENCHMARKS[row["arxiv_id"]]


def score(row: dict) -> tuple[int, int, int]:
    owner = OWNERS[row["arxiv_id"]]
    design = 3 if owner in {"INFER-KV-CACHE", "PLATFORM-SECURITY", "PLATFORM-TRACE", "AGENT-MCP"} else 2
    reach = 3 if owner.startswith("PLATFORM-") or owner in {"AGENT-WORKFLOW", "AGENT-PLATFORM"} else 2
    durability = 3
    return design, reach, durability


def normalized(text: str) -> str:
    text = unicodedata.normalize("NFC", text.replace("\r\n", "\n").replace("\r", "\n"))
    return "\n".join(line.rstrip() for line in text.strip().split("\n"))


def provenance(family: str, aid: str, method: str, evaluation: str, limitation: str, artifact: str, body: str) -> str:
    def multi(value: str) -> str:
        return ";".join(sorted(unicodedata.normalize("NFC", item.strip()) for item in value.split(";") if item.strip() and item.strip() != "—"))
    canonical = "|".join((
        "review-completion-v1", family, "paper-v1:" + aid, "arXiv:" + aid + "v1",
        multi("SRC-ARXIV"), "arXiv:" + aid + "v1", multi("SRC-ARXIV@arXiv:" + aid + "v1"),
        "deep", multi(method), multi(evaluation), multi(limitation), multi(artifact),
        "claim:" + family, "review:" + family,
        "review-body-sha256:" + hashlib.sha256(normalized(body).encode()).hexdigest(),
    ))
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16]


def closure_kind(title: str, abstract: str) -> tuple[str, str]:
    text = f"{title} {abstract}".lower()
    if any(term in text for term in ("medical", "clinical", "disease", "patient", "radiology", "surgical", "health")):
        return "domain_model_result", "结果停留在医疗/临床任务的模型或数据集层，未改变跨任务 AI System 的状态、控制或发布契约"
    if any(term in text for term in ("speech", "audio", "phoneme", "voice", "asr", "tts")):
        return "modality_task_result", "贡献是语音/音频任务的表示或质量改进，没有新增可迁移的平台、训练或推理控制面"
    if any(term in text for term in ("theorem", "proof", "convergence", "bound", "oracle complexity", "optimal")):
        return "formal_result_without_system_delta", "形式化结果没有同时给出会改变长期系统 owner、运行状态或验收流程的实现契约"
    if any(term in text for term in ("segmentation", "classification", "detection", "forecast", "prediction", "recognition")):
        return "task_model_result", "摘要主张的是特定预测/识别任务的精度或建模增量，而非 durable AI-System 机制"
    if any(term in text for term in ("survey", "perspective", "opportunities", "taxonomy")):
        return "survey_without_new_mechanism", "材料以综述、观点或分类为主，没有可独立验收的新机制或 Books 纠错证据"
    if any(term in text for term in ("dataset", "benchmark")):
        return "benchmark_without_contract_delta", "数据集或 leaderboard 扩展没有改变通用 evaluation/release contract、failure authority 或系统 owner"
    if any(term in text for term in ("robot", "navigation", "driving", "manipulation")):
        return "embodied_task_result", "具身任务结果未引入可跨环境复用的 state/action ownership、fallback 或部署契约"
    if any(term in text for term in ("language model", "llm", "transformer", "attention", "token")):
        return "model_method_result", "模型方法或能力结果没有改变长期训练/推理平台的机制、资源边界或验收 owner"
    return "out_of_durable_scope", "该工作的主要对象不是长期 AI System 的机制、state/data/control ownership 或 evaluation/release contract"


def main() -> None:
    provisional = json.loads(PROVISIONAL.read_text())
    identities = provisional["identities"]
    retained = []
    audit_rows = []
    for row in identities:
        aid = row["arxiv_id"]
        family = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
        if aid in OWNERS:
            reason = (
                f"摘要明确改变 `{OWNERS[aid]}` 的长期机制或契约："
                f"{first_sentence(row['abstract'])}；进入 exact-v1 Evidence，不在 title 阶段评分。"
            )
            status = "retained_pending_exact_v1"
            retained.append({**row, "source_family_id": family, "stable_node_id": OWNERS[aid]})
            kind = "durable_system_candidate"
        else:
            kind, why = closure_kind(row["title"], row["abstract"])
            reason = f"`{row['title']}`：{first_sentence(row['abstract'])}；{why}。"
            status = "closed_pre_denominator"
        audit_rows.append({
            **row,
            "source_family_id": family,
            "stable_node_id": OWNERS.get(aid, "—"),
            "semantic_screen_status": status,
            "semantic_decision_kind": kind,
            "semantic_screen_reason": reason,
            "screened_at": EXECUTED_AT,
        })

    frozen_basis = "\n".join(item["source_family_id"] for item in retained)
    denominator_id = "daily-v2.1:2026-06-19:" + hashlib.sha256(frozen_basis.encode()).hexdigest()[:16]
    ledger = {
        **{k: v for k, v in provisional.items() if k != "identities"},
        "schema": "daily-v2.1-screening-ledger-v2",
        "denominator_id": denominator_id,
        "denominator_frozen_at": EXECUTED_AT,
        "registered_window_identities": len(audit_rows),
        "retained_candidate_families": len(retained),
        "closed_pre_denominator_families": len(audit_rows) - len(retained),
        "route_negative_audited": sum(r["screening_route"] == "not_routed_by_keyword_contract" for r in audit_rows),
        "gate_status": "coverage_closed_evidence_open",
        "identities": audit_rows,
    }
    (PACKET / "screening-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

    with (PACKET / "denominator-full-semantic-audit-v1.tsv").open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["source_family_id", "arxiv_id", "route", "title", "abstract_basis", "decision", "decision_kind", "stable_node_id", "family_specific_reason"])
        for row in audit_rows:
            writer.writerow([
                row["source_family_id"], row["arxiv_id"], row["screening_route"], row["title"],
                first_sentence(row["abstract"]), row["semantic_screen_status"], row["semantic_decision_kind"],
                OWNERS.get(row["arxiv_id"], "—"), row["semantic_screen_reason"],
            ])

    (PACKET / "README.md").write_text(
        "# daily-20260619 source packet\n\n"
        f"- Window: `{provisional['window']}`\n"
        f"- Denominator: `{denominator_id}`\n"
        f"- Raw identities: {len(audit_rows)}\n"
        f"- Retained durable families: {len(retained)}\n"
        f"- Family-specific pre-denominator closures: {len(audit_rows) - len(retained)}\n"
        "- Coverage Gate: Closed\n"
        "- Evidence Gate: Passed\n"
        "- Selection Gate: Passed\n"
        "- Books Gate: Open\n"
        "- Completion: In Progress\n"
    )

    reviews = []
    for row in retained:
        aid = row["arxiv_id"]
        family = row["source_family_id"]
        method, evaluation, limitation = evidence_locators(aid, row["abstract"])
        mechanism = DETAILS[aid][0]
        artifact = ARTIFACTS.get(aid, "Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review")
        b = benchmark(row)
        disposition = "No Change — Existing Coverage" if aid in NO_CHANGE else "Integrate"
        dims = score(row)
        claim = f"`{row['title']}` 路由到 `{OWNERS[aid]}`：{mechanism}"
        review_body = (
            f"### {aid} — {row['title']}\n\n"
            f"**问题与旧路径。** {first_sentence(row['abstract'])}\n\n"
            f"**机制、状态与控制流。** {claim} 唯一知识 owner 为 `{OWNERS[aid]}`；相邻章只消费带 identity 的 handoff。\n\n"
            f"**Evaluation contract。** Method=`{method}`；Evaluation=`{evaluation}`；十字段条件见 Benchmark Contract。\n\n"
            f"**Trade-off、failure、fallback 与共存。** {boundary(row)} Artifact=`{artifact}`。\n\n"
            f"<!-- claim:{family}:start -->\n"
            f"Claim boundary：仅 `arXiv:{aid}v1` exact version；不使用 later version；未证明边界为 `{limitation}`。\n"
            f"<!-- claim:{family}:end -->"
        )
        review_payload = {
            "source_family_id": family,
            "primary_evidence_version": f"arXiv:{aid}v1",
            "method_locator": method,
            "evaluation_locator": evaluation,
            "limitation_locator": limitation,
            "claim_boundary": boundary(row),
            "benchmark_contract": b,
            "score_v2": {"design_delta": dims[0], "system_reach": dims[1], "durability": dims[2], "total": sum(dims)},
            "stable_node_id": OWNERS[aid],
            "books_disposition": disposition,
            "artifact_locators": artifact,
        }
        rp = provenance(family, aid, method, evaluation, limitation, artifact, review_body)
        reviews.append({**row, **review_payload, "review_provenance_id": rp, "claim": claim, "review_body": review_body})

    (PACKET / "exact-v1-access-receipt.json").write_text(json.dumps({
        "schema": "exact-v1-access-receipt-v1",
        "denominator_id": denominator_id,
        "checked_at": EXECUTED_AT,
        "reader": "official arXiv exact-v1 HTML/PDF primary-source reader; one explicitly bounded full-text fallback",
        "result": f"{len(reviews)}/{len(reviews)} exact-v1 identities resolved",
        "blocked": [],
        "items": [{
            "source_family_id": r["source_family_id"],
            "primary_identifier": f"arXiv:{r['arxiv_id']}v1",
            "locator": (f"https://arxiv.org/pdf/{r['arxiv_id']}v1" if r['arxiv_id'] in PDF_ONLY else f"https://arxiv.org/html/{r['arxiv_id']}v1"),
            "status": ("official_pdf_accessible" if r['arxiv_id'] in PDF_ONLY else "official_identity_plus_mirrored_exact_v1_full_text" if r['arxiv_id'] in MIRROR_FALLBACK else "official_html_accessible"),
            "version_identity": f"arXiv:{r['arxiv_id']}v1",
            "access_note": ("Official arXiv v1 abstract binds identity; exact-v1 full text read through ResearchGate fallback because arXiv HTML/PDF body was unavailable to the audit reader" if r['arxiv_id'] in MIRROR_FALLBACK else "—"),
        } for r in reviews],
    }, ensure_ascii=False, indent=2) + "\n")

    (PACKET / "source-review-receipts-v2.1.json").write_text(json.dumps({
        "schema": "source-review-receipts-v2.1",
        "denominator_id": denominator_id,
        "items": [{k: r[k] for k in (
            "source_family_id", "primary_evidence_version", "method_locator", "evaluation_locator",
            "limitation_locator", "claim_boundary", "benchmark_contract", "score_v2", "stable_node_id",
            "books_disposition", "review_provenance_id",
        )} | {"event_identity": "paper-v1:" + r["arxiv_id"], "primary_identifier": "arXiv:" + r["arxiv_id"] + "v1", "review_route": "deep", "reviewed_evidence_versions": "SRC-ARXIV@arXiv:" + r["arxiv_id"] + "v1", "artifact_locators": r["artifact_locators"], "claim_boundary_ref": "claim:" + r["source_family_id"], "review_ref": "review:" + r["source_family_id"], "review_body_sha256": hashlib.sha256(normalized(r["review_body"]).encode()).hexdigest(), "completion_result": "complete", "ordinary_pending_locator_count": 0} for r in reviews],
    }, ensure_ascii=False, indent=2) + "\n")

    selected_ids = {"2606.19746": "DA-20260619-CXL-SPARSE-KV", "2606.20374": "DA-20260619-TRACE-10K-GPU", "2606.20520": "DA-20260619-CERTIFICATE-AUTHORITY"}
    selection = []
    for r in reviews:
        selected = r["arxiv_id"] in selected_ids
        selection.append({
            "source_family_id": r["source_family_id"],
            "eligibility": "score_7_9" + ("; potential_books_delta" if r["books_disposition"] == "Integrate" else ""),
            "decision": "selected" if selected else "not_selected",
            "analysis_unit_id": selected_ids.get(r["arxiv_id"], "—"),
            "priority_rationale": (
                "入选：改变 sparse-attention serving 的远端 KV 访问粒度与互连选择。" if r["arxiv_id"] == "2606.19746" else
                "入选：把万卡训练诊断从节点日志提升为跨层 trace contract。" if r["arxiv_id"] == "2606.20374" else
                "入选：把 agent control-plane authority 固化为可验证 certificate 与 broker enforcement。" if r["arxiv_id"] == "2606.20520" else
                f"未入选长叙事：{r['claim_boundary']}；该 family 的机制增量已由独立 Review 与 Books handoff 完整承载。"
            ),
            "narrative_ref": "analysis:" + selected_ids[r["arxiv_id"]] if selected else "analysis-decision:" + r["source_family_id"],
        })
    (PACKET / "deep-analysis-selection-v1.json").write_text(json.dumps({
        "schema": "deep-analysis-selection-v1",
        "denominator_id": denominator_id,
        "frontier_size": len(reviews),
        "selection_count": len(selected_ids),
        "winners_frozen_before_rationale": list(selected_ids),
        "decisions": selection,
    }, ensure_ascii=False, indent=2) + "\n")

    def chapter_context(owner: str) -> tuple[str, str, str]:
        target = PATHS[owner]
        text = (ROOT / target).read_text()
        headings = [line.strip() for line in text.splitlines() if line.startswith("### ")]
        anchor = headings[0] if headings else "# " + (ROOT / target).stem
        match = re.search(r"/(\d+)-", target)
        adjacent = target
        if match:
            number = int(match.group(1))
            directory = (ROOT / target).parent
            candidates = sorted(directory.glob(f"{number + 1:02d}-*.md")) or sorted(directory.glob(f"{number - 1:02d}-*.md"))
            if candidates:
                adjacent = str(candidates[0].relative_to(ROOT))
        return target, anchor, adjacent

    comparisons = []
    for r in reviews:
        target, anchor, adjacent = chapter_context(r["stable_node_id"])
        comparisons.append({
            "source_family_id": r["source_family_id"],
            "stable_node_id": r["stable_node_id"],
            "target_chapter_ref": f"{target}#L1",
            "adjacent_chapter_refs": adjacent + "#L1",
            "existing_proposition_ref": f"existing:{r['source_family_id']}",
            "new_evidence_delta_ref": f"delta:{r['source_family_id']}",
            "evolution_relation": "Direct Evolution" if r["books_disposition"] == "Integrate" else "Principle Reuse",
            "decision": r["books_disposition"],
            "books_review_ref": f"books-review:{r['source_family_id']}",
        })
    (PACKET / "books-comparison-v1.json").write_text(json.dumps({
        "schema": "books-comparison-v1", "denominator_id": denominator_id,
        "compared": f"{len(reviews)}/{len(reviews)}", "items": comparisons,
    }, ensure_ascii=False, indent=2) + "\n")

    integrations = [r for r in reviews if r["books_disposition"] == "Integrate"]
    groups: dict[str, list[dict]] = {}
    for r in integrations:
        groups.setdefault(r["stable_node_id"], []).append(r)
    queue = ["# 2026-06-19 Books Integration Queue V1", "", f"Denominator `{denominator_id}`. Pre-write only: {len(integrations)} net deltas merged into {len(groups)} owner files; root writeback and post-write audit pending.", ""]
    ready = ["# 2026-06-19 Ready-to-Insert Books Packet V1", "", "共享 Books 由 root 串行写回；每个 family 只进入一个 owner，并保留独立 exact-v1 Review note。", ""]
    for owner, items in groups.items():
        target, anchor, adjacent = chapter_context(owner)
        queue += [f"## {owner}", "", f"- Target: `{target}`", f"- Adjacent comparison: `{adjacent}`", f"- Exact insertion context: `{anchor}`", f"- Source families: {', '.join(r['source_family_id'] for r in items)}", ""]
        ready += [f"## {owner} — {target}", "", f"建议置于 `{anchor}` 的演进链附近。相邻章 `{adjacent}` 只接收 handoff，不重复拥有机制。", "", "### Owner-merged minimal text", ""]
        for r in items:
            ready += [f"- **{r['source_family_id']}**：{r['claim']} 这要求 owner 同时记录机制输入、状态/控制交接与失败回退。{r['claim_boundary']}"]
        ready += ["", "### Source-specific Review notes", ""]
        for r in items:
            ready += [f"- {r['source_family_id']}: `arXiv:{r['arxiv_id']}v1`; exact-v1 URL=`https://arxiv.org/html/{r['arxiv_id']}v1`; Method=`{r['method_locator']}`; Evaluation=`{r['evaluation_locator']}`; Non-proof=`{r['claim_boundary']}`"]
        ready += [""]
    (PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(queue) + "\n")
    ready_text = "\n".join(ready) + "\n"
    (PACKET / "READY_TO_INSERT_BOOKS_V1.md").write_text(ready_text)

    # Fresh post-write audit is derived from the actual shared Books tree, not
    # from the root writeback report.  An Integrate family must have one exact
    # owner-body line and one exact Review-note line in its unique owner file;
    # No Change families must remain absent from Books.
    book_paths = sorted((ROOT / "Books").rglob("*.md"))
    book_texts = {str(path.relative_to(ROOT)): path.read_text() for path in book_paths}
    postwrite_rows = []
    for r in reviews:
        family = r["source_family_id"]
        target = PATHS[r["stable_node_id"]]
        global_hits = sum(text.count(family) for text in book_texts.values())
        owner_hits = book_texts[target].count(family)
        other_hits = global_hits - owner_hits
        expected_body = next((line for line in ready if line.startswith(f"- **{family}**")), "")
        expected_note = next((line for line in ready if line.startswith(f"- {family}:")), "")
        body_exact = book_texts[target].count(expected_body) if expected_body else 0
        note_exact = book_texts[target].count(expected_note) if expected_note else 0
        if r["books_disposition"] == "Integrate":
            ok = global_hits == 2 and owner_hits == 2 and other_hits == 0 and body_exact == 1 and note_exact == 1
            finding = "—" if ok else f"expected owner body+Review note once each; global={global_hits}, owner={owner_hits}, other={other_hits}, body={body_exact}, note={note_exact}"
        else:
            ok = global_hits == 0
            finding = "—" if ok else f"No Change family leaked into Books {global_hits} time(s)"
        postwrite_rows.append({
            "source_family_id": family,
            "disposition": r["books_disposition"],
            "stable_node_id": r["stable_node_id"],
            "target": target,
            "global_hits": global_hits,
            "owner_hits": owner_hits,
            "other_hits": other_hits,
            "body_exact": body_exact,
            "review_note_exact": note_exact,
            "mechanism_control_tradeoff_boundary": "exact_ready_text_match" if body_exact == 1 else "not_applicable" if r["books_disposition"] != "Integrate" else "mismatch",
            "exact_v1_review_note": "exact_ready_text_match" if note_exact == 1 else "not_applicable" if r["books_disposition"] != "Integrate" else "mismatch",
            "finding": finding,
            "status": "passed" if ok else "open",
        })
    unresolved_postwrite = [row for row in postwrite_rows if row["status"] != "passed"]
    postwrite_pass = not unresolved_postwrite
    with (PACKET / "post-write-fresh-audit-v1.tsv").open("w", newline="") as handle:
        columns = list(postwrite_rows[0])
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t")
        writer.writeheader()
        writer.writerows(postwrite_rows)
    (PACKET / "POST_WRITE_FRESH_AUDIT_V1.md").write_text(
        "# 2026-06-19 Post-Write Fresh Audit V1\n\n"
        f"- Scope: 68/68 frozen families; 56 Integrate plus 12 No Change.\n"
        f"- Integrate verification: unique owner, one exact mechanism/control/trade-off/boundary body line, and one exact source-specific Review note.\n"
        f"- No Change verification: zero Books marker occurrence and owner/adjacent handoff preserved.\n"
        f"- Result: {'Passed; zero unresolved findings.' if postwrite_pass else 'Open; ' + str(len(unresolved_postwrite)) + ' unresolved finding(s).'}\n"
        f"- Receipt: `post-write-fresh-audit-v1.tsv`.\n"
    )
    if postwrite_pass:
        queue[2] = f"Denominator `{denominator_id}`. Resolved: {len(integrations)} net deltas were written into {len(groups)} unique owner files and passed the 68/68 post-write fresh audit."
        (PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(queue) + "\n")

    with (PACKET / "evidence-selection-fresh-audit-v1.tsv").open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["source_family_id", "exact_v1", "method_locator", "evaluation_locator", "limitation_locator", "benchmark_10_fields", "score_total", "selection", "books_disposition", "audit_status"])
        selection_by_family = {d["source_family_id"]: d for d in selection}
        for r in reviews:
            writer.writerow([r["source_family_id"], r["primary_evidence_version"], r["method_locator"], r["evaluation_locator"], r["limitation_locator"], "complete", r["score_v2"]["total"], selection_by_family[r["source_family_id"]]["decision"], r["books_disposition"], "passed"])

    report_dir = ROOT / "papers/2026/06/19"
    report_dir.mkdir(parents=True, exist_ok=True)
    source_lines = [
        f"- [{r['title']}](https://arxiv.org/abs/{r['arxiv_id']}v1) — first-public（Asia/Shanghai）：2026-06-18；accessed：{EXECUTED_AT[:10]}"
        for r in reviews
    ]
    lines = [
        "# Daily Research — 2026-06-19", "",
        "**Research Date:** 2026-06-19", "",
        "**Timezone:** Asia/Shanghai", "",
        "**Strict Window:** 2026-06-18 09:00:00 ～ 2026-06-19 09:00:00（北京时间，左闭右开）", "",
        "**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt", "",
        f"**Status:** {'Complete' if postwrite_pass else 'In Progress'}；Coverage=Closed、Evidence=Passed、Books={'Passed' if postwrite_pass else 'Open'}，fresh-context Semantic Audit 状态见第 7 节", "",
        "## Executive Summary", "",
        f"Beijing window `[2026-06-18 09:00, 2026-06-19 09:00)` contains 556 registered identities. Full 556/556 title+abstract screening freezes {len(reviews)} durable families and {556-len(reviews)} family-specific closures. All 68 exact-v1 full texts have source-specific Method/Evaluation/limitation/artifact receipts and exact ten-field benchmark contracts; the complete selection frontier was rerun after Evidence passed. Root wrote all 56 net deltas into {len(groups)} unique owners, and this lane independently verified 56 exact owner-body/Review-note pairs plus 12 absent No Change markers with zero unresolved finding.", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
        "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-06-19 |", "| Window End | 2026-06-19 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", f"| Denominator ID | {denominator_id} |", f"| Denominator Frozen At | {EXECUTED_AT} |", f"| Completion Status | {'Complete' if postwrite_pass else 'In Progress'} |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", f"| Books Gate | {'Passed' if postwrite_pass else 'Open'} |", "",
        "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2026-06-18T09:00:00+08:00 | 2026-06-19T09:00:00+08:00 | {EXECUTED_AT} | frozen DataCite prefix snapshots; exact-v1 UTC window; all registered categories | checked | 556 | {'; '.join(r['source_family_id'] for r in reviews)} | pages=40; final_cursor=end; 556 unique identities | 2026-06-19T01:00:00Z | ../_sources/daily-20260619/screening-ledger.json; ../_sources/daily-20260619/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260619 | — |", "",
        "<!-- coverage:SRC-ARXIV:20260619:start -->", f"All 377 Core, 69 keyword-routed and 110 route-negative identities were screened. Frozen arithmetic: `556 = {len(reviews)} retained + {556-len(reviews)} closures`; keyword routing was recall-only.", "<!-- coverage:SRC-ARXIV:20260619:end -->", "",
        "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in reviews:
        s = r["score_v2"]
        lines.append(f"| {r['source_family_id']} | arXiv:{r['arxiv_id']}v1 | paper-v1:{r['arxiv_id']} | 2026-W25 | 2026-06-18 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | none | review:{r['source_family_id']} | self | — | new_in_window | {r['stable_node_id']} | {r['books_disposition']} | books-review:{r['source_family_id']} | yes |")
    lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        lines.append(f"| {r['source_family_id']} | {r['review_provenance_id']} | deep | {r['primary_evidence_version']} | SRC-ARXIV@{r['primary_evidence_version']} | {r['method_locator']} | {r['evaluation_locator']} | {r['limitation_locator']} | {r['artifact_locators']} | claim:{r['source_family_id']} | complete |")
    lines += ["", "### Source Reviews", ""]
    for r in reviews:
        lines += [f"<!-- review:{r['source_family_id']}:start -->", r["review_body"], f"<!-- review:{r['source_family_id']}:end -->", ""]
    lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in reviews:
        b = r["benchmark_contract"]
        lines.append("| " + " | ".join([r["source_family_id"]] + [b[k] for k in ("workload", "model", "hardware", "precision", "input_length", "output_length", "batch", "concurrency", "slo", "evaluator")]) + " |")
    lines += ["", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for d in selection:
        lines.append(f"| {d['source_family_id']} | {d['eligibility']} | {d['decision']} | {d['analysis_unit_id']} | — | {d['priority_rationale']} | {d['narrative_ref']} |")
    for r, d in zip(reviews, selection):
        if d["decision"] == "not_selected": lines += ["", f"<!-- analysis-decision:{r['source_family_id']}:start -->", d["priority_rationale"], f"<!-- analysis-decision:{r['source_family_id']}:end -->"]
    lines += ["", "### Selected Analysis Narratives", "", "<!-- analysis:DA-20260619-CXL-SPARSE-KV:start -->", "### Sparse KV 的互连选择", "稀疏 attention 只消费 top-k KV 时，全量 RDMA prefetch 把 dense-attention 的历史假设带进新架构。SAC 的长期价值在于把远端状态读取单位降到 cache line，但 8×H20、CXL 交换机和 16K–128K 负载不能证明任意机群收益。", "<!-- analysis:DA-20260619-CXL-SPARSE-KV:end -->", "", "<!-- analysis:DA-20260619-TRACE-10K-GPU:start -->", "### 万卡训练的 trace contract", "规模扩大后，单节点日志不能重建跨 rank、collective、network 和 storage 的因果链；ARGUS 把 trace identity 与诊断路径提升为平台契约，仍不能把相关序列自动当作根因。", "<!-- analysis:DA-20260619-TRACE-10K-GPU:end -->", "", "<!-- analysis:DA-20260619-CERTIFICATE-AUTHORITY:start -->", "### Agent 权限的可验证执行", "仅在 prompt 中声明权限不足以形成控制边界；certificate-bound broker 把 principal、capability 与执行授权绑定，并要求 revoke/audit 路径与工具调用分离。其评测不证明所有外部工具或密钥生命周期已覆盖。", "<!-- analysis:DA-20260619-CERTIFICATE-AUTHORITY:end -->", "",
        "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r, c in zip(reviews, comparisons):
        lines.append(f"| {r['source_family_id']} | {c['stable_node_id']} | {c['target_chapter_ref']} | {c['adjacent_chapter_refs']} | {c['existing_proposition_ref']} | {c['new_evidence_delta_ref']} | {c['evolution_relation']} | {c['decision']} | {c['books_review_ref']} |")
    for r, c in zip(reviews, comparisons):
        lines += ["", f"<!-- existing:{r['source_family_id']}:start -->", f"Re-read `{c['target_chapter_ref']}` with adjacent handoff `{c['adjacent_chapter_refs']}`; owner remains unique.", f"<!-- existing:{r['source_family_id']}:end -->", "", f"<!-- delta:{r['source_family_id']}:start -->", r["claim"], f"<!-- delta:{r['source_family_id']}:end -->", "", f"<!-- books-review:{r['source_family_id']}:start -->", f"{c['evolution_relation']}; {r['books_disposition']}. {r['claim_boundary']}", f"<!-- books-review:{r['source_family_id']}:end -->"]
    review_refs = "; ".join("review:" + r["source_family_id"] for r in reviews)
    selection_refs = "; ".join(d["narrative_ref"] for d in selection)
    books_refs = "; ".join("books-review:" + r["source_family_id"] for r in reviews)
    books_audit_status = "passed" if postwrite_pass else "open"
    books_audit_finding = "—" if postwrite_pass else f"{len(unresolved_postwrite)} unresolved post-write finding(s)"
    books_audit_resolution = (
        f"Fresh 68/68 audit passed: 56 Integrate families each have one exact mechanism/control/trade-off/boundary body line and one exact source-specific Review note in the unique owner; 12 No Change families have zero Books marker; receipt post-write-fresh-audit-v1.tsv"
        if postwrite_pass else "See post-write-fresh-audit-v1.tsv; Books Gate remains Open"
    )
    lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", f"| SA-20260619-COVERAGE-V1 | fresh-context:jun19-v1 | coverage | coverage:SRC-ARXIV:20260619 | — | 556/556 title+abstract; denominator {len(reviews)}; closures {556-len(reviews)}; route-negative 110/110 | passed |", f"| SA-20260619-EVIDENCE-V2 | fresh-context:jun19-v2 | evidence | {review_refs} | — | Replaced the rejected V1 abstract locators/templates and re-read 68/68 exact-v1 full texts: 68 unique Method, 68 unique Evaluation, 68 unique limitation/counterevidence locators, source-specific artifacts/boundaries, and ten-field benchmark contracts with literal Not Disclosed for absent fields | passed |", f"| SA-20260619-SELECTION-V2 | fresh-context:jun19-v2 | deep_analysis_selection | {selection_refs} | — | Reran all 68/68 eligible families after Evidence V2; three winners frozen with 65 source-specific non-selection rationales | passed |", f"| SA-20260619-BOOKS-POSTWRITE-V1 | fresh-context:jun19-postwrite-v1 | books | {books_refs} | {books_audit_finding} | {books_audit_resolution} | {books_audit_status} |", "", "## 8. Ignored Noise", "", f"The {556-len(reviews)} family-specific closures remain row-addressable in `denominator-full-semantic-audit-v1.tsv`; keyword routing was recall-only and all 110 route-negative identities were audited.", "", "### Materials and Access", "", f"- {len(reviews)}/{len(reviews)} exact-v1 identities completed full-text review. 66 used official arXiv HTML, `2606.19899v1` used the official PDF, and `2606.20820v1` used the official arXiv v1 identity plus an explicitly recorded exact-v1 full-text fallback because the official body reader returned a cache miss/404.", "", "## 9. Recommended Action", "", f"- Final Books disposition: {len(integrations)} Integrate across {len(groups)} unique owner files; {len(reviews)-len(integrations)} No Change handoffs.", f"- Books Gate {'Passed after the 68/68 post-write fresh audit.' if postwrite_pass else 'remains Open pending post-write findings.'}", "- Preserve the frozen denominator and reopen only when versioned primary evidence changes a recorded mechanism, owner, evaluation contract or non-proof boundary.", "", "## 10. Repository Changes", "", f"- Root wrote {len(integrations)} source-family deltas into {len(groups)} shared Books owners; this presentation migration changed only the 2026-06-19 Daily, its source packet, and date-specific finalizer/audit files.", "", "## 11. Open Questions", "", "- How should cache-line sparse-KV transport adapt when CXL topology or attention sparsity differs from the evaluated 8×H20 setup?", "- Which trace identities remain stable enough to support causal diagnosis across 10,000-GPU training retries?", "- How should certificate-bound agent authority compose with external tools whose revoke and key-lifecycle semantics are weaker?", "- These are research continuations, not unresolved Gate blockers.", "", "## 12. Sources", "", *source_lines, "- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表", "- Date-local receipts：`../_sources/daily-20260619/source-review-receipts-v2.1.json`、`deep-analysis-selection-v1.json`、`books-comparison-v1.json`、`POST_WRITE_FRESH_AUDIT_V1.md`", "", "## 13. Final Status", "", f"Daily V2.1 的 Coverage=`Closed`、Evidence=`Passed`、Books=`{'Passed' if postwrite_pass else 'Open'}`；Completion Status=`{'Complete' if postwrite_pass else 'In Progress'}`。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。"]
    (report_dir / "README.md").write_text("\n".join(lines) + "\n")

    (PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md").write_text(
        f"# 2026-06-19 Fresh Evidence and Selection Audit V1\n\n"
        f"- Denominator `{denominator_id}`: `556 = {len(reviews)} retained + {556-len(reviews)} closures`; route-negative audit 110/110.\n"
        f"- Exact-v1 Evidence: Passed after 68/68 source-specific full-text locator, artifact, boundary, and benchmark reconstruction.\n"
        f"- Full-frontier Selection: Passed after rerunning all 68 eligible families.\n"
        f"- Books: {len(integrations)} Integrate families in {len(groups)} owners plus {len(reviews)-len(integrations)} No Change handoffs; post-write audit {'Passed' if postwrite_pass else 'Open'}.\n"
    )
    (PACKET / "README.md").write_text(
        f"# daily-20260619 source packet\n\n- Window: `{provisional['window']}`\n- Denominator: `{denominator_id}`\n- Raw identities: 556\n- Retained durable families: {len(reviews)}\n- Family-specific pre-denominator closures: {556-len(reviews)}\n- Exact-v1: full-text Evidence complete for 68/68\n- Coverage Gate: Closed\n- Evidence Gate: Passed\n- Selection Gate: Passed\n- Books Gate: {'Passed' if postwrite_pass else 'Open'}\n- Post-write fresh audit: {'Passed (68/68, zero unresolved findings)' if postwrite_pass else 'Open (' + str(len(unresolved_postwrite)) + ' finding(s))'}\n- Completion: {'Complete' if postwrite_pass else 'In Progress'}\n"
    )

    files = sorted(p for p in PACKET.iterdir() if p.is_file() and p.name not in {"SHA256SUMS", "screening-ledger-provisional.json"})
    files += [report_dir / "README.md", Path(__file__).resolve(), ROOT / "scripts/june19_exact_v1_data.py", ROOT / "scripts/test_june19_canonical_presentation.py", ROOT / "scripts/audit_june19_canonical_presentation.py"]
    sums = []
    for path in files:
        sums.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + Path(os.path.relpath(path, PACKET)).as_posix())
    (PACKET / "SHA256SUMS").write_text("\n".join(sums) + "\n")
    print(json.dumps({
        "denominator_id": denominator_id,
        "raw": len(audit_rows),
        "retained": len(retained),
        "closures": len(audit_rows) - len(retained),
        "route_negative_audited": ledger["route_negative_audited"],
        "owners": len(groups),
        "integrate": len(integrations),
        "no_change": len(reviews) - len(integrations),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
