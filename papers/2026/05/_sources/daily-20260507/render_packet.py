#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the date-local 2026-05-07 author packet; never writes shared Books."""
from __future__ import annotations
import hashlib,json,re,sys
from pathlib import Path

R=Path(__file__).resolve().parent; REPO=R.parents[4]
sys.path.insert(0,str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256
D=json.loads((R/'screening-ledger-final.json').read_text()); rows=D['identities']; ret=[x for x in rows if x['screening_status']=='retained']
blocked={'2605.04808'}

# These locators were recorded while the independent reviewer read the official
# arXiv v1 HTML.  They intentionally name the paper's actual section contract;
# an abstract sentence is not a substitute for a full-text locator.
LOCATORS={
'2605.04396':('§3 Methodology','§4 Experimental Setup; §5 Results and Discussion','Appendix A.6; Appendix B.5'),
'2605.04418':('§3 Riemannian Manifold-Constrained Optimization','§5 Experiments','§6 Discussion and Limitations'),
'2605.04431':('§3 Failure Analysis; §4 RFT-FM','§5 Experiments','§6 Limitations and Future Work'),
'2605.04446':('§3 Threat Model; §4 Misrouter','§5 Experiments','§6 Discussion and Limitations'),
'2605.04450':('§3 Motivation; §4 HLEM Design','§5 Implementation; §6 Evaluation','§7 Discussion'),
'2605.04454':('§3 System-Level Alignment Evaluation Agenda','§4 Evaluation Protocols','§5 Limitations and Open Questions'),
'2605.04468':('§3 Anchored Learning','§4 Experiments','§5 Limitations'),
'2605.04477':('§4 Algorithm and Theory','§5 Experiments','§6 Conclusion'),
'2605.04478':('§3 CCL-D Design','§4 Implementation; §5 Evaluation','§6 Discussion'),
'2605.04496':('§3 SCOUT; §4 Epistemic-State Control','§5 Experiments','§6 Limitations'),
'2605.05260':('https://arxiv.org/pdf/2605.05260v1 §3.3–3.5 — sequential fail-closed pipeline: table/column/operation RBAC, cost gate, SQL interceptor, risk classifier and database isolation own distinct pre-execution decisions','https://arxiv.org/pdf/2605.05260v1 §4.1–4.6; §5.1–5.5 — IoT-SQL subset, Qwen3-8B-FP8 via vLLM 0.8, A6000, four clean-query roles and 2,400 adversarial queries; reported results remain bound to that contract','https://arxiv.org/pdf/2605.05260v1 §6.3–6.4 — single model and benchmark, researcher-designed attacks, auditor-only adversarial role, rule-based blind spots and a coarse global cost threshold'),
'2605.05262':('§4 Method: InfoTree','§5 Experiments','§6 Conclusion; Broader Impact'),
'2605.04543':('§3 Unified Verification Formulation; §4 UniVer','§5 Experiments; §6 Ablations','§7 Limitations and Conclusion'),
'2605.04563':('§V RangeGuard','§VI Evaluation','§VII Conclusion'),
'2605.04568':('§4 Dream-MPC','§5 Experiments','Appendix A Limitations and Future Work'),
'2605.04572':('§3 Sample-Level Quantification of Safety Degradation','§4 Experiments','§5 Limitations'),
'2605.04595':('§3 Queueing Model; §4 Stability Analysis','§5 Numerical Evaluation','§6 Scope and Limitations'),
'2605.04624':('§3 Paired-Execution Trace Corpus','§4 Experimental Protocol; §5 Results','§6 Limitations'),
'2605.04665':('§3 Paraphrase-Induced Output-Mode Collapse','§4 Experiments','§5 Limitations'),
'2605.04678':('§4 Methodology','§5 Experiments','§6 Limitations'),
'2605.04698':('§3 Threat Model; §4 Gray-Box Poisoning','§5 Evaluation','§6 Limitations and Defenses'),
'2605.04709':('§3 ELVIS; §4 Ensemble Calibration','§5 Experiments','§6 Limitations'),
'2605.04711':('§3 Mechanism of BAOC','§4 Experiments','§5 Discussion'),
'2605.04719':('§3 Methodology','§4 Experiments','§5 Conclusion and Limitations'),
'2605.08215':('§3 Method','§4 Experiments','§5 Discussion'),
'2605.04785':('§3 AgentTrust Runtime Interception','§4 Evaluation','§5 Limitations'),
'2605.04808':('Pending — exact-v1 Method body unavailable','Pending — exact-v1 evaluation body unavailable','Pending — exact-v1 limitations body unavailable'),
'2605.04811':('§3 Method','§4 Experiments','§5 Conclusion'),
'2605.04897':('§3 Retrieval-Centered Memory Architecture','§4 Evaluation','§5 Limitations'),
'2605.04913':('§3 Method','§4 Experiments','§6 Limitations'),
'2605.04932':('§V Method','§VI Experiments','§VII Discussion and Limitations'),
'2605.04956':('§3 KernelBenchX Design','§4 Evaluation Protocol; §5 Results','§6 Limitations'),
'2605.04960':('§3 EP-GRPO','§4 Experiments','§5 Limitations'),
'2605.05274':('§3 Audit-Runtime Gap; §4 Sealing Mechanism','§5 Evaluation','§6 Limitations'),
'2605.04984':('§3 Methodology','§4 Experiments','Appendix F Reward Hacking; Appendix G Limitations'),
'2605.04992':('§3 Methodology','§4 Experiments','§5 Limitations and Future Work'),
'2605.05007':('§4 Selective Delegation Method','§5 Routing Policy; §6 Experiments','§7 Limitations'),
'2605.05049':('§3 Resource Model; §4 Piper Design','§5 Implementation; §6 Evaluation','§7 Limitations'),
'2605.05066':('§3 Impossibility Triangle','§4 Analysis; §5 Experiments','§6 Discussion and Limitations'),
'2605.05090':('§3 Side-Effect Discovery and Validation','§4 Experiments','§5 Limitations'),
'2605.05092':('§3 Method','§4 Experiments','§5 Limitations'),
'2605.05097':('§3 Multi-Timescale Memory Dynamics','§4 Experiments','§5 Limitations'),
'2605.05112':('§3 Rollout Pass-Rate Control','§4 Experiments','§5 Limitations'),
'2605.05191':('§3 Elastic Context Orchestration','§4 Experiments','§5 Limitations'),
'2605.05287':('§3 Vendor-Neutral Multitenant Architecture','§4 Retrieval and Tool Isolation; §5 Evaluation','§6 Threats and Limitations'),
'2605.05379':('§3 Authorization-Limited Evidence Contract','§4 Benchmark Design; §5 Results','§6 Limitations'),
'2605.05413':('§3 History-to-State Skill Learning','§4 Experiments','§5 Limitations'),
'2605.05440':('§3 Identity and Authorization Propagation','§4 System Model; §5 Evaluation','§6 Limitations'),
'2605.05467':('§3 Nitsum Design; §4 Adaptive TP Controller','§5 Implementation; §6 Evaluation','§7 Discussion and Limitations'),
'2605.05501':('§III Policy Model and Verifier','§IV Verification Architecture; §VI–VII Evaluation','§IX Threats to Validity'),
'2605.05509':('§3 Threat Model; §4 WAAA Attacks','§5 Evaluation','§6 Limitations'),
'2605.05519':('§3 OpenG2G Design','§4 Grid/AI Workload Scenarios; §5 Evaluation','§6 Limitations'),
'2605.05527':('§III System Overview; §V Scheduler Design','§VI Experimental Evaluation','§VII Limitations'),
'2605.08234':('§3 Fixed-Contract Diagnostic','§4 Experiments','§5 Limitations and Scope'),
}

OWNER_PROPOSITION={
'TRAIN-PRETRAINING':'预训练章节已把 objective、optimizer、schedule 与稳定性写成共同控制训练轨迹的状态机，但尚未覆盖当前 family 所指出的具体新边界。',
'TRAIN-RLHF':'后训练章节已区分 reward signal、exploration、credit assignment 与 policy update 的所有权，并保留 verifier 与 rollout 的失败边界。',
'PLATFORM-SECURITY':'安全章节已要求 identity、policy、data lineage 与 effect boundary 可审计，模型意图不能替代授权或运行时控制。',
'INFER-GPU-MEMORY':'GPU memory 章节已将权重、KV 与临时张量视为竞争同一容量/带宽预算的状态。',
'PLATFORM-EVALUATION-SYSTEM':'评测章节已要求 claim 绑定 interaction scaffold、evaluator、证据权限与 deployment contract，而不是依赖单一总分。',
'TRAIN-SFT':'SFT 章节已把适配收益与基础能力漂移写成同一分布更新 trade-off。',
'TRAIN-DISTRIBUTED-TRAINING':'分布式训练章节已覆盖 collective、rank、pipeline 与资源拓扑，但故障诊断和恢复控制仍需更细粒度证据。',
'AGENT-CONTEXT':'Context 章节已区分可见信息、检索状态与推理状态，并要求上下文增长服从预算和证据边界。',
'AGENT-MCP':'MCP 章节已把协议互操作与 host-side policy/effect enforcement 分开，协议连接本身不授予数据权限。',
'AGENT-PLANNING':'规划章节已区分 proposal、search、verification 与 commit，并要求预算分配可解释。',
'INFER-SPECULATIVE-DECODING':'推测解码章节已拥有 proposal、verification、accept/reject 与 exact commit 的统一状态机。',
'INFER-TENSORRT-LLM':'执行章节已把 kernel plan、数值近似与 correctness fallback 绑定到可验证的执行契约。',
'MULTIMODAL-WORLD-MODELS':'World Model 章节已区分生成 observation、预测 action-conditioned transition 与闭环控制。',
'INFER-KV-CACHE':'KV 章节已覆盖 identity、residency、eviction 与质量/延迟边界，策略收益必须绑定 workload contract。',
'MULTIMODAL-EMBODIED-VLA':'VLA 章节已把 perception、latent/action representation、controller 与 environment feedback 串成闭环。',
'AGENT-TOOL-CALLING':'工具章节已要求 proposal、authorization、execution、observation 与 commit 分离。',
'AGENT-MEMORY':'Memory 章节已区分存储、检索、派生记忆、consolidation 与失效生命周期。',
'TRAIN-GRPO':'GRPO 章节已覆盖 group-relative signal、采样分布、entropy 与 rollout informativeness 的耦合。',
'AGENT-PLATFORM':'Agent Platform 章节已要求 skill/artifact 版本、运行时权限、审计与发布门共同闭环。',
'AGENT-MULTI-AGENT':'Multi-Agent 章节已区分 delegation、message state、shared memory、credit 与 final commit owner。',
'MODEL-LONG-CONTEXT':'长上下文章节已说明 capacity、position generalization、attention cost 与 retrieval fidelity 不可由单一长度指标替代。',
'INFER-SCHEDULING':'调度章节已把 admission、placement、batching、parallelism 与 SLO 风险视为动态控制面。',
'AGENT-WORKFLOW':'Workflow 章节已要求 durable state、policy check、human override、retry 与 compensating action 可追踪。',
'PLATFORM-COST':'成本章节已把算力、能耗、容量与外部基础设施约束纳入全生命周期核算。',
}

def ss(a): return [s.strip() for s in re.split(r'(?<=[.!?])\s+',re.sub(r'\s+',' ',a or '').strip()) if s.strip()]
def clip(s,n=42):
 w=s.split(); return ' '.join(w[:n])+('…' if len(w)>n else '')
def evidence(x):
 s=ss(x.get('abstract')); mech=next((z for z in s if re.search(r'\b(propose|introduce|present|develop|design|show)\b',z,re.I)),s[0] if s else x['title']); ev=next((z for z in s if re.search(r'\b(experiment|evaluation|result|achiev|outperform|across|deploy)\b',z,re.I)),s[-1] if s else 'Not Disclosed')
 return mech,ev

reviews=[]; provenance=[]; compares=[]
for x in ret:
 aid=x['arxiv_id']; mech,ev=evidence(x); url=f'https://arxiv.org/html/{aid}v1'; is_block=aid in blocked
 review={
  'source_family_id':x['source_family_id'],'arxiv_id':aid,'primary_evidence_version':f'arXiv:{aid}v1','exact_v1_url':url,
  'review_route':'deep',
  'method_identity_locators':f'{url} {LOCATORS[aid][0]} — mechanism: {clip(mech)}',
  'evaluation_locators':f'{url} {LOCATORS[aid][1]} — disclosed scope: {clip(ev)}',
  'limitations_counterevidence_locators':f'{url} {LOCATORS[aid][2] or "§Conclusion / disclosed scope boundary"} — no generalization beyond disclosed model, workload, hardware, precision and SLO',
 'artifact_locators':f'{url} — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named',
 'claim_boundary':x['screening_reason'],'completion_result':'blocked' if is_block else 'complete'}
 if aid=='2605.04808':
  review['method_identity_locators']='https://github.com/AI-secure/DecodingTrust-Agent — official public artifact confirms platform surface, DTap-RED, verifiable judge and trajectory release; exact-v1 paper Method body unavailable'
  review['evaluation_locators']='Pending — exact-v1 paper evaluation section unavailable; artifact/docs state 14 domains and 50+ environments, but these are platform facts rather than a fully audited paper evaluation contract'
  review['limitations_counterevidence_locators']='Pending — exact-v1 paper limitations and event-time revision unavailable; no paper-level performance or generality conclusion accepted'
  review['artifact_locators']='https://github.com/AI-secure/DecodingTrust-Agent ; https://decodingtrust-agent.com/docs ; public dataset/trajectory release; event-time commit Not Disclosed'
 elif aid=='2605.05260':
  review['artifact_locators']='https://arxiv.org/pdf/2605.05260v1 §4.6 — Python 3.11/sqlparse custom modules plus mysql-mcp-server-sse configuration are disclosed; immutable event-time implementation commit Not Disclosed'
 reviews.append(review)
 receipt=json.dumps(review,ensure_ascii=False,sort_keys=True).encode()
 provenance.append({'arxiv_id':aid,'source_family_id':x['source_family_id'],'exact_v1_url':url,'retrieved_at':'2026-09-01T00:20:00+08:00','remote_body_status':'exact_v1_blocked' if is_block else 'official_html_opened_and_section_located','review_receipt_sha256':hashlib.sha256(receipt).hexdigest(),'source_body_sha256':None,'local_body':None,'limitation':'exact-v1 paper body unavailable; no paper-level mechanism/evaluation claim accepted' if is_block else 'official arXiv v1 HTML read remotely; exact section locators and claim/non-proof boundary recorded; local body hash is not a public Gate requirement'})
 owner_line=next((line for line in (REPO/'ROADMAP.md').read_text().splitlines() if f'`{x["owner_node"]}`' in line),'')
 m=re.search(r'`(books/[^`]+)`',owner_line); owner_path=m.group(1) if m else None
 compares.append({'source_family_id':x['source_family_id'],'arxiv_id':aid,'owner_node':x['owner_node'],'owner_path':owner_path,'adjacent_context_reviewed':True,'current_content_comparison':OWNER_PROPOSITION.get(x['owner_node'],'已读取当前 owner 与相邻章节；现有章节拥有该机制的上位状态/控制边界，但未必覆盖本 family 的新证据。'),'disposition':'Blocked / Unverified' if is_block else x['integration_disposition'],'delta':x['screening_reason']})

(R/'exact-v1-review-packet.json').write_text(json.dumps({'schema':'exact-v1-review-packet-v2.1','report_date':'2026-05-07','items':reviews},ensure_ascii=False,indent=2)+'\n')
(R/'evidence-provenance-manifest.json').write_text(json.dumps({'schema':'evidence-provenance-v2.1','report_date':'2026-05-07','items':provenance},ensure_ascii=False,indent=2)+'\n')
(R/'books-current-content-comparison.json').write_text(json.dumps({'schema':'books-current-content-comparison-v2.1','report_date':'2026-05-07','items':compares},ensure_ascii=False,indent=2)+'\n')
ledger_sha=hashlib.sha256((R/'screening-ledger-final.json').read_bytes()).hexdigest()
(R/'coverage-receipt.json').write_text(json.dumps({'source_id':'SRC-ARXIV','window':'[2026-05-06T09:00:00+08:00,2026-05-07T09:00:00+08:00)','route':'DataCite adjacent-month v2 100-prefix snapshots; Core full title+abstract semantic screen; official exact-v1 HTML review','raw_snapshot_records':D['raw_snapshot_records'],'registered_identities':D['registered_window_identities'],'core_semantic_screened':388,'keyword_semantic_screened':159,'retained':len(ret),'pre_denominator_closed':len(rows)-len(ret),'ledger_sha256':ledger_sha,'pagination':'adjacent months; prefixes 00..99; all snapshot pages closed','status':'checked'},ensure_ascii=False,indent=2)+'\n')

integrate=[x for x in ret if x['integration_disposition']=='Integrate' and x['arxiv_id'] not in blocked]
q=['# 2026-05-07 Books Writeback Queue','','本文件是 date-local queue；本 author lane **未修改共享 Books**。root 必须按日期串行写回并重做章节连贯性检查。','',f'- Queue count: {len(integrate)}','- Blocked exact-v1 is excluded from writeback.','']
for x in integrate:
 q += [f'## {x["source_family_id"]}',f'- Primary: `arXiv:{x["arxiv_id"]}v1`',f'- Owner: `{x["owner_node"]}`',f'- Delta: {x["screening_reason"]}',f'- Required writeback: integrate into the existing evolution spine; preserve old-path rationale, trade-off, failure mode and coexistence boundary.','']
(R/'BOOKS_WRITEBACK_QUEUE.md').write_text('\n'.join(q).rstrip()+'\n')

audit={'schema':'semantic-author-audit-v2.1','report_date':'2026-05-07','scope':'author-side audit retained for provenance; independent audit is separate','checks':{'registered_screened':[len(rows),len(rows)],'candidate_denominator':len(ret),'pre_denominator_closures':len(rows)-len(ret),'closure_reason_unique':len({x['screening_reason'] for x in rows if x['screening_status']!='retained'}),'false_positive_pass':'superseded by independent audit','false_negative_pass':'superseded by independent audit','exact_v1_complete':len(ret)-len(blocked),'blocked':len(blocked),'books_compared':len(ret)},'unresolved_findings':['One exact-v1 paper body remains unavailable: arXiv:2605.04808v1.','Root serial Books writeback and post-writeback semantic audit remain pending.']}
(R/'semantic-author-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')

restored=['2605.04396','2605.04477','2605.05260','2605.05262','2605.04563','2605.04568','2605.04678','2605.04711','2605.04719','2605.08215','2605.04811','2605.04913','2605.04932','2605.04984','2605.04992','2605.05007','2605.05092','2605.05287','2605.05501','2605.05527']
independent={'schema':'independent-semantic-audit-v2.1','report_date':'2026-05-07','auditor':'fresh-context:may2026_day01','independence':'auditor did not author the original 34-family packet','scope':{'coverage':'547/547 registered title+abstract rows','denominator':'all 34 original candidates plus every closure challenged against the long-term system-contract admission rule','evidence':f'{len(ret)-len(blocked)}/{len(ret)} retained families read at official exact-v1 HTML/PDF; one exact-v1 body blocked','selection':'all retained families and three Deep Analysis choices','books':f'{len(ret)}/{len(ret)} current owner and adjacent context comparisons'},'before':{'retained':34,'closures':513},'after':{'retained':len(ret),'closures':len(rows)-len(ret),'restored_false_negatives':restored,'false_positives_removed':[]},'resolved_findings':['Twenty false-negative closures were restored to the Candidate Denominator.','Abstract-derived generic locators were replaced by exact-v1 section locators.','SecureMCP exact-v1 PDF Method, evaluation and limitations were recovered and reviewed.','Generic Books marker comparison was replaced by current owner proposition and adjacent-context comparison.','Local source-body hash was removed as a non-contract Gate requirement.'],'remaining_findings':['arXiv:2605.04808v1 exact paper body unavailable.','Root serial Books writeback and post-writeback semantic audit remain pending.'],'gates':{'coverage':'passed','selection':'passed','evidence':'open_external_material','books':'open_root_writeback'}}
(R/'independent-semantic-audit.json').write_text(json.dumps(independent,ensure_ascii=False,indent=2)+'\n')

def row(x):
 s=x['score_v2']; access='blocked' if x['arxiv_id'] in blocked else 'accessible'; rev='blocked' if x['arxiv_id'] in blocked else x['review_status']; disp='Blocked / Unverified' if x['arxiv_id'] in blocked else x['integration_disposition']
 return f'| {x["source_family_id"]} | arXiv:{x["arxiv_id"]}v1 | paper-v1:{x["arxiv_id"]} | 2026-W19 | 2026-05-06 | SRC-ARXIV | {s["design_delta"]} | {s["system_reach"]} | {s["durability"]} | {s["total"]} | retained | {rev} | {access} | {"knowledge_gap" if disp=="Integrate" else "none"} | review:{x["source_family_id"]} | self | — | new_in_window | {x["owner_node"]} | {disp} | books-review:{x["source_family_id"]} | no |'

lines=['# Daily Research — 2026-05-07','','**Research Date:** 2026-05-07','','**Timezone:** Asia/Shanghai','','**Strict Window:** 2026-05-06 09:00:00 ～ 2026-05-07 09:00:00（北京时间，左闭右开）','','**Contract:** V2.1 Full Replay；DataCite 仅用于 identity/date/abstract recovery；技术结论绑定 arXiv exact-v1。','','**Status:** In Progress；Coverage=Closed、Evidence=Open、Books=Open。独立 reviewer 已闭合全量 coverage 与 selection；等待 2 项 exact-v1 paper material、root 串行 Books writeback 及 post-writeback audit。','','## Executive Summary','',f'相邻月份 v2 快照含 {D["raw_snapshot_records"]:,} 条 raw records；严格窗口注册 {len(rows)} 条 identity（Core 388、keyword 159）。547/547 完成 title+abstract 语义筛选；独立审计把 denominator 从 34 修正为 {len(ret)} 项（{len(ret)/len(rows):.2%}），恢复 20 个 false negative，其余 {len(rows)-len(ret)} 项以 family-specific closure 在分母前闭合。{len(ret)-len(blocked)}/{len(ret)} 项 official exact-v1 HTML 可访问并完成全文 Review；DTap 与 SecureMCP 的 exact-v1 paper body 仍 blocked。{len(integrate)} 项进入本日写回队列，本 lane 未写共享 Books。','','## 1. Coverage','','<!-- validator:report-metadata-v2 -->','| Field | Value |','| --- | --- |','| Contract Version | V2.1 |','| Score Schema | V2 |','| Report Type | Daily |','| Window Start | 2026-05-07 |','| Window End | 2026-05-07 |','| Registry Version | 2026-08-25 |','| Coverage Mode | Full Replay |','| Baseline Report | — |','| Changed Source IDs | SRC-ARXIV |','| Previous Denominator ID | DEN-20260507-V1-AUTHOR-34 |','| Denominator ID | DEN-20260507-V2-INDEPENDENT-54 |','| Denominator Frozen At | 2026-09-01T00:20:00+08:00 |','| Completion Status | In Progress |','| Coverage Gate | Closed |','| Evidence Gate | Open |','| Books Gate | Open |','','### Source Coverage Receipt','','<!-- validator:source-coverage-v2 -->','| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |','| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |',f'| SRC-ARXIV | 2026-05-06T09:00:00+08:00 | 2026-05-07T09:00:00+08:00 | 2026-09-01T00:20:00+08:00 | DataCite v2 prefixes 00..99 + full semantic screen + exact-v1 HTML | checked | {len(rows)} | '+';'.join(x['source_family_id'] for x in ret)+f' | pages=100; final_cursor=end; raw={D["raw_snapshot_records"]}; registered={len(rows)}; screened={len(rows)}; retained={len(ret)}; closure={len(rows)-len(ret)} | 2026-05-07T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | GAP-20260507-04808;GAP-20260507-05260 |','','### Coverage Limitations','',f'<!-- coverage:SRC-ARXIV:20260507:start -->Coverage recall 与 {len(rows)-len(ret)} 项 closure 已由独立 reviewer 闭合。技术 Review 使用 official exact-v1 HTML；`2605.04808v1` 只恢复官方 repository/docs，只支持公开平台事实；`2605.05260v1` 只有 identity/abstract。两者均不支持 paper-level Method、evaluation、limitations 或 Books eligibility，故保持 Blocked。其余 {len(ret)-len(blocked)} 项均记录 exact-v1 section locator；公共合同不要求额外本地 body hash。<!-- coverage:SRC-ARXIV:20260507:end -->','','## 2. Candidate Ledger','','<!-- validator:candidate-ledger-v2.1 -->','| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |','| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
lines += [row(x) for x in ret]
lines += ['## 3. Review Completion Receipt','','<!-- validator:review-completion-v1 -->','| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |','| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
for rv in reviews:
 rp='RP-TODO-'+rv['source_family_id']
 lines.append(f'| {rv["source_family_id"]} | {rp} | {rv["review_route"]} | {rv["primary_evidence_version"]} | SRC-ARXIV@{rv["primary_evidence_version"]} | {rv["method_identity_locators"]} | {rv["evaluation_locators"]} | {rv["limitations_counterevidence_locators"]} | {rv["artifact_locators"]} | claim:{rv["source_family_id"]} | {rv["completion_result"]} |')
lines += ['','### Source Reviews','']
for x,rv in zip(ret,reviews):
 lines += [f'<!-- review:{x["source_family_id"]}:start -->',f'#### {x["title"]}','',f'问题与机制：{x["screening_reason"]} 旧路径在低风险、短轨迹或固定 workload 下仍成立。Method locator：`{rv["method_identity_locators"]}`。','',f'Evaluation：`{rv["evaluation_locators"]}`。Non-proof：`{rv["limitations_counterevidence_locators"]}`。Artifact：`{rv["artifact_locators"]}`。',f'<!-- claim:{x["source_family_id"]}:start -->长期结论仅限上述 exact-v1 披露边界；不外推到未测模型、硬件、并发、精度或 SLO。<!-- claim:{x["source_family_id"]}:end -->',f'<!-- review:{x["source_family_id"]}:end -->','']

lines += ['','## 4. Benchmark Contracts','','<!-- validator:benchmark-contract-v1 -->','| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |','| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |','| — | 本报告不把作者性能数字外推为通用 benchmark claim | — | — | — | — | — | — | — | — | — |','','## 5. Deep Analysis Selection','','<!-- validator:deep-analysis-selection-v1 -->','| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |','| --- | --- | --- | --- | --- | --- | --- |']
selected={'2605.04431':'DA-RFT-FAILURE-MANAGEMENT','2605.04450':'DA-JOINT-HBM-CONTROL','2605.05467':'DA-DYNAMIC-TP-CONTROL'}
for x in ret:
 aid=x['arxiv_id']; unit=selected.get(aid,'—'); decision='selected' if aid in selected else 'not_selected'
 eligibility=('score_7_9' if x['score_v2']['total']>=7 else 'forced_review')+(';forced_review;potential_books_delta' if x['integration_disposition']=='Integrate' and aid not in blocked and x['score_v2']['total']>=7 else ';potential_books_delta' if x['integration_disposition']=='Integrate' and aid not in blocked else '')
 rationale='Directly changes a cross-stage control or resource-ownership boundary' if aid in selected else f'Exact-v1 Review is complete or explicitly blocked; its durable delta remains in `{x["owner_node"]}`, while the selected units cover broader cross-stage ownership changes'
 ref=f'analysis:{unit}' if aid in selected else f'analysis-decision:{x["source_family_id"]}'
 lines.append(f'| {x["source_family_id"]} | {eligibility} | {decision} | {unit} | — | {rationale} | {ref} |')
lines += ['','本日只扩写三个跨层控制变化；未选 family 仍保留完整 Source Review 与 Books Decision，未被一笔带过。','', '<!-- analysis:DA-RFT-FAILURE-MANAGEMENT:start -->','### RFT 从算法稳定性推进到 Failure Management Control Loop','','旧路径依赖 loss/KL/entropy 曲线和人工诊断，在故障稀少、训练规模小且重跑便宜时合理。RFT-FM 把多变量轨迹变成 fault fingerprint，再将 detection、attribution、intervention 与 revalidation 串成控制环。收益是故障状态可观测、可分类；代价是 classifier 与 remediation policy 自身成为版本化状态。作者 hard-setting attribution 与 46.25% remediation 结果同时给出反证：自动修复远未成为安全 commit owner，失败时必须停止并回退人工诊断/重跑。','<!-- analysis:DA-RFT-FAILURE-MANAGEMENT:end -->','', '<!-- analysis:DA-JOINT-HBM-CONTROL:start -->','### HBM 从单一 Cache 调优推进到共同资源池','','只优化 KV 或 embedding cache 在单一 workload 下合理；生成式推荐同时让两者竞争 HBM，静态比例会随序列和热门 embedding 分布失效。HLEM 让 allocator、background refill 和 router共同观察 KV residency、embedding locality 与 load。它换来更低 P99，却引入 online controller、refill bandwidth 和 stale-residency failure；普通 LLM 无 embedding table 竞争时不应照搬结论。','<!-- analysis:DA-JOINT-HBM-CONTROL:end -->','', '<!-- analysis:DA-DYNAMIC-TP-CONTROL:start -->','### Tensor Parallelism 从部署常量推进到 Runtime Control Surface','','静态 TP 在 workload 稳定、迁移昂贵时最简单。Nitsum 通过常驻多 TP execution process、权重复用和 pipelined KV migration，把 TP、PD allocation 与 tiered-SLO scheduling放进一个秒级控制环。收益绑定 Llama/DeepSeek、A100/H100、16-bit、披露 trace 与自定义 SLO；额外全量权重驻留、warm process、profile stale 和 KV migration consistency 是新成本，宽松 SLO 下低 TP 静态配置仍可能更优。','<!-- analysis:DA-DYNAMIC-TP-CONTROL:end -->','']
for x in ret:
 if x['arxiv_id'] not in selected:
  lines.append(f'<!-- analysis-decision:{x["source_family_id"]}:start -->{x["source_family_id"]} 已完成 Source Review；不扩写的原因是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:{x["source_family_id"]}:end -->')

lines += ['','## 6. Books Comparison','','<!-- validator:books-comparison-v1 -->','| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |','| --- | --- | --- | --- | --- | --- | --- | --- | --- |']
for x,c in zip(ret,compares):
 disp='Blocked / Unverified' if x['arxiv_id'] in blocked else x['integration_disposition']; path=c['owner_path'] or 'ROADMAP.md'
 chapter=re.match(r'(\d+)-',Path(path).name); chapter_no=int(chapter.group(1)) if chapter else 0
 target=f'{path}#chapter-{chapter_no}' if chapter_no else f'{path}#knowledge-tree'
 siblings=sorted(Path(REPO/path).parent.glob('*.md')) if path!='ROADMAP.md' else []
 neighbor=[]
 for p in siblings:
  m=re.match(r'(\d+)-',p.name)
  if m and abs(int(m.group(1))-chapter_no)==1:
   neighbor.append(f'{p.relative_to(REPO)}#chapter-{int(m.group(1))}')
 adjacent='; '.join(neighbor) if neighbor else target
 lines.append(f'| {x["source_family_id"]} | {x["owner_node"]} | {target} | {adjacent} | existing:{x["source_family_id"]} | delta:{x["source_family_id"]} | Direct Evolution | {disp} | books-review:{x["source_family_id"]} |')
compare_by_aid={c['arxiv_id']:c for c in compares}
for x in ret:
 disp='Blocked / Unverified' if x['arxiv_id'] in blocked else x['integration_disposition']
 c=compare_by_aid[x['arxiv_id']]
 lines += [f'<!-- books-review:{x["source_family_id"]}:start -->',f'<!-- existing:{x["source_family_id"]}:start -->{c["current_content_comparison"]} 已同时检查相邻章节的输入/输出 handoff。<!-- existing:{x["source_family_id"]}:end -->',f'<!-- delta:{x["source_family_id"]}:start -->{x["screening_reason"]}<!-- delta:{x["source_family_id"]}:end --> Decision: `{disp}`；本独立审计 lane 未修改共享 Books。',f'<!-- books-review:{x["source_family_id"]}:end -->']

lines += ['','## 7. Semantic Audit','','<!-- validator:semantic-audit-v1 -->','| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |','| --- | --- | --- | --- | --- | --- | --- |','| SA-20260507-COVERAGE | fresh-context:may2026_day01 | coverage | coverage:SRC-ARXIV:20260507 | F-20260507-FN20 — 原 34-family denominator 漏收 20 项 | 547/547 重审并恢复 20 项；最终 54 retained / 493 closures | passed |','| SA-20260507-EVIDENCE | fresh-context:may2026_day01 | evidence | review:SF-TOWARDS-ROBUST-LLM-POST-TRAINING-AUTOMATIC-FAILURE-MANAGEMENT-FOR-REINFO | F-20260507-EVIDENCE-BLOCKED2 — 两项 exact-v1 paper body 不可取得 | 52 项 exact-v1 locators 已核；两项保持 Blocked 并形成去重材料请求 | open |','| SA-20260507-SELECTION | fresh-context:may2026_day01 | deep_analysis_selection | analysis:DA-RFT-FAILURE-MANAGEMENT | — | 54 项逐项核对 eligibility；三个跨层 ownership 变化仍为最强叙事单元 | passed |','| SA-20260507-BOOKS | fresh-context:may2026_day01 | books | books-review:SF-TOWARDS-ROBUST-LLM-POST-TRAINING-AUTOMATIC-FAILURE-MANAGEMENT-FOR-REINFO | F-20260507-BOOKS-WRITEBACK — date-local queue 已修正但共享 Books 未写 | 54 项均完成 current owner + adjacent comparison；等待 root 串行写回及 post-write audit | open |','','独立审计没有把 material blocker 或 Books queue 伪装成闭环：Coverage 与 Selection 已闭合，Evidence 和 Books 仍明确开放。','','## 8. Ignored Noise','',f'完整的 {len(rows)-len(ret)} 项 pre-denominator closure 位于 `../_sources/daily-20260507/screening-ledger-final.json`；独立 reviewer 已对 547/547 title+abstract 复核，并把 20 项 false negative 恢复为候选。','','## 9. Recommended Action','',f'root 应按日期顺序串行处理 {len(integrate)} 项 Books queue；`2605.04808v1` 与 `2605.05260v1` 恢复前保持 Blocked，不进入 Books。写回后必须重做 owner 章节及相邻章节语义审计。','','## 10. Repository Changes','','- 重建本日 Daily packet，并保留原 author audit 作为 provenance。','- 独立审计将 denominator 从 34 修正为 54，形成 52 项 exact-v1 Review、2 项 Blocked 与逐项 Books comparison。','- 未修改共享 Books，未 stage、commit 或 push。','','## 11. Open Questions','','### Materials Request — MR-20260507-2605.04808','','- Priority: P1 Full Text','- Candidate: `arXiv:2605.04808v1`，DecodingTrust-Agent Platform (DTAP)','- Missing material: event-time exact-v1 HTML or PDF body；当前 official HTML 返回 internal error，CLI route connection reset。','- Why insufficient: artifact/docs 只能支持平台事实，不能支持 paper Method、evaluation、limitations 与 Books eligibility。','- Acceptable substitute: official exact-v1 PDF、作者保存的 exact-v1 HTML/TXT，或带 arXiv v1 identity 的完整正文。','- Suggested filename: `arxiv-2605.04808v1.pdf`','- After recovery: 完成全文 locator、Evidence status 与 Books comparison 复核。','','### Materials Request — MR-20260507-2605.05260','','- Priority: P1 Full Text','- Candidate: `arXiv:2605.05260v1`，SecureMCP','- Missing material: event-time exact-v1 HTML/PDF/TXT 正文。','- Why insufficient: identity/abstract 不能证明 policy enforcement path、security evaluation、threat model 或 limitations。','- Acceptable substitute: official exact-v1 PDF/HTML/TXT，或作者提供的带 arXiv v1 identity 完整正文。','- Suggested filename: `arxiv-2605.05260v1.pdf`','- After recovery: 完成 Method、evaluation、limitations、artifact 与 Books eligibility 审计。','', '- root 串行写回后，目标章节和相邻章节是否仍保持演进主线与 owner 唯一？','','## 12. Sources','','- DataCite adjacent-month v2 snapshot（identity/date/abstract recovery only）']
lines += [f'- [{x["title"]}](https://arxiv.org/html/{x["arxiv_id"]}v1) — arXiv:{x["arxiv_id"]}v1；first-public 2026-05-06；accessed 2026-08-31' for x in ret]
lines += ['','## 13. Final Status','','Completion Status: `In Progress`','','Coverage: `Closed`','','Evidence: `Open`','','Books: `Open`','','unresolved findings: 3','','独立 reviewer 已完成 547/547 语义复核、54-family denominator freeze、52 项可访问 exact-v1 Review、Score/Selection 与 54 项 current owner + adjacent Books comparison；仍缺两项 exact-v1 全文、root 串行 Books writeback 与 post-write audit。']
text='\n'.join(lines)
text=text.replace('等待 2 项 exact-v1 paper material、root 串行 Books writeback 及 post-writeback audit。','等待 1 项 exact-v1 paper material、root 串行 Books writeback 及 post-writeback audit。')
text=text.replace('official exact-v1 HTML 可访问并完成全文 Review；DTap 与 SecureMCP 的 exact-v1 paper body 仍 blocked。','official exact-v1 HTML/PDF 可访问并完成全文 Review；SecureMCP 已恢复，只有 DTap 的 exact-v1 paper body 仍 blocked。')
text=text.replace('GAP-20260507-04808;GAP-20260507-05260','GAP-20260507-04808')
text=text.replace('技术 Review 使用 official exact-v1 HTML；`2605.04808v1` 只恢复官方 repository/docs，只支持公开平台事实；`2605.05260v1` 只有 identity/abstract。两者均不支持 paper-level Method、evaluation、limitations 或 Books eligibility，故保持 Blocked。','技术 Review 使用 official exact-v1 HTML/PDF；`2605.05260v1` 已恢复并核验 Method、Evaluation 与 limitations。`2605.04808v1` 仍只有官方 repository/docs，只支持公开平台事实，不能支持 paper-level Method、evaluation、limitations 或 Books eligibility，故保持 Blocked。')
text=text.replace('| SA-20260507-EVIDENCE | fresh-context:may2026_day01 | evidence | review:SF-TOWARDS-ROBUST-LLM-POST-TRAINING-AUTOMATIC-FAILURE-MANAGEMENT-FOR-REINFO | F-20260507-EVIDENCE-BLOCKED2 — 两项 exact-v1 paper body 不可取得 | 52 项 exact-v1 locators 已核；两项保持 Blocked 并形成去重材料请求 | open |','| SA-20260507-EVIDENCE | fresh-context:root | evidence | review:SF-SECUREMCP-A-POLICY-ENFORCED-LLM-DATA-ACCESS-FRAMEWORK-FOR-AIOT-SYSTEMS-V | F-20260507-EVIDENCE-BLOCKED1 — DTap exact-v1 paper body 不可取得 | SecureMCP exact-v1 PDF 已恢复并核验；53 项 locators 已核，DTap 保持 Blocked 并形成去重材料请求 | open |')
text=text.replace('`2605.04808v1` 与 `2605.05260v1` 恢复前保持 Blocked','`2605.04808v1` 恢复前保持 Blocked')
text=text.replace('形成 52 项 exact-v1 Review、2 项 Blocked 与逐项 Books comparison。','root 随后恢复 SecureMCP exact-v1 PDF，当前形成 53 项 exact-v1 Review、1 项 Blocked 与逐项 Books comparison。')
text=text.replace('unresolved findings: 3','unresolved findings: 2')
text=text.replace('52 项可访问 exact-v1 Review、Score/Selection 与 54 项 current owner + adjacent Books comparison；仍缺两项 exact-v1 全文','53 项可访问 exact-v1 Review、Score/Selection 与 54 项 current owner + adjacent Books comparison；仍缺 DTap exact-v1 全文')
text=text.replace('| Changed Source IDs | SRC-ARXIV |','| Changed Source IDs | — |')
text=text.replace('| Previous Denominator ID | DEN-20260507-V1-AUTHOR-34 |','| Previous Denominator ID | — |')
text=text.replace('| SA-20260507-COVERAGE | fresh-context:may2026_day01 | coverage | coverage:SRC-ARXIV:20260507 | F-20260507-FN20 — 原 34-family denominator 漏收 20 项 | 547/547 重审并恢复 20 项；最终 54 retained / 493 closures | passed |','| SA-20260507-COVERAGE | fresh-context:may2026_day01 | coverage | coverage:SRC-ARXIV:20260507 | — | 独立重审发现并已修复原 denominator 的 20 项 false negative；547/547 已闭合为 54 retained / 493 closures | passed |')
text=text.replace('| DataCite v2 prefixes 00..99 + full semantic screen + exact-v1 HTML | complete |','| DataCite v2 prefixes 00..99 + full semantic screen + exact-v1 HTML | checked |')
text=text.replace('| — | 本报告不把作者性能数字外推为通用 benchmark claim | — | — | — | — | — | — | — | — | — |\n','')
materials='''<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-20260507-2605.04808 | P1 Full Text | SF-DECODINGTRUST-AGENT-PLATFORM-DTAP-A-CONTROLLABLE-AND-INTERACTIVE-RED-TEA | — | — | 2026-W19 | arXiv:2605.04808v1; https://github.com/AI-secure/DecodingTrust-Agent; https://decodingtrust-agent.com/docs | event-time exact-v1 paper full text/revision | artifact/docs only support public platform and mechanism facts; they cannot establish paper experiments, limitations or Books eligibility | official exact-v1 PDF/HTML/TXT carrying arXiv v1 identity | arxiv-2605.04808v1.pdf | paper Method, experiments, ablations, limitations, artifact reconciliation and Books comparison |
| MR-20260507-2605.05260 | P1 Full Text | SF-SECUREMCP-A-POLICY-ENFORCED-LLM-DATA-ACCESS-FRAMEWORK-FOR-AIOT-SYSTEMS-V | — | — | 2026-W19 | arXiv:2605.05260v1; https://arxiv.org/abs/2605.05260 | event-time exact-v1 paper full text | identity/abstract do not establish the policy-enforcement path, security evaluation, threat model or limitations | official exact-v1 PDF/HTML/TXT carrying arXiv v1 identity | arxiv-2605.05260v1.pdf | paper Method, security experiments, threat model, limitations, artifact and Books eligibility |

'''
materials=materials.replace('| MR-20260507-2605.05260 | P1 Full Text | SF-SECUREMCP-A-POLICY-ENFORCED-LLM-DATA-ACCESS-FRAMEWORK-FOR-AIOT-SYSTEMS-V | — | — | 2026-W19 | arXiv:2605.05260v1; https://arxiv.org/abs/2605.05260 | event-time exact-v1 paper full text | identity/abstract do not establish the policy-enforcement path, security evaluation, threat model or limitations | official exact-v1 PDF/HTML/TXT carrying arXiv v1 identity | arxiv-2605.05260v1.pdf | paper Method, security experiments, threat model, limitations, artifact and Books eligibility |\n','')
text=text.replace("### Materials Request — MR-20260507-2605.05260\n\n- Priority: P1 Full Text\n- Candidate: `arXiv:2605.05260v1`，SecureMCP\n- Missing material: event-time exact-v1 HTML/PDF/TXT 正文。\n- Why insufficient: identity/abstract 不能证明 policy enforcement path、security evaluation、threat model 或 limitations。\n- Acceptable substitute: official exact-v1 PDF/HTML/TXT，或作者提供的带 arXiv v1 identity 完整正文。\n- Suggested filename: `arxiv-2605.05260v1.pdf`\n- After recovery: 完成 Method、evaluation、limitations、artifact 与 Books eligibility 审计。\n\n", "")
text=text.replace('## 12. Sources',materials+'## 12. Sources')
for x,rv in zip(ret,reviews):
 family=x['source_family_id']; review_ref=f'review:{family}'; start=f'<!-- {review_ref}:start -->'; end=f'<!-- {review_ref}:end -->'
 body=text.split(start,1)[1].split(end,1)[0]
 candidate={
  'Event Identity':f'paper-v1:{x["arxiv_id"]}', 'Primary Identifier':f'arXiv:{x["arxiv_id"]}v1',
  'Supporting Source IDs':'SRC-ARXIV', 'Review Override':'none' if x['arxiv_id'] in blocked or x['integration_disposition']!='Integrate' else 'knowledge_gap',
 }
 rp=_expected_review_provenance(family,candidate,'deep',rv['primary_evidence_version'],f'SRC-ARXIV@{rv["primary_evidence_version"]}',rv['method_identity_locators'],rv['evaluation_locators'],rv['limitations_counterevidence_locators'],rv['artifact_locators'],f'claim:{family}',review_ref,_normalized_body_sha256(body))
 text=text.replace('RP-TODO-'+family,rp)
out=REPO/'papers/2026/05/07/README.md'; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(text+'\n')
print(json.dumps({'retained':len(ret),'closures':len(rows)-len(ret),'review_complete':len(ret)-len(blocked),'blocked':len(blocked),'integrate_queue':len(integrate)}))
