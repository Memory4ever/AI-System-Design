#!/usr/bin/env python3
"""Freeze the 2026-05-07 strict denominator and date-local author packet."""
from __future__ import annotations

import csv, hashlib, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
INV=json.loads((ROOT/'screening-ledger-provisional.json').read_text())

# Full 547-row title+abstract semantic pass.  Retention means a durable system
# contract delta, not merely AI topical relevance or ROADMAP mappability.
K={
'2605.04396':('TRAIN-PRETRAINING',(3,2,3),'No Change — Existing Coverage','regularization timing creates a critical training window that changes the reasoning-versus-memorization basin'),
'2605.04410':('PLATFORM-EVALUATION-SYSTEM',(2,2,3),'No Change — Existing Coverage','evaluation artifacts need explicit assumptions, gaming risks, baselines and failure cases'),
'2605.04418':('TRAIN-PRETRAINING',(3,2,3),'Integrate','explicit manifold constraints bound activation scale and update geometry rather than acting as an unexplained stabilization heuristic'),
'2605.04431':('TRAIN-RLHF',(3,3,3),'Integrate','RFT reliability requires observable fault fingerprints plus diagnosis and remediation as a closed training control loop'),
'2605.04446':('PLATFORM-SECURITY',(3,2,3),'Integrate','MoE routing is a remotely exploitable safety surface even when attackers can only influence input tokens'),
'2605.04450':('INFER-GPU-MEMORY',(3,3,3),'Integrate','embedding hot-cache and KV-cache allocation must be co-scheduled as one HBM control problem under tail-latency SLOs'),
'2605.04454':('PLATFORM-EVALUATION-SYSTEM',(3,3,3),'No Change — Existing Coverage','deployment claims require interaction and scaffold evidence rather than model-only scores'),
'2605.04468':('TRAIN-SFT',(3,2,3),'Integrate','SFT can constrain distribution drift through moving trust-region anchors instead of accepting catastrophic forgetting as a downstream surprise'),
'2605.04477':('TRAIN-RLHF',(3,2,3),'Integrate','online preference learning should allocate exploration from historical uncertainty rather than unreliable on-policy estimates alone'),
'2605.04478':('TRAIN-DISTRIBUTED-TRAINING',(3,3,3),'Integrate','collective slow/hang diagnosis needs rank probes, fault fingerprints and remediation ownership inside the training runtime'),
'2605.04495':('AGENT-RAG',(2,2,3),'No Change — Existing Coverage','retrieval confidence must remain distinct from evidence entailment and answer confidence'),
'2605.04496':('AGENT-CONTEXT',(3,2,3),'Integrate','long-context agents need explicit epistemic state and active information acquisition rather than passive context accumulation'),
'2605.05260':('AGENT-MCP',(3,3,3),'No Change — Existing Coverage','MCP data access must be policy-enforced at the effect boundary rather than delegated to model intent'),
'2605.04507':('AGENT-MULTI-AGENT',(2,2,3),'Integrate','negotiation agents can expose compact Bayesian belief state as an auditable intermediate contract'),
'2605.05262':('AGENT-PLANNING',(3,2,3),'Integrate','tool-use rollout selection should optimize marginal information under a budget rather than expand a search tree uniformly'),
'2605.04543':('INFER-SPECULATIVE-DECODING',(3,3,3),'No Change — Existing Coverage','multi-step and multi-draft speculation share one proposal-verification-commit state machine'),
'2605.04563':('INFER-TENSORRT-LLM',(2,2,2),'Integrate','approximate execution needs an explicit bounded-error correction contract rather than an average-accuracy claim'),
'2605.04565':('INFER-SCHEDULING',(3,2,2),'Integrate','large-small model collaboration must jointly price delay, transfer and selection rather than optimize model quality in isolation'),
'2605.04568':('MULTIMODAL-WORLD-MODELS',(3,3,3),'No Change — Existing Coverage','latent imagination is useful only when uncertainty and closed-loop MPC correction remain explicit'),
'2605.04572':('PLATFORM-SECURITY',(3,2,3),'Integrate','fine-tuning safety degradation can be localized to sample-level parameter dynamics and therefore audited during training'),
'2605.04595':('INFER-KV-CACHE',(3,3,3),'No Change — Existing Coverage','KV capacity and queue stability must be analyzed together under arrival and service contracts'),
'2605.04624':('PLATFORM-EVALUATION-SYSTEM',(3,2,3),'Integrate','agent-repair evaluation can become unstable when paired execution traces and evaluator channels disagree'),
'2605.04638':('PLATFORM-EVALUATION-SYSTEM',(2,2,2),'No Change — Existing Coverage','semantic-gradient signals are uncertainty sensors, not calibrated evidence confidence'),
'2605.04665':('PLATFORM-EVALUATION-SYSTEM',(3,2,3),'Integrate','semantically equivalent prompts can trigger output-mode collapse, requiring invariance tests in release evaluation'),
'2605.04678':('MULTIMODAL-EMBODIED-VLA',(3,2,3),'Integrate','latent action supervision changes the representation bridge between pixels, language and controllable action'),
'2605.04698':('PLATFORM-SECURITY',(3,3,3),'Integrate','continuous ingestion turns data poisoning into a persistent supply-chain control problem with delayed effects'),
'2605.04709':('MULTIMODAL-WORLD-MODELS',(3,3,3),'Integrate','visual MPC must calibrate ensembles of imagined rollouts before imagined state can safely drive long-horizon control'),
'2605.04711':('TRAIN-PRETRAINING',(3,2,2),'Integrate','optimizer configuration can be treated as a measured budget-aware control decision rather than a static recipe'),
'2605.04719':('TRAIN-RLHF',(3,2,3),'Integrate','tool-integrated generation needs step-level credit tied to observable effects instead of terminal answer reward alone'),
'2605.04738':('INFER-TENSORRT-LLM',(3,3,2),'No Change — Existing Coverage','low-bit quantization must absorb outliers under a declared error and hardware execution contract'),
'2605.08215':('MULTIMODAL-EMBODIED-VLA',(3,2,3),'Integrate','VLA visual foresight can adapt at test time, but adaptation state becomes part of the control-loop safety identity'),
'2605.04785':('AGENT-TOOL-CALLING',(3,3,3),'No Change — Existing Coverage','tool calls require runtime interception and effect-side safety checks'),
'2605.04808':('PLATFORM-EVALUATION-SYSTEM',(3,2,3),'Integrate','agent red-teaming needs controllable environment state and interactive attack traces rather than static prompts'),
'2605.04811':('AGENT-MEMORY',(3,2,3),'Integrate','multi-agent memory requires tree-structured credit assignment over shared and delegated state changes'),
'2605.04897':('AGENT-MEMORY',(3,3,3),'No Change — Existing Coverage','durable storage is not usable memory without retrieval, admission and update ownership'),
'2605.04913':('TRAIN-RLHF',(3,2,3),'Integrate','local post-training shifts update ownership from end-to-end backpropagation to cheaper layer-local objectives with new consistency costs'),
'2605.04932':('PLATFORM-EVALUATION-SYSTEM',(3,2,3),'Integrate','deployment risk under covariate drift needs a Jacobian-sensitive bound rather than IID benchmark extrapolation'),
'2605.04956':('INFER-TENSORRT-LLM',(2,3,3),'No Change — Existing Coverage','generated GPU kernels need fixed-contract correctness and performance evaluation across architectures'),
'2605.04960':('TRAIN-GRPO',(3,2,3),'Integrate','GRPO updates can align entropy with verified progress instead of treating entropy as an undirected exploration proxy'),
'2605.05274':('AGENT-PLATFORM',(3,3,3),'Integrate','LLM skills require a sealed audit-to-runtime identity so the reviewed artifact is the artifact actually executed'),
'2605.04984':('TRAIN-RLHF',(3,2,3),'Integrate','turn-level agent credit can be inferred without external verifiers by using outcome-potential deltas, subject to identifiability limits'),
'2605.04992':('PLATFORM-SECURITY',(3,2,2),'Integrate','safety alignment restoration after fine-tuning can be modeled as a weight-space repair operation with explicit regression risk'),
'2605.05007':('AGENT-MULTI-AGENT',(3,2,3),'Integrate','multi-agent routing should selectively delegate from task and uncertainty state rather than invoke a fixed team'),
'2605.05025':('PLATFORM-EVALUATION-SYSTEM',(2,2,2),'No Change — Existing Coverage','internal attention divergence is a bounded hallucination sensor and cannot by itself certify truth'),
'2605.05049':('TRAIN-DISTRIBUTED-TRAINING',(3,3,3),'Integrate','large MoE training needs resource-model-driven pipelined hybrid parallelism that co-owns expert placement and communication'),
'2605.05278':('TRAIN-DISTRIBUTED-TRAINING',(3,3,3),'Integrate','finite expert-bank routing exposes communication cost as a first-class MoE training decision'),
'2605.05066':('MODEL-LONG-CONTEXT',(3,2,3),'No Change — Existing Coverage','long-context design cannot simultaneously optimize capacity, generalization and efficient exact access without workload trade-offs'),
'2605.05090':('PLATFORM-EVALUATION-SYSTEM',(3,2,3),'Integrate','model interventions need systematic validation of unexpected side-effects before release'),
'2605.05092':('MULTIMODAL-WORLD-MODELS',(3,2,3),'Integrate','driver-centric world models must preserve traffic-conditioned latent state rather than optimize generic video fidelity'),
'2605.05097':('AGENT-MEMORY',(3,3,3),'No Change — Existing Coverage','continual knowledge requires distinct timescales for weights, retrieval state and episodic memory'),
'2605.05112':('TRAIN-GRPO',(3,2,3),'Integrate','binary-reward RL should control rollout pass rate to keep sampling in an informative regime'),
'2605.05134':('PLATFORM-EVALUATION-SYSTEM',(2,2,2),'No Change — Existing Coverage','black-box trajectory dynamics are a low-cost hallucination detector, not truth evidence'),
'2605.05166':('PLATFORM-EVALUATION-SYSTEM',(2,2,2),'No Change — Existing Coverage','first-token state can support cheap abstention but does not establish calibrated claim confidence'),
'2605.05191':('AGENT-CONTEXT',(3,3,3),'No Change — Existing Coverage','long-horizon search needs elastic context orchestration across active, compressed and recoverable state'),
'2605.05287':('PLATFORM-SECURITY',(3,3,3),'No Change — Existing Coverage','enterprise agent retrieval and tool use require tenant-scoped identity and effect authorization'),
'2605.05379':('PLATFORM-EVALUATION-SYSTEM',(3,3,3),'Integrate','agent evaluation must model authorization-limited evidence rather than assume universal access to ground truth'),
'2605.05400':('AGENT-CONTEXT',(2,2,3),'No Change — Existing Coverage','coding-agent performance depends on deliberate structured context preparation before execution'),
'2605.05413':('AGENT-WORKFLOW',(3,3,3),'Integrate','recurring procedures can move from growing prompts into learned modules while deterministic workflow state remains explicit'),
'2605.05440':('PLATFORM-SECURITY',(3,3,3),'No Change — Existing Coverage','authorization must propagate through delegation, aggregation and time, not attach only to the initiating identity'),
'2605.05467':('INFER-SCHEDULING',(3,3,3),'Integrate','tensor parallelism can become a runtime control surface jointly optimized with PD split and request scheduling'),
'2605.05501':('AGENT-WORKFLOW',(3,3,3),'No Change — Existing Coverage','deterministic policy verifiers must own mandatory ordering and approval gates for agent plans'),
'2605.05509':('PLATFORM-SECURITY',(3,3,3),'Integrate','agentic-browser threat models must include ordinary web attacks and confused-deputy effects, not only prompt injection'),
'2605.05519':('PLATFORM-COST',(3,3,3),'Integrate','datacenter workload control and grid response form one closed-loop runtime coordination problem'),
'2605.05527':('INFER-SCHEDULING',(3,2,3),'Integrate','edge multi-model scheduling should optimize system-wide deadline risk across model, early exit and batch decisions'),
'2605.08234':('INFER-KV-CACHE',(3,3,3),'No Change — Existing Coverage','KV eviction evaluation must decompose evidence recovery, output value and coupled-token projection'),
'2605.05538':('AGENT-RAG',(3,2,3),'No Change — Existing Coverage','agentic retrieval shifts control from a fixed candidate set to iterative search with explicit evidence navigation'),
}

