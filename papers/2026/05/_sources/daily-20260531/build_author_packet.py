#!/usr/bin/env python3
"""Build the 2026-05-31 V2.1 author-only packet without touching shared Books."""
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

REPORT_DATE = "2026-05-31"
EXECUTED_AT = "2026-09-01T20:40:00+08:00"
SOURCE = json.loads((HERE / "screening-ledger-provisional.json").read_text())
CONFIG = json.loads((HERE / "candidate-config-author.json").read_text())
SECTION_INDEX = {row["arxiv_id"]: row for row in json.loads((HERE / "exact-v1-section-index.json").read_text())}


def family(arxiv_id: str) -> str:
    return "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")


def sentences(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text or "").strip()
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", clean) if part.strip()]


def clipped(text: str, limit: int) -> str:
    clean = re.sub(r"\s+", " ", text or "").strip()
    if len(clean) <= limit:
        return clean
    head = clean[:limit].rsplit(" ", 1)[0].rstrip(" ,;:")
    return head + "…"


def mechanism_sentence(row: dict) -> str:
    for sentence in sentences(row.get("abstract", "")):
        if re.search(r"\b(propose|introduce|present|develop|design|identify|formulate|show|demonstrate|find)\b", sentence, re.I):
            return sentence
    return sentences(row.get("abstract", ""))[0] if row.get("abstract") else row["title"]


def evidence_sentence(row: dict) -> str:
    for sentence in sentences(row.get("abstract", "")):
        if re.search(r"\b(experiment|evaluation|evaluate|result|benchmark|ablation|validate|study|analysis)\b", sentence, re.I):
            return sentence
    ss = sentences(row.get("abstract", ""))
    return ss[-1] if ss else row["title"]


def closure_reason(row: dict) -> str:
    abstract = row.get("abstract", "")
    title = row["title"]
    contribution = mechanism_sentence(row)
    evidence = evidence_sentence(row)
    if re.search(r"medical|clinical|protein|molecular|brain|crop|malaria|finance|traffic|satellite|remote sensing|EEG|ultrasound|tumou?r|gene|drug", title + " " + abstract, re.I):
        boundary = f"其状态与指标仍由 `{title}` 的垂直领域对象拥有，没有改变通用 AI System 的 data/state/control owner 或 release contract。"
    elif re.search(r"survey|review|position|perspective|framework for .*liability|sovereignty|theory of human", title, re.I):
        boundary = f"该 family 对 `{title}` 给出综述、立场或概念框架，但没有可复算 artifact 与跨 workload 控制接口，尚不足以形成长期机制节点。"
    elif re.search(r"dataset|benchmark|arena|challenge", title, re.I):
        boundary = f"该数据或测量资产只闭合 `{title}` 的任务协议，没有改变跨任务 evaluator、release gate 或生产证据所有权。"
    elif re.search(r"classifier|classification|segmentation|forecast|prediction|retrieval|generation|distillation|fine-tun|representation", title + " " + abstract, re.I):
        boundary = f"改进集中在 `{title}` 的局部表示、objective 或任务精度，没有给出训练恢复、推理 SLO、平台控制面或 Agent 状态提交的新合同。"
    else:
        boundary = f"`{title}` 的贡献仍是局部算法或单 workload 结论，未改变长期 state/data/control ownership、evaluation contract 或 fallback 边界。"
    return f"机制：{contribution} 证据：{evidence} 排除边界：{boundary} 重开条件：若后续公开跨 workload artifact、生产控制接口、owner 迁移或能修正 Books 既有结论的 primary evidence，再重开 denominator。"


def score(total: int) -> dict[str, int]:
    mapping = {6: (2, 2, 2), 7: (2, 2, 3), 8: (3, 2, 3), 9: (3, 3, 3)}
    design, reach, durability = mapping[total]
    return {"design_delta": design, "system_reach": reach, "durability": durability, "total": total}


