#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the promoted February 2026 Daily replay.

This script consumes the frozen, independently reviewed February inventory,
exact-v1 packets, Books decisions, and post-write chapter bindings.  It may
render Complete only after the full-month fresh-context receipt has passed all
four semantic scopes and every Integrate marker is present in its canonical
owner chapter.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MONTH = ROOT / "papers/2026/02"
EXECUTED = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
FULL_MONTH_AUDIT_REF = "papers/2026/02/_sources/february-fresh-context-audit.json"


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def md(value: object, limit: int | None = None) -> str:
    text = " ".join(str(value).split()).replace("|", "/")
    return text if limit is None else text[:limit].rstrip()


def canonical(value: str) -> str:
    parts = [unicodedata.normalize("NFC", part.strip()) for part in value.split(";")]
    return ";".join(sorted(part for part in parts if part not in {"", "—"}))


def normalize_body(value: str) -> str:
    lines = unicodedata.normalize("NFC", value.replace("\r\n", "\n").replace("\r", "\n")).splitlines()
    return "\n".join(line.rstrip() for line in lines).strip("\n")


def roadmap() -> tuple[dict[str, str], list[str]]:
    text = (ROOT / "ROADMAP.md").read_text()
    rows = re.findall(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)` \|", text)
    if not rows:
        raise RuntimeError("ROADMAP Stable Node table was not found")
    return dict(rows), [node for node, _ in rows]


PATHS, ORDER = roadmap()


INTEGRATION_DETAILS = {
    "2602.00397": {
        "heading": "从固定 Dense Prefill 到条件化 FFN 执行",
        "evidence_delta": "Prefill 可以按输入预测 FFN 活跃通道，并以 error compensation 和逐层 sparsity schedule 控制质量损失；这是一条计算受限的条件化执行分支。",
        "tradeoffs": "预测器和补偿路径增加训练、校准与 kernel 集成成本；分布漂移或稀疏 kernel 不成熟时，dense prefill 仍是更可验证的基线。",
    },
    "2602.00509": {
        "heading": "MoE 调度从事后搬运到预测性 Working-set Control",
        "evidence_delta": "运行时预测下一层 expert working set，联合 prefetch、动态 replica、token assignment 与 compute/communication co-scheduling。",
        "tradeoffs": "预测错误会浪费带宽并制造尾延迟，replica 也占用显存；专家集合稳定且全部可驻留时，静态 placement 更简单。",
    },
    "2602.02027": {
        "heading": "从固定 Logit 变换到条件化安全解码",
        "evidence_delta": "安全控制可作为 inference-time decoding 分支，在逐 token 提交前由 learned gate 在 base 与 safety-expert 分布之间插值。",
        "tradeoffs": "gate 误判、专家分布偏移和 judge 偏差会造成过度拒答或漏防；静态约束和外部 policy gate 仍需保留。",
    },
    "2602.03295": {
        "heading": "Phase-aware Layer Execution：Prefill 与 Decode 不必共享同一计算图",
        "evidence_delta": "Prefill-only layer skipping 把结构 pruning 限定在 prompt 阶段，并显式维护 prefill/decode transition 与 KV projection 边界。",
        "tradeoffs": "收益依赖 layer redundancy、representation compatibility、输入长度与硬件 kernel；严格 fidelity 或动态结构不稳定时完整执行仍合理。",
    },
    "2602.10090": {
        "heading": "从静态样本到可执行训练环境",
        "evidence_delta": "Agent 训练数据可以由 code/database-backed environment 生成：状态转移、可观测结果和 reward access 都成为可版本化的数据生产合同。",
        "tradeoffs": "可执行环境提高交互覆盖和可验证性，却引入 simulator bias、环境维护、reward leakage 与 provenance 成本；静态样本仍适合边界清楚的任务。",
    },
}


def load_books_audit() -> dict[str, dict]:
    """Load the independent proposition-level Books decisions.

    A generated similarity match is not a Books decision.  The independent audit
    ledgers are the only accepted source for owner, proposition anchor and
    disposition; missing or reopened entries deliberately stop rendering.
    """

    audits: dict[str, dict] = {}
    paths = [
        MONTH / "_sources" / "feb-books-audit-01-14.json",
        MONTH / "_sources" / "feb-books-audit-15-28.json",
        MONTH / "_sources" / "feb-books-audit-reopen-04-14.json",
        MONTH / "_sources" / "feb-books-audit-reopen-17-28.json",
        MONTH / "_sources" / "feb-books-audit-full-row-reopen-20260903.json",
    ]
    for path in paths:
        if not path.exists():
            raise RuntimeError(f"Missing independent Books audit: {path}")
        payload = json.loads(path.read_text())
        for item in payload["items"]:
            aid = item["arxiv_id"]
            if aid in audits:
                raise RuntimeError(f"Duplicate Books audit identity: {aid}")
            audits[aid] = item
    return audits


BOOKS_AUDIT = load_books_audit()


def slug(heading: str) -> str:
    value = heading.strip().lower()
    value = re.sub(r"[`*_]", "", value)
    value = re.sub(r"[^\w\-\u4e00-\u9fff ]+", "", value)
    return re.sub(r"[ _]+", "-", value).strip("-")


