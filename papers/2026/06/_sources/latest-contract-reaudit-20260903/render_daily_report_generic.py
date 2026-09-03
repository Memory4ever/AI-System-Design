#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render a frozen author-side V2.1 Historical Daily without writing Books."""

from __future__ import annotations

import argparse
import gzip
import importlib.util
import json
import re
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent


def helper():
    path = HERE / "render_day_20260713_report.py"
    spec = importlib.util.spec_from_file_location("daily_render_helpers", path)
    module = importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(module)
    return module


H = helper()


def gz(path: Path) -> dict:
    with gzip.open(path, "rt", encoding="utf-8") as f: return json.load(f)


def reviews(packet: Path) -> dict[str, dict]:
    out = {}
    for path in sorted(packet.glob("source-review-batch-*-v2.1.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("status") != "complete": raise RuntimeError(f"incomplete batch {path}")
        for item in payload["reviews"]: out[item["source_family_id"]] = item
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("date", help="YYYY-MM-DD")
    ap.add_argument("--selected", nargs=3, required=True, help="three arXiv IDs")
    args = ap.parse_args()
    d = date.fromisoformat(args.date); prev = d - timedelta(days=1); compact = args.date.replace("-", "")
    packet = ROOT / f"papers/{d.year:04d}/{d.month:02d}/_sources/daily-{compact}"
    report = ROOT / f"papers/{d.year:04d}/{d.month:02d}/{d.day:02d}/README.md"
    month_queue_path = ROOT / f"papers/{d.year:04d}/{d.month:02d}/_sources/BOOKS_WRITEBACK_QUEUE_latest-contract.json"
    raw = gz(packet / "canonical-raw-identity-inventory-v2.1.json.gz")
    semantic = gz(packet / "fresh-context-semantic-decisions-v2.1.json.gz")
    denom_path = packet / "candidate-denominator-v2.1.json"; denom = json.loads(denom_path.read_text())
    revs = reviews(packet); admissions = {x["source_family_id"]: x for x in semantic["items"] if x["decision"] == "retain_in_candidate_denominator"}
    raw_by_id = {x["arxiv_id"]: x for x in raw["identities"]}
    if set(revs) != set(admissions): raise RuntimeError("review set differs from denominator")
    selected = {f"SF-2026-ARXIV-{aid.replace('.', '-')}": f"DA-{compact}-{i:02d}" for i, aid in enumerate(args.selected, 1)}
    if set(selected) - set(revs): raise RuntimeError("selected family absent")

    candidates, receipts, bodies, titles = {}, {}, {}, {}
    for family in sorted(revs):
        rv, admission = revs[family], admissions[family]
        aid = rv["primary_evidence"].removeprefix("arXiv:").removesuffix("v1"); titles[family] = raw_by_id[aid]["title"]
        score = rv["score_v2"]; override = admission.get("review_override", "none")
        route = "deep" if score["total"] >= 7 or override != "none" else "standard"
        candidate = {"Source Family ID": family, "Primary Identifier": f"arXiv:{aid}v1", "Event Identity": f"paper-v1:{aid}", "Owner Week": f"{d.isocalendar().year}-W{d.isocalendar().week:02d}", "First-public Date": args.date, "Supporting Source IDs": "SRC-ARXIV", "Design Delta": str(score["design_delta"]), "System Reach": str(score["system_reach"]), "Durability": str(score["durability"]), "Total": str(score["total"]), "Candidate State": "retained", "Review Status": f"{route}_complete", "Access Status": "accessible", "Review Override": override, "Review Ref": f"review:{family}", "Owner Report Ref": "self", "Prior Review Ref": "—", "Reconciliation": "new_in_window", "Stable Node ID": rv["stable_node_id"], "Books Disposition": "Not Assessed", "Books Review Ref": "—", "Benchmark Claim": "no"}
        artifact = rv["artifact_boundary"]
        if not re.search(r"https?://|Not (?:Disclosed|Required|Verified)", artifact): artifact = "Not Disclosed — " + artifact
        receipt = {"Review Route": route, "Primary Evidence Version": f"arXiv:{aid}v1", "Reviewed Evidence Versions": f"SRC-ARXIV@arXiv:{aid}v1", "Method / Identity Locators": "; ".join(rv["method_locators"]), "Evaluation Locators": "; ".join(rv["evaluation_locators"]) or "Not Required — no empirical claim", "Limitations / Counterevidence Locators": "; ".join(rv["limitations_locators"]), "Artifact Locators": artifact, "Claim Boundary Ref": f"claim:{family}", "Completion Result": "complete"}
        body = H.review_body(titles[family], admission, rv); receipt["Review Provenance ID"] = H.provenance(candidate, receipt, body)
        candidates[family], receipts[family], bodies[family] = candidate, receipt, body
    deep = [f for f in sorted(candidates) if int(candidates[f]["Total"]) >= 7 or candidates[f]["Review Override"] != "none"]
    closure_counts = Counter(x["decision_kind"] for x in semantic["items"] if x["decision"] == "pre_denominator_closure")
    proposed_counts = Counter(x["books_disposition"] for x in revs.values())
    families = ";".join(sorted(candidates)); generated = f"2026-09-04T05:00:00+08:00"
    lines = [f"# Daily Research — {args.date}", "", f"**Research Date:** {args.date}", "", "**Timezone:** Asia/Shanghai", "", f"**Strict Window:** {prev.isoformat()} 09:00:00 ～ {args.date} 09:00:00（北京时间，左闭右开）", "", "**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源", "", "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较", "", "## Executive Summary", "", f"官方 owner inventory 共 **{semantic['raw_identity_count']}** 个 identity；全量 title + abstract 筛选后冻结 **{len(candidates)}** 个候选与 **{semantic['pre_denominator_closure_count']}** 个 family-specific closure，retain rate **{semantic['retain_rate']*100:.2f}%**。exact-v1 Review 为 {len(candidates)}/{len(candidates)}：Deep {len(deep)}、Standard {len(candidates)-len(deep)}、blocked 0。", "", "当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。", "", "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", f"| Window Start | {args.date} |", f"| Window End | {args.date} |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", f"| Denominator ID | {denom['denominator_id']} |", f"| Denominator Frozen At | {denom['frozen_at']} |", "| Completion Status | In Progress |", "| Coverage Gate | Open |", "| Evidence Gate | Open |", "| Books Gate | Open |", "", "### Source Coverage Receipt", "", f"<!-- coverage:SRC-ARXIV:{compact}:start -->", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |", f"| SRC-ARXIV | {prev.isoformat()}T09:00:00+08:00 | {args.date}T09:00:00+08:00 | {semantic['executed_at']} | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | {semantic['raw_identity_count']} | {families} | all registered category pages; cross-category dedup complete | {args.date}T09:00:00+08:00 | sha256:{denom['denominator_id'].rsplit(':',1)[-1]} | — |", f"<!-- coverage:SRC-ARXIV:{compact}:end -->", "", "### Coverage Limitations", "", "- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。", "- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。", "", "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->", "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    cols = list(next(iter(candidates.values())).keys())
    for f in sorted(candidates): lines.append("| " + " | ".join(H.md(candidates[f][c]) for c in cols) + " |")
    lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    rcols = ["Review Provenance ID", "Review Route", "Primary Evidence Version", "Reviewed Evidence Versions", "Method / Identity Locators", "Evaluation Locators", "Limitations / Counterevidence Locators", "Artifact Locators", "Claim Boundary Ref", "Completion Result"]
    for f in sorted(receipts): lines.append("| " + H.md(f) + " | " + " | ".join(H.md(receipts[f][c]) for c in rcols) + " |")
    lines += ["", "### Source Reviews", ""]
    for f in sorted(bodies): lines += [f"<!-- review:{f}:start -->", bodies[f], f"<!-- review:{f}:end -->", ""]
    lines += ["## 4. Benchmark Contracts", "", "None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for f in deep:
        parts = (["score_7_9"] if int(candidates[f]["Total"]) >= 7 else []) + (["forced_review"] if candidates[f]["Review Override"] != "none" else [])
        if f in selected: decision, unit, ref, rationale = "selected", selected[f], f"analysis:{selected[f]}", f"V2={candidates[f]['Total']}/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。"
        else: decision, unit, ref, rationale = "not_selected", "—", f"analysis-decision:{f}", f"V2={candidates[f]['Total']}/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。"
        lines.append("| " + " | ".join(H.md(x) for x in (f, ";".join(parts), decision, unit, "—", rationale, ref)) + " |")
    lines += ["", "### Selection Decisions", ""]
    for f in deep:
        if f not in selected: lines += [f"<!-- analysis-decision:{f}:start -->", f"`{f}` 的 exact-v1 Deep Review 已保留。其机制为：{revs[f]['mechanism']} 为避免挤压 `{revs[f]['stable_node_id']}` owner，本日报不将它合并进三条主叙事。", f"<!-- analysis-decision:{f}:end -->", ""]
    lines += ["### Selected Analysis Narratives", ""]
    for f, unit in selected.items():
        rv = revs[f]; lines += [f"<!-- analysis:{unit}:start -->", f"### {titles[f]}", "", f"**约束变化与机制。** {rv['mechanism']}", "", f"**证明与未证明。** {rv['proved']} 但 {rv['not_proved']}", "", f"**Trade-off 与共存边界。** {rv['trade_off']} 旧方案在不承受该约束时仍成立。", "", f"关联：`review:{f}`。", f"<!-- analysis:{unit}:end -->", ""]
    lines += ["## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。", "", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", f"| SA-{compact}-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:{compact} | GAP-{compact}-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |", f"| SA-{compact}-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-{compact}-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |", f"| SA-{compact}-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-{compact}-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |", f"| SA-{compact}-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-{compact}-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |", "", "## 8. Ignored Noise", "", f"{semantic['pre_denominator_closure_count']} 项均有 family-specific pre-denominator closure：", ""]
    for kind, count in sorted(closure_counts.items()): lines.append(f"- `{kind}`：{count}")
    lines += ["", "## 9. Recommended Action", "", "1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。", f"2. root 逐项比较 Books。建议起点：Integrate {proposed_counts['Integrate']}、No Change {proposed_counts['No Change — Existing Coverage']}、Structural {proposed_counts['Structural Candidate']}；不是最终决定。", "", "## 10. Repository Changes", "", f"- 重建 `papers/{d.year:04d}/{d.month:02d}/{d.day:02d}/README.md` 及 date-local frozen queue。", "- 未修改 Books、ROADMAP、docs、Learning State、Weekly。", "", "## 11. Open Questions", "", "- 独立审计是否恢复 closure 中的漏项？", "- proposed Integrate 是否已被现有 Books 命题覆盖？", "", "## 12. Sources", ""]
    pdf_ids = {x["arxiv_id"] for x in json.loads((packet / "exact-v1-access-manifest-v2.1.json").read_text())["items"] if x.get("medium") == "official_exact_v1_pdf"}
    for f in sorted(candidates):
        aid = candidates[f]["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1"); medium = "pdf" if aid in pdf_ids else "html"
        lines.append(f"- [{titles[f]}](https://arxiv.org/{medium}/{aid}v1) — first-public（Asia/Shanghai）：{args.date}；exact evidence：v1；accessed：2026-09-04")
    lines += ["", "## 13. Final Status", "", f"Author-side screening、denominator、exact-v1 access、{len(candidates)}/{len(candidates)} Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。", "", "State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。", ""]
    report.write_text("\n".join(lines), encoding="utf-8")

    entries = []
    for f in sorted(revs):
        rv = revs[f]; aid = candidates[f]["Primary Identifier"].removeprefix("arXiv:").removesuffix("v1")
        entries.append({"date": args.date, "source_family_id": f, "primary_identifier": f"arXiv:{aid}v1", "review_provenance_id": receipts[f]["Review Provenance ID"], "stable_node_id": rv["stable_node_id"], "proposed_books_disposition": rv["books_disposition"], "evolution_relation": rv["evolution_relation"], "report": report.relative_to(ROOT).as_posix(), "queue_status": "frozen_pending_independent_audit_and_root_books_comparison", "reason": "Exact-v1 evidence is author-complete; final Books disposition requires independent audit and root comparison."})
    day_queue = {"schema": "books-writeback-queue-v2.1", "report_date": args.date, "generated_at": generated, "status": "frozen", "write_authority": "root-sequential-owner-only", "entry_count": len(entries), "proposed_disposition_counts": dict(sorted(proposed_counts.items())), "entries": entries}
    (packet / "BOOKS_WRITEBACK_QUEUE_V2.1.json").write_text(json.dumps(day_queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    month = json.loads(month_queue_path.read_text()) if month_queue_path.exists() else {"schema": "books-writeback-queue-v2.1", "entries": []}
    month.update({"generated_at": generated, "status": "frozen", "write_authority": "root-sequential-owner-only"}); month["entries"] = sorted([x for x in month.get("entries", []) if x.get("date") != args.date] + entries, key=lambda x: (x.get("date", ""), x.get("source_family_id", ""))); month["entry_count"] = len(month["entries"])
    month_queue_path.write_text(json.dumps(month, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    denom["status"] = "frozen_author_evidence_complete_independent_audit_and_books_pending"; denom["review_completion"] = {"expected": len(revs), "complete": len(revs), "blocked": 0}; denom["deep_analysis_selection"] = {"eligible": len(deep), "selected": 3, "author_receipt": "complete"}; denom["books_status"] = "frozen_pending_root_sequential_comparison"
    denom_path.write_text(json.dumps(denom, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"date": args.date, "raw": semantic["raw_identity_count"], "retained": len(revs), "deep": len(deep), "standard": len(revs)-len(deep), "queue": len(entries)}, ensure_ascii=False, indent=2))


if __name__ == "__main__": main()