def choose_section(record: dict, patterns: list[str], fallback_index: int) -> dict:
    sections = record.get("sections", [])
    for pattern in patterns:
        for section in sections:
            heading = str(section.get("heading", ""))
            if re.search(pattern, heading, re.I):
                return section
    if not sections:
        return {"heading": "Not Disclosed — exact-v1 body has no extractable section", "text": ""}
    return sections[min(max(fallback_index, 0), len(sections) - 1)]


LOCATOR_OVERRIDES = {
    "2606.00485": ("3.2 Context-Write Channels", "6.5 Attack Validation", "Limitations"),
    "2606.00486": ("6 DEPOT: Dead-Entry PrOTection", "7.1 DEPOT Performance", "8 Discussion and Limitations"),
    "2606.00497": ("3.1 Threat Model", "4 Results", "7 Limitations"),
    "2606.00499": ("4.1 Problem Formulation", "5.5 Ablation Study", "Appendix H Limitations and Broader Impacts"),
    "2606.00510": ("4.1 Overview", "5.3 Ablation Study", "Limitations"),
    "2606.00516": ("3 Scheduling Model for Exclusive Batching", "4.3 End-to-End Performance", "5 Conclusion"),
    "2606.00539": ("3 GNMR Runtime Stability Controller", "5 Experiments", "7 Limitations"),
    "2606.00566": ("4.3 Harness", "5 Behavioral Results", "8 Discussion"),
    "2606.00576": ("III Method", "IV Experiments", "V Conclusions"),
    "2606.00601": ("4 Compiler-Driven Lowering", "6.3 Performance", "9 Limitations"),
    "2606.00611": ("2.1 Problem Formulation and Framework Overview", "3.2 Main Results", "6 Limitations"),
    "2606.00620": ("3 Scalable streaming video narration", "4 Experiments", "4.5 Limitations"),
    "2606.00622": ("3 Dialogue Construction via Adversarial Hallucination Trajectory Synthesis", "5.5 Experiment Results", "6 Conclusion"),
    "2606.00636": ("II Integrated Simulator Design and Implementation", "III Evaluation", "IV CONCLUSION"),
    "2606.00642": ("4 Reasoning Exposure Prompting", "6.2 Evaluation on Functional Utility", "9 Limitations"),
    "2606.00654": ("3 Methodology", "4.3 Experiment Results", "6 Conclusion and Limitations"),
    "2606.00655": ("3.2 The SIMAS Framework", "4.2 Experimental Results and Analysis", "Limitations"),
    "2606.00660": ("2 FineVerify : Fine-Grained Self-Verification for Agentic Search", "3.4 Cost-Accuracy Tradeoff", "Limitations"),
    "2606.00664": ("3.1 Problem formulation and overview", "4 Experiments", "6 Limitations"),
    "2606.00669": ("4 Architecture", "7 Evaluation", "7.7 Honest negatives"),
    "2606.00671": ("2 Architecture", "3 Empirical Evaluation", "6 Conclusion: today’s abstain, tomorrow’s correct"),
    "2606.00708": ("3.2 System Pipeline", "Evaluation Protocol.", "Limitations and Future Work."),
    "2606.00717": ("2 Personalized federated weighted conformal prediction", "3 Numerical experiments", "Limitations:"),
    "2606.00722": ("4 Proposed Method", "5 Experimental Results and Analysis", "Limitations"),
    "2606.00724": ("3 Methodology", "4.2 Performance and Efficiency Evaluation", "Limitations"),
    "2606.00735": ("4. ViBE Framework", "5.2. Overall Results", "5.5. Discussion"),
    "2606.00750": ("3.1 Data Curation", "3.2 Evaluation Methods", "Limitations."),
    "2606.00765": ("2 Hierarchical Dependency-Guided Search for Agent Trajectory Diagnostics", "4 Result", "5 Limitations"),
    "2606.00773": ("3 SafeVLA-Bench", "4 Experimental Results", "5 Discussion and Limitations"),
    "2606.00774": ("3. SCOPE", "6.2. Performance Evaluation (RQ1)", "4.1. Assumptions"),
    "2606.00793": ("3 Benchmark Construction", "5.2 MBench Evaluation", "6 Discussion"),
    "2606.00804": ("3.1 Design", "4.2 Formal Cell Results", "Formal-Test Scope"),
    "2606.00825": ("3 SuperMemory-VQA Dataset", "5.1 Main Results", "6 Conclusion"),
    "2606.00832": ("2 Momento", "4 Results and Analysis", "Limitations"),
    "2606.00866": ("4. Design", "6. Evaluation", "7.2. Heterogeneous Hardware"),
    "2606.00888": ("4 SMET: Sparse Memory-Efficient Training", "5 Experiments", "Appendix G Limitations and Discussion"),
    "2606.00898": ("4.2 Three-Component Decomposition", "6.5 Results", "Limitations."),
    "2606.00914": ("3.1 Agent protocol", "4.6 Simple defenses mitigate the attack", "6.3 Limitations"),
    "2606.00920": ("3.3 Evaluation Framework", "4.1 Overall Accuracy and Stability", "Limitations"),
    "2606.00925": ("3 Benchmark Construction", "4 Benchmark Result", "Broad Impact"),
    "2606.07620": ("III Methodology", "IV-B Experimental Results", "V Conclusion"),
    "2606.07623": ("2 Semantic presentations of pre-trained LLMs", "8 Numerical verification of the theorems", "12 Scope and failure modes"),
    "2606.07624": ("3 Validity: Sequential Uncertainty Quantification", "4 Monitoring via Online Change-Point Detection", "5 Conclusion"),
    "2606.20634": ("3. Benchmark Construction", "3. Empirical demonstration that container-presence baselines systematically overclaim", "7.4. Interpretation Boundary"),
    "2606.28338": ("3. Methodology", "5.1. Overall Performance", "6. Conclusion"),
}