# A second false-positive pass after the high-recall abstract review removes
# papers that merely instantiate an existing mechanism in a single domain or
# offer a local method delta without changing a durable contract.
ACTIVE=set('''2605.04418 2605.04431 2605.04446 2605.04450 2605.04454
2605.04396 2605.04468 2605.04477 2605.04478 2605.04496 2605.05260
2605.05262 2605.04543 2605.04563 2605.04568 2605.04572 2605.04595
2605.04624 2605.04665 2605.04678 2605.04698 2605.04709 2605.04711
2605.04719 2605.08215 2605.04785 2605.04808 2605.04811 2605.04897
2605.04913 2605.04932 2605.04956 2605.04960 2605.05274 2605.04984
2605.04992 2605.05007 2605.05049 2605.05066 2605.05090 2605.05092
2605.05097 2605.05112 2605.05191 2605.05287 2605.05379 2605.05413
2605.05440 2605.05467 2605.05501 2605.05509 2605.05519 2605.05527
2605.08234'''.split())
BLOCKED={'2605.04808'}

# Current-content comparison found that later material already carries these
# contracts.  Keep the families in the denominator as evidence, but do not
# enqueue duplicate prose.
for _aid in ('2605.05509','2605.05519'):
 _node,_score,_disp,_delta=K[_aid]
 K[_aid]=(_node,_score,'No Change — Existing Coverage',_delta)

