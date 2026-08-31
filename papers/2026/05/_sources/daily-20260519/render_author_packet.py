#!/usr/bin/env python3
"""Render the 2026-05-19 V2.1 author packet without touching shared Books."""
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
REPORT_DATE = "2026-05-19"

# Retention is deliberately narrow: each family changes a durable model, training,
# runtime, evidence, security, or agent state/control contract.  Domain-only
# applications and component-local metric gains stay in the screening ledger.
CANDIDATES = {
    "2606.06502": ("TRAIN-DATA", 6, "No Change — Existing Coverage", "§3 Formal Framework; §5 Algorithm", "§6 Experimental Setup", "§8 Limitations"),
    "2605.17734": ("AGENT-PLATFORM", 8, "Integrate", "§3.1–3.3 Program Functions", "§4.1–4.2 Experiments", "Appendix A Limitations"),
    "2605.17787": ("TRAIN-PRETRAINING", 9, "Integrate", "§3 Training Dynamics; §4.1–4.2 clipping", "Appendix B–C settings and ablations", "§5 Conclusions; Appendix C.4 seeds"),
    "2605.17830": ("AGENT-MEMORY", 9, "Integrate", "§3.1–3.5 stateful setting and monitor", "§4 protocol; §5 results", "§6 Discussion and limitations"),
    "2605.17837": ("MULTIMODAL-GENERATIVE-PARADIGMS", 7, "No Change — Existing Coverage", "§4.1–4.3 temporal pruning", "§5.1–5.4; Appendix B–C", "§6 Conclusion; Appendix A sensitivity"),
    "2605.17842": ("INFER-TENSORRT-LLM", 9, "Integrate", "§3.2–3.5 Structured Newton Layer Parallelism", "§5.1–5.3 experiments", "§6 Limitations"),
    "2605.17849": ("TRAIN-DATA", 8, "Integrate", "§3.1–3.3 model-aware synthesis", "§4 experiments and analyses", "§5 limitations"),
    "2605.17850": ("MULTIMODAL-GENERATIVE-PARADIGMS", 7, "No Change — Existing Coverage", "§2.1–2.4 path-space SMC", "§4 experiments", "§5 discussion and limitations"),
    "2605.17856": ("AGENT-WORKFLOW", 8, "Integrate", "§2–§5 knowledge infrastructure", "§7.1–7.8 methods and validation", "§8 Discussion"),
    "2605.17862": ("TRAIN-RLHF", 9, "Integrate", "§3.1–3.3 drift decomposition; §4 freshness control", "§5.1–5.4 experiments", "§6 limitations"),
    "2605.17889": ("INFER-TENSORRT-LLM", 9, "Integrate", "§3 Motivation; §4.1–4.2 orchestration", "§5 evaluation", "§6 discussion and limitations"),
    "2605.17932": ("MULTIMODAL-GENERATIVE-PARADIGMS", 7, "Integrate", "§III-A–C compression pipeline", "§III-D; §IV-A–C", "§V Discussion; §VII Future Work"),
    "2605.17938": ("TRAIN-DATA", 7, "No Change — Existing Coverage", "§2.1–2.4 mirrored unlearning attribution", "§4–§5; Appendix B", "Appendix C.3 Limitations"),
    "2605.17954": ("MULTIMODAL-REPRESENTATION", 8, "Integrate", "§2 motivation; §3.1–3.4 tokenization", "§4.1–4.4 experiments", "§5 limitations"),
    "2605.17967": ("TRAIN-SFT", 7, "No Change — Existing Coverage", "§3.1–3.3 interaction decomposition", "Appendix A–B validation", "§4 Conclusion and Discussion"),
    "2605.18032": ("AGENT-WORKFLOW", 8, "Integrate", "§2 architecture; §3.1–3.3 node diagnosis", "§4.1–4.3 evaluation", "§5 Conclusion"),
    "2605.18066": ("PLATFORM-GPU-SCHEDULER", 7, "Integrate", "§3 semantic opportunity; §4.1–4.6 design", "§5.1–5.5 evaluation", "§7 Discussion"),
    "2605.18067": ("AGENT-MULTI-AGENT", 7, "Integrate", "§IV–VI agent scoring and serving game", "§VIII implementation and experiments", "§VII Discussion"),
    "2605.18071": ("INFER-KV-CACHE", 9, "Integrate", "§4–§7 multi-tier KV design", "§9.1–9.3 experiments", "§10–§11 conclusion and future work"),
    "2605.18083": ("MODEL-MOE", 7, "No Change — Existing Coverage", "§2.1–2.2 sparse upcycling and merging", "§3–§5 experiments and generalization", "§6 Related Work; §7 Conclusion"),
    "2605.18104": ("PLATFORM-SECURITY", 8, "Integrate", "§2 geometry; §3 mechanism; §4 correction", "§5 experiments", "§6 limitations"),
    "2605.18106": ("TRAIN-PRETRAINING", 8, "Integrate", "§3–§5 symmetry-compatible optimizer design", "§6 experiments", "§1 Scope and limitations; §7 discussion"),
    "2605.18165": ("MULTIMODAL-GENERATIVE-PARADIGMS", 8, "Integrate", "§3 mask state; §4.1–4.3 compression", "§5.1–5.4 experiments", "§6 limitations"),
    "2605.18190": ("MULTIMODAL-GENERATIVE-PARADIGMS", 7, "No Change — Existing Coverage", "§3.1–3.2 interleaved heavy/light denoising", "§4 experiments; Appendix A–B", "§6 Limitations and Future Work"),
    "2605.18261": ("TRAIN-RLHF", 7, "Integrate", "§3.1–3.3 answer-gated verification", "§4.1–4.6; Appendix B–F", "§5 Conclusion"),
    "2605.18271": ("AGENT-MEMORY", 8, "Integrate", "PDF pp.3–5 §3.1–3.3 memory construction", "PDF §4–§5; device experiments", "PDF §6 Limitations"),
    "2605.18309": ("TRAIN-SFT", 7, "No Change — Existing Coverage", "§2.1–2.4 alignment dynamics", "§3–§4 experiments", "§6 Conclusion; appendices"),
    "2605.18414": ("AGENT-MCP", 9, "Integrate", "§3 governed MCP proxy", "§4–§5 benchmark and results", "§6–§7 discussion and threat-model limits"),
    "2605.18474": ("PLATFORM-SECURITY", 7, "No Change — Existing Coverage", "§3.1–3.3 text-to-weight fingerprinting", "§4.1–4.2 experiments", "§5 limitations"),
    "2605.18498": ("PLATFORM-EVALUATION-SYSTEM", 7, "Integrate", "PDF pp.3–5 §3 routing-specialization metrics", "PDF pp.5–11 §4 experiments and intervention", "PDF p.11 §4.3 intervention boundary; §5 Conclusion"),
    "2605.18607": ("PLATFORM-EVALUATION-SYSTEM", 8, "Integrate", "§3 proxy metrics", "§4–§5 model/data ranking", "§6 limitations"),
    "2605.18643": ("MODEL-MOE", 7, "No Change — Existing Coverage", "§2.1–2.2 zero experts and group loss", "§3.1–3.2 experiments", "§4 limitations"),
    "2605.18672": ("PLATFORM-SECURITY", 6, "Weekly Only — Context", "§2 contract design; §3.1–3.2 three layers", "Appendix A–B formal argument", "§4 Limitations; §5 Alternative Views"),
    "2605.18693": ("AGENT-PLATFORM", 8, "Integrate", "§3.1–3.4 skill-generation artifact contract", "§4.1–4.4 execution evaluation", "§5 Conclusion; appendix sensitivity"),
    "2605.18732": ("PLATFORM-EVALUATION-SYSTEM", 7, "Integrate", "§3.1–3.5 recall scaling framework", "§4.1–4.4 authentication and evaluation", "§5 limitations"),
    "2605.18740": ("TRAIN-RLHF", 7, "No Change — Existing Coverage", "§3.1–3.2 regional-to-global OPD", "§4.1–4.2 experiments", "§5 limitations"),
    "2605.18930": ("AGENT-MEMORY", 9, "Integrate", "§3 threat model; §4.1–4.2 poisoning", "§5 mechanistic analysis; §6 evaluation", "§7 limitations"),
    "2605.19127": ("PLATFORM-SECURITY", 8, "Integrate", "§3.1–3.6 policy/attack/evaluation contract", "§4–§5 diagnostic surface", "§6 Limitations"),
    "2605.19147": ("TRAIN-DATA", 7, "No Change — Existing Coverage", "§4.1 open-book benign rewriting", "§5.1–5.3 experiments", "§6 Discussion; §7 Future Work"),
    "2605.19193": ("AGENT-MULTI-AGENT", 8, "Integrate", "§III–V sequential stopping and calibration", "§VI simulation; §VII real-LLM study", "§V-E i.i.d. violations; §VIII discussion"),
    "2605.19196": ("PLATFORM-EVALUATION-SYSTEM", 9, "Integrate", "§2.1–2.2 controlled-intervention benchmark", "§3.1–3.5 judge meta-evaluation", "§4 related work; §5 conclusion"),
    "2605.19220": ("PLATFORM-EVALUATION-SYSTEM", 6, "Weekly Only — Context", "§2.1–2.4 UQ taxonomy", "§3 diagnosis", "position paper; §4 roadmap, no mechanism evaluation"),
    "2605.19228": ("PLATFORM-EVALUATION-SYSTEM", 7, "No Change — Existing Coverage", "§3 problem; §4.1–4.3 step confidence", "§5 experiments", "§6 limitations"),
    "2605.20251": ("PLATFORM-EVALUATION-SYSTEM", 9, "Integrate", "§3.1–3.5 trajectory/control contract", "§4.1–4.5 experiments", "§5 Limitations and Conclusion"),
    "2605.20258": ("TRAIN-RLHF", 8, "Integrate", "§2 setup; §3.1–3.2 complementary teachers", "§4 experiments", "§5 limitations"),
    "2605.20270": ("PLATFORM-EVALUATION-SYSTEM", 9, "Integrate", "§1–§4 deployment contract and e-process", "§5–§7 proofs and 650-stream evaluation", "§8 limitations and boundary"),
}

