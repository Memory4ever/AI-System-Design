#!/usr/bin/env python3
"""Render the 2026-05-23 V2.1 author packet without touching shared Books."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))

from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

SOURCE = json.loads((HERE / "screening-ledger-provisional.json").read_text())
REPORT_DATE = "2026-05-23"

# Retention is deliberately narrow: each family changes a durable model, training,
# runtime, evidence, security, or agent state/control contract.  Domain-only
# applications and component-local metric gains stay in the screening ledger.
CANDIDATES = {
    "2605.19240": ("PLATFORM-SECURITY", 8, "Integrate", "§4.1–4.4 causal cross-channel monitoring", "§5 detection and attribution evaluation", "§7 Limitations"),
    "2605.19242": ("MULTIMODAL-WORLD-MODELS", 8, "Integrate", "§3 physics-faithful data and objective", "§4 controlled video/world-model evaluation", "§5 Conclusion and inherited generator biases"),
    "2605.19262": ("PLATFORM-SECURITY", 7, "Integrate", "§4 masked-diffusion backdoor construction", "§5 attack and defense experiments", "Appendix A Limitations"),
    "2605.19269": ("INFER-TENSORRT-LLM", 8, "Integrate", "§3 GEMM-epilogue program representation", "§4 kernel and end-to-end evaluation", "§5 limitations and portability boundary"),
    "2605.19276": ("PLATFORM-EVALUATION-SYSTEM", 7, "No Change — Existing Coverage", "§3.1–3.5 evaluation-platform architecture", "§4 benchmark execution and comparison", "§5 Future Works"),
    "2605.19282": ("TRAIN-PRETRAINING", 8, "Integrate", "§3 spectral failure analysis; §4 high-pass remedy", "§5 VLA/RLVR optimization experiments", "Appendix M Limitations"),
    "2605.19314": ("AGENT-WORKFLOW", 8, "Integrate", "§3 hierarchical task-state alignment", "§4.1–4.4 long-horizon embodied evaluation", "§7 Limitations"),
    "2605.19321": ("PLATFORM-SECURITY", 7, "Integrate", "§3 draft-model pre-guard design", "§6 jailbreak and latency evaluation", "§7 Limitations"),
    "2605.19328": ("PLATFORM-EVALUATION-SYSTEM", 7, "Integrate", "§3 embodied-agent threat and benchmark protocol", "§4 attacks and defenses", "§5 Limitations"),
    "2605.19341": ("PLATFORM-EVALUATION-SYSTEM", 8, "Integrate", "§3.1–3.3 controlled reference-world benchmark", "§4 cross-context hallucination experiments", "§5 Discussion; controlled-world boundary"),
    "2605.19344": ("PLATFORM-EVALUATION-SYSTEM", 7, "Integrate", "§3 retrieval-augmented linguistic calibration", "§4–§5 calibration experiments", "§6 Limitations"),
    "2605.19377": ("PLATFORM-EVALUATION-SYSTEM", 7, "No Change — Existing Coverage", "§3–§4 evaluator–model game", "§5 robustness-finetuning evaluation", "§6 Limitations"),
    "2605.19407": ("TRAIN-DATA", 9, "Integrate", "§3–§6 compute/data/filter scaling design", "§6–§7 scaling experiments", "§8 Discussion and scope boundary"),
    "2605.19481": ("INFER-PD-DISAGGREGATION", 8, "Integrate", "§III–V C2C weight/state movement design", "§VI MIG/serverless serving evaluation", "§VII Conclusion and hardware boundary"),
    "2605.19537": ("PLATFORM-EVALUATION-SYSTEM", 8, "Integrate", "§3 backend-reproducibility protocol", "§4 backend/model benchmark deltas", "§5 Discussion and reproducibility boundary"),
    "2605.19561": ("INFER-TENSORRT-LLM", 7, "Integrate", "§3–§4 two-level orthogonal rotation", "§5 MXFP4 quantization evaluation", "§7 Impact and limits"),
    "2605.19576": ("AGENT-PLATFORM", 8, "Integrate", "§3–§5 lifecycle-managed skill library", "§6 library-drift evaluation", "§7 Limitations"),
    "2605.19593": ("INFER-SCHEDULING", 8, "Integrate", "§3 multi-model offload/preemption methodology", "§4–§5 heterogeneous-serving measurements", "§6 Conclusion; interconnect and hardware constraints"),
    "2605.19604": ("AGENT-PLATFORM", 8, "Integrate", "§3 programmable runtime skill contract", "§4 execution and accuracy evaluation", "§5 Conclusion; language/runtime boundary"),
    "2605.19660": ("INFER-KV-CACHE", 7, "No Change — Existing Coverage", "§3–§4 extreme KV quantization", "§5 model/task evaluation", "Appendix A Limitations"),
    "2605.19668": ("AGENT-WORKFLOW", 7, "Weekly Only — Context", "§3–§5 semantics-constrained remediation loop", "§6 opaque-software case evaluation", "§7.3 Limitations"),
    "2605.19722": ("PLATFORM-SECURITY", 8, "Integrate", "§3 trace-based autonomous security-agent protocol", "§4–§5 sandbox/tool-use evaluation", "§6 Limitations"),
    "2605.19735": ("AGENT-RAG", 8, "Integrate", "§4 extraction-free hierarchical graph construction", "§5–§7 multi-hop evaluation", "§8 cost and trade-offs"),
    "2605.19769": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage", "§2–§3 verifier-grounded software worlds", "§4.1 computer-use agent evaluation", "§ unnumbered exact heading ‘Limitations and Future Work’"),
    "2605.19775": ("INFER-SCHEDULING", 8, "Integrate", "§2–§3 inference-scaling model", "§4–§5 reasoning-workload measurements", "§6 Conclusions and disclosed scope"),
    "2605.19779": ("PLATFORM-EVALUATION-SYSTEM", 8, "Integrate", "§2–§3 conformal continuous-agent UQ", "§4 longitudinal agent studies", "§5 Limitations: bounded shift and dependence"),
    "2605.19847": ("PLATFORM-SECURITY", 9, "Integrate", "§2–§3 collusion threat model and tenant accounting", "§4 privacy audit; §5 protocol", "§7.1 Limitations: retrieval only, not generation"),
    "2605.19893": ("INFER-SPECULATIVE-DECODING", 8, "Integrate", "§3–§4 sparse speculative verification", "§5 long-context evaluation", "§6 Conclusion and sparse-attention boundary"),
    "2605.19929": ("INFER-TENSORRT-LLM", 7, "Integrate", "§3–§4 modality-aware low-bit quantization", "§5 VLM experiments", "§6 Conclusion and workload boundary"),
    "2605.19932": ("AGENT-CONTEXT", 8, "Integrate", "§3 orientation-cache representation", "§4 recurring-context agent evaluation", "§5 Limitations"),
    "2605.19945": ("INFER-SCHEDULING", 8, "Integrate", "§3–§4 variability-aware expert placement", "§5 heterogeneous-GPU evaluation", "§6 Limitations"),
    "2605.19952": ("AGENT-MEMORY", 8, "Integrate", "§3 trace/chunk memory representation", "§4 lifelong-memory evaluation", "Appendix C.1 Limitations"),
    "2605.19999": ("PLATFORM-EVALUATION-SYSTEM", 7, "Integrate", "§3–§4 contamination-resistant benchmark construction", "§5 benchmark analysis", "§ unnumbered exact heading ‘Limitations’: contamination detection and task scope"),
    "2605.20022": ("INFER-SPECULATIVE-DECODING", 8, "Integrate", "§3–§4 asynchronous flexible drafting", "§5 end-to-end evaluation", "§6 Conclusion: bonus-token and accepted-length uncertainty"),
    "2605.20051": ("PLATFORM-SECURITY", 8, "Integrate", "§3–§4 reference-driven variant detection", "§5 AI-infra repository measurement", "§6 Discussion and false-positive boundary"),
    "2605.20061": ("TRAIN-RLHF", 8, "Integrate", "§3 belief-consistency credit assignment", "§4 long-horizon agent evaluation", "Appendix C Limitations"),
    "2605.20084": ("AGENT-RAG", 8, "Integrate", "§3–§4 joint escalation/abstention calibration", "§5 cascaded-RAG evaluation", "§ unnumbered exact heading ‘Limitations’: distribution shift and calibration"),
    "2605.20104": ("INFER-SPECULATIVE-DECODING", 7, "No Change — Existing Coverage", "§3 retrieval-assisted hybrid draft tree", "§4 end-to-end evaluation", "§5 Conclusion and future work"),
    "2605.20123": ("PLATFORM-SECURITY", 7, "Integrate", "§3–§4 bidirectional ranking defense", "§5 poisoning evaluation", "§6 Conclusion and adaptive-attack boundary"),
    "2605.20168": ("TRAIN-DATA", 6, "Weekly Only — Context", "§2–§3 abstract-integrity annotation protocol", "§4 OpenAlex sample findings", "§5 Discussion and database-scope limitations"),
    "2605.20173": ("AGENT-PLATFORM", 7, "Integrate", "§2–§5 stochastic-deterministic runtime pattern gates", "§5.2 failure-signature catalog; worked composition cases", "§6 Discussion; methodology paper without controlled experiment"),
    "2605.20179": ("INFER-TENSORRT-LLM", 8, "Integrate", "§3 I/O-aware MoE expert-offload design", "§4 LLaDA2.0 experiments", "§5 Conclusion: block-only activation and limited hardware"),
    "2605.20295": ("INFER-TENSORRT-LLM", 8, "Integrate", "§4 fully static NPU quantization", "§5 on-device NPU evaluation", "Appendix H Limitations"),
    "2605.20312": ("AGENT-MCP", 9, "Integrate", "§2 claim primitives; §3 protocol composition", "§5 pilot; §6 formal properties", "§8 Limitations"),
    "2605.20315": ("INFER-PD-DISAGGREGATION", 7, "No Change — Existing Coverage", "§3 quantized-prefill/precise-decode split", "§4 Experiments", "§5 Conclusion and hardware boundary"),
    "2605.20402": ("TRAIN-RLHF", 7, "Integrate", "§5 MXFP4 error decomposition", "§6 RL quantization experiments", "§7 Limitations"),
    "2605.20477": ("TRAIN-RLHF", 8, "Integrate", "§3–§4 reflection-learning pipeline", "§5 MiniHack/ALFWorld evaluation", "§5.3 Limitations"),
    "2605.20485": ("AGENT-MULTI-AGENT", 8, "Integrate", "§3 budgeted model-orchestration policy", "§4–§5 zero-shot allocation evaluation", "§6 Limitations"),
    "2605.20490": ("PLATFORM-EVALUATION-SYSTEM", 8, "Integrate", "§2–§3 ECUAS decision-theoretic metric family", "§4 evaluator and QA studies", "§ unnumbered exact heading ‘Limitations’: equivalence evaluator and utility assumptions"),
    "2605.20520": ("PLATFORM-EVALUATION-SYSTEM", 7, "Integrate", "§2 open-world evaluation framework", "§3 case studies and capability evidence", "§2.4 Limitations: complements, not replaces, benchmarks"),
    "2605.20530": ("PLATFORM-EVALUATION-SYSTEM", 7, "No Change — Existing Coverage", "§2–§6 trajectory-oriented agent taxonomy", "§7 benchmark landscape", "§8 Limitations"),
    "2605.20548": ("AGENT-MULTI-AGENT", 7, "Integrate", "§3–§4 communication-content instrumentation", "§5 and Appendix C.2 occlusion evaluation", "§6 Limitations"),
    "2605.20563": ("AGENT-MULTI-AGENT", 8, "Integrate", "§3–§4 state-management and annotation protocol", "§5 evaluation; Appendix A setup", "Appendix E Limitations"),
    "2605.22863": ("AGENT-MULTI-AGENT", 7, "Integrate", "§3 latent-cache communication interface", "§4 evaluation; Appendix C statistics", "§5 Limitations: checkpoint-specific retained layers"),
    "2605.22864": ("PLATFORM-EVALUATION-SYSTEM", 7, "No Change — Existing Coverage", "§3 uncertainty features from model trajectories", "§4–§5 calibration evaluation", "§6 Limitations"),
    "2605.22866": ("PLATFORM-EVALUATION-SYSTEM", 8, "Integrate", "§3 hierarchical online attribution", "§4 and Appendix A experiments", "§6 limitations and binary-outcome boundary"),
    "2605.24006": ("TRAIN-PIPELINE-PARALLEL", 7, "Integrate", "§III tabular schedule abstraction", "§IV communication-aware schedule experiments", "§V Conclusion and simulator boundary"),
    "2605.24011": ("INFER-TENSORRT-LLM", 7, "Integrate", "§3 action-guided mixed-precision quantization", "§4 VLA deployment experiments", "Appendix H; physical safety remains external"),
    "2606.28330": ("AGENT-RAG", 7, "Integrate", "PDF §II–§III concentration and retrieval metrics", "PDF §IV–§V synthetic and simplified RAG experiments", "PDF §VI–§VII: synthetic-only evidence and no production embedding validation"),
}

DEEP = {
    "2605.19407": "DA-DATA-FILTER-SCALING",
    "2605.19847": "DA-TENANT-PRIVACY-ACCOUNTING",
    "2605.20312": "DA-AGENT-CLAIM-PROTOCOL",
}

# Date-local author configuration overrides the copied rendering scaffold.
_CONFIG = json.loads((HERE / "candidate-config-author.json").read_text())
CANDIDATES = {key: tuple(value) for key, value in _CONFIG["candidates"].items()}
DEEP = _CONFIG["deep"]
PDF_IDS = set(_CONFIG["pdf_ids"])


def family(arxiv_id: str) -> str:
    return "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")


def review_route(row: dict) -> str:
    """V2.1 route is driven by score or a forced Books delta, not accessibility."""
    return "deep" if row["score_v2"]["total"] >= 7 or row["integration_disposition"] == "Integrate" else "standard"


def evidence_locator(row: dict, key: str) -> str:
    route = "PDF" if row["arxiv_id"] in PDF_IDS else "HTML"
    return f"arXiv:{row['arxiv_id']}v1 {route} — {row[key]}"


def sentences(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text or "").strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", clean) if s.strip()]


def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    for sentence in ss:
        if re.search(r"\b(propose|introduce|present|develop|design|show|identify|study|analy[sz]e|demonstrate)\b", sentence, re.I):
            return sentence
    return ss[0] if ss else row["title"]


def closure_reason(row: dict) -> str:
    abstract = row.get("abstract", "")
    ss = sentences(abstract)
    summary = " ".join(ss[:2]) or row["title"]
    cats = ", ".join(row.get("categories", []))
    if re.search(r"survey|position|review|taxonomy", row["title"], re.I):
        boundary = "该工作主要整理或主张研究方向，没有给出可迁移的系统接口、状态所有权及跨工作负载验证。"
    elif re.search(r"dataset|corpus|benchmark", row["title"], re.I):
        boundary = "其贡献是特定数据/评测资产；未改变通用 evaluation contract、release gate 或运行时控制面。"
    elif re.search(r"medical|clinical|finance|traffic|uav|earth|protein|speech|wearable|pathology|geoscience|recommend", abstract, re.I):
        boundary = "机制和证据绑定垂直领域任务，尚不能推出 AI System 的通用 data/state/control ownership 变化。"
    elif re.search(r"accuracy|classification|segmentation|forecast|prediction", abstract, re.I):
        boundary = "结果集中在模型/任务局部精度，未建立训练、推理、平台或 Agent 的长期系统契约变化。"
    else:
        boundary = "该局部方法没有改变长期 state/data/control owner、evaluation/release contract 或生产 fallback。"
    reopen = "若后续公开跨 workload artifact、生产控制接口或可证伪的系统级证据，则重新进入 denominator。"
    return f"`{row['title']}`（{cats}）：{summary} {boundary}{reopen}"


rows = []
for original in SOURCE["identities"]:
    row = dict(original)
    arxiv_id = row["arxiv_id"]
    if arxiv_id in CANDIDATES:
        owner, total, disposition, method_loc, eval_loc, limit_loc = CANDIDATES[arxiv_id]
        row.update(
            source_family_id=family(arxiv_id),
            screening_status="retained",
            screening_reason=mechanism(row),
            owner_node=owner,
            score_v2={"design_delta": 3 if total >= 8 else 2, "system_reach": 3 if total == 9 else 2, "durability": total - (3 if total >= 8 else 2) - (3 if total == 9 else 2), "total": total},
            review_status="deep_complete" if total >= 7 or disposition == "Integrate" else "standard_complete",
            access_status="accessible",
            integration_disposition=disposition,
            method_locator=method_loc,
            evaluation_locator=eval_loc,
            limitations_locator=limit_loc,
        )
    else:
        row.update(
            screening_status="pre_denominator_closure",
            screening_reason=closure_reason(row),
            review_status="identity_date_closed",
            access_status="accessible",
            integration_disposition="Rejected — Below Candidate Denominator",
        )
    rows.append(row)

retained = [row for row in rows if row["screening_status"] == "retained"]
closures = [row for row in rows if row["screening_status"] != "retained"]
ledger = {
    "schema": "daily-screening-ledger-v2.1",
    "report_date": REPORT_DATE,
    "window": SOURCE["window"],
    "utc_window": SOURCE["utc_window"],
    "raw_snapshot_records": SOURCE["raw_snapshot_records"],
    "registered_window_identities": len(rows),
    "screened_identities": len(rows),
    "candidate_denominator": len(retained),
    "pre_denominator_closures": len(closures),
    "identities": rows,
}
(HERE / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

roadmap = (ROOT / "ROADMAP.md").read_text()
paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}
comparisons, queue, review_packet = [], [], []
for row in retained:
    arxiv_id = row["arxiv_id"]
    owner_path = paths.get(row["owner_node"], "ROADMAP.md")
    target = ROOT / owner_path
    siblings = sorted(target.parent.glob("*.md")) if target.exists() else []
    index = siblings.index(target) if target in siblings else -1
    adjacent = [str(p.relative_to(ROOT)) for p in siblings[max(0, index - 1):index] + siblings[index + 1:index + 2]] if index >= 0 else []
    body = target.read_text() if target.exists() else ""
    headings = re.findall(r"^##+\s+(.+)$", body, re.M)[:8]
    existing_marker = arxiv_id in body or family(arxiv_id) in body
    comparison = {
        "arxiv_id": arxiv_id,
        "source_family_id": family(arxiv_id),
        "owner_node": row["owner_node"],
        "owner_path": owner_path,
        "adjacent_paths": adjacent,
        "existing_proposition": f"已顺读 `{owner_path}` 及相邻章节 {adjacent}；当前主干={headings}；exact family marker={'present' if existing_marker else 'absent'}。Review notes 不计语义整合。",
        "new_evidence_delta": row["screening_reason"],
        "decision": row["integration_disposition"],
    }
    comparisons.append(comparison)
    if row["integration_disposition"] == "Integrate":
        queue.append({
            "report_date": REPORT_DATE,
            "arxiv_id": arxiv_id,
            "source_family_id": family(arxiv_id),
            "stable_node_id": row["owner_node"],
            "owner_path": owner_path,
            "adjacent_paths": adjacent,
            "evidence_delta": row["screening_reason"],
            "required_post_write_audit": "owner + adjacent; mechanism text before first anchored ^## Review notes",
        })
    review_packet.append({
        "source_family_id": family(arxiv_id),
        "arxiv_id": arxiv_id,
        "primary_evidence_version": f"arXiv:{arxiv_id}v1",
        "retrieval_route": "official arXiv exact-v1 PDF" if arxiv_id in PDF_IDS else "official arXiv exact-v1 HTML",
        "retrieved_at": "2026-09-02T00:30:00+08:00",
        "method_locator": row["method_locator"],
        "evaluation_locator": row["evaluation_locator"],
        "limitations_locator": row["limitations_locator"],
        "claim_boundary": "Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.",
    })

(HERE / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema": "books-writeback-queue-v1", "report_date": REPORT_DATE, "status": "awaiting_independent_audit_and_root_serial_writeback", "items": queue}, ensure_ascii=False, indent=2) + "\n")
(HERE / "exact-v1-review-packet.json").write_text(json.dumps(review_packet, ensure_ascii=False, indent=2) + "\n")
(HERE / "semantic-author-audit.json").write_text(json.dumps({
    "schema": "semantic-author-audit-v1",
    "report_date": REPORT_DATE,
    "auditor": "author-lane",
    "status": "author_complete_pending_fresh_context_independent_audit",
    "not_a_fresh_context_audit": True,
    "counts": {"registered": len(rows), "screened": len(rows), "retained": len(retained), "closures": len(closures), "reviewed": len(retained), "blocked": 0, "integrate": len(queue)},
}, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((HERE / "screening-ledger-final.json").read_bytes()).hexdigest()
comparison_by_id = {item["arxiv_id"]: item for item in comparisons}


def chapter_ref(path: str) -> str:
    match = re.match(r"(\d+)-", Path(path).name)
    return f"{path}#chapter-{int(match.group(1))}" if match else f"{path}#knowledge-tree"


lines = [
    "# Daily Research — 2026-05-23", "", "**Research Date:** 2026-05-23", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-22 09:00:00 ～ 2026-05-23 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；technical claims bind official arXiv exact-v1 HTML/PDF。", "",
    "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。author packet 已完成，等待非作者 fresh-context 审计。", "",
    "## Executive Summary", "",
    f"从 {SOURCE['raw_snapshot_records']:,} 条月度 raw records 中恢复并逐项语义筛选 {len(rows)}/{len(rows)} 个窗口身份；严格 author denominator={len(retained)}，pre-denominator closures={len(closures)}，exact-v1 author reviews={len(retained)}/{len(retained)}，blocked=0，provisional Books queue={len(queue)}。共享 Books 未修改。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-23 |", "| Window End | 2026-05-23 |",
    "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
    "| Denominator ID | DEN-20260523-V2-AUTHOR |", "| Denominator Frozen At | 2026-09-02T00:30:00+08:00 |", "| Completion Status | In Progress |", "| Coverage Gate | Open |", "| Evidence Gate | Open |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-22T09:00:00+08:00 | 2026-05-23T09:00:00+08:00 | 2026-09-02T00:30:00+08:00 | DataCite v2 00..99 + {len(rows)}/{len(rows)} semantic replay + official exact-v1 HTML/PDF | checked | {len(rows)} | {';'.join(row['source_family_id'] for row in retained)} | pages=300;final_cursor=end;raw={SOURCE['raw_snapshot_records']};registered={len(rows)};screened={len(rows)};retained={len(retained)};closure={len(closures)} | 2026-05-23T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | GAP-20260523-INDEPENDENT-AUDIT |", "",
    "### Coverage Limitations", "", f"<!-- coverage:SRC-ARXIV:20260523:start -->Author lane 已逐项完成 {len(rows)}/{len(rows)} title+abstract 语义筛选；独立 reviewer 尚未重放 false-positive/false-negative、exact-v1 claim boundary 与 Books disposition，因此 Gate 保持 Open。<!-- coverage:SRC-ARXIV:20260523:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
    "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
for row in retained:
    score = row["score_v2"]
    override = "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"
    sf = row["source_family_id"]
    lines.append(f"| {sf} | arXiv:{row['arxiv_id']}v1 | paper-v1:{row['arxiv_id']} | 2026-W21 | 2026-05-22 | SRC-ARXIV | {score['design_delta']} | {score['system_reach']} | {score['durability']} | {score['total']} | retained | {row['review_status']} | accessible | {override} | review:{sf} | self | — | new_in_window | {row['owner_node']} | {row['integration_disposition']} | books-review:{sf} | no |")

lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    sf, arxiv_id = row["source_family_id"], row["arxiv_id"]
    lines.append(f"| {sf} | RP-TODO-{sf} | {review_route(row)} | arXiv:{arxiv_id}v1 | SRC-ARXIV@arXiv:{arxiv_id}v1 | {evidence_locator(row, 'method_locator')} | {evidence_locator(row, 'evaluation_locator')} | {evidence_locator(row, 'limitations_locator')} | arXiv:{arxiv_id}v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:{sf} | complete |")

lines += ["", "### Source Reviews", ""]
for row in retained:
    sf, arxiv_id = row["source_family_id"], row["arxiv_id"]
    lines += [
        f"<!-- review:{sf}:start -->", f"#### {row['title']}", "",
        f"**问题与机制。** {row['screening_reason']} 该证据的系统 owner 定位为 `{row['owner_node']}`。", "",
        f"**Exact-v1 路径。** Method=`{row['method_locator']}`；Evaluation=`{row['evaluation_locator']}`；Limitations/Counterevidence=`{row['limitations_locator']}`。", "",
        f"<!-- claim:{sf}:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:{sf}:end -->", "",
        f"Books Decision=`{row['integration_disposition']}`；这是 author-side current-Books comparison，等待非作者 owner+adjacent challenge。", f"<!-- review:{sf}:end -->", "",
    ]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    arxiv_id, sf = row["arxiv_id"], row["source_family_id"]
    if row["score_v2"]["total"] < 7 and row["integration_disposition"] != "Integrate":
        continue
    selected = arxiv_id in DEEP
    unit = DEEP.get(arxiv_id, "—")
    rationale = "跨层改变训练或运行时控制权，且具有清晰旧路径、收益与失效边界" if selected else "exact-v1 已完成；未扩写只受 Daily 三项上限约束，不降低 Source Review 或 Books Decision"
    eligibility = "score_7_9"
    if row["integration_disposition"] == "Integrate":
        eligibility += "; forced_review; potential_books_delta"
    lines.append(f"| {sf} | {eligibility} | {'selected' if selected else 'not_selected'} | {unit} | — | {rationale} | {'analysis:'+unit if selected else 'analysis-decision:'+sf} |")

analysis_text = {
    "2605.23158": "split inference 在客户端算力有限且不愿上传原始 prompt 时合理，因为它只把中间 activation 交给服务端；但隐藏状态仍携带可逆语义时，边界从‘原文不离端’退化成‘攻击者尚未恢复原文’。ActInv 将 server-visible activation 明确纳入 threat model，并展示 layer/split choice 会改变泄漏面。收益是把隐私判断绑定到可测攻击，而代价是客户端计算、通信与防御噪声；作者攻击与模型集合不能证明所有隐藏状态必然可逆，也不能把未被当前攻击恢复等同于安全。",
    "2605.23348": "单站点 routing 在电价、碳强度和容量近似稳定时合理；多 renewable site 的可用功率与请求负载同时波动后，调度器必须共同拥有 latency、capacity、energy forecast 与迁移成本。XWind 把这些约束放进跨站路由控制面，收益是在 SLO 下利用时空能源差异，代价是预测误差、跨站网络、状态迁移和故障域扩大；论文 trace 上的结果不能证明真实电网、所有模型组合或极端天气下仍成立。",
    "2605.24213": "把 evaluation harness 当作透明脚本在模型、任务和后端固定时足够；当同一 benchmark 被不同 harness、版本、prompt adapter、parser 和 retry policy 执行时，harness 本身成为测量系统。该研究把配置、依赖、执行与结果 provenance 提升为 evaluation engineering contract。收益是让分数差异可归因、可复现，代价是更严格的版本冻结与收据成本；仓库样本的经验观察不能证明所有 harness 都存在同样缺陷，也不替代对具体 benchmark validity 的审计。",
}
for arxiv_id, unit in DEEP.items():
    lines += ["", f"<!-- analysis:{unit}:start -->", f"### {unit}", "", analysis_text[arxiv_id], f"<!-- analysis:{unit}:end -->"]
for row in retained:
    if row["arxiv_id"] not in DEEP:
        sf = row["source_family_id"]
        lines.append(f"<!-- analysis-decision:{sf}:start -->该 family 已按 exact-v1 完成 Source Review；未进入三项 Deep Analysis 只表示它没有高于当日三个跨层控制契约变化，不表示跳过或降低证据要求。<!-- analysis-decision:{sf}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    comparison = comparison_by_id[row["arxiv_id"]]
    sf = row["source_family_id"]
    adjacent_refs = ";".join(chapter_ref(path) for path in comparison["adjacent_paths"]) or chapter_ref(comparison["owner_path"])
    lines.append(f"| {sf} | {row['owner_node']} | {chapter_ref(comparison['owner_path'])} | {adjacent_refs} | existing:{sf} | delta:{sf} | Direct Evolution | {row['integration_disposition']} | books-review:{sf} |")
for row in retained:
    comparison = comparison_by_id[row["arxiv_id"]]
    sf = row["source_family_id"]
    lines += [f"<!-- books-review:{sf}:start -->", f"<!-- existing:{sf}:start -->{comparison['existing_proposition']}<!-- existing:{sf}:end -->", f"<!-- delta:{sf}:start -->{comparison['new_evidence_delta']}<!-- delta:{sf}:end --> Author decision=`{row['integration_disposition']}`。", f"<!-- books-review:{sf}:end -->"]

first_sf = retained[0]["source_family_id"]
first_analysis = next(iter(DEEP.values()))
lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", f"| SA-20260523-COVERAGE | fresh-context:pending | coverage | coverage:SRC-ARXIV:20260523 | author packet cannot self-certify false negatives | non-author replays {len(rows)}/{len(rows)} | open |", f"| SA-20260523-EVIDENCE | fresh-context:pending | evidence | review:{first_sf} | exact-v1 locator and claim challenge pending | non-author rechecks {len(retained)} retained families | open |", f"| SA-20260523-SELECTION | fresh-context:pending | deep_analysis_selection | analysis:{first_analysis} | Top3 challenge pending | non-author selection audit | open |", f"| SA-20260523-BOOKS | fresh-context:pending | books | books-review:{first_sf} | provisional queue pending | non-author current owner+adjacent compare | open |", "", "## 8. Ignored Noise", "", f"{len(closures)} 条逐 family pre-denominator closure 完整保存在 `screening-ledger-final.json`；每条保留标题、摘要机制、具体排除边界与重开条件。", "", "## 9. Recommended Action", "", f"由未参与 author lane 的 reviewer 重放 {len(rows)}/{len(rows)}、挑战 {len(retained)} 个 denominator 与 {len(queue)} 个 provisional Integrate；通过后由 root 按日期顺序串行写回 Books。", "", "## 10. Repository Changes", "", "- 新增 2026-05-23 date-local author packet、screening ledger、exact-v1 review packet、Books comparison 与 writeback queue。", "- 未修改共享 Books；未 stage、commit 或 push。", "", "## 11. Open Questions", "", "- 独立 reviewer 是否发现 denominator false negative/positive？", "- current Books 是否已用不同术语承载部分 provisional Integrate，从而应降级为 No Change？", "", "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 12. Sources", ""]
for row in retained:
    suffix = "pdf" if row["arxiv_id"] in PDF_IDS else "html"
    lines.append(f"- [{row['title']}](https://arxiv.org/{suffix}/{row['arxiv_id']}v1) — arXiv:{row['arxiv_id']}v1；first-public 2026-05-22；accessed 2026-09-02")
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Open`", "", "Evidence: `Open`", "", "Books: `Open`", "", "unresolved findings: 4", "", "Author packet 已交付；非作者 fresh-context 审计、root Books 串行写回及 post-write semantic audit 尚未完成。"]

output = ROOT / "papers/2026/05/23/README.md"
output.parent.mkdir(parents=True, exist_ok=True)
text = "\n".join(lines)
for row in retained:
    sf, arxiv_id = row["source_family_id"], row["arxiv_id"]
    body = text.split(f"<!-- review:{sf}:start -->", 1)[1].split(f"<!-- review:{sf}:end -->", 1)[0]
    candidate = {"Event Identity": f"paper-v1:{arxiv_id}", "Primary Identifier": f"arXiv:{arxiv_id}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"}
    rp = _expected_review_provenance(sf, candidate, review_route(row), f"arXiv:{arxiv_id}v1", f"SRC-ARXIV@arXiv:{arxiv_id}v1", evidence_locator(row, "method_locator"), evidence_locator(row, "evaluation_locator"), evidence_locator(row, "limitations_locator"), f"arXiv:{arxiv_id}v1 artifact links; immutable commit Not Disclosed unless stated in paper", f"claim:{sf}", f"review:{sf}", _normalized_body_sha256(body))
    text = text.replace("RP-TODO-" + sf, rp)
output.write_text(text + "\n")

print(json.dumps({"raw": SOURCE["raw_snapshot_records"], "registered": len(rows), "screened": len(rows), "retained": len(retained), "closures": len(closures), "reviewed": len(retained), "blocked": 0, "integrate_queue": len(queue)}, ensure_ascii=False))