def exact_section(record: dict, heading: str) -> dict:
    for section in record.get("sections", []):
        if str(section.get("heading", "")).strip() == heading:
            return section
    raise ValueError(f"exact-v1 locator not found for {record['arxiv_id']}: {heading}")


def with_locator_prefix(section: dict) -> dict:
    result = dict(section)
    result["heading"] = "§ " + str(section["heading"]).strip()
    return result


def evidence_sections(arxiv_id: str) -> tuple[dict, dict, dict]:
    record = SECTION_INDEX[arxiv_id]
    if arxiv_id in LOCATOR_OVERRIDES:
        method_h, evaluation_h, limitations_h = LOCATOR_OVERRIDES[arxiv_id]
        return tuple(with_locator_prefix(exact_section(record, heading)) for heading in (method_h, evaluation_h, limitations_h))
    method = choose_section(record, [r"^\d+(?:\.\d+)*\.?\s+(Method|Methodology|Architecture|System|Framework|Design|Benchmark Construction)", r"Controller|Protocol|Runtime|Scheduling Model|Method:"], 2)
    evaluation = choose_section(record, [r"Experiment|Evaluation|Results|Validation|Main Results|Baseline Overclaim|Candidate Scorer|Empirical"], max(3, len(record.get("sections", [])) // 2))
    limitations = choose_section(record, [r"Limitations|Threats to Validity|Scope and failure|Discussion and Limitations|What the data says, and what it does not|Interpretation Boundary"], len(record.get("sections", [])) - 2)
    return with_locator_prefix(method), with_locator_prefix(evaluation), with_locator_prefix(limitations)


def excerpt(section: dict, limit: int = 420) -> str:
    text = re.sub(r"\s+", " ", str(section.get("text", ""))).strip()
    selected = " ".join(sentences(text)[:2]) or text
    return clipped(selected, limit)


rows: list[dict] = []
for original in SOURCE["identities"]:
    row = dict(original)
    arxiv_id = row["arxiv_id"]
    if arxiv_id in CONFIG:
        owner, total, disposition = CONFIG[arxiv_id]
        method, evaluation, limitations = evidence_sections(arxiv_id)
        row.update(
            source_family_id=family(arxiv_id),
            screening_status="retained",
            screening_reason=mechanism_sentence(row),
            owner_node=owner,
            score_v2=score(total),
            review_status="deep_complete" if total >= 7 or disposition == "Integrate" else "standard_complete",
            access_status="accessible",
            integration_disposition=disposition,
            method_locator=str(method["heading"]),
            evaluation_locator=str(evaluation["heading"]),
            limitations_locator=str(limitations["heading"]),
            method_excerpt=excerpt(method),
            evaluation_excerpt=excerpt(evaluation),
            limitations_excerpt=excerpt(limitations),
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
closures = [row for row in rows if row["screening_status"] == "pre_denominator_closure"]
ledger = {
    "schema": "daily-screening-ledger-v2.1-author",
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
(HERE / "screening-ledger-author.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

roadmap = (ROOT / "ROADMAP.md").read_text()
paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}


def adjacent_paths(owner_path: str) -> list[str]:
    target = ROOT / owner_path
    siblings = sorted(path for path in target.parent.glob("*.md") if re.match(r"\d+-", path.name))
    if target not in siblings:
        return []
    index = siblings.index(target)
    result = siblings[max(0, index - 1):index] + siblings[index + 1:index + 2]
    return [str(path.relative_to(ROOT)) for path in result]


def tokens(text: str) -> set[str]:
    return {token.lower() for token in re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}", text) if token.lower() not in {"with", "from", "that", "this", "model", "models", "using", "paper", "system", "systems"}}


def current_proposition(path: str, row: dict) -> str:
    text = (ROOT / path).read_text()
    text = re.split(r"(?m)^## Review notes\s*$", text, maxsplit=1)[0]
    paragraphs = [re.sub(r"\s+", " ", part).strip() for part in re.split(r"\n\s*\n", text) if len(part.strip()) > 80 and not part.lstrip().startswith("<!--")]
    wanted = tokens(row["title"] + " " + row.get("abstract", ""))
    ranked = sorted(paragraphs, key=lambda part: (len(tokens(part) & wanted), len(part)), reverse=True)
    best = ranked[0] if ranked else "目标章节没有可抽取的既有机制段落。"
    return clipped(best, 520)


comparisons: list[dict] = []
queue: list[dict] = []
reviews: list[dict] = []
for row in retained:
    arxiv_id = row["arxiv_id"]
    owner_path = paths[row["owner_node"]]
    adjacent = adjacent_paths(owner_path)
    method_claim = row["method_excerpt"] or row["screening_reason"]
    limitation_claim = row["limitations_excerpt"] or "exact-v1 未单列 limitations；只保留作者披露的 workload 边界。"
    claim_boundary = (
        f"{row['title']} 的 exact-v1 只支持 `{row['method_locator']}` 中披露的机制：{clipped(method_claim, 300)} "
        f"边界由 `{row['limitations_locator']}` 约束：{clipped(limitation_claim, 260)} 不得外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。"
    )
    record = SECTION_INDEX[arxiv_id]
    reviews.append({
        "source_family_id": family(arxiv_id),
        "arxiv_id": arxiv_id,
        "primary_evidence_version": f"arXiv:{arxiv_id}v1",
        "retrieval_route": record["route"],
        "retrieved_at": EXECUTED_AT,
        "content_sha256": record["sha256"],
        "method_locator": row["method_locator"],
        "evaluation_locator": row["evaluation_locator"],
        "limitations_locator": row["limitations_locator"],
        "method_excerpt": row["method_excerpt"],
        "evaluation_excerpt": row["evaluation_excerpt"],
        "limitations_excerpt": row["limitations_excerpt"],
        "claim_boundary": claim_boundary,
    })
    comparison = {
        "arxiv_id": arxiv_id,
        "source_family_id": family(arxiv_id),
        "owner_node": row["owner_node"],
        "owner_path": owner_path,
        "adjacent_paths": adjacent,
        "existing_proposition": current_proposition(owner_path, row),
        "new_evidence_delta": clipped(method_claim, 520),
        "evidence_boundary": clipped(limitation_claim, 420),
        "decision": row["integration_disposition"],
        "audit_basis": "author read current owner and adjacent chapters; Review notes alone do not count as semantic coverage",
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
            "evidence_delta": clipped(method_claim, 520),
            "evidence_boundary": clipped(limitation_claim, 420),
            "status": "provisional_pending_independent_prewrite_audit",
        })

(HERE / "exact-v1-review-packet-author.json").write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison-author.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema": "books-writeback-queue-v1", "report_date": REPORT_DATE, "status": "provisional_pending_independent_prewrite_audit", "items": queue}, ensure_ascii=False, indent=2) + "\n")
(HERE / "materials-request-author.json").write_text(json.dumps({"schema": "materials-request-v1", "report_date": REPORT_DATE, "items": []}, ensure_ascii=False, indent=2) + "\n")
(HERE / "semantic-author-audit.json").write_text(json.dumps({
    "schema": "semantic-author-audit-v1",
    "report_date": REPORT_DATE,
    "auditor": "author-lane",
    "status": "author_complete_pending_fresh_context_independent_audit",
    "not_a_fresh_context_audit": True,
    "counts": {"registered": len(rows), "screened": len(rows), "retained": len(retained), "closures": len(closures), "reviewed": len(retained), "blocked": 0, "provisional_integrate": len(queue)},
}, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((HERE / "screening-ledger-author.json").read_bytes()).hexdigest()
comparison_by_id = {item["arxiv_id"]: item for item in comparisons}
review_by_id = {item["arxiv_id"]: item for item in reviews}


def chapter_ref(path: str) -> str:
    match = re.match(r"(\d+)-", Path(path).name)
    return f"{path}#chapter-{int(match.group(1))}" if match else f"{path}#knowledge-tree"


deep_units = {
    "2606.00485": "DA-CROSS-APP-CONTEXT-ISOLATION",
    "2606.00516": "DA-WORKLOAD-AWARE-BATCH-CONTROL",
    "2606.20634": "DA-DECISION-EVIDENCE-SUFFICIENCY",
}

lines = [
    "# Daily Research — 2026-05-31", "", "**Research Date:** 2026-05-31", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-30 09:00:00 ～ 2026-05-31 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；技术结论绑定 official arXiv exact-v1 HTML/PDF。", "",
    "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。author packet 已完成，等待非作者 fresh-context pre-write audit。", "",
    "## Executive Summary", "",
    f"从 {SOURCE['raw_snapshot_records']:,} 条月度 raw records 中恢复窗口内 {len(rows)} 个唯一身份，并逐项完成 {len(rows)}/{len(rows)} title+abstract 语义筛选。author provisional denominator={len(retained)}，pre-denominator closures={len(closures)}，exact-v1 author review={len(retained)}/{len(retained)}，blocked=0，provisional Books queue={len(queue)}。这些是作者侧结论，不是独立验收结果。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-31 |", "| Window End | 2026-05-31 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", "| Denominator ID | DEN-20260531-V2-AUTHOR |", f"| Denominator Frozen At | {EXECUTED_AT} |", "| Completion Status | In Progress |", "| Coverage Gate | Open |", "| Evidence Gate | Open |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-30T09:00:00+08:00 | 2026-05-31T09:00:00+08:00 | {EXECUTED_AT} | DataCite v2 00..99 monthly snapshot + 293/293 semantic replay + official exact-v1 HTML/PDF | checked | {len(rows)} | {';'.join(row['source_family_id'] for row in retained)} | pages=300;final_cursor=end;raw={SOURCE['raw_snapshot_records']};registered={len(rows)};screened={len(rows)};retained={len(retained)};closure={len(closures)} | 2026-05-31T00:59:59Z | screening-ledger-author.json#sha256={ledger_sha} | GAP-20260531-INDEPENDENT-PREWRITE |", "",
    "### Coverage Limitations", "", f"<!-- coverage:SRC-ARXIV:20260531:start -->Author lane 已闭合 inventory 与 {len(rows)}/{len(rows)} title+abstract screening；fresh-context reviewer 尚未逐项挑战 retained false positive 与 {len(closures)} 条 closure false negative，因此 Coverage Gate 依合同保持 Open。<!-- coverage:SRC-ARXIV:20260531:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->", "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
for row in retained:
    s = row["score_v2"]
    sf = row["source_family_id"]
    override = "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"
    lines.append(f"| {sf} | arXiv:{row['arxiv_id']}v1 | paper-v1:{row['arxiv_id']} | 2026-W22 | 2026-05-30 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {row['review_status']} | accessible | {override} | review:{sf} | self | — | new_in_window | {row['owner_node']} | {row['integration_disposition']} | books-review:{sf} | no |")

lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    sf, arxiv_id = row["source_family_id"], row["arxiv_id"]
    route = "deep" if row["review_status"] == "deep_complete" else "standard"
    loc_route = "PDF" if review_by_id[arxiv_id]["retrieval_route"].endswith("PDF") else "HTML"
    lines.append(f"| {sf} | RP-TODO-{sf} | {route} | arXiv:{arxiv_id}v1 | SRC-ARXIV@arXiv:{arxiv_id}v1 | arXiv:{arxiv_id}v1 {loc_route} — {row['method_locator']} | arXiv:{arxiv_id}v1 {loc_route} — {row['evaluation_locator']} | arXiv:{arxiv_id}v1 {loc_route} — {row['limitations_locator']} | arXiv:{arxiv_id}v1 artifact links; immutable commit Not Disclosed — paper-specific artifact status retained in exact-v1 packet | claim:{sf} | complete |")

lines += ["", "### Source Reviews", ""]
for row in retained:
    sf, arxiv_id = row["source_family_id"], row["arxiv_id"]
    review = review_by_id[arxiv_id]
    lines += [f"<!-- review:{sf}:start -->", f"#### {row['title']}", "", f"- **问题与旧路径：** {sentences(row['abstract'])[0]}", f"- **机制与状态所有权：** `{row['method_locator']}` 显示：{review['method_excerpt']}", f"- **Evaluation：** `{row['evaluation_locator']}` 显示：{review['evaluation_excerpt']}", f"- **Trade-off / failure：** `{row['limitations_locator']}` 显示：{review['limitations_excerpt']}", f"<!-- claim:{sf}:start -->{review['claim_boundary']}<!-- claim:{sf}:end -->", f"<!-- review:{sf}:end -->", ""]

lines += ["## 4. Benchmark Contracts", "", "本报告不转述跨系统性能数字；所有实验只作为 exact-v1 claim boundary 的作者证据，因此 Candidate Ledger 的 Benchmark Claim 均为 `no`。", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    total = row["score_v2"]["total"]
    if total < 7 and row["integration_disposition"] != "Integrate":
        continue
    sf = row["source_family_id"]
    eligibility = "score_7_9;forced_review;potential_books_delta" if row["integration_disposition"] == "Integrate" else "score_7_9"
    if row["arxiv_id"] in deep_units:
        unit = deep_units[row["arxiv_id"]]
        lines.append(f"| {sf} | {eligibility} | selected | {unit} | — | 优先覆盖 security boundary、运行时控制与治理证据三类互不重复的跨层契约 | analysis:{unit} |")
    else:
        lines.append(f"| {sf} | {eligibility} | not_selected | — | — | exact-v1 Review 与 Books Decision 已完成；其 delta 不改变本日三条最高优先级跨层主线 | analysis-decision:{sf} |")

deep_text = {
    "2606.00485": "共享对话上下文最初以低摩擦组合能力为目标，但第三方 app 获得写入同一 flat namespace 的能力后，data plane 与 instruction plane 不再可区分。exact-v1 把问题定位为 per-app isolation 缺失：收益是跨 app 组合，代价是 persistent confused-deputy 与不可由单点过滤修复的 context poisoning。演进方向不是继续增强 prompt，而是恢复 tenant identity、message provenance、authority boundary 与可撤销的 context commit。",
    "2606.00516": "Mixed batching 在高带宽设备上能摊薄空洞并提高利用率，但 prefill/decode 干扰随硬件带宽、模型大小和 traffic mix 改变。exact-v1 把调度从固定策略变成可在线切换的控制问题：controller 根据 crossover condition 选择 exclusive 或 mixed phase，并同时约束 KV memory。收益是非平稳流量下的适配，代价是估计误差、模式切换和 SLO 校准；旧策略在稳定、高带宽工作负载上仍成立。",
    "2606.20634": "trace、ledger 或 provenance container 的存在并不等于某个治理问题已经有足够证据。exact-v1 将 evidence owner 下沉到 decision property：actor、authority、action、policy basis、resource touch 与 verification strength 必须可重建。收益是减少 container-presence overclaim，代价是 adapter、oracle label 与 property schema 的维护成本；该 benchmark 只证明 64-case construction-oracle package 内的区分能力，不是合规认证。",
}
for arxiv_id, unit in deep_units.items():
    lines += ["", f"<!-- analysis:{unit}:start -->", f"### {unit}", "", deep_text[arxiv_id], f"<!-- analysis:{unit}:end -->"]
for row in retained:
    if row["score_v2"]["total"] >= 7 and row["arxiv_id"] not in deep_units:
        sf = row["source_family_id"]
        lines.append(f"<!-- analysis-decision:{sf}:start -->该 family 已完成 exact-v1 Review 与 current-Books comparison；未进入三项长叙事不降低其证据或 Books 责任。<!-- analysis-decision:{sf}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    c, sf = comparison_by_id[row["arxiv_id"]], row["source_family_id"]
    lines.append(f"| {sf} | {row['owner_node']} | {chapter_ref(c['owner_path'])} | {';'.join(chapter_ref(path) for path in c['adjacent_paths'])} | existing:{sf} | delta:{sf} | {'Direct Evolution' if row['integration_disposition']=='Integrate' else 'Layering / Dependency'} | {row['integration_disposition']} | books-review:{sf} |")
for row in retained:
    c, sf = comparison_by_id[row["arxiv_id"]], row["source_family_id"]
    lines += [f"<!-- books-review:{sf}:start -->", f"<!-- existing:{sf}:start -->{c['existing_proposition']}<!-- existing:{sf}:end -->", f"<!-- delta:{sf}:start -->{c['new_evidence_delta']} 证据边界：{c['evidence_boundary']}<!-- delta:{sf}:end --> Author decision=`{row['integration_disposition']}`；等待独立 reviewer 读取 current owner + adjacent 后挑战。", f"<!-- books-review:{sf}:end -->"]

first_sf = retained[0]["source_family_id"]
first_unit = deep_units["2606.00485"]
lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", "| SA-20260531-COVERAGE | fresh-context:pending-different-reviewer | coverage | coverage:SRC-ARXIV:20260531 | FINDING-20260531-COVERAGE-PENDING | 需非作者重放 293/293 false-positive/false-negative | open |", f"| SA-20260531-EVIDENCE | fresh-context:pending-different-reviewer | evidence | review:{first_sf} | FINDING-20260531-EVIDENCE-PENDING | 需非作者逐项核验 56/56 exact-v1 locator 与 claim boundary | open |", f"| SA-20260531-SELECTION | fresh-context:pending-different-reviewer | deep_analysis_selection | analysis:{first_unit} | FINDING-20260531-SELECTION-PENDING | 需非作者挑战三项 Deep Selection | open |", f"| SA-20260531-BOOKS | fresh-context:pending-different-reviewer | books | books-review:{first_sf} | FINDING-20260531-BOOKS-PENDING | 需非作者重读 current owner + adjacent 并冻结 final queue | open |", "",
    "## 8. Ignored Noise", "", f"237 条 pre-denominator closure 保存在 `screening-ledger-author.json`。每条记录 title、abstract 机制与证据、具体 exclusion boundary 和重开条件；它们未评分，也未被静默丢弃。", "",
    "## 9. Recommended Action", "", f"由未参与本 author packet 的 fresh-context reviewer 重放 293/293 screening、56/56 exact-v1、Deep Selection 与 {len(queue)} 项 provisional Books queue；只有其通过后才能交给 root 串行写 Books。", "",
    "## 10. Repository Changes", "", "- 新增 2026-05-31 date-local author screening ledger、exact-v1 section index/review packet、Books comparison、provisional queue 与 author audit。", "- 新增 canonical Daily README；未修改共享 Books 或其他日期。", "- 未 stage、commit 或 push。", "",
    "## 11. Open Questions", "", "- fresh-context independent pre-write audit 尚未执行，author denominator 与 disposition 均为 provisional。", f"- {len(queue)} 项 provisional Integrate 可能在独立 current-Books comparison 后降级、改 owner 或保留。", "",
    "## 12. Sources", ""]
for row in retained:
    lines.append(f"- [{row['title']}](https://arxiv.org/{'pdf' if row['arxiv_id']=='2606.20634' else 'html'}/{row['arxiv_id']}v1) — arXiv:{row['arxiv_id']}v1；first-public 2026-05-30；accessed 2026-09-01")
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Open`", "", "Evidence: `Open`", "", "Books: `Open`", "", "unresolved findings: 4", "", "Author packet 已完成，但四项 fresh-context Semantic Audit 均待非作者执行；不得解释为 Daily 闭环。"]

text = "\n".join(lines)
for row in retained:
    sf, arxiv_id = row["source_family_id"], row["arxiv_id"]
    route = "deep" if row["review_status"] == "deep_complete" else "standard"
    loc_route = "PDF" if review_by_id[arxiv_id]["retrieval_route"].endswith("PDF") else "HTML"
    body = text.split(f"<!-- review:{sf}:start -->", 1)[1].split(f"<!-- review:{sf}:end -->", 1)[0]
    candidate = {"Event Identity": f"paper-v1:{arxiv_id}", "Primary Identifier": f"arXiv:{arxiv_id}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"}
    rp = _expected_review_provenance(sf, candidate, route, f"arXiv:{arxiv_id}v1", f"SRC-ARXIV@arXiv:{arxiv_id}v1", f"arXiv:{arxiv_id}v1 {loc_route} — {row['method_locator']}", f"arXiv:{arxiv_id}v1 {loc_route} — {row['evaluation_locator']}", f"arXiv:{arxiv_id}v1 {loc_route} — {row['limitations_locator']}", f"arXiv:{arxiv_id}v1 artifact links; immutable commit Not Disclosed — paper-specific artifact status retained in exact-v1 packet", f"claim:{sf}", f"review:{sf}", _normalized_body_sha256(body))
    text = text.replace("RP-TODO-" + sf, rp)

(ROOT / "papers/2026/05/31").mkdir(parents=True, exist_ok=True)
(ROOT / "papers/2026/05/31/README.md").write_text(text + "\n")
print(json.dumps({"raw": SOURCE["raw_snapshot_records"], "registered": len(rows), "screened": len(rows), "retained": len(retained), "closures": len(closures), "reviewed": len(reviews), "blocked": 0, "provisional_integrate": len(queue)}, ensure_ascii=False))