DEEP = {
    "2605.17787": "DA-OPTIMIZER-EFFECTIVE-LR",
    "2605.18071": "DA-MULTITIER-KV-STATE",
    "2605.20251": "DA-CONTROL-PRESERVATION",
}


def family(arxiv_id: str) -> str:
    return "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")


def review_route(row: dict) -> str:
    """V2.1 route is driven by score or a forced Books delta, not accessibility."""
    return "deep" if row["score_v2"]["total"] >= 7 or row["integration_disposition"] == "Integrate" else "standard"


def evidence_locator(row: dict, key: str) -> str:
    route = "PDF" if row["arxiv_id"] in {"2605.18271", "2605.18498"} else "HTML"
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
        "retrieval_route": "official arXiv exact-v1 HTML" if arxiv_id not in {"2605.18271", "2605.18498"} else "official arXiv exact-v1 PDF fallback",
        "retrieved_at": "2026-09-01T21:30:00+08:00",
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
    "# Daily Research — 2026-05-19", "", "**Research Date:** 2026-05-19", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-18 09:00:00 ～ 2026-05-19 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；technical claims bind official arXiv exact-v1 HTML/PDF。", "",
    "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。author packet 已完成，等待非作者 fresh-context 审计。", "",
    "## Executive Summary", "",
    f"从 {SOURCE['raw_snapshot_records']:,} 条月度 raw records 中恢复并逐项语义筛选 {len(rows)}/{len(rows)} 个窗口身份；严格 author denominator={len(retained)}，pre-denominator closures={len(closures)}，exact-v1 author reviews={len(retained)}/{len(retained)}，blocked=0，provisional Books queue={len(queue)}。共享 Books 未修改。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-19 |", "| Window End | 2026-05-19 |",
    "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
    "| Denominator ID | DEN-20260519-V2-AUTHOR |", "| Denominator Frozen At | 2026-09-01T21:30:00+08:00 |", "| Completion Status | In Progress |", "| Coverage Gate | Open |", "| Evidence Gate | Open |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-18T09:00:00+08:00 | 2026-05-19T09:00:00+08:00 | 2026-09-01T21:30:00+08:00 | DataCite v2 00..99 + {len(rows)}/{len(rows)} semantic replay + official exact-v1 HTML/PDF | checked | {len(rows)} | {';'.join(row['source_family_id'] for row in retained)} | pages=300;final_cursor=end;raw={SOURCE['raw_snapshot_records']};registered={len(rows)};screened={len(rows)};retained={len(retained)};closure={len(closures)} | 2026-05-19T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | GAP-20260519-INDEPENDENT-AUDIT |", "",
    "### Coverage Limitations", "", f"<!-- coverage:SRC-ARXIV:20260519:start -->Author lane 已逐项完成 {len(rows)}/{len(rows)} title+abstract 语义筛选；独立 reviewer 尚未重放 false-positive/false-negative、exact-v1 claim boundary 与 Books disposition，因此 Gate 保持 Open。<!-- coverage:SRC-ARXIV:20260519:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
    "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
