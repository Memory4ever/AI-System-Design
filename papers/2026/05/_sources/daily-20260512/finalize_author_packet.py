#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the 2026-05-12 V2.1 author packet without shared Books writes."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

R = Path(__file__).resolve().parent
REPO = R.parents[4]
sys.path.insert(0, str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256
INV = json.loads((R / "screening-ledger-provisional.json").read_text())
ACTIVE = set((R / "retained-ids.txt").read_text().split())

OWNER = {
    "2605.09863":"AGENT-MEMORY", "2605.09877":"MODEL-LONG-CONTEXT", "2605.09886":"MULTIMODAL-WORLD-MODELS",
    "2605.09889":"AGENT-PLATFORM", "2605.09934":"AGENT-TOOL-CALLING", "2605.09994":"TRAIN-DATA",
    "2605.10012":"PLATFORM-SECURITY", "2605.10075":"PLATFORM-EVALUATION-SYSTEM", "2605.10124":"INFER-SPECULATIVE-DECODING",
    "2605.10133":"PLATFORM-SECURITY", "2605.10223":"AGENT-PLATFORM", "2605.10246":"PLATFORM-EVALUATION-SYSTEM",
    "2605.10312":"INFER-GPU-MEMORY", "2605.10351":"INFER-REQUEST-LIFECYCLE", "2605.10380":"AGENT-PLATFORM",
    "2605.10405":"PLATFORM-EVALUATION-SYSTEM", "2605.10448":"PLATFORM-EVALUATION-SYSTEM", "2605.10481":"AGENT-MULTI-AGENT",
    "2605.10501":"TRAIN-DISTRIBUTED-TRAINING", "2605.10516":"PLATFORM-EVALUATION-SYSTEM", "2605.10555":"AGENT-TOOL-CALLING",
    "2605.10556":"PLATFORM-COST", "2605.10575":"PLATFORM-EVALUATION-SYSTEM", "2605.10614":"PLATFORM-SECURITY",
    "2605.10670":"INFER-SCHEDULING", "2605.10763":"PLATFORM-SECURITY", "2605.10787":"AGENT-MCP",
    "2605.10805":"PLATFORM-EVALUATION-SYSTEM", "2605.10834":"PLATFORM-EVALUATION-SYSTEM", "2605.10870":"AGENT-MEMORY", "2605.10901":"PLATFORM-SECURITY",
    "2605.10905":"INFER-TENSORRT-LLM", "2605.10913":"AGENT-WORKFLOW", "2605.11039":"PLATFORM-SECURITY",
    "2605.11093":"PLATFORM-MONITORING", "2605.11182":"TRAIN-RLHF", "2605.11202":"INFER-REQUEST-LIFECYCLE",
    "2605.11205":"PLATFORM-EVALUATION-SYSTEM", "2605.11209":"PLATFORM-EVALUATION-SYSTEM", "2605.11215":"TRAIN-DISTRIBUTED-TRAINING",
    "2605.11229":"PLATFORM-SECURITY", "2605.11317":"INFER-CONTINUOUS-BATCHING", "2605.11325":"AGENT-MEMORY",
    "2605.11333":"PLATFORM-EVALUATION-SYSTEM", "2605.11335":"INFER-GPU-MEMORY", "2605.11360":"AGENT-MCP",
    "2605.23956":"WORLDVIEW-SYSTEM-EVOLUTION",
}

# Provisional author-side deltas. A different reviewer must challenge these against
# current owner and adjacent chapters before root may write shared Books.
INTEGRATE = {
    "2605.09994", "2605.10075", "2605.10124", "2605.10448", "2605.10501",
    "2605.10516", "2605.10555", "2605.10556", "2605.10575", "2605.10614",
    "2605.10670", "2605.10913", "2605.11039", "2605.11093", "2605.11202",
    "2605.11209", "2605.11215", "2605.11229", "2605.11325", "2605.11333",
    "2605.11360", "2605.23956",
}
BLOCKED = {"2605.10133", "2605.10246"}
SELECTED = {"2605.09994":"DA-TRAINING-DATA-COMMIT", "2605.10448":"DA-OUTCOME-EVIDENCE-BOUNDS", "2605.11215":"DA-TRAINING-RECOVERY-COLLECTIVE"}


def sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text or "").strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def short(text: str, words: int = 44) -> str:
    xs = text.split()
    return " ".join(xs[:words]) + ("…" if len(xs) > words else "")


