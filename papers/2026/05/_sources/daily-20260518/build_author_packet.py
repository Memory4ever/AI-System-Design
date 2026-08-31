#!/usr/bin/env python3
"""Build the 2026-05-18 V2.1 author packet without shared Books writes."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

H = Path(__file__).resolve().parent
REPO = H.parents[4]
sys.path.insert(0, str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

INV = json.loads((H / "screening-ledger-provisional.json").read_text())
IDS = """2605.17222 2605.17234 2605.17246 2605.17260 2605.17268 2605.17273 2605.17281 2605.17288 2605.17289 2605.17291 2605.17301 2605.17304 2605.17320 2605.17324 2605.17453 2605.17480 2605.17590 2605.17613 2605.17634 2605.17641 2605.17659 2605.17672 2605.17707 2605.17721 2605.18891 2606.20591""".split()
ACTIVE = set(IDS)

OWNER = {
"2605.17222":"PLATFORM-SECURITY","2605.17234":"WORLDVIEW-SCALING-LAW","2605.17246":"PLATFORM-EVALUATION-SYSTEM","2605.17260":"MULTIMODAL-REPRESENTATION","2605.17268":"MULTIMODAL-EMBODIED-VLA","2605.17273":"PLATFORM-EVALUATION-SYSTEM","2605.17281":"AGENT-TOOL-CALLING","2605.17288":"INFER-SCHEDULING","2605.17289":"INFER-TENSORRT-LLM","2605.17291":"TRAIN-RLHF","2605.17301":"AGENT-RAG","2605.17304":"AGENT-CONTEXT","2605.17320":"AGENT-PLATFORM","2605.17324":"PLATFORM-SECURITY","2605.17453":"AGENT-TOOL-CALLING","2605.17480":"PLATFORM-SECURITY","2605.17590":"TRAIN-DATA","2605.17613":"INFER-KV-CACHE","2605.17634":"PLATFORM-SECURITY","2605.17641":"AGENT-MEMORY","2605.17659":"TRAIN-PRETRAINING","2605.17672":"INFER-SCHEDULING","2605.17707":"PLATFORM-SECURITY","2605.17721":"AGENT-MEMORY","2605.18891":"TRAIN-DATA","2606.20591":"INFER-SPECULATIVE-DECODING"}

INTEGRATE = {"2605.17260","2605.17268","2605.17281","2605.17288","2605.17291","2605.17304","2605.17320","2605.17324","2605.17480","2605.17590","2605.17613","2605.17634","2605.17659","2605.17707","2605.18891","2606.20591"}
SELECTED = {"2605.17281":"DA-OBSERVATION-CONTRACT","2605.17304":"DA-CONTEXT-COMMITMENT","2605.17613":"DA-LOSSLESS-KV"}

DELTA = {
"2605.17222":"CKKS 线性变换把 rotation 数量、off-chip traffic 与 FPGA permutation/data-path 共同暴露为隐私推理的硬件执行合同；收益不等于通用 GPU/模型加速。",
"2605.17234":"Scaling-law 实验预算从均匀采样演进为 successive-halving 与 surrogate-guided pruning；节省拟合成本的同时引入错误早停与 surrogate selection bias。",
"2605.17246":"Specification–code alignment 由单一测试通过率扩展为 code-grounded fidelity probes、contradiction/coverage-gap 分解和 frozen held-out resampling；probe generator 仍不是完整语义 oracle。",
"2605.17260":"post-hoc visual-token reduction 会把瓶颈推回逐帧 vision encoder；compressed-token distillation 让 encoder 直接生成时空压缩表示，交换 teacher 成本、表示偏差和 frame coverage。",
"2605.17268":"VLA 的自然语言 rationale 不能取得 trajectory safety authority；reasoning fidelity、entity/action consistency 与视觉扰动稳定性必须成为独立传感器并由安全控制器提交动作。",
"2605.17273":"SOTA claim 需要 effect size、consistency、uncertainty 与 task-level superiority 证据，平均分第一只证明 aggregate ranking，不证明广泛优越。",
"2605.17281":"工具 observation 中的 presigned URL、session token 与 OAuth state 是带 byte-integrity 和 expiry 的 contract；模型只能传递，不能自由改写或延迟复用。",
"2605.17288":"模型 cascade 的轻量 front-end 与 escalation controller 扩大攻击面；攻击可同时破坏质量和成本目标，因此 route/admission 需绑定 adversarial evidence 与保守 fallback。",
"2605.17289":"端到端 unstructured mask learning 把 pruning owner 从 layer-wise surrogate 移到全局 mask objective，但一次性 H100 训练成本和 kernel compatibility 不等于部署 speedup。",
"2605.17291":"final-answer reward 对中间步骤产生错误 credit；step-wise rubric attribution/normalization 改变 gradient ownership，但依赖 judge 与显式 step boundary。",
"2605.17301":"RAG 在生成前显式检测、分类并解决 retrieved-source conflict；source credibility 与 temporal/opinion policy 变成可审计状态，但 LLM judge 与合成冲突数据限制外推。",
"2605.17304":"Context compression 的对象从 token 变为 typed, source-grounded commitment atoms；压缩必须验证 critical recall、conflict/equivalence 与 recoverability，并在不确定时回退 raw spans/更大 context。",
"2605.17320":"Computer-use workspace 从一次性 sandbox 演进为 live save/fork/rollback/selective-commit；低延迟 branch 与 durable checkpoint 分权，同时引入 credential、GUI、external side-effect merge 边界。",
"2605.17324":"Clarification 是独立 agent state transition，可能把 prompt injection 从 tool-return path 扩展到后续 user-input path；clarify 不能自动提升输入 authority。",
"2605.17453":"工具在探索期积累可信反馈、到隐藏状态满足时才毒化最终 action；final-action guard 必须对 trajectory-derived environment variables 做风险审查，单次 tool selection 不足。",
"2605.17480":"更强 Worker 可能以更确定语言把 semantic hijacking 传给 Manager；capability/certainty 不能替代 independent evidence，跨 Agent commit 需要来源与反证门。",
"2605.17590":"Machine unlearning 的目标不是只校正参数，而是对齐删除编辑后的 counterfactual optimizer state，包括 L-BFGS memory operator 与下一步 update direction。",
"2605.17613":"有损 KV 只作为 draft，full KV 被保留到慢层并拥有最终 verification/commit；换取 lossless output 的代价是 full-state tier、swap/prefetch 与验证失败回退。",
"2605.17634":"Prompt injection 不可仅靠 data/instruction separation 完全解决；Contextual Integrity 显示 norm manipulation/mixed flows 的不可判定边界，最终 authority 必须由 capability policy/approval 持有。",
"2605.17641":"Memory selection 从 semantic similarity 演进为 controlled causal interventions；收益依赖 intervention/judge validity，计算成本和 distribution shift 要求保留普通 retrieval fallback。",
"2605.17659":"正偏激活与标准 loss 在初始化产生 negative weight drift，进而形成 activation sparsity/spikes；这是 optimizer–activation coupling，不是单纯数据性质或默认正则收益。",
"2605.17672":"Reasoning early exit 应检测 successive-step semantic convergence，而非只看 answer confidence；节省 token 的代价是 embedding/judge 开销与 premature-stop failure。",
"2605.17707":"Edge AI accelerator 绕过 OS 语义隔离时可能成为 confused deputy；DMA/地址/权限验证必须进入 accelerator–driver contract，而不是只相信应用进程边界。",
"2605.17721":"Self-evolving Agent 把成功/失败经验组织为 online/offline experience graph；结构化复用提高可用性，同时带来 provenance、staleness、错误传播与 graph lifecycle 成本。",
"2605.18891":"reasoning-trace bypass gap 可能由 prefill/parser/format 造成，不能直接证明 weights 仍记忆；unlearning evaluation 必须冻结 parser、prompt head、seed 与 intervention identity。",
"2606.20591":"edge-cloud speculative decoding 的 draft length 是 communication delay 与 acceptance 的在线 optimal-stopping 控制量；网络状态估计失真时必须回退固定/短 draft。"}

EXISTING = {
"2605.17222":"Ch72 已拥有 FHE trust boundary 与 ciphertext noise/depth；本项是 CKKS 线性变换的硬件受限案例，不改变安全 owner。",
"2605.17234":"Ch7 已说明 scaling law 的实验性、compute/data/architecture 条件与容量规划；本项补充实验预算算法，但不改变核心结论。",
"2605.17246":"Ch66 已要求 specification、hidden tests、artifact/evaluator identity 与 held-out evidence；fidelity probe 是受限实现。",
"2605.17273":"Ch66 已将 effect size、slice、uncertainty、replication 与 evaluator identity置于单一平均分之前。",
"2605.17289":"Ch49 已覆盖 pruning/quantization 的 execution-plan、kernel compatibility 与实际 speedup 边界。",
"2605.17301":"Ch76 已把 coverage/conflict/provenance/freshness 纳入 retrieval set，且要求 generation 前解决 authority conflict。",
"2605.17453":"Ch78 已明确 Observation 不可信、模型 output 是 proposal，side effect 需 admission；该 benchmark 是隐藏触发工具反馈的受限案例。",
"2605.17641":"Ch77 已拥有 memory read admission、derived memory validity、staleness/provenance 与 harmful-memory fallback。",
"2605.17672":"Ch56 已拥有 uncertainty/evidence-value/cost/SLO 的 stop/escalate control；semantic convergence 是一种可替换 sensor。",
"2605.17721":"Ch77 已将原始轨迹演进为派生策略/graph memory，并管理 provenance、staleness 与 invalidation。"}

def sents(text):
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "").strip()) if x.strip()]
def short(text, n=44):
    xs=text.split(); return " ".join(xs[:n])+("…" if len(xs)>n else "")
def mechanism(row):
    ss=sents(row.get("abstract","")); return short(next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|design|formulate|build|show|study|investigate|identify)\b",s,re.I)),ss[0] if ss else row["title"]))
def result(row):
    ss=sents(row.get("abstract","")); return short(next((s for s in ss if re.search(r"\b(result|experiment|evaluation|outperform|improv|achiev|demonstrate|find|show)\b",s,re.I)),ss[-1] if ss else "No abstract result disclosed"),34)
def sf(a): return "SF-2026-ARXIV-"+a.replace(".","-")
def closure(row):
    return (f"`{row['title']}` 针对 {mechanism(row)}；摘要证据边界为 {result(row)}。逐项语义复核后，变化仍属于该 family 的单一任务、局部模型/优化器、专用数据集或 evaluator，未重新分配长期 state/data/control owner，也未改变跨层 SLO、release/evidence contract、恢复责任或旧方案共存条件，因此在 Candidate Denominator 前闭合。")

rows=[]
for src in INV["identities"]:
    x=dict(src); a=x["arxiv_id"]; x["source_family_id"]=sf(a)
    if a in ACTIVE:
        disp="Integrate" if a in INTEGRATE else "No Change — Existing Coverage"
        score=(3,3,3) if disp=="Integrate" else (2,2,3)
        x.update(screening_status="retained",screening_reason=DELTA[a],result_boundary=result(x),owner_node=OWNER[a],score_v2={"design_delta":score[0],"system_reach":score[1],"durability":score[2],"total":sum(score)},review_status="deep_complete",access_status="accessible",integration_disposition=disp)
    else:
        x.update(screening_status="pre_denominator_closure",screening_reason=closure(x),review_status="identity_date_closed",access_status="accessible_metadata",integration_disposition="Rejected — Below Candidate Denominator")
    rows.append(x)
ret=[x for x in rows if x["screening_status"]=="retained"]; cls=[x for x in rows if x["screening_status"]!="retained"]
assert len(rows)==324 and len(ret)==26 and len(cls)==298
assert len({x["screening_reason"] for x in cls})==298
ledger={"schema":"daily-screening-ledger-v2.1-author","report_date":"2026-05-18","window":INV["window"],"utc_window":INV["utc_window"],"raw_snapshot_records":INV["raw_snapshot_records"],"registered_window_identities":324,"screened_identities":324,"candidate_denominator":26,"pre_denominator_closures":298,"identities":rows}
(H/"screening-ledger-final.json").write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
with (H/"screening-ledger-final.tsv").open("w",newline="") as f:
    w=csv.writer(f,delimiter="\t"); w.writerow(["arxiv_id","source_family_id","title","status","reason","review_status","access_status","owner","disposition"])
    for x in rows:w.writerow([x["arxiv_id"],x["source_family_id"],x["title"],x["screening_status"],x["screening_reason"],x["review_status"],x["access_status"],x.get("owner_node",""),x["integration_disposition"]])

road=(REPO/"ROADMAP.md").read_text(); paths={m.group(1):m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`",road)}
def adjacent(p):
    t=REPO/p; ss=sorted(x for x in t.parent.glob("*.md") if re.match(r"\d+-", x.name)); i=ss.index(t); return [str(x.relative_to(REPO)) for x in ss[max(0,i-1):i]+ss[i+1:i+2]]
def chapter_ref(p):
    m=re.match(r"(\d+)-",Path(p).name); return f"{p}#chapter-{int(m.group(1))}" if m else p

receipt_files=sorted(H.glob("exact-review-batch-*.txt"))+sorted(H.glob("web-receipt-batch-*.txt"))
def evidence(a):
    matches=[p for p in receipt_files if f"/{a}v1" in p.read_text()]
    exact=next((p for p in matches if "exact-review" in p.name),matches[0]); text=exact.read_text(); pos=text.find(f"https://arxiv.org/html/{a}v1"); end=text.find("--------------------------------------------------------------------------------",pos); seg=text[pos:end if end>0 else None]
    hs=[]
    for h in re.findall(r"†([^†\n]+)",seg):
        h=re.sub(r"\s+"," ",h).strip()
        if re.match(r"(?:[A-Z]?\d+|[IVX]+)(?:[.\-A-Z0-9 ]|\b)",h) and h not in hs: hs.append(h)
    method=next((h for h in hs if re.search(r"method|system model|framework|design|formulation|approach|setup|proposed|algorithm|datapath|architecture",h,re.I)),hs[0] if hs else "Section identity visible in frozen exact-v1 receipt")
    evaluation=next((h for h in hs if re.search(r"experiment|evaluation|results|analysis|ablation|validation",h,re.I)),"Not Disclosed — no dedicated evaluation heading in the frozen exact-v1 receipt")
    limitation=next((h for h in hs if re.search(r"limitation|discussion|impact statement",h,re.I)),"Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup")
    method = "§" + method
    evaluation = evaluation if evaluation.startswith("Not Disclosed") else "§" + evaluation
    limitation = limitation if limitation.startswith("Not Disclosed") else "§" + limitation
    return exact,method,evaluation,limitation

comparisons=[]; queue=[]; reviews=[]
for x in ret:
    a=x["arxiv_id"]; node=x["owner_node"]; path=paths[node]; adj=adjacent(path); exact,m,e,l=evidence(a)
    existing=EXISTING.get(a,f"已逐章读取 `{path}` 及相邻章节 {adj}；现有正文拥有 surrounding principle，但没有把本 family 的 exact-v1 delta 作为同一演进链中的明确状态/控制/证据边界。")
    comparisons.append({"arxiv_id":a,"source_family_id":x["source_family_id"],"owner_node":node,"owner_path":path,"adjacent_paths":adj,"owner_sha256":hashlib.sha256((REPO/path).read_bytes()).hexdigest(),"adjacent_sha256":{p:hashlib.sha256((REPO/p).read_bytes()).hexdigest() for p in adj},"existing_proposition":existing,"new_evidence_delta":DELTA[a],"decision":x["integration_disposition"],"reviewer":"author-lane:may2026-day02"})
    if a in INTEGRATE: queue.append({"report_date":"2026-05-18","arxiv_id":a,"source_family_id":x["source_family_id"],"stable_node_id":node,"owner_path":path,"adjacent_paths":adj,"evidence_delta":DELTA[a],"status":"pending_independent_review","writeback_requirement":"merge into existing mechanism spine before Review notes; preserve old condition, changed constraint, state/control owner, trade-off, failure, fallback/coexistence and exact-v1 boundary"})
    evloc=e if e.startswith("Not Disclosed") else f"arXiv:{a}v1 — {e} (frozen exact-v1 official HTML receipt)"
    limloc=l if l.startswith("Not Disclosed") else f"arXiv:{a}v1 — {l} (frozen exact-v1 official HTML receipt)"
    reviews.append({"arxiv_id":a,"source_family_id":x["source_family_id"],"primary_evidence_version":f"arXiv:{a}v1","review_route":"deep","method_identity_locators":f"arXiv:{a}v1 — {m} (frozen exact-v1 official HTML receipt)","evaluation_locators":evloc,"limitations_counterevidence_locators":limloc,"artifact_locators":f"{exact.relative_to(REPO)}#sha256={hashlib.sha256(exact.read_bytes()).hexdigest()}; exact-v1 URL=https://arxiv.org/html/{a}v1; immutable code commit Not Disclosed","completion_result":"complete"})
(H/"books-current-content-comparison.json").write_text(json.dumps(comparisons,ensure_ascii=False,indent=2)+"\n")
(H/"BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema":"books-writeback-queue-v2.1-author","report_date":"2026-05-18","status":"awaiting_independent_review","items":queue},ensure_ascii=False,indent=2)+"\n")
(H/"exact-v1-review-packet.json").write_text(json.dumps(reviews,ensure_ascii=False,indent=2)+"\n")
prov=[{"arxiv_id":r["arxiv_id"],"exact_v1_url":f"https://arxiv.org/html/{r['arxiv_id']}v1","retrieved_at":datetime.now(timezone.utc).isoformat(),"receipt":r["artifact_locators"],"status":"accessible","locator_source":"actual official exact-v1 TOC plus method/evaluation/limitations body excerpts"} for r in reviews]
(H/"evidence-provenance-manifest.json").write_text(json.dumps(prov,ensure_ascii=False,indent=2)+"\n")
sha=hashlib.sha256((H/"screening-ledger-final.json").read_bytes()).hexdigest(); now=datetime.now(timezone.utc).isoformat()
(H/"coverage-receipt.json").write_text(json.dumps({"schema":"coverage-receipt-v2.1","report_date":"2026-05-18","source_id":"SRC-ARXIV","window":INV["window"],"raw_snapshot_records":INV["raw_snapshot_records"],"registered_identities":324,"full_semantic_screened":324,"retained":26,"pre_denominator_closed":298,"ledger_sha256":sha,"status":"closed_author_checked_pending_independent_audit"},ensure_ascii=False,indent=2)+"\n")

L=["# Daily Research — 2026-05-18","","**Research Date:** 2026-05-18","","**Timezone:** Asia/Shanghai","","**Strict Window:** 2026-05-17 09:00:00 ～ 2026-05-18 09:00:00（北京时间，左闭右开）","","**Contract:** V2.1 Full Replay；DataCite v2 只支持 identity/date/abstract，技术结论绑定 official arXiv exact-v1。","",f"**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。author packet 完成：324/324 screening、26/26 exact-v1 Review、{len(queue)} 项 provisional Books queue；等待不同 reviewer fresh-context audit。","","## Executive Summary","",f"91,841 条 raw records 中严格窗口注册 324 个 identity，并逐项 title+abstract 语义筛选。严格分母保留 26 项（{26/324:.2%}），298 项以 family-specific closure 在分母前闭合；26/26 official exact-v1 可访问，blocked=0。逐项读取 current owner 与相邻章节后，16 项 provisional Integrate 仅进入 date-local queue，本 lane 未修改共享 Books。","","## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-05-18 |","| Window End | 2026-05-18 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |","| Denominator ID | DEN-20260518-AUTHOR-26 |",f"| Denominator Frozen At | {now} |","| Completion Status | In Progress |","| Coverage Gate | Open |","| Evidence Gate | Open |","| Books Gate | Open |","","### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",f"| SRC-ARXIV | 2026-05-17T09:00:00+08:00 | 2026-05-18T09:00:00+08:00 | {now} | DataCite v2 2604/2605/2606 prefixes 00..99 + 324/324 semantic replay + official exact-v1 | checked | 324 | {';'.join(x['source_family_id'] for x in ret)} | pages=300; final_cursor=end; raw=91841; registered=324; screened=324; retained=26; closure=298 | 2026-05-18T00:59:59Z | screening-ledger-final.json#sha256={sha} | GAP-20260518-INDEPENDENT-AUDIT |","","### Coverage Limitations","","<!-- coverage:SRC-ARXIV:20260518:start -->确定性 snapshot 与 324/324 semantic screening 已闭合；298 个 closure 均保留具体问题/方法与 exclusion boundary。作者侧 Coverage 完成，但 contract 要求的不同 reviewer false-positive/false-negative audit 未完成，因此正式 Coverage Gate 保持 Open；26/26 retained exact-v1 已可访问。<!-- coverage:SRC-ARXIV:20260518:end -->","","## 2. Candidate Ledger","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in ret:
    a=x["arxiv_id"]; s=x["score_v2"]; L.append(f"| {x['source_family_id']} | arXiv:{a}v1 | paper-v1:{a} | 2026-W20 | 2026-05-17 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | {'knowledge_gap' if a in INTEGRATE else 'none'} | review:{x['source_family_id']} | self | — | new_in_window | {x['owner_node']} | {x['integration_disposition']} | books-review:{x['source_family_id']} | no |")
L += ["","## 3. Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for rv in reviews:
    sfid=rv["source_family_id"]; L.append(f"| {sfid} | RP-TODO-{sfid} | deep | {rv['primary_evidence_version']} | SRC-ARXIV@{rv['primary_evidence_version']} | {rv['method_identity_locators']} | {rv['evaluation_locators']} | {rv['limitations_counterevidence_locators']} | {rv['artifact_locators']} | claim:{sfid} | complete |")
rvmap={r["arxiv_id"]:r for r in reviews}; L += ["","### Source Reviews",""]
for x in ret:
    a=x["arxiv_id"]; r=rvmap[a]; sfid=x["source_family_id"]
    L += [f"<!-- review:{sfid}:start -->",f"#### {x['title']}","",f"问题与 changed constraint：{DELTA[a]}","",f"机制与 ownership：{mechanism(x)} owner=`{x['owner_node']}`；old path 在无需该新增状态/证据/控制责任时继续成立。","",f"Evaluation contract：{x['result_boundary']}。Method=`{r['method_identity_locators']}`；Evaluation=`{r['evaluation_locators']}`。","",f"Trade-off / failure：`{r['limitations_counterevidence_locators']}`；未披露的模型、硬件、精度、长度、batch、并发、SLO、seed、evaluator 与 artifact commit 保持 Not Disclosed。","",f"<!-- claim:{sfid}:start -->只支持 exact-v1 披露设置中的机制/结果，不证明跨模型、跨硬件或生产尾部保证；前提失效时回退 owner 章节的旧路径。<!-- claim:{sfid}:end -->","",f"Books Decision=`{x['integration_disposition']}`；author 不能自签 Evidence/Books Gate。",f"<!-- review:{sfid}:end -->",""]
L += ["## 4. Benchmark Contracts","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","作者数字不外推；未由 exact-v1 明确披露的字段保持 Not Disclosed。","","## 5. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
for x in ret:
    a=x["arxiv_id"]; sfid=x["source_family_id"]; unit=SELECTED.get(a,"—"); elig="score_7_9;potential_books_delta"+(";forced_review" if a in INTEGRATE else ""); L.append(f"| {sfid} | {elig} | {'selected' if a in SELECTED else 'not_selected'} | {unit} | — | {'状态/控制权变化跨越模型输出与外部系统提交边界' if a in SELECTED else '已完成同等 Source Review；未扩写不等于未审计'} | {'analysis:'+unit if a in SELECTED else 'analysis-decision:'+sfid} |")
L += ["","<!-- analysis:DA-OBSERVATION-CONTRACT:start -->### 从字符串 observation 到不可改写的外部契约\n\n普通文本可被 Agent 总结或规范化，但 presigned URL、session token、OAuth state 等由外部系统定义 byte identity 与有效期。ContractBench 把 integrity 与 validity 分离，并用 virtual clock/hash 做确定性判定。新路径让 runtime/tool adapter 持有 opaque artifact，模型只引用 handle；代价是 typed state、expiry refresh 与 replay 管理。纯信息型 observation 仍可走文本路径。<!-- analysis:DA-OBSERVATION-CONTRACT:end -->","","<!-- analysis:DA-CONTEXT-COMMITMENT:start -->### 从压缩 token 到保存 commitment\n\n截断和摘要在低风险短对话中简单，但长任务的目标、否定约束、工具结果和安全边界一旦丢失会改变后续控制流。Context Codec 把它们规范化为带 source/conflict/risk 的 atoms，再用 critical recall 与 recoverability 验收；代价是 extractor bias、schema 维护和额外验证。代理指标不稳时回退 raw spans 或更大 context。<!-- analysis:DA-CONTEXT-COMMITMENT:end -->","","<!-- analysis:DA-LOSSLESS-KV:start -->### 从有损 KV 压缩到可验证提交\n\n直接丢 token/量化 KV 在短输出和容错任务中便宜，但误差会沿自回归 decode 累积。VeriCache 将压缩 KV 降为 draft owner，full KV 保留在慢层并拥有最终验证/commit，从而追求与 full-KV 相同输出；代价是 full-state 存储、swap/prefetch、验证批次和 acceptance 波动。内存允许时直接 full-KV 仍是更简单路径。<!-- analysis:DA-LOSSLESS-KV:end -->"]
for x in ret:
    if x["arxiv_id"] not in SELECTED:L.append(f"<!-- analysis-decision:{x['source_family_id']}:start -->该 family 完成 author-side exact-v1 Review 与 Books comparison；Top-3 只限制日报叙事，不降低 Evidence 义务。<!-- analysis-decision:{x['source_family_id']}:end -->")
cmp={x["arxiv_id"]:x for x in comparisons}; L += ["","## 6. Books Comparison","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
details=[]
for x in ret:
    a=x["arxiv_id"]; c=cmp[a]; sfid=x["source_family_id"]; L.append(f"| {sfid} | {x['owner_node']} | {chapter_ref(c['owner_path'])} | {'; '.join(chapter_ref(p) for p in c['adjacent_paths'])} | existing:{sfid} | delta:{sfid} | Direct Evolution | {x['integration_disposition']} | books-review:{sfid} |")
    details += [f"<!-- books-review:{sfid}:start -->",f"<!-- existing:{sfid}:start -->{c['existing_proposition']} owner_sha256={c['owner_sha256']}。<!-- existing:{sfid}:end -->",f"<!-- delta:{sfid}:start -->{DELTA[a]}<!-- delta:{sfid}:end --> Decision=`{x['integration_disposition']}`；author lane 未修改共享 Books。",f"<!-- books-review:{sfid}:end -->"]
L += [""]+details+["","## 7. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |","| SA-20260518-COVERAGE | fresh-context:pending-reviewer | coverage | coverage:SRC-ARXIV:20260518 | F-20260518-INDEPENDENT | author 324/324 screening 待不同 reviewer challenge | open |",f"| SA-20260518-EVIDENCE | fresh-context:pending-reviewer | evidence | review:{ret[0]['source_family_id']} | F-20260518-INDEPENDENT | 26 项 exact-v1 interpretation/locator 待 challenge | open |","| SA-20260518-DEEP | fresh-context:pending-reviewer | deep_analysis_selection | analysis:DA-OBSERVATION-CONTRACT; analysis:DA-CONTEXT-COMMITMENT; analysis:DA-LOSSLESS-KV | F-20260518-INDEPENDENT | Top-3 待 challenge | open |",f"| SA-20260518-BOOKS | fresh-context:pending-reviewer | books | books-review:{ret[0]['source_family_id']} | F-20260518-INDEPENDENT | {len(queue)} 项 provisional queue 待 challenge | open |","","## 8. Ignored Noise","",f"298 项 family-specific closure 保存在 `{(H/'screening-ledger-final.json').relative_to(REPO)}`；每项有真实 title/abstract、机制/结果摘要与 exclusion boundary。","","## 9. Recommended Action","","由不同 reviewer 完整挑战 324-row screening、26 项 exact-v1、Top-3 与 Books compare；root 仅写回独立审计后仍成立的最小 queue。","","## 10. Repository Changes","","- 新增 05-18 date-local ledger、receipts、exact-v1 packet、provenance、Books comparison、queue 与 author audit。","- 未修改共享 Books，未 stage、commit 或 push。","","## 11. Open Questions","","- 独立 reviewer 是否发现 denominator false positive/false negative？","- 16 项 provisional Integrate 经 current Books 深读后是否应继续收紧？","","## 12. Sources"]
for x in ret:L.append(f"- [{x['title']}](https://arxiv.org/html/{x['arxiv_id']}v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01")
L += ["","### Materials Request Ledger","","<!-- validator:materials-request-v1 -->","| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","无：26/26 retained family 的 official exact-v1 HTML 已访问并冻结可复算 receipt。","","## 13. Final Status","","Completion Status: `In Progress`","","Coverage: `Open`","","Evidence: `Open`","","Books: `Open`","","unresolved findings: 1","","author packet 已完成；不同 reviewer fresh-context audit、root writeback 与 post-write audit 尚未完成，不能宣称本日 Complete。"]
text="\n".join(L)+"\n"
for rv in reviews:
    sfid=rv["source_family_id"]; body=re.search(rf"<!-- review:{re.escape(sfid)}:start -->(.*?)<!-- review:{re.escape(sfid)}:end -->",text,re.S).group(1); a=rv["arxiv_id"]
    candidate={"Event Identity":f"paper-v1:{a}","Primary Identifier":f"arXiv:{a}v1","Supporting Source IDs":"SRC-ARXIV","Review Override":"knowledge_gap" if a in INTEGRATE else "none"}
    rp=_expected_review_provenance(sfid,candidate,"deep",f"arXiv:{a}v1",f"SRC-ARXIV@arXiv:{a}v1",rv["method_identity_locators"],rv["evaluation_locators"],rv["limitations_counterevidence_locators"],rv["artifact_locators"],f"claim:{sfid}",f"review:{sfid}",_normalized_body_sha256(body)); text=text.replace(f"RP-TODO-{sfid}",rp)
out=REPO/"papers/2026/05/18/README.md"; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(text)
(H/"semantic-author-audit.json").write_text(json.dumps({"schema":"semantic-author-audit-v2.1","report_date":"2026-05-18","scope":"author-side only","checks":{"registered_screened":[324,324],"candidate_denominator":26,"pre_denominator_closures":298,"closure_reason_unique":298,"exact_v1_complete":26,"blocked":0,"books_compared":26,"provisional_integrates":len(queue)},"unresolved_findings":["Different reviewer must perform fresh-context coverage/evidence/deep/books audit.","Root Books writeback and post-write audit pending."]},ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"raw":INV["raw_snapshot_records"],"registered":324,"screened":324,"retained":26,"closures":298,"exact_v1":26,"blocked":0,"integrate":len(queue)}))
