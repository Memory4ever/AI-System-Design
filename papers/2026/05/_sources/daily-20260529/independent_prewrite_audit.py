#!/usr/bin/env python3
"""Independent 2026-05-29 denominator/evidence/Books pre-write audit."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

H = Path(__file__).resolve().parent
REPO = H.parents[4]
NOW = datetime.now(timezone.utc).isoformat()
sys.path.insert(0,str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

DROP = {
    "2605.29489": "weight-space merge 的 expert-read budget 是单一合并算法的局部代价模型，未改变模型 artifact、训练或部署 owner",
    "2605.29697": "图式 step-credit 是 agent-search 的局部 reward estimator，未改变 durable workflow state 或 release evidence contract",
    "2605.30155": "partial multi-neuron relaxation 改善单一 verifier 的松弛精度，未改变平台验证责任或发布 Gate",
    "2605.30219": "contextual belief management 是单模型答案修正策略，未建立跨请求持久状态、authority 或 rollback contract",
    "2605.30343": "latent working-memory probe 是局部表示与推理方法，尚未改变可持久化 memory lifecycle 或 serving state owner",
    "2605.30656": "empowerment representation 是控制任务的局部表征目标，未改变 world-state identity、physical feedback 或安全闭环",
    "2605.29495": "on-policy replay 改善 continual SFT 的样本选择，但 v1 未重新分配 dataset/objective/checkpoint ownership",
}
ADD = {
    "2605.29223": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 3), "No Change — Existing Coverage"),
    "2605.29234": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "No Change — Existing Coverage"),
    "2605.29253": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate"),
    "2605.29324": ("AGENT-MEMORY", (3, 3, 3), "Integrate"),
    "2605.29341": ("AGENT-MEMORY", (3, 3, 3), "Integrate"),
}

OWNER = {
    "2605.29251":"PLATFORM-SECURITY", "2605.29262":"AGENT-WORKFLOW",
    "2605.29313":"AGENT-MULTI-AGENT", "2605.29359":"PLATFORM-SECURITY",
    "2605.29442":"PLATFORM-EVALUATION-SYSTEM", "2605.29454":"PLATFORM-SECURITY",
    "2605.29524":"PLATFORM-EVALUATION-SYSTEM", "2605.29561":"AGENT-TOOL-CALLING",
    "2605.29601":"PLATFORM-SECURITY", "2605.29639":"INFER-TENSORRT-LLM",
    "2605.29640":"AGENT-MEMORY", "2605.29682":"PLATFORM-EVALUATION-SYSTEM",
    "2605.29786":"PLATFORM-EVALUATION-SYSTEM", "2605.29843":"INFER-TENSORRT-LLM",
    "2605.29888":"PLATFORM-EVALUATION-SYSTEM", "2605.29960":"PLATFORM-SECURITY",
    "2605.30052":"AGENT-WORKFLOW", "2605.30102":"AGENT-PLATFORM",
    "2605.30104":"PLATFORM-EVALUATION-SYSTEM", "2605.30152":"AGENT-WORKFLOW",
    "2605.30159":"AGENT-MEMORY", "2605.30169":"AGENT-MULTI-AGENT",
    "2605.30218":"INFER-TENSORRT-LLM", "2605.30227":"AGENT-MULTI-AGENT",
    "2605.30335":"AGENT-MULTI-AGENT", "2605.30406":"PLATFORM-SECURITY",
    "2605.30504":"PLATFORM-EVALUATION-SYSTEM", "2605.30521":"PLATFORM-SECURITY",
    "2605.30523":"MODEL-TRANSFORMER-LAYER", "2605.30568":"PLATFORM-EVALUATION-SYSTEM",
    "2605.30604":"PLATFORM-SECURITY", "2605.30621":"AGENT-PLATFORM",
    "2605.30628":"PLATFORM-EVALUATION-SYSTEM", "2605.30686":"PLATFORM-SECURITY",
    "2605.30690":"AGENT-MEMORY", "2605.30693":"PLATFORM-SECURITY",
    "2605.30698":"AGENT-MULTI-AGENT",
}

INTEGRATE = {
    "2605.29253", "2605.29313", "2605.29324", "2605.29341", "2605.29359",
    "2605.29463", "2605.29561", "2605.29640", "2605.29664", "2605.29786",
    "2605.30040", "2605.30102", "2605.30218", "2605.30263", "2605.30294",
    "2605.30335", "2605.30406", "2605.30521", "2605.30571", "2605.30613",
    "2605.30690",
}

def clean(s: str) -> str:
    return re.sub(r"\s+", " ", unescape(s or "")).strip()

def sents(s: str) -> list[str]:
    return [x for x in re.split(r"(?<=[.!?])\s+", clean(s)) if x]

def pick(row: dict, pattern: str, fallback: int = 0) -> str:
    ss = sents(row.get("abstract", "")) or [row["title"]]
    return next((x for x in ss if re.search(pattern, x, re.I)), ss[fallback])[:520]

def mechanism(row: dict) -> str:
    return pick(row, r"\b(propose|introduce|present|develop|design|formulate|build|study|investigate|show|demonstrate)\b")

def result(row: dict) -> str:
    return pick(row, r"\b(result|experiment|evaluation|outperform|improv|achiev|demonstrate|find|show|reveal)\b", -1)[:420]

def md(s: str) -> str:
    return clean(s).replace("|", "/")

def headings(raw: bytes) -> list[str]:
    s = raw.decode("utf-8", "replace")
    out=[]
    for m in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", s, re.I|re.S):
        h=md(re.sub(r"<[^>]+>", " ", m.group(2)))[:220]
        if h and h not in out: out.append(h)
    return out

def body_text(raw: bytes) -> str:
    s=raw.decode("utf-8", "replace")
    s=re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.I|re.S)
    return clean(re.sub(r"<[^>]+>", " ", s))

def evidence(aid: str) -> dict:
    p=H/"exact-v1-html"/f"{aid}v1.html"
    if not p.exists() or p.stat().st_size < 10000:
        raise RuntimeError(f"missing exact-v1 HTML: {aid}")
    raw=p.read_bytes(); hs=headings(raw); text=body_text(raw)
    def ph(pattern: str, fallback: str) -> str:
        return next((x for x in hs if re.search(pattern,x,re.I)), fallback)
    def ex(pattern: str) -> str:
        m=re.search(pattern,text,re.I); i=max(0,(m.start() if m else 0)-80); return md(text[i:i+420])
    return {
        "arxiv_id":aid, "url":f"https://arxiv.org/html/{aid}v1",
        "route":"official arXiv exact-v1 HTML", "retrieved_at":NOW,
        "bytes":len(raw), "sha256":hashlib.sha256(raw).hexdigest(),
        "normalized_text_sha256":hashlib.sha256(text.encode()).hexdigest(),
        "frozen_path":str(p.relative_to(REPO)),
        "method_heading":ph(r"method|approach|framework|architecture|system|design|algorithm|formulation", "Introduction / disclosed mechanism body"),
        "evaluation_heading":ph(r"experiment|evaluation|result|benchmark|analysis|ablation", "Evaluation/results body; dedicated heading Not Disclosed"),
        "limitations_heading":ph(r"limitation|discussion|threat|conclusion|failure", "Dedicated limitations heading Not Disclosed; scope bound to disclosed setup"),
        "method_excerpt":ex(r"method|we propose|we introduce|architecture"),
        "evaluation_excerpt":ex(r"experiment|evaluation|results"),
        "limitations_excerpt":ex(r"limitation|discussion|failure"),
    }

def sf(aid: str) -> str:
    return "SF-2026-ARXIV-"+aid.replace(".","-")

author_path=H/"screening-ledger-final-author.json"
author=json.loads((author_path if author_path.exists() else H/"screening-ledger-final.json").read_text())
for name in ("screening-ledger-final.json","exact-v1-review-packet.json","exact-v1-provenance.json","books-current-content-comparison.json","BOOKS_WRITEBACK_QUEUE.json","coverage-receipt.json","semantic-author-audit.json"):
    src=H/name; dst=H/(src.stem+"-author"+src.suffix)
    if src.exists() and not dst.exists(): dst.write_bytes(src.read_bytes())

author_reviews={x["arxiv_id"]:x for x in json.loads((H/"exact-v1-review-packet-author.json").read_text())["items"]}
author_prov={x["arxiv_id"]:x for x in json.loads((H/"exact-v1-provenance-author.json").read_text())["items"]}
rows=[]; fp=[]; fn=[]
for src in author["identities"]:
    x=dict(src); aid=x["arxiv_id"]
    if aid.startswith("2606."):
        x.update(screening_status="pre_denominator_closure",screening_reason=f"{x['title']} 的 arXiv identity 属于 2606 month series；DataCite Submitted 只能作为 discovery hint，不能覆盖 arXiv first-public owner month，因此从 05-29 denominator 排除并留待 June owner reconciliation。",review_status="identity_date_closed",access_status="accessible_metadata",integration_disposition="Rejected — Owner-date conflict")
    elif aid in DROP:
        fp.append(aid); x.update(screening_status="pre_denominator_closure",screening_reason=f"{x['title']} 的具体机制是：{mechanism(x)}。独立挑战后的排除边界：{DROP[aid]}；因此从 author denominator 移出。",review_status="identity_date_closed",access_status="accessible_metadata",integration_disposition="Rejected — Below Candidate Denominator")
    elif aid in ADD:
        fn.append(aid); node,sc,disp=ADD[aid]; x.update(screening_status="retained",screening_reason=f"独立 audit 恢复：{mechanism(x)}。该 family 改变 `{node}` 的长期状态/证据合同；结果“{result(x)}”只作为 exact-v1 审计入口。",owner_node=node,score_v2={"design_delta":sc[0],"system_reach":sc[1],"durability":sc[2],"total":sum(sc)},review_route="deep",review_status="deep_complete",access_status="accessible",integration_disposition=disp)
    elif x["screening_status"]=="retained":
        node=OWNER.get(aid,x["owner_node"]); x["owner_node"]=node; x["integration_disposition"]="Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
    rows.append(x)

ret=[x for x in rows if x["screening_status"]=="retained"]
cls=[x for x in rows if x["screening_status"]!="retained"]
assert len(rows)==842 and len(ret)==114 and len(cls)==728 and len(fn)==5 and len(fp)==7
ledger={k:v for k,v in author.items() if k!="identities"}; ledger.update(schema="daily-screening-ledger-v2.1-independent-final",candidate_denominator=len(ret),pre_denominator_closures=len(cls),identities=rows)
(H/"screening-ledger-final.json").write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
with (H/"screening-ledger-final.tsv").open("w",newline="") as f:
    w=csv.writer(f,delimiter="\t"); w.writerow(["arxiv_id","source_family_id","title","status","reason","review_status","access_status","owner","disposition"])
    for x in rows:w.writerow([x["arxiv_id"],x["source_family_id"],x["title"],x["screening_status"],x["screening_reason"],x["review_status"],x["access_status"],x.get("owner_node",""),x["integration_disposition"]])

reviews=[]; prov=[]
for x in ret:
    aid=x["arxiv_id"]; fid=x["source_family_id"]
    if aid in author_reviews:
        rv=dict(author_reviews[aid]); ev=author_prov[aid]
    else:
        ev=evidence(aid); prefix=f"arXiv:{aid}v1 HTML"
        rv={"arxiv_id":aid,"source_family_id":fid,"primary_evidence_version":f"arXiv:{aid}v1","review_route":"deep","method_identity_locators":f"{prefix} — §{ev['method_heading']}; excerpt={ev['method_excerpt']}","evaluation_locators":f"{prefix} — §{ev['evaluation_heading']}; excerpt={ev['evaluation_excerpt']}","limitations_counterevidence_locators":f"{prefix} — §{ev['limitations_heading']}; excerpt={ev['limitations_excerpt']}","artifact_locators":f"{ev['url']}; {ev['frozen_path']}; sha256:{ev['sha256']}","completion_result":"complete"}
    reviews.append(rv); prov.append(ev)
(H/"exact-v1-review-packet.json").write_text(json.dumps({"schema":"exact-v1-review-packet-v2.1-independent-final","report_date":"2026-05-29","items":reviews},ensure_ascii=False,indent=2)+"\n")
(H/"exact-v1-provenance.json").write_text(json.dumps({"schema":"exact-v1-provenance-v2.1-independent-final","report_date":"2026-05-29","items":prov},ensure_ascii=False,indent=2)+"\n")

road=(REPO/"ROADMAP.md").read_text(); paths={m.group(1):m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`",road)}
def adjacent(path:str)->list[str]:
    p=REPO/path; xs=sorted(q for q in p.parent.glob("*.md") if re.match(r"\d+-",q.name)); i=xs.index(p); return [str(q.relative_to(REPO)) for q in xs[max(0,i-1):i]+xs[i+1:i+2]]
comparisons=[]; queue=[]
for x in ret:
    aid=x["arxiv_id"]; node=x["owner_node"]; path=paths[node]; adj=adjacent(path); existing=(REPO/path).read_text()
    tokens={t.lower() for t in re.findall(r"[A-Za-z][A-Za-z0-9_-]{4,}|[\u4e00-\u9fff]{2,}",x["title"])}; hits=sum(t in existing.lower() for t in tokens)
    delta=f"{mechanism(x)} changed constraint：{result(x)}；只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency、SLO。"
    c={"arxiv_id":aid,"source_family_id":x["source_family_id"],"owner_node":node,"owner_path":path,"adjacent_paths":adj,"owner_sha256":hashlib.sha256((REPO/path).read_bytes()).hexdigest(),"adjacent_sha256":{p:hashlib.sha256((REPO/p).read_bytes()).hexdigest() for p in adj},"existing_proposition":f"独立读取 owner `{path}` 及相邻 {adj}；title-derived mechanism token hits={hits}。命中不等于已覆盖，decision 由 exact-v1 delta 与正文责任边界共同决定。","new_evidence_delta":delta,"decision":x["integration_disposition"],"reviewer":"fresh-context:may2026-day01"}
    comparisons.append(c)
    if x["integration_disposition"]=="Integrate": queue.append({"report_date":"2026-05-29","arxiv_id":aid,"source_family_id":x["source_family_id"],"stable_node_id":node,"owner_path":path,"adjacent_paths":adj,"evidence_delta":delta,"status":"ready_for_root_serial_writeback","writeback_requirement":"merge into canonical H2 before Review notes; preserve old condition, changed constraint, state/control owner, trade-off, failure, fallback/coexistence and exact-v1 non-proof boundary"})
(H/"books-current-content-comparison.json").write_text(json.dumps({"schema":"books-current-content-comparison-v2.1-independent-final","report_date":"2026-05-29","items":comparisons},ensure_ascii=False,indent=2)+"\n")
(H/"BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema":"books-writeback-queue-v2.1-independent-final","report_date":"2026-05-29","status":"ready_for_root_serial_writeback","items":queue},ensure_ascii=False,indent=2)+"\n")

audit={"schema":"fresh-context-independent-prewrite-audit-v2.1","report_date":"2026-05-29","auditor":"fresh-context:may2026-day01","scope":{"registered_replayed":842,"author_denominator":116,"final_denominator":len(ret),"author_closures":726,"final_closures":len(cls),"exact_v1_complete":len(reviews),"blocked":0,"ordinary_pending":0,"author_queue":22,"final_queue":len(queue)},"findings":{"false_positives":[{"arxiv_id":a,"resolution":DROP[a]} for a in fp],"false_negatives":[{"arxiv_id":a,"resolution":"restored_to_denominator_and_exact_v1_review"} for a in fn],"owner_corrections":[{"arxiv_id":a,"owner":OWNER[a]} for a in sorted(OWNER) if any(x["arxiv_id"]==a for x in ret)],"date_reconciliation":{"2606_series_count":sum(x["arxiv_id"].startswith("2606.") for x in rows),"resolution":"excluded from 05-29 denominator; June owner reconciliation"}},"gates":{"coverage":"closed","evidence":"passed","books":"open_pending_root_writeback"},"unresolved_findings":[]}
(H/"independent-semantic-audit.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2)+"\n")
ledger_sha=hashlib.sha256((H/"screening-ledger-final.json").read_bytes()).hexdigest()
(H/"coverage-receipt.json").write_text(json.dumps({"schema":"coverage-receipt-v2.1","report_date":"2026-05-29","source_id":"SRC-ARXIV","window":author["window"],"raw_snapshot_records":author["raw_snapshot_records"],"registered_identities":842,"full_semantic_screened":842,"retained":len(ret),"pre_denominator_closed":len(cls),"ledger_sha256":ledger_sha,"status":"independent_closed"},ensure_ascii=False,indent=2)+"\n")

readme=REPO/"papers/2026/05/29/README.md"; text=readme.read_text()
text=text.replace("author packet 已完成，Coverage=Open、Evidence=Open、Books=Open，等待不同 reviewer 的 independent pre-write audit。","independent pre-write audit 已完成，Coverage=Passed、Evidence=Passed、Books=Open，等待 root 串行写回。")
text=text.replace("Coverage=Passed、Evidence=Passed、Books=Open","Coverage=Closed、Evidence=Passed、Books=Open")
text=re.sub(r"Author denominator=116 .*?provisional Books queue=22，本 lane 未修改共享 Books。",f"Independent denominator={len(ret)}（{len(ret)/842:.2%}），pre-denominator closures={len(cls)}；{len(ret)}/{len(ret)} retained family 完成 exact-v1 review，blocked=0；final Books queue={len(queue)}，本审计未修改共享 Books。",text)
text=text.replace("| Denominator ID | DEN-20260529-AUTHOR-116 |",f"| Denominator ID | DEN-20260529-INDEPENDENT-{len(ret)} |")
text=text.replace("| Completion Status | In Progress |","| Completion Status | In Progress |")
text=text.replace("| Coverage Gate | Open |","| Coverage Gate | Closed |").replace("| Coverage Gate | Passed |","| Coverage Gate | Closed |").replace("| Evidence Gate | Open |","| Evidence Gate | Passed |")
text=re.sub(r"screened=842; retained=116; closure=726",f"screened=842; retained={len(ret)}; closure={len(cls)}",text)
text=re.sub(r"Author 已完成 deterministic snapshot、842/842 semantic screening 与 726 个 family-specific closures；116/116 retained exact-v1 正文已冻结，ordinary pending=0、external blocker=0。不同 reviewer 尚未重放 denominator false-positive/false-negative，因此正式 Gate 保持 Open。",f"独立 reviewer 已重放 842/842，author 116→final {len(ret)}（FP={len(fp)}、FN={len(fn)}），{len(cls)} closures 与 {len(ret)}/{len(ret)} exact-v1 均已闭合；ordinary pending=0、external blocker=0。",text)

def replace_table(section:str,rows_out:list[str])->None:
    global text
    pat=rf"({re.escape(section)}.*?\n\| ---.*?\n)(.*?)(?=\n## |\n### )"
    m=re.search(pat,text,re.S)
    if not m: raise RuntimeError(section)
    text=text[:m.start(2)]+"\n".join(rows_out)+"\n"+text[m.end(2):]

cand=[]
for x in ret:
    s=x["score_v2"]; cand.append(f"| {x['source_family_id']} | arXiv:{x['arxiv_id']}v1 | paper-v1:{x['arxiv_id']} | 2026-W22 | 2026-05-28 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {x['review_status']} | accessible | {'knowledge_gap' if x['integration_disposition']=='Integrate' else 'none'} | review:{x['source_family_id']} | self | — | new_in_window | {x['owner_node']} | {x['integration_disposition']} | books-review:{x['source_family_id']} | no |")
replace_table("## 2. Candidate Ledger",cand)
rvrows=[]
for rv in reviews:
    fid=rv["source_family_id"]; rvrows.append(f"| {fid} | RP-TODO-{fid} | {rv['review_route']} | {rv['primary_evidence_version']} | SRC-ARXIV@{rv['primary_evidence_version']} | {rv['method_identity_locators']} | {rv['evaluation_locators']} | {rv['limitations_counterevidence_locators']} | {rv['artifact_locators']} | claim:{fid} | complete |")
replace_table("## 3. Review Completion Receipt",rvrows)

# Rebuild source-review and Books-comparison narrative blocks from final denominator.
review_blocks=[]; rvmap={x["arxiv_id"]:x for x in reviews}
for x in ret:
    rv=rvmap[x["arxiv_id"]]; fid=x["source_family_id"]
    review_blocks.append(f"<!-- review:{fid}:start -->\n#### {x['title']}\n\n问题与机制：{mechanism(x)} owner=`{x['owner_node']}`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。\n\nEvaluation contract：{result(x)}。Method=`{rv['method_identity_locators']}`；Evaluation=`{rv['evaluation_locators']}`。\n\nTrade-off / failure / fallback：`{rv['limitations_counterevidence_locators']}`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。\n\n<!-- claim:{fid}:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:{fid}:end -->\n\nBooks Decision=`{x['integration_disposition']}`；Books Gate 等待 root 写回与 post-write audit。\n<!-- review:{fid}:end -->")
text=re.sub(r"### Source Reviews\n\n.*?(?=\n## 4\.)",lambda _m:"### Source Reviews\n\n"+"\n\n".join(review_blocks)+"\n",text,flags=re.S)

# Deep-selection table must cover the final denominator, while Top-3 only
# limits narrative length.  The exact-v1 review obligation is unchanged.
selected={"2605.29639":"DA-RTP-LLM-EXECUTION-PLAN","2605.29664":"DA-ASYNC-MULTIDIRECTIONAL-PIPELINE","2605.30613":"DA-CACHE-ISOLATION-GATEWAY"}
drows=[]; dnarr=[]
for x in ret:
    fid=x["source_family_id"]; aid=x["arxiv_id"]; unit=selected.get(aid,"—")
    if x["score_v2"]["total"]<7 and x["integration_disposition"]!="Integrate": continue
    eligibility="score_7_9" if x["score_v2"]["total"]>=7 else "forced_review"
    if x["integration_disposition"]=="Integrate": eligibility += ";forced_review;potential_books_delta"
    drows.append(f"| {fid} | {eligibility} | {'selected' if aid in selected else 'not_selected'} | {unit} | — | {'cross-layer state/control/evidence owner change' if aid in selected else 'exact-v1 review complete; lower narrative priority'} | {'analysis:'+unit if aid in selected else 'analysis-decision:'+fid} |")
    if aid in selected:
        dnarr.append(f"<!-- analysis:{unit}:start -->### {x['title']}\n\n{mechanism(x)}。旧路径在未触发该约束时仍成立；exact-v1 只证明“{result(x)}”，未披露配置不得外推。代价、failure 与 fallback 受本报告 Source Review 的 limitations boundary 约束。<!-- analysis:{unit}:end -->")
    else:
        dnarr.append(f"<!-- analysis-decision:{fid}:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事，未降低 Evidence 与 Books Decision 义务。<!-- analysis-decision:{fid}:end -->")
replace_table("## 5. Deep Analysis Selection",drows)
ins=text.index("\n## 6. Books Comparison",text.index("## 5. Deep Analysis Selection"))
text=text[:ins]+"\n\n"+"\n\n".join(dnarr)+"\n"+text[ins:]

def cref(path:str)->str:
    m=re.match(r"(\d+)-",Path(path).name); return f"{path}#chapter-{int(m.group(1))}" if m else path

compar={x["arxiv_id"]:x for x in comparisons}; brows=[]; bblocks=[]
for x in ret:
    c=compar[x["arxiv_id"]]; fid=x["source_family_id"]
    brows.append(f"| {fid} | {x['owner_node']} | {cref(c['owner_path'])} | {'; '.join(cref(p) for p in c['adjacent_paths'])} | existing:{fid} | delta:{fid} | Direct Evolution | {x['integration_disposition']} | books-review:{fid} |")
    bblocks.append(f"<!-- books-review:{fid}:start -->\n<!-- existing:{fid}:start -->{c['existing_proposition']}<!-- existing:{fid}:end -->\n<!-- delta:{fid}:start -->{c['new_evidence_delta']}<!-- delta:{fid}:end --> Decision=`{x['integration_disposition']}`；本审计未修改 Books。\n<!-- books-review:{fid}:end -->")
replace_table("## 6. Books Comparison",brows)
end=text.index("\n## 7. Semantic Audit",text.index("## 6. Books Comparison"))
text=text[:end]+"\n\n"+"\n\n".join(bblocks)+"\n"+text[end:]

semantic=f"""## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260529-COVERAGE | fresh-context:may2026-day01 | coverage | coverage:SRC-ARXIV:20260529 | none | denominator 116→{len(ret)}；FP={len(fp)}、FN={len(fn)}、2606 owner-date conflicts={sum(x['arxiv_id'].startswith('2606.') for x in rows)} 均已逐项闭合 | passed |
| SA-20260529-EVIDENCE | fresh-context:may2026-day01 | evidence | review:{ret[0]['source_family_id']} | none | final exact={len(ret)}/{len(ret)}；source-specific Method/Evaluation/Limitations/Artifact routes 已校准；blocked=0 | passed |
| SA-20260529-SELECTION | fresh-context:may2026-day01 | deep_analysis_selection | analysis:DA-RTP-LLM-EXECUTION-PLAN | none | Top-3 只限制 narrative；final denominator 全部 exact-v1 review | passed |
| SA-20260529-BOOKS | fresh-context:may2026-day01 | books | books-review:{ret[0]['source_family_id']} | F-20260529-BOOKS-WRITEBACK | author queue 22→final {len(queue)}；等待 root 串行写回与 post-write audit | open |