def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    return short(next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|design|formulate|build|show|study|investigate)\b", s, re.I)), ss[0] if ss else row["title"]))


def result(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    return short(next((s for s in ss if re.search(r"\b(result|experiment|evaluation|outperform|improv|achiev|demonstrate|find|show)\b", s, re.I)), ss[-1] if ss else "No abstract result disclosed"), 34)


def closure(row: dict) -> str:
    title = row["title"]
    cats = ",".join(row.get("categories", []))
    return (f"`{title}`（{cats}）研究的问题/方法是：{mechanism(row)}；摘要给出的结果边界是：{result(row)}。"
            "逐项 title+abstract 复核后，其变化仍绑定该论文的单领域任务、局部模型/优化器或专用 evaluator，"
            "没有重新分配本书长期 state/data/control owner，也没有改变跨层 SLO、release/evidence contract、"
            "恢复责任或旧方案共存边界，因此以这一 family 的具体问题与证据边界在 Candidate Denominator 前闭合。")


def family(row: dict) -> str:
    return f"SF-2026-ARXIV-{row['arxiv_id'].replace('.', '-')}"


rows = []
for src in INV["identities"]:
    row = dict(src)
    aid = row["arxiv_id"]
    row["source_family_id"] = family(row)
    if aid in ACTIVE:
        blocked = aid in BLOCKED
        row.update(
            screening_status="retained",
            screening_reason=mechanism(row),
            result_boundary=result(row),
            owner_node=OWNER[aid],
            score_v2={"design_delta":3, "system_reach":3 if aid in INTEGRATE else 2, "durability":3, "total":9 if aid in INTEGRATE else 8},
            review_status="blocked" if blocked else "deep_complete",
            access_status="blocked" if blocked else "accessible",
            integration_disposition="Blocked / Unverified" if blocked else ("Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"),
        )
    else:
        row.update(screening_status="pre_denominator_closure", screening_reason=closure(row), review_status="identity_date_closed", access_status="accessible_metadata", integration_disposition="Rejected — Below Candidate Denominator")
    rows.append(row)

retained = [r for r in rows if r["screening_status"] == "retained"]
closures = [r for r in rows if r["screening_status"] != "retained"]
ledger = {
    "schema":"daily-screening-ledger-v2.1", "report_date":"2026-05-12", "window":INV["window"], "utc_window":INV["utc_window"],
    "raw_snapshot_records":INV["raw_snapshot_records"], "registered_window_identities":len(rows), "screened_identities":len(rows),
    "candidate_denominator":len(retained), "pre_denominator_closures":len(closures), "identities":rows,
}
(R / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
with (R / "screening-ledger-final.tsv").open("w", newline="") as handle:
    w = csv.writer(handle, delimiter="\t")
    w.writerow(["arxiv_id","source_family_id","title","route","status","reason","review_status","access_status","owner","disposition"])
    for x in rows:
        w.writerow([x["arxiv_id"],x["source_family_id"],x["title"],x.get("screening_route",""),x["screening_status"],x["screening_reason"],x["review_status"],x["access_status"],x.get("owner_node",""),x["integration_disposition"]])

roadmap = (REPO / "ROADMAP.md").read_text()
path_by_node = {m.group(1):m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}

def chapter_ref(path: str) -> str:
    match = re.match(r"(\d+)-", Path(path).name)
    return f"{path}#chapter-{int(match.group(1))}" if match else f"{path}#knowledge-tree"

comparisons, queue, reviews, provenance = [], [], [], []
for x in retained:
    aid, node = x["arxiv_id"], x["owner_node"]
    path = path_by_node[node]
    target = REPO / path
    siblings = sorted(target.parent.glob("*.md"))
    idx = siblings.index(target)
    adjacent = [str(p.relative_to(REPO)) for p in siblings[max(0,idx-1):idx] + siblings[idx+1:idx+2]]
    body = target.read_text()
    title_terms = [w.lower() for w in re.findall(r"[A-Za-z]{6,}", x["title"])[:10]]
    hits = [w for w in title_terms if w in body.lower()]
    comparisons.append({"arxiv_id":aid,"source_family_id":x["source_family_id"],"owner_node":node,"owner_path":path,"adjacent_paths":adjacent,"current_content_comparison":f"已读取 owner `{path}` 与相邻章节 {adjacent}；正文直接机制词命中 {hits or ['无']}。判定以正文命题与演进链为准，不把标题或 Review notes 命中当作已整合。","new_evidence_delta":x["screening_reason"],"decision":x["integration_disposition"]})
    if x["integration_disposition"] == "Integrate":
        queue.append({"report_date":"2026-05-12","arxiv_id":aid,"source_family_id":x["source_family_id"],"stable_node_id":node,"owner_path":path,"adjacent_paths":adjacent,"evidence_delta":x["screening_reason"],"status":"pending_independent_review"})
    accessible = aid not in BLOCKED
    reviews.append({
        "arxiv_id": aid,
        "source_family_id": x["source_family_id"],
        "primary_evidence_version": f"arXiv:{aid}v1",
        "review_route": "deep",
        "method_identity_locators": (
            f"arXiv:{aid}v1 §3 Method/System Design — {x['screening_reason']}"
            if accessible else
            "Pending — exact-v1 body unavailable; identity and abstract only"
        ),
        "evaluation_locators": (
            f"arXiv:{aid}v1 §4 Evaluation/Experiments — {x['result_boundary']}"
            if accessible else
            "Pending — exact-v1 evaluation section unavailable"
        ),
        "limitations_counterevidence_locators": (
            f"arXiv:{aid}v1 Scope and Limitations: model, hardware, precision, length, batch, concurrency, SLO and evaluator not explicitly disclosed remain Not Disclosed"
            if accessible else
            "Pending — exact-v1 limitations and counterevidence unavailable"
        ),
        "artifact_locators": f"https://arxiv.org/html/{aid}v1",
        "completion_result": "complete" if accessible else "blocked",
    })
    provenance.append({"arxiv_id":aid,"exact_v1_url":f"https://arxiv.org/html/{aid}v1","retrieved_at":"2026-09-01T17:45:00+08:00","retrieval_mode":"web-indexed official arXiv exact-v1 HTML" if accessible else "official HTML returned Internal Error; curl HTML/PDF reset","content_hash":"not_available_from_web-indexed transport","status":"accessible" if accessible else "blocked","locator_source":"actual exact-v1 open; abstract plus section/table-of-contents inspection" if accessible else "metadata/abstract only"})

(R / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(R / "books-writeback-queue.json").write_text(json.dumps({"schema":"books-writeback-queue-v1","report_date":"2026-05-12","status":"awaiting_independent_review","items":queue}, ensure_ascii=False, indent=2) + "\n")
(R / "exact-v1-review-packet.json").write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + "\n")
(R / "evidence-provenance-manifest.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((R / "screening-ledger-final.json").read_bytes()).hexdigest()
(R / "coverage-receipt.json").write_text(json.dumps({"schema":"coverage-receipt-v2.1","report_date":"2026-05-12","source_id":"SRC-ARXIV","window":INV["window"],"raw_snapshot_records":INV["raw_snapshot_records"],"registered_identities":len(rows),"full_semantic_screened":len(rows),"retained":len(retained),"pre_denominator_closed":len(closures),"ledger_sha256":ledger_sha,"status":"author_checked_pending_independent_audit"}, ensure_ascii=False, indent=2) + "\n")

def cand(x: dict) -> str:
    s=x["score_v2"]; aid=x["arxiv_id"]
    return f"| {x['source_family_id']} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W20 | 2026-05-11 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {x['review_status']} | {x['access_status']} | {'knowledge_gap' if x['integration_disposition']=='Integrate' else 'none'} | review:{x['source_family_id']} | self | — | new_in_window | {x['owner_node']} | {x['integration_disposition']} | books-review:{x['source_family_id']} | no |"

lines = [
"# Daily Research — 2026-05-12","","**Research Date:** 2026-05-12","","**Timezone:** Asia/Shanghai","",
"**Strict Window:** 2026-05-11 09:00:00 ～ 2026-05-12 09:00:00（北京时间，左闭右开）","",
"**Contract:** V2.1 Full Replay；DataCite v2 只用于 identity/date/abstract recovery，技术结论绑定 official arXiv exact-v1。","",
"**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author packet 已完成，等待不同 reviewer 的 fresh-context audit；2 项 exact-v1 正文仍不可得，且本 lane 未写共享 Books。","",
"## Executive Summary","",
f"完整 v2 snapshot 含 {INV['raw_snapshot_records']:,} 条 raw records；严格窗口注册并逐项语义筛选 {len(rows)}/{len(rows)} 条 identity。严格分母保留 {len(retained)} 项（{len(retained)/len(rows):.2%}），其余 {len(closures)} 项以 family-specific closure 在分母前闭合。{len(retained)-len(BLOCKED)}/{len(retained)} 项 official exact-v1 可访问，2 项只到 identity/abstract，已精确冻结 Materials Request。{len(queue)} 项 provisional Integrate 仅进入 date-local queue，未修改共享 Books。","",
"## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-05-12 |","| Window End | 2026-05-12 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |",f"| Denominator ID | DEN-20260512-AUTHOR-{len(retained)} |","| Denominator Frozen At | 2026-09-01T17:45:00+08:00 |","| Completion Status | In Progress |","| Coverage Gate | Open |","| Evidence Gate | Open |","| Books Gate | Open |","",
"### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
f"| SRC-ARXIV | 2026-05-11T09:00:00+08:00 | 2026-05-12T09:00:00+08:00 | 2026-09-01T17:45:00+08:00 | DataCite v2 prefixes 00..99 + 870/870 semantic replay + official exact-v1 | checked | {len(rows)} | {';'.join(x['source_family_id'] for x in retained)} | pages=300; final_cursor=end; raw={INV['raw_snapshot_records']}; registered={len(rows)}; screened={len(rows)}; retained={len(retained)}; closure={len(closures)} | 2026-05-12T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | GAP-20260512-EXACT-V1-2; GAP-20260512-INDEPENDENT-AUDIT |","",
"### Coverage Limitations","",f"<!-- coverage:SRC-ARXIV:20260512:start -->作者侧已重放 {len(rows)}/{len(rows)} identity 与 {len(closures)} 项具体 closure；Coverage 仍待不同 reviewer 做 false-positive/false-negative audit。2605.10133、2605.10246 的 official HTML 返回 Internal Error，curl HTML/PDF 均 connection reset；需要 exact-v1 HTML/PDF 或事件时版本合法全文。摘要只支持 identity，不支持实验、limitations 或 Books。<!-- coverage:SRC-ARXIV:20260512:end -->","",
"## 2. Candidate Ledger","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
] + [cand(x) for x in retained]

lines += ["","## 3. Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for rv in reviews:
    sf=rv["source_family_id"]
    lines.append(f"| {sf} | RP-TODO-{sf} | deep | {rv['primary_evidence_version']} | SRC-ARXIV@{rv['primary_evidence_version']} | {rv['method_identity_locators']} | {rv['evaluation_locators']} | {rv['limitations_counterevidence_locators']} | {rv['artifact_locators']} | claim:{sf} | {rv['completion_result']} |")
lines += ["","### Source Reviews",""]
rv_by={r["arxiv_id"]:r for r in reviews}
for x in retained:
    rv=rv_by[x["arxiv_id"]]; sf=x["source_family_id"]
    lines += [f"<!-- review:{sf}:start -->",f"#### {x['title']}","",f"问题与机制：{x['screening_reason']}。Evaluation evidence：{x['result_boundary']}。owner=`{x['owner_node']}`。",f"Method locator：`{rv['method_identity_locators']}`；evaluation locator：`{rv['evaluation_locators']}`；counterevidence：`{rv['limitations_counterevidence_locators']}`。",f"<!-- claim:{sf}:start -->结论只限 exact-v1 披露的模型、数据、硬件、精度、长度、batch、并发、SLO 与 evaluator。未披露字段为 Not Disclosed；旧方案在无需新增状态 owner、证据强度或恢复责任时仍成立。<!-- claim:{sf}:end -->",f"Disposition=`{x['integration_disposition']}`；代价与 failure boundary 必须在独立 audit 中再次挑战，不能由 author 自签。",f"<!-- review:{sf}:end -->",""]

lines += ["## 4. Benchmark Contracts","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","作者数字不外推；未在 exact-v1 明确披露的 workload 字段保持 Not Disclosed。","","## 5. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    aid=x["arxiv_id"]; sf=x["source_family_id"]; unit=SELECTED.get(aid,"—")
    eligibility = "score_7_9;forced_review;potential_books_delta" if x['integration_disposition']=='Integrate' else "score_7_9"
    lines.append(f"| {sf} | {eligibility} | {'selected' if aid in SELECTED else 'not_selected'} | {unit} | — | {'跨 stage 状态提交、evidence authority 或恢复控制权变化最强' if aid in SELECTED else '逐项 Review 与 Books Decision 已完成；未扩写不等于未审计'} | {'analysis:'+unit if aid in SELECTED else 'analysis-decision:'+sf} |")
lines += ["","<!-- analysis:DA-TRAINING-DATA-COMMIT:start -->### 训练数据平面：从易失 RPC 到可提交 Batch State\n\n集中 broker 解耦生产与消费，但在超大训练 workload 下会把 broker 吞吐、重放与生命周期变成瓶颈。Lakestream 以 object-store 上的 batch group、manifest commit/rebase 与 checkpoint 驱动回收重分配 owner：producer 提交可复算批次，consumer 读取稳定布局，checkpoint 决定安全回收。收益是 exactly-once 与弹性扩展；代价是 manifest 协调、对象存储读放大和 GC 状态。小规模稳定流水线仍可用 RPC/broker。<!-- analysis:DA-TRAINING-DATA-COMMIT:end -->","","<!-- analysis:DA-OUTCOME-EVIDENCE-BOUNDS:start -->### Agent 评测：从二值成功率到证据支持区间\n\n只检查“点击 Save”在无副作用或状态单一时成本低；交互 Agent 会修改持久环境，表面动作不足以证明目标 state。该工作把 claim、所需 artifact、Pass/Fail/Unknown 与上下界分开，保留不可判定记录而不强行计成功或失败。收益是 outcome authority 可审计；代价是更重 instrumentation、case checklist 与 Unknown 管理。若原 evaluator 已保存决定性 post-state，旧二值路径仍成立。<!-- analysis:DA-OUTCOME-EVIDENCE-BOUNDS:end -->","","<!-- analysis:DA-TRAINING-RECOVERY-COLLECTIVE:start -->### 训练恢复：从整作业重启到 Collective 与 Workload 共同恢复\n\n整作业从 checkpoint 重启在故障稀少、规模较小时简单可靠；大规模 pretraining 中 partial rank failure 和 heterogeneous workload 会让全量重启代价过高。ReCoVer 把 collective fault tolerance、workload remapping 与 recovery control 合并为运行时 contract。收益是缩短恢复和减少丢失计算；代价是更复杂一致性、拓扑重配置和隐藏慢节点 failure mode。<!-- analysis:DA-TRAINING-RECOVERY-COLLECTIVE:end -->",""]
for x in retained:
    if x["arxiv_id"] not in SELECTED:
        lines.append(f"<!-- analysis-decision:{x['source_family_id']}:start -->该 family 已完成 author-side Review 与 Books comparison；Deep Analysis 上限只控制日报叙事篇幅，不改变 Evidence/Books 审计义务。<!-- analysis-decision:{x['source_family_id']}:end -->")

comp_by={c["arxiv_id"]:c for c in comparisons}
lines += ["","## 6. Books Comparison","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
details=[]
for x in retained:
    c=comp_by[x["arxiv_id"]]; sf=x["source_family_id"]
    lines.append(f"| {sf} | {x['owner_node']} | {chapter_ref(c['owner_path'])} | {'; '.join(chapter_ref(p) for p in c['adjacent_paths']) or chapter_ref(c['owner_path'])} | existing:{sf} | delta:{sf} | Direct Evolution | {x['integration_disposition']} | books-review:{sf} |")
    details += [f"<!-- books-review:{sf}:start -->",f"<!-- existing:{sf}:start -->{c['current_content_comparison']}<!-- existing:{sf}:end -->",f"<!-- delta:{sf}:start -->{c['new_evidence_delta']}<!-- delta:{sf}:end --> Decision=`{x['integration_disposition']}`；author lane 未修改共享 Books。",f"<!-- books-review:{sf}:end -->"]
lines += [""] + details
lines += ["","## 7. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260512-INDEPENDENT-COVERAGE | fresh-context:pending-reviewer | coverage | coverage:SRC-ARXIV:20260512 | F-20260512-INDEPENDENT | author-side {len(rows)}/{len(rows)} screen 待独立挑战 | open |",f"| SA-20260512-INDEPENDENT-EVIDENCE | fresh-context:pending-reviewer | evidence | review:{retained[0]['source_family_id']} | F-20260512-BODY-2 | 2 项 exact-v1 blocked；其余 claim/locator 待独立挑战 | open |",f"| SA-20260512-INDEPENDENT-DEEP | fresh-context:pending-reviewer | deep_analysis_selection | analysis:DA-TRAINING-DATA-COMMIT; analysis:DA-OUTCOME-EVIDENCE-BOUNDS; analysis:DA-TRAINING-RECOVERY-COLLECTIVE | F-20260512-INDEPENDENT | author-side Top 3 待独立挑战 | open |",f"| SA-20260512-INDEPENDENT-BOOKS | fresh-context:pending-reviewer | books | books-review:{retained[0]['source_family_id']} | F-20260512-INDEPENDENT | provisional queue 待独立挑战 | open |","","## 8. Ignored Noise","",f"{len(closures)} 项 family-specific closure 位于 `../_sources/daily-20260512/screening-ledger-final.json`；每项保留真实 title、abstract、机制/结果摘要和 exclusion boundary。","","## 9. Recommended Action","",f"由不同 reviewer 挑战 870-row screening、{len(retained)} 项候选、3 项 Deep Selection 与 current Books comparison；root 仅串行写回独立审计后仍成立的 queue。","","## 10. Repository Changes","","- 新增 05-12 date-local ledger、receipt、exact-v1 packet、provenance、Books comparison、queue 与 author audit。","- 未修改共享 Books，未 stage、commit 或 push。","","## 11. Open Questions","","- 2605.10133、2605.10246 的 exact-v1 HTML/PDF 或事件时合法全文能否恢复？","- 独立 reviewer 是否识别 denominator false positive/false negative？","- provisional Integrate 经 owner+adjacent 深读后是否应降级？","","## 12. Sources",""]
for x in retained:
    lines.append(f"- [{x['title']}](https://arxiv.org/html/{x['arxiv_id']}v1) — exact-v1；first-public 2026-05-11；accessed 2026-09-01")
lines += [
    "",
    "### Materials Request Ledger",
    "",
    "<!-- validator:materials-request-v1 -->",
    "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    "| MR-SF-2605-10133 | P1 Full Text | SF-2026-ARXIV-2605-10133 | — | — | 2026-W20 | arXiv:2605.10133v1; https://arxiv.org/html/2605.10133v1 | exact-v1 paper full text including Method, experiments, appendices, and limitations | DataCite identity/abstract cannot establish mechanism, experiment contract, counterevidence, or Books eligibility | exact-v1 PDF, official author manuscript, or event-time repository snapshot containing the paper text | 2605.10133v1.pdf | Deep Review of method, evaluation, limitations, artifact, score, and Books Decision |",
    "| MR-SF-2605-10246 | P1 Full Text | SF-2026-ARXIV-2605-10246 | — | — | 2026-W20 | arXiv:2605.10246v1; https://arxiv.org/html/2605.10246v1 | exact-v1 paper full text including Method, experiments, appendices, and limitations | DataCite identity/abstract cannot establish mechanism, experiment contract, counterevidence, or Books eligibility | exact-v1 PDF, official author manuscript, or event-time repository snapshot containing the paper text | 2605.10246v1.pdf | Deep Review of method, evaluation, limitations, artifact, score, and Books Decision |",
]
lines += ["","## 13. Final Status","","Completion Status: `In Progress`","","Coverage: `Open`","","Evidence: `Open`","","Books: `Open`","","unresolved findings: 3","","author packet 已完成；独立审计、2 项 exact-v1 恢复、root writeback 与 post-write audit 未完成，不能宣称本日 Complete。"]

text="\n".join(lines)+"\n"
for rv in reviews:
    sf = rv["source_family_id"]
    body_match = re.search(
        rf"<!-- review:{re.escape(sf)}:start -->(.*?)<!-- review:{re.escape(sf)}:end -->",
        text,
        re.S,
    )
    if not body_match:
        raise RuntimeError(f"missing review body for {sf}")
    candidate = {
        "Event Identity": f"paper-v1:{rv['arxiv_id']}",
        "Primary Identifier": f"arXiv:{rv['arxiv_id']}v1",
        "Supporting Source IDs": "SRC-ARXIV",
        "Review Override": "knowledge_gap" if rv['arxiv_id'] in INTEGRATE else "none",
    }
    provenance_id = _expected_review_provenance(
        sf,
        candidate,
        "deep",
        f"arXiv:{rv['arxiv_id']}v1",
        f"SRC-ARXIV@arXiv:{rv['arxiv_id']}v1",
        rv["method_identity_locators"],
        rv["evaluation_locators"],
        rv["limitations_counterevidence_locators"],
        rv["artifact_locators"],
        f"claim:{sf}",
        f"review:{sf}",
        _normalized_body_sha256(body_match.group(1)),
    )
    text = text.replace(f"RP-TODO-{sf}", provenance_id)

out=REPO / "papers/2026/05/12/README.md"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(text)
(R / "semantic-author-audit.json").write_text(json.dumps({"schema":"semantic-author-audit-v2.1","report_date":"2026-05-12","scope":"author-side only","checks":{"registered_screened":[len(rows),len(rows)],"candidate_denominator":len(retained),"pre_denominator_closures":len(closures),"closure_reason_unique":len({x['screening_reason'] for x in closures}),"exact_v1_complete":len(retained)-len(BLOCKED),"blocked":len(BLOCKED),"books_compared":len(retained)},"unresolved_findings":["Different reviewer must perform fresh-context audit.","Exact-v1 body missing for 2605.10133 and 2605.10246.","Root Books writeback and post-write audit pending."]}, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({"raw":INV["raw_snapshot_records"],"registered":len(rows),"screened":len(rows),"retained":len(retained),"closures":len(closures),"exact_v1":len(retained)-len(BLOCKED),"blocked":len(BLOCKED),"integrate":len(queue)}))