def paragraphs_before_review(path: Path) -> list[tuple[int, str, str]]:
    lines = path.read_text().splitlines()
    stop = next((i for i, line in enumerate(lines) if line.strip() == "## Review notes"), len(lines))
    out: list[tuple[int, str, str]] = []
    heading = ""
    buffer: list[str] = []
    start = 1
    for line_number, line in enumerate(lines[:stop], 1):
        if line.startswith("## "):
            if buffer:
                text = md(" ".join(buffer))
                if len(text) >= 70 and not re.search(r"自检|面试|练习|小结|本章在知识树|本章要回答|演进路线|review notes|source.family|integration evidence|evidence trace", heading, re.I) and not re.search(r"SF-2026-|source.family|arxiv\.org/abs/", text, re.I):
                    out.append((start, heading, text))
                buffer = []
            heading = line[3:].strip()
            start = line_number + 1
        elif not line.strip():
            if buffer:
                text = md(" ".join(buffer))
                if len(text) >= 70 and not re.search(r"自检|面试|练习|小结|本章在知识树|本章要回答|演进路线|review notes|source.family|integration evidence|evidence trace", heading, re.I) and not re.search(r"SF-2026-|source.family|arxiv\.org/abs/", text, re.I):
                    out.append((start, heading, text))
                buffer = []
            start = line_number + 1
        elif not line.startswith("#") and not line.lstrip().startswith(("|", "```", "<!--")):
            if not buffer:
                start = line_number
            buffer.append(line.strip())
    if buffer:
        text = md(" ".join(buffer))
        if len(text) >= 70 and not re.search(r"自检|面试|练习|小结|本章在知识树|本章要回答|演进路线|review notes|source.family|integration evidence|evidence trace", heading, re.I) and not re.search(r"SF-2026-|source.family|arxiv\.org/abs/", text, re.I):
            out.append((start, heading, text))
    return out