def sents(a): return [s.strip() for s in re.split(r'(?<=[.!?])\s+',re.sub(r'\s+',' ',a or '').strip()) if s.strip()]
def clip(s,n=32):
 w=s.split(); return ' '.join(w[:n])+('…' if len(w)>n else '')
def closure(x):
 ss=sents(x.get('abstract')); title=re.sub(r'\s+',' ',x['title']).strip()
 m=next((s for s in ss if re.search(r'\b(propose|introduce|present|develop|construct|formulate|evaluate|study|analy[sz]e|investigate|design|derive)\b',s,re.I)),ss[0] if ss else '摘要没有可识别方法句')
 r=next((s for s in ss if s!=m and re.search(r'\b(result|experiment|evaluation|achiev|outperform|improv|show|demonstrate|find)\b',s,re.I)),'摘要未给出跨 workload 结果')
 text=(title+' '+' '.join(ss)).lower()
 if re.search(r'medical|clinical|patient|cancer|protein|molecule|drug|gene|weather|satellite|agricultur|finance',text): b='结论绑定领域数据、标签与任务指标，不改变通用 AI System 的状态、数据或控制 owner'
 elif re.search(r'benchmark|dataset|challenge|leaderboard',text): b='主要建立任务集或局部测量，未重定义跨系统 evaluation identity、污染控制或 release contract'
 elif re.search(r'survey|position paper|perspective|case study|meta-analysis',text): b='证据是综述、立场或个案，没有提供可执行且可迁移的系统控制机制'
 elif re.search(r'agent|tool|memory|rag|retriev',text): b='改进停留在该 agent/RAG 任务，未改变 durable state、effect ownership、admission/rollback 或跨运行评价契约'
 elif re.search(r'quantization|pruning|routing|cache|kernel|distributed|parallel|serving|training',text): b='只证明局部算法/实现增量，未改变跨层执行计划、状态 ownership、SLO/evaluation contract 或共存边界'
 else: b='贡献停留在论文自身问题与实验对象，没有形成可迁移的 AI System owner、长期 contract 或 Books 反例'
 return f'问题/机制：{title}；方法为“{clip(m)}”；结果线索为“{clip(r)}”。排除边界：{b}。'

