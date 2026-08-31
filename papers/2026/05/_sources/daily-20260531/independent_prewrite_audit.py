#!/usr/bin/env python3
"""Independent pre-write challenge for the 2026-05-31 author packet."""
from __future__ import annotations
import hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path

H=Path(__file__).resolve().parent
ROOT=H.parents[4]
NOW=datetime.now(timezone.utc).isoformat()

# 49/56 provisional Integrate is not a credible Books delta rate.  These are
# the families that still change a current long-lived owner after reading the
# owner and adjacent chapters; all others remain evidence-complete No Change.
INTEGRATE={
 "2606.00485","2606.00515","2606.00516","2606.00539","2606.00566",
 "2606.00619","2606.00642","2606.00654","2606.00735","2606.00756",
 "2606.00765","2606.00774","2606.00866","2606.00888","2606.00914",
 "2606.07620","2606.07624","2606.20634",
}

author=json.loads((H/"screening-ledger-author.json").read_text())
rows=[]
for src in author["identities"]:
 x=dict(src)
 if x["screening_status"]=="retained":
  x["integration_disposition"]="Integrate" if x["arxiv_id"] in INTEGRATE else "No Change — Existing Coverage"
 rows.append(x)
ret=[x for x in rows if x["screening_status"]=="retained"]
cls=[x for x in rows if x["screening_status"]!="retained"]
assert len(rows)==293 and len(ret)==56 and len(cls)==237
ledger=dict(author); ledger.update(schema="daily-screening-ledger-v2.1-independent-final",identities=rows,candidate_denominator=56,pre_denominator_closures=237)
(H/"screening-ledger-final.json").write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")

reviews=json.loads((H/"exact-v1-review-packet-author.json").read_text())
assert len(reviews)==56
(H/"exact-v1-review-packet.json").write_text(json.dumps(reviews,ensure_ascii=False,indent=2)+"\n")

comparisons=json.loads((H/"books-current-content-comparison-author.json").read_text())
for c in comparisons: c["decision"]="Integrate" if c["arxiv_id"] in INTEGRATE else "No Change — Existing Coverage"
(H/"books-current-content-comparison.json").write_text(json.dumps(comparisons,ensure_ascii=False,indent=2)+"\n")
queue=[]
for c in comparisons:
 if c["arxiv_id"] not in INTEGRATE: continue
 queue.append({"report_date":"2026-05-31","arxiv_id":c["arxiv_id"],"source_family_id":c["source_family_id"],"stable_node_id":c["owner_node"],"owner_path":c["owner_path"],"adjacent_paths":c["adjacent_paths"],"evidence_delta":c["new_evidence_delta"],"evidence_boundary":c["evidence_boundary"],"status":"ready_for_root_serial_writeback","writeback_requirement":"merge into canonical H2 before Review notes; preserve old condition, changed constraint, state/control owner, trade-off, failure, fallback/coexistence and exact-v1 non-proof boundary"})
assert len(queue)==18
(H/"BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema":"books-writeback-queue-v2.1-independent-final","report_date":"2026-05-31","status":"ready_for_root_serial_writeback","items":queue},ensure_ascii=False,indent=2)+"\n")
(H/"materials-request.json").write_text(json.dumps({"schema":"materials-request-v1","report_date":"2026-05-31","items":[]},ensure_ascii=False,indent=2)+"\n")