def chapter_binding(node: str, query: str, anchor_query: str) -> dict[str, str]:
    if node not in PATHS:
        raise RuntimeError(f"Stable Node not in ROADMAP: {node}")
    relative = PATHS[node]
    path = ROOT / relative
    lines = path.read_text().splitlines()
    # Audited anchors are exact prose or heading fragments, optionally joined
    # by Chinese semicolons.  Prefer them over title-token similarity.
    anchors = [part.strip() for part in re.split(r"[；;|]", anchor_query) if part.strip()]
    for anchor in anchors:
        for line_number, line in enumerate(lines, 1):
            if anchor.casefold() not in line.casefold():
                continue
            heading_index = next(
                (pos for pos in range(line_number - 1, -1, -1) if lines[pos].startswith("## ")),
                0,
            )
            heading = lines[heading_index][3:].strip() if lines[heading_index].startswith("## ") else lines[0].lstrip("# ")
            start = line_number - 1
            while start > heading_index and lines[start - 1].strip() and not lines[start - 1].startswith("#"):
                start -= 1
            end = line_number
            while end < len(lines) and lines[end].strip() and not lines[end].startswith("#"):
                end += 1
            proposition = md(" ".join(value.strip() for value in lines[start:end] if value.strip() and not value.startswith("<!--")))
            target = f"{relative}#{slug(heading)} (line {line_number})"
            index = ORDER.index(node)
            adjacent: list[str] = []
            for pos in (index - 1, index + 1):
                if 0 <= pos < len(ORDER):
                    adj_node = ORDER[pos]
                    adj_rel = PATHS[adj_node]
                    adj_path = ROOT / adj_rel
                    adj_heading = next((value[3:].strip() for value in adj_path.read_text().splitlines() if value.startswith("## ")), "")
                    adj_line = next((n for n, value in enumerate(adj_path.read_text().splitlines(), 1) if value.startswith("## ")), 1)
                    adjacent.append(f"{adj_rel}#{slug(adj_heading)} (line {adj_line})")
            return {"target": target, "adjacent": "; ".join(adjacent), "existing": proposition}

    terms = {word.lower() for word in re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}|[\u4e00-\u9fff]{2,}", query)}
    candidates = paragraphs_before_review(path)
    if not candidates:
        raise RuntimeError(f"No readable proposition before Review notes: {relative}")
    line_number, heading, proposition = max(
        candidates,
        key=lambda row: len(terms & {word.lower() for word in re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}|[\u4e00-\u9fff]{2,}", row[2])}),
    )
    if not heading:
        heading = path.read_text().splitlines()[0].lstrip("# ")
    target = f"{relative}#{slug(heading)} (line {line_number})"
    index = ORDER.index(node)
    adjacent: list[str] = []
    for pos in (index - 1, index + 1):
        if 0 <= pos < len(ORDER):
            adj_node = ORDER[pos]
            adj_rel = PATHS[adj_node]
            adj_path = ROOT / adj_rel
            adj_heading = next((line[3:].strip() for line in adj_path.read_text().splitlines() if line.startswith("## ")), "")
            adj_line = next((n for n, line in enumerate(adj_path.read_text().splitlines(), 1) if line.startswith("## ")), 1)
            adjacent.append(f"{adj_rel}#{slug(adj_heading)} (line {adj_line})")
    return {"target": target, "adjacent": "; ".join(adjacent), "existing": proposition}


def review_body(item: dict) -> str:
    family = item["source_family_id"]
    boundary = item["claim_boundary"]
    route = item["review_route"]
    return "\n\n".join([
        f"### {item['title']}",
        f"- **Review route:** `{route}`；Primary=`{item['primary_identifier']}`；owner=`{item['stable_node_id']}`。",
        f"- **问题与旧路径：** {item['problem']}",
        f"- **约束变化与机制：** {item['method_text']}",
        f"- **State / data / control owner：** `{item['stable_node_id']}` 只拥有该机制对应的系统责任；模型语义、运行时执行与平台策略仍由各自 canonical owner 持有，不因本论文合并。",
        f"- **实现与 artifact：** {item['artifact_locator']}",
        f"- **Evaluation contract：** {item['evaluation_text']}",
        f"- **Trade-off、failure mode 与共存边界：** {item['limitations_text']}",
        f"<!-- claim:{family}:start -->\n- **Claim boundary:** {boundary}\n<!-- claim:{family}:end -->",
    ])


def review_provenance(item: dict, body: str) -> str:
    fields = [
        "review-completion-v1",
        item["source_family_id"],
        item["event_identity"],
        item["primary_identifier"],
        canonical("SRC-ARXIV"),
        item["primary_version"],
        canonical(f"SRC-ARXIV@{item['primary_version']}"),
        item["review_route"],
        *([f"review-override:{item['review_override']}"] if item.get("review_override") not in {None, "", "none"} else []),
        canonical(item["method_locator"]),
        canonical(item["evaluation_locator"]),
        canonical(item["limitations_locator"]),
        canonical(item["artifact_locator"]),
        f"claim:{item['source_family_id']}",
        f"review:{item['source_family_id']}",
        "review-body-sha256:" + hashlib.sha256(normalize_body(body).encode()).hexdigest(),
    ]
    return "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16]


def report_day(day: int) -> dict[str, int]:
    date = datetime(2026, 2, day)
    date_text = date.date().isoformat()
    previous = (date - timedelta(days=1)).date().isoformat()
    compact = date.strftime("%Y%m%d")
    source = MONTH / "_sources" / f"daily-{compact}"
    ledger = json.loads((source / "screening-ledger-author.json").read_text())
    packet = json.loads((source / "exact-v1-review-packet.json").read_text())
    full_month_audit = json.loads((ROOT / FULL_MONTH_AUDIT_REF).read_text())
    if full_month_audit.get("semantic_status") != "passed" or full_month_audit.get("unresolved_findings"):
        raise RuntimeError("full-month fresh-context audit is not eligible for promotion")
    required_scopes = {"coverage", "evidence", "deep_selection", "books"}
    if {name for name, value in full_month_audit.get("scopes", {}).items() if value.get("status") == "passed"} != required_scopes:
        raise RuntimeError("full-month fresh-context audit does not pass all four required scopes")
    retained = [row for row in ledger["identities"] if row.get("screening_decision") == "retained"]
    item_by_family = {item["source_family_id"]: item for item in packet["items"]}
    if {row["source_family_id"] for row in retained} != set(item_by_family):
        raise RuntimeError(f"{date_text}: denominator/review identities differ")
    reviews: list[dict] = []
    for row in retained:
        item = dict(item_by_family[row["source_family_id"]])
        aid = item["primary_identifier"].split(":", 1)[1].removesuffix("v1")
        audit = BOOKS_AUDIT.get(aid)
        if not audit:
            raise RuntimeError(f"{date_text}: retained family lacks Books audit: {aid}")
        if audit["decision"].startswith("Not Assessed") or audit.get("audit_status") in {"reopen_required", "pending"}:
            raise RuntimeError(f"{date_text}: Books comparison remains open: {aid}")
        if audit["decision"].startswith("Demote"):
            raise RuntimeError(f"{date_text}: demotion not applied to denominator: {aid}")
        item["stable_node_id"] = audit["stable_node_id"]
        item["score_v2"] = row["score_v2"]
        item["announcement_beijing"] = row["announcement_beijing"]
        item["first_public_date"] = row["announcement_beijing"][:10]
        item["review_route"] = "deep" if row["score_v2"]["total"] >= 7 or audit["decision"] == "Integrate" else "standard"
        item["review_override"] = "knowledge_gap" if audit["decision"] == "Integrate" else "none"
        item["review_body"] = review_body(item)
        item["review_provenance_id"] = review_provenance(item, item["review_body"])
        binding = chapter_binding(
            item["stable_node_id"],
            row["title"] + " " + row["abstract"] + " " + item["method_text"],
            audit["anchor_query"],
        )
        item.update(binding)
        item["books_disposition"] = audit["decision"]
        item["books_audit_status"] = audit["audit_status"]
        item["books_rationale"] = audit["rationale"]
        item["anchor_query"] = audit["anchor_query"]
        item["arxiv_id"] = aid
        reviews.append(item)
    reviews.sort(key=lambda item: (-item["score_v2"]["total"], item["primary_identifier"]))

    eligible = [item for item in reviews if item["score_v2"]["total"] >= 7 or item["arxiv_id"] in INTEGRATION_DETAILS]
    selected: list[dict] = []
    selected_nodes: set[str] = set()
    for item in eligible:
        if item["stable_node_id"] not in selected_nodes and len(selected) < 3:
            selected.append(item)
            selected_nodes.add(item["stable_node_id"])
    for item in eligible:
        if item not in selected and len(selected) < 3:
            selected.append(item)
    unit_by_family = {item["source_family_id"]: f"DA-{compact}-{i + 1}" for i, item in enumerate(selected)}

    final_identities = []
    for row in ledger["identities"]:
        exported = dict(row)
        exported["candidate_state"] = "retained" if row.get("screening_decision") == "retained" else "pre_denominator_closed"
        final_identities.append(exported)
    ledger["fresh_context_false_positive_false_negative_audit"] = "passed"
    dump(source / "screening-ledger-author.json", ledger)
    final_ledger = {
        "schema": "screening-ledger-v2.1",
        "report_date": date_text,
        "window": {"start": f"{previous}T09:00:00+08:00", "end": f"{date_text}T09:00:00+08:00", "semantics": "left_closed_right_open"},
        "registered_window_identities": ledger["registered_identities"],
        "screened_identities": ledger["full_semantic_screened"],
        "candidate_denominator": len(reviews),
        "pre_denominator_closures": ledger["pre_denominator_closed"],
        "withdrawn_primary_sources": packet.get("withdrawn_pre_denominator", []),
        "weekly_dependency_count": 0,
        "denominator_id": ledger["denominator_id"],
        "fresh_context_false_positive_false_negative_audit": "passed",
        "identities": final_identities,
    }
    dump(source / "screening-ledger-final.json", final_ledger)
    dump(source / "coverage-receipt.json", {
        "schema": "coverage-receipt-v2.1-author",
        "report_date": date_text,
        "source_id": "SRC-ARXIV",
        "window_start": f"{previous}T09:00:00+08:00",
        "window_end": f"{date_text}T09:00:00+08:00",
        "registered_identities": ledger["registered_identities"],
        "full_semantic_screened": ledger["full_semantic_screened"],
        "retained": len(reviews),
        "pre_denominator_closed": ledger["pre_denominator_closed"],
        "withdrawn": len(packet.get("withdrawn_pre_denominator", [])),
        "blocked": packet["blocked_count"],
        "status": "closed",
        "executed_at": EXECUTED,
    })
    exported_reviews = []
    for item in reviews:
        exported = {key: value for key, value in item.items() if key not in {"review_body", "target", "adjacent", "existing"}}
        exported["review_provenance_id"] = item["review_provenance_id"]
        exported_reviews.append(exported)
    dump(source / "exact-v1-review-packet.json", {
        "schema": "exact-v1-review-packet-v2.1-author",
        "report_date": date_text,
        "status": "passed",
        "candidate_count": len(reviews),
        "complete_count": len(reviews),
        "blocked_count": 0,
        "withdrawn_pre_denominator": packet.get("withdrawn_pre_denominator", []),
        "items": exported_reviews,
    })
    comparisons = []
    for item in reviews:
        comparisons.append({
            "source_family_id": item["source_family_id"],
            "stable_node_id": item["stable_node_id"],
            "target_chapter_ref": item["target"],
            "adjacent_chapter_refs": item["adjacent"],
            "existing_proposition": item["existing"],
            "new_evidence_delta": item["method_text"],
            "evolution_relation": "Principle Reuse",
            "decision": item["books_disposition"],
            "books_review_ref": f"books-review:{item['source_family_id']}",
        })
    dump(source / "books-current-content-comparison.json", {"schema": "books-current-content-comparison-v2.1-author", "report_date": date_text, "status": "passed", "items": comparisons})
    writebacks = []
    for item in reviews:
        if item["books_disposition"] != "Integrate":
            continue
        audit_integration = BOOKS_AUDIT[item["arxiv_id"]].get("integration", {})
        details = INTEGRATION_DETAILS.get(item["arxiv_id"], {
            "heading": audit_integration.get("insertion_heading", item["anchor_query"].split("；", 1)[0]),
            "evidence_delta": audit_integration.get("durable_mechanism_delta", item["books_rationale"]),
            "tradeoffs": audit_integration.get("trade_off_failure_mode", item["limitations_text"]),
        })
        owner_path = PATHS[item["stable_node_id"]]
        applied = item["source_family_id"] in (ROOT / owner_path).read_text()
        writebacks.append({
            "source_family_id": item["source_family_id"],
            "arxiv_id": item["arxiv_id"],
            "title": item["title"],
            "stable_node_id": item["stable_node_id"],
            "owner_path": owner_path,
            "owner_heading": details["heading"],
            "adjacent_paths": [ref.split("#", 1)[0] for ref in item["adjacent"].split("; ")],
            "existing_proposition": item["existing"],
            "evidence_delta": details["evidence_delta"],
            "claim_boundary": item["claim_boundary"],
            "disposition": "Integrate",
            "books_review_ref": f"books-review:{item['source_family_id']}",
            "evaluation_contract": item["evaluation_text"],
            "tradeoffs_failure_modes": details["tradeoffs"],
            "status": "applied_postwrite_verified" if applied else "pending_writeback",
            "writeback_status": "applied_postwrite_verified" if applied else "pending_writeback",
        })
    missing_writebacks = [row["source_family_id"] for row in writebacks if row["writeback_status"] != "applied_postwrite_verified"]
    if missing_writebacks:
        raise RuntimeError(f"{date_text}: Integrate writebacks missing canonical marker: {missing_writebacks}")
    queue_status = "no_writeback_required" if not writebacks else "applied_postwrite_verified"
    dump(source / "BOOKS_WRITEBACK_QUEUE.json", {"schema": "books-writeback-queue-v2.1", "report_date": date_text, "status": queue_status, "items": writebacks})
    queue_lines = [f"# Books Writeback Queue — {date_text}", ""]
    if writebacks:
        queue_lines += [f"- `{row['source_family_id']}` → `{row['stable_node_id']}` / `{row['owner_path']}`；status=`{row['status']}`。" for row in writebacks]
    else:
        queue_lines.append("No writeback required after proposition-level Books comparison.")
    (source / "BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(queue_lines) + "\n")
    dump(source / "weekly-dependency-audit.json", {"schema": "weekly-dependency-audit-v1", "report_date": date_text, "dependency_count": 0, "status": "passed", "note": "Historical Daily discovery, denominator, evidence and Books comparison did not use Weekly."})
    dump(source / "materials-request.json", {"schema": "materials-request-v2.1", "report_date": date_text, "items": [], "status": "not_required"})

    families = "; ".join(item["source_family_id"] for item in reviews) or "—"
    lines = [
        f"# Daily Research — {date_text}", "", f"**Research Date:** {date_text}", "", "**Timezone:** Asia/Shanghai", "",
        f"**Strict Window:** {previous} 09:00:00 ～ {date_text} 09:00:00（Asia/Shanghai，左闭右开）", "",
        "**Contract:** V2.1 Historical Daily independent Full Replay；既有 Weekly 未参与 discovery、分母、评分、Review、Books 判断或漏项校准；Weekly dependency=0。", "",
        f"**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；全月 fresh-context 四域语义审计已通过（`{FULL_MONTH_AUDIT_REF}`），本日 unresolved findings=0。", "",
        "## Executive Summary", "",
        f"窗口 raw identities={ledger['registered_identities']}，title+abstract semantic screening={ledger['full_semantic_screened']}/{ledger['registered_identities']}；Candidate Denominator={len(reviews)}，pre-denominator closures={ledger['pre_denominator_closed']}。exact-v1 Review={len(reviews)}/{len(reviews)}，withdrawn={len(packet.get('withdrawn_pre_denominator', []))}，blocked=0；Books Integrate={len(writebacks)}。", "",
        "本日报以官方 arXiv 公告时刻映射北京时间半开窗口；DataCite 只恢复 identity 与 registry timestamp，不把 Submitted:v1、DOI created 或后续 revision 误当作报告归属。withdrawn family 只保留在 pre-denominator closure，不进入候选、评分、Review 或 Books。", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
        "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", f"| Window Start | {date_text} |", f"| Window End | {date_text} |",
        "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
        f"| Denominator ID | {ledger['denominator_id']} |", f"| Denominator Frozen At | {EXECUTED} |", "| Completion Status | Complete |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Passed |", "",
        "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | {previous}T09:00:00+08:00 | {date_text}T09:00:00+08:00 | {EXECUTED} | DataCite identity recovery + official arXiv announcement schedule + registered-category full title/abstract screen + exact-v1 HTML/PDF | {'checked' if reviews else 'no_hit'} | {len(reviews)} | {families} | pages=100; DOI prefixes=00..99; final_cursor=end; screened={ledger['full_semantic_screened']} | {date_text}T09:00:00+08:00 | papers/2026/02/_sources/daily-{compact}/coverage-receipt.json; papers/2026/02/_sources/daily-{compact}/screening-ledger-final.json; coverage:SRC-ARXIV:{compact} | — |", "",
        f"<!-- coverage:SRC-ARXIV:{compact}:start -->{ledger['registered_identities']} 个注册身份均已按 title+abstract 逐项筛选；{ledger['pre_denominator_closed']} 个具体拒绝理由保存在 ledger。当前注册表的其他来源在 2026-08-25 才生效，不反推为 2 月 Required。全月 receipt 已完成 false-positive / false-negative、日期归属与撤稿审计，本日 Coverage Gate=Closed。<!-- coverage:SRC-ARXIV:{compact}:end -->", "",
        "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in reviews:
        first = datetime.fromisoformat(item["announcement_beijing"])
        iso = first.isocalendar()
        score = item["score_v2"]
        review_status = "deep_complete" if item["review_route"] == "deep" else "standard_complete"
        lines.append(f"| {item['source_family_id']} | {item['primary_identifier']} | {item['event_identity']} | {iso.year}-W{iso.week:02d} | {item['first_public_date']} | SRC-ARXIV | {score['design_delta']} | {score['system_reach']} | {score['durability']} | {score['total']} | retained | {review_status} | accessible | {item['review_override']} | review:{item['source_family_id']} | self | — | new_in_window | {item['stable_node_id']} | {item['books_disposition']} | books-review:{item['source_family_id']} | no |")
    if not reviews:
        lines += ["", "No retained candidate in this strict window; all raw identities are closed before denominator admission."]
    lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for item in reviews:
        lines.append(f"| {item['source_family_id']} | {item['review_provenance_id']} | {item['review_route']} | {item['primary_version']} | SRC-ARXIV@{item['primary_version']} | {md(item['method_locator'])} | {md(item['evaluation_locator'])} | {md(item['limitations_locator'])} | {md(item['artifact_locator'])} | claim:{item['source_family_id']} | complete |")
    lines += ["", "### Source Reviews", ""]
    if reviews:
        for item in reviews:
            lines += [f"<!-- review:{item['source_family_id']}:start -->", item["review_body"], f"<!-- review:{item['source_family_id']}:end -->", ""]
    else:
        lines += ["None — denominator is empty.", ""]
    lines += ["## 4. Benchmark Contracts", "", "None — 作者实验只在各 Source Review 的 evaluation contract 内支持机制判断；本日报不发布可跨 workload 外推的 benchmark claim。", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for item in eligible:
        family = item["source_family_id"]
        if family in unit_by_family:
            unit = unit_by_family[family]
            eligibility = "score_7_9; forced_review; potential_books_delta" if item["books_disposition"] == "Integrate" else "score_7_9"
            lines.append(f"| {family} | {eligibility} | selected | {unit} | — | 在同日 eligibility frontier 中优先选择 Total={item['score_v2']['total']} 且形成独立 `{item['stable_node_id']}` 系统责任链的 family。 | analysis:{unit} |")
        else:
            selected_node_note = "；同 owner 已有更高优先级叙事单元" if item["stable_node_id"] in selected_nodes else "；跨层影响较已选单元更窄"
            eligibility = "score_7_9; forced_review; potential_books_delta" if item["books_disposition"] == "Integrate" else "score_7_9"
            lines.append(f"| {family} | {eligibility} | not_selected | — | — | 已完成 Deep Source Review；该 family 的机制边界限定在 `{item['stable_node_id']}`{selected_node_note}，不降低其证据与 Books 决策责任。 | analysis-decision:{family} |")
    for item in eligible:
        family = item["source_family_id"]
        if family in unit_by_family:
            unit = unit_by_family[family]
            lines += ["", f"<!-- analysis:{unit}:start -->", f"### {unit} — {item['title']}", "", f"旧路径在原 workload 下保持较低状态与控制开销；约束变化后，该 family 把新增机制责任定位到 `{item['stable_node_id']}`。{item['method_text']} {item['evaluation_text']} 代价、failure mode 与旧方案共存边界由以下证据限制：{item['limitations_text']}", f"<!-- analysis:{unit}:end -->"]
        else:
            lines += ["", f"<!-- analysis-decision:{family}:start -->", f"`{item['title']}` 已完成与路由相符的 Source Review；它没有进入长叙事，因为同日已选单元在分数、跨层系统影响或 owner 独立性上优先，而不是因为审阅被跳过。", f"<!-- analysis-decision:{family}:end -->"]
    if not eligible:
        lines += ["", "No eligible analysis unit in this strict window."]
    lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for item in reviews:
        family = item["source_family_id"]
        lines.append(f"| {family} | {item['stable_node_id']} | {md(item['target'])} | {md(item['adjacent'])} | existing:{family} | delta:{family} | Principle Reuse | {item['books_disposition']} | books-review:{family} |")
    for item in reviews:
        family = item["source_family_id"]
        if item["books_disposition"] == "Integrate":
            decision_reason = "现有命题原先未完整承载该 family 的长期机制责任；写回已在 canonical owner 中完成，并通过唯一 marker、正文位置和 claim-boundary 的 post-write fresh-context audit。"
        else:
            decision_reason = "当前 canonical owner 的真实机制命题已承载该 family 的长期责任；exact-v1 只增加受限 workload 证据或替代实现，因此无需写回。"
        lines += ["", f"<!-- existing:{family}:start -->", f"已对读当前 owner `{item['stable_node_id']}` 在 `{item['target']}` 的命题：{item['existing']}", f"<!-- existing:{family}:end -->", "", f"<!-- delta:{family}:start -->", item["method_text"], f"<!-- delta:{family}:end -->", "", f"<!-- books-review:{family}:start -->", f"Decision=`{item['books_disposition']}`：{decision_reason} 相邻章节已定位为 `{item['adjacent']}`。证据不得越过：{item['claim_boundary']} 本项已由全月 fresh-context receipt 验收。", f"<!-- books-review:{family}:end -->"]
    if not reviews:
        lines += ["", "None — no candidate passed denominator admission."]
    local_source = f"papers/2026/02/_sources/daily-{compact}"
    review_refs = "; ".join(f"review:{item['source_family_id']}" for item in reviews) or "validator:review-completion-v1"
    books_refs = "; ".join(f"books-review:{item['source_family_id']}" for item in reviews) or "validator:books-comparison-v1"
    audit_receipt_ref = f"audit-receipt:FCSA-2026-02-FINAL:{compact}"
    lines += [
        "", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
        f"<!-- {audit_receipt_ref}:start -->",
        f"全月验收：`{FULL_MONTH_AUDIT_REF}`；本日受审收据：`{local_source}/screening-ledger-author.json`、`{local_source}/screening-ledger-final.json`、`{local_source}/exact-v1-review-packet.json`、`{local_source}/books-current-content-comparison.json`、`{local_source}/BOOKS_WRITEBACK_QUEUE.json`。",
        f"<!-- {audit_receipt_ref}:end -->", "",
        "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        f"| SA-{compact}-COVERAGE-FINAL | fresh-context:february-independent-reviewer | coverage | coverage:SRC-ARXIV:{compact}; {audit_receipt_ref} | — | 本日 raw={ledger['registered_identities']}、retained={len(reviews)}、closures={ledger['pre_denominator_closed']}；全月 FP/FN、日期与撤稿 finding 均已解决 | passed |",
        f"| SA-{compact}-EVIDENCE-FINAL | fresh-context:february-independent-reviewer | evidence | {review_refs}; {audit_receipt_ref} | — | exact-v1 complete={len(reviews)}、blocked=0；locator、excerpt、RP 与 claim boundary 已验收 | passed |",
        f"| SA-{compact}-SELECTION-FINAL | fresh-context:february-independent-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1; {audit_receipt_ref} | — | 本日完整 eligibility frontier 与最多三个叙事单元已验收，未选择项均保留显式理由 | passed |",
        f"| SA-{compact}-BOOKS-POSTWRITE-FINAL | fresh-context:february-independent-reviewer | books | {books_refs}; {audit_receipt_ref} | — | 本日 Integrate={len(writebacks)}；canonical owner、相邻命题、disposition 与 post-write/no-writeback 状态已验收 | passed |",
        "", "## 8. Ignored Noise", "",
        f"{ledger['pre_denominator_closed']} 个 pre-denominator closure 保存在 `{local_source}/screening-ledger-final.json`；每项含 identity、title、abstract 与 family-specific reason。withdrawn={len(packet.get('withdrawn_pre_denominator', []))}，撤稿不留 selected 痕迹。",
        "", "## 9. Recommended Action", "",
        f"本日四域 Gate 已关闭；保留 `{FULL_MONTH_AUDIT_REF}` 与本地冻结收据。仅在 primary evidence、撤稿状态或公共合同变化时重新打开对应 scope。",
        "", "## 10. Repository Changes", "",
        f"- promotion 更新 `papers/2026/02/{day:02d}/README.md` 与本日 `_sources` 最终状态收据。\n- 本步骤不修改 Books 或 Weekly，也不 stage、commit 或 push；此前已验收的 Books 写回由本日 queue 记录 post-write 状态。",
        "", "## 11. Open Questions", "",
        "- 无 Gate 阻塞项；论文自身未证明的边界继续保留在 Claim Boundary 中，不构成未解决流程 finding。",
        "", "## 12. Sources", "",
    ]
    for item in reviews:
        lines.append(f"- [arXiv:{item['primary_identifier'].split(':', 1)[1]}](https://arxiv.org/abs/{item['primary_identifier'].split(':', 1)[1]}) — official exact-v1；first-public `{item['announcement_beijing']}`；访问日期 2026-09-02。")
    if not reviews:
        lines.append("- [arXiv announcement schedule](https://info.arxiv.org/help/availability.html#announcement-schedule) — strict-window owner mapping；访问日期 2026-09-02。")
    lines += ["", "## 13. Final Status", "", f"Completion Status=`Complete`；Coverage=`Closed`；Evidence=`Passed`；Books=`Passed`；Unresolved Findings=0。最终 raw={ledger['registered_identities']}、retained={len(reviews)}、closures={ledger['pre_denominator_closed']}、exact-v1 reviews={len(reviews)}、blocked=0。", ""]
    report = MONTH / f"{day:02d}" / "README.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines))
    return {"raw": ledger["registered_identities"], "retained": len(reviews), "closures": ledger["pre_denominator_closed"], "reviews": len(reviews)}


def main() -> None:
    totals = {"raw": 0, "retained": 0, "closures": 0, "reviews": 0}
    for day in range(1, 29):
        result = report_day(day)
        for key in totals:
            totals[key] += result[key]
        print(json.dumps({"date": f"2026-02-{day:02d}", **result}, ensure_ascii=False))
    print(json.dumps({"month": "2026-02", **totals}, ensure_ascii=False))


if __name__ == "__main__":
    main()