rows=[]
for o in INV['identities']:
 x=dict(o); aid=x['arxiv_id']
 if aid in ACTIVE:
  node,score,disp,delta=K[aid]; sf='SF-'+re.sub(r'[^A-Z0-9]+','-',x['title'].upper()).strip('-')[:72]
  x.update(source_family_id=sf,screening_status='retained',screening_reason=delta,owner_node=node,score_v2={'design_delta':score[0],'system_reach':score[1],'durability':score[2],'total':sum(score)},review_status='blocked' if aid in BLOCKED else 'deep_complete' if sum(score)>=7 or disp=='Integrate' else 'standard_complete',access_status='blocked' if aid in BLOCKED else 'verified',integration_disposition='Blocked / Unverified' if aid in BLOCKED else disp)
 else:
  x.update(screening_status='pre_denominator_closure',screening_reason=closure(x),review_status='identity_date_closed',access_status='verified',integration_disposition='Rejected — Below Candidate Denominator')
 rows.append(x)

ret=[x for x in rows if x['screening_status']=='retained']; clo=[x for x in rows if x['screening_status']!='retained']
out={'schema':'daily-screening-ledger-v2.1','report_date':'2026-05-07','window':INV['window'],'utc_window':INV['utc_window'],'raw_snapshot_records':INV['raw_snapshot_records'],'registered_window_identities':len(rows),'screened_identities':len(rows),'candidate_denominator':len(ret),'pre_denominator_closures':len(clo),'identities':rows}
(ROOT/'screening-ledger-final.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
cols=['arxiv_id','title','source_kind','screening_status','source_family_id','screening_reason','owner_node','review_status','access_status','integration_disposition']
with (ROOT/'screening-ledger-final.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
print(json.dumps({'registered':len(rows),'retained':len(ret),'closures':len(clo),'integrate':sum(x['integration_disposition']=='Integrate' for x in ret)},ensure_ascii=False))
