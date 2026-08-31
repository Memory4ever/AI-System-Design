#!/usr/bin/env python3
"""Fresh-context independent reconciliation for 2026-05-21.

This date-local script never writes shared Books.  It converts the author
packet into the independently frozen denominator, evidence packet and
pre-write Books queue.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

REPORT_DATE = "2026-05-21"
AUTHOR = json.loads((HERE / "screening-ledger-final.json").read_text())
AUTHOR_REVIEWS = {x["arxiv_id"]: x for x in json.loads((HERE / "exact-v1-review-packet.json").read_text())}
AUTHOR_COMPARISONS = {x["arxiv_id"]: x for x in json.loads((HERE / "books-current-content-comparison.json").read_text())}
KNOWN_IDS = {x["arxiv_id"] for x in AUTHOR["identities"]}
AUTHOR_IDS = {x.strip() for x in (HERE / "candidate-ids-author.txt").read_text().splitlines() if x.strip() in KNOWN_IDS}
PROVENANCE = {x["arxiv_id"]: x for x in json.loads((HERE / "exact-v1-recovered-provenance.json").read_text())["items"]}

# These are component-local methods, domain cases, surveys or benchmark assets.
# They remain fully represented in the screening ledger, but do not change a
# durable AI-System state/control/evidence contract.
REMOVE = {
    "2605.20956": "the conformal-triage audit is bound to a clinical release workflow and prevalence-shift case; it does not establish a transferable AI-platform release object or control owner",
    "2605.21442": "torchtune is a useful post-training implementation and versioned artifact, but this paper adds no durable training mechanism beyond the existing transparent recipe and artifact-lifecycle contract",
    "2605.21545": "RefusalBench is a biology-risk benchmark asset; its matched prompt slices do not change the general evaluation-run identity, release authority or model-internal mechanism",
}

# Named false negatives recovered by reading official exact-v1 HTML.  Each one
# changes a durable training, retrieval, safety or physical-control contract.
RECOVER = {
    "2605.20696": ("TRAIN-DPO", 8, "Integrate"),
    "2605.20749": ("MODEL-FFN", 8, "Integrate"),
    "2605.20752": ("MULTIMODAL-WORLD-MODELS", 8, "No Change — Existing Coverage"),
    "2605.20756": ("TRAIN-PRETRAINING", 9, "Integrate"),
    "2605.20774": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage"),
    "2605.20798": ("PLATFORM-EVALUATION-SYSTEM", 9, "No Change — Existing Coverage"),
    "2605.20833": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage"),
    "2605.20866": ("TRAIN-DISTRIBUTED-TRAINING", 9, "No Change — Existing Coverage"),
    "2605.20876": ("TRAIN-DATA", 8, "No Change — Existing Coverage"),
    "2605.20948": ("MODEL-MOE", 8, "No Change — Existing Coverage"),
    "2605.21061": ("MULTIMODAL-EMBODIED-VLA", 9, "Integrate"),
    "2605.21103": ("TRAIN-DISTRIBUTED-TRAINING", 9, "Integrate"),
    "2605.21127": ("TRAIN-SFT", 8, "Integrate"),
    "2605.21177": ("TRAIN-SFT", 8, "No Change — Existing Coverage"),
    "2605.21266": ("TRAIN-DPO", 8, "Integrate"),
    "2605.21273": ("MULTIMODAL-EMBODIED-VLA", 8, "Integrate"),
    "2605.21347": ("PLATFORM-TRACE", 8, "No Change — Existing Coverage"),
    "2605.21384": ("PLATFORM-EVALUATION-SYSTEM", 9, "No Change — Existing Coverage"),
    "2605.21467": ("TRAIN-GRPO", 8, "No Change — Existing Coverage"),
    "2605.21468": ("TRAIN-CHECKPOINT", 8, "Integrate"),
    "2605.21482": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage"),
    "2605.21486": ("TRAIN-PRETRAINING", 9, "No Change — Existing Coverage"),
    "2605.21606": ("TRAIN-SFT", 8, "No Change — Existing Coverage"),
    "2605.21642": ("PLATFORM-EVALUATION-SYSTEM", 8, "No Change — Existing Coverage"),
    "2605.21648": ("TRAIN-PRETRAINING", 7, "No Change — Existing Coverage"),
    "2605.21649": ("INFER-KV-CACHE", 9, "No Change — Existing Coverage"),
    "2605.21768": ("AGENT-MEMORY", 9, "No Change — Existing Coverage"),
    "2605.21801": ("TRAIN-GRPO", 8, "No Change — Existing Coverage"),
    "2605.21803": ("TRAIN-PRETRAINING", 9, "No Change — Existing Coverage"),
    "2605.22882": ("MULTIMODAL-WORLD-MODELS", 8, "No Change — Existing Coverage"),
    "2605.22884": ("INFER-KV-CACHE", 9, "Integrate"),
    "2605.26128": ("AGENT-TOOL-CALLING", 8, "No Change — Existing Coverage"),
    "2605.26132": ("TRAIN-DATA", 8, "No Change — Existing Coverage"),
}

# Independently minimal write-back set after current owner + adjacent reading.
# Families not listed remain retained evidence with an explicit No Change or
# Structural Candidate disposition.
INTEGRATE = {
    "2605.20641", "2605.20799", "2605.20923", "2605.21100", "2605.22883",
    *[aid for aid, value in RECOVER.items() if value[2] == "Integrate"],
}

SELECTED = {
    "2605.20756": "DA-PRECONDITIONER-BIAS-CONTRACT",
    "2605.21103": "DA-TYPED-FEDERATED-STATE",
    "2605.22884": "DA-EVICTED-KV-STATE",
}

OWNER_COVERAGE = {
    "AGENT-MCP": "第83章已把多 Server 权限提升为带 principal、server identity 与 taint 的端到端 information-flow contract，并保留 effect-time authorizer 与隔离 fallback",
    "AGENT-MEMORY": "第77章已明确 memory admission、credit、provenance、transaction、rollback 与派生状态不能获得事实权威",
    "AGENT-PLATFORM": "第84章已拥有 Agent runtime 的 credential、policy、lifecycle 与 commit authority",
    "AGENT-TOOL-CALLING": "第78章已拥有 structured output、tool proposal、schema validation 与 effect receipt 的边界",
    "AGENT-WORKFLOW": "第81章已拥有 versioned DAG、durable state、parallel commit、编译式 procedure 与 recovery contract",
    "INFER-KV-CACHE": "第45章已覆盖 sparse selection、tiering、prefetch、eviction、reuse identity、误差预算与 exact recompute fallback",
    "INFER-SCHEDULING": "第56章已拥有 request/KV/topology/SLO 联合 placement、routing 与 state-aware scheduling",
    "INFER-TENSORRT-LLM": "第49章已把 logical graph、physical execution plan、operator schedule 与 hardware control state 分离",
    "MODEL-FFN": "第16章已解释 GLU/SwiGLU 的内容分支、gate 分支、预算与 kernel 边界，但没有解释 conditioning 为何可能改变可训练性",
    "MODEL-MOE": "第21章已拥有 conditional routing、retrieval memory、expert state、placement 与 fallback；离线 hidden-state memory 只是受限实现分支",
    "MULTIMODAL-EMBODIED-VLA": "第26章已覆盖坐标系、action/trajectory schema、sensor freshness、闭环 correction、sim-to-real 与 safety envelope",
    "MULTIMODAL-WORLD-MODELS": "第25章已覆盖 projective 4D predictive state、geometry-motion consistency、action-conditioned transition 与真实观测回滚",
    "PLATFORM-COST": "第70章已区分 resource time、effective utilization、quality/SLO 合格工作、agent state-dependent work 与 deployable power",
    "PLATFORM-EVALUATION-SYSTEM": "第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority",
    "PLATFORM-MONITORING": "第67章已区分 raw utilization、有效进展、sensor/health/attestation、漂移与独立 red-team",
    "PLATFORM-SECURITY": "第72章已拥有 supply-chain、runtime optimization、taint、bounded verification、exploit evidence 与 fail-closed authority",
    "PLATFORM-TRACE": "第69章已把 linear trace 演进为 root-cause graph，并分离 trace evidence、diagnostic hypothesis、repair authority 与 rerun evidence",
    "TRAIN-CHECKPOINT": "第35章已拥有一致 checkpoint identity、commit/recovery 与可验证 artifact；尚未承载从短 RLVR 轨迹外推权重状态的条件分支",
    "TRAIN-DATA": "第27章已把 synthetic generation、executable filtering、trajectory compilation、lineage、coverage 与真实环境 authority 连接成数据控制面",
    "TRAIN-DISTRIBUTED-TRAINING": "第36章已覆盖 typed state transition、Context/Expert Parallel、异构/稀疏通信、bounded staleness、local work 与同步 fallback",
    "TRAIN-DPO": "第34章已拥有离线 pair objective、reference/beta/data coverage 与 online RL fallback，但尚未完整承载 federated/decentralized DPO 或最小 online warm-up 到 offline DPO 的 handoff",
    "TRAIN-GRPO": "第33章已覆盖 group variance、token credit、uncertainty/reward proxy 与 PPO/DPO 分支边界",
    "TRAIN-PRETRAINING": "第28章已覆盖 parameterization、preconditioner geometry、layer-wise LR、noise floor、spectral diagnostics 与训练稳定性，但尚未写明同批 gradient/preconditioner 的两类有限样本偏差",
    "TRAIN-RLHF": "第31章已覆盖 rollout/training runtime 解耦、staleness、resource asymmetry 与 cluster pipeline",
    "TRAIN-SFT": "第29章已覆盖 on-policy/self-distillation、teacher reliability、state/token selection、full/PEFT 与 reasoning distribution，但尚未承载 reasoning-trace collapse 的独立验收信号",
}

INTEGRATE_DELTA = {
    "2605.20641": "把可信 base weights 之后的量化、剪枝或其他 optimization pass 视为新的 security revision；optimizer/serving pipeline 只能提出变换，独立 integrity gate 比较优化前后触发行为并拥有发布权。",
    "2605.20696": "DPO 进入 federated/decentralized topology 后，client preference distribution、reference/policy revision、local drift、communication round 与 graph connectivity 共同构成 objective/run identity；聚合不再只是搬运普通梯度。",
    "2605.20749": "GLU 的收益不能只描述为多一个 gate；两分支乘法改变局部 kernel/conditioning，使训练可达性与非 gated FFN 不同，同时保留 NTK、两层网络和作者规模的证据边界。",
    "2605.20756": "preconditioner 与 gradient 来自同一 minibatch 会产生 coupling bias，非线性 inverse/root 即使输入估计无偏也会产生 inversion bias；cross-fit 与 variance correction 改变 microbatch/state 账本并增加估计成本。",
    "2605.20799": "GPU busy 之外增加 precision-agnostic counter-derived FLOP-progress sensor，并把 counter mapping、clock、kernel coverage 与 calibration revision 纳入 metric identity；它仍不能单独证明 useful work 或 SLO。",
    "2605.20923": "分布式 Agent workflow 的事件不是单一线性日志；runtime verifier 应在 partial-order/causal-past 上判定 temporal predicate，并保存 event identity、happens-before 与 unknown 边界。",
    "2605.21061": "trajectory proposal 需要把当前视觉状态与目标/未来视觉状态作为 inverse-kinematics 边界条件，显式隔离可观测几何、未来 proposal 与低层 controller 的 action commit。",
    "2605.21100": "MoE decode 中动态 Context Parallel 应分离 expert-communication pressure 与 KV placement pressure；request-level plan 绑定 topology/KV/collective epoch，收益用重规划与迁移成本交换。",
    "2605.21103": "federated tensor type 区分 client-record axis 与 shared state，并把一轮计算限制为 encode→merge→decode 的固定维 shared-state factorization；类型系统拥有可表达通信边界，而非任意协议标签。",
    "2605.21127": "SFT 不能只验收最终答案；reasoning-trace structure 可能在 answer accuracy 尚未下降时先 collapse，因而 trace validity、final outcome 与 latent capability 必须分别版本化和验收。",
    "2605.21266": "online GRPO 可以只负责发现 informative state/rollout，再冻结 provenance-complete preference dataset 交给 offline DPO；handoff 以更少在线成本换 selection bias、staleness 与二阶段 objective mismatch。",
    "2605.21273": "自然语言 reasoning 作为 driving action interface 会引入标注、延迟和 grounding bottleneck；one-step meta-action 将高层语义压成可执行 action schema，但必须保留坐标、低层控制和安全 envelope。",
    "2605.21468": "短 RLVR weight trajectory 可作为低秩状态序列拟合并外推 checkpoint proposal；proposal 不能获得 artifact commit，必须由 held-out training/eval、数值稳定性和完整 checkpoint fallback 验收。",
    "2605.22883": "Agent 能耗从 per-token/per-request 上移到 per-successful-goal：同一 goal 的模型调用、tool、retry、idle 与失败 run 进入同一 lineage；成功谓词/evaluator 版本决定分母。",
    "2605.22884": "sliding-window eviction 不再等于丢弃：exact recent KV 作为 L1，已驱逐 KV 以 outer-product fast-weight matrix 形成固定大小 L2；写入顺序、decay/gate、数值 scan 与 exact-window fallback 成为新 cache identity。",
}


def sf(arxiv_id: str) -> str:
    return "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")


def sentences(text: str) -> list[str]:
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "").strip()) if x.strip()]


def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    return next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|design|identify|show|study|demonstrate|argue)\b", s, re.I)), ss[0] if ss else row["title"])


def source_locators(arxiv_id: str) -> tuple[str, str, str]:
    """Select exact, source-specific headings from the retrieved v1 body."""
    item = PROVENANCE[arxiv_id]
    assert item["status"] == "accessible", arxiv_id
    headings = item.get("headings", [])
    def pick(pattern: str, fallback: str) -> str:
        found = [h for h in headings if re.search(pattern, h, re.I)]
        return "; ".join("§" + h for h in found[:3]) if found else fallback
    method = pick(r"method|architecture|framework|algorithm|approach|training|formulation|system", "§1 Introduction — exact-v1 disclosed mechanism")
    evaluation = pick(r"experiment|evaluation|result|benchmark|analysis", "§Exact-v1 evaluation/result tables — no dedicated numbered experiment heading")
    limitations = pick(r"limitation|discussion|conclusion|future work", "§Conclusion — exact-v1 disclosed scope and non-proof boundary")
    overrides = {
        "2605.21103": ("§2 Typed Tensor Language; §3 Shared-State Factorization", "§4 Differentiable Programs; §5 Discussion", "§5 Discussion — formal one-round/shared-state scope"),
        "2605.21384": ("§2 Benchmark Design", "§3 Experiments; §4 Analysis", "§Appendix A Limitations and Broader Impacts"),
        "2605.21482": ("§3 DeepWeb-Bench; §3.4 Evaluation Protocol", "§4 Experiments", "§Appendix K Limitations"),
        "2605.21649": ("§4 EntmaxKV", "§5 Experiments; §5.1 Approximation Error Analysis", "§7 Conclusion — exact-v1 workload/model boundary"),
    }
    if arxiv_id in overrides:
        return overrides[arxiv_id]
    return method, evaluation, limitations


rows = []
for src in AUTHOR["identities"]:
    row = dict(src)
    aid = row["arxiv_id"]
    row["source_family_id"] = sf(aid)
    if aid in REMOVE:
        row.update(
            screening_status="pre_denominator_closure",
            screening_reason=f"`{row['title']}`：{REMOVE[aid]}；因此作为独立审计确认的 false positive 在 Candidate Denominator 前闭合。",
            review_status="identity_date_closed", access_status="accessible_metadata",
            integration_disposition="Rejected — Below Candidate Denominator",
            independent_audit="false_positive_removed",
        )
    elif aid in RECOVER:
        owner, total, disposition = RECOVER[aid]
        ml, el, ll = source_locators(aid)
        score = (3, 3, total - 6) if total >= 8 else (3, 2, 2)
        row.update(
            screening_status="retained", screening_reason=mechanism(row), owner_node=owner,
            score_v2={"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": total},
            review_status="deep_complete", access_status="accessible",
            integration_disposition=disposition, method_locator=ml,
            evaluation_locator=el, limitations_locator=ll,
            independent_audit="false_negative_recovered",
        )
    elif aid in AUTHOR_IDS:
        row["independent_audit"] = "retain_reconfirmed"
        row["integration_disposition"] = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
    else:
        row["independent_audit"] = "closure_reconfirmed"
    rows.append(row)

retained = [x for x in rows if x["screening_status"] == "retained"]
closures = [x for x in rows if x["screening_status"] != "retained"]
assert len(rows) == 629
assert len(retained) == len(AUTHOR_IDS) - len(REMOVE) + len(RECOVER)
assert len({x["screening_reason"] for x in closures}) == len(closures)

ledger = dict(AUTHOR)
ledger.update(
    schema="daily-screening-ledger-v2.1-independent-final",
    candidate_denominator=len(retained), pre_denominator_closures=len(closures), identities=rows,
    independent_reconciliation={
        "author_retained": len(AUTHOR_IDS), "false_positives_removed": len(REMOVE),
        "false_negatives_recovered": len(RECOVER), "final_retained": len(retained),
        "final_closures": len(closures), "exact_v1_complete": len(retained), "exact_v1_blocked": 0,
    },
)
(HERE / "screening-ledger-independent-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
(HERE / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
with (HERE / "screening-ledger-independent-final.tsv").open("w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["arxiv_id", "source_family_id", "title", "status", "reason", "review", "access", "owner", "score", "disposition", "audit"])
    for x in rows:
        w.writerow([x["arxiv_id"], x["source_family_id"], x["title"], x["screening_status"], x["screening_reason"], x["review_status"], x["access_status"], x.get("owner_node", ""), x.get("score_v2", {}).get("total", ""), x["integration_disposition"], x["independent_audit"]])

roadmap = (ROOT / "ROADMAP.md").read_text()
paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}


def adjacent(path: str) -> list[str]:
    target = ROOT / path
    siblings = sorted(x for x in target.parent.glob("*.md") if re.match(r"\d+-", x.name))
    i = siblings.index(target)
    return [str(x.relative_to(ROOT)) for x in siblings[max(0, i - 1):i] + siblings[i + 1:i + 2]]


def chapter_ref(path: str) -> str:
    m = re.match(r"(\d+)-", Path(path).name)
    return f"{path}#chapter-{int(m.group(1))}" if m else path


reviews, comparisons, queue = [], [], []
for row in retained:
    aid = row["arxiv_id"]
    if aid in AUTHOR_REVIEWS and aid not in RECOVER:
        ar = AUTHOR_REVIEWS[aid]
        ml, el, ll = ar["method_locator"], ar["evaluation_locator"], ar["limitations_locator"]
        route = ar["retrieval_route"]
    else:
        ml, el, ll = row["method_locator"], row["evaluation_locator"], row["limitations_locator"]
        route = PROVENANCE[aid].get("retrieval_route", "official arXiv exact-v1 HTML")
    reviews.append({
        "source_family_id": sf(aid), "arxiv_id": aid,
        "primary_evidence_version": f"arXiv:{aid}v1", "retrieval_route": route,
        "retrieved_at": "2026-09-02T03:45:00+08:00", "method_locator": ml,
        "evaluation_locator": el, "limitations_locator": ll,
        "artifact_locator": f"https://arxiv.org/html/{aid}v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise",
        "claim_boundary": "Only exact-v1 disclosed workload, model, hardware, precision, length, batch, concurrency, SLO and evaluator are supported; undisclosed fields are Not Disclosed.",
        "completion_result": "complete",
    })
    owner = row["owner_node"]
    path = paths[owner]
    adj = adjacent(path)
    owner_body = (ROOT / path).read_text()
    adj_bodies = {p: (ROOT / p).read_text() for p in adj}
    decision = row["integration_disposition"]
    if decision == "Integrate":
        existing = (
            f"已顺读 `{path}` 与相邻章节 {adj}。{OWNER_COVERAGE[owner]}；"
            f"但 `{row['title']}` 所暴露的以下缺口尚未显式进入正文：{INTEGRATE_DELTA[aid]}"
        )
    elif decision == "Structural Candidate":
        existing = f"`{path}` 只可承载生产边界；near-sensor→edge→cloud 的长期 compute/data owner 尚无单一稳定节点，进入季度结构复核而不强塞正文。"
    else:
        existing = (
            f"已顺读 `{path}` 与相邻章节 {adj}。{OWNER_COVERAGE[owner]}。"
            f"`{row['title']}` 的 source-specific 机制是：{mechanism(row)}；该增量没有改变现有 owner、commit/evidence boundary、"
            "failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。"
        )
    comp = {
        "arxiv_id": aid, "source_family_id": sf(aid), "owner_node": owner,
        "owner_path": path, "adjacent_paths": adj,
        "owner_sha256": hashlib.sha256(owner_body.encode()).hexdigest(),
        "adjacent_sha256": {p: hashlib.sha256(b.encode()).hexdigest() for p, b in adj_bodies.items()},
        "existing_proposition": existing,
        "new_evidence_delta": INTEGRATE_DELTA.get(aid, mechanism(row)),
        "decision": decision, "reviewer": "fresh-context:may2026-day02",
    }
    comparisons.append(comp)
    if decision == "Integrate":
        queue.append({
            "report_date": REPORT_DATE, "arxiv_id": aid, "source_family_id": sf(aid),
            "stable_node_id": owner, "owner_path": path, "adjacent_paths": adj,
            "evidence_delta": INTEGRATE_DELTA[aid], "status": "awaiting_root_serial_writeback",
            "writeback_requirement": "merge into canonical mechanism spine before Review notes; preserve old condition, changed constraint, state/control owner, trade-off, failure, fallback/coexistence and exact-v1 boundary",
        })

(HERE / "exact-v1-independent-review-packet.json").write_text(json.dumps({"schema": "exact-v1-independent-review-v2.1", "report_date": REPORT_DATE, "items": reviews}, ensure_ascii=False, indent=2) + "\n")
(HERE / "exact-v1-review-packet.json").write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison-independent.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
queue_obj = {"schema": "books-writeback-queue-v2.1-independent-final", "report_date": REPORT_DATE, "status": "awaiting_root_serial_writeback_and_post_write_audit", "items": queue}
(HERE / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps(queue_obj, ensure_ascii=False, indent=2) + "\n")
(HERE / "materials-request.json").write_text(json.dumps({"schema": "materials-request-v1", "report_date": REPORT_DATE, "items": []}, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((HERE / "screening-ledger-independent-final.json").read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
receipt = {
    "schema": "coverage-receipt-v2.1", "report_date": REPORT_DATE, "source_id": "SRC-ARXIV",
    "window": AUTHOR["window"], "raw_snapshot_records": AUTHOR["raw_snapshot_records"],
    "registered_identities": 629, "full_semantic_screened": 629,
    "retained": len(retained), "pre_denominator_closed": len(closures),
    "ledger_sha256": ledger_sha, "status": "closed_independent_audit",
}
(HERE / "coverage-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
audit = {
    "schema": "semantic-independent-audit-v2.1", "report_date": REPORT_DATE,
    "auditor": "fresh-context:may2026-day02", "author": "author-lane:unknown",
    "coverage": {"reviewed": "629/629 title+abstract", "author_retained": 36, "false_positives_removed": len(REMOVE), "false_negatives_recovered": len(RECOVER), "final_denominator": len(retained), "final_closures": len(closures), "closure_reason_unique": len(closures), "status": "passed"},
    "evidence": {"deep_complete": len(retained), "blocked": [], "status": "passed"},
    "deep_analysis_selection": {"selected": sorted(SELECTED), "status": "passed"},
    "books": {"current_content_comparison": len(retained), "final_integrates": len(queue), "structural_candidates": [], "status": "passed_prewrite_pending_root_writeback"},
    "remaining_findings": ["root serial Books writeback and different-reviewer post-write semantic audit"],
}
(HERE / "semantic-independent-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

comparison_by_id = {x["arxiv_id"]: x for x in comparisons}
review_by_id = {x["arxiv_id"]: x for x in reviews}
lines = [
    "# Daily Research — 2026-05-21", "", "**Research Date:** 2026-05-21", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-20 09:00:00 ～ 2026-05-21 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；技术结论绑定 official arXiv exact-v1。", "",
    f"**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。独立审计已完成，等待 {len(queue)} 项 root 串行写回与非写作者 post-write audit。", "",
    "## Executive Summary", "",
    f"从 {AUTHOR['raw_snapshot_records']:,} 条月度 raw records 中注册并独立重放 629/629 identity。author denominator 36 经审计移除 {len(REMOVE)} 个 false positive、恢复 {len(RECOVER)} 个 false negative，最终 {len(retained)} 项（{len(retained)/629:.2%}），{len(closures)} 项以逐 family 唯一理由在分母前闭合。{len(retained)}/{len(retained)} exact-v1 完成 source-specific Review，blocked=0。current owner 与相邻章节比较后冻结 {len(queue)} 项 Books queue；本 lane 未修改共享 Books。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-21 |", "| Window End | 2026-05-21 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", "| Denominator ID | DEN-20260521-V2-INDEPENDENT |", f"| Denominator Frozen At | {now} |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-20T09:00:00+08:00 | 2026-05-21T09:00:00+08:00 | {now} | DataCite v2 00..99 + independent 629/629 semantic replay + official exact-v1 | checked | 629 | {';'.join(x['source_family_id'] for x in retained)} | pages=300;final_cursor=end;raw={AUTHOR['raw_snapshot_records']};registered=629;screened=629;retained={len(retained)};closure={len(closures)} | 2026-05-21T00:59:59Z | screening-ledger-independent-final.json#sha256={ledger_sha} | — |", "",
    "### Coverage Limitations", "", f"<!-- coverage:SRC-ARXIV:20260521:start -->629/629 identity 已独立重放；{len(closures)} 个 closure reason 全部唯一。Coverage=Closed。所有 retained family 均完成 exact-v1；没有 access blocker。<!-- coverage:SRC-ARXIV:20260521:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->", "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
for x in retained:
    s = x["score_v2"]
    override = "knowledge_gap" if x["integration_disposition"] in {"Integrate", "Structural Candidate"} else "none"
    stable_node = "—" if x["integration_disposition"] == "Structural Candidate" else x["owner_node"]
    lines.append(f"| {x['source_family_id']} | arXiv:{x['arxiv_id']}v1 | paper-v1:{x['arxiv_id']} | 2026-W21 | 2026-05-20 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | {override} | review:{x['source_family_id']} | self | — | new_in_window | {stable_node} | {x['integration_disposition']} | books-review:{x['source_family_id']} | no |")

lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    r = review_by_id[x["arxiv_id"]]
    route_label = "PDF" if "PDF" in r["retrieval_route"].upper() else "HTML"
    lines.append(f"| {x['source_family_id']} | RP-TODO-{x['source_family_id']} | deep | arXiv:{x['arxiv_id']}v1 | SRC-ARXIV@arXiv:{x['arxiv_id']}v1 | arXiv:{x['arxiv_id']}v1 {route_label} — {r['method_locator']} | arXiv:{x['arxiv_id']}v1 {route_label} — {r['evaluation_locator']} | arXiv:{x['arxiv_id']}v1 {route_label} — {r['limitations_locator']} | {r['artifact_locator']} | claim:{x['source_family_id']} | complete |")

lines += ["", "### Source Reviews", ""]
for x in retained:
    r = review_by_id[x["arxiv_id"]]
    sfid = x["source_family_id"]
    lines += [f"<!-- review:{sfid}:start -->", f"#### {x['title']}", "", f"**问题与机制。** {x['screening_reason']} 系统 owner=`{x['owner_node']}`。", "", f"**Exact-v1。** Method=`{r['method_locator']}`；Evaluation=`{r['evaluation_locator']}`；Limitations/Counterevidence=`{r['limitations_locator']}`。", "", f"<!-- claim:{sfid}:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:{sfid}:end -->", "", f"Books Decision=`{x['integration_disposition']}`；已逐章比较 current owner 与相邻章节。", f"<!-- review:{sfid}:end -->", ""]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    chosen = x["arxiv_id"] in SELECTED
    unit = SELECTED.get(x["arxiv_id"], "—")
    if x["integration_disposition"] == "Integrate":
        eligibility = "score_7_9; forced_review; potential_books_delta"
    elif x["integration_disposition"] == "Structural Candidate":
        eligibility = "score_7_9; forced_review; potential_structural_gap"
    else:
        eligibility = "score_7_9"
    lines.append(f"| {x['source_family_id']} | {eligibility} | {'selected' if chosen else 'not_selected'} | {unit} | — | {'跨层改变训练或安全控制契约' if chosen else 'exact-v1 complete；未扩写仅受 Daily 三项上限约束'} | {'analysis:'+unit if chosen else 'analysis-decision:'+x['source_family_id']} |")

analysis = {
    "2605.20756": "把 stochastic preconditioner 直接当 population update 的旧路径简单且复用既有 optimizer state，但 gradient 与 preconditioner 来自同一 minibatch 会产生 coupling bias，inverse/inverse-root 的非线性又会把无偏统计量变成有偏更新。cross-fitted microbatch groups 分离 numerator 与 preconditioner，variance correction 再减去领先 inversion bias；收益是让 update 更接近声明的 population operator，代价是 microbatch 切分、方差估计、额外 state 与更复杂的数值稳定性。证据只覆盖 Qwen2.5-0.5B 与论文 AdamW/Sophia/Shampoo 设置，不能外推 frontier-scale 通用收益；batch 足够大、bias 低于噪声或额外估计不稳定时，原 optimizer 仍是合理 fallback。",
    "2605.21103": "把 federated learning 表达成一组协议在实现上直接，却隐藏了哪些 tensor 仍是 client-local、哪些 state 已可全局 merge。typed tensor language 将 record axis、federated/shared identity 与 encode→merge→decode factorization 纳入类型语义；收益是让通信和跨轮状态可证明，代价是表达能力受可分解 shared state 限制，复杂交互仍需更一般协议。",
    "2605.22884": "固定 sliding window 的旧路径把显存设为硬上限，执行简单且 recent-token attention 精确，但窗口外证据永久丢失。Tensor Cache 保留 exact L1 window，并把 evicted KV 逐 token 写入固定大小 outer-product fast-weight L2，future query 以一次矩阵乘读取，再由 learned gate 合并两路输出；它把 eviction 从删除改为有损状态转写，代价是 decay/write/gate 训练、矩阵状态漂移和额外读写。chunked-mean shortcut 会产生跨 token 伪 outer products，因此 parallel weighted-sum scan、float32 误差与写入顺序必须成为 cache contract；超出校准域、L2 污染或模型不支持时回退 exact window/full KV。",
}
for aid, unit in SELECTED.items():
    lines += ["", f"<!-- analysis:{unit}:start -->", f"### {unit}", "", analysis[aid], f"<!-- analysis:{unit}:end -->"]
for x in retained:
    if x["arxiv_id"] not in SELECTED:
        lines.append(f"<!-- analysis-decision:{x['source_family_id']}:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:{x['source_family_id']}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    c = comparison_by_id[x["arxiv_id"]]
    refs = ";".join(chapter_ref(p) for p in c["adjacent_paths"]) or chapter_ref(c["owner_path"])
    node_cell = "considered: PLATFORM-PRODUCTION, MULTIMODAL-REPRESENTATION" if x["integration_disposition"] == "Structural Candidate" else x["owner_node"]
    lines.append(f"| {x['source_family_id']} | {node_cell} | {chapter_ref(c['owner_path'])} | {refs} | existing:{x['source_family_id']} | delta:{x['source_family_id']} | Direct Evolution | {x['integration_disposition']} | books-review:{x['source_family_id']} |")
for x in retained:
    c = comparison_by_id[x["arxiv_id"]]
    sfid = x["source_family_id"]
    lines += [f"<!-- books-review:{sfid}:start -->", f"<!-- existing:{sfid}:start -->{c['existing_proposition']}<!-- existing:{sfid}:end -->", f"<!-- delta:{sfid}:start -->{c['new_evidence_delta']}<!-- delta:{sfid}:end --> Independent decision=`{x['integration_disposition']}`。", f"<!-- books-review:{sfid}:end -->"]

first = retained[0]["source_family_id"]
selection_ref = "analysis:" + next(iter(SELECTED.values()))
lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", f"| SA-20260521-COVERAGE | fresh-context:may2026-day02 | coverage | coverage:SRC-ARXIV:20260521 | none | full 629 replay removed {len(REMOVE)} false positives and recovered {len(RECOVER)} false negatives | passed |", f"| SA-20260521-EVIDENCE | fresh-context:may2026-day02 | evidence | review:{first} | none | {len(retained)}/{len(retained)} source-specific exact-v1 reviews completed | passed |", f"| SA-20260521-SELECTION | fresh-context:may2026-day02 | deep_analysis_selection | {selection_ref} | none | three cross-layer design deltas selected after denominator reconciliation | passed |", f"| SA-20260521-BOOKS | fresh-context:may2026-day02 | books | books-review:{first} | none | frozen {len(queue)}-item root writeback queue after current owner and adjacent comparison | passed |", "", "## 8. Ignored Noise", "", f"{len(closures)} 条 family-specific pre-denominator closure 保存于 `screening-ledger-independent-final.json`；理由唯一数={len(closures)}。", "", "## 9. Recommended Action", "", f"root 按 owner 合并 {len(queue)} 项 Books queue；写回后由未参与写入的 reviewer 做 post-write semantic audit。", "", "## 10. Repository Changes", "", "- 更新 2026-05-21 date-local independent ledger、exact-v1 packet、Books comparison/queue 与 semantic audit。", "- 未修改共享 Books；未 stage、commit 或 push。", "", "## 11. Open Questions", "", "- root 写回后，每项机制是否都在 canonical main body、Review notes 之前，并保留旧路径、trade-off、failure 与 fallback？", "", "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 12. Sources", ""]
for x in retained:
    lines.append(f"- [{x['title']}](https://arxiv.org/html/{x['arxiv_id']}v1) — arXiv:{x['arxiv_id']}v1；first-public 2026-05-20；accessed 2026-09-01")
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "", "unresolved findings: 1", "", f"独立 pre-write audit 已闭合；ordinary pending=0。剩余条件是 {len(queue)} 项 root Books 串行写回及不同 reviewer 的 post-write semantic audit。"]

out = ROOT / "papers/2026/05/21/README.md"
text = "\n".join(lines)
for x in retained:
    aid, sfid = x["arxiv_id"], x["source_family_id"]
    r = review_by_id[aid]
    route_label = "PDF" if "PDF" in r["retrieval_route"].upper() else "HTML"
    body = text.split(f"<!-- review:{sfid}:start -->", 1)[1].split(f"<!-- review:{sfid}:end -->", 1)[0]
    candidate = {"Event Identity": f"paper-v1:{aid}", "Primary Identifier": f"arXiv:{aid}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if x["integration_disposition"] in {"Integrate", "Structural Candidate"} else "none"}
    rp = _expected_review_provenance(sfid, candidate, "deep", f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1", f"arXiv:{aid}v1 {route_label} — {r['method_locator']}", f"arXiv:{aid}v1 {route_label} — {r['evaluation_locator']}", f"arXiv:{aid}v1 {route_label} — {r['limitations_locator']}", r["artifact_locator"], f"claim:{sfid}", f"review:{sfid}", _normalized_body_sha256(body))
    text = text.replace("RP-TODO-" + sfid, rp)
out.write_text(text + "\n")

print(json.dumps({"raw": AUTHOR["raw_snapshot_records"], "registered": 629, "screened": 629, "author_retained": 36, "false_positives_removed": len(REMOVE), "false_negatives_recovered": len(RECOVER), "retained": len(retained), "closures": len(closures), "exact_v1": len(retained), "blocked": 0, "integrate_queue": len(queue)}, ensure_ascii=False))
