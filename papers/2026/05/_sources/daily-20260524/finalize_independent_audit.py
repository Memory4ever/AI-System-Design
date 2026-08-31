#!/usr/bin/env python3
"""Materialize the non-author 2026-05-24 pre-write audit.

Only date-local research artifacts and the canonical Daily are written.  The
current Books are read for owner/adjacent comparison but never modified.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

DATE = "2026-05-24"
NOW = "2026-09-01T11:30:00+08:00"
SOURCE = json.loads((HERE / "screening-ledger-final.json").read_text())
AUTHOR = json.loads((HERE / "candidate-config-author.json").read_text())["candidates"]

def sf(aid: str) -> str:
    return "SF-2026-ARXIV-" + aid.replace(".", "-")

# owner, score, disposition, exact-v1 Method, Evaluation, non-proof locator.
# The first 21 rows are author retentions reconfirmed after exact-v1 review.
C = {
"2606.02606":("PLATFORM-PRODUCTION",8,"Integrate","§III Method; III-A–III-C adaptive initialization and scheduled regularization","§IV Evaluation; IV-A–IV-E","§VI Discussion and Limitation; VI-C–VI-D"),
"2605.24326":("TRAIN-DISTRIBUTED-TRAINING",8,"No Change — Existing Coverage","§3–§6 placement, scheduling, network and ScaleAcross Explorer","§6.3 Evaluation Results; Appendix A testbed/simulation settings","§7 Lessons Learned; §8 Conclusion; cross-building testbed/simulator scope"),
"2605.24391":("INFER-TENSORRT-LLM",9,"Integrate","§IV MX-SAFE format; §V accelerator","§VI Experimental Results","§VII Conclusion; tested MXSF hardware/model boundary"),
"2605.24421":("PLATFORM-SECURITY",9,"Integrate","§2 Threat Model; §3 taxonomy; §4 pipeline/defenses","§5 Experiments","§6.4 Limitations"),
"2605.24461":("PLATFORM-GPU-SCHEDULER",9,"Integrate","§3 power hierarchy; §§4–6 provisioning, validation and active operation","§4.2 empirical data; §§5–7 deployment/runtime measurements","§8 Research Wishlist; §10 Conclusion; single 150MW/83K-GB200 site boundary"),
"2605.24468":("AGENT-MEMORY",8,"No Change — Existing Coverage","§2.2–§2.3 State-Adaptive Memory and optimization","§3 Experiments; §4 Discussions","Appendix A Limitations and Broader Impact"),
"2605.24517":("MULTIMODAL-WORLD-MODELS",8,"No Change — Existing Coverage","§3 Method; ECHO hybrid policy/observation objective","§4 Experimental Setup; §5 Results","§7 Conclusion; terminal-environment and training-only auxiliary-loss boundary"),
"2605.24579":("AGENT-MEMORY",8,"Integrate","§3 four-condition diagnostic; §4 expected predictive compression","§5 Experimental Setup; §6 Results; §7 Analysis","§7 Analysis and §8 Conclusion; tested readers, memories and two benchmarks"),
"2605.24598":("AGENT-MULTI-AGENT",9,"Integrate","§5 Hera step-level device-cloud coordinator","§6 Experiment; §6.2–§6.4","Appendix E Limitations and Future Work"),
"2605.24619":("AGENT-PLATFORM",8,"No Change — Existing Coverage","§4 Design; §5 Implementation","§6 Evaluation","§7.2 Limitations"),
"2605.24657":("AGENT-CONTEXT",8,"No Change — Existing Coverage","§2 Method; memory taxonomy and consolidation/compaction pipelines","§3 Evaluation","§4 Discussion — Limitations"),
"2605.24659":("PLATFORM-SECURITY",8,"No Change — Existing Coverage","§3 Threat Model; §4 feedback-guided payload optimization","§5 Experimental Setup; §6 Evaluation","Limitations after §7 Conclusion; tested agents/channels only"),
"2605.24660":("AGENT-TOOL-CALLING",8,"Integrate","§3 Bits-over-Random and MDP exposure policy","§4 Empirical Evaluation","§5.3 Limitations"),
"2605.24733":("AGENT-REFLECTION",8,"No Change — Existing Coverage","§3 formulation; §4 hybrid checker; §5 typed process reward","§6 checker evaluation; §7 GRPO training","Limitations after §8 Conclusion"),
"2605.24737":("PLATFORM-MONITORING",9,"No Change — Existing Coverage","§3 governance from metrics; §4 govllm architecture; §5 contributions","§6 Preliminary experiments","§6.3 and §7.4 Limitations"),
"2605.24756":("PLATFORM-EVALUATION-SYSTEM",9,"Integrate","§4 proper trajectory scores under complete and censored observation","§5 metrics; §6 Experiments","§7 Conclusion and Limitations"),
"2605.24775":("AGENT-MULTI-AGENT",8,"No Change — Existing Coverage","§III identity; §§IV–VIII protocol, scoring, orchestration and persistence","reported operational examples and convergence traces in §§VI–VIII","§I/§II claim scope; pattern/prototype rather than general production proof"),
"2605.24785":("AGENT-PLATFORM",8,"No Change — Existing Coverage","§3 cost decomposition and online skill-distillation lifecycle","§5 Experimental Setup and reported results","§7 Limitations and Conclusion"),
"2605.24786":("INFER-KV-CACHE",8,"No Change — Existing Coverage","§3 confidence-aware mixed-precision cache manager","§§4–6 setup, results and ablations","§7 failure modes; §8 Limitations and conclusion"),
"2605.24793":("INFER-SPECULATIVE-DECODING",9,"Integrate","§3 utility view, collaborative arbitration and RL training","§4 Experiments; §§4.2–4.4","§5 Conclusion and Appendix A tested-model/benchmark boundary"),
"2605.28872":("PLATFORM-GPU-SCHEDULER",8,"Integrate","§IV measurement; §§V–VI reclaim-aware membership/lease protocol","§VII Evaluation and campus deployment measurements","§VIII Limitations and Conclusion; voluntary campus-network and failure-domain boundary"),

# False negatives recovered by independent 289/289 title+abstract replay.
"2606.00089":("MULTIMODAL-EMBODIED-VLA",8,"Integrate","§§3–5 prediction-control interface, physical conditions and rejection semantics","§6 Experimental Protocol","§7.1 Limitations"),
"2605.24420":("PLATFORM-SECURITY",8,"Integrate","§3 Methodology; §5 theory; §6 mitigation","§4 Experiments; §4.3 membership inference","Appendix A.3 theoretical limitations; tested normalization/model/data boundary"),
"2605.24425":("MODEL-TRANSFORMER-LAYER",8,"Integrate","§§3–5 optimizer view, optimizer-inspired block and momentum stream","§4.2; §§5–6; Appendix D Experimental Details","§7 Conclusion; architecture/scale/recipe boundary"),
"2605.24426":("TRAIN-RLHF",9,"Integrate","§3 verifier-grounded diagnosis, interface evolution and advantage reweighting","§4 Experiments; Appendix C controlled protocol","§5 Conclusion and Limitations"),
"2605.24547":("TRAIN-RLHF",8,"Integrate","§2 problem formulation; §3 bilevel natural-language actor-critic","§4 Experiments; Appendix A.5 efficiency","§5 Conclusion; tested task/model and higher-order-gradient boundary"),
"2605.24558":("TRAIN-DATA",7,"No Change — Existing Coverage","§§2–3 measurement pipeline as observation/inference component","§4 empirical audit; §5 alternative views","§6 Call to Action; position/audit does not prove a universal pipeline"),
"2605.24583":("PLATFORM-EVALUATION-SYSTEM",8,"Integrate","§§2–4 separability metric and three confound-control tests","§§5–6 calibration and current-alignment audit","§7 Scope; §8 open problem and failed spectral-gap claim"),
"2605.24614":("PLATFORM-EVALUATION-SYSTEM",8,"No Change — Existing Coverage","§3 Unlearning Depth Score and activation patching","§4 Meta-Evaluation; §5 case studies","Limitations after §7 Conclusion"),
"2605.24661":("PLATFORM-EVALUATION-SYSTEM",7,"No Change — Existing Coverage","§4 multi-dimensional behavioral framework and aggregation","§5 Results","§6.2 Limitations"),
"2605.24662":("PLATFORM-EVALUATION-SYSTEM",8,"No Change — Existing Coverage","§II–§IV OpenTwin closed-loop data assimilation, calibration and policy-validation workflow","§A Experimental Setup; §B Experimental Results","§V Limitations; real-network drift and Open-RAN testbed boundary"),
"2605.24667":("TRAIN-PRETRAINING",8,"Integrate","§§3–4 mean/median CE interventions and top-K self-distillation","§3.2; §§4.2–4.4; Appendix C protocol","§5 Discussion — Limitations"),
"2605.24683":("PLATFORM-MONITORING",8,"Integrate","§III deterministic L2 topology, identity loop and HIL protocol","§IV Implementation and Results","§V Limitations and Constraints"),
"2605.24697":("MULTIMODAL-GENERATIVE-PARADIGMS",9,"Integrate","§3 future-stability labels, learned commitment and TraceLock deployment","§4 Experiments; §§4.2–4.4","§5 Conclusion; frozen generator/tested diffusion backbones boundary"),
"2605.24709":("TRAIN-RLHF",8,"Integrate","§3 Methodology; streaming partially-observed recurrent policy with exact RTRL","§4 Experiments","§6 Discussion and Limitations"),
"2605.24727":("PLATFORM-EVALUATION-SYSTEM",8,"Integrate","§3 four explanation conditions; §4 quadrilemma theorem/implications","formal construction and implications in §4","§5 Conclusion, limitations and future work"),
"2605.24728":("MULTIMODAL-EMBODIED-VLA",8,"Structural Candidate","§4 operability state/graph, spatial transactions and effect diffs; §5 agency gates","§6 repair stress test; §7 qualitative result","§1.2 Scope of Claims; prototype/trajectory does not establish general runtime validity"),
"2605.24743":("TRAIN-DATA",8,"Integrate","§3 bilevel synthetic-trajectory weighting; §4 theory","§§5–6 experiments and learned-weight analysis","§7 Conclusion; three tasks and synthetic-generator boundary"),
"2605.24749":("TRAIN-RLHF",8,"Integrate","§§3–5 reward-weighted feature recovery and tilted-policy value gap","theory and deployment-temperature analysis in §§4–5","§6 Conclusion and Discussion; single-index/theoretical-assumption boundary"),
"2605.24770":("TRAIN-PRETRAINING",8,"Integrate","§§2–5 Muon geometry and recipe interaction","§§3–6; Appendices C–E","§7 Conclusions and limitations"),
}

AUTHOR_FP = {"2605.27444", "2605.27445"}
FN = set(C) - (set(AUTHOR) - AUTHOR_FP)
DEEP = {"2605.24461":"DA-POWER-LIFECYCLE", "2605.24426":"DA-COEVOLUTION-CONTROL", "2605.24697":"DA-TOKEN-COMMIT"}
INTEGRATE = {aid for aid, v in C.items() if v[2] == "Integrate"}
PDF = {"2605.24517", "2605.24737", "2605.24785", "2605.24662", "2605.24709"}

def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "").strip()) if s.strip()]

def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    for s in ss:
        if re.search(r"\b(propose|introduce|present|develop|design|formalize|prove|show|identify|study|audit)\b", s, re.I):
            return s
    return ss[0] if ss else row["title"]

def closure(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    concrete = " ".join(ss[:2]) or row["title"]
    cats = ", ".join(row.get("categories", []))
    return (f"`{row['title']}`（{cats}）：{concrete} 独立重放后，该 family 仍只改变其领域任务、局部模型/表示、"
            "单一 benchmark 或产品封装，没有改变长期 AI-System 的 state/data/control owner、evaluation/release contract 或 fallback。"
            "若后续公开跨 workload 的系统接口、可复算 artifact 或与 Books 现有结论冲突的证据，重开该 family。")

by = {r["arxiv_id"]: dict(r) for r in SOURCE["identities"]}
assert len(by) == 289 and set(C) <= set(by)
rows=[]
for original in SOURCE["identities"]:
    row=dict(original); aid=row["arxiv_id"]
    if aid in C:
        owner,total,disp,m,e,l=C[aid]
        design=3 if total>=8 else 2; reach=3 if total==9 else 2; durability=total-design-reach
        row.update(source_family_id=sf(aid), screening_status="retained", screening_reason=mechanism(row),
                   owner_node=owner, score_v2={"design_delta":design,"system_reach":reach,"durability":durability,"total":total},
                   review_status="deep_complete", access_status="accessible", integration_disposition=disp,
                   method_locator=m,evaluation_locator=e,limitations_locator=l,
                   independent_audit="false_negative_recovered" if aid in FN else "author_retention_reconfirmed")
    else:
        row.update(screening_status="pre_denominator_closure",screening_reason=closure(row),review_status="identity_date_closed",
                   access_status="accessible",integration_disposition="Rejected — Below Candidate Denominator",
                   independent_audit="author_false_positive_closed" if aid in AUTHOR_FP else "closure_reconfirmed")
    rows.append(row)
retained=[r for r in rows if r["screening_status"]=="retained"]
closures=[r for r in rows if r["screening_status"]!="retained"]
assert (len(retained),len(closures),len(FN))==(40,249,19)

ledger={"schema":"daily-screening-ledger-v2.1","report_date":DATE,"window":SOURCE["window"],"utc_window":SOURCE["utc_window"],
        "raw_snapshot_records":SOURCE["raw_snapshot_records"],"registered_window_identities":289,"screened_identities":289,
        "candidate_denominator":40,"pre_denominator_closures":249,
        "independent_reconciliation":{"author_denominator":23,"false_positives":sorted(AUTHOR_FP),"false_negatives":sorted(FN),"final_denominator":40},
        "identities":rows}
for name in ["screening-ledger-independent-final.json","screening-ledger-final.json"]:
    (HERE/name).write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n")
with (HERE/"screening-ledger-independent-final.tsv").open("w",newline="") as f:
    w=csv.writer(f,delimiter="\t"); w.writerow(["arxiv_id","title","status","reason","owner","score","disposition"])
    for r in rows:w.writerow([r["arxiv_id"],r["title"],r["screening_status"],r["screening_reason"],r.get("owner_node",""),r.get("score_v2",{}).get("total",""),r["integration_disposition"]])

roadmap=(ROOT/"ROADMAP.md").read_text()
paths={m.group(1):m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`",roadmap)}
gaps={
"2606.02606":"现有 production/registry 已绑定 adapter 与 base revision，但没有定义 base service 演进后 adapter initialization、service-readiness recovery 与 rollout promotion 的同一迁移契约。",
"2605.24391":"现有执行计划覆盖 bit-exact format，却未表达同一 microscaling block 在 training/direct-cast inference 间按 exponent/mantissa mode 切换的格式与硬件共同身份。",
"2605.24421":"现有 prompt-injection 边界没有把 attacker-controlled log field 明确视为安全分析链路的 untrusted instruction substrate。",
"2605.24461":"现有 scheduler 讨论 power-aware admission，但未贯通 design provisioning、rack validation、operational cap 与 runtime power swing 的责任交接。",
"2605.24579":"现有 Memory 章有 write/read 分离，却没有以 TFC/OE/CSM/RM 四个干预条件区分 reader ceiling、write loss 与 retrieval loss。",
"2605.24598":"现有多 Agent 协调未覆盖 device/cloud step-level routing 在任务历史、成功概率、网络开销与 cost budget 下的可学习控制状态。",
"2605.24660":"现有 tool shortlist 没有用 chance-corrected information gain 把 candidate-set size 与 random baseline 从 tool exposure reward 中扣除。",
"2605.24756":"现有 proper scoring 主要针对 outcome/confidence；缺少带 early termination/censoring 的整条 agent trajectory 的严格 proper score。",
"2605.24793":"现有 speculation 以 target exactness 为 commit contract；缺少 draft 可能优于 target 时由 utility-aware arbitrator 拥有非 exact commit 的 alternative branch。",
"2605.28872":"现有 reclaim 以 scheduler-owned GPU 为前提；缺少 voluntary host、membership lease、network reachability 与 reclaim notice 共同决定可用容量的协议。",
"2606.00089":"现有 physical safety gate 尚未明确分离 action-conditioned transition violation 与 merely off-log behavior，混合 max score 会丢失 rejection semantics。",
"2605.24420":"现有 privacy 章没有把 BatchNorm cross-sample statistics 作为 memorization 与 membership inference 的训练态共享通道。",
"2605.24425":"现有 Transformer Layer 把 residual stream 当 activation carrier，未表达跨层 momentum state 如何改变深度方向更新以及与 preconditioning 分工。",
"2605.24426":"现有 RLHF 将 environment/interface 多视作固定 rollout 条件；缺少 verifier diagnosis 驱动 learning interface 与 policy 同步演进的双 owner 闭环。",
"2605.24547":"现有 textual feedback 是静态 rubric/critic artifact；缺少以 policy return 为上层目标反向学习 feedback generator 的 bilevel control loop。",
"2605.24583":"现有 alignment evaluation 未把 prompt/template confound、mean-direction shift、effective-rank proxy 与 causal ablation 组织成可反驳的 activation audit。",
"2605.24667":"现有 pretraining 以 mean CE 为主，没有记录 heavy-tail token loss 下 median CE/mean CE 与 downstream quality 的 concordance regime。",
"2605.24683":"现有 monitoring 假设 topology/asset identity 可得；缺少 fragmented admin domain 下 deterministic L2 ground truth、integrity loop 与 HIL admission。",
"2605.24697":"现有 diffusion commit 比较 confidence/block schedule，未包含从 future stability trace 学习 token-local commitment policy 与动态 threshold 的分支。",
"2605.24709":"现有 RL loop 多按完整 trajectory 更新；缺少 partial observation 下 recurrent hidden/eligibility state 的 per-step exact online update ownership。",
"2605.24727":"现有 explainability/evidence 章节未显式给出 fidelity、completeness、human comprehensibility 与 universal applicability 不可同时保证的 claim boundary。",
"2605.24743":"现有 synthetic-data admission 未表达由 held-out real trajectory loss 反向拥有每条 multi-turn synthetic trajectory weight 的 bilevel选择。",
"2605.24749":"现有 reward model 评价未把 training distribution 的 prediction error 与 reward-tilted deployment distribution 的 policy value gap分开。",
"2605.24770":"现有 Muon 机制讨论 update geometry，但未把 augmentation/mixing/smoothing recipe 与 gradient spectrum 共同纳入 optimizer recipe identity。",
}
covered={
"TRAIN-DISTRIBUTED-TRAINING":"现有章节已覆盖 topology-aware placement、collective/parallelism co-design、异构网络 profile、simulation 与 fallback；ScaleAcross 属于同一机制的跨楼宇实例。",
"AGENT-MEMORY":"现有章节已经由 raw immutable trajectory、derived cue、write/read policy、provenance 和 rollback 构成同一 memory lifecycle；SAM 未改变该 owner。",
"MULTIMODAL-WORLD-MODELS":"现有章节已明确 training-only observation/world-token auxiliary supervision 不等于 runtime world state；ECHO 是该边界内案例。",
"AGENT-PLATFORM":"现有章节已把 LLM proposal 与 deterministic/formal verifier 的 authority 分离；IC3Syn 未改变 commit owner。",
"AGENT-CONTEXT":"现有 Context/Memory 已比较 compaction 与 durable learned state，并绑定 base/model revision；该 consolidation 实验未改变 owner。",
"PLATFORM-SECURITY":"现有章节已覆盖 indirect injection、adaptive adversary、tool/output boundary 与 defense-in-depth；IterInject 是攻击搜索增强，不是新的生产防御契约。",
"AGENT-REFLECTION":"现有章节已经以 evidence gap、typed verification failure 与 selective rerun 组织 reflection；StepGap 是 NLI/LLM 实现实例。",
"PLATFORM-MONITORING":"现有 monitoring 已覆盖 policy-bound sensor、versioned metric、continuous compliance 与 unknown propagation；govllm 未改变 owner。",
"AGENT-MULTI-AGENT":"现有章节已覆盖 verifiable identity、delegation、convergence feedback、append-only state 与 branch/merge；PRIMA 是同构 pattern bundle。",
"AGENT-PLATFORM-SKILL":"现有 Agent Platform 已拥有 skill distillation、promotion、drift、rollback 与 lifecycle evidence；PANDO 的 web-agent实验不改变该 contract。",
"INFER-KV-CACHE":"现有 KV 章已拥有 confidence-aware mixed precision、budget/eviction、estimator drift 和 FullKV fallback；CONF-KV 属已覆盖分支。",
"TRAIN-DATA":"现有 Data 章已把 observation/measurement pipeline、schema/provenance 与 transformation version 纳入 dataset identity；position paper 未给出新的可验证接口。",
"PLATFORM-EVALUATION-SYSTEM":"现有 Evaluation 已覆盖 unlearning counterfactual/activation audit、多维 score、simulator feedback loop 与 release gate；对应 family 是已覆盖受限实例。",
}

comparisons=[]; queue=[]; packet=[]
for r in retained:
    aid=r["arxiv_id"]; owner=r["owner_node"]; path=paths[owner]; target=ROOT/path; body=target.read_text()
    siblings=sorted(p for p in target.parent.glob("*.md") if re.match(r"\d+-",p.name)); idx=siblings.index(target)
    adj=[str(p.relative_to(ROOT)) for p in siblings[max(0,idx-1):idx]+siblings[idx+1:idx+2]]
    disp=r["integration_disposition"]
    key="AGENT-PLATFORM-SKILL" if aid=="2605.24785" else owner
    existing=gaps.get(aid) if disp=="Integrate" else covered.get(key,"当前 owner 与相邻章节已覆盖同一长期 mechanism、identity、trade-off 与 fallback；该 exact-v1 仅提供受限实例。")
    delta=mechanism(r)
    comparisons.append({"arxiv_id":aid,"source_family_id":r["source_family_id"],"owner_node":owner,"owner_path":path,"owner_sha256":hashlib.sha256(body.encode()).hexdigest(),"adjacent_paths":adj,"adjacent_sha256":{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in adj},"existing_proposition":existing,"new_evidence_delta":delta,"decision":disp,"review_scope":"current owner full body + immediate adjacent; Review notes do not count as semantic coverage"})
    route=(f"https://arxiv.org/pdf/{aid}v1" if aid in PDF else f"https://arxiv.org/html/{aid}v1")
    packet.append({"source_family_id":r["source_family_id"],"arxiv_id":aid,"primary_evidence_version":f"arXiv:{aid}v1","retrieval_route":route,"retrieved_at":NOW,"method_locator":r["method_locator"],"evaluation_locator":r["evaluation_locator"],"limitations_locator":r["limitations_locator"],"claim_boundary":f"{r['title']} only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.","completion_result":"complete"})
    if disp=="Integrate":
        queue.append({"report_date":DATE,"arxiv_id":aid,"source_family_id":r["source_family_id"],"stable_node_id":owner,"owner_path":path,"adjacent_paths":adj,"evidence_delta":delta,"missing_current_proposition":existing,"status":"awaiting_root_serial_writeback","writeback_requirement":"canonical mechanism spine before exact H2 Review notes; preserve old condition, changed constraint, state/control owner, gain/cost, failure, fallback/coexistence and exact-v1 non-proof boundary"})

for name,obj in [("exact-v1-review-packet.json",packet),("exact-v1-independent-review-packet.json",packet),("books-current-content-comparison.json",comparisons),("books-current-content-comparison-independent.json",comparisons)]:
    (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n")
(HERE/"BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema":"books-writeback-queue-v1","report_date":DATE,"status":"awaiting_root_serial_writeback_and_independent_post_write","items":queue},ensure_ascii=False,indent=2)+"\n")
(HERE/"materials-request.json").write_text(json.dumps({"schema":"materials-request-v1","report_date":DATE,"status":"none","requests":[]},ensure_ascii=False,indent=2)+"\n")
(HERE/"semantic-independent-audit.json").write_text(json.dumps({"schema":"semantic-independent-audit-v1","report_date":DATE,"auditor":"fresh-context:may2026-day03-non-author","author_independent":True,"cross_model_review":"skipped — non-interactive delegated context","status":"passed_prewrite_pending_root_serial_writeback","scope":{"registered_replayed":289,"denominator_reviewed":40,"exact_v1_reviewed":40,"books_compared":40},"findings":{"false_positives":sorted(AUTHOR_FP),"false_negatives":sorted(FN),"ordinary_pending":0,"blocked":[]},"resolution":{"author_denominator":23,"final_denominator":40,"closures":249,"author_queue":20,"final_integrate_queue":len(queue),"structural_candidates":["2605.24728"]}},ensure_ascii=False,indent=2)+"\n")

ledger_sha=hashlib.sha256((HERE/"screening-ledger-final.json").read_bytes()).hexdigest(); comp={x["arxiv_id"]:x for x in comparisons}
def cref(p):
    m=re.match(r"(\d+)-",Path(p).name); return f"{p}#chapter-{int(m.group(1))}" if m else p
def ev(r,k):
    route=(f"https://arxiv.org/pdf/{r['arxiv_id']}v1" if r['arxiv_id'] in PDF else f"https://arxiv.org/html/{r['arxiv_id']}v1")
    return f"{route} — {r[k]}"

L=["# Daily Research — 2026-05-24","","**Research Date:** 2026-05-24","","**Timezone:** Asia/Shanghai","","**Strict Window:** 2026-05-23 09:00:00 ～ 2026-05-24 09:00:00（北京时间，左闭右开）","","**Contract:** V2.1 Full Replay；technical claims bind official arXiv exact-v1 HTML/PDF。","","**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。非作者 pre-write 审计已通过，等待 root 串行写回与不同 reviewer post-write audit。","","## Executive Summary","",f"独立重放 289/289 个窗口身份：author denominator 23，经 2 个 false positive 与 19 个 false negative reconciliation 后冻结为 40；pre-denominator closures=249，exact-v1=40/40，blocked=0，ordinary pending=0。current Books owner+adjacent challenge 将 author queue 20 重判为最终 Integrate queue {len(queue)}，另有 1 个 Structural Candidate；共享 Books 未修改。","","## 1. Coverage","","<!-- validator:report-metadata-v2 -->","| Field | Value |","| --- | --- |","| Contract Version | V2.1 |","| Score Schema | V2 |","| Report Type | Daily |","| Window Start | 2026-05-24 |","| Window End | 2026-05-24 |","| Registry Version | 2026-08-25 |","| Coverage Mode | Full Replay |","| Baseline Report | — |","| Changed Source IDs | — |","| Previous Denominator ID | — |","| Denominator ID | DEN-20260524-V2-INDEPENDENT |",f"| Denominator Frozen At | {NOW} |","| Completion Status | In Progress |","| Coverage Gate | Closed |","| Evidence Gate | Passed |","| Books Gate | Open |","","### Source Coverage Receipt","","<!-- validator:source-coverage-v2 -->","| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",f"| SRC-ARXIV | 2026-05-23T09:00:00+08:00 | 2026-05-24T09:00:00+08:00 | {NOW} | DataCite v2 00..99 + independent 289/289 title+abstract replay + official exact-v1 HTML/PDF | checked | 289 | {';'.join(r['source_family_id'] for r in retained)} | pages=300;final_cursor=end;raw={SOURCE['raw_snapshot_records']};registered=289;screened=289;retained=40;closure=249 | 2026-05-24T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | — |","","### Coverage Limitations","","<!-- coverage:SRC-ARXIV:20260524:start -->289/289 identity 已由非作者独立逐项重放；19 个 false negative 恢复，2 个领域/通用 RAG false positive 降回 family-specific closure。first-public、v1、revision、owner day 与重复 family 已对账；无 ordinary pending 或 exact-version blocker。<!-- coverage:SRC-ARXIV:20260524:end -->","","## 2. Candidate Ledger","","<!-- validator:candidate-ledger-v2.1 -->","| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in retained:
    s=r["score_v2"]; disp=r["integration_disposition"]
    stable = "—" if disp == "Structural Candidate" else r["owner_node"]
    L.append(f"| {r['source_family_id']} | arXiv:{r['arxiv_id']}v1 | paper-v1:{r['arxiv_id']} | 2026-W21 | 2026-05-23 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | {'knowledge_gap' if disp in ('Integrate','Structural Candidate') else 'none'} | review:{r['source_family_id']} | self | — | new_in_window | {stable} | {disp} | books-review:{r['source_family_id']} | no |")
L += ["","## 3. Review Completion Receipt","","<!-- validator:review-completion-v1 -->","| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in retained:
    L.append(f"| {r['source_family_id']} | RP-TODO-{r['source_family_id']} | deep | arXiv:{r['arxiv_id']}v1 | SRC-ARXIV@arXiv:{r['arxiv_id']}v1 | {ev(r,'method_locator')} | {ev(r,'evaluation_locator')} | {ev(r,'limitations_locator')} | Not Disclosed — no separate immutable artifact required for this review | claim:{r['source_family_id']} | complete |")
L += ["","### Source Reviews",""]
for r in retained:
    p=next(x for x in packet if x["arxiv_id"]==r["arxiv_id"]); s=r["source_family_id"]
    L += [f"<!-- review:{s}:start -->",f"#### {r['title']}","",f"**问题与机制。** {r['screening_reason']} owner=`{r['owner_node']}`；independent reconciliation=`{r['independent_audit']}`。","",f"**Exact-v1。** Method=`{r['method_locator']}`；Evaluation=`{r['evaluation_locator']}`；Limitations/Counterevidence=`{r['limitations_locator']}`。","",f"<!-- claim:{s}:start -->{p['claim_boundary']}<!-- claim:{s}:end -->","",f"Books Decision=`{r['integration_disposition']}`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。",f"<!-- review:{s}:end -->",""]
L += ["## 4. Benchmark Contracts","","<!-- validator:benchmark-contract-v1 -->","| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","## 5. Deep Analysis Selection","","<!-- validator:deep-analysis-selection-v1 -->","| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |","| --- | --- | --- | --- | --- | --- | --- |"]
for r in retained:
    aid=r["arxiv_id"]; selected=aid in DEEP; unit=DEEP.get(aid,"—"); disp=r["integration_disposition"]
    eligibility=["score_7_9"]
    if disp in ("Integrate","Structural Candidate"): eligibility.append("forced_review")
    if disp=="Integrate": eligibility.append("potential_books_delta")
    if disp=="Structural Candidate": eligibility.append("potential_structural_gap")
    L.append(f"| {r['source_family_id']} | {';'.join(eligibility)} | {'selected' if selected else 'not_selected'} | {unit} | — | {'跨层改变 power、training control 或 token commit ownership' if selected else 'exact-v1 已完成；未选只受三项叙事上限约束'} | {'analysis:'+unit if selected else 'analysis-decision:'+r['source_family_id']} |")
deeptext={"2605.24461":"旧 scheduler 在 facility power 被视为静态容量时只需排 GPU；100MW 级 cluster 的 rack variance、cooling demand 与 power swing 让 provisioning、validation 和 runtime cap 成为连续状态机。收益是提高可用功率与设备利用率，代价是 telemetry/model drift 和 correlated thermal failure；单站测量不能外推所有 datacenter，失配时回退保守 cap。","2605.24426":"固定 environment/interface 在任务分布稳定时可简化 RL；当 agent failure 暴露 observation、tool schema 或 feedback interface 的系统缺口，只有改 policy 会反复学习坏接口。SEAL 把 verifier diagnosis 同时路由到 interface evolution 与 advantage reweighting，收益是闭合 agent/environment feedback，代价是双边漂移和 credit ambiguity；验证失败时冻结 interface 并回到固定环境。","2605.24697":"固定 block 或 confidence threshold 在 diffusion trajectory 稳定时可并行 commit；不同 token 的 future stability 不同后，commit controller 必须观察 trace-local evidence。TraceLock 学习 token-local policy，提高并行度但引入 selector drift、错误早提交与回滚成本；只证明所测 frozen generator，置信不足时回退保守 schedule。"}
for aid,unit in DEEP.items(): L += ["",f"<!-- analysis:{unit}:start -->",f"### {unit}","",deeptext[aid],f"<!-- analysis:{unit}:end -->"]
for r in retained:
    if r["arxiv_id"] not in DEEP:L.append(f"<!-- analysis-decision:{r['source_family_id']}:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:{r['source_family_id']}:end -->")
L += ["","## 6. Books Comparison","","<!-- validator:books-comparison-v1 -->","| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |","| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in retained:
    c=comp[r["arxiv_id"]]; s=r["source_family_id"]; adj=";".join(cref(x) for x in c["adjacent_paths"]) or cref(c["owner_path"])
    rel="Direct Evolution" if r["integration_disposition"]=="Integrate" else ("Layering / Dependency" if r["integration_disposition"]=="Structural Candidate" else "Principle Reuse")
    books_node = "considered:MULTIMODAL-EMBODIED-VLA,AGENT-WORKFLOW" if r["integration_disposition"]=="Structural Candidate" else r["owner_node"]
    L.append(f"| {s} | {books_node} | {cref(c['owner_path'])} | {adj} | existing:{s} | delta:{s} | {rel} | {r['integration_disposition']} | books-review:{s} |")
for r in retained:
    c=comp[r["arxiv_id"]]; s=r["source_family_id"]
    L += [f"<!-- books-review:{s}:start -->",f"<!-- existing:{s}:start -->{c['existing_proposition']}<!-- existing:{s}:end -->",f"<!-- delta:{s}:start -->{c['new_evidence_delta']}<!-- delta:{s}:end --> Independent decision=`{c['decision']}`；owner_sha256={c['owner_sha256']}。",f"<!-- books-review:{s}:end -->"]
first=retained[0]["source_family_id"]
L += ["","## 7. Semantic Audit","","<!-- validator:semantic-audit-v1 -->","| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |","| --- | --- | --- | --- | --- | --- | --- |",f"| SA-20260524-COVERAGE | fresh-context:may2026-day03-non-author | coverage | coverage:SRC-ARXIV:20260524 | none | semantic-independent-audit.json#scope | passed |",f"| SA-20260524-EVIDENCE | fresh-context:may2026-day03-non-author | evidence | review:{first} | none | semantic-independent-audit.json#scope | passed |",f"| SA-20260524-SELECTION | fresh-context:may2026-day03-non-author | deep_analysis_selection | analysis:{next(iter(DEEP.values()))} | none | semantic-independent-audit.json#scope | passed |",f"| SA-20260524-BOOKS | fresh-context:may2026-day03-non-author | books | books-review:{first} | none | semantic-independent-audit.json#scope | passed |","","Cross-model skipped: non-interactive delegated context。","","## 8. Ignored Noise","","249 条 family-specific pre-denominator closure 保存在 `screening-ledger-final.json`；每条保留 title、abstract 机制、排除边界与重开条件。","","## 9. Recommended Action","",f"由 root 按日期序列写回最终 `BOOKS_WRITEBACK_QUEUE.json` 的 {len(queue)} 项；`2605.24728` 保留为 Structural Candidate，进入结构复核而非强塞现有章节。写回后必须由不同 reviewer 顺读 owner+adjacent。","","## 10. Repository Changes","",f"- 重建 05-24 independent ledger、40 项 exact-v1 receipt、current Books comparison、{len(queue)} 项 root writeback queue、semantic audit 与空 Materials Request。","- 未修改共享 Books；未 stage、commit 或 push。","","## 11. Open Questions","",f"- root 串行写回后，{len(queue)} 项是否全部位于 canonical H2 的演进主线，并通过不同 reviewer post-write audit？","- Hylos 的 operability contract 是否在季度结构审计中需要独立 owner，还是可由 Embodied 与 Agent Workflow 双向 handoff 承载？","","<!-- validator:materials-request-v1 -->","| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |","","## 12. Sources",""]
for r in retained:L.append(f"- [{r['title']}](https://arxiv.org/{'pdf' if r['arxiv_id'] in PDF else 'html'}/{r['arxiv_id']}v1) — arXiv:{r['arxiv_id']}v1；first-public 2026-05-23；accessed 2026-09-01")
L += ["","## 13. Final Status","","Completion Status: `In Progress`","","Coverage: `Closed`","","Evidence: `Passed`","","Books: `Open`","","unresolved findings: 1","",f"05-24 已达到 root-writeback-ready：289/289、40/40 exact-v1、ordinary pending=0、blocked=0、final Books queue={len(queue)}；剩余条件是 root 串行 Books 写回与不同 reviewer post-write semantic audit。"]
text="\n".join(L)
for r in retained:
    s=r["source_family_id"]; aid=r["arxiv_id"]
    body=text.split(f"<!-- review:{s}:start -->",1)[1].split(f"<!-- review:{s}:end -->",1)[0]
    candidate={"Event Identity":f"paper-v1:{aid}","Primary Identifier":f"arXiv:{aid}v1","Supporting Source IDs":"SRC-ARXIV","Review Override":"knowledge_gap" if r["integration_disposition"] in ("Integrate","Structural Candidate") else "none"}
    rp=_expected_review_provenance(s,candidate,"deep",f"arXiv:{aid}v1",f"SRC-ARXIV@arXiv:{aid}v1",ev(r,"method_locator"),ev(r,"evaluation_locator"),ev(r,"limitations_locator"),"Not Disclosed — no separate immutable artifact required for this review",f"claim:{s}",f"review:{s}",_normalized_body_sha256(body))
    text=text.replace("RP-TODO-"+s,rp)
(ROOT/"papers/2026/05/24/README.md").write_text(text+"\n")
print(json.dumps({"raw":SOURCE["raw_snapshot_records"],"registered":289,"screened":289,"author_denominator":23,"false_positive":2,"false_negative":19,"final_denominator":40,"closures":249,"exact_v1":40,"blocked":0,"ordinary_pending":0,"final_queue":len(queue),"structural_candidates":1},ensure_ascii=False))