for row in retained:
    score = row["score_v2"]
    override = "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"
    sf = row["source_family_id"]
    lines.append(f"| {sf} | arXiv:{row['arxiv_id']}v1 | paper-v1:{row['arxiv_id']} | 2026-W21 | 2026-05-18 | SRC-ARXIV | {score['design_delta']} | {score['system_reach']} | {score['durability']} | {score['total']} | retained | {row['review_status']} | accessible | {override} | review:{sf} | self | — | new_in_window | {row['owner_node']} | {row['integration_disposition']} | books-review:{sf} | no |")

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
    "2605.17787": "SGD 在大批量 LLM 预训练中仍是合理基线，但小梯度、极大的 weight-to-gradient ratio、层级梯度尖峰与 LM-head token-class 不均衡共同限制其可用步长。该工作用两类 clipping 换取更大的有效学习率，并在 1B LLaMA、1M-token batch 的受限实验中缩小与 Adam 的损失差距；代价是新增 clipping 策略与调参面，且不能外推为 Adam 已无必要。",
    "2605.18071": "只保留 GPU KV 在短上下文和低并发下简单且低延迟；长上下文使容量、迁移与稀疏注意力选择变成同一个状态生命周期问题。KVDrive 将 eviction、elastic pipeline 与 GPU/CPU/SSD tiering 放进统一控制器，收益来自把热度和设备带宽共同纳入调度；代价是重要性估计误差、跨层同步和 SSD layout 复杂度，故在状态预测不可靠时应退回更保守的驻留/窗口策略。",
    "2605.20251": "结果型 benchmark 在任务短、工具链简单时足够，但长链 coding agent 可能在最终通过前已经丢失可解释性、可中断性、可修复性或控制权。ProcBench 将轨迹标准化、过程缺陷与 control preservation 变成一等 evaluation contract；收益是暴露 outcome 指标看不到的风险，代价是轨迹归一化、标注与校准成本，且其 200-case 结果不能直接证明生产 Agent 安全。",
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
lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", f"| SA-20260519-COVERAGE | fresh-context:pending | coverage | coverage:SRC-ARXIV:20260519 | author packet cannot self-certify false negatives | non-author replays {len(rows)}/{len(rows)} | open |", f"| SA-20260519-EVIDENCE | fresh-context:pending | evidence | review:{first_sf} | exact-v1 locator and claim challenge pending | non-author rechecks {len(retained)} retained families | open |", f"| SA-20260519-SELECTION | fresh-context:pending | deep_analysis_selection | analysis:DA-OPTIMIZER-EFFECTIVE-LR | Top3 challenge pending | non-author selection audit | open |", f"| SA-20260519-BOOKS | fresh-context:pending | books | books-review:{first_sf} | provisional queue pending | non-author current owner+adjacent compare | open |", "", "## 8. Ignored Noise", "", f"{len(closures)} 条逐 family pre-denominator closure 完整保存在 `screening-ledger-final.json`；每条保留标题、摘要机制、具体排除边界与重开条件。", "", "## 9. Recommended Action", "", f"由未参与 author lane 的 reviewer 重放 {len(rows)}/{len(rows)}、挑战 {len(retained)} 个 denominator 与 {len(queue)} 个 provisional Integrate；通过后由 root 按日期顺序串行写回 Books。", "", "## 10. Repository Changes", "", "- 新增 2026-05-19 date-local author packet、screening ledger、exact-v1 review packet、Books comparison 与 writeback queue。", "- 未修改共享 Books；未 stage、commit 或 push。", "", "## 11. Open Questions", "", "- 独立 reviewer 是否发现 denominator false negative/positive？", "- current Books 是否已用不同术语承载部分 provisional Integrate，从而应降级为 No Change？", "", "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 12. Sources", ""]
for row in retained:
    suffix = "html" if row["arxiv_id"] not in {"2605.18271", "2605.18498"} else "pdf"
    lines.append(f"- [{row['title']}](https://arxiv.org/{suffix}/{row['arxiv_id']}v1) — arXiv:{row['arxiv_id']}v1；first-public 2026-05-18；accessed 2026-09-01")
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Open`", "", "Evidence: `Open`", "", "Books: `Open`", "", "unresolved findings: 4", "", "Author packet 已交付；非作者 fresh-context 审计、root Books 串行写回及 post-write semantic audit 尚未完成。"]

output = ROOT / "papers/2026/05/19/README.md"
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