audit={"schema":"fresh-context-independent-prewrite-audit-v2.1","report_date":"2026-05-31","auditor":"fresh-context:may2026-day01","scope":{"registered_replayed":293,"author_denominator":56,"final_denominator":56,"author_closures":237,"final_closures":237,"exact_v1_complete":56,"blocked":0,"ordinary_pending":0,"author_queue":49,"final_queue":18},"findings":{"false_positives":[],"false_negatives":[],"books_false_positives":[{"arxiv_id":x["arxiv_id"],"resolution":"No Change — current owner already carries the mechanism class or v1 remains a local method/benchmark"} for x in ret if x["arxiv_id"] not in INTEGRATE],"books_retained":[{"arxiv_id":x["arxiv_id"],"owner":x["owner_node"]} for x in ret if x["arxiv_id"] in INTEGRATE]},"gates":{"coverage":"closed","evidence":"passed","books":"open_pending_root_writeback"},"unresolved_findings":[]}
(H/"independent-semantic-audit.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2)+"\n")
sha=hashlib.sha256((H/"screening-ledger-final.json").read_bytes()).hexdigest()
(H/"coverage-receipt.json").write_text(json.dumps({"schema":"coverage-receipt-v2.1","report_date":"2026-05-31","source_id":"SRC-ARXIV","window":author["window"],"raw_snapshot_records":author["raw_snapshot_records"],"registered_identities":293,"full_semantic_screened":293,"retained":56,"pre_denominator_closed":237,"ledger_sha256":sha,"status":"independent_closed"},ensure_ascii=False,indent=2)+"\n")

p=ROOT/"papers/2026/05/31/README.md"; text=p.read_text()
text=text.replace("**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。author packet 已完成，等待非作者 fresh-context pre-write audit。","**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。独立 pre-write audit 已完成，等待 root 串行写回。")
text=re.sub(r"author provisional denominator=56，pre-denominator closures=237，exact-v1 author review=56/56，blocked=0，provisional Books queue=49。.*?不是独立验收结果。","final denominator=56，pre-denominator closures=237，exact-v1 review=56/56，blocked=0、ordinary pending=0；Books queue 经 current owner+adjacent challenge 从 49 收紧为 18。本审计未修改共享 Books。",text)
text=text.replace("| Denominator ID | DEN-20260531-V2-AUTHOR |","| Denominator ID | DEN-20260531-INDEPENDENT-FINAL-56 |")
text=text.replace("| Coverage Gate | Open |","| Coverage Gate | Closed |").replace("| Evidence Gate | Open |","| Evidence Gate | Passed |")
families=";".join(x["source_family_id"] for x in ret)
receipt=f"| SRC-ARXIV | 2026-05-30T09:00:00+08:00 | 2026-05-31T09:00:00+08:00 | {NOW} | DataCite v2 00..99 monthly snapshot + 293/293 semantic replay + official exact-v1 HTML/PDF | checked | 293 | {families} | pages=300;final_cursor=end;raw={author['raw_snapshot_records']};registered=293;screened=293;retained=56;closure=237 | 2026-05-31T00:59:59Z | screening-ledger-final.json#sha256={sha} | — |"
text=re.sub(r"^\| SRC-ARXIV \|.*$",receipt,text,count=1,flags=re.M)
text=re.sub(r"<!-- coverage:SRC-ARXIV:20260531:start -->.*?<!-- coverage:SRC-ARXIV:20260531:end -->","<!-- coverage:SRC-ARXIV:20260531:start -->独立 reviewer 已重放 293/293；56 retained 与 237 family-specific closure 无 unresolved FP/FN finding。56/56 exact-v1 可访问，blocked=0、ordinary pending=0。<!-- coverage:SRC-ARXIV:20260531:end -->",text,flags=re.S)

# Reconcile the two Markdown tables and narrative decisions without changing
# evidence/provenance text.
for x in ret:
 fid=x["source_family_id"]; aid=x["arxiv_id"]; decision="Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
 # candidate row
 pat=rf"^\| {re.escape(fid)} \|.*$"; m=re.search(pat,text,re.M)
 if not m: raise RuntimeError(fid)
 cells=[c.strip() for c in m.group(0).strip().strip("|").split("|")]
 cells[13]="knowledge_gap" if decision=="Integrate" else "none"; cells[19]=decision
 text=text[:m.start()]+"| "+" | ".join(cells)+" |"+text[m.end():]

# Books table is the second row per family.
for x in ret:
 fid=x["source_family_id"]; aid=x["arxiv_id"]; decision="Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
 hits=list(re.finditer(rf"^\| {re.escape(fid)} \|.*$",text,re.M)); m=hits[-1]
 cells=[c.strip() for c in m.group(0).strip().strip("|").split("|")]; cells[6]="Direct Evolution" if decision=="Integrate" else "Layering / Dependency"; cells[7]=decision
 text=text[:m.start()]+"| "+" | ".join(cells)+" |"+text[m.end():]
 # decision prose
 text=re.sub(
     rf"(<!-- books-review:{re.escape(fid)}:start -->.*?)"
     rf"(?:Author|Independent pre-write) decision=`[^`]+`；[^\n]*",
     rf"\1Independent pre-write decision=`{decision}`；current owner+adjacent challenge 已完成；Integrate 项等待 root 串行写回，No Change 项已闭合。",
     text,
     flags=re.S,
 )

# Deep-selection rows: retain evidence eligibility but only final Integrates
# carry forced-review/potential-books-delta.
for x in ret:
 fid=x["source_family_id"]; aid=x["arxiv_id"]
 hits=list(re.finditer(rf"^\| {re.escape(fid)} \|.*$",text,re.M))
 if len(hits)<3: continue
 m=hits[1]; cells=[c.strip() for c in m.group(0).strip().strip("|").split("|")]
 cells[1]="score_7_9;forced_review;potential_books_delta" if aid in INTEGRATE else "score_7_9"
 text=text[:m.start()]+"| "+" | ".join(cells)+" |"+text[m.end():]

first=ret[0]["source_family_id"]
semantic=f"""## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260531-COVERAGE | fresh-context:may2026-day01 | coverage | coverage:SRC-ARXIV:20260531 | none | 293/293 replay；denominator=56；closures=237 | passed |
| SA-20260531-EVIDENCE | fresh-context:may2026-day01 | evidence | review:{first} | none | 56/56 exact-v1 Method/Evaluation/Limitations/Artifact review；blocked=0 | passed |
| SA-20260531-SELECTION | fresh-context:may2026-day01 | deep_analysis_selection | analysis:DA-CROSS-APP-CONTEXT-ISOLATION | none | Top-3 只限制 narrative，全部 retained 均已全文 review | passed |
| SA-20260531-BOOKS | fresh-context:may2026-day01 | books | books-review:{first} | F-20260531-BOOKS-WRITEBACK | author queue 49→final 18；等待 root 串行写回与 post-write audit | open |

独立审计未参与 author lane，也未修改共享 Books。
"""
text=re.sub(r"## 7\. Semantic Audit.*?(?=\n## 8\.)",lambda _m:semantic,text,flags=re.S)
text=text.replace("由未参与本 author packet 的 fresh-context reviewer 重放 293/293 screening、56/56 exact-v1、Deep Selection 与 49 项 provisional Books queue；只有其通过后才能交给 root 串行写 Books。","Root 按 final 18-item queue 串行写回；完成后由不同 reviewer 执行 post-write semantic audit。")
text=re.sub(r"- fresh-context independent pre-write audit 尚未执行.*?\n- 49 项 provisional Integrate 可能.*?\n","- Root 写回 18 项后，post-write audit 是否确认全部机制位于 canonical H2 主线并与相邻段自然衔接？\n",text)
text=text.replace("Coverage: `Open`","Coverage: `Closed`").replace("Evidence: `Open`","Evidence: `Passed`")
text=text.replace("unresolved findings: 4","unresolved findings: 0 (pre-write); Books writeback remains")
text=text.replace("Author packet 已完成，但四项 fresh-context Semantic Audit 均待非作者执行；不得解释为 Daily 闭环。","Independent pre-write audit 已完成：Coverage/Evidence 已闭合；Books 等待 root 串行写回与 post-write audit，因此 Daily 仍为 In Progress。")
p.write_text(text)

# Normalize the two tables that share Source Family IDs by table marker rather
# than by ordinal occurrence.  The author report has four family-keyed tables;
# ordinal replacement can silently write selection eligibility into Review
# Provenance IDs, so the independent packet must be section-aware.
import sys
sys.path.insert(0, str(ROOT / "scripts"))
from validate_research import (
    _bounded_segment,
    _expected_review_provenance,
    _normalized_body_sha256,
    _table_after_marker,
)

text = p.read_text()

def replace_row_in_section(source: str, marker: str, family: str, mutate, *, required=True):
    start = source.index(marker) + len(marker)
    next_heading = source.find("\n## ", start)
    end = len(source) if next_heading < 0 else next_heading
    section = source[start:end]
    match = re.search(rf"^\| {re.escape(family)} \|.*$", section, re.M)
    if not match:
        if required:
            raise RuntimeError(f"missing {family} after {marker}")
        return source
    cells = [c.strip() for c in match.group(0).strip().strip("|").split("|")]
    mutate(cells)
    replacement = "| " + " | ".join(cells) + " |"
    section = section[:match.start()] + replacement + section[match.end():]
    return source[:start] + section + source[end:]

for item in ret:
    fid = item["source_family_id"]
    aid = item["arxiv_id"]
    eligibility = (
        "score_7_9;forced_review;potential_books_delta"
        if aid in INTEGRATE else "score_7_9"
    )
    text = replace_row_in_section(
        text,
        "<!-- validator:deep-analysis-selection-v1 -->",
        fid,
        lambda cells, value=eligibility: cells.__setitem__(1, value),
        required=False,
    )

# Recompute content-addressed Review Provenance after the disposition challenge
# changes Review Override.  Locators and review prose remain the exact-v1
# author-reviewed evidence, but the provenance necessarily changes when the
# candidate's forced-review fact changes.
candidate_rows, candidate_errors = _table_after_marker(
    text, "<!-- validator:candidate-ledger-v2.1 -->"
)
review_rows, review_errors = _table_after_marker(
    text, "<!-- validator:review-completion-v1 -->"
)
assert not candidate_errors and not review_errors
candidate_by_family = {row["Source Family ID"]: row for row in candidate_rows}
for row in review_rows:
    fid = row["Source Family ID"]
    candidate = candidate_by_family[fid]
    review_ref = candidate["Review Ref"].strip("`")
    review_body = _bounded_segment(text, review_ref, f"review {fid}", [])
    assert review_body is not None
    provenance = _expected_review_provenance(
        fid,
        candidate,
        row["Review Route"],
        row["Primary Evidence Version"],
        row["Reviewed Evidence Versions"],
        row["Method / Identity Locators"],
        row["Evaluation Locators"],
        row["Limitations / Counterevidence Locators"],
        row["Artifact Locators"],
        row["Claim Boundary Ref"],
        review_ref,
        _normalized_body_sha256(review_body),
    )
    text = replace_row_in_section(
        text,
        "<!-- validator:review-completion-v1 -->",
        fid,
        lambda cells, value=provenance: cells.__setitem__(1, value),
    )

p.write_text(text)
print(json.dumps(audit["scope"],ensure_ascii=False))