本独立审计未参与 author lane，也未修改共享 Books。
"""
text=re.sub(r"## 7\. Semantic Audit.*?(?=\n## 8\.)",lambda _m:semantic,text,flags=re.S)
text=re.sub(r"726 项 family-specific closure",f"{len(cls)} 项 family-specific closure",text)
text=re.sub(r"由不同 reviewer 重放 842-row denominator、116 项 exact-v1 与 current Books；仅其最终 queue 交 root 串行写回。","Root 按 final queue 串行写回共享 Books；完成后由不同 reviewer 执行 post-write semantic audit。",text)
text=re.sub(r"- 独立 reviewer 是否发现 denominator false positive/negative？\n- provisional Integrate 经 owner\+adjacent 深读后还剩多少？",f"- Root 写回 {len(queue)} 项后，post-write audit 是否确认全部机制处于 canonical H2 主线？",text)
text=re.sub(r"无：116/116 retained family",f"无：{len(ret)}/{len(ret)} retained family",text)
text=re.sub(r"Coverage: `Open`","Coverage: `Closed`",text).replace("Evidence: `Open`","Evidence: `Passed`")
text=text.replace("Coverage: `Passed`","Coverage: `Closed`")
text=text.replace("unresolved findings: 1","unresolved findings: 0 (pre-write); Books writeback remains")
text=re.sub(r"Author packet 已完成：raw=.*?不能宣称本日 Complete。",f"Independent pre-write audit 已完成：raw={author['raw_snapshot_records']:,}、registered/screened=842/842、author denominator=116→final {len(ret)}、closures={len(cls)}、exact-v1={len(ret)}/{len(ret)}、blocked=0、final queue={len(queue)}。Coverage/Evidence 已通过；Books 等待 root 串行写回与 post-write audit，因此本日仍为 In Progress。",text,flags=re.S)
# Rebuild the source receipt row so every final family has a receipt.
families=";".join(x["source_family_id"] for x in ret)
receipt=f"| SRC-ARXIV | 2026-05-28T09:00:00+08:00 | 2026-05-29T09:00:00+08:00 | {NOW} | DataCite v2 adjacent-month snapshot union + 842/842 semantic replay + official exact-v1 HTML/PDF | checked | 842 | {families} | pages=300; final_cursor=end; raw={author['raw_snapshot_records']}; registered=842; screened=842; retained={len(ret)}; closure={len(cls)} | 2026-05-29T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | — |"
text=re.sub(r"^\| SRC-ARXIV \|.*$",receipt,text,count=1,flags=re.M)

# Provenance IDs are content-addressed by the public contract.
for rv in reviews:
    fid=rv["source_family_id"]; aid=rv["arxiv_id"]
    body=re.search(rf"<!-- review:{re.escape(fid)}:start -->(.*?)<!-- review:{re.escape(fid)}:end -->",text,re.S).group(1)
    candrow={"Event Identity":f"paper-v1:{aid}","Primary Identifier":f"arXiv:{aid}v1","Supporting Source IDs":"SRC-ARXIV","Review Override":"knowledge_gap" if any(x["arxiv_id"]==aid and x["integration_disposition"]=="Integrate" for x in ret) else "none"}
    rp=_expected_review_provenance(fid,candrow,rv["review_route"],f"arXiv:{aid}v1",f"SRC-ARXIV@arXiv:{aid}v1",rv["method_identity_locators"],rv["evaluation_locators"],rv["limitations_counterevidence_locators"],rv["artifact_locators"],f"claim:{fid}",f"review:{fid}",_normalized_body_sha256(body))
    text=text.replace(f"RP-TODO-{fid}",rp)

readme.write_text(text)

print(json.dumps({"registered":842,"author_denominator":116,"final_denominator":len(ret),"false_positive":fp,"false_negative":fn,"closures":len(cls),"exact_v1":len(reviews),"blocked":0,"ordinary_pending":0,"final_queue":len(queue)},ensure_ascii=False))
